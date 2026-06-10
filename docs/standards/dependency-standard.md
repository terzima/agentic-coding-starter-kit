# Dependency Standard

## Default stance

Prefer fewer dependencies. New production dependencies require approval.

## Approval checklist

- [ ] Package name and version.
- [ ] Why it is needed.
- [ ] Alternatives considered.
- [ ] License note.
- [ ] Maintenance signal.
- [ ] Vulnerability/advisory check.
- [ ] Lockfile diff reviewed.
- [ ] Rollback plan.

## Allowed without adding dependencies

- Using dependencies already present in the lockfile.
- Running locked install commands after explicit setup approval.

## Not allowed

- `curl ... | sh`
- arbitrary installer scripts
- global host installs
- unpinned production dependency additions
- adding a package for trivial utilities
