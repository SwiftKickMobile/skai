Managed-By: skai
Managed-Id: guide.artifact-hosting
Managed-Source: Guides/Core/artifact-hosting.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Artifact Hosting

Print `- 📖 SKAI guide: artifact-hosting` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read this when the artifact does not exist yet. That is the one time the README does not link it yet,
so its absence is expected, not a blocked gate; a reopened package already settled this when it was
created.

The supervisor says which repository the artifact goes in; never infer it. Its fixed
root under `skai/` is named by its content guide. When the package is created, add the README link
pointing at that final location; it resolves when promotion writes the artifact.

## Project Addendum

If `<active-project-root>/skai/addenda/artifact-hosting-addendum.md` exists, read it and immediately print
`- 📎 Addendum loaded` as a line of its own, nested under this guide's line; its rules are part of this
guide and win any conflict.
