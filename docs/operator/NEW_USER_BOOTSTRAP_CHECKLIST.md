# New User Bootstrap Checklist

Use this checklist when a new person copies the agentic coding starter kit into a real project repo.

The goal is to configure the repo for controlled agentic development before any application implementation begins.

This checklist should be completed once per new repo.

---

## 1. Copy the starter kit into the repo

Minimum files/directories to copy:

```txt
AGENTS.md
README.md
START_HERE.md
AGENTIC_CODING_GUIDELINES.md
PROMPT_LIBRARY.md
BOUNDARY_AND_SANDBOX_POLICY.md
LARGE_SPEC_SEEDING_PLAYBOOK.md
docs/
.github/
.githooks/
scripts/
```

Do not copy old project-specific docs from another project unless they are intentionally being adapted.

---

## 2. Confirm repo identity

Update project-specific placeholders in:

```txt
README.md
docs/project-charter.md
docs/repo-map.md
docs/roadmap.md
```

If these files do not exist yet, they will be created during seeding.

---

## 3. Install local Git hooks

Run:

```bash
chmod +x scripts/agent/*.sh .githooks/*
bash scripts/agent/install_git_hooks.sh
```

Expected result:

```txt
core.hooksPath=.githooks
```

Verify:

```bash
git config --get core.hooksPath
```

This should print:

```txt
.githooks
```

---

## 4. Review the permission model

Read:

```txt
BOUNDARY_AND_SANDBOX_POLICY.md
AGENTS.md
```

Confirm the repo uses this default policy:

```txt
Inside repo: mostly autonomous
Outside repo: no
Internet: ask
Dependencies: ask
Secrets/system: never
Git local: yes
Git remote: ask
```

Do not start implementation until this is clear.

---

## 5. Confirm agent output style

For implementation work, use bare engineering output:

```txt
Mode: Implementation.
Output style: bare engineering.

Do not narrate routine steps.
Only report blockers, change requests, test failures, or final summary.
```

Do not use bare output for:

```txt
project seeding
spec writing
planning
review
architecture decisions
```

Those modes need visible reasoning.

---

## 6. Add the raw project overview

Create:

```txt
docs/intake/PROJECT_OVERVIEW_RAW.md
```

Paste the full founding overview into that file.

This file may be long, rough, and exploratory.

It is not the permanent working spec.

---

## 7. Run the seeding prompt

Use the seeding prompt from:

```txt
PROMPT_LIBRARY.md
```

The seeding pass should produce:

```txt
docs/project-charter.md
docs/glossary.md
docs/repo-map.md
docs/roadmap.md
docs/specs/SPEC-0000-project-foundation.md
docs/specs/SPEC-0001-application-scaffold.md
docs/plans/PLAN-0001-application-scaffold.md
docs/plans/batches/BATCH-0001-application-scaffold.md
docs/seed/SEED-0000-project-decomposition.md
docs/seed/SEED-0000-results.md
docs/worklog/0000-seeding-notes.md
```

It may produce an ADR only if architecture choices are explicit or strongly implied.

---

## 8. Do not overproduce specs and plans

During seeding, the agent should be broad but shallow.

Expected output depth:

```txt
Always:
- project charter
- glossary
- repo map
- roadmap
- foundation spec
- seeding notes

Usually:
- 1–3 initial specs
- 1–3 matching plans
- 1–2 proposed batches

Not yet:
- 20 full specs
- 20 full plans
- late-stage implementation details
- production code
```

Future work should remain as roadmap items, spec candidates, ADR candidates, open questions, or deferred decisions.

---

## 9. Review seeded docs before implementation

Run a review-only prompt.

The review should check:

```txt
- Are specs implementation-safe?
- Are plans small enough?
- Are batches grouped correctly?
- Is BATCH-0001 ready?
- Is the first human-testable milestone clear?
- Are approval classes correct?
```

Do not code during this review.

---

## 10. Execute the application scaffold batch

The first implementation batch should usually be:

```txt
docs/plans/batches/BATCH-0001-application-scaffold.md
```

This batch creates the actual software structure, such as:

```txt
backend/
frontend/
shared/
tests/
.env.example
Makefile
docs/setup/local-prerequisites.md
```

It should not implement product behavior.

---

## 11. Configure project-specific commands

Once the application scaffold exists, update:

```txt
Makefile
README.md
docs/repo-map.md
docs/setup/local-prerequisites.md
```

These should define:

```txt
install command
dev command
test command
lint command
typecheck command
build command
format command
```

Future agents should use these commands instead of guessing.

---

## 12. Dependency and network policy

Agents may propose dependencies.

Agents must ask before:

```txt
npm install
pnpm add
pip install
uv add
brew install
docker pull
git clone
curl
wget
```

If approval is needed, the agent must provide:

```txt
Action:
Exact command:
Why needed:
Scope:
Risk:
Fallback if denied:
```

---

## 13. Git policy

Agents may usually run:

```bash
git status
git diff
git add
git commit
git branch
git checkout -b
```

Agents should ask before:

```bash
git push
gh pr create
gh pr merge
```

Use local commits freely inside task branches.

Use PRs for meaningful review units, not every tiny spec.

---

## 14. First optimization pass

After application scaffold exists, run an optimization review.

Ask the agent to check:

```txt
- Are repeated instructions moved into AGENTS.md or docs?
- Are commands centralized in Makefile/package scripts?
- Are specs/plans concise?
- Are future agents told what not to read?
- Are approval classes assigned?
- Are hooks installed?
- Is README useful for a new developer?
- Is PROJECT_OVERVIEW_RAW.md no longer required for routine work?
```

The goal is to reduce repeated context and approval noise before real implementation accelerates.

---

## 15. Ongoing maintenance

Update the starter-kit control docs when:

```txt
repo structure changes
commands change
approval policy changes
agent behavior needs correction
new recurring failure modes are discovered
```

Do not update governance docs for every small feature.

The control layer should stay durable, concise, and stable.
