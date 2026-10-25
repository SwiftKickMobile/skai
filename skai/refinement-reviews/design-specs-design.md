# Design Specs — Design Spec

The standard for refining the design-specs building block: the four guides under
`Guides/DesignSpecs/` and their two skill wrappers. Condensed from the session plan
(`skai/working-docs/work/ui-specs/design-specs/design-specs-plan.md` in the SalesPro checkout),
whose Decisions and Review Resolutions are the supervisor's rulings of 2026-10-13, amended on
2026-10-14 from the UI Specs Review of the prototype package (critiques grouped in
`skai/working-docs/main/design-specs/ui-specs-review-critiques.md`). Where this document and
the plan differ on a 2026-10-13 ruling, the plan is the record; the 2026-10-14 amendments are
recorded here only.

## What a Design Spec Is

A design spec joins a screen's design to the product's requirements. It says which drawn state shows
under which condition, how data is formatted, which copy varies with state or data, what each
control does within the screen, where the screen leads, and which shared patterns it uses by
reference. A story is fully described by three artifacts: requirements, designs, design specs. The
UI Map is a technical document downstream of all three and references none of them.

## Decisions

1. **One home per fact.** Requirements own promises and product thresholds; the design owns
   appearance and the copy of what it draws; the spec owns how a screen presents the promises. A
   spec cites a requirement and never restates its rule. A rule that narrows a requirement is a
   requirements gap, raised as a change request against the open product spec package or the
   catalog (amended 2026-10-18; previously a sibling requirements package), never specified quietly.
2. **Product language only, never appearance, never mechanism.** No design-tool identifiers, no
   platform names in rules, no color, position, shape or size words, no framework or code names.
   The ban on appearance is semantic: established product names and the relationships needed to
   identify a thing are allowed; prescribing how a thing looks is not.
3. **Copy.** A spec quotes a string only when it carries a format, varies with data, or belongs to
   something the design does not draw, which the spec then carries as data. Controls are named by
   what they do, never by their label; a label that changes with state is a mapping under the item.
4. **What counts as a state.** A screen state is a different layout, drawn by the design and bound
   by the spec. A component appearance is the same layout styled by condition; the design draws the
   variants, the spec binds condition to variant by product name. A data substitution is a
   different string in the same look and is data, not a state. An element dropping out without
   moving the rest is a component property. Standard system UI the app does not style is specified
   by condition and choices and never drawn.
   **Motion and polish** (supervisor, 2026-10-14) is a category of its own: transitions, animation,
   timing, haptics, the feel of loading and refresh, how things appear and leave. The design file
   cannot convey them and a careful developer will not add them unasked, so the spec says them,
   under the item they apply to, in product language (what moves, when, and what it conveys; never
   easing curves or pixel values). The test: would a careful developer ship this without being
   told? If not, the spec says it. The completeness check asks for it.
5. **Organization.** Screen is the primary key. One file per screen as product names it; a common
   file for a family of screens, still under `screens/`; `shared/` for a piece shown on screens of
   different families; `global/` for what every screen uses. A rule goes in the first place that
   fits; a piece is extracted the first time a rule would otherwise be written twice. All three
   folders exist from the start, each with an index. The glossary is the second index: it
   identifies and routes, binds nothing, and lists the items governing each thing the specs name.
   A glossary entry says what the term means and what it is for (supervisor, 2026-10-14); a
   recognizable detail or two may follow as secondary text, but it never inventories the thing's
   elements, position or appearance. For "Closed card": its purpose is essential, "features a
   celebration graphic" is allowable, every element listed is not. The glossary mirrors the spec
   organization: sections Global, Shared, then one per screen family, alphabetical within each; a
   term sits under the home of its governing item, never by first appearance or the agent's choice,
   so a cross-family term lands in Shared by the extraction rule and an entry moves with its item.
   An agent working a screen reads Global, Shared and that family's section. If the glossary
   outgrows one file it splits into per-folder glossaries along the same seams.
   **Overrides** (supervisor, 2026-10-14): a rule that narrows or replaces a shared or family rule
   says so and links the rule it supersedes; the parent rule never names its overrides. The
   override may restate the parent rule with its modifications rather than only the delta, for
   readability; that bends "stated once" deliberately. No silent precedence.
6. **IDs.** `UI-<PREFIX>-<NN>` per item, `-<NN>` per rule beneath it and `-<NN>-<NN>` one level
   down, which is the limit (amended 2026-10-18 from `.<NN>` and "nested as needed"; dashes read as
   one ID and parse unambiguously because a prefix never holds a digit). Prefixes name the thing
   specified, never the file, and are unique across the specs; a prefix is a namespace and may span
   files after a move. IDs are file-independent and append-only from first drafting; retire in
   place at every level; modify keeps the ID when the promise is the same, a changed contract
   retires and adds. The next number for a prefix is its maximum in canon plus one; a collision
   between packages is caught when the later one promotes. A prefix names the thing including its
   kind where the bare noun is abstract (`UI-DEFAULT-STAGE`, not `UI-DEFAULT`; supervisor,
   2026-10-14); abbreviation is fine, readers learn prefixes by familiarity.
7. **Format.** The shared spec file shape of [`spec-format-design.md`](spec-format-design.md),
   common to product specs and design specs since 2026-10-18: Title Case headings, a title and an
   intro paragraph, then `##` parts (not cited), `###` per citable item carrying only its ID, rules
   as bold two-digit bullets, data as tables keyed on their first column or plain lists. Glossary
   entries are `###` headings and every occurrence of a glossary term in spec prose links its entry.
   The spec tool validates the shape before the ten checks run. An item opens with a brief statement of what it is about and the link to the
   requirement it presents, then its rules (supervisor, 2026-10-14: `UI-STAGE-01` opened straight
   into "Day headings" with no statement of what a day group is and no link to the requirement
   defining it). A `##` part is a grouping only: it may open with a one-line description that
   orients and binds nothing; anything that says what shows or when belongs under an item. Reference-style links with definitions at the bottom; requirement IDs cited as
   links that may target a draft in an active product spec package until promotion repoints them;
   nothing links into the design tool. Known differences are a blockquote under the item, in the
   catalog's form, platform words appearing there and nowhere else. Pending specs are named inline
   as `(spec pending: <file>)`; a pending destination never blocks promotion, a pending global
   pattern an item depends on does.
8. **Authoring.** Inputs are open-ended; the agent always proposes; Discussion items only for what
   needs the supervisor. "What does the app do" is answered from the code and the requirements.
   Design-versus-app differences and undrawn states are Discussion items with a recommendation; a
   drawing is made directly or through a design package as the project's conventions and the
   supervisor say, and the item resolves only once the drawing exists and the agent has seen it.
   Platform differences the agent could not observe are assumptions, not known differences. No
   delegated authoring; cited files are drafted first.
   **Audit entry** (supervisor, 2026-10-14): "audit this package", or the guides having changed
   since an open package was drafted, is input on that package. The first move is all ten checks
   over every draft in it, not only changed items; each failure becomes a Discussion item before
   any fix. An agent must not presume an open package's drafts conform.
9. **Change packages.** Same shape as product specs: authoring then promotion, under
   `skai/changes/<change-id>/design-specs/`, drafts whole-file under `proposed-design-specs/`,
   typed change items (`S<n>`, add/modify/retire/move × file, item, rule, index line, glossary
   entry, known-difference note), each identity a link to the draft, with no inlined text since
   2026-10-18 (the rendered page shows the diff; spec-format-design decision 15), maintained as the
   drafts change rather than written after the gate, since the page takes each change's reason from it
   (2026-10-18, target 3); a new file is one item whose identity links the whole draft
   (clarified 2026-10-14, round 8; the description field went with inlined text on 2026-10-18).
   Packages are decoupled; the links that may cross are a cited draft requirement and a change
   request filed against the product spec package (2026-10-18). Promotion
   runs the ten verification checks, prepares destination links, writes whole files, archives the
   package; a spec promotes on approval and has no concern with implementation or the design
   file's state beyond the drawn-state check.
10. **Verification checks.** Ten, enumerated once in the content guide and run by authoring before
    its Discussion gate and by promotion before the write: restatement, appearance, product
    language, static copy, drawn state (the agent looks, on production or any approved change
    page; unavailable access blocks), links, one home, IDs and prefixes, indexes and glossary,
    completeness. Scope is the changed items plus every touched file as a whole.
    Authoring records one evidence line per check in its artifact before the gate (supervisor,
    2026-10-14: two backfill rounds in which the authoring agent reported the checks passed and a
    cold conformance review then found ten and twelve defects).

## Guide Shape

- Four guides: `design-specs.md` (content rules and the checks), `design-specs-authoring.md`
  (with *Working a Baseline* inside it), `design-specs-promotion.md`, `design-specs-artifacts.md`.
  The lookup name is the file stem. Two thin skill wrappers.
- Every rule sits inside the template it governs. Examples use LumenNotes; the worked example is
  SalesPro's and stays outside the guides.
- The guides cite the Figma guide and the design process guides for drawing conventions and change
  pages rather than restating them, and cite the product spec guides for the package lifecycle they
  mirror.
- Gates and advance intent follow skai's standard model: one planned gate in authoring (Discussion
  complete), one in promotion (Promotion Checks); `auto` never bypasses the Discussion blocked gate.

## Holes Already Found

- The checks were drafted as five and settled as ten; authoring and promotion must name the same
  ten in the same order.
- Review Resolution 20 said the next ID counts every active draft; the supervisor reversed that on
  2026-10-13 (canon only). The artifact-location pass applied the reversal; any stale wording is a
  defect.
- The worked example predates the guides and does not conform to them; it is context, not a
  compliance target.
- The prototype package passed V2 (appearance) at authoring with "dark" describing a tip card and
  the selected tab, and glossary entries describing dark mode and screen position (review,
  2026-10-14). The rule exists; the check as written did not make it applicable. Likely a ❌/✅
  pair on decision 2, or a test the check can run ("could a designer change this without the rule
  changing?").
- Glossary entries in the prototype enumerated content (seven tabs, rows) and held detail that
  belongs under an item (celebratory icons, which belong to the closed-stage spec); V9 (indexes and
  glossary) did not catch it.
- The shared day-headings rule in the family common file named the stage that overrides it; the
  link ran the wrong way.
- Nothing in the prototype specifies motion or polish anywhere, and no check asked.

## Scope

**Target:** `Guides/DesignSpecs/design-specs.md`, `design-specs-authoring.md`,
`design-specs-promotion.md`, `design-specs-artifacts.md`;
`Templates/skills/skai-design-specs-authoring/SKILL.md` and
`skai-design-specs-promotion/SKILL.md`.

**Not the target:** the product spec guides (their lifecycle is inherited, not reviewed here); the
design process and Figma guides; artifact location and the addendum boilerplate (settled by their
own passes); the SalesPro worked example and its package.

## What Simple Looks Like

- **Size budget: 60,000 bytes** for the four guides and two wrappers together, measured with
  `wc -c` (supervisor, 2026-10-14; 76,459 at declaration). It binds every repair per the
  refinement guide's size-budget rule: each fix states its byte cost, an addition pairs with a
  trim, and a fix that cannot fit is a supervisor decision.
- A rule is stated once, in the guide that owns it; the other guides cite it.
- A reader with a screen in hand finds the rule for it in one file.
- The checks read as the same ten in both workflows, with nothing discovered late.

## Settled Dispositions

- Acceptance criteria is not a fourth artifact: the package's item list is the AC.
- ~~No design change request artifact (tried, withdrawn).~~ Superseded 2026-10-18: change
  requests are a cross-type artifact any consumer files against a package or a catalog.
- ~~Spec and requirements packages stay decoupled; a requirements gap seeds a sibling package and
  stops.~~ Superseded 2026-10-18: a requirements gap files a change request against the open
  product spec package (or the catalog); the spec cites the draft ID once it is incorporated and
  waits for its promotion. Packages remain decoupled otherwise.
- Platform deviations use the known-difference blockquote; a shared deviation form is parked.
- Static-copy drift between design and specs is parked.
- `move` for requirements is parked.
- Title Case alignment of the product specs catalog and the older guides rides the 2026-10-18
  migration to the shared shape.

## Amendments — 2026-10-18

From the Offers retrospective (SalesPro checkout, `working-docs/requirements-process/planning.md`,
ephemeral). Product specs adopt this guide set's item shape, and the shape becomes a shared guide
with its own standard, [`spec-format-design.md`](spec-format-design.md), which both guide sets cite
instead of restating. Changes to this guide set:

- Rule IDs use dashes (`UI-NOTES-01-03`); nesting is capped one level below a rule.
- Glossary entries are `###` headings; every occurrence of a glossary term is linked.
- The spec tool validates shape, IDs, links and glossary links before the ten checks, at authoring's
  gate and at promotion; `references` lists citing locations before a modify or retire.
- A requirements gap is a change request, not a seeded sibling package.
- The size budget is re-measured after the shape rules move to the shared guide; 60,000 bytes stays
  the reference point until the supervisor re-sets it.
- Refinement order: the shared shape guide and tool first, then product specs, then this guide set,
  then one consistency pass across all three.

## Decisions — 2026-10-19 (change request triage)

Supervisor decisions after the catalog rework, where the agent proposed rejecting a request the
product owner had made. Shared by product specs, design specs and UI Map architecture.

1. **The supervisor rules; the agent applies.** A change request is read and decided by the
   supervisor, who tells the agent what to do with it ("incorporate 001", "reject 001, it belongs
   with the sync work"). The agent then applies that: for an incorporation the drafts and the
   change list, then `Incorporated`; otherwise the status and the supervisor's reason in
   `Reviewer Response`; then re-render. Until told, the agent leaves a `Proposed` request alone;
   it summarizes open requests when asked. `Proposed` keeps blocking promotion. The agent never
   rejects or supersedes on its own, and does not raise Discussion items to drive the ruling.
2. **A change request exists only against an open package.** It is the trace of someone other than
   the package's author asking for its drafts to change, without editing them. With no package
   open for the subject, whoever finds the defect opens a change package through authoring; the
   supervisor reviews it like any other. There is no request against the catalog, and supervisor
   input during authoring is a decision, never a request.
3. **A request carries drafts (supervisor, 2026-10-19).** Filing a request is authoring in
   miniature: the agent drafts the requested changes, in the spec shape, from the supervisor's
   input, and its page diffs them against the package's drafts like the package's own page. Where
   the input does not settle what the drafts should say, the agent asks at the filing workflow's
   own Discussion gate; a request goes out without drafts only when the supervisor, asked, agrees
   the drafts cannot be written from what they know. Observed 2026-10-19: a request filed from a
   fully stated model as a bare list, because the guide called drafts "optional".

Design specs adopt all three decisions of [`product-specs-system-design.md`](product-specs-system-design.md) § Decisions — 2026-10-19 unchanged; UI Map architecture adopts decision 1 (its requests come only from implementation).

## Size Budgets — 2026-10-18

Set by the supervisor from four efficiency reviews (SalesPro checkout, `working-docs/requirements-process/reviews/`), as today's size less measured obsolete content, less the reviewed trim on what remains, plus known growth. Whole-file bytes by `wc -c`, managed header and addendum footer included. They bind every repair per the refinement guide's size-budget rule.

These replace the 60,000-byte budget above.

| Target | File | Cap |
| --- | --- | --- |
| 2. Content | design-specs.md | 15,000 |
| 2. Content | design-specs-artifacts.md | 5,000 |
| 3. Authoring | design-specs-authoring.md | 17,000 (raised 2026-10-18 from 15,500 after the decided additions exceeded the growth estimate; confirmed by the supervisor) |
| 3. Authoring | skai-design-specs-authoring skill | 450 |
| 4. Promotion | design-specs-promotion.md | 12,800 |
| 4. Promotion | skai-design-specs-promotion skill | 450 |

Group caps across both spec types and the design process guides: content 37,000; authoring 54,900 (raised 2026-10-18 with design-specs-authoring); promotion 42,700.

**Rendered page, prominently linked (supervisor, 2026-10-18).** The authoring and promotion artifacts each link the package's rendered review page (`design-specs-review.html`) at the top, directly under the title; a change request's `request.md` links `request-review.html` the same way.

**Live render (supervisor, 2026-10-18).** The rendered page is the primary way the supervisor views a change package while it is being iterated on. Any time the package materially changes — a draft edited, a discussion item resolved, a change item added, a request triaged — the agent validates and re-renders before anything else, in every workflow that writes a package. The gate and promotion renders are not the only ones; they are the last of many. Validation and rendering take milliseconds, so there is no cost argument for deferring them.

## Adopts — 2026-10-20 (known gaps)

Design specs authoring, its artifact reference and promotion adopt
[`product-specs-system-design.md`](product-specs-system-design.md) § Decisions — 2026-10-20 (format
definitions and propagation) unchanged: the **Gap** sub-bullet, one Decision line, `## Decision Log`
as the artifact's last section, the pointer sentence to `known-gaps.md`, gap items carried past the
Discussion gate, readiness item 1 failing on an open gap. Caps (supervisor, 2026-10-20, a little
under the compressed sizes): `design-specs-authoring.md` 17,800; `design-specs-artifacts.md` 5,000
(unchanged); `design-specs-promotion.md` 12,800 (unchanged). These supersede the 2026-10-18 rows.

Slice 3 (2026-10-20): design specs authoring's *Drafting* adopts the gap footnote the same way (`product-specs-system-design.md` § Decisions — 2026-10-20 (known gaps: spec files)); cap 17,800 held (supervisor, 2026-10-20).

## Adopts — 2026-10-21 (working docs placement)

Working documents serving a package live in its `working-docs/` folder and archive with it at promotion (`design-specs-artifacts.md` layout, `design-specs-promotion.md` § Archive the Package; caps held; skai#92, `Guides/Core/working-doc-conventions.md`); build and test output goes to the scratch root, never the package.

## Amendment — 2026-10-25 (change requests: authoring against a base)

Design specs adopt [`product-specs-system-design.md`](product-specs-system-design.md) § Amendment —
2026-10-25 and the shared [`change-requests-design.md`](change-requests-design.md) with `S` for `R`
and `C3`/`C4` for `C7`/`C8`: `design-specs-artifacts.md` § Change Requests and its `request.md`
layout go; § The Package names the base and the two request folders and cites the shared guide;
`design-specs-authoring.md` § Requirements Gaps files "a package against the open product specs
package" instead of a request in the old form; `design-specs-promotion.md` § Raising a Change Request
becomes "start a package against the base". Supersedes § Decisions — 2026-10-19 where they conflict.
The set's cap of 60,000 holds unless compression says otherwise.


## Amendment — 2026-10-25 (plain language: a change item's reason)

Design specs adopt [`product-specs-system-design.md`](product-specs-system-design.md) § Amendment —
2026-10-25 (plain language): a spec change item's Justification is a reason in plain words, then its
source as a link; `design-specs-artifacts.md`'s Source line ("as the product spec guide") inherits
the rule and its example shows a reason before the source. Same plain-language pass, same standard.

Cap (supervisor, 2026-10-25, series PL): the design specs set **47,500** combined (was 60,000), a little under the compressed 47,721.
