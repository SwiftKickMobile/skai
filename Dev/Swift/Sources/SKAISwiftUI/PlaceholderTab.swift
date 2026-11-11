import SwiftUI

/// One tab in a tabbed placeholder scene.
///
/// Each tab hosts a child scene's placeholder, so click-through exercises real
/// tab switching rather than a faked stack.
public struct PlaceholderTab: Identifiable {
    /// The tab's case of the scene's tab route enum. A route's identity is its
    /// whole value, so it stays the same across redraws and SwiftUI keeps the
    /// tab's content and its state; selecting the tab sets the scene's
    /// `selection` binding to it.
    public let id: AnyHashable

    /// Tab label — the child scene's name.
    public let label: String

    /// SF Symbol name for the tab item. Use a base name with a `.fill` variant
    /// so iOS solidifies it when selected. If it doesn't resolve, the scene
    /// falls back to a default.
    public let systemImage: String

    /// The tab's hosted child-scene placeholder (type-erased for array storage).
    public let content: AnyView

    public init(label: String, systemImage: String = "square", route: some Hashable, @ViewBuilder content: () -> some View) {
        self.id = AnyHashable(route)
        self.label = label
        self.systemImage = systemImage
        self.content = AnyView(content())
    }
}
