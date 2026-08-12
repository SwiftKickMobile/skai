import SwiftUI
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

/// The placeholder body for a UI Map scene. A scaffolded scene view's `body`
/// invokes this.
///
/// Root, pushed, modal, child-hosted, and tab scenes render full-bleed. A scene
/// embedded as composite content draws an inset fill so the nesting remains
/// visible. Layout is inferred from the declared routes, tabs, and content.
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
        domainColor: Color = .accentColor,
        routes: [PlaceholderRoute] = [],
        tabs: [PlaceholderTab] = [],
        @ViewBuilder embedded: () -> EmbeddedContent
    ) {
        self.title = title
        self.domainColor = domainColor
        self.routes = routes
        self.tabs = tabs
        self.embedded = embedded()
        self.hasEmbedded = true
    }

    /// Leaf scene (no embedded content) or a tabs-only container.
    public init(
        title: String,
        domainColor: Color = .accentColor,
        routes: [PlaceholderRoute] = [],
        tabs: [PlaceholderTab] = []
    ) where EmbeddedContent == EmptyView {
        self.title = title
        self.domainColor = domainColor
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
    private let domainColor: Color
    private let routes: [PlaceholderRoute]
    private let tabs: [PlaceholderTab]
    private let embedded: EmbeddedContent
    private let hasEmbedded: Bool

    @Environment(\.dismiss) private var dismiss
    @Environment(\.placeholderCrumbs) private var crumbs
    @Environment(\.placeholderIsEmbedded) private var isEmbedded
    @Environment(\.placeholderShowsDismiss) private var showsDismiss

    @State private var breadcrumbScroll = ScrollPosition(edge: .trailing)

    // MARK: - Lifecycle

    public var body: some View {
        layout
            .background {
                if !isFullBleed {
                    RoundedRectangle(cornerRadius: Self.cornerRadius)
                        .fill(Colors.composite)
                }
            }
            .padding(isFullBleed ? 0 : Self.insetPadding)
            .modifier(InlineNavTitle(title: title, enabled: isFullBleed))
            .tint(domainColor)
    }

    // MARK: - Layout

    /// A full-bleed scene fills edge-to-edge with no box border or inset gap.
    /// Composite children are inset; presentation boundaries and destinations
    /// are full-bleed. Breadcrumbs/dismiss context takes precedence when a scene
    /// nested in a composite presents another destination.
    private var isFullBleed: Bool { !isEmbedded || !crumbs.isEmpty || showsDismiss }

    /// This scene's inherited crumbs plus itself — handed down to tab content so
    /// the breadcrumb accumulates through the tab boundary.
    private var effectiveCrumbs: [PlaceholderCrumb] {
        crumbs + [PlaceholderCrumb(title: title, color: domainColor, routes: routes)]
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
                        .environment(\.placeholderIsEmbedded, true)
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
                        titleMenu(title: crumb.title, routes: crumb.routes, color: crumb.color)
                        Text("›").font(.headline).foregroundStyle(.secondary)
                    }
                    titleMenu(title: title, routes: routes, color: domainColor)
                }
            }
            .scrollPosition($breadcrumbScroll)

            if showsDismiss {
                dismissButton
            }
        }
    }

    @ViewBuilder
    private func titleMenu(title: String, routes: [PlaceholderRoute], color: Color) -> some View {
        let visible = routes.filter { !$0.isCurrent }
        let pill = Text(title)
            .font(.subheadline)
            .foregroundStyle(.black)
            .padding(.vertical, 3)
            .padding(.horizontal, 8)
            .background(RoundedRectangle(cornerRadius: 8).fill(color))
        if visible.isEmpty {
            pill.opacity(0.5)
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
                pill
            }
        }
    }

    private var tabView: some View {
        TabView {
            ForEach(tabs) { tab in
                tab.content
                    .environment(\.placeholderCrumbs, effectiveCrumbs)
                    .environment(\.placeholderShowsDismiss, false)
                    .tabItem { Label(tab.label, systemImage: resolvedSymbol(tab.systemImage)) }
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    /// Returns `name` if it's a real SF Symbol, else the default — guards against
    /// a scaffold picking a symbol that doesn't exist (which would render blank).
    private func resolvedSymbol(_ name: String) -> String {
        #if canImport(UIKit)
        return UIImage(systemName: name) != nil ? name : "square"
        #elseif canImport(AppKit)
        return NSImage(systemSymbolName: name, accessibilityDescription: nil) != nil ? name : "square"
        #else
        return name
        #endif
    }

    private var dismissButton: some View {
        Button {
            dismiss()
        } label: {
            Image(systemName: "xmark")
                .font(.caption.weight(.bold))
                .foregroundStyle(.black)
                .padding(7)
                .background(Circle().fill(domainColor))
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Dismiss")
    }
}

private struct PlaceholderIsEmbeddedKey: EnvironmentKey {
    static let defaultValue = false
}

private extension EnvironmentValues {
    var placeholderIsEmbedded: Bool {
        get { self[PlaceholderIsEmbeddedKey.self] }
        set { self[PlaceholderIsEmbeddedKey.self] = newValue }
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
