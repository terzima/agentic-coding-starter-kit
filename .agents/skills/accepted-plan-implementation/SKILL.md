---
name: accepted-plan-implementation
description: Use when implementing an accepted repo plan or an explicitly named ready implementation slice; compresses the standard long implementation prompt into a guarded workflow with accepted-plan verification, minimal context read, scope check, proof-first slices, focused checks, CURRENT_STATE update, and completion-review-gate before DONE.
---

# Accepted Plan Implementation

Use this skill to execute an already accepted plan without making the user paste the long implementation prompt every time.

## Core Rule

Implement only from an accepted or ready implementation contract. This skill does not authorize work from a draft plan, missing spec, vague request, or unsupported scope.

## Workflow

1. Read `AGENTS.md`.
2. Read `docs/status/CURRENT_STATE.md`.
3. Read the accepted spec and accepted plan named by the user or dashboard.
4. Confirm the plan status is `Ready for Implementation` or that the owner explicitly approved the exact plan in the current request.
5. Run `git status --short` before editing.
6. Identify allowed files, stop gates, A2/A3 gates, and required checks.
7. Run proof-first or focused pre-checks when the plan defines them.
8. Set a task cursor before each slice: name the active plan task, allowed files, expected failure/pass evidence, and focused check.
9. Check the allowed-file list before each edit.
10. Scan stop gates before and after each meaningful slice.
11. Implement in small plan-scoped slices.
12. Rerun focused checks after each meaningful slice.
13. Update `docs/status/CURRENT_STATE.md` at the end of meaningful implementation.
14. Use `.agents/skills/completion-review-gate/SKILL.md` before final reporting when committing, closing a plan, or reporting completion.
15. Final response uses the repo implementation `DONE:` contract.

## Implementation Discipline

Borrow these habits from strong implementation workflows:

- work in small verified steps;
- prefer proof-first checks when they are useful;
- use expected failure and expected pass when the plan defines them;
- do not edit a file until it is in the accepted plan's allowed-file set;
- treat a failed expected-failure/pass proof as the first owner to debug before downstream work;
- identify the first failing owner when blocked;
- do not claim completion without evidence.

This skill does not depend on any external plugin being installed.

## Stop Conditions

Stop and report the matching blocker when:

- the plan is Draft and the current request does not explicitly approve it;
- the accepted spec or plan is missing;
- work needs files outside the plan;
- a check fails and cannot be fixed inside scope;
- an A2 or A3 gate is reached;
- a Change Request is required;
- network, dependency, lockfile, CI, deployment, security policy, secret, or remote Git work is needed;
- product judgment is required before continuing.

## Output Contract

```txt
DONE:
- Summary
- Files changed
- Tests/checks run
- Docs updated
- Deviations from plan
- Remaining risks
- Next action
```

## What To Avoid

- Rewriting the plan during implementation.
- Treating useful progress as complete without running the required checks.
- Continuing after a failed proof into downstream work that depends on it.
- Bypassing this repo's spec, plan, approval, or Change Request rules.
