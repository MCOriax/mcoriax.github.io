#!/usr/bin/env python3
"""
Generate the MCIdentity profession documentation pages.

This script renders the profession listing page and one detail page per
bundled profession into ``docs/profession/``. The profession data below is a
normalised copy of the plugin's default ``professions/*.yml`` resources
(max level, EXP per level, starting stats, and the action-based EXP rules that
tell players how to level up). Re-run it whenever the bundled professions
change:

    python3 scripts/generate_professions.py
"""

import os

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
STAT_ORDER = ["energy", "health", "food", "strength", "defense",
              "wisdom", "luck", "agility", "resilience"]

# Human-readable trigger descriptions for each supported action key.
TRIGGERS = {
    "survive_fall": "Take fall damage but survive it (by amount survived)",
    "glide_elytra": "Start gliding with an elytra (rate-limited)",
    "dodge_action": "Evade incoming damage (chance scales with agility)",
    "discover_structure": "Discover a major structure (stronghold, fortress, bastion)",
    "open_loot_chest": "Open a naturally generated loot container",
    "explore_biome": "Enter a biome for the first time this session",
    "brush_archaeology": "Brush a suspicious block",
    "sniff_sniffer_egg": "A sniffer unearths an ancient seed",
    "deal_ranged_damage": "Deal damage with a projectile such as a bow (by damage dealt)",
    "place_block": "Place a block (rewarded once per location)",
    "shear_entity": "Shear an entity such as a sheep",
    "consume_food": "Eat a food item",
    "craft_item": "Craft an item",
    "dye_item": "Dye a sheep (rate-limited)",
    "carve_pumpkin": "Carve a pumpkin with shears (once per location)",
    "play_music_disc": "Insert a music disc into an empty jukebox",
    "ignite_campfire": "Light an unlit campfire (rate-limited)",
    "plant_flower": "Plant a flower (rewarded once per location)",
    "smelt_furnace": "Extract a smelted item from a furnace",
    "milk_entity": "Milk a cow, mooshroom, or goat with a bucket",
    "brew_potion": "Collect a brewed potion from a brewing stand",
    "sculpt_chiseled_block": "Cut a chiseled block variant on a stonecutter",
    "use_smithing_template": "Take a result out of a smithing table",
    "enchant_item": "Enchant an item at an enchanting table",
    "repair_item": "Take a repaired or combined item out of an anvil",
    "consume_potion": "Drink a potion",
    "repair_trident": "Take a repaired trident out of an anvil",
    "clean_armor_trim": "Wash a trimmed armor piece in a cauldron (rate-limited)",
    "place_redstone": "Place a redstone component (once per location)",
    "activate_conduit": "Activate a conduit (once per location)",
    "create_golem": "Build a utility golem (credited to the nearest player)",
    "ride_vehicle": "Start riding a boat or minecart (rate-limited)",
    "ignite_fire": "Ignite a fire with flint and steel (rate-limited)",
    "enter_portal": "Travel through a nether or end portal (rate-limited)",
    "sleep_in_bed": "Successfully sleep in a bed (rate-limited)",
    "complete_map_fill": "Lock a map at a cartography table",
    "use_ender_eye_portal": "Place an eye of ender into an end portal frame (once per frame)",
    "harvest_crop": "Break a fully grown crop",
    "plant_crop": "Plant a crop seed",
    "hatch_egg": "A thrown egg hatches into a chick",
    "shear_sheep_color": "Shear a sheep, keyed by its wool color",
    "shear_mushroom_cow": "Shear a mooshroom (only once before it reverts)",
    "deal_damage": "Deal melee damage to another entity (by damage dealt)",
    "kill_mob": "Kill an entity",
    "critical_hit": "Land a critical melee hit",
    "apply_debuff": "Land a harmful potion on another entity",
    "summon_boss": "Summon a boss such as the Wither (credited to the nearest player)",
    "fish_caught": "Reel in a fish",
    "catch_entity_bucket": "Capture an entity in a bucket",
    "spawn_axolotl_bucket": "Release an axolotl from a bucket into the world",
    "strip_log": "Strip a log with an axe (once per location)",
    "collect_honey": "Bottle honey from a full beehive or nest",
    "harvest_sweet_berries": "Gather berries from a ripe sweet berry bush",
    "trigger_raid": "Trigger a village raid (e.g. entering with Bad Omen)",
    "win_raid": "Be credited with winning a village raid",
    "use_totem": "A totem of undying saves you from death",
    "extinguish_fire": "Extinguish a fire block (rate-limited)",
    "chop_tree": "Break a log block",
    "swim_distance": "Sprint-swim in water (per 10 blocks travelled)",
    "villager_trade": "Collect the result of a villager trade",
    "cure_zombie_villager": "Feed a golden apple to a weakened zombie villager",
    "trade_special_wandering": "Complete a trade with a wandering trader",
    "break_ore": "Break an ore block",
    "survive_explosion": "Take explosion damage but survive it (by amount survived)",
    "apply_buff": "Land a beneficial (non-healing) potion on another player",
    "heal_target": "Heal another entity with a splash potion",
    "ring_bell": "Ring a bell (rate-limited)",
    "tame_animal": "Tame an animal",
    "breed_animal": "Breed two animals",
    "leash_entity": "Leash an entity (rate-limited)",
    "feed_pet": "Feed one of your own tamed pets (rate-limited)",
    "receive_damage": "Take damage (by damage received)",
    "shield_block": "Block incoming damage with a shield",
}

# Normalised profession data (from platforms/*/src/main/resources/professions/*.yml).
# actions: list of (action_key, value) where value is a string (simple/range or
# numeric-condition) or a list of (subkey, value) tuples for keyed variants.
PROFESSIONS = {
    "acrobat": {
        "name": "Acrobat", "emoji": "\U0001F938", "theme": "Agility & acrobatics",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 140, "health": 80, "food": 120, "strength": 20, "defense": 10, "wisdom": 10, "luck": 25, "agility": 70, "resilience": 15},
        "actions": [
            ("survive_fall", [("1-5", "5"), ("6-15", "20"), ("16-100", "40~70")]),
            ("glide_elytra", "10~15"),
            ("dodge_action", "20"),
        ],
    },
    "archaeologist": {
        "name": "Archaeologist", "emoji": "\U0001F3FA", "theme": "Discovery & excavation",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 160, "health": 90, "food": 140, "strength": 20, "defense": 15, "wisdom": 40, "luck": 55, "agility": 25, "resilience": 20},
        "actions": [
            ("discover_structure", "80~150"),
            ("open_loot_chest", "50~80"),
            ("explore_biome", "30"),
            ("brush_archaeology", [("suspicious_sand", "40~60"), ("suspicious_gravel", "50~70")]),
            ("sniff_sniffer_egg", [("torchflower_seeds", "80"), ("pitcher_pod", "90")]),
        ],
    },
    "archer": {
        "name": "Archer", "emoji": "\U0001F3F9", "theme": "Ranged combat",
        "max": 100, "exp_up": 150, "random": "0",
        "stats": {"energy": 120, "health": 70, "food": 100, "strength": 30, "defense": 15, "wisdom": 10, "luck": 15, "agility": 60, "resilience": 10},
        "actions": [
            ("deal_ranged_damage", [("1-10", "3~6"), ("11-50", "12~22"), ("51-100", "35~55")]),
        ],
    },
    "builder": {
        "name": "Builder", "emoji": "\U0001F9F1", "theme": "Building & art",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 200, "health": 110, "food": 180, "strength": 30, "defense": 20, "wisdom": 10, "luck": 10, "agility": 10, "resilience": 40},
        "actions": [
            ("place_block", "1~2"),
            ("shear_entity", [("sheep", "4"), ("mooshroom", "8")]),
            ("consume_food", "2~4"),
            ("craft_item", "3"),
            ("dye_item", "2~4"),
            ("carve_pumpkin", "5~8"),
            ("play_music_disc", "10~15"),
            ("ignite_campfire", [("campfire", "5"), ("soul_campfire", "8")]),
            ("plant_flower", "2~4"),
        ],
    },
    "chef": {
        "name": "Chef", "emoji": "\U0001F373", "theme": "Cooking & provisions",
        "max": 100, "exp_up": 110, "random": "0",
        "stats": {"energy": 160, "health": 100, "food": 220, "strength": 15, "defense": 15, "wisdom": 40, "luck": 25, "agility": 15, "resilience": 20},
        "actions": [
            ("smelt_furnace", "3"),
            ("consume_food", "2~4"),
            ("milk_entity", "3~5"),
        ],
    },
    "crafter": {
        "name": "Crafter", "emoji": "\U0001F6E0️", "theme": "Crafting & processing",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 150, "health": 80, "food": 100, "strength": 10, "defense": 10, "wisdom": 50, "luck": 20, "agility": 10, "resilience": 10},
        "actions": [
            ("craft_item", "2"),
            ("smelt_furnace", "3"),
            ("brew_potion", "12"),
            ("sculpt_chiseled_block", "4~6"),
            ("use_smithing_template", "10~15"),
        ],
    },
    "enchanter": {
        "name": "Enchanter", "emoji": "✨", "theme": "Magic, alchemy & repair",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 180, "health": 80, "food": 100, "strength": 10, "defense": 10, "wisdom": 60, "luck": 40, "agility": 10, "resilience": 10},
        "actions": [
            ("enchant_item", "20~35"),
            ("repair_item", "8~15"),
            ("brew_potion", "12"),
            ("consume_potion", "5~10"),
            ("repair_trident", "12~20"),
            ("clean_armor_trim", "8~12"),
        ],
    },
    "engineer": {
        "name": "Engineer", "emoji": "⚙️", "theme": "Engineering & mechanics",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 180, "health": 90, "food": 130, "strength": 20, "defense": 20, "wisdom": 60, "luck": 20, "agility": 15, "resilience": 25},
        "actions": [
            ("place_redstone", "1~3"),
            ("activate_conduit", "30~50"),
            ("create_golem", [("iron_golem", "40~60"), ("snow_golem", "15~25")]),
        ],
    },
    "explorer": {
        "name": "Explorer", "emoji": "\U0001F9ED", "theme": "Exploration & travel",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 160, "health": 90, "food": 140, "strength": 20, "defense": 15, "wisdom": 20, "luck": 50, "agility": 60, "resilience": 20},
        "actions": [
            ("open_loot_chest", "50~80"),
            ("explore_biome", "30"),
            ("ride_vehicle", "3~5"),
            ("ignite_fire", "2~4"),
            ("enter_portal", [("nether", "15~25"), ("the_end", "40~60")]),
            ("sleep_in_bed", "5~10"),
            ("complete_map_fill", "25~40"),
            ("use_ender_eye_portal", "30~50"),
        ],
    },
    "farmer": {
        "name": "Farmer", "emoji": "\U0001F33E", "theme": "Agriculture & ranching",
        "max": 100, "exp_up": 110, "random": "0",
        "stats": {"energy": 150, "health": 100, "food": 200, "strength": 20, "defense": 10, "wisdom": 10, "luck": 30, "agility": 20, "resilience": 20},
        "actions": [
            ("harvest_crop", "1~3"),
            ("plant_crop", "1~2"),
            ("milk_entity", "3~5"),
            ("hatch_egg", "5~10"),
            ("shear_sheep_color", [("pink", "25"), ("brown", "15"), ("light_blue", "18")]),
            ("shear_mushroom_cow", "20~30"),
        ],
    },
    "fighter": {
        "name": "Fighter", "emoji": "⚔️", "theme": "Melee combat & bosses",
        "max": 100, "exp_up": 150, "random": "0",
        "stats": {"energy": 100, "health": 80, "food": 150, "strength": 50, "defense": 25, "wisdom": 0, "luck": 0, "agility": 0, "resilience": 0},
        "actions": [
            ("deal_damage", [("1-10", "2~5"), ("11-50", "10~20"), ("51-100", "30~50")]),
            ("kill_mob", [("zombie", "20~30"), ("skeleton", "25~35"), ("creeper", "40~60"), ("spider", "20~30"), ("enderman", "100~150")]),
            ("critical_hit", "15~25"),
            ("apply_debuff", "10~18"),
            ("summon_boss", [("wither", "200~400")]),
        ],
    },
    "fisher": {
        "name": "Fisher", "emoji": "\U0001F3A3", "theme": "Fishing",
        "max": 100, "exp_up": 100, "random": "0",
        "stats": {"energy": 100, "health": 90, "food": 120, "strength": 20, "defense": 10, "wisdom": 30, "luck": 60, "agility": 10, "resilience": 20},
        "actions": [
            ("fish_caught", "4~8"),
            ("catch_entity_bucket", [("cod", "5"), ("salmon", "5"), ("pufferfish", "8"), ("tropical_fish", "12"), ("axolotl", "25"), ("tadpole", "8")]),
            ("spawn_axolotl_bucket", "15~25"),
        ],
    },
    "gatherer": {
        "name": "Gatherer", "emoji": "\U0001F9FA", "theme": "Foraging",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 200, "health": 100, "food": 150, "strength": 40, "defense": 20, "wisdom": 0, "luck": 10, "agility": 20, "resilience": 30},
        "actions": [
            ("strip_log", "2~3"),
            ("collect_honey", "5~10"),
            ("harvest_sweet_berries", "3~5"),
        ],
    },
    "guard": {
        "name": "Guard", "emoji": "\U0001F6E1️", "theme": "Raid defense & protection",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 130, "health": 200, "food": 150, "strength": 40, "defense": 50, "wisdom": 10, "luck": 10, "agility": 15, "resilience": 45},
        "actions": [
            ("trigger_raid", "20~40"),
            ("win_raid", "150~300"),
            ("use_totem", "50~100"),
            ("extinguish_fire", "3~6"),
        ],
    },
    "lumberjack": {
        "name": "Lumberjack", "emoji": "\U0001FA93", "theme": "Woodcutting",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 190, "health": 110, "food": 160, "strength": 50, "defense": 20, "wisdom": 5, "luck": 10, "agility": 20, "resilience": 30},
        "actions": [
            ("chop_tree", "2~4"),
            ("strip_log", "2~3"),
        ],
    },
    "mariner": {
        "name": "Mariner", "emoji": "⛵", "theme": "Seafaring & aquatic",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 170, "health": 100, "food": 150, "strength": 25, "defense": 15, "wisdom": 25, "luck": 30, "agility": 50, "resilience": 25},
        "actions": [
            ("swim_distance", "2~4"),
            ("ride_vehicle", "3~5"),
            ("catch_entity_bucket", [("cod", "5"), ("salmon", "5"), ("pufferfish", "8"), ("tropical_fish", "12"), ("axolotl", "25")]),
        ],
    },
    "merchant": {
        "name": "Merchant", "emoji": "\U0001F4B0", "theme": "Trade & economy",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 150, "health": 80, "food": 120, "strength": 10, "defense": 10, "wisdom": 45, "luck": 60, "agility": 15, "resilience": 10},
        "actions": [
            ("villager_trade", [("enchanted_book", "30"), ("experience_bottle", "12"), ("emerald", "4")]),
            ("cure_zombie_villager", "100~150"),
            ("trade_special_wandering", [("emerald", "8"), ("experience_bottle", "20"), ("enchanted_book", "40")]),
        ],
    },
    "miner": {
        "name": "Miner", "emoji": "⛏️", "theme": "Mining & cave hazards",
        "max": 100, "exp_up": 130, "random": "0",
        "stats": {"energy": 200, "health": 110, "food": 150, "strength": 45, "defense": 25, "wisdom": 5, "luck": 15, "agility": 15, "resilience": 35},
        "actions": [
            ("break_ore", [("coal_ore", "2"), ("iron_ore", "4"), ("gold_ore", "6"), ("diamond_ore", "20"), ("emerald_ore", "25"), ("ancient_debris", "50")]),
            ("survive_explosion", [("1-5", "10"), ("6-15", "30"), ("16-100", "60~100")]),
        ],
    },
    "supporter": {
        "name": "Supporter", "emoji": "\U0001F49A", "theme": "Team & community aid",
        "max": 100, "exp_up": 120, "random": "0",
        "stats": {"energy": 180, "health": 100, "food": 160, "strength": 10, "defense": 20, "wisdom": 50, "luck": 20, "agility": 20, "resilience": 30},
        "actions": [
            ("apply_buff", "15~25"),
            ("heal_target", "20"),
            ("ring_bell", "3~5"),
            ("cure_zombie_villager", "100~150"),
        ],
    },
    "tamer": {
        "name": "Tamer", "emoji": "\U0001F43E", "theme": "Animal handling",
        "max": 100, "exp_up": 100, "random": "0",
        "stats": {"energy": 120, "health": 100, "food": 120, "strength": 10, "defense": 20, "wisdom": 40, "luck": 20, "agility": 30, "resilience": 10},
        "actions": [
            ("tame_animal", "25~40"),
            ("breed_animal", "8~12"),
            ("leash_entity", "5~8"),
            ("feed_pet", "2~4"),
        ],
    },
    "tanker": {
        "name": "Tanker", "emoji": "\U0001FAA8", "theme": "Defense & mitigation",
        "max": 120, "exp_up": 100, "random": "100~120",
        "stats": {"energy": 100, "health": 250, "food": 120, "strength": 0, "defense": 50, "wisdom": 0, "luck": 0, "agility": 0, "resilience": 50},
        "actions": [
            ("receive_damage", [("1-10", "5~10"), ("11-50", "20~40"), ("51-100", "60~100")]),
            ("shield_block", "10~18"),
            ("dodge_action", "20"),
        ],
    },
}

ORDER = sorted(PROFESSIONS.keys())


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def head(title, desc, root, section, css):
    # Absolute URLs (the shared MCEngine theme) are used as-is; repo-local
    # stylesheets are resolved relative to the page via `root`.
    links = "\n".join(
        '  <link rel="stylesheet" href="%s">' % c if c.startswith("http")
        else '  <link rel="stylesheet" href="%s%s">' % (root, c)
        for c in css)
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "  <title>%s</title>\n"
        "  <meta name=\"description\" content=\"%s\">\n"
        "%s\n"
        "  <script>window.SITE_ROOT = \"%s\"; window.PAGE_SECTION = \"%s\";</script>\n"
        "</head>\n<body>\n  <div id=\"site-header\"></div>\n"
        % (esc(title), esc(desc), links, root, section))


def foot(root):
    return ("\n  <div id=\"site-footer\"></div>\n"
            "  <script src=\"%sjs/site.js\" defer></script>\n"
            "</body>\n</html>\n" % root)


def stat_bars(stats):
    maxv = max(stats.values()) or 1
    rows = []
    for key in STAT_ORDER:
        val = stats[key]
        pct = round(val / maxv * 100)
        rows.append(
            '    <div class="stat-bar">\n'
            '      <div class="stat-bar__top"><span class="stat-bar__name">%s</span>'
            '<span class="stat-bar__val">%d</span></div>\n'
            '      <div class="stat-bar__track"><div class="stat-bar__fill" style="width:%d%%"></div></div>\n'
            '    </div>' % (key, val, pct))
    return '  <div class="stats-grid">\n' + "\n".join(rows) + "\n  </div>"


def action_rows(actions):
    rows = []
    for key, val in actions:
        trigger = TRIGGERS.get(key, "Perform this action")
        if isinstance(val, list):
            subs = "<br>".join(
                '<span class="sub-key">%s</span> &rarr; %s EXP' % (esc(sk), esc(sv))
                for sk, sv in val)
            rows.append(
                "        <tr><td><span class=\"action-key\">%s</span></td>"
                "<td>%s</td><td>%s</td></tr>" % (esc(key), esc(trigger), subs))
        else:
            rows.append(
                "        <tr><td><span class=\"action-key\">%s</span></td>"
                "<td>%s</td><td class=\"exp-val\">%s EXP</td></tr>"
                % (esc(key), esc(trigger), esc(val)))
    return "\n".join(rows)


def detail_page(code, p):
    root = "../../"
    css = ["https://mcengine.github.io/css/main.css",
           "https://mcengine.github.io/css/shared/layout.css",
           "https://mcengine.github.io/css/shared/components.css",
           "css/custom/custom.css",
           "css/profession/profession.css"]
    total = p["exp_up"] * (p["max"] - 1)
    random_note = ("randomly distributed across the six primary attributes"
                   if p["random"] != "0" else "none for this profession")
    body = []
    body.append('  <main class="container narrow">')
    body.append('    <nav class="breadcrumbs" aria-label="Breadcrumb">')
    body.append('      <a href="%sindex.html">Home</a><span class="sep">/</span>'
                '<a href="../index.html">Professions</a><span class="sep">/</span>'
                '<span>%s</span>' % (root, esc(p["name"])))
    body.append('    </nav>')
    body.append('    <div class="hero prof-hero">')
    body.append('      <div class="prof-hero__emoji" aria-hidden="true">%s</div>' % p["emoji"])
    body.append('      <div>')
    body.append('        <span class="eyebrow">Profession</span>')
    body.append('        <h1>%s</h1>' % esc(p["name"]))
    body.append('        <p class="lead">Theme: <strong>%s</strong>. System code '
                '<code>%s</code>.</p>' % (esc(p["theme"]), esc(code)))
    body.append('      </div>')
    body.append('    </div>')

    # Facts
    body.append('    <section class="section">')
    body.append('      <div class="facts">')
    body.append('        <div class="fact"><div class="fact__label">Max level</div>'
                '<div class="fact__value">%d</div></div>' % p["max"])
    body.append('        <div class="fact"><div class="fact__label">EXP per level</div>'
                '<div class="fact__value">%s</div>'
                '<div class="fact__sub">to advance one level</div></div>' % f'{p["exp_up"]:,}')
    body.append('        <div class="fact"><div class="fact__label">EXP to max</div>'
                '<div class="fact__value">%s</div>'
                '<div class="fact__sub">%s &times; %d levels</div></div>'
                % (f'{total:,}', f'{p["exp_up"]:,}', p["max"] - 1))
    body.append('        <div class="fact"><div class="fact__label">Bonus points</div>'
                '<div class="fact__value">%s</div>'
                '<div class="fact__sub">%s</div></div>'
                % (esc(p["random"]), esc(random_note)))
    body.append('      </div>')
    body.append('    </section>')

    # How to level up
    body.append('    <section class="section">')
    body.append('      <h2>How to level up</h2>')
    body.append('      <p>Every level takes <strong>%s EXP</strong>, and the class '
                'caps at <strong>level %d</strong>. Earn experience by performing the '
                'actions below — each is configured in this profession\'s YAML file. '
                'Ranges such as <code>a~b</code> award a random amount between '
                '<code>a</code> and <code>b</code>; numeric conditions such as '
                '<code>1-10</code> match the amount involved (for example damage '
                'dealt or survived).</p>'
                % (f'{p["exp_up"]:,}', p["max"]))
    body.append('      <div class="table-wrap">')
    body.append('        <table>')
    body.append('          <thead><tr><th>Action</th><th>How it triggers</th><th>EXP</th></tr></thead>')
    body.append('          <tbody>')
    body.append(action_rows(p["actions"]))
    body.append('          </tbody>')
    body.append('        </table>')
    body.append('      </div>')
    body.append('      <div class="callout callout--info"><span class="callout__icon" aria-hidden="true">\U0001F4A1</span>'
                '<div class="callout__body"><p>These values come from the bundled '
                '<code>professions/%s.yml</code>. Server owners can edit them or add '
                'entirely new professions — see <a href="../index.html#custom">Professions &amp; EXP</a>.</p></div></div>'
                % esc(code))
    body.append('    </section>')

    # Starting stats
    body.append('    <section class="section">')
    body.append('      <h2>Starting stats</h2>')
    body.append('      <p>A freshly created %s identity starts with these attributes:</p>' % esc(p["name"]))
    body.append(stat_bars(p["stats"]))
    body.append('      <p class="fact__sub">Health regenerates automatically by 1% of '
                'maximum health every 5 seconds. Food governs the hunger bar only.</p>')
    body.append('    </section>')
    body.append('  </main>')

    return (head("%s — Profession — MCIdentity" % p["name"],
                 "Max level, starting stats, and how to level up the %s profession in MCIdentity."
                 % p["name"], root, "profession", css)
            + "\n".join(body) + foot(root))


def index_page():
    root = "../"
    css = ["https://mcengine.github.io/css/main.css",
           "https://mcengine.github.io/css/shared/layout.css",
           "https://mcengine.github.io/css/shared/components.css",
           "css/custom/custom.css",
           "css/profession/profession.css"]
    cards = []
    for code in ORDER:
        p = PROFESSIONS[code]
        cards.append(
            '      <a class="prof-card" href="%s/index.html">\n'
            '        <span class="prof-card__emoji" aria-hidden="true">%s</span>\n'
            '        <span><span class="prof-card__name">%s</span><br>'
            '<span class="prof-card__theme">%s</span></span>\n'
            '      </a>' % (code, p["emoji"], esc(p["name"]), esc(p["theme"])))
    rows = []
    for code in ORDER:
        p = PROFESSIONS[code]
        acts = ", ".join(k for k, _ in p["actions"][:3])
        rows.append(
            '            <tr><td><a href="%s/index.html">%s</a></td><td>%s</td>'
            '<td>%d</td><td>%s</td><td><code>%s</code></td></tr>'
            % (code, esc(p["name"]), esc(p["theme"]), p["max"],
               f'{p["exp_up"]:,}', esc(acts)))

    body = []
    body.append('  <main class="container">')
    body.append('    <nav class="breadcrumbs" aria-label="Breadcrumb">')
    body.append('      <a href="%sindex.html">Home</a><span class="sep">/</span>'
                '<span>Professions</span>' % root)
    body.append('    </nav>')
    body.append('    <span class="eyebrow">Classes &amp; leveling</span>')
    body.append('    <h1>Professions &amp; EXP</h1>')
    body.append('    <p class="lead">Each identity is characterised by its profession. '
                'MCIdentity ships with <strong>%d bundled professions</strong>, each with its '
                'own starting stats, max level, and action-based EXP rules. Pick one to see '
                'exactly how it levels up.</p>' % len(ORDER))

    body.append('    <div class="prof-grid">')
    body.append("\n".join(cards))
    body.append('    </div>')

    # How EXP works (custom-exp.md intro)
    body.append('    <section class="section panel" id="custom">')
    body.append('      <h2>How profession EXP works</h2>')
    body.append('      <p>Server owners customise how professions gain experience by defining '
                'action-based EXP configurations in YAML files within the <code>professions/</code> '
                'folder. New professions are registered into the database automatically on first run.</p>')
    body.append('      <h3>Key requirements</h3>')
    body.append('      <ul>'
                '<li><code>system_code</code> — must be unique and provided in <strong>lowercase</strong>.</li>'
                '<li><code>display_name</code> — the human-readable name for the profession.</li></ul>')
    body.append('      <h3>EXP gain syntax</h3>')
    body.append('      <div class="accordion">')
    body.append('        <details class="acc"><summary>Simple value</summary><div class="acc__body">'
                '<p>Award a specific amount or random range of EXP.</p>'
                '<pre><code>receive_damage: 10 # Fixed\n'
                'deal_damage: 10~20 # Random range</code></pre></div></details>')
    body.append('        <details class="acc"><summary>Condition-based (numerical)</summary><div class="acc__body">'
                '<p>Award EXP based on numerical thresholds (e.g. damage amount). '
                'Supports range keys (<code>min-max</code> or <code>min~max</code>).</p>'
                '<pre><code>deal_damage:\n'
                '  "1-10": 5       # 1 to 10 damage awards 5 EXP\n'
                '  "11-50": 10~20  # 11 to 50 damage awards random 10-20 EXP\n'
                '  "51-100": 50    # 51 to 100 damage awards 50 EXP</code></pre></div></details>')
    body.append('        <details class="acc"><summary>Condition-based (string)</summary><div class="acc__body">'
                '<p>Award EXP based on specific targets (e.g. mob types).</p>'
                '<pre><code>kill_mob:\n'
                '  zombie: 20      # Killing a zombie awards 20 EXP\n'
                '  skeleton: 25    # Killing a skeleton awards 25 EXP\n'
                '  ender_dragon: 1000~2000 # Boss kill awards random large EXP</code></pre></div></details>')
    body.append('        <details class="acc"><summary>Configuration keys</summary><div class="acc__body">'
                '<ul>'
                '<li><code>level.max</code> / <code>level.exp_up</code> — the max level and EXP required per level.</li>'
                '<li><code>stats</code> — starting attributes (energy, health, food, strength, defense, wisdom, luck, agility, resilience).</li>'
                '<li><code>stats_random</code> — bonus points randomly distributed across the six primary attributes on creation.</li>'
                '<li><code>skins</code> — available Base64 skin textures; one is chosen at random per new identity.</li>'
                '</ul></div></details>')
    body.append('      </div>')
    body.append('      <div class="callout"><span class="callout__icon" aria-hidden="true">ℹ️</span>'
                '<div class="callout__body"><p>Editing or deleting a default file does not bring it back '
                'automatically; defaults are only written when the file is missing.</p></div></div>')
    body.append('    </section>')

    # Summary table
    body.append('    <section class="section">')
    body.append('      <h2>All bundled professions</h2>')
    body.append('      <div class="table-wrap"><table>')
    body.append('        <thead><tr><th>Profession</th><th>Theme</th><th>Max level</th>'
                '<th>EXP / level</th><th>Highlighted actions</th></tr></thead>')
    body.append('        <tbody>')
    body.append("\n".join(rows))
    body.append('        </tbody>')
    body.append('      </table></div>')
    body.append('    </section>')
    body.append('  </main>')

    return (head("Professions & EXP — MCIdentity",
                 "Browse MCIdentity's 21 bundled professions and learn how profession experience works.",
                 root, "profession", css)
            + "\n".join(body) + foot(root))


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", os.path.relpath(path, DOCS))


def main():
    write(os.path.join(DOCS, "profession", "index.html"), index_page())
    for code in ORDER:
        write(os.path.join(DOCS, "profession", code, "index.html"),
              detail_page(code, PROFESSIONS[code]))
    print("Generated %d profession pages + index." % len(ORDER))


if __name__ == "__main__":
    main()
