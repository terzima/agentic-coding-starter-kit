# BATCH-XXXX - Batch Name

Status: Draft | Accepted | In Progress | Completed | Superseded
Approval Class: A0 | A1 | A2 | A3
Batch Type: Documentation | Scaffold | Backend | Frontend | Integration | User-Testable | Other
User-testable: Yes | No
Human gate: Yes | No

## How to write this batch

Use this section while drafting, then remove it before marking the batch ready.

- Read `.agents/skills/controlled-planning-docs/references/batch-writing.md`.
- Group only already-written specs and plans.
- Keep the batch short; do not repeat full plan tasks.
- Separate A2 human checkpoints and A3 dependency/network/deployment/policy gates from normal A0/A1 implementation work.
- Do not use a batch to introduce scope absent from the included specs/plans.

## Purpose

One paragraph describing the outcome and why these specs/plans belong together.

## Included work

| Type | File | Role |
|---|---|---|
| Spec | `docs/specs/SPEC-XXXX-title.md` |  |
| Plan | `docs/plans/PLAN-XXXX-title.md` |  |
| ADR | None |  |

## Scope summary

### In scope

- Item:

### Out of scope

- Item:

## Execution contract

- Agent may continue automatically: Yes | No
- Dependency/network approval required before start: Yes | No
- Human checkpoint timing:
- Research checkpoint timing:
- Special constraints beyond `AGENTS.md`:

## Required checks

```bash
git status --short
```

Add exact commands from included plans. Avoid generic commands that are not valid for this repo.

## Human checks

- Human check:

## Stop conditions

- Stop if:

## Commit strategy

- Suggested local commits:
- Remote push/PR: requires explicit approval unless this batch says otherwise.

## Final report

Report:

1. Batch status.
2. Specs/plans completed.
3. Files changed.
4. Checks run and skipped.
5. Human checks, if any.
6. Deviations and Change Requests.
7. Remaining risks.
8. Recommended next batch.
