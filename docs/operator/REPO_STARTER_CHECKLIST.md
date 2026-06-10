# New Repo Starter Checklist

## Phase 0 — Create and protect the repo

- [ ] Create GitHub repo.
- [ ] Initialize local repo.
- [ ] Copy `starter-repo/` contents into repo root.
- [ ] Install local hooks with `scripts/agent/install_git_hooks.sh`.
- [ ] Commit scaffold.
- [ ] Push initial branch.
- [ ] Set branch protection on `main` or `master`.
- [ ] Require PR before merge.
- [ ] Require status checks before merge.
- [ ] Require conversation resolution before merge.
- [ ] Consider requiring CODEOWNERS review for protected areas.

## Phase 1 — Seed project context

- [ ] Paste large overview into `docs/intake/PROJECT_OVERVIEW_RAW.md`.
- [ ] Run `docs/intake/SEEDING_PROMPT.md` in Discovery/Spec mode only.
- [ ] Review generated `docs/project-charter.md`.
- [ ] Review generated `docs/glossary.md` if applicable.
- [ ] Review first `SPEC-*`.
- [ ] Review first `PLAN-*`.
- [ ] Review ADR candidates.
- [ ] Accept or revise docs manually before coding.

## Phase 2 — Configure agent boundaries

- [ ] Confirm `AGENTS.md` matches your personal preferences.
- [ ] Confirm `.codex/config.toml` network policy if using Codex.
- [ ] Trust repo-local Codex hooks only after reviewing them.
- [ ] If using Claude Code, copy or adapt `.claude/settings.example.json` to `.claude/settings.local.json` or user settings.
- [ ] If using Cursor, verify `.cursor/rules/agentic-development.mdc` loads.
- [ ] Decide whether the agent may push task branches.
- [ ] Decide whether opening PRs requires approval each time.

## Phase 3 — First task

- [ ] Create task worktree:

```bash
scripts/agent/new_agent_task.sh 0001 first-slice
```

- [ ] Start agent in the new worktree.
- [ ] Tell agent to read `AGENTS.md`.
- [ ] Begin in Discovery or Implementation mode based on accepted docs.
- [ ] Require bare output in implementation.
- [ ] Stop for Change Request if scope shifts.

## Phase 4 — PR gate

- [ ] Run finalizer:

```bash
scripts/agent/agent_finalize.sh
```

- [ ] Push task branch.
- [ ] Open PR.
- [ ] Confirm PR links spec, plan, ADRs, and Change Requests.
- [ ] Confirm CI passes.
- [ ] Review diff as human owner.
- [ ] Merge only after acceptance.
