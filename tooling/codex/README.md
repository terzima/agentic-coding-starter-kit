# Codex Adapter Notes

Active project files are in `.codex/` at repo root.

Recommended default:

```bash
codex --sandbox workspace-write --ask-for-approval on-request
```

The starter `.codex/config.toml` keeps network off by default and enables hooks. The hooks block obvious dangerous commands and force ask-first behavior for network, dependency installs, Docker operations, direct protected-branch pushes, and PR creation.

Review hooks with the Codex `/hooks` UI before trusting them.

Do not use `--dangerously-bypass-approvals-and-sandbox` for normal work. If you run Codex inside a fully isolated disposable container, document that exception.
