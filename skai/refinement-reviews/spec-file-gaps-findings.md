# Spec File Gaps — Findings Log

Earlier series on this guide (FN, GO, 2026-10-24) are logged in `design-process-findings.md`.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-11-09 | Routed: "Read when raising a gap" narrower than known-gaps rule 3 | logged | Older text matching the spec ("read when a gap is raised"); outside this change |
| 2026-11-09 | Routed: marker-less notes for inherited bare gaps | closed — moot | Known-gaps 2026-11-09: a bare upstream gap's part is omitted, unmarked |
| 2026-11-09 r1 | F1 Owner sentence (#118 edit) chains two colons, has no route to the link form `change-requests.md` gives, and leaves "there" bound to "elsewhere" | closed | Reviewer's text: identity first ("…not inherited; questions stay only there."), then "Bare here, or [linked](change-requests.md) elsewhere (`[D27][001 D27]`)." 1,845 / 1,850 |
| 2026-11-09 r1 | F2 "define under its item" has no parallel for design change-list entries; a definition under the Discussion item renders nothing (`design-tool.py:84-91`) | logged | Older text outside the #118 change; real and verified — follow-up for the design guides' pass or a ticket |
| 2026-11-09 r1 | Open: a request copying a base file without relinking bare owners can pass falsely when it has its own same-numbered gap | logged | `change-requests.md` 5.1 owns it (tool gap) |
| 2026-11-09 r1 | Open: labels by change id do not name the type for sibling-type packages | logged | Already logged under `change-requests.md` |
| 2026-11-09 r1 | Open: `check-changes` also requires a linked owner's target to hold the item (stricter than spec) | logged | Reasonable sanity check; no wrong action taught |
| 2026-11-09 r2 | F1 r1's bare "[linked]" route says nothing of the label definition; design pages render an undefined label as this artifact's own item | closed | "Bare here; elsewhere [linked, label defined](change-requests.md) (…)" (reviewer's text) |
| 2026-11-09 r2 | F2 "where raised, not inherited" reads as "do not mark inherited gaps" | closed | "not where inherited" |
| 2026-11-09 r2 | F5 the example labels a request (`001`), not a package by change id | logged | Cosmetic; valid once defined; `change-requests.md` 4.1 uses the same form |
| 2026-11-09 r2 | F3 "unpaired ones fail" binds to footnotes, not unmarked open gaps | logged | Older text outside the change; the tool fails both |
| 2026-11-09 r2 | F4 when a marker-less note is written is not stated | logged | Older text; the two marker-less clauses were kept apart on purpose (2026-10-24) |
| 2026-11-09 r2 | Funding trims | applied | Lines 13, 26, 30 reworded (−14); "; neither check runs" (FN r2) and "own" (GO r2) kept. 1,849 / 1,850 |
| 2026-11-10 r3 | F1 "elsewhere" does not say the base is cited by link (spec: "the base's included"); a request's copied files read the base's items as "here" | closed | "Bare here; elsewhere, base too, [linked, label defined](…)" (reviewer's text) |
| 2026-11-10 r3 | F2 r2's funding trim "The gaps tile counts and filters footnoted items" omits gap items | closed | "…counts and filters gap items and footnoted ones." |
| 2026-11-10 r3 | F3 nothing says scope-word owners copied from an older base are retired | logged | Cosmetic, off-normal; tools read the old form by ruling |
| 2026-11-10 r3 | Cap | raised | Supervisor: 1,850 → 1,900; trims that fit 1,850 dropped "filters" or the spec's "draft". No funding trims applied |
| 2026-11-10 r4 | F1 "Bare here" reads as "in this file, write it bare" (r1 wording); a bare base owner can silently pair with a same-numbered own gap | closed | "Raised here, bare; elsewhere, base too, …" (reviewer's text) |
| 2026-11-10 r4 | F2 "footnoted ones" (r3 wording) binds to "gap items" | closed | "footnoted cards" |
| 2026-11-10 r4 | F3 the guide does not say a footnote makes an existing requirement modified | logged | Older text; settled by design; the tool's message names the missing change entry |
| 2026-11-10 r4 | Open: header date stale | closed | `Managed-Updated-At: 2026-11-10` |
| 2026-11-10 r5 | F3 "Raised here" leans on "base too" to pin "here" to the authoring artifact | logged | Cosmetic as written; keep "base too" |
| 2026-11-10 r5 | F1 `validate` "placement" checks the definition, not the marker | logged | Older text outside the change; no downstream effect |
| 2026-11-10 r5 | F2 a canon footnote in an unheld file is a note, not a failure | logged | Older text outside the change; the tool states the severity |
| 2026-11-10 r5 | Open: the prompt's settled disposition "defined once per file, shown under every entry" is the design renderer's; spec drafts need a definition under each item | logged | Prompt wording, not the guide; the guide agrees with the tools. Fix the disposition's wording in later prompts |
| 2026-11-10 | Pass closed | closed | Supervisor, 2026-11-10, after r5 (score 1, nothing accept-grade): end the pass with the unimplemented ledger logged (r2 F5, r3 F3, r5 F3), stop rule (b). `spec-file-gaps.md` 1,882 / 1,900 |
