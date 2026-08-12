import SwiftUI

/// Shared color palette for placeholder scenes.
///
/// The domain colors mirror the UI Map render's `DOMAIN_PALETTE`
/// (`Bin/ui-map-render.py`) in declaration order, so a scaffolded scene's tint
/// matches its node color in the rendered map. `composite` is the light-gray
/// fill the render uses for composite wrappers.
///
/// Values are duplicated from the render script's palette for now; deduplication
/// is a later concern.
public enum Colors {
    /// The domain palette, mirroring the render's `DOMAIN_PALETTE`
    /// (`Bin/ui-map-render.py`) by index — not by name.
    private static let palette: [Color] = [
        0x8AD1FA, 0xEFD74E, 0xFE9CA8, 0x78DB85, 0xD39AE7,
        0xFFB677, 0x87AFFF, 0x37D8CB, 0xF277D5,
    ].map(rgb)

    /// The tint for the domain at `index` (its declaration order in the map),
    /// so a scaffolded scene's `domainColor` matches its node in the rendered
    /// map. Wraps if there are more domains than palette slots, as the render does.
    public static func domain(at index: Int) -> Color { palette[index % palette.count] }

    /// Light-gray fill for composite scenes — mirrors the render's composite
    /// wrapper (`#f0f0f0`, no border).
    public static let composite = Color(white: 0xF0 / 255.0)

    private static func rgb(_ hex: Int) -> Color {
        Color(red: Double((hex >> 16) & 0xFF) / 255.0,
              green: Double((hex >> 8) & 0xFF) / 255.0,
              blue: Double(hex & 0xFF) / 255.0)
    }
}
