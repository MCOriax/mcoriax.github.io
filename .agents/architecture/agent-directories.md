# Agent Directories

All agent-specific files and configurations must be centralized under the `.agents/` directory. Each repository will have its own `.agents/` directory. Agents must strictly use the agent directory belonging to the current repository and must not use or cross-reference `.agents/` directories from another repository.

* `.agents/`: Root directory for all agent configurations.
* `.agents/skills/`: Specific skill definitions and execution steps.
* `.agents/tools/`: Tool definitions and schemas.
* `.agents/knowledge/`: Domain-specific context.
* `.agents/personas/`: Specific roles to adopt.
* `.agents/ethics/`: Safety bounds and constraints.

In addition to the categories above, this instruction set uses the following
working folders (each with its own `README.md`):

* `.agents/rules/`: Behavioural rules (iron rules, execution standards, and repository-specific rules).
* `.agents/git/`: Git and branching workflow.
* `.agents/architecture/`: Repository structure, the index template, this directory layout, and the site's own structure.
