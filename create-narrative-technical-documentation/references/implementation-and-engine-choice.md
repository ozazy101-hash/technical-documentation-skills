# Implementation and engine choice

Choose the explanatory pattern first. Choose its rendering engine second.

## The five layers

### Semantic HTML — durable truth

Use headings, paragraphs, definition lists, tables, code blocks, details, links, and landmarks for information that must remain searchable, selectable, printable, accessible, and understandable without custom rendering.

Best for contracts, field dictionaries, matrices, exact values, evidence, decisions, runbooks, and fallbacks.

### CSS — composition and small visual grammar

Use CSS Grid/Flexbox, borders, tracks, tokens, pseudo-elements, and state classes for simple timelines, stages, swimlanes, callouts, gauges, heat cells, and responsive page composition.

Best when the geometry follows document flow and contains limited data. Keep wide flows in labeled scroll containers.

### Inline SVG — precise custom diagrams

Use inline SVG when stable geometry, direct labeling, custom paths, linked highlighting, or exact visual control is central. Store the underlying data in JavaScript objects or semantic HTML; render SVG from that source rather than duplicating truth manually.

Best for custom lineage explorers, dependency graphs, Sankey-like row flows, query-plan flame views, fan charts, and schematic deployment maps.

### Mermaid — maintainable formal diagrams

Use a locally bundled Mermaid build for topology, flowcharts, sequence, state, ER, class, or C4-style diagrams when maintainability and text-authored structure matter more than bespoke interaction.

Mermaid is optional. Provide a readable relationship table or ordered fallback and test the actual local bundle. Read `mermaid-and-architecture.md`.

### ECharts — quantitative exploration

Use a locally bundled ECharts build when data volume, responsive axes, tooltips, brushing, zoom, multiple coordinated series, or accessible chart descriptions justify the library cost.

ECharts is optional. Pair it with a visible summary or data table. Avoid using graph series for deterministic architecture layouts.

## Decision table

| Need | Preferred engine | Why |
|---|---|---|
| Exact reference, dictionary, comparison | semantic HTML | durable and auditable |
| Three-to-seven step flow or rollout | CSS + HTML | simpler than a graph engine |
| Formal topology maintained by engineers | Mermaid + fallback | concise source and standard grammar |
| Bespoke clickable lineage with a side inspector | inline SVG + JavaScript + relationship table | stable layout and linked interaction |
| Dense pairwise dependencies | HTML/CSS matrix | node-link diagrams become unreadable |
| High-volume time series or distributions | ECharts + table | robust quantitative interaction |
| Small line, waterfall, or fan experiment | inline SVG + table | portable and visually controlled |
| Progressive disclosure and deep links | semantic HTML + JavaScript enhancement | works as a document first |

## What the laboratories demonstrate

The seven source laboratories use no external charting library. Their visual systems are composed from semantic HTML, CSS, inline SVG, and vanilla JavaScript. They prove that a one-file artifact can support custom diagrams, coordinated inspectors, filters, scenario replay, and responsive layouts.

That does not make native SVG universally preferable. Hand-authored geometry costs more to maintain; use Mermaid or ECharts when the data or topology changes frequently and the bundled library is acceptable.

## Interaction grammar

Prefer a small set of repeatable interactions:

- **select → inspect:** clicking a node updates a nearby detail panel without moving the reader;
- **select → highlight:** graph, code, table, and field path share one selection state;
- **overview → deep link:** an explicit action opens a stable object or field section;
- **lens → foreground:** a reader choice marks or orders relevant modules without creating duplicate facts;
- **scenario → replay:** controls step through a finite, inspectable sequence;
- **filter → compare:** a matrix or table narrows to a meaningful subset and shows a no-result state;
- **current/proposed/overlay:** stable geometry makes semantic change visible;
- **stage → evidence:** release or process stages reveal entry, proof, abort, and recovery criteria.

Use one state model for each interaction. Update ARIA state (`aria-pressed`, `aria-selected`, `aria-expanded`) with the visual state. Keyboard activation must produce the same result as pointer activation.

## Motion

Motion earns its place when it explains order, movement, causality, or state. Prefer user-triggered replay, short route tokens, linked emphasis, and gentle transitions between known states.

Preserve the final state, include pause/reset when a replay is longer than a moment, and implement a static equivalent under `prefers-reduced-motion`. Avoid continuous animation and scroll-jacking.

## One-file delivery

A self-contained HTML file may include:

- inline CSS;
- inline SVG;
- inline JavaScript;
- data-URI icons and small images;
- inlined local library bundles when licensing and file size permit.

Test the real workplace environment. Email scanners, content-security policy, attachment limits, browser restrictions, and disabled JavaScript can change what is viable. When inline scripts are blocked, deliver a static HTML reference or an HTML-plus-assets folder according to the user's constraints.

## Fallback contract

Every visual has an exact companion:

- graph → relationship or impact table;
- sequence → ordered event log;
- state machine → transition table;
- Sankey → stage accounting table;
- heatmap or chart → data table and numeric summary;
- inspector → durable object or field section;
- scenario replay → static steps and outcomes;
- map → region, route, latency, and policy table.

The fallback is not merely for accessibility. It is the auditable truth and a defence against rendering failure.
