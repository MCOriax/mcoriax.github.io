# `.agents/` — portable agent instruction set

This directory holds every rule, workflow, and reference an AI agent needs to
work in this repository. The root [`AGENTS.md`](../AGENTS.md) is a thin pointer;
the real content lives here so it can be maintained and reused consistently
across repositories.

Read [`INDEX.md`](INDEX.md) first — it indexes every file below. Each subfolder
has its own `README.md` explaining what it holds.

| Folder | Purpose |
|---|---|
| [`rules/`](rules/) | Behavioural rules: iron rules and execution standards. |
| [`git/`](git/) | Git and branching workflow. |
| [`architecture/`](architecture/) | Repository structure, the index template, agent-directory layout, and this site's own structure. |

Agents must use only the `.agents/` directory belonging to the current
repository, and must not cross-reference another repository's `.agents/`.
