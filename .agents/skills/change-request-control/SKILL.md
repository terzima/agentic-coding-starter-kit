---
name: change-request-control
description: Use when implementation reveals that an accepted spec or plan is wrong, incomplete, too broad, or no longer safely executable without an owner decision.
---

# Change Request Control

Use this skill when accepted scope breaks during implementation. It creates a clear decision surface before work continues.

## Core Rule

Do not silently modify an accepted spec or plan during implementation. Stop, name the failed assumption, and route the change through a reviewable Change Request.

## Workflow

1. Read `AGENTS.md`.
2. Read `docs/status/CURRENT_STATE.md`.
3. Read the accepted spec, accepted plan, active batch, or Change Request context named by the current task.
4. Read `docs/change-requests/_template.md`.
5. Identify the failed assumption in plain language.
6. State what the accepted contract currently says.
7. State the proposed change and why implementation cannot continue cleanly without it.
8. Identify scope impact across files, tests, docs, risks, approvals, and token/context use.
9. Recommend exactly one outcome: `accept`, `reject`, or `defer`.
10. If asked to create the CR, write it under `docs/change-requests/` using the repo template and run the planning-doc checker.

## Stop Conditions

Stop and report the blocker when:

- there is no accepted spec, plan, batch, or current implementation contract to compare against;
- the issue is only a bug inside accepted scope and does not require a contract change;
- the proposed change needs product, business, security, dependency, deployment, or external-service approval;
- the CR would bundle unrelated behavior changes.

## Output Contract

```txt
CR path:
Failed assumption:
Accepted contract impact:
Proposed change:
Why implementation must stop or may continue:
Scope impact:
Files/tests/docs impact:
Risk and context impact:
Recommendation: accept | reject | defer
Exact next prompt:
```

## What To Avoid

- Continuing implementation while the accepted contract is known to be wrong.
- Rewriting the spec or plan directly instead of using a CR.
- Treating useful cleanup as a Change Request when it is already within accepted scope.
- Combining multiple unrelated scope changes into one CR.
- Recommending more than one next prompt.
