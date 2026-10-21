# Post-meeting workup

**Account / meeting:** name, meeting type, date, time zone.
**Status:** Draft — commitments and wording awaiting participant verification.
**Coverage:** actual source, time range/pages read, missing sections.
**Baseline:** dated assessment/version, or “not supplied”.

## Recap

Up to five evidence-backed bullets: customer objective; decisions; open questions; risks/competition; agreed next step. Separate a proposal from a decision.

## Commitments

### Customer side

| ID | Owner | Action | Status | Deadline: wording → absolute date | Evidence |
|---|---|---|---|---|---|

### Seller side

| ID | Owner | Action | Status | Deadline: wording → absolute date | Evidence |
|---|---|---|---|---|---|

Statuses: explicit commitment; conditional offer; requested, not accepted; proposed; superseded. Keep conditional/requested items clearly apart from confirmed obligations. Put unassigned actions in a clarification list with the source wording, rather than guessing a side or individual. Where no time was agreed, say so.

## MEDDPICC evidence

Use these dimensions for comparison. These definitions do not establish an account's facts:

- **Metrics:** measurable customer outcome, baseline and owner.
- **Economic buyer:** person with discretionary authority for this spend; title alone is insufficient.
- **Decision criteria:** what the customer will evaluate, including technical, business and governance needs.
- **Decision process:** steps, people and timing for the decision.
- **Paper process:** procurement, contracting, legal and security mechanics.
- **Identify pain:** customer-owned problem, consequence and urgency.
- **Champion:** influential supporter who has taken a verifiable action; friendliness is insufficient.
- **Competition:** evidenced alternatives, including maintaining the current situation.

With a baseline:

| Dimension | Previous finding / source date | Evidence on this call | Proposed change | Uncertainty / verification |
|---|---|---|---|---|

Without a baseline, replace “Previous” and “Proposed change” with “Observed evidence” and “Question for the next review”. Do not imply a score moved. No evidence found is not a positive qualification result.

## Stakeholders, risks and signals

| Person or signal | What is evidenced | Interpretation / hypothesis | Source | Verification needed |
|---|---|---|---|---|

## Follow-up draft

Subject, concise recap, confirmed commitments and a clearly separated request to confirm unresolved points. No invented obligation, endorsement or delivery promise. Mark **Draft — not sent** even after participant verification.

## CRM-ready notes

Account/opportunity identification and match status; factual meeting note; confirmed next steps; unresolved ownership/dates. List proposed field changes only where actual IDs/schema have been checked. **Prepared only — no CRM write performed.**

## Participant correction log

| Workup version | Row / section | Previous interpretation | Correction | Basis: transcript or participant clarification | Outputs revised |
|---|---|---|---|---|---|

Keep the prior version or this concise before/after table. Do not keep raw private copies in the public skills clone.

## Structured hand-offs

One small object per supported signal; omit empty categories rather than inventing them. JSON or a table is acceptable. No actual call to another skill is implied.

```json
{
  "meeting": {"account": "", "meeting_date": "", "time_zone": "", "coverage": ""},
  "workup_version": "v1",
  "participant_review": "pending",
  "destination": "Deal Health Reviewer | Whitespace Mapper | Basho Engine",
  "signal_type": "stakeholder | commitment | meddpicc_evidence | expansion_hypothesis | candidate_trigger",
  "finding": "",
  "evidence": [{"source": "", "locator": "", "quote": "", "source_date": ""}],
  "baseline_reference": null,
  "verification_status": "",
  "hypothesis": null,
  "unknowns": [],
  "next_question": "",
  "disclosure_limits": "Internal account analysis only unless approved otherwise",
  "prepared_only": true
}
```

Distinguish the event date from the meeting/source date when they differ. Use null or “unknown” for absent dates, owners and baseline references. The source quote must be real; example placeholders are not evidence.
