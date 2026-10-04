"""Render brand/riyal.svg back with Microsoft Edge (Playwright, channel=msedge)
at the source resolution (3000 x 3353) and compare it with the PNG mask.

Outputs brand/riyal_compare.png and prints IoU / pixel stats (also written
into brand/riyal_vector_meta.json under "verification").
"""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PNG = ROOT / "brand" / "riyal.png"
SVG = ROOT / "brand" / "riyal.svg"
META = ROOT / "brand" / "riyal_vector_meta.json"
OUT = ROOT / "brand" / "riyal_compare.png"


def render_svg_mask(w: int, h: int, off: tuple[float, float]) -> np.ndarray:
    svg = SVG.read_text(encoding="utf-8")
    d = re.search(r' d="([^"]+)"', svg).group(1)
    html = f"""<!doctype html><html><head><style>
      html,body{{margin:0;padding:0;background:#fff}} svg{{display:block}}
    </style></head><body>
    <svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{-off[0]} {-off[1]} {w} {h}">
      <path fill="#000" fill-rule="evenodd" d="{d}"/></svg></body></html>"""
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.set_content(html)
        png = pg.screenshot(clip={"x": 0, "y": 0, "width": w, "height": h})
        b.close()
    g = np.array(Image.open(io.BytesIO(png)).convert("L"))
    return g


def main():
    alpha = np.array(Image.open(PNG))[..., 3]
    h, w = alpha.shape
    meta = json.loads(META.read_text(encoding="utf-8"))
    off = tuple(meta["offset_in_source"])
    gray = render_svg_mask(w, h, off)
    a = alpha >= 128
    b = gray < 128
    inter = np.logical_and(a, b).sum()
    union = np.logical_or(a, b).sum()
    iou = inter / union
    only_png = np.logical_and(a, ~b)
    only_svg = np.logical_and(b, ~a)
    # boundary error: distance of every mismatched pixel to the PNG edge
    edge = cv2.Canny(a.astype(np.uint8) * 255, 50, 150)
    dist = cv2.distanceTransform((edge == 0).astype(np.uint8), cv2.DIST_L2, 5)
    mism = np.logical_or(only_png, only_svg)
    max_dev = float(dist[mism].max()) if mism.any() else 0.0
    p99_dev = float(np.percentile(dist[mism], 99)) if mism.any() else 0.0
    # coverage-weighted IoU (soft masks)
    sa = alpha.astype(np.float64) / 255
    sb = 1 - gray.astype(np.float64) / 255
    soft_iou = np.minimum(sa, sb).sum() / np.maximum(sa, sb).sum()
    stats = {"renderer": "Microsoft Edge (Playwright channel=msedge)", "size": [w, h],
             "iou": round(float(iou), 5), "soft_iou": round(float(soft_iou), 5),
             "png_px": int(a.sum()), "svg_px": int(b.sum()),
             "only_png_px": int(only_png.sum()), "only_svg_px": int(only_svg.sum()),
             "max_edge_deviation_px": round(max_dev, 2), "p99_edge_deviation_px": round(p99_dev, 2)}
    meta["verification"] = stats
    META.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=2))

    # ---------- comparison image
    def colorise(y0, y1, x0, x1, scale):
        A, B = a[y0:y1, x0:x1], b[y0:y1, x0:x1]
        img = np.full(A.shape + (3,), 255, np.uint8)
        img[A & B] = (60, 60, 60)
        img[A & ~B] = (230, 30, 30)      # in PNG only
        img[B & ~A] = (30, 90, 230)      # in SVG only
        im = Image.fromarray(img)
        return im.resize((int(im.width * scale), int(im.height * scale)), Image.NEAREST if scale >= 1 else Image.LANCZOS)

    panel_h = 900
    full = colorise(0, h, 0, w, panel_h / h)
    crops = [  # (label, y0, y1, x0, x1)
        ("top terminal of left stem", 0, 300, 1040, 1440),
        ("bottom-left fillet", 2340, 2900, 1000, 1440),
        ("left terminal, lower bar", 2680, 3120, 0, 300),
    ]
    tiles = [("full glyph, 3000 px render", full)]
    for lab, y0, y1, x0, x1 in crops:
        s = panel_h / (y1 - y0)
        tiles.append((f"{lab} (x{s:.1f})", colorise(y0, y1, x0, x1, s)))
    # side-by-side: original PNG vs Edge render at small size
    small = 220
    src_small = Image.fromarray(255 - alpha).convert("RGB").resize((int(w * small / h), small), Image.LANCZOS)
    svg_small = Image.fromarray(gray).convert("RGB").resize((int(w * small / h), small), Image.LANCZOS)

    pad = 24
    W = sum(t.width for _, t in tiles) + pad * (len(tiles) + 1)
    H = panel_h + 3 * pad + 40 + small + 40 + 120
    canvas = Image.new("RGB", (W, H), (250, 248, 244))
    dr = ImageDraw.Draw(canvas)
    try:
        f = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
        fb = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    except OSError:
        f = fb = ImageFont.load_default()
    x = pad
    for lab, t in tiles:
        canvas.paste(t, (x, pad + 36))
        dr.rectangle([x - 1, pad + 35, x + t.width, pad + 36 + t.height], outline=(200, 200, 200))
        dr.text((x, pad), lab, fill=(30, 30, 30), font=f)
        x += t.width + pad
    y = pad + 36 + panel_h + pad
    canvas.paste(src_small, (pad, y + 34)); dr.text((pad, y), "PNG (source)", fill=(30, 30, 30), font=f)
    canvas.paste(svg_small, (pad * 2 + src_small.width, y + 34))
    dr.text((pad * 2 + src_small.width, y), "SVG (Edge render)", fill=(30, 30, 30), font=f)
    tx = pad * 4 + src_small.width * 2
    lines = [
        f"IoU (50% coverage masks) = {stats['iou']:.4f}    soft IoU = {stats['soft_iou']:.4f}    target >= 0.985",
        f"PNG-only px = {stats['only_png_px']:,}   SVG-only px = {stats['only_svg_px']:,}   of {stats['png_px']:,} glyph px",
        f"edge deviation: p99 = {stats['p99_edge_deviation_px']} px, max = {stats['max_edge_deviation_px']} px (at 3000 px)",
        "colours: dark = both,  red = PNG only,  blue = SVG only",
        f"SVG: {meta['bytes']} bytes, viewBox {' '.join(str(v) for v in meta['viewBox'])}",
    ]
    dr.text((tx, y + 20), "Riyal symbol vectorisation check", fill=(20, 20, 20), font=fb)
    for i, ln in enumerate(lines):
        dr.text((tx, y + 64 + i * 34), ln, fill=(40, 40, 40), font=f)
    canvas.save(OUT, optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    main()
