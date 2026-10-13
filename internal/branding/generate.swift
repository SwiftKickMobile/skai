import Foundation
import CoreGraphics
import CoreText

// Angular ribbon: equal perpendicular widths for the three straight diagonal bands.
// Outer corners and rounded cutouts remain independently shaped, rather than stroked.
let canvas: CGFloat = 1200
let center = canvas / 2
let bandWidth: CGFloat = 200
let slope = tan(CGFloat.pi / 6)
let diagonalOffset = bandWidth / cos(CGFloat.pi / 6)
let peakY: CGFloat = 100
let peakCornerRadius: CGFloat = 100
let upperPeakCenter = CGPoint(x: center, y: peakY + 2 * peakCornerRadius / sqrt(3))
let lowerPeakCenter = CGPoint(x: center, y: canvas - upperPeakCenter.y)
let upperInnerY = peakY + diagonalOffset
let middleUpperY = center - diagonalOffset / 2
let cutoutRadius = (middleUpperY - upperInnerY) * cos(CGFloat.pi / 6) / 2
let notchCenter = CGPoint(x: 560, y: (upperInnerY + middleUpperY) / 2 + slope * (560 - center))
let normal = CGPoint(x: -0.5, y: sqrt(3) / 2)
let direction = CGPoint(x: sqrt(3) / 2, y: 0.5)
let upperTangent = CGPoint(x: notchCenter.x - cutoutRadius * normal.x, y: notchCenter.y - cutoutRadius * normal.y)
let lowerTangent = CGPoint(x: notchCenter.x + cutoutRadius * normal.x, y: notchCenter.y + cutoutRadius * normal.y)
let notchTip = CGPoint(x: notchCenter.x - cutoutRadius * direction.x, y: notchCenter.y - cutoutRadius * direction.y)
let k: CGFloat = 0.552284749831
func shifted(_ p: CGPoint, _ v: CGPoint, _ amount: CGFloat) -> CGPoint {
    CGPoint(x: p.x + v.x * amount, y: p.y + v.y * amount)
}
let half = CGMutablePath()
// A circular fillet meets each diagonal tangentially; no protruding tip.
half.move(to: CGPoint(x: center, y: upperPeakCenter.y - peakCornerRadius))
half.addArc(center: upperPeakCenter, radius: peakCornerRadius, startAngle: -.pi / 2, endAngle: -.pi / 3, clockwise: false)
half.addLine(to: CGPoint(x: 910, y: peakY + 310 * slope))
half.addCurve(to: CGPoint(x: 955, y: 357), control1: CGPoint(x: 943, y: 298), control2: CGPoint(x: 955, y: 318))
half.addLine(to: CGPoint(x: 955, y: 422))
half.addCurve(to: CGPoint(x: 870, y: upperInnerY + 270 * slope), control1: CGPoint(x: 955, y: 507), control2: CGPoint(x: 930, y: upperInnerY + 330 * slope))
half.addLine(to: upperTangent)
half.addCurve(to: notchTip, control1: shifted(upperTangent, direction, -cutoutRadius * k), control2: shifted(notchTip, normal, -cutoutRadius * k))
half.addCurve(to: lowerTangent, control1: shifted(notchTip, normal, cutoutRadius * k), control2: shifted(lowerTangent, direction, -cutoutRadius * k))
half.addLine(to: CGPoint(x: 910, y: middleUpperY + 310 * slope))
half.addCurve(to: CGPoint(x: 955, y: 741.5), control1: CGPoint(x: 943, y: middleUpperY + 343 * slope), control2: CGPoint(x: 955, y: 702.5))
half.addLine(to: CGPoint(x: 955, y: 843))
half.addCurve(to: CGPoint(x: 910, y: 1200 - peakY - 310 * slope), control1: CGPoint(x: 955, y: 882), control2: CGPoint(x: 943, y: 902))
half.addLine(to: CGPoint(x: center + peakCornerRadius / 2, y: lowerPeakCenter.y + peakCornerRadius * sqrt(3) / 2))
half.addArc(center: lowerPeakCenter, radius: peakCornerRadius, startAngle: .pi / 3, endAngle: .pi / 2, clockwise: false)
var rotation = CGAffineTransform(translationX: center, y: center).rotated(by: .pi).translatedBy(x: -center, y: -center)
let opposite = half.copy(using: &rotation)!
let outline = CGMutablePath()
outline.addPath(half)
opposite.applyWithBlock { pointer in
    let e = pointer.pointee
    switch e.type {
    case .moveToPoint: break // Already at the rotated starting point.
    case .addLineToPoint: outline.addLine(to: e.points[0])
    case .addCurveToPoint: outline.addCurve(to: e.points[2], control1: e.points[0], control2: e.points[1])
    default: fatalError("Unexpected angular contour element")
    }
}
outline.closeSubpath()
let cap = CGMutablePath()
cap.move(to: CGPoint(x: 0, y: 0))
cap.addLine(to: CGPoint(x: 1200, y: 0))
cap.addLine(to: CGPoint(x: 1200, y: middleUpperY + 600 * slope))
cap.addLine(to: lowerTangent)
cap.addLine(to: CGPoint(x: 320, y: middleUpperY - 280 * slope))
cap.addCurve(to: CGPoint(x: 290, y: 279), control1: CGPoint(x: 290, y: 310), control2: CGPoint(x: 285, y: 290))
cap.addLine(to: CGPoint(x: 0, y: 0))
cap.closeSubpath()
let visibleBounds = outline.boundingBoxOfPath
let scale: CGFloat = 1 // Preserve the established size; only the two tip curves change.
let offsetX = center - scale * visibleBounds.midX
let offsetY = center - scale * visibleBounds.midY
let normalizedBounds = CGRect(x: offsetX + scale * visibleBounds.minX, y: offsetY + scale * visibleBounds.minY,
                              width: scale * visibleBounds.width, height: scale * visibleBounds.height)

func svgPath(_ path: CGPath) -> String {
    func point(_ value: CGPoint) -> String { String(format: "%.3f %.3f", value.x, value.y) }
    var parts: [String] = []
    path.applyWithBlock { pointer in
        let element = pointer.pointee
        switch element.type {
        case .moveToPoint: parts.append("M " + point(element.points[0]))
        case .addLineToPoint: parts.append("L " + point(element.points[0]))
        case .addQuadCurveToPoint: parts.append("Q " + point(element.points[0]) + " " + point(element.points[1]))
        case .addCurveToPoint: parts.append("C " + point(element.points[0]) + " " + point(element.points[1]) + " " + point(element.points[2]))
        case .closeSubpath: parts.append("Z")
        @unknown default: fatalError("Unsupported path element")
        }
    }
    return parts.joined(separator: " ")
}

let definitions = """
<defs>
  <path id="half-outline" d="\(svgPath(outline))"/>
  <path id="cap-outline" d="\(svgPath(cap))"/>
  <clipPath id="silhouette">
    <use href="#half-outline"/>
  </clipPath>
  <clipPath id="upper-face"><use href="#cap-outline"/></clipPath>
  <clipPath id="lower-face"><use href="#cap-outline" transform="rotate(180 600 600)"/></clipPath>
  <linearGradient id="body" x1="220" y1="200" x2="960" y2="1100" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#009DDE"/>
    <stop offset="0.48" stop-color="#504185"/>
    <stop offset="1" stop-color="#A1268C"/>
  </linearGradient>

</defs>
"""
let symbol = """
<g transform="translate(\(offsetX) \(offsetY)) scale(\(scale))">
<g id="skai-symbol" clip-path="url(#silhouette)">
  <rect width="1200" height="1200" fill="url(#body)"/>
  <g clip-path="url(#upper-face)"><rect width="1200" height="1200" fill="#009DDE"/></g>
  <g clip-path="url(#lower-face)"><rect width="1200" height="1200" fill="#A1268C"/></g>
</g>
</g>
"""
let font = CTFontCreateWithName("HelveticaNeue-Bold" as CFString, 720, nil)
var cursor: CGFloat = 0
var letters: [String] = []
var wordBounds = CGRect.null
for character in "SKAI".utf16 {
    var code = character
    var glyph: CGGlyph = 0
    guard CTFontGetGlyphsForCharacters(font, &code, &glyph, 1), let path = CTFontCreatePathForGlyph(font, glyph, nil) else { fatalError("Missing wordmark glyph") }
    wordBounds = wordBounds.union(path.boundingBoxOfPath.offsetBy(dx: cursor, dy: 0))
    letters.append("<path transform=\"translate(\(String(format: "%.3f", cursor)) 0)\" d=\"\(svgPath(path))\"/>")
    var advance = CGSize.zero
    CTFontGetAdvancesForGlyphs(font, .horizontal, &glyph, &advance, 1)
    cursor += advance.width + 12
}
let baseline = center + wordBounds.midY
let symbolShift = 80 - normalizedBounds.minX
let wordX = symbolShift + normalizedBounds.maxX + 96 - wordBounds.minX
let width = Int(ceil(wordX + wordBounds.maxX + 80))
func document(_ content: String, width: Int, title: String) -> String {
    """
    <svg xmlns="http://www.w3.org/2000/svg" width="\(width)" height="1200" viewBox="0 0 \(width) 1200" role="img" aria-labelledby="title">
    <title id="title">\(title)</title>
    <desc>Flat SwiftKick cyan and magenta ribbon. The three straight diagonal bands have equal perpendicular width; opposing contours are rotationally symmetric. The visible bounds are centered.</desc>
    \(definitions)
    \(content)
    </svg>
    """
}
let destination = URL(fileURLWithPath: CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "internal/branding", isDirectory: true)
try FileManager.default.createDirectory(at: destination, withIntermediateDirectories: true)
for (file, color) in [("skai-logo.svg", "#000000"), ("skai-logo-dark.svg", "#FFFFFF")] {
    let text = "<g fill=\"\(color)\" transform=\"translate(\(String(format: "%.3f", wordX)) \(String(format: "%.3f", baseline))) scale(1 -1)\">" + letters.joined() + "</g>"
    try document("<g transform=\"translate(\(symbolShift) 0)\">" + symbol + "</g>\n" + text, width: width, title: "SKAI").write(to: destination.appendingPathComponent(file), atomically: true, encoding: .utf8)
}
print("Generated outlined wordmarks in \(destination.path)")

// Icon Composer foreground layer, written into SKAIConfigure.icon: the symbol alone on a transparent 1024 canvas,
// as plain paths (no clip paths or <use>, which Icon Composer may not honour). The system draws the
// rounded square, whose size is the whole canvas, so the symbol keeps the proportion it had inside the
// legacy white plate: its 1200 canvas filled 740 of the 896 plate.
let layerScale: CGFloat = 1024 * (740.0 / 896) / 1200
let layerOffset = (1024 - 1200 * layerScale) / 2
var layerPlacement = CGAffineTransform(translationX: layerOffset, y: layerOffset)
    .scaledBy(x: layerScale, y: layerScale).translatedBy(x: offsetX, y: offsetY)
var halfTurn = CGAffineTransform(translationX: 600, y: 600).rotated(by: .pi).translatedBy(x: -600, y: -600)
let lowerCap = cap.copy(using: &halfTurn)!
func layerPath(_ path: CGPath) -> String { svgPath(path.copy(using: &layerPlacement)!) }
func layerNumber(_ value: CGFloat) -> String { String(format: "%.3f", value) }
let gradientStart = CGPoint(x: 220, y: 200).applying(layerPlacement), gradientEnd = CGPoint(x: 960, y: 1100).applying(layerPlacement)
let iconLayer = """
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<title>SKAI symbol for the app icon: 1024 canvas, plain paths, transparent background</title>
<defs>
  <linearGradient id="body" x1="\(layerNumber(gradientStart.x))" y1="\(layerNumber(gradientStart.y))" x2="\(layerNumber(gradientEnd.x))" y2="\(layerNumber(gradientEnd.y))" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#009DDE"/>
    <stop offset="0.48" stop-color="#504185"/>
    <stop offset="1" stop-color="#A1268C"/>
  </linearGradient>
</defs>
<path d="\(layerPath(outline))" fill="url(#body)"/>
<path d="\(layerPath(outline.intersection(cap)))" fill="#009DDE"/>
<path d="\(layerPath(outline.intersection(lowerCap)))" fill="#A1268C"/>
</svg>

"""
let iconAssets = destination.appendingPathComponent("SKAIConfigure.icon/Assets", isDirectory: true)
try FileManager.default.createDirectory(at: iconAssets, withIntermediateDirectories: true)
try iconLayer.write(to: iconAssets.appendingPathComponent("skai-app-icon-symbol.svg"), atomically: true, encoding: .utf8)

print("Straight band width: \(bandWidth); visible center: \(normalizedBounds.midX), \(normalizedBounds.midY); bounds: \(normalizedBounds)")
