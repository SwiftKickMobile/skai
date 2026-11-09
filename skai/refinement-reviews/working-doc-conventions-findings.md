# Working Document Conventions — Findings Log

Target: `Guides/Core/working-doc-conventions.md`, with the release entry's migration, work spec implementation's evidence paragraph and the integration template's Scratch root field as the scoped review surface. Design spec: `working-doc-conventions-design.md` (backfilled 2026-10-21).

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-21 r1 | F1 creation step's unconditional `mkdir` and the work-spec formula compete with the package-placement rule | closed | step 3 creates the folder chosen in steps 1–2; "a work spec serves a change, not a package" in the guide and the release entry |
| 2026-10-21 r1 | F2+F4+F5 migration completion defined by folder shape and `git status` (discovery skips top-level `working-docs/`; link repair omits relative links inside moved documents; `git status` is not an inventory) | closed | discovery covers top-level folders and skai's checkout; the list is the inventory; links inside moved documents repaired; verification against the inventory |
| 2026-10-21 r1 | F3 `git mv` cannot move a tracked file into another repository | closed | step 4: copy then remove, each side reviewed in its own repository |
| 2026-10-21 r1 | Open: partially migrated folder identity on restart; collisions have no merge procedure | logged | escalation route and collision stop cover both; intended |
| 2026-10-21 r2 | F1+F2 migration's unit of work: output exclusion after approval and move; "second discovery finds nothing" fails on valid nested sessions | closed | classification of documents, output and already-placed items before one approval stop; verification against the inventory |
| 2026-10-21 r2 | F3 scratch rule covered shipped build products (verified against `build.sh`) | closed | rule narrowed to output captured to verify a build or test; a build's deliverable goes where its guide says (guide, Scratch root field, release line) |
| 2026-10-21 r3 | F1+F2 "already placed" decided by path, exempting contents from classification and conflicting with link repair | closed | discovery lists current-looking folders as entries; "already placed" assigned after the association test; verification says "not relocated" and allows step 5's link repair |
| 2026-10-21 r3 | F3 interrupted cross-repository copy needs the supervisor on rerun | logged | collision stop protects the work; no recurrence; automatic duplicate removal would be disproportionate |
| 2026-10-21 r3 | A1 template's Test artifacts example teaches in-repository results | closed (outside binding passages) | example rewritten; the r3 wording introduced a copy-from-`build/` step, fixed in r4 |
| 2026-10-21 r4 | F1 discovery scope narrower than classification scope: package-level `evidence/` build captures never enter the inventory | closed | discovery lists every place the old guides sent captured output; promotion check output stays |
| 2026-10-21 r4 | Open: restart after relocation but before link repair relies on the kept inventory | logged | missing approval or inventory escalates; no migration journal without a demonstrated strand |
| 2026-10-21 r4 | Reviewer note: skill dispatch loaded the refiner-facing process-refinement guide before the exclusion was noticed | logged | for the skai#90 procedure: host skills can fire inside a Codex review when a guide name appears in the prompt |
| 2026-10-21 r5 | F1 restates r3's interrupted-copy case | logged | same rationale |
| 2026-10-21 r5 | Open: step 6 does not repeat link verification | logged | step 5 already requires it |
| 2026-10-21 r5 | Terminal round: no new live findings | converged | stop rule (a), clean round over the current text |
| 2026-10-21 post-r5 (supervisor) | skai's own working documents must not be committed: the library ships whole to every host; refinement records are tracked | closed | G15: skai's `.gitignore` ignores `skai/working-docs/`; refinement working documents moved to `skai/refinement-reviews/<target>-refinement.md`; maintenance guide and release entry say so; no guide sentence added |
| 2026-10-31 (supervisor) | Session working documents under `skai/working-docs/` are not committed; package working documents stay committed | closed | Requirement 3 amended; guide, three adapter runbooks, `component-selection.md`, README and release entry updated |
