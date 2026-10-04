"""Build the Siraj Attar proposal (Arabic + English) from proposal/content.json.

  .venv\\Scripts\\python proposal\\build.py            # HTML + PDF, both languages
  .venv\\Scripts\\python proposal\\build.py --html     # HTML only
  .venv\\Scripts\\python proposal\\build.py --qa       # also run the layout checks (overflow / safe area / fonts)

Image slots point to the final files:
  product shots   posters/out/P01.png .. P16.png
  posters         posters/out/<id>_fusha.png, posters/out/<id>_saudi.png
  "before" photos data/images/<productid>_<n>.<ext>
A missing file renders as a neutral placeholder box with its id, so the build is always re-runnable.
Web-sized JPEG copies are written to proposal/img/ (keeps each PDF small); stale copies are removed.
"""
import html, json, re, subprocess, sys
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PROP = ROOT / "proposal"
IMG = PROP / "img"
OUT = ROOT / "posters" / "out"
W, H = 1920, 1080

C = json.loads((PROP / "content.json").read_text(encoding="utf-8"))
RIYAL_D = re.search(r'\sd="([^"]+)"', (ROOT / "brand" / "riyal.svg").read_text(encoding="utf-8")).group(1)

L = "en"           # current language, set per build
USED = set()       # img/ files referenced by this run
STATUS = {}        # slot -> final / placeholder


# ----------------------------------------------------------------------------- text helpers
def t(v):
    if isinstance(v, dict) and ("en" in v or "ar" in v):
        return v.get(L, v.get("en"))
    return v


ARROW = '<svg class="arr" viewBox="0 0 26 12" aria-hidden="true"><path d="M1 6h22M17 1l6 5-6 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
TICK = '<svg class="tick" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3.2 3.2L13 4.8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
RANGE = re.compile(r"\d[\d.,]*%?\s*[–\-×]\s*\d[\d.,]*%?")
ARABIC_RUN = re.compile(r"[؀-ۿ][؀-ۿ\s]*[؀-ۿ]|[؀-ۿ]")


def sar(amount):
    lab = "ريال سعودي" if L == "ar" else "Saudi riyals"
    return (f'<span class="sar" dir="ltr"><svg class="riyal" viewBox="0 0 3000 3353" role="img" aria-label="{lab}">'
            f'<use href="#riyal"/></svg><span class="num">{amount}</span></span>')


def rt(s):
    """Rich text: escape, LTR-isolate Arabic number ranges, **strong**, {->}, {sar:n}, newlines."""
    s = html.escape(t(s) or "", quote=False)
    if L == "ar":
        s = RANGE.sub(lambda m: f'<span class="ltr" dir="ltr">{m.group(0)}</span>', s)
    else:  # isolate Arabic runs inside English lines so punctuation keeps its place
        s = ARABIC_RUN.sub(lambda m: f'<bdi lang="ar">{m.group(0)}</bdi>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = s.replace("{-&gt;}", ARROW).replace("{->}", ARROW)
    s = re.sub(r"\{sar:([^}]+)\}", lambda m: sar(m.group(1)), s)
    return s.replace("\n", "<br>")


# ----------------------------------------------------------------------------- images
def resolve(slot, reg="fusha"):
    names = [f"{slot}.png", f"{slot}.jpg"] if slot.startswith("P") else [f"{slot}_{reg}.png", f"{slot}_{reg}.jpg"]
    for n in names:
        if (OUT / n).exists():
            STATUS[f"{slot}{'' if slot.startswith('P') else '_' + reg}"] = "final"
            return OUT / n
    STATUS[f"{slot}{'' if slot.startswith('P') else '_' + reg}"] = "MISSING (placeholder)"
    return None


def _save(im, name, q=88):
    IMG.mkdir(exist_ok=True)
    p = IMG / name
    im.convert("RGB").save(p, "JPEG", quality=q, optimize=True, progressive=True)
    USED.add(name)
    return f"img/{name}"


def webcopy(src, w, h, tag=""):
    """JPEG copy at 2x the displayed size (never upscaled); cached on source mtime."""
    src = Path(src)
    with Image.open(src) as im:
        sw, sh = im.size
        scale = min(1.0, 2 * w / sw, 2 * h / sh)
        tw, th = max(1, round(sw * scale)), max(1, round(sh * scale))
        name = f"{src.stem}{tag}_{tw}x{th}.jpg"
        p = IMG / name
        if p.exists() and p.stat().st_mtime >= src.stat().st_mtime:
            USED.add(name)
            return f"img/{name}"
        im = im.convert("RGB")
        if scale < 1:
            im = im.resize((tw, th), Image.LANCZOS)
        return _save(im, name)


def placeholder(label, w, h, extra=""):
    return (f'<div class="fr ph {extra}" style="width:{w}px;height:{h}px"><div><b>{html.escape(label)}</b>'
            f'<span>{"قيد الإعداد" if L == "ar" else "pending"}</span></div></div>')


def pic(slot, w, h, reg="fusha", extra=""):
    src = resolve(slot, reg)
    if src is None:
        return placeholder(f"{slot}{'' if slot.startswith('P') else ' · ' + reg}", w, h, extra)
    return f'<div class="fr {extra}" style="width:{w}px;height:{h}px"><img src="{webcopy(src, w, h)}" alt="{slot}"></div>'


def store_frame(path, w, h, pins=None, margin=0.07):
    """Store photo framed to the slot aspect: crop to the product + margin, pad with the photo's own ground."""
    src = ROOT / path
    if not src.exists():
        return placeholder(Path(path).name, w, h), "#E8E0D2"
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    sh, sw = a.shape[:2]
    b = max(4, int(min(sw, sh) * 0.02))
    border = np.concatenate([a[:b].reshape(-1, 3), a[-b:].reshape(-1, 3), a[:, :b].reshape(-1, 3), a[:, -b:].reshape(-1, 3)])
    bg = np.median(border, axis=0)
    diff = np.abs(a - bg).max(axis=2) > 28
    rows, cols = np.where(diff.sum(1) > sw * 0.004)[0], np.where(diff.sum(0) > sh * 0.004)[0]
    if len(rows) and len(cols):
        x0, x1, y0, y1 = cols[0], cols[-1], rows[0], rows[-1]
    else:
        x0, y0, x1, y1 = 0, 0, sw - 1, sh - 1
    m = margin * max(x1 - x0, y1 - y0)
    x0, y0, x1, y1 = x0 - m, y0 - m, x1 + m, y1 + m
    bw, bh, ar = x1 - x0, y1 - y0, w / h
    if bw / bh > ar:
        ch, cw = bw / ar, bw
    else:
        cw, ch = bh * ar, bh
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    left, top = cx - cw / 2, cy - ch / 2
    bgc = tuple(int(v) for v in bg)
    canvas = Image.new("RGB", (round(cw), round(ch)), bgc)
    canvas.paste(im, (round(-left), round(-top)))
    scale = min(1.0, 2 * w / cw)
    canvas = canvas.resize((max(1, round(cw * scale)), max(1, round(ch * scale))), Image.LANCZOS)
    rel = _save(canvas, f"{src.stem}_framed_{w}x{h}.jpg", 90)
    hexbg = "#%02X%02X%02X" % bgc
    pin_html = ""
    for i, p in enumerate(pins or [], 1):
        px, py = (p["x"] * sw - left) / cw, (p["y"] * sh - top) / ch
        pin_html += f'<span class="pin" style="left:{px*100:.2f}%;top:{py*100:.2f}%">{i}</span>'
    return (f'<div class="fr store" style="width:{w}px;height:{h}px;background:{hexbg}"><img src="{rel}" alt="">'
            f'{pin_html}</div>'), hexbg


# ----------------------------------------------------------------------------- slide chrome
TOTAL = len(C["slides"])


def chrome(i, foot_start=96, mark=True, foot=True):
    s = ""
    if mark:
        s += '<img class="mark" src="../brand/roundel_color.png" alt="">'
    if foot:
        s += (f'<footer class="ft" style="inset-inline-start:{foot_start}px"><span class="ftl"><img class="ft-es" src="../brand/everyside_wordmark.svg" alt="Everyside"><bdi>{html.escape(t(C["meta"]["footer"]))}</bdi></span>'
              f'<span class="pg" dir="ltr">{i:02d} / {TOTAL:02d}</span></footer>')
    return s


def head(s, cls=""):
    out = f'<header class="hd {cls}"><div class="kicker">{rt(s["kicker"])}</div><h1>{rt(s["h1"])}</h1>'
    if s.get("sub"):
        out += f'<p class="sub">{rt(s["sub"])}</p>'
    return out + "</header>"


# ----------------------------------------------------------------------------- slides
def s_cover(s, i):
    hero = pic(s["hero"], 864, 1080, extra="bleed")
    return f'''<section class="slide cover">
  <div class="cv-field bleed">
    <img class="cv-logo" src="../brand/logo_reversed.png" alt="محمد سراج عطار وأخويه · M. Siraj Attar &amp; Bros">
    <div class="cv-text">
      <div class="cv-prep">{rt(s["prepared"])}</div>
      <div class="cv-title">{rt(s["title"])}</div>
      <div class="cv-sub">{rt(s["subtitle"])}</div>
    </div>
    <div class="cv-foot"><span>{rt(s["kicker"])} · {rt(s["date"])}</span><span class="cv-by">{rt(s["by"])} <img class="es" src="../brand/everyside_wordmark_white.svg" alt="Everyside"></span></div>
  </div>
  <div class="cv-hero bleed">{hero}</div>
</section>'''


def s_line(s, i):
    other = "ar" if L == "en" else "en"
    oline = html.escape(s["line"][other]).replace("\n", " ")
    proofs = "".join(f"<li>{TICK}<span>{html.escape(p)}</span></li>" for p in t(s["proofs"]))
    return f'''<section class="slide line">
  <div class="ln-img bleed">{pic(s["image"], 864, 1080, extra="bleed")}</div>
  <div class="ln-text">
    <div class="kicker">{rt(s["kicker"])}</div>
    <h1 class="big">{rt(s["line"])}</h1>
    <p class="ln-other {'lat' if other == 'en' else 'arab'}" lang="{other}" dir="{'ltr' if other == 'en' else 'rtl'}">{oline}</p>
    <p class="ln-body">{rt(s["body"])}</p>
    <ul class="proofs">{proofs}</ul>
  </div>
  {chrome(i, foot_start=864 + 112)}
</section>'''


def s_found(s, i):
    h, so, st = s["heritage"], s["social"], s["store"]
    tl = "".join(f'<li><b>{rt(x["k"])}</b><span>{rt(x["t"])}</span></li>' for x in h["items"])
    stats = "".join(f'<div class="stat"><b>{rt(x["n"])}</b><span>{rt(x["l"])}</span></div>' for x in so["stats"])
    mx = max(x["v"] for x in so["compare"])
    bars = "".join(f'<div class="bar"><div class="bl"><span>{rt(x["name"])}</span><b>{rt(x["label"])}</b></div>'
                   f'<div class="bt"><i style="width:{max(0.6, 100 * x["v"] / mx):.2f}%"></i></div></div>' for x in so["compare"])
    sst = "".join(f'<div class="stat"><b>{x["n"]}</b><span>{rt(x["l"])}</span></div>' for x in st["stats"])
    return f'''<section class="slide found">{head(s)}
  <div class="bd cols3">
    <div class="col"><h3>{rt(h["title"])}</h3><ol class="tl">{tl}</ol></div>
    <div class="col"><h3>{rt(so["title"])}</h3><div class="stats2">{stats}</div>
      <h4>{rt(so["compare_title"])}</h4>{bars}<p class="note">{rt(so["note"])}</p></div>
    <div class="col"><h3>{rt(st["title"])}</h3><div class="stats4">{sst}</div><p class="vat">{rt(st["vat"])}</p></div>
  </div>{chrome(i)}
</section>'''


def s_gaps(s, i):
    cards = "".join(f'<div class="card"><span class="no">{n:02d}</span><h3>{rt(c["t"])}</h3><p>{rt(c["b"])}</p>'
                    f'<p class="angle">{ARROW}<span>{rt(c["a"])}</span></p></div>' for n, c in enumerate(s["cards"], 1))
    return f'<section class="slide gaps">{head(s)}<div class="bd grid3x2">{cards}</div>{chrome(i)}</section>'


def s_how(s, i):
    st = s["steps"]
    pw, ph, pw3 = 320, 425, 560
    p1, _ = store_frame(s["store_photo"], pw, ph)
    p2, _ = store_frame(s["store_photo"], pw, ph, pins=s["pins"])
    legend = "".join(f'<li><span class="pin s">{n}</span>{html.escape(t(p["l"]))}{TICK}</li>' for n, p in enumerate(s["pins"], 1))
    regs = t(st[2]["regs"])
    lines = st[2]["lines"]
    tw = 262
    p3 = (f'<div class="p3pair"><figure>{pic(s["pair"], tw, tw, "fusha")}<figcaption>{html.escape(regs[0])}</figcaption></figure>'
          f'<figure>{pic(s["pair"], tw, tw, "saudi")}<figcaption>{html.escape(regs[1])}</figcaption></figure></div>'
          f'<div class="p3lines"><p><b>{html.escape(regs[0])}</b><span lang="ar" dir="rtl">{html.escape(lines["fusha"])}</span></p>'
          f'<p><b>{html.escape(regs[1])}</b><span lang="ar" dir="rtl">{html.escape(lines["saudi"])}</span></p></div>')
    ch = st[3]["chart"]
    keys = t(ch["keys"])
    rows = ""
    for r in ch["rows"]:
        segs = "".join(f'<i class="k{n}" style="flex:{v}">{v}%</i>' for n, v in enumerate(r["v"]))
        rows += f'<div class="crow"><span>{rt(r["l"])}</span><div class="stack">{segs}</div></div>'
    leg = "".join(f'<span><i class="k{n}"></i>{html.escape(k)}</span>' for n, k in enumerate(keys))
    chart = f'<div class="chart"><div class="ct">{rt(ch["title"])}</div>{rows}<div class="leg">{leg}</div></div>'
    p4post = f'<div class="p4post">{pic(s["poster"], 176, 220, s.get("poster_reg", "saudi"))}</div>'
    panels = [
        (pw, f'<div class="frwrap">{p1}<span class="chip on">{rt(st[0]["chip"])}</span></div>'),
        (pw, f'<div class="frwrap">{p2}<ul class="legend">{legend}</ul></div>'),
        (pw3, f'<div class="frwrap p3" style="width:{pw3}px;height:{ph}px">{p3}</div>'),
        (pw, f'<div class="frwrap p4" style="width:{pw}px;height:{ph}px">{p4post}{chart}</div>'),
    ]
    cells = ""
    for n, (stp, (w, body)) in enumerate(zip(st, panels), 1):
        cells += (f'<div class="step" style="width:{w}px"><div class="sh"><span class="sn">{n:02d}</span><h3>{rt(stp["t"])}</h3></div>{body}'
                  f'<p>{rt(stp["b"])}</p></div>')
        if n < 4:
            cells += f'<div class="sarr">{ARROW}</div>'
    return f'''<section class="slide how">{head(s, "h-sm")}
  <div class="steps">{cells}</div>
  <p class="answer">{rt(s["answer"])}</p>{chrome(i)}
</section>'''


def s_beforeafter(s, i):
    lab, sub = s["labels"], s["sublabels"]

    def pair(p, w, h, hero=False):
        b, bg = store_frame(p["before"], w, h)
        a = pic(p["after"], w, h)
        cls = "pair hero" if hero else "pair"
        return (f'<div class="{cls}"><div class="pp"><div class="ba">{b}<span class="tag before">{rt(lab["before"])}</span></div>'
                f'<div class="ba">{a}<span class="tag after">{rt(lab["after"])}</span></div></div>'
                f'<div class="pcap"><b>{html.escape(p["name"])}</b><span>{rt(p["change"])}</span></div></div>')
    pr = s["pairs"]
    subrow = f'<div class="subl"><span>{rt(sub["before"])}</span><span>{rt(sub["after"])}</span></div>'
    return f'''<section class="slide beforeafter">{head(s)}
  <div class="bd barow">
    <div class="bahero">{subrow}{pair(pr[0], 420, 525, True)}</div>
    <div class="baside">{pair(pr[1], 196, 245)}{pair(pr[2], 196, 245)}</div>
  </div>
  <p class="answer">{rt(s["caption"])}</p>{chrome(i)}
</section>'''


def s_calendar(s, i):
    d0, d1 = (date.fromisoformat(x) for x in s["range"])
    span = (d1 - d0).days

    def pos(d):
        return 100 * (date.fromisoformat(d) - d0).days / span

    months = t(s["months"])
    ticks, m = "", d0
    k = 0
    while m <= d1:
        ticks += f'<span class="mt" style="inset-inline-start:{pos(m.isoformat()):.3f}%">{html.escape(months[k])}</span>'
        k += 1
        m = date(m.year + (m.month == 12), m.month % 12 + 1, 1)
    br = "".join(f'<div class="brk" style="inset-inline-start:{pos(b["from"]):.3f}%;width:{pos(b["to"]) - pos(b["from"]):.3f}%"><span>{rt(b["l"])}</span></div>'
                 for b in s["brackets"])
    rows = ""
    for r in s["rows"]:
        marks = "".join(f'<i class="span {r["kind"]}" style="inset-inline-start:{pos(a):.3f}%;width:{max(0.6, pos(b) - pos(a)):.3f}%"></i>' for a, b in r.get("spans", []))
        marks += "".join(f'<i class="pt {r["kind"]}" style="inset-inline-start:{pos(p):.3f}%"></i>' for p in r.get("points", []))
        chips = "".join(f'<span class="pf">{html.escape(p)}</span>' for p in t(r["p"]))
        rows += (f'<div class="cr"><div class="cl"><b>{rt(r["n"])}</b><span>{rt(r["d"])}</span></div>'
                 f'<div class="cc">{marks}</div><div class="cn"><span>{rt(r["note"])}</span><div class="pfs">{chips}</div></div></div>')
    grid = "".join(f'<i class="vg" style="inset-inline-start:{pos(date(2026 + (mm < 10), mm, 1).isoformat()):.3f}%"></i>' for mm in (11, 12, 1, 2, 3))
    return f'''<section class="slide calendar">{head(s, "h-cal")}
  <div class="cal">
    <div class="cr axis"><div class="cl"></div><div class="cc">{br}</div><div class="cn"></div></div>
    <div class="cr axis"><div class="cl"></div><div class="cc">{ticks}</div><div class="cn"></div></div>
    <div class="calrows"><div class="gridl">{grid}</div>{rows}</div>
  </div>{chrome(i)}
</section>'''


def s_shots(s, i):
    w, h = 202, 252
    cells = "".join(f'<figure class="cell">{pic(x["id"], w, h)}<figcaption><b>{rt(x["n"])}</b><span>{rt(x["a"])}</span></figcaption></figure>'
                    for x in s["items"])
    return f'''<section class="slide shots">{head(s)}
  <p class="lead">{rt(s["body"])} <span class="spec">{rt(s["spec"])}</span></p>
  <div class="bd g8">{cells}</div>{chrome(i)}
</section>'''


def s_catalogue(s, i):
    w, h = 236, 295
    cells = ""
    for x in s["items"]:
        name = x["n"] if L == "ar" else x["en"]
        cells += (f'<figure class="cell">{pic(x["id"], w, h)}<figcaption><b>{html.escape(name)}</b>'
                  f'<span>{sar(x["price"])}</span></figcaption></figure>')
    cells += (f'<div class="cell notecell" style="width:{w}px;height:{h}px"><p>{rt(s["note"])}</p>'
              f'<div class="pricedemo">{sar(s["price_sample"])}</div><span>{rt(s["price_label"])}</span></div>')
    bl = "".join(f"<li>{TICK}<span>{rt(b)}</span></li>" for b in t(s["bullets"]))
    return f'''<section class="slide catalogue">{head(s, "h-side")}
  <ul class="side checks">{bl}</ul>
  <div class="bd g5">{cells}</div>{chrome(i)}
</section>'''


def s_row(s, i):
    h = s["height"]
    gap = s.get("gap", 32)
    cells = ""
    for x in s["items"]:
        rw, rh = x["ratio"]
        w = round(h * rw / rh)
        cells += f'<figure class="cell">{pic(x["id"], w, h)}<figcaption>{rt(x["c"])}</figcaption></figure>'
    return f'''<section class="slide row {s["id"]}">{head(s)}
  <div class="bd rowa" style="gap:{gap}px">{cells}</div>{chrome(i)}
</section>'''


def s_carousel(s, i):
    w = 326
    cells = "".join(f'<figure class="cell">{pic(x["id"], w, w)}<figcaption>{rt(x["c"])}</figcaption></figure>' for x in s["items"])
    return f'''<section class="slide carousel">{head(s)}
  <div class="bd rowa car">{cells}</div>
  <div class="swipe">{rt(s["swipe"])} {ARROW}</div>{chrome(i)}
</section>'''


def s_registers(s, i):
    labs = t(s["labels"])
    w = 520
    posters = (f'<div class="regp"><figure><span class="rtag f">{html.escape(labs[0])}</span>{pic(s["poster"], w, w, "fusha")}</figure>'
               f'<figure><span class="rtag s">{html.escape(labs[1])}</span>{pic(s["poster"], w, w, "saudi")}</figure></div>')
    rows = "".join(f'<tr><td lang="ar">{html.escape(a)}</td><td lang="ar">{html.escape(b)}</td></tr>' for a, b in s["pairs"])
    return f'''<section class="slide registers">{head(s, "h-side")}
  <div class="regtext"><p>{rt(s["body"])}</p>
    <table class="pairs"><thead><tr><th>{html.escape(labs[0])}</th><th>{html.escape(labs[1])}</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="note">{rt(s["pairs_note"])}</p><p class="test">{rt(s["test"])}</p></div>
  {posters}<p class="regcap">{rt(s["caption"])}</p>{chrome(i)}
</section>'''


def s_media(s, i):
    tiers = "".join(f'<div class="tier{" g" if n else ""}"><span>{rt(x["n"])}</span><b>{sar(x["v"])}</b><em>{rt(x["w"])}</em></div>'
                    for n, x in enumerate(s["tiers"]))
    cols = t(s["cols"])
    rows = ""
    for r in s["rows"]:
        rows += (f'<tr><th>{rt(r["n"])}</th><td class="sh"><b>{r["s"]}%</b><div class="sb"><i style="width:{r["s"] / 35 * 100:.1f}%"></i></div></td>'
                 f'<td class="amt">{sar(r["c"])}</td><td class="amt">{sar(r["g"])}</td><td class="job">{rt(r["j"])}</td></tr>')
    return f'''<section class="slide media">{head(s)}
  <div class="bd mrow">
    <div class="mleft"><h3>{rt(s["tiers_title"])}</h3>{tiers}<p class="vat">{rt(s["vat"])}</p>
      <p class="reach">{rt(s["reach"])}</p><p class="note">{rt(s["source"])}</p></div>
    <table class="mtab"><thead><tr>{"".join(f"<th>{html.escape(c)}</th>" for c in cols)}</tr></thead><tbody>{rows}</tbody></table>
  </div>{chrome(i)}
</section>'''


def s_testplan(s, i):
    ph = ""
    for n, p in enumerate(s["phases"]):
        lis = "".join(f"<li>{rt(b)}</li>" for b in t(p["b"]))
        ph += f'<div class="phase"><h3>{rt(p["t"])}</h3><span class="pd">{rt(p["d"])}</span><ul>{lis}</ul></div>'
        if n < 2:
            ph += f'<div class="parr">{ARROW}</div>'
    bl = ""
    for b in s["blocks"]:
        lis = "".join(f"<li>{rt(x)}</li>" for x in t(b["b"]))
        bl += f'<div class="blk"><h3>{rt(b["t"])}</h3><ul>{lis}</ul></div>'
    return f'''<section class="slide testplan">{head(s)}
  <div class="phases">{ph}</div>
  <div class="blocks">{bl}</div>{chrome(i)}
</section>'''


def s_offer(s, i):
    gr = ""
    for g in s["groups"]:
        lis = "".join(f"<li>{rt(x)}</li>" for x in t(g["b"]))
        gr += f'<div class="grp"><h3>{rt(g["t"])}</h3><ul>{lis}</ul></div>'
    rows = "".join(f'<tr><th>{rt(r["t"])}<span>{rt(r["c"])}</span></th><td class="{"tbc" if r.get("tbc") else "amt"}">{rt(r["a"])}</td></tr>'
                   for r in s["rows"])
    terms = "".join(f'<li><span>{rt(x["t"])}</span><em>{rt(s["tbc"])}</em></li>' for x in s["terms"])
    return f'''<section class="slide offer">{head(s)}
  <div class="bd orow">
    <div class="oleft"><h2>{rt(s["groups_title"])}</h2><div class="grps">{gr}</div><p class="note">{rt(s["note"])}</p></div>
    <div class="oright"><h2>{rt(s["inv_title"])}</h2><table class="inv"><tbody>{rows}</tbody></table>
      <h4>{rt(s["terms_title"])}</h4><ul class="terms">{terms}</ul><p class="note">{rt(s["inv_note"])}</p></div>
  </div>{chrome(i)}
</section>'''


def s_next(s, i):
    st = "".join(f'<li><span class="nd">{rt(x["d"])}</span><span class="nt">{rt(x["t"])}</span></li>' for x in s["steps"])
    return f'''<section class="slide next">
  <div class="nx-text">{head(s)}<ol class="nsteps">{st}</ol></div>
  <div class="nx-field bleed"><img class="nx-logo" src="../brand/logo_reversed.png" alt="محمد سراج عطار وأخويه">
    <p class="nx-line">{rt(s["line"])}</p><p class="nx-by"><img src="../brand/everyside_wordmark_white.svg" alt="Everyside"></p></div>
  {chrome(i, mark=False)}
</section>'''


RENDER = {"cover": s_cover, "line": s_line, "found": s_found, "gaps": s_gaps, "how": s_how, "beforeafter": s_beforeafter,
          "calendar": s_calendar, "shots": s_shots, "catalogue": s_catalogue, "row": s_row, "carousel": s_carousel,
          "registers": s_registers, "media": s_media, "testplan": s_testplan, "offer": s_offer, "next": s_next}

# ----------------------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:'Cairo';src:url('../fonts/cairo/Cairo%5Bslnt,wght%5D.ttf') format('truetype');font-weight:200 1000;font-style:normal}
@font-face{font-family:'MessiriAr';src:url('../fonts/elmessiri/ElMessiri%5Bwght%5D.ttf') format('truetype');font-weight:400 700;
  unicode-range:U+0600-06FF,U+0750-077F,U+08A0-08FF,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}
@font-face{font-family:'Playfair Display';src:url('../fonts/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf') format('truetype');font-weight:400 900}
@font-face{font-family:'Manrope';src:url('../fonts/manrope/Manrope%5Bwght%5D.ttf') format('truetype');font-weight:200 800}
@page{size:1920px 1080px;margin:0}
:root{--ivory:#F4EFE5;--green:#004738;--gold:#C3A278;--ink:#1E1A16;--muted:#5C534A;--line:#D8CEBD;--sand:#E7DFD1;
  --goldd:#7A5C33;--card:#FAF7F1;--red:#B3261E}
html[lang=en]{--fh:'Playfair Display','MessiriAr','Cairo',serif;--fb:'Manrope','Cairo',sans-serif}
html[lang=ar]{--fh:'MessiriAr','Cairo',serif;--fb:'Cairo',sans-serif}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--ivory)}
body{font-family:var(--fb);color:var(--ink);font-synthesis:none;-webkit-print-color-adjust:exact;print-color-adjust:exact;
  font-variant-numeric:lining-nums;font-size:22px;line-height:1.5}
html[lang=ar] body{line-height:1.7}
.slide{position:relative;width:1920px;height:1080px;overflow:hidden;background:var(--ivory);break-after:page;page-break-after:always}
.slide:last-child{break-after:auto;page-break-after:auto}
h1,h2,h3,h4,p,ul,ol,figure{margin:0;padding:0}
ul,ol{list-style:none}
strong{font-weight:600}
.ltr{direction:ltr;unicode-bidi:isolate}
.lat{font-family:'Playfair Display',serif;font-weight:600}
.arab{font-family:'MessiriAr','Cairo',serif;font-weight:600}
/* riyal */
.sar{display:inline-flex;align-items:baseline;gap:.25em;direction:ltr;unicode-bidi:isolate;white-space:nowrap}
html[lang=ar] .sar{--rh:.670em} html[lang=en] .sar{--rh:.733em}
.riyal{height:var(--rh);width:calc(var(--rh) * 3000 / 3353);flex:none;fill:currentColor;overflow:visible}
.arr{width:1.1em;height:.55em;vertical-align:middle;flex:none}
html[dir=rtl] .arr{transform:scaleX(-1)}
.tick{width:.8em;height:.8em;flex:none;color:var(--green)}
/* header + chrome */
.hd{position:absolute;top:88px;inset-inline:96px 200px}
.kicker{font-size:18px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--goldd);margin-bottom:14px}
html[lang=ar] .kicker{font-size:22px;letter-spacing:0;font-weight:600}
h1{font-family:var(--fh);font-weight:600;font-size:56px;line-height:1.16;color:var(--green);letter-spacing:-.005em}
html[lang=ar] h1{font-weight:700;font-size:54px;line-height:1.4}
.h-sm h1{font-size:46px} html[lang=ar] .h-sm h1{font-size:46px}
.sub{font-size:23px;color:var(--muted);margin-top:14px;max-width:1350px}
.mark{position:absolute;top:80px;inset-inline-end:96px;width:72px;height:72px}
.ft{position:absolute;bottom:38px;inset-inline-end:96px;display:flex;justify-content:space-between;align-items:center;
  font-size:15px;color:var(--muted);border-top:1px solid var(--line);padding-top:12px}
html[lang=ar] .ft{font-size:16px}
.ft .pg{font-family:'Manrope',sans-serif;font-weight:500;letter-spacing:.06em}
.bd{position:absolute;inset-inline:96px}
.note{font-size:16px;color:var(--muted)}
/* frames */
.fr{position:relative;background:var(--sand);overflow:hidden;flex:none}
.fr img{display:block;width:100%;height:100%;object-fit:contain}
.fr.store{outline:1px solid var(--line);outline-offset:-1px}
.ph{display:flex;align-items:center;justify-content:center;border:2px dashed #B7AB97;text-align:center}
.ph b{display:block;font:600 24px 'Manrope',sans-serif;color:#7A6E5C}.ph span{font-size:15px;color:#8C8170}
figcaption{font-size:16px;line-height:1.4;color:var(--muted);margin-top:10px}
html[lang=ar] figcaption{font-size:17px;line-height:1.55}
figcaption b{display:block;color:var(--ink);font-weight:600}
/* cover */
.cover .cv-field{position:absolute;top:0;inset-inline-start:0;width:1056px;height:1080px;background:var(--green);color:var(--ivory)}
.cv-logo{position:absolute;top:150px;inset-inline-start:328px;width:400px}
.cv-text{position:absolute;top:610px;inset-inline:96px}
.cv-prep{font-size:32px;color:var(--gold);font-weight:500;margin-bottom:22px}
html[lang=ar] .cv-prep{font-weight:600}
.cv-title{font-family:var(--fh);font-weight:600;font-size:92px;line-height:1.08;color:var(--ivory)}
html[lang=ar] .cv-title{font-weight:700;font-size:96px;line-height:1.3}
.cv-sub{font-size:25px;color:#D9D2C3;margin-top:18px;max-width:820px}
.cv-foot{position:absolute;bottom:56px;inset-inline:96px;display:flex;justify-content:space-between;align-items:baseline;font-size:17px;color:#BFC9C2}
.cv-by .es{height:26px;width:auto;vertical-align:-6px;margin-inline-start:10px}
.ftl{display:inline-flex;align-items:center;gap:10px}.ft-es{height:17px;width:auto}
.nx-by img{height:30px;width:auto;display:block}
.cover .cv-hero{position:absolute;top:0;inset-inline-end:0;width:864px;height:1080px}
/* line */
.line .ln-img{position:absolute;top:0;inset-inline-start:0}
.ln-text{position:absolute;top:0;bottom:120px;inset-inline-start:976px;inset-inline-end:110px;display:flex;flex-direction:column;justify-content:center}
h1.big{font-size:62px;line-height:1.16;margin-bottom:26px}
html[lang=ar] h1.big{font-size:56px;line-height:1.55}
.ln-other{font-size:28px;color:var(--goldd);margin-bottom:44px}
.ln-body{font-size:23px;margin-bottom:22px}
.proofs{display:flex;flex-wrap:wrap;gap:12px}
.proofs li{display:flex;align-items:center;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:40px;padding:8px 18px;font-size:20px}
/* found */
.found .bd{top:280px;bottom:120px}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:64px}
.col h3{font:600 26px var(--fh);color:var(--green);border-bottom:2px solid var(--gold);padding-bottom:10px;margin-bottom:22px}
html[lang=ar] .col h3{font-weight:700;font-size:28px}
.tl li{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:12px 0;border-bottom:1px solid var(--line);font-size:19px;line-height:1.45}
html[lang=ar] .tl li{line-height:1.6}
.tl b{font-family:var(--fh);font-weight:600;font-size:24px;color:var(--green)}
.stats2{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:26px}
.stat b{display:block;font:600 50px/1.1 var(--fh);color:var(--green)}
html[lang=ar] .stat b{font:700 44px/1.3 'Cairo',sans-serif}
.stat span{font-size:17px;color:var(--muted);line-height:1.35;display:block}
.col h4{font-size:19px;font-weight:600;margin-bottom:10px}
.bar{margin-bottom:14px}
.bl{display:flex;justify-content:space-between;font-size:17px;margin-bottom:4px}
.bl b{font-weight:600}
.bt{height:16px;background:#E6DED0;border-radius:3px;overflow:hidden}
.bt i{display:block;height:100%;background:var(--green)}
.bar:last-of-type .bt i{background:#9A8F80}
.stats4{display:grid;grid-template-columns:1fr 1fr;gap:18px 20px;margin-bottom:22px}
.vat{font-size:18px;line-height:1.5;background:var(--card);border-inline-start:4px solid var(--gold);padding:14px 18px}
html[lang=ar] .vat{line-height:1.7}
/* gaps */
.gaps .bd{top:270px;bottom:120px}
.grid3x2{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:28px}
.card{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--green);padding:26px 28px;display:flex;flex-direction:column}
.card .no{font:600 22px 'Manrope',sans-serif;color:var(--goldd);margin-bottom:6px}
.card h3{font:600 29px/1.2 var(--fh);color:var(--green);margin-bottom:12px}
html[lang=ar] .card h3{font-weight:700;line-height:1.4}
.card p{font-size:19px;line-height:1.5}
html[lang=ar] .card p{line-height:1.65}
.card .angle{margin-top:auto;display:flex;gap:10px;align-items:baseline;color:var(--green);font-weight:600;padding-top:12px}
/* how */
.how .hd{inset-inline-end:200px}
.steps{position:absolute;top:350px;inset-inline:96px;display:flex;align-items:flex-start}
.step{width:340px;flex:none}
.sarr{width:64px;flex:none;display:flex;justify-content:center;padding-top:250px;color:var(--gold);font-size:40px}
.sh{display:flex;align-items:baseline;gap:14px;margin-bottom:12px;height:44px}
.sn{font:700 30px 'Manrope',sans-serif;color:var(--goldd)}
.sh h3{font:600 26px var(--fh);color:var(--green);white-space:nowrap}
html[lang=ar] .sh h3{font-weight:700;font-size:27px}
.step>p{font-size:18px;line-height:1.45;margin-top:12px;color:var(--ink)}
html[lang=ar] .step>p{line-height:1.6}
.frwrap{position:relative}
.chip{display:inline-flex;align-items:center;gap:6px;background:rgba(250,247,241,.94);color:var(--ink);font-size:15px;font-weight:600;
  padding:5px 12px;border-radius:30px;border:1px solid var(--line)}
.frwrap>.chip.on{position:absolute;top:14px;inset-inline-start:14px}
.pin{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;border-radius:50%;background:var(--green);color:#fff;
  font:700 16px/30px 'Manrope',sans-serif;text-align:center;box-shadow:0 0 0 3px rgba(255,255,255,.9)}
.pin.s{position:static;display:inline-block;margin:0;width:22px;height:22px;font-size:13px;line-height:22px;box-shadow:none;flex:none}
.legend{position:absolute;inset-inline:12px;bottom:12px;display:grid;grid-template-columns:1fr 1fr;gap:6px 10px}
.legend li{display:flex;align-items:center;gap:7px;font-size:14.5px;font-weight:600;line-height:1.2}
.chips3{position:absolute;top:14px;inset-inline:14px;display:flex;flex-direction:column;align-items:flex-start;gap:8px}
.chip.shd{position:absolute;bottom:14px;inset-inline-start:14px}
.p4{background:var(--card);border:1px solid var(--line);padding:10px}
.p4post{display:flex;justify-content:center}
.p3{background:var(--card);border:1px solid var(--line);padding:12px}
.p3pair{display:flex;justify-content:space-between}
.p3pair figcaption{margin-top:4px;text-align:center;font-weight:700;color:var(--green);font-size:16px}
.p3lines{margin-top:10px;display:flex;flex-direction:column;gap:6px}
.p3lines p{display:flex;gap:10px;align-items:baseline;font-size:17px;line-height:1.5;margin:0}
.p3lines b{flex:none;min-width:52px;color:var(--gold);font-weight:700}
.p3lines span{font-family:'Cairo',sans-serif}
.p4post figcaption{margin-top:4px;text-align:center;font-weight:600;color:var(--ink);font-size:15px}
.chart{margin-top:10px}
.ct{font-size:13.5px;color:var(--muted);margin-bottom:6px;line-height:1.3}
.crow{display:grid;grid-template-columns:96px 1fr;align-items:center;gap:8px;margin-bottom:6px;font-size:13.5px;line-height:1.2}
.stack{display:flex;height:24px;border-radius:3px;overflow:hidden}
.stack i{display:flex;align-items:center;justify-content:center;color:#fff;font:600 12px 'Manrope',sans-serif;font-style:normal}
.k0{background:#9A8F80}.k1{background:var(--green)}.k2{background:var(--gold)}
.leg{display:flex;gap:12px;font-size:12.5px;color:var(--muted);margin-top:4px}
.leg i{display:inline-block;width:10px;height:10px;margin-inline-end:4px;vertical-align:middle}
.answer{position:absolute;bottom:104px;inset-inline:96px;font:600 24px var(--fb);color:var(--green);border-top:1px solid var(--line);padding-top:16px}
/* before/after */
.barow{top:268px;display:flex;gap:72px}
.subl{display:flex;gap:12px;margin-bottom:8px}
.subl span{width:420px;font-size:17px;color:var(--muted);font-weight:600}
.pp{display:flex;gap:12px}
.ba{position:relative}
.tag{position:absolute;top:14px;inset-inline-start:14px;font:700 30px/1 var(--fb);padding:9px 16px 11px;border-radius:4px;color:#fff;letter-spacing:.02em}
html[lang=ar] .tag{font:700 32px/1.1 'Cairo',sans-serif;padding:6px 18px 10px}
.tag.before{background:var(--ink)}.tag.after{background:var(--green)}
.pair:not(.hero) .tag{font-size:27px;padding:7px 12px 9px;top:10px;inset-inline-start:10px}
html[lang=ar] .pair:not(.hero) .tag{font-size:28px;padding:4px 12px 8px}
.pcap{margin-top:12px;font-size:18px;line-height:1.45}
.pcap b{display:block;font-weight:600;color:var(--green);font-size:20px}
.pcap span{color:var(--muted);display:inline-flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.baside{display:flex;flex-direction:column;gap:34px;padding-top:34px}
.baside .pair{display:flex;gap:24px;align-items:flex-start}
.baside .pcap{margin-top:0;width:300px}
.beforeafter .answer{bottom:112px}
/* calendar */
.calendar .sub{max-width:1500px}
.cal{position:absolute;top:340px;inset-inline:96px}
.cr{display:grid;grid-template-columns:330px 1fr 380px;gap:28px;align-items:center}
.cr.axis{height:30px}
.cc{position:relative;height:100%}
.calrows{position:relative}
.calrows .cr{height:59px;border-bottom:1px solid var(--line)}
.gridl{position:absolute;top:0;bottom:0;inset-inline-start:358px;inset-inline-end:408px}
.vg{position:absolute;top:0;bottom:0;width:1px;background:var(--line)}
.calrows .cc{height:59px}
.cl b{display:block;font-size:19px;font-weight:600;line-height:1.25;color:var(--green)}
.cl span{font-size:14.5px;color:var(--muted);line-height:1.3;display:block}
.cn span{font-size:15px;line-height:1.3;display:block}
.pfs{display:flex;gap:5px;flex-wrap:wrap;margin-top:3px}
.pf{font-size:12.5px;font-weight:600;background:#E6DED0;border-radius:3px;padding:1px 7px;line-height:1.5}
.span{position:absolute;top:22px;height:16px;border-radius:8px}
.pt{position:absolute;top:21px;width:18px;height:18px;margin-inline-start:-9px;transform:rotate(45deg);border:2px solid var(--ivory)}
.season{background:var(--green)}.event{background:var(--gold)}.pay{background:var(--goldd)}.trade{background:#8C6A3E}
.religious{background:#3E5A50}.national{background:var(--red)}
.span.trade{background:repeating-linear-gradient(135deg,#8C6A3E 0 8px,#A8865A 8px 16px)}
.mt{position:absolute;top:4px;font-size:15px;font-weight:600;color:var(--muted);padding-inline-start:6px;border-inline-start:1px solid var(--muted)}
.brk{position:absolute;top:2px;height:24px;border:1.5px solid var(--green);border-bottom:none;border-radius:4px 4px 0 0;text-align:center}
.brk span{position:relative;top:-14px;background:var(--ivory);padding:0 10px;font-size:15px;font-weight:600;color:var(--green)}
/* shots */
.shots .lead{position:absolute;top:262px;inset-inline:96px 96px;font-size:20px;color:var(--muted)}
.spec{color:var(--goldd);font-weight:600;white-space:nowrap}
.g8{top:340px;display:grid;grid-template-columns:repeat(8,202px);gap:22px 16px}
.g8 figcaption{font-size:15px;margin-top:7px;line-height:1.35}
html[lang=ar] .g8 figcaption{font-size:16px;line-height:1.45}
/* catalogue */
.h-side{inset-inline-end:auto;width:400px}
.registers .h-side{width:520px}.registers .h-side h1{font-size:40px}
.h-side h1{font-size:44px} html[lang=ar] .h-side h1{font-size:42px}
.side{position:absolute;top:470px;inset-inline-start:96px;width:390px}
.checks li{display:flex;gap:12px;align-items:baseline;font-size:19px;line-height:1.45;padding:9px 0;border-bottom:1px solid var(--line)}
html[lang=ar] .checks li{line-height:1.6}
.g5{top:96px;inset-inline-start:552px;inset-inline-end:96px;display:grid;grid-template-columns:repeat(5,236px);gap:28px 23px}
.g5 figcaption{font-size:15px;margin-top:6px}
html[lang=ar] .g5 figcaption{font-size:16px}
.g5 figcaption b{line-height:1.3}
.g5 figcaption .sar{color:var(--green);font-weight:600;font-size:17px}
.catalogue .mark{display:none}
.notecell{background:var(--green);color:var(--ivory);padding:24px;display:flex;flex-direction:column;gap:14px}
.notecell p{font-size:19px;line-height:1.45}
.pricedemo{font:700 44px 'Cairo',sans-serif;color:var(--gold);margin-top:auto}
html[lang=en] .pricedemo{font-family:'Manrope',sans-serif}
.notecell>span{font-size:15px;color:#CFD8D2}
/* rows */
.row .bd{top:var(--rowtop,330px)}
.rowa{display:flex;align-items:flex-start}
.rowa figcaption{max-width:100%}
.campaignwork .bd{top:330px}
.howposters .bd{top:350px}
/* carousel */
.carousel .bd{top:350px;gap:24px}
.swipe{position:absolute;top:780px;inset-inline-end:96px;display:flex;gap:10px;align-items:center;font-size:20px;font-weight:600;color:var(--green)}
/* registers */
.regtext{position:absolute;top:410px;inset-inline-start:96px;width:500px}
.regtext>p{font-size:19px;line-height:1.5;margin-bottom:18px}
html[lang=ar] .regtext>p{line-height:1.7}
.pairs{width:100%;border-collapse:collapse;margin-bottom:10px}
.pairs th{text-align:start;font-size:16px;color:var(--goldd);font-weight:600;padding:4px 0;border-bottom:2px solid var(--gold)}
.pairs td{font-family:'Cairo',sans-serif;font-size:19px;font-weight:600;padding:5px 0;border-bottom:1px solid var(--line);direction:rtl;text-align:start;width:50%}
html[lang=en] .pairs td{text-align:left}
html[lang=en] .pairs th{text-align:left}
.pairs td+td{color:var(--goldd)}
.test{font-size:18px;font-weight:600;color:var(--green);margin-top:10px}
.regp{position:absolute;top:150px;inset-inline-end:96px;display:flex;gap:36px}
.regp figure{position:relative}
.rtag{position:absolute;top:-46px;inset-inline-start:0;font-size:24px;font-weight:700;color:var(--green)}
.rtag.s{color:var(--goldd)}
.regcap{position:absolute;top:740px;inset-inline-end:96px;width:1076px;text-align:center;font:600 24px var(--fb);color:var(--green)}
.registers .mark{display:none}
/* media */
.mrow{top:280px;display:grid;grid-template-columns:470px 1fr;gap:64px}
.mleft h3{font-size:19px;font-weight:600;color:var(--goldd);margin-bottom:12px}
.tier{background:var(--card);border:1px solid var(--line);padding:16px 22px;margin-bottom:14px;display:grid;grid-template-columns:1fr auto;align-items:baseline}
.tier span{font-size:20px;font-weight:600}
.tier b{font:700 46px 'Cairo',sans-serif;color:var(--green)}
html[lang=en] .tier b{font-family:'Manrope',sans-serif}
.tier em{grid-column:1/-1;font-style:normal;font-size:16px;color:var(--muted)}
.tier.g{border-top:4px solid var(--gold)}.tier:not(.g){border-top:4px solid var(--green)}
.mleft .vat{margin:6px 0 16px;font-size:16px}
.reach{font-size:18px;line-height:1.5;margin-bottom:6px}
table.mtab{border-collapse:collapse;width:100%;align-self:start}
.mtab th,.mtab td{text-align:start;padding:12px 10px;border-bottom:1px solid var(--line);vertical-align:middle}
.mtab thead th{font-size:15px;color:var(--goldd);font-weight:600;border-bottom:2px solid var(--gold)}
.mtab tbody th{font:600 22px var(--fb);color:var(--green);white-space:nowrap}
.mtab td.sh{width:130px}.mtab td.sh b{font-size:20px}
.sb{height:8px;background:#E6DED0;margin-top:4px}.sb i{display:block;height:100%;background:var(--green)}
.mtab td.amt{font-size:20px;font-weight:600;white-space:nowrap}
.mtab td.job{font-size:16.5px;line-height:1.4;color:var(--ink)}
html[lang=ar] .mtab td.job{line-height:1.55}
/* testplan */
.phases{position:absolute;top:270px;inset-inline:96px;display:flex;align-items:stretch}
.phase{flex:1;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--green);padding:18px 22px}
.phase h3{font:600 25px var(--fh);color:var(--green)} html[lang=ar] .phase h3{font-weight:700}
.pd{display:block;font-size:16px;font-weight:600;color:var(--goldd);margin:2px 0 8px}
.phase li,.blk li,.grp li{position:relative;padding-inline-start:16px;font-size:17px;line-height:1.42;margin-bottom:5px}
html[lang=ar] .phase li,html[lang=ar] .blk li,html[lang=ar] .grp li{line-height:1.6}
.phase li:before,.blk li:before,.grp li:before{content:"";position:absolute;inset-inline-start:0;top:.62em;width:6px;height:6px;background:var(--gold)}
.parr{width:44px;flex:none;display:flex;align-items:center;justify-content:center;color:var(--gold);font-size:28px}
.blocks{position:absolute;top:620px;inset-inline:96px;display:grid;grid-template-columns:repeat(3,1fr);gap:44px}
.blk h3{font:600 21px var(--fb);color:var(--green);border-bottom:2px solid var(--gold);padding-bottom:6px;margin-bottom:10px}
.blk li{font-size:16px}
/* offer */
.orow{top:270px;display:grid;grid-template-columns:1fr 760px;gap:72px}
.offer h2{font:600 24px var(--fh);color:var(--green);margin-bottom:14px} html[lang=ar] .offer h2{font-weight:700}
.grps{display:grid;grid-template-columns:1fr 1fr;gap:18px 32px;margin-bottom:12px}
.grp h3{font-size:19px;font-weight:700;color:var(--goldd);margin-bottom:6px}
.grp li{font-size:16.5px}
table.inv{width:100%;border-collapse:collapse;margin-bottom:16px}
.inv th{text-align:start;font-size:20px;font-weight:600;color:var(--green);padding:11px 0;border-bottom:1px solid var(--line)}
.inv th span{display:block;font-size:15.5px;font-weight:400;color:var(--muted);line-height:1.4}
.inv td{text-align:end;padding:11px 0;border-bottom:1px solid var(--line);font-size:18px;font-weight:600;width:270px}
.inv td.tbc{color:var(--goldd);font-style:italic;font-weight:500}
html[lang=ar] .inv td.tbc{font-style:normal}
.offer h4{font-size:17px;font-weight:600;margin-bottom:6px}
.terms{display:grid;grid-template-columns:1fr 1fr;gap:6px 28px;margin-bottom:12px}
.terms li{display:flex;justify-content:space-between;gap:10px;font-size:16px;border-bottom:1px dotted var(--line);padding:3px 0}
.terms em{color:var(--goldd)}
/* next */
.next .nx-text{position:absolute;inset:0}
.next .hd{inset-inline-end:960px}
.nsteps{position:absolute;top:330px;inset-inline-start:96px;width:820px;counter-reset:n}
.nsteps li{display:grid;grid-template-columns:210px 1fr;gap:24px;padding:24px 0;border-bottom:1px solid var(--line);align-items:baseline}
.nd{font-weight:700;color:var(--goldd);font-size:22px}
.nt{font-size:26px;line-height:1.45}
.nsteps li:last-child .nt{font-weight:700;color:var(--green)}
.nx-field{position:absolute;top:0;inset-inline-end:0;width:864px;height:1080px;background:var(--green);color:var(--ivory);
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.nx-logo{width:420px;margin-bottom:96px}
.nx-line{font:600 36px/1.35 var(--fh);color:var(--gold);max-width:640px}
html[lang=ar] .nx-line{font-weight:700;line-height:1.6}
.nx-by{position:absolute;bottom:56px;font:700 18px 'Manrope',sans-serif;color:#BFC9C2;letter-spacing:.04em}
.next .ft{inset-inline-end:960px}
.slide *{font-variant-numeric:lining-nums!important}
"""


def build_html(lang):
    global L
    L = lang
    body = "".join(RENDER[s["type"]](s, n) for n, s in enumerate(C["slides"], 1))
    sym = (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><symbol id="riyal" viewBox="0 0 3000 3353">'
           f'<path fill-rule="evenodd" d="{RIYAL_D}"/></symbol></defs></svg>')
    d = "rtl" if lang == "ar" else "ltr"
    doc = (f'<!doctype html><html lang="{lang}" dir="{d}"><head><meta charset="utf-8"><title>{html.escape(t(C["meta"]["title"]))}</title>'
           f'<style>{CSS}</style></head><body>{sym}{body}</body></html>')
    out = PROP / f"proposal_{lang}.html"
    out.write_text(doc, encoding="utf-8")
    return out


QA_JS = r"""() => {
  const out = [];
  document.querySelectorAll('section.slide').forEach((sec, si) => {
    const R = sec.getBoundingClientRect();
    sec.querySelectorAll('*').forEach(el => {
      if (el.closest('.bleed') || el.closest('svg') || el.closest('.ft')) return;
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (!hasText && !el.classList.contains('fr')) return;
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) return;
      const x0 = r.left - R.left, x1 = r.right - R.left, y0 = r.top - R.top, y1 = r.bottom - R.top;
      if (x0 < 90 || x1 > 1830 || y0 < 70 || y1 > 1022)
        out.push(`slide ${si + 1}: <${el.tagName.toLowerCase()} class="${el.className}"> out of safe area [${x0|0},${y0|0} → ${x1|0},${y1|0}] "${(el.textContent||'').trim().slice(0, 40)}"`);
    });
    // footer collision
    const ft = sec.querySelector('.ft');
    if (ft) {
      const fr = ft.getBoundingClientRect();
      sec.querySelectorAll('p,li,figcaption,.fr,h1,h3,td,th').forEach(el => {
        if (el.closest('.bleed') || el.closest('.ft')) return;
        const r = el.getBoundingClientRect();
        if (r.height && r.bottom > fr.top - 6 && r.right > fr.left && r.left < fr.right)
          out.push(`slide ${si + 1}: <${el.tagName.toLowerCase()}> touches footer (${(r.bottom - R.top)|0} > ${(fr.top - R.top)|0}) "${(el.textContent||'').trim().slice(0, 40)}"`);
      });
    }
  });
  const bad = [...document.fonts].filter(f => f.status === 'error').map(f => f.family);
  if (bad.length) out.push('font errors: ' + bad.join(', '));
  const lg = document.querySelector('.cv-logo'), es = document.querySelector('.cv-by .es');
  if (lg && es) out.push(`cover: client logo ${lg.getBoundingClientRect().width|0}px (${(lg.getBoundingClientRect().width/19.2).toFixed(1)}% of width), Everyside ${es.getBoundingClientRect().width|0}px`);
  return out;
}"""


def qa(html_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(channel="msedge", headless=True)
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(html_path.resolve().as_uri(), wait_until="load")
        pg.evaluate("async () => { await document.fonts.ready; await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))); }")
        res = pg.evaluate(QA_JS)
        b.close()
    return res


def main():
    args = sys.argv[1:]
    paths = [build_html("ar"), build_html("en")]
    for f in IMG.glob("*.jpg"):
        if f.name not in USED:
            f.unlink()
    miss = sorted(k for k, v in STATUS.items() if v != "final")
    print(f"slides: {TOTAL} · image slots: {len(STATUS)} · missing: {len(miss)} {miss if miss else ''}")
    if "--qa" in args:
        for pth in paths:
            for line in qa(pth):
                print(f"[qa {pth.stem[-2:]}] {line}")
    if "--html" not in args:
        for lang, pth in zip(("AR", "EN"), paths):
            pdf = PROP / f"Siraj-Attar-Proposal-{lang}.pdf"
            subprocess.run([sys.executable, str(ROOT / "tools" / "render.py"), "pdf", str(pth), str(pdf)], check=True, cwd=ROOT)
            print("wrote", pdf.relative_to(ROOT), f"{pdf.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
