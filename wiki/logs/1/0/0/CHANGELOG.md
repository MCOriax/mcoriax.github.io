# Changelog — 1.0.0

**Released:** 2026-08-09

Adds the agent instruction architecture and a `wiki/` documentation tree to the
repository. The published site under `docs/` is unchanged.

## Added

- `.agents/creators/` with four creator instructions: `instruction-creator.md`,
  `information-creator.md`, `changelog-creator.md`, and `index-creator.md`. Each
  embeds the branch and commit convention and the discovery protocol in full.
- `.agents/planning/task-workflow.md` — Goal/Objective/Detail intake, task
  decomposition, one stacked branch per task, in-order execution, and one pull
  request per branch merged in order after user approval.
- `.agents/git/branching-strategy.md` and `.agents/git/commit-conventions.md`,
  split out of the former single `git/workflow.md`.
- `.agents/git/pull-request-template.md` — human-readable pull request titles and
  the required Overview / Added / Modified / Deleted / Summary body.
- `.agents/rules/directories.md` — the placement authority for `.agents/` and
  `wiki/`, absorbing the retired `architecture/agent-directories.md`.
- `.agents/rules/versioning.md` — forbids claiming a release or editing the
  version navigation without explicit user approval.
- `.agents/prompts/branch-and-commit.md` — standing prompt so the convention
  never has to be restated.
- A `wiki/` tree documenting how the site is built: `information/overview.md`,
  `information/architecture.md`, `reference/site-structure.md`,
  `environments/setup.md`, and three guides covering adding a page, publishing a
  change log, and regenerating the profession pages.
- `wiki/INDEX.md` and `wiki/logs/INDEX.md` routing indexes.
- `LICENSE` placeholder, pending the licensing decision.

## Changed

- Every `.agents/` file now carries `name` + `description` frontmatter.
- `.agents/INDEX.md` rewritten to the canonical index template with a scope line
  and a parent link.
- `.agents/rules/execution.md` reconciled with the new architecture: the rule
  requiring a version bump on every pull request is superseded by
  `rules/versioning.md`, and the flat `wiki/*.md` file list is replaced by the
  `wiki/{folder}/{file}.md` placement algorithm.
- Root `INDEX.md` reduced to a pure router; the 85-row site map it carried moved
  to `wiki/reference/site-structure.md`.
- Root `AGENTS.md` rewritten as an overview with the mandatory reading order,
  routing protocol, iron rules, and discovery protocol.
- `README.md` reduced to an overview; its detail moved into `wiki/` pages.

## Removed

- `.agents/README.md` and the per-folder `README.md` files in `rules/`, `git/`,
  and `architecture/` — their folder summaries are now index rows, and an
  uppercase `README.md` is not permitted under `.agents/` (only `INDEX.md` is).
- `.agents/architecture/index-template.md` — the index template it defined is now
  owned by `creators/index-creator.md`.
- `.agents/architecture/agent-directories.md` — superseded by
  `rules/directories.md`.
- `.agents/architecture/website.md` — it was documentation, not an instruction;
  its content became the `wiki/` architecture page and the three guides.
