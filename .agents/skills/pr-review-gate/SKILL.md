---
name: pr-review-gate
description: Use before opening or reviewing a PR to verify the diff against accepted spec, plan, tests, docs, dependency policy, and security boundaries.
---

# PR Review Gate Skill

## Checklist

1. Diff matches accepted spec and plan.
2. No unplanned files unless Change Request accepted.
3. Tests/checks run and reported.
4. Docs updated where behavior changed.
5. No unexpected dependencies.
6. No secrets or high-risk commands.
7. PR template complete.
8. Branch targets protected base branch via PR, not direct push.

## Output

Return:

- PASS/FAIL
- Blocking issues
- Non-blocking issues
- Tests run
- Suggested PR summary
- Merge risk
