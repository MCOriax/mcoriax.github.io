# mcoriax.github.io

The documentation website for the **MCIdentity** Minecraft plugin and its
**MCIdentitySkill**, **MCIdentityRune**, and **MCIdentityCosmetic** add-ons,
published with GitHub Pages.

Plain, self-contained static HTML — no build step, no framework, and no external
fonts, scripts, or stylesheets.

## Live site

<https://mcoriax.github.io/>

> **GitHub Pages source:** set the Pages build source to the **`/docs` folder**
> so the site root maps to `docs/index.html` and URLs such as
> `https://mcoriax.github.io/api/` resolve.

## Key features

- One folder per page, with a shared header and footer injected at runtime.
- The "Silver Glass" theme vendored locally — no runtime dependency on another
  repository.
- Versioned change logs with permanent URLs, and a separate version tree per
  product.
- Profession pages generated from the plugin's bundled data.

## Quick start

```bash
python3 -m http.server 8000 --directory docs
```

Then open <http://localhost:8000/>. Always test over HTTP — the header and footer
are fetched at runtime, so opening files directly will not work.

## Documentation

Full documentation lives in [`wiki/INDEX.md`](wiki/INDEX.md).

Start here:

- [Project Overview](wiki/information/overview.md) — what this repository is and
  the `docs/` versus `wiki/` split.
- [Site Architecture](wiki/information/architecture.md) — how pages are
  assembled.
- [Site Structure](wiki/reference/site-structure.md) — every file under `docs/`.
- [Add a Page](wiki/guides/add-a-page.md) — adding a new section.

## Theme

A modern, glassmorphism-inspired theme built around white, silver, and
transparent surfaces, documented in [`DESIGN.md`](DESIGN.md) and kept in sync
with the canonical copy in `MCEngine/mcengine.github.io`.

## License

See [`LICENSE`](LICENSE).
