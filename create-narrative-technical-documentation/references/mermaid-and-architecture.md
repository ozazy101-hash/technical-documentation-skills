# Mermaid and architecture diagrams

## Model the claim first

Write a one-sentence claim before writing diagram syntax. Examples:

- “Curated cash flows are produced only after project and valuation keys resolve.”
- “A failed invoice is quarantined and does not block unrelated batches.”

The diagram includes only the elements needed to support that claim. Put the sentence in `<figcaption>`.

## Diagram selection

- `flowchart TD`: complex pipelines, decisions, layered lineage.
- `flowchart LR`: only simple three- or four-stage linear flows.
- `sequenceDiagram`: request, event, retry, and service interactions over time.
- `erDiagram`: stable entity relationships and cardinality.
- `stateDiagram-v2`: lifecycle states and transitions.
- `classDiagram`: types and contracts when classes are the reader's actual concern.
- C4: system context or container boundaries when C4 support is available.

Use ELK layout for complex diagrams when the local Mermaid build supports it. Test the actual bundle; do not assume feature availability.

## Invariants

- Label every meaningful edge with a verb or payload: `loads`, `publishes invoice`, `joins on property_id`.
- Use directionality; avoid symmetric lines when movement is directional.
- Show mechanisms, not boxes named after concepts.
- Keep node titles concise and put detail in the surrounding page.
- Use `<br/>` in quoted labels; do not use escaped `\n`.
- Use `theme: "base"` with variables matching the page tokens.
- Never set page-level `.node` styles.
- Put the accessibility label on the stable diagram shell, not the generated SVG.

## Required shell for large diagrams

Use this hierarchy:

```html
<figure>
  <div class="doc-diagram-shell" role="img" aria-label="Lineage from sources to curated model">
    <div class="doc-diagram-toolbar">…zoom, reset, expand…</div>
    <div class="doc-diagram-viewport">
      <div class="doc-diagram-canvas mermaid">…</div>
    </div>
  </div>
  <figcaption>The curated model is published only after keys resolve.</figcaption>
</figure>
```

For an overview that fits legibly, zoom controls are optional. For a diagram that overflows, provide zoom in/out/reset, pointer drag panning, Ctrl/Cmd+wheel zoom, and an expanded view.

## Large architectures

At roughly 15 or more elements, stop expanding the same graph. Use:

- a domain or layer overview;
- links from nodes to detailed sections;
- one focused figure per critical mechanism;
- structured component specifications below.

Split diagrams on meaningful seams such as ingestion, transformation, serving, and control—not arbitrary page fit.

## Failure behavior

If Mermaid is unavailable or fails to render, retain a readable fallback: an ordered flow, relationship table, or visible source block. Never deliver an empty diagram region. Log the render failure only during development; the finished page should fail gracefully.
