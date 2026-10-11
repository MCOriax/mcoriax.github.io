# Publish a Change Log

[← Back to README](../../README.md)

Logs use a versioned directory structure so every published build gets a
permanent URL: `docs/logs/{major}/{minor}/{patch}/index.html` — for example
`docs/logs/1/0/0/`, `docs/logs/1/0/1/`, `docs/logs/1/1/0/`, `docs/logs/2/0/0/`.

`docs/logs/index.html` always mirrors the **latest** release; each versioned page
is the permalink for that specific version.

> **Approval required.** Publishing a version is a version claim. Never do it on
> your own initiative — see
> [`../../.agents/rules/versioning.md`](../../.agents/rules/versioning.md).

## To publish a log for version `X.Y.Z`

### 1. Create the versioned page

Create `docs/logs/X/Y/Z/index.html`.

* Copy the layout of the most recent versioned page as a starting point.
* A page four levels deep sets `window.SITE_ROOT = "../../../../"` and links the
  stylesheets (`css/main.css`, `css/shared/layout.css`,
  `css/shared/components.css`, `css/logs/logs.css`) with that same prefix. Use
  `window.PAGE_SECTION = "logs"`.
* Fill in the version, date, and change sections. Use the `log-tag--new` /
  `log-tag--improve` / `log-tag--note` labels for Added / Changed / Notes.
* The page needs no navigation markup of its own — it carries an empty mount and
  the loader fills it:

  ```html
  <aside class="logs-nav" id="logs-nav" aria-label="Log versions"></aside>
  ```

### 2. Add the version to the shared navigation

[`docs/partials/logs-nav.html`](../../docs/partials/logs-nav.html) is the one file
that lists versions. Every log page loads it, so this is the only place the
navigation is edited.

* Add an `<li>` for the version being **superseded**, pointing at its own
  permalink.
* Move the product's newest entry forward: its label and its `data-permalink`.
  Its `href` keeps pointing at the product index, which always mirrors the latest
  release.
* **Do not** write `class="is-current"` anywhere. `site.js` marks the entry
  matching the page being read, so a hand-written marker would be a second source
  of truth that goes stale.
* Nothing else is needed for the product picker or the scrolling. `site.js`
  builds the dropdown from the `<h4>` above each list and caps a list at five
  visible rows, so a list simply growing longer needs no other change.

### 3. Refresh the product's index

`docs/logs/index.html` for the core plugin, or `docs/logs/{product}/index.html`
for an add-on. Show the new version's content as the latest entry, mark it
`badge--ok "Latest"`, and point its permalink line at `X/Y/Z/index.html`.

### 4. Remove the `Latest` badge from the superseded permalink

The `.logs-nav` pill is handled by the shared partial, but the `badge--ok` in the
page's own `log-entry__head` is not — and a page that keeps it claims to be
current forever.

### 5. Update the structure reference

Add the new log path to
[`../reference/site-structure.md`](../reference/site-structure.md) in the same
commit.

## Content rule

Describe **what changed for users and integrators** — features, fixes, config,
and public-API changes only, in plain language. A log page contains no code:
no inline code, no class or method names, no table or configuration keys.
Commands and permission nodes stay as ordinary words.

## Versioning

Semantic Versioning: `Major.Minor.Patch`. Keep the directory numbers in sync with
the released version of the product the log belongs to. Each add-on has its own
version tree, so the products' versions never collide.
