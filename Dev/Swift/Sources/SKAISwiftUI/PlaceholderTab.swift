import SwiftUI

/// One tab in a tabbed placeholder scene.
///
/// Each tab hosts a child scene's placeholder, so click-through exercises real
/// tab switching rather than a faked stack.
public struct PlaceholderTab: Identifiable {
    public let id = UUID()

    /// Tab label — the one the app's design or requirements give, else a sensible label.
    public let label: String

    /// SF Symbol name for the tab item. Use a base name with a `.fill` variant
    /// so iOS solidifies it when selected. If it doesn't resolve, the scene
    /// falls back to a default.
    public let systemImage: String

    /// The tab's case of the scene's tab route enum, matched against the
    /// `PlaceholderScene` selection binding; `nil` when the scene has no binding.
    public let route: AnyHashable?

    /// The tab's hosted child-scene placeholder (type-erased for array storage).
    public let content: AnyView

    public init(label: String, systemImage: String = "square", @ViewBuilder content: () -> some View) {
        self.label = label
        self.systemImage = systemImage
        self.route = nil
        self.content = AnyView(content())
    }

    /// A tab selected through its scene's tab route enum: `route` is this tab's case.
    public init<Route: Hashable>(label: String, systemImage: String = "square", route: Route, @ViewBuilder content: () -> some View) {
        self.label = label
        self.systemImage = systemImage
        self.route = AnyHashable(route)
        self.content = AnyView(content())
    }
}
