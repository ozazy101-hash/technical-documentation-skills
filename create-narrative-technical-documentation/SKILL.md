---
name: create-narrative-technical-documentation
description: Create narrative-first, self-contained HTML technical documentation by analyzing the evidence and reader's question, then selecting only the diagrams, interactive inspectors, tables, code views, and operational stories that advance that narrative. Use for SQL and data models, lineage, ETL/ELT, Snowflake, SFTP, APIs, systems, processes, incidents, and technical changes when visual storytelling, representation choice, or audience-specific reading routes matter. For a straightforward exhaustive reference page without narrative design, use create-technical-html-documentation.
---

# Create Narrative Technical Documentation

Create a durable technical HTML document whose structure follows the reader's question. Treat diagrams, charts, tables, code, inspectors, and motion as explanatory patterns—not a checklist of features.

## Boundary

Use this skill when the user wants one or more of the following:

- help choosing how technical material should be explained;
- a visual or interactive narrative rather than a uniform reference template;
- a self-contained HTML artifact for SQL, data, API, architecture, process, operational, incident, or change documentation;
- multiple reading lenses for genuinely different audiences or decisions.

For slides or a speaker-led deck, use `$create-high-end-html-presentations`. For a conventional exhaustive reference whose form is already clear, use `$create-technical-html-documentation`.

## Workflow

### 1. Ground the material

Inspect the supplied sources before designing. Separate verified, derived, reported, illustrative, unknown, and to-confirm content. Never invent production schemas, owners, SLAs, security boundaries, incidents, or outcomes.

Read [source-grounding-and-coverage.md](references/source-grounding-and-coverage.md) when evidence comes from files, code, SQL, metadata, or multiple sources. Read [sql-and-data-objects.md](references/sql-and-data-objects.md) for the relevant SQL, pipeline, API, architecture, or change content model. These are coverage prompts, not mandatory page sections.

### 2. Frame the narrative contract

Identify:

- reader and decision;
- primary question;
- one-sentence claim or learning outcome;
- scope and evidence boundary;
- desired depth, visual intensity, and delivery constraints.

Read [narrative-routing.md](references/narrative-routing.md) when the narrative is not explicit, several plausible stories compete, or several audiences need different paths.

If the user already states the audience and desired story, proceed. If materially different choices remain, propose a compact story plan—question, claim, spine, selected patterns, and deliberate exclusions—and ask for confirmation before the expensive build. When the choice is low-risk or the user asked to proceed directly, state the assumption and continue.

### 3. Build a narrative coverage map

Classify each source fact as:

- **must answer** — necessary to establish the selected claim;
- **supporting evidence** — useful in an inspector, table, or disclosure;
- **material unknown** — could change the conclusion or safe use;
- **outside this story** — valid information intentionally excluded.

The map is complete when every must-answer item and material unknown has a destination and evidence locator. Completeness is relative to the agreed story, not the maximum information available.

### 4. Select the minimum viable narrative

Read [pattern-catalog.md](references/pattern-catalog.md) before selecting representations for a new artifact. Choose one primary narrative spine and only the supporting patterns needed to answer the next reader questions.

For every proposed component, record:

1. the question it answers;
2. the claim it makes visible;
3. the evidence it requires;
4. its exact textual or tabular fallback.

Remove components without a distinct job. Prefer an overview plus linked detail over an all-purpose diagram. Use alternate reader lenses only when the underlying material genuinely supports different routes; lenses foreground relevant sections rather than duplicating the truth.

### 5. Choose the rendering engine after the pattern

Read [implementation-and-engine-choice.md](references/implementation-and-engine-choice.md) when the page includes diagrams, quantitative charts, custom interaction, animation, or strict offline delivery.

Default order:

1. semantic HTML for exact facts and repeated values;
2. CSS for layout, state, simple flows, and timelines;
3. inline SVG plus small vanilla JavaScript for custom linked views;
4. Mermaid for maintainable formal topology;
5. ECharts for data-driven quantitative exploration.

The engine is an implementation choice, not the information architecture. Keep exact truth outside pixels.

### 6. Design and build

Create a scrolling, deep-linkable document unless the user's use case calls for a different shell. Provide progressive disclosure: orientation first, in-context inspection second, durable detail third. Read [page-design-and-navigation.md](references/page-design-and-navigation.md) before choosing type, palette, density, navigation, themes, or motion.

Use the optional starter only when it accelerates the selected story:

```bash
python3 scripts/scaffold_documentation.py ./output \
  --title "Customer identity change" \
  --system "Data platform"
```

Adapt or replace its composition freely. A starter is a shell, not a required visual identity.

For formal lineage, topology, sequence, state, schema, or C4 diagrams, read [mermaid-and-architecture.md](references/mermaid-and-architecture.md). State one claim per figure, label meaningful edges, keep identifiers stable across views, and pair large maps with focused detail.

Motion may demonstrate sequence, causality, state transition, or selected-route orientation. Keep it user-triggered or brief, preserve a static end state, and respect `prefers-reduced-motion`.

### 7. Validate the story and artifact

Read [qa-and-delivery.md](references/qa-and-delivery.md). Verify both layers:

- **Narrative:** the selected route answers its primary question without requiring unrelated sections; claims, diagrams, tables, code, and conclusions agree.
- **Artifact:** self-contained delivery, console, deep links, interaction, keyboard use, theme, print, reduced motion, and desktop/mobile layouts all work.

Run:

```bash
python3 scripts/validate_html_documentation.py path/to/document.html --strict-self-contained
```

If workplace policy blocks inline script or large attachments, deliver a local asset bundle instead of pretending one-file portability is possible. Use `scripts/inline_assets.py` only when inlining is permitted.

## Output modes

Match the user's requested stopping point:

- **Recommend:** return the story plan and representation choices; do not build HTML.
- **Prototype:** build only the uncertain interaction or diagram needed to test the idea.
- **Create:** deliver the complete HTML and required local assets.
- **Redesign:** preserve grounded content while changing narrative structure or visual grammar.

Do not turn a recommendation request into an artifact build or an artifact request into a preliminary workshop.

## Deliverables

For a complete build, deliver:

1. the HTML source of truth;
2. any required local asset folder or a verified self-contained file;
3. a short statement of the chosen narrative and why each major pattern was selected;
4. visible material unknowns and illustrative content;
5. a validation note.

Do not create Markdown, PDF, slides, or an exhaustive appendix unless requested or necessary to answer the agreed story.

## Bundled resources

- `references/narrative-routing.md` — story selection, confirmation, and multi-audience routes.
- `references/pattern-catalog.md` — question-to-pattern catalog derived from the seven documentation laboratories.
- `references/implementation-and-engine-choice.md` — native HTML/CSS/SVG/JavaScript, Mermaid, ECharts, portability, and interaction rules.
- `references/source-grounding-and-coverage.md` — evidence states, locators, and narrative coverage maps.
- `references/sql-and-data-objects.md` — optional content models for SQL, pipelines, APIs, systems, and changes.
- `references/page-design-and-navigation.md` — page composition, responsive design, themes, motion, and accessibility.
- `references/mermaid-and-architecture.md` — formal diagram rules.
- `references/qa-and-delivery.md` — content, visual, technical, and release checks.
- `assets/starter/technical-page.html` — optional accessible page shell.
- `scripts/scaffold_documentation.py` — copies the optional shell.
- `scripts/inline_assets.py` — inlines permitted local assets.
- `scripts/validate_html_documentation.py` — validates structure and portability.
