# Status, Handoff, And Worklog Reference

Use when writing `docs/status/CURRENT_STATE.md`, `docs/handoff/*.md`, or `docs/worklog/*.md`.

## Purpose Split

`docs/status/CURRENT_STATE.md` is a dashboard. It tells the next session what is active and what to do next.

`docs/handoff/` is a restart package. It exists when work is incomplete, blocked, interrupted, or complex enough that a future agent needs precise resume context.

`docs/worklog/` is evidence and narrative. It stores research notes, failed approaches, discoveries, and reasoning that may matter later but should not bloat startup context.

## Current State Rules

Include:

- active objective,
- active contract,
- branch/worktree state,
- blocking gates or approvals,
- last verified checks,
- current working files,
- next safest action,
- handoff or worklog pointers,
- last updated date.

Avoid:

- long histories,
- full diffs,
- copied spec/plan text,
- every command ever run,
- stale completed work that no longer changes the next action.

## Handoff Rules

Use handoff when someone must resume work safely.

Include:

- resume point,
- critical context,
- files changed or in flight,
- last verified checks,
- known failed approaches,
- next command or prompt.

Do not duplicate the active spec or plan. Link to them.

## Worklog Rules

Use worklog for research or exploratory evidence.

Include:

- question or hypothesis,
- evidence gathered,
- result,
- decision,
- follow-up.

Summarize logs and cite commands instead of pasting long outputs.

## Self-Review

- Could a new agent start from `CURRENT_STATE.md` in under a minute?
- Is narrative evidence outside the dashboard?
- Is restart-critical context easy to find?
- Are failed approaches recorded only when they prevent wasted retries?
