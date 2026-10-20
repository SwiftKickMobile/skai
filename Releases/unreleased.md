# Unreleased

**Known gaps (skai#82)**

- 2026-10-20 **New reference guide `Guides/Core/known-gaps.md`** (`guide.known-gaps`, core, no skill wrapper): how an agent works with a gap — a question that must be decided before the work ships, carried as a placeholder. Workflow guides send the agent to it with one inlined sentence; that propagation ships in a later release. **Migration:** none; nothing points at it yet.
- 2026-10-20 **Discussion schema house style gains gaps and the Decision Log** (`Guides/Core/process-flow.md` § Structured discussion items, mirrored in the gated-workflow template): a `- **Gap** <placeholder>` sub-bullet on an open item; open gap items do not count toward the blocked gate and block promotion; every Discussion-based artifact ends with `## Decision Log` (`- <ID> decided|gap|reopened — <one line>`, append-only, no dates); at most one Decision line per item. Workflow guides inline the schema, so no installed guide changes until the propagation release. **Migration:** none now; the propagation release says what to add to existing artifacts.
