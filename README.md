# mcoriax.github.io

The documentation website for the **MCIdentity** Minecraft plugin, published with
GitHub Pages.

## Project Overview

* **Platform:** [github.com](https://github.com)
* **Organization:** [MCOriax](https://github.com/MCOriax)
* **Repository:** [mcoriax.github.io](https://github.com/MCOriax/mcoriax.github.io)

## Live site

Once GitHub Pages is enabled for this repository, the documentation is served at:

<https://mcoriax.github.io/>

> **GitHub Pages source:** set the Pages build source to the **`/docs` folder**
> so the site root maps to `docs/index.html` and the URLs above resolve
> (for example `https://mcoriax.github.io/api/`).

## Structure

All site content lives in [`docs/`](docs/). See [`INDEX.md`](INDEX.md) for the
full structure. In short:

| Path | Purpose |
|---|---|
| [`docs/index.html`](docs/index.html) | Central landing page with overview cards. |
| [`docs/partials/`](docs/partials/) | Shared header and footer, included by every page. |
| [`docs/css/`](docs/css/) | Root, shared, and per-section stylesheets. |
| [`docs/js/site.js`](docs/js/site.js) | Client-side include loader and navigation behaviour. |
| [`docs/profession/`](docs/profession/) | One page per bundled profession. |
| [`docs/api/`](docs/api/) | Developer API usage. |
| [`docs/platforms/`](docs/platforms/) | SpigotMC, PaperMC, and FoliaMC guides. |
| [`docs/logs/`](docs/logs/) | Versioned change logs. |
| [`scripts/generate_professions.py`](scripts/generate_professions.py) | Regenerates the profession pages from bundled data. |

## Regenerating the profession pages

The profession pages are generated from a normalised copy of the plugin's
default `professions/*.yml` data:

```bash
python3 scripts/generate_professions.py
```

## Theme

A modern, glassmorphism-inspired theme built around **white**, **silver**, and
**transparent** surfaces. The design tokens live in
[`docs/css/main.css`](docs/css/main.css); shared layout and components live under
[`docs/css/shared/`](docs/css/shared/). The site is fully self-contained — no
external fonts, scripts, or stylesheets.
