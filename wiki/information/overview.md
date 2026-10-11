# Project Overview

[← Back to README](../../README.md)

## Project identity

| | |
|---|---|
| **Platform** | [github.com](https://github.com) |
| **Organization** | [MCOriax](https://github.com/MCOriax) |
| **Repository** | [mcoriax.github.io](https://github.com/MCOriax/mcoriax.github.io) |
| **Live site** | <https://mcoriax.github.io/> |

## What this repository is

The documentation website for the **MCIdentity** Minecraft plugin and its
**MCIdentitySkill**, **MCIdentityRune**, **MCIdentityCosmetic**, and **MCIdentityPerks** add-ons and the **MCIdentity Central Server**,
published with GitHub Pages.

It is plain, self-contained static HTML — no build step, no framework, and no
external fonts, scripts, or stylesheets.

## Two trees, two purposes

| Tree | Holds |
|---|---|
| `docs/` | **The published site.** Everything under it is served by GitHub Pages. |
| `wiki/` | **Documentation about the site** — how it is assembled and how to change it. Not published. |

Do not confuse them. A page a visitor reads lives in `docs/`; a page explaining
how to add that page lives in `wiki/`.

## What the site documents

| Section | Covers |
|---|---|
| Features, Installation, Storage, GUI, Commands | The core MCIdentity plugin. |
| API, Listeners | The developer surface for third-party plugins. |
| Profession | One generated page per bundled profession, plus the EXP action reference. |
| Skill, Rune, Cosmetic, Perks | The standalone add-ons. Perks is in development. |
| Server | The MCIdentity Central Server. |
| Platforms | SpigotMC, PaperMC, and FoliaMC guides. |
| Logs | Versioned change logs, with a separate version tree per product. |

## The rule that shapes every page

This is a **public, user-facing** site. It explains what each MCOriax project is
and how it works, in prose and tables. **No page contains code or code snippets
of any kind**, not even build or configuration examples, and implementation
details never appear on a page. See
[`../../.agents/rules/repository.md`](../../.agents/rules/repository.md) for the
full iron rules.

## Where to go next

| Page | For |
|---|---|
| [Site Architecture](architecture.md) | How pages are assembled at runtime. |
| [Site Structure](../reference/site-structure.md) | Every file under `docs/`, with its purpose. |
| [Local Setup](../environments/setup.md) | Serving the site and configuring Pages. |
| [Add a Page](../guides/add-a-page.md) | Adding a new section. |
