import SwiftUI

/// Hosts a child-routed scene full-bleed.
///
/// A child route replaces the parent's content entirely, so the parent draws no
/// box of its own. Instead it renders the selected child filling the available
/// space and appends its identity (title + child-switcher routes) to the
/// breadcrumb the child shows, so the parent stays reachable.
public struct PlaceholderChildHost<Content: View>: View {

    // MARK: - API

    public init(
        title: String,
        routes: [PlaceholderRoute] = [],
        @ViewBuilder content: () -> Content
    ) {
        self.title = title
        self.routes = routes
        self.content = content()
    }

    // MARK: - Constants

    // MARK: - Variables

    private let title: String
    private let routes: [PlaceholderRoute]
    private let content: Content

    @Environment(\.placeholderCrumbs) private var crumbs

    // MARK: - Lifecycle

    public var body: some View {
        content
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .environment(\.placeholderCrumbs, crumbs + [PlaceholderCrumb(title: title, routes: routes)])
    }
}
