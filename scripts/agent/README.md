# Agent Scripts

`scripts/agent/` is the local framework automation layer. Scripts in this folder should stay small, repo-local, and useful to humans or agents following `AGENTS.md`.

These scripts do not run product tests by default. Product-specific checks still come from the active plan or `docs/repo-map.md`.

## Retained Scripts

| Script | Purpose | Invocation path | Validation |
| --- | --- | --- | --- |
| `install_git_hooks.sh` | Configure this repo to use `.githooks` by setting `core.hooksPath`. | `make install-hooks` or direct owner-run command. | `bash -n scripts/agent/install_git_hooks.sh` |
| `agent_preflight.sh` | Print branch/worktree state, startup docs, and required scaffold-file checks. | `make preflight`; start-of-session helper. | `make preflight` |
| `agent_finalize.sh` | Print status/stat and run framework checks before closeout. | `make finalize`; end-of-session helper. | `make finalize` |
| `check_change_control.sh` | CI/local policy check for likely secret files and code/test changes without control docs. | `.github/workflows/ci.yml`; framework policy tests. | `python3 scripts/agent/test_framework_policy.py` |
| `filter_output.py` | Trim noisy command output for agent-readable test or log summaries. | Optional pipe from long-running local commands. | `python3 -m py_compile scripts/agent/filter_output.py` |
| `new_agent_task.sh` | Create a task worktree and branch with the `codex/` default branch prefix. | `make new-task TASK=0010 SLUG=short-name`; optional manual helper. | `bash -n scripts/agent/new_agent_task.sh` |
| `run_framework_checks.sh` | One-command framework validation entrypoint for humans, agents, and CI. | `bash scripts/agent/run_framework_checks.sh`; `make finalize`; CI generic checks. | `bash scripts/agent/run_framework_checks.sh docs/status/CURRENT_STATE.md docs/AGENTIC_WORKFLOW_MANUAL.md agent-adapters.md scripts/agent/README.md` |
| `policy_lib.py` | Shared canonical command-policy patterns imported by both `.codex/hooks/` and `.claude/hooks/` adapters. | Imported by hook wrappers; not invoked directly. | `python3 -m py_compile scripts/agent/policy_lib.py` |
| `test_framework_policy.py` | Python standard-library smoke tests for framework policy behavior and script inventory. | `run_framework_checks.sh`; direct local validation. | `python3 scripts/agent/test_framework_policy.py` |

## Removed Or Folded Scripts

| Script | Decision | Replacement |
| --- | --- | --- |
| `policy_check.py` | Removed. It was a third independent command-policy classifier and did not own canonical policy behavior. | Use `AGENTS.md` for permission policy and adapter/hook policy checks for enforceable behavior. |
| `seed_large_spec.sh` | Folded into docs and removed. It mostly pointed to the intake prompt without adding real validation. | Use `docs/AGENTIC_WORKFLOW_MANUAL.md` and `.agents/skills/controlled-planning-docs/references/intake-seeding.md` for intake/seeding guidance. |

## Framework Validation

Run the default framework checks:

```bash
bash scripts/agent/run_framework_checks.sh
```

Run checks for explicit docs:

```bash
bash scripts/agent/run_framework_checks.sh docs/specs/SPEC-0008-repo-cleanup-framework-quality.md docs/plans/PLAN-0010-agent-scripts-framework-automation.md docs/status/CURRENT_STATE.md scripts/agent/README.md agent-adapters.md
```

The framework check entrypoint runs planning-doc checks, shell syntax checks, Python syntax checks, framework policy smoke tests, and whitespace checks. It does not run product tests, builds, static export checks, level validation, or solver checks.

## Safety Rules

Scripts must not silently install dependencies, use the network, read secrets, modify files outside the repo, change OS settings, push to remotes, or open or merge PRs.

Scripts may inspect repo files, run documented checks, configure repo-local Git hooks when intentionally invoked by the owner, and print diagnostics.

## Spike And Research

Use Spike mode for bounded evidence gathering. Put narrative findings in `docs/worklog/`; put only restart-critical state in `docs/handoff/`; keep `docs/status/CURRENT_STATE.md` compact.
