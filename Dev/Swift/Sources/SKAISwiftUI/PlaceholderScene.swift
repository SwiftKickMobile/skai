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

    // MARK: - Variables

    private let title: String
    private let routes: [PlaceholderRoute]
    private let tabs: [PlaceholderTab]
    private let embedded: EmbeddedContent
    private let hasEmbedded: Bool

    @Environment(\.dismiss) private var dismiss

    // MARK: - Lifecycle

    public var body: some View {
        layout
            .overlay(alignment: .topTrailing) {
                dismissButton.padding(Self.contentPadding)
            }
            .overlay {
                RoundedRectangle(cornerRadius: Self.cornerRadius)
                    .strokeBorder(Color.secondary, lineWidth: 1)
            }
            .padding(Self.insetPadding)
    }

    // MARK: - Layout

    private var isLeaf: Bool { !hasEmbedded && tabs.isEmpty }

    @ViewBuilder
    private var layout: some View {
        if isLeaf {
            VStack(spacing: 16) {
                titleLabel
                routesMenu
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .padding(Self.contentPadding)
        } else {
            VStack(alignment: .leading, spacing: 16) {
                header
                if hasEmbedded { embedded }
                if !tabs.isEmpty { tabView }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
            .padding(Self.contentPadding)
        }
    }

    private var header: some View {
        HStack(spacing: 12) {
            titleLabel
            routesMenu
            Spacer(minLength: 0)
        }
    }

    private var titleLabel: some View {
        Text(title).font(.headline)
    }

    @ViewBuilder
    private var routesMenu: some View {
        if !routes.isEmpty {
            Menu("Routes") {
                ForEach(routes) { route in
                    Button(route.label) { route.action() }
                }
            }
        }
    }

    private var tabView: some View {
        TabView {
            ForEach(tabs) { tab in
                tab.content
                    .tabItem { Label(tab.label, systemImage: "square.dashed") }
            }
        }
        .frame(maxWidth: .infinity, minHeight: 240, maxHeight: .infinity)
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

// MARK: - Previews

#Preview("Leaf") {
    PlaceholderScene(title: "Cancel Appointment")
}

#Preview("Leaf + routes") {
    PlaceholderScene(
        title: "Profile",
        routes: [
            PlaceholderRoute(label: "Debug") {},
            PlaceholderRoute(label: "Web") {},
        ]
    )
}

#Preview("Container") {
    PlaceholderScene(
        title: "Appointment Details",
        routes: [PlaceholderRoute(label: "Cancel Appointment") {}]
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
        routes: [PlaceholderRoute(label: "Menu") {}],
        tabs: [
            PlaceholderTab(label: "Appointments") { PlaceholderScene(title: "Appointments Stage") },
            PlaceholderTab(label: "Closed") { PlaceholderScene(title: "Closed Pipeline Stage") },
        ]
    ) {
        PlaceholderScene(title: "Header Banner")
    }
}
