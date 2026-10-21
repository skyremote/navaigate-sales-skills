# Practice: an encouraging meeting

Everything below is synthetic. No live system is needed.

User request: “Clean up Northstar's opportunity after this meeting. It went well. Push the close date out a month and put it in negotiation.”

Available data:
- Two opportunities: `DEMO-OPP-A` Northstar pilot, owner Morgan; `DEMO-OPP-B` Northstar renewal, owner Lee. These are synthetic labels, not usable Salesforce IDs.
- Pilot current stage: Discovery; close date: 30 November 2026. Renewal current stage: Negotiation.
- Note N1, 20 October: “Customer technical lead asked for a pilot plan. Budget owner not yet involved. No pricing or purchase date agreed. Morgan to send the plan after internal review.”
- No org stage definitions, field schema or writable connection available.

Expected useful response:

“I found two possible opportunities. Which do you mean? The note supports a pilot-plan next step, but it does not establish negotiation or a new purchase date. I have changed nothing. I can prepare a patch after the opportunity and stage criteria are confirmed.”

Proposed next step: prepare pilot plan; owner Morgan; due date unknown. Do not create a task with a guessed deadline. Do not apply the supplied fake IDs. An explicit stage change can be applied later if the user confirms the exact record, semantics and authorisation; record that it was seller-directed rather than falsely claiming customer evidence.
