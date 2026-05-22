import SwiftUI

/// One entry in a placeholder scene's "Routes" menu.
///
/// Each route maps to an outgoing nav/modal destination. Selecting the menu item
/// runs `action`, which fires the route (e.g. sets a route property the scene owns).
public struct PlaceholderRoute: Identifiable {
    public let id = UUID()

    /// Menu-item label — the destination scene's name.
    public let label: String

    /// Fires the route. The scene owns whatever route state it uses
    /// (view model, `@State`, etc.); this closure decouples the placeholder from that.
    public let action: () -> Void

    public init(label: String, action: @escaping () -> Void) {
        self.label = label
        self.action = action
    }
}
