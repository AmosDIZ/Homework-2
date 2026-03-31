# Homework 2 Report

## Business Use Case

This project focuses on summarizing meetings into action items. In many teams, meetings produce useful discussion, decisions, and next steps, but the final outcomes are often scattered across rough notes or incomplete transcripts. This makes follow-up harder and can reduce accountability.

The intended user for this workflow is a team member, project manager, or meeting organizer who needs a quick and structured summary after a meeting. The system takes meeting notes or short transcript-style text as input and produces three sections as output: Action Items, Decisions, and Open Questions / Follow-Ups.

This task is valuable enough to automate partially because it is repetitive, writing-heavy, and time-sensitive. A draft summary can save time and improve consistency. At the same time, it is also a task where accuracy matters, especially when ownership, deadlines, or final decisions are unclear. Because of that, this is a good example of a workflow where AI can assist but should not fully replace human review. :contentReference[oaicite:1]{index=1}

## Model Choice

I chose OpenAI's `gpt-4o-mini` model for this prototype. My main reasons were ease of use, low cost compared with larger models, and simple integration with Python through the OpenAI SDK. Since this assignment is focused on building a small reproducible prototype rather than a production system, `gpt-4o-mini` was a practical choice.

I did not run a broad formal comparison across multiple providers for this assignment. Instead, I focused on getting one model working reliably and then improving the results through prompt iteration. That approach matched the purpose of the assignment, which emphasizes real LLM calls, a stable evaluation set, and honest iteration rather than building a complex system. 

## Baseline vs. Final Design

My baseline design used a short and simple instruction asking the model to summarize meeting notes into action items, decisions, and follow-up items. This version was easy to write, but it left too much freedom to the model. As a result, the formatting could vary, and there was a higher risk that the model would treat uncertain discussion points as confirmed actions or decisions.

The final design used a much stricter prompt structure. It required the model to return exactly three sections: Action Items, Decisions, and Open Questions / Follow-Ups. It also included explicit rules such as: only use information stated in the notes, do not invent owners or deadlines, write "Not specified" when information is missing, and move tentative or unresolved items into the follow-up section. In the strict version, I also added a rule to write "- None" if a section had no valid content.

This prompt iteration improved the workflow in several ways. First, the output became easier to read because the format stayed more consistent across examples. Second, the stricter rules reduced hallucination risk by discouraging the model from filling in missing details. Third, the final version handled ambiguous notes better because it separated confirmed decisions from unresolved questions. Overall, the final prompt was more reliable for evaluation because it produced output that was easier to compare across test cases. 

## Where the Prototype Still Fails or Needs Human Review

This prototype still has important limitations. The model can only work with what appears in the meeting notes, so if the notes are incomplete, vague, or messy, the output will also be limited. For example, if a task is mentioned but no owner is assigned, the model can mark the owner as "Not specified," but it cannot resolve the missing information. Similarly, when notes contain tentative language such as "maybe," "probably," or "we should consider," the system may still require human judgment to decide whether something should be treated as an action item or just a discussion point.

Human review is especially important in high-stakes or ambiguous cases. If a meeting discusses budget changes, hiring decisions, launch delays, or legal concerns, an incorrect summary could create confusion or misrepresent the team's actual decision. For that reason, I would not trust this prototype as a fully autonomous meeting documentation system. It works better as a drafting assistant that gives a first pass for someone to review and correct.

## Deployment Recommendation

I would recommend deploying this workflow only with clear human-review boundaries. It is useful as a support tool for turning rough notes into a structured first draft, especially for routine internal meetings. In that setting, the system can save time, improve consistency, and make it easier for teams to track follow-up items.

However, I would not recommend deploying it as a fully automated system that sends summaries directly to stakeholders without review. The risk of ambiguity, missing ownership, or overconfident interpretation is still too high. A practical deployment condition would be: the model generates a draft summary, and a human meeting owner reviews it before sharing it. Under those conditions, this workflow could be helpful and realistic. Without that review step, the system would need tighter controls and more testing before deployment.