# AGENTS.md

## Prime directive

Make small, reviewable, well-tested changes. Prefer explicitness over cleverness. Do not expand scope without opening a Change Request.

Use durable repo files as the handoff surface. A future agent should be able to resume from `AGENTS.md`, `docs/repo-map.md`, `docs/status/CURRENT_STATE.md`, and the active spec/plan/batch without relying on chat history.

## Operating modes

Declare one mode before working:

- **Discovery**: read-only repo inspection.
- **Spike**: bounded research or experimentation where the output is evidence, not accepted production behavior.
- **Spec**: write or revise requirements only.
- **Plan**: produce implementation steps only.
- **Implementation**: edit only according to an accepted plan.
- **Review**: inspect diffs, tests, risks, and docs.

Do not combine Spec, Plan, and Implementation in one pass unless explicitly instructed.

Spike mode must state:

- question or hypothesis,
- allowed files or surfaces,
- evidence to collect,
- budget or kill criteria,
- output destination, and
- promotion rule.

Spike output must not become accepted implementation behavior until it is captured in an accepted spec or plan.

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
- docs/status/CURRENT_STATE.md
- active spec
- active plan

L2 only when needed:
- directly affected source files
- directly affected tests
- relevant ADRs
```

Do not load unrelated files into context. Do not read the whole repo unless the task is explicitly architectural or the relevant area is unknown.

Do not load `docs/intake/PROJECT_OVERVIEW_RAW.md` routinely during implementation. Use seeded docs and active specs/plans instead.

## Handoff, status, and worklog policy

New agent sessions should start by reading:

1. `AGENTS.md`
2. `docs/repo-map.md`
3. `docs/status/CURRENT_STATE.md`
4. The active spec/plan/batch listed in `docs/status/CURRENT_STATE.md`
5. Directly relevant source files

`docs/status/CURRENT_STATE.md` is a compact startup dashboard. It should contain the active objective, active contract, branch/worktree state, blocking gates, last verified checks, current working files, and next safest action.

`docs/worklog/` is for narrative session evidence, failed approaches, research notes, and decisions that may inform future reasoning.

`docs/handoff/` is for concise restart packages when work is incomplete, blocked, interrupted, or complex enough that the next agent needs a restart point.

At the end of every meaningful implementation session, update `docs/status/CURRENT_STATE.md`. Create or update a handoff file only when it changes future action.

## Implementation output contract

During Implementation mode, do not narrate routine steps. Report only:

- `BLOCKED:` approval or decision needed.
- `CR REQUIRED:` accepted spec/plan needs change.
- `CHECK FAILED:` verification failed.
- `DONE:` final summary.

Final implementation summaries must include:

1. Summary of changes.
2. Files changed.
3. Tests/checks run.
4. Docs updated.
5. Deviations from plan.
6. Remaining risks.
7. Next action.

## Permission policy

The agent should avoid asking for approval for routine safe repo-local work.

Auto-allowed inside the active repo/worktree:

- Read local non-secret project files.
- Search with `rg`, `find`, `ls`, `grep`, `cat`, `head`, `tail`, and similar local tools.
- Edit files inside the accepted plan.
- Create directories/files inside the accepted plan.
- Run documented lint, typecheck, test, build, and planning-doc checks.
- Run local Git commands: `git status`, `git diff`, `git add`, `git commit`, `git branch`, `git switch`, `git checkout -b`, and `git worktree list`.
- Create local task branches and local worktrees.

Ask before:

- Accessing the network from commands.
- Installing, updating, adding, or removing dependencies.
- Downloading binaries, scripts, or remote assets.
- Running remote-fetch commands or remote execution helpers.
- Running Docker with network, privileged mode, host mounts, or Docker socket access.
- Modifying CI, deployment, infrastructure, auth, billing, or security policy files unless an accepted A3 plan explicitly includes those files.
- Running schema migrations.
- Reading or handling secrets.
- Pushing a branch.
- Opening or editing pull requests.
- Modifying files outside the accepted plan.
- Deleting files recursively.

Never do:

- Pipe remote content into a shell.
- Use administrator elevation or privilege escalation.
- Install global system tools on the host.
- Modify shell startup files, OS settings, or user/global Git config unless explicitly requested.
- Read environment files, private keys, credentials, browser profiles, keychains, cloud credentials, or unrelated documents unless explicitly requested.
- Write outside the repository/worktree.
- Push directly to `main`, `master`, `prod`, `production`, or release branches.
- Force-push unless explicitly approved.
- Disable hooks, CI, tests, or security checks to make work pass.

Approval requests must include:

- Action:
- Exact command:
- Why needed:
- Scope:
- Risk:
- Fallback if denied:

Human approval is required only when human input adds value: product judgment, UX judgment, physical/manual testing, business decisions, unsettled architecture tradeoffs, credentials/secrets/payment/deployment/external services, dependencies/network, destructive operations, or remote Git operations.

Machine-verifiable work may continue when automated checks pass and accepted docs authorize the scope.

Approval classes:

- A0: no human approval needed; continue if automated checks pass.
- A1: batch approval only; complete the batch, then summarize.
- A2: human checkpoint required before continuing.
- A3: hard approval required before taking the action.

Default approval class:

- Scaffolding, documentation setup, test harnesses, repo structure, local commits, and non-user-testable implementation default to A1.
- Usable UI flows, physical hardware behavior, first end-to-end product flows, dependency changes, deployment, secrets, and external services default to A2 or A3.

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

This repo uses Git hooks through `.githooks`. Do not bypass hooks with `--no-verify` unless explicitly approved.

If a hook fails, fix the issue if it is within accepted scope. If fixing it requires changing scope, stop and open a Change Request.

## Quality gates

Before completion:

- Run relevant lint/typecheck/test/build commands.
- Run relevant planning-doc checks for docs.
- Update docs if behavior changed.
- Confirm acceptance criteria.
- Summarize changed files.
- List tests run and tests not run.
- List unresolved risks.

## Documentation map

- `docs/AGENTIC_WORKFLOW_MANUAL.md`: human-facing framework manual, copy kit, prompt index, and troubleshooting.
- `docs/project-charter.md`: stable product/project summary.
- `docs/repo-map.md`: architecture map and commands.
- `docs/status/CURRENT_STATE.md`: active project dashboard and next-action context.
- `docs/handoff/`: concise restart packages.
- `docs/specs/`: accepted/draft requirements.
- `docs/plans/`: implementation plans.
- `docs/plans/batches/`: execution batches.
- `docs/change-requests/`: controlled scope changes.
- `docs/adr/`: architecture decisions.
- `docs/worklog/`: session notes, research evidence, and failed approaches.
- `docs/standards/`: coding, testing, docs, security, dependency standards.

## Template discipline

Use the repo-local `controlled-planning-docs` skill when writing or revising specs, plans, batch plans, Change Requests, status dashboards, handoffs, repo maps, worklogs, or other durable project documentation.

Reference `AGENTS.md` for operating modes, permissions, approval classes, git rules, hooks, and Change Requests.

Put mission-critical reusable rules in `AGENTS.md`; put task-local contracts, interfaces, fixtures, commands, and gates in the spec/plan/batch.

Delete template prompts and non-applicable sections before accepting a document.

Prefer concise tables, exact file/function/API contracts, and focused task slices over broad prose.

Plans should be executable without redesign: name files, public interfaces, validation commands, expected outputs, rollback steps, and stop conditions.

Do not paste large source material or long generated logs into specs/plans. Link to durable files and summarize only what implementation needs.
