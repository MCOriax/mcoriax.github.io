# Site Structure

[← Back to README](../../README.md)

Every directory and file under `docs/` (the published site) and `scripts/` (build
tooling), with its purpose. Keep this page current whenever the structure
changes — see [`../guides/add-a-page.md`](../guides/add-a-page.md).

For *how* the pieces fit together, read
[Site Architecture](../information/architecture.md).

## Site Architecture

The site is plain, self-contained static HTML — no build step and no external fonts, scripts, or stylesheets. Every page injects a shared header and footer at runtime via [`docs/js/site.js`](../../docs/js/site.js), which fetches the partials in [`docs/partials/`](../../docs/partials/) and resolves navigation links relative to each page's depth.

### Entry & shared assets

| Directory / File | Purpose |
|---|---|
| [`docs/`](../../docs/) | Site root directory. |
| [`docs/.nojekyll`](../../docs/.nojekyll) | Disables Jekyll when the Pages source is `/docs`. |
| [`docs/index.html`](../../docs/index.html) | Central landing page with the project overview and clickable cards. |
| [`docs/partials/`](../../docs/partials/) | Shared HTML fragments included on every page. |
| [`docs/partials/header.html`](../../docs/partials/header.html) | Shared site header and primary navigation, with the Platforms and Add-ons dropdowns and the Donation link right-aligned. |
| [`docs/partials/footer.html`](../../docs/partials/footer.html) | Shared site footer. |
| [`docs/partials/logs-nav.html`](../../docs/partials/logs-nav.html) | The change-log version navigation, listed once and loaded by every log page. The only file a release edits. |
| [`docs/js/`](../../docs/js/) | Client-side scripts. |
| [`docs/js/site.js`](../../docs/js/site.js) | Include loader, favicon injection, active-nav, mobile menu, and the log version navigation (the product picker, the five-row scroll cap, the current release, and the back link). |

### Stylesheets

The shared "Silver Glass" theme is vendored locally in this repository (no
runtime dependency on another site); the design system is documented in
[`DESIGN.md`](../../DESIGN.md).

| Directory / File | Purpose |
|---|---|
| [`docs/css/`](../../docs/css/) | Root CSS directory. |
| [`docs/css/main.css`](../../docs/css/main.css) | Root theme tokens (white / silver / transparent) and base styles. |
| [`docs/css/shared/`](../../docs/css/shared/) | Shared CSS used across multiple pages. |
| [`docs/css/shared/layout.css`](../../docs/css/shared/layout.css) | Header, navigation, footer, breadcrumbs, and this site's header/footer extras (brand logo, donation link, Platforms dropdown, footer bar). |
| [`docs/css/shared/components.css`](../../docs/css/shared/components.css) | Cards, accordions, tables, code, badges, buttons, callouts. |
| [`docs/css/home/`](../../docs/css/home/) | Home page styles. |
| [`docs/css/features/`](../../docs/css/features/) | Features page styles. |
| [`docs/css/installation/`](../../docs/css/installation/) | Installation page styles. |
| [`docs/css/storage/`](../../docs/css/storage/) | Data storage page styles. |
| [`docs/css/gui/`](../../docs/css/gui/) | GUI page styles. |
| [`docs/css/profession/`](../../docs/css/profession/) | Profession pages styles. |
| [`docs/css/commands/`](../../docs/css/commands/) | Commands page styles. |
| [`docs/css/api/`](../../docs/css/api/) | API page styles. |
| [`docs/css/listeners/`](../../docs/css/listeners/) | Listeners page styles. |
| [`docs/css/platforms/`](../../docs/css/platforms/) | Platform pages styles. |
| [`docs/css/donation/`](../../docs/css/donation/) | Donation page styles. |
| [`docs/css/logs/`](../../docs/css/logs/) | Change logs page styles. |
| [`docs/css/skill/`](../../docs/css/skill/) | Skill add-on page styles. |
| [`docs/css/addon/`](../../docs/css/addon/) | Shared add-on page styles (hero badges, ownership split, slot maps, backend chips), used by the rune and cosmetic pages. |

### Content pages

| Directory / File | Purpose |
|---|---|
| [`docs/features/index.html`](../../docs/features/index.html) | Key features overview. |
| [`docs/installation/index.html`](../../docs/installation/index.html) | Installation steps, death behaviour, requirements, and quality, in prose. |
| [`docs/storage/index.html`](../../docs/storage/index.html) | Data storage backends, how they work, upgrade notes, identity aliases, and the data stored. |
| [`docs/gui/index.html`](../../docs/gui/index.html) | The multi-tier GUI system. |
| [`docs/commands/index.html`](../../docs/commands/index.html) | All command usages and permissions. |
| [`docs/api/index.html`](../../docs/api/index.html) | What the developer library offers, how to get it, the events to react to, and the one identity, one account rule, in prose. |
| [`docs/skill/index.html`](../../docs/skill/index.html) | The MCIdentitySkill add-on: skills stored on the item, the profession restriction (including the base `player` identity owning no skills), MythicMobs casting, the single player command and its operator only subcommands, and its developer API. |
| [`docs/rune/index.html`](../../docs/rune/index.html) | The MCIdentityRune add-on: identity-scoped rune slots, the permanent held-once assignment rules, the menu layout, `/rune`, its own storage, and its developer API. |
| [`docs/cosmetic/index.html`](../../docs/cosmetic/index.html) | The MCIdentityCosmetic add-on: the independent skin and aura fields, the menu layout, `/cosmetic`, its own storage, and its developer API. |
| [`docs/perks/index.html`](../../docs/perks/index.html) | The MCIdentityPerks add-on, in development: Sigils, Relics, and Perks, all stored against the identity. |
| [`docs/server/index.html`](../../docs/server/index.html) | The MCIdentity Central Server: what it is, how game servers use it, storage, security, running it, and compatibility. |
| [`docs/listeners/index.html`](../../docs/listeners/index.html) | The identity events other plugins can react to, as a plain table, and the gameplay listeners. |
| [`docs/donation/index.html`](../../docs/donation/index.html) | Donation page with the GitHub sponsor block. |

### Profession pages

| Directory / File | Purpose |
|---|---|
| [`docs/profession/index.html`](../../docs/profession/index.html) | Professions overview, the per-action EXP gain reference (one accordion per action, with examples shown as plain tables), and the full profession table. |
| [`docs/profession/{profession_name}/index.html`](../../docs/profession/) | Detail page per bundled profession (max level, stats, how to level up). Covers `acrobat`, `archaeologist`, `archer`, `builder`, `chef`, `crafter`, `enchanter`, `engineer`, `explorer`, `farmer`, `fighter`, `fisher`, `gatherer`, `guard`, `lumberjack`, `mariner`, `merchant`, `miner`, `supporter`, `tamer`, and `tanker`. |

### Platform pages

| Directory / File | Purpose |
|---|---|
| [`docs/platforms/spigotmc/index.html`](../../docs/platforms/spigotmc/index.html) | How the plugin works on SpigotMC. |
| [`docs/platforms/papermc/index.html`](../../docs/platforms/papermc/index.html) | How the plugin works on PaperMC. |
| [`docs/platforms/foliamc/index.html`](../../docs/platforms/foliamc/index.html) | How the plugin works on FoliaMC. |

### Change logs

| Directory / File | Purpose |
|---|---|
| [`docs/logs/index.html`](../../docs/logs/index.html) | Latest MCIdentity change log (`4.7.0`) with a right-side version navigation bar. Each add-on and the central server keep their own version tree under `logs/skill/`, `logs/rune/`, `logs/cosmetic/`, `logs/perks/`, and `logs/server/`, so the products' versions never collide. |
| [`docs/logs/1/0/0/index.html`](../../docs/logs/1/0/0/index.html) | Permalink for version 1.0.0 (versioned `major/minor/patch` structure). |
| [`docs/logs/1/1/0/index.html`](../../docs/logs/1/1/0/index.html) | Permalink for version 1.1.0 (universal JAR architecture). |
| [`docs/logs/2/0/0/index.html`](../../docs/logs/2/0/0/index.html) | Permalink for version 2.0.0 (developer API namespace move). |
| [`docs/logs/3/0/0/index.html`](../../docs/logs/3/0/0/index.html) | Permalink for version 3.0.0 (skill decoupling; the ability tables are dropped). |
| [`docs/logs/4/0/0/index.html`](../../docs/logs/4/0/0/index.html) | Permalink for version 4.0.0 (rune and cosmetic decoupling; those tables are dropped). |
| [`docs/logs/4/1/0/index.html`](../../docs/logs/4/1/0/index.html) | Permalink for version 4.1.0 (identity aliases: the `alias` column and `/identity alias`). |
| [`docs/logs/4/2/0/index.html`](../../docs/logs/4/2/0/index.html) | Permalink for version 4.2.0 (one supported way in: the provider owns storage, the manager owns RAM state). |
| [`docs/logs/4/3/0/index.html`](../../docs/logs/4/3/0/index.html) | Permalink for version 4.3.0 (a claimed alias names the player in chat and the tab list). |
| [`docs/logs/4/3/1/index.html`](../../docs/logs/4/3/1/index.html) | Permalink for version 4.3.1 (the profession prefix is kept in chat alongside the alias). |
| [`docs/logs/4/4/0/index.html`](../../docs/logs/4/4/0/index.html) | Permalink for version 4.4.0 (an alias is claimed once; the base `Player` identity keeps the Minecraft name). |
| [`docs/logs/4/5/0/index.html`](../../docs/logs/4/5/0/index.html) | Permalink for version 4.5.0 (identities are named by their alias, with profession and level in the lore). |
| [`docs/logs/4/5/1/index.html`](../../docs/logs/4/5/1/index.html) | Permalink for version 4.5.1 (the identity item is re-titled on alias claim and on equip). |
| [`docs/logs/4/6/0/index.html`](../../docs/logs/4/6/0/index.html) | Permalink for version 4.6.0 (`/identity unuse` is renamed to `/identity unequip`, node included). |
| [`docs/logs/4/6/1/index.html`](../../docs/logs/4/6/1/index.html) | Permalink for version 4.6.1 (a quality and security clean-up). |
| [`docs/logs/4/7/0/index.html`](../../docs/logs/4/7/0/index.html) | Permalink for version 4.7.0 (one shared central server connection for the add-ons). |
| [`docs/logs/skill/index.html`](../../docs/logs/skill/index.html) | Latest MCIdentitySkill change log (`0.3.1`), with its own version navigation. |
| [`docs/logs/skill/0/0/0/index.html`](../../docs/logs/skill/0/0/0/index.html) | Permalink for MCIdentitySkill version 0.0.0 (initial release). |
| [`docs/logs/skill/0/1/0/index.html`](../../docs/logs/skill/0/1/0/index.html) | Permalink for MCIdentitySkill version 0.1.0 (the base `player` identity owns no skills and has no skill menu). |
| [`docs/logs/skill/0/2/0/index.html`](../../docs/logs/skill/0/2/0/index.html) | Permalink for MCIdentitySkill version 0.2.0 (a player has one command, `/skill`, which opens the menu they equip in). |
| [`docs/logs/skill/0/3/0/index.html`](../../docs/logs/skill/0/3/0/index.html) | Permalink for MCIdentitySkill version 0.3.0 (an identity holds a given skill in at most one slot). |
| [`docs/logs/skill/0/3/1/index.html`](../../docs/logs/skill/0/3/1/index.html) | Permalink for MCIdentitySkill version 0.3.1 (maintenance). |
| [`docs/logs/rune/index.html`](../../docs/logs/rune/index.html) | Latest MCIdentityRune change log (`0.1.1`), with its own version navigation. |
| [`docs/logs/rune/0/0/0/index.html`](../../docs/logs/rune/0/0/0/index.html) | Permalink for MCIdentityRune version 0.0.0 (initial release). |
| [`docs/logs/rune/0/1/0/index.html`](../../docs/logs/rune/0/1/0/index.html) | Permalink for MCIdentityRune version 0.1.0 (a rune assignment is permanent and held once). |
| [`docs/logs/rune/0/1/1/index.html`](../../docs/logs/rune/0/1/1/index.html) | Permalink for MCIdentityRune version 0.1.1 (maintenance). |
| [`docs/logs/cosmetic/index.html`](../../docs/logs/cosmetic/index.html) | Latest MCIdentityCosmetic change log, with its own version navigation. |
| [`docs/logs/cosmetic/0/0/0/index.html`](../../docs/logs/cosmetic/0/0/0/index.html) | Permalink for MCIdentityCosmetic version 0.0.0 (initial release). |
| [`docs/logs/perks/index.html`](../../docs/logs/perks/index.html) | Latest MCIdentityPerks change log (`0.1.0`), with its own version navigation. |
| [`docs/logs/perks/0/1/0/index.html`](../../docs/logs/perks/0/1/0/index.html) | Permalink for MCIdentityPerks version 0.1.0 (project set up). |
| [`docs/logs/server/index.html`](../../docs/logs/server/index.html) | Latest MCIdentity Central Server change log (`3.4.5`), with its own version navigation. |
| [`docs/logs/server/3/4/0/index.html`](../../docs/logs/server/3/4/0/index.html) | Permalink for MCIdentity Central Server version 3.4.0 (documentation reorganised). |
| [`docs/logs/server/3/4/1/index.html`](../../docs/logs/server/3/4/1/index.html) | Permalink for MCIdentity Central Server version 3.4.1 (two security hardenings). |
| [`docs/logs/server/3/4/2/index.html`](../../docs/logs/server/3/4/2/index.html) | Permalink for MCIdentity Central Server version 3.4.2 (housekeeping). |
| [`docs/logs/server/3/4/3/index.html`](../../docs/logs/server/3/4/3/index.html) | Permalink for MCIdentity Central Server version 3.4.3 (stat statements prepared in advance). |
| [`docs/logs/server/3/4/4/index.html`](../../docs/logs/server/3/4/4/index.html) | Permalink for MCIdentity Central Server version 3.4.4 (housekeeping). |
| [`docs/logs/server/3/4/5/index.html`](../../docs/logs/server/3/4/5/index.html) | Permalink for MCIdentity Central Server version 3.4.5 (checked against every plugin). |

## Tooling

| Directory / File | Purpose |
|---|---|
| [`scripts/`](../../scripts/) | Build scripts (not served by the site). |
| [`scripts/generate_professions.py`](../../scripts/generate_professions.py) | Generates the profession listing and detail pages from embedded profession data. |
| [`scripts/exp_actions.py`](../../scripts/exp_actions.py) | Catalog of every EXP gain action key with its trigger, accepted value shapes, and examples; rendered as plain tables onto the profession listing page. |
