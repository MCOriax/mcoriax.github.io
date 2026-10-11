# Changelog — 1.1.0

**Released:** 2026-10-11

Rewrites every page of the published site under `docs/` as prose and plain tables,
with no code or code snippets anywhere, and brings the content in line with what
the MCOriax repositories say today: core 4.7.0, add-ons requiring core 4.2.0 or
newer, and the central server at 3.4.5.

## Added

- `docs/perks/index.html` — the MCIdentityPerks add-on (Sigils, Relics, Perks),
  marked as in development, linked from the header's Add-ons menu, the home page,
  and the features page.
- `docs/server/index.html` — the MCIdentity Central Server: what it is, how game
  servers use it, its two databases, its security model, running it, and a
  compatibility table. Linked from a new header "Server" link and the home page.
- A "The MCOriax projects" section on the home page describing the core, the four
  add-ons, and the central server.
- Change-log pages for releases that were missing: core 4.6.1 and 4.7.0, skill
  0.3.1, rune 0.1.1, perks 0.1.0, and central server 3.4.0 to 3.4.5, with new
  MCIdentityPerks and MCIdentity Central Server sections in the version picker.

## Changed

- Home, features, installation, storage, commands, GUI, and the three platform
  pages rewritten as prose. Commands now carries the real permission nodes, and
  storage no longer shows configuration or schema snippets.
- Developer API and listeners pages rewritten as prose: where to get the library
  (GitHub Packages, version 4.7.0), what it offers, and a plain table of the six
  events. The stale dependency version 2.0.0 is gone.
- Skill, rune, and cosmetic pages rewritten as prose, with the real core version
  floor of 4.2.0 (4.7.0 when stored on the central server).
- `scripts/generate_professions.py` and `scripts/exp_actions.py` now render EXP
  examples as plain tables and sentences; all 22 profession pages regenerated.
- Every existing change-log page stripped of code formatting, with class and table
  names reworded into plain language and no change to what each release says.
- `.agents/rules/repository.md`: the site may no longer contain code or snippets of
  any kind, consumer examples included.
- `README.md` and the `wiki/` guides, overview, and site-structure reference
  updated for the new pages and the no-code rule.

## Removed

- Every `<pre>` and `<code>` element from every page under `docs/`.
