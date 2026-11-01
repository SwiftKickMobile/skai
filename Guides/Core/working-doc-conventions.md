Managed-By: skai
Managed-Id: guide.working-doc-conventions
Managed-Source: Guides/Core/working-doc-conventions.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-31

# Working Document Conventions

Print `📖 SKAI guide: working-doc-conventions` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Working documents (planning docs, work specs, source notes, reviews, test work docs) track in-progress work and live beside the artifact they serve. A package's working documents are committed with it; session documents are not.

## Location

- **A document serving a change package** goes in that package's `working-docs/` folder: `skai/changes/<change-id>/<type>/working-docs/`, in the package's canonical repository. Promotion archives it with the package. A document serves a package when it exists because of that package: its source notes, reviews, audits, scripts. Notes serving two packages go with the upstream one and are linked from the other; related packages can live in different repositories, so they have no shared folder.
- **A document serving no package** goes in a session folder under `skai/working-docs/`, which the project's `.gitignore` excludes. A work spec serves a change, not a package, so it is a session document.

**Path formula (no package):** `skai/working-docs/<session-name>/<subpath>/<filename>`

Where:
- `<session-name>` = a short, stable name for this effort; the folder holds all its documents
- `<subpath>` = workflow-specific subfolder (may be empty)
- `<filename>` = the document name (specified by the workflow guide)

Notes:
- The `session-name` is required for workflows that create working docs.
- Choose a name no other effort uses; returning to the same effort reuses its folder.
- Workflow guides may use a more specific term such as `spec-name`, but it still occupies the required `session-name` path segment.

## Build And Test Output

Output captured to verify a build or test never goes in a working document or anywhere in the repository: command captures, result bundles, extracted results and screenshots go under the scratch root `skai/integration.md` names, by default `/tmp/skai/<session-name>/` (the change ID for package work). The document's evidence line names the command, the result and the scratch path. The evidence line is the record: the output can be reproduced by rerunning the command and need not survive. A deliverable a build produces on purpose (a tool shipped from the repository) is not captured output; it goes where its own guide says.

## Creating a working document

1. Decide whether the document serves a change package (see [Location](#location)); if it does, use that package's `working-docs/` folder.
2. Otherwise choose a `session-name` for this effort and construct the path from the formula (the calling guide specifies `<subpath>` and `<filename>`).
3. Create the folder chosen in step 1 or 2: the package's `working-docs/` folder, or
   ```bash
   mkdir -p skai/working-docs/<session-name>/<subpath>
   ```
4. Write the document.

## Examples

| Document | Path |
|---|---|
| Source notes for the `reminder-expiry` product specs package | `skai/changes/reminder-expiry/product-specs/working-docs/source-notes.md` |
| Work spec design | `skai/working-docs/observable-wrapper/observable-wrapper-design.md` |
| Work spec implementation | `skai/working-docs/observable-wrapper/observable-wrapper-impl.md` |
| Unit testing orchestration | `skai/working-docs/login-tests/testing/unit-testing.md` |
| Unit test suite infrastructure | `skai/working-docs/login-tests/testing/LoginViewModelTests/infrastructure.md` |
| Process improvement drafts | `skai/working-docs/retro-cleanup/process-tickets.md` |
| Test output for `login-tests` | `/tmp/skai/login-tests/unit-tests.txt` (scratch, outside the repository) |

## Project Addendum

If `<active-project-root>/skai/addenda/working-doc-conventions-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
