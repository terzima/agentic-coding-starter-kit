# Agentic Coding Starter Kit

This repo is a reusable operating system for agent-assisted software projects.
It is not an application scaffold. It is the workflow, documentation, adapter,
hook, and review structure that can be copied into future projects before the
actual product code exists.

The goal is to make a new project easy to start, easy to resume, and hard for an
agent to accidentally turn into a sprawling undocumented mess.

The intended flow is:

```txt
project idea or existing repo
  -> durable startup docs
  -> specs
  -> implementation plans
  -> optional batches
  -> implementation
  -> review
  -> local commit / optional PR
```

The central habit is that important project state lives in repo files, not chat
history.

## What This Repo Provides

This starter kit provides a governance scaffold:

- canonical agent rules;
- startup and handoff docs;
- planning templates;
- repo-local workflow skills;
- Codex, Claude, and Cursor adapters;
- optional local Git hooks;
- optional GitHub policy files;
- small verification and helper scripts.

It does not provide a product scaffold:

- no `frontend/`;
- no `backend/`;
- no `package.json`;
- no `pyproject.toml`;
- no database;
- no deployment setup.

Those belong in the new project's first accepted application scaffold spec and
plan.

## Core Rule

Agents should not brainstorm, specify, plan, implement, and review all in one
undifferentiated pass.

Use explicit modes:

| Mode | Purpose | Writes product code? |
| --- | --- | --- |
| Discovery | Inspect repo state and recommend the next safest action. | No |
| Spike | Gather bounded evidence before changing specs, plans, or code. | No accepted behavior |
| Spec | Define what must be true. | No |
| Plan | Define how an accepted spec will be implemented. | No |
| Implementation | Edit files according to an accepted plan or explicitly approved slice. | Yes |
| Review | Inspect diffs, docs, tests, and risks. | No |

`AGENTS.md` is the canonical behavior contract. Other files translate, support,
or verify that contract.

## Fresh Project Startup Sequence

1. Create the new project repo.
2. Copy the framework files listed in the copy surface below.
3. Customize `AGENTS.md`, `agent-adapters.md`, `docs/status/CURRENT_STATE.md`,
   and `docs/repo-map.md`.
4. Decide which adapters are active: Codex, Claude, Cursor, Git hooks, GitHub.
5. Use `project-intake-seeding` to convert owner notes or raw intake into
   durable startup docs.
6. Use `spike-research` for bounded unknowns that block a useful spec.
7. Use `controlled-planning-docs` to create the first spec and plan.
8. Use `accepted-plan-implementation` only after a plan is accepted or the owner
   explicitly approves the exact implementation slice.

## First Prompt To Paste

Use this when opening a fresh agent session in a project that has this framework:

```txt
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

## What To Copy Into A New Project

This is the intended copy surface. The unresolved questions at the end call out
paths that still need reconciliation in this repo.

### Required Core

| Path | What it does | Customize? |
| --- | --- | --- |
| `AGENTS.md` | Canonical rules for modes, permissions, approvals, git, quality gates, and Change Requests. | Yes. Make it match the new project. |
| `README.md` | Human-facing entrypoint explaining how to use the framework. | Yes. Keep only guidance that applies. |
| `agent-adapters.md` | Explains how Codex, Claude, Cursor, skills, hooks, and GitHub policy connect to `AGENTS.md`. | Yes. Mark each adapter as active, optional, inert, or deferred. |
| `docs/AGENTIC_WORKFLOW_MANUAL.md` | Startup manual and prompt index for humans and agents. | Yes. Remove examples that do not fit. |
| `docs/repo-map.md` | Compact map of the new project's architecture, commands, and important files. | Yes. Must be project-specific. |
| `docs/status/CURRENT_STATE.md` | Compact startup dashboard: active objective, active contract, branch/worktree state, gates, checks, files, next action. | Yes. Must be current before agent work starts. |

### Planning Templates

| Path | What it does |
| --- | --- |
| `docs/specs/_template.md` | Template for requirements: goals, non-goals, behavioral contracts, interfaces, gates, risks, stop conditions. |
| `docs/plans/_template.md` | Template for executable implementation plans tied to accepted specs. |
| `docs/plans/batches/_template.md` | Template for grouping already-written specs/plans into an execution batch. |
| `docs/change-requests/_template.md` | Template for scope changes discovered during implementation. |
| `docs/status/_template.md` | Template for creating `docs/status/CURRENT_STATE.md`. |
| `docs/handoff/_template.md` | Template for restart-critical handoff notes when work is incomplete or complex. |
| `docs/worklog/_template.md` | Template for research evidence, session notes, failed approaches, and decisions. |

### Repo-Local Skills

Copy `.agents/skills/`.

| Skill | Use when |
| --- | --- |
| `project-intake-seeding` | Starting a fresh project from notes, raw intake, or an existing repo without durable context. |
| `spike-research` | Gathering bounded evidence before a spec, plan, or implementation decision. |
| `controlled-planning-docs` | Writing or revising specs, plans, batches, Change Requests, status files, handoffs, or worklogs. |
| `controlled-agentic-development` | Deciding whether the current request may proceed under the controlled workflow. |
| `accepted-plan-implementation` | Implementing an accepted plan or explicitly approved implementation slice. |
| `change-request-control` | Handling accepted scope that proves wrong, incomplete, or too broad during implementation. |
| `completion-review-gate` | Checking whether work is truly complete before closeout, commit, or PR. |
| `spec-plan-alignment` | Reviewing whether a plan will actually deliver its linked spec. |
| `token-triage` | Reducing active context and moving reusable knowledge into durable repo files. |

Skills are procedural helpers, not always-on policy. `AGENTS.md` remains the
canonical rule source.

### Tool Adapters

Copy only the adapters you plan to use.

| Path | Tool | What it does | Status vocabulary |
| --- | --- | --- | --- |
| `.codex/` | Codex | Project config and hook wrappers for sandbox, approval, and policy behavior. | Usually `native-active` after project trust. |
| `CLAUDE.md` | Claude | Thin Claude entrypoint pointing back to `AGENTS.md` and repo-local skills. | `native-active` when Claude reads it. |
| `.claude/` | Claude | Settings, hooks, output style, and slash-command launchers for repo-local skills. | `native-active` or `copied-inert` depending on setup. |
| `.cursor/` | Cursor | Always-on Cursor rules that summarize the workflow. | Guidance only, not a security boundary. |

Adapter status labels:

| Status | Meaning |
| --- | --- |
| `native-active` | The tool uses the files directly once the project is opened or trusted. |
| `manual-setup-required` | Files are present, but the owner must activate them locally. |
| `optional-remote` | Files matter only after external repository settings are configured. |
| `copied-inert` | Files are references or examples until promoted. |
| `future-spike` | Behavior is intentionally deferred until bounded research proves the design. |

### Local Guardrails And Scripts

| Path | What it does |
| --- | --- |
| `.githooks/` | Optional local Git guardrails. Active only after `core.hooksPath` points to `.githooks`. |
| `scripts/agent/install_git_hooks.sh` | Installs local hooks intentionally. |
| `scripts/agent/agent_preflight.sh` | Prints branch/worktree state and checks required startup files. |
| `scripts/agent/agent_finalize.sh` | Prints closeout state and runs framework checks. |
| `scripts/agent/check_change_control.sh` | CI/local check for likely secrets and code/test changes without planning docs. |
| `scripts/agent/filter_output.py` | Trims noisy command output for agent-readable summaries. |
| `scripts/agent/new_agent_task.sh` | Creates a task branch/worktree using the default `codex/` branch prefix. |
| `scripts/agent/policy_lib.py` | Shared command-policy patterns imported by Codex and Claude hooks. |
| `scripts/agent/run_framework_checks.sh` | One-command framework validation entrypoint. |
| `scripts/agent/test_framework_policy.py` | Python smoke tests for framework policy behavior and script inventory. |

### Optional GitHub Policy

Copy `.github/` only when you are ready to configure repository settings.

| Path | What it does | When it is active |
| --- | --- | --- |
| `.github/pull_request_template.md` | Shapes PR review information. | When PRs are opened on GitHub. |
| `.github/workflows/ci.yml` | Runs generic framework and policy checks. | When GitHub Actions is enabled. |
| `.github/workflows/dependency-review.yml` | Manual dependency review scaffold. | After Dependency Graph is enabled. |
| `.github/CODEOWNERS` | Owner review policy template. | After real owners and branch protection are configured. |

Remote policy is not real until GitHub Actions, branch protection, required
checks, CODEOWNERS, and dependency-review prerequisites are configured and
verified with a PR.

## What To Customize Before First Agent Work

Update these before asking an agent to build product behavior:

- `AGENTS.md`: project-specific rules, permissions, quality gates, and doc map.
- `docs/status/CURRENT_STATE.md`: current objective, active contract, gates,
  last checks, working files, and next safest action.
- `docs/repo-map.md`: project architecture, commands, test surfaces, and file
  ownership.
- `agent-adapters.md`: which adapters are active, optional, inert, or deferred.
- `CLAUDE.md`: keep it thin and pointed at `AGENTS.md` plus repo-local skills.
- `.github/CODEOWNERS`: replace placeholders before enabling code owner review.
- `docs/project-charter.md`, `docs/roadmap.md`, and `docs/glossary.md` when the
  project uses them.

Keep `docs/status/CURRENT_STATE.md` compact. Put narrative evidence in
`docs/worklog/`. Put restart-critical details in `docs/handoff/`.

## Normal Workflow

### Seed A New Project

Use this when the project starts from owner notes, a large overview, or an
existing repo without durable startup context.

```txt
Mode: Spec.

Use the repo-local `project-intake-seeding` skill.

Goal:
Seed a new project from raw intake into durable startup docs, initial specs,
initial plans, and proposed batches.

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

### Create A Spec

```txt
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

Do not edit plans, application code, dependencies, lockfiles, CI, deployment,
generated files, or secrets.
```

### Create A Plan

```txt
Mode: Plan.

Use the repo-local `controlled-planning-docs` skill.

Goal:
Create an implementation plan for the accepted spec.

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
```

### Execute A Plan

```txt
Mode: Implementation.

Use the repo-local `accepted-plan-implementation` skill.

Execute `[PLAN or BATCH path]` exactly.

Do not expand scope.
Do not install dependencies or access the network unless the accepted plan
explicitly approves it.
Do not push or open a PR.

Before editing, run:
git status --short

Before final response:
- Run the plan's required checks.
- Update `docs/status/CURRENT_STATE.md`.
```

### Review Work

```txt
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

## Useful Commands

Run from the repo root:

```bash
make preflight
make finalize
make install-hooks
make new-task TASK=0001 SLUG=short-name
```

Direct script equivalents:

```bash
bash scripts/agent/agent_preflight.sh
bash scripts/agent/agent_finalize.sh
bash scripts/agent/install_git_hooks.sh
bash scripts/agent/run_framework_checks.sh
python3 scripts/agent/test_framework_policy.py
```

`make seed-spec` is currently stale if it still points at the removed
`scripts/agent/seed_large_spec.sh`; use `project-intake-seeding` instead.

## Verification

After setup, verify the framework with:

```bash
bash scripts/agent/run_framework_checks.sh
python3 scripts/agent/test_framework_policy.py
git diff --check
```

After installing local hooks intentionally:

```bash
git config core.hooksPath
bash -n .githooks/commit-msg .githooks/pre-commit .githooks/pre-push
python3 scripts/agent/test_framework_policy.py
```

Adapter checks:

```bash
python3 -m py_compile .codex/hooks/*.py .claude/hooks/*.py scripts/agent/*.py
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py docs/status/CURRENT_STATE.md
```

Remote GitHub policy requires one verification PR after repository settings are
configured.

## What Not To Copy

Do not copy project-specific or generated material into a new project unless you
are intentionally adapting it:

- old `docs/specs/SPEC-*.md`;
- old `docs/plans/PLAN-*.md`;
- old `docs/plans/batches/BATCH-*.md`;
- old `docs/change-requests/CR-*.md`;
- old `docs/worklog/*.md`;
- old `docs/handoff/*.md`;
- product docs such as `docs/project-charter.md`, `docs/roadmap.md`,
  `docs/glossary.md`, and `docs/repo-map.md` unless rewritten for the new
  project;
- raw intake from a different project;
- product source, tests, deployment files, domain data, screenshots, or manual
  test artifacts;
- generated folders such as `dist/`, `.venv/`, `.pytest_cache/`, `__pycache__/`,
  `node_modules/`, and `*.egg-info`;
- secrets, credentials, local machine settings, browser profiles, shell startup
  files, or private keys.

## Current Adapter Summary

| Area | Current intent | Verification |
| --- | --- | --- |
| Codex | Native project config and hooks under `.codex/`. | Codex loads project config; hooks import shared `scripts/agent/policy_lib.py`. |
| Claude | Native `CLAUDE.md`, settings, hooks, output style, and slash-command wrappers. | Hook blocks denied commands; skill slash commands are available. |
| Cursor | Always-on project rule guidance. | Cursor applies `.cursor/rules/agentic-development.mdc`. |
| Repo-local skills | Task-triggered workflow helpers. | Skill frontmatter and referenced files exist. |
| Git hooks | Manual local guardrails. | `git config core.hooksPath` prints `.githooks`. |
| GitHub Actions | Optional remote policy. | Verification PR runs expected checks. |
| CODEOWNERS | Optional remote review policy. | Real owner/team receives review request. |
| Dependency review | Optional remote dependency guardrail. | Dependency Graph enabled and workflow passes. |

## Open Questions To Review

These are the current question marks to resolve as this README becomes the final
copy guide:

1. Should there be a real `framework-kit/` directory with `MANIFEST.md` and
   `verify_framework_kit.py`, or should the manifest-based copy-kit concept be
   removed from the docs?
2. Should `agentic-workflow-manual.md` be moved to
   `docs/AGENTIC_WORKFLOW_MANUAL.md`, since the adapters and scripts reference
   that path?
3. Should `README2.md` be deleted after this README absorbs the current system,
   or kept as a scratch/review file until the copy surface is finalized?
4. Should `docs/repo-map.md` and `docs/status/CURRENT_STATE.md` exist in this
   starter repo as template-like examples, or should only `_template.md` files be
   committed?
5. Should `docs/change-requests/_template.md` be restored as a required template?
6. Should `docs/standards/` be restored, kept optional, or removed from all copy
   guidance?
7. Should `docs/project-charter.md`, `docs/roadmap.md`, and `docs/glossary.md`
   be part of the starter copy surface, or only generated by
   `project-intake-seeding` in each new project?
8. Should `.github/` be copied by default as optional remote policy, or omitted
   until a project is ready for GitHub settings?
9. Should `.claude/settings.json` be committed as active project config, or
   should only `.claude/settings.example.json` be copied to future projects?
10. Should `make seed-spec` be removed now that `seed_large_spec.sh` has been
    folded into the `project-intake-seeding` skill?
11. Should local generated `__pycache__/` directories be cleaned from this
    working tree before the starter kit is finalized?
12. Which file should be the single canonical human entrypoint:
    `README.md`, `docs/AGENTIC_WORKFLOW_MANUAL.md`, or both with distinct jobs?
