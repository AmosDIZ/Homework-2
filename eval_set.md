# Evaluation Set

## Case 1 - Normal Case
**Input:**
Project sync meeting notes:
- Sarah will update the onboarding slides by Friday.
- Kevin will send the revised budget to the team by Wednesday.
- The team agreed to launch the pilot on April 15.
- Next check-in meeting will be on Monday morning.

**What a good output should do:**
The output should clearly identify the main action items, assign Sarah and Kevin correctly, include the stated deadlines, and mention the agreed pilot launch date.

---

## Case 2 - Normal Case with Multiple Owners
**Input:**
Marketing meeting notes:
- Emily will draft the email campaign.
- Jason will review the draft before it goes out.
- Priya will prepare the customer segment list by Thursday.
- The campaign should be sent next Tuesday.

**What a good output should do:**
The output should separate each task clearly, match each task with the correct owner, and preserve the timeline in a structured way.

---

## Case 3 - Edge Case: Missing Owners
**Input:**
Team discussion notes:
- Finalize the presentation deck by Friday.
- Send follow-up notes to stakeholders.
- Confirm who will present the demo.
- The client meeting is next Wednesday.

**What a good output should do:**
The output should capture the action items without inventing owners. It should mark missing ownership clearly and keep the known deadline and meeting date.

---

## Case 4 - Edge Case: Messy and Informal Notes
**Input:**
Random meeting notes:
- website slow on mobile
- maybe Daniel check images?
- checkout bug still there
- fix before launch
- ask Anna about updated product copy
- launch maybe end of month

**What a good output should do:**
The output should organize messy notes into readable action items, avoid overconfidence where details are uncertain, and preserve uncertainty such as "maybe" or unclear deadlines.

---

## Case 5 - Likely Failure / Human Review Needed
**Input:**
Leadership meeting transcript excerpt:
- We should probably reduce hiring in Q3 unless sales improves.
- Someone needs to follow up with finance about the revised forecast.
- It may make sense to delay the product launch, but no final decision was made.
- James mentioned that legal concerns might affect the partnership timeline.

**What a good output should do:**
The output should distinguish between decisions, tentative suggestions, and unresolved issues. It should not present undecided points as confirmed action items, and it should flag this case for human review.

---

## Case 6 - Hallucination Risk Case
**Input:**
Meeting notes:
- Discussed customer complaints about delays.
- Reviewed dashboard metrics.
- Agreed that communication needs improvement.

**What a good output should do:**
The output should stay conservative. It should not invent owners, deadlines, or specific tasks that were not explicitly stated. It may note that follow-up actions are unclear.