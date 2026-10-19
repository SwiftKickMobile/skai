Managed-By: skai
Managed-Id: guide.artifact-hosting
Managed-Source: Guides/Core/artifact-hosting.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Artifact Hosting

Print `📖 SKAI guide: artifact-hosting` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read this when the artifact does not exist yet. That is the one time the README does not link it yet,
so its absence is expected, not a blocked gate; a reopened package already settled this when it was
created.

The supervisor says which repository the artifact goes in; never infer it. Its fixed
root under `skai/` is named by its content guide. When the package is created, add the README link
pointing at that final location; it resolves when promotion writes the artifact.

## The Link Entry

An entry is the artifact's name, its link and a description. Use the README's own format for linked
resources when it has one. When it has none, a table:

| Resource | Description | Path |
| --- | --- | --- |
| Product specs | What LumenNotes must do when a note is captured, organized or shared, by domain | [`skai/product-specs/_product-specs.md`](skai/product-specs/_product-specs.md) |

Add a repository column only when the path does not make the repository obvious; the agent follows
the link and learns nothing from the column.

## The Description

The description is what tells an agent whether to open the artifact. A reader who has not opened it
must be able to tell from the description alone whether their current question is answered there.
So say what questions it answers, not what it contains; name the scope, so the reader also knows
what is not in it; do not restate the name, the format or how it was made; one sentence.

## Two READMEs

Link the artifact from the README the agent reads. When the artifact's repository is a different
one, link it from that repository's README as well, with the same entry and the path relative to
that README. That README may be read without the host project, so the description cannot lean on it.

## Project Addendum

If `<active-project-root>/skai/addenda/artifact-hosting-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
