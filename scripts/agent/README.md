# Scripts Directory

This directory contains utility scripts for setting up and enforcing the agentic development workflow.

Scripts should be small, readable, and safe by default.

They should never silently install global dependencies, access secrets, modify system settings, or use the network unless the user explicitly approved that action.

---

## Directory layout

Recommended structure:

```txt
scripts/
  agent/
    install_git_hooks.sh
    verify_agent_setup.sh
    check_repo_boundaries.sh
    check_for_sensitive_files.sh
    print_agent_context.sh

  dev/
    setup_local.sh
    check_prerequisites.sh
    run_all_checks.sh

  maintenance/
    audit_docs.sh
    audit_specs_plans.sh
```

Not every project needs every script.

Start small and add scripts only when they reduce repeated manual work or repeated agent confusion.

---

## Script categories

### `scripts/agent/`

Scripts used to support safe agent operation.

Examples:

```txt
install_git_hooks.sh
verify_agent_setup.sh
check_repo_boundaries.sh
check_for_sensitive_files.sh
print_agent_context.sh
```

These scripts should not modify application behavior.

### `scripts/dev/`

Scripts used by humans and agents during normal local development.

Examples:

```txt
check_prerequisites.sh
setup_local.sh
run_all_checks.sh
```

These may depend on the actual project stack.

### `scripts/maintenance/`

Scripts used to audit documentation/process health.

Examples:

```txt
audit_docs.sh
audit_specs_plans.sh
```

---

## Required first scripts

A new repo should usually include at least these scripts.

### 1. `scripts/agent/install_git_hooks.sh`

Purpose:

```txt
Configure Git to use the repo's .githooks directory.
```

Expected behavior:

```bash
git config core.hooksPath .githooks
```

This is safe and repo-local.

It should not install external tools.

### 2. `scripts/agent/verify_agent_setup.sh`

Purpose:

```txt
Check whether the repo is ready for controlled agentic work.
```

Should verify:

```txt
AGENTS.md exists
docs/repo-map.md exists or is pending seeding
docs/intake/PROJECT_OVERVIEW_RAW.md exists before seeding
.githooks is configured
README.md exists
PROMPT_LIBRARY.md exists
BOUNDARY_AND_SANDBOX_POLICY.md exists
```

It should report missing items but not make broad changes.

### 3. `scripts/dev/check_prerequisites.sh`

Purpose:

```txt
Check required local tools for the project.
```

Should verify project-specific tools, such as:

```txt
node
npm / pnpm / yarn
python3
uv / pip
go
flutter
docker
git
gh
```

depending on the project.

It may check versions.

It must not install missing tools without approval.

### 4. `scripts/dev/run_all_checks.sh`

Purpose:

```txt
Run the project's standard verification commands.
```

This should become the agent's default validation command.

Examples:

```bash
npm run lint
npm run typecheck
npm test
npm run build
```

or:

```bash
ruff check .
mypy .
pytest
```

or project-specific equivalents.

---

## Script safety rules

Scripts must not do these things without explicit approval:

```txt
install dependencies
install global packages
use network access
modify files outside repo
read secrets
use sudo
change OS settings
delete many files
run destructive database operations
push to remote Git
create or merge PRs
```

Scripts may do these things by default:

```txt
inspect repo files
check installed tool versions
run tests/lint/typecheck/build
configure repo-local Git hooks
print setup diagnostics
create missing documentation directories when explicitly scoped
```

---

## Recommended script headers

Every script should start with:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

For scripts that operate from repo root, add:

```bash
ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"
```

---

## Example: install Git hooks

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

git config core.hooksPath .githooks

echo "Configured Git hooks path:"
git config --get core.hooksPath
```

---

## Example: verify agent setup

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

missing=0

check_file() {
  if [[ ! -f "$1" ]]; then
    echo "MISSING: $1"
    missing=1
  else
    echo "OK: $1"
  fi
}

check_dir() {
  if [[ ! -d "$1" ]]; then
    echo "MISSING: $1"
    missing=1
  else
    echo "OK: $1"
  fi
}

check_file "AGENTS.md"
check_file "README.md"
check_file "PROMPT_LIBRARY.md"
check_file "BOUNDARY_AND_SANDBOX_POLICY.md"
check_dir "docs"
check_dir "docs/intake"
check_dir "docs/specs"
check_dir "docs/plans"
check_dir "docs/plans/batches"
check_dir "docs/adr"
check_dir "docs/worklog"

hooks_path="$(git config --get core.hooksPath || true)"
if [[ "$hooks_path" != ".githooks" ]]; then
  echo "MISSING: git core.hooksPath is not .githooks"
  missing=1
else
  echo "OK: git hooks path is .githooks"
fi

if [[ "$missing" -eq 1 ]]; then
  echo "Agent setup verification failed."
  exit 1
fi

echo "Agent setup verification passed."
```

---

## Example: check prerequisites

This is project-specific. Keep it conservative.

```bash
#!/usr/bin/env bash
set -euo pipefail

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "MISSING: $1"
    missing=1
  else
    echo "OK: $1 -> $($1 --version 2>/dev/null | head -n 1 || true)"
  fi
}

missing=0

need git

# Uncomment only when the actual stack requires them.
# need node
# need npm
# need python3
# need docker
# need go
# need flutter

if [[ "$missing" -eq 1 ]]; then
  echo
  echo "One or more prerequisites are missing."
  echo "Do not install automatically. Ask the user for approval with exact commands."
  exit 1
fi

echo "Prerequisite check passed."
```

---

## Example: run all checks

This should be updated once the project stack is known.

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(git rev-parse --show-toplevel)"
cd "$ROOT_DIR"

if [[ -f "package.json" ]]; then
  npm run lint --if-present
  npm run typecheck --if-present
  npm test --if-present
  npm run build --if-present
fi

if [[ -f "pyproject.toml" ]]; then
  command -v ruff >/dev/null 2>&1 && ruff check . || true
  command -v mypy >/dev/null 2>&1 && mypy . || true
  command -v pytest >/dev/null 2>&1 && pytest || true
fi
```

Important: avoid hiding meaningful failures. This example is intentionally conservative, but once the stack is chosen, remove `|| true` from required checks.

---

## When agents should add scripts

Agents may add or modify scripts when:

```txt
a command is repeated often
setup steps are becoming ambiguous
validation needs to be standardized
a safety check can prevent a recurring mistake
a script reduces token usage by replacing repeated instructions
```

Agents should not add scripts just to make the repo look sophisticated.

Every script should have a clear purpose.

---

## When scripts should be referenced

If a script becomes the preferred way to perform a task, reference it in:

```txt
README.md
docs/repo-map.md
AGENTS.md
```

Example:

```txt
To run all checks, use:

bash scripts/dev/run_all_checks.sh
```

Future agents should use documented scripts instead of inventing command sequences.

---

## New-user optimization items

When a new user starts a real project from this kit, they should complete these optimization items early:

1. Install repo-local Git hooks.
2. Verify agent setup.
3. Add the raw project overview.
4. Run seeding.
5. Review seeded docs.
6. Create the application scaffold spec/plan/batch.
7. Define local prerequisite documentation.
8. Define canonical run/test/lint/build commands.
9. Add `run_all_checks.sh` or equivalent.
10. Update README with real setup commands.
11. Confirm approval classes.
12. Confirm dependency/network policy.
13. Confirm that future agents do not need to reread the raw overview.
14. Keep `AGENTS.md` concise.
15. Move recurring workflow details into scripts or docs instead of prompts.

---

## Script philosophy

Scripts are part of token optimization.

A script turns repeated prompt instructions like:

```txt
run lint, run tests, run typecheck, check docs, verify hooks
```

into one stable command:

```bash
bash scripts/dev/run_all_checks.sh
```

That reduces tokens, reduces mistakes, and gives future agents a documented command surface.

Prefer scripts when the same instruction would otherwise be repeated across multiple agent sessions.
