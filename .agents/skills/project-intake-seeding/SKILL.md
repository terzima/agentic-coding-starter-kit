---
name: project-intake-seeding
description: Use when turning a new project idea, raw project notes, or an existing repository into durable startup docs, first planning candidates, assumptions, and open questions.
---

# Project Intake Seeding

Use this skill at the beginning of a new project or when a repo lacks durable startup context. The output is orientation and planning evidence, not accepted implementation behavior.

## Core Rule

Separate what is known from what is assumed. Raw intake can seed durable docs, but it does not become accepted requirements until captured in an accepted spec or plan.

## Workflow

1. Read `AGENTS.md` first when it exists.
2. Read `docs/AGENTIC_WORKFLOW_MANUAL.md`, `docs/status/CURRENT_STATE.md`, `docs/repo-map.md`, and `docs/project-charter.md` when present.
3. Read only the user-provided intake material or explicitly relevant repo files needed to orient the project.
4. Classify findings into:
   - durable facts;
   - assumptions;
   - open questions;
   - roadmap candidates;
   - first safe specs;
   - out-of-scope ideas.
5. Create or recommend updates to:
   - `docs/project-charter.md`;
   - `docs/repo-map.md`;
   - `docs/status/CURRENT_STATE.md`;
   - `docs/roadmap.md`;
   - `docs/glossary.md`;
   - `docs/worklog/intake-seeding-topic.md` when evidence is exploratory or too detailed for status.
6. Keep startup docs concise enough for future sessions to read quickly.
7. Recommend the first spec prompt only after the project shape, first safe slice, and open questions are visible.

## Stop Conditions

Stop and report the blocker when:

- the user asks for implementation before durable context exists;
- required source material is missing or contradictory;
- the next step requires product judgment from the owner;
- raw intake contains secrets or private credentials;
- evidence is too uncertain and needs a Spike before seeding.

## Output Contract

```txt
Durable facts:
Assumptions:
Open questions:
Roadmap candidates:
First safe specs:
Out-of-scope ideas:
Docs created or recommended:
Recommended next prompt:
```

## What To Avoid

- Treating raw intake as accepted requirements.
- Writing implementation plans before the first safe spec is clear.
- Copying large raw source material into durable docs.
- Reading the whole repo when startup docs and targeted files are enough.
- Hiding uncertainty in broad roadmap language.
