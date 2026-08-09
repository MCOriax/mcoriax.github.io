---
name: execution-rules
description: Strict initialization, execution, modularity, versioning, documentation, and environment standards.
---

# Strict Rules & Execution

* **Initialization (Read & Understand):** For every repository being worked on (single or multiple), you must perform the following:
  1. **Structure (`INDEX.md`):** Always read the root `INDEX.md` — the router — and then the ONE scope index it points at that matches the task. Follow the reading order in [`../../AGENTS.md`](../../AGENTS.md). Index shape, the split threshold, and the canonical template are owned by [`../creators/index-creator.md`](../creators/index-creator.md). Update the index that owns a changed scope in the same commit.
  2. **Context (`README.md`):** Always read `README.md` to understand the core project goals, context, setup instructions, and to verify the project hosting information. If the hosting information is missing, refer to the **Project Hosting Validation** iron rule in [`iron.md`](iron.md) immediately.
* **Execution:** Create a solid plan. Write code section-by-section. Test thoroughly by executing the project's standard test suite via the command line (e.g., `npm test`, `pytest`, `cargo test`) and fix any errors. Verify code security for modified files before completing the task.
* **Modularity:** Separate code into multiple focused files and modules to prevent spaghetti code. Keep files concise and adhere to the Single Responsibility Principle.
* **Dashes:** Do not use dashes (`-`) unnecessarily. Use them strictly for file or directory names (e.g., `getting-started.md`) and branch names. Avoid them in variable names, database schemas, or general prose unless standard conventions explicitly require it.
* **Versioning:** Versions use Semantic Versioning (`Major.Minor.Patch`). **Never change a version on your own initiative** — propose the bump, state which of major/minor/patch and why, and wait for explicit user approval. This supersedes any earlier instruction to bump the version on every pull request. See [`versioning.md`](versioning.md).
* **Documents:** The root `README.md` must contain only an overview of the project. Detailed documentation lives under `wiki/{folder}/{file-name}.md`, in kebab-case, one topic per file, placed by the algorithm in [`directories.md`](directories.md). Never place a loose file at the root of `wiki/` — `INDEX.md` is the only file allowed there.
* **Environment:** Do not create a `.env.example` file. Instead, document the required environment variables within `wiki/environments/env.md` using a code block. When providing example values, do not use actual realistic text; use standardized placeholders such as `your_{name}_api_key`, `your_server_api_key`, or `your_openrouter_api_key`. Any examples of infrastructure configurations (e.g., Kubernetes, docker-compose, etc.) must also be written exclusively within `wiki/environments/`.
* **Website Synchronization:** If the user has also cloned the website repository, the agents must update the website contents accordingly.
