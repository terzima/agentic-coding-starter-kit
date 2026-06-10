# Security Policy

## Agent safety rules

- Do not commit secrets.
- Do not let agents read `.env`, private keys, credential files, or secret stores unless explicitly instructed.
- Do not pipe remote content into a shell.
- Do not install new dependencies without approval and a dependency rationale.
- Do not disable security checks, hooks, CI, or dependency review to make work pass.

## Reporting issues

For now, open a private issue or contact the repository owner.

## Dependency changes

Every new production dependency must include:

- reason for use
- alternatives considered
- license note
- known security/advisory review
- lockfile diff
- rollback plan
