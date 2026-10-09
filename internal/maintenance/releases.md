# Release maintenance

This is a maintainer reference, read only when the routing table in [`../maintain-skai.md`](../maintain-skai.md) applies. It is not an installed asset or a runtime dependency of host workflows.

## Release planning

Releases are cut only when the supervisor asks. A request to cut a release authorizes the agent to prepare and create the release commit and its `v<N>` tag using normal git release mechanisms; pushing still requires a separate request. `CHANGELOG.md` mirrors this: a `## Unreleased` staging section at the top, frozen `## Release <N>` sections below it (newest first), and a legacy `## Released` bucket at the bottom for entries that predate release numbering.

**Default:** new changelog entries go under `## Unreleased`, which is a staging log (see the [entry guide's CHANGELOG rules](../maintain-skai.md#required-bookkeeping-most-common-misses)) — left to accumulate, not consolidated as you go.

**Cutting release `<N>`** (only when the supervisor asks):

1. **Consolidate** the whole `## Unreleased` stack into clean notes for the installing agent — merge related entries, drop superseded intermediate steps, group by theme. Cross-check `git log` since the previous release so nothing host-affecting is missed.
2. **Convert** the `## Unreleased` heading to `## Release <N> — <YYYY-MM-DD>`; those bullets are now frozen.
3. **Open** a fresh empty `## Unreleased` at the top.
4. **Verify and cut** the release: stage the complete release scope, create the release commit, and tag that commit `v<N>`. Do not push unless the supervisor also asks.

The tag is the anchor the update workflow targets by default; the `## Release <N>` heading and the `v<N>` tag name the same release.
