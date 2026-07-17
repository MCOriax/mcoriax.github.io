# Agent Instructions — mcoriax.github.io

This repository is the **static documentation website** for the MCIdentity
Minecraft plugin, published with GitHub Pages from the [`docs/`](docs/) folder.
Read [`INDEX.md`](INDEX.md) for the file structure and [`DESIGN.md`](DESIGN.md)
for the design system before making changes.

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

### 2. Keep the site self-contained

No external fonts, scripts, stylesheets, CDNs, trackers, or network calls at
runtime. Everything ships in-repo. Inline small SVGs / data URIs when an asset
is needed. This keeps the site fast, private, and CSP-friendly.

### 3. Follow the existing conventions

* Every page includes the shared header/footer via the client-side loader
  (`docs/js/site.js` + `docs/partials/`). Do not hard-code the nav into a page.
* CSS lives under `docs/css/` — root tokens in `main.css`, cross-page styles in
  `docs/css/shared/`, and one folder per section (`docs/css/{section}/`).
* Use the design tokens and components from [`DESIGN.md`](DESIGN.md); do not
  invent new colors or one-off styles.
* Keep files focused (one page = one folder). Prefer editing shared partials
  over duplicating markup.

---

## How to add or update content

### Add a new page

1. Create `docs/{section}/index.html`.
2. Set the correct relative root in `<head>`:
   `window.SITE_ROOT = "<relative-path-back-to-docs>/"` (e.g. `"../"` one level
   deep, `"../../"` two levels deep) and `window.PAGE_SECTION = "<section>"`.
3. Link `css/main.css`, `css/shared/layout.css`, `css/shared/components.css`,
   and a per-section stylesheet `css/{section}/{section}.css`, all prefixed with
   the same relative root.
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
   * A page four levels deep sets `window.SITE_ROOT = "../../../../"` and links
     the stylesheets (`main.css`, `shared/layout.css`, `shared/components.css`,
     `logs/logs.css`) with that same prefix. Use `window.PAGE_SECTION = "logs"`.
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
