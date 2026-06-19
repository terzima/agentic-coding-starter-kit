# Agentic Workflow Manual

## What This Framework Is

This framework keeps agentic development reviewable and resumable. It turns large, uncertain work into a controlled sequence:

```txt
Discovery -> Spike -> Spec -> Plan -> Implementation -> Review -> Commit/PR
```

`AGENTS.md` is the canonical operating contract. This manual is the human-facing guide: what to copy, what to paste, when to stop, and how to keep the next session from relying on chat history.

The main habit is simple: use durable repo files instead of memory. Specs say what must be true. Plans say exactly how to implement accepted specs. Worklogs hold narrative evidence. Handoffs hold restart-critical state. `docs/status/CURRENT_STATE.md` stays compact.

## What To Copy Into A New Project

For a fresh project, start with `framework-kit/`. Its README gives the startup sequence, `framework-kit/MANIFEST.md` names the exact source paths to copy, and `framework-kit/verify_framework_kit.py` checks that the kit still matches the repo.

Required core files:

- `AGENTS.md`
- `agent-adapters.md`
- `.agents/skills/controlled-planning-docs/SKILL.md`
- `.agents/skills/controlled-planning-docs/references/spec-writing.md`
- `.agents/skills/controlled-planning-docs/references/plan-hardening.md`
- `.agents/skills/controlled-planning-docs/references/batch-writing.md`
- `.agents/skills/accepted-plan-implementation/SKILL.md`
- `.agents/skills/change-request-control/SKILL.md`
- `.agents/skills/completion-review-gate/SKILL.md`
- `.agents/skills/controlled-agentic-development/SKILL.md`
- `.agents/skills/project-intake-seeding/SKILL.md`
- `.agents/skills/spec-plan-alignment/SKILL.md`
- `.agents/skills/spike-research/SKILL.md`
- `.agents/skills/token-triage/SKILL.md`
- `docs/AGENTIC_WORKFLOW_MANUAL.md`
- `docs/specs/_template.md`
- `docs/plans/_template.md`
- `docs/plans/batches/_template.md`
- `docs/change-requests/_template.md`
- `docs/status/_template.md`
- `docs/handoff/_template.md`
- `docs/worklog/_template.md`
- `scripts/agent/`
- `.githooks/`

Optional intake/seeding files:

- `docs/intake/SEEDING_PROMPT.md`, or the `Seed Project From Intake` prompt in this manual.
- `docs/intake/PROJECT_OVERVIEW_RAW.md`, created fresh in the new project and filled with the user's own project overview.

Optional tool adapters:

- `.codex/`
- `.claude/`
- `.cursor/`

Adapter setup, generated-cache guidance, and current-repo adapter status live in `agent-adapters.md`. Use that file instead of adding separate adapter READMEs.

Root-file ownership guidance lives in `docs/operator/repo-root-files.md`. Use it before copying root files into a new project.

Optional GitHub policy and CI files:

- `.github/pull_request_template.md`
- `.github/workflows/ci.yml`
- `.github/workflows/dependency-review.yml`

GitHub policy files are copied but inactive until repository settings are configured. When using the dependency review workflow, enable GitHub Dependency Graph before restoring pull-request triggers or expecting dependency-review checks to pass.

Fresh-project setup sequence:

1. Copy the required core files and any adapters you actually use.
2. Review `AGENTS.md` and remove rules that do not match your project.
3. Run `python3 framework-kit/verify_framework_kit.py`.
4. Use `agent-adapters.md` to decide which adapters are `native-active`, `manual-setup-required`, `optional-remote`, `copied-inert`, or `future-spike`.
5. Install repo-local hooks with `bash scripts/agent/install_git_hooks.sh` only when you want local Git enforcement active.
6. Use `project-intake-seeding` to create or seed `docs/project-charter.md`, `docs/roadmap.md`, `docs/glossary.md`, and `docs/repo-map.md`.
7. Use `spike-research` for bounded unknowns before writing specs.
8. Start the first task in Discovery or Spec mode.

If you already have a long product overview, use the intake/seeding process before writing normal specs. Seeding is broad but shallow: it turns raw overview material into starter project docs, a foundation spec, one to three initial specs/plans, and one or two proposed batches. It should not write product code or fully plan the entire project.

Detailed writing guidance lives in `.agents/skills/controlled-planning-docs/references/`. Keep those reference files when copying the framework; they are the practical instructions behind the concise templates.

For approved implementation work, use the short implementation skill prompt instead of pasting the long implementation prompt each time:

```txt
Mode: Implementation.

Use the repo-local accepted-plan-implementation skill.

Execute [PLAN path] exactly.
```

## What Not To Copy

Do not copy historical or product-specific context from another project unless you intentionally adapt it:

- historical `docs/specs/SPEC-*.md`
- historical `docs/plans/PLAN-*.md`
- historical `docs/plans/batches/BATCH-*.md`
- historical `docs/change-requests/CR-*.md`
- historical `docs/worklog/*.md`
- historical `docs/handoff/*.md`
- product docs such as `docs/project-charter.md`, `docs/roadmap.md`, `docs/glossary.md`, and `docs/repo-map.md`
- product source, tests, intake files, generated files, caches, local artifacts, and package manifests unless the new project actually uses them

Do not copy local scratch directories or tool caches. Classify them first, then decide.

## Quick Command Index

Use these short labels in your notes, then paste the matching full prompt from the next section.

| Label | Use when | Full prompt |
|---|---|---|
| `Start Session` | A new agent session needs repo state. | `Full Paste-Ready Prompts` -> `Start Session` |
| `Discovery` | You need a read-only answer or file map. | `Full Paste-Ready Prompts` -> `Discovery` |
| `Spike` | You need bounded evidence before changing specs/plans. | `Full Paste-Ready Prompts` -> `Spike` |
| `Seed Project From Intake` | You have a new project idea, existing repo, or raw overview and need starter docs. | `Full Paste-Ready Prompts` -> `Seed Project From Intake` |
| `Create Spec` | Durable requirements are needed. | `Full Paste-Ready Prompts` -> `Create Spec` |
| `Approve Spec` | A spec is approved and needs status updated. | `Full Paste-Ready Prompts` -> `Approve Spec` |
| `Create Plan` | An accepted spec needs an M4 implementation plan. | `Full Paste-Ready Prompts` -> `Create Plan` |
| `Approve Plan` | A plan is approved and needs status updated. | `Full Paste-Ready Prompts` -> `Approve Plan` |
| `Execute Plan` | An accepted plan should be implemented. | `Full Paste-Ready Prompts` -> `Execute Plan` |
| `Review` | Diff or docs need readiness review. | `Full Paste-Ready Prompts` -> `Review` |
| `Open Change Request` | Implementation reveals accepted scope is wrong. | `Full Paste-Ready Prompts` -> `Open Change Request` |
| `Commit Work` | Current worktree should be committed locally. | `Full Paste-Ready Prompts` -> `Commit Work` |

Spec, Plan, Implementation, and Review final responses should include the next exact prompt when the next step is clear. If the next step requires human judgment, the response should say what the human must decide first.

## Workflow

Discovery is read-only. It answers what exists, what is risky, and what mode should come next.

Spike is bounded research. It has a question, allowed scope, evidence target, budget or kill criteria, output destination, and promotion rule. A spike result is not accepted implementation behavior until a spec or plan captures it.

Seeding is a one-time startup path for projects that begin with a large raw overview. It extracts durable project docs, initial specs/plans, and proposed batches. After seeding, normal sessions should use `AGENTS.md`, `docs/repo-map.md`, `docs/status/CURRENT_STATE.md`, and active specs/plans instead of rereading raw intake.

Spec mode writes or revises requirements. It should define goals, non-goals, behavioral contracts, interfaces, validation, open questions, and stop conditions.

Plan mode turns an accepted spec into executable implementation steps. An M4 plan names files, functions, fixtures, commands, expected outputs, docs updates, rollback, risks, and stop conditions.

Implementation edits only according to an accepted plan. If accepted scope is wrong, stop and open a Change Request.

Review inspects readiness or implementation quality. Findings lead. Summaries stay secondary.

Commits are local by default. Pushes and PRs require explicit approval.

## Full Paste-Ready Prompts

### Start Session

```txt
Mode: Discovery.

We are in `[repo path]`.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. The active spec, plan, and batch listed in `docs/status/CURRENT_STATE.md`

Do not edit files.
Do not install dependencies.
Do not access the network.

Goal:
Summarize the current repo state and identify the next safest action.

Return:
- Active objective
- Active spec/plan/batch
- Current branch and worktree status
- Blocking gates or approvals
- Recommended next prompt
```

Next prompt: use `Discovery`, `Create Spec`, `Create Plan`, `Execute Plan`, or `Review` based on the returned next action.

### Discovery

```txt
Mode: Discovery.

We are in `[repo path]`.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. Any active docs named in `docs/status/CURRENT_STATE.md` that are relevant to this task

Do not edit files.
Do not write code.
Do not install dependencies.
Do not access the network.

Task:
[Describe the question or area to inspect.]

Return:
- Relevant files and why they matter
- Existing patterns to follow
- Risks and unknowns
- Whether this needs Discovery, Spike, Spec, Plan, Implementation, Review, ADR, or Change Request mode
- Recommended next prompt
```

Next prompt: if the answer is uncertain but bounded evidence would help, use `Spike`; if behavior is clear, use `Create Spec` or `Create Plan`.

### Spike

```txt
Mode: Spike.

We are in `[repo path]`.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. The active spec/plan if relevant

Do not ship behavior.
Do not edit accepted specs or plans unless explicitly asked.
Do not install dependencies or access the network.

Question or hypothesis:
[State the uncertainty.]

Allowed files or surfaces:
- [paths or areas]

Evidence to collect:
- [measurements, traces, prototypes, comparisons, or failures]

Budget and kill criteria:
- [time, token, attempt, or command limit]
- Stop if [condition]

Output destination:
- `docs/worklog/[date]-[topic].md` or a concise response

Promotion rule:
Only promote spike findings into implementation after they are captured in an accepted spec or plan.

Return:
- Evidence gathered
- Failed approaches
- Recommendation
- Whether to update a spec, plan, Change Request, or worklog
- Exact next prompt
```

Next prompt: usually `Open Change Request`, `Create Spec`, or `Create Plan`.

### Seed Project From Intake

```txt
Mode: Spec.

We are in `[repo path]`.

Use the repo-local `project-intake-seeding` skill.

Goal:
Seed a new project from a raw overview into durable repo docs, initial specs, initial plans, and proposed batches.

Read:
1. `AGENTS.md`
2. `.agents/skills/project-intake-seeding/SKILL.md`
3. The raw intake file or project notes supplied by the owner
4. Existing templates under `docs/specs/`, `docs/plans/`, `docs/plans/batches/`, `docs/status/`, and `docs/worklog/` only when the skill needs durable output shapes

Do not write application code.
Do not create production application files.
Do not install dependencies.
Do not access the network.
Do not run framework generators.
Do not execute implementation tasks.

Depth policy:
- `docs/project-charter.md`, `docs/glossary.md`, `docs/repo-map.md`, and `docs/roadmap.md` should be concise orientation docs.
- `docs/specs/SPEC-0000-project-foundation.md` should capture foundation requirements, boundaries, assumptions, open questions, first implementation slice, and first human-testable milestone.
- Create only the first 1-3 implementation specs when requirements, boundaries, and acceptance gates are clear.
- Create matching plans only when expected files/directories and validation commands can be named.
- Create at most 1-2 proposed batches, and only from specs/plans created during seeding.
- Keep later work as roadmap items, spec candidates, ADR candidates, open questions, or deferred decisions.

Approved output paths:
- `docs/project-charter.md`
- `docs/glossary.md`
- `docs/repo-map.md`
- `docs/roadmap.md`
- `docs/seed/SEED-0000-project-decomposition.md`
- `docs/seed/SEED-0000-results.md`
- `docs/specs/SPEC-0000-project-foundation.md`
- initial `docs/specs/SPEC-0001-*.md` through `SPEC-0003-*.md` only if clear
- matching `docs/plans/PLAN-0001-*.md` through `PLAN-0003-*.md` only if clear
- matching `docs/plans/batches/BATCH-0001-*.md` and at most one additional near-term batch
- `docs/worklog/0000-seeding-notes.md`
- `docs/adr/ADR-0000-architecture-direction.md` only if architecture choices are explicit or strongly implied
- `docs/status/CURRENT_STATE.md`

Required behavior:
1. Treat `docs/intake/PROJECT_OVERVIEW_RAW.md` as source material, not the permanent working spec.
2. Preserve raw overview intent while separating confirmed requirements, assumptions, non-goals, risks, open questions, and deferred ideas.
3. Do not invent implementation details where the overview is silent.
4. Do not create full specs/plans for speculative future work.
5. Put routine future work into roadmap/spec-candidate language.
6. Stop only if missing decisions prevent useful decomposition.

Run:
```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py docs/specs/SPEC-0000-project-foundation.md docs/specs/SPEC-0001-*.md docs/plans/PLAN-0001-*.md docs/plans/batches/BATCH-0001-*.md
git diff --check
git diff --stat
git diff
```

Final response:
- Documents created or updated
- Specs created
- Plans created
- Proposed batches created
- Key assumptions
- Open questions
- Recommended next prompt
```

Next prompt: review seeded docs. If the first spec and plan are acceptable, use `Approve Spec` and then `Approve Plan`.

### Create Spec

```txt
Mode: Spec.

We are in `[repo path]`.

Use the repo-local `controlled-planning-docs` skill at `.agents/skills/controlled-planning-docs/SKILL.md`.

Goal:
Create a new spec for [feature/slice name] from durable repo context, not prior chat history.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. `docs/project-charter.md`
5. `docs/roadmap.md`
6. `docs/glossary.md`, if relevant
7. Relevant ADRs, if needed
8. Existing nearby specs in `docs/specs/` for numbering, status wording, and scope boundaries
9. Directly relevant shared contracts or source files only if the new spec crosses that boundary

Avoid reading raw intake unless startup docs are insufficient. If needed, read only the narrow relevant section and summarize the need.

Do not edit plans, batches, application code, dependencies, lockfiles, CI, deployment, generated files, or secrets.

Tasks:
1. Pick the next spec number and descriptive filename.
2. Derive context from durable docs.
3. State source docs and current evidence.
4. Define goals, non-goals, actors, behavioral contract, interfaces/data/API/runtime contracts, requirements, dependencies/approval class, acceptance gates, risks, open questions, and stop conditions.
5. Keep future/speculative work in roadmap language unless it is required for this slice.
6. Update `docs/status/CURRENT_STATE.md` only if the active objective or next action changes.

Run:
```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [new spec path]
git diff --check
git diff --stat
git diff
```

Final response:
- New spec path
- Source docs used
- Approval class
- Open questions
- Checks run
- Exact spec approval prompt the user can send next
```

Next prompt: use `Approve Spec` if the spec is acceptable, or ask for specific spec changes.

### Approve Spec

```txt
Mode: Spec.

We are in `[repo path]`.

The user approves these specs:
- [spec paths]

Use the repo-local `controlled-planning-docs` skill.

Task:
Mark only the listed specs as `Status: Accepted` unless a listed spec is historical and should be `Status: Completed`.

Do not edit plans, batches, application code, dependencies, lockfiles, CI, deployment, or generated files.

Run:
```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [spec paths]
git diff --check
git diff --stat
git diff
```

Final response:
- Specs marked accepted or completed
- Checks run
- Next recommended plan-hardening prompt
```

Next prompt: use `Create Plan`.

### Create Plan

```txt
Mode: Plan.

We are in `[repo path]`.

Use the repo-local `controlled-planning-docs` skill.

Goal:
Create an M4 implementation plan for this accepted spec:
- [accepted spec path]

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. `.agents/skills/controlled-planning-docs/SKILL.md`
5. `.agents/skills/controlled-planning-docs/references/plan-hardening.md`
6. [accepted spec path]
7. Directly affected source/test/docs files named by the spec

Do not edit specs unless explicitly asked.
Do not edit application code.
Do not install dependencies.
Do not access the network.

Run:
```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [new plan path]
git diff --check
git diff --stat
git diff
```

Final response:
- New plan path
- Source docs used
- Whether the plan is M4
- Approval gates
- Checks run
- Exact plan approval prompt the user can send next
```

Next prompt: use `Approve Plan` if the plan is acceptable, or use `Review` if you want a readiness check first.

### Approve Plan

```txt
Mode: Plan.

We are in `[repo path]`.

The user approves these plans and batches:
- [plan paths]
- [batch paths, if any]

Use the repo-local `controlled-planning-docs` skill.

Task:
Mark only the listed plans and batches ready for implementation using the repo's established status wording. Do not implement.

Do not edit specs, application code, dependencies, lockfiles, CI, deployment, or generated files.

Run:
```bash
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [plan and batch paths]
git diff --check
git diff --stat
git diff
```

Final response:
- Plans/batches marked ready
- Checks run
- Whether any A3 approval is still needed
- Exact implementation prompt the user can send next
```

Next prompt: use `Execute Plan`.

### Execute Plan

```txt
Mode: Implementation.

We are in `[repo path]`.

Use the repo-local `accepted-plan-implementation` skill if it exists.

Execute this accepted plan exactly:
- [plan path]

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. linked accepted spec
5. [plan path]
6. directly affected source files

Do not expand scope.
Do not edit accepted specs.
Do not install dependencies or access the network unless the required A3 approval has already been granted in this thread.
Do not create lockfiles unless explicitly approved.
Do not modify CI, deployment, security policy, secrets, or unrelated files.

Before editing, run:
```bash
git status --short
```

Stop if:
- The plan is still Draft.
- An A2 or A3 gate is reached.
- A Change Request is required.
- Tests fail and cannot be resolved within scope.
- Work requires files outside the plan.

Before final response:
- Run the plan's required checks.
- Update `docs/status/CURRENT_STATE.md`.
- Create or update a handoff file only if needed.

Required final response:
DONE:
- Summary
- Files changed
- Tests/checks run
- Docs updated
- Deviations from plan
- Remaining risks
- Next action
```

Next prompt: use `Review` or `Commit Work` after checks pass, depending on the plan.

### Review

```txt
Mode: Review.

We are in `[repo path]`.

Review the current diff against:
- Spec: [spec path]
- Plan: [plan path]
- Batch: [batch path, if applicable]

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. [spec path]
5. [plan path]
6. [batch path, if applicable]

Do not implement fixes unless explicitly asked after the review.

Run or inspect:
```bash
git status --short
git diff --stat
git diff
```

Check:
1. Acceptance criteria.
2. Unplanned files.
3. Scope creep.
4. Test adequacy.
5. Docs/status updates.
6. Dependency/security risk.
7. Naming, boundaries, duplication, and dead code.

Return:
- Blocking findings first, with file references
- Non-blocking improvements
- Tests run or missing
- Whether implementation can be accepted
- Suggested next prompt
```

Next prompt: use `Commit Work` if accepted, or ask for targeted implementation fixes.

### Open Change Request

```txt
Mode: Plan.

Stop implementation.

Open a Change Request using `docs/change-requests/_template.md`.

Read:
1. `AGENTS.md`
2. `docs/status/CURRENT_STATE.md`
3. accepted spec
4. accepted plan
5. directly relevant files

Explain:
1. What assumption failed.
2. What the accepted spec/plan currently says.
3. What change is proposed.
4. Why implementation cannot continue cleanly without it.
5. Scope, files, tests, docs, risks, and token/context impact.
6. Recommendation: accept, reject, or defer.

Do not edit implementation code until the Change Request is accepted.

Run:
```bash
git diff --check
git diff --stat
git diff
```
```

Next prompt: if accepted, harden the affected spec/plan before resuming implementation.

### Commit Work

```txt
Mode: Implementation.

We are in `[repo path]`.

Commit the current worktree.

Before committing:
1. Run `git status --short`.
2. Run the relevant planning-doc checker or tests for the changed files.
3. Run `git diff --check`.
4. Run `git diff --stat`.
5. Confirm the files staged match the requested scope.

Include these user-approved files even if they were manually edited:
- [manual file paths, if any]

Commit message:
[conventional commit message]

Do not push.
Do not open a PR.

Final response:
- Commit SHA and message
- Files committed summary
- Checks run
- Worktree status
```

Next prompt: decide whether to push/open a PR. Remote Git actions require explicit approval.

## Spike And Research Work

Use Spike mode when implementation would otherwise become trial-and-error. A good spike has a small question and a clear kill point. Examples:

- Compare two local APIs without changing product behavior.
- Replay a failing trace and summarize the mismatch.
- Prototype a parser in a worklog, then promote only the accepted contract.

Spike output belongs in a concise response or `docs/worklog/`. If the spike changes the product direction, open a Change Request or update the spec/plan before implementation continues.

## Change Requests

Open a Change Request when accepted implementation scope is wrong, incomplete, or contradicted by evidence. Do not silently edit the accepted spec during implementation.

Use trigger types:

- Implementation discovery
- Research failure
- Product decision
- Policy/tooling limitation

A good Change Request says what failed, what the accepted docs currently say, what should change, why continuation is unsafe without it, and how scope/tests/docs/risk are affected.

## Commits And Pull Requests

Commit local reviewable units with Conventional Commit messages. Good examples:

```txt
docs(agent): consolidate framework manual
chore(agent): align policy hooks
test(agent): add framework policy checks
```

Before committing, run the relevant checks, `git diff --check`, `git diff --stat`, and inspect staged files.

Do not push or open a PR without explicit approval. Do not push directly to protected branches.

## Troubleshooting

If the agent keeps asking for approval on routine local work, check whether the plan is too vague or whether `AGENTS.md` duplicated approval language. Routine repo-local reads, planned edits, checks, and local commits should not need repeated approval.

If implementation keeps discovering new scope, stop and open a Change Request. Do not patch the spec while coding.

If `CURRENT_STATE.md` is too long, move narrative history into `docs/worklog/` and keep only active objective, contract, gates, last verified checks, working files, and next safest action.

If a dependency review job fails before dependency analysis runs, confirm GitHub Dependency Graph is enabled for the repository and that the workflow was intentionally restored to a pull-request trigger.

If a hook blocks a legitimate action, fix the hook only if the accepted plan includes policy work. Otherwise open a Change Request.

## Maintaining The Framework

Keep `AGENTS.md` short and durable. Move detailed workflows into this manual, skills, templates, or scripts.

Keep specs and plans task-local. They should not paste permission policy, git policy, or full logs.

Keep scripts honest. If a README names a script, the script should exist. If a script becomes the preferred command, reference it in the manual or repo map.

When templates feel too bare, add focused guidance to `.agents/skills/controlled-planning-docs/references/` first. Only add template prose when the user needs to see it while filling out the document.

Review the framework after repeated friction:

- repeated low-value approval requests,
- large startup context,
- stale operator docs,
- hooks or CI that disagree with `AGENTS.md`,
- specs/plans that routinely require redesign during implementation.

When in doubt, make the next session easier to start from files, not from memory.
