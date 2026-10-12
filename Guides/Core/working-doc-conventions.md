Managed-By: skai
Managed-Id: guide.working-doc-conventions
Managed-Source: Guides/Core/working-doc-conventions.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-10

# Working Document Conventions

Before using this guide, complete [Project addendum](#project-addendum) loading below.

Working documents (planning docs, work specs, test work docs, test artifacts) are ephemeral files that track in-progress work. They live under `skai/working-docs/`, are organized by git branch, and are grouped into named session folders so multiple efforts on the same branch do not collide.

## Location

All working documents live under `skai/working-docs/` at the project root.

Within `skai/working-docs/`, the current git branch name is used to create a subdirectory path. If the branch name contains `/`, each segment becomes a nested folder.

Inside the branch path, each workflow session must choose a required `session-name` folder. This session folder distinguishes separate efforts on the same branch and contains all primary documents and related artifacts for that effort.

**Path formula:** `skai/working-docs/<branch-path>/<session-name>/<subpath>/<filename>`

Where:
- `<branch-path>` = the current git branch name, with `/` decomposed into nested directories
- `<session-name>` = a short name for this effort on that branch
- `<subpath>` = workflow-specific subfolder (may be empty)
- `<filename>` = the document name (specified by the workflow guide)

Notes:
- The `session-name` is required for workflows that create working docs.
- Use a concise, stable name that helps distinguish different sessions on the same branch.
- Workflow guides may use a more specific term such as `spec-name`, but it still occupies the required `session-name` path segment.

**Examples:**

| Branch | Branch path |
|---|---|
| `work/step-refactor` + `observable-wrapper` | `skai/working-docs/work/step-refactor/observable-wrapper/` |
| `work/foo` + `retro-cleanup` | `skai/working-docs/work/foo/retro-cleanup/` |
| `feature/auth-flow` + `login-tests` | `skai/working-docs/feature/auth-flow/login-tests/` |
| `main` + `ticket-maintenance` | `skai/working-docs/main/ticket-maintenance/` |

## Creating a working document

1. Determine the current git branch:
   ```bash
   git branch --show-current
   ```
2. Choose a `session-name` for this effort.
3. Construct the full path using the formula above (the calling guide specifies `<subpath>` and `<filename>`).
4. Create the directory structure:
   ```bash
   mkdir -p skai/working-docs/<branch-path>/<session-name>/<subpath>
   ```
5. Write the document.

## Examples

- Work spec design:
  - `skai/working-docs/<branch-path>/observable-wrapper/observable-wrapper-design.md`
- Work spec implementation:
  - `skai/working-docs/<branch-path>/observable-wrapper/observable-wrapper-impl.md`
- Unit testing orchestration:
  - `skai/working-docs/<branch-path>/login-tests/testing/unit-testing.md`
- Unit test suite infrastructure:
  - `skai/working-docs/<branch-path>/login-tests/testing/LoginViewModelTests/infrastructure.md`
- Process improvement drafts:
  - `skai/working-docs/<branch-path>/retro-cleanup/process-tickets.md`

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/working-doc-conventions-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Before work, report
`📎 ADDENDUM: <project-entry filename> — loaded` or `No project addendum found: <project-entry filename>.`
Report only the project entry, not each referenced document. Receipt is not a gate; keep GATE lines last.
