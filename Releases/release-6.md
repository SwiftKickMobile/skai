# Release 6 — 2026-09-04

- 2026-09-04 **Work-spec creation is now API-first Work Spec Design.** `Guides/Spec/work-spec-creation.md` keeps its installed path and id but now accepts open-ended inputs, fills gaps with agent proposals, maintains a complete changed-production-API sketch during Discussion, and has one supervisor approval before completing the design. The working artifact is now `<spec-name>-design.md` instead of `<spec-name>-plan.md`; requirements normalization, task-list authoring, formal phased mini-cycles, and `auto` were removed from this side of the workflow. Optional delivery slices appear only when activated.
- 2026-09-04 **Work-spec implementation now owns planning and continuous execution.** `Guides/Spec/work-spec-implementation.md` audits the approved design, creates the task list, stops once for supervisor approval, then executes without per-task gates. It preserves UI Map handoffs, mandatory non-view unit tests, agent-operated runtime UI verification, planned or unexpected human testing, and fresh completion evidence. Build, test, and runtime commands must be filled in `skai/integration.md` before planning.
- 2026-09-04 **Work-spec wrappers, README, and supporting guides aligned.** `skai-work-spec-creation` retains its installed name as the Work Spec Design entry point, while `skai-work-spec-implementation` now plans as well as builds. `Guides/Core/working-doc-conventions.md` uses `<spec-name>-design.md`, and `Guides/Process/process-refinement-guide.md` assigns task-list ownership only to implementation.
- 2026-09-04 **UI Map workflow documentation clarified.** The README now explains that architecture maintains a provisional proposed map during Discussion, derives typed changes only after decisions are resolved, and distinguishes Plan promotion from Build promotion. No installed UI Map asset changed.

**Migration:**
1. **Re-run every installed adapter.** This refreshes both work-spec skill wrappers and the managed work-spec, working-document, and process-refinement guides.
2. Use `<spec-name>-design.md` for new work-spec design artifacts; `<spec-name>-plan.md` is no longer the current convention.
3. Complete the build, test, and runtime command fields in `skai/integration.md` before using work-spec implementation.
4. No managed asset paths or ids changed, so no installed files need to be removed or renamed.
