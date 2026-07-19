# Website structure — mcoriax.github.io

This repository's own site structure and how-to guides.

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

### Shared theme — vendored locally

The visual language (design tokens, layout, and components) is the shared
MCEngine "Silver Glass" design system, documented in this repository's own
`DESIGN.md` (a copy kept in sync with the canonical `DESIGN.md` in
`MCEngine/mcengine.github.io`). Each site vendors its own copy of the theme
locally so it has no runtime dependency on another repository:

* The theme files live under `docs/css/` in this repository: `main.css` (root
  tokens), `shared/layout.css` and `shared/components.css` (cross-page styles),
  and one folder per section (`docs/css/{section}/`).
* Every page links these local files with **relative** paths. Never import a
  stylesheet or script over the network (`https://mcengine.github.io/...` or raw
  content URLs).
* Add a local `docs/css/{section}/{section}.css` for this site's own custom,
  per-page styling.

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
     the stylesheets (`css/main.css`, `css/shared/layout.css`,
     `css/shared/components.css`, `css/logs/logs.css`) with that same prefix. Use
     `window.PAGE_SECTION = "logs"`.
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
