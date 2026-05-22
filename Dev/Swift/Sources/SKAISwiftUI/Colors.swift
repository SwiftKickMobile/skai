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
    public static let app = Color(red: 138.0 / 255.0, green: 209.0 / 255.0, blue: 250.0 / 255.0)     // #8AD1FA
    public static let library = Color(red: 239.0 / 255.0, green: 215.0 / 255.0, blue: 78.0 / 255.0)  // #EFD74E
    public static let note = Color(red: 254.0 / 255.0, green: 156.0 / 255.0, blue: 168.0 / 255.0)    // #FE9CA8
    public static let other = Color(red: 120.0 / 255.0, green: 219.0 / 255.0, blue: 133.0 / 255.0)   // #78DB85
    public static let common = Color(red: 211.0 / 255.0, green: 154.0 / 255.0, blue: 231.0 / 255.0)  // #D39AE7

    /// Light-gray fill for composite scenes — mirrors the render's composite
    /// wrapper (`#f0f0f0`, no border).
    public static let composite = Color(white: 0xF0 / 255.0)
}
