---
name: agents-index
description: Index of .agents/ — the sole authority for the mcoriax.github.io agent instruction set.
---

# Agents Index

**Scope:** `.agents/`
**Parent:** [root-index](../INDEX.md)

This index is the sole authority that indexes and manages `.agents/`. Nothing
outside `.agents/` may dictate or write files inside this tree. Any file added to
or removed from `.agents/` is reflected here in the same commit.

Agents must use only the `.agents/` directory belonging to this repository, and
must never cross-reference another repository's `.agents/`.

## Rules

| File | Purpose |
|---|---|
| [`rules/repository.md`](rules/repository.md) | Rules specific to this site: never expose internal source, stay self-contained. |
| [`rules/iron.md`](rules/iron.md) | Platform specification and project-hosting validation. |
| [`rules/execution.md`](rules/execution.md) | Initialization, execution, modularity, documentation, and environment standards. |
| [`rules/directories.md`](rules/directories.md) | Placement authority for `.agents/` and `wiki/`, including creating a new folder. |
| [`rules/versioning.md`](rules/versioning.md) | Never publish a version or claim a release without explicit user approval. |

## Git

| File | Purpose |
|---|---|
| [`git/branching-strategy.md`](git/branching-strategy.md) | Branch naming, stacking order, and site-specific change tags. |
| [`git/commit-conventions.md`](git/commit-conventions.md) | Conventional Commits formatting rules. |
| [`git/pull-request-template.md`](git/pull-request-template.md) | Human-readable PR titles and the required body sections. |

## Planning

| File | Purpose |
|---|---|
| [`planning/task-workflow.md`](planning/task-workflow.md) | Intake, task decomposition, stacked branches, in-order merging. |

## Prompts

| File | Purpose |
|---|---|
| [`prompts/branch-and-commit.md`](prompts/branch-and-commit.md) | Standing prompt applying the branch and commit convention to every task. |

## Memory

| File | Purpose |
|---|---|
| [`memory/tasks/content-refresh.md`](memory/tasks/content-refresh.md) | Plan and outcome of the no-code content refresh released as site 1.1.0. |
| [`memory/tasks/content-refresh-findings.md`](memory/tasks/content-refresh-findings.md) | Unapplied follow-ups from the 1.1.0 refresh, for the owner to choose from. |

Memory records what happened; it never states a rule.

## Creators

| File | Purpose |
|---|---|
| [`creators/instruction-creator.md`](creators/instruction-creator.md) | Creates and maintains instruction files under `.agents/`. |
| [`creators/information-creator.md`](creators/information-creator.md) | Creates and maintains documentation pages under `wiki/`. |
| [`creators/changelog-creator.md`](creators/changelog-creator.md) | Creates and maintains versioned logs under `wiki/logs/`. |
| [`creators/index-creator.md`](creators/index-creator.md) | Owns the template, split threshold, and audit for every `INDEX.md`. |
