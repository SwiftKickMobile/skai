Managed-By: skai
Managed-Id: guide.artifact-hosting
Managed-Source: Guides/Core/artifact-hosting.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# Artifact Hosting

Before using this guide, complete [Project addendum](#project-addendum) loading below.

Read this when the artifact does not exist yet. That is the one time the README does not link it yet,
so its absence is expected, not a blocked gate; a reopened package already settled this when it was
created.

The supervisor says which repository the artifact goes in; never infer it. Its fixed
root under `skai/` is named by its content guide. When the package is created, add the README link
pointing at that final location; it resolves when promotion writes the artifact.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/artifact-hosting-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: artifact-hosting`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
