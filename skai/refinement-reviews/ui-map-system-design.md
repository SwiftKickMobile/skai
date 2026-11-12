# UI Map System Design

## Purpose

This document defines SKAI's UI Map system: a YAML map of every scene in an app and the routes
between them, the tool that validates and renders it, the architecture workflow that proposes
changes to it in a change package, the implementation workflow that conforms code to it and
promotes it, and the platform references that say how a map becomes SwiftUI or Jetpack Compose
code. It is the standard used to write and cold-review the runtime guides, not a guide an
executing agent reads.

**Provenance.** Backfilled 2026-10-19 from the ten guides under `Guides/UIMap/`, the renderer,
schema and viewer under `Bin/`, and the refinement records consolidated in
[`ui-map-system-findings.md`](ui-map-system-findings.md). The original spec,
`docs/ui-map-skill-plan.md` (May 2026), was never committed and is lost; the May findings quote
its sections, and those quotes are used here. A principle inferred from guide text rather than recorded says so.

### Scope

- **Architecture** produces map artifacts only: proposed map, render, decisions, typed map change
  items. No app-code tasks, file moves, build steps or sequencing.
- **Implementation** conforms code to the target map and promotes the proposed map. **Plan**
  writes the conformance spec and promotes, leaving UI-map-owned work `planned` for a larger
  effort that owns the same structural work; **Build** scaffolds, moves, renames, builds green,
  then promotes.
- **Out of scope** (inferred from the guides' boundaries): feature content; click-through QA;
  design — the map is a technical document downstream of design specs; a central router.

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), Guide house style;
  [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) for gates, advance intent,
  `auto` and markers.
- The ten guides under `Guides/UIMap/`; `Bin/ui-map-render.py` (its docstring's *RENDER
  CONVENTIONS* is the canonical render spec), `Bin/ui-map.schema.json`, `Bin/ui-map-viewer.v1.js` (versioned: a breaking change is a new file, old versions stay).
- [`product-specs-system-design.md`](product-specs-system-design.md) § Decisions — 2026-10-19,
  adopted in P8.

This document is authoritative for UI Map behavior. Because it is reconstructed from the guides,
a conflict between the two is first a question about the reconstruction; the findings log
records which side the supervisor ruled stale.

## Complexity baseline

No size budget is declared. On 2026-10-19 the ten guides total 176,025 bytes (`wc -c`); the
implementation guide is 50,025 and the architecture guide 34,964.

## Design invariants

### P1. Portable core, thin host adapters

The map format, schema, renderer and viewer, the authoring conventions, the platform references
and the artifact formats are host-independent and may be lifted out of SKAI into another host. A
SKAI skill owns only session choreography: gates, advance intent, `auto`, markers. Reason
(supervisor, May 2026): the mapping process is expected to be used outside SKAI.

### P2. The map leads, code follows

The official map is the architecture authority; code conforms to it. Implementation may scaffold,
align, move, rename, hand off, block or raise a change request; it never edits map content to
justify code. In the May design the audit's Discussion was the one sanctioned moment the map
could be revised; since the June 2026 split every map revision goes through architecture's
package.

### P3. One official map, frozen while a proposal is reviewed

`skai/ui-map/ui-map.yaml` lives in the repository the supervisor names and is written only by implementation's terminal promote: copy the proposed YAML over it,
re-render the official page **from the official YAML**, archive the package to `skai/promoted/`.
Architecture edits only the proposed map. `## Map Changes` is exactly the diff between the two:
recomputable, reconciled on reopen, never regenerated; the `M#` ids and justifications are what a
raw diff cannot reconstruct. Reason (inferred from the split): the May model edited the map in
place, so a proposal could not be reviewed, reopened or abandoned without disturbing the
authority.

### P4. Code mirrors the map's domains

Each domain is a top-level folder or package; a scene's folder sits where the map *defines* it,
under its domain, nested by the route containers it sits in. Every other appearance is a
reference: cross-domain references, repeats and `primary_parent` never create or move a folder.
Scene ids map to code identities by platform convention. Reason (supervisor, May 2026): this is what domains are for; a clause
letting commonly accessed scenes move higher as a convenience let an agent misplace a scene in a
cold run and was removed for good.

### P5. Validate and render is how a map is checked

The schema catches structure; the renderer catches semantics, and an invalid map is never
presented. The render is the review surface at every gate, the interactive HTML page since
2026-10-07. Rendering validates the target; it never authorizes editing it. What the renderer
cannot see, the authoring conventions, is architecture's structural self-check before each gate.

### P6. Structure, not features

Placeholders are skeleton plus navigation: compiling, routing correctly, visibly identifiable,
tinted by domain. A new scene models no inputs. Every scaffold site carries `🟡 UI Map scaffold <change-id>`; implementation
never removes them, and no markers left means fully productionized. A scaffold that seems to need
feature content is over-built: stop. A missing code mapping blocks before Code Changes; it is
never hand-rolled and never a `handoff`.

### P7. Discussion earns its items; the preview is the review surface

A `D#` item is raised only when a choice is both unforced (nothing in the design, a convention or
ownership settles it) and material (it changes a route container, nesting or a domain).
Everything else is encoded and reviewed in the render, in plain language rather than schema
fields or rule names. `D#`, `M#`, `T#` ids are stable and never renumbered; resolution is `- [x]`
plus a `Decision` line with the Kind kept; sibling items are tight, because a loose list wraps the
checkbox.

### P8. Audits record deviations; change requests flow one way and the supervisor rules

The audit is exhaustive within the reach `## Map Changes` sets and records deviations only. Each
source (`M#`, `D#`, or an id-less finding) yields exactly one `T#`. Mechanical work is
`implement` / `placeholder` in Build and `planned` in Plan; non-mechanical work owned elsewhere is
`handoff`, which blocks a Build; a map change is the heaviest stop. Only implementation raises a
change request, after an approved `D#`, against the package it is working; architecture consumes
it on reopen of the same artifact in the same kind. Per the 2026-10-19 decision adopted from
product specs: the supervisor reads the request and says what to do; the agent applies that and
re-renders, leaves a `Proposed` request alone until told, never rejects or supersedes on its own,
and raises no Discussion item to drive the ruling.

### P9. Platform references own the code mapping; projects override in the open

Routing is local to each scene; there is no central router. Standard `modal_style` values map to native
presentation; non-standard styles are declared in the map and documented in the project README or
addendum, never inferred. The placeholder rule is a decision procedure (SwiftUI: one
`NavigationStack` per root-to-leaf path at the presentation boundary; Compose: each navigating
scene owns its hosts), so a composition the examples do not draw is derived, not gated.

## Artifacts

```text
<map repo>/skai/ui-map/ui-map.yaml · .html   official map and render; written only by the terminal promote

skai/changes/<change-id>/ui-map/
  ui-map-architecture.md     Goal · Inputs · Mode · Provisional preview · Discussion (D#) ·
                             Map Changes (M#, typed, no checkbox) · Deferrals · Assumptions and TODOs · Out of scope
  proposed-ui-map.yaml · .html   the proposal and its render
  ui-map-implementation.md   Goal · Inputs · Mode (Plan|Build) · Audit · Discussion (D#) ·
                             Code Changes (- [ ] T# with Disposition, ending in the terminal promote) ·
                             Change Requests · Evidence
  change-requests/ui-map-<nnn>.md   Change Request Status · Reviewer Response · the request
  evidence/                  persisted build and render output

skai/promoted/<change-id>/ui-map/   the whole package after promotion, pending Plan work included
skai/working-docs/<branch>/<session>/ui-map-implementation.md   a conformance run with no proposal
```

Formats: the two artifacts guides, `ui-map-guide.md` and the schema.

## Workflow

1. **Initiate** architecture on an explicit signal; infer Baseline map or Scoped map change.
   New input, a change request included, reopens the same artifact.
2. **Discussion**: seed the proposed map from the official one (or empty) when none exists,
   maintain it and its render, self-check, render before every gate or state the concrete
   reason. Blocked while any `- [ ]` remains; planned gate *Discussion complete*.
3. **Map Changes**: diff official against proposed into `M#` items, write Deferrals and Assumptions, render,
   complete directly with `🏁 Complete.`
4. **Audit** (implementation) the codebase against the target map within the reach Map Changes
   sets; a stale change list returns to architecture.
5. **Discussion** only for genuine decisions; an approved change request blocks at once. Then
   the **Code Changes ready** gate: the supervisor reviews the `T#` spec and the terminal promote.
6. **Implement**: Build works `implement` / `placeholder` items top-down with builds at chunk
   boundaries; Plan goes straight to promotion.
7. **Promote and archive**: compare again, copy YAML, render official from official, archive,
   repair links, re-render the preview, check the terminal item. A restart resumes from recorded
   progress and never repeats a verified write.

## Acceptance checks for the guides

A cold reviewer should verify:

1. Architecture produces map artifacts only; implementation never edits map content; the only
   path back is a change request handled per P8.
2. The official map is written only by the terminal promote; the official page is rendered from
   the official YAML, never copied.
3. Map Changes is a recomputable diff with stable `M#` ids; Code Changes has one `T#` per source
   with a disposition that never changes on check.
4. Every gate shows a render or the concrete reason there is none.
5. Folders mirror canonical definition nesting; references and `primary_parent` never move a
   folder; no convenience clause exists.
6. Placeholders carry no feature content, no inputs, and change-id markers; missing mappings
   block before Code Changes and never become handoffs.
7. Discussion items meet the unforced-and-material bar, carry a recommendation, read in plain
   language, and keep ids, Kind and tight lists.
8. Audit records deviations only; route kind is read from the bound modifier; every check
   records a result.
9. Platform references map every route kind and standard modal style and state the placeholder
   rule as a decision procedure.
10. A fresh agent can run either workflow from the artifacts, the guides and
    `skai/integration.md`.

## Decisions — 2026-05 (planning refinement)

From the pass of 2026-05-19 to 2026-05-23 against the May guide `ui-map-planning.md` and the
lost spec; dispositions in the findings log.

- **Findings are approved individually** under `Map fixes` / `Code conformance` / `Defers`; the
  05-19 single-marker decision was reversed on 05-20 when a 16-finding audit could not be read at a glance. Grouping by
  resolution direction and per-instance enumeration were codified after four cold runs reached
  for them regardless: count for uniform, bucket for divergent (05-23).
- **Defer is a resolution direction**, tracked by a map TODO and a Deferrals section, living in
  Discussion only; Out of scope holds boundaries, not deferrals.
- **Conformance deviations are Phase-1 findings** (model A, 05-23), approved per finding; the
  resulting entries are mechanical and not re-debated.
- **Project convention** joins the Source taxonomy; the README is the authority for overrides;
  project-specific modal rows left the SwiftUI reference.
- **Gates**: Blocked while items remain, Planned when none; user-facing lines use section names;
  no Phase-2 advancing gate. "`auto` never auto-decides
  architecture" is enforced implicitly, not restated (#9, logged).
- **Format**: `- [x]` with a `Decision` line, Kind retained; letter-led ids; bold labels with no
  separator; tight lists, the root cause of checkbox wrapping and below the spec's design level.
- **Sharpen before adding**: the bound-modifier example (F8) rather than a new detection rule.

## Decisions — 2026-06-03 to 2026-10-14 (release documents)

- 2026-06-03 **Architecture and implementation split**: frozen official map, proposed map in a
  change package, implementation owning code changes, change requests and terminal promotion.
- 2026-08-11 Stable `M#`/`T#` ownership and `implement | placeholder | planned | handoff`;
  `modal_style` required on every modal destination, validated and used; Build evidence
  append-only.
- 2026-10-05 Left-to-right ELK layout; a scene referenced twice by one parent draws twice.
  2026-10-07 The HTML page is the render artifact. 2026-10-10 Packages independent per type.
  2026-10-13 Visual-home loops are an error; no package discovery; a first map is hosted
  through the README.

## Decisions — 2026-09-02 (Compose library)

Three cold rounds on the Compose placeholder and routing library (`Dev/Compose`, branch
`work/uimap-cmp`): SKAI-selected dependencies with KMP `commonMain` placement; Hilt Android-only;
a canonical modal table (`ModalNavHost`, `bottomSheet`, `bottomSheetFullScreenModal`, `dialog`);
`PlaceholderColors.domain(index)` for all nine renderer slots; root scenes full-bleed; state, event and effect files only for scenes with
state responsibility; every scaffold begins with the change-id marker; **a tab-plus-composite
placeholder is unsupported by the renderer's shape and blocks in Discussion** (owner ruling). None of this reached `main`: see Open.

## Decisions — 2026-10-18 (Compose naming and viewer)

Compose scene packages are the map id with underscores removed under a `scenes/` root. The viewer
centres rows, wraps lines between route containers and never inside one, places a filtered view
by visible cell *area*, keeps the selection when the side panel closes, and dismisses the panel by
revealing rather than re-placing.

## Decisions — 2026-10-19 (change request triage)

UI Map architecture adopts decision 1 of `product-specs-system-design.md` § Decisions —
2026-10-19 (P8). Decision 2 is not needed: its requests come only from implementation, and a
no-package run seeds the package before filing. Its repairs (r1 F3, r5 F1) are in the findings log.

## Open

- **No size budget.** To be set by the supervisor, as for the spec guides.
- **The Compose library is unmerged.** `Dev/Compose` and the September guide revisions exist only
  on `work/uimap-cmp` and `work/skai-v6-uimap-integration`; `main`'s Compose placeholder guide
  still says the libraries are project-vendored. Merge or retire is a supervisor decision.
- **The real-screen entry trigger** is deferred on both platforms ("rebuild-plan D12"); that plan
  is in neither repository. Until it lands, reaching a scaffold from a real screen blocks.
- Top-level `todos:` are not rendered.
- May 2026 H3 deferred; the scope-expansion rule and L1 / L3 / L6 logged pending recurrence.
- The lost spec's *Skills* section may have held host-adapter rules beyond P1; nothing survives.

## Adopts — 2026-10-20 (known gaps)

UI Map implementation and both artifact references adopt
[`product-specs-system-design.md`](product-specs-system-design.md) § Decisions — 2026-10-20 (format
definitions and propagation): the **Gap** sub-bullet, one Decision line, `## Decision Log` as the
artifact's last section, the pointer sentence, gap items carried past the Discussion gate, and zero
open gaps in either artifact before the official-map write. The architecture guide adopts the same,
keeping its lean Discussion (collapse a topic around the current decision, remove stale items): the
supervisor ruled 2026-10-20 that the house style follows UI Map here, the log outliving its items.
Caps (supervisor, 2026-10-20), set a little under the compressed sizes after the known-gaps
additions; the guides' extensive refinement history counts as compression, so these are not interim:
`ui-map-architecture.md` 35,700; `ui-map-architecture-artifacts.md` 5,500;
`ui-map-implementation.md` 50,900; `ui-map-implementation-artifacts.md` 6,500. Whole-file bytes by
`wc -c`; they bind every repair per the refinement guide's size-budget rule.

## Adopts — 2026-10-21 (working docs placement)

Working documents serving a package live in its `working-docs/` folder and archive with it at promotion (`ui-map-architecture-artifacts.md`, `ui-map-implementation-artifacts.md`, `ui-map-implementation.md` § Archive the package; caps held; skai#92, `Guides/Core/working-doc-conventions.md`); build and test output goes to the scratch root, never the package. The layout above is superseded on two lines: build and render output is no longer persisted under `evidence/` (the Evidence bracket names the scratch path), and a no-proposal conformance run lives at `skai/working-docs/<session>/ui-map-implementation.md`, with no branch segment.

## Amendment — 2026-11-11: Change Requests As Packages Against A Base; Map Changes By Domain (skai#101)

Rulings: skai#101 (body updated 2026-11-11: requests only against architecture; the page marks changes rather than comparing maps), the `ui-map-chg-mgmt` design package's decisions and code TODOs (merged from `work/ui-map-changes`), and the shared model in `change-requests-design.md` § Amendment — 2026-11-11 (skai#108, skai#129) and § Amendment — 2026-11-07 (skai#118). Supersedes P8's request file, status and reviewer response, the 2026-10-19 change request triage, and the Artifacts entry `change-requests/ui-map-<nnn>.md`. The UI Map guides keep no size budget (§ Open; supervisor: no aggressive compression), so the compression round is skipped; edits replace text in place. Inventory per skai#90, before prose.

**ui-map-architecture-artifacts.md must say:**

1. **A UI Map change request is the `ui-map/` sub-package of a request folder** per `change-requests.md`: `skai/changes/<change-id>/changes/CR-<id>/ui-map/`, holding the architecture artifact, its proposed map and render; its base is the nearest UI Map package up the chain, else the production map. The package paragraph no longer says the type folder owns requests.
2. **`## Change requests` (the request file, `Change Request Status`, `Reviewer Response`, lifecycle) goes**; a pointer to `change-requests.md` replaces it.
3. **Map Changes grouped by domain** (designs): a `### <domain>` heading per domain in the map's order, entries in the map's scene order; each entry `- M<n> <Type>: <identity>` naming one scene by ID, or one domain for a domain change (a change to several scenes is several entries); a route entry names the scene it starts from; a moved scene sits under its new domain, a removed one under its old domain. **Touches** goes. Several changes in one entry are numbered sub-changes, as Design Changes; an entry resting on an open gap carries a gap footnote, as Design Changes.
4. After a fold, each difference the request brought ends `; Change request: CR-<id> M<n>` in the base's recomputed list; the `Change request` Source stays for that.
5. **"Production map"** replaces "official map" throughout the UI Map guides.

**ui-map-architecture.md must say:**

6. **Initiation:** per `change-requests.md`, settle whether the work is a request; for one, reopen or create its `ui-map/` sub-package. The reopen-on-change-request paragraphs (the supervisor reads the request and says what to do; status moves) go.
7. **Base and diff:** a request's proposed map starts from its base's proposed map (or the production map); `## Map Changes` is the diff against the base.
8. **Folding a request into its base** (proposal; the supervisor confirms, since #121 moves UI Map promotion out of implementation later): architecture, on the supervisor's ask, writes the request's proposed map into the base's, marks the base's `## Map Changes` `Pending re-derivation.`, moves the request per `change-requests.md` and re-renders the base. Unlike other types, the request's entries are not appended (Tim, 2026-11-11: a change list is a diff, so it is recomputed): the base's author recomputes the list on reopen, as any reopen does, a difference the request brought joining its scene's existing entry (a sub-change, or part of an added scene's addition), else a new entry at the next `M` number, citing `; Change request: CR-<id> M<n>` either way. This replaces the appended-entry overlap rules (duplicate entries, merging under the lower ID) that cold rounds r6–r17 kept finding faults in.

**ui-map-implementation.md and its artifacts must say:**

9. **A map that must change** is an input this run's decisions change: per `change-requests.md` rule 8 the supervisor picks, reopen architecture on the package or file a request against it; the request file, its numbering and the "change request is open" gate go, replaced by the outcome-pending block. `## Change Requests` in the implementation artifact links the requests filed, if any.
10. **Terminal promote into production** follows `change-requests.md` rule 6: no other open `ui-map/` request part in the change.

**Tools (ui-map-render.py and the viewer, a new viewer version):** the `ui-map-chg-mgmt` code TODOs: the change package page's Map and Review tabs; change badges on scenes with any change to them or their outgoing connections; the Changes toggle with its count; a scene's entries first in the side panel, linked to the Review tab; the Review tab built from the package's Discussion and `## Map Changes` in the new format; domain filters in the review pages' style with scene counts; the hops drop-down; the search field's cross; no Theme or Clear buttons, the page following the system theme; section heading icons in their heading's color, no counts on Reached from and Opens; render fails when an entry names a scene not on the proposed map, except a removed scene; a request's proposed map layered over every UI Map package up its chain. The backfill's owed items stay out unless the designs carry them.

**Migration:** active packages' `## Map Changes` move to the grouped format (domain headings in map order, Touches removed, sub-changes numbered); the release notes say how. No UI Map request files exist in known hosts; any found in an active package are listed for the supervisor.
