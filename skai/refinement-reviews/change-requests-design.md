# Change Requests Guide Design

## Purpose

This document is the standard for SKAI's shared change requests reference: what it is for, what it
must and must not contain, and the decisions behind it. It is used to write and cold-review the
guide; it is not something an operator reads at runtime.

- [`Guides/Core/change-requests.md`](../../Guides/Core/change-requests.md) — what every change
  package type shares about bases and requests: a package authors against a base; a change request
  is a package whose base is another open package; promotion folds it into its base.

The guide is a reference, like the known-gaps guide: not a gated workflow and not a skill. Every
authoring and promotion guide sends the agent to it with one sentence where it first names the
base; the type's guide keeps what is specific to its artifact (how drafts or frames fold). Written
2026-10-25 from SwiftKickMobile/skai#99 and the design guides' request model of 2026-10-23.

## Authority and references

- [`design-process-design.md`](design-process-design.md) § Amendment — 2026-10-23 and its Rulings:
  the model as first written for design packages; this guide generalizes it and the design guides
  come to cite it.
- [`product-specs-system-design.md`](product-specs-system-design.md) § Amendment — 2026-10-25 and
  [`design-specs-design.md`](design-specs-design.md) § Amendment — 2026-10-25: what each spec guide
  must say; they supersede those standards' change request decisions of 2026-10-18 and 2026-10-19.
- [`internal/maintenance/change-packages.md`](../../internal/maintenance/change-packages.md) owns the
  package paths for maintainers; its change request paragraph is rewritten to this model.

## Requirements

1. **One model, stated once.** A package authors against a base: production by default; for a
   change request, another open package of the same type. Nothing differs but the base. A request
   against a request is one more level. The guide says this and the type guides cite it; none
   restates it.
2. **Paths.** A package against production at `skai/changes/<change-id>/<type>/`; a request at
   `<base>/change-requests/<nnn>/`, numbered by filing order across open and promoted requests, with its base's layout, holding only what it changes;
   `change-requests/` and `promoted-change-requests/` appear in any package that has them. The
   request's first input is its base.
3. **Starting a request.** The signal names the base ("request a change to <package>"); the request
   is created at the base's next free number unless an open request for the same work is named or in
   context, which is reopened; a promoted request is never reopened. A defect found in a base goes to
   an open package for it, or else starts a package against that base, whatever it is.
4. **No roles.** Whoever runs a workflow on a package authors it and may change anything in it. A
   request filed by one person and continued by another is one package under one set of rules.
   Selective acceptance is ordinary authoring: trim or edit the request, then promote what is left.
5. **Promotion folds into the base.** Into production as each type's promotion guide says; into a
   package, the request's drafts become the base's, its change items are appended to the base's list
   with the base's next IDs and a provenance note (the entry's own reason and source, then `; Change request: <nnn> <id>`),
   its open gap items join the base's Discussion with Gap lines kept, the base names the promoted
   request, the request archives at `<base>/promoted-change-requests/<nnn>/`, and then the base's
   page is re-rendered, so its links follow the move. The type guide owns how its drafts or frames fold.
6. **Gaps.** A request inherits its base's open gaps like any input's; its own travel into the base
   at promotion; promotion into production allows none (known-gaps rule 6).
7. **The record.** The request's Discussion and Decision Log are the trail of what was accepted,
   edited or dropped and why; the base's Assumptions name the promoted request. The originator
   reads that record or asks; a view of the outcome built for the originator is a later renderer
   feature (deferred, supervisor, 2026-10-24).
8. **Pages and tools.** The same renderer and checks serve a request and a package; a request's
   page is layered on its base's drafts; the top bar reads `<title>: <change-id> | <nnn> | …`.
9. **Requests against inputs** (supervisor, 2026-10-25, cross-check item 2 generalized). A package
   whose decisions change an input other than its base asks the supervisor, no later than its review
   gate advancing, whether that input is edited directly through its own workflow or by a request
   against it; the guides never pick the route (supervisor, 2026-11-07: the artifact guides are
   workflow-agnostic); before the package
   promotes, every such request has its outcome applied, an invalidating outcome returns it to
   authoring and unruled ones block. The design and spec promotion guides point at this rule instead
   of stating it; the design guide batches its filings at the Review gate, the spec guides file as they
   find each gap, and neither restates the other's timing.
10. **Agent-facing, short, plain.** Numbered rules with a bold lead sentence, one LumenNotes path
   example, no narrative. Read whole when a base or request is in play.

## Rulings — 2026-10-25

- **Ending without promotion: no rule.** A package that is not promoted is simply not promoted,
  as a cancelled feature's changes are not merged; the guides spend no bytes on it (supervisor).
- **Into production nothing is open; into a package, open things move up a level** (supervisor,
  2026-10-25). Promotion into production requires no open Discussion item, gap or request. Promotion
  into a package carries whatever is open with the request: open items and gaps join the base's
  Discussion as the base's own (next `D` numbers, Gap lines kept, logged), and a request still open
  against the promoted request is re-filed against the base at the base's next number, so it keeps a
  live base. This widens the design promotion readiness, which required non-gap items resolved into a
  package too; recorded as a cross-check change for the design guides.
- **UI Map guides are not in this pass.** They keep their request-on-reopen model until their own
  refinement and do not point at the shared guide yet; the shared guide says nothing about who uses
  it (supervisor: a guide references a shared guide, never the reverse).

## Size budget

**2,950 bytes** (supervisor, 2026-10-25; drafted 2,990, compressed twice to 2,985). Whole-file bytes by
`wc -c`, managed header and addendum footer included. It binds every repair per the refinement guide's
size-budget rule.

## Boundaries

The guide does not say how a type's drafts or frames fold, what a change item looks like, how a page
is rendered, or what readiness checks; each type's guides own those and cite this one. It has no
gates and invokes no skill.

## Size Budget — 2026-10-25

Cap **2,950** holds (supervisor, 2026-10-25, series PL); the provenance tag on a folded entry now follows the entry's own reason and source.

## Amendment — 2026-11-07: Open Items Stay Where Raised (skai#118, skai#116)

Supersedes requirement 5's open-gap clause, requirement 6's "its own travel into the base", and the
2026-10-25 ruling "into a package, open things move up a level" (supervisor, 2026-11-07; rulings in
the #118 planning document, D1–D5). The guide must say:

1. **Open work stays put.** An open Discussion item or gap stays in the package where it was raised
   and keeps its ID; promotion moves and renumbers none.
2. **Citations are links.** Another package's item, the base's included, is cited by link,
   `[D27][001 D27]` defined as `<path>#d27`, wherever it is cited (gap footnotes, prose,
   justifications, the Decision Log). Moving a package only updates link paths.
3. **Folding.** A request's footnotes naming its own items become links to them in the archived
   request.
4. **Deciding another package's item.** A request deciding an open item of its base
   (another input's item takes requirement 9's route; supervisor, 2026-11-07), drafts that item's answer in place of its placeholder, without its gap markers, and logs `- [D12][reminder-expiry D12] decided — <decision>`;
   its promotion checks D12 off where it lives with that decision ending `(<nnn>)`, removes its
   Gap line and markers, and logs `- D12 decided — <decision> (<nnn>)` there. The request holds each base file
   marking the item, without the marker. A link's label is defined once, to the cited package's
   authoring artifact, and names that package, never `base` (supervisor, 2026-11-07). Folding also turns the request's own `D<n>` in
   drafts and change items into links to the archived request (with item 3).
5. **Open requests of a promoted request** move to the base's `change-requests/` as
   `<nnn>-<their nnn>`, keeping that ID; their base, and first input, is now the base.
6. **Into production.** No open item, gap or request in the package or its promoted requests; those
   in a promoted request are resolved there by the base's author.

The type guides, `known-gaps.md`, `process-flow.md` and `spec-file-gaps.md` state their own parts of
this change and are refined against their own design specs.

## Size Budget — 2026-11-07

Superseded for `change-requests.md` below. Provisional, set before this amendment's refinement pass: skai#118, caps **3,200** for `change-requests.md`, **15,550** for `product-specs-promotion.md` and **47,500** for the design specs set (supervisor, 2026-11-07). Sizes at commit: 3,164; 15,469; 47,459.

Cap for `change-requests.md` after the amendment's compression round: **3,150** (supervisor, 2026-11-07; before 2,949, compressed 3,175). Trimmed under it by wording in rules 5–7.

Cap for `change-requests.md` raised to **3,300** (supervisor, 2026-11-07, after cold-review round 10; trims under 3,150 kept dropping spec qualifiers that the next round flagged).

Cap for `change-requests.md` raised to **3,450** (supervisor, 2026-11-09): content cut to fit 3,300 was restored (the LumenNotes example's contents, "Read for any base or request.", "in filing order", "Any package may hold…", "under the same rules"); a Fable compression review reached 3,442 and found nothing further without loss.

Cap for `change-requests.md` raised to **3,600** (supervisor, 2026-11-09, after cold-review round 18): rules 5 and 6 are restructured as short steps, one action each; byte-neutral fixes to the long sentences kept producing the next round's findings.

## Amendment — 2026-11-09: No Selective-Acceptance Instruction

Supersedes requirement 4's last sentence ("Selective acceptance is ordinary authoring: trim or edit the request, then promote what is left") and requirement 7's record for the originator (supervisor, 2026-11-09, after cold-review round 24). Promotion takes the package in whatever state its author left it; how anyone changes a package before promotion is ordinary authoring and not this guide's concern. Changed decisions, decided gaps and edited or dropped changes are already recorded by the Discussion, Decision Log and change-list rules every workflow follows, so the guide adds no instruction or record for partial acceptance and names no originator.

## Amendment — 2026-11-09: No Rule on Who Edits a Request

Supersedes requirement 4 in full (supervisor, 2026-11-09). Who may change a request is policy, and policy belongs to the workflow the supervisor defines; any statement here could contradict it, so the guide says nothing about it. The role assumption requirement 4 targeted (an agent forcing a change request instead of a direct edit) is covered by requirement 9: the supervisor picks between editing an input in its workflow and filing a request against it.

## Amendment — 2026-11-11: Requests As Folders Of Sub-Packages; Confirming The Route (skai#108, skai#129)

Rulings: skai#108 (supervisor, 2026-10-28, 2026-10-30 and 2026-11-07; the planning record's D1–D4, 2026-11-07 and 2026-11-11) and skai#129. Supersedes requirement 1's "a request differs only by base", requirement 2's paths and numbering, requirement 3's signal, requirement 8's top bar, and the 2026-11-07 amendment's item 5 paths. Inventory per skai#90: what each guide must say, before any prose.

**`change-requests.md` must say:**

1. **A request is a folder of sub-packages.** A change request is a folder `CR-<id>/` holding one sub-package per artifact type it changes, `<type>/`, each with that type's package layout and only the files it changes. Its sub-packages are authored and promoted under the same rules as any package.
2. **Where requests live.** An open request sits in its parent's `changes/` folder; a promoted one in its parent's `promoted/` folder. The parent is the change (`skai/changes/<change-id>/changes/CR-01/<type>/`) or, for a request against a request, that request (`changes/CR-01/changes/CR-01-01/`, promoted `changes/CR-01/promoted/CR-01-01/`). The names mirror `skai/changes/` and `skai/promoted/`.
3. **IDs.** `CR-` and two digits, the parent's next free number across its open and promoted requests, every type counted; a nested request's ID is its parent's plus its own (`CR-01-01`).
4. **Each sub-package's base** is the nearest package of its type up the chain: the parent request's sub-package of that type, else that request's parent's, up to the change's own package of that type; production where none has it. The base is the sub-package's first input.
5. **Starting work (skai#129).** When the supervisor's words say whether the work edits a package directly or is a change request, proceed; otherwise ask before creating or reopening anything. A request reopens an open request for the same work, named or in context; otherwise it takes the next free ID. A promoted request is never reopened. A defect in a base goes to an open package for it, or starts one against the base (unchanged).
6. **Promotion.** Each sub-package folds into its base per its type's promotion guide; a request's sub-packages promote together by default, part by part in any order only when the supervisor asks (#91 owns grouping). Each promoted sub-package moves to the parent's `promoted/CR-<id>/<type>/`; the open request's folder goes once its last sub-package has moved.
6a. **Into production, structure kept** (supervisor, 2026-11-11). When a type's package moves to `skai/promoted/<change-id>/<type>/`, that type's promoted request sub-packages move with it, keeping the folder structure: `skai/promoted/<change-id>/promoted/CR-01/<type>/`. A request's other types stay in the active change until their own package goes to production.
7. **Folding into a package** (the 2026-11-07 amendment's steps, with the new IDs): appended change items end `; Change request: CR-01 <id>`; the request's bare `D<n>` link to it (`[D5][CR-01 D5]`); base items the request decided are checked off with `(CR-01)`; the request is named in the base's Assumptions; the base is re-rendered after the move.
8. **Open requests inside a promoted request** move to the parent's `changes/` when the promoted request's folder goes, keeping their IDs (`changes/CR-01/changes/CR-01-01/` becomes `changes/CR-01-01/`); each sub-package's base follows from item 4.
9. **Another repository.** A type kept in another repository puts its sub-package at the same path there (as before; the cross-repository concern is parked in skai#123).
10. **Pages.** A request sub-package's page is layered on its base's drafts; the top bar reads `<title>: <change-id> | CR-01 | CR-01-01 | …`.
11. **Example.** LumenNotes: `skai/changes/reminder-expiry/changes/CR-01/product-specs/` holds `product-specs-authoring.md` and `proposed-product-specs/features/reminders.md`, the one draft it changes.
12. Requirement 9 (the supervisor picks how an input other than the base changes) stands as rule 8.

**The type guides must say** (each refined against its own design spec, which adopts this amendment):

13. **Artifacts guides** (product specs, design specs): the package layout no longer holds `change-requests/` or `promoted-change-requests/`; a request's sub-package has the type's layout; the provenance tag is `; Change request: CR-01 R<n>` (`S<n>`, `V<n>`).
14. **Authoring guides** (product specs, design specs, design): the entry step says that whether work edits a package directly or is a request follows `change-requests.md` (confirmed with the supervisor when unclear), and a request's sub-package is created or reopened per that guide; no guide hard-codes a route to another package (the product specs references sweep and the design specs requirements gaps point at rule 8 instead).
15. **Promotion guides** (product specs, design specs, design): a request sub-package archives to `<parent>/promoted/CR-<id>/<type>/`; production readiness counts every promoted request sub-package of the type in the change, at any depth; the promoted-path check names the new path.
16. **Figma designer guide:** a request's Section is `CR-01 — <name>`, a nested one `CR-01-01 — <name>`; the ID is the request's.
17. **README, `internal/maintenance/change-packages.md`:** the request paths and their one-line descriptions.

**Tools:** `spec-tool.py`, `design-tool.py` and `figma-page-check.js` read only the new layout: a request is a `CR-<id>` folder under a `changes/` or `promoted/` folder inside a change, never a change folder under `skai/changes/`; a missing base type falls back up the chain, then to production; promoted requests are found under `promoted/`.

**Migration** (release notes): within active base packages, every request, open or promoted, moves to the new layout with two-digit IDs, nested ones too, with links, page paths, provenance tags and Figma Section names updated and pages re-rendered; archived packages are never touched; a request whose promotion is unfinished finishes under the old layout first; a `request.md` from before requests were packages stays as a record.

**Process (supervisor, 2026-11-11, skai#90 as amended):** the guide edits were first written into the guides; they are withdrawn and become a proposal for a proposal review, and caps follow the compression of the shape that review settles. Caps recorded earlier the same day are withdrawn.

**Rulings after the first draft (supervisor, 2026-11-11):**

- Prefer lean until more is shown to be needed. Left implied: the promoted nested path, "in any order" for part-by-part promotion, the nested ID in the top-bar example, "authored and promoted like any package". Kept explicit: numbering across open and promoted requests whatever their types, the move-up example, a request's other types staying.
- Items 6, 6a and 8 are one rule for any base: promotion moves what it promotes from `changes/` to the matching place under `promoted/`, or into production under `skai/promoted/<change-id>/`, taking along the promoted sub-packages folded into it, paths kept. Links follow per rule 5.2.
- Production readiness counts open request sub-packages of the promoting package's type only; a request's other types may stay open.
- A request page layers on the drafts of every package of its type above it, nearest winning; its base (item 4) stays singular.
- Production is the root base (supervisor, 2026-11-11): a request part with no package of its type up the chain builds on production like any base; it archives under `skai/promoted/<change-id>/` by the one promotion rule, and its Figma Section sits on a change page, never on `Production`.

**Proposal review (Codex Terra 6.1 high, 2026-11-11), applied:** readiness into production checks for open request sub-packages of the type anywhere in the change; authoring settles whether work is a request before reopening or creating, and keeps the request signal; the type guides' base-write steps no longer move open requests (the shared rule's last-sub-package move owns it); a moved request's first input is repointed to its new base; type archive steps send a request's sub-package to its destination per `change-requests.md`; design specs' provenance tag ends `S<n>`.

**Caps (supervisor, 2026-11-11, after the proposal review and compression of the settled shape; a little under the compressed sizes):** `change-requests.md` **4,220** (compressed 4,240 after dropping three additions the supervisor judged unneeded: "in the active change", the full destination path in rule 4's lead, removing the empty request folder); `product-specs-authoring.md` **18,920** (18,931); the design specs set **47,800** (47,827); `design-promotion.md` **12,160** (12,172); the Figma pair **18,140** (18,152). Unchanged: `product-specs-artifacts.md` 5,450, `product-specs-promotion.md` 15,550, `design-authoring.md` 16,000.

**Cap (supervisor, 2026-11-11, after design specs rounds 3–4 found two defects shared with product specs promotion):** `product-specs-promotion.md` **15,620** (was 15,550; 15,628 with the two fixes: a pending input outcome waits instead of returning to authoring, and the pre-write check names the `product-specs/` destination).
