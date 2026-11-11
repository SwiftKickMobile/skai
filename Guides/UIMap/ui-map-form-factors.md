Managed-By: skai
Managed-Id: guide.ui-map-form-factors
Managed-Source: Guides/UIMap/ui-map-form-factors.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# UI Map — Form Factors

Print `📖 SKAI guide: ui-map-form-factors` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

This [`ui-map-guide.md`](ui-map-guide.md) companion covers form factors (phone, tablet, …). Read it when the map declares `form_factors` or work adds a screen or route that differs by form factor.

## Marking

A map may list project `form_factors` at top level; without it nothing is marked and the map reads as before. Unmarked means every form factor:

- A screen not on every form factor declares `form_factor: [...]` on its definition.
- A route with its own form factors is a `to:` entry: `to:` names the destination, `form_factor` lists where it is used, and `scene:` holds its fields when defining it. Bare names remain references and single-key mappings definitions. An unmarked route is used wherever both ends exist.
- `modal_style` is a string for every form factor or a map from form factor to style.

```yaml
version: 1
app: Darts
modal_styles: [full_screen, card]
form_factors: [phone, tablet]

domains:
  game:
    nav:
      - to: log # pushed on a phone
        form_factor: [phone]
    modal:
      - to: log # a card on a tablet; defines log
        form_factor: [tablet]
        scene:
          modal_style: card
      - settings:
          modal_style: { phone: full_screen, tablet: card }
      - rounds: # exists only on a tablet
          form_factor: [tablet]
          modal_style: card
```

The renderer rejects routes marked outside their source's or destination's form factors, non-root screens whose `form_factor` doesn't match where routes reach them, and `modal_style` maps without a style for exactly the form factors on which a modal route presents the screen. Each error names the conflict and, for an unmarked partially reachable screen, the `form_factor` to declare. Resolve against the intended screens and routes, never by copying the message.

## Code

SKAI sets no form-factor coding rule. The project's pattern is in this guide's addendum or a project document it points to. Before writing or auditing code for anything that differs by form factor (screen, route or modal style), find it; if missing, STOP in Discussion at a blocked gate and work with the supervisor to add it there, not to the implementation addendum.

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-form-factors-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
