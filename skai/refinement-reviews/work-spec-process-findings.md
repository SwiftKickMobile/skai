# Findings log — work-spec design and implementation

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|
| 2026-09-04 r1 | F1 Design reopen path missing | closed | Design Inputs now reopens in place, preserves decisions, updates API, and re-gates. |
| 2026-09-04 r1 | F2 Resolved D# could be overwritten | closed | Resolved items are immutable; superseding decisions receive new IDs. |
| 2026-09-04 r1 | F3 Work-spec resume could skip plan gate | closed | Every reopen re-audits, preserves only current checked evidence, and reuses gate 2. |
| 2026-09-04 r1 | F4 Handoffs defined only for human testing | closed | One general handoff task rule now runs all independent owned work before blocking. |
| 2026-09-04 r1 | F5 Gate 2 omitted completed design | closed | Gate summary and line now present Design plus implementation plan. |
| 2026-09-04 r1 | F6 Audit made runtime verification optional | closed | Audit routes all unit/runtime verification to the mandatory Testing rules. |
| 2026-09-04 r1 | F7a Evidence section undefined | closed | Removed redundant section; task Verification lines are canonical. |
| 2026-09-04 r1 | F7b Evidence output path inconsistent | closed | Failure output now uses the session-level `evidence/` directory. |
| 2026-09-04 r1 | F8 No faithful task example | closed | Added one filled image-provider task example. |
| 2026-09-04 r1 | F9 Bare next at blocked Discussion ambiguous | closed | Bare next resolves nothing; explicit all-proposals approval is defined. |
| 2026-09-04 r1 | F10 Conversation facts not persisted | closed | Conversation-only facts must be restated in durable design sections. |
| 2026-09-04 r1 | F11 Backfill scope and no-catalog guard lost | closed | Backfill blocks only when design needs it and is skipped as a workflow under `none`. |
| 2026-09-04 r1 | F12 Audit design-return rule misplaced | closed | Audit routes material design/API problems to the existing return before gate 2. |
| 2026-09-04 r1 | F13 API discussion example did not name API | closed | D1 now names `ImageProviding`. |
| 2026-09-04 r1 | F14 Unit-test task relationship ambiguous | closed | Dedicated, coherently batched test tasks follow covered production behavior. |
| 2026-09-04 r1 | F15 Modified API notation lacked an example | closed | Existing example now includes struck-old then new signature. |
| 2026-09-04 r1 | F16 Sibling workflows were not linked | closed | UI Map, requirements, and unit-testing mentions are direct relative links. |
| 2026-09-04 r1 | F17 Sibling gates conflicted with continuous run | closed | Continuous outer execution explicitly yields to sibling gates. |
| 2026-09-04 r1 | F18 Work-spec Inputs omitted required sources | closed | Inputs now list design, realized siblings, and key implementation sources. |
| 2026-09-04 r1 | Duplicate process-flow text across guides | rejected | Self-contained gate behavior is required at point of use; contextual pass retracted it. |
| 2026-09-04 r1 | Author-work-spec endpoint ambiguity | rejected | Legacy usage and current Plan endpoint agree; contextual pass retracted it. |
| 2026-09-04 r1 | Readiness screen duplicated | logged | Both skills need the short screen at entry; keep wording aligned rather than relocate. |
| 2026-09-04 r1 | Pending requirement IDs not qualified | logged | Sibling artifact path in Inputs preserves resolution; no observed failure. |
| 2026-09-04 r1 | Questions during continuous task could mutate code | logged | Rare path remains covered by explicit authority and blocker boundaries. |
| 2026-09-04 r1 | Slicing after unsliced impl file exists | logged | Rare transition; stable-ID reopen rules provide a safe route if encountered. |
| 2026-09-04 r1 | Generic and specific blocked-line tails differ | logged | Specific lines govern their cases; difference does not change behavior. |
| 2026-09-04 r2 | F1 Reopened design passed readiness before re-approval | closed | Reopen removes Implementation Design until gate 1 advances again. |
| 2026-09-04 r2 | F2 Design-return owner and gate ambiguous | closed | Implementation transfers to Design; Design owns reopen and its Discussion gate. |
| 2026-09-04 r2 | F3 Readiness wording differed by `complete` | logged | Cosmetic; both entry screens remain local and structural checks carry the behavior. |
| 2026-09-04 r2 | F4 Slice path writer ambiguous | closed | Design declares the path when a slice becomes current. |
| 2026-09-04 r2 | F5 Backfill should run without a catalog | rejected | Context pass confirmed Requirements Authoring under `none` is terminal; settled fallback stands. |
| 2026-09-04 r2 | F6 Greenfield task might edit Integration | closed | Write boundary makes Integration read-only; its owner receives a handoff. |
| 2026-09-04 r2 | F7 Deferrals could hide hard work | closed | Only supervisor-approved gate-2 deferrals are valid; later deferral is a scope change. |
| 2026-09-04 r2 | F8 Passing mid-list handoff said complete | closed | Passing result resumes next unchecked task and completes only at end. |
| 2026-09-04 r2 | F9 Goal and Inputs appeared optional | closed | Both are explicitly required. |
| 2026-09-04 r2 | F10 UI Map invocation might mutate before plan gate | rejected | Context pass confirmed sibling Plan mode produces planning artifacts and sibling-owned promotion, not feature code. |
| 2026-09-04 r2 | N1 Work-spec skills might edit canonical requirements | closed | General write boundaries make canon read/link-only. |
| 2026-09-04 r2 | N2 Evidence outcome could be vague | closed | Examples and rule require exit code or observed result. |
| 2026-09-04 r2 | Handoff gate templates live outside Gates | logged | Point-of-use templates are operable; no observed misuse warrants relocation. |
| 2026-09-04 r2 | Sibling T# namespace could collide | logged | Inputs carry artifact paths; qualify on use if a real collision appears. |
| 2026-09-04 r2 | Sibling change-id convention unstated | logged | Sibling workflows already stop safely when identity is unclear. |
| 2026-09-04 r2 | Question during continuous implementation might not pause | logged | Supervisor interjection pauses the turn; authority boundaries cover mutation. |
| 2026-09-04 r3 | F1 Checked task proof invalidation missing | closed | Stale or failed proof unchecks the task until fresh evidence passes. |
| 2026-09-04 r3 | F2 Later test proof conflicted with earlier task completion | closed | Earlier task names later test T# and is invalidated if that test fails. |
| 2026-09-04 r3 | F3 UI Map adoption trigger undefined | closed | Existing map triggers normal use; baseline adoption requires a material D#. |
| 2026-09-04 r3 | F4 UI Map Plan items mapping unclear | closed | Planned/handoff items become artifact-qualified outer tasks; sibling owns promotion. |
| 2026-09-04 r3 | F5 Bounded stop conflicted with fresh re-entry | closed | Fresh invocation re-audits; in-run requested boundary resumes without another audit. |
| 2026-09-04 r3 | F6 Design return could block before transfer | closed | Transfer occurs in the same response and ends at Design's Discussion gate. |
| 2026-09-04 r3 | F7 Removing Implementation Design on reopen | rejected | Settled structural-readiness decision; no demonstrated defect after contextual review. |
| 2026-09-04 r3 | F8 Gate presentations underspecified | closed | Gates name artifact/review; gate 2 covers design, tasks, verification, deferrals, handoffs. |
| 2026-09-04 r3 | F9 Plan default missing | closed | A work-spec/plan-only request means Plan. |
| 2026-09-04 r3 | F10 Incomplete design content had no readiness route | closed | Any design-content failure transfers to Work Spec Design. |
| 2026-09-04 r3 | F11 Question item content missing | closed | Question line and provisional proposal are both required. |
| 2026-09-04 r3 | F12 Exact heading rule missing | closed | Required headings are exact and status-free; Delivery Slices aligned. |
| 2026-09-04 r3 | F13 Plan/Build gate variants differed from spec | closed in spec | Design spec now records both settled gate variants. |
| 2026-09-04 r3 | F14 Process-flow text duplicated | rejected | Self-contained runtime mechanics are intentional and required at point of use. |
| 2026-09-04 r3 | F15 Closing sibling planned item contradicted ownership | closed | Narrow exception updates sibling item state exactly as its guide requires. |
| 2026-09-04 r3 | F16 Blocker resolution not persisted | closed | Non-design resolution is recorded on affected task before resume. |
| 2026-09-04 r3 | Handoff gate templates outside Gates | logged | Point-of-use lines remain operable; relocation has no observed behavioral benefit. |
| 2026-09-04 r3 | Sibling item IDs may collide | logged | Realizes now carries artifact path plus item ID. |
| 2026-09-04 r3 | Sibling change ID convention unstated | logged | Sibling workflows safely resolve or block on their own identity. |
| 2026-09-04 r3 | Tight-list typography implicit | logged | Existing examples are tight; no observed rendering failure. |
| 2026-09-04 r4 | F1 Sibling gate precedence absent | closed | While sibling active only its gate is emitted; outer resumes after completion. |
| 2026-09-04 r4 | F2 Required sibling could finish after dependent gate | closed | A sibling shaping design/API completes before the outer planned gate. |
| 2026-09-04 r4 | F3 Greenfield Integration trigger/recipient wrong | closed | Undefined commands trigger bootstrap; Integration update is supervisor install/update handoff. |
| 2026-09-04 r4 | F4 Implementation without design had no route | closed | Missing design routes through Work Spec Design and returns after completion. |
| 2026-09-04 r4 | F5 Task example omitted later test proof | closed | Existing example names T2 as automated proof. |
| 2026-09-04 r4 | F6 Non-final handoff conflicted with ordered execution | closed | Execution chooses first runnable owned task and skips pending handoffs until blocked. |
| 2026-09-04 r4 | F7 Readiness wording drift | closed | Design screen now matches structural presence check. |
| 2026-09-04 r4 | F8 Proposed blanket completion rerun | closed with lighter fix | Completion audits mutation relevance and reruns only invalidated checks. |
| 2026-09-04 r4 | F9 Bounded resume audit ambiguity | rejected | Current text already distinguishes fresh invocation from active-run boundary. |
| 2026-09-04 r4 | F10 Discussion empty state missing | closed | Added one sibling-style sentence, absent when items exist. |
| 2026-09-04 r4 | F11 Gate boilerplate duplicated | rejected | Self-contained runtime mechanics are intentional. |
| 2026-09-04 r4 | N1 UI Map scaffold markers not cleared | closed | Outer realization follows sibling checkbox and scaffold-marker lifecycle. |
| 2026-09-04 r4 | N2 Unit-test task Done when not repeated | logged | Generic Done when plus sibling completion already determines it. |
| 2026-09-04 r4 | N3 Pause-on-question rule lost | logged | Supervisor interjection and authority boundaries suffice. |
| 2026-09-04 r5 | F1 Sibling gate rule misplaced for audit | closed | Gate precedence moved to Implementation Gates. |
| 2026-09-04 r5 | F2 UI Map baseline adoption D# | rejected | Settled: baseline adoption is a material project decision. |
| 2026-09-04 r5 | F3 Requirements catalog presence vague | closed | Guard reads the Integration requirements declaration. |
| 2026-09-04 r5 | F4 Sibling could pre-empt initial Discussion gate | closed | Sibling invocation begins only after the initial draft reaches its gate. |
| 2026-09-04 r5 | F5 Active bounded stop vs fresh initiation implicit | closed | Active run resumes directly; re-initiation follows audit/gate entry. |
| 2026-09-04 r5 | F6 Ambiguous resume Plan/Build intent | logged | Plan gate prevents mutation either way; no stored mode added. |
| 2026-09-04 r5 | F7 Empty state interrupted Discussion template | closed | Empty state moved below contiguous template. |
| 2026-09-04 r5 | F8 `Always appears` contradicted pre-gate omission | closed | Requirement now applies to completed designs. |
| 2026-09-04 r5 | F9 Later test conflicted with task-check rule | closed | Named later test is explicitly a revocation condition. |
| 2026-09-04 r5 | F10 Integration install/update was unlinked | logged | Handoff action is clear; no extra runtime dependency needed. |
| 2026-09-04 r5 | F11 Reopen deletes Implementation Design | rejected | Settled presence-based readiness behavior; no reproduced defect. |
| 2026-09-04 r5 | F12 Audit says block where return says transfer | logged | Same-response transfer path is explicit and safe. |
| 2026-09-04 r5 | F13 Unready sibling route ambiguous | logged | Both safe branches reach supervisor; sibling owns readiness. |
| 2026-09-04 r5 | F14 API-specific D# template naming absent | closed | Placeholder now names affected API/type when applicable. |
| 2026-09-04 r5 | F15 D# resolution repeated | logged | Point-of-use restatement is consistent and small. |
| 2026-09-04 r5 | N1 Structural UI trigger vague | closed | Trigger names scene, route, or domain. |
| 2026-09-04 r5 | N2 Obligation coverage source set vague | closed | Checklist names API definitions, resolved D#s, and requirement IDs. |
| 2026-09-04 r5 | N3 Generic Design planned gate was unused | closed | Deleted; specific planned gate remains. |
| 2026-09-04 r5 | N4 Task example referenced absent T2 | closed | Same example now includes the dedicated test task. |
| 2026-09-04 r6 | F1 Zero-item draft could not sequence needed sibling | closed by supervisor decision | Required sibling may run during initial draft; its gate alone is active. |
| 2026-09-04 r6 | F2 Nonblocking backfill had no independent mechanism | closed by supervisor decision | Report for separate supervisor orchestration and continue without waiting. |
| 2026-09-04 r6 | F3 Baseline map D# could be forced | logged | Invocation no longer creates a synthetic D#; material adoption remains supervisor-reviewed. |
| 2026-09-04 r6 | F4 Return-to-Discussion procedure drift | closed | One canonical Design procedure owns all reopen paths. |
| 2026-09-04 r6 | F5 Reopen removes Implementation Design | rejected | Settled structural-readiness choice; rewrite reuses still-valid text. |
| 2026-09-04 r6 | F6 Greenfield Integration handoff ambiguous | closed by supervisor decision | Commands must be established before planning; missing values block, including greenfield. |
| 2026-09-04 r6 | F7 Unexpected blocker absent from artifact | closed | Blocked evidence bracket is written before waiting; resolution follows there. |
| 2026-09-04 r6 | F8 Miscellaneous low-impact ambiguities | logged | No concrete failure warranted more runtime text. |
| 2026-09-04 r6 | F9 Mid-run task-list mutation approval unclear | closed by supervisor decision | Mechanical add/split/reorder is autonomous; outcome/scope/verification changes re-gate. |
| 2026-09-04 r6 | F10 Design sibling gate placement | logged | Related-workflow point of use states precedence; no duplicate needed. |
| 2026-09-04 r7 | F1 Reopen depended on deleted Implementation Design text | closed | Regeneration now uses durable design sources only. |
| 2026-09-04 r7 | F2 UI Map Plan might change code before outer gate | rejected | Context confirmed sibling Plan mode writes planning artifacts, not feature code. |
| 2026-09-04 r7 | F3 Generic Implementation planned line competed with exact lines | closed | Deleted; exact Plan/Build/bounded lines remain. |
| 2026-09-04 r7 | F4 Design-only completion preceded Integration check | logged | Implementation entry check is the authority and safely blocks. |
| 2026-09-04 r7 | F5 Reopen reasons narrower than routes | logged | Canonical procedure degrades safely for incomplete designs. |
| 2026-09-04 r7 | F6 Design sibling gate precedence outside Gates | closed | Precedence moved under Gates; invocation timing retained under Related. |
| 2026-09-04 r7 | F7 Sibling handoff mechanically became outer handoff | closed | Outer disposition now follows outer ownership. |
| 2026-09-04 r7 | F8 Seeded unit tests could close unfinished | closed | Example requires no yellow test markers before completion. |
| 2026-09-04 r7 | F9 Use cases omitted from optional design list | logged | Design spec permits them; no observed omission warrants more runtime text. |
| 2026-09-04 r7 | F10 API documentation carry-forward unstated | logged | Exact API Realizes contract already covers it; no observed loss. |
| 2026-09-04 r8 | F1 Later slice lacked implementation-side trigger | closed | Non-current slice routes through Design before planning. |
| 2026-09-04 r8 | F2 Blocked-gate resumption unclear | closed | Both guides re-evaluate after resolution and emit the appropriate next gate. |
| 2026-09-04 r8 | F3 Additional review material omitted pre-gate | closed | First pass includes all gate-1 review material except Implementation Design. |
| 2026-09-04 r8 | F4 Blocking assumption/TODO undefined | closed | Wrongness that changes D#/API is blocking; other notes are nonblocking. |
| 2026-09-04 r8 | F5 No-catalog guide/spec mismatch | closed in spec | Spec aligned to settled no-catalog and supervisor-orchestration behavior. |
| 2026-09-04 r8 | F6 Feedback handling misplaced under return | closed | Moved to Discussion item lifecycle. |
| 2026-09-04 r8 | F7 Test example cited T1 as Realizes | closed | Removed cross-task Realizes citation; T1 remains later proof only. |
| 2026-09-04 r8 | F8 Sibling task-state write ownership | rejected | UI Map guide explicitly delegates checkbox and scaffold-marker lifecycle. |
| 2026-09-04 r8 | F9 Task-change rationale location unspecified | logged | Work spec remains auditable without another mandatory field. |
| 2026-09-04 r8 | F10 Targeted command might derive an undefined variant | logged | Existing Integration/evidence rules suffice; no command taxonomy added. |
| 2026-09-04 r8 | L1 Direct-answer behavior lost | closed | Supervisor questions are answered directly unless the answer is a material choice. |
| 2026-09-04 r8 | L2 Use cases omitted from design prose | closed | Added to optional supporting prose; no required section. |
| 2026-09-04 r9 | F1 Generic re-entry trigger list incomplete | logged | Canonical material reopen plus active-phase rules safely cover interruptions. |
| 2026-09-04 r9 | F2 Design readiness failure gate assertion | rejected | Context confirms Discussion names its blocked/planned cycle. |
| 2026-09-04 r9 | F3 Later-slice mechanics residual | logged | Existing later-slice reopen trigger and Design ownership converge safely. |
| 2026-09-04 r9 | F4 Non-material gate-2 design feedback is heavy | logged | Settled single reopen path avoids a second edit mechanism. |
| 2026-09-04 r9 | F5 Readiness criterion missing in Implementation | closed | Same blocking-assumption test now appears in both entry screens. |
| 2026-09-04 r9 | F6 Bulk proposal approval item scope unclear | closed | Explicitly covers Proposal, Tradeoff, and Question items at stated Proposal. |
| 2026-09-04 r9 | F7 Port backfill blocking unit vague | closed | Inline only when open D# or current-slice API cannot resolve without it. |
| 2026-09-04 r9 | F8 Evidence example used a reference placeholder | closed | Bracket now records literal command placeholder plus exit code. |
| 2026-09-04 r9 | F9 Artifact path versus verbatim gate | rejected | Path belongs in response body; exact gate remains last. |
| 2026-09-04 r9 | F10 Contract-edit ordering lost | closed | Propose exact change at gate and edit only after approval. |
| 2026-09-04 r9 | F11 Official-map target had no Design producer | closed by lightweight decision | Deleted routine conformance trigger; change package is sole trigger. |
| 2026-09-04 r10 | F1-F4 Re-entry and pre/post-gate edge interpretations | logged | Settled canonical reopen and materiality rules cover them without another path. |
| 2026-09-04 r10 | F5 Sibling timing allegedly violated settled order | rejected | Reviewer received one superseded prompt bullet; current guide matches supervisor-approved initial-draft invocation. |
| 2026-09-04 r10 | F7 Sibling handoff mechanically became outer handoff | closed | Deleted contradiction; outer ownership alone determines outer disposition. |
| 2026-09-04 r10 | F8 Blocking-assumption route | logged | Generic blocked gate and proposal-led drafting safely cover the rare path. |
| 2026-09-04 r10 | F9 Revocation rule repeated | rejected | Testing defines relation; implementation loop is required point-of-use restatement. |
| 2026-09-04 r10 | F10 Sibling-readiness route ambiguity | logged | Both branches stop safely and sibling guide owns resolution. |
| 2026-09-04 r10 | F11 Runtime gate boilerplate duplicated | rejected | Intentional self-containment required by house style. |
