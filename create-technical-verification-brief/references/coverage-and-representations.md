# Coverage and representation guide

Read the relevant domain prompts, then choose representations by the verification question rather than by visual variety. These prompts are checks for omitted behavior, not mandatory page sections.

## SQL views and data models

Establish, when applicable:

- database, schema, object name, materialization, and refresh mechanism;
- output grain and the expressions or constraints that enforce it;
- upstream relations and the role of each alias or CTE;
- join type, predicate, expected cardinality, and fan-out risk;
- row filters, date windows, status rules, and incremental boundaries;
- primary, unique, natural, surrogate, and foreign keys;
- field-level provenance, calculations, casts, defaults, and null handling;
- unions, aggregation, ranking, deduplication, and late-arriving data behavior;
- tests, source freshness, downstream models, and access controls evidenced in scope.

Useful representations:

- lineage map for object dependencies;
- field derivation matrix for output logic;
- join contract table for cardinality and grain;
- transformation funnel for filters, joins, aggregation, and row-count checkpoints;
- before/after behavior table for modified SQL.

## Pipelines, orchestration, and SFTP

Establish, when applicable:

- trigger, schedule, timezone, ordering, and concurrency behavior;
- source and destination locations without revealing secrets;
- file naming, format, compression, encryption, and manifest rules;
- validation, quarantine, idempotency, checkpointing, and replay behavior;
- retries, timeouts, partial failure, notification, and recovery path;
- archival, retention, deletion, and reconciliation;
- hand-offs between tasks, systems, teams, and security boundaries.

Useful representations:

- sequence diagram for execution and acknowledgements;
- state flow for arrival, validation, processing, delivery, and failure;
- stage-gate diagram for validation and promotion;
- operational contract table for schedules, retries, and recovery.

## APIs and services

Establish, when applicable:

- caller, endpoint, method, version, request, response, and status semantics;
- authentication and authorization boundary;
- validation, transformation, persistence, and side effects;
- pagination, rate limits, retry safety, idempotency, and timeouts;
- synchronous and asynchronous dependencies;
- error mapping, logging, metrics, traces, and tests.

Useful representations:

- request sequence for calls and dependencies;
- contract table for inputs, outputs, and errors;
- state machine for asynchronous jobs;
- failure-path tree for retries and terminal outcomes.

## Applications and Streamlit

Establish, when applicable:

- entry points, pages, components, callbacks, and session state;
- input validation, caching, query construction, and data access;
- control flow from user action to output;
- authorization, secrets boundary, and environment configuration;
- error states, empty states, observability, and tests.

Useful representations:

- annotated code map for responsibility by region;
- interaction sequence for user action to result;
- state table for session and cache behavior;
- dependency map for modules, services, and data sources.

## Change-centered verification

When a diff is the evidence, distinguish:

- structural changes: objects, interfaces, schemas, dependencies;
- behavioral changes: filters, calculations, branching, error handling;
- operational changes: schedules, retries, configuration, observability;
- validation changes: tests added, removed, weakened, or left absent;
- documented intent that the implementation does not establish.

A compact change ledger should identify the object, change, observed effect, evidence locator, verification state, and downstream impact if established.

## Representation selection

Choose by the reader's immediate verification question:

| Question | Strong default | Add when useful |
|---|---|---|
| What changed? | Change ledger | Before/after delta |
| What depends on what? | Dependency table | Lineage map |
| How is this field produced? | Field derivation matrix | Focused expression trace |
| In what order does it run? | Ordered steps | Sequence diagram |
| What happens on failure? | Failure contract table | State flow or failure tree |
| What is tested? | Test matrix | Coverage callout |
| What could this affect? | Impact table | Blast-radius view |

Prefer zero diagrams when tables answer the question faster. Prefer one focused diagram over one system-wide canvas. Use interactivity only when it helps locate or compare evidence; the exact facts must remain readable without it.

