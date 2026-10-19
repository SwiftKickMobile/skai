# Release 8 — 2026-10-05

**Requirements**

- **Product contracts and authoring scope.** Clearer examples distinguish product guarantees from incidental screen structure, encourage reuse of existing contracts when backfilling bugs, and explain how to record adjacent findings within authorized scope. These clarifications govern new or changed prose; do not rewrite existing contracts or IDs during upgrade.
- **Known implementation differences.** Drafts and canonical requirements support `> **Known difference — <app/platform>:** <confirmed current behavior and gap>` with a tracking link when available; approved contracts may promote with these notes while fixes remain pending. Work-spec implementation updates or removes only verified notes and their unused link definitions, preserving outstanding platform differences and requirement text/IDs; do not infer notes from suspected bugs during upgrade.
- **Links and Discussion direction.** Stored requirements documents use reference-style links with definitions at the bottom; conversation uses inline links to the exact draft or canonical item. Discussion links to affected drafts, replacing draft `(D#)` back-citations; promotion C6 prepares canonical destination links and C7 remains the terminal write/completion identity.

**Installation**

- **Manifest-driven skills.** All three adapters install every `skill` asset tagged for them, using its `sourcePath`, including previously omitted requirements skills. Obsolete managed SKAI skills are proposed for cleanup during discovery, never removed without approval.
- **Shared instruction composition and root Codex file.** Claude Code and Codex retain Release 7's dated managed blocks and existing template IDs, composing them from new `Templates/agents/instructions-block.md` (`template.agent-instructions-block`) and applicable policies through new `Install/agent-instructions-install-update.md` (`install-policy.agent-instructions-install-update`). Codex now installs root `AGENTS.md` instead of `.agents/AGENTS.md`; the single install entry prompt and Release 7 ownership rules remain unchanged.
- **Cursor frontmatter.** Generated `.mdc` rules place frontmatter before their managed marker comment.

**UI Map and change packages**

- **Canonical scene placement.** When a reused scene's `primary_parent` reaches it through multiple route kinds, the renderer places its canonical instance in the container where the map defines it. A scene defined under `child` and referenced under `modal` on the same parent now renders canonically under `child`; the guide includes a worked example.
- **Packages follow canonical artifacts.** Requirements and UI Map guides, artifact references, and retro package seeding resolve `skai/changes/` in the catalog or map repository, including shared submodules. App Integration documents and app-code paths remain in the app repository.

**Maintenance**

- **Migration completeness.** The maintainer guidance and `internal/maintain-retro.md` (`guide.maintain-retro`) require actionable migration instructions for existing host artifacts. Refresh the SKAI checkout to use the revised retro; this maintenance change requires no host artifact transformation.

**Upgrade instructions**

1. **Re-run every installed adapter.** Refresh the SKAI checkout and installed assets to pick up the manifest-driven skills, instruction composition, Cursor frontmatter, and revised guides.
2. **Migrate Codex instructions.** Preserve custom content from `.agents/AGENTS.md` in root `AGENTS.md` before separately approving cleanup of the old file. Preserve project-owned content outside dated managed blocks.
3. **Confirm artifact locations.** Name the catalog and map repositories in project documentation, including shared roots; resolve their change packages there while retaining app Integration and app-code paths in the app repository.
4. **Migrate requirements presentation.** Apply the following steps to existing catalogs and open packages through the existing upgrade plan.

- **Discover and plan.** Resolve catalog repositories from host Integration requirements blocks, including shared repos, and inventory canonical catalogs plus open `skai/changes/*/` requirements packages there; a package with promotion C7 checked is historical. Include the presentation-only changes below in the existing upgrade plan and obtain approval covering these project-owned artifacts; they are not managed-file overwrites, and multiple adapters must not repeat an already-completed sweep.
- **Transfer associations first.** For each open draft `(D#)` citation, resolve the package's Discussion item and add a reference-style link there to every affected draft requirement before removing the back-citation. Preserve item IDs, decisions, checkbox state, and requirement dependencies; when the item or target is ambiguous/missing, report it and leave that unresolved association intact.
- **Convert and resolve links.** In canonical catalogs and open requirements documents (drafts, authoring, promotion and change requests), convert citations and document links to reference-style links with definitions at the bottom, preserving visible IDs and requirement prose. Resolve a package citation to its draft when present, otherwise to the canonical file; use actual heading anchors, including retired headings, and supported explicit Discussion anchors or topic anchors plus item context—never assume checkbox IDs create anchors.
- **Reconcile paths and current changes.** Rebase definitions for each document's actual location; on promotion, draft targets map to canonical destinations and untouched dependencies remain canonical. Compare prose and resolved target identities when reconciling open Requirement Changes: location-only rebasing is not a requirement change, but added/removed citations and changed targets must be accounted for without renumbering existing R# items or discarding rationale.
- **Preserve history.** Do not rewrite promoted packages merely for style, or alter approval/completion state or recorded verification evidence. In open promotion artifacts, retain prior C6 labels/results as history and identify the next run as using the new C6 link-preparation meaning; normal promotion rerun rules reset current checks when resumed, never reinterpret an old scaffolding result as fresh link verification.
- **Verify the migration.** Check every converted definition and citation against the intended file/item from its new location, including shared roots and partial packages, and confirm each removed back-citation has its forward association. Compare pre/post requirement prose and IDs, decisions, check states and evidence; report unresolved targets rather than guessing, keep pending authoring/promotion gates intact, and do not run promotion as part of migration.
