# Repository-specific rules — mcoriax.github.io

This repository is the **static documentation website** for the MCIdentity
Minecraft plugin, published with GitHub Pages from the [`docs/`](docs/) folder.
Read [`INDEX.md`](INDEX.md) for the file structure and [`DESIGN.md`](DESIGN.md)
for the design system before making changes. `DESIGN.md` is this repository's own
copy of the shared MCEngine "Silver Glass" design system; keep it aligned with
the canonical copy in `MCEngine/mcengine.github.io`. The theme CSS is vendored
locally under `docs/css/` — this site has no runtime dependency on another
repository (see [Website repository structure](#website-repository-structure)).

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
* Use the design tokens and components from [`DESIGN.md`](DESIGN.md); do not
  invent new colors or one-off styles.
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
