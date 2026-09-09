# SQL, data-object, process, and system content models

Use these as coverage models, not mandatory page templates. Omit irrelevant fields and visibly mark material unknowns.

## SQL view, model, or table

Document:

- fully qualified name and object type;
- business purpose and technical purpose;
- grain—what one row represents;
- primary, natural, surrogate, and foreign keys;
- upstream objects and downstream consumers;
- joins, cardinality expectations, and fan-out risks;
- filters, exclusions, and row-security behavior;
- calculated fields and business rules;
- column dictionary;
- materialization, refresh method, and cadence;
- late-arriving data, deduplication, and history strategy;
- ownership and support route;
- access classification and sensitive fields;
- performance considerations, partitioning, clustering, or indexes;
- tests, monitors, and quality expectations;
- limitations, edge cases, and unresolved questions;
- change impact and compatibility considerations;
- source locators and last verification date.

### Column dictionary

Use a semantic table. Recommended columns:

| Column | Type | Nullable | Definition | Derivation/source | Example | Quality/security notes |
|---|---|---:|---|---|---|---|

Preserve exact identifiers in mono text. Mark examples as illustrative unless verified. If a table is wide, place it in a horizontally scrollable region and keep the first column sticky when useful.

### Transformation logic

Explain logic in the reader's order of concern:

1. source selection and effective-date handling;
2. joins and cardinality;
3. filters and exclusions;
4. deduplication or ranking;
5. calculations and classifications;
6. aggregation and final grain;
7. incremental or merge behavior.

Pair each business rule with its implementation locator. Include only the SQL fragments that clarify a rule; make the full definition collapsible or link it to source.

## Data pipeline or operational process

Document:

- trigger and schedule;
- inputs and contracts;
- ordered processing steps;
- branches and decisions;
- outputs and downstream effects;
- state, idempotency, and replay behavior;
- failure modes, retries, dead-letter or quarantine handling;
- monitoring, alerting, SLA/SLO, and freshness;
- manual interventions and runbook links;
- owner and escalation route;
- security boundaries and credentials involved;
- known capacity or cost constraints.

A flowchart shows control or data movement. A sequence diagram shows time-ordered interactions. Do not combine both into one overloaded figure.

## API or service

Document:

- responsibility and boundary;
- callers and dependencies;
- endpoints or messages;
- authentication and authorization;
- request/response or event contracts;
- lifecycle and sequence behavior;
- validation, errors, retries, and idempotency;
- rate limits, timeouts, and availability targets;
- observability and ownership;
- versioning and compatibility.

## System architecture

Document:

- context and user or system actors;
- components and responsibilities;
- interfaces and direction of flow;
- data stores and systems of record;
- trust and security boundaries;
- runtime behavior for important scenarios;
- deployment environments;
- availability, recovery, monitoring, cost, and capacity concerns;
- decisions, constraints, alternatives, and known debt.

Prefer a context overview plus separate component and runtime sections. Readers should not have to decode one all-purpose diagram.

## Implementation plan or change review

Document:

- goal and non-goals;
- current state and target state;
- affected objects and interfaces;
- ordered implementation stages and dependencies;
- data migration or backfill;
- compatibility and rollout controls;
- validation and acceptance evidence;
- risks, mitigations, rollback, and ownership;
- status matrix and decisions still required.
