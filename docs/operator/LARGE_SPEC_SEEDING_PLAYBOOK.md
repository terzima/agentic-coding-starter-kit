# Large Spec Seeding Playbook

## Problem

You already have a large, detailed project overview written outside the controlled repo process. That document is valuable, but it is too large to feed into every implementation session.

The correct move is to treat it as **source material**, not the canonical working spec.

## Target structure

```txt
docs/intake/PROJECT_OVERVIEW_RAW.md       # original large overview, mostly immutable
docs/project-charter.md                   # stable summary of what the project is
docs/glossary.md                          # domain language
docs/repo-map.md                          # updated as repo appears
docs/specs/SPEC-0000-project-foundation.md
docs/specs/SPEC-0001-first-slice.md
docs/plans/PLAN-0000-repo-bootstrap.md
docs/plans/PLAN-0001-first-slice.md
docs/adr/ADR-0000-architecture-direction.md
docs/worklog/0000-seeding-notes.md
```

## Seed once, then stop pasting the raw overview

After seeding, normal implementation sessions should reference:

```txt
AGENTS.md
docs/project-charter.md
docs/repo-map.md
active SPEC
active PLAN
```

The raw overview should only be revisited when resolving ambiguity.

## Seeding process

### Pass 1 — Extraction

Ask the agent to extract the project from the raw overview without coding.

Output:

```txt
project purpose
actors/users
core user journeys
data objects
external integrations
non-functional requirements
explicit non-goals
open questions
risk register
```

### Pass 2 — Canonical docs

Ask the agent to write:

```txt
docs/project-charter.md
docs/glossary.md
docs/specs/SPEC-0000-project-foundation.md
```

### Pass 3 — Architecture decision candidates

Ask the agent to identify decisions that need ADRs:

```txt
frontend framework
backend/runtime
database
auth
deployment
queue/background jobs
state management
API style
observability
```

Only write ADRs for decisions that truly constrain future work.

### Pass 4 — Slice the work

Ask the agent to decompose the project into slices:

```txt
Slice 0: repo bootstrap and tooling
Slice 1: smallest end-to-end happy path
Slice 2: persistence
Slice 3: auth
Slice 4: edge cases / admin / scaling
```

Avoid starting with the full system.

### Pass 5 — First implementation plan

Produce only the first plan:

```txt
docs/plans/PLAN-0000-repo-bootstrap.md
```

Do not generate plans for the entire project. Future plans should be created when the prior slice is complete.

## Prompt

Use the exact prompt in:

```txt
docs/intake/SEEDING_PROMPT.md
```

## Acceptance checklist for seeded docs

Before implementation starts, verify:

- The project charter is under 2 pages.
- The first spec has concrete acceptance criteria.
- The first plan is small enough to complete in one PR.
- There is a glossary if domain terms matter.
- ADRs are drafted only for real decisions.
- Non-goals are explicit.
- Open questions are listed instead of hidden in vague prose.
- The raw overview is archived as source material, not repeatedly pasted.
