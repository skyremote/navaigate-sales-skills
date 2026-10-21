# Fictional example and practice

Everything below is invented for training. Product categories are generic; no customer, price, licence rule or return is implied.

## Inputs

**Account:** Alder Components, fictional account ID DEMO-014. **As of:** 21 October 2026. **Planning horizon:** this quarter.

- **S1 — `fictional-footprint.csv`, 20 October, all three named centres:** Engineering uses CAD and has a PDM pilot in one of its three teams; no PLM deployment. Quality confirms no PLM deployment; its CAD/PDM coverage was not collected. Manufacturing uses CAD and confirms no PLM deployment; PDM coverage was not collected. Blank fields mean not collected.
- **S2 — `fictional-call.txt`, 19 October, lines 10–28:** Engineering lead Maya Chen owns the PDM pilot, wants to resolve revision confusion, and will discuss a wider pilot. Quality lead Luis Morgan reports manual change handoffs and proposes a PLM discovery conversation. Manufacturing manager Erin Shah wants to understand handover requirements for a planned line. None of these statements establishes a purchase or budget approval.
- **S3 — `fictional-usage.csv`, September, Engineering only:** CAD active across the three engineering teams; PDM active in the one pilot team. Report contains no Quality or Manufacturing telemetry and no commercial entitlement information.

## First output

| Buying centre | CAD | PDM | PLM |
|---|---|---|---|
| Engineering | Owned [S1, S3] | Partial [S1, S3] | Whitespace [S1] |
| Quality | Unknown — not collected [S1] | Unknown — not collected [S1] | Whitespace [S1] |
| Manufacturing | Owned [S1] | Unknown — not collected [S1] | Whitespace [S1] |

Entitlement is **unknown for every cell**. Quality and Manufacturing usage is unknown: S1 establishes a footprint or its absence, not telemetry. The incomplete CAD/PDM fields are not expansion claims.

### Provisional candidates

| Rank / ID | Candidate | Value / effort / readiness | First stakeholder |
|---|---|---|---|
| 1 / Q | Test a PLM workflow for Quality's manual change handoffs | Potentially useful cross-team improvement [S2]; technical fit and commercial terms unknown; organisational coordination needed. Conditional: discovery requested, business case untested. | Luis Morgan, who raised the issue [S2]; authority unconfirmed. |
| 2 / E | Extend Engineering's PDM pilot to one more team | Bounded revision-control improvement [S2]; existing pilot may reduce technical work, but team adoption and entitlement remain unconfirmed. Ready for a validation conversation, not a rollout commitment. | Maya Chen, pilot owner [S2]. |
| 3 / M | Explore Manufacturing's handover requirements before suggesting PLM | Potential future value [S2]; need and technical fit untested, timing and commercial work unknown. Conditional and weaker than E. | Erin Shah, requester [S2]. |

Initial thesis for E: **For Engineering, test whether extending the PDM pilot to one additional team reduces revision confusion, using an agreed workflow check before wider rollout.** No savings or ROI figure is supportable.

## The seller changes the decision

**S4 — fictional seller correction, 21 October:** “Quality's change budget is frozen this quarter. Luis is interested but cannot sponsor work now. Maya has agreed a 30-minute workflow review next week. Erin's line proposal is still awaiting approval; do not treat it as a funded programme.”

Treat S4 as seller-reported information. It corrects readiness and effort, not the footprint matrix. Re-rank:

1. **E rises from 2 to 1:** a specific next conversation and existing pilot make validation practical; budget and entitlement still need checking. Maya is an evidenced first contact, not a proven economic buyer.
2. **Q falls from 1 to 2 and is parked this quarter:** the apparent value does not remove the budget barrier. Do not write that a purchase or enablement programme is ready.
3. **M stays 3:** funded timing is not established; confirm the programme before making a product recommendation.

If the seller selects E, record that selection explicitly. If not, say **recommended E; awaiting choice**. A possible seller rewrite, shown here only as an illustration, is: “Let's work with Maya on one more team's revision process and see whether the current pilot can support it.” Do not attribute this wording to a real seller.

### Prepared handoffs

**Deal Health:** DEMO-014; Engineering; Maya Chen is an engaged pilot owner [S2], with a workflow review agreed per seller [S4]. Budget owner and entitlement unknown. E is a bounded validation hypothesis; Q is parked for budget timing [S4]. No automatic change to MEDDPICC or CRM.

**Basho:** DEMO-014; Maya Chen, pilot owner [S2]; E thesis above. **No verified external trigger.** Internal pain and invitation are supported by S2/S4; do not claim a funded rollout or numerical result. Discovery question: “Which revision handoff should we test with the next team?” A draft can be prepared from this context, but nothing has been sent.

## 15-minute practice

1. **3 minutes:** run the first prompt in SKILL.md with S1–S3. Check that blank fields stay Unknown and entitlement stays separate.
2. **4 minutes:** read the three proposed plays. Challenge which needs are proven, who has authority, and what the model assumed about effort.
3. **3 minutes:** add S4 as your seller correction. Ask for the new order and one reason per change. The model must not rewrite historical evidence to hide its first ranking.
4. **3 minutes:** choose one play, rewrite its thesis in your own words, name the first person and a proposed next validation action.
5. **2 minutes:** say which play you are parking and why. Copy the handoff to a new conversation if useful; this does not update another skill or CRM automatically.

For a real account, replace the fixture with a sanctioned export and an account conversation you are allowed to use. When evidence is missing, the useful output is a focused discovery question rather than an invented opportunity.
