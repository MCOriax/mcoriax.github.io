---
name: commit-conventions
description: Conventional Commits formatting rules for commit messages in this repository.
---

# Git: Commit Conventions

Use Conventional Commits: `type(optional scope): description`.

## Types

`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`,
`chore`, `revert`.

## Scopes

Prefer a section or subsystem scope, e.g. `docs(logs):`, `feat(nav):`,
`style(theme):`, `fix(partials):`, `chore(scripts):`.

## Rules

* Subject line in plain text, imperative mood, no trailing period.
* **No links and no issue-tracker IDs** in the message.
* Body (optional) explains what and why as short bullet points.
* Commit each change or group of related changes; do not batch an entire session
  into one commit. Always review the diff before committing.

## Examples

```
feat(nav): add the add-ons dropdown to the shared header

- List the skill, rune, and cosmetic pages
- Resolve links through the {{ROOT}} token so depth stays correct
```

```
fix(logs): drop the stale Latest badge from the superseded permalink
```

## Scope

**This format applies to commit messages only. Pull request titles use a
different format** — a plain, human-readable phrase with no `feat:` / `fix:` /
`chore:` prefix. See
[`pull-request-template.md`](pull-request-template.md).
