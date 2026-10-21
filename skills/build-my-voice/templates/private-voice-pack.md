# Templates for the participant's private writing-voice folder

These are authoring templates, not a ready personal profile. Replace every placeholder with evidence or explicitly mark it unknown. Keep this folder outside the public repository. Do not include raw source emails in the reusable package.

## File: SKILL.md

```markdown
---
name: your-name-voice
description: Draft and edit writing in the owner's personally reviewed voice. Use for their messages and updates when asked to apply their writing style. Check the profile's language, context and approval status before drafting.
---

# My writing voice

Read PROFILE.md, CALIBRATION.md and EXAMPLES.md before drafting. Use confirmed rules appropriate to the requested situation. Candidate rules are provisional; do not represent them as the owner's settled preference.

Keep facts separate from style. Use the supplied brief for facts and ask about missing details. Never copy customer details, commitments or claims from a voice example. Return a draft for the owner to review; do not send it.

Apply recent direct corrections within their recorded scope. If instructions conflict, ask the owner. Before returning a draft, check opening, sentence rhythm, level of detail, request and closing against the relevant approved example. State any missing facts separately.

Do not fetch emails for routine drafting unless the owner requests that extra context. Propose profile changes only when the owner supplies a correction or authorises a new sample. Confirm that file changes succeeded; do not imply background learning or cross-platform sync.
```

Keep the generated name lowercase, hyphenated and under 64 characters. File links may replace the plain filenames when supported.

## File: PROFILE.md

```markdown
# Personal writing profile

Owner: [participant's chosen name]
Status: [candidate / participant calibrated]
Version and date: [version; date]
Language and spelling: [participant-confirmed preference]
Coverage: [actual sample count; date range; writing situations]
Limitations: [missing situations; unavailable sources; uncertain patterns]

| ID | Writing rule | Situation | Private evidence IDs | Status |
| --- | --- | --- | --- | --- |
| R01 | [observable choice that changes a draft] | [scope] | [IDs] | [candidate / confirmed, date] |

## Differences by situation

- Customer follow-up: [supported choices or insufficient evidence]
- Internal update: [supported choices or insufficient evidence]
- Difficult message: [supported choices or insufficient evidence]

## Avoid

[Only language and habits the owner rejected, with correction IDs or confirmed evidence.]

## Check before returning a draft

Use the right situation and language. Preserve the factual brief. Apply confirmed rules and scoped corrections. Do not reproduce private example facts. Ask for missing facts. Leave the message unsent.
```

## File: EXAMPLES.md

```markdown
# Approved writing examples

Only participant-approved text belongs here. If no examples are approved yet, state that plainly and keep test drafts in a separate private working file.

## [Example ID and writing situation]

Approval: [owner; date; approved wording]
Factual brief: [fictional or redacted context]
Approved text: [approved, redacted text]
Rules illustrated: [rule IDs and observable decisions]

Example facts must not be copied into new messages.
```

## File: CALIBRATION.md

```markdown
# Personal writing corrections

## [Correction ID; date; situation]

Before: [draft line]
After: [participant's replacement]
Lesson: [narrow writing decision]
Scope: [this message / this situation / all writing, as confirmed]
Approval: [participant's confirmation or still pending]
Profile change: [rule ID; version; applied / proposed]
Example change: [example ID or none]

Keep corrections with pending approval distinct from accepted changes.
```

## File: EVIDENCE.md — keep private and outside any shared package

```markdown
# Writing evidence ledger

Account identity and scope: [participant; selected mailbox/folder; date range]
Retrieved at: [date and timezone]
Actually read: [count]
Included after exclusions: [count]

| Source ID | Date | Situation | Authorship | Included portion / exclusions | Supports |
| --- | --- | --- | --- | --- | --- |
| E01 | [date] | [situation] | [verified own / participant confirmed / uncertain] | [decision; minimal redacted evidence] | [rule IDs] |

Missing access or coverage: [specific limitations]
```

## File: CHATGPT-PROJECT-INSTRUCTIONS.md

Generate a self-contained version that includes the current confirmed rules, rather than leaving `[paste rules]` for the owner to assemble. Keep it concise enough for the platform's current instruction limit. If necessary, place the detailed profile and approved examples in separate private Project files and explicitly name them.

```markdown
Use my personally reviewed writing style for drafting and editing. Return unsent drafts for my review.

My language and spelling: [confirmed preference].
My confirmed rules: [insert the actual confirmed rules, with scope].
My recent scoped corrections: [include actual approved corrections or state none].
My current status and limitations: [candidate / calibrated; coverage].

If I have attached PROFILE.md, EXAMPLES.md and CALIBRATION.md to this Project, read the relevant files before drafting and apply confirmed rules for this situation. If a file is missing, say so and use only the rules actually provided here. Do not pretend you can open a local folder or read my mailbox from these instructions alone.

Use the facts I give you. Voice examples teach writing choices, not customer facts. Ask about missing information and do not create promises, dates or evidence. Keep messages unsent.

When I correct a line, propose the narrow profile change. Explain which Project instruction or file I need to replace if you cannot save it. Do not claim to remember updates across products or to monitor my emails in the background.
```

## Delivery receipt

Return the private destination or filenames, actual files created, current approval status, source coverage, fourth-draft check and whether installation or upload has actually been verified. A draft returned in chat is not an installed skill.
