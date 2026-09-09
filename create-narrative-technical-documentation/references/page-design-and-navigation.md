# Page design and navigation

The agreed narrative contract determines section order and density. The structures below are defaults for durable reference pages, not mandatory output templates.

## Design posture

Technical documentation is polished-utilitarian. The page should feel intentionally designed, but the design serves scanning, comparison, traceability, and sustained reading.

Before coding, define:

- four to six named colors;
- heading, body, label, and code type roles;
- a one-sentence layout concept tied to the domain;
- density appropriate to the audience.

Prefer project design tokens when they exist. Otherwise use hue-biased neutrals, one primary accent, and separate semantic colors for success, warning, error, unknown, and information.

## Information architecture

For a page with four or more substantial sections, provide persistent navigation on wide screens and a compact mobile alternative. Navigation labels must match visible headings. Use stable, readable fragment identifiers.

Recommended order:

1. scope and summary;
2. system or lineage context;
3. object or process specification;
4. detailed fields or steps;
5. operational behavior;
6. risks, limitations, and change impact;
7. sources and freshness.

## Typography and density

- Keep running prose near 60–75 characters per line.
- Use a clear, committed scale; do not make every heading enormous.
- Use mono text for identifiers, code, data types, and exact values.
- Use `font-variant-numeric: tabular-nums` in quantitative columns.
- Apply `text-wrap: balance` to short headings, not code or identifiers.
- Load every weight used or rely on a dependable local/system stack.

## Components

- Use definition lists for small specifications.
- Use semantic tables for repeated fields or comparisons.
- Use `<details>` for long SQL, payloads, logs, examples, and secondary edge cases.
- Use badges only for meaningful state or confidence.
- Make copy controls say what they copy.
- Use callouts sparingly for material risk, unknowns, or decisions.
- Put source locators next to claims.

## Responsive behavior

- Set `min-width: 0` on grid and flex children.
- Wrap long prose and identifiers safely; preserve code with scroll.
- Put wide tables in labeled scroll containers.
- Collapse the sidebar into a top disclosure or drawer on narrow screens.
- Avoid fixed heights for content sections.
- Ensure anchored headings are not hidden behind sticky chrome.

## Themes and motion

Persistent pages benefit from deliberate light and dark schemes. Define tokens in `:root`; override tokens only in the alternate scheme. Do not use filter inversion.

Motion may clarify expansion, navigation state, or diagram transitions. Respect `prefers-reduced-motion`. Avoid scroll-jacking, continuous effects, and slide-like entrance choreography.

## Accessibility

- Use landmarks: header, nav, main, aside, footer.
- Maintain heading order.
- Provide visible `:focus-visible` styles.
- Give controls accessible names and accurate expanded states.
- Do not encode status by color alone.
- Put captions on tables and figures when they add context.
- Preserve keyboard operation for search, disclosures, theme controls, and diagram tools.
