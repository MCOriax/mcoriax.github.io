# Repository Index

This file is the entry point for understanding the project structure. Agents MUST read it first, and keep it updated whenever the structure or indexed content of this repository changes. It reflects only the files and directories that exist in this repository.

Agent rules are not kept in this repository. They live in the portable `.agents` instruction set used alongside it.

This repository is the **static documentation website** for the MCIdentity Minecraft plugin, published with GitHub Pages from the [`docs/`](docs/) directory.

## Root Files

| Directory / File | Purpose |
|---|---|
| [`./`](./) | Repository root directory. |
| [`INDEX.md`](INDEX.md) | This project structure index. |
| [`README.md`](README.md) | Human-facing project overview. |
| [`AGENTS.md`](AGENTS.md) | Agent rules for this site (no internal source code; how to create a change log). |
| [`DESIGN.md`](DESIGN.md) | Universal "Silver Glass" design system (tokens, components, reuse guide). |
| [`.nojekyll`](.nojekyll) | Disables Jekyll processing so files are served as-is. |
| [`docs/`](docs/) | GitHub Pages site root (set the Pages source to this folder). |
| [`scripts/`](scripts/) | Build tooling used to generate repetitive pages. |

## Site Architecture

The site is plain, self-contained static HTML — no build step and no external fonts, scripts, or stylesheets. Every page injects a shared header and footer at runtime via [`docs/js/site.js`](docs/js/site.js), which fetches the partials in [`docs/partials/`](docs/partials/) and resolves navigation links relative to each page's depth.

### Entry & shared assets

| Directory / File | Purpose |
|---|---|
| [`docs/`](docs/) | Site root directory. |
| [`docs/.nojekyll`](docs/.nojekyll) | Disables Jekyll when the Pages source is `/docs`. |
| [`docs/index.html`](docs/index.html) | Central landing page with the project overview and clickable cards. |
| [`docs/partials/`](docs/partials/) | Shared HTML fragments included on every page. |
| [`docs/partials/header.html`](docs/partials/header.html) | Shared site header and primary navigation (Donation link right-aligned). |
| [`docs/partials/footer.html`](docs/partials/footer.html) | Shared site footer. |
| [`docs/js/`](docs/js/) | Client-side scripts. |
| [`docs/js/site.js`](docs/js/site.js) | Include loader, favicon injection, active-nav, and mobile menu. |

### Stylesheets

| Directory / File | Purpose |
|---|---|
| [`docs/css/`](docs/css/) | Root CSS directory. |
| [`docs/css/main.css`](docs/css/main.css) | Root theme tokens (white / silver / transparent) and base styles. |
| [`docs/css/shared/`](docs/css/shared/) | Shared CSS used across multiple pages. |
| [`docs/css/shared/layout.css`](docs/css/shared/layout.css) | Header, navigation, footer, and breadcrumbs. |
| [`docs/css/shared/components.css`](docs/css/shared/components.css) | Cards, accordions, tables, code, badges, buttons, callouts. |
| [`docs/css/home/`](docs/css/home/) | Home page styles. |
| [`docs/css/features/`](docs/css/features/) | Features page styles. |
| [`docs/css/installation/`](docs/css/installation/) | Installation page styles. |
| [`docs/css/storage/`](docs/css/storage/) | Data storage page styles. |
| [`docs/css/gui/`](docs/css/gui/) | GUI page styles. |
| [`docs/css/profession/`](docs/css/profession/) | Profession pages styles. |
| [`docs/css/commands/`](docs/css/commands/) | Commands page styles. |
| [`docs/css/api/`](docs/css/api/) | API page styles. |
| [`docs/css/listeners/`](docs/css/listeners/) | Listeners page styles. |
| [`docs/css/platforms/`](docs/css/platforms/) | Platform pages styles. |
| [`docs/css/donation/`](docs/css/donation/) | Donation page styles. |
| [`docs/css/logs/`](docs/css/logs/) | Change logs page styles. |

### Content pages

| Directory / File | Purpose |
|---|---|
| [`docs/features/index.html`](docs/features/index.html) | Key features overview. |
| [`docs/installation/index.html`](docs/installation/index.html) | Installation, death behaviour, requirements, and testing. |
| [`docs/storage/index.html`](docs/storage/index.html) | Data storage backends and schema. |
| [`docs/gui/index.html`](docs/gui/index.html) | The multi-tier GUI system. |
| [`docs/commands/index.html`](docs/commands/index.html) | All command usages and permissions. |
| [`docs/api/index.html`](docs/api/index.html) | Developer API usage of the provider class (accordion reference). |
| [`docs/listeners/index.html`](docs/listeners/index.html) | Custom Bukkit events and gameplay listeners. |
| [`docs/donation/index.html`](docs/donation/index.html) | Donation page with the GitHub sponsor block. |

### Profession pages

| Directory / File | Purpose |
|---|---|
| [`docs/profession/index.html`](docs/profession/index.html) | Professions overview, EXP syntax, and the full profession table. |
| [`docs/profession/{profession_name}/index.html`](docs/profession/) | Detail page per bundled profession (max level, stats, how to level up). Covers `acrobat`, `archaeologist`, `archer`, `builder`, `chef`, `crafter`, `enchanter`, `engineer`, `explorer`, `farmer`, `fighter`, `fisher`, `gatherer`, `guard`, `lumberjack`, `mariner`, `merchant`, `miner`, `supporter`, `tamer`, and `tanker`. |

### Platform pages

| Directory / File | Purpose |
|---|---|
| [`docs/platforms/spigotmc/index.html`](docs/platforms/spigotmc/index.html) | How the plugin works on SpigotMC. |
| [`docs/platforms/papermc/index.html`](docs/platforms/papermc/index.html) | How the plugin works on PaperMC. |
| [`docs/platforms/foliamc/index.html`](docs/platforms/foliamc/index.html) | How the plugin works on FoliaMC. |

### Change logs

| Directory / File | Purpose |
|---|---|
| [`docs/logs/index.html`](docs/logs/index.html) | Latest change log with a right-side version navigation bar. |
| [`docs/logs/1/0/0/index.html`](docs/logs/1/0/0/index.html) | Permalink for version 1.0.0 (versioned `major/minor/patch` structure). |
| [`docs/logs/1/1/0/index.html`](docs/logs/1/1/0/index.html) | Permalink for version 1.1.0 (universal JAR architecture). |

## Tooling

| Directory / File | Purpose |
|---|---|
| [`scripts/`](scripts/) | Build scripts (not served by the site). |
| [`scripts/generate_professions.py`](scripts/generate_professions.py) | Generates the profession listing and detail pages from embedded profession data. |
