---
name: branching-strategy
description: Branch off the default branch, one task per branch, {type}/{primary-noun} naming, stacked in dependency order.
---

# Git: Branching Strategy

## Base

* Branch off the default branch (`master`) for every task. Never work directly on
  `master` or `main`.
* One task per branch, one pull request per branch, merged separately.
* Create a new branch if the task scope changes; otherwise continue on the active
  branch.
* Keep branches short-lived and rebased on the default branch.
* For multi-task work, branches **stack in dependency order** — task 1 branches
  off the default branch, task `k` branches off task `k-1`. See
  [`../planning/task-workflow.md`](../planning/task-workflow.md).

## Naming

* Follow `{type}/{primary-noun}`, e.g. `feat/login`, `docs/agents-setup`,
  `fix/logs-nav`.
* Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
  `build`, `ci`, `chore`, `revert`.
* **Absolutely do not use tool-preset prefixes** such as `claude/`, `codex/`, or
  `cursor/`. If a branch does not follow the convention, recreate it under the
  correct name and delete the incorrect one, or present the options to the user.

## Change tags

Distinguish the nature of the change so reviewers know the blast radius:

* **Shared partial or script changes** — edits to `docs/partials/` or
  `docs/js/site.js` affect **every page** on the site. Call these out explicitly
  in the pull request body.
* **Theme changes** — edits to `docs/css/main.css` or `docs/css/shared/` affect
  every page; per-section stylesheets under `docs/css/{section}/` do not.
* **Single-page content** — a change confined to one `docs/{section}/index.html`
  is the lowest risk and reviewable independently.
* **Generated pages** — profession pages are generated. A change there must come
  from `scripts/generate_professions.py`, never a hand edit.
