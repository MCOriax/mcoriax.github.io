#!/usr/bin/env python3
"""
EXP gain action catalog for the MCIdentity documentation site.

Every entry mirrors an action key the plugin accepts inside a
``professions/*.yml`` file and pairs it with a ready-to-paste example.
``generate_professions.py`` renders this catalog into the accordion list on the
Professions & EXP page, so the site documents each action individually instead
of describing the syntax in the abstract.

Each action declares a ``mode`` that states which value shapes it accepts:

* ``flat``   — a single value only. The action reports neither a target nor an
               amount, so a nested map is ignored.
* ``amount`` — a single value, or a map of numeric range keys matched against
               the amount the action reports.
* ``target`` — a single value, or a map keyed by the target the action reports.

Values themselves are either a fixed number (``10``) or a random range
(``10~20``), which rolls a fresh amount between the two bounds on every gain.
"""

# Display order of the action groups on the page.
GROUPS = [
    "Combat",
    "Defense",
    "Gathering",
    "Crafting & Processing",
    "Interaction & Exploration",
    "Magic & Economy",
    "Building & Survival",
    "Advanced Exploration & Movement",
    "Team & Support",
    "Farming & Ranching",
    "Exploration & Travel",
    "Interaction & Art",
    "Magic, Utility & Combat",
    "Engineering & Mechanics",
    "Dimensions & Aquatic",
    "Survival & Resilience",
    "Special Events & Bosses",
    "Specialty Farming & Pets",
    "Ranching & Wildlife",
    "Workstations & Economy",
    "World Interaction",
]

ACTIONS = [
    # --- Combat ---
    {
        "key": "deal_damage",
        "group": "Combat",
        "title": "Deal melee damage",
        "desc": "Triggered when the player deals melee damage to another entity.",
        "mode": "amount",
        "keyed_by": "the final damage dealt",
        "examples": [
            ("Same EXP for any hit", "deal_damage: 5"),
            ("Bigger hits award more",
             'deal_damage:\n'
             '  "1-10": 2~5      # a 1 to 10 damage hit awards a random 2 to 5 EXP\n'
             '  "11-50": 10~20\n'
             '  "51-100": 30~50'),
        ],
    },
    {
        "key": "kill_mob",
        "group": "Combat",
        "title": "Kill an entity",
        "desc": "Triggered when the player kills an entity.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for any kill", "kill_mob: 15"),
            ("Per entity type",
             'kill_mob:\n'
             '  zombie: 20~30\n'
             '  skeleton: 25~35\n'
             '  creeper: 40~60\n'
             '  enderman: 100~150\n'
             '  ender_dragon: 1000~2000'),
        ],
    },
    {
        "key": "deal_ranged_damage",
        "group": "Combat",
        "title": "Deal projectile damage",
        "desc": "Triggered when the player deals damage with a projectile, for example a bow.",
        "mode": "amount",
        "keyed_by": "the final damage dealt",
        "examples": [
            ("Same EXP for any shot", "deal_ranged_damage: 8"),
            ("Rewarding accurate, fully drawn shots",
             'deal_ranged_damage:\n'
             '  "1-10": 3~6\n'
             '  "11-50": 12~22\n'
             '  "51-100": 35~55'),
        ],
    },
    {
        "key": "critical_hit",
        "group": "Combat",
        "title": "Land a critical melee hit",
        "desc": "Triggered when the player lands a critical melee hit.",
        "mode": "amount",
        "keyed_by": "the final damage dealt",
        "examples": [
            ("Same EXP for any critical hit", "critical_hit: 15~25"),
            ("Scaled by the damage of the critical hit",
             'critical_hit:\n'
             '  "1-10": 5~10\n'
             '  "11-50": 15~25\n'
             '  "51-100": 40~60'),
        ],
    },

    # --- Defense ---
    {
        "key": "receive_damage",
        "group": "Defense",
        "title": "Take damage",
        "desc": "Triggered when the player takes damage.",
        "mode": "amount",
        "keyed_by": "the damage taken",
        "examples": [
            ("Same EXP for any hit taken", "receive_damage: 10"),
            ("Surviving heavier hits pays more",
             'receive_damage:\n'
             '  "1-10": 5~10\n'
             '  "11-50": 20~40\n'
             '  "51-100": 60~100\n'
             '  "101-1000": 150~300'),
        ],
    },
    {
        "key": "shield_block",
        "group": "Defense",
        "title": "Block damage with a shield",
        "desc": "Triggered when the player blocks incoming damage with a shield.",
        "mode": "amount",
        "keyed_by": "the blocked damage",
        "examples": [
            ("Same EXP for any block", "shield_block: 10~18"),
            ("Scaled by the damage absorbed",
             'shield_block:\n'
             '  "1-10": 5\n'
             '  "11-50": 15~30\n'
             '  "51-100": 40~70'),
        ],
    },
    {
        "key": "dodge_action",
        "group": "Defense",
        "title": "Evade incoming damage",
        "desc": "Triggered when the player evades incoming damage. The dodge chance scales with "
                "the identity's <code>agility</code> stat, and a successful dodge fully negates "
                "the damage.",
        "mode": "flat",
        "examples": [
            ("Fixed reward per dodge", "dodge_action: 20"),
        ],
    },

    # --- Gathering ---
    {
        "key": "break_ore",
        "group": "Gathering",
        "title": "Break an ore block",
        "desc": "Triggered when the player breaks an ore block.",
        "mode": "target",
        "keyed_by": "the ore material",
        "examples": [
            ("Same EXP for every ore", "break_ore: 3"),
            ("Rarer ores pay more",
             'break_ore:\n'
             '  coal_ore: 2\n'
             '  iron_ore: 4\n'
             '  gold_ore: 6\n'
             '  diamond_ore: 20\n'
             '  emerald_ore: 25\n'
             '  ancient_debris: 50'),
        ],
    },
    {
        "key": "chop_tree",
        "group": "Gathering",
        "title": "Break a log block",
        "desc": "Triggered when the player breaks a log block.",
        "mode": "target",
        "keyed_by": "the log material",
        "examples": [
            ("Same EXP for every log", "chop_tree: 2~4"),
            ("Per wood type",
             'chop_tree:\n'
             '  oak_log: 2\n'
             '  birch_log: 2\n'
             '  dark_oak_log: 3\n'
             '  warped_stem: 5'),
        ],
    },
    {
        "key": "harvest_crop",
        "group": "Gathering",
        "title": "Break a fully grown crop",
        "desc": "Triggered when the player breaks a fully grown crop.",
        "mode": "target",
        "keyed_by": "the crop material",
        "examples": [
            ("Same EXP for every crop", "harvest_crop: 1~3"),
            ("Per crop",
             'harvest_crop:\n'
             '  wheat: 2\n'
             '  carrots: 2\n'
             '  potatoes: 2\n'
             '  beetroots: 3\n'
             '  nether_wart: 4'),
        ],
    },
    {
        "key": "fish_caught",
        "group": "Gathering",
        "title": "Reel in a fish",
        "desc": "Triggered when the player reels in a fish.",
        "mode": "flat",
        "examples": [
            ("Random reward per catch", "fish_caught: 4~8"),
        ],
    },

    # --- Crafting & processing ---
    {
        "key": "craft_item",
        "group": "Crafting & Processing",
        "title": "Craft an item",
        "desc": "Triggered when the player crafts an item.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every recipe", "craft_item: 2"),
            ("Valuable recipes pay more",
             'craft_item:\n'
             '  stick: 1\n'
             '  iron_pickaxe: 8\n'
             '  diamond_sword: 30\n'
             '  enchanting_table: 50'),
        ],
    },
    {
        "key": "smelt_furnace",
        "group": "Crafting & Processing",
        "title": "Take a smelted item from a furnace",
        "desc": "Triggered when the player extracts a smelted item from a furnace.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every smelt", "smelt_furnace: 3"),
            ("Per smelted result",
             'smelt_furnace:\n'
             '  cooked_beef: 3\n'
             '  iron_ingot: 5\n'
             '  gold_ingot: 6\n'
             '  netherite_scrap: 40'),
        ],
    },
    {
        "key": "brew_potion",
        "group": "Crafting & Processing",
        "title": "Collect a brewed potion",
        "desc": "Triggered when the player collects a brewed potion from a brewing stand.",
        "mode": "flat",
        "examples": [
            ("Fixed reward per potion", "brew_potion: 12"),
        ],
    },

    # --- Interaction & exploration ---
    {
        "key": "tame_animal",
        "group": "Interaction & Exploration",
        "title": "Tame an animal",
        "desc": "Triggered when the player tames an animal.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every tame", "tame_animal: 25~40"),
            ("Per animal",
             'tame_animal:\n'
             '  wolf: 25\n'
             '  cat: 30\n'
             '  llama: 30\n'
             '  parrot: 35\n'
             '  horse: 40'),
        ],
    },
    {
        "key": "breed_animal",
        "group": "Interaction & Exploration",
        "title": "Breed two animals",
        "desc": "Triggered when the player breeds two animals.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every pairing", "breed_animal: 8~12"),
            ("Harder animals pay more",
             'breed_animal:\n'
             '  cow: 8\n'
             '  sheep: 8\n'
             '  turtle: 30\n'
             '  panda: 40'),
        ],
    },
    {
        "key": "explore_biome",
        "group": "Interaction & Exploration",
        "title": "Enter a new biome",
        "desc": "Triggered the first time the player enters a given biome during the current "
                "server session.",
        "mode": "target",
        "keyed_by": "the biome name",
        "examples": [
            ("Same EXP for every new biome", "explore_biome: 30"),
            ("Remote biomes pay more",
             'explore_biome:\n'
             '  plains: 10\n'
             '  desert: 15\n'
             '  jungle: 30\n'
             '  deep_dark: 80\n'
             '  end_highlands: 120'),
        ],
    },
    {
        "key": "heal_target",
        "group": "Interaction & Exploration",
        "title": "Heal another entity",
        "desc": "Triggered when the player heals another entity with a splash potion.",
        "mode": "flat",
        "examples": [
            ("Fixed reward per heal", "heal_target: 20"),
        ],
    },

    # --- Magic & economy ---
    {
        "key": "enchant_item",
        "group": "Magic & Economy",
        "title": "Enchant an item",
        "desc": "Triggered when the player enchants an item at an enchanting table.",
        "mode": "target",
        "keyed_by": "the item material",
        "examples": [
            ("Same EXP for every enchant", "enchant_item: 20~35"),
            ("Per enchanted item",
             'enchant_item:\n'
             '  book: 15\n'
             '  diamond_sword: 35\n'
             '  netherite_chestplate: 60'),
        ],
    },
    {
        "key": "villager_trade",
        "group": "Magic & Economy",
        "title": "Complete a villager trade",
        "desc": "Triggered when the player collects the result of a villager trade.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every trade", "villager_trade: 5"),
            ("Per traded result",
             'villager_trade:\n'
             '  emerald: 4\n'
             '  experience_bottle: 12\n'
             '  enchanted_book: 30'),
        ],
    },
    {
        "key": "repair_item",
        "group": "Magic & Economy",
        "title": "Repair or combine an item on an anvil",
        "desc": "Triggered when the player takes a repaired or combined item out of an anvil. "
                "Only durability-bearing items qualify.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every repair", "repair_item: 8~15"),
            ("Per repaired item",
             'repair_item:\n'
             '  iron_pickaxe: 8\n'
             '  diamond_chestplate: 20\n'
             '  elytra: 40'),
        ],
    },

    # --- Building & survival ---
    {
        "key": "place_block",
        "group": "Building & Survival",
        "title": "Place a block",
        "desc": "Triggered when the player places a block. A location is rewarded only once, "
                "preventing the place / break / replace EXP farm.",
        "mode": "target",
        "keyed_by": "the block material",
        "examples": [
            ("Same EXP for every block", "place_block: 1~2"),
            ("Decorative blocks pay more",
             'place_block:\n'
             '  stone: 1\n'
             '  oak_planks: 1\n'
             '  quartz_block: 3\n'
             '  sea_lantern: 5'),
        ],
    },
    {
        "key": "consume_food",
        "group": "Building & Survival",
        "title": "Eat a food item",
        "desc": "Triggered when the player eats a food item. Non-food consumables such as "
                "potions and milk are ignored.",
        "mode": "target",
        "keyed_by": "the food material",
        "examples": [
            ("Same EXP for every meal", "consume_food: 2~4"),
            ("Per dish",
             'consume_food:\n'
             '  bread: 2\n'
             '  cooked_beef: 4\n'
             '  golden_carrot: 10\n'
             '  enchanted_golden_apple: 50'),
        ],
    },
    {
        "key": "shear_entity",
        "group": "Building & Survival",
        "title": "Shear an entity",
        "desc": "Triggered when the player shears an entity such as a sheep.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every shear", "shear_entity: 4"),
            ("Per entity",
             'shear_entity:\n'
             '  sheep: 4\n'
             '  snow_golem: 6\n'
             '  mooshroom: 8'),
        ],
    },

    # --- Advanced exploration & movement ---
    {
        "key": "open_loot_chest",
        "group": "Advanced Exploration & Movement",
        "title": "Open a generated loot container",
        "desc": "Triggered when the player opens a naturally generated loot container. A vanilla "
                "loot table only generates once, so the reward cannot be farmed.",
        "mode": "flat",
        "examples": [
            ("Random reward per container", "open_loot_chest: 50~80"),
        ],
    },
    {
        "key": "glide_elytra",
        "group": "Advanced Exploration & Movement",
        "title": "Start gliding with an elytra",
        "desc": "Triggered when the player starts gliding with an elytra. Rate-limited per player "
                "to prevent rapid toggle farming.",
        "mode": "flat",
        "examples": [
            ("Random reward per launch", "glide_elytra: 10~15"),
        ],
    },
    {
        "key": "survive_fall",
        "group": "Advanced Exploration & Movement",
        "title": "Survive fall damage",
        "desc": "Triggered when the player takes fall damage but survives it.",
        "mode": "amount",
        "keyed_by": "the survived damage amount",
        "examples": [
            ("Same EXP for any fall", "survive_fall: 20"),
            ("Longer falls pay more",
             'survive_fall:\n'
             '  "1-5": 5\n'
             '  "6-15": 20\n'
             '  "16-100": 40~70'),
        ],
    },

    # --- Team & support ---
    {
        "key": "apply_buff",
        "group": "Team & Support",
        "title": "Buff another player",
        "desc": "Triggered when the player lands a beneficial (non-healing) potion on another "
                "player. Kept distinct from <code>heal_target</code>, which covers instant "
                "healing.",
        "mode": "flat",
        "examples": [
            ("Random reward per buff", "apply_buff: 15~25"),
        ],
    },

    # --- Farming & ranching ---
    {
        "key": "plant_crop",
        "group": "Farming & Ranching",
        "title": "Plant a crop seed",
        "desc": "Triggered when the player plants a crop seed.",
        "mode": "target",
        "keyed_by": "the planted crop material",
        "examples": [
            ("Same EXP for every seed", "plant_crop: 1~2"),
            ("Per crop",
             'plant_crop:\n'
             '  wheat: 1\n'
             '  carrots: 1\n'
             '  potatoes: 1\n'
             '  nether_wart: 3\n'
             '  torchflower_crop: 8'),
        ],
    },
    {
        "key": "strip_log",
        "group": "Farming & Ranching",
        "title": "Strip a log with an axe",
        "desc": "Triggered when the player strips a log with an axe. A location is rewarded only "
                "once, preventing the place / strip / break / replace farm.",
        "mode": "target",
        "keyed_by": "the log material",
        "examples": [
            ("Same EXP for every log", "strip_log: 2~3"),
            ("Per wood type",
             'strip_log:\n'
             '  oak_log: 2\n'
             '  spruce_log: 2\n'
             '  crimson_stem: 4'),
        ],
    },
    {
        "key": "milk_entity",
        "group": "Farming & Ranching",
        "title": "Milk an entity with a bucket",
        "desc": "Triggered when the player milks a cow, mushroom cow or goat with a bucket.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every bucket", "milk_entity: 3~5"),
            ("Per animal",
             'milk_entity:\n'
             '  cow: 3\n'
             '  mooshroom: 5\n'
             '  goat: 8'),
        ],
    },
    {
        "key": "catch_entity_bucket",
        "group": "Farming & Ranching",
        "title": "Capture an entity in a bucket",
        "desc": "Triggered when the player captures an entity in a bucket, such as a fish or an "
                "axolotl.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every capture", "catch_entity_bucket: 5"),
            ("Rarer catches pay more",
             'catch_entity_bucket:\n'
             '  cod: 5\n'
             '  salmon: 5\n'
             '  pufferfish: 8\n'
             '  tadpole: 8\n'
             '  tropical_fish: 12\n'
             '  axolotl: 25'),
        ],
    },

    # --- Exploration & travel ---
    {
        "key": "discover_structure",
        "group": "Exploration & Travel",
        "title": "Discover a major structure",
        "desc": "Triggered when the player discovers a major structure, detected through the "
                "vanilla advancement granted on entry (stronghold, nether fortress, bastion "
                "remnant).",
        "mode": "flat",
        "examples": [
            ("Random reward per discovery", "discover_structure: 80~150"),
        ],
    },
    {
        "key": "ride_vehicle",
        "group": "Exploration & Travel",
        "title": "Start riding a vehicle",
        "desc": "Triggered when the player starts riding a vehicle such as a boat or a minecart. "
                "Rate-limited per player.",
        "mode": "target",
        "keyed_by": "the vehicle entity type",
        "examples": [
            ("Same EXP for every vehicle", "ride_vehicle: 3~5"),
            ("Per vehicle",
             'ride_vehicle:\n'
             '  boat: 3\n'
             '  minecart: 4\n'
             '  chest_boat: 6'),
        ],
    },
    {
        "key": "leash_entity",
        "group": "Exploration & Travel",
        "title": "Leash an entity",
        "desc": "Triggered when the player leashes an entity. Rate-limited per player.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every leash", "leash_entity: 5~8"),
            ("Per animal",
             'leash_entity:\n'
             '  cow: 4\n'
             '  sheep: 4\n'
             '  llama: 8\n'
             '  allay: 15'),
        ],
    },

    # --- Interaction & art ---
    {
        "key": "play_music_disc",
        "group": "Interaction & Art",
        "title": "Play a music disc",
        "desc": "Triggered when the player inserts a music disc into an empty jukebox. Ejecting "
                "a disc is not rewarded.",
        "mode": "flat",
        "examples": [
            ("Random reward per disc", "play_music_disc: 10~15"),
        ],
    },
    {
        "key": "dye_item",
        "group": "Interaction & Art",
        "title": "Dye a sheep",
        "desc": "Triggered when the player dyes a sheep. Rate-limited per player.",
        "mode": "target",
        "keyed_by": "the dye material",
        "examples": [
            ("Same EXP for every dye", "dye_item: 2~4"),
            ("Per dye",
             'dye_item:\n'
             '  black_dye: 2\n'
             '  cyan_dye: 4\n'
             '  pink_dye: 4'),
        ],
    },
    {
        "key": "carve_pumpkin",
        "group": "Interaction & Art",
        "title": "Carve a pumpkin",
        "desc": "Triggered when the player carves a pumpkin with shears. A location is rewarded "
                "only once.",
        "mode": "flat",
        "examples": [
            ("Random reward per pumpkin", "carve_pumpkin: 5~8"),
        ],
    },
    {
        "key": "ring_bell",
        "group": "Interaction & Art",
        "title": "Ring a bell",
        "desc": "Triggered when the player rings a bell. Rate-limited per player.",
        "mode": "flat",
        "examples": [
            ("Random reward per ring", "ring_bell: 3~5"),
        ],
    },

    # --- Magic, utility & combat ---
    {
        "key": "ignite_fire",
        "group": "Magic, Utility & Combat",
        "title": "Ignite a fire",
        "desc": "Triggered when the player ignites a fire with flint and steel. Rate-limited per "
                "player.",
        "mode": "flat",
        "examples": [
            ("Random reward per fire", "ignite_fire: 2~4"),
        ],
    },
    {
        "key": "consume_potion",
        "group": "Magic, Utility & Combat",
        "title": "Drink a potion",
        "desc": "Triggered when the player drinks a potion.",
        "mode": "flat",
        "examples": [
            ("Random reward per potion", "consume_potion: 5~10"),
        ],
    },
    {
        "key": "apply_debuff",
        "group": "Magic, Utility & Combat",
        "title": "Debuff another entity",
        "desc": "Triggered when the player lands a harmful potion on another entity.",
        "mode": "flat",
        "examples": [
            ("Random reward per debuff", "apply_debuff: 10~18"),
        ],
    },
    {
        "key": "cure_zombie_villager",
        "group": "Magic, Utility & Combat",
        "title": "Cure a zombie villager",
        "desc": "Triggered when the player feeds a golden apple to a weakened zombie villager, "
                "starting the cure.",
        "mode": "flat",
        "examples": [
            ("Random reward per cure", "cure_zombie_villager: 100~150"),
        ],
    },

    # --- Engineering & mechanics ---
    {
        "key": "place_redstone",
        "group": "Engineering & Mechanics",
        "title": "Place a redstone component",
        "desc": "Triggered when the player places a redstone component such as dust, a repeater, "
                "a piston, an observer, a button or a pressure plate. A location is rewarded "
                "only once, preventing the place / break / replace farm.",
        "mode": "target",
        "keyed_by": "the block material",
        "examples": [
            ("Same EXP for every component", "place_redstone: 1~3"),
            ("Per component",
             'place_redstone:\n'
             '  redstone_wire: 1\n'
             '  repeater: 3\n'
             '  observer: 5\n'
             '  piston: 6'),
        ],
    },
    {
        "key": "create_golem",
        "group": "Engineering & Mechanics",
        "title": "Build a utility golem",
        "desc": "Triggered when a player builds a utility golem. The Bukkit API does not "
                "attribute the build to a player, so the reward is credited to the nearest "
                "player around the spawn.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every golem", "create_golem: 30"),
            ("Per golem",
             'create_golem:\n'
             '  snow_golem: 15~25\n'
             '  iron_golem: 40~60'),
        ],
    },
    {
        "key": "activate_conduit",
        "group": "Engineering & Mechanics",
        "title": "Activate a conduit",
        "desc": "Triggered when the player places (activates) a conduit. A location is rewarded "
                "only once.",
        "mode": "flat",
        "examples": [
            ("Random reward per conduit", "activate_conduit: 30~50"),
        ],
    },

    # --- Dimensions & aquatic ---
    {
        "key": "swim_distance",
        "group": "Dimensions & Aquatic",
        "title": "Swim 10 blocks",
        "desc": "Triggered for every 10 blocks the player swims (sprint-swimming in water). "
                "Distance is accumulated per player so the reward scales with genuine travel "
                "rather than firing on every move.",
        "mode": "flat",
        "examples": [
            ("Random reward per 10 blocks", "swim_distance: 2~4"),
        ],
    },
    {
        "key": "enter_portal",
        "group": "Dimensions & Aquatic",
        "title": "Travel through a portal",
        "desc": "Triggered when the player travels through a nether or end portal. Rate-limited "
                "per player to stop back-and-forth farming.",
        "mode": "target",
        "keyed_by": "the destination environment",
        "examples": [
            ("Same EXP for every portal", "enter_portal: 20"),
            ("Per destination",
             'enter_portal:\n'
             '  nether: 15~25\n'
             '  the_end: 40~60'),
        ],
    },
    {
        "key": "use_totem",
        "group": "Dimensions & Aquatic",
        "title": "Be saved by a totem of undying",
        "desc": "Triggered when a totem of undying saves the player from death.",
        "mode": "flat",
        "examples": [
            ("Random reward per totem", "use_totem: 50~100"),
        ],
    },

    # --- Survival & resilience ---
    {
        "key": "sleep_in_bed",
        "group": "Survival & Resilience",
        "title": "Sleep in a bed",
        "desc": "Triggered when the player successfully lies down to sleep in a bed. Rate-limited per player.",
        "mode": "flat",
        "examples": [
            ("Random reward per night", "sleep_in_bed: 5~10"),
        ],
    },
    {
        "key": "extinguish_fire",
        "group": "Survival & Resilience",
        "title": "Extinguish a fire block",
        "desc": "Triggered when the player extinguishes a fire block. Rate-limited per player to "
                "defeat the ignite / extinguish farm.",
        "mode": "target",
        "keyed_by": "the fire material",
        "examples": [
            ("Same EXP for every fire", "extinguish_fire: 3~6"),
            ("Per fire type",
             'extinguish_fire:\n'
             '  fire: 3\n'
             '  soul_fire: 6'),
        ],
    },
    {
        "key": "survive_explosion",
        "group": "Survival & Resilience",
        "title": "Survive an explosion",
        "desc": "Triggered when the player takes block or entity explosion damage but survives "
                "it.",
        "mode": "amount",
        "keyed_by": "the survived damage amount",
        "examples": [
            ("Same EXP for any explosion", "survive_explosion: 30"),
            ("Bigger blasts pay more",
             'survive_explosion:\n'
             '  "1-5": 10\n'
             '  "6-15": 30\n'
             '  "16-100": 60~100'),
        ],
    },

    # --- Special events & bosses ---
    {
        "key": "trigger_raid",
        "group": "Special Events & Bosses",
        "title": "Trigger a village raid",
        "desc": "Triggered when the player triggers a village raid, for example by entering a "
                "village while carrying Bad Omen.",
        "mode": "flat",
        "examples": [
            ("Random reward per raid", "trigger_raid: 20~40"),
        ],
    },
    {
        "key": "win_raid",
        "group": "Special Events & Bosses",
        "title": "Win a village raid",
        "desc": "Triggered for every player credited with winning a village raid.",
        "mode": "flat",
        "examples": [
            ("Random reward per victory", "win_raid: 150~300"),
        ],
    },
    {
        "key": "summon_boss",
        "group": "Special Events & Bosses",
        "title": "Summon a boss",
        "desc": "Triggered when a player summons a boss such as the Wither. The reward is "
                "credited to the nearest player around the spawn.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every boss", "summon_boss: 200~400"),
            ("Per boss",
             'summon_boss:\n'
             '  wither: 200~400'),
        ],
    },

    # --- Specialty farming & pets ---
    {
        "key": "feed_pet",
        "group": "Specialty Farming & Pets",
        "title": "Feed one of your own pets",
        "desc": "Triggered when the player feeds one of their own tamed pets an actual food "
                "item. Rate-limited per player.",
        "mode": "target",
        "keyed_by": "the entity type",
        "examples": [
            ("Same EXP for every pet", "feed_pet: 2~4"),
            ("Per pet",
             'feed_pet:\n'
             '  wolf: 2\n'
             '  cat: 3\n'
             '  parrot: 4'),
        ],
    },
    {
        "key": "hatch_egg",
        "group": "Specialty Farming & Pets",
        "title": "Hatch a chick from a thrown egg",
        "desc": "Triggered when a thrown egg hatches into a chick.",
        "mode": "flat",
        "examples": [
            ("Random reward per chick", "hatch_egg: 5~10"),
        ],
    },
    {
        "key": "collect_honey",
        "group": "Specialty Farming & Pets",
        "title": "Bottle honey from a full hive",
        "desc": "Triggered when the player bottles honey from a full beehive or bee nest with a "
                "glass bottle. Only a full hive yields honey, which the bees take real time to "
                "refill.",
        "mode": "flat",
        "examples": [
            ("Random reward per bottle", "collect_honey: 5~10"),
        ],
    },

    # --- Ranching & wildlife ---
    {
        "key": "shear_sheep_color",
        "group": "Ranching & Wildlife",
        "title": "Shear a sheep of a given color",
        "desc": "Triggered when the player shears a sheep. Fires alongside "
                "<code>shear_entity</code>, so configs can reward rare colors specifically. "
                "Re-shearing is gated by vanilla wool regrowth.",
        "mode": "target",
        "keyed_by": "the sheep's wool color",
        "examples": [
            ("Same EXP for every color", "shear_sheep_color: 10"),
            ("Rare colors pay more",
             'shear_sheep_color:\n'
             '  white: 5\n'
             '  brown: 15\n'
             '  light_blue: 18\n'
             '  pink: 25'),
        ],
    },
    {
        "key": "shear_mushroom_cow",
        "group": "Ranching & Wildlife",
        "title": "Shear a mooshroom",
        "desc": "Triggered when the player shears a mooshroom. A mooshroom is sheared only once "
                "before it reverts to a cow, so it cannot be farmed.",
        "mode": "flat",
        "examples": [
            ("Random reward per mooshroom", "shear_mushroom_cow: 20~30"),
        ],
    },
    {
        "key": "spawn_axolotl_bucket",
        "group": "Ranching & Wildlife",
        "title": "Release an axolotl from a bucket",
        "desc": "Triggered when the player releases an axolotl from a bucket into the world. The "
                "companion action to <code>catch_entity_bucket</code>.",
        "mode": "flat",
        "examples": [
            ("Random reward per release", "spawn_axolotl_bucket: 15~25"),
        ],
    },
    {
        "key": "sniff_sniffer_egg",
        "group": "Ranching & Wildlife",
        "title": "A sniffer unearths an ancient seed",
        "desc": "Triggered when a sniffer unearths an ancient seed. The dig is not attributed by "
                "the Bukkit API, so the reward is credited to the nearest player around the "
                "sniffer.",
        "mode": "target",
        "keyed_by": "the unearthed seed item",
        "examples": [
            ("Same EXP for every seed", "sniff_sniffer_egg: 80"),
            ("Per seed",
             'sniff_sniffer_egg:\n'
             '  torchflower_seeds: 80\n'
             '  pitcher_pod: 90'),
        ],
    },

    # --- Workstations & economy ---
    {
        "key": "sculpt_chiseled_block",
        "group": "Workstations & Economy",
        "title": "Cut a chiseled block on a stonecutter",
        "desc": "Triggered when the player cuts a chiseled block variant on a stonecutter.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every cut", "sculpt_chiseled_block: 4~6"),
            ("Per variant",
             'sculpt_chiseled_block:\n'
             '  chiseled_stone_bricks: 4\n'
             '  chiseled_deepslate: 5\n'
             '  chiseled_quartz_block: 6'),
        ],
    },
    {
        "key": "use_smithing_template",
        "group": "Workstations & Economy",
        "title": "Take a result out of a smithing table",
        "desc": "Triggered when the player takes a result out of a smithing table, which always "
                "consumes a smithing template.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every upgrade", "use_smithing_template: 10~15"),
            ("Per result",
             'use_smithing_template:\n'
             '  diamond_helmet: 10\n'
             '  netherite_sword: 25\n'
             '  netherite_chestplate: 30'),
        ],
    },
    {
        "key": "repair_trident",
        "group": "Workstations & Economy",
        "title": "Repair a trident on an anvil",
        "desc": "Triggered when the player takes a repaired trident out of an anvil. Kept "
                "separate from the general <code>repair_item</code> so tridents can be rewarded "
                "specifically.",
        "mode": "flat",
        "examples": [
            ("Random reward per repair", "repair_trident: 12~20"),
        ],
    },
    {
        "key": "complete_map_fill",
        "group": "Workstations & Economy",
        "title": "Lock a map at a cartography table",
        "desc": "Triggered when the player finalizes a map by locking it at a cartography table. "
                "Locking captures a permanent snapshot of the explored map, and the glass-pane "
                "cost is the natural gate.",
        "mode": "flat",
        "examples": [
            ("Random reward per locked map", "complete_map_fill: 25~40"),
        ],
    },
    {
        "key": "trade_special_wandering",
        "group": "Workstations & Economy",
        "title": "Trade with a wandering trader",
        "desc": "Triggered when the player completes a trade with a wandering trader "
                "specifically. Fires alongside <code>villager_trade</code>.",
        "mode": "target",
        "keyed_by": "the result material",
        "examples": [
            ("Same EXP for every trade", "trade_special_wandering: 10"),
            ("Per traded result",
             'trade_special_wandering:\n'
             '  emerald: 8\n'
             '  experience_bottle: 20\n'
             '  enchanted_book: 40'),
        ],
    },

    # --- World interaction ---
    {
        "key": "ignite_campfire",
        "group": "World Interaction",
        "title": "Light an unlit campfire",
        "desc": "Triggered when the player lights an unlit campfire with flint and steel or a "
                "fire charge. Rate-limited per player to defeat the light / extinguish farm.",
        "mode": "target",
        "keyed_by": "the campfire material",
        "examples": [
            ("Same EXP for every campfire", "ignite_campfire: 5"),
            ("Per campfire type",
             'ignite_campfire:\n'
             '  campfire: 5\n'
             '  soul_campfire: 8'),
        ],
    },
    {
        "key": "harvest_sweet_berries",
        "group": "World Interaction",
        "title": "Gather sweet berries",
        "desc": "Triggered when the player gathers berries from a ripe sweet berry bush. Gated "
                "by the vanilla bush growth stage, so it cannot be farmed by re-clicking an "
                "empty bush.",
        "mode": "flat",
        "examples": [
            ("Random reward per bush", "harvest_sweet_berries: 3~5"),
        ],
    },
    {
        "key": "brush_archaeology",
        "group": "World Interaction",
        "title": "Brush a suspicious block",
        "desc": "Triggered when the player brushes a suspicious block. A suspicious block holds "
                "a single loot and is rewarded only once.",
        "mode": "target",
        "keyed_by": "the brushed block material",
        "examples": [
            ("Same EXP for every brush", "brush_archaeology: 40~60"),
            ("Per block",
             'brush_archaeology:\n'
             '  suspicious_sand: 40~60\n'
             '  suspicious_gravel: 50~70'),
        ],
    },
    {
        "key": "use_ender_eye_portal",
        "group": "World Interaction",
        "title": "Place an eye of ender in a portal frame",
        "desc": "Triggered when the player places an eye of ender into an empty end portal "
                "frame. A frame is rewarded only once.",
        "mode": "flat",
        "examples": [
            ("Random reward per frame", "use_ender_eye_portal: 30~50"),
        ],
    },
    {
        "key": "plant_flower",
        "group": "World Interaction",
        "title": "Plant a flower",
        "desc": "Triggered when the player plants a flower on the ground or into a flower pot. A "
                "location is rewarded only once, preventing the place / break / replace farm.",
        "mode": "target",
        "keyed_by": "the flower material",
        "examples": [
            ("Same EXP for every flower", "plant_flower: 2~4"),
            ("Rare flowers pay more",
             'plant_flower:\n'
             '  dandelion: 2\n'
             '  poppy: 2\n'
             '  lily_of_the_valley: 5\n'
             '  wither_rose: 12'),
        ],
    },
    {
        "key": "clean_armor_trim",
        "group": "World Interaction",
        "title": "Wash a trimmed armor piece",
        "desc": "Triggered when the player washes a trimmed armor piece in a cauldron. Rate-limited per player.",
        "mode": "target",
        "keyed_by": "the trim pattern",
        "examples": [
            ("Same EXP for every trim", "clean_armor_trim: 8~12"),
            ("Per pattern",
             'clean_armor_trim:\n'
             '  dune: 8\n'
             '  sentry: 8\n'
             '  eye: 15\n'
             '  silence: 20'),
        ],
    },
]


def actions_by_group():
    """Groups the catalog in display order.

    :return: A list of ``(group_name, [action, ...])`` pairs.
    """
    return [(group, [a for a in ACTIONS if a["group"] == group]) for group in GROUPS]


def shape_note(action):
    """Builds the sentence that states which value shapes an action accepts.

    :param action: A catalog entry.
    :return: A sentence with inline ``<code>`` markup.
    """
    mode = action["mode"]
    if mode == "flat":
        return ("Takes a single value. The action reports neither a target nor an amount, "
                "so a nested map is ignored.")
    if mode == "amount":
        return ("Takes a single value, or a map of range keys written "
                "<code>\"min-max\"</code> or <code>\"min~max\"</code> and matched against %s. "
                "An amount outside every range awards nothing." % action["keyed_by"])
    return ("Takes a single value that rewards every case equally, or a map keyed by %s in "
            "lowercase. Keys you leave out award nothing." % action["keyed_by"])
