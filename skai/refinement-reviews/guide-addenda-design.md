# Project guide addenda — design

## Requested capability

Each SKAI guide supports a project-owned, optional freeform Markdown addendum. It can add rules or explicitly override that guide's procedure/conventions. SKAI skills are building blocks composed by a project; this does not introduce a SKAI-wide workflow.

The base guide owns its dependencies, including reading Integration whenever operational settings are needed. Addendum authors do not have to restate or reference those dependencies. Integration remains the global settings document; no global configuration format migration is requested.

## Loading contract

- Read the complete base guide, then its addendum if present, before applying the guide or executing a procedure. A short entry cue routes to a footer containing the protocol and exact lookup path.
- Use `skai/addenda/<guide-name>-addendum.md` under the active project root as the initial entry point. It may reference shared addenda in another repository; a shared-context repository can itself be the active project. Use the published guide filename stem initially; preserve this lookup name across future renames or explicitly migrate it. Names must be unambiguous.
- Read required shared addenda before applying project-local additions/overrides; resolve relative links from their containing file. Report each successfully loaded file. Missing/unreadable required references block. This freeform composition needs no addendum inventory.
- An absent project entry is normal. Unknown root, failed existence lookup or unreadable existing file blocks instead of implying absence.
- Report an emoji-prefixed receipt with the resolved path and loaded/absent status. It introduces no approval gate and precedes any required trailing GATE line. Loading and reporting remain required even when the addendum replaces the guide's procedure.
- Apply addendum additions and overrides instead of conflicting guide defaults. Current task instructions and project-wide policies remain authoritative; unexpected conflicts there use existing escalation. A supported guide override does not require repeated permission merely because it differs from SKAI's guide text.
- Load only guides needed for the selected building block; every such guide checks its own addendum, including references and handoffs after rollout. The addendum applies to its own guide, not arbitrary other guides.
- No required headings, frontmatter, schema or managed header. Project owners control the content; SKAI installers must not create, overwrite, conform or delete addenda. No mandatory empty folders/files.

## Prototype and rollout

Prototype Product Specs Promotion with its thin wrapper and the installed instruction-block exception. Other guides' addendum support is not yet assumed during prototype review. Review the loading/precedence/receipt contract in this concrete guide; unrelated requirements semantics and earlier change-package work are outside this review.

After refinement, promote the exact settled entry/footer text into a maintainer house-style reference and apply it to all 35 registered guide assets: 33 files under Guides plus the two internal guide-runbooks. Non-guide installer runbooks and maintainer-only references are not separate skill building blocks; their ownership/update instructions must preserve addenda. No new runtime loader or guide dependency is requested.

## Constraints and acceptance

- Current guide behavior remains the default when no addendum exists; no new review gate or progress field.
- Only the thin wrapper routes to the canonical guide; it must not restate procedure restrictions that contradict overrides or current recovery.
- Keep the existing 11,000-word cap across the four product spec guides. Initial total is 10,608; additions during rollout may need compensating trims.
- Verify no-addendum, added-rule, explicit-override, unreadable/unknown-root and root-project/task conflict paths. The receipt must be truthful and before work, while existing gate placement is preserved.
- This is instruction-based loading and acknowledgement, not a technical guarantee that an agent obeys the text. Do not add hooks, mandatory user schemas or proof fields to address that limitation.
- Preserve current asset IDs, addendum content and released history (`CHANGELOG.md` and `Releases/`). No commit, push, release, host migration or issue operation is requested.

## Shared-context follow-up — 2026-10-09

Supervisor chose a conventional project addendum that points to shared content and may add local rules. The README provides optional copyable shared-first/local-second prose. This supersedes the prototype's categorical shared-repository exclusion; its review remains historical, not a new review of this clarification.

## Footer Rewrite — 2026-10-13

Supervisor decision. The boilerplate every guide carries (the entry cue after the title and the
`## Project addendum` footer) is too long and says things that are not needed. What it must achieve,
and nothing more:

1. The agent reads the addendum for guide X, if one exists, after reading guide X in full, and
   treats it as part of the guide. The addendum wins any conflict.
2. The agent acknowledges the guide was read by printing a "guide" line.
3. The agent acknowledges the addendum was read by printing an indented "addendum" line under it.
4. If there is no addendum, there is no "addendum" line.
5. The lines are printed immediately: the guide line on opening the guide, from the entry cue at
   its top, before anything else; the addendum line the moment the addendum is read. "Before work" is not enough: agents have deferred the line behind other reading
   (supervisor, 2026-10-14).

**Placement (supervisor, 2026-10-14):** after seventeen cold runs and five agent interviews, the
guide line moved from the footer to the entry cue at the top of the guide ("Print `- 📖 SKAI guide:
<name>` now, as a line of its own. Read this guide fully, then follow Project Addendum."); the footer
keeps only the addendum check and its nested line. The agent instruction block says the lines are
printed when the guide says to and, when an agent's only output is a final report, first in it.
Interviewed agents had read the footer but took it as "find the addendum", not as required output,
and "now" at the end of a long guide read as a note.

**Bullet dropped (supervisor, 2026-10-14):** the guide line is printed without a bullet
(`📖 SKAI guide: <name>`), matching gate lines; the addendum line keeps its bullet and is indented
two spaces under it (`  - 📎 Addendum loaded`). A bullet under a plain line still renders offset from
it, so the parent bullet was carrying nothing.

**Headroom (supervisor, 2026-10-14):** if testing shows the shortened footer is not effective, one
more sentence may be added. No more than that without a new decision.

**Size budget:** the footer at most half its current length (118 words → 59 words or fewer), the
entry cue no longer than today's. Headings in Title Case. Anything in the current text that these
four goals do not require is a candidate for deletion; the cold reviewer proposes the replacement
wording. Earlier settled points stand where the goals do not touch them: the lookup path
`skai/addenda/<guide-name>-addendum.md`, the shared-context entry convention, no schema, installers
never touch addenda, the receipt is not a gate.

**Dropped (supervisor, 2026-10-13):** the failure line and stop (unknown root, unreadable file,
"never infer absence") are over-engineering. No addendum found means no addendum line; nothing
else is reported about the lookup.
