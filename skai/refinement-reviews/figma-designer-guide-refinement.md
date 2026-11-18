# Figma Designer Guide — Refinement Working Document

The kept working record of refinement passes over `Guides/Design/figma-designer-guide.md` and `Bin/figma-page-check.js`, beside the standard ([figma-designer-guide-design.md](figma-designer-guide-design.md)) and the findings log ([figma-designer-guide-findings.md](figma-designer-guide-findings.md)).

## Pass 2026-11-17: How Designs Are Drawn

Target: `figma-designer-guide.md` and the structure check, against items 1–12 of the standard's § Amendment — 2026-11-17. The multiple-sizes guide has its own pass. Reviewer: Codex 6.1 Terra at xhigh effort.

### Figma Mechanics Proven On A Test File

The standard's items 9 and 12 state Figma mechanics as unproven until the pass proves them. Run 2026-11-17 through the Figma tool on a scratch file holding a color variable, dimension variables, a text style, a `Button` component set with a text property, a `Row` component nesting it, a `Chrome` set whose variant property is bound to a variable, and a screen with overridden instances.

| # | Claim | Result |
| --- | --- | --- |
| 1 | Changing a variable or text style in place keeps every binding; what uses it shows the change | Holds. Bound IDs unchanged, resolved color and font follow |
| 2 | Setting it back from a `Backup/<package>/<name>` copy restores the exact look | Holds |
| 3 | Renaming a variable or style keeps its bindings, a rename into `Backup/…` included | Holds |
| 4 | A binding can be pointed from a draft variable at another variable | Holds |
| 5 | A copied page stays bound to the same variables and styles, and its instances point at the original main components | Holds. The copy shows a changed definition's new look |
| 6 | A copied page backs up the components on it | **Fails for standalone components.** Copying a page turns each standalone main component into an instance of the original; component sets are copied as sets. Copying a Section, a frame or the component itself keeps a component a component |
| 7 | Changing a main component in place (a property, a new layer, a new component property) keeps instance overrides and nested instances | Holds. Label, variant choice and fill overrides survive |
| 8 | Setting a main component back in place from a copy of it returns every instance exactly | Holds. Instance state after the restore equals the state before the change |
| 9 | A copied component's nested instances point at the original nested component | Holds. A nested component that changes needs its own backup |
| 10 | Swapping a component carries overrides over | Holds, for layer overrides and for component property values |
| 11 | Resetting overrides after a swap clears what carried over | **Partly.** It clears layer overrides and plain text overrides. A component property's value stays and has to be set again |
| 12 | Renaming a variant property drops a variable binding on existing instances | Holds. Renaming a text property keeps instance values |
| 13 | Resizing a layer inside an instance is ignored | Holds. No error, size unchanged |
| 14 | Hidden instance children are skipped unless the script turns that off | Holds. `figma.skipInvisibleInstanceChildren` was `true` |
| 15 | Setting a property on a hidden nested instance un-hides it | **Did not reproduce,** for a text property, a variant switch or a swap |
| 16 | A description reads back escaped | Holds |
| 17 | Resizing an auto-layout frame turns hugging off | Holds for each axis the resize changes; both when both change |
| 18 | A cloned variant loses its component property links | Holds |
| 19 | A layer cloned into another auto-layout frame keeps absolute positioning | Holds |
| 20 | A script that throws is rolled back whole | Holds. Nothing the failed script created was left |

Not tested, so not stated in the guide: an instance property overridden with its main's value stops rendering; a copy differs in explicit variable modes; a translucent variable fill on a kit instance renders opaque (no kit in the test file).

Consequences:

- Row 6 corrects the standard's item 9 and a rule the guide has today: a backup of `Components` is built from copies of its Sections, never from a copy of the page.
- Row 11 corrects the remedy after a swap: reset overrides, then set the component properties the screen needs.
- Row 15 removes that item from this pass and leaves the multiple-sizes pass to test its own rule about layers shown at one size.

### Structure Check

`Bin/figma-page-check.js` and its test were extended before round 1, so the reviewer can check the guide's claims against the code. New breaches: `color`, `text-style`, `dimension`, `type-size`, `purpose`. New signals, reported in a list of their own: `loose-layers`, `repeated-override`, `kit-lookalike`. The content checks stop at an instance and, on the instance itself, read only what it overrides. `python3 internal/tests/tools/figma-page-check/test.py`: 7 tests pass. Run in real Figma on the test file's change page: it reported the planted missing purpose note, the unbound fills and paddings, an instance's fill override and the unbound draft style, and nothing on the inherited values.

### Round 1 (Proposal)

The proposal is the guide's full proposed text, 23,079 bytes against 16,119 today. Prompt built from the cold-review template with slots filled and the legacy and observed-failure sections removed.
The reviewer's verdict on the proposal: endorse the reading of `Conventions` first, the `Global` reconciliation, the state examples, the names, the sample data rules, auto layout, scale-1 components, documented foundations, the purpose note and the split of breaches from signals; amend the Pages and kit wording, the draft and backup wording, the re-pointing remedy and the purpose annotation write; repair the check script before its claims are relied on. It proposed no trims and did not measure a recommended shape.

Finding matrix (one row per defect; a proposal round is not scored):

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The check skipped overrides on layers inside an instance | accept | standard item 11; script `layers`, `checkContent` | Read into instances; on every layer in one, check only what the instance overrides | Inherited values in a kit instance are the kit's |
| F2 A dimension bound to a variable outside `Dimensions` passes; the wrap gap was unchecked | accept the gap; log the collection | script `SPACING`, header | `counterAxisSpacing` added; header says the collection is not checked | Zero values exempt |
| F3 Gradient stops with no variable passed | accept | Styles rule 1; script `unbound` | Gradient stops checked | Image paints exempt |
| F4 Components and specimens were treated as screens | accept, kept small | script `screensOf`, `checkSection` | No purpose note asked on the `Components` or `Design System` pages; no screen columns in a `Design System` Section | Screens in package and request Sections still need notes |
| F5 The repeated-override signal grouped by field name, not value | accept | script signal | One field, one value, per component | Stays a signal |
| F6 A page check failed on another package's draft style | accept | script `type-size` | Skip `Draft/…` styles outside this page's own folder | The page's own drafts still fail |
| F7 No failing case for `padding` | accept | test | A badly padded Section, and cases for F1–F6 | Findings and signals stay apart |
| F8 "Only added or changed frames" excluded a request's `Components` and `Design System` Sections | accept | Pages rule 1 | Sentence rewritten | A request holds only its own screens |
| F9 "Only through drafts" implied a rename or removal needs one | accept | Pages rule 3; Design system drafts intro | "how one looks"; "A rename or a removal needs no draft" | Production is not changed in place during authoring |
| F10 A component backup's place for a base package was missing | accept | Design system drafts rule 4 | Both places named | Page backups stay bound to shared definitions |
| F11 Resetting overrides could erase what must be restored | accept | Design system drafts rule 6 | Note what the screen needs before the swap | The proven reset-then-set remedy |
| F12 Writing a purpose note could drop a gap annotation | accept | Purpose notes | "keeping the node's other annotations" | Gap stays yellow and off `Production` |
| F13 A host project's addendum says reading `Conventions` is no prerequisite | routed | the host's addendum, not this guide | None here; the project is told | An addendum's precedence |
| F14 Promotion's order lived in the conventions guide | accept in part | Design system drafts intro, rules 4 and 7 | Rules worded as what each thing is; the intro says the process guides own when and in what order. Pages rule 1's existing sentence left alone | Names, places, identity kept |
| F15 "Nothing is redrawn" forbade adding what the kit lacks | accept | Components rule 6 | "A component the kit supplies is not redrawn"; "reused with its whole structure" | Linked, then wrapped, then a detached copy |

Self-check after the guide-text cluster (F8–F12, F14, F15): no adjacent text contradicted; no stale sentence left teaching the old behavior in the proposal; no rule moved from its point of use; no enforced rule weakened. After the script cluster (F1–F7): header, code and test agree; 9 tests pass.

### Size

Measured with `wc -c` on the settled proposal (a working copy outside skai).

| Before | Settled | Delta | Old cap | Proposed cap |
| ---: | ---: | ---: | ---: | ---: |
| 16,119 | 23,607 | +7,488 | 16,122 (the pair's 18,820 less the multiple-sizes guide's 2,698) | 23,600 |

Where the growth is: Design system drafts +2,972 (new section); Agent tooling +1,097; Components +882; Canvas layout +769; Purpose notes +611 (new section); Styles +432; Design conventions +318; Copy and sample data +263; Pages +111; Dimensions +33.

**Cap not approved (supervisor, 2026-11-17):** 46% growth in one guide is too much; the document is to be broken up. Design system changes are infrequent. Two splits were drafted and measured:

| Shape | Main guide | Design system changes | Agent tooling |
| --- | ---: | ---: | ---: |
| One guide | 23,607 | | |
| Design system changes in a linked guide | 20,207 | 4,438 | |
| Design system changes and agent tooling in linked guides | 18,506 | 4,438 | 2,604 |

The four silent failures that arise when changing shared definitions (a swap, a renamed variant property, a cloned variant, a copied page) move with the design system rules. The choice is the supervisor's.

**Split chosen (supervisor, 2026-11-17):** design system changes and agent tooling each become a linked guide. Caps recorded in the standard: 18,500, 4,400 and 2,600.

### Applied After Round 1

The settled shape was applied as three guides: `figma-designer-guide.md` 18,494 bytes, `figma-designer-guide-design-system-changes.md` 4,394, `figma-designer-guide-agent-tooling.md` 2,591 (`wc -c`). The two new guides are in `assets.manifest.json`; the README's two lists of Figma guides name them.

Mechanical checks, 2026-11-17:

- Sizes: all three under their caps.
- Links: every relative link in the three guides resolves; anchors used are `#design-conventions`, `#dimensions`, `#project-addendum`, all present.
- `Managed-Updated-At` is 2026-11-17 on all three; `Managed-Id` matches the manifest for the two new guides.
- `\bhuman`: 0 occurrences in the three guides.
- Old-style names (`brandBlue`, `mutedBlue`, `brandWhite`, `alwaysBrand`, `secondaryText`, `spacing20`): 0 in the three guides; one `spacing20adapt` in the multiple-sizes guide, left for that guide's pass.
- Rule references: "(rule 4)", "(rule 6 under Components)", "(rule 6)" in the main guide still point at the rules they name. No reference to a rule that moved.
- Writing-style pointer: the purpose note is text a person reads, so the main guide now carries the pointer sentence verbatim in § Purpose notes, in place of style rules of its own.
- Tool claims: the main guide says the structure check "reports breaches to fix and signals to look at and judge, as its header lists". The script returns `findings` and `signals`; the header lists both. Test: 9 pass.
- The repaired script was run in real Figma on the test file's change page: it reported a raw fill planted on a layer inside an instance, the unbound values on the screens, and the missing purpose note; it skipped inherited values, the backup style and another package's draft style.

### Round 2 (Applied Text)

Finding matrix:

| Defect | Triage | Touches | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The main guide sent only appearance changes to the design system changes guide | accept | standard's ruling on the split; main guide Pages rule 3 | One sentence naming every case, promotion included | A package using only what exists does not read that guide |
| F2 Components rule 1 and the kit rule still put draft work on `Components`; the kit sentence on fills fought the color override | accept | Components rules 1 and 6 | Rule 1 covers new and changed drafts and supporting copies; rule 6 points at rule 1; one sentence on what a kit look keeps | Linked, then wrapped, then a detached copy |
| F3 "A request's being inside its package's" was unclear; two tooling bullets repeated rules 4 and 6 | accept | design system changes rule 8, rule 6, Agent tooling | Folders and Sections said separately; the two bullets removed; rule 6 says why | Who cleans up and when stays the process guides' |
| F4 The signals saw only instances in no other instance, so a kit inside its wrapper and nested overrides were missed | accept | script `layers`, `checkContent`, wrapper | Every instance, at any depth | Signals stay signals; only overrides are checked for breaches |
| F5 The header said another package's draft style is skipped, but a request's on the same page is checked | accept, header only | script header | Header: "outside this page's own folder". A page check covers every Section on the page, requests included | The page's own drafts still fail |
| F6+F7 Pages were classified by name prefix, and backup pages were content-checked | accept | script `check` | Exact page names; `<page> — Pre <change-id>` is laid out as its page and its content is skipped | Section model stays as the header states |
| F8 "One to one" and "product words, with no IDs" were lost | accept | standard items 3 and 10; Styles rule 5, Purpose notes | Both restored | The shared writing-style sentence stays verbatim |
| F9 The check for half-built results and the restore comparison were dropped | accept | standard items 9 and 12; tooling guide, design system changes rule 7 | Both restored | Restore in place; a throwing script is rolled back whole |

The open question on hidden instance children is logged, not fixed: the script reads what Figma returns by default, which skips hidden children of instances.

Round 2 arithmetic: F1 divergent · normal · speculative = 2.5 · F2 divergent · normal · speculative = 2.5 · F3 divergent · off-normal · speculative = 1.875 · F4 divergent · normal · verified = 5 · F5 divergent · off-normal · verified = 3.75 · F6+F7 one defect (how a page is classified), heaviest F7, divergent · normal · verified = 5 · F8 divergent · normal · speculative = 2.5 · F9 divergent · off-normal · speculative = 1.875.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |

Whose findings: F4 and F5 are about round 1's script repairs, and F1–F3 about the split made after round 1. The script's instance handling was therefore rewritten whole for this round (every instance, one rule), not patched a second time.

Self-check after the guide cluster (F1–F3, F8, F9): no adjacent text contradicted; the old "on `Components`" wording is gone from rule 6; no rule moved from its point of use; nothing enforced was weakened. After the script cluster (F4–F7): header, code and test agree; 11 tests pass.

Sizes after round 2's repairs, with the reviewer's own trims: 18,494 / 18,500; 4,285 / 4,400; 2,598 / 2,600. Links resolve; rule references ("rule 1", "rule 4", "rule 6") point at the rules they name.

### Round 3 (Applied Text)

A fix became the next round's finding twice (round 1's script repairs in round 2; round 2's backup-page repair and round 1's "how one looks" wording in round 3), so the pass moves to the structured tier for what is left.

Invariants:

- **P1 The rules and the check agree.** What a rule exempts the check exempts, and what the script's header says is skipped is skipped on every path through the code.
- **P2 One home per rule.** Each rule lives in one of the three guides; the others link to it and do not restate it in different words.
- **P3 A scope statement is as wide as the rules under it,** and no wider than a ruling allows.

Ownership:

| Content | Owner | Derivative surfaces |
| --- | --- | --- |
| What binds a color variable | main guide, Styles rule 1 | script header (`color`), script `unbound` |
| What needs a draft | design system changes guide, intro and rules 1–2 | main guide Pages rule 3 and Components rule 1; the process standard's items 7 and 9 |
| What scaling does to text styles | agent tooling guide, rule 6 | main guide Components rule 8 |
| Which pages the script checks, and what it skips on each | script header | script `check`; main guide § Structure check |

Finding matrix, each accepted row restated as a violation:

| Defect | Triage | Invariant | Owner and dependents (by grep) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 "Every fill and stroke binds a color variable" has no room for an image fill, which the check passes | accept | P1 | Styles rule 1; `grep -n "fill" figma-designer-guide.md` shows no other binding claim; header and `unbound` already exempt images | "Every solid fill or stroke and every gradient stop" | No color styles; images are components |
| F2 "Scales the instance, which keeps the component's text styles" reads as if scaled text stays linked | accept | P2 | tooling rule 6 owns it; Components rule 8 is the one dependent | "Scale each instance; the component keeps its linked text styles" | Drawn once at scale 1 |
| F3 A change that alters nothing visible is neither clearly drafted nor clearly exempt | accept, with a different fix | P3 | intro of the design system changes guide; the process standard's item 9 (supervisor, 2026-10-26: such a fix goes straight into the base) | Reviewer's "each change to one" rejected: it would require a draft the ruling says is not needed. One sentence says such a change is not drafted and the process guides say how it is made | A rename or a removal needs no draft |
| F4 The script lays out Sections on the `Design System` page as screen columns, and treats an asset page as a change page | accept in part | P1 | script header; `check`, `checkSection`; main guide § Structure check says only "as its header lists" | No screen columns anywhere on `Design System`. The header says which pages the script is for; an asset page is not one. No way to mark a page as an asset page is added: logged | Exact page names; the Section model the header states |
| F5 A backup page still ran the text-style check | accept | P1 | `grep -n "kind === name" Bin/figma-page-check.js`: two paths decide content scope, `checkContent` and the style loop | The style loop takes the same condition | Layout of a backup page is still checked |

Round 3 arithmetic: F1 divergent · normal · verified = 5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · F4 divergent · off-normal · verified = 3.75 · F5 divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |

The open question on which rename drops a binding is settled by the test record: a renamed variant property drops a bound variable; a renamed text property keeps instance values. The guide says "variant property"; the standard's candidate list said "a component property, or a variable's value" and is corrected.

Self-check after round 3's repairs, each dependent re-read: Styles rule 1 now agrees with the script's `unbound` and its header; Components rule 8 no longer speaks for the tooling guide's rule 6; the design system changes intro agrees with the process standard's items 7 and 9; both paths in the script that decide content scope carry the same condition. No stale sentence found. 12 tests pass. Sizes: 18,471 / 18,500; 4,391 / 4,400; 2,598 / 2,600.

### Round 4 (Applied Text)

Two more invariants, from this round's findings:

- **P4 An example obeys the rule it illustrates and the rules beside it.**
- **P5 A statement about Figma says what the test record shows, and no more.**

| Defect | Triage | Invariant | Owner and dependents | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 The script applies screen columns to component Sections | log only | — | script `checkSection`; behavior older than this change, and a single stacked column passes | None. Not caused by the change; no failure seen | — |
| F2 A text layer whose ranges differ in style was reported as unstyled, and its fills were not read | accept | P1 | script `checkContent`; header | Read such a layer range by range; proven against Figma (`getStyledTextSegments` returns each range's style and fills) | Only what an instance overrides is checked |
| F3 The Section fill check reads the first paint only | log only | — | script `checkSection`; older than this change | None | — |
| F4 Styles rule 1 read literally covers the canvas Section fill and paints inside a kit | log only | — | Styles rule 1; Canvas rule 2 sets the Section fill and Components rule 6 covers kit paints, each at its point of use | None. The same breadth has stood since the guide was written | — |
| F5 Components rule 1 said "new or changed" where the linked guide drafts only what changes visibly | accept | P2 | owner: the linked guide's intro; dependent: Components rule 1 (grep "changed components") | "new or visibly changed" | Supporting copies |
| F6 The draft-name examples used a page name with no concept letter | accept | P4 | design system changes rule 1; script `"Draft/" + name + "/"` | `Draft/Pinned Notes A/…` | The request ID inside the page's folder |
| F7 "The earlier look of a changed one is its own backup" promised a frozen look; a copied component stays bound | accept | P5 | design system changes rule 4; test record row 9 | "the earlier definition of each changed one is in its own backup" | Backups stay bound |
| F8 The ✅ example was an empty state, which the `Global` Section draws | accept | P4 | Screen pages rule 2; rule 4 lists the app-wide states | Example changed to a mode: `notes — selecting` | Varying text and an absent button earn no frame |

Round 4 arithmetic: F1 logged, noise · F2 divergent · normal · verified = 5 · F3 logged, noise · F4 logged, noise · F5 divergent · off-normal · speculative = 1.875 · F6 divergent · off-normal · speculative = 1.875 · F7 divergent · off-normal · speculative = 1.875 · F8 divergent · normal · speculative = 2.5.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |
| r4 | 13.125 | 5 | 0 | 5 | 0 | 3 |

Self-check, dependents re-read: `grep -n "changed components" Guides/Design/figma-designer-guide*.md` shows the two guides agree; the example in rule 2 no longer names a state rule 4 lists; rule 4 of the linked guide says "definition". 12 tests pass. Sizes: 18,491 / 18,500; 4,393 / 4,400; 2,598 / 2,600.

### Round 5 (Applied Text)

All four findings are in the design system changes guide; the reviewer found no tooling claim to fault.

| Defect | Triage | Invariant | Owner and dependents | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 The intro said a package drawing from what exists "never needs" the guide, though one that only renames or removes does | accept | P3 | the linked guide's intro; main guide Pages rule 3 already names every case | "a package with no such change does not need it" | A package with no design system change does not read it |
| F2 "Not changed in place before promotion" was unconditional beside the nothing-visible exception | accept | P3 | same intro; the process standard's item 9 | "production definitions keep their look until promotion" | Visible changes never reach production during authoring |
| F3 Rule 6 kept what "the screen needs", though a draft can be used inside a component | accept | P3 | rule 6; rule 2's supporting copies | "that use needs" | Reset, then set again |
| F4 Rule 7 restored only an edited definition; new, renamed, removed and re-pointed were not reversed | accept | P3 | rule 7; the standard's item 9 ("reverses each step"); rule 5's four cases | Rule 7 rewritten to reverse each of rule 5's and rule 6's steps | Identity kept; drafts untouched; the process guides own the order |

The intro was rewritten whole, since two rounds had each changed one sentence of it.

Round 5 arithmetic: F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · F4 divergent · off-normal · speculative = 1.875.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |
| r4 | 13.125 | 5 | 0 | 5 | 0 | 3 |
| r5 | 7.5 | 4 | 0 | 4 | 0 | 0 |

Self-check, dependents re-read: the intro's four sentences agree with rules 1–2 and 5 and with the main guide's Pages rule 3 and Components rule 1; rule 7 names each case rule 5 and rule 6 create. Sizes: 18,491 / 18,500; 4,397 / 4,400; 2,598 / 2,600. The script was not touched; 12 tests pass.

### Round 6 (Applied Text)

No finding against the text of the three guides. All three are about the script.

| Defect | Triage | Invariant | Owner and dependents | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 Any page named `… — Pre …` was read as a backup page and its content skipped | accept, in code | P1 | script `PAGE_BACKUP`, `check`; header | Only `Production`, a target-size page, `Components` or `Design System` followed by ` — Pre <change-id>` is a backup page. The reviewer's naming rule for the guide is not added: the other names it lists (`Components`, `Design System`, `Scratch — …`, `Base — Pre …`) are the guide's own names for those Sections | The backup naming convention |
| F2 A Section target loses what it sits inside (scratch, backup, depth) | noise: logged 2026-11-11 (#118 r2 F5), and the disposition stands | — | script header | None in code. The header now says a Section target is read on its own | — |
| F3 The repeated-override signal saw overrides on instances only, not on a plain layer inside them | accept | P1 | script `layers`, `checkContent`; header | A layer inside an instance is matched by name across instances of its component | Stays a signal; the threshold; different values are no signal |

Round 6 arithmetic: F1 divergent · off-normal · verified = 3.75 · F2 restates a logged finding whose disposition stands, noise · F3 divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |
| r4 | 13.125 | 5 | 0 | 5 | 0 | 3 |
| r5 | 7.5 | 4 | 0 | 4 | 0 | 0 |
| r6 | 7.5 | 2 | 0 | 2 | 0 | 1 |

Self-check: header, code and test agree on both repairs; the three guides were not touched, so their sizes stand (18,491 / 4,397 / 2,598). 13 tests pass. The script has now drawn findings in every round, each on a narrower case; its tests, not further reading, are what holds it, so each repair added a test that fails without it.

### Round 7 (Applied Text)

| Defect | Triage | Invariant | Owner and dependents | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 Rule 6 re-pointed "each" use of a draft, the package's own mockups included | accept | P3 | design system changes rule 6; the standard's "the package's drafts stay as they are" | "a draft in the base" | Note, swap, reset, set again |
| F2 "A later run's backups replace earlier ones" did not say whose | accept | P3 | rule 4; the standard's item 9 | "A run after a return to authoring replaces that package's backups" | Backup names and places |
| F3 Frames rule 2 made any check below a target size a state, against "another frame only when its layout changes" | accept | P2 | Frames rule 2; Screen pages rule 2 owns what earns a frame | "A smaller layout is a state. When a screen's layout changes below a target size, name the state for its width" | The width-based name |
| F4 The tooling guide says `resize()` turns hugging off "on each axis it changes"; the standard said both axes | reject for the guide; the standard corrected | P5 | test record row 17 | None in the guide: the test shows only the axes the resize changes. The standard's item 12 now says the same | — |
| F5 A target-size page whose size name contains " — Pre " had its backup cut at the wrong place | accept | P1 | script `check` | The matched page name is kept, not re-cut | Only main pages have backup pages |
| F6 A uniform radius override could be missed when the layer also has corner values | reject, checked in Figma | P5 | script `checkContent` | None. Figma lists a uniform radius override as `cornerRadius` and all four corners, so the corner check sees it | — |

Checking F6 in Figma showed a real fault next to it: because Figma lists five fields for one uniform radius override, the repeated-override signal would have reported it five times. It now counts once; test added.

Round 7 arithmetic: F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · F4 rejected, the guide matches the test record, noise · F5 divergent · off-normal · verified = 3.75 · F6 rejected against Figma, noise.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |
| r4 | 13.125 | 5 | 0 | 5 | 0 | 3 |
| r5 | 7.5 | 4 | 0 | 4 | 0 | 0 |
| r6 | 7.5 | 2 | 0 | 2 | 0 | 1 |
| r7 | 10.0 | 4 | 0 | 4 | 0 | 2 |

Self-check, dependents re-read: rule 6 and rule 7 of the linked guide agree on "in the base"; Frames rule 2 and Screen pages rule 2 agree; the standard's item 12 matches the tooling guide. 14 tests pass.
Sizes after round 7's repairs, with the reviewer's trims: 18,499 / 18,500; 4,380 / 4,400; 2,598 / 2,600.

### Round 8 (Applied Text)

No finding against the text of the three guides, for the second round in three. Both findings are about the script's signals.

| Defect | Triage | Invariant | Owner and dependents | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- | --- |
| F1 The loose-layers signal was raised for components and specimens, which are made of layers | accept | P1 | script `screensOf`, `checkContent`; header says "per screen" | Each collected frame carries whether it is a screen; the signal is raised for screens only | Content breaches are still checked on components and specimens |
| F2 Different mixed fills on a text layer were grouped as one repeated override | accept | P1 | script `checkContent`; `values` already reads ranges | The signal compares a text layer's fills range by range | One signal for a uniform radius override |

Round 8 arithmetic: F1 divergent · normal · verified = 5 · F2 divergent · off-normal · verified = 3.75.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| r2 | 25.0 | 8 | 0 | 8 | 0 | 0 |
| r3 | 16.25 | 5 | 0 | 5 | 0 | 0 |
| r4 | 13.125 | 5 | 0 | 5 | 0 | 3 |
| r5 | 7.5 | 4 | 0 | 4 | 0 | 0 |
| r6 | 7.5 | 2 | 0 | 2 | 0 | 1 |
| r7 | 10.0 | 4 | 0 | 4 | 0 | 2 |
| r8 | 8.75 | 2 | 0 | 2 | 0 | 0 |

Self-check: header, code and test agree on both; 14 tests pass. The finished script was run in real Figma on the test file's change page with the same raw fill planted on the title layer inside three instances of one component: it reported the three fills as breaches and raised one repeated-override signal naming the layer. Guide sizes unchanged: 18,499 / 18,500; 4,380 / 4,400; 2,598 / 2,600.

### Where The Pass Stands

Rounds r1–r8. The guides' text drew no finding in r6 or r8. Every finding in the last three rounds that was accepted is closed, each script repair with a test that fails without it. Round 8's two script repairs have not been read by a fresh round, so the pass is not closed by a clean round. It awaits the supervisor: end it here (the stop rule's ruling), or run on.

### Closure

Ended by the supervisor's ruling, 2026-11-17, after round 8: another round over two small, tested script fixes has no point. Rounds r2–r8: 25.0 · 16.25 · 13.125 · 7.5 · 7.5 · 10.0 · 8.75.

Every accepted finding is closed, with one line of evidence each in the findings log. Logged and left as they are: the collection a dimension variable comes from is not checked; hidden children of instances are not read; a Section target is read on its own; screen columns are checked in component Sections; the Section fill check reads the first paint; Styles rule 1 is stated for every paint; asset pages are not a target of the script.

Net size: `figma-designer-guide.md` 16,119 to 18,499 (cap 18,500); new `figma-designer-guide-design-system-changes.md` 4,380 (cap 4,400); new `figma-designer-guide-agent-tooling.md` 2,598 (cap 2,600).

### Maintenance Retro, Run Again (2026-11-18)

This change set's retro was run again together with the design process guides'; the migration assessment, every check's result and the change package verification are recorded in `design-process-refinement.md` under the same heading. The release entry's "change nothing" note for existing design files is replaced by the migration under **Design process guides** in `Releases/unreleased.md`.

## Pass — 2026-11-18: Form Factors (F4)

Target: `figma-designer-guide-multiple-sizes.md`, renamed `figma-designer-guide-form-factors.md`, and `figma-designer-guide.md` for the term, the `Conventions` definition and the stretch rule; `Bin/figma-page-check.js` for purpose notes on repeated screens. Standard: `figma-designer-guide-design.md` § Amendment — 2026-11-18. The supervisor's go: "Start" (2026-11-18), after ruling on each row of the scope (the Stream F plan records them).

### Figma Mechanics Proven On The Test File

Run 2026-11-18 through the Figma tool on the scratch file of the earlier pass (file key `xOCqqKq4UCd0G9wz0PQkRS`, page `form-factors-test`). The `Dimensions` collection was given two modes, `Compact` and `Wide`; `target` names the mode; `visible/Wide` is a boolean, false at `Compact`; `spacing-adapt/20` is 20 and 30. A `Bar` set has a `Target` variant property and a text property; a screen component holds a bar bound to `target`, three rows, a fourth row and a second bar bound to `visible/Wide`, and a footer pinned to the bottom. One Section per mode holds an instance of the screen, the `Wide` one resized from 390 to 800.

| # | Claim | Result |
| --- | --- | --- |
| 1 | A Section set to a mode gives everything in it that mode's values | Holds. The screen's gap read 20 in one Section and 30 in the other |
| 2 | A variant property bound to a string variable picks the variant by mode | Holds. The bar was `Target=Compact` in one Section and `Target=Wide` in the other |
| 3 | A value set in the screen component on such an instance is lost when the variable switches the variant | Holds. The title set to "Notes" read "Title" at `Wide`; the layer's own name was lost too. Set on the `Wide` instance, it stayed |
| 4 | A layer whose visibility is bound to a boolean variable shows by mode, nested instances included | Holds. The fourth row and second bar were hidden at `Compact` and shown at `Wide` |
| 5 | Setting a property on a nested instance hidden that way un-hides it | **Does not happen.** Still hidden after its text property was set and after its variant was switched. With the earlier pass's row 15, the reason for making a part transparent is gone |
| 6 | A layer inside an instance can be moved | **Refused with an error** ("This property cannot be overridden in an instance"). Loud, so it is no tooling item |
| 7 | A screen built with auto layout stretches as an instance | Holds. Rows set to fill went from 390 to 800; the footer, positioned absolutely with constraints, stayed on the bottom edge and stretched |
| 8 | A bar's instance follows its variant's height | Only when every variant hugs its content and the instance hugs. An instance of fixed height stayed 44 where the `Wide` variant is 64. With hugging variants and a hugging instance it read 64. Where the `Wide` variant had no auto layout, the instance kept the other variant's 35 against 70 |

Not tested: a kit component as the bar (no kit in the file).

### Structure Check

`purpose` is no longer asked of an instance placed as a screen: at a further form factor a repeated screen is an instance of the screen component, and one with its own layout there is a component. Header and code changed together; a new test, `test_a_screen_repeated_at_a_further_form_factor_needs_no_purpose_note`, fails without the change (checked by reverting it). 15 tests pass. The header says "form factor" where it said "target size".

### Migration Assessment (Before Drafting)

What the change asks of work that already exists (`internal/maintain-skai.md`, Required bookkeeping):

| Existing Thing | What The Change Asks Of It | Migration |
| --- | --- | --- |
| `Conventions` in every design file | Each form factor has a name, a definition and a default frame size; the label says "form factors" | Propose a definition for each from what the file shows, stop for the supervisor, write it into the frame |
| The guide's addendum, `skai/addenda/figma-designer-guide-multiple-sizes-addendum.md` | The lookup name follows the file | Moved unchanged to the new name; links to the old guide path in project documents repointed |
| A further form factor's page that does not hold every base frame | A full set | Missing instances listed, approved, added; a frame that exists only there and repeats another Section is reported, since removing it changes the designs |
| Open packages in a file with several form factors | A Section per form factor on the change page, repeating every frame the package draws | Sections and instances proposed and added; a screen with its own layout there needs its change drawn, which is listed for the package's next round |
| Purpose notes on repeated screens in open packages | None needed | The earlier migration's note-writing step skips instances, as the check now does |
| Parts hidden at one form factor by other means; bars whose variants do not hug | How a drawing is built | Left alone and reported, as the earlier migration leaves how production drawings are built |
| The `target` variable and `Target` property | Names kept | None |
| Project documents and addenda that say "target size" | Project-owned words | Reported in addenda; nothing edited |
| The package artifact, app code, the UI Map | Nothing | None |

### A Change Page With A Section Per Form Factor, In Figma

Built 2026-11-18 on the scratch file (page `ff-change A`): a `Pinned Notes` Section set to `Compact` holding a draft screen component with a purpose note, and beside it `Pinned Notes (Wide)` set to `Wide`, holding an instance of that screen resized to 800 wide and a screen component with its own layout and no note. Read back: the repeated screen is an `INSTANCE` and carries no annotation, although its main component has one, so a note on a screen does not show on its repeats; the screen with its own layout is a `COMPONENT`. That is what the structure check's new condition reads. The full script was not run again in Figma for this one-condition change; its test covers it.

Seen while building it, for triage with round 1: the repeated screen has the same name as the draft it repeats, on the same page, and the main guide's Frames rule 5 says no two frames on a page share a name, with copies in request, backup and scratch Sections excepted.

### Round 1 (The Proposal)

Prompt `reviews-f/f4-r1-prompt.md` (SalesPro working documents), built from the template's block: every template line appears verbatim except the slot lines and the two deleted sections (legacy artifacts, observed failures). Proposal as reviewed: `reviews-f/f4-proposed/`. Sizes of the draft before the round: form factors guide 5,245 (from 2,698); main guide 19,603 (from 19,000); design authoring 18,848 (unchanged); design promotion 13,347 (from 13,349).

Report: `reviews-f/f4-r1-out.md`. The reviewer changed nothing in skai (`git status --short` before and after agree). A proposal round is not scored. Verdict on the proposal: endorsed in its structure (the rename, project-named form factors, a mode each, full sets, boolean visibility, no workflow in the guide, the two process-guide wordings), to be amended as below. Nine findings, each checked against the files.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 A request gets a Section per form factor, but the main guide's backup sentence and promotion's fold speak of one Section | accept, in a smaller form than the reviewer's (which edited four guides) | item 35 · form factors rule 11 | Rule 11 names a request's further Sections and says that what the main guide says of a package's or request's Section, backup and fold included, holds for each form factor's | Promotion's sentence as proposed; no rule on completeness in promotion (supervisor); the design system and cleanup guides untouched |
| F2 A repeated screen shares its name with the draft it repeats, on one page, against Frames rule 5 (seen in Figma before the round) | accept | item 35 · main guide § Frames rule 5 | The rule's exception gains a further form factor's Section | The other exceptions; any other copy is still renamed |
| F3 "Set again to the screen component's values" can be read as the component's defaults | accept the rewording; the reviewer's sentence for a screen with its own layout is not added | item 30 · rule 5 | Content is set on the screen instance on each further form factor's page | Binding, hugging, content through properties |
| F3b No instruction for chrome content in a screen with its own layout | log only | — | None: nothing switches while such a screen is edited in its own mode, and the practices already put content in through properties | — |
| F4 "Differs by form factor … even where it looks the same everywhere" contradicts itself | accept | item 30, reworded with it · rule 5 | The kit case is named: chrome whose kit component differs while the app looks the same | Chrome that neither differs nor wraps a differing kit component gains no variants |
| F5 The script's header says every instance placed as a screen is a repeat; the main guide allows an instance as a screen anywhere (verified) | accept | item 36 · `figma-page-check.js` header | The header says what the script does: no note asked of an instance placed as a screen; whether one that is no repeat needs a note is for the reader | The check's behavior and its test |
| F6 Nothing says where a repeated screen's note is found, which the standard's earlier item 10 requires | accept | item 36 · rule 12 | Its note is on the base form factor's frame of the same name | A repeat carries none |
| F7 One name per form factor cannot name a part shown at two of three | accept as a sharpening, without the reviewer's joined-name format | item 31, reworded with it · rule 8 | Named for where it shows; true in the modes where it shows, false in the others | `visible/<form factor name>` for one; boolean visibility |
| F8 The stretch rule says a further form factor "reuses the same screen", against the rule for a layout that differs | accept | item 26 · main guide § Components rule 7 | "can then reuse the screen" | Stretching is a rule for every file |
| F9 Rule 4 opened by telling every screen to build its content as a component | accept | item 32 · rule 4 | The condition leads the sentence | Both examples; shared content for a layout that differs |

Why F1 and F7 are not supervisor decisions: neither fix adds a gate, a field or a proof, drops content or misses a cap; each sharpens a sentence the proposal already had. F7's name for a part shown at several of three or more form factors is left to the file.

Settled sizes after triage: form factors guide 5,505; main guide 19,624; design authoring 18,848; design promotion 13,347. The reviewer's own shape, with every one of its fixes, measured 5,670 and 19,784.

### Tightening Review

The supervisor's order for a pass: the proposal's review, the settled text, the reviewer's tightening, then one cap table. Prompt `reviews-f/f4-compress-prompt.md`, on the pattern of the design process guides' pass.

Report: `reviews-f/f4-compress-out.md`. The reviewer changed nothing in skai or in the proposal (status and checksums before and after agree; the one status line that differs is the refiner's own entry in the findings log). It found the text already tight: seven trims worth 188 bytes and five restorations.

| Reviewer's Item | Disposition |
| --- | --- |
| Form factors trim 1, the opening's example sentence | Taken in other words: "This guide's examples call two of them `Compact` and `Wide`". The reviewer's "For example, two are" reads as a statement about a file |
| Form factors trims 2 to 5 (where a part shows; same people and records; top level; the matching base frame) | Taken |
| Form factors restoration 1, the side panel example the current guide has | Taken. The draft had lost an example |
| Form factors restoration 2, content set "on each form factor's page to match the screen component's values" | Not taken. It brings back the wording round 1 found misleading, and the base page holds the component, not an instance. The standard's item 30 was loose and is corrected: content is set in the screen component and again on the instance on each further form factor's page, as the Figma test showed. The reviewer's question for the supervisor is answered by that test |
| Form factors restoration 3, each form factor's version is assembled from the content | Taken, in one sentence |
| Form factors restoration 4, added data follows the main guide's coherence rule | Not taken. That rule covers every frame; restating it is the duplication the review exists to remove. Item 33 now says so |
| Main guide trim 1, `Conventions` overrides examples and defaults | Taken |
| Main guide trim 2, the definition and the deferred sentence | Half taken. "What the name stands for" stays, since it is the reason for the definition; the sentence on deferred form factors is unchanged text and stays |
| Main guide restoration, longer content among what reuses a stretching screen | Taken |

Sizes by `wc -c`, proposal as tightened:

| Guide | Before | Compressed | Delta | Old cap | Proposed cap |
| --- | ---: | ---: | ---: | ---: | ---: |
| `figma-designer-guide-form-factors.md` | 2,698 | 5,542 | +2,844 | none of its own | 5,540 |
| `figma-designer-guide.md` | 19,000 | 19,596 | +596 | 19,000 | 19,590 |
| `design-authoring.md` | 18,848 | 18,848 | 0 | 18,900 | 18,900 holds |
| `design-promotion.md` | 13,349 | 13,347 | −2 | 13,350 | 13,350 holds |

Where the main guide's 596 comes from: the stretch rule, 278 (moved in by the supervisor's ruling); two pointers where a core rule changes with several form factors (the change page's Sections, purpose notes on repeated screens), 233; the form factor definition in `Conventions`, 33 net; the term and the name exception, 52. Caps await the supervisor.

### Caps And Application

The supervisor approved the caps on 2026-11-18: 5,540 for the form factors guide and 19,590 for the main guide; 18,900 and 13,350 hold for design authoring and promotion. Two words were trimmed to fit (5,542 to 5,540; 19,596 to 19,588). Applied: the guide renamed with `git mv` and replaced, the main guide's passages, the two process sentences, the manifest's `sourcePath` (id kept), and the README's two mentions.

Checks after applying, each with its result: sizes by `wc -c` 5,540 / 19,588 / 18,848 / 13,347, all within cap. Old term or path (`grep -rn -i "multiple-sizes|target size|target-size|size page|size name"` over `Guides`, `README.md`, `Templates`, `Install`, `Bin`, `internal`, the manifest): 0 occurrences besides the kept manifest id. Relative links in the four guides and the README's guide links: 0 broken. Manifest parses. `figma-page-check` test: OK, 15 tests. Headers: all four guides read 2026-11-18. The form factors guide's entry cue and addendum footer carry the new name. The process guides' gate sections are untouched, so their recorded flow simulations stand.

### Round 2

Prompt `reviews-f/f4-r2-prompt.md`, built by `reviews-f/f4-build-prompt.py` from the template's block (every template line verbatim except slot lines and three deleted sections: legacy artifacts, observed failures, proposed edits). Report `reviews-f/f4-r2-out.md`. The reviewer changed no guide (checksums before and after agree).

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 Rule 3 puts an instance of each screen on every further page, against rule 4's own component; and says the mode changes spacing and type, where which values change is the project's choice | accept | item 30 · rule 3 | "or its own screen component where the layout differs (rule 4)"; "modes resolve adaptive values" | A full set on every further page; no variants |
| F2 Rule 4 builds shared content "on `Components`", against the main guide's rule that a new component is a draft in its package | accept | item 32 · rule 4 | The location is the main guide's Components rules | Content defined once and shared |
| F3 The visibility name's template form reads as one form factor's name. This is round 1's F7 repair coming back | accept; the sentence takes the reviewer's shape | item 31 · rule 8 | The name is given as an example, `visible/Wide` | Boolean in `Dimensions`; no naming scheme for several |
| Open question: `Conventions` does not say which form factor is the base | log only | — | None: no strand seen, and a required field would be new | — |

Net size by `wc -c`: 5,540 before the round, 5,535 after the three fixes and three trims the reviewer gave to fit (the opening's example sentence, kept with "Form factor names"; the sample data sentence; rule 11's last sentence). The standard's items 30, 31 and 32 were reworded to match.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875 · the open question is neither

Consolidation: one of three findings is the refiner's own earlier repair (F3). It is the first such return in this pass; rule 8's sentence now has the reviewer's shape.

### Round 3

Prompt `reviews-f/f4-r3-prompt.md` (same builder; one more settled line). Report `reviews-f/f4-r3-out.md`. The reviewer changed no guide (checksums agree).

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The main guide says a request "uses one" Section; the form factors guide gives it one per form factor. Round 1's F1 repair left this word standing | accept | item 35 · main guide § Pages rule 1 | "uses a" | Naming, top-level placement, backup and fold |
| F2 Rule 4 builds every version from "the shared screens" and puts a differing layout "on its own page", against a draft's place in a change-page Section. The sentence was the refiner's own, written at the tightening | accept | item 32 · rule 4 | "and any shared screens"; "on its form factor's page or change-page Section" | Shared content; the same name |
| F3 Rule 6 gives every form factor a full set and then draws "the other orientation" only for a screen with its own layout; if both orientations are form factors the two collide | accept as a sharpening; the reviewer's supervisor-decision is not needed | item 29, reworded with it · rule 6; main guide § Frames rule 6 | "An orientation that is not a form factor"; the main guide's rule against rotated frames no longer calls a landscape design a form factor | Every named form factor gets the full set |

Why F3 needs no ruling: the supervisor accepted the row as written ("The other orientation is drawn only for a screen with its own layout there"), and its source in the field notes is about an orientation the file has no full set for. Naming that case is what the row meant; it changes no decision.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875 · F3 divergent · off-normal · speculative = 1.875

### Structured Tier (From Round 3)

Two of round 3's three findings are the refiner's own earlier repairs (F1 from round 1, F2 from the tightening), after one in round 2. The pass moves to the structured tier.

**Invariants**, each grounded in the standard's amendment:

- **P1** Whatever is said of a screen at a further form factor holds for both kinds: one repeated as an instance, and one with its own layout, which is a component (items 30, 32, 36).
- **P2** Whatever is said of where a screen or a Section is holds in both places a form factor's screens can be, its production page and its Section of a change page, and for a request as for a package (item 35).
- **P3** A sentence of the main guide that several form factors change does not state the single case as the only case (items 25, 35, 36).
- **P4** The guide says nothing of what a design's values are and holds no platform's part (the amendment's "Supersedes", item 19 out).
- **P5** A name in the guide reads as an example unless it is a rule for every file; it is never a template for a case the guide leaves to the file (item 31).
- **P6** A form factor is what `Conventions` names. Whatever is said of "a form factor" holds for every one named, and an orientation not named is not one (items 25, 29).

Round 3's findings restated: F1 is P3 (and P2); F2 is P2 (and a mandatory reading of "the shared screens", which the standard never required); F3 is P6.

**Ownership:**

| Content | Owner | Where It Is Restated Or Pointed To |
| --- | --- | --- |
| Where a component lives, drafts included | Main guide § Components rule 1 | Form factors rule 4 points |
| A package's or request's Section, its backup and fold | Main guide § Pages rule 1 | Form factors rule 11 extends it to each form factor's Section |
| Purpose notes | Main guide § Purpose notes | Its own parenthetical; form factors rule 12; the structure check's header |
| How a screen stretches | Main guide § Components rule 7 | Form factors rule 3 points |
| Sample data rules | Main guide § Copy and sample data | Form factors rule 9 adds only what crosses form factors |
| Frame sizes | Main guide § Frames | Form factors rule 3 points |
| A complete set at promotion | Design promotion `C3` step 3 | Form factors rules 3, 6 and 11 answer it |

**Sweep, by invariant** (each sentence of the form factors guide and of the main guide's touched passages read against it; `grep -n "repeat\|instance\|page\|Section\|orientation"` to find them):

- P1: rule 3 names both kinds (round 2). Rule 5 said content is set again "on the screen instance on each further form factor's page", which leaves out a screen with its own layout: now "on each further form factor's screen". Rules 6 and 11 use "repeats" for both kinds and rule 11 says so; rule 12's two sentences tell them apart. No other sentence.
- P2: rule 4's "on its own page" (F2), fixed. Rule 3 speaks of production pages only, by name. Rule 11 covers a request. Rule 12's "matching base frame" holds in both places.
- P3: "uses one" (F1), fixed. The package Section sentence, the frame-name rule, the purpose-note sentence and the stretch rule were corrected in round 1. The backup sentence is singular and rule 11 extends it, which round 3's reviewer left standing.
- P4: "modes resolve adaptive values" (round 2). `spacing-adapt/20` "is 20 at `Compact` and 30 at `Wide`" is the released example of the naming rule and names no rule for values. Parts named (navigation, tab bar, header, sheet, card, split view, side panel) belong to no one platform.
- P5: `visible/Wide` is given as an example. `Production (<form factor name>)`, `<package> (<form factor name>)` and the request's form are rules for every file.
- P6: rule 6's orientation sentence (F3), fixed. The main guide's Frames rule 6 called a landscape design "a landscape form factor", which collides with an orientation that is not one: now "drawn at landscape size".

Sizes by `wc -c` after the repairs: 5,539 of 5,540 and 19,589 of 19,590. One trim is the reviewer's (rule 9's first sentence); two are shorter forms of this round's own new sentences. Tests: 15 pass. Old term: 0 occurrences.

### Round 4

Prompt `reviews-f/f4-r4-prompt.md`. Report `reviews-f/f4-r4-out.md`. The reviewer changed no guide (checksums agree).

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 "A repeated screen carries no purpose note", when rule 11 uses "repeats" for a screen with its own layout too, which needs a note. P1. The round 3 sweep saw the word, wrote "repeated as an instance", then took it back to fit the cap | accept, in the reviewer's shape | item 36, reworded with it · rule 12; main guide § Purpose notes | "A base screen's instance at a further form factor carries no purpose note"; the main guide's parenthetical says "an instance repeating a base screen" | A screen with its own layout carries a note; the check exempts every instance |
| F2 "Repeats every frame the package draws" takes in component drafts, swatches and specimens, which the next sentence keeps single, and does not name the base Section as the source. P2 | accept | item 35, reworded with it · rule 11 | "every screen frame the package draws in the base Section" | `Components` and `Design System` stay single |

Trims, all the reviewer's: rule 3 "has a page"; rule 4 "Each version"; rule 5's opening reordered; rule 8 "differing placement"; the opening's "Names come from `Conventions`" (given in round 2 and declined then); the main guide's Frames rule 6, "Draw landscape designs at landscape size." Two of round 4's trims were declined as telegraphic ("Nested instances too:", "Keep people and records; larger ones add, never swap them").

Lesson for the method: a reviewer's shaped sentence is not trimmed by the refiner to fit a cap. Round 3's own trim of "as an instance" was this round's F1.

Sizes by `wc -c`: 5,539 of 5,540; 19,578 of 19,590. Tests: 15 pass. `grep -n -i "repeat"` over both guides: rule 6 (a page repeats every base frame, both kinds), rule 11 (now screen frames, both kinds named), the main guide's parenthetical (an instance); no bare "repeated screen" left.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · off-normal · speculative = 1.875

### Round 5

Prompt `reviews-f/f4-r5-prompt.md`. Report `reviews-f/f4-r5-out.md`. The reviewer changed no guide (checksums agree). It found no defect in round 4's repairs.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The main guide says a file with several form factors "adds modes and adaptive variables", as if one were always needed. P4 | accept | item 30 · main guide § Dimensions rule 2 | "adds modes and may use adaptive variables" (+8) | A mode for every named form factor |
| Open question: "a kit component cannot bind the project's values" is a claim about Figma with no proof the reviewer could see | accept as the refiner's own check, since the pass states no Figma claim it has not proven | item 30, reworded with it · rule 5 | The reason clause comes out of the guide; the rule stays (−53) | Chrome whose kit component differs is still wrapped |

Sweep after the open question, every claim in the form factors guide about what Figma does against the proof table: a Section's mode (row 1), a variant bound to a variable (2), a value lost at the switch (3), visibility bound to a boolean, nested instances included (4, 5), a layer inside an instance cannot be moved (6), a screen stretches (7), hugging (8), added content shown through the visibility variable (4). The kit clause was the only one with no row.

Sizes by `wc -c`: 5,486 of 5,540; 19,586 of 19,590. Tests: 15 pass.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · the open question is neither, and its edit is the refiner's own

### Round 6

Prompt `reviews-f/f4-r6-prompt.md`. Report `reviews-f/f4-r6-out.md`. The reviewer changed no guide (checksums agree). It found no defect in round 5's repairs and endorsed both.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 Rule 5 says that without hugging an instance "keeps one variant's size at every form factor"; the two tests show it can, not that it always does | accept | item 30 · rule 5 | "can keep one variant's size when it switches" (−1) | Every variant uses auto layout and hugs; each instance hugs |

Sizes by `wc -c`: 5,485 of 5,540; 19,586 of 19,590.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875

The round still found a defect in the text, so the pass does not end on it: a fresh round follows.

### Round 7

Prompt `reviews-f/f4-r7-prompt.md`. Report `reviews-f/f4-r7-out.md`. The reviewer changed no guide (checksums agree). It found no defect in the form factors guide; both findings are in main guide sentences this pass wrote.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The main guide lists per-screen Sections, `Components` and `Design System` "inside one Section … (one per form factor…)", which reads as the whole list in every form factor's Section; rule 11 keeps the last two single. P3 | accept, the reviewer's wording | item 35 · main guide § Pages rule 1 | "inside a Section named for the package (for several form factors: …)" (−21) | One Section per form factor; `Components` and `Design System` in the base one only |
| F2 "Below its form factor's width": a form factor has a definition and a default frame size, not one width. P6 | accept, the reviewer's wording | item 25 · main guide § Frames rule 2 | "below its form factor's default frame width" (+14) | A narrower layout is a state, named for its width |

Sweep, P3 and P6 again, over every main guide sentence this pass touched (the ten listed in the builder's `GUIDES` slot): the request sentence, the backup sentence, Pages rule 2, the two `Conventions` sentences, the page table and the sentence after it, Frames rules 1, 5 and 6, Dimensions rule 2, Components rules 1 and 7 and the purpose-note parenthetical each read correctly for one form factor and for several, and none gives a form factor a property `Conventions` does not give it. No further edit.

Sizes by `wc -c`: 5,485 of 5,540; 19,579 of 19,590. Tests: 15 pass.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r7 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · normal · speculative = 2.5 · F2 divergent · off-normal · speculative = 1.875

### Round 8

Prompt `reviews-f/f4-r8-prompt.md`. Report `reviews-f/f4-r8-out.md`. The reviewer changed no guide (checksums agree). It found no defect in round 7's repairs and called the guides usable by a fresh agent.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The main guide's change page sentence lists `Components` and `Design System` as if every package has them, and rule 11 says they "stay single"; a package that draws only screens could make two empty Sections. The wording predates this pass, in a sentence the pass touched | accept, the reviewer's wording: valid and small, in a sentence the change edits | item 35 · main guide § Pages rule 1; rule 11 | "per-screen Sections and any `Components` and `Design System` Sections"; "Any `Components` and `Design System` Sections stay single" (+7, +4) | One concept per page; the request sentence; backup and fold |

Sizes by `wc -c`: 5,489 of 5,540; 19,586 of 19,590. Tests: 15 pass.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r7 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r8 | 1.0 | 1 | 0 | 0 | 1 | 0 |

> F1 cosmetic · normal · speculative = 1.0

### Round 9

Prompt `reviews-f/f4-r9-prompt.md`. Report `reviews-f/f4-r9-out.md`. The reviewer changed no guide (checksums agree). Both findings are about names in the main guide.

| Defect | Triage | Touches (spec § + target doc §) | Minimal fix | Must remain unchanged |
| --- | --- | --- | --- | --- |
| F1 The frame-name rule excepts "copies" in a further form factor's Section; a screen with its own layout there is no copy, yet rule 4 gives it the base screen's name. P1, in a sentence round 1 wrote | accept, the reviewer's wording | new item 38 · main guide § Frames rule 5 | "except copies in a request, backup or scratch Section and frames in a further form factor's Section" | The three earlier exceptions; any other copy is renamed |
| F2 Screens are named in lowercase and components in Title Case, and in a file with several form factors every screen is a component. The two rules have met since the earlier pass added the Title Case rule | accept, the reviewer's wording. It keeps what files already do: a screen is named as a screen | new item 38 · main guide § Colors rule 5 | "components other than screens, and all component properties have readable Title Case names" | Lowercase screen names; Title Case for every other component and for all properties |

**P7**, a new invariant from F2: a rule about components holds, or says it does not, for a screen that is a component. Sweep of the main guide's rules that speak of components: Components rule 1 already excepts screen components; rule 7 names "components and screens" together; the names rule is fixed; Pages rule 7 lists the three kinds of node a screen may be. Outside the target, logged for its owner: `figma-designer-guide-design-system-changes.md` rule 2 drafts "a changed component" in the package's `Components` Section and does not say that a changed screen component is a changed screen, drafted in its screen Section as the main guide's Pages rule 1 says.

P1 sweep of the main guide's touched sentences, which the round 3 sweep had done only for the form factors guide: the frame-name rule (fixed here); the purpose-note parenthetical says "instance"; no other sentence speaks of a screen at a further form factor.

To fit the cap, the reviewer's trim of the `Conventions` entry is taken whole: "Its definition names devices or window widths and orientation. Some the app supports may be deferred." This drops "says what the name stands for", which the tightening review's disposition had kept; the entry still says what a definition holds, and the alternative was another cap raise for 46 bytes.

Sizes by `wc -c`: 5,489 of 5,540; 19,577 of 19,590. Tests: 15 pass.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r7 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r8 | 1.0 | 1 | 0 | 0 | 1 | 0 |
| r9 | 4.375 | 2 | 0 | 2 | 0 | 0 |

> F1 divergent · off-normal · speculative = 1.875 · F2 divergent · normal · speculative = 2.5

### Round 10

Prompt `reviews-f/f4-r10-prompt.md`. Report `reviews-f/f4-r10-out.md`. The reviewer changed no guide (checksums agree). **No findings**: no defect, no wording change and no trim recommended; it walked the seven paths and called the guide usable by a fresh operator. Its limits, in its words: Figma's behavior was judged from the standard's recorded proofs and not retested, and the migration of existing files and addenda sits in the release document, which it could not read.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r7 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r8 | 1.0 | 1 | 0 | 0 | 1 | 0 |
| r9 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r10 | 0 | 0 | 0 | 0 | 0 | 0 |

> nothing scored

### Closure

The pass ends on round 10 by the stop rule's first condition: a fresh round over the current text, with nothing repaired after it, left nothing to apply. Fifteen findings were fixed across rounds 2 to 9, none irreversible; four were the refiner's own earlier edits returning (r2 F3, r3 F1, r3 F2, r4 F1), which moved the pass to the structured tier at round 3. Every finding and its disposition is in the findings log.

Final sizes by `wc -c`: `figma-designer-guide-form-factors.md` 5,489 / 5,540; `figma-designer-guide.md` 19,577 / 19,590; `design-authoring.md` 18,848 / 18,900; `design-promotion.md` 13,347 / 13,350. Net change over the pass: +2,791, +577, 0 and −2.

Logged and left: `Conventions` does not say which form factor is the base; where a frame in an orientation that is no form factor sits; how a part shown at several of three or more form factors is named; a bar's content in a screen with its own layout; the design system changes Figma guide's "changed component" against a changed screen component (that guide's own pass); a kit component as a switching bar was not tested, since the scratch file has no kit.

### Maintenance Retro (2026-11-18)

Scope: this pass's change set (uncommitted, on top of `7c3133e`). Host-install-visible.

**Bookkeeping, each with its result:**

- Release documents: `Releases/unreleased.md` has the entry "The guide for several sizes is renamed for form factors and grows from five rules to twelve" under Figma designer guides, and `CHANGELOG.md` has a **Form factors** line; they describe the same change. The entry was brought in line with the final text after round 10 (frame names, Title Case for components other than screens, "may use adaptive variables").
- Migration (`internal/maintain-skai.md`, Required bookkeeping), assessed before drafting (table above) and written into the one migration this stream's three entries share, now nine steps: the addendum's move to its new name, definitions for each form factor in `Conventions`, the missing frames of each further form factor's set, a Section per form factor for open packages, each proposed at the stop for the supervisor before anything changes; what a drawing shows or how it is built is left alone and reported; a second discovery pass verifies. Every step is safe to repeat (a moved addendum, a present definition, an existing instance are skipped). Step references checked by reading: the intro's steps 7 and 8, step 2's 7 and 8, "steps 6 and 7", "step 3 moves".
- Update guide and adapter runbooks: unchanged.
- Manifest: `guide.figma-designer-guide-multiple-sizes` kept, `sourcePath` now `Guides/Design/figma-designer-guide-form-factors.md` (`grep -A3` on the id); the file's `Managed-Id` matches; the manifest parses.
- `Managed-Updated-At`: the four guides edited read 2026-11-18 (`date +%Y-%m-%d`).
- README: both mentions link the new file and say "form factors" (`grep "multiple-sizes|target size"` on `README.md`: 0 occurrences).
- `internal/maintain-skai.md`: no invariant or maintenance rule changed.
- Integration templates and installer runbooks: unchanged.

**Consistency, each with its result:**

- Stale paths and terms: `grep -rn -i "multiple-sizes|target size|target-size|size page|size name"` over `Guides`, `README.md`, `Templates`, `Install`, `Bin`, `internal`, `assets.manifest.json`: 0 occurrences besides the kept manifest id.
- Links: every relative `.md` target in the four guides exists; every `](Guides/…)` link in the README exists; 0 broken.
- Managed header, entry cue, addendum footer: one each in all four guides, the form factors guide's cue and footer under its new name; footer names unique.
- Gates: the two Figma guides emit no gate line and have no `## Gates`; they are conventions. The process guides' gate sections are untouched (their one changed sentence each is in § Mockups and in `C3` step 3), so the flow simulations recorded when their text was applied stand.
- Terms: `grep -i "Next Command|checkpoint|🟡|GitHub|human"` on the two Figma guides: 0 occurrences.
- Writing for people: the main guide's purpose-note passage keeps its writing-style pointer; the form factors guide tells no one to write prose.
- Working documents: neither Figma guide creates any.
- Skills: none added or changed; the manifest's skill entries are untouched.
- Change package verification (`internal/maintenance/change-packages.md`): no path, lifecycle, reopen, promotion order or archive step changed; design authoring and promotion each changed the words "target sizes" in one sentence. Migration coverage for open packages is in the migration above.
- Guide addenda contract: the guide's published lookup name changed with its file, and the release document moves a project's addendum to the new name unchanged and stops on a collision, as the contract asks for a rename. No user addendum is generated, edited or deleted.
- Tool tests: `internal/tests/tools/figma-page-check/test.py`: OK, 15 tests, one new, which fails without the script change.
- Guide placement: the renamed guide stays under `Guides/Design/`.

**Process suggestions** (for the supervisor):

1. `Guides/Process/process-refinement-guide.md`, § Size caps: say that the refiner never shortens a fix the reviewer shaped in order to meet a cap; it takes the reviewer's trims or brings the cap to the supervisor. Round 4's first finding was a phrase the refiner had cut for 15 bytes.
2. Same guide, § Scaling the ceremony, the structured tier's sweep: say the sweep covers every guide the change edits, the main target and the others alike. Round 3's sweep read only the form factors guide, and rounds 7 and 9 found the same class in the main guide.

### Reopened: No Concept Of Orientation (2026-11-18)

After the closure the supervisor read the report's line on a form factor's "other orientation" and ruled: a different orientation is a different form factor, defined in `Conventions` like any other, and the guides hold no concept of orientation at all. "You messed up with all of that. You need to fix it." The standard gained item 39.

What the pass had written, and where each came from:

| Text | Source | Now |
| --- | --- | --- |
| Rule 6: "An orientation that is not a form factor is drawn only for a screen with its own layout in it" | The second sentence of the scope's row 3, from the field notes of one project; reworded in round 3 to answer F3 | Deleted |
| Main guide, `Conventions`: "Its definition names devices or window widths and orientation" | The standard's item 25, the refiner's wording of the ruling that each form factor has a definition | "Its definition says what the name stands for." |
| Main guide, Frames rule 6: "Draw landscape designs at landscape size" | Round 3, changed from "A landscape design is a landscape form factor, not a rotated frame" to make room for rule 6's sentence | "A design that would need one is a form factor of its own." |
| Migration step 2: a definition written from the file's "frame size and orientation" | The release document | "its frame size; what the name stands for is the supervisor's to confirm" |

What went wrong in the method: round 3's F3 showed that the orientation sentence collided with the rule that every form factor gets a full set. The refiner kept the sentence and reworded a settled main guide rule to make room for it, where the collision was the sign that the sentence itself was wrong. Its only source was one project's notes, the same failure as the scope's row 7.

Sizes by `wc -c`: 5,391 of 5,540; 19,574 of 19,590. `grep -n -i "orientation|landscape|portrait"` over `Guides/Design`, `Releases/unreleased.md` and `Bin/figma-page-check.js`: 0 occurrences. Tests: 15 pass. A fresh round follows, in the same score series.

### Round 11

Prompt `reviews-f/f4-r11-prompt.md`. Report `reviews-f/f4-r11-out.md`. The reviewer changed no guide (checksums agree). **No findings**; it recommends no edits. Its limits are the same as round 10's: Figma's behavior judged from the standard's account, and the release document not read.

| Round | Score | Total defects | Irreversible | Divergent | Cosmetic | Noise |
| --- | --- | --- | --- | --- | --- | --- |
| r2 | 6.25 | 3 | 0 | 3 | 0 | 0 |
| r3 | 5.625 | 3 | 0 | 3 | 0 | 0 |
| r4 | 3.75 | 2 | 0 | 2 | 0 | 0 |
| r5 | 2.5 | 1 | 0 | 1 | 0 | 0 |
| r6 | 1.875 | 1 | 0 | 1 | 0 | 0 |
| r7 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r8 | 1.0 | 1 | 0 | 0 | 1 | 0 |
| r9 | 4.375 | 2 | 0 | 2 | 0 | 0 |
| r10 | 0 | 0 | 0 | 0 | 0 | 0 |
| r11 | 0 | 0 | 0 | 0 | 0 | 0 |

> nothing scored

**A fault in the order.** The orientation change was a change the supervisor directed after the pass had closed. The refiner added it to the standard, edited the guides, and then commissioned round 11 over the applied text. A change is drafted as a proposal and reviewed before it touches a guide; the refiner treated this one as a repair inside the pass and skipped that step. The supervisor asked whether the fixes went through refinement (2026-11-18). What did happen: the standard was updated first (item 39), and a fresh cold round read the changed text with the change described and found nothing. What did not: the reviewer never assessed it as a proposal. Whether the pass ends on round 11 or the change is taken out and redone as a proposal is the supervisor's to say.

Sizes by `wc -c`: 5,391 of 5,540; 19,574 of 19,590; 18,848 of 18,900; 13,347 of 13,350.

### Closure, After The Reopening

Supervisor, 2026-11-18, on the order fault: "OK good enough." The pass ends on round 11: a fresh round over the current text left nothing to apply, and the supervisor accepts that the orientation change was reviewed after it was applied.

Final sizes by `wc -c`: `figma-designer-guide-form-factors.md` 5,391 / 5,540; `figma-designer-guide.md` 19,574 / 19,590; `design-authoring.md` 18,848 / 18,900; `design-promotion.md` 13,347 / 13,350. Net change over the pass: +2,693, +574, 0 and −2. These replace the sizes in the first closure. Of the items logged and left there, "where a frame in an orientation that is no form factor sits" no longer applies.

### Maintenance Retro, Second Run (2026-11-18)

Scope: what changed after the first run, which is the orientation change (two guides, the migration's step 2, the standard). Each check, with its result:

- Release documents: the form factors entry and the `CHANGELOG.md` line say nothing the change made stale (read: "`Conventions` gives each form factor a name, a definition and a default frame size"); the migration's step 2 now has a definition written from the file's frame size, with what the name stands for the supervisor's to confirm. `grep -rn -i "orientation|landscape|portrait"` over `Guides/Design`, `README.md`, `Releases/unreleased.md`, `CHANGELOG.md` and `Bin/figma-page-check.js`: 0 occurrences.
- The standard: the 2026-11-18 amendment uses the word only in item 39, which records the ruling.
- Sizes: 5,391 / 19,574 / 18,848 / 13,347, all within cap.
- Old term or path (`grep -rn -i "multiple-sizes|target size|target-size|size page|size name"` over `Guides`, `README.md`, `Templates`, `Install`, `Bin`, `internal`, the manifest): 0 occurrences besides the kept manifest id.
- Links in the four guides and the README's guide links: 0 broken.
- `Managed-Updated-At`: all four read 2026-11-18, today's date by `date +%Y-%m-%d`.
- Manifest parses; unchanged since the first run.
- Sanity scan of the two edited guides: no gate text; no "human", "checkpoint" or "Next Command"; the main guide's writing-style pointer is in place.
- Tool test `figma-page-check`: OK, 15 tests.
- Nothing else in the first run's list is touched by this change (README, skills, update guide, installers, change package lifecycle, addenda contract).

No misses found. One process suggestion is added to the first run's two:

3. `Guides/Process/process-refinement-guide.md`, § Rounds and stopping: say that a change the supervisor asks for after a pass has closed is a change, proposed and reviewed before it is applied, and not a repair inside the closed pass.
