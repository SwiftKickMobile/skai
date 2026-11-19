# Component configuration findings

Refiner-facing durable record. Standard: component-configuration-design.md.

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-10-10 | R1 F1 approval contradictions (standalone auto-apply / duplicate explicit-apply approval) | closed | Configure waits for explicit standalone apply; all3 Confirm sections accept the existing authorization; ordinary/unmanaged gates preserved. |
| 2026-10-10 | R1 F2 customized-only history summaries | closed | All3 state summaries, shared selection and update caller read the removal-aware shared contract every reconciliation. |
| 2026-10-10 | R1 F3 copied wrapper paths ignore actual checkout | closed | Shared Installed wrapper paths rule plus all3 skill-copy points substitute discovered root before stamping; Executed all3 stamped wrappers at Vendor tools/SKAI; all guide references exist, while the unmodified default-path negative control does not. |
| 2026-10-10 | R1 F4 untracked migration list overclaim | closed | Helper description now states tracking:false empty list does not replace adapter/changelog artifact checks. |
| 2026-10-10 | Legacy-only state helper boundary | logged | Existing path migration remains prerequisite; no new migration flow needed. |
| 2026-10-10 | Old Claude adapter-ID discovery timing | logged | Discovery remains read-only; planned ID merge must retain provenance until successful reconciliation. Rare wording tension doesn't add a new gate. |
| 2026-10-10 | R2 F1 already-approved removals conflict with mandatory policy | closed | Safe Operations approval owner and STOP condition now require a pause only when scoped approval is missing; unmanaged/Git/unrelated protection preserved. |
| 2026-10-10 | R2 F2 recorded SHA wrongly establishes actual HEAD | closed | Update guide reads actual rev-parse HEAD; installed version stays separate migration baseline. Recovery fixture covers drift. |
| 2026-10-10 | R2 F3 old Claude IDs mutate discovery/date evidence | closed | Discovery plans only; old dates/versions/history retained through baseline capture and conversion merged at verified success. Prior R1 tension resolved without new gate. |
| 2026-10-10 | R2 F4 global SHA borrowed from sole other adapter | closed | Failing regression reproduced Cursor→Codex misattribution; sole matching fallback retained, other/mixed adapter versions stay unknown.18 history tests pass, including foreign-date and malformed new-baseline guards. |
| 2026-10-10 | R2 schema-version numeric parity edge | accepted outside binding target | Native accepted1.0 while portable rejected; both-layer regression reproduced, native integer-type guard corrected; rebuilt21 and both-layer regression plus54 valid resolver comparisons pass. |
| 2026-10-10 | R3 F1 legacy state omitted by configure/selection/helper discovery | closed | Existing history owner now routes both entry points; helper safely reads local/shared/legacy, retaining canonical/local proposal destinations.21 history tests pass with legacy SHA/date, precedence, malformed and escape cases; no writes. Prior logged legacy-helper boundary superseded by this verified deterministic mismatch. |
| 2026-10-10 | R3 rollback filesystem failure tension | logged | Existing failure/escalation path applies; no observed stranded invocation or proportionate new gate established. |
| 2026-10-10 | R4 F1 config drift exceeds scoped approval | closed | Final verification resolves/reports drift, applies only already-authorized work, uses existing route for outside-scope work; stale config cannot receive success. No routine reapproval introduced. |
| 2026-10-10 | R4 F2 helper loses legacy Claude identity evidence | closed | Helper now explicitly defers all3 aliases with a clear error; shared helper documentation routes existing direct migration procedure.22 tests pass including source-byte preservation and independent other-adapter planning. |
| 2026-10-10 | R4 rollback failure / newly shared adapters under local authority | logged | No observed strand or mandatory wrong action; existing error/escalation route applies. No new proof burden or merged-state authority introduced. |
| 2026-10-10 | R5 final fresh review | clean — pass closed | No actionable findings; all required scenarios and tooling source claims coherent. Score0. Native/bundled parity,22 history tests, all3 installer fixtures and Git-clone packaging checks passed independently. No post-review binding edits. |
| 2026-10-10 | R5 unavailable old stored runbook tension | logged | No actual legacy state sample established the strand; existing stop/escalation covers unavailable required inputs. No new routing rule warranted. |
| 2026-11-18 r1 (proposal) | F3 The move would take a shared default `skai/` whole; `skai` set explicitly reported as a change | accepted | Design wording narrowed to what the setting covers; app compares effective folders |
| 2026-11-18 r1 (proposal) | F4 Location gate had no advance, revision, failure or completion path | accepted | Applied; held through round 9 |
| 2026-11-18 r1 (proposal) | F5 A standalone Save loses the old locations a later apply needs | supervisor decision | Ruled: the old locations come from the last committed `skai/config.json` in source control |
| 2026-11-18 r1 (proposal) | F6 Hidden User tab left override badges and Save availability misdescribed | accepted | Applied; held through round 9 |
| 2026-11-18 r1 (proposal) | F7 "Reconciliation does not read them" was false | accepted | Applied; held through round 9 |
| 2026-11-18 r1 (proposal) | F8 New components keyed on file presence | accepted | Applied; held through round 9 |
| 2026-11-18 r2 | F2 Location proposal deferred behind a failed reconciliation | closed | Proposed after reconciliation whether or not it succeeded |
| 2026-11-18 r2 | F3 "Made or declined" completed with setting and files disagreeing | closed | Completion on the gate's resolution; a declined change is reported as a mismatch |
| 2026-11-18 r2 | F4 Apply without event had no folder comparison | closed | Unset read as `skai`; only differing folders are changes |
| 2026-11-18 r2 | F5 Same-named folder already at the destination | closed | The proposal names it instead of moving onto it |
| 2026-11-18 r2 | F6 A Save error after the config write leaves config saved, Cancel then reports cancelled | logged | Existing app behavior since the decline flow, untouched by this change; no observed occurrence |
| 2026-11-18 r3 | F2 Location gate had no decline outcome | closed | Gate offers approve, decline or revise; a decline reconciles without the changes |
| 2026-11-18 r3 | F3 Installer blocker vs location proposal had no order | closed | Proposal and gate come before reconciliation |
| 2026-11-18 r3 | F4 Covered folder missing at the old location | closed | The proposal names moves that cannot be made as stated |
| 2026-11-18 r3 | F5 Relative links from moved files | logged | A setting's folders move together; the supervisor reviews the named edits |
| 2026-11-18 r5 | F1 "config.local.json still overrides it" read as covering locations | closed | "overrides its component selection" |
| 2026-11-18 r6 | F1 Location step's proposal unconditional | closed | "When a location changed" |
| 2026-11-18 r7 | F1 Explicit apply skips Launch's discovery paragraph | logged | The branch and its order predate this change; no observed misuse |
| 2026-11-18 r7 | F4 Blank location values read as the default; guide said "unset" | closed | "blank or absent" |
| 2026-11-18 r8 | F1 Explicit apply skips Launch's checkout resolution (re-raise of r7 F1) | closed | "resolve the host and checkout as in Launch" |
| 2026-11-18 r8 | F2 "Checkboxes represent desired components" described the screen | closed | Deleted |
| 2026-11-18 r9 | "Absent" read as a missing committed config | rejected | With no committed config the old locations were the defaults: determined, so no block |

Pass 2026-11-18 (skai#144, shared with artifact-location) converged by a clean round: r9 scored 0. Series: r2 11.25 · r3 10.625 · r4 13.125 · r5 8.75 · r6 11.25 · r7 11.25 · r8 2.875 · r9 0. `configure-skai.md` 10,939 → 10,585 (cap 10,600).
