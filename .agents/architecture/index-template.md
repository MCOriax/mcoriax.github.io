# Universal Repository Index Template

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
