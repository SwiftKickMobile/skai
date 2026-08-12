Managed-By: skai
Managed-Id: guide.skill-refinement
Managed-Source: Guides/Process/skill-refinement-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-11

# Skill Refinement Guide

A process for refining a skill — its guide document(s) — based on a cold review. Applies to any skill under development.

A fresh session running this should read: this guide, the skill's design spec, the skill guide(s) under refinement, and the cold-review findings.

## When to use this

Use it when a cold review finds real problems in a skill's guide(s). Trivial copy edits (a typo, a broken link) don't need it — just fix them. Anything touching workflow, control-flow semantics, document structure, or fidelity to the skill's design spec does.

## The cold review

The input is a **cold review**: a fresh, independent session that reads the skill's guide(s) and its design spec with no prior context and critically assesses fidelity, completeness, clarity, internal consistency, and conciseness. It produces findings — each with a severity and a suggested fix — and a verdict. The review is meant to be aggressive; it is not blunted to spare feelings.

To launch one, fill in the slots in [`cold-review-prompt-template.md`](cold-review-prompt-template.md) and hand the filled prompt to a fresh session. That reviewer must **not** read this guide or the template (both are refiner-facing and would bias the review); give it only the filled prompt and the files it names.

**When the findings are wrong, suspect the prompt.** The fidelity check below guards against a prompt that is *biased*; the complementary failure is a prompt that is *under-specified*. If rounds stop converging, the defect is in the prompt, and the symptom tells you which slot: findings demanding content you deliberately placed in another document mean a missing `{{SCOPE}}`; the same disposition returning round after round means a missing `{{SETTLED_DISPOSITIONS}}`. Revise the prompt and rerun; do not patch the guide to satisfy a mis-scoped critic.

**Prompt-fidelity check before handoff.** Use the template's "Copy/paste prompt" block *verbatim* — fill `{{SLOT}}` markers and delete entire inapplicable slot sections only. Do not rephrase the surrounding prose, add a preamble, or assert facts about the review target in the prompt. Diff your filled prompt against the template; the only differences should be slot replacements and slot-section deletions. Prose drift in the prompt taints the review: the cold reviewer inherits the maintainer's unverified framing as premises, and findings come back biased toward what the maintainer already believed.

## The design spec is the standard

Every skill should have a **design spec** — a plan, requirements doc, or equivalent source-of-truth describing what the skill is supposed to do. That doc is the standard each finding is judged against. A guide that contradicts the spec is a defect; a finding that asks for something the spec deliberately decided against is weighed against the spec, not accepted automatically. If a skill has no design spec, refining it reliably is hard — close that gap first.

## The refinement working document

A refinement pass records its work in a **refinement working document**: the finding matrix, the triage decisions, the repair clusters, and the closure table — plus, at the structured tier (see *Scaling the ceremony*), the invariants, the canonical-ownership table, and each finding's rule impact map. It is a working document — create it following `Guides/Core/working-doc-conventions.md`, placed under `skai/working-docs/<branch-path>/<session-name>/`, named `<skill-name>-refinement.md`. This is the same logic the work-spec creation guide uses for its plan and work-spec documents, and the UI Map implementation guide uses for its implementation working document: process artifacts are working docs, kept out of the skill's own committed files.

A trivial pass — a couple of clarity fixes — may skip the persisted document and keep the matrix inline in the conversation. Anything beyond that gets the working document.

## The coverage map

Across refinement passes on the same skill, a **coverage map** records every finding and its disposition. It is a durable working document under `skai/working-docs/<branch-path>/<session-name>/`, named `<skill-name>-coverage.md`. Each pass's closure entries append to it.

The map itself is never shown to the cold reviewer — it is refiner-facing and would stop the review being cold. What *is* shown is the short list of settled decisions extracted from it, via the prompt's `{{SETTLED_DISPOSITIONS}}` slot. Keeping those two distinct is what lets the review stay fresh while still not relitigating.

Format — a single appended table:

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|

The map is consulted at *triage* (not by the cold reviewer — a cold review must remain fresh):

- When a new finding matches one already in the map, do not relitigate. If it restates a `rejected` one, refer back to the prior disposition and skip. If it restates a `closed` one with the same surface, the prior fix did not hold and the closure must be revisited.
- The map provides the cross-pass memory the recurrence threshold (see Across passes) depends on — without it, every pass treats every finding as a first sighting.

## Triage before editing

A cold review is intentionally aggressive — do not blunt it, but do not act on it raw. The refining agent owns a critical second pass. **Default to "no rule"** — most findings either fail to meet the codification bar or are already covered by existing rules. Classify every finding before any edit:

When a finding comes from an observed agent run, interview the original agent before classifying it when that session is available. Resume it read-only and ask what reasoning and cues produced the behavior, whether the controlling rule was ambiguous or overlooked, and what smallest existing-rule or point-of-use change would have prevented the mistake. Treat the explanation as diagnostic evidence, not authority: judge the finding against the design spec, guide, transcript, and artifacts. If the original session is unavailable, record that limitation instead of substituting a fresh agent's guess.

- **accept** — a real defect that warrants a fix to the guide.
- **log only** — valid observation that does not meet the codification bar (see below). Record it in the coverage map; do not change the guide.
- **reject** — speculative, ignores ownership already clear in the docs, or treats a hypothetical misuse as a normal-use failure.
- **human decision** — the finding may be valid, but the likely fix adds *process weight*: a new gate, a mirror/duplicate field, a checklist, a proof burden, extra validation, a wrapper, repeated re-approval. Not the refining agent's call.

**Codification check** — before classifying a finding as `accept`, work through this in order:

1. *Does an existing rule already cover this case?* If yes, the fix is sharpening that rule or adding a ❌/✅ example to it — not a new rule.
2. *Single observation, or recurring across cases?* If single (and not already in the coverage map from a prior pass), classify as `log only` — record it; codify only on recurrence.
3. *Can one principle cover the class, or is the fix per-instance?* If you find yourself adding a third sibling rule, you missed the generalization — look for the principle.

Only when all three pass does adding a new rule fit. The failure mode this prevents: codifying from a single observation, adding sibling rules instead of generalizing, and writing new rules when the real issue is a rule the agent failed to apply.

## The `human decision` rule

For every `human decision` finding, STOP before editing and present the tradeoff plainly:

- the real failure the reviewer is worried about
- what existing rule or artifact already covers it, if anything
- the smallest documentation-only fix
- the heavier, control-oriented fix
- a recommendation

Do not implement the heavy fix unless the human explicitly chooses it. Record the decision; don't re-litigate it in the same pass.

## Finding matrix

Before editing, organize every finding into one table in the refinement working document:

| Finding | Triage | Touches (spec § + skill doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|

The last column is the churn guard — name the adjacent semantics the fix must not disturb.

**Prefer examples over rules.** When the minimal fix is to teach a distinction, add a ❌/✅ worked example to an existing rule rather than write a new rule. Examples teach without inflating rule count.

## Architecture vs. content

If a finding exposes a genuine *design* contradiction — not just unclear guide wording — do not repair it directly. Frame it as a decision topic:

- the exact contradiction
- the minimum decision that resolves it
- what downstream docs the decision would ripple to

Discuss it, get a decision, update the skill's design spec, then repair the guide. Pure content/clarity findings are lighter — fix them directly once triaged.

## Repairing

- Group accepted findings into small clusters of related fixes.
- **Patch exactly one cluster, then STOP and run the self-check below in writing before touching the next cluster.** Do not batch several clusters into a single edit pass — patching every finding at once is the failure mode this prevents: it produces shallow fixes that break adjacent behavior. (Architecture findings are resolved and the spec updated *before* any cluster is patched — see above.)
- Do not fold opportunistic cleanup into a repair — if it isn't needed to close a finding, leave it.
- After each cluster, self-check (record the result before proceeding): Did I contradict adjacent text in the same file or a sibling guide? Did I leave a stale sentence teaching the old behavior? Did I move a rule away from the point where the agent needs it? Did I weaken an enforced rule into a suggestion?

## Verify your repairs before the next review

**A review round must never be spent on something a check could have caught.** It is minutes of expensive reasoning; a script is a second and never forgets a case. Before handing the guide back for another round:

- **Run everything the guide tells an operator to run.** Not just "does it parse" — does it exit the way the prose claims, and does a guard actually stop when its input is missing? A guard that prints a warning and returns success reads as safe and is not.
- **Re-read the implementation behind every claim you changed.** If the guide says a tool enforces something, confirm it still does.
- **After changing a tool, search the guide for every mention of it.** Prose that describes tooling goes stale silently — the guide keeps promising what the tool stopped doing. Search; do not rely on remembering where you wrote it.

**A defect class that appears twice gets a script, not more care.** This is the automation counterpart of the codification threshold: the first occurrence is a fix, the second is evidence that hand-checking does not hold, and resolving to be more careful has a poor track record against it. Write the check, run it before every handoff, and extend it whenever it misses one.

The signal you skipped this: a round whose findings are mostly mechanical defects in your own last repair. That is a review doing a linter's job, and it crowds out the judgment work only a fresh reader can do.

## Closing the pass

In the refinement working document, mark every finding `closed` / `downgraded` / `still open` / `rejected` / `deferred` / `logged`, each with one line of evidence. For `rejected` and `logged` entries, that evidence must be the **rationale** — *why* the finding was declined or didn't meet the bar — not merely the disposition: these are exactly what a later cold review will re-raise, and the recorded rationale is what lets the next pass refer back and skip instead of relitigating. `logged` means the finding was classified `log only` at triage and recorded in the coverage map without a guide change. A finding is not `closed` if the underlying problem still reproduces under different wording. And a finding about a command, script, or tool behavior cannot be closed on the strength of a description of the fix — run it, including its failure branch, and record what you observed. Closing on intent is how a bug survives its own repair: three closures in one refinement effort were recorded against fixes that did not work, and each one then suppressed the finding when a later round raised it again.

Append every entry to the skill's coverage map at this step, so future passes have the cross-pass record.

## Iterated review

Sometimes one refinement effort runs several review → repair rounds back-to-back on the same document, rather than passes separated in time. Four rules keep that from becoming an endless loop:

- **Start the coverage map at round 1**, not when you notice you are re-litigating. It is what lets you answer a repeated finding with "logged — see the prior disposition" instead of relitigating it.
- **Stop rule.** Convergence is only ever declared by a fresh round over the current text — a round you repaired after can never be the terminal round. Terminal means either: **(a)** the round produced no new in-scope findings (re-raises are answered by the coverage map; out-of-scope findings route to their owning document), or **(b)** findings remain that the refiner argues should not be implemented — presented per *The `human decision` rule* as the complete unimplemented ledger, and the human approves; record the ruling in the coverage map, so convergence-by-ruling is distinguishable from convergence-by-clean-round. A round of *misfired* findings is neither — that is a prompt defect (see "When the findings are wrong, suspect the prompt" in *The cold review*); fix the prompt and rerun. The old convergence shape — all in scope, all sharpen-level, no bloat flags — is an approach signal, never the stop.
- **Consolidation trigger.** If your fix in one round becomes the finding in the next, stop patching. That is the observable symptom of editing with a keyhole view: you are closing findings locally while the document drifts. Group the outstanding findings by root cause and restructure — then review again. **If it happens twice, consolidating is not enough** — the problem is your editing method, not the document's structure. Move to the structured tier in *Scaling the ceremony*.
- **Watch who the findings are about.** A round whose findings are mostly *your own previous repairs* is not measuring the document any more; it is measuring you. Count them each round — it is the clearest convergence signal you have, and it points at a fix no additional review round can deliver.

## Scaling the ceremony

Three tiers. Match the tier to the evidence, and do not default to a heavier one than the evidence supports.

**Lightweight (default).** Everything above: triage, finding matrix, cluster-at-a-time repair with the self-check, closure list, coverage map. A handful of clarity fixes needs nothing more.

**Structured.** Add these three when the consolidation trigger has fired twice, or when a round's findings are mostly your own previous repairs. They exist to fix *how you edit*, which more review rounds cannot:

- **Invariants.** Name the properties a repair must not break — give them stable IDs (`P1`, `P2`, …) in the refinement working document. Then **restate every accepted finding as an invariant violation before editing**. That is the move that turns a one-off fix into a class fix. A finding that violates no invariant is either a clarity edit or a candidate for a new invariant (which must clear the codification bar).
- **Canonical ownership.** Rule text gets exactly one home; every other surface points rather than restates. Write the owner down — a small table of *content → canonical owner → derivative surfaces* — because drift between a guide, its template, and a materialized copy is one of the highest-yield finding streams there is, and it is invisible from inside any one of them. Where a derivative copy is generated once and never refreshed, add a mechanical sync check; an ownership rule nobody can verify will silently rot.
- **Rule impact map.** Before editing, for each accepted finding write: the invariant violated, the canonical owner of the rule you are changing, **every dependent that consumes or restates it — found by grep, not by memory** — and what must not change. Edit the owner first, then re-check every dependent. The fix is not finished when the flagged instance is repaired; it is finished when the search that found it returns a consistent document.

  Corollary — **sweep the class, not the instance.** When a finding names an instance of a class, enumerate the class and fix it entire. Take the sweep wider than the obvious form: a search over fenced code blocks misses the same defect in inline code spans.

**Full apparatus.** A dated worklog per pass, a numbered audit catalog with stable IDs, required stale-text sweeps, cold-reader simulations, and explicit stop conditions — weight calibrated for a large, in-use, multi-doc workflow. Reach for it when a structural repair spans several guides and a later reviewer must be able to reconstruct exactly which checks ran.

## Across passes

The disciplines below apply when a skill receives more than one refinement pass over time. A single-pass user can ignore this section.

**Recurrence threshold.** Do not codify from a single observation. First sighting = `log only` (recorded in the coverage map). Second sighting in a different case = consider codification. Third = codify. The coverage map provides the cross-pass memory this rule depends on.

**Periodic restructure.** Every several passes, refactor the guide for accumulated cruft — consolidate overlapping rules, remove dead text, reorganize sections by what is actually load-bearing. Bloat is fought retrospectively as well as at the entry point. This is a deliberate pass of its own; do not fold it into a normal refinement pass.
