# Writing Style Guide Design

## Purpose

This document is the standard for SKAI's writing style guide: what it is for, what it must and must
not contain, and the decisions behind it. It is used to write and cold-review the guide; it is not
something an operator reads at runtime.

- [`Guides/Core/writing-style.md`](../../Guides/Core/writing-style.md) — how an agent writes
  anything a person will read: discussion items, descriptions and reasons, footnotes, spec text,
  gate messages, requests and replies.

The guide is a reference, like the known-gaps guide: not a gated workflow and not a skill. Every
guide whose agent writes for a person sends it there with one inlined sentence; the agent reads it
whole before writing. Written 2026-10-24 from SwiftKickMobile/skai#97 and the Offers design run.

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md) § Common house style governs how
  guides themselves are written; this guide governs what agents write for people. The two do not
  overlap.
- [`Guides/Core/process-flow.md`](../../Guides/Core/process-flow.md) owns the pointer sentence, as
  it owns the gap pointer; the sanity scan in `internal/maintenance/guide-authoring.md` checks it.
- Content rules stay with their guides: `product-specs-catalog.md` § Writing style (what a
  requirement says and in which voice) and `design-specs.md` § Product Language Only. This guide
  says how any sentence reads; they say what a spec sentence must contain.

## Requirements

1. **One rule set for everything written for a person.** Discussion items in all their
   sub-bullets, change descriptions and their reasons, gap footnotes, spec text, gate messages,
   change requests, replies to the supervisor. The guide names the kinds once and never carries a
   per-artifact section.
2. **Stands alone.** The reader is a colleague who knows the product but was not in the session; the guide says so once. The test is mechanical: with every ID, link and term of art deleted the
   sentence still reads correctly. IDs and links supplement the words. A fact is stated, not
   pointed at ("as decided in D3" becomes what was decided).
3. **Reasons in words.** A citation is where to look; a reason is a sentence. Every justification
   or Why says the reason and then cites.
4. **The thing, not the instance.** Descriptions name the screen, state, behavior or rule in the
   product's words, never the sample data, frame name, node ID or code name that happens to show
   it, unless the reader must go there.
5. **Everyday words; guide vocabulary stays in guides.** The guides use tool-neutral terms (draw,
   drawings, the package, promote); a person reading the artifact gets the words people use for the
   work (mock up, design, add a screen, show a state, this request). No coined labels, no shorthand
   the reader has not seen defined, no contract phrasing. Precision comes from citations.
6. **First person, one idea per sentence, the point first.** The agent writes as the one doing the
   work. A summary line or description tells the reader at once what is decided or changed.
7. **Agent-facing, short, plain.** Six numbered rules with a bold lead sentence, one ❌/✅ pair,
   one self-check before a gate. Under 2,500 bytes before compression; read whole every run, so it
   stays small.
8. **Refined from real feedback** (a rule for the maintainers, not guide text). Each supervisor
   correction of the agent's writing is logged as a finding; a pattern becomes a rule here through a
   refinement round. The guide starts minimal.
9. **Never restates a content guide.** It does not say what a requirement must contain, which
   voice specs use, or what a design spec may name; it points nowhere, and those guides point at it.

## Settled decisions

- A separate reference guide reached by a pointer, not boilerplate inlined in every guide
  (supervisor, 2026-10-24). The earlier ruling that required cross-guide rules are inlined house
  style covers formats used at every state change (the Gap line, the Decision Log); a reading-time
  reference, like the gap workflow, is pointed at. The pointer is one sentence, verbatim, owned by
  process-flow and checked by the sanity scan, so no guide grows by more than that.
- Scope now is what the supervisor reads in artifacts and specs; the style of the guides themselves
  stays with `maintain-skai.md`. Chat replies and gate messages are covered because the agent writes
  them for the same reader.
- The design guide's own instruction defects found on the Offers request (a Description written as
  a visual diff, a Justification that is only a pointer, footnotes restating the frame) are repaired
  in the design guide and the gap guide, not here (`design-process-design.md` and
  `spec-format-design.md` § Amendment — 2026-10-24).

## Size budget

**2,150 bytes** (supervisor, 2026-10-24; first draft 2,267, compressed 2,183, installed 2,188). Whole-file
bytes by `wc -c`, managed header and addendum footer included. It binds every repair per the refinement
guide's size-budget rule.

## Boundaries

The guide does not define the Discussion schema, the footnote form, the spec content rules, or any
gate. It has no gates of its own and invokes no skill.

## Amendment — 2026-10-25 (the rule for guide writers)

Ruled (supervisor, 2026-10-25): the plain-language standard binds the guides' own examples and the
templates of text a person reads, so that every current and future guide produces it, not only the
guides repaired by hand. Series PL found thirteen defects in guides that already carried the pointer
sentence: their formats and examples taught citation-only reasons, letter-only proposals and
shorthand, and an agent copies the example in front of it.

10. **A guide's examples and reader-facing templates pass this guide.** Every worked example of
    text a person reads (a Discussion item, a change entry and its reason, a gate line, an evidence
    line, a handoff) and every template an agent fills for a person reads correctly under Requirements
    2–6. This is a rule for whoever writes a guide: `internal/maintain-skai.md` § Common house style
    states it, the guide-authoring sanity check in `internal/maintenance/guide-authoring.md` asks it
    of every edited guide, and the cold-review prompt template names examples that teach shorthand or
    a citation-only reason among its recurring failure modes.

Caps (supervisor, 2026-10-25, series PL): `process-flow.md` **21,500** (was 21,550); the UI Map guides keep no cap and were not compressed (supervisor: the only guides with an extensive regression test; no aggressive compression now).
