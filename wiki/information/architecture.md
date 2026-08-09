# Site Architecture

[← Back to README](../../README.md)

The site is plain, self-contained static HTML — no build step and no external
fonts, scripts, or stylesheets. Every page injects a shared header and footer at
runtime.

## Repository layout

Every site in the MCEngine ecosystem shares this layout. `{org}` is this
repository's organization/name and `{section}` is a page folder (for example
`home`, `api`, `logs`).

```
{org}.github.io/
├── AGENTS.md                         # agent entry point
├── INDEX.md                          # root router
├── README.md                         # human-facing project overview
├── DESIGN.md                         # the "Silver Glass" design system
├── .agents/                          # agent instruction set
├── wiki/                             # documentation about the site (not published)
└── docs/                             # served by GitHub Pages (Settings → Pages → branch master, folder /docs)
    ├── index.html                    # homepage
    ├── {section}/index.html          # one folder per page/section
    ├── css/                          # this repository's own copy of the theme
    │   └── {section}/{section}.css   #   per-section stylesheet
    ├── js/                           # page scripts (site.js include loader)
    └── partials/                     # shared fragments
        ├── header.html
        ├── footer.html
        └── logs-nav.html             #   the one place change-log versions are listed
```

## Runtime includes

Every page carries empty mounts and lets the loader fill them:

* `<div id="site-header"></div>` at the top of `<body>`.
* `<div id="site-footer"></div>` before the `site.js` script.

[`docs/js/site.js`](../../docs/js/site.js) fetches the fragments in
[`docs/partials/`](../../docs/partials/) and resolves navigation links relative
to each page's depth. It also handles favicon injection, the active-nav marker,
the mobile menu, and the log version navigation — the product picker, the
five-row scroll cap, the current release, and the back link.

Because the header and footer are fetched at runtime, the site **must be tested
over HTTP**, never by opening files directly. See
[Local Setup](../environments/setup.md).

### Depth tokens

Each page declares its own depth in `<head>`:

```html
<script>
  window.SITE_ROOT = "../";      // relative path back to docs/
  window.PAGE_SECTION = "api";   // marks the active nav entry
</script>
```

A page one level deep uses `"../"`; two levels deep `"../../"`; a change-log
page four levels deep uses `"../../../../"`. The shared header uses a `{{ROOT}}`
token that `site.js` substitutes with the same value.

## Shared theme — vendored locally

The visual language (design tokens, layout, and components) is the shared
MCEngine "Silver Glass" design system, documented in this repository's own
[`DESIGN.md`](../../DESIGN.md) — a copy kept in sync with the canonical
`DESIGN.md` in `MCEngine/mcengine.github.io`.

Each site vendors its own copy of the theme locally so it has **no runtime
dependency on another repository**:

* The theme files live under [`docs/css/`](../../docs/css/):
  `main.css` (root tokens), `shared/layout.css` and `shared/components.css`
  (cross-page styles), and one folder per section (`docs/css/{section}/`).
* Every page links these local files with **relative** paths. Never import a
  stylesheet or script over the network.
* Add a local `docs/css/{section}/{section}.css` for this site's own custom,
  per-page styling.

## Change-log architecture

Logs use a **versioned directory structure** so every published build gets a
permanent URL: `docs/logs/{major}/{minor}/{patch}/index.html`.

`docs/logs/index.html` always mirrors the **latest** release; each versioned page
is the permalink for that specific version. Each add-on keeps its own version
tree under `docs/logs/skill/`, `docs/logs/rune/`, and `docs/logs/cosmetic/`, so
the products' versions never collide.

[`docs/partials/logs-nav.html`](../../docs/partials/logs-nav.html) is the single
place versions are listed. Every log page loads it, so it is the only file a
release edits. See [Publish a Change Log](../guides/publish-a-change-log.md).

## Generated pages

Profession pages are **generated, not hand-written**. Their source data lives in
[`scripts/generate_professions.py`](../../scripts/generate_professions.py), which
mirrors the plugin's default `professions/*.yml`. See
[Regenerate Professions](../guides/regenerate-professions.md).
