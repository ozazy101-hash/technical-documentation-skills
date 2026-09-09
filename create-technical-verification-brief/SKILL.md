---
name: create-technical-verification-brief
description: Create a compact, evidence-first, self-contained HTML brief after technical implementation or change work so the builder can verify what the code actually does. Use for SQL models and views, pipelines, APIs, SFTP flows, applications, schemas, configuration, and related tests when the immediate goal is implementation understanding rather than polished publication. For an audience-led visual story, use create-narrative-technical-documentation; for a durable exhaustive reference, use create-technical-html-documentation.
---

# Create Technical Verification Brief

Produce a fast builder-facing verification artifact. Its governing question is:

> What does the current evidence show was implemented, and where might the builder's mental model still be wrong or incomplete?

Keep the grounding bar high and the presentation cost low. Prefer exact facts, traceable locations, and useful compression over decorative polish.

## Boundary

Use this skill to inspect and explain completed or in-progress technical work. It may identify suspicious behavior, gaps, and contradictions, but it is not a substitute for an explicitly requested code review, security audit, or test run.

Create a self-contained HTML brief unless the user requests another format. Do not turn the brief into a publication narrative, an exhaustive system encyclopedia, or a redesign exercise.

## Workflow

### 1. Fix the evidence snapshot

Establish what is in scope before interpreting it. Use the user's stated scope first. When appropriate, inspect:

- the relevant working-tree or commit diff;
- changed and directly affected files;
- SQL, schemas, configuration, migrations, orchestration, and tests;
- generated metadata or plans when already available.

Record the repository or source location, branch or revision when known, inspected scope, and generation time. When no version-control snapshot exists, state exactly which supplied files or objects were inspected.

Treat code and executable configuration as primary evidence. Treat comments, tickets, prior documentation, and AI summaries as claims to reconcile. Never expose secrets or reproduce credentials.

### 2. Reconstruct actual behavior

Work from evidence to behavior, not from filenames or intended design. Trace the relevant path far enough to explain inputs, transformations, state changes, outputs, and safeguards. For each in-scope object, determine the applicable facts:

- role and execution context;
- inputs, outputs, dependencies, and downstream consumers;
- grain, keys, joins, filters, calculations, null behavior, and deduplication;
- scheduling, retries, ordering, delivery, authentication boundary, or failure handling;
- tests, assertions, observability, and operational controls;
- behavior added, removed, or changed.

Read [coverage-and-representations.md](references/coverage-and-representations.md) when choosing domain-specific coverage or a visual representation.

### 3. Maintain evidence states

Label material conclusions as one of:

- **Verified** — directly supported by inspected evidence;
- **Derived** — logically reconstructed from multiple verified facts;
- **Reported** — stated by a ticket, comment, document, or user but not independently confirmed;
- **Unknown** — evidence is absent, ambiguous, stale, or contradictory.

Attach a useful locator to important verified and derived claims: file and line, object and field, configuration key, migration, test, or query fragment. Do not invent production behavior, owners, volumes, SLAs, schemas, or downstream consumers.

### 4. Select diagnostic representations

Start with semantic HTML: a change ledger, behavior tables, field derivations, callouts, and short code excerpts. Add a visual only when it reduces verification effort.

Typical choices include:

- dependency or lineage map for upstream/downstream structure;
- before/after delta for changed behavior;
- field derivation matrix for calculated outputs;
- sequence or state flow for runtime order and failure paths;
- test matrix for coverage and unverified cases;
- blast-radius view for established downstream impact.

Use the smallest representation that makes the question easier to answer. Pair every diagram with a textual or tabular fallback. Keep identifiers consistent between diagrams, tables, and code.

### 5. Build the brief

Create one restrained, navigable HTML file that works offline. Use semantic markup, legible typography, compact navigation, clear evidence labels, accessible contrast, keyboard-reachable controls, responsive layouts, and print styles.

Let the evidence determine the sections. A useful default reading order is:

1. snapshot and scope;
2. concise implementation summary;
3. changed-object ledger;
4. actual behavior and dependencies;
5. tests and safeguards;
6. discrepancies, risks, and unknowns;
7. evidence index.

This is a starting shape, not a mandatory template. Omit sections without a job. Keep code excerpts short and link them to their explanation within the document. Avoid ornamental animation; use motion only when it demonstrates execution order and preserve a static end state.

### 6. Verify the artifact

Before delivery, confirm:

- every in-scope changed object is accounted for;
- every material behavior claim has evidence or an explicit non-verified state;
- diagrams, tables, summaries, and code excerpts agree;
- unknowns that could change the interpretation are visible;
- the HTML opens without network access and has no broken navigation or controls;
- no secrets or sensitive values are embedded.

When available, run the relevant existing tests or static checks if the user asked for implementation verification rather than documentation alone. Report what was and was not executed; do not imply runtime verification from source inspection.

## Interaction with the user

Proceed without a design interview when the scope is discoverable. Ask only when a missing choice would materially change which implementation is being documented or how a contradiction should be interpreted.

If the user supplies their expected behavior, compare it with the evidence and surface differences neutrally. The brief supports their decision; it does not silently redefine the intended system.

## Handoff to narrative documentation

Treat this brief as an intermediate evidence map, not a permanent source of truth. A later narrative document may use it to find code, decisions, and unresolved questions, but should re-check the current implementation and reconcile any newer changes.

## Deliverables

Return:

1. the self-contained HTML brief;
2. a one-sentence scope statement;
3. the revision or evidence snapshot used;
4. material unknowns and tests not executed.

