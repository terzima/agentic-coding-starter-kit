# Documentation Standard

## Documentation control

- Specs describe what must be true.
- Plans describe how one accepted spec will be implemented.
- ADRs describe significant architectural decisions.
- Change Requests describe accepted scope changes.
- Worklogs capture session discoveries and carry-forward context.

## Spec policy

Accepted specs are frozen during implementation. Change them only through accepted Change Requests.

## Plan policy

Plans may be updated within accepted scope. If scope changes, open a Change Request.

## ADR policy

Do not rewrite history. Supersede old ADRs with new ADRs.

## README policy

The README is for humans. `AGENTS.md` is for agents. Avoid duplicating long agent instructions in the README.
