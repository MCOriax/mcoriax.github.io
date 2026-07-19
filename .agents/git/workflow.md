# Git & Branching Workflow (STRICT)

* **Task Management:** If the user provides one or multiple tasks, each task must have its own branch created, a pull request (PR) opened, and be merged separately.
* **No Master/Main:** Never work directly on the `main` or `master` branches. Create a new branch if the task scope changes; otherwise, continue on the active branch.
* **Branch Naming & Validation:** Must follow `{type}/{primary-noun}` (e.g., `feat/login`). Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Absolutely do not use preset prefixes (e.g., `claude/`, `codex/`). If a created branch does not follow the naming convention, you must recreate it (rewrite the branch name and delete the incorrect branch) or provide the user with options on how to proceed.
* **Commit Frequency & Verification:** Commit each change or group related commits. Do not wait for the entire session to finish. Always check the diff before creating a commit.
* **Commits:** Must use Conventional Commits (`type[optional scope]: description`). Commit messages must be plain text with **no links** or Jira IDs.
* **Pull Requests (PR):** Open sequentially. Always ask for user approval first. Provide a detailed report of added/modified/deleted features in the PR body. PR titles and descriptions must contain **no links**. Assume any references to github.com or gitlab.com are for their cloud-hosted environments.
