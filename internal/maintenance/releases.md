# Release maintenance

This is a maintainer reference, read only when the routing table in [`../maintain-skai.md`](../maintain-skai.md) applies. It is not an installed asset or a runtime dependency of host workflows.

## Two documents, two audiences

- `CHANGELOG.md` is release notes for people: per release, a short themed summary and one link to that release's technical document. A release's section is also its GitHub release notes.
- `Releases/release-<N>.md` is the technical document the installing agent reads (see the [entry guide's bookkeeping rules](../maintain-skai.md#required-bookkeeping-most-common-misses) for what it must contain). `Releases/unreleased.md` stages the next release's document; `Releases/release-0.md` holds the entries that predate release numbering. The documents are read from the SKAI checkout and are not manifest assets.

**Default:** new entries go to `Releases/unreleased.md` (dated, a staging log left to accumulate, not consolidated as you go) and to the `## Unreleased` section of `CHANGELOG.md` (one human line per change). Every host-affecting change writes both; internal-only changes write neither.

## Cutting release `<N>`

Releases are cut only when the supervisor asks. A request to cut a release authorizes the agent to prepare and create the release commit and its `v<N>` tag using normal git release mechanisms; pushing still requires a separate request.

1. **Consolidate** `Releases/unreleased.md` into clean instructions for the installing agent — merge related entries, drop superseded intermediate steps, group by theme, keep every migration step safe to re-run. Cross-check `git log` since the previous release so nothing host-affecting is missed.
2. **Rename** `Releases/unreleased.md` to `Releases/release-<N>.md` with the title `# Release <N> — <YYYY-MM-DD>`; its contents are now frozen (fix an outright error, never rewrite shipped scope). Open a fresh `Releases/unreleased.md` holding only the title `# Unreleased`.
3. **Write the human notes**: in `CHANGELOG.md`, convert `## Unreleased` to `## Release <N> — <YYYY-MM-DD>`, rewrite its lines as a short themed summary that agrees with the technical document, and keep its single link, now to `Releases/release-<N>.md`. Open a fresh empty `## Unreleased` at the top with a link to `Releases/unreleased.md`. For Release 14 only, the section's opening bold line (the instruction to hosts whose update guide still reads this changelog) is retargeted to `Releases/release-14.md` and kept.
4. **Verify and cut**: both documents exist and agree; stage the complete release scope, create the release commit, and tag that commit `v<N>`. Do not push unless the supervisor also asks.

The tag is the anchor the update workflow targets by default; the `## Release <N>` heading, the `v<N>` tag and `release-<N>.md` name the same release. The update workflow reads every `release-<n>.md` after the host's installed release in ascending order, so a release document must stand on its own and must not assume the host applied the previous unreleased staging.
