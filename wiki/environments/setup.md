# Local Setup and Publishing

[← Back to README](../../README.md)

There is no build step and no dependency to install. The only requirement is
Python 3 for the local server and the page generator.

## Serve the site locally

```bash
python3 -m http.server 8000 --directory docs
```

Then open <http://localhost:8000/>.

**Always test over HTTP, never by opening the HTML files directly.** The shared
header and footer are fetched at runtime by
[`docs/js/site.js`](../../docs/js/site.js), and a `file://` page cannot fetch
them.

## Verify a change

Click through the affected pages and confirm:

* the header and footer load;
* navigation links resolve at the page's depth;
* there are no console errors.

## GitHub Pages source

The site is published from the **`/docs` folder**, not from the repository root.

> **Settings → Pages → Branch: `master`, Folder: `/docs`**

That mapping is what makes the site root resolve to `docs/index.html` and gives
pages their clean URLs — for example `https://mcoriax.github.io/api/` serves
`docs/api/index.html`.

[`.nojekyll`](../../.nojekyll) at the repository root and
[`docs/.nojekyll`](../../docs/.nojekyll) disable Jekyll processing so files are
served exactly as committed.

## Regenerating pages

The profession pages are generated. See
[Regenerate the Profession Pages](../guides/regenerate-professions.md).

## No environment variables

This is a static site with no runtime configuration. It reads no environment
variables, no `.env` file, and makes no network calls at runtime — no external
fonts, scripts, stylesheets, CDNs, or trackers. Everything ships in-repo,
including this repository's own copy of the theme.
