import SwiftUI

/// One tab in a tabbed placeholder scene.
///
/// Each tab hosts a child scene's placeholder, so click-through exercises real
/// tab switching rather than a faked stack.
public struct PlaceholderTab: Identifiable {
    public let id = UUID()

    /// Tab label — the child scene's name.
    public let label: String

    /// SF Symbol name for the tab item. Use a base name with a `.fill` variant
    /// so iOS solidifies it when selected. If it doesn't resolve, the scene
    /// falls back to a default.
    public let systemImage: String

    /// The tab's hosted child-scene placeholder (type-erased for array storage).
    public let content: AnyView

    public init(label: String, systemImage: String = "square", @ViewBuilder content: () -> some View) {
        self.label = label
        self.systemImage = systemImage
        self.content = AnyView(content())
    }
}
