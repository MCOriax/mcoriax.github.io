# Regenerate the Profession Pages

[← Back to README](../../README.md)

The profession pages are **generated — do not hand-edit them.** Any manual edit
is lost the next time the generator runs.

## Regenerate

```bash
python3 scripts/generate_professions.py
```

This rewrites:

* `docs/profession/index.html` — the professions overview, the per-action EXP
  gain reference (one accordion with a worked example per action key), and the
  full profession table.
* `docs/profession/{profession_name}/index.html` — one detail page per bundled
  profession, covering max level, stats, and how to level up.

## Add or change a profession

Update the data in
[`scripts/generate_professions.py`](../../scripts/generate_professions.py) — it
mirrors the plugin's default `professions/*.yml` — then regenerate.

The bundled professions are `acrobat`, `archaeologist`, `archer`, `builder`,
`chef`, `crafter`, `enchanter`, `engineer`, `explorer`, `farmer`, `fighter`,
`fisher`, `gatherer`, `guard`, `lumberjack`, `mariner`, `merchant`, `miner`,
`supporter`, `tamer`, and `tanker`.

## Add or change an EXP action

The catalog of EXP gain action keys — each with its trigger, accepted value
shapes, and YAML examples — lives in
[`scripts/exp_actions.py`](../../scripts/exp_actions.py). It is rendered onto the
profession listing page, so edit it there and regenerate.

## After regenerating

1. Review the diff. A data change should produce a proportionate page change; a
   sweeping diff usually means a template change you did not intend.
2. Serve the site locally and check a profession page renders correctly — see
   [Local Setup](../environments/setup.md).
3. If the set of professions changed, update
   [`../reference/site-structure.md`](../reference/site-structure.md) in the same
   commit.
