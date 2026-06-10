# Cursor Adapter Notes

The starter repo includes `.cursor/rules/agentic-development.mdc` for always-on repo behavior.

Cursor rules are not a security boundary. Use them for behavior steering, and rely on:

- Git hooks
- GitHub branch protection
- CI checks
- agent sandbox/approval settings
- human PR review

Keep Cursor rules short. Put detailed workflows in docs and skills instead.
