---
name: wiki-index
description: Index of wiki/ — documentation about how this documentation site is built and maintained.
---

# Wiki Index

**Scope:** `wiki/`
**Parent:** [root-index](../INDEX.md)

These pages document **how the site is built and maintained**. The site's own
published content lives in `docs/` and is served by GitHub Pages — it is not
part of this tree.

Any page added to or removed from `wiki/` is reflected here in the same commit.
This index never writes into `.agents/`.

## Information

| File | Purpose |
|---|---|
| [`information/overview.md`](information/overview.md) | What this repository is and what it publishes. |
| [`information/architecture.md`](information/architecture.md) | How the site is assembled: runtime includes, the vendored theme, and the repository layout. |

## Guides

| File | Purpose |
|---|---|
| [`guides/add-a-page.md`](guides/add-a-page.md) | Adding a new section page to the site. |
| [`guides/publish-a-change-log.md`](guides/publish-a-change-log.md) | Publishing a new versioned change log and updating the navigation. |
| [`guides/regenerate-professions.md`](guides/regenerate-professions.md) | Regenerating the profession pages from the bundled data. |

## Reference

| File | Purpose |
|---|---|
| [`reference/site-structure.md`](reference/site-structure.md) | Every directory and file under `docs/` and `scripts/`, with its purpose. |

## Environments

| File | Purpose |
|---|---|
| [`environments/setup.md`](environments/setup.md) | Serving the site locally and configuring the GitHub Pages source. |

## Child Indexes

| Index | Scope | Load when |
|---|---|---|
| [`logs/INDEX.md`](logs/INDEX.md) | Versioned change logs | You need release history or must record a change. |
