"""Compose every poster in both registers (fusha, saudi) and export the product shots.

  python tools/posters.py            # build HTML for all posters + render PNGs + export product shots
  python tools/posters.py C01 K06    # only these ids

Inputs: plan/assets.json, plan/copy.json, data/campaign_prices.json, data/catalogue.json, gen/out/*.png.
Outputs: posters/html/<id>_<tone>.html, posters/out/<id>_<tone>.png, posters/out/<id>.png (product shots).
All type is Cairo (the face the client approved inside images); prices carry the official riyal SVG.
"""
import html, json, os, re, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PY = os.path.join(ROOT, ".venv", "Scripts", "python")
SIZES = {"4:5": (1080, 1350), "9:16": (1080, 1920), "1:1": (1080, 1080)}
TONES = ("fusha", "saudi")
URL = "SIRAJATTARBROS.COM"

assets = json.load(open("plan/assets.json", encoding="utf-8"))
prices = json.load(open("data/campaign_prices.json", encoding="utf-8"))
catalogue = {p["id"]: p for p in json.load(open("data/catalogue.json", encoding="utf-8"))}
copy = {}
COPY_FILE = os.environ.get("COPY", "plan/copy.json")
if os.path.exists(COPY_FILE):
    copy = {p["id"]: p for p in json.load(open(COPY_FILE, encoding="utf-8"))["posters"]}
RIYAL_PATH = re.search(r' d="([^"]+)"', open("brand/riyal.svg", encoding="utf-8").read()).group(1)


def esc(s):
    return html.escape(s or "")


DISPLAY = {"189452492": "عطر العطار 3", "265256366": "كبك فضي",
           "892978768": "قميص داخلي وثير إيطالي", "1292393513": "قماش العطار 909"}


def title(pid):
    return DISPLAY.get(pid) or re.sub(r"\s+", " ", catalogue[pid]["title"]).strip()


def money(v):
    if v is None:
        return ""
    if float(v).is_integer():
        return f"{int(v):,}"
    return f"{v:,.2f}"


def sar(v, cls=""):
    """Price unit: the riyal symbol on the LEFT of the amount inside an LTR isolate (SAMA rule)."""
    return (f'<span class="sar {cls}" dir="ltr"><svg class="riyal" viewBox="0 0 3000 3353" aria-label="ريال سعودي">'
            f'<path d="{RIYAL_PATH}"/></svg><span class="amt">{money(v)}</span></span>')


def price_block(pid, light=False):
    p = prices[pid]
    old = p["campaign_old_price_incl_vat"]
    out = f'<div class="price-row{" light" if light else ""}"><span class="pill">{sar(p["campaign_price_incl_vat"])}</span>'
    if old:
        out += f'<s class="old">{sar(old)}</s>'
    return out + "</div>"


CSS = """
@font-face{font-family:Cairo;src:url('../../fonts/cairo/Cairo%5Bslnt%2Cwght%5D.ttf') format('truetype');font-weight:200 1000;}
@font-face{font-family:Inter;src:url('../../fonts/inter/Inter%5Bopsz%2Cwght%5D.ttf') format('truetype');font-weight:100 900;}
:root{--green:#004738;--gold:#C3A278;--ivory:#F4EFE5;--paper:#FBF8F2;--ink:#1E1A16;--muted:#6B6257;--m:64px;}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:var(--w);height:var(--h);overflow:hidden;background:var(--paper)}
body{font-family:Cairo,sans-serif;color:var(--ink);direction:rtl;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}
.canvas{position:relative;width:var(--w);height:var(--h);overflow:hidden}
.ph{position:absolute;overflow:hidden;background:#d9d2c5}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.rule{position:absolute;left:0;right:0;bottom:0;height:20px;background:var(--green)}
.seal{position:absolute;top:48px;right:48px;width:92px;height:92px;filter:drop-shadow(0 4px 14px rgba(0,0,0,.28))}
.lockup{position:absolute;width:230px}
.kicker{font-weight:700;font-size:26px;color:var(--gold);letter-spacing:0;line-height:1.3}
.headline{font-weight:900;line-height:1.18;letter-spacing:0}
.subline{font-weight:500;line-height:1.45}
.name{font-weight:800;line-height:1.25}
.spec{font-weight:500;color:var(--green);line-height:1.45}
.url{font-family:Inter,sans-serif;font-weight:600;font-size:17px;letter-spacing:.14em;direction:ltr;color:var(--muted)}
.cta{display:inline-block;font-weight:800;font-size:24px;padding:10px 30px 12px;border-radius:999px;background:var(--green);color:var(--ivory);line-height:1.3}
.cta.gold{background:var(--gold);color:var(--green)}
.sar{display:inline-flex;align-items:baseline;gap:.22em;direction:ltr;unicode-bidi:isolate;white-space:nowrap}
.riyal{height:.67em;width:calc(.67em * 3000 / 3353);flex:none;fill:currentColor;overflow:visible}
.price-row{display:flex;align-items:center;gap:22px;direction:rtl}
.pill{display:inline-flex;align-items:center;border:3px solid var(--ink);border-radius:999px;padding:4px 26px 8px;font-weight:800;font-size:50px;line-height:1.2;color:var(--ink)}
.price-row.light .pill{border-color:var(--ivory);color:var(--ivory)}
.old{font-weight:500;font-size:30px;color:var(--muted);text-decoration:none;position:relative}
.old::after{content:"";position:absolute;left:-4px;right:-4px;top:54%;height:3px;background:currentColor}
.price-row.light .old{color:rgba(244,239,229,.75)}
.scrim-b{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(to top,rgba(14,11,8,.86) 0%,rgba(14,11,8,.62) 45%,rgba(14,11,8,0) 100%)}
.scrim-t{position:absolute;left:0;right:0;top:0;background:linear-gradient(to bottom,rgba(14,11,8,.62) 0%,rgba(14,11,8,0) 100%)}
.light-txt{color:var(--ivory)}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{font-weight:700;font-size:22px;padding:6px 18px 8px;border:2px solid rgba(244,239,229,.8);border-radius:999px;color:var(--ivory)}
.stepnum{font-weight:900;color:var(--gold);line-height:1}
.facts{display:flex;gap:0;direction:rtl}
.fact{flex:1;padding:0 22px;border-inline-start:2px solid var(--gold)}
.fact:first-child{border-inline-start:none;padding-inline-start:0}
.fact b{display:block;font-weight:900;font-size:40px;color:var(--green);line-height:1.2}
.fact span{display:block;font-weight:500;font-size:21px;color:var(--muted);line-height:1.4}
.rows .row{display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1.5px solid rgba(30,26,22,.14)}
.rows .row:last-child{border-bottom:none}
.rows .row .t{font-weight:700;font-size:26px}
.rows .row .p{font-weight:800;font-size:28px;color:var(--green)}
.items{display:grid;grid-template-columns:1fr 1fr;gap:14px 34px}
.item .t{font-weight:700;font-size:23px;line-height:1.35}
.item .p{font-weight:800;font-size:27px;color:var(--green)}
.swipe{font-weight:700;font-size:22px;color:var(--ivory);opacity:.9}
.pager{font-family:Inter,sans-serif;font-weight:600;font-size:18px;letter-spacing:.12em;color:var(--muted);direction:ltr}
"""


def page(w, h, body):
    return (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
            f'<style>{CSS}</style><style>:root{{--w:{w}px;--h:{h}px}}</style></head>'
            f'<body><div class="canvas">{body}</div></body></html>')


def img(src):
    return f'<img src="../../{src}" alt="">'


SEAL = '<img class="seal" src="../../brand/roundel_color.png" alt="">'


def c(asset, tone):
    return copy.get(asset["id"], {}).get(tone, {})


# ------------------------------- layouts (minimal system) --------------------
# Client constraint: few components. Every poster = the photograph + one calm paper panel holding at most:
# a title, one supporting line, the price and one call to action. The seal is the only element on the photo.
PH = {"4:5": 810, "9:16": 1260, "1:1": 720}  # 4:3 and 3:2 photo panels = exact image aspect, nothing cropped


def photo(a, w, ph):
    return f'<div class="ph" style="left:0;top:0;width:{w}px;height:{ph}px">{img(a["image"])}</div>{SEAL}'


def panel(ph, inner, pad_top=48):
    return f'<div style="position:absolute;right:var(--m);left:var(--m);top:{ph + pad_top}px">{inner}</div>'


def bottom_row(left, right, bottom=84):
    return (f'<div style="position:absolute;right:var(--m);left:var(--m);bottom:{bottom}px;display:flex;'
            f'justify-content:space-between;align-items:center">{right}{left}</div>')


def L_catalogue(a, t, w, h):
    pid, k, ph = a["product_ids"][0], c(a, t), PH[a["format"]]
    return (photo(a, w, ph) +
            panel(ph, f'<div class="name" style="font-size:50px">{esc(title(pid))}</div>'
                      f'<div class="spec" style="font-size:26px;margin-top:8px">{esc(k.get("spec_line"))}</div>') +
            bottom_row(f'<span class="cta">{esc(k.get("cta"))}</span>', price_block(pid)) + '<div class="rule"></div>')


def L_hero(a, t, w, h):
    pid, k, ph = (a["product_ids"] or [None])[0], c(a, t), PH[a["format"]]
    return (photo(a, w, ph) +
            panel(ph, f'<div class="headline" style="font-size:58px;color:var(--green)">{esc(k.get("headline"))}</div>'
                      f'<div class="subline" style="font-size:27px;margin-top:6px">{esc(k.get("subline"))}</div>', 40) +
            bottom_row(f'<span class="cta">{esc(k.get("cta"))}</span>', price_block(pid) if pid else "<span></span>") +
            '<div class="rule"></div>')


def L_story(a, t, w, h):
    # full-bleed photograph + one compact card that sits above the bottom 20% (platform UI safe zone)
    pid, k = a["product_ids"][0], c(a, t)
    bot = int(h * .20)
    return (photo(a, w, h).replace('class="seal"', f'class="seal" style="top:{int(h * .14) + 6}px"') +
            f'<div style="position:absolute;right:48px;left:48px;bottom:{bot + 16}px;background:rgba(251,248,242,.97);'
            f'border-radius:28px;padding:40px 44px 42px;box-shadow:0 10px 40px rgba(0,0,0,.18)">'
            f'<div class="headline" style="font-size:64px;color:var(--green)">{esc(k.get("headline"))}</div>'
            f'<div class="subline" style="font-size:29px;margin-top:6px">{esc(k.get("subline"))}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:28px">'
            f'{price_block(pid)}<span class="cta" style="font-size:28px">{esc(k.get("cta"))}</span></div></div>')


def L_look_cover(a, t, w, h):
    k, ph = c(a, t), PH["1:1"]
    return (photo(a, w, ph) +
            panel(ph, f'<div class="headline" style="font-size:56px;color:var(--green)">{esc(k.get("headline"))}</div>'
                      f'<div class="subline" style="font-size:26px;margin-top:4px">{esc(k.get("subline"))}</div>', 40) +
            f'<div class="swipe" style="position:absolute;left:var(--m);bottom:74px;color:var(--green)">{esc(k.get("cta"))} ←</div>'
            '<div class="rule"></div>')


def L_look_item(a, t, w, h):
    pid, k, ph = a["product_ids"][0], c(a, t), PH["1:1"]
    return (photo(a, w, ph) +
            panel(ph, f'<div class="name" style="font-size:44px">{esc(title(pid))}</div>'
                      f'<div class="spec" style="font-size:24px;margin-top:6px">{esc(k.get("spec_line"))}</div>', 40) +
            bottom_row("<span></span>", price_block(pid), 66) + '<div class="rule"></div>')


def L_how_step(a, t, w, h):
    pid, k, ph = a["product_ids"][0], c(a, t), PH["1:1"]
    ex = k.get("extras", [])
    instr = ex[1] if len(ex) > 1 else k.get("subline")
    num = "1" if a["id"] == "K05a" else "2"
    tail = bottom_row("<span></span>", price_block(pid), 66) if a["id"] == "K05b" else \
        f'<div class="swipe" style="position:absolute;left:var(--m);bottom:74px;color:var(--green)">{esc(k.get("cta"))} ←</div>'
    return (photo(a, w, ph) +
            f'<div class="stepnum" style="position:absolute;left:var(--m);top:{ph + 30}px;font-size:120px">{num}</div>' +
            panel(ph, f'<div class="headline" style="font-size:46px;color:var(--green);margin-left:120px">{esc(k.get("headline"))}</div>'
                      f'<div class="subline" style="font-size:26px;margin-top:6px;margin-left:120px">{esc(instr)}</div>', 40) +
            tail + '<div class="rule"></div>')


def L_bundle(a, t, w, h):
    k, ph = c(a, t), 810
    items = "".join(f'<div class="item"><div class="t">{esc(title(pid))}</div><div class="p">{sar(prices[pid]["campaign_price_incl_vat"])}</div></div>'
                    for pid in a["product_ids"])
    return (photo(a, w, ph) +
            panel(ph, f'<div class="headline" style="font-size:50px;color:var(--green)">{esc(k.get("headline"))}</div>'
                      f'<div class="items" style="margin-top:22px">{items}</div>', 38) +
            bottom_row(f'<span class="cta">{esc(k.get("cta"))}</span>', f'<span class="spec" style="font-size:22px">{esc((k.get("extras") or [""])[0])}</span>', 60) +
            '<div class="rule"></div>')


def L_heritage(a, t, w, h):
    k, ph = c(a, t), 810
    facts = ""
    for x in k.get("extras", [])[:3]:
        m = re.search(r"\d[\d.,]*(?:\s*هـ)?", x)
        big = m.group(0).strip() if m else x
        small = (x[:m.start()] + x[m.end():]).strip() if m else ""
        small = re.sub(r"\s*(منذ|من)$", "", small).strip()
        small = re.sub(r"^في\s+", "", small).strip()
        facts += f'<div class="fact"><b>{esc(big)}</b><span>{esc(small)}</span></div>'
    return (photo(a, w, ph) +
            panel(ph, f'<div class="headline" style="font-size:54px;color:var(--green)">{esc(k.get("headline"))}</div>', 40) +
            f'<div class="facts" style="position:absolute;right:var(--m);left:var(--m);bottom:70px">{facts}</div>'
            '<div class="rule"></div>')


def L_fabric_library(a, t, w, h):
    k, ph = c(a, t), 720
    order = ["1292393513", "1449104353", "1029444903", "563952490"]
    ex = k.get("extras") or []
    rows = "".join(f'<div class="row"><span class="t">{esc(ex[i] if i < len(ex) else title(pid))}</span>'
                   f'<span class="p">{sar(prices[pid]["campaign_price_incl_vat"])}</span></div>' for i, pid in enumerate(order))
    return (photo(a, w, ph) +
            panel(ph, f'<div class="headline" style="font-size:48px;color:var(--green)">{esc(k.get("headline"))}</div>'
                      f'<div class="rows" style="margin-top:10px">{rows}</div>', 34) +
            bottom_row(f'<span class="cta">{esc(k.get("cta"))}</span>', "<span></span>", 56) + '<div class="rule"></div>')


LAYOUTS = {"catalogue": L_catalogue, "hero": L_hero, "story": L_story, "look-cover": L_look_cover,
           "look-item": L_look_item, "how-step": L_how_step, "bundle": L_bundle, "heritage": L_heritage,
           "fabric-library": L_fabric_library}


def export_shot(a):
    src = a["image"]
    if not os.path.exists(src):
        return False
    im = Image.open(src).convert("RGB")
    W, H = 1080, 1350
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - W) // 2, (im.height - H) // 2
    im.crop((l, t, l + W, t + H)).save(f"posters/out/{a['id']}.png", optimize=True)
    return True


def main(only):
    os.makedirs("posters/html", exist_ok=True)
    os.makedirs("posters/out", exist_ok=True)
    jobs, missing = [], []
    for a in assets:
        if only and a["id"] not in only:
            continue
        if a["kind"] == "product_shot":
            if not export_shot(a):
                missing.append(a["id"])
            continue
        if not os.path.exists(a["image"]):
            missing.append(a["id"])
            continue
        if a["id"] not in copy:
            missing.append(a["id"] + "(copy)")
            continue
        w, h = SIZES[a["format"]]
        for t in TONES:
            fn = f"posters/html/{a['id']}_{t}.html"
            open(fn, "w", encoding="utf-8").write(page(w, h, LAYOUTS[a["layout"]](a, t, w, h)))
            jobs.append({"html": fn, "out": f"posters/out/{a['id']}_{t}.png", "w": w, "h": h})
    json.dump(jobs, open("posters/html/_jobs.json", "w", encoding="utf-8"), indent=1)
    if jobs:
        subprocess.run([PY, "tools/render.py", "batch", "posters/html/_jobs.json"], check=True)
    print(f"rendered {len(jobs)} poster files; missing: {missing}")


if __name__ == "__main__":
    main(set(sys.argv[1:]))
