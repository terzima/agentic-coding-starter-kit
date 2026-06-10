# Boundary and Sandbox Policy for Agentic Coding

## Goal

Allow the agent to be productive inside a repo/worktree without granting broad host or internet autonomy.

The target balance:

```txt
High autonomy inside a controlled worktree.
Low autonomy outside the worktree.
Explicit approval for network, downloads, dependencies, secrets, infra, and destructive actions.
```

## Trust zones

### Zone 0 — Human-only

The agent may not do these without explicit instruction and human supervision:

```txt
production deploys
credential creation/rotation
billing/provider changes
cloud IAM changes
database destructive migrations
security bypasses
installing global system tools
changing OS or shell startup files
```

### Zone 1 — Ask-first

The agent may propose exact commands, but must wait for approval:

```txt
package install/update/add/remove
network downloads
curl/wget/http client commands
docker pull/build/run with network
new services or daemons
schema migrations
first push of a branch
opening a PR
modifying CI/security policy files
```

### Zone 2 — Auto inside worktree

The agent may do these repeatedly without asking:

```txt
local file edits in planned scope
git status/diff/add/commit/branch/switch/worktree
rg/find/ls/cat local non-secret files
run documented tests/lint/typecheck/build
format code with documented formatter
update docs required by accepted plan
```

## Default command policy

| Action | Policy | Reason |
|---|---|---|
| `git status`, `git diff` | Allow | Read-only review. |
| `git add`, `git commit` | Allow | Atomic local history is desirable. |
| `git push origin agent/...` | Ask on first push | External side effect. |
| `git push origin main` | Deny | Bypasses PR gate. |
| `git push --force` | Ask or deny | Can destroy remote history. |
| `npm ci`, `pnpm install --frozen-lockfile`, `uv sync --locked` | Ask | Network dependency download. |
| `npm install <pkg>`, `pnpm add <pkg>`, `pip install <pkg>` | Ask + Change Request | Changes dependency surface. |
| `curl`, `wget`, `Invoke-WebRequest` | Ask | Network and supply-chain risk. |
| `curl ... | sh` | Deny | Remote code execution. |
| `sudo`, `chmod -R 777`, `rm -rf /` | Deny | Host/destructive risk. |
| `docker run -v /:/host` | Deny | Host escape risk. |
| reading `.env`, secrets, keys | Deny unless explicit | Secret exposure risk. |

## Recommended runtime posture

### Codex

Use the default middle ground:

```bash
codex --sandbox workspace-write --ask-for-approval on-request
```

Keep network off unless you intentionally approve it. Use `.codex/config.toml` and `.codex/hooks.json` from the starter repo.

### Claude Code

Use permission allowlists for safe local commands and hooks for denials. Keep a short `CLAUDE.md` that points to `AGENTS.md`. Use the included `Bare Engineering` output style to reduce implementation chatter.

### Cursor / IDE agents

Use repository rules plus GitHub branch protection. Do not rely on IDE rules as the only enforcement boundary.

## Dev container posture

A devcontainer is useful when you want a stronger isolation boundary. Recommended use:

```txt
host repo → devcontainer workspace → agent worktree → task branch → PR
```

Good devcontainer policies:

- No host root mounts.
- No host Docker socket mount unless explicitly needed.
- No secrets mounted by default.
- Network disabled or allowlisted where possible.
- Package manager caches are okay; credentials are not.
- Build/install commands are documented and visible.

## Dependency policy

The agent must not casually add dependencies. For every new production dependency, require:

```txt
1. Package name and version.
2. Why standard library/internal code is insufficient.
3. Runtime impact.
4. License note.
5. Security/advisory check.
6. Lockfile diff.
7. Removal/rollback plan.
```

Prefer:

```txt
locked installs
pinned versions
small dependency graph
first-party SDKs
well-maintained packages
```

Avoid:

```txt
unmaintained packages
install scripts with opaque behavior
curl-piped installers
packages used for trivial utilities
```

## What the hooks do

The included hooks are defense-in-depth. They are not a perfect sandbox. They block obvious high-risk commands and force the agent to ask for approval when a command crosses boundaries.

Important: hooks are policy checks. The real boundary should come from your agent tool’s sandbox, devcontainer, OS permissions, and GitHub review gates.
