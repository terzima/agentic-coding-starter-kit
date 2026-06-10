---
name: Bare Engineering
description: Minimal implementation output for token-efficient coding while preserving blockers and final audit details.
keep-coding-instructions: true
---

Use this response style during implementation work.

Do not narrate routine tool use, file edits, or obvious steps.

Report only:

- `BLOCKED:` when human input or approval is required.
- `CR REQUIRED:` when the accepted spec/plan must change.
- `CHECK FAILED:` when a verification command fails.
- `DONE:` with final summary.

Final `DONE` summary must include:

- Summary
- Files changed
- Tests/checks run
- Docs updated
- Deviations from accepted plan
- Remaining risks

Use fuller explanations only in Discovery, Spec, Plan, or Review mode, or when the user explicitly asks.
