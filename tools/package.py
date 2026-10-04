"""Assemble the local delivery folder: deliverables/ with every asset, contact sheets and an index.

  python tools/package.py
"""
import json, os, shutil
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
D = "deliverables"
assets = json.load(open("plan/assets.json", encoding="utf-8"))
GROUP = {"product_shot": "01_product_shots", "poster": "02_catalogue_posters"}


def folder(a):
    return GROUP.get(a["kind"], "03_campaign_mawsim_al_wasm")


def sheet(files, out, cols, cell_w, label=True):
    ims = [(os.path.basename(f), Image.open(f).convert("RGB")) for f in files if os.path.exists(f)]
    if not ims:
        return
    hs = [int(im.height * cell_w / im.width) for _, im in ims]
    rows = (len(ims) + cols - 1) // cols
    rh = [max(hs[r * cols:(r + 1) * cols]) + (34 if label else 0) for r in range(rows)]
    S = Image.new("RGB", (cols * cell_w + (cols + 1) * 16, sum(rh) + (rows + 1) * 16), (244, 239, 229))
    d = ImageDraw.Draw(S)
    font = ImageFont.truetype("arial.ttf", 20)
    y = 16
    for r in range(rows):
        x = 16
        for i in range(r * cols, min((r + 1) * cols, len(ims))):
            name, im = ims[i]
            S.paste(im.resize((cell_w, hs[i]), Image.LANCZOS), (x, y))
            if label:
                d.text((x, y + hs[i] + 6), os.path.splitext(name)[0], fill=(30, 26, 22), font=font)
            x += cell_w + 16
        y += rh[r] + 16
    S.save(out, quality=88)


def main():
    if os.path.exists(D):
        shutil.rmtree(D)
    rows = []
    for a in assets:
        sub = os.path.join(D, folder(a))
        os.makedirs(sub, exist_ok=True)
        if a["kind"] == "product_shot":
            src = f"posters/out/{a['id']}.png"
            shutil.copy(src, os.path.join(sub, f"{a['id']}.png"))
            os.makedirs(os.path.join(sub, "full_resolution"), exist_ok=True)
            ext = os.path.splitext(a["image"])[1]
            shutil.copy(a["image"], os.path.join(sub, "full_resolution", f"{a['id']}{ext}"))
            files = f"{a['id']}.png"
        else:
            for t in ("fusha", "saudi"):
                os.makedirs(os.path.join(sub, t), exist_ok=True)
                shutil.copy(f"posters/out/{a['id']}_{t}.png", os.path.join(sub, t, f"{a['id']}_{t}.png"))
            files = f"fusha/{a['id']}_fusha.png, saudi/{a['id']}_saudi.png"
        rows.append(f"| {a['id']} | {a['kind']} | {a['format']} | {a.get('layout') or '-'} | {a['title_en']} | {folder(a)}/{files} |")
    vids = []  # no reels or videos in this delivery (client instruction)
    if vids:
        os.makedirs(os.path.join(D, "04_videos"), exist_ok=True)
        for v in vids:
            shutil.copy(f"gen/out/{v}.mp4", os.path.join(D, "04_videos", f"{v}.mp4"))
    # contact sheets
    os.makedirs(os.path.join(D, "00_overview"), exist_ok=True)
    shots = [f"posters/out/{a['id']}.png" for a in assets if a["kind"] == "product_shot"]
    sheet(shots, f"{D}/00_overview/product_shots.jpg", 4, 420)
    for t in ("fusha", "saudi"):
        sheet([f"posters/out/{a['id']}_{t}.png" for a in assets if a["kind"] == "poster"], f"{D}/00_overview/catalogue_{t}.jpg", 3, 420)
        sheet([f"posters/out/{a['id']}_{t}.png" for a in assets if a["kind"] not in ("product_shot", "poster")], f"{D}/00_overview/campaign_{t}.jpg", 5, 340)
    pairs = []
    for a in assets:
        if a["kind"] != "product_shot":
            pairs += [f"posters/out/{a['id']}_fusha.png", f"posters/out/{a['id']}_saudi.png"]
    sheet(pairs[:24], f"{D}/00_overview/two_tones_side_by_side_1.jpg", 4, 360)
    sheet(pairs[24:], f"{D}/00_overview/two_tones_side_by_side_2.jpg", 4, 360)
    for f in ("Siraj-Attar-Proposal-AR.pdf", "Siraj-Attar-Proposal-EN.pdf"):
        if os.path.exists(f"proposal/{f}"):
            shutil.copy(f"proposal/{f}", f"{D}/{f}")
    led = [json.loads(l) for l in open("gen/ledger.jsonl", encoding="utf-8") if l.strip()]
    spent = sum(r.get("cost", 0) for r in led if r.get("status") in ("completed", "unknown"))
    open(f"{D}/README.md", "w", encoding="utf-8").write(
        "# Siraj Attar: 40 assets + proposal (Claude Code + Higgsfield)\n\n"
        "Every poster ships twice with the identical design: `fusha/` (فصحى) and `saudi/` (سعودي). "
        "Prices are VAT-inclusive (store prices x 1.15) and use the official Saudi Riyal symbol. "
        "Product shots have no text; `full_resolution/` holds the 2K originals.\n\n"
        f"Higgsfield credits spent: {spent:.2f} (ledger: gen/ledger.jsonl).\n\n"
        "| id | kind | format | layout | asset | file(s) |\n|---|---|---|---|---|---|\n" + "\n".join(rows) +
        ("\n\nVideos (bonus): " + ", ".join(f"04_videos/{v}.mp4" for v in vids) if vids else "") + "\n")
    print("packaged", len(rows), "assets;", "videos:", vids, "; credits", round(spent, 2))


if __name__ == "__main__":
    main()
