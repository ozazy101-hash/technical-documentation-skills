# Technical storytelling pattern catalog

This catalog routes reader questions to explanatory patterns. It is derived from seven exploratory HTML documentation laboratories; it is a working design system, not an industry-standard taxonomy.

## Vocabulary

- **Primitive** — HTML table, definition list, CSS grid, SVG path, button, disclosure, code block.
- **Engine** — browser-native HTML/CSS/SVG/JavaScript, Mermaid, ECharts, or another renderer.
- **Pattern** — a repeatable answer to a reader question, such as lineage delta or stage-gated release.
- **Composition** — several patterns arranged into one coherent story.
- **Template** — a reusable page shell or code scaffold. Templates implement patterns but should not choose the story.
- **Narrative spine** — the ordered questions that determine which patterns belong.

Use the pattern name as a design vocabulary, then adapt it to the evidence. Do not copy a laboratory's synthetic content or fixed visual style.

## Fast router

| Reader question | Start with | Pair with |
|---|---|---|
| What exists and what does each item mean? | object dossier or field dictionary | searchable navigation |
| Where does this sit in the wider system? | context/container topology | component details |
| Where did this field or row come from? | layered lineage explorer | field provenance + SQL |
| How does one request, file, or event move? | runtime sequence replay | topology + event log |
| What state is it in and what can happen next? | state-machine debugger | transition table |
| Who owns each step and exception? | swimlane/process token | responsibility matrix |
| Where were rows removed? | row-accounting Sankey + waterfall | exact accounting table |
| When does instability occur? | calendar heatmap + distribution | incident list |
| What will a change affect? | blast-radius graph | consumer impact register |
| What changed between versions? | current/proposed/overlay lineage delta | schema or rule diff |
| How should this change be released? | stage-gated release | validation gates + recovery tree |
| Why is this query slow? | query autopsy | linked SQL + critical path |
| Which domains are tightly coupled? | directed adjacency matrix | selected-pair inspector |
| Where is cost, storage, or ownership concentrated? | hierarchy tree + treemap | ranked ledger |
| Where do latency, residency, or trust rules apply? | policy-aware deployment atlas | route/policy table |
| Which requirement is actually proven? | evidence loom | traceability matrix |
| How uncertain is the forecast? | fan chart + sensitivity | percentile table |
| What do I do when it fails? | symptom-specific recovery path | runbook decision matrix |

## Reference and navigation patterns

### Searchable document shell

**Answers:** How do I find a model, field, rule, or section later?

Use stable fragment links, persistent table of contents on wide screens, compact mobile navigation, search/filter, and scroll-location feedback. This is page infrastructure, not the narrative itself.

Use for documents with four or more substantial sections or many named objects. Preserve native browser Find by keeping important text in the DOM.

### Overview → inspector → dossier → field

**Answers:** How do I move from orientation to exact detail without losing context?

Select a graph node to update an in-context inspector. Provide a separate explicit deep link to a durable object dossier and field anchor. Selection should not unexpectedly navigate.

Pair with a relationship table and back/return links. Use tabs only inside the compact inspector; keep durable dossiers as sections.

### Reader-lens router

**Answers:** Which parts matter to my current question?

Offer a small set of genuine questions—such as movement, delay, control, and recovery—and foreground the matching sections. Keep a single shared truth underneath.

Use when audiences or tasks have materially different routes. Avoid turning every heading into a tab or hiding essential caveats from a lens.

## Structure, lineage, and dependency patterns

### Context or container topology

**Answers:** Which actors, systems, containers, stores, and boundaries participate?

Use C4-style levels or a small directional topology. Label edges with actions or payloads. Pair with component responsibilities and a textual relationship list.

Use for orientation. Avoid combining runtime sequence, every table, and every security detail into the same graph.

### Layer-isolated lineage explorer

**Answers:** Which sources and transformations produce this output?

Group nodes by source, loading, intermediate, final, and consumer layers. Provide lens controls, zoom/expand for large graphs, node inspection, and stable identifiers.

Pair with object dossiers and an exact dependency table. At roughly 15 nodes, split by domain or layer rather than shrinking labels.

### Field provenance and influence

**Answers:** Which fields directly derive this output, and which merely affect whether or how it appears?

Separate direct source fields from indirect influences such as filters, join eligibility, ranking, policy, or configuration. Link each path to SQL lines or rule locators.

Use when a column-level lineage arrow would otherwise overstate direct derivation.

### Entity relationship detail

**Answers:** What are the keys, cardinalities, and grain relationships?

Show only attributes required to understand identity and cardinality. Pair with a full semantic field dictionary. Mark expected one-to-one, one-to-many, optional, and fan-out risks explicitly.

### Blast-radius graph with linked evidence

**Answers:** Which downstream objects and consumers are reachable from this change?

Re-root a directional dependency graph from the selected object or field. Highlight reachable consumers and coordinate selection with SQL, an ordered impact list, and owning teams.

Use only with sufficiently complete edges. A graph is not a reliable impact assessment when metadata excludes dynamic SQL, data movement, external extracts, or unobserved consumers; show those limits.

### Current/proposed/overlay lineage delta

**Answers:** What is added, changed, retired, and unchanged?

Keep node positions stable across current and proposed modes; use an overlay for semantic comparison. Selection reveals purpose, owner, field impact, and contract effect.

Pair with an exact SQL/schema/rule diff. Use status labels and line styles in addition to color.

### Directed adjacency matrix

**Answers:** Which domains or components are most densely coupled?

Rows are callers or changed domains; columns are dependencies or affected domains. Encode strength in cells, state direction beside the matrix, and let the reader threshold or switch coupling measures.

Use when dozens of pairwise relationships make a node-link graph unreadable. Pair with ranked pairs and a selected-cell explanation. Avoid when the goal is tracing one long path.

### Hierarchy tree + treemap + ledger

**Answers:** Where are cost, storage, people, objects, or ownership concentrated?

Use hierarchy for parentage, treemap area for part-to-whole concentration, drill-down for domains, and a ranked ledger for exact comparison.

Use only with additive, trustworthy measures. Avoid area comparison for many nearly equal values.

### Policy-aware deployment atlas

**Answers:** Where do latency, residency, failover, sovereignty, or trust policies apply?

Use a schematic region map with explicit boundaries, measured latency labels, route replay, and policy outcomes. Screen distance must not imply geographic or network distance.

Pair with a route table containing hop, region, latency, data class, and policy result.

## Time, behavior, and process patterns

### Runtime sequence replay

**Answers:** Who acts, in what order, and where do waits, retries, or alerts occur?

Use actor columns and finite steps. Scenario controls may replay healthy, late, failed, or degraded paths. Show the current step, event log, and static ordered fallback.

Pair with topology when the reader also needs structural context. Sequence answers when; topology answers where.

### Executable state-machine debugger

**Answers:** Which states and transitions are valid from here?

Select a current state to illuminate valid exits, events, guards, and invalid transitions. Pair with a transition table containing source, event, guard, target, side effect, and failure behavior.

Use for lifecycle truth. Avoid using a state machine for a simple ordered process without branching.

### Swimlane or BPMN-style process token

**Answers:** Who owns each step, decision, exception, and hand-off?

Separate participants into lanes. Replay one token through tasks, gateways, quarantine, and manual intervention. Pair with a responsibility/exception table.

Use BPMN semantics only when the notation is accurate; otherwise label the result BPMN-inspired.

### File or job lifecycle + failure scenarios

**Answers:** What is true now, and how should a failed artifact be handled?

Pair a clickable lifecycle state strip with named failure scenarios and recovery playbooks. Preserve delivery identifiers, checkpoints, idempotency, quarantine, replay, and validation evidence.

State and recovery are related but distinct: state describes truth; the playbook describes action.

### Stage-gated release

**Answers:** In what order can a change advance safely?

Represent prepare, backfill, shadow, dual-read, cutover, observe, and cleanup—or the stages grounded in the actual system. Each stage reveals entry evidence, verification, output, abort condition, and rollback position.

Use for migrations and risky changes. Avoid presenting a generic seven-stage ritual when fewer stages are sufficient.

### Symptom-specific recovery decision path

**Answers:** What should happen after this detectable failure?

Start from an observable symptom. Lead through detect, contain, decide, and restore. Make the rollback boundary and preserved evidence explicit.

Pair with a runbook decision matrix and exact owner/escalation route. Avoid a single arrow labeled “rollback.”

### Architecture epochs + semantic diff

**Answers:** How did the system evolve, and when did a control or boundary appear?

Keep architecture geometry stable across named epochs and highlight semantic changes. Pair with a timeline and schema/configuration diff.

Use when historical sequence explains present constraints or migration decisions.

## Quantitative and diagnostic patterns

### Row-accounting Sankey + waterfall

**Answers:** Where did rows, events, money, or workload go?

Use ribbon width for surviving magnitude and named branches for exclusions. Use a waterfall and accounting table to reconcile exact entering, lost, and leaving values.

All flows must conserve the measured quantity or disclose why they do not. Avoid when quantities are inferred or incomparable.

### Freshness or reliability envelope

**Answers:** Is performance inside the objective, and where are incidents?

Use a time series with objective band, incident annotations, and exact run table. Distinguish source-event, arrival, load, and publication latency when available.

### Calendar heatmap + distribution

**Answers:** When does instability recur, and how unusual is it?

Use a calendar/hour heatmap for temporal location and a histogram/box plot for spread, quartiles, and outliers. Pair with thresholds and representative observations.

Use with enough observations for a pattern. Encode warning/breach with more than color.

### Query autopsy

**Answers:** Where does runtime, row amplification, spill, or scanning accumulate?

Use a plan-shaped flame view whose width represents elapsed contribution inside the parent. Highlight the critical path and link operators to SQL. Inspect rows out, spill, partitions, and diagnostic meaning.

Operator times may overlap; do not blindly sum siblings. Prefer the platform's actual query profile when available.

### Fan chart + sensitivity

**Answers:** What range of futures is plausible, and which assumptions drive the decision?

Show percentile bands around the median, an explicit decision threshold, numeric breach probability, and sensitivity bars or controls for key assumptions.

Use only with defensible samples or models. Label percentile intervals as uncertainty, not guaranteed bounds.

## Contracts, assurance, and decision patterns

### SQL object contract

**Answers:** What does this model guarantee and how is each rule implemented?

Combine fully qualified identity, purpose, grain, keys, joins, filters, calculations, refresh, tests, security, and limitations. Use a field dictionary and targeted SQL fragments with source locators.

Treat the SQL content model as a prompt. Include only items required by the agreed narrative and material safe-use constraints.

### Interface contract

**Answers:** What constitutes a valid file, request, event, or response?

Document naming/path, finalization, encoding/schema, authentication, time semantics, validation, rejection, compatibility, idempotency, ownership, and examples. Use definition lists and semantic tables.

### Trust-boundary and least-privilege matrix

**Answers:** Where does authority change, and what may each identity do?

Show zones and crossings, then use a matrix for identity, permitted action, object boundary, prohibited reach, and evidence. Refer to secret locations; never include credentials.

### Requirement → control → test → evidence loom

**Answers:** Which requirement is actually proven by current evidence?

Make every node selectable and every chain bidirectional. Pair with a traceability matrix containing stable evidence locators and verification dates.

Missing evidence differs from a failed test. Do not collapse both into a red badge.

### Validation gate + evidence packet

**Answers:** What measurable result permits the next decision?

For each gate, name measure, window, threshold, owner, status, and stored evidence. Selection opens the evidence packet or query locator.

Thresholds without owner approval are proposals, not facts.

### Consumer impact register

**Answers:** How does technical change reach contracts, teams, and user-visible behavior?

Record surface, field path, change, compatibility class, owner, behavior, and proof required. Distinguish schema-compatible from behavior-compatible.

### ADR + unknowns

**Answers:** Why was this option chosen, what was rejected, and what remains unresolved?

Record context, decision, alternatives, consequences, reversibility, owner, and material unknowns. Use this as durable reasoning beneath the visual narrative.

### Evidence capability and limitation model

**Answers:** What can each metadata source prove, and where are its blind spots?

For every catalog, log, monitor, or metadata view, state declared versus observed evidence, retention/latency, privilege requirements, exclusions, and the claim it can support.

Avoid treating one platform view as complete lineage or operational truth.

## Composition recipes

Recipes are starting points, not mandatory structures.

### SQL or data-model explanation

Narrative brief → layered lineage explorer → selected object inspector → field provenance → SQL contract/dictionary → tests and unknowns.

### Data-pipeline operation

Operational topology → runtime sequence replay → interface contract → lifecycle/failure scenarios → trust boundaries → evidence limitations.

### Technical change review

Current/proposed lineage delta → consumer impact register → stage-gated release → validation gates → recovery paths → ADR and unknowns.

### Performance diagnosis

Symptom and objective → query autopsy → linked SQL → time/distribution evidence → causal hypothesis → validation or remediation evidence.

### Assurance or audit

Scope and requirement set → evidence loom → traceability matrix → gaps and limitations → owner actions and verification date.

## Selection discipline

Before including a pattern, complete this sentence:

> The reader needs to answer **[question]**; **[pattern]** reveals **[relationship or value]** using **[evidence]**, while **[fallback]** preserves exact truth.

If the sentence is weak, choose semantic HTML or omit the visual. If two patterns answer the same question, keep the simpler one unless their pairing reveals distinct truths, such as Sankey plus waterfall or heatmap plus distribution.
