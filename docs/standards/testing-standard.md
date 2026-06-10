# Testing Standard

## Principles

- New behavior requires tests.
- Bug fixes should include regression tests when feasible.
- Tests should prove acceptance criteria, not implementation trivia.
- Prefer focused tests that fail for one clear reason.

## Required test plan per implementation plan

- Unit tests:
- Integration tests:
- End-to-end/manual verification:
- Negative/error cases:
- Regression coverage:

## Agent behavior

The agent must report tests run and tests skipped. If tests cannot run, it must explain why and propose the exact command for the human to run.

## Output filtering

When test output is large, use:

```bash
<test command> 2>&1 | scripts/agent/filter_output.py --kind test --limit 200
```
