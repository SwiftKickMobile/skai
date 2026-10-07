// Renders PDF pages to PNG with Apple's PDF renderer (PDFKit / Quartz), the one iOS apps use to draw
// PDF assets. Use it as the reference when converting an app's PDF artwork for Figma: other
// converters (Inkscape's PDF import in particular) misread soft masks and blend effects.
//
// Usage: swift pdf-render.swift <file.pdf> <out-dir> [pages] [scale] [background]
//   pages       comma-separated page numbers, 1-based (default: all)
//   scale       pixels per point (default 3)
//   background  "white" or "clear" (default clear)
// Writes <out-dir>/<pdf name>-p<NN>.png and prints each page's size in points.

import AppKit
import PDFKit

let args = CommandLine.arguments
guard args.count >= 3, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    print("Usage: swift pdf-render.swift <file.pdf> <out-dir> [pages] [scale] [background]")
    exit(1)
}
let outDir = args[2]
let pages: [Int] = args.count > 3 && !args[3].isEmpty
    ? args[3].split(separator: ",").compactMap { Int($0) }
    : Array(1...doc.pageCount)
let scale = args.count > 4 ? CGFloat(Double(args[4]) ?? 3) : 3
let white = args.count > 5 && args[5] == "white"
let base = URL(fileURLWithPath: args[1]).deletingPathExtension().lastPathComponent
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)

for number in pages {
    guard let page = doc.page(at: number - 1) else { continue }
    let box = page.bounds(for: .mediaBox)
    let w = Int((box.width * scale).rounded()), h = Int((box.height * scale).rounded())
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8,
                               samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                               colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    let ctx = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = ctx
    let cg = ctx.cgContext
    cg.clear(CGRect(x: 0, y: 0, width: w, height: h))
    if white { cg.setFillColor(NSColor.white.cgColor); cg.fill(CGRect(x: 0, y: 0, width: w, height: h)) }
    cg.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: cg)
    NSGraphicsContext.restoreGraphicsState()
    let path = "\(outDir)/\(base)-p\(String(format: "%02d", number)).png"
    try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: path))
    print("\(path)  \(box.width)×\(box.height) pt")
}
