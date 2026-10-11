---
name: repository-rules
description: Rules specific to this documentation site — never expose internal source, stay self-contained, follow the existing conventions.
---

# Repository-specific rules — mcoriax.github.io

This repository is the **static documentation website** for the MCIdentity
Minecraft plugin, published with GitHub Pages from the [`docs/`](../../docs/) folder.
Read [`../../wiki/reference/site-structure.md`](../../wiki/reference/site-structure.md)
for the file structure and [`../../DESIGN.md`](../../DESIGN.md) for the design
system before making changes. `DESIGN.md` is this repository's own
copy of the shared MCEngine "Silver Glass" design system; keep it aligned with
the canonical copy in `MCEngine/mcengine.github.io`. The theme CSS is vendored
locally under `docs/css/` — this site has no runtime dependency on another
repository (see
[`../../wiki/information/architecture.md`](../../wiki/information/architecture.md)).

---

## Iron Rules

### 1. Never expose internal source code

This is a **public, user-facing** documentation site. It documents how to *use*
the plugin, never how it is built inside.

* **No page may contain code or code snippets of any kind.** That covers
  `<pre>` and `<code>` elements, and also code written out as plain text: Java,
  build files, configuration files, method signatures, and package or class
  paths.
* Describe behaviour in prose and tables instead: what each project is, how it
  works, and what a reader can do with it. Configuration becomes sentences such
  as "switch the storage type to the central server"; EXP rules become tables
  of conditions and rewards.
* Names a reader has to type stay as ordinary words: commands such as
  /identity, permission nodes, and the names of the libraries' modules.
* Never describe how the plugin is built inside: no internal classes, fields,
  or helpers.

When in doubt, ask: *"Is this something a reader would copy into a file?"* If
yes, it does not belong on the site.

### 2. Keep the site self-contained

No external fonts, scripts, stylesheets, CDNs, trackers, or network calls at
runtime. Everything ships in-repo, including this repository's own copy of the
shared theme. Inline small SVGs / data URIs when an asset is needed. This keeps
the site fast, private, and CSP-friendly.

### 3. Follow the existing conventions

* Every page includes the shared header/footer via the client-side loader
  (`docs/js/site.js` + `docs/partials/`). Do not hard-code the nav into a page.
* CSS lives under `docs/css/` — root tokens in `main.css`, cross-page styles in
  `docs/css/shared/` (`layout.css`, `components.css`), and one folder per section
  (`docs/css/{section}/`). This site's header/footer extras (brand logo, donation
  link, Platforms dropdown, footer bar) live in `docs/css/shared/layout.css`.
* Use the design tokens and components from [`../../DESIGN.md`](../../DESIGN.md);
  do not invent new colors or one-off styles.
* Keep files focused (one page = one folder). Prefer editing shared partials
  over duplicating markup.

---

## Companion repositories

When working on this repository, the session must always have both of these
github.com companion repositories checked out:

* `MCOriax/mcidentity` (`https://github.com/MCOriax/mcidentity.git`)
* `MCOriax/server-expressjs` (`https://github.com/MCOriax/server-expressjs.git`)

If either repository is not already present in the session, clone it before
starting work, so the documentation site stays in sync with the plugin it
documents and the backend server it describes. This is a development-time
requirement only and adds no runtime dependency; the published site remains
fully self-contained (see Iron Rule 2).

---

## Versions

Never publish a new change-log version or edit `docs/partials/logs-nav.html` to
claim a release without explicit user approval. See
[`versioning.md`](versioning.md).
