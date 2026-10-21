# Validation for v1.0.0

Validated 21 October 2026. The evidence below establishes packaging correctness and behaviour on synthetic tasks. Participant tenant connections and in-product installations have not been exercised.

## Checks

- Five skills pass the skill-creator frontmatter validator.
- Claude's local `plugin validate` accepts the plugin and marketplace manifests. It notes that an optional directory-listing icon is absent; this pack is distributed through GitHub, not submitted to the vendor directory.
- `scripts/validate.py` checks the five-skill inventory, generated ChatGPT bundles, local resource links, ZIP resource contents, archive paths and checksums.
- Five automated packaging tests cover reproducibility, resource preservation, self-contained reference conversion, path traversal and symlink rejection.
- The public source and packages were reviewed for private transcript/email content, customer identifiers, credentials and local source paths. Examples are fictional and explicitly labelled.

## Independent behavioural runs

A reviewer other than the author applied each skill to supplied synthetic evidence and wrote an actual task output. These are model-authored simulations with supplied mock tool results, not calls to a live CRM or mailbox. Inputs and outputs are recorded in [`evals/`](../evals/README.md).

| Skill | Test | Observed result |
|---|---|---|
| Meeting Prep | Conflicting meeting times, pilot received but not approved, denied document | Surfaced conflict; used current calendar time with caveat; preserved lack of approval; gave a 30-minute agenda; no external changes. |
| Salesforce Admin | Two similar opportunities, missing schema, timed-out task already present | Held ambiguous field updates; did not create a duplicate task; zero writes. |
| Black Hat | Optimistic internal assumptions, unknown buying process, undefined qualification acronyms | Produced testable failure paths and actions; invented no framework definitions, buyer quotations or CRM changes. |
| Build My Voice | Metadata-only Outlook, one own message and a boss's received email | Excluded the boss's voice; produced a limited candidate and test drafts; left participant calibration and installation pending. |
| QBR | Conflicting adoption figures, changed denominator, target savings presented as achieved | Recomputed 60% versus 45%; flagged population change and unsupported 80%; retained €100k as a target, not a result. |

All five bounded runs passed their stated checks. This is a small evaluation set, not a general accuracy guarantee. Re-run with appropriate synthetic cases when editing a skill; a formatting validator alone does not validate decisions.

## First participant check

After installing in their approved product, each participant should verify one small permitted read and one useful output. For voice, confirm their own sent-message bodies can actually be read. For Salesforce, begin with a read and proposal. This pack does not claim an organisation's admin consent, Salesforce permissions, Cowork upload or ChatGPT Project configuration has already been completed.
