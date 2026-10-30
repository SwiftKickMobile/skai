# Changelog

Release notes for people. Each release has a short summary here and one technical document under
[`Releases/`](Releases/), which the installing agent reads when it updates a host
([update-installation guide](Guides/Core/update-installation-guide.md)). A release's section here
is also its GitHub release notes.

## Unreleased

Technical document: [`Releases/unreleased.md`](Releases/unreleased.md).

## Release 16 — 2026-10-29

Technical document: [`Releases/release-16.md`](Releases/release-16.md).

- **Known gaps.** A question nobody in the work can answer yet is carried as a gap with a placeholder: one Gap line on its Discussion item, one footnote form in spec drafts and design change lists naming the item that raised it, one yellow `Gap` annotation per gap on Figma change pages, and a Decision Log closing every Discussion-based artifact. Gaps block promotion into production and move up into a base package.
- **Change requests are packages.** A design or spec change request is an ordinary package whose base is another open package; anyone can file one, whoever picks it up authors it, and promotion folds it into the base.
- **Design packages.** Design Changes is a live typed list that walks the canvas, one entry per frame with sub-changes; a new renderer gives design packages a review page, and a new script checks a Figma page's structure.
- **Writing for people.** A short writing style guide every workflow points at; the guides' own templates and examples now read that way, and say what a requirement, a design spec item and a gap are.
- **Working documents.** They live beside the package they serve and are committed; captured build and test output goes to a scratch root outside the repository.
- **Glossary alternate terms.** An entry can list what other people call the term, so an agent reading Slack or email recognizes it.
- **Review pages.** One versioned stylesheet and script shared by every page; count tiles filter, chips always explain themselves, and the page keeps its state on reload.

## Release 15 — 2026-10-19

Technical document: [`Releases/release-15.md`](Releases/release-15.md).

- **Change requests.** The supervisor rules on a change request and the agent applies the ruling; a request is always against an open package, never the catalog, and carries drafts written from the requester's input. A supervisor's input during authoring is a decision, not a request.
- **House style.** Stable IDs in process artifacts are zero-padded (`D01`, `T01`, `R01`); existing artifacts keep their IDs.
- **Review page.** Discussion items are collapsible cards with their state on the summary line; bare IDs and glossary terms in Discussion, Situations and justifications get chips and popovers; popovers open after a short rest and stay open while you read them; the package card says "discussion complete" instead of claiming promotion readiness.
- **Spec tool.** `check-changes` matches each entry only to things of its own kind, so a glossary term and a same-named index line no longer collide; `render` and `check-changes` can layer another open package's drafts over the catalog with `--base`; `link-terms` no longer nests a link inside a longer term's link.

## Release 14 — 2026-10-18

**Installing agent: before running the adapter runbooks, read `Releases/release-<n>.md` for every release after the one installed on the host, in ascending order, ending with [`Releases/release-14.md`](Releases/release-14.md). The installed release is `lastRelease` in the host's install state; with none recorded, `git tag --list 'v[0-9]*' --merged <lastSHA> --sort=-v:refname | head -1` in the skai checkout gives it.** Hosts on Release 13 or earlier run an update guide that reads this section; the documents under `Releases/` are what it needs.

- **Release documents.** This changelog is now the human notes; the installing agent reads one technical document per release under `Releases/`, and an update reads every release between the host's installed release and its target instead of only the latest.
- **Product specs.** Requirements are renamed product specs: the guides, folders, package type and the two skills (now `skai-product-specs-authoring` and `skai-product-specs-promotion`) carry the new name, and the update offers to rename a project's addenda; a single ID'd item is still a requirement. Product specs and design specs share one file shape (`Guides/Core/spec-file-shape.md`), checked and rendered by `Bin/spec-tool.py`; the content, authoring and promotion guides of both spec types, and the design process guides, follow the 2026-10-18 decisions and are shorter. Migrating a host to this release is reviewed, not just run.
- **Spec consistency.** The guides of both spec types and the design process say each shared mechanic one way; a change item's design justification names the screen, never a design-tool link.
- **Design specs guides refined** after the first prototype package: sharper verification checks, a consistent glossary, and a guide set a fifth shorter.
- **UI Map.** Compose scene packages follow Kotlin naming. The HTML viewer centres rows, wraps lines between route containers, packs filtered views into the visible area, and keeps the selection when the side panel closes.

## Release 13 — 2026-10-14

Technical document: [`Releases/release-13.md`](Releases/release-13.md).

- **Design specs** join the system: four guides and two skills describing how a screen's design presents the requirements.
- **Artifacts live under `skai/`** and are found through the project README; a new `artifact-hosting.md` guide says where a new artifact goes; guides no longer scan for change packages.
- Shorter Project Addendum boilerplate; Figma multiple-sizes chrome fix; design packages keep evidence in their own folder; Configure SKAI user overrides are chosen from a menu.

## Release 12 — 2026-10-13

Technical document: [`Releases/release-12.md`](Releases/release-12.md).

- **New components are offered at update**, never silently skipped; the Configure SKAI window is rewritten in SwiftUI.
- **Design process**: the Figma designer guide is rewritten as platform-agnostic conventions (now `figma-designer-guide.md`, with a multiple-sizes companion), and design authoring and promotion get their own guides and skills.
- New addendum report lines; the UI Map renderer reports visual-home loops instead of dropping scenes.

## Release 11 — 2026-10-10

Technical document: [`Releases/release-11.md`](Releases/release-11.md).

- **Configure SKAI**: the `skai-configure` skill and a bundled Mac app choose which components a project installs; installation is configuration-driven, with per-adapter component history and update recovery.
- Project guide addenda; requirements and UI Map change packages are independent per type; the UI Map planning compatibility router is retired; SKAI logo and app icon.

## Release 10 — 2026-10-07

Technical document: [`Releases/release-10.md`](Releases/release-10.md).

- The interactive **HTML UI Map render** is the primary render artifact, replacing the SVG.
- A first Figma designer guide.

## Release 9 — 2026-10-05

Technical document: [`Releases/release-9.md`](Releases/release-9.md).

- UI Map renderer: left-to-right ELK layout; a scene referenced twice by one parent draws twice.

## Release 8 — 2026-10-05

Technical document: [`Releases/release-8.md`](Releases/release-8.md).

- **Requirements**: product contracts versus screen structure, known implementation differences, reference-style links.
- **Installation**: manifest-driven skills, shared instruction composition, root Codex `AGENTS.md`, Cursor frontmatter fix; maintainers must leave migration instructions for existing host artifacts.

## Release 7 — 2026-09-30

Technical document: [`Releases/release-7.md`](Releases/release-7.md).

- "Human" becomes "supervisor" everywhere; agent instruction files are managed blocks; one install prompt for all adapters.
- Requirements baseline guide; maintainer runbooks move to `internal/`, findings logs to `skai/refinement-reviews/`.

## Release 6 — 2026-09-04

Technical document: [`Releases/release-6.md`](Releases/release-6.md).

- Work-spec creation is API-first design; work-spec implementation owns planning and continuous execution.

## Release 5 — 2026-08-30

Technical document: [`Releases/release-5.md`](Releases/release-5.md).

- **Requirements system** added: catalog conventions, authoring and promotion skills, change packages; the dev retro seeds a requirements package.

## Release 4 — 2026-08-29

Technical document: [`Releases/release-4.md`](Releases/release-4.md).

- New `skai-process-refinement` skill; `skai-suggestion` reworded as a suggestion box; two process guides renamed.

## Release 3 — 2026-08-29

Technical document: [`Releases/release-3.md`](Releases/release-3.md).

- Refinement gains round scoring; cold reviews state consequence and reachability facts; findings logs are committed under `skai/refinement-reviews/`.

## Release 2 — 2026-08-28

Technical document: [`Releases/release-2.md`](Releases/release-2.md).

- Cold-review template gains scoped and empirical review slots; refinement triage and size budgets sharpened. No migration.

## Release 1 — 2026-08-12

Technical document: [`Releases/release-1.md`](Releases/release-1.md).

- Checkbox progress markers; project-owned artifacts move to `skai/`; UI Map split into architecture and implementation; installation updates target numbered releases; cold review hardening; integration commands preserve exit status.

## Release 0 — before release numbering

Technical document: [`Releases/release-0.md`](Releases/release-0.md).

- History from 2026-02-13 to 2026-05-24: the IDE-neutral restructuring and rename to SKAI, gated process flow, the UI Map system, the Codex adapter, install state and the update skill.
