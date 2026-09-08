Managed-By: skai
Managed-Id: guide.unit-testing
Managed-Source: Guides/Test/unit-testing-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Unit Testing Guide

## Purpose

Orchestrates the unit testing workflow. This guide coordinates the overall process while delegating detailed execution to specialized sub-guides.

**Use Cases:**
- **Writing tests for a single type** - One test file, one source type
- **Writing tests for multiple types** - Multiple test files planned upfront, implemented sequentially
- **Adding new tests to existing suites** - Adding sections or tests to existing files
- **Fixing failing tests** - Addressing test failures in existing tests

**Multi-Type Testing:**
When testing multiple types in a single session:
1. **Plan all test files upfront** - Planning phase creates all test files with 🟡 sections
2. **Implement one file at a time** - Complete all sections in one file before moving to the next
3. **Sequential by file** - Aligns with work spec subtask structure

**Sub-guides:**
- **Planning**: `Guides/Test/unit-test-planning-guide.md`
- **Infrastructure**: `Guides/Test/unit-test-infrastructure-guide.md`
- **Writing & Execution**: `Guides/Test/unit-test-writing-guide.md`

## Gates

Core rule: every time the agent is waiting on the operator, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what was completed and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the operator.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the operator gives advance intent.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the operator resolves it.

Workflow-specific gate note:
- This guide is an orchestrator. Some planned gates are emitted by the planning/infrastructure/writing sub-guides. When a sub-guide stops at a gate, control returns here and the operator's response resumes the orchestrated testing flow.

Planned gates for this workflow:
- After planning is complete (all files/sections/tests are stubbed and marked 🟡 in the test files — see the Mixed marker model note below).
- After the global infrastructure review is complete for all planned tests (owned by the infrastructure sub-guide).
- Before running tests for a section (owned by the writing sub-guide).
- After test execution results are gathered for a section (owned by the writing sub-guide).
- At the end of `next auto`, if work remains or the run stopped early, to report what was completed vs what was skipped and why.

---

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the active workflow step below. Do not use them to skip phases or clear section markers early.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit operator resolution.
`auto to <target>` = auto-advance but STOP before the named workflow target. Use stable identifiers such as `<suite-name>` or `<suite-name>/<section-name>`.

Progress tracking (mixed marker model — both conventions apply):

This workflow uses both progress-marker conventions because it produces both kinds of artifact (see `Guides/Core/process-flow.md`, "Progress markers"):
- `- [ ]` / `- [x]` in the **orchestration document** (process artifact, markdown).
- `🟡` in the **test files** (in-code, where completion is removal of the marker as tests are written and pass).

Orchestration document:
- This workflow owns an orchestration document at `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md`.
- `session-name` is the required name for this overall testing effort on the current branch.
- The orchestration document is the parent workflow artifact and owns these gate/phase items:
  - `- [ ] Planning`
  - `- [ ] Infrastructure`
  - `- [ ] Writing`
- Planning seeds the orchestration document with these `- [ ]` phase items and creates the test files/sections/tests with `🟡` markers.
- At the planning gate, `- [ ] Planning` remains unchecked until the operator gives advance intent.
- At the infrastructure gate, `- [ ] Infrastructure` remains unchecked until the operator gives advance intent.
- `- [ ] Writing` remains unchecked until all planned sections across the testing session are complete and the operator gives advance intent at the final section-completion gate.
- If writing later discovers missing infrastructure, leave `- [ ] Writing` unchecked and uncheck `Infrastructure` again (`- [ ]`) in the orchestration document so the parent workflow clearly shows that another infrastructure pass is required.

Test files (in code):
- At section-level writing gates, the section's `🟡` marker (on the `// MARK:` comment in code) remains until the relevant writing-guide gate is approved.
- If a section is skipped because infrastructure remains missing or a non-trivial failure remains unresolved, leave that section's `🟡` marker in place.

Default rule: a progress marker (either `- [ ]` or `🟡`) means TODO or pending approval. Do not clear it without operator approval.

**Behavior:** This guide orchestrates the sub-guides. When a sub-process stops at a gate, control returns here and the operator's next response resumes the global workflow, whether that means entering infrastructure, continuing the current file's section writing, or deciding how to handle skipped work.

**Workflow-specific `auto` rules:**

- `auto` advances through all remaining work without stopping at planned gates.
- Complete the global infrastructure pass before starting section-by-section writing.
- In the orchestration document:
  - check `Planning` (`- [x]`) only after the planning gate is auto-approved.
  - check `Infrastructure` (`- [x]`) only after the infrastructure gate is auto-approved.
  - keep `Writing` unchecked (`- [ ]`) until all remaining sections in the testing session are actually complete.
- Skip and continue behavior:
  - **Missing infrastructure discovered during writing**: skip the affected tests/section, leave `🟡` markers in the test files, document what infrastructure is missing, and continue to the next section. Uncheck `Infrastructure` in the orchestration document if it was checked. At the next planned gate, the operator can decide whether to re-enter the infrastructure phase.
  - **Non-trivial test failure**: skip failing tests, leave `🟡` markers in the test files, document failure details, continue with remaining tests or next section.
- Auto-fixes allowed: obvious typos, missing imports, simple compilation errors.
- `auto to <target>` should use stable identifiers such as `<suite-name>` or `<suite-name>/<section-name>`. Do not use a bare section name by itself.
- If auto completes everything with no skipped work and no bounded target stop, finish with `🏁 Complete...`.
- If auto stops early because work remains, report which tests were completed and which were skipped (with reasons) at the planned gate.

---

## Workflow

**If you want to deviate from the process below, STOP and ask first.** Do not skip phases, reorder steps, or combine phases without explicit approval.

### Step 1: Planning

**Trigger:** Advance intent

**Process:**
1. Create the orchestration document for this workflow:
   - **Session name:** `<session-name>`
   - **Subpath:** `testing`
   - **File name:** `unit-testing.md`
   - **Full path:** `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md`
   - Start with `- [ ] Planning` in the checklist.
2. Execute `Guides/Test/unit-test-planning-guide.md`

**Output:**
- Test file(s) with sections marked `🟡` in code (in-code TODO indicators — see `Guides/Test/unit-test-planning-guide.md`).
- Orchestration document updated with:
  - `- [ ] Infrastructure`
  - `- [ ] Writing`

**Gate:** STOP with the planned gate line. Leave `- [ ] Planning` unchecked in the orchestration document. `Next` should say you will check `Planning` and begin the infrastructure pass for all planned tests.

---

### Step 2: Infrastructure (one pass for all planned tests)

**Trigger:** Advance intent

**For all planned tests in the current testing session:**

1. **Infrastructure pass**
   - Execute `Guides/Test/unit-test-infrastructure-guide.md` once for the whole testing session.
   - That guide covers **all planned sections/tests across all planned test files**, not one suite or one section at a time.
   - Follow the gates defined in that guide.
   - Advance intent after infrastructure completion → check `Infrastructure` (`- [x]`) in the orchestration document and proceed to section writing.

---

### Step 3: Section Writing & Execution (repeat per section, file-by-file)

**Trigger:** Advance intent

**For each section marked `🟡` in the current test file:**

1. **Writing & Execution Phase**
   - Execute `Guides/Test/unit-test-writing-guide.md` for this section.
   - Follow the gates defined in that guide.
   - When the writing guide reaches the post-results gate:
     - if the section passed, advance intent completes that section.
     - if the section stopped with skipped tests due to missing infrastructure, advance intent returns control here with that section still marked `🟡`.

2. **Section complete**
   - Remove the `🟡` from the completed section's MARK in the test file only after the operator gives advance intent at the relevant gate.
   - If no `🟡` sections remain anywhere, check `Writing` (`- [x]`) in the orchestration document only after that final advance intent and complete the workflow.

**Repeat:** Finish the current file before moving to the next file:
- Find the next `🟡` section in the current file and repeat Step 3.
- If the current file has no remaining runnable sections, the operator may decide at the next planned gate whether to re-enter infrastructure or move to the next file.
- Move to the next file only after the current file's remaining work is either completed or explicitly deferred by the operator.

---

## Work Documents

Created during implementation, following `Guides/Core/working-doc-conventions.md`:

**Orchestration document (owned by this guide):**
- **Subpath:** `testing`
- **File name:** `unit-testing.md`
- **Full path:** `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md`
- **Purpose:** Tracks parent-workflow progress across planning, one global infrastructure pass, and overall writing completion.
- **Structure:**
  ```markdown
  # Unit Testing
  
  ## Context
  This document tracks the overall unit-testing workflow for [scope].
  
  ## Checklist
  
  - [ ] Planning
  - [ ] Infrastructure
  - [ ] Writing
  
  ## Notes
  
  - [High-level status, skips, or handoff notes]
  ```

**Sub-guide documents:**
- Infrastructure guide: `skai/working-docs/<branch-path>/<session-name>/testing/infrastructure.md`
- Writing guide: per-section writing/execution document under `skai/working-docs/<branch-path>/<session-name>/testing/<suite-name>/`

---

## Example Workflow

### Single Type (One Test File)

```
--- Planning ---
Operator: "begin"
AI: [Creates `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md` with `- [ ] Planning`]
AI: [Creates TemplateRendererTests.swift with sections:
     - Render Success Tests 🟡
     - Error Handling Tests 🟡]
AI: [Adds `- [ ] Infrastructure` and `- [ ] Writing` to `unit-testing.md`]
AI: [⏳ GATE: Next: Begin the infrastructure pass for all planned tests.]

--- Infrastructure ---
Operator: "next"
AI: [Checks `Planning` in `unit-testing.md`]
AI: [Executes infrastructure guide for all planned tests in the session]
AI: [⏳ GATE emitted by infrastructure guide]
Operator: "next"
AI: [Checks `Infrastructure` in `unit-testing.md`]
AI: [Marks infrastructure complete, proceeds to first section]

--- Section 1 ---
Operator: "next"
AI: [Finds first 🟡 section: Render Success Tests]
AI: [Implements tests]
AI: [⏳ GATE emitted by writing guide before running tests]
Operator: "next"
AI: [Runs tests, documents results]
AI: [⏳ GATE emitted by writing guide with test results]
Operator: "next"
AI: [Removes 🟡 from Render Success Tests]

--- Section 2 ---
Operator: "next"
AI: [Finds next 🟡 section: Error Handling Tests]
...
[Continues until all sections complete]

--- Done ---
Operator: "next"
AI: [Checks `Writing` in `unit-testing.md`]
AI: "🏁 Complete. Let me know if anything needs adjustment."
```

### Multiple Types (Multiple Test Files)

```
--- Planning (creates ALL test files upfront) ---
Operator: "begin"
AI: [Creates `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md` with `- [ ] Planning`]
AI: [Creates PlaceholderParserTests.swift with sections:
     - Doc Placeholder Tests 🟡
     - Fragment Placeholder Tests 🟡]
AI: [Creates MarkdownTokenizerTests.swift with sections:
     - Heading Tests 🟡
     - Code Fence Tests 🟡]
AI: [Creates TemplateRendererTests.swift with sections:
     - Render Success Tests 🟡
     - Error Handling Tests 🟡]
AI: [Adds `- [ ] Infrastructure` and `- [ ] Writing` to `unit-testing.md`]
AI: [⏳ GATE: Next: Begin the infrastructure pass for all planned tests.]

--- Infrastructure ---
Operator: "next"
AI: [Checks `Planning` in `unit-testing.md`]
AI: [Executes infrastructure guide for all planned tests across all planned test files]
AI: [⏳ GATE emitted by infrastructure guide]
Operator: "next"
AI: [Checks `Infrastructure` in `unit-testing.md`]

--- File 1: PlaceholderParserTests ---
Operator: "next"
AI: [Finds first 🟡 section in first file: Doc Placeholder Tests]
...
[Completes all sections in PlaceholderParserTests]

--- File 2: MarkdownTokenizerTests (after File 1 is complete) ---
Operator: "next"
AI: [Moves to first 🟡 section in next file: Heading Tests]
...
[Completes all sections in MarkdownTokenizerTests]

--- File 3: TemplateRendererTests (after File 2 is complete) ---
Operator: "next"
AI: [Moves to first 🟡 section in final file: Render Success Tests]
...
[Completes all sections]

--- Done ---
Operator: "next"
AI: [Checks `Writing` in `unit-testing.md`]
AI: "🏁 Complete. Let me know if anything needs adjustment."
```

### Using "next auto"

```
Operator: "next auto"
AI: [Creates/updates `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md`, auto-checks `- [x] Planning`, completes the global infrastructure pass, auto-checks `- [x] Infrastructure`]
AI: [Completes all Feature B Tests - infrastructure already covered, all pass]
AI: [Completes all Helper Tests - infrastructure already covered, all pass]
AI: [Encounters Feature C Tests - missing infrastructure was not identified earlier]
AI: [Skips all Feature C Tests, leaves section 🟡 markers in place in the test files, unchecks `- [ ] Infrastructure` in the orchestration doc, documents missing infrastructure needs]
AI: [Completes 3 of 5 Feature D Tests - 2 fail with unclear logic]
AI: [Removes 🟡 from 3 passing tests, keeps 🟡 on 2 failing, leaves `- [ ] Writing` unchecked, documents failures]
AI: [Completes all Feature E Tests - no infrastructure, all pass]
AI: "Auto-advance complete. Completed: B (5/5), Helper (3/3), D (3/5), E (4/4). Skipped: C (0/6 - missing infrastructure discovered during writing), D (2/5 - test failures)"
Operator: [Reviews skipped tests]
Operator: "next"
AI: [At the next planned gate, the operator decides to re-enter infrastructure; the agent runs the infrastructure pass for the missing pieces, checks `Infrastructure` again, and then resumes section writing]
```

---

## Quick Reference

**Sub-guides:**
- Planning: `Guides/Test/unit-test-planning-guide.md`
- Infrastructure: `Guides/Test/unit-test-infrastructure-guide.md`
- Writing & Execution: `Guides/Test/unit-test-writing-guide.md`

**Parent progress artifact:**
- `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md`
