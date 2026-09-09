# QA and delivery

## Content verification

- Every in-scope object or source fact appears in the coverage map and page.
- Grain, keys, joins, filters, calculations, and refresh behavior are either documented or visibly unknown.
- Identifiers match the source exactly.
- Illustrative values and examples are labeled.
- Conflicting evidence is disclosed.
- Source locators and verification date are present.
- Summary claims are supported by detail sections.

## Technical verification

- Complete HTML document with `lang`, viewport, title, and self-contained favicon.
- No unresolved template tokens.
- No console errors.
- No missing local scripts, styles, fonts, or images.
- If self-contained delivery is promised, no external URLs remain.
- Deep links load at the intended heading.
- Search and table filters handle empty and no-result states.
- Copy buttons work on secure and local contexts or fail visibly.
- Mermaid has a readable fallback and redraws correctly after theme changes when applicable.
- ECharts resizes with its container and includes a textual or tabular equivalent.

## Visual verification

Inspect at a wide desktop size, a typical laptop size, and a narrow mobile width:

- navigation remains usable;
- headings and tables do not clip;
- code scrolls rather than widening the page;
- focus rings are visible;
- contrast holds in each deliberate theme;
- long object names wrap safely;
- sticky elements do not cover anchor targets;
- the first viewport makes scope and status obvious.

Test reduced motion and keyboard-only navigation.

## Diagram verification

- The caption states the claim.
- Edge labels explain action or payload.
- Direction and cardinality are accurate.
- Overview and detail use the same identifiers.
- A graph with many nodes is split or paired with detail sections.
- Zoom/pan/expand exist when normal-width labels are not legible.
- Fallback content remains understandable without JavaScript.

## Release package

Deliver either:

- one verified self-contained `.html`; or
- one `.html` plus a clearly named local asset folder.

Keep HTML as the source of truth. Include a concise handoff note covering:

- scope;
- evidence snapshot or commit;
- unknowns and illustrative content;
- required local assets, if any;
- how to regenerate or validate.

Do not silently replace an existing artifact. Use a new descriptive filename unless the user explicitly requested an update.
