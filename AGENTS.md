# Agent Instructions — mcoriax.github.io

This repository is the **static documentation website** for the MCIdentity
Minecraft plugin, published with GitHub Pages from the [`docs/`](docs/) folder.
Read [`INDEX.md`](INDEX.md) for the file structure before making changes. The
design system is **not** defined here: it lives in `DESIGN.md` of
`MCEngine/mcengine.github.io`, the single source of truth for the whole
ecosystem's visual language. This site imports the shared theme over the network
from `https://mcengine.github.io/css/...` and keeps only its own custom styles
locally (see [Website repository structure](#website-repository-structure)).

---

## Iron Rules

### 1. Never expose internal source code

This is a **public, user-facing** documentation site. It documents how to *use*
the plugin, never how it is built inside.

* **Do not** copy the plugin's implementation (Java classes, method bodies,
  internal fields, private helpers, package-internal logic) onto any page.
* For the API, show **only the usage of the provider class** and the public
  contract: how a consumer calls `MCIdentityProvider`, the public method
  signatures, parameters, and return types, and how to listen to the public
  Bukkit events (accessors, cancellable status). Nothing about how those are
  implemented.
* Code blocks are allowed only when they are **consumer-facing usage**:
  * calling the public API (`provider.getActiveIdentity(...)`, etc.),
  * a third-party plugin's own listener class,
  * build configuration (`build.gradle`, `plugin.yml`),
  * server-owner **configuration** (`config.yml`, `professions/*.yml`).
* If an example seems to require internal source to explain something, describe
  the behaviour in prose instead and link to the public API surface.

When in doubt, ask: *"Would this line appear in the plugin's own source tree?"*
If yes, it does not belong on the site.

### 2. Keep the site self-contained (except the shared theme)

No external fonts, CDNs, trackers, or third-party network calls at runtime.
Everything ships in-repo **except the shared MCEngine theme**, which is imported
from `https://mcengine.github.io/...` (never raw content URLs, never local
copies). Inline small SVGs / data URIs when an asset is needed. This keeps the
site fast, private, and CSP-friendly.

### 3. Follow the existing conventions

* Every page includes the shared header/footer via the client-side loader
  (`docs/js/site.js` + `docs/partials/`). Do not hard-code the nav into a page.
* The shared theme (root tokens, layout, components) is imported from
  `https://mcengine.github.io/css/` — `main.css`, `shared/layout.css`, and
  `shared/components.css`. Do not copy them into this repository.
* Local CSS under `docs/css/` is for **custom styles only**: one folder per
  section (`docs/css/{section}/`) plus `docs/css/custom/custom.css`, which holds
  this site's header/footer extras (brand logo, donation link, Platforms
  dropdown, footer bar) that are not part of the shared theme.
* Use the design tokens and components from `MCEngine/mcengine.github.io`'s
  `DESIGN.md`; do not invent new colors or one-off styles.
* Keep files focused (one page = one folder). Prefer editing shared partials
  over duplicating markup.

---

## Website repository structure

Every site in the MCEngine ecosystem shares this repository layout. `{org}` is
this repository's organization/name and `{section}` is a page folder (for
example `home`, `api`, `logs`).

```
{org}.github.io/
├── AGENTS.md                         # agent rules for this repository (this file)
├── INDEX.md                          # repository structure index
├── README.md                         # human-facing project overview
└── docs/                             # served by GitHub Pages (Settings → Pages → branch master, folder /docs)
    ├── index.html                    # homepage
    ├── {section}/index.html          # one folder per page/section
    ├── css/                          # OPTIONAL — only this repo's OWN custom styles
    │   └── {section}/{section}.css   #   per-section stylesheet (custom only)
    ├── js/                           # OPTIONAL — page scripts (e.g. site.js include loader)
    └── partials/                     # OPTIONAL — shared header/footer fragments
        ├── header.html
        └── footer.html
```

### Shared theme — single source of truth

The visual language (design tokens, layout, and components) is defined **once**
in `MCEngine/mcengine.github.io` and consumed by every site over the network —
it is never copied into this repository:

* `DESIGN.md` in `MCEngine/mcengine.github.io` is the single source of truth for
  the design system. This repository keeps **no** `DESIGN.md` of its own.
* The shared stylesheets are served from `https://mcengine.github.io/`. Import
  them in every page's `<head>` — either the modular theme:

  ```html
  <link rel="stylesheet" href="https://mcengine.github.io/css/main.css">
  <link rel="stylesheet" href="https://mcengine.github.io/css/shared/layout.css">
  <link rel="stylesheet" href="https://mcengine.github.io/css/shared/components.css">
  ```

  or, for pages built on the single-file theme with page transitions:

  ```html
  <link rel="stylesheet" href="https://mcengine.github.io/styles/main/style.css">
  <script src="https://mcengine.github.io/scripts/main/script.js" defer></script>
  ```

* Add a local `docs/css/{section}/{section}.css` **only** when this repository
  needs its own custom, per-page styling. Never re-create the shared theme files
  locally, and never use raw `raw.githubusercontent.com` URLs.

---

## How to add or update content

### Add a new page

1. Create `docs/{section}/index.html`.
2. Set the correct relative root in `<head>`:
   `window.SITE_ROOT = "<relative-path-back-to-docs>/"` (e.g. `"../"` one level
   deep, `"../../"` two levels deep) and `window.PAGE_SECTION = "<section>"`.
3. Import the shared theme with absolute URLs
   (`https://mcengine.github.io/css/main.css`,
   `.../css/shared/layout.css`, `.../css/shared/components.css`), then link the
   local `css/custom/custom.css` and a per-section stylesheet
   `css/{section}/{section}.css`, both prefixed with the same relative root.
4. Add `<div id="site-header"></div>` at the top of `<body>` and
   `<div id="site-footer"></div>` before the `site.js` script.
5. If it is a top-level section, add a nav link in
   `docs/partials/header.html` using the `{{ROOT}}` token and a matching
   `data-section` value, and a footer link if appropriate.
6. Update [`INDEX.md`](INDEX.md).

### Add or change a profession

Profession pages are generated — do not hand-edit them. Update the data in
[`scripts/generate_professions.py`](scripts/generate_professions.py) (it mirrors
the plugin's default `professions/*.yml`) and regenerate:

```bash
python3 scripts/generate_professions.py
```

---

## How to create a change log

Logs use a **versioned directory structure** so every published build gets a
permanent URL: `docs/logs/{major}/{minor}/{patch}/index.html` (for example
`docs/logs/1/0/0/`, `docs/logs/1/0/1/`, `docs/logs/1/1/0/`, `docs/logs/2/0/0/`).

`docs/logs/index.html` always mirrors the **latest** release; each versioned
page is the permalink for that specific version. To publish a new log for
version `X.Y.Z`:

1. **Create the versioned page** `docs/logs/X/Y/Z/index.html`.
   * Copy the layout of the most recent versioned page
     (`docs/logs/1/0/0/index.html`) as a starting point.
   * A page four levels deep sets `window.SITE_ROOT = "../../../../"`. Import the
     shared theme with absolute `https://mcengine.github.io/css/...` URLs, then
     link the local `css/custom/custom.css` and `css/logs/logs.css` with that
     same prefix. Use `window.PAGE_SECTION = "logs"`.
   * Fill in the version, date, and change sections. Use the
     `log-tag--new` / `log-tag--improve` / `log-tag--note` labels for
     Added / Changed / Notes.
2. **Update the right-side version navigation** (`.logs-nav`) so it lists every
   version, newest first. Give the newest entry `class="is-current"` on its own
   page and the `Latest` pill; remove the `Latest` pill from the previous
   newest.
3. **Refresh `docs/logs/index.html`** to show the new version's content as the
   latest entry, mark it `badge--ok "Latest"`, and update its version list to
   include the new version (pointing at `X/Y/Z/index.html`).
4. **Content rule:** describe *what changed for users and integrators* —
   features, fixes, config, and public-API changes only. Never paste internal
   implementation details (see Iron Rule 1).
5. Update [`INDEX.md`](INDEX.md) with the new log path.

> Semantic Versioning: `Major.Minor.Patch`. Keep the directory numbers in sync
> with the plugin's released version.

---

## Verifying changes

Serve the site locally and click through the affected pages — header/footer must
load, links must resolve, and there should be no console errors:

```bash
python3 -m http.server 8000 --directory docs
# then open http://localhost:8000/
```

Because the header/footer are fetched at runtime, always test over HTTP (the
command above), not by opening files directly.
