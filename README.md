# Agentic Coding Starter Kit

A reusable starter kit for running agentic software projects with stronger process control, cleaner documentation, safer permissions, and lower token waste.

This repository is not an application template. It is a **project operating system** for agent-assisted development.

It gives future agents a controlled way to move from:

```txt
raw project idea
  → seeded project docs
  → decomposed specs
  → implementation plans
  → execution batches
  → reviewed pull requests
```

The goal is to let agents work with useful autonomy while avoiding uncontrolled scope drift, noisy approvals, messy work trees, and undocumented implementation decisions.

---

## Who this is for

Use this starter kit when you want to:

- start a new software project from a large written product overview,
- use coding agents without giving them unrestricted YOLO access,
- keep specs, plans, decisions, and implementation work separate,
- reduce token usage by creating stable source-of-truth documents,
- avoid mid-implementation spec rewrites,
- group low-risk work into batches so the agent does not ask for pointless approvals,
- preserve human review for moments where human judgment actually matters.

This kit is especially useful for projects that will evolve through multiple implementation passes rather than one short coding session.

---

## Core idea

The central rule is:

> The agent may brainstorm, seed, specify, plan, implement, or review — but it should not do all of those at once.

The repo is organized around explicit operating modes:

| Mode | Purpose | Writes code? |
|---|---|---|
| Project Seeding | Convert a raw overview into controlled project docs | No |
| Discovery | Inspect and understand the repo | No |
| Spec | Define what must be true | No |
| Plan | Define how to implement an accepted spec | No |
| Batch Planning | Group already-written specs/plans for execution | No |
| Implementation | Edit code according to an accepted plan or batch | Yes |
| Review | Check the diff against the accepted contract | No |

---

## Important distinction: governance scaffold vs application scaffold

This starter kit provides a **governance scaffold**.

That means it gives you:

```txt
AGENTS.md
docs/
spec templates
plan templates
batch templates
ADR templates
prompt library
sandbox policy
approval policy
workflow rules
```

It does **not** automatically create your actual application structure, such as:

```txt
backend/
frontend/
shared/
tests/
package.json
pyproject.toml
Dockerfile
database/
mobile/
```

That application scaffold should be created by the first implementation spec/plan in the real project, usually:

```txt
docs/specs/SPEC-0001-application-scaffold.md
docs/plans/PLAN-0001-application-scaffold.md
docs/plans/batches/BATCH-0001-application-scaffold.md
```

The application scaffold should define backend/frontend/shared structure, local commands, prerequisite tools, environment policy, dependency manifests, and test/lint/build command surfaces.

---

## Repository layout

A typical starter-kit layout should look like this:

```txt
.
├── AGENTS.md
├── README.md
├── START_HERE.md
├── AGENTIC_CODING_GUIDELINES.md
├── PROMPT_LIBRARY.md
├── BOUNDARY_AND_SANDBOX_POLICY.md
├── LARGE_SPEC_SEEDING_PLAYBOOK.md
├── docs/
│   ├── intake/
│   │   └── PROJECT_OVERVIEW_RAW.md
│   ├── seed/
│   ├── specs/
│   │   └── _template.md
│   ├── plans/
│   │   ├── _template.md
│   │   └── batches/
│   │       └── _template.md
│   ├── adr/
│   │   └── _template.md
│   ├── worklog/
│   ├── standards/
│   └── setup/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
├── .githooks/
└── scripts/
```

Not every real project needs every file forever, but the structure is designed so agents can quickly find the right source of truth.

---

## Quick start for a new project

### 1. Create a new repo

Create your new GitHub/local repo normally.

Then copy the starter kit files into the new repo.

Recommended minimum:

```txt
AGENTS.md
README.md
docs/
.github/
.githooks/
scripts/
```

### 2. Add your raw project overview

Paste the large founding overview into:

```txt
docs/intake/PROJECT_OVERVIEW_RAW.md
```

This file is treated as an intake artifact.

It is allowed to be long, messy, exploratory, and comprehensive.

Future agents should not keep rereading it every session. The seeding process extracts durable source-of-truth docs from it.

### 3. Run the seeding prompt

Use the seeding prompt from:

```txt
PROMPT_LIBRARY.md
```

or the large-spec seeding skill if your agent system supports skills.

The seeding pass should create the controlled project starting point:

```txt
docs/project-charter.md
docs/glossary.md
docs/repo-map.md
docs/roadmap.md
docs/specs/SPEC-0000-project-foundation.md
docs/specs/SPEC-0001-application-scaffold.md
docs/plans/PLAN-0001-application-scaffold.md
docs/plans/batches/BATCH-0001-application-scaffold.md
docs/seed/SEED-0000-project-decomposition.md
docs/seed/SEED-0000-results.md
docs/worklog/0000-seeding-notes.md
```

It may also create:

```txt
docs/adr/ADR-0000-architecture-direction.md
```

only if the raw overview explicitly or strongly implies architecture choices.

### 4. Review the seeded documents

Before implementation, run a review-only pass.

The agent should check:

- Are the specs implementation-safe?
- Are the first plans small enough?
- Are the proposed batches reasonable?
- Is the first human-testable milestone identified?
- Are approval classes correct?
- Are assumptions and open questions visible?

Do not start coding until the first implementation batch is clear.

### 5. Execute the first application scaffold batch

The first implementation batch should usually be:

```txt
docs/plans/batches/BATCH-0001-application-scaffold.md
```

This creates the actual project skeleton.

It may create files and directories such as:

```txt
backend/
frontend/
shared/
tests/
.env.example
Makefile
README.md
docs/setup/local-prerequisites.md
```

It should not implement real product behavior yet.

---

## Document maturity levels

Use maturity levels to prevent overplanning.

| Level | Meaning |
|---|---|
| M0 | Intake: raw unprocessed material |
| M1 | Seeded: extracted into controlled docs |
| M2 | Specified: requirements and acceptance criteria are clear |
| M3 | Planned: implementation steps and validation are clear |
| M4 | Executable: safe for agent implementation |
| M5 | Validated: implemented and checked |

During seeding:

- `docs/project-charter.md` should reach M1/M2.
- `docs/specs/SPEC-0000-project-foundation.md` should reach M1/M2.
- The first 1–3 implementation specs should reach M2.
- The first 1–3 matching plans should reach M3/M4.
- Future work should remain in `docs/roadmap.md` as roadmap items, spec candidates, ADR candidates, open questions, or deferred decisions.

Do not create 20 fully detailed specs and plans from the raw overview unless the early implementation path is unusually clear.

---

## Specs, plans, and batches

### Spec

A spec defines **what must be true**.

Specs belong in:

```txt
docs/specs/
```

Example:

```txt
docs/specs/SPEC-0001-application-scaffold.md
```

A spec should include:

- purpose,
- scope,
- non-goals,
- requirements,
- acceptance criteria,
- dependencies,
- approval class,
- automated gate,
- human gate,
- stop conditions.

### Plan

A plan defines **how to implement one accepted spec**.

Plans belong in:

```txt
docs/plans/
```

Example:

```txt
docs/plans/PLAN-0001-application-scaffold.md
```

A plan should include:

- linked spec,
- expected file changes,
- implementation steps,
- validation commands,
- documentation updates,
- local commit strategy,
- risks,
- stop conditions.

### Batch

A batch defines **which already-written specs/plans may be executed together**.

Batches belong in:

```txt
docs/plans/batches/
```

Example:

```txt
docs/plans/batches/BATCH-0001-application-scaffold.md
```

A batch should not define the project from scratch.

It should group related specs/plans so the agent can safely continue through low-risk work without asking for human approval after every small step.

---

## Approval classes

Every meaningful spec, plan, or batch should declare an approval class.

| Class | Meaning | Agent behavior |
|---|---|---|
| A0 | No human approval needed | Continue if checks pass |
| A1 | Batch approval only | Complete the batch, then summarize |
| A2 | Human checkpoint required | Stop when human judgment adds value |
| A3 | Hard approval required | Ask before taking action |

Examples:

| Work | Typical class |
|---|---|
| Documentation cleanup | A0 |
| Repo/application scaffold | A1 |
| Core non-user-testable backend scaffolding | A1 |
| First usable UI flow | A2 |
| Physical hardware test point | A2 |
| Dependency install | A3 |
| Network access | A3 |
| Deployment | A3 |
| Secrets/API keys | A3 |

The agent should not ask for approval just because a local commit, spec, or plan is complete.

It should stop only when human judgment changes the outcome.

---

## Permission and sandbox policy

The recommended default is:

```txt
Inside the repo: mostly autonomous.
Outside the repo: no.
Internet: ask.
Dependencies: ask.
Secrets/system: never.
Git local: yes.
Git remote: ask.
```

Agents may generally perform:

```txt
read/edit files inside repo
create files/directories inside repo
run tests/lint/typecheck/build
run git status/diff/add/commit
```

Agents must ask before:

```txt
installing dependencies
using network access
changing lockfiles
running destructive commands
pushing branches
creating PRs
modifying CI/CD
touching deployment files
```

Agents must not:

```txt
use sudo
install global packages
read secrets
write outside the repo
touch OS settings
control other applications
use curl | bash
```

If approval is required, the request should include:

```txt
Action:
Exact command:
Why needed:
Scope:
Risk:
Fallback if denied:
```

Vague approval requests should be denied.

---

## Token optimization strategy

This kit reduces token usage by moving repeated context into stable files.

The agent should normally read:

```txt
AGENTS.md
docs/repo-map.md
active spec
active plan or batch
directly relevant source files
```

The agent should not repeatedly load:

```txt
the full raw project overview
all specs
all plans
all worklogs
entire source tree
```

Use this hierarchy:

```txt
L0 — Always:
AGENTS.md, current user instruction

L1 — Serious task:
docs/repo-map.md, active spec, active plan or batch

L2 — Only as needed:
relevant source files, tests, and implementation docs
```

Use bare output during implementation:

```txt
Mode: Implementation.
Output style: bare engineering.

Do not narrate routine steps.
Only report blockers, change requests, test failures, or final summary.
```

Do not use bare output during seeding, planning, or review, where reasoning needs to be visible.

---

## How to maintain the real project README.md

Every real project built from this kit should have its own root `README.md`.

That README is not the same as this starter-kit README.

The real project README should explain the application, not the agent process.

### Real project README responsibilities

A real project README should include:

```txt
project name
short description
current status
tech stack
repo layout
prerequisites
setup instructions
environment variables
local development commands
test/lint/build commands
how to run the app
known limitations
links to key docs
```

### Recommended real project README structure

```md
# Project Name

Brief description of what the project does.

## Status

Current maturity:
- Prototype / MVP / Active development / Production
- Current milestone
- First human-testable flow, if applicable

## Tech Stack

- Frontend:
- Backend:
- Database:
- Mobile:
- Infrastructure:
- Package manager:

## Prerequisites

List required local tools.

Example:

- Node.js:
- Python:
- Docker:
- GitHub CLI:
- Xcode / Android Studio:
- Database:

## Setup

```bash
# install dependencies
# copy env file
# run setup commands
```

## Environment Variables

Use `.env.example` as the source of truth.

| Variable | Required | Purpose |
|---|---|---|
| `EXAMPLE_VAR` | Yes | Example only |

Never commit real secrets.

## Local Development

```bash
# start backend
# start frontend
# run full app
```

## Tests and Checks

```bash
# test
# lint
# typecheck
# build
```

## Repo Layout

```txt
backend/
frontend/
shared/
docs/
tests/
```

## Agent Workflow

This project uses controlled agentic development.

Agents should read:

1. `AGENTS.md`
2. `docs/repo-map.md`
3. the active spec
4. the active plan or batch

Agents should not use `docs/intake/PROJECT_OVERVIEW_RAW.md` as the normal working spec.

## Key Project Docs

- `docs/project-charter.md`
- `docs/specs/SPEC-0000-project-foundation.md`
- `docs/roadmap.md`
- `docs/repo-map.md`
- `docs/adr/`
- `docs/plans/batches/`

## Current Milestone

Describe the current implementation target.

## Known Limitations

List anything intentionally not built yet.
```

### When agents should update the real project README

The README should be updated when:

- setup commands change,
- prerequisites change,
- environment variables change,
- repo structure changes,
- run/test/build commands change,
- the project status changes,
- the first human-testable flow changes,
- deployment or installation instructions change.

The README should not be updated for every small internal refactor.

### README update rule for agents

Add this to project instructions:

```txt
If implementation changes how a developer installs, runs, tests, configures, or understands the project structure, update README.md in the same plan or open a Change Request explaining why the README update is needed.
```

---

## Recommended first agent session

After copying this kit into a new repo and adding `PROJECT_OVERVIEW_RAW.md`, use:

```txt
Mode: Project Seeding / Spec Decomposition.

Read:
1. AGENTS.md
2. docs/intake/PROJECT_OVERVIEW_RAW.md

Do not write application code.
Do not create production application files.
Do not install dependencies.
Do not access the network.
Do not run framework generators.

Goal:
Convert the raw project overview into controlled project documents, decomposed specs, decomposed plans, and proposed execution batches.

Important distinction:
This is not batch execution.
This is repo seeding and project decomposition.

The purpose is to create the starting point that future batch execution will use.

Output:
- project charter
- glossary
- repo map
- roadmap
- foundation spec
- first 1–3 implementation specs
- first 1–3 implementation plans
- first 1–2 proposed batches
- seeding notes
- ADR only if justified

Depth policy:
Be broad but shallow across the whole project.
Be deep only for the first implementation-safe slices.
Do not fully specify or plan the entire project from the raw overview.
```

---

## Recommended second agent session

After seeding, run review:

```txt
Mode: Review only.

Read:
1. AGENTS.md
2. docs/seed/SEED-0000-results.md
3. docs/roadmap.md
4. docs/specs/SPEC-0000-project-foundation.md
5. docs/plans/batches/BATCH-0001-*.md

Review the seeded project control documents.

Do not write code.
Do not install dependencies.

Check:
1. Are the specs decomposed into implementation-safe chunks?
2. Are the plans small enough to execute safely?
3. Are the proposed batches grouped correctly?
4. Are any batches too broad?
5. Is the first human-testable milestone clearly identified?
6. Are approval classes assigned correctly?
7. Are there missing docs before implementation should begin?

Return:
- blocking issues
- non-blocking improvements
- recommended edits
- whether BATCH-0001 is ready for execution
```

---

## Recommended third agent session

Execute the first application scaffold batch:

```txt
Mode: Batch Implementation.

Read:
1. AGENTS.md
2. docs/repo-map.md
3. docs/plans/batches/BATCH-0001-application-scaffold.md
4. all specs and plans referenced by the batch

Execute only the accepted batch.

Continue automatically through A0/A1 work.

Stop only if:
- an A2 human checkpoint is reached,
- an A3 approval is required,
- automated checks fail and cannot be fixed within accepted scope,
- a Change Request is required,
- scope expands beyond the batch.
```

---

## What agents should not do

Agents should not:

- treat the raw overview as the permanent spec,
- implement code during seeding,
- create 20 detailed specs/plans from the initial overview,
- ask for approval after every local commit,
- silently change accepted specs during implementation,
- install dependencies without approval,
- use network access without approval,
- modify files outside the repo,
- create late-stage plans before early implementation has validated the foundation.

---

## Change Requests

If implementation reveals that an accepted spec or plan is wrong, the agent should stop and open a Change Request.

A Change Request should include:

```md
# Change Request: CR-0001

## Trigger

What did implementation reveal?

## Current accepted spec says

What requirement or assumption is affected?

## Proposed change

What should change?

## Why this is necessary

Why can’t the current plan complete cleanly?

## Impact

- Scope:
- Files:
- Tests:
- Docs:
- Risks:
- Token/context impact:

## Recommendation

Accept / Reject / Defer
```

The agent should not silently modify the spec and keep coding.

---

## Pull request expectations

A pull request should represent a meaningful review unit.

Do not require a PR after every small spec if the work is still non-user-testable scaffolding.

Use PRs for:

- completed scaffold batch,
- first user-testable milestone,
- architecture slice,
- CI-clean foundation,
- deployable increment,
- human-review checkpoint.

Every PR should include:

```txt
summary
linked specs/plans/batches
tests run
docs updated
risks
deviations
screenshots or manual test notes if user-facing
```

---

## How to evolve this kit

This starter kit should remain small and process-focused.

Good changes:

- improve templates,
- clarify approval classes,
- add stack-specific examples,
- add better hooks,
- improve prompt library,
- refine sandbox rules.

Bad changes:

- adding product-specific implementation details,
- turning the starter kit into a framework template,
- making every possible tool mandatory,
- growing AGENTS.md into a giant manual,
- creating rules that force human approval when no human judgment is needed.

When you discover a better practice in a real project, extract the general rule back into this starter kit only if it will help future projects too.

---

## Summary

Use this kit to create controlled momentum.

The raw overview preserves the full vision.

The seeding pass creates the first stable project control layer.

Specs define what must be true.

Plans define how to implement.

Batches define when the agent may continue without low-value human approvals.

Change Requests prevent silent scope drift.

The README keeps humans oriented.

The result is agentic development that is faster, cleaner, safer, and easier to review.
