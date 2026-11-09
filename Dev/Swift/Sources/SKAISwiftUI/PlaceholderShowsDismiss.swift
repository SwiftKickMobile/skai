import SwiftUI

public extension EnvironmentValues {
    /// Whether a placeholder scene should show its dismiss "✕".
    ///
    /// Default `false`: roots, full-bleed children, tabs of a non-modal scene,
    /// and composites have nothing to dismiss. Set `true` on a scene presented modally
    /// (`.sheet` / `.fullScreenCover` / `.popover`); set `false` on a scene
    /// pushed via `.navigationDestination` (the navigation back button dismisses
    /// it). `PlaceholderScene` resets it to `false` for its embedded content; its
    /// tab content inherits the scene's value.
    var placeholderShowsDismiss: Bool {
        get { self[PlaceholderShowsDismissKey.self] }
        set { self[PlaceholderShowsDismissKey.self] = newValue }
    }
}

private struct PlaceholderShowsDismissKey: EnvironmentKey {
    static var defaultValue: Bool { false }
}
