# Narrative routing

Use this reference when the material could support several stories, the audience is unclear, or the user wants different reading paths.

## Narrative contract

A narrative contract is a compact agreement about what the document must help a reader understand or decide. Capture:

| Element | Question |
|---|---|
| Reader | Who will use this, and what do they already know? |
| Decision | What action, review, diagnosis, implementation, or operation follows? |
| Primary question | What must become easier to answer? |
| Claim | What single sentence should the page establish? |
| Scope | Which systems, objects, environments, and time window are included? |
| Evidence boundary | Which facts are verified, reported, illustrative, or missing? |
| Depth | Orientation, working detail, audit detail, or a layered combination? |
| Delivery | One file, local asset bundle, printable reference, workplace constraints? |

Do not force the user to fill in a questionnaire when their request already supplies the answers. Infer low-risk choices from the material and state them briefly.

## Story spines

Choose one primary spine. Add another only when the reader's task genuinely crosses both.

| Spine | Reader's dominant question | Typical order |
|---|---|---|
| Reference | What is this object and how do I use it? | summary → contract → fields → logic → operations |
| Mechanism | How does this work end to end? | context → flow → transformation → output → edge cases |
| Diagnosis | Why is this failing, slow, late, or inconsistent? | symptom → evidence → causal path → containment → verification |
| Change | What changes, what is affected, and how is it released? | current → delta → impact → rollout → proof → recovery |
| Operation | What happens in normal and exceptional execution? | trigger → sequence → state → monitoring → intervention |
| Recovery | How do we contain and restore safely? | signal → scope → decision → rollback/replay → validation |
| Contract | What crosses this boundary and under which rules? | actors → interface → validation → errors → compatibility |
| Assurance | What requirement is proven by which evidence? | requirement → control → test → evidence → gap |

The page may contain supporting sections outside the primary spine. Keep the opening route focused on the primary question.

## Confirmation rule

Ask for confirmation only when selecting the story would materially change the artifact. Examples:

- an operator runbook and an architecture explainer would prioritize different evidence;
- an executive overview and an implementation reference require different density;
- the user supplied a repository but no task, audience, or desired output;
- two incompatible visual approaches are equally plausible.

Offer one recommendation first:

```text
Recommended story
Reader: data engineers reviewing a model change
Question: what changes downstream, and can we retreat safely?
Claim: the proposed identity seam changes derivation but preserves the public model contract.
Spine: current/proposed delta → blast radius → release gates → recovery
Keep as supporting detail: field dictionary and full SQL
Leave out: estate metrics and generic system inventory
```

If the user has already asked to build a particular artifact, proceed without turning confirmation into ceremony. State the assumed reader and question in commentary or the artifact brief.

## Multiple audiences

Use selectable lenses when the same evidence supports distinct, recurring reader questions. A lens should:

- change the recommended reading route or foregrounded modules;
- retain one shared source of truth;
- use stable deep links;
- avoid duplicating facts into separate versions;
- leave all essential evidence reachable.

Useful lenses include proposer/reviewer/operator, overview/implementation/audit, movement/delay/control/recovery, and current/target/impact.

Use one linear route when audiences differ only slightly. A row of tabs is not a narrative strategy by itself.

## Minimum viable narrative

Start with the fewest components that establish the claim:

1. orientation: scope, state, and the primary claim;
2. mechanism or evidence: the one representation that reveals the hard relationship;
3. consequence: impact, decision, or next action;
4. supporting truth: exact table, code, definitions, or evidence packet.

Add a component only if it answers a new question. Put secondary material in linked detail or disclosure rather than the primary route.

## Narrative review

Before building, test the outline:

- Can the intended reader state the point after the first viewport?
- Does each section answer a question that logically follows the prior section?
- Does every figure make one checkable claim?
- Are operational consequences and material unknowns visible at the moment they matter?
- Can a reader reach exact fields, rules, SQL, or evidence without reverse-engineering the graphic?
- Could any component disappear without weakening the story? If yes, remove or demote it.
