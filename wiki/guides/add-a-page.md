# Add a Page

[← Back to README](../../README.md)

How to add a new section page to the site.

## Steps

1. **Create the file** at `docs/{section}/index.html`.

2. **Set the correct relative root** in `<head>`:

   ```html
   <script>
     window.SITE_ROOT = "../";          // relative path back to docs/
     window.PAGE_SECTION = "{section}";
   </script>
   ```

   Use `"../"` one level deep, `"../../"` two levels deep, and so on.

3. **Link the stylesheets**, all prefixed with that same relative root:

   * `css/main.css`
   * `css/shared/layout.css`
   * `css/shared/components.css`
   * `css/{section}/{section}.css` — the per-section stylesheet

4. **Add the mounts.** Put `<div id="site-header"></div>` at the top of `<body>`
   and `<div id="site-footer"></div>` before the `site.js` script. Do not
   hard-code the navigation into the page.

5. **Register it in the navigation** if it is a top-level section: add a link in
   [`docs/partials/header.html`](../../docs/partials/header.html) using the
   `{{ROOT}}` token and a matching `data-section` value, plus a footer link if
   appropriate.

6. **Update the index** — add the page to
   [`../reference/site-structure.md`](../reference/site-structure.md) and to
   [`../INDEX.md`](../INDEX.md) if it introduces a new documented area, in the
   same commit.

## Conventions to respect

* **One page = one folder.** Keep files focused.
* **Prefer editing shared partials** over duplicating markup.
* **Use the design tokens** from [`DESIGN.md`](../../DESIGN.md). Do not invent
  new colors or one-off styles.
* **Never expose internal source.** Code blocks are allowed only for
  consumer-facing usage: calling the public API, a third-party listener class,
  build configuration, or server-owner configuration. See
  [`../../.agents/rules/repository.md`](../../.agents/rules/repository.md).

## Verify

Serve the site locally and click through the new page — the header and footer
must load, links must resolve, and the console must be clean. See
[Local Setup](../environments/setup.md).
