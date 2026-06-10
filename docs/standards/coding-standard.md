# Coding Standard

## Principles

- Prefer simple, explicit, readable code.
- Keep modules cohesive and boundaries clear.
- Avoid hidden global state.
- Avoid speculative abstraction.
- Keep public APIs documented.
- Handle errors deliberately.
- Preserve existing style unless changing it is part of the accepted plan.

## Implementation expectations

- Small functions with focused responsibilities.
- Clear names over clever names.
- No broad refactors inside feature work unless accepted in the plan.
- No dead code.
- No TODOs without issue/spec reference.
- No generated code edits unless documented.

## Comments

Use comments to explain why, not what. Public APIs should have docstrings/comments where the language ecosystem expects them.
