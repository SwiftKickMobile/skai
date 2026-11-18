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
