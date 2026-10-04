"""Build brand/riyal_test.html (riyal symbol next to Arabic-Indic and Western
numerals at several sizes) and screenshot it to brand/riyal_test.png with
Microsoft Edge (Playwright channel=msedge).

Needs fonts/ (tools/fonts_download.py) and fonts/metrics.json
(tools/build_specimen.py) for the per-font digit heights.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT_HTML = ROOT / "brand" / "riyal_test.html"
OUT_PNG = ROOT / "brand" / "riyal_test.png"

FACES = {  # css family -> (font file relative to brand/, weight range)
    "Cairo": ("../fonts/cairo/Cairo[slnt,wght].ttf", "200 1000"),
    "Noto Naskh Arabic": ("../fonts/notonaskharabic/NotoNaskhArabic[wght].ttf", "400 700"),
    "El Messiri": ("../fonts/elmessiri/ElMessiri[wght].ttf", "400 700"),
    "Manrope": ("../fonts/manrope/Manrope[wght].ttf", "200 800"),
    "Inter": ("../fonts/inter/Inter[opsz,wght].ttf", "100 900"),
    "Playfair Display": ("../fonts/playfairdisplay/PlayfairDisplay[wght].ttf", "400 900"),
}
SLUG = {"Cairo": "cairo", "Noto Naskh Arabic": "naskh", "El Messiri": "messiri", "Manrope": "manrope",
        "Inter": "inter", "Playfair Display": "playfair"}

AR = "١٥٧٫٨٢"
LAT = "157.82"
SIZES = [12, 14, 16, 20, 24, 32, 40, 48]


def riyal_symbol() -> tuple[str, str]:
    svg = (ROOT / "brand" / "riyal.svg").read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    d = re.search(r' d="([^"]+)"', svg).group(1)
    return vb, d


def price(num: str, digits: str, label: str = "ريال سعودي") -> str:
    return (f'<span class="sar" dir="ltr" data-d="{digits}">'
            f'<svg class="riyal" viewBox="0 0 3000 3353" role="img" aria-label="{label}"><use href="#riyal"/></svg>'
            f'{num}</span>')


def build():
    metrics = json.loads((ROOT / "fonts" / "metrics.json").read_text(encoding="utf-8"))
    vb, d = riyal_symbol()
    faces = "\n".join(
        f"@font-face{{font-family:'{f}';src:url('{quote(p, safe='/.')}') format('truetype');font-weight:{w};font-display:block}}"
        for f, (p, w) in FACES.items())
    tokens = "\n".join(
        f".f-{SLUG[f]} {{ font-family:'{f}', sans-serif; --riyal-ar:{metrics[f]['ar_digits']:.3f}em; "
        f"--riyal-lat:{metrics[f]['lat_digits']:.3f}em; }}"
        for f in FACES)

    cols = [("Cairo", "ar", AR, 700), ("Cairo", "lat", LAT, 700), ("Noto Naskh Arabic", "ar", AR, 700),
            ("Manrope", "lat", LAT, 600), ("Playfair Display", "lat", LAT, 600)]
    head = "".join(f"<th>{f}<br><span>{'Arabic-Indic' if dg == 'ar' else 'Western'} &middot; "
                   f"riyal {metrics[f]['ar_digits' if dg == 'ar' else 'lat_digits']:.3f}em</span></th>"
                   for f, dg, _, _ in cols)
    head += "<th>Cairo, generic<br><span>height: 1cap</span></th>"
    rows = []
    for s in SIZES:
        cells = "".join(f'<td class="f-{SLUG[f]}" style="font-size:{s}px;font-weight:{w}">{price(n, dg)}</td>'
                        for f, dg, n, w in cols)
        cells += f'<td class="f-cairo generic" style="font-size:{s}px;font-weight:700">{price(LAT, "cap")}</td>'
        rows.append(f"<tr><th class='sz'>{s}px</th>{cells}</tr>")

    proofs = "".join(
        f'<div class="proof f-{SLUG[f]}" style="font-weight:{w}"><span class="lbl">{f} &middot; '
        f'{"Arabic-Indic" if dg == "ar" else "Western"}</span>'
        f'<div class="line">{price(n, dg)}<i class="bl"></i></div></div>'
        for f, dg, n, w in [("Cairo", "ar", AR, 800), ("Cairo", "lat", LAT, 800), ("Manrope", "lat", LAT, 600)])

    page = f"""<!doctype html>
<html lang="en" dir="ltr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Riyal Symbol Test</title>
<style>
{faces}
:root {{ --ink:#1c1b19; --paper:#f5f0e6; --card:#fffdf8; --green:#0d3b2e; --gold:#a8834a; --muted:#6f6a61; --line:#e4dccb; --guide:#d2442f; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --ink:#f2ede3; --paper:#14130f; --card:#1d1c18; --green:#7fbfa4; --gold:#d2b07a; --muted:#a49d90; --line:#34312a; }} }}
:root[data-theme="dark"] {{ --ink:#f2ede3; --paper:#14130f; --card:#1d1c18; --green:#7fbfa4; --gold:#d2b07a; --muted:#a49d90; --line:#34312a; }}
{tokens}
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:var(--paper); color:var(--ink); font-family:'Inter',sans-serif; padding:48px; }}
h1 {{ font-family:'Playfair Display',serif; font-weight:600; color:var(--green); font-size:40px; direction:ltr; text-align:left }}
h2 {{ font-family:'Inter',sans-serif; font-size:13px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); font-weight:600; margin:40px 0 14px; direction:ltr; text-align:left }}
.intro {{ direction:ltr; text-align:left; color:var(--muted); max-width:1100px; line-height:1.55; margin-top:8px; font-size:15px }}
.panel {{ background:var(--card); border:1px solid var(--line); border-radius:6px; padding:26px 30px }}

/* ---------- the recommended component (see brand/RIYAL.md) ---------- */
.sar {{ display:inline-flex; align-items:baseline; gap:calc(var(--riyal-h) / 3);
        direction:ltr; unicode-bidi:isolate; white-space:nowrap; }}
.sar[data-d="ar"]  {{ --riyal-h: var(--riyal-ar, 0.68em); }}
.sar[data-d="lat"] {{ --riyal-h: var(--riyal-lat, 0.72em); }}
.sar[data-d="cap"] {{ --riyal-h: 1cap; }}
.riyal {{ height:var(--riyal-h); width:calc(var(--riyal-h) * 3000 / 3353); flex:none; fill:currentColor; overflow:visible }}
/* -------------------------------------------------------------------- */

.hero {{ display:flex; gap:28px; flex-wrap:wrap; direction:ltr }}
.sw {{ width:300px; height:300px; border-radius:6px; display:grid; place-items:center; position:relative }}
.sw svg {{ height:150px; width:calc(150px * 3000 / 3353) }}
.sw .cz {{ position:absolute; inset:calc(50% - 75px - 50px) calc(50% - 67px - 50px); border:1px dashed currentColor; opacity:.45 }}
.sw p {{ position:absolute; bottom:10px; left:12px; font-size:11px; opacity:.75 }}
.proofs {{ display:grid; grid-template-columns:repeat(3,1fr); gap:20px; direction:ltr }}
.proof {{ background:var(--card); border:1px solid var(--line); border-radius:6px; padding:16px 22px 22px; }}
.proof .lbl {{ font-family:'Inter',sans-serif; font-size:12px; color:var(--muted); font-weight:400 }}
.proof .line {{ position:relative; font-size:108px; line-height:1.3; text-align:center; overflow:hidden }}
.proof .bl {{ display:inline-block; width:0; height:0; vertical-align:baseline }}
.guide {{ position:absolute; left:-10px; right:-10px; border-top:1.5px solid var(--guide); pointer-events:none }}
.guide.top {{ border-top-style:dashed }}
table {{ border-collapse:collapse; width:100%; table-layout:fixed; direction:ltr; background:var(--card); border:1px solid var(--line) }}
th, td {{ padding:8px 14px; border-bottom:1px solid var(--line); text-align:center; vertical-align:middle }}
thead th {{ font-size:12.5px; font-weight:600; color:var(--green); }}
thead th span {{ font-weight:400; color:var(--muted); font-size:11.5px }}
th.sz {{ font-size:12px; color:var(--muted); font-weight:500; width:70px }}
td.generic {{ background:rgba(168,131,74,.07) }}
.ctx {{ display:grid; grid-template-columns:1fr 1fr; gap:20px }}
.ctx .panel p {{ font-size:22px; line-height:1.9 }}
.ctx .panel p + p {{ margin-top:6px }}
.old {{ color:var(--muted); text-decoration:line-through; text-decoration-thickness:.06em; font-size:.8em }}
.badge {{ display:inline-flex; align-items:baseline; border:2px solid currentColor; border-radius:999px; padding:.02em .55em .12em; }}
.dont {{ display:grid; grid-template-columns:repeat(4,1fr); gap:20px; direction:ltr }}
.dont .panel {{ text-align:center; font-family:'Cairo'; font-weight:700; font-size:40px; position:relative }}
.dont .panel small {{ display:block; font-family:'Inter'; font-weight:400; font-size:12px; color:var(--muted); margin-top:8px }}
.dont .panel.bad::after {{ content:"\\2715"; position:absolute; top:8px; right:12px; font-size:18px; color:var(--guide) }}
.dont .panel.good::after {{ content:"\\2713"; position:absolute; top:8px; right:12px; font-size:18px; color:#2e7d4f }}
.big {{ height:1.4em !important; width:calc(1.4em * 3000 / 3353) !important }}
@media (max-width:900px) {{ body {{ padding:24px 16px }} .proofs, .ctx, .dont {{ grid-template-columns:1fr }} table {{ display:block; overflow-x:auto }} }}
</style></head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="riyal" viewBox="{vb}"><path fill="currentColor" d="{d}"/></symbol></defs></svg>

<h1>Saudi Riyal symbol &middot; type test</h1>
<p class="intro">Vector: brand/riyal.svg (from SAMA's official artwork, IoU 0.998 vs the PNG at 3000&nbsp;px). SAMA rules applied:
symbol to the <b>left</b> of the number in every language, a space between them, symbol height = text (numeral) height,
clear space = &frac13; of the symbol height. Here the gap is exactly &frac13; of the symbol height and the height is the measured
ink height of each font's digits (red guides below show baseline and digit top).</p>

<h2>Artwork &middot; clear space &frac13; height &middot; colour via currentColor</h2>
<div class="hero">
  <div class="sw" style="background:#fffdf8;color:#1c1b19;border:1px solid var(--line)"><svg><use href="#riyal"/></svg><span class="cz"></span><p>ink on ivory</p></div>
  <div class="sw" style="background:#0d3b2e;color:#fbf7ef"><svg><use href="#riyal"/></svg><span class="cz"></span><p>ivory on brand green</p></div>
  <div class="sw" style="background:#0d3b2e;color:#c9a46a"><svg><use href="#riyal"/></svg><span class="cz"></span><p>gold on brand green</p></div>
  <div class="sw" style="background:#1c1b19;color:#fbf7ef"><svg><use href="#riyal"/></svg><span class="cz"></span><p>ivory on ink</p></div>
</div>

<h2>Alignment proof at 108&nbsp;px (solid = baseline, dashed = digit top)</h2>
<div class="proofs">{proofs}</div>

<h2>Size ladder &middot; per-font digit height vs generic 1cap</h2>
<table><thead><tr><th></th>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table>

<h2>In context</h2>
<div class="ctx">
  <div class="panel f-cairo" dir="rtl" lang="ar">
    <p style="font-weight:400">السعر {price(AR, 'ar')} شامل ضريبة القيمة المضافة.</p>
    <p style="font-weight:700;font-size:34px;color:var(--green)">{price(AR, 'ar')} <span class="old">{price('٣٣٠', 'ar')}</span></p>
    <p style="font-weight:800;font-size:44px"><span class="badge">{price(AR, 'ar')}</span></p>
    <p style="font-weight:400;font-size:16px">النص الصغير: الشحن مجاني للطلبات فوق {price('٢٠٠', 'ar')} داخل المملكة.</p>
  </div>
  <div class="panel f-manrope" dir="ltr" lang="en">
    <p style="font-weight:400">Price {price(LAT, 'lat', 'Saudi riyals')} including VAT.</p>
    <p style="font-weight:700;font-size:34px;color:var(--green)">{price(LAT, 'lat', 'Saudi riyals')} <span class="old">{price('330', 'lat', 'Saudi riyals')}</span></p>
    <p class="f-cairo" style="font-weight:800;font-size:44px"><span class="badge">{price(LAT, 'lat', 'Saudi riyals')}</span></p>
    <p style="font-weight:400;font-size:16px">Small print: free delivery in the Kingdom on orders over {price('200', 'lat', 'Saudi riyals')}.</p>
  </div>
</div>

<h2>Do / don't</h2>
<div class="dont">
  <div class="panel good" dir="rtl">{price(AR, 'ar')}<small>symbol left, &frac13;-height gap, digit height</small></div>
  <div class="panel bad" dir="rtl"><span dir="ltr" style="unicode-bidi:isolate">{AR} ر.س</span><small dir="ltr">&ldquo;ر.س&rdquo; or &ldquo;SAR&rdquo; reads as not knowing the market</small></div>
  <div class="panel bad" dir="rtl"><span dir="ltr" class="sar" data-d="ar" style="unicode-bidi:isolate">{AR}<svg class="riyal" viewBox="0 0 3000 3353"><use href="#riyal"/></svg></span><small>symbol on the right of the number</small></div>
  <div class="panel bad" dir="rtl"><span class="sar" dir="ltr" data-d="ar"><svg class="riyal big" viewBox="0 0 3000 3353"><use href="#riyal"/></svg>{AR}</span><small>symbol taller than the numerals</small></div>
</div>

<script>
// Draw baseline + digit-top guides on the proofs from the same --riyal-h the component uses.
document.fonts.ready.then(() => {{
  for (const pr of document.querySelectorAll('.proof .line')) {{
    const s = pr.querySelector('.sar'), bl = pr.querySelector('.bl'), svg = s.querySelector('svg');
    const box = pr.getBoundingClientRect(), b = bl.getBoundingClientRect().bottom - box.top;
    const h = svg.getBoundingClientRect().height;
    for (const [y, cls] of [[b, 'guide'], [b - h, 'guide top']]) {{
      const g = document.createElement('i'); g.className = cls; g.style.top = y + 'px'; pr.appendChild(g); }}
  }}
  document.body.dataset.ready = '1';
}});
</script>
</body></html>
"""
    OUT_HTML.write_text(page, encoding="utf-8")
    print("wrote", OUT_HTML)


def render():
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        pg = b.new_page(viewport={"width": 1600, "height": 1000}, device_scale_factor=1)
        pg.goto(OUT_HTML.as_uri())
        pg.wait_for_selector("body[data-ready='1']", timeout=60000)
        pg.wait_for_timeout(400)
        # check: symbol bottom sits on the baseline and its height equals --riyal-h
        chk = pg.evaluate("""() => [...document.querySelectorAll('.proof .line')].map(l => {
            const r = l.querySelector('svg').getBoundingClientRect(), bl = l.querySelector('.bl').getBoundingClientRect();
            return {bottom_minus_baseline: +(r.bottom - bl.bottom).toFixed(2), h: +r.height.toFixed(2)}; })""")
        pg.screenshot(path=str(OUT_PNG), full_page=True)
        b.close()
    print("baseline check:", chk)
    print("wrote", OUT_PNG)


if __name__ == "__main__":
    build()
    render()
