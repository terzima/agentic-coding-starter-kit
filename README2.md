# Framework Kit

## Purpose

This kit is the portable startup surface for this repo's controlled agentic development framework. It tells a new project what to copy, what to customize, what prompt to paste first, and how to verify the framework is active.

The committed kit is manifest-based. It points at canonical source files in this repo instead of duplicating them into a second tree, which keeps the framework copy path exact without creating drift.

## 1. What Files Do I Copy Into A New Project?

Copy the paths listed as included in `framework-kit/MANIFEST.md`.

At minimum, copy:

- `AGENTS.md`
- `CLAUDE.md`
- `agent-adapters.md`
- `docs/AGENTIC_WORKFLOW_MANUAL.md`
- planning templates under `docs/specs/`, `docs/plans/`, `docs/change-requests/`, `docs/status/`, `docs/handoff/`, and `docs/worklog/`
- retained `.agents/skills/`
- adapter folders you plan to use: `.codex/`, `.claude/`, `.cursor/`
- `.githooks/`
- `scripts/agent/`
- referenced files under `docs/standards/`

Copy `.github/` only when you are ready to configure repository settings. Treat it as optional remote policy until branch protection, Actions, owners, and dependency-review prerequisites are active.

Do not copy project history, product data, generated artifacts, or local caches from this repo.

## 2. What Files Must I Customize Before The First Agent Run?

Customize these files before asking an agent to work:

- `AGENTS.md`: project rules, permissions, quality gates, and documentation map.
- `docs/status/CURRENT_STATE.md`: active objective, branch/worktree state, gates, and next safest action.
- `docs/repo-map.md`: current architecture and commands for the new project.
- `docs/project-charter.md`, `docs/roadmap.md`, and `docs/glossary.md` when those files are part of the new project.
- `agent-adapters.md`: which adapters are active, copied but inactive, or not used.
- `CLAUDE.md`: keep it thin and point Claude to `AGENTS.md` plus repo-local skills.
- `.github/CODEOWNERS`: replace template owners before enabling code owner review.

Keep `docs/status/CURRENT_STATE.md` compact. Put narrative evidence in `docs/worklog/` and restart-critical detail in `docs/handoff/`.

## 2a. Fresh-Project Bootstrap Sequence

1. Copy only the included paths from `framework-kit/MANIFEST.md`.
2. Customize `AGENTS.md`, `agent-adapters.md`, `docs/status/CURRENT_STATE.md`, and `docs/repo-map.md`.
3. Run `python3 framework-kit/verify_framework_kit.py`.
4. Use the `project-intake-seeding` skill to turn owner notes or raw intake into durable startup docs.
5. Use `spike-research` only for bounded unknowns that block a useful spec.
6. Create the first spec and plan through `controlled-planning-docs`.
7. Use `accepted-plan-implementation` only after a plan is accepted or explicitly approved.

## 3. What Is The First Prompt I Paste?

```text
Mode: Discovery.

We are in `[repo path]`.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. Any active spec, plan, or batch listed in `docs/status/CURRENT_STATE.md`

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

## 4. What Should The First Agent Read?

The first agent should read only startup context:

1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. Any active spec, plan, or batch listed in the status dashboard
5. Directly relevant source files only when the task needs them

Avoid raw intake during routine implementation. Raw intake is for seeding, not normal task execution.

## 5. How Do I Seed A New Project From Intake?

Use `project-intake-seeding` when the project starts from a new idea, an existing repo without durable context, or a large raw overview.

```text
Mode: Spec.

Use the repo-local `project-intake-seeding` skill.

Goal:
Seed a new project from raw intake into durable startup docs, initial specs, initial plans, and proposed batches.

Read:
1. `AGENTS.md`
2. `.agents/skills/project-intake-seeding/SKILL.md`
3. The raw intake file supplied by the owner

Do not write product code.
Do not install dependencies.
Do not access the network.

Return:
- Source docs used
- Seeded docs created or updated
- Initial specs and plans proposed
- Open questions
- Exact next prompt
```

## 6. How Do I Create The First Spec?

```text
Mode: Spec.

Use the repo-local `controlled-planning-docs` skill.

Goal:
Create a new spec from durable repo context, not chat history.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. `docs/project-charter.md`, `docs/roadmap.md`, and `docs/glossary.md` when present
5. Existing nearby specs for numbering and scope boundaries

Do not edit plans, application code, dependencies, lockfiles, CI, deployment, generated files, or secrets.

Run:
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [new spec path]
git diff --check
git diff --stat
git diff
```

## 7. How Do I Create The First Plan?

```text
Mode: Plan.

Use the repo-local `controlled-planning-docs` skill.

Goal:
Create an M4 implementation plan for the accepted spec.

Read:
1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. `.agents/skills/controlled-planning-docs/SKILL.md`
5. `.agents/skills/controlled-planning-docs/references/plan-hardening.md`
6. The accepted spec
7. Directly affected source, test, and docs files named by the spec

Do not edit specs unless explicitly asked.
Do not edit application code.
Do not install dependencies.
Do not access the network.

Run:
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py [new plan path]
git diff --check
git diff --stat
git diff
```

## 8. How Do I Execute Implementation Safely?

Use the accepted-plan implementation skill once a plan or batch is ready.

```text
Mode: Implementation.

Use the repo-local `accepted-plan-implementation` skill.

Execute `[PLAN or BATCH path]` exactly.

Do not expand scope.
Do not install dependencies or access the network unless the accepted plan explicitly approves it.
Do not push or open a PR.

Before editing, run:
git status --short

Before final response:
- Run the plan's required checks.
- Update `docs/status/CURRENT_STATE.md`.
```

## 8a. What Skill Do I Use?

| Need | Skill |
| --- | --- |
| Fresh project startup or raw intake | `project-intake-seeding` |
| Bounded research before deciding | `spike-research` |
| Writing specs, plans, batches, status, handoffs, or worklogs | `controlled-planning-docs` |
| Accepted scope breaks during implementation | `change-request-control` |
| Implementing an accepted plan | `accepted-plan-implementation` |
| Checking completion honesty | `completion-review-gate` |
| Reviewing plan-to-spec delivery | `spec-plan-alignment` |

## 9. How Do I Review Or Commit Work?

For review, ask for findings first:

```text
Mode: Review.

Review the current diff against the accepted spec, plan, or batch.

Do not edit files.
Do not implement.

Return:
- Blocking issues
- Non-blocking improvements
- Whether the work is completion-ready
- Exact next prompt
```

For a local commit, run checks first and commit only intentional files:

```text
Mode: Implementation.

Commit the current worktree.

Before committing:
1. Run `git status --short`.
2. Run the relevant planning-doc checker or tests for the changed files.
3. Run `git diff --check`.
4. Run `git diff --stat`.
5. Confirm staged files match the requested scope.

Do not push.
Do not open a PR.
```

## 10. How Do I Verify The Framework Is Active?

Run the kit verifier:

```bash
python3 framework-kit/verify_framework_kit.py
```

Run framework checks:

```bash
bash scripts/agent/run_framework_checks.sh
python3 scripts/agent/test_framework_policy.py
```

Verify local hooks only after intentionally installing them:

```bash
bash scripts/agent/install_git_hooks.sh
git config core.hooksPath
```

Remote GitHub policy is not active until repository settings are configured and a verification PR proves the expected checks.

Claude setup is also manual. Copy approved `.claude/settings.example.json` content into the active Claude settings location, install or select the output style when supported, and keep the explicit `.agents/skills/{skill-name}/SKILL.md` fallback unless a future plan proves native skill discovery.

## Excluded Material

Do not copy:

- source-project specs, plans, Change Requests, handoffs, worklogs, deployment docs, domain data, raw intake packs, manual test artifacts, and analysis fixtures
- historical project-specific archives
- raw intake from this repo
- generated folders such as `dist/`, `.venv/`, `.pytest_cache/`, `__pycache__/`, and `*.egg-info`
- large borrowed examples removed by the planning-quality cleanup

When in doubt, copy framework rules, templates, skills, adapters, hooks, and scripts only when the manifest says how they are invoked and verified.
