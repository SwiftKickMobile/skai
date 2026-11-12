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
never hand-rolled and never a `handoff`. Wiring can land in production code (a new case on a real
route enum, a new tab on the app's bar); building it to designs or specs (labels, icons, new
feature data) is the feature work that follows, never the scaffold's.

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

## Decisions — 2026-11-07 (route files and tab bars; skai#81, skai#57)

**Route files (skai#81).** Each nav, tab or child route enum lives in its own `<Scene><Kind>Route` file beside the scene's view model, not inside it; a scene's modal destinations share one `<Scene>ModalRoute` file (the SwiftUI per-style modal enums together, or the Compose modal sealed class). Both platform guides' scene layouts show these files, and Compose placeholder routes follow the same layout.

**Tab bars (skai#57).** The scaffold uses the app's bars as already set up; styling bars the app hasn't styled, building non-standard bars, and adding components or customizations to standard bars are not its job. A tab added to the app's own tab bar uses that bar, through the placeholder guides' real-screen route (skai#127). As in production, a scaffolded tab bar is selected through the view model's tab route enum: the SwiftUI placeholder library's `PlaceholderScene` takes a `selection:` binding and each `PlaceholderTab` its `route:` case, and debug builds stop when a tab given `selection:` has no route of that enum (supervisor, 2026-11-07). Withdrawn 2026-11-11 (supervisor): the rule that a scaffolded tab bar's labels and icons are production code taken from the inputs. A tab is labeled with its scene's name and a fitting icon, like the rest of the placeholder; building the bar to designs or specs is feature work (P6).

Caps (supervisor, 2026-11-07), whole-file bytes by `wc -c`, binding every repair per the refinement guide's size-budget rule: `ui-map-swiftui.md` 10,050 (raised to 10,170 on 2026-11-10 for nav and child `.id(route)`); `ui-map-compose.md` 10,850; `ui-map-swiftui-placeholders.md` 15,100 (raised from 15,050 for the tab selection binding; raised to 15,160 on 2026-11-11 for nav and child `.id(route)`; lowered to 15,080 the same day after the #57 label rule's removal); `ui-map-compose-placeholders.md` 16,000; `ui-map-implementation.md` 51,500, replacing its 50,900 cap of 2026-10-20, which the guide already exceeded (lowered to 51,350 on 2026-11-11 after the #57 label rule's removal).

## Decisions — 2026-11-09 (Compose library merged; skai#128)

`Dev/Compose` is merged (supervisor), so the 2026-09-02 decisions hold and both Compose guides point to SKAI's library instead of project-vendored ones. The September guide text is redone against the current guides: route files (skai#81), the 2026-11-07 tab bar rules (skai#57), and the 2026-10-18 package naming win over it. The library's M3 `bottomSheetModal` replaces the September table's `bottomSheet` for `sheet`; `bottomSheet` stays for legacy code. Tabs are routes in a tab `NavHost`, switched with `navigateToTab`: the placeholder library's `PlaceholderTab` takes its `<Scene>TabRoute` case, and production tab routing does the same, reading the current tab from the `NavController` with no current-tab field in the view state (*State ownership*: Compose Navigation is the source of truth). A tabbed placeholder presented modally keeps its ✕ in each tab, as on SwiftUI.

**SwiftUI is the standard for the Compose guides** (supervisor, 2026-11-09). Each Compose guide matches its SwiftUI counterpart in content and depth; Compose text with no SwiftUI counterpart is there only for a need Compose has and SwiftUI doesn't, and says it as briefly. This replaces the 2026-11-07 Compose caps for this pass; new caps follow the series. Caps (supervisor, 2026-11-11), after a section-by-section comparison with the SwiftUI guides and targeted trims: `ui-map-compose.md` 13,150; `ui-map-compose-placeholders.md` 16,500, lowered to 16,380 the same day after the #57 label rule's removal.

**The app owns its dependencies** (supervisor, 2026-11-10; skai#133). The Compose library declares its dependencies as `implementation` at the oldest versions its sources build with, so Gradle keeps a host's newer versions and linking the library upgrades nothing. The guide names the include and the two artifacts and gives no other project setup. This reverses the `api` repair of compose-r1 F1.

**Route identity is the whole value** (supervisor, 2026-11-10; skai#131). A route's associated values are part of its destination's identity, so a new value is a new screen; data that isn't part of a screen's identity is an event, not a route (rationale only: the guides state no rule on how an app sends events). Every SwiftUI route enum, tabs included, is `Identifiable, Hashable` with `var id: Self { self }`, and the guide adds no rule on values in tab routes. Nav and child destination content takes `.id(route)`, in placeholder wiring as in production, since feature work builds on the scaffold's routing, since a view's view model lives as long as the view and SwiftUI otherwise keeps the shown screen when only the value changes; `item:` modals replace themselves. Animating the swap, or updating a screen in place instead, is feature work. The SwiftUI placeholder library requires `route:` on every `PlaceholderTab`, takes the tab's identity from the route value, and matches selection by `==`; a tabbed `PlaceholderScene` always takes `selection:`. Compose is unchanged: its data-class routes already compare by value, and matching tabs by class differs only for tabs that share a case. This replaces the 2026-11-07 tab-bar paragraph's selection details.

## Decisions — 2026-11-11 (form factors; skai#67)

**Form factors** (supervisor, 2026-11-11). A map may declare a top-level `form_factors` list, the project's own values (`phone`, `tablet`, …), as it declares `modal_styles`. A map without it reads and validates exactly as before, and no form-factor marking is allowed in it. Unmarked means every form factor; marking is the exception. The guides say what form factors are for and set no limit on the values.

- A screen that doesn't exist on every form factor says so on its definition: `form_factor: [tablet]`. Agents read the YAML, so this is declared, not derived; the validator works out where each screen is reachable and names any screen whose declaration doesn't match.
- A route with form factors of its own is a `to:` entry: `- to: log` with `form_factor: [...]`, and `scene:` holding the screen's fields when the entry defines it. A bare name stays a reference and a single-key mapping a definition. A route's form factors must fall within its source's and its destination's; an unmarked route into a marked screen takes the screen's.
- `modal_style` may be a map from form factor to style (`{ phone: full_screen, tablet: card }`); a plain string means every form factor. The map form needs a style for every form factor on which a modal route reaches the screen, and only those.
- A screen reached by several routes from one parent, and no other, takes that parent as its visual home without `primary_parent`, in the container that defines it. A screen reached differently per form factor is the common case.
- Form factors have a guide of their own, `ui-map-form-factors.md`, so sessions without them don't read the rules (supervisor, 2026-11-11). The map guide keeps what applies to every map and one pointer: read it when the map declares `form_factors` or the work adds a form-factor difference; the renderer's form-factor errors name it too.
- How code reads which form factor applies and branches on it is the project's pattern, reached from `ui-map-form-factors-addendum.md`; SKAI bakes in no form-factor coding rule. A missing pattern blocks, and the agent works with the supervisor to add it.
- Map identifiers (domain and scene IDs, `implements` values, `modal_styles`, `form_factors`) are lower snake case, stated in the map guide and enforced by the schema; the platform guides keep only their conversion to code names.
- The viewer marks a screen's or route's form factors and filters the map by form factor: held until the `ui-map-chg-mgmt` design package is folded, since both change the map page's top bar (supervisor, 2026-11-11).
- A project's UI Map conventions (deliberate overrides, non-standard modal styles and their code, the scenes folder root) are reached from `ui-map-implementation-addendum.md`, which may point to project documents, not from the README, which is becoming a table of pointers (supervisor, 2026-11-11). A missing one blocks, and the agent works with the supervisor to add it.
- Caps (supervisor, 2026-11-11), whole-file bytes by `wc -c`, binding every repair per the refinement guide's size-budget rule: `ui-map-guide.md` 17,300 (its first cap: 16,876 plus the compressed 439-byte addition, set a little under); `ui-map-form-factors.md` 2,800 (its text went through a compression round before moving out of the map guide).
- Caps for the conventions move (supervisor, 2026-11-11), after a compression round: `ui-map-implementation.md` 51,370; `ui-map-swiftui.md` 10,120; `ui-map-compose.md` 13,110; `ui-map-swiftui-placeholders.md` 15,080 and `ui-map-compose-placeholders.md` 16,380 (unchanged); `ui-map-architecture-artifacts.md` 5,920, replacing its 5,500 cap of 2026-10-20, which the guide already exceeded.
- Caps after merging main's skai#101 work (supervisor, 2026-11-11), each the merged size rounded up to the next 10 so the next refinement doesn't cut text to fit: `ui-map-guide.md` 17,370; `ui-map-implementation.md` 52,470; `ui-map-architecture-artifacts.md` 6,310; `ui-map-architecture.md` 36,980 and `ui-map-implementation-artifacts.md` 6,880, replacing their 35,700 and 6,500 caps of 2026-10-20, which the guides already exceeded.

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
