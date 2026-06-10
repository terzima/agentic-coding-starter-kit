# Devcontainer Notes

A devcontainer can provide an outer isolation boundary for agentic work.

Recommended principles:

- No secrets mounted by default.
- No Docker socket mount by default.
- No host root mounts.
- Network disabled or allowlisted where practical.
- All installed tools are visible in the Dockerfile.
- Dependency installs are explicit and reproducible.

A generic devcontainer is not included at repo root because project stack choices matter. Create one after the runtime stack is selected and document it in an ADR.
