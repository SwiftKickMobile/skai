import SwiftUI

/// The placeholder body for a UI Map scene. A scaffolded scene view's `body`
/// invokes this.
///
/// Every `PlaceholderScene` draws its own inset border, so nesting (embedded
/// composites/children, or tabs) reads as nested bordered boxes. Layout is
/// inferred from what's declared:
/// - **Leaf** (no embedded content, no tabs): centered title + Routes menu.
/// - **Container** (embedded children/composites and/or tabs): a header row
///   (title, Routes, dismiss) with the content below — embedded children stacked,
///   tabs as a real `TabView`; the two compose.
///
/// Shows the scene's name as a visible label, an optional "Routes" menu, and a
/// dismiss "✕" driven by `@Environment(\.dismiss)`.
public struct PlaceholderScene<EmbeddedContent: View>: View {

    // MARK: - API

    /// Scene with embedded composite/child content — optionally also tabbed.
    /// - Parameters:
    ///   - title: The scene's name (the visible identifier).
    ///   - routes: Outgoing nav/modal routes for the "Routes" menu; empty hides the menu.
    ///   - tabs: Tab children rendered as a real `TabView`; empty for a non-tabbed scene.
    ///   - embedded: Composite/child scene placeholders, instantiated directly; each is
    ///     itself a `PlaceholderScene` and carries its own border.
    public init(
        title: String,
        routes: [PlaceholderRoute] = [],
        tabs: [PlaceholderTab] = [],
        @ViewBuilder embedded: () -> EmbeddedContent
    ) {
        self.title = title
        self.routes = routes
        self.tabs = tabs
        self.embedded = embedded()
        self.hasEmbedded = true
    }

    /// Leaf scene (no embedded content) or a tabs-only container.
    public init(
        title: String,
        routes: [PlaceholderRoute] = [],
        tabs: [PlaceholderTab] = []
    ) where EmbeddedContent == EmptyView {
        self.title = title
        self.routes = routes
        self.tabs = tabs
        self.embedded = EmptyView()
        self.hasEmbedded = false
    }

    // MARK: - Constants

    private static var insetPadding: CGFloat { 6 }
    private static var contentPadding: CGFloat { 12 }
    private static var cornerRadius: CGFloat { 10 }
    /// Light-gray fill for composite scenes — mirrors the UI Map render's
    /// composite wrapper (`#f0f0f0`, no border).
    private static var compositeFill: Color { Color(white: 0xF0 / 255.0) }

    // MARK: - Variables

    private let title: String
    private let routes: [PlaceholderRoute]
    private let tabs: [PlaceholderTab]
    private let embedded: EmbeddedContent
    private let hasEmbedded: Bool

    @Environment(\.dismiss) private var dismiss
    @Environment(\.placeholderCrumbs) private var crumbs
    @Environment(\.placeholderShowsDismiss) private var showsDismiss

    @State private var breadcrumbScroll = ScrollPosition(edge: .trailing)

    // MARK: - Lifecycle

    public var body: some View {
        layout
            .background {
                if !isFullBleed {
                    RoundedRectangle(cornerRadius: Self.cornerRadius)
                        .fill(Self.compositeFill)
                }
            }
            .padding(isFullBleed ? 0 : Self.insetPadding)
            .modifier(InlineNavTitle(title: title, enabled: isFullBleed))
    }

    // MARK: - Layout

    /// A full-bleed scene fills edge-to-edge with no box border or inset gap.
    /// True when it carries breadcrumbs (a child host, tab, or nav push) or is
    /// presented modally. Only embedded/composite content (crumbs reset, not
    /// modal) keeps the bordered box.
    private var isFullBleed: Bool { !crumbs.isEmpty || showsDismiss }

    /// This scene's inherited crumbs plus itself — handed down to tab content so
    /// the breadcrumb accumulates through the tab boundary.
    private var effectiveCrumbs: [PlaceholderCrumb] {
        crumbs + [PlaceholderCrumb(title: title, routes: routes)]
    }

    @ViewBuilder
    private var layout: some View {
        if !tabs.isEmpty {
            // Tabbed: a full-bleed TabView owns the screen edges (tab bar at the
            // bottom). The breadcrumb is delegated to the tab content, which
            // accumulates this scene into its crumbs and renders it under its
            // own nav bar.
            tabView
        } else {
            VStack(alignment: .leading, spacing: 16) {
                breadcrumb
                if hasEmbedded {
                    embedded
                        .environment(\.placeholderCrumbs, [])
                        .environment(\.placeholderShowsDismiss, false)
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
            .padding(Self.contentPadding)
        }
    }

    private var breadcrumb: some View {
        HStack(spacing: 8) {
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 6) {
                    ForEach(crumbs) { crumb in
                        titleMenu(title: crumb.title, routes: crumb.routes)
                        Text("›").font(.headline).foregroundStyle(.secondary)
                    }
                    titleMenu(title: title, routes: routes)
                }
            }
            .scrollPosition($breadcrumbScroll)

            if showsDismiss {
                dismissButton
            }
        }
    }

    @ViewBuilder
    private func titleMenu(title: String, routes: [PlaceholderRoute]) -> some View {
        let visible = routes.filter { !$0.isCurrent }
        if visible.isEmpty {
            Text(title).font(.headline).foregroundStyle(.secondary)
        } else {
            Menu {
                ForEach(PlaceholderRouteKind.allCases, id: \.self) { kind in
                    let kindRoutes = visible.filter { $0.kind == kind }
                    if !kindRoutes.isEmpty {
                        Section(kind.title) {
                            ForEach(kindRoutes) { route in
                                Button(route.label) { route.action() }
                            }
                        }
                    }
                }
            } label: {
                Text(title).font(.headline)
            }
        }
    }

    private var tabView: some View {
        TabView {
            ForEach(tabs) { tab in
                tab.content
                    .environment(\.placeholderCrumbs, effectiveCrumbs)
                    .environment(\.placeholderShowsDismiss, false)
                    .tabItem { Label(tab.label, systemImage: "square.dashed") }
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    private var dismissButton: some View {
        Button {
            dismiss()
        } label: {
            Image(systemName: "xmark.circle.fill")
                .imageScale(.large)
                .foregroundStyle(.secondary)
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Dismiss")
    }
}

// MARK: - Nav title

/// Sets the scene's nav-bar title (inline on iOS). A no-op outside a
/// `NavigationStack`. `navigationBarTitleDisplayMode` is iOS-only, so it's
/// guarded for the package's macOS build.
private struct InlineNavTitle: ViewModifier {
    let title: String
    let enabled: Bool

    @ViewBuilder
    func body(content: Content) -> some View {
        if enabled {
            #if os(iOS)
            content
                .navigationTitle(title)
                .navigationBarTitleDisplayMode(.inline)
            #else
            content.navigationTitle(title)
            #endif
        } else {
            content
        }
    }
}

// MARK: - Previews

#Preview("Leaf") {
    PlaceholderScene(title: "Cancel Appointment")
}

#Preview("Leaf + routes") {
    PlaceholderScene(
        title: "Profile",
        routes: [
            PlaceholderRoute(label: "Debug", kind: .nav) {},
            PlaceholderRoute(label: "Web", kind: .nav) {},
        ]
    )
}

#Preview("Container") {
    PlaceholderScene(
        title: "Appointment Details",
        routes: [PlaceholderRoute(label: "Cancel Appointment", kind: .sheet) {}]
    ) {
        PlaceholderScene(title: "Thumbnail Slider")
        PlaceholderScene(title: "Record Warning")
    }
}

#Preview("Tabbed") {
    PlaceholderScene(
        title: "Main",
        tabs: [
            PlaceholderTab(label: "Home") { PlaceholderScene(title: "Home") },
            PlaceholderTab(label: "Library") { PlaceholderScene(title: "Library") },
        ]
    )
}

#Preview("Tabbed + embedded") {
    PlaceholderScene(
        title: "Pipeline",
        routes: [PlaceholderRoute(label: "Menu", kind: .nav) {}],
        tabs: [
            PlaceholderTab(label: "Appointments") { PlaceholderScene(title: "Appointments Stage") },
            PlaceholderTab(label: "Closed") { PlaceholderScene(title: "Closed Pipeline Stage") },
        ]
    ) {
        PlaceholderScene(title: "Header Banner")
    }
}
