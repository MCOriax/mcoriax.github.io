---
name: content-refresh-findings
description: Three unapplied follow-ups found during the site 1.1.0 refresh, for the owner to choose from.
---

# Website refresh: findings to choose from

Found while refreshing mcoriax.github.io (site 1.1.0, PRs #31 to #38, all merged).
Nothing below has been applied. Pick the ones you want.

## Finding 1 (local, mcoriax.github.io): AGENTS.md names only three add-ons

Target set: local. File: `AGENTS.md`, opening paragraph. `name`: agents-entry-point
(unchanged). `description`: unchanged.

Proposed opening paragraph:

```
This repository is the **documentation website** for the MCIdentity Minecraft
plugin, its MCIdentitySkill, MCIdentityRune, MCIdentityCosmetic, and
MCIdentityPerks add-ons, and the MCIdentity Central Server, published with GitHub
Pages from `docs/`. It is plain, self-contained static HTML with no build step,
and no page may contain code. Two trees matter: `docs/` is the **published
site**, and `wiki/` is **documentation about how the site is built**.
```

Why: agents reading the entry point today don't learn that Perks and the server
have pages, or that the site is code-free.

## Finding 2 (local, mcidentity): stale permission node in the core wiki

Target set: local (documentation, not an instruction file). File:
`mcidentity/wiki/reference/commands.md` still says `mcidentity.admin`; the plugin
uses `mcoriax.mcidentity.admin` and per-command `mcoriax.mcidentity.command.*`
nodes.

Why: the website now shows the real nodes, so the core wiki contradicts it.

## Finding 3 (local, skill, rune, cosmetic): API line mismatch

Target set: local (documentation). Files: `wiki/environments/installation.md` in
mcidentity-skill, mcidentity-rune and mcidentity-cosmetic say "26.2.x API line";
the core says 26.1.x. The website avoids naming an API line on add-on pages until
this is settled.

Why: one of the two is wrong, and server owners read both.
