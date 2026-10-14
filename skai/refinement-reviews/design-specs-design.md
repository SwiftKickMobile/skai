# Design Specs — Design Spec

The standard for refining the design-specs building block: the four guides under
`Guides/DesignSpecs/` and their two skill wrappers. Condensed from the session plan
(`skai/working-docs/work/ui-specs/design-specs/design-specs-plan.md` in the SalesPro worktree),
whose Decisions and Review Resolutions are the supervisor's rulings of 2026-10-13. Where this
document and the plan differ, the plan is the record. Nothing here is inferred beyond it: no size
budget is declared, because none was decided.

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
5. **Organization.** Screen is the primary key. One file per screen as product names it; a common
   file for a family of screens, still under `screens/`; `shared/` for a piece shown on screens of
   different families; `global/` for what every screen uses. A rule goes in the first place that
   fits; a piece is extracted the first time a rule would otherwise be written twice. All three
   folders exist from the start, each with an index. The glossary is the second index: it
   identifies and routes, binds nothing, and lists the items governing each thing the specs name.
6. **IDs.** `UI-<PREFIX>-<NN>` per item, `.<NN>` per rule beneath it. Prefixes name the thing
   specified, never the file, and are unique across the specs; a prefix is a namespace and may span
   files after a move. IDs are file-independent and append-only from first drafting; retire in
   place at every level; modify keeps the ID when the promise is the same, a changed contract
   retires and adds. The next number for a prefix is its maximum in canon plus one; a collision
   between packages is caught when the later one promotes.
7. **Format.** Title Case headings. A title and an intro paragraph, then `##` parts (not cited),
   `###` per citable item carrying only its ID, rules as bold two-digit bullets, data as tables or
   plain lists. Reference-style links with definitions at the bottom; requirement IDs cited as
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
9. **Change packages.** Same shape as requirements: authoring then promotion, under
   `skai/changes/<change-id>/design-specs/`, drafts whole-file under `proposed-design-specs/`,
   typed change items (`S<n>`, add/modify/retire/move × file, item, sub-item, index line, glossary
   entry, known-difference note) showing changed text inline, each identity a link to the draft.
   Packages are decoupled; the one link that may cross is a cited draft requirement. Promotion
   runs the ten verification checks, prepares destination links, writes whole files, archives the
   package; a spec promotes on approval and has no concern with implementation or the design
   file's state beyond the drawn-state check.
10. **Verification checks.** Ten, enumerated once in the content guide and run by authoring before
    its Discussion gate and by promotion before the write: restatement, appearance, product
    language, static copy, drawn state (the agent looks, on production or any approved change
    page; unavailable access blocks), links, one home, IDs and prefixes, indexes and glossary,
    completeness. Scope is the changed items plus every touched file as a whole.

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

## Scope

**Target:** `Guides/DesignSpecs/design-specs.md`, `design-specs-authoring.md`,
`design-specs-promotion.md`, `design-specs-artifacts.md`;
`Templates/skills/skai-design-specs-authoring/SKILL.md` and
`skai-design-specs-promotion/SKILL.md`.

**Not the target:** the requirements guides (their lifecycle is inherited, not reviewed here); the
design process and Figma guides; artifact location and the addendum boilerplate (settled by their
own passes); the SalesPro worked example and its package.

## What Simple Looks Like

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
