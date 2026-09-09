# Source grounding and coverage

## Evidence hierarchy

Prefer evidence in this order when sources disagree:

1. executable definitions and deployed configuration;
2. schema/catalog output and generated metadata;
3. tests and monitored runtime behavior;
4. maintained repository documentation;
5. tickets, meeting notes, and supplied prose;
6. inference.

The order is a default, not a substitute for judgment. A stale deployed definition can be less authoritative than an approved migration that has not run yet. State the relevant date and environment.

## Coverage map

Before authoring, maintain a compact working map:

| Item | Page destination | Representation | Evidence | State |
|---|---|---|---|---|
| `analytics.fact_cashflow` | Object detail | specification + columns | `models/fact_cashflow.sql` | verified |
| Refresh cadence | Operations | definition list | not supplied | unknown |

Use the map to prevent attractive summaries from silently dropping filters, dependencies, edge cases, or operational constraints.

## Evidence locators

Use the most precise locator available:

- repository path and line;
- database and fully qualified object name;
- catalog or API endpoint;
- ticket or decision-record identifier;
- dated interview or supplied brief.

In the page, place locators near the relevant claim. A sources appendix is useful, but it does not replace local traceability.

## Confidence language

Use visible, consistent states:

- **Verified** — directly supported by authoritative evidence.
- **Derived** — calculated or mechanically inferred from verified evidence.
- **Reported** — stated by a stakeholder or secondary document.
- **Illustrative** — example data or behavior, not a production fact.
- **Unknown** — not present in available evidence.
- **To confirm** — a specific unresolved question that affects use or operation.

Do not hide uncertainty in footnotes. If an unknown affects correctness, place it in the summary and the relevant detail section.

## Source inspection

For code-backed documentation:

- read definitions and their imports/references;
- inspect tests for boundary behavior;
- search downstream use before claiming impact;
- distinguish development, staging, and production;
- identify generated files and avoid documenting them as hand-maintained sources;
- record snapshot date or commit when persistence matters.

## Change documentation

For a diff, plan, or implementation review, document:

- prior behavior;
- changed mechanism;
- affected interfaces and consumers;
- migration or compatibility behavior;
- rollback or recovery path when known;
- tests and evidence;
- unresolved risk.

Show the causal chain, not merely a list of modified files.
