# BATCH-XXXX — <Batch Name>

## Status

Draft / Accepted / In Progress / Completed / Superseded

## Approval Class

A0 / A1 / A2 / A3

Recommended meanings:

- A0 — No human approval needed; continue if automated checks pass.
- A1 — Batch approval only; complete the batch, then summarize.
- A2 — Human checkpoint required before continuing.
- A3 — Hard approval required before taking the action.

## Batch Purpose

Briefly describe what this batch is meant to accomplish.

Example:

This batch establishes the repo foundation, documentation control system, agent governance files, baseline CI, and initial test harness. It does not claim any user-facing product behavior is complete.

## Batch Type

Select one:

- Repo foundation
- Documentation/control-plane setup
- Architecture scaffolding
- Core domain scaffolding
- Backend implementation
- Frontend implementation
- Integration slice
- First user-testable flow
- Physical/hardware-testable flow
- Refactor/cleanup
- Bugfix batch
- Other: <describe>

## Human Gate

Does this batch require human review before the agent continues to the next batch?

- Yes / No

### Human Gate Reason

Explain why human input does or does not add value here.

Examples:

- No. This batch is scaffolding only and can be validated by automated checks.
- No. This batch does not expose a user-testable behavior yet.
- Yes. This batch produces the first usable UI flow and requires manual product review.
- Yes. This batch requires physical testing on real hardware.
- Yes. This batch requires choosing between unresolved architecture options.

## Included Specs

- `docs/specs/SPEC-XXXX-<name>.md`
- `docs/specs/SPEC-XXXX-<name>.md`
- `docs/specs/SPEC-XXXX-<name>.md`

## Included Plans

- `docs/plans/PLAN-XXXX-<name>.md`
- `docs/plans/PLAN-XXXX-<name>.md`
- `docs/plans/PLAN-XXXX-<name>.md`

## Related ADRs

- `docs/adr/ADR-XXXX-<decision>.md`

If no ADRs are required, write:

None.

## Scope

### In Scope

- <item>
- <item>
- <item>

### Out of Scope

- <item>
- <item>
- <item>

## Agent Autonomy Rules

The agent may continue automatically through this batch if all of the following remain true:

- [ ] Work stays inside the active repo/worktree.
- [ ] Work stays within the included specs and plans.
- [ ] No user-facing behavior is claimed complete unless this batch is explicitly user-testable.
- [ ] No physical/manual testing is required.
- [ ] No unresolved product decision is encountered.
- [ ] No unresolved architecture decision is encountered.
- [ ] No dependency installation is required without approval.
- [ ] No network access is required without approval.
- [ ] No secrets, credentials, payment, deployment, or external-service setup is required.
- [ ] No destructive operation is required.
- [ ] No files outside the approved scope are modified.
- [ ] Automated checks pass or failures are resolved within accepted scope.

## Approval-Required Actions

The agent must stop and request approval before:

- Installing, updating, or removing dependencies.
- Modifying lockfiles, unless the batch explicitly authorizes it.
- Using network access.
- Reading or writing outside the repo/worktree.
- Using secrets, credentials, API keys, or environment-specific values.
- Running deployment commands.
- Running destructive commands such as recursive delete, hard reset, database wipe, or prune.
- Changing CI/CD, release, or deployment behavior outside the accepted scope.
- Pushing to a remote branch or creating/editing a PR, unless explicitly authorized.

## Stop Conditions

The agent must stop if:

- [ ] A Change Request is needed.
- [ ] The accepted spec is discovered to be wrong, incomplete, or contradictory.
- [ ] The batch becomes human-testable.
- [ ] Manual/physical testing becomes necessary.
- [ ] Product judgment is required.
- [ ] Architecture judgment is required beyond accepted ADRs/specs.
- [ ] A dependency or network action is required.
- [ ] A security, privacy, or secrets issue is encountered.
- [ ] Automated checks fail and cannot be fixed within scope.
- [ ] The agent would need to modify files outside the included specs/plans.
- [ ] The agent would need to perform an action classified as A3.

## Automated Gate

This batch is complete when:

- [ ] All included specs have been satisfied.
- [ ] All included plans have been completed or explicitly deferred.
- [ ] Relevant tests pass.
- [ ] Relevant lint checks pass.
- [ ] Relevant type checks pass.
- [ ] Relevant build checks pass.
- [ ] Documentation has been updated.
- [ ] No unplanned files were modified.
- [ ] No user-facing behavior is claimed complete unless validated.
- [ ] Any skipped checks are documented with reasons.

## Required Checks

List the exact commands the agent should run when applicable.

```bash
# Examples only; replace with project-specific commands.
git status --short
make test
make lint
make typecheck
make build
```

If no commands exist yet, write:

```bash
git status --short
```

And explain why formal checks do not exist yet.

## Commit Policy

Local commits are allowed inside this batch if:

- [ ] Each commit is coherent and reviewable.
- [ ] Commit messages use the repo convention.
- [ ] Commits stay inside the accepted scope.
- [ ] No remote push is performed without approval.

Suggested commit sequence:

1. `docs(batch): add batch execution plan`
2. `<type>(<scope>): <description>`
3. `<type>(<scope>): <description>`

## Final Batch Report

At completion, the agent must report:

1. Batch status.
2. Specs completed.
3. Plans completed.
4. Files changed.
5. Local commits created.
6. Checks run.
7. Checks not run and why.
8. Deviations from the batch plan.
9. Change Requests opened, if any.
10. Deferred items.
11. Whether the next batch is A0, A1, A2, or A3.
12. Whether the next batch requires human testing.

## Next Batch Recommendation

After completing this batch, recommend the next batch:

- `docs/plans/batches/BATCH-XXXX-<name>.md`

Recommended approval class:

- A0 / A1 / A2 / A3

Reason:

<explain>

## Notes

Use this section for implementation notes, assumptions, or links to relevant files.

