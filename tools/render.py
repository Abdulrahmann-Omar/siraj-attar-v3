"""Render HTML pages to PNG (posters) or PDF (proposal) with the installed Microsoft Edge.

  python tools/render.py png <page.html> <out.png> --w 1080 --h 1350 [--scale 1]
  python tools/render.py pdf <page.html> <out.pdf>
  python tools/render.py batch <jobs.json>      # [{"html":..., "out":..., "w":..., "h":...}, ...]

Fonts load through @font-face from the local fonts/ folder; the renderer waits for document.fonts.ready
and for every <img> to decode, so nothing renders in a fallback face.
"""
import json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

WAIT = """async () => {
  await document.fonts.ready;
  await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
  return [...document.fonts].filter(f => f.status === 'error').map(f => f.family);
}"""


def _png(page, html, out, w, h, scale):
    page.set_viewport_size({"width": w, "height": h})
    page.goto(Path(html).resolve().as_uri(), wait_until="load")
    bad = page.evaluate(WAIT)
    if bad:
        print("font load errors:", bad, file=sys.stderr)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    page.screenshot(path=out, clip={"x": 0, "y": 0, "width": w, "height": h}, type="png")


def main():
    mode = sys.argv[1]
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge", headless=True)
        if mode == "pdf":
            page = b.new_page()
            page.goto(Path(sys.argv[2]).resolve().as_uri(), wait_until="load")
            page.evaluate(WAIT)
            page.pdf(path=sys.argv[3], prefer_css_page_size=True, print_background=True)
        else:
            args = sys.argv[2:]
            opts = {k: v for k, v in zip(args[::2], args[1::2]) if k.startswith("--")}
            scale = float(opts.get("--scale", 1))
            ctx = b.new_context(device_scale_factor=scale)
            page = ctx.new_page()
            if mode == "png":
                _png(page, args[0], args[1], int(opts.get("--w", 1080)), int(opts.get("--h", 1350)), scale)
            elif mode == "batch":
                for j in json.load(open(args[0], encoding="utf-8")):
                    _png(page, j["html"], j["out"], j["w"], j["h"], scale)
                    print("ok", j["out"], flush=True)
        b.close()


if __name__ == "__main__":
    main()
