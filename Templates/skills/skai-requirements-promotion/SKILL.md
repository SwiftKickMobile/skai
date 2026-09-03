---
name: skai-requirements-promotion
description: Promotes an approved requirements change package into the canonical catalog (readiness screen, checklisted verification with evidence, and change requests when the catalog itself is wrong). Use when the user asks to promote requirements or land a requirements package.
---

# SKAI: Requirements promotion

## Instructions

- Read `Submodules/skai/Guides/Requirements/requirements-promotion.md` and follow it.
- Read `Submodules/skai/Guides/Requirements/requirements-catalog.md` — the writing-style rules run against it.
- Resolve the catalog root from `skai/integration.md`; a local catalog defaults to `skai/requirements/`. Never fall back to a root-level `requirements/` path.
- Preserve its hard boundaries: never rewrite a requirement's prose — a failing check blocks and returns the package to authoring; write nothing to the catalog before the Promotion Checks gate advances; reset every check on re-run rather than resuming mid-list.
