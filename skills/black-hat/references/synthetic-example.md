# Synthetic example: a successful demo is not a purchase decision

All people, companies, records and source excerpts below are fictional. These references identify the supplied example files; they are not live customer records.

## Supplied material

**S1 — Opportunity export, 12 February 2026**
Northstar Engineering. Seller's target: expand from 60 to 100 seats by 31 March. Internal note: “Great demo. Head of Design is our champion. Budget should be fine.” No budget owner, agreed decision process or procurement start date is recorded.

**S2 — Buyer email, 14 February 2026**
Head of Design: “The pilot team liked the review workflow. Before adding seats, we need to understand why only 28 of the current 60 seats were active last month. Finance has asked us to keep spending flat. Can we solve this within our current agreement?”

**S3 — Pilot meeting record, 16 February 2026**
Pilot lead reports that the test exported the required file format successfully. The implementation owner has not confirmed the data-access approach for a rollout. No commercial decision was made.

**User request:** “Black Hat our expansion plan. Tell me whether to invest another week in a full rollout demo, and what to ask the customer. Use only these files. Do not change Salesforce.”

## Example review

**Recommendation: qualify before investing a full week.** The pilot has a useful technical result, but the buyer is asking about existing usage and a flat-spend option. The supplied records do not establish approval for expansion.

**As of:** 17 February 2026. **Source boundary:** S1–S3 only; no live Salesforce or mailbox access.

### Main failure paths

| Failure path | Evidence or hypothesis | Test |
|---|---|---|
| The buyer prioritises current value over adding seats. | Customer evidence: S2 asks to understand current usage before expansion. | Ask which existing-seat result must improve before an expansion is considered. |
| The expansion cannot fit the spending constraint. | Customer evidence: S2 reports Finance's flat-spend request. Whether a reallocation is possible is unknown. | Ask what commercial options Finance will consider and who can confirm them. |
| We prepare for a seller deadline that the buyer has not adopted. | Internal claim: 31 March appears in S1; S2–S3 do not confirm that buying date. | Ask what event drives a decision and what steps would need to finish first. |
| Technical pilot success does not carry through to rollout. | S3 confirms one export test; rollout data access remains unconfirmed. | Agree a small access test with a proposed implementation owner before building the full demo. |

There is no fifth distinct failure path supported by these files. No named competitor or rejection has been established.

### Strongest counter-evidence

Our claim is that a good demo and a supportive contact make expansion likely. S2 instead asks whether the problem can be solved within the existing agreement. S3 supports the technical feasibility of one export task, which is valuable but does not establish willingness or authority to buy 40 more seats. The Head of Design's purchasing authority remains unknown.

### Three questions

1. “What would you need to see from the 60 existing seats before you would consider any additional seats?”
2. “When Finance says spending should stay flat, which options can we explore, and who should confirm that with us?”
3. “Who can help us test the rollout data access, and is there a customer event that requires a decision by a specific date?”

### Rehearsal — simulation, not a buyer quotation

**Possible buyer objection:** “Why would we add seats while we are still trying to understand the ones we have?”

**Proposed seller response:** “We should establish that first. Can we agree which teams need access, what stopped the other seats being used and what outcome would make the current agreement work better? Then we can decide whether expansion belongs in the plan.”

### Minimum action plan

| Proposed action | Owner status | Timing status | Required evidence | If the test fails |
|---|---|---|---|---|
| Verify the usage definition and discuss the existing-seat gap. | Proposed: account lead with the customer's operations owner; customer owner not yet confirmed. | Proposed: next customer conversation. | A consistent usage measure and the buyer's priority outcome. | Reframe around current value; do not assume expansion. |
| Confirm the commercial options and decision process. | Proposed: account lead; Finance/procurement contact to confirm. | Before committing the extra demo week. | Buyer-confirmed constraint, decision roles and sequence. | Hold the expansion demo and qualify a smaller next step. |
| Run a bounded data-access test. | Proposed: technical specialist with implementation owner to confirm. | After the customer agrees the test. | Observed access to the required data in the approved environment. | Stop or redesign the rollout approach before promising delivery. |

**Evidence ledger:** S1 is an internal record of the team's plan; S2 is a dated statement by one buyer contact; S3 records a bounded technical result. None establishes an approved expansion, a confirmed champion, or a win probability. The “28 of 60” figure is the buyer's reported measure, not a verified adoption analysis.

**Actions taken:** review produced only. No CRM records, calendar entries, tasks or emails changed.
