import argparse
import os
from pathlib import Path

from openai import OpenAI


DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_OUTPUT_FILE = "meeting_summary_output.txt"
SAMPLE_MEETING_NOTE = """Project sync meeting notes

- Sarah said the team should update the onboarding guide before the next release.
- No owner was assigned for the onboarding guide update.
- The mobile bug affecting login was discussed. James will investigate the bug.
- The team wants a status update on the login bug by Friday.
- The group agreed to delay the analytics dashboard launch until after user testing.
- It was suggested that the team might add a customer FAQ page, but no final decision was made.
- The budget for contractor support is still being reviewed.
"""


PROMPTS = {
    "baseline": """You summarize meeting notes into structured sections.

Return exactly these sections:
1. Action Items
2. Decisions
3. Open Questions / Follow-Ups

Rules:
- Only use information explicitly stated in the notes.
- Do not invent owners, deadlines, or decisions.
- If owner is missing, write "Not specified".
- If deadline is missing, write "Not specified".
- If something is tentative, unclear, or undecided, place it under Open Questions / Follow-Ups.
- Keep the output concise and easy to read.

For Action Items, use this format:
- Task: ...
  Owner: ...
  Deadline: ...

For Decisions, use this format:
- Decision: ...

For Open Questions / Follow-Ups, use this format:
- Item: ...
""",
    "strict": """You are a careful meeting-notes extraction assistant.

Return exactly these sections and no others:
1. Action Items
2. Decisions
3. Open Questions / Follow-Ups

Follow these rules strictly:
- Use only facts explicitly written in the notes.
- Do not infer missing details.
- Do not invent owners, deadlines, decisions, or next steps.
- If an action item has no owner, write "Not specified".
- If an action item has no deadline, write "Not specified".
- If a point is tentative, pending review, or not finalized, place it under Open Questions / Follow-Ups.
- If there are no items for a section, write "- None".

For Action Items, use this exact format:
- Task: ...
  Owner: ...
  Deadline: ...

For Decisions, use this exact format:
- Decision: ...

For Open Questions / Follow-Ups, use this exact format:
- Item: ...
""",
}


def parse_args():
    """Read command-line arguments for the homework script."""
    parser = argparse.ArgumentParser(
        description="Summarize meeting notes into action items, decisions, and follow-ups."
    )
    parser.add_argument(
        "--input_file",
        help="Optional path to a text file containing meeting notes.",
    )
    parser.add_argument(
        "--output_file",
        default=DEFAULT_OUTPUT_FILE,
        help=f"Path to save the final output. Default: {DEFAULT_OUTPUT_FILE}",
    )
    parser.add_argument(
        "--prompt_version",
        choices=sorted(PROMPTS.keys()),
        default="baseline",
        help="Prompt version to use.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model name to use. Default: {DEFAULT_MODEL}",
    )
    return parser.parse_args()


def load_notes(input_file):
    """Load meeting notes from a file, or fall back to the built-in sample."""
    if not input_file:
        return SAMPLE_MEETING_NOTE.strip()

    return Path(input_file).read_text(encoding="utf-8").strip()


def build_user_prompt(notes):
    """Create the user message sent to the model."""
    return f"""Meeting notes:
{notes}

Please convert these notes into:
- Action Items
- Decisions
- Open Questions / Follow-Ups
"""


def format_result(model, prompt_version, notes, generated_output):
    """Prepare a clear text report for printing and saving."""
    return f"""MODEL
{model}

PROMPT VERSION
{prompt_version}

INPUT NOTES
{notes}

GENERATED OUTPUT
{generated_output}
"""


def main():
    args = parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError(
            "OPENAI_API_KEY is not set. Please export your API key before running the script."
        )

    notes = load_notes(args.input_file)
    system_prompt = PROMPTS[args.prompt_version]

    client = OpenAI()

    response = client.responses.create(
        model=args.model,
        instructions=system_prompt,
        input=build_user_prompt(notes),
    )

    generated_output = response.output_text.strip()
    final_report = format_result(
        model=args.model,
        prompt_version=args.prompt_version,
        notes=notes,
        generated_output=generated_output,
    )

    output_path = Path(args.output_file)
    output_path.write_text(final_report, encoding="utf-8")

    print(final_report)
    print(f"Saved output to: {output_path}")


if __name__ == "__main__":
    main()
