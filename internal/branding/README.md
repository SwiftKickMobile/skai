# SKAI branding

The canonical artwork is SVG:

- [Symbol](skai-symbol.svg)
- [Mac app icon](skai-app-icon.svg): the same symbol centered on a rounded-square white backplate.
- [Light-background wordmark](skai-logo.svg)
- [Dark-background wordmark](skai-logo-dark.svg)

The flat ribbon retains its angular peaks, vertical sides and rounded cutouts. The three
straight diagonal bands have the same 200-unit perpendicular width. Opposing contours are
exact 180-degree copies; both cutouts have matching radii. Top and bottom tips use
circular fillets tangent to the adjoining straight edges. Width equality applies to the
straight bands, rather than forcing the entire silhouette into a monoline stroke.
All exports are centered using visible path bounds, not nominal drawing coordinates. Wordmark
exports have equal outer ink margins; the Mac icon centers the symbol inside its backplate.
Both wordmarks reuse the same symbol geometry. Letterforms are outlined, so viewing needs no font.

Palette: cyan `#009DDE` and magenta `#A1268C` from the
[SwiftKick logo](https://swiftkick.ai/assets/images/logo.svg), with their intermediate blend for the ribbon.
The brand symbol and wordmarks contain no shading, grain, external images or background panels.
The separate Mac icon intentionally adds a rounded-square white backplate.

Regenerate vectors with `swift generate.swift .` from this directory on a Mac. PNG files are derived
exports; the Mac app build packages the separate app-icon export into its standard ICNS sizes.
Export the symbol at 1024×1024 and the wordmarks at 2000 pixels wide using an existing SVG renderer
when vectors change; keep those PNG exports in sync. The prototype exports used the existing
workspace Sharp renderer; no renderer is required to run the prebuilt app.

The source geometry is maintained in [generate.swift](generate.swift). Artwork edits do not change
project configuration or installed components.
