# Agentic Coding Starter Kit — Start Here

This kit is designed for a new repository where you want three properties at the same time:

1. **Lower token usage** through scoped context, bare output, skills, hooks, and durable repo documents.
2. **Controlled implementation** through spec → plan → implementation → review gates.
3. **Bounded autonomy** so the agent can work efficiently inside a repo/worktree, but cannot casually download, install, exfiltrate, mutate host configuration, or bypass GitHub review.

## What to copy into a new repo

Copy the contents of `starter-repo/` into the root of the new repository.

Minimum set:

```txt
AGENTS.md
CLAUDE.md
.cursor/rules/agentic-development.mdc
.github/pull_request_template.md
.github/workflows/ci.yml
.github/workflows/dependency-review.yml
.githooks/
.codex/
.agents/skills/
docs/
scripts/agent/
```

Then run:

```bash
chmod +x scripts/agent/*.sh scripts/agent/*.py .githooks/* .codex/hooks/*.py
scripts/agent/install_git_hooks.sh
scripts/agent/agent_preflight.sh
```

## First repo bootstrap sequence

Use this sequence before the implementation agent writes application code:

```txt
1. Create repo.
2. Copy starter-repo files into repo root.
3. Commit the process scaffold.
4. Paste your large project overview into docs/intake/PROJECT_OVERVIEW_RAW.md.
5. Ask the agent to run the prompt in docs/intake/SEEDING_PROMPT.md in Discovery/Spec mode only.
6. Review and accept the generated project charter, glossary, first SPEC, first PLAN, and ADR candidates.
7. Only then start implementation.
```

## Recommended first commit

```bash
git add AGENTS.md CLAUDE.md .cursor .github .githooks .codex .agents docs scripts Makefile .editorconfig .gitattributes .gitignore .pre-commit-config.yaml SECURITY.md
git commit -m "chore(agent): add controlled agentic development scaffold"
```

## Files in this kit

Top-level files explain the system to you:

```txt
AGENTIC_CODING_GUIDELINES.md
TOKEN_OPTIMIZATION_PLAYBOOK.md
BOUNDARY_AND_SANDBOX_POLICY.md
LARGE_SPEC_SEEDING_PLAYBOOK.md
REPO_STARTER_CHECKLIST.md
PROMPT_LIBRARY.md
IMPORTANT_LINKS.md
```

`starter-repo/` contains copy-ready repository files.

## Tool-specific adapters

The repo scaffold is agent-agnostic first. It also includes adapters:

```txt
.codex/                      Active Codex project config and hooks
.claude/                     Claude Code output style and settings example
.cursor/rules/               Cursor-style repo rule
.agents/skills/              Codex/OpenAI-style skills for progressive disclosure
tooling/                     Non-active extra examples and notes
```

If you are not using a tool, leave its adapter alone. The core workflow still works through `AGENTS.md`, docs, Git hooks, and GitHub PR gates.
