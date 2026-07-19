# Iron Rules

* **Platform Specification:** Whether working with a single repository or multiple repositories, the user must explicitly specify the cloud hosting platform for each repository. For example:
  * `{org}/{repo} - github.com`
  * `{org}/{repo} - gitlab.com`
* **Project Hosting Validation:** The project hosting information must be clearly documented in the first section of the `README.md` file. If this information is missing, you must ask the user where the project is hosted and update the `README.md` to include it using exactly this format (ensuring the items are clickable links):
  ```markdown
  # Project Overview

  * **Platform:** [github.com](link) or [gitlab.com](link)
  * **Organization:** [organization-name](link)
  * **Repository:** [repository-name](link)
  ```
