---
name: controlled-agentic-development
description: Use when deciding whether a repo task may proceed under the Discovery -> Spike -> Spec -> Plan -> Implementation -> Review workflow, including Change Requests, approval gates, and next safest action decisions.
---

# Controlled Agentic Development

Use this skill as a workflow decision gate. It does not replace `AGENTS.md`; it turns the current request and durable docs into a clear continue/stop decision.

## Core Rule

Always identify the active authority before acting. If the current request, accepted spec, accepted plan, or accepted Change Request does not authorize the next action, stop or move to the correct mode.

## Workflow

1. Name the current mode: Discovery, Spike, Spec, Plan, Implementation, or Review.
2. Identify the authority for the requested action:
   - current user request;
   - accepted spec;
   - accepted plan;
   - accepted Change Request;
   - repo policy in `AGENTS.md`.
3. Name the exact scope source and allowed files.
4. Check whether the task needs a Change Request because accepted scope is wrong, incomplete, or too broad.
5. Classify approval need as A0, A1, A2, or A3 using `AGENTS.md`.
6. State the next safest action as one concrete action.

## Stop Conditions

Stop when:

- implementation lacks an accepted plan;
- implementation needs files outside the accepted plan;
- the accepted spec or plan needs a behavior, file, or approval change;
- the next action needs A2/A3 approval that has not been granted;
- a requested mode mixes Spec, Plan, and Implementation without explicit authorization;
- the action would read secrets, access the network, install dependencies, push, open a PR, or touch protected policy/deployment surfaces without approval.

## Output Contract

```txt
Mode:
Authority:
Scope source:
Allowed files:
Stop gates:
Needs CR:
Needs approval:
Next safest action:
```

## What To Avoid

- Repeating the full permission, git, dependency, or Change Request policy from `AGENTS.md`.
- Treating a useful partial improvement as authority to expand scope.
- Proceeding in Implementation mode from a draft plan.
- Asking for human approval when automated checks and accepted docs already authorize A0/A1 work.
