# Agent Instructions — mcoriax.github.io

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

---

## Organization Standard — Agent Instructions & Workflow

### Iron Rules

* **Platform Specification:** Whether working with a single repository or multiple repositories, the user must explicitly specify the cloud hosting platform for each repository. For example:
  * `{org}/{repo} - github.com`
  * `{org}/{repo} - gitlab.com`
* **Project Hosting Validation:** The project hosting information must be clearly documented in the first section of the `README.md` file. If this information is missing, you must ask the user where the project is hosted and update the `README.md` to include it using exactly this format (ensuring the items are clickable links):
  ```markdown
  # Project Overview

  * **Platform:** [github.com](link) or [gitlab.com](link)
  * **Organization:** [organization-name](link)
  * **Repository:** [repository-name](link)
  ```

### Strict Rules & Execution

* **Initialization (Read & Understand):** For every repository being worked on (single or multiple), you must perform the following:
  1. **Structure (`INDEX.md`):** Always read `INDEX.md` to understand the project structure. If it does not exist, create it first using the **Universal Repository Index Template** provided below. Actively update it whenever structural changes occur.
  2. **Context (`README.md`):** Always read `README.md` to understand the core project goals, context, setup instructions, and to verify the project hosting information. If the hosting information is missing, refer to the **Project Hosting Validation** iron rule immediately.
* **Execution:** Create a solid plan. Write code section-by-section. Test thoroughly by executing the project's standard test suite via the command line (e.g., `npm test`, `pytest`, `cargo test`) and fix any errors. Verify code security for modified files before completing the task.
* **Modularity:** Separate code into multiple focused files and modules to prevent spaghetti code. Keep files concise and adhere to the Single Responsibility Principle.
* **Dashes:** Do not use dashes (`-`) unnecessarily. Use them strictly for file or directory names (e.g., `getting-started.md`) and branch names. Avoid them in variable names, database schemas, or general prose unless standard conventions explicitly require it.
* **Versioning:** If a project is newly created, its version must be set to "0.0.0". For any pull request (PR) update, the version must always be updated. The version must use the Semantic Versioning format (`Major.Minor.Patch`). If it does not, update it to this format. Before merging, check if the version has been updated. If it hasn't changed, ask the user if they want to update it. If they answer yes, update the version according to the standard definitions of Major, Minor, and Patch.
* **Documents:** The root `README.md` must contain only an overview of the project. The project must have the following documentation files: `wiki/requirements.md`, `wiki/api.md`, `wiki/environment.md`, and `wiki/system.md`. Any other required documentation files must be created within the `wiki/` directory using lowercase filenames, and use hyphens for multiple words (e.g., `wiki/getting-started.md`).
* **Environment:** Do not create a `.env.example` file. Instead, document the required environment variables within the `wiki/environment.md` file using a code block. When providing example values, do not use actual realistic text; use standardized placeholders such as `your_{name}_api_key`, `your_server_api_key`, or `your_openrouter_api_key`. Any examples of infrastructure configurations (e.g., Kubernetes, docker-compose, etc.) must also be written exclusively within the `wiki/environment.md` file.
* **Website Synchronization:** If the user has also cloned the website repository, the agents must update the website contents accordingly.

### Universal Repository Index Template

When creating or updating `INDEX.md`, Agents must follow this structure, adapting the sections to fit the specific project type. Every table must list the directory in the first row, followed by its respective files or subdirectories. **Every single file or directory must have its own dedicated row.**

```markdown
# Repository Index

This file is the entry point for understanding the project structure. Agents MUST read it first, and keep it updated whenever the structure or indexed content of this repository changes. It reflects only the files and directories that exist in this repository.

Agent rules are not kept in this repository. They live in the portable `.agents` instruction set used alongside it.

## Root Files

| Directory / File | Purpose |
|---|---|
| [`./`](./) | Repository root directory. |
| [`INDEX.md`](INDEX.md) | This project structure index. |
| [`README.md`](README.md) | Human-facing project overview. |
| [`package.json`](package.json) | Core dependency and build configuration. |
| [`Dockerfile`](Dockerfile) | Main Docker image configuration. |
| [`docker-compose.yml`](docker-compose.yml) | Multi-container orchestration. |
| [`.gitignore`](.gitignore) | Git ignore configuration. |
| [`.gitattributes`](.gitattributes) | Git attributes configuration. |

## Source Modules / Architecture

Description of the overall architectural patterns (e.g., MVC, Monolith, Multi-module, Microservices). All core packages or directories must be listed below.

### [Module/Layer Name]

Description of the responsibility of this specific module or layer.

| Directory / File | Purpose |
|---|---|
| [`src/`](src/) | Root source directory. |
| [`src/core/`](src/core/) | Core business logic and types. |
| [`src/api/`](src/api/) | API routes, controllers, or contracts. |
| [`src/infrastructure/`](src/infrastructure/) | Database connections, external service clients, or drivers. |

*(Repeat the module/layer block above for every major module, package, or application layer in the repository)*

## Documentation

| Directory / File | Purpose |
|---|---|
| [`wiki/`](wiki/) | Human-facing documentation root directory. |
| [`wiki/api.md`](wiki/api.md) | API specifications and endpoints. |
| [`wiki/environment.md`](wiki/environment.md) | Environment configuration, variables, and infrastructure examples. |
| [`wiki/requirements.md`](wiki/requirements.md) | Project requirements. |
| [`wiki/system.md`](wiki/system.md) | System architecture documentation. |
```

### Agent Directories

All agent-specific files and configurations must be centralized under the `.agents/` directory. Each repository will have its own `.agents/` directory. Agents must strictly use the agent directory belonging to the current repository and must not use or cross-reference `.agents/` directories from another repository.
* `.agents/`: Root directory for all agent configurations.
* `.agents/skills/`: Specific skill definitions and execution steps.
* `.agents/tools/`: Tool definitions and schemas.
* `.agents/knowledge/`: Domain-specific context.
* `.agents/personas/`: Specific roles to adopt.
* `.agents/ethics/`: Safety bounds and constraints.

### Git & Branching Workflow (STRICT)

* **Task Management:** If the user provides one or multiple tasks, each task must have its own branch created, a pull request (PR) opened, and be merged separately.
* **No Master/Main:** Never work directly on the `main` or `master` branches. Create a new branch if the task scope changes; otherwise, continue on the active branch.
* **Branch Naming & Validation:** Must follow `{type}/{primary-noun}` (e.g., `feat/login`). Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Absolutely do not use preset prefixes (e.g., `claude/`, `codex/`). If a created branch does not follow the naming convention, you must recreate it (rewrite the branch name and delete the incorrect branch) or provide the user with options on how to proceed.
* **Commit Frequency & Verification:** Commit each change or group related commits. Do not wait for the entire session to finish. Always check the diff before creating a commit.
* **Commits:** Must use Conventional Commits (`type[optional scope]: description`). Commit messages must be plain text with **no links** or Jira IDs.
* **Pull Requests (PR):** Open sequentially. Always ask for user approval first. Provide a detailed report of added/modified/deleted features in the PR body. PR titles and descriptions must contain **no links**. Assume any references to github.com or gitlab.com are for their cloud-hosted environments.
