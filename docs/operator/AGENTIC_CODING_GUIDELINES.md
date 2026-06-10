# Agentic Coding Guidelines for Structured, Token-Efficient Work

## Operating thesis

Your prior failure mode was allowing the agent to mutate the **spec**, **plan**, and **implementation** in one continuous stream. The fix is not less AI usage. The fix is **controlled agentic development**:

```txt
Discovery → Spec → Spec acceptance → Plan → Plan acceptance → Implementation → Review → PR
```

The agent may be fast, but the workflow must be boring, auditable, and recoverable.

## Non-negotiable rules

1. **No implementation before an accepted spec and accepted plan** for non-trivial work.
2. **No spec mutation during implementation.** If the spec is wrong, stop and create a Change Request.
3. **No dirty-tree coding.** Start from a clean working tree or a dedicated worktree.
4. **No silent dependency additions.** New production dependencies require explicit approval and a dependency rationale.
5. **No network downloads by default.** The agent may propose exact commands; it may not fetch arbitrary internet content, pipe remote scripts into a shell, or install packages without approval.
6. **No direct pushes to protected branches.** GitHub is the source of truth. The agent may push task branches and open PRs; humans approve merges.
7. **No broad repo scans unless in Discovery mode.** Implementation mode reads only the accepted spec, accepted plan, repo map, affected files, and nearby tests.
8. **No verbose narration in implementation mode.** Use bare status updates and final summaries.

## The five operating modes

### 1. Discovery mode

Use when the relevant files, architecture, or constraints are unclear.

Allowed:

- Read repository instructions.
- Inspect relevant directories.
- Search with `rg`, file tree commands, and existing docs.
- Produce findings, risks, and recommended next mode.

Forbidden:

- Editing code.
- Writing an implementation plan.
- Installing dependencies.
- Changing the spec.

Prompt:

```txt
Mode: Discovery only.
Read AGENTS.md first.
Do not edit files.
Do not write a plan yet.

Task:
[task]

Return:
1. Relevant files and why they matter.
2. Existing patterns to follow.
3. Risks and unknowns.
4. Whether this needs a spec, ADR, or direct implementation.
5. Recommended next mode.
```

### 2. Spec mode

Use when the desired behavior, constraints, or acceptance criteria need to be made explicit.

Allowed:

- Create or revise files in `docs/specs/`.
- Ask precise questions if genuinely blocking.
- Extract requirements from a large overview document.

Forbidden:

- Writing code.
- Creating implementation steps beyond high-level constraints.
- Expanding scope beyond the project intent.

Prompt:

```txt
Mode: Spec only.
Use docs/specs/_template.md.
Do not write code.
Do not write an implementation plan.

Inputs:
- docs/intake/PROJECT_OVERVIEW_RAW.md
- docs/project-charter.md if present
- docs/repo-map.md if present

Produce:
1. A concise SPEC file with goals, non-goals, behavior, constraints, acceptance criteria, and open questions.
2. A list of scope boundaries.
3. A recommendation on whether an ADR is required.
```

### 3. Plan mode

Use after accepting a spec.

Allowed:

- Create or revise files in `docs/plans/`.
- Identify files likely to change.
- Identify tests and docs to update.
- Identify rollback and stop conditions.

Forbidden:

- Editing application code.
- Changing the accepted spec.
- Adding work outside accepted scope.

Prompt:

```txt
Mode: Plan only.
Use the accepted spec below.
Do not edit code.
Do not change the spec.

Return:
1. File change list.
2. Step-by-step implementation tasks.
3. Test plan.
4. Documentation plan.
5. Risks.
6. Stop conditions that require a Change Request.
```

### 4. Implementation mode

Use only after plan acceptance.

Allowed:

- Edit files listed in the accepted plan.
- Add or update tests listed in the plan.
- Run local checks.
- Commit atomic changes on the task branch/worktree.

Forbidden:

- Editing the accepted spec.
- Expanding scope.
- Installing new dependencies without approval.
- Network access unless explicitly approved.
- Mutating host/global config.
- Direct push to `main`, `master`, `prod`, `production`, or release branches.

Bare output contract:

```txt
During implementation, do not narrate every step.
Only report:
- BLOCKED: when a decision/approval is needed.
- CR REQUIRED: when the spec or plan is wrong.
- CHECK FAILED: when a verification command fails.
- DONE: final summary, files changed, tests run, deviations, risks.
```

### 5. Review mode

Use after implementation.

Allowed:

- Inspect diff.
- Compare implementation to accepted spec and plan.
- Run tests, lint, typecheck, build.
- Create review notes.

Forbidden:

- Opportunistic refactors.
- Expanding feature scope.
- Hiding skipped tests.

Prompt:

```txt
Mode: Review only.
Review the current diff against the accepted spec and plan.

Check:
1. Every acceptance criterion.
2. Unplanned files.
3. Broad or risky changes.
4. Test adequacy.
5. Docs updates.
6. Security/dependency risk.
7. Naming, module boundaries, dead code, duplication.

Return:
- Pass/fail.
- Blocking issues.
- Non-blocking improvements.
- Tests run.
- Recommended commit/PR summary.
```

## Change control

During implementation, if the plan or spec is wrong, do not say “just update it and keep going.” Say:

```txt
Stop implementation.
Open a Change Request using docs/change-requests/_template.md.
Explain what assumption failed, what must change, scope impact, file impact, test impact, docs impact, and whether this belongs in the current task or a separate task.
Do not edit code until the Change Request is accepted.
```

## Token optimization rules

### Keep persistent instructions short

`AGENTS.md` should contain stable rules and commands, not essays. Specialized workflows belong in skills, prompt files, or docs that are loaded only when needed.

### Use context tiers

```txt
L0: Always loaded
- AGENTS.md
- Current user request

L1: Serious task
- docs/repo-map.md
- active SPEC
- active PLAN

L2: Only when needed
- directly affected source files
- directly affected tests
- relevant ADRs
```

### Prefer references over pasted history

Bad:

```txt
Here is everything we discussed yesterday...
[paste 20,000 tokens]
```

Good:

```txt
Read AGENTS.md, docs/repo-map.md, docs/specs/SPEC-0003-auth.md, and docs/plans/PLAN-0003-auth.md.
Operate in Implementation mode only.
```

### Use large-spec seeding once

Your large project overview should become a durable source document, not something pasted into every coding session. Put it at:

```txt
docs/intake/PROJECT_OVERVIEW_RAW.md
```

Then run the seeding prompt in:

```txt
docs/intake/SEEDING_PROMPT.md
```

The agent should extract:

```txt
docs/project-charter.md
docs/repo-map.md
docs/specs/SPEC-0000-project-foundation.md
docs/plans/PLAN-0000-repo-bootstrap.md
docs/adr/ADR-0000-architecture-direction.md
docs/worklog/0000-seeding-notes.md
```

Do not use the raw overview as routine implementation context after seeding.

### Use bare output during implementation

Verbose explanation is valuable in Discovery, Spec, Plan, and Review. It is expensive and often counterproductive during implementation. In implementation mode, require terse status updates and a structured final summary.

### Move specialized instructions to skills

If a workflow is used sometimes but not every session, put it in `.agents/skills/<skill-name>/SKILL.md` instead of bloating `AGENTS.md`.

Examples:

```txt
.agents/skills/large-spec-seeding/SKILL.md
.agents/skills/token-triage/SKILL.md
.agents/skills/pr-review-gate/SKILL.md
```

## Bounded autonomy policy

### Safe by default

The agent may do these without repeated approval inside its worktree:

```txt
git status
git diff
git add <planned files>
git commit -m <message>
git branch
git switch
git checkout -b
git worktree list
rg / grep-like local search
ls / find local project files
run documented test/lint/typecheck/build commands
edit files inside accepted plan
```

### Ask first

The agent must ask before:

```txt
network access
package install/update/add/remove
downloading binaries or scripts
running curl/wget/http clients
running docker with network or host mounts
changing CI, auth, deployment, billing, or infra config
schema migrations
secret handling
pushing a branch for the first time
opening a PR
modifying files outside the accepted plan
```

### Deny outright

The agent must not:

```txt
pipe remote content into a shell
use sudo or privilege escalation
change shell startup files
read .env or secret files unless explicitly asked
write outside the repo/worktree
push directly to protected branches
force-push without explicit approval
disable security checks, hooks, or CI to make a task pass
install globally on the host machine
```

## GitHub source-of-truth model

Use GitHub as the final gate:

```txt
Local/worktree agent autonomy → task branch → PR → CI checks → human review → merge
```

The agent can be trusted to work inside a bounded branch. It should not be trusted to merge itself.

## New repo setup checklist

1. Copy `starter-repo/` into the repo root.
2. Install local Git hooks: `scripts/agent/install_git_hooks.sh`.
3. Commit the process scaffold.
4. Paste the large raw project overview into `docs/intake/PROJECT_OVERVIEW_RAW.md`.
5. Run the seeding prompt in Spec mode only.
6. Review generated docs.
7. Accept the first spec and plan.
8. Create the first worktree with `scripts/agent/new_agent_task.sh`.
9. Run implementation mode.
10. Open PR and require CI/human approval before merge.
