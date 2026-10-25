# Product Specs — Suggestions | 001: Attention For Notebooks With Suggestions

[Review page](product-specs-review.html)

## Goal

Let the home view order notebooks by how much they need the owner, which needs attention to account for expiring suggestions, not only stage.

## Inputs

- The base: the Suggestions package, [its notes](../../product-specs-authoring.md) and drafts.
- The home view design.

## Mode

Scoped change.

## Discussion

The listed Inputs determine the drafts.

## Requirement Changes

- R1 modify requirement: [STAGE-09]
  - **Justification** Design: the home view orders notebooks by urgency, and a suggestion expiring tomorrow is more urgent than a Drafting entry with no suggestions.
  - **Touches** domains/workflow-stage.md
- R2 modify requirement: [STAGE-01]
  - **Justification** Catalog: the Drafting transition builds on the open question base D3, marked with a footnote.
  - **Touches** domains/workflow-stage.md

## Assumptions and TODOs

## Out of scope

## Verification

## Decision Log

[STAGE-09]: proposed-product-specs/domains/workflow-stage.md#stage-09
[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01
