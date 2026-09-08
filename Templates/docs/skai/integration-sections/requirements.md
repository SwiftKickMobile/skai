## Requirements

Records where this project's requirements catalog lives. See
`Submodules/skai/Guides/Requirements/requirements-catalog.md` for what each shape and scope means.

- 🟡 **Repository shape**: {operator response}
  - INSTRUCTION: One of `local`, `shared`, or `none`.
    - `local` — the catalog is or will be in this repo. A project intending to keep requirements
      here is `local` even before the folder exists.
    - `shared` — the catalog is in another repo, typically a submodule. This repo has none of its
      own.
    - `none` — this project has deliberately opted out of keeping requirements. Requirements
      workflows skip entirely. Choose it only as a decision, never as a default for a project that
      simply has not started yet.

- 🟡 **Requirements root**: {operator response}
  - INSTRUCTION: Path to the catalog root. For `local`, a path inside this repo, normally
    `skai/requirements/`. For `shared`, the path to the other repo's catalog, e.g.
    `Submodules/shared-requirements/requirements/`. Set to `n/a` for `none`.
