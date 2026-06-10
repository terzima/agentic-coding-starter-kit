# AGENTS.md

## Prime directive

Make small, reviewable, well-tested changes. Prefer explicitness over cleverness. Do not expand scope without opening a Change Request.

## Required operating mode

Declare one mode before working:

- **Discovery**: read-only repo inspection.
- **Spec**: write or revise requirements only.
- **Plan**: produce implementation steps only.
- **Implementation**: edit code only according to an accepted plan.
- **Review**: inspect diffs, tests, risks, and docs.

Do not combine Spec, Plan, and Implementation in one pass unless explicitly instructed.

## Change control

Once implementation starts, the accepted spec is frozen.

If implementation reveals that the accepted spec or plan is wrong, incomplete, or too broad:

1. Stop implementation.
2. Create a Change Request in `docs/change-requests/` using `_template.md`.
3. Explain impact on scope, files, tests, docs, risks, and token/context use.
4. Wait for acceptance before continuing.

Do not silently modify the spec mid-implementation.

## Context discipline

Read only what is needed for the active mode.

Default context tiers:

```txt
L0 always:
- AGENTS.md
- current user request

L1 serious task:
- docs/repo-map.md
- active spec
- active plan

L2 only when needed:
- directly affected source files
- directly affected tests
- relevant ADRs
```

Do not load unrelated files into context. Do not read the whole repo unless the task is explicitly architectural or the relevant area is unknown.

## Bare implementation output

During Implementation mode, do not narrate routine steps. Report only:

- `BLOCKED:` approval or decision needed.
- `CR REQUIRED:` accepted spec/plan needs change.
- `CHECK FAILED:` verification failed.
- `DONE:` final summary.

Final summary must include:

1. Summary of changes.
2. Files changed.
3. Tests run.
4. Docs updated.
5. Deviations from plan.
6. Remaining risks.

## Allowed without repeated approval inside the worktree

- Read local non-secret project files.
- Search with `rg`, `find`, `ls`, and similar local tools.
- Edit files listed in the accepted plan.
- Run documented lint/typecheck/test/build commands.
- `git status`, `git diff`, `git add`, `git commit`, `git branch`, `git switch`, `git checkout -b`, `git worktree list`.
- Create local task branches and local worktrees.

## Ask before doing

- Accessing the network from commands.
- Installing, updating, adding, or removing dependencies.
- Downloading binaries, scripts, or remote assets.
- Running `curl`, `wget`, `Invoke-WebRequest`, `npx` for remote execution, or equivalent network-fetch commands.
- Running Docker with network, privileged mode, host mounts, or Docker socket access.
- Modifying CI, deployment, infrastructure, auth, billing, or security policy files.
- Running schema migrations.
- Reading or handling secrets.
- Pushing a branch for the first time.
- Opening a pull request.
- Modifying files outside the accepted plan.

## Never do

- Do not pipe remote content into a shell.
- Do not use `sudo` or privilege escalation.
- Do not install global system tools on the host.
- Do not modify shell startup files, OS settings, or user/global Git config unless explicitly requested.
- Do not read `.env`, private keys, credentials, or secret stores unless explicitly requested.
- Do not write outside the repository/worktree.
- Do not push directly to `main`, `master`, `prod`, `production`, or release branches.
- Do not force-push unless explicitly approved.
- Do not disable hooks, CI, tests, or security checks to make work pass.

## Dependency policy

New production dependencies require explicit approval and a short dependency rationale:

- Package and version.
- Why it is necessary.
- Alternatives considered.
- License note.
- Security/advisory considerations.
- Lockfile impact.
- Rollback plan.

Locked installs may be run only after approval when network access is required.

## Git discipline

Use one branch/worktree per task.

Before implementation:

```bash
git status --short
```

During work:

```bash
git diff --stat
git diff
```

Commit atomic units with Conventional Commit style where practical:

```txt
feat(scope): description
fix(scope): description
docs(scope): description
refactor(scope): description
test(scope): description
chore(scope): description
```

## Quality gates

Before completion:

- Run relevant lint/typecheck/test/build commands.
- Update docs if behavior changed.
- Confirm acceptance criteria.
- Summarize changed files.
- List tests run and tests not run.
- List unresolved risks.

## Documentation map

- `docs/project-charter.md`: stable product/project summary.
- `docs/repo-map.md`: architecture map and commands.
- `docs/specs/`: accepted/draft requirements.
- `docs/plans/`: implementation plans.
- `docs/change-requests/`: controlled scope changes.
- `docs/adr/`: architecture decisions.
- `docs/worklog/`: session notes and discoveries.
- `docs/standards/`: coding, testing, docs, security, dependency standards.

## Large raw overview policy

`docs/intake/PROJECT_OVERVIEW_RAW.md` is source material. Do not load it routinely during implementation. Use seeded docs and active specs/plans instead.

## Permission Policy

The agent should avoid asking for approval for routine safe repo-local work.

### Auto-allowed actions

The agent may perform these without asking:

- Read files inside the active repo.
- Edit files inside the active repo.
- Create directories/files inside the active repo.
- Run local inspection commands such as `pwd`, `ls`, `find`, `rg`, `grep`, `cat`, `head`, `tail`.
- Run local verification commands documented in `Makefile`, `package.json`, `pyproject.toml`, or `docs/repo-map.md`.
- Run local Git commands including `git status`, `git diff`, `git add`, `git commit`, `git branch`, and `git checkout -b`.

## Git Hooks

This repo uses Git hooks through `.githooks`.

The agent must not bypass hooks with `--no-verify` unless explicitly approved.

If a hook fails, the agent should fix the issue if it is within accepted scope.
If fixing the hook failure requires changing scope, the agent must stop and open a Change Request.

### Approval-required actions

The agent must ask before:

- Installing, updating, or removing dependencies.
- Modifying lockfiles.
- Using network access.
- Running `git push`.
- Creating or editing pull requests.
- Modifying CI/CD workflows.
- Modifying deployment, Docker, credentials, or environment configuration.
- Deleting files recursively.
- Running database migrations that change data.
- Running commands that affect files outside the repo.

### Hard-denied actions

The agent must not:

- Use `sudo`.
- Install global packages.
- Use `curl | bash` or equivalent remote-code execution.
- Read secrets or credentials from the user’s home directory.
- Modify files outside the active repo.
- Modify OS settings.
- Open or control other applications.
- Access browser profiles, keychains, SSH keys, cloud credentials, or unrelated documents.

### Approval request format

When approval is required, the agent must provide:

- Action:
- Exact command:
- Why needed:
- Scope:
- Risk:
- Fallback if denied:

Vague approval requests are invalid.

## Human Approval Value Policy

The agent must not ask for human approval merely because a spec, plan, or local commit is complete.

Human approval is required only when human input adds value.

### Machine-verifiable gates

If the next step can be validated by automated checks, the agent may continue without human approval.

Machine-verifiable checks include:

- lint
- typecheck
- unit tests
- integration tests
- build
- schema validation
- static analysis
- snapshot tests
- generated file existence
- no unplanned file modifications
- no policy violations

### Human-verifiable gates

The agent must stop and request human input when the next decision depends on:

- product judgment
- UX judgment
- visual/design taste
- physical-device testing
- manual app testing
- business decision
- architecture tradeoff not already settled by ADR/spec
- credentials, secrets, payment, deployment, or external service setup
- dependency installation or network access
- destructive operation
- remote Git operation if not explicitly authorized

### Approval classes

Every spec/plan must declare one approval class:

- A0: no human approval needed; continue if automated checks pass.
- A1: batch approval only; complete the batch, then summarize.
- A2: human checkpoint required before continuing.
- A3: hard approval required before taking the action.

### Default approval class

Scaffolding, documentation setup, test harnesses, repo structure, local commits, and non-user-testable implementation default to A1.

Usable UI flows, physical hardware behavior, first end-to-end product flows, dependency changes, deployment, secrets, and external services default to A2 or A3.

### Anti-pattern

Do not stop after each local spec/plan/commit merely to ask for approval.

Stop only when:
1. automated validation fails,
2. scope changed,
3. a policy exception is needed,
4. human judgment is required,
5. physical/manual testing is now possible, or
6. the current batch is complete.