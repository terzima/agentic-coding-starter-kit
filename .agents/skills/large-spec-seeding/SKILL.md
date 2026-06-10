````md
---
name: large-spec-seeding
description: Use when converting a large raw product/project overview into controlled repo seed documents, decomposed specs, decomposed plans, proposed execution batches, ADR candidates, and worklogs. This skill is for project seeding and decomposition only, not implementation.
---

# Large Spec Seeding Skill

## Purpose

Convert `docs/intake/PROJECT_OVERVIEW_RAW.md` into durable, concise, smaller source-of-truth documents that can guide future agent work without requiring agents to reload or reinterpret the full raw overview every session.

This skill creates the project starting point.

It does not execute implementation work.

## Core Distinction

Seeding is not batch execution.

Seeding produces:

- project source-of-truth documents
- decomposed specs
- decomposed plans
- proposed execution batches
- open questions
- ADR candidates
- a carry-forward worklog

Batch execution comes later, after specs and plans exist.

## Inputs

Primary input:

- `docs/intake/PROJECT_OVERVIEW_RAW.md`

Optional inputs, if present:

- `AGENTS.md`
- `docs/intake/*.md`
- prior research notes
- user-provided constraints
- existing repo notes
- existing architecture notes

Do not require optional inputs to proceed if the raw overview is sufficient.

## Approved Output Paths

The skill may create or update only documentation/control files, including:

- `docs/project-charter.md`
- `docs/glossary.md`
- `docs/repo-map.md`
- `docs/roadmap.md`
- `docs/seed/SEED-0000-project-decomposition.md`
- `docs/seed/SEED-0000-results.md`
- `docs/specs/SPEC-0000-project-foundation.md`
- `docs/specs/SPEC-0001-*.md`
- `docs/specs/SPEC-0002-*.md`
- `docs/specs/SPEC-0003-*.md`
- `docs/plans/PLAN-0001-*.md`
- `docs/plans/PLAN-0002-*.md`
- `docs/plans/PLAN-0003-*.md`
- `docs/plans/batches/BATCH-0001-*.md`
- `docs/plans/batches/BATCH-0002-*.md`
- `docs/worklog/0000-seeding-notes.md`
- `docs/adr/ADR-0000-architecture-direction.md` only if justified

Do not create application code, production source files, dependency manifests, generated framework files, or runtime configuration unless explicitly instructed.

## Process

### 1. Read and classify the raw overview

Extract:

- project intent
- target users
- user journeys
- core product behavior
- major entities
- workflows
- integrations
- technical constraints
- product constraints
- non-goals
- risks
- assumptions
- contradictions
- open questions
- first meaningful human-testable milestone

Treat the raw overview as an intake artifact, not the permanent working spec.

### 2. Create or update the project charter

Write `docs/project-charter.md`.

It should define:

- project purpose
- target users
- core problem
- product goals
- non-goals
- success criteria
- constraints
- first meaningful human-testable milestone

Keep this document concise.

### 3. Create or update the glossary

Write `docs/glossary.md` if domain or project-specific terms exist.

It should define:

- domain terms
- project terms
- acronyms
- ambiguous terms that need clarification

Do not overfill it with obvious terms.

### 4. Create or update the repo map

Write `docs/repo-map.md`.

It should define:

- expected top-level repo structure
- responsibility of each major directory
- architectural boundaries
- files future agents should read first
- files future agents should not casually modify
- expected local verification commands, if known

If the repo structure is not yet known, mark proposed structure explicitly as proposed.

### 5. Create the foundation spec

Write `docs/specs/SPEC-0000-project-foundation.md`.

It should define:

- problem statement
- confirmed requirements
- product boundaries
- technical boundaries
- non-goals
- assumptions
- open questions
- acceptance criteria
- first implementation slice
- first human-testable milestone

This is the highest-level controlled spec. It should not become a duplicate of the raw overview.

### 6. Decompose into initial specs

Create a small number of initial specs such as:

- `docs/specs/SPEC-0001-repo-foundation.md`
- `docs/specs/SPEC-0002-core-domain-model.md`
- `docs/specs/SPEC-0003-application-shell.md`

Only create specs that are clear enough to be useful.

Each spec must include:

- purpose
- scope
- non-goals
- requirements
- acceptance criteria
- dependencies
- approval class: A0, A1, A2, or A3
- automated gate
- human gate
- stop conditions

Prefer fewer, sharper specs over many speculative specs.

### 7. Create initial implementation plans

Create plan files only for specs that are sufficiently clear to implement.

Each plan must include:

- linked spec
- implementation objective
- expected files or directories to create/change
- implementation steps
- validation commands
- documentation updates
- local commit strategy
- risks
- stop conditions

Do not write plans for unclear specs. Instead, list the unresolved questions.

### 8. Propose execution batches

After specs and plans exist, group related plans into proposed batch files under:

- `docs/plans/batches/`

A batch is an execution grouping. It is not a replacement for specs or plans.

Each batch must include:

- included specs
- included plans
- approval class
- whether it is user-testable
- whether the agent may continue automatically
- automated gates
- human gates
- stop conditions
- final batch output

Use batches to group small, related plans so execution is less risky and requires fewer low-value human approvals.

Do not create a batch until the specs/plans it references exist or are being created in the same seeding pass.

### 9. Create the roadmap

Write `docs/roadmap.md`.

It should include:

- proposed implementation sequence
- dependency ordering between specs
- proposed batches
- approval class for each batch
- first human-testable checkpoint
- work that should not require human approval
- work that must require human approval

The roadmap should make clear which work is machine-verifiable and which work is human-verifiable.

### 10. Draft ADR only if justified

Create `docs/adr/ADR-0000-architecture-direction.md` only if the raw overview explicitly states or strongly implies real architecture decisions.

An ADR is justified for decisions such as:

- frontend framework
- backend framework
- database choice
- local-first vs server-backed architecture
- authentication model
- deployment model
- state management strategy
- major integration boundary

If architecture is not yet decided, do not invent it. Instead, record an ADR candidate or open question.

### 11. Write seeding traceability docs

Write:

- `docs/seed/SEED-0000-project-decomposition.md`
- `docs/seed/SEED-0000-results.md`
- `docs/worklog/0000-seeding-notes.md`

`SEED-0000-project-decomposition.md` should include:

- how the raw overview was decomposed
- document map
- spec map
- plan map
- batch map
- decomposition rationale

`SEED-0000-results.md` should include:

- created documents
- assumptions made
- open questions
- risks
- recommended next prompt
- whether the next step is planning, implementation, or human clarification

`0000-seeding-notes.md` should include:

- what was extracted from the raw overview
- what was excluded
- why items were deferred
- unresolved questions
- recommendations for the next agent session

## Approval Classes

Use these approval classes:

- A0: no human approval needed; continue if automated checks pass.
- A1: batch approval only; complete the batch, then summarize.
- A2: human checkpoint required before continuing.
- A3: hard approval required before taking the action.

During seeding, most documentation and scaffolding-preparation work should be A1.

Mark A2 when user judgment, UX judgment, physical testing, or product validation is required.

Mark A3 for dependencies, network access, secrets, deployment, destructive operations, or system-level changes.

## Rules

- Do not implement application code.
- Do not create production source files.
- Do not install dependencies.
- Do not access the network unless explicitly approved.
- Do not run framework generators.
- Do not invent architecture where the overview is silent.
- Do not turn brainstormed possibilities into committed requirements.
- Do not duplicate the raw overview into every document.
- Keep generated docs concise and useful.
- Mark open questions explicitly.
- Mark assumptions explicitly.
- Identify contradictions explicitly.
- Identify the smallest first implementation slice.
- Identify the first meaningful human-testable milestone.
- Create batches only after specs/plans exist.
- Do not ask for approval after each document.
- Stop only if a missing decision blocks useful decomposition.

## Stop Conditions

Stop and ask for human input only if:

- the raw overview contains contradictions that block decomposition
- the project cannot be decomposed without inventing core product behavior
- a major architecture choice is required but not specified or strongly implied
- implementation would need to begin before documents can be useful
- dependency installation is required
- network access is required
- files outside approved documentation paths must be modified

When stopping, ask one targeted question. Do not ask for generic approval.

## Final Response Format

After completing the skill, return only:

```md
SEEDING DONE

- Documents created/updated:
- Specs created:
- Plans created:
- Proposed batches:
- ADRs created or deferred:
- Key assumptions:
- Open questions:
- First implementation slice:
- First human-testable milestone:
- Recommended next prompt:
````

Do not include full document contents in the final response unless specifically requested.

```
```
