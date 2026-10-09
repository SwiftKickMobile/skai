# Guide authoring conventions

This is a maintainer reference, read only when the routing table in [`../maintain-skai.md`](../maintain-skai.md) applies. It is not an installed asset or a runtime dependency of host workflows.

## Guides/ subdirectory convention

All runtime guides live under a topical subdirectory within `Guides/`. Do not place guides at the `Guides/` top level. Register them in the manifest with the matching managed header. Maintainer-only references under `internal/maintenance/` are not runtime assets and need neither a manifest entry nor a managed header.

| Subdirectory | Purpose |
|---|---|
| `Core/` | Cross-cutting foundations: debugging, working-doc conventions, update installation |
| `Spec/` | Work spec design and implementation |
| `Test/` | Unit testing (planning, infrastructure, writing) |
| `Process/` | Retro, process problem reporting, ticket creation |
| `UIMap/` | UI Map system: YAML format, platform references, planning/implementation methods, FigJam migration |
| `Requirements/` | Requirements system: catalog content rules, authoring, promotion, artifact formats |
| `Design/` | Figma design file conventions |

When adding a new guide, place it in the most appropriate existing subdirectory. If none fits, propose a new subdirectory and document it here.

### Examples vs. derivations

Agents copy the worked **example**, not the surrounding prose — an example outweighs any rule, and a missing or mismatched one misleads more than absent text. Two consequences for authoring:

- **Each distinct *path* a guide teaches needs its own faithful example.** With only one (e.g. only the audit case, or only the root case), it becomes the gravitational center and agents misapply it to the other paths.
- **Never enumerate *compositions*.** Route kinds, options, and states combine combinatorially — an example per combination bloats the guide and still leaves gaps. State the governing rule as a **decision procedure the agent applies** ("before X, ask Y; do Z only if…"), frame per-case recipes as *derivations* of it, and let the agent derive the combinations you didn't draw. Illustrate the bounded base set; derive the rest.

## Sanity scan (after every guide edit)

Run this scan after *each* guide edit, not just at the end of a batch. Deferring the scan to the end of a batch is the proven failure mode -- violations introduced early in the batch survive unchecked.

**Record the result of every check, even when clean.** For each check below, write down either `0 occurrences` (with the search / inspection used — file paths, `grep` / `rg` pattern, or "visual review of section X") or a list of occurrences classified per-check (e.g., `<path>:<line>` → `false positive (intentional per …)` / `to fix` / `to revisit`). Reading the check and self-certifying "done" without a recorded result is the failure mode this rule prevents — a `0 occurrences` line with the search used is the minimum evidence. This matches the recording discipline already required for flow-reflection simulations (see [`gated-workflows.md`](gated-workflows.md#flow-reflection-required-for-guides-with-gates)).

Apply the gated-workflow checks only to workflows with gates; use the change-package checks in [`change-packages.md`](change-packages.md#verification) when packages are involved. For ephemeral working documents use the working-doc path formula; change packages use their own type paths.

Checks:

**Structure:**
- A managed file you edited whose `Managed-Updated-At` is earlier than that edit (`git status --short` lists the candidates; read each header)
- Missing `## Gates` section (if the guide has gates)
- Missing `## Advance intent` section (if the guide has gates)
- Inconsistent terms ("Next Command" instead of "advance intent")
- "human" used for the supervisor role (should be "supervisor"; grep `\bhuman` and classify each hit)
- A gated guide whose `## Gates` lacks the one-sentence supervisor definition
- Mixed gate terminology ("checkpoint" and "gate" used interchangeably without a workflow-specific reason)
- Stack-mismatched references (e.g., Xcode terms in Android-only sections)
- If the guide creates ephemeral working docs, stale path layouts that skip the required `session-name` folder

**Process-flow template compliance:**
- Gate controls missing shared approval, persistence or blocked-stop invariants; assess an explicitly declared compact control model against those invariants rather than requiring default text verbatim
- Advance controls missing their declared authorization/phase semantics; preserve documented variants such as no-auto workflows rather than inserting default auto text
- References to `Guides/Core/process-flow.md` that imply it is a required runtime read (e.g., "This guide follows the shared process-flow mechanics in...")
- Standalone "Progress Tracking" or "Emoji System" sections that redefine the canonical marker conventions (`- [ ]` / `🟡`).

**Marker convention compliance:**
- `🟡` used in process artifacts (markdown workflow docs) — should be `- [ ]` / `- [x]` instead. `🟡` is reserved for in-code progress (test files, source files) where completion = removal. Canonical in-code case: `Guides/Test/unit-test-planning-guide.md`.
- `- [ ]` items missing a stable letter-led ID on the same line (e.g., `- [ ] Do thing` instead of `- [ ] T1 Do thing`). Letter-led so a leading digit isn't misparsed as an ordered-list item.
- Loose `- [ ]` lists under the same heading (blank lines between sibling items) — pushes the checkbox onto its own line in some renderers. Use tight lists for sibling checkbox items.
- `- [ ]` inside a heading line (`## - [ ] Foo`) — markdown task lists are scoped to list items; this renders as plain text.
- Discussion items in aggregator sections (`## Questions`, `## Decisions`, `## Tradeoffs`, `## Open Items`) instead of inline with their topic.
- Discussion items missing the `[Kind]` label (`[Question]` / `[Proposal]` / `[Tradeoff]`) — every item should declare its shape.
- Discussion phases that do not use the canonical gate pattern: blocked gate while `- [ ]` items remain, planned gate the moment they're all resolved (the *first planned gate* of the workflow). See `Guides/Core/process-flow.md` "Discussion-phase gate behavior".
- Discussion phases with a separate "draft is ready, please review" planned gate before the discussion begins — this duplicates the blocked/planned gate cycle. The drafting response itself should end with the blocked or planned gate per item state.

**Flow control integrity:**
- Any place where the guide says the agent waits for the supervisor but does not end with a `⏳ GATE:` line in the described runtime behavior.
- Walkthroughs or examples that show multi-turn back-and-forth at a gate but only display the `⏳ GATE:` line on the first turn. Every turn that ends with the agent still waiting on the supervisor should re-emit the gate line verbatim.
- Guide-defined ad-hoc `⏳ GATE:` lines that don't correspond to gates listed in the guide's `## Gates` section (the "fabricated gates" anti-pattern). Each `⏳ GATE:` template in the guide should trace back to a named gate.
- Any planned gate without its review artifact and explicit state/marker lifecycle. A documented Discussion-only model may have resolved D items at that gate; do not add a redundant pending phase marker.
- Any "remove 🟡" or "check the box" language that is not explicitly gated on advance intent or a documented workflow-specific exception. Search for `remove 🟡`, `Remove 🟡`, `check the box`, `mark `…` complete`, and `- [x]` walkthroughs, and verify each occurrence is tied either to a gate/advance-intent step or to an explicitly documented custom lifecycle.
- Any planned gate whose post-approval action/artifact change is unclear. Check marker clearing against that workflow's declared lifecycle; locally resolved Discussion items need not be cleared again.
- Flow/sequence descriptions where marker clearing appears before a STOP/gate (wrong order -- the STOP comes first, marker clearing happens on the subsequent advance intent unless a documented local exception applies).
- Examples or walkthroughs that show markers cleared without a preceding gate + advance intent step, unless the guide explicitly documents a narrower exception (for example, inline discussion items resolved during supervisor-approved discussion).
- `auto` sections that list gates bypassed by `auto` without labeling which gates are hard (not bypassed). If a guide has both soft and hard gates, the `## Gates` section should label the hard ones.
- Inline "Gate:" signposts that add mechanics not present in the `## Gates` section (acceptable to say "Gate: STOP"; not acceptable to add new rules about what happens at the gate unless they are already defined in the gate model).
- If the guide defines working-doc paths, any examples or artifact paths that place files directly under `skai/working-docs/<branch-path>/...` instead of `skai/working-docs/<branch-path>/<session-name>/...`.

## README Usage section conventions

The Usage section documents each **skill** (not sub-processes or internal maintenance workflows). Each entry follows this format:

1. Heading: `### <Human-readable name> (skill <skill-name>)` (no colon)
2. One-paragraph description of what the workflow does.
3. **Prerequisites:** what's needed before starting.
4. **Phases:** numbered list of the workflow's phases. Each phase is one line: `<number>. **<Phase name>.** <What happens>.`
   - If a phase has sub-steps, use a numbered sub-list under the phase.
   - If an entire phase is optional, mark it `(optional)` in the phase name.

Formatting rule:
- When referencing a file or directory path within this repo in `README.md`, use a markdown link so supervisors can click it in the browser (do not leave bare backticked paths).

Do not add entries for:
- Sub-processes that are invoked by other skills (e.g., the filing phase of the ticket-filing guide is invoked by the retro -- it appears as a phase within that entry, not as its own heading).
- Internal maintenance workflows (e.g., `internal/maintain-tickets.md` -- these belong in the Development guide section).
