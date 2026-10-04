"""PIL/numpy/OpenCV heuristics for every product's MAIN photograph (n=1) + labelled contact sheets for visual review.

Writes scratch/photo_features.json and scratch/sheets/sheet_XX.jpg.
Features: border uniformity/brightness (plain studio background), skin fraction (worn by model / hands),
edge density + border-vs-centre texture similarity (fabric close-up), saturation (lifestyle colour), resolution.
"""
import json, os
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cat = json.load(open(os.path.join(ROOT, 'data', 'catalogue.json'), encoding='utf-8'))


def feats(path):
    im = Image.open(path).convert('RGB')
    W, H = im.size
    sm = im.copy(); sm.thumbnail((400, 400))
    a = np.asarray(sm).astype(np.float32)
    h, w, _ = a.shape
    m = max(2, int(0.05 * min(h, w)))
    border = np.concatenate([a[:m].reshape(-1, 3), a[-m:].reshape(-1, 3), a[:, :m].reshape(-1, 3), a[:, -m:].reshape(-1, 3)])
    lum_b = border.mean(1)
    sat_b = border.max(1) - border.min(1)
    plain = (lum_b > 200) & (sat_b < 25)          # white / light grey studio pixels
    bgr = cv2.cvtColor(np.asarray(sm), cv2.COLOR_RGB2BGR)
    ycc = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
    cr, cb = ycc[..., 1].astype(int), ycc[..., 2].astype(int)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    skin = (cr > 135) & (cr < 175) & (cb > 85) & (cb < 130) & (hsv[..., 1] > 40) & (hsv[..., 2] > 60)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 60, 160)
    centre = (slice(h // 4, 3 * h // 4), slice(w // 4, 3 * w // 4))
    ed_c = edges[centre].mean() / 255
    ed_b = np.concatenate([edges[:m].ravel(), edges[-m:].ravel()]).mean() / 255
    sat = (a.max(2) - a.min(2))
    # fraction of whole image that is plain light background
    plain_all = ((a.mean(2) > 200) & (sat < 25)).mean()
    return {
        'width': W, 'height': H, 'long_edge': max(W, H), 'aspect': round(W / H, 3),
        'border_plain_frac': round(float(plain.mean()), 3),
        'border_lum': round(float(lum_b.mean()), 1), 'border_std': round(float(border.std(0).mean()), 1),
        'plain_frac_all': round(float(plain_all), 3),
        'skin_frac': round(float(skin.mean()), 3),
        'skin_frac_upper_half': round(float(skin[: h // 2].mean()), 3),
        'edge_centre': round(float(ed_c), 3), 'edge_border': round(float(ed_b), 3),
        'mean_sat': round(float(sat.mean()), 1),
        'sharpness': round(float(cv2.Laplacian(cv2.cvtColor(np.asarray(im.resize((min(W, 1200), int(H * min(W, 1200) / W)))), cv2.COLOR_RGB2GRAY), cv2.CV_64F).var()), 1),
    }


def guess(f):
    if f['skin_frac'] > 0.04 and f['skin_frac_upper_half'] > 0.03:
        return 'worn_by_model'
    if f['border_plain_frac'] > 0.85:
        return 'packshot_plain'
    if f['edge_border'] > 0.08 and abs(f['edge_border'] - f['edge_centre']) < 0.06 and f['border_plain_frac'] < 0.2:
        return 'fabric_closeup'
    if f['border_std'] < 12 and f['border_plain_frac'] < 0.5:
        return 'packshot_coloured_bg'
    return 'lifestyle'


def main():
    out = {}
    tiles = []
    for p in cat:
        files = p.get('image_files') or []
        if not files:
            continue
        main = files[0]
        f = feats(os.path.join(ROOT, main['path']))
        f['heuristic'] = guess(f)
        f['path'] = main['path']
        out[p['id']] = f
        tiles.append((p['id'], main['path'], f['heuristic'], p['top_level_categories'][0] if p['top_level_categories'] else 'uncat'))
    os.makedirs(os.path.join(ROOT, 'scratch', 'sheets'), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, 'scratch', 'photo_features.json'), 'w', encoding='utf-8'), indent=1)
    font = ImageFont.truetype('arial.ttf', 18)
    T, cols, rows = 300, 6, 4
    for s in range(0, len(tiles), cols * rows):
        sheet = Image.new('RGB', (cols * T, rows * (T + 26)), 'white')
        d = ImageDraw.Draw(sheet)
        for k, (pid, path, hg, _) in enumerate(tiles[s:s + cols * rows]):
            im = Image.open(os.path.join(ROOT, path)).convert('RGB'); im.thumbnail((T - 6, T - 6))
            x, y = (k % cols) * T, (k // cols) * (T + 26)
            sheet.paste(im, (x + (T - im.size[0]) // 2, y + (T - im.size[1]) // 2))
            d.rectangle([x, y, x + T - 1, y + T - 1], outline=(200, 0, 0))
            d.text((x + 4, y + T + 3), f'{pid} {hg}', fill=(0, 0, 0), font=font)
        sheet.save(os.path.join(ROOT, 'scratch', 'sheets', f'sheet_{s // (cols * rows) + 1:02d}.jpg'), quality=85)
    print('features', len(out))


if __name__ == '__main__':
    main()
