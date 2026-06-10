# Security Standard

## Agent-specific rules

- No secret reads without explicit instruction.
- No credential printing.
- No network downloads by default.
- No remote script execution.
- No global installs on the host.
- No disabling security checks.

## Secret patterns

Never commit:

- `.env` or `.env.*` except `.env.example`
- private keys
- cloud credentials
- API tokens
- database dumps containing real data

## Auth/security-sensitive changes

Changes to auth, authorization, crypto, session management, billing, permissions, or CI/CD require Review mode and should generally have an ADR or Change Request.
