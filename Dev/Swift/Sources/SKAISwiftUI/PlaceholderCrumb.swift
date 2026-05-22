import SwiftUI

/// One ancestor entry in a placeholder breadcrumb: a scene's title plus its
/// routes (surfaced as that title's menu).
///
/// Crumbs accumulate only across child-routing boundaries — where the child
/// renders full-bleed and the parent's box (and identity) would otherwise
/// disappear. Embedded/tab/composite content resets the chain, since its
/// nesting is already shown by the surrounding box.
struct PlaceholderCrumb: Identifiable {
    // Stable id (the title) so rebuilding the crumb each render doesn't churn
    // ForEach identity — which otherwise tears down and recreates the segment's
    // Menu, swallowing taps. Breadcrumb titles are distinct within a path.
    var id: String { title }
    let title: String
    let routes: [PlaceholderRoute]

    init(title: String, routes: [PlaceholderRoute] = []) {
        self.title = title
        self.routes = routes
    }
}

// MARK: - Environment

extension EnvironmentValues {
    var placeholderCrumbs: [PlaceholderCrumb] {
        get { self[PlaceholderCrumbsKey.self] }
        set { self[PlaceholderCrumbsKey.self] = newValue }
    }
}

private struct PlaceholderCrumbsKey: EnvironmentKey {
    static var defaultValue: [PlaceholderCrumb] { [] }
}

// MARK: - Crumb appender

public extension View {
    /// Appends a crumb to the placeholder breadcrumb for this view's subtree.
    ///
    /// The package injects crumbs automatically across child-host and tab
    /// boundaries, but `.navigationDestination` is host-applied, so a pushed
    /// scene doesn't inherit the nav owner's crumb. Apply this on the
    /// destination — passing the owner's title — so the pushed scene's
    /// breadcrumb includes it.
    func placeholderCrumb(_ title: String, routes: [PlaceholderRoute] = []) -> some View {
        modifier(PlaceholderCrumbAppender(title: title, routes: routes))
    }
}

private struct PlaceholderCrumbAppender: ViewModifier {
    @Environment(\.placeholderCrumbs) private var crumbs
    let title: String
    let routes: [PlaceholderRoute]

    func body(content: Content) -> some View {
        content.environment(\.placeholderCrumbs, crumbs + [PlaceholderCrumb(title: title, routes: routes)])
    }
}
