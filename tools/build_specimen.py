"""Build fonts/specimen.html from fonts/manifest.json and render fonts/specimen.png
with Microsoft Edge (Playwright channel=msedge).

Also writes fonts/metrics.json: per family, measured ink heights (in em) of
Latin caps, Western digits and Arabic-Indic digits, used to size the riyal.

Run:  .venv\\Scripts\\python tools\\build_specimen.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "fonts"
OUT_HTML = FONTS / "specimen.html"
OUT_PNG = FONTS / "specimen.png"
METRICS = FONTS / "metrics.json"

WEIGHT_NAMES = {"Thin": 100, "ExtraLight": 200, "Light": 300, "Regular": 400, "Medium": 500,
                "SemiBold": 600, "Bold": 700, "ExtraBold": 800, "Black": 900}

# Short editorial notes shown on each card (style class / origin).
NOTES = {
    "Cairo": ("Contemporary Kufi sans", "The face inside the old poster images (Everyside composer: Cairo for Arabic, Black 900 display). Client: 'a wise choice'."),
    "IBM Plex Sans Arabic": ("Corporate humanist sans", "The old proposal's Arabic body face. Client asked to reconsider it."),
    "Alexandria": ("Geometric Kufi sans", "Gaber; wide, airy, 9 weights."),
    "Readex Pro": ("Lexend-derived sans", "Built for legibility; wide letterforms."),
    "Noto Kufi Arabic": ("Kufi sans", "Google Noto; sturdy, neutral, 9 weights."),
    "Noto Naskh Arabic": ("Naskh text", "Classic book Naskh, 400-700."),
    "Noto Sans Arabic": ("Low-contrast Naskh sans", "Google Noto UI/sans; width axis."),
    "Amiri": ("Classical Naskh (Bulaq press)", "Khaled Hosny; literary, high-contrast."),
    "Aref Ruqaa": ("Ruqaa calligraphic", "Accent / signature use only."),
    "Reem Kufi": ("Fatimid-style geometric Kufi", "Logotype-like; display only."),
    "Tajawal": ("Geometric sans (Boutros)", "Common in Gulf retail; 7 weights."),
    "Almarai": ("Sans (Boutros)", "Very common in Saudi UI; 4 weights."),
    "Changa": ("Squared Kufi display", "Tech / sport flavour."),
    "Rubik": ("Rounded sans", "Soft corners; casual."),
    "Lalezar": ("Heavy display", "One weight; loud promo."),
    "Marhey": ("Playful display", "Hand-drawn, informal."),
    "Baloo Bhaijaan 2": ("Rounded display", "Friendly, childlike."),
    "El Messiri": ("Naskh-inspired display", "Gaber; elegant contemporary Naskh."),
    "Zain": ("Slim geometric (Boutros, 2024)", "Light, modern, 8 styles."),
    "Kufam": ("Kufi display (Morcos)", "Distinctive, editorial."),
    "Lateef": ("Sindhi/Naskh text (SIL)", "South-Asian Naskh flavour."),
    "Scheherazade New": ("Traditional Naskh (SIL)", "Scholarly text face."),
    "Harmattan": ("West-African Arabic (SIL)", "Regional letterforms, not Gulf."),
    "Mada": ("Modern sans (Hosny)", "Clean, compact, 8 weights."),
    "Vazirmatn": ("Persian-leaning sans", "Excellent UI face; Persian forms."),
    "Beiruti": ("Display sans (Boutros, 2024)", "Condensed-ish, poster-friendly."),
}

HEAD = "أكثر من ثمانين عامًا من الحِرفة"
DIALECT = "شماغك جاهز للشتاء، اطلبه الحين"
BODY = ("منذ أكثر من ثمانين عامًا يختار محمد سراج عطار وأخويه أقمشة الشماغ والغترة والثوب بعناية، "
        "ويُتقن حرفيّوه ما لا يُرى من بعيد: كثافة النسيج، واستقامة الحواف، وثبات اللون بعد كل غسلة. "
        "هذه ليست ملابس موسم، بل إرثٌ يُلبس كل يوم ويُورَّث من جيل إلى جيل.")
PRICE_AR = "١٥٧٫٨٢"
PRICE_LAT = "157.82"

LAT_HEAD = "Eighty years of craft."
LAT_BODY = ("Since the 1940s, M. Siraj Attar & Bros have chosen every shemagh, ghutra and thobe cloth by hand: "
            "the density of the weave, the line of the hem, the colour that survives every wash.")


def weights_of(entry) -> tuple[list[int], list[tuple[str, str, str]]]:
    """Available weights and @font-face rows (file, weight descriptor, style)."""
    rows = []
    ws: set[int] = set()
    axes = {a["tag"]: a for a in entry.get("axes") or []}
    for f in entry["files"]:
        name = f["file"]
        if not name.endswith(".ttf"):
            continue
        italic = "Italic" in name
        style = "italic" if italic else "normal"
        if "[" in name:
            a = axes.get("wght")
            if a:
                lo, hi = int(a["min"]), int(a["max"])
                rows.append((name, f"{lo} {hi}", style))
                if not italic:
                    ws.update(w for w in range(100, 1001, 100) if lo <= w <= hi)
            else:
                rows.append((name, "400", style))
                ws.add(400)
        else:
            stem = name.rsplit("-", 1)[-1].replace(".ttf", "").replace("Italic", "") or "Regular"
            w = WEIGHT_NAMES.get(stem, 400)
            rows.append((name, str(w), style))
            if not italic:
                ws.add(w)
    return sorted(ws), rows


def pick(ws, want):
    if want in ws:
        return want
    below = [w for w in ws if w <= want]
    return max(below) if below else min(ws)


def font_faces(manifest) -> str:
    css = []
    for e in manifest["families"]:
        if e.get("status") != "ok":
            continue
        _, rows = weights_of(e)
        d = e["dir"].split("/", 1)[1]
        for file, wdesc, style in rows:
            css.append(
                f"@font-face{{font-family:'{e['family']}';src:url('{d}/{quote(file)}') format('truetype');"
                f"font-weight:{wdesc};font-style:{style};font-display:block}}"
            )
    return "\n".join(css)


def riyal_symbol() -> str:
    svg = (ROOT / "brand" / "riyal.svg").read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    d = re.search(r' d="([^"]+)"', svg).group(1)
    return f'<symbol id="riyal" viewBox="{vb}"><path fill="currentColor" d="{d}"/></symbol>'


def price(num: str, lang: str, label: str) -> str:
    return (f'<span class="price" dir="ltr" data-digits="{lang}" role="text" aria-label="{label}">'
            f'<svg class="riyal" aria-hidden="true"><use href="#riyal"/></svg>'
            f'<span class="amt">{num}</span></span>')


def card(e) -> str:
    fam = e["family"]
    ws, _ = weights_of(e)
    wh, wd, wb, wp = pick(ws, 700), pick(ws, 500), pick(ws, 400), pick(ws, 700)
    style, note = NOTES.get(fam, ("", ""))
    badge = ""
    if fam == "Cairo":
        badge = '<span class="badge gold">in the old posters &middot; client liked it</span>'
    elif fam == "IBM Plex Sans Arabic":
        badge = '<span class="badge red">old proposal face &middot; reconsider</span>'
    wl = f"{min(ws)}&ndash;{max(ws)}" if len(ws) > 1 else str(ws[0])
    q = html.escape
    return f"""
<section class="card" data-family="{q(fam)}" style="--f:'{q(fam)}'">
  <header dir="ltr">
    <h2>{q(fam)}</h2>{badge}
    <p class="meta">{q(style)} &middot; weights {wl} &middot; {q(e.get('designer') or '')} &middot; {q(e['license'])}</p>
    <p class="note">{q(note)}</p>
  </header>
  <div class="ar" dir="rtl" lang="ar">
    <p class="h64" style="font-weight:{wh}">{HEAD}</p>
    <p class="h40" style="font-weight:{wd}">{DIALECT}</p>
    <p class="b16" style="font-weight:{wb}">{BODY}</p>
    <p class="prices" style="font-weight:{wp}">
      {price(PRICE_AR, 'ar', '157.82 ريال سعودي')}
      {price(PRICE_LAT, 'lat', '157.82 ريال سعودي')}
      <span class="m" dir="ltr"></span>
    </p>
  </div>
  <p class="weights" dir="ltr">headline {wh} &middot; dialect {wd} &middot; body {wb} &middot; price {wp}</p>
</section>"""


def latin_card(e) -> str:
    fam = e["family"]
    ws, _ = weights_of(e)
    q = html.escape
    wh = pick(ws, 600 if fam in ("Playfair Display", "Fraunces") else 700)
    if fam.startswith("Cormorant"):
        wh = pick(ws, 600)
    return f"""
<section class="card latin" data-family="{q(fam)}" style="--f:'{q(fam)}'" dir="ltr">
  <header><h2>{q(fam)}</h2>
    <p class="meta">weights {min(ws)}&ndash;{max(ws)} &middot; {q(e.get('designer') or '')} &middot; {q(e['license'])}</p></header>
  <p class="h64" style="font-weight:{wh}">{LAT_HEAD}</p>
  <p class="h40" style="font-weight:400">M. Siraj Attar &amp; Bros &mdash; <i>since the 1940s</i></p>
  <p class="b16">{LAT_BODY}</p>
  <p class="prices" style="font-weight:{pick(ws, 600)}">{price(PRICE_LAT, 'lat', '157.82 Saudi riyals')}
     <span class="caps">SIRAJATTARBROS.COM</span><span class="m"></span></p>
</section>"""


def recommended() -> str:
    """Three proof tiles for the recommended system (see fonts/FONTS.md)."""
    return f"""
<h3 class="group">Recommended system</h3>
<div class="rec">
  <section class="tile poster" dir="rtl" lang="ar">
    <p class="tag" dir="ltr">1+2 &middot; Posters: Cairo 900 display / Cairo 500 body</p>
    <p class="ph" style="font-family:'Cairo';font-weight:900">أكثر من ثمانين عامًا<br>من الحِرفة</p>
    <p class="ps" style="font-family:'Cairo';font-weight:500">شماغ كلاسيك زفير</p>
    <p class="pp" style="font-family:'Cairo';font-weight:800">{price(PRICE_AR, 'ar', '157.82 ريال سعودي')}</p>
    <p class="url" dir="ltr">SIRAJATTARBROS.COM</p>
  </section>
  <section class="tile deck" dir="rtl" lang="ar">
    <p class="tag" dir="ltr">3+4 &middot; Proposal: El Messiri 700 headings / Cairo 400 body</p>
    <p class="dk" style="font-family:'Cairo';font-weight:600">التحدي</p>
    <p class="dh" style="font-family:'El Messiri';font-weight:700">إتقان أكثر من ثمانين عامًا يستحق أن يُرى</p>
    <p class="db" style="font-family:'Cairo';font-weight:400">{BODY}</p>
    <p class="dp" style="font-family:'Cairo';font-weight:700">مثال للسعر {price(PRICE_AR, 'ar', '157.82 ريال سعودي')}</p>
  </section>
  <section class="tile latin-t" dir="ltr">
    <p class="tag">5 &middot; Latin: Playfair Display 600 / Manrope 400</p>
    <p class="dk" style="font-family:'Manrope';font-weight:600;letter-spacing:.16em;text-transform:uppercase;font-size:13px">Prepared for M. Siraj Attar &amp; Bros</p>
    <p class="dh" style="font-family:'Playfair Display';font-weight:600">From the House of Attar</p>
    <p class="db" style="font-family:'Manrope';font-weight:400">{LAT_BODY}</p>
    <p class="dp" style="font-family:'Manrope';font-weight:600">Price example {price(PRICE_LAT, 'lat', '157.82 Saudi riyals')}</p>
  </section>
</div>"""


def build():
    manifest = json.loads((FONTS / "manifest.json").read_text(encoding="utf-8"))
    ok = [e for e in manifest["families"] if e.get("status") == "ok"]
    ar = [e for e in ok if e["group"] == "arabic"]
    la = [e for e in ok if e["group"] == "latin"]
    cards = "\n".join(card(e) for e in ar)
    lcards = "\n".join(latin_card(e) for e in la)
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arabic Type Specimen</title>
<style>
{font_faces(manifest)}
:root {{ --ink:#1c1b19; --paper:#f5f0e6; --card:#fffdf8; --green:#0d3b2e; --gold:#a8834a; --muted:#6f6a61; --line:#e4dccb; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --ink:#f2ede3; --paper:#14130f; --card:#1d1c18; --green:#7fbfa4; --gold:#d2b07a; --muted:#a49d90; --line:#34312a; }} }}
:root[data-theme="dark"] {{ --ink:#f2ede3; --paper:#14130f; --card:#1d1c18; --green:#7fbfa4; --gold:#d2b07a; --muted:#a49d90; --line:#34312a; }}
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ background:var(--paper); color:var(--ink); font-family:'Inter',system-ui,sans-serif; padding:56px 48px 80px; }}
.top {{ display:flex; justify-content:space-between; align-items:flex-end; gap:24px; border-bottom:1px solid var(--line); padding-bottom:24px; margin-bottom:36px; flex-wrap:wrap }}
.top h1 {{ font-family:'Playfair Display',serif; font-weight:600; font-size:44px; color:var(--green); letter-spacing:-.01em }}
.top p {{ color:var(--muted); font-size:15px; max-width:880px; line-height:1.5 }}
.kicker {{ font-size:12px; letter-spacing:.18em; text-transform:uppercase; color:var(--gold); font-weight:600; margin-bottom:8px }}
h3.group {{ font-family:'Playfair Display',serif; font-weight:600; font-size:28px; color:var(--green); margin:44px 0 18px }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(min(100%,1080px),1fr)); gap:24px }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:6px; padding:26px 30px 18px; font-family:var(--f),'Inter',sans-serif; overflow:hidden }}
.card header {{ font-family:'Inter',sans-serif; margin-bottom:14px }}
.card h2 {{ display:inline; font-size:20px; font-weight:700; color:var(--green); margin-right:10px }}
.badge {{ display:inline-block; font-size:11px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; padding:3px 8px; border-radius:3px; vertical-align:3px }}
.badge.gold {{ background:#efe2c8; color:#6b4f1d }} .badge.red {{ background:#f3d9d4; color:#7a2a1d }}
.meta {{ font-size:12.5px; color:var(--muted); margin-top:4px }}
.note {{ font-size:12.5px; color:var(--ink); opacity:.8; margin-top:2px }}
.h64 {{ font-size:64px; line-height:1.45; font-synthesis:none; white-space:nowrap; overflow:hidden; text-overflow:clip }}
.h40 {{ font-size:40px; line-height:1.5; color:var(--green); font-synthesis:none; white-space:nowrap; overflow:hidden }}
.b16 {{ font-size:16px; line-height:1.85; max-width:62em; margin:6px 0 10px; font-synthesis:none }}
.latin .b16 {{ line-height:1.6 }}
.prices {{ font-size:40px; line-height:1.3; display:flex; gap:44px; align-items:baseline; flex-wrap:wrap; font-synthesis:none }}
.prices .m {{ font-family:'Inter',sans-serif; font-size:11.5px; color:var(--muted); font-weight:400 }}
.caps {{ font-family:'Inter',sans-serif; font-size:14px; letter-spacing:.16em; font-weight:500; color:var(--muted) }}
/* Riyal: SAMA rule = symbol left of the number, a space between, height = numeral height. */
.price {{ display:inline-flex; align-items:baseline; gap:calc(var(--riyal-h, .72em) / 3); white-space:nowrap; unicode-bidi:isolate }}
.riyal {{ height:var(--riyal-h, .72em); width:calc(var(--riyal-h, .72em) * 3000 / 3353); fill:currentColor; flex:none; overflow:visible }}
.rec {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,700px),1fr)); gap:24px }}
.tile {{ border-radius:6px; padding:30px 36px 28px; position:relative; min-height:430px }}
.tile .tag {{ font-family:'Inter',sans-serif; font-size:12px; letter-spacing:.04em; opacity:.75; margin-bottom:18px }}
.tile.poster {{ background:#0d3b2e; color:#fbf7ef }}
.tile.poster .ph {{ font-size:66px; line-height:1.25 }}
.tile.poster .ps {{ font-size:26px; margin-top:12px; opacity:.9 }}
.tile.poster .pp {{ font-size:46px; margin-top:20px; display:inline-block; border:2px solid #fbf7ef; border-radius:999px; padding:2px 28px 6px }}
.tile.poster .url {{ font-family:'Inter',sans-serif; font-size:14px; letter-spacing:.16em; margin-top:18px; opacity:.85; text-align:right }}
.tile.deck, .tile.latin-t {{ background:var(--card); border:1px solid var(--line); border-bottom:12px solid #0d3b2e }}
.dk {{ color:var(--gold); font-size:19px }}
.dh {{ color:var(--green); font-size:46px; line-height:1.35; margin:6px 0 16px }}
.db {{ font-size:18px; line-height:1.85; max-width:40em }}
.latin-t .db {{ line-height:1.6; font-size:17px }}
.dp {{ font-size:22px; margin-top:16px; color:var(--green); display:flex; gap:.5em; align-items:baseline }}
.weights {{ font-family:'Inter',sans-serif; font-size:11px; color:var(--muted); margin-top:10px; border-top:1px dashed var(--line); padding-top:8px }}
@media (max-width:700px) {{ body {{ padding:24px 16px }} .h64 {{ font-size:40px; white-space:normal }} .h40 {{ font-size:28px; white-space:normal }} }}
</style></head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{riyal_symbol()}</svg>
<div class="top">
  <div><p class="kicker">Siraj Attar v3 &middot; type research</p><h1>Arabic type specimen</h1></div>
  <p>Each card: headline 64&nbsp;px bold (or the family's heaviest weight up to 700, no faux bold), Saudi-dialect line 40&nbsp;px,
  body 16&nbsp;px, and a price in Arabic-Indic and Western digits next to the vectorised SAMA riyal symbol. The symbol's height is set to
  the measured height of that font's digits (value shown beside the prices). All families are SIL OFL&nbsp;1.1 from google/fonts.</p>
</div>
{recommended()}
<h3 class="group">Arabic families</h3>
<div class="grid">{cards}</div>
<h3 class="group">Latin pairing candidates</h3>
<div class="grid">{lcards}</div>
<script>
// Measure ink heights (em) of caps and digits per family; size the riyal to the digits.
async function measureAll() {{
  await document.fonts.ready;
  const fams = [...new Set([...document.querySelectorAll('.card')].map(c => c.dataset.family))];
  await Promise.all(fams.flatMap(f => [400, 700].map(w => document.fonts.load(`${{w}} 100px "${{f}}"`, 'Hأ٠١٢157'))));
  // Pixel scan at 300 px (canvas TextMetrics are quantised to 1/64 em in Chromium).
  const C = document.createElement('canvas'); C.width = 2600; C.height = 700;
  const X = C.getContext('2d', {{ willReadFrequently: true }});
  const ink = (font, text) => {{
    X.clearRect(0, 0, C.width, C.height); X.font = font; X.direction = 'ltr'; X.textAlign = 'left';
    X.textBaseline = 'alphabetic'; X.fillStyle = '#000'; X.fillText(text, 20, 500);
    const d = X.getImageData(0, 0, C.width, C.height).data; let top = -1, bot = -1;
    for (let y = 0; y < C.height; y++) {{ const r = y * C.width * 4;
      for (let x = 3; x < C.width * 4; x += 4) if (d[r + x] > 127) {{ if (top < 0) top = y; bot = y; break; }} }}
    return {{ asc: (500 - top) / 300, desc: (bot + 1 - 500) / 300 }};
  }};
  const out = {{}};
  for (const f of fams) {{
    const m = (t, w) => ink(`${{w}} 300px "${{f}}"`, t);
    const ar = m('١٢٣٤٥٦٧٨٩', 700);
    out[f] = {{ cap: m('HE', 400).asc, x: m('xz', 400).asc, lat_digits: m('0123456789', 700).asc,
               ar_digits: ar.asc, ar_digits_desc: ar.desc, alef: m('ا', 400).asc }};
  }}
  for (const c of document.querySelectorAll('.card')) {{
    const r = out[c.dataset.family];
    for (const p of c.querySelectorAll('.price')) {{
      const h = p.dataset.digits === 'ar' ? r.ar_digits : r.lat_digits;
      p.style.setProperty('--riyal-h', h.toFixed(3) + 'em');
    }}
    const m = c.querySelector('.prices .m');
    if (m) m.textContent = c.classList.contains('latin')
      ? `riyal = ${{r.lat_digits.toFixed(3)}}em (digit height) · cap ${{r.cap.toFixed(3)}}em`
      : `riyal height = digit height · Arabic-Indic ${{r.ar_digits.toFixed(3)}}em · Western ${{r.lat_digits.toFixed(3)}}em · cap ${{r.cap.toFixed(3)}}em`;
  }}
  window.__metrics = out; document.body.dataset.ready = '1';
}}
measureAll();
</script>
</body></html>
"""
    OUT_HTML.write_text(page, encoding="utf-8")
    print("wrote", OUT_HTML, len(page) // 1024, "KB")


def render():
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge")
        pg = b.new_page(viewport={"width": 2400, "height": 1400}, device_scale_factor=1)
        pg.goto(OUT_HTML.as_uri())
        pg.wait_for_selector("body[data-ready='1']", timeout=60000)
        pg.wait_for_timeout(500)
        metrics = pg.evaluate("window.__metrics")
        # overflow check: does any 64px headline overflow its card?
        over = pg.evaluate("""[...document.querySelectorAll('.card .h64, .card .h40')]
            .filter(e => e.scrollWidth > e.clientWidth + 1)
            .map(e => e.closest('.card').dataset.family + ' ' + e.className)""")
        pg.screenshot(path=str(OUT_PNG), full_page=True)
        b.close()
    METRICS.write_text(json.dumps({k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in metrics.items()},
                                  indent=2, ensure_ascii=False), encoding="utf-8")
    print("overflow:", over)
    print("wrote", OUT_PNG)


if __name__ == "__main__":
    build()
    render()
