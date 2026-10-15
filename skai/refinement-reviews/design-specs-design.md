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
   requirements gap, raised as a sibling requirements package, never specified quietly.
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
6. **IDs.** `UI-<PREFIX>-<NN>` per item, `.<NN>` per rule beneath it. Prefixes name the thing
   specified, never the file, and are unique across the specs; a prefix is a namespace and may span
   files after a move. IDs are file-independent and append-only from first drafting; retire in
   place at every level; modify keeps the ID when the promise is the same, a changed contract
   retires and adds. The next number for a prefix is its maximum in canon plus one; a collision
   between packages is caught when the later one promotes. A prefix names the thing including its
   kind where the bare noun is abstract (`UI-DEFAULT-STAGE`, not `UI-DEFAULT`; supervisor,
   2026-10-14); abbreviation is fine, readers learn prefixes by familiarity.
7. **Format.** Title Case headings. A title and an intro paragraph, then `##` parts (not cited),
   `###` per citable item carrying only its ID, rules as bold two-digit bullets, data as tables or
   plain lists. An item opens with a brief statement of what it is about and the link to the
   requirement it presents, then its rules (supervisor, 2026-10-14: `UI-STAGE-01` opened straight
   into "Day headings" with no statement of what a day group is and no link to the requirement
   defining it). A `##` part is a grouping only: it may open with a one-line description that
   orients and binds nothing; anything that says what shows or when belongs under an item. Reference-style links with definitions at the bottom; requirement IDs cited as
   links that may target a draft in an active requirements package until promotion repoints them;
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
9. **Change packages.** Same shape as requirements: authoring then promotion, under
   `skai/changes/<change-id>/design-specs/`, drafts whole-file under `proposed-design-specs/`,
   typed change items (`S<n>`, add/modify/retire/move × file, item, sub-item, index line, glossary
   entry, known-difference note) showing changed text inline for changes inside an existing file,
   each identity a link to the draft; a new file is one item whose identity links the whole draft
   and whose description summarizes it (clarified 2026-10-14, round 8).
   Packages are decoupled; the one link that may cross is a cited draft requirement. Promotion
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
  pages rather than restating them, and cite the requirements guides for the package lifecycle they
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

**Not the target:** the requirements guides (their lifecycle is inherited, not reviewed here); the
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
- No design change request artifact (tried, withdrawn).
- Spec and requirements packages stay decoupled; a requirements gap seeds a sibling package and
  stops; the spec cites the draft ID and waits for its promotion.
- Platform deviations use the known-difference blockquote; a shared deviation form is parked.
- Static-copy drift between design and specs is parked.
- `move` for requirements is parked.
- Title Case alignment of the requirements catalog and the older guides is a separate change.
