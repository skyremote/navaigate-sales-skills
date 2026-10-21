# Log the work against the right opportunity

Use this when the request is to keep activities current, connect work to an opportunity, or reconcile changed/closed/reopened records. An activity is not a completed sale, and a record label is not the full customer context.

## First prompt

> Review my customer meetings from this week and propose the missing Salesforce activity entries. Match each one to the right account and opportunity, and show me any ambiguous or closed records before you change anything.

## Read and match

Use a bounded date range and the user's own relevant calendar/meeting evidence. Record the actual meeting date, attendees, purpose, outcome and next step. A calendar invitation alone does not prove that a meeting happened. Confirm held/completed status using supplied notes or another relevant source.

Find existing activities before proposing a new one. Match account, opportunity, contact and owner through verified relationships and record IDs. Do not assume that a contact's other opportunity is the correct destination. Ask which record is intended when a customer has several concurrent opportunities.

Use the organisation's actual activity objects, fields and allowed values. A call, meeting, email, task and note may be represented differently. Determine which is appropriate from the schema and team conventions. Record participants' actual contribution without inflating credit or logging the same work several times.

## Changed, closed or reopened opportunities

Read available history and related records to establish what changed and when. Preserve the event's actual date even when logging it later. Keep a historical activity on its correct record unless the user authorises a verified correction under team policy.

If the requested destination is closed, confirm the permitted activity-logging route; do not assume a new opportunity or stage change is required. If a record has reopened, distinguish the old and current buying process. Do not automatically copy old commitments, amount, stage, close date or technical success into the new decision.

If the organisation's policy or field meaning is unknown, ask its record owner or administrator for that specific rule. Return an actionable proposal while that question is resolved. Do not use a system workaround to change credit, ownership or historical reporting.

## Useful entry

| Field | Proposed content |
|---|---|
| Related records | Verified account, contact and opportunity IDs |
| Actual date | Date/time/timezone supported by the evidence |
| Type/status | Allowed values confirmed from this organisation |
| Summary | What the customer needed, what was discussed and what was decided |
| Contribution | What the participant actually did |
| Next step | Owner and date if agreed; otherwise explicitly unconfirmed |
| Evidence | Private note/message/file reference |
| Duplicate check | Existing matching entry, or searched scope and result |

Show proposed entries before applying them unless the user already explicitly authorised this precise scope. Use the main skill's reread, authorisation, retry and readback checks. If a tool times out after a create, look for the matching existing entry before another attempt.
