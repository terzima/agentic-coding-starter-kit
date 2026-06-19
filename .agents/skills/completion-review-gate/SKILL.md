---
name: completion-review-gate
description: Use before committing, closing a plan/spec, opening a PR, or reporting completion to decide whether the actual result is complete, partial, blocked, or wrong-direction against the accepted objective.
---

# Completion Review Gate

Use this skill for outcome honesty. The question is not whether progress was useful; the question is whether the work reached the expected result.

## Core Rule

Compare the expected result to the actual evidence. A partial improvement stays partial unless the accepted spec/plan's outcome and gates are actually satisfied.

## Workflow

1. Read the accepted objective from the current request, spec, plan, batch, or Change Request.
2. State the expected result in plain language.
3. Compare changed files, tests, docs, and manual/human gates against that expected result.
4. Classify the outcome as exactly one value: `complete`, `partial`, `blocked`, or `wrong-direction`.
5. Decide whether the work can be committed.
6. Decide whether the plan/spec can be closed.
7. Provide one recommended next prompt when follow-up is needed.

## Outcome Values

- `complete`: required result and gates are satisfied.
- `partial`: useful progress exists, but required result or gates are incomplete.
- `blocked`: progress cannot continue without owner decision, approval, external state, or a Change Request.
- `wrong-direction`: the work moved away from the intended result or implemented unsupported scope.

## PR Readiness Use

Before a PR, also check that the diff matches accepted scope, checks are reported, docs are updated where behavior changed, dependency/security boundaries are respected, and known gaps are visible in the PR body.

## Partial Work Rule

Partial work may be committed only when the commit message, status docs, and next prompt clearly preserve the remaining gap. Do not close the plan or call the outcome complete.

## Stop Conditions

Stop when:

- expected result cannot be identified from durable docs or the current request;
- evidence is missing for a required gate;
- changed files include unsupported scope;
- a required approval, manual checkpoint, or Change Request is missing.

## Output Contract

```txt
Outcome:
Expected result:
Actual result:
Delta:
Evidence:
Can commit:
Can close plan/spec:
Follow-up needed:
Recommended next prompt:
```

## What To Avoid

- Giving a PASS/FAIL without explaining the delta.
- Treating green tests as completion when the product or documentation result is still missing.
- Expanding into implementation fixes during Review unless the user explicitly changes mode.
- Listing more than one recommended next prompt.
