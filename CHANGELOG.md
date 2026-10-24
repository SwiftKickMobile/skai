# Changelog

Release notes for people. Each release has a short summary here and one technical document under
[`Releases/`](Releases/), which the installing agent reads when it updates a host
([update-installation guide](Guides/Core/update-installation-guide.md)). A release's section here
is also its GitHub release notes.

## Unreleased

Technical document: [`Releases/unreleased.md`](Releases/unreleased.md).

- **Writing style guide.** One short guide says how an agent writes anything a person reads: sentences that stand alone without their IDs, reasons in words, the thing named rather than the sample that shows it, everyday words instead of the guides' own vocabulary, first person. Every workflow guide points at it.
- **Design change descriptions say what changed.** A change entry names the state or behavior that changed and gives its reason in a sentence; gap footnotes sit only on the entry whose change rests on the placeholder.
- **A footnote names the item that raised the question.** Never one that merely inherits it; change request pages now link footnote owners and count gaps like package pages.
- **Design change requests.** A design package now authors against a base, and a change request is simply a package whose base is another open design package: same artifact, same phases, same page; promotion folds it into the base. Anyone can file one, with or without drawings.
- **Design Changes is a live typed list.** One entry per change with a description and a justification, kept current while drawing; "approved" is gone, the review gate's "next" is the approval, and completion reconciles the designs against their inputs.
- **Design packages get a review page.** A new renderer writes `design-review.html` beside the design artifact, sharing the spec pages' look; cards and the top bar sit on a 5 grid.
- **One gap footnote for every artifact.** Spec drafts and design change lists mark a placeholder the same way, numbered by first use, naming the item that owns the question instead of repeating it; on the page the notes are one line each, with the question a hover away.
- **Inherited gaps are footnotes, not discussion items.** A design that builds on a spec's placeholder marks the entry that stands on it and names the owner, instead of re-raising the question; the Figma annotation now says what it is: Gap, Placeholder, Owner.
- **The design change list walks like the canvas.** Headings per screen in canvas order, one entry per frame, several changes to one frame as numbered sub-changes; change pages keep one section per screen, and a new script checks a page's structure against the guide.
- **State filters partition the discussion.** The review page's tiles are open, gaps and resolved, each its own set; "open" no longer includes gaps.
- **Glossary alternate terms.** A glossary entry can list what other people call the term ("Also called: bid (Salesforce)"), so an agent reading Slack, email or wiki pages recognizes it; the specs still use only the entry's term, and the spec tool checks and shows the note.
- **Review pages share one stylesheet, versioned.** The page's styles and script now live in the skai checkout, like the UI Map viewer's, so a style fix reaches every page; a change that would break old pages becomes a new version and old pages keep theirs.
- **Gaps count and filter.** The review page counts gaps in its header and its count tiles filter the page, several at once; the separate Gaps list is gone.
- **Quieter term links.** Glossary terms on the review page are body-colored with a thin dashed underline.
- **Fix.** Open gap items on the review page no longer shrink to the footnote's type size.
- **Decision Log off the page.** The review page no longer shows the Decision Log; it stays in the artifact.
- **Verification at the end.** The authoring artifact's Verification section now comes after the content sections, just before the Decision Log.
- **Known gaps, wording.** A gap that has no placeholder yet now says "no placeholder; waiting on …" instead of "none; waiting on …".
- **Known gaps, part four.** On a Figma change page, each open design gap is marked with an annotation on the drawn placeholder, removed when the gap closes; promotion refuses drafts that still carry one.
- **Working documents.** Working documents now live beside what they serve — a change package's notes in that package's `working-docs/` folder, archived with it at promotion, everything else in a session folder with no branch level — and they are committed. Output captured to verify a build or test goes to a scratch folder outside the repository (`/tmp/skai/` by default, set in `skai/integration.md`), and documents record only the command, the result and where the output was. The update asks before moving existing working documents.
- **Known gaps, part three.** A placeholder in a spec draft is marked with a footnote that names its Discussion item; the tool checks the footnotes against the items, refuses any footnote in canon, and lists the gaps on the review page.
- **Known gaps, part two.** Every Discussion-based guide now carries the Gap line, the Decision Log and the pointer to the gaps guide; promotion refuses a package with an open gap; the spec tool checks the log and shows gaps on the review page. Existing packages get a seeded Decision Log at update.
- **Known gaps, part one.** A new reference guide says how to carry a question that must be decided before shipping as a placeholder, and the Discussion schema gains a Gap line and a per-artifact Decision Log. Nothing changes in installed workflows until the guides adopt it in a later release.

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
