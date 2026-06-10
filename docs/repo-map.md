# Repo Map

Status: Draft
Last updated: YYYY-MM-DD

## Purpose

Briefly describe the repository.

## Main directories

- `src/` or `app/`: application code.
- `tests/`: tests.
- `docs/`: specs, plans, ADRs, standards, worklogs.
- `scripts/agent/`: deterministic helper scripts for agent workflow.
- `.github/`: PR template and CI workflows.
- `.githooks/`: local Git hooks.
- `.codex/`, `.claude/`, `.cursor/`: tool-specific agent adapters.

## Main commands

Update these once the stack is chosen.

```bash
# install
TBD

# dev
TBD

# test
TBD

# lint
TBD

# typecheck
TBD

# build
TBD
```

## Architectural boundaries

- UI layer:
- API layer:
- Domain layer:
- Persistence layer:
- Integration layer:

## Do not touch casually

- Auth/security:
- Billing/payments:
- Migrations:
- Shared types/contracts:
- Generated files:
- CI/deployment:

## Common patterns

- Error handling:
- Logging:
- Configuration:
- Testing:
- Dependency injection:

## Agent context notes

Agents should read this file before broad codebase discovery. Keep it short and current.
