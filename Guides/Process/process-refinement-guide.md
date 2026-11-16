Managed-By: skai
Managed-Id: guide.process-refinement
Managed-Source: Guides/Process/process-refinement-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-31

# Process Refinement Guide

Print `📖 SKAI guide: process-refinement-guide` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

How to change or repair a **refinement target** — the guide(s) that tell an agent how to carry out a process, whether or not they back a skill — through rounds of fresh review. You are the **refiner**: you draft changes, commission rounds, triage findings and apply fixes. The **reviewer** is fresh each round: it reads cold, finds defects, shapes fixes and edits nothing. The **supervisor** brings the problem and rules on escalations.

A fresh refiner reads this guide, the target's design spec and guides, and the latest report, if any.

## When to use this

For a guide change the supervisor routes through refinement — a new guide, new content, a change to existing rules — and when a review finds real problems in a guide. Whether a change goes through it is the supervisor's call.

**A pass.** For a change: add to the design spec what the change must say; draft it as a proposal, rewriting the affected text rather than adding beside it and deleting what the change makes obsolete; check the draft against the design spec yourself. A new guide is proposed in full. Round 1 assesses the proposal; you triage its verdict on the proposal (endorse, amend or reject) along with the findings, and apply the shape you settle on; later rounds review the applied text until the stop rule (*Rounds and stopping*). So a pass that applies a change has at least two rounds. A pass with no proposed change — a review of a guide as it stands, such as one driven by observed failures — starts with a round over the current text.

## The design spec is the standard

Every target has a **design spec** — a plan, requirements doc, or equivalent source of truth for what the target must do — at `skai/refinement-reviews/<target-name>-design.md`, beside its findings log, so a later pass finds both by name. Every finding and change is judged against it: a guide that contradicts it is a defect; a finding that asks for something it deliberately decided against is weighed against it, not accepted automatically. Size caps, when set, are recorded there. A target without a design spec can't be refined reliably — write one first.

## Records

**Refinement working document.** Each pass records its finding matrix, triage decisions, repair clusters, score table and closure table — plus, at the structured tier, invariants, the ownership table and impact maps — in `<target-name>-refinement.md`, placed per `Guides/Core/working-doc-conventions.md`. A trivial pass (a couple of clarity fixes) may keep its matrix in the conversation.

**Findings log.** One per target at `skai/refinement-reviews/<target-name>-findings.md`, committed, with no branch or session in the path, because a pass months later has to find it. It is not a working document: it spans every pass. One appended table:

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|

Start it at round 1 and append each round's dispositions before commissioning the next, or "already settled" is unknowable when you score. It is never shown to the reviewer — that would stop the review being cold; the settled decisions you extract from it go into the prompt's `{{SETTLED_DISPOSITIONS}}` slot. At triage, point re-raises to their prior disposition: skip a non-fix only if it still stands after considering recurrence; revisit a `closed` finding if its problem still reproduces. It is also the cross-pass memory the recurrence threshold (*Across passes*) depends on.

## Commissioning a round

Each round is a **cold review**: a fresh, independent session, on the supervisor's chosen model at its highest effort, reads the target's guide(s) and design spec with no prior context and critically assesses fidelity, completeness, clarity, internal consistency and conciseness. It is meant to be aggressive, not blunted to spare feelings. It returns findings, each with a fix shaped toward the best overall solution — refactoring existing text where that serves better than adding — and suggested wording, plus a verdict. Round 1 shapes the proposal the same way. The report covers the change, or the whole target if none; out-of-charter findings go in an appendix and are triaged like any other. A **scoped / empirical review** adds observed behavioral failures of the target through the template's optional slots; the reviewer still reads the whole guide set cold, and everything downstream applies unchanged.

Build each round's prompt from [`cold-review-prompt-template.md`](cold-review-prompt-template.md) and give a fresh session the prompt; it reads every named file and everything they or the proposed edits reference directly, except excluded files, the findings log always among them. The reviewer must **not** read this guide or the template — both are refiner-facing and would bias it — except that a review of either one has both as its target. Each round, refill the slots that move: what changed since the last round, the settled dispositions so far, the proposed edits (round 1 only) and the report charter.

**Prompt fidelity.** Use the template's "Copy/paste prompt" block *verbatim*: fill `{{SLOT}}` markers and delete whole inapplicable slot sections only — no rephrasing, preamble or target claims outside the slots. Diff the prompt against the template before handoff; the only differences should be slot fills and deletions. Prose drift hands the reviewer your unverified framing as premises, and findings come back biased toward what you already believed.

**When the findings are wrong, suspect the prompt.** Fidelity guards against a *biased* prompt; the other failure is an *under-specified* one, and its symptom names the slot: findings demanding content you deliberately placed elsewhere mean a missing `{{SCOPE}}`; a settled decision returning round after round calls for checking `{{SETTLED_DISPOSITIONS}}`. Fix missing or unclear slots and rerun; do not patch the guide to satisfy a mis-scoped critic.

## Triage before editing

Don't act on the review raw: you own a critical second pass. Start from the reviewer's suggested fix and wording; you decide the final wording, and record why when you depart from it. **Default to "no rule"** — most findings fail the codification bar or are already covered. Account for every finding, and classify each defect row once, before any edit:

- **accept** — a real defect that warrants a fix to the guide.
- **log only** — a valid observation that warrants no guide change. Record it in the findings log; don't change the guide.
- **reject** — fails to establish a live defect: guesswork, ignores ownership already clear in the docs, or posits a misuse the text doesn't support. Reasoning from the documents rather than from running something is *not* grounds to reject — that is the reviewer's `speculative` mark, and most of what a review of a process guide can offer.
- **supervisor decision** — a live defect whose likely fix adds *process weight* (a new gate, a mirror field, a checklist, a proof burden, extra validation, a wrapper, repeated re-approval) or drops valid content or examples, or cannot fit a cap. Not your call.

When a finding comes from an observed agent run whose session is still available, interview it read-only before classifying: what reasoning and cues produced the behavior, whether the controlling rule was ambiguous or overlooked, and what smallest change at an existing rule or the point of use would have prevented it. Its answer is evidence, not authority: judge it against the design spec, guide, transcript and artifacts. If the session is gone, record that; never substitute a fresh agent's guess.

**Codification check** — before accepting a new rule a review proposes on its own (a change the supervisor asked for needs no proof that its problem recurs), in order:

1. *Does an existing rule already cover this case?* Then sharpen it or add a ❌/✅ example to it — not a new rule.
2. *Single observation, or recurring?* A first sighting not already in the findings log is `log only`, a second in another case is considered, a third can be codified. This bar gates **codification** — minting rules from incidental observations. It never gates repairing a deterministic defect (a contradiction, a dangling reference, a design-spec requirement the text misses), or sharpening an existing rule against the observed failure a scoped review was chartered on — there the failure is the evidence. 
3. *Can one principle cover the class?* A third sibling rule means you missed the generalization.

This prevents premature rules, sibling rules, and new rules where the agent failed to apply an existing one.

**Stranded is not broken.** A gap on a rare path that violates no design-spec requirement and merely strands the operator, where the workflow already says to stop and escalate when the guide doesn't answer, is `log only`, whatever its severity, until the strand actually occurs. Repair at any likelihood is for text that teaches a wrong action: a misroute stated as mandatory, a false tool claim, a contradiction both of whose readings violate the spec.

**Supervisor decisions.** STOP before editing and present the tradeoff plainly: the real failure the reviewer is worried about; what already covers it, if anything; the smallest documentation-only fix and the heavier, control-oriented fix. For dropping valid content, also show why it adds no value and what tightening was tried; for a fix that cannot fit, also show its measured size, cap and options. Give a recommendation. Implement the heavy fix or drop the content only if the supervisor chooses it; record the ruling and don't reopen it in the pass.

**Design contradictions.** A finding that exposes a contradiction in the design itself, not just unclear wording, is not repaired directly. Frame it as a decision — the exact contradiction, the smallest decision that resolves it, the documents it ripples to — get the ruling, update the design spec, then repair the guide, before any cluster is patched. Content and clarity findings are fixed directly once triaged.

## Finding matrix

Before editing, organize the round into one table in the working document — **one row per defect, not per reported finding**:

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|

The last column is the churn guard: the adjacent semantics the fix must not disturb.

**Collapse before you count.** On applied text, first correct labels that plainly fail their tests in [`cold-review-prompt-template.md`](cold-review-prompt-template.md) § *Output* (`verified` with no command run or implementation read; `normal` where an unopposed rule makes `past-a-rule` first), noting each in the arithmetic line; otherwise the reviewer's labels stand. Then reported findings that are one defect become one row — the reviewer's root-cause section usually names these clusters. **The row copies the whole label set of its heaviest finding** — largest consequence × reachability × verification, ties broken by report order — never the strongest value on each axis separately: that builds a row no reviewer reported, and two findings worth 5 can collapse into one worth 20. Do this first: how finely a reviewer chopped its report is not a property of the document, and a score taken before collapsing measures the reviewer instead.

A finding that restates a logged defect is that defect: noise if a non-fix disposition still stands after considering recurrence; live and scored if an accepted fix has not resolved it, a failed closure included. Every reported finding keeps its mapping to a row, so the log receives all of them at closure.

**Score the round here** if it reviewed applied text — once every row is settled and before the first repair, from the reviewer's facts and your triage (see *Round score*). A proposal round is not scored.

**Before repairing:**

- **Consolidation trigger.** If your fix in one round becomes the finding in the next, stop patching: you are closing findings locally while the document drifts. Rewrite the affected step or sentence whole against the design spec; restructure only when the repeated findings span more than one step, grouping them by root cause — then review again. **If it happens twice**, the problem is your editing method, not the document: move to the structured tier.
- **Watch who the findings are about.** A round whose findings are mostly *your own last repairs* is measuring you, not the document. Count them each round: it is the clearest convergence signal you have, and when they are the majority, move the pass to the structured tier.

**Prefer, in this order:** remove wrong or duplicated text, or move a misplaced rule to where it is used · sharpen existing wording · add a ❌/✅ example to an existing rule, which teaches a distinction without inflating rule count · restate a rule at its point of use · last, a new rule, gate or required field.

## Repairing

- Group the settled proposal, if any, and accepted fixes into small clusters: an endorsed proposal is work even without findings.
- **Patch exactly one cluster, then STOP and write the self-check before the next.** Patching every finding at once produces shallow fixes that break adjacent behavior. Self-check: Did I contradict adjacent text in this file or a sibling guide? Leave a stale sentence teaching the old behavior? Move a rule away from where the agent needs it? Weaken an enforced rule into a suggestion?
- No opportunistic cleanup — leave what no finding needs, except tightening to meet a cap.
- A fix copied into a sibling guide outside the target joins the same round: the sibling's changed passage becomes part of the binding target, and the round stays in its score series. Name that passage in later prompts; the reviewer reads the whole sibling, but only the passage and what it references are binding.

**Size caps.** A cap is optional. When the design spec sets one, it binds every repair: state each fix's net size in the finding matrix and fill the template's size-cap slot as directed there. Meet it mainly by tighter writing — of the new and nearby text, or anywhere else in the document that can be improved. Removing wrong, duplicated or obsolete text is an ordinary fix; dropping valid content or examples is a last resort and a `supervisor decision`, argued on the grounds that it adds no value. A real fix that can't fit is a `supervisor decision`, never a silent overrun. Record the net size change at closure. When a change sets or revises a cap, propose it after triaging round 1 and before applying: measure the settled shape on a temporary copy, and give a table of before size, settled size, change, old cap and proposed cap: for a new guide, a little under the settled size; for an existing guide, the old cap (or, if it had none, its size before the change) plus the settled addition, trimmed a little. Once the supervisor approves, record it in the design spec; then, before applying, tighten the settled shape to fit, or escalate if it can't.

## Verify your repairs before the next review

**Never spend a review round on something a check could have caught.** After the clusters, measure each guide with `wc -c`, capped or not and whatever the reviewer measured, and run every applicable mechanical check before the next round, until the stop rule:

- **Check every command and tool claim against the tool's current code or documentation** — not just "does it parse": do its options exist, and does it do, output and exit the way the prose claims, a guard stopping when its input is missing? A guard that warns and returns success reads as safe and is not. Don't test the tool itself; its maintainers do.
- **After changing a tool, search the guide for every mention of it.** Prose about tooling goes stale silently; search rather than remember.

**A defect class that appears twice gets a script, not more care.** This is the automation counterpart of the codification threshold: the first occurrence is a fix, the second is evidence that hand-checking does not hold. Run the check before every handoff and extend it whenever it misses one. The signal you skipped this: a round whose findings are mostly mechanical defects in your own last repair — a review doing a linter's job.

## Rounds and stopping

- **Stop rule.** Only a fresh round over the current text can end a pass — never a round you repaired after. It ends when **(a)** the round's triaged findings leave nothing to apply in the binding review target (re-raises are answered by the findings log; findings outside the target route to their owning document), or **(b)** you present the remaining findings you argue should not be implemented as one ledger, per *Supervisor decisions*, and the supervisor approves — record that ruling in the findings log so ending by ruling is distinguishable from a clean round. A round of *misfired* findings is neither: fix the prompt and rerun.

### Round score

Score every round that reviewed applied text: an evidence-weighted estimate of what its live defects could still do to someone following the document. Lower is better within a series; 0 means nothing scored, not a clean guide. The reviewer never grades — it states three facts per finding, and the score is arithmetic on them:

**score = Σ over the matrix's live rows of consequence × reachability × verification**

| Consequence | Reachability | Verification |
|---|---|---|
| irreversible **20** · divergent **5** · cosmetic **2** | normal **×1.0** · off-normal **×0.75** · past-a-rule **×0.25** | verified **×1.0** · speculative **×0.5** |

**What counts.** A row scores when your triage says it is a live defect in the binding review target — any of its guides, or a sibling passage a copied fix joined, with what they reference — with no earlier non-fix disposition still holding, wherever the report printed it. Every other row is **noise**: counted beside the score and never added, so rejecting freely can't buy a clean round; three rejected findings that were one defect are one noise entry. A row belonging outside the target routes to its owner, and an open question is reported on its own; neither is counted.

Append to the working document each round (or beside an inline matrix):

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
|---|---|---|---|---|---|---|

`Total defects` sums the three consequence columns. Beneath it, the round's arithmetic on one line, naming each row by its findings:

> F01+F03+F06 one defect, heaviest F03, so the row is divergent · normal · verified = 5 · F02 round-2 closure did not hold, live again, irreversible · off-normal · speculative = 7.5 · F04 rejected, noise · F05 outside the binding target, routed to the schema doc · F07 open question, neither
>
> `| r3 | 12.5 | 2 | 1 | 1 | 0 | 1 |`

- **It is a monitor, never the stop criterion.**
- **Scores compare only within one series.** A series is fixed by what decides which findings can be raised and what they weigh: the scoring model, the files under review, the design spec and scope, the report charter, and any evidence the commission supplies. Change one, or start a different effort, and later rows are a separate series — label them, and don't compare across. Repairs stay in series, including a copied fix that adds a sibling guide; if a repair changes another series input, such as the scoring model, later rounds start a new series. Routine refreshes — a newly settled disposition, a note on what you just repaired — do not start a series.

## Closing the pass

In the working document, mark every finding `closed` / `downgraded` / `still open` / `rejected` / `deferred` / `logged` (`log only` at triage), each with one line of evidence. For `rejected` and `logged`, the evidence is the **rationale** — why it was declined — so later passes can assess re-raises and recurrence. A finding is not `closed` while its problem reproduces under other wording. A finding about a command, script or tool closes only when the guide's claim matches the tool's current code or documentation, failure handling included, never on a description of the fix.

Append every entry to the findings log, then hand the finished change to the supervisor for review.

## Scaling the ceremony

Three tiers; match the tier to the evidence, never heavier than it supports. Every tier triages, self-checks, checks mechanically, measures size and reviews until the stop rule is met; higher tiers add the safeguards below.

**Lightweight (default).** Everything above. A handful of clarity fixes needs nothing more.

**Structured.** When the consolidation trigger has fired twice, or a round's findings are mostly your own last repairs, add three things that fix *how you edit*, which more rounds cannot:

- **Invariants.** Name the properties a repair must not break, with stable IDs (`P1`, `P2`, …) in the working document, and **restate every accepted finding as an invariant violation before editing** — the move that turns a one-off fix into a class fix. If none fits, add one grounded in the design spec.
- **Canonical ownership.** Each rule has one home, and other surfaces point to it. Where a surface needs the rule restated — the reviewer's prompt, which can't read this guide — keep the restatement consistent with its home. Write a small table of *content → canonical owner → derivative surfaces*: drift between a guide, its template and a materialized copy is one of the highest-yield finding streams, and invisible from inside any one of them. A derivative copy generated once and never refreshed gets a mechanical sync check; an ownership rule nobody can verify silently rots.
- **Rule impact map.** Before editing, per accepted finding: the invariant violated, the owner of the rule you are changing, **every dependent that consumes or restates it — found by grep, not memory** — and what must not change. Edit the owner first, then re-check every dependent; the fix is finished when the search that found it returns a consistent document. **Sweep the class, not the instance**, and wider than the obvious form: a search over fenced code blocks misses the same defect in inline code spans.

**Full apparatus.** A dated worklog per pass, a numbered audit catalog with stable IDs, required stale-text sweeps, cold-reader simulations and explicit stop conditions consistent with the stop rule — for a structural repair spanning several guides, where a later reviewer must reconstruct exactly which checks ran.

## Across passes

For a target refined more than once over time:

**Recurrence threshold.** The codification check's count runs across passes, carried by the findings log; like the check, it never blocks fixing a deterministic defect, sharpening a rule against a scoped review's chartered failure, or a change the supervisor asked for.

**Periodic restructure.** Every several passes, refactor the guide for accumulated cruft — consolidate overlapping rules, remove dead text, reorganize by what is load-bearing. Bloat is fought retrospectively as well as at the entry point. It is a deliberate pass of its own, not folded into a normal one.

## Project Addendum

If `<active-project-root>/skai/addenda/process-refinement-guide-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
