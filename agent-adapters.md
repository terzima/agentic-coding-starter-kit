# Agent Adapters

## Purpose

This file explains how tool-specific adapter folders use the framework defined by `AGENTS.md`.

`AGENTS.md` is the canonical behavior contract. This file is the translation layer: it tells a future owner or agent which adapter files are automatic, which require setup, which are only guidance, and which files belong in a fresh-project copy kit.

## Canonical Rules

| Surface | Role | How it is used |
| --- | --- | --- |
| `AGENTS.md` | Canonical rule | Read first by agents and humans. Reusable workflow rules live here. |
| `docs/AGENTIC_WORKFLOW_MANUAL.md` | Startup manual | Human-facing prompt index and operating guide. |
| `agent-adapters.md` | Adapter manual | Explains how Codex, Claude, Cursor, skills, hooks, and remote policy connect to the canonical rules. |
| `.agents/skills/` | Procedural skills | Read by capable agents when a named skill or matching workflow is needed. |
| `.githooks/` | Local guardrails | Active only after `core.hooksPath` points to `.githooks`. |
| `.github/` | Remote guardrails | Active only after GitHub settings, Actions, CODEOWNERS, and branch protection are configured. |

Do not put long policy blocks in adapter files. Put durable repo behavior in `AGENTS.md`; put task-local contracts in specs and plans; put adapter setup and verification details here.

## Adapter Status Vocabulary

Use these labels when describing adapter state:

| Status | Meaning |
| --- | --- |
| `native-active` | The tool uses the files directly once the project is opened or trusted. |
| `manual-setup-required` | Files are present, but the owner must activate them locally. |
| `optional-remote` | Files matter only after external repository settings are configured. |
| `copied-inert` | Files are references or examples until a project owner promotes them. |
| `future-spike` | Behavior is intentionally deferred until a bounded Spike proves the design. |

## Codex

Codex-native project files live in `.codex/`.

| File or surface | How used | Current status | Required setup | Verification |
| --- | --- | --- | --- | --- |
| `.codex/config.toml` | Project-local Codex settings for sandbox, approvals, and hooks | `native-active` | Trust the project in Codex so project config is loaded | Inspect the Codex session settings or run a safe command and confirm normal approval flow |
| `.codex/hooks.json` | Wires Codex hook events to repo-local Python wrappers | `native-active` | Keep Codex hooks enabled | Use Codex hook UI or a safe command that exercises hook loading |
| `.codex/hooks/pre_tool_use_policy.py` | Codex pre-tool wrapper | `native-active` | No current setup beyond hooks enabled | Safe command is allowed; blocked command asks or denies according to policy |
| `.codex/hooks/permission_request_policy.py` | Codex permission-request wrapper | `native-active` | No current setup beyond hooks enabled | Approval requests are filtered through repo policy |

Previous Codex adapter guidance has been folded here: use Codex with workspace-write sandboxing, ask before network/dependency/remote work, keep network disabled by default, and do not use dangerous bypass modes for normal work.

## Claude

Claude-native project files live in `CLAUDE.md` and `.claude/`.

| File or surface | How used | Current status | Required setup | Verification |
| --- | --- | --- | --- | --- |
| `CLAUDE.md` | Thin repo entrypoint that points Claude to `AGENTS.md` | `native-active` | Keep it concise and canonical-rule oriented | Ask Claude to start a session and confirm it reads `AGENTS.md` |
| `.claude/settings.json` | Active Claude Code project settings: PreToolUse hook, permissions, and output style | `native-active` | No setup required; active on project open | Safe command runs without prompt; blocked command is denied by hook |
| `.claude/settings.example.json` | Copy-kit reference for the settings shape | `copied-inert` | Do not modify; use as a reference for new projects | Matches `.claude/settings.json` structure |
| `.claude/hooks/pre_tool_use_policy.py` | PreToolUse policy hook; imports from `scripts/agent/policy_lib.py`; covers `Bash\|Edit\|Write` | `native-active` | Wired via `.claude/settings.json` | `echo '{"tool_input":{"command":"sudo rm -rf /"}}' \| python3 .claude/hooks/pre_tool_use_policy.py` produces `"permissionDecision":"deny"` |
| `.claude/output-styles/Bare Engineering.md` | Implementation output style wired via `settings.json` `outputStyle` key | `native-active` | No setup required | Implementation responses use BLOCKED/CR REQUIRED/CHECK FAILED/DONE style |
| `.claude/commands/` | Thin-launcher slash commands for repo-local skills; type `/skill-name` in Claude Code | `native-active` | No setup required; available on project open | `/controlled-planning-docs`, `/accepted-plan-implementation`, `/project-intake-seeding`, and others appear in slash command autocomplete |

Claude adapter is now first-class and native. Policy enforcement is active via `settings.json` and `policy_lib.py` (shared with Codex). Skill discovery uses `.claude/commands/` slash commands as the primary invocation path, with direct SKILL.md reads as the explicit fallback documented in `CLAUDE.md`.

See `docs/worklog/claude-native-skill-discovery.md` for the evidence record behind the skill-discovery design. Stop-hook behavior remains `future-spike`; see the Spike Addendum in `docs/plans/PLAN-0019-claude-adapter-activation-and-skill-commands.md` before implementing session wrap-up reminders.

**Policy enforcement layer notes:**

`scripts/agent/policy_lib.py` technically enforces a subset of the `AGENTS.md` permission policy — the patterns in `DENY_PATTERNS` and `ASK_PATTERNS`. Items in `AGENTS.md`'s "Never" list that are not in those pattern lists (e.g., "modify shell startup files", "modify OS settings") are guidance-only and are not enforced at the tool level. When adding a hard-deny rule, update both `AGENTS.md` and `scripts/agent/policy_lib.py` together; a prose-only addition to the "Never" list adds no technical enforcement.

The implementation output format (BLOCKED / CR REQUIRED / CHECK FAILED / DONE) is defined in three places: `AGENTS.md` § Implementation output contract, `CLAUDE.md` (reference), and `.claude/output-styles/Bare Engineering.md` (active file loaded by `settings.json`). If the format changes, update all three.

## Cursor

Cursor-native project rules live in `.cursor/`.

| File or surface | How used | Current status | Required setup | Verification |
| --- | --- | --- | --- | --- |
| `.cursor/rules/agentic-development.mdc` | Always-on Cursor behavior guidance | `native-active` | Open the repo in Cursor with project rules enabled | Cursor applies Discovery, Plan, Implementation, and scope-control guidance |

Cursor rules are guidance, not a security boundary. Use Git hooks, GitHub branch protection, CI, sandboxing, and human review for enforcement.

## Repo-Local Skills

Repo-local skills are procedural helpers. They are not always-on policy.

| Skill | Use when | How invoked by Codex | Claude fallback | Copy-kit treatment |
| --- | --- | --- | --- | --- |
| `controlled-planning-docs` | Writing or revising specs, plans, batches, Change Requests, status, handoffs, worklogs, or templates | Codex skill discovery can trigger from the skill metadata | `/controlled-planning-docs` slash command or read `.agents/skills/controlled-planning-docs/SKILL.md` | Include |
| `controlled-agentic-development` | Deciding whether a task may proceed under the controlled workflow | Codex skill discovery can trigger from workflow/approval wording | `/controlled-agentic-development` slash command or read `.agents/skills/controlled-agentic-development/SKILL.md` | Include |
| `accepted-plan-implementation` | Implementing an accepted plan or explicitly ready implementation slice | User may say `Use the repo-local accepted-plan-implementation skill` | `/accepted-plan-implementation` slash command or read `.agents/skills/accepted-plan-implementation/SKILL.md` | Include |
| `change-request-control` | Accepted implementation scope breaks or needs owner decision | User may say `Use the repo-local change-request-control skill` | `/change-request-control` slash command or read `.agents/skills/change-request-control/SKILL.md` | Include |
| `completion-review-gate` | Checking whether work is complete, partial, blocked, or wrong-direction before commit/closeout/PR | Codex skill discovery can trigger before completion or commit | `/completion-review-gate` slash command or read `.agents/skills/completion-review-gate/SKILL.md` | Include |
| `spec-plan-alignment` | Reviewing whether a plan will deliver its linked spec | Codex skill discovery can trigger from alignment/review wording | `/spec-plan-alignment` slash command or read `.agents/skills/spec-plan-alignment/SKILL.md` | Include |
| `project-intake-seeding` | Starting a fresh project or turning intake into durable startup docs | User may say `Use the repo-local project-intake-seeding skill` | `/project-intake-seeding` slash command or read `.agents/skills/project-intake-seeding/SKILL.md` | Include |
| `spike-research` | Bounded evidence gathering before specs, plans, or implementation | User may say `Use the repo-local spike-research skill` | `/spike-research` slash command or read `.agents/skills/spike-research/SKILL.md` | Include |
| `token-triage` | Reducing active-context waste and moving durable details into repo files | Codex skill discovery can trigger from token/context concerns | `/token-triage` slash command or read `.agents/skills/token-triage/SKILL.md` | Include |

Claude skill discovery uses `.claude/commands/` slash commands as the primary path. The `CLAUDE.md` fallback (read the SKILL.md when a skill is named) remains active for contexts where slash commands are unavailable.

## Git Hooks

`.githooks/` is the local Git guardrail layer.

| File or surface | How used | Current status | Required setup | Verification |
| --- | --- | --- | --- | --- |
| `scripts/agent/install_git_hooks.sh` | Installs repo-local hooks by setting `core.hooksPath` | `manual-setup-required` | Run intentionally from repo root | `git config core.hooksPath` prints `.githooks` |
| `.githooks/commit-msg` | Enforces Conventional Commit format | `manual-setup-required` | Install hooks locally | `bash -n .githooks/commit-msg` and `test -x .githooks/commit-msg` |
| `.githooks/pre-commit` | Allows root `.env.example`; blocks real env/key files, large files, and staged secret patterns | `manual-setup-required` | Install hooks locally | `python3 scripts/agent/test_framework_policy.py` |
| `.githooks/pre-push` | Blocks direct pushes to protected local or remote branches | `manual-setup-required` | Install hooks locally | `bash -n .githooks/pre-push` and `python3 scripts/agent/test_framework_policy.py` |

Hooks are active only after installation. Do not bypass hooks unless the repo policy explicitly permits it for the task.

Install and verify local hooks:

```bash
bash scripts/agent/install_git_hooks.sh
git config core.hooksPath
bash -n .githooks/commit-msg .githooks/pre-commit .githooks/pre-push
python3 scripts/agent/test_framework_policy.py
```

Safe regression checks are simulated by `scripts/agent/test_framework_policy.py`; they do not require committing dangerous files.

## GitHub Policy

`.github/` is the remote guardrail layer. It is setup-dependent.

| File or surface | How used | Current status | Required setup | Verification |
| --- | --- | --- | --- | --- |
| `.github/pull_request_template.md` | Shapes PR review information | `optional-remote` | GitHub uses it after the repo is linked and PRs are opened | Open a test PR and confirm the template appears |
| `.github/workflows/ci.yml` | Runs policy and generic framework checks on PRs | `optional-remote` | Enable GitHub Actions and required checks | Verification PR runs the workflow |
| `.github/workflows/dependency-review.yml` | Manual dependency review scaffold | `optional-remote` | Enable GitHub Dependency Graph before adding a pull-request trigger | Manual run passes, then a verification PR passes after activation |
| `.github/CODEOWNERS` | Comments-only owner review template | `optional-remote` | Add a real owner/team and enable code owner review | PR shows requested code owner review |

GitHub policy status values:

```txt
Not copied | `optional-remote`
```

`optional-remote` means the files are copied locally, but enforcement depends on GitHub Actions, pull requests, CODEOWNERS, branch protection, required checks, code owner review, and Dependency Graph setup.

Manual setup checklist before treating `.github/` policy as enforced:

- Enable GitHub Actions for the repository.
- Configure branch protection for the base branch.
- Select required status checks.
- Add a real GitHub user or team to CODEOWNERS before enabling code owner review.
- Enable GitHub Dependency Graph before changing dependency review back to a pull-request workflow.
- Open one verification PR and confirm the expected checks and review requests appear.

## Local Generated Artifacts

These files are local/generated artifacts, not framework source.

| Artifact | Why it appears | Copy or commit? | Cleanup |
| --- | --- | --- | --- |
| `.pytest_cache/` | Pytest creates it during test runs for local test-run state such as last-failed data | Do not copy or commit | Safe to delete; pytest recreates it |
| `block_builder.egg-info/` | Pip/setuptools creates it during editable installs or metadata commands; it records package name, version, dependencies, extras, and source lists | Do not copy or commit | Safe to delete; packaging tools may recreate it |
| `__pycache__/` | Python creates bytecode caches when importing or compiling `.py` files | Do not copy or commit | Safe to delete; Python recreates it |

Centralizing Python bytecode caches with `PYTHONPYCACHEPREFIX` or `python -X pycache_prefix` is possible, but it is not the default recommendation because every Python command would need that environment setup.

Owner-run cleanup examples:

```bash
find . -type d -name '__pycache__' -prune -exec rm -rf {} +
rm -rf .pytest_cache
rm -rf block_builder.egg-info
```

These are intentionally destructive local cleanup commands. Run them only as the owner or under explicit approval.

## How To Customize For A New Project

Use `framework-kit/` as the reusable copy surface for fresh projects. Its README provides the startup prompts, its manifest names exact included paths, and its verifier checks that those paths still exist.

Use this table to decide what belongs in a fresh project.

| Path | Role in framework | When used | How invoked/read | Required customization | Verification |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | canonical rule | Every agent session | Read first by agents and humans | Replace project-specific policy or paths | New session can summarize rules |
| `CLAUDE.md` | adapter | Claude sessions | Claude reads it as project guidance | Keep thin; point to `AGENTS.md` and skills | Claude follows startup instructions |
| `agent-adapters.md` | adapter | Adapter setup and verification | Read by humans and agents during setup | Update adapter status and setup plan | Required sections exist |
| `docs/AGENTIC_WORKFLOW_MANUAL.md` | startup manual | Human prompt workflow | Read by owner or agent during startup | Replace product-specific examples | Prompt index works for the new repo |
| `docs/specs/_template.md` | template | New specs | Filled by planning-doc work | Tune required sections if needed | Planning-doc checker passes |
| `docs/plans/_template.md` | template | New plans | Filled by plan work | Tune task/check conventions | Planning-doc checker passes |
| `docs/plans/batches/_template.md` | template | Batch plans when used | Filled by batch planning | Decide whether batches stay in workflow | Batch docs pass checker |
| `docs/change-requests/_template.md` | template | Scope changes | Filled when implementation scope breaks | Tune risk fields if needed | Change Request is reviewable |
| `docs/status/_template.md` | template | Startup dashboard | Copied to `docs/status/CURRENT_STATE.md` | Fill active project state | New session can resume from it |
| `docs/handoff/_template.md` | template | Complex restart points | Filled only when needed | Define handoff threshold | Handoff is concise |
| `docs/worklog/_template.md` | template | Research/session evidence | Filled for spikes or durable notes | Define worklog naming | Worklog does not become status |
| `docs/standards/` | standards reference | Coding/testing/security standards | Read when referenced by plans | Keep only standards used by the workflow | Manual or plans reference each retained standard |
| `.agents/skills/` | skill | Specialized workflows | Codex skill discovery or explicit read | Keep only retained skills | Skill frontmatter is valid |
| `.codex/` | adapter | Codex project config and hooks | Codex loads after project trust | Review sandbox/hook paths | Safe commands behave as expected |
| `.claude/` | adapter | Claude settings/hooks/styles | Manual setup from examples | Copy approved settings into active Claude config | Hook/style behavior is verified |
| `.cursor/` | adapter | Cursor rule guidance | Cursor project rules | Keep rules short and canonical | Cursor applies rules |
| `.githooks/` | hook | Local Git guardrails | Installed with `scripts/agent/install_git_hooks.sh` | Review hook policy for project | `git config core.hooksPath` prints `.githooks` |
| `.github/` | optional remote policy | PRs and remote checks | GitHub repository settings | Add owner/team and enable required settings | Verification PR proves checks |
| `scripts/agent/` | script | Framework automation | Invoked by docs, Make targets, hooks, or CI | Keep retained scripts small and local | `scripts/agent/README.md` matches retained scripts |

Do not copy source-project specs, plans, Change Requests, handoffs, worklogs, deployment notes, domain data, raw intake packs, manual test artifacts, analysis fixtures, `dist/`, `.venv/`, `.pytest_cache/`, `__pycache__/`, or `*.egg-info`.

## How To Verify Adapter Behavior

Use these checks after setup:

```bash
git config core.hooksPath
bash -n scripts/agent/*.sh .githooks/*
python3 -m py_compile .codex/hooks/*.py .claude/hooks/*.py scripts/agent/*.py
python3 scripts/agent/test_framework_policy.py
bash scripts/agent/run_framework_checks.sh
python3 .agents/skills/controlled-planning-docs/scripts/check_planning_doc.py docs/status/CURRENT_STATE.md
```

For remote policy, use one verification PR or dry-run workflow after GitHub settings are configured.

## What Not To Put In Adapter Files

- Product requirements that belong in specs.
- Implementation task steps that belong in plans.
- Long duplicate policy copied from `AGENTS.md`.
- Secrets, credentials, local paths to private files, or personal cloud settings.
- Generated caches or build output.
- Tool-specific behavior that cannot be verified.

## Upgrade Checklist

- Keep `AGENTS.md` canonical.
- Keep adapter files short and native to their tool.
- Label inactive policy files as copied but inactive.
- Verify hooks and remote checks before calling them active.
- Keep repo-local skills concise and task-triggered.
- Move product-specific copy-kit content out of reusable framework material.
- Split hook, GitHub, scripts, tests, and tools cleanup into later focused plans.
- When adding a hard-deny rule to `AGENTS.md`, also add it to `scripts/agent/policy_lib.py`; prose-only additions are guidance, not enforcement.
- If the implementation output format (BLOCKED / CR REQUIRED / CHECK FAILED / DONE) changes, update `AGENTS.md` § Implementation output contract, `CLAUDE.md`, and `.claude/output-styles/Bare Engineering.md`.

## Current Repo Setup Plan

| Area | Status | Next step | Verification |
| --- | --- | --- | --- |
| Codex adapter | `native-active` | Keep `.codex/` config and hooks unchanged; `policy_lib.py` now shared from `scripts/agent/` | Codex loads project config; hooks import from shared policy source |
| Claude adapter | `native-active` | Run the Stop-hook Spike before adding session-end reminders | `python3 scripts/agent/test_framework_policy.py` passes; hook denies blocked commands |
| Cursor adapter | `native-active` | Keep `.cursor/rules/agentic-development.mdc` short | Cursor applies project rules |
| Repo-local skills | `native-active` | Use `accepted-plan-implementation` for future approved plan execution prompts | Skill frontmatter and manual pointer pass validation |
| Git hooks | `manual-setup-required` | Run `bash scripts/agent/install_git_hooks.sh` intentionally when ready | `git config core.hooksPath` prints `.githooks` |
| GitHub Actions | `optional-remote` | Enable Actions and decide required checks in repository settings | Verification PR runs CI |
| CODEOWNERS | `optional-remote` | Add a real owner/team and enable code owner review when branch protection is configured | PR requests real code owner review |
| Branch protection | `optional-remote` | Configure protected base branch and required checks | Protected branch rejects direct or unchecked merges |
| Dependency review | `optional-remote` | Enable Dependency Graph before restoring a pull-request trigger | Dependency review job passes |
| Verification PR | `optional-remote` | Open one low-risk PR after remote settings are configured | Required remote checks and owner review appear |
| Remaining adapter work | `future-spike` | Plan `.githooks/`, `.github/`, `scripts/agent/`, tests, tools, and copy-kit cleanup slices | Each later plan passes planning checks |
