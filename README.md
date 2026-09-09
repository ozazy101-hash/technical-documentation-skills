# Technical Documentation Skills

Two complementary Codex skills for turning technical implementation evidence into useful HTML documentation.

## Included skills

### `create-technical-verification-brief`

Creates a compact, evidence-first, self-contained HTML brief after implementation work. It is designed for the builder who needs to verify what changed, how the code now behaves, what is tested, and which conclusions remain uncertain.

### `create-narrative-technical-documentation`

Creates polished, audience-aware, self-contained HTML technical documentation. It selects diagrams, tables, code views, interactive inspectors, and narrative structure according to the reader's question rather than emitting every available component.

## Intended workflow

```text
Implement or change the system
            ↓
Create a technical verification brief
            ↓
Review, test, and correct the implementation
            ↓
Create narrative technical documentation
            ↓
Publish the durable audience-facing artifact
```

The verification brief is an intermediate evidence map, not a substitute for checking the current source. Narrative documentation should reconcile the brief with the current implementation before publication.

## Install

Copy either skill directory into your Codex skills directory:

```bash
cp -R create-technical-verification-brief ~/.codex/skills/
cp -R create-narrative-technical-documentation ~/.codex/skills/
```

Each directory is independently installable and contains its own `SKILL.md`, UI metadata, and required supporting resources.

## Repository structure

```text
.
├── create-technical-verification-brief/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── create-narrative-technical-documentation/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

No license is granted by default. Add an explicit license before distributing or accepting external contributions.

