import SwiftUI

/// The presentation kind of a route — used to group the menu items into sections.
public enum PlaceholderRouteKind: String, CaseIterable {
    case nav
    case sheet
    case fullScreen
    case popover
    case child

    /// Title-case section header shown in the Routes menu.
    var title: String {
        switch self {
        case .nav: "Nav"
        case .sheet: "Sheet"
        case .fullScreen: "Full Screen"
        case .popover: "Popover"
        case .child: "Child"
        }
    }
}

/// One entry in a placeholder scene's "Routes" menu.
///
/// Each route maps to an outgoing destination. Selecting the menu item runs
/// `action`, which fires the route (e.g. sets a route property the scene owns).
public struct PlaceholderRoute: Identifiable {
    public let id = UUID()

    /// Menu-item label — the destination scene's name.
    public let label: String

    /// The route's presentation kind — groups the menu item into a section.
    public let kind: PlaceholderRouteKind

    /// When `true`, the route targets the currently-selected destination
    /// (e.g. the active child) and is omitted from the menu.
    public let isCurrent: Bool

    /// Fires the route. The scene owns whatever route state it uses
    /// (view model, `@State`, etc.); this closure decouples the placeholder from that.
    public let action: () -> Void

    public init(label: String, kind: PlaceholderRouteKind, isCurrent: Bool = false, action: @escaping () -> Void) {
        self.label = label
        self.kind = kind
        self.isCurrent = isCurrent
        self.action = action
    }
}
