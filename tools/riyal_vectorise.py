"""Vectorise brand/riyal.png (official Saudi Riyal symbol) into brand/riyal.svg.

Pipeline
  1. The PNG stores the glyph in its alpha channel (17 anti-aliasing levels).
     Upsample alpha 4x (bilinear), threshold at 50 % coverage -> sub-pixel mask.
  2. cv2.findContours(RETR_CCOMP) keeps outer contours and holes.
  3. Light Gaussian smoothing along each contour, resample at 0.5 px.
  4. Corner detection (turning angle over an 8 px window, non-max suppressed),
     corners sharpened by intersecting lines fitted on both sides.
  5. Between corners: straight run -> L, otherwise Schneider cubic-bezier
     fitting (tolerance 0.5 px at 3000 px) -> C.
  6. viewBox = tight bounding box of the fitted outline, fill="currentColor".

Run:  .venv\\Scripts\\python tools\\riyal_vectorise.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "brand" / "riyal.png"
OUT = ROOT / "brand" / "riyal.svg"
META = ROOT / "brand" / "riyal_vector_meta.json"

UP = 4            # sub-pixel factor
PAD = 8           # glyph touches the image edges, pad before contouring
STEP = 0.5        # resample spacing (src px)
TOL = 0.5         # max fit error (src px)
CORNER_DEG = 22   # turning angle that counts as a corner
WIN = 8.0         # half window (src px) for the turning angle


# ---------------------------------------------------------------- contours
def subpixel_contours():
    rgba = np.array(Image.open(SRC))
    alpha = rgba[..., 3] if rgba.ndim == 3 and rgba.shape[2] == 4 else 255 - np.array(Image.open(SRC).convert("L"))
    h, w = alpha.shape
    a = np.pad(alpha, PAD, constant_values=0)
    big = cv2.resize(a, (a.shape[1] * UP, a.shape[0] * UP), interpolation=cv2.INTER_LINEAR)
    mask = (big >= 128).astype(np.uint8)
    del big
    cs, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    out = []
    for i, c in enumerate(cs):
        p = c[:, 0, :].astype(np.float64)
        p = (p + 0.5) / UP - PAD          # pixel-edge coordinates of the source
        is_hole = hier[0][i][3] != -1
        out.append((p, is_hole))
    return out, (w, h)


def resample_closed(p: np.ndarray, step: float) -> np.ndarray:
    q = np.vstack([p, p[:1]])
    seg = np.linalg.norm(np.diff(q, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    n = max(8, int(round(s[-1] / step)))
    t = np.linspace(0, s[-1], n, endpoint=False)
    return np.column_stack([np.interp(t, s, q[:, 0]), np.interp(t, s, q[:, 1])])


def smooth_closed(p: np.ndarray, sigma_samples: float) -> np.ndarray:
    r = int(math.ceil(3 * sigma_samples))
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma_samples) ** 2)
    k /= k.sum()
    ext = np.vstack([p[-r:], p, p[:r]])
    return np.column_stack([np.convolve(ext[:, 0], k, "valid"), np.convolve(ext[:, 1], k, "valid")])


def _area(p: np.ndarray) -> float:
    return 0.5 * float(np.sum(p[:, 0] * np.roll(p[:, 1], -1) - np.roll(p[:, 0], -1) * p[:, 1]))


def outward_offset(p: np.ndarray, d: float, hole: bool) -> np.ndarray:
    """Contour pixels sit (on average) half a sub-pixel inside the true
    50 % iso-line; push them out of the filled region by d."""
    t = np.roll(p, -1, 0) - np.roll(p, 1, 0)
    t /= np.linalg.norm(t, axis=1, keepdims=True) + 1e-12
    n = np.column_stack([t[:, 1], -t[:, 0]])
    a = p + d * n
    b = p - d * n
    grow_a = abs(_area(a)) > abs(_area(b))
    # outer contour: grow; hole: shrink the hole (also = away from ink)
    return a if grow_a != hole else b


# ---------------------------------------------------------------- corners
def turning(p: np.ndarray, k: int) -> np.ndarray:
    v1 = p - np.roll(p, k, 0)
    v2 = np.roll(p, -k, 0) - p
    a1 = np.arctan2(v1[:, 1], v1[:, 0])
    a2 = np.arctan2(v2[:, 1], v2[:, 0])
    d = np.abs((a2 - a1 + np.pi) % (2 * np.pi) - np.pi)
    return np.degrees(d)


def find_corners(p: np.ndarray) -> list[int]:
    k = int(round(WIN / STEP))
    th = turning(p, k)
    n = len(p)
    idx = []
    for i in range(n):
        if th[i] < CORNER_DEG:
            continue
        lo = [(i + j) % n for j in range(-k, k + 1)]
        if th[i] >= th[lo].max() - 1e-9:
            # tie-break: keep first of equal plateau
            if not idx or (i - idx[-1]) % n > k:
                idx.append(i)
    return idx


def pca_line(pts: np.ndarray):
    c = pts.mean(0)
    u, s, vt = np.linalg.svd(pts - c)
    return c, vt[0]


def intersect(c1, d1, c2, d2):
    m = np.array([d1, -d2]).T
    if abs(np.linalg.det(m)) < 1e-6:
        return None
    t = np.linalg.solve(m, c2 - c1)
    return c1 + t[0] * d1


def sharpen(p: np.ndarray, corners: list[int]) -> dict[int, np.ndarray]:
    n = len(p)
    out = {}
    m1 = int(3 / STEP)
    for ci, i in enumerate(corners):
        prev_c = corners[ci - 1]
        next_c = corners[(ci + 1) % len(corners)]
        gap_prev = (i - prev_c) % n or n
        gap_next = (next_c - i) % n or n
        m2p = min(int(20 / STEP), gap_prev // 2)
        m2n = min(int(20 / STEP), gap_next // 2)
        if m2p <= m1 + 3 or m2n <= m1 + 3:
            out[i] = p[i]
            continue
        left = p[[(i - j) % n for j in range(m1, m2p)]]
        right = p[[(i + j) % n for j in range(m1, m2n)]]
        c1, d1 = pca_line(left)
        c2, d2 = pca_line(right)
        x = intersect(c1, d1, c2, d2)
        if x is None or np.linalg.norm(x - p[i]) > 4.0:
            out[i] = p[i]
        else:
            out[i] = x
    return out


# ---------------------------------------------------------------- bezier fitting (Schneider 1990)
def bez(ctrl, t):
    t = np.asarray(t)[:, None]
    mt = 1 - t
    return mt**3 * ctrl[0] + 3 * mt**2 * t * ctrl[1] + 3 * mt * t**2 * ctrl[2] + t**3 * ctrl[3]


def bez_d1(ctrl, t):
    t = np.asarray(t)[:, None]
    mt = 1 - t
    return 3 * mt**2 * (ctrl[1] - ctrl[0]) + 6 * mt * t * (ctrl[2] - ctrl[1]) + 3 * t**2 * (ctrl[3] - ctrl[2])


def bez_d2(ctrl, t):
    t = np.asarray(t)[:, None]
    return 6 * (1 - t) * (ctrl[2] - 2 * ctrl[1] + ctrl[0]) + 6 * t * (ctrl[3] - 2 * ctrl[2] + ctrl[1])


def chord_param(pts):
    d = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))])
    return d / d[-1]


def gen_bezier(pts, u, t1, t2):
    p0, p3 = pts[0], pts[-1]
    a1 = t1[None, :] * (3 * (1 - u) ** 2 * u)[:, None]
    a2 = t2[None, :] * (3 * (1 - u) * u**2)[:, None]
    c00 = np.sum(a1 * a1); c01 = np.sum(a1 * a2); c11 = np.sum(a2 * a2)
    base = bez(np.array([p0, p0, p3, p3]), u)
    tmp = pts - base
    x0 = np.sum(a1 * tmp); x1 = np.sum(a2 * tmp)
    det = c00 * c11 - c01 * c01
    seg = np.linalg.norm(p3 - p0)
    if abs(det) > 1e-12:
        al = (x0 * c11 - x1 * c01) / det
        ar = (c00 * x1 - c01 * x0) / det
    else:
        al = ar = seg / 3
    eps = 1e-6 * seg
    if al < eps or ar < eps:
        al = ar = seg / 3
    return np.array([p0, p0 + t1 * al, p3 + t2 * ar, p3])


def reparam(ctrl, pts, u):
    q = bez(ctrl, u) - pts
    d1 = bez_d1(ctrl, u)
    d2 = bez_d2(ctrl, u)
    num = np.sum(q * d1, axis=1)
    den = np.sum(d1 * d1, axis=1) + np.sum(q * d2, axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        nu = np.where(np.abs(den) > 1e-12, u - num / den, u)
    nu = np.clip(nu, 0, 1)
    nu[0], nu[-1] = 0.0, 1.0
    return np.maximum.accumulate(nu)


def max_err(ctrl, pts, u):
    d = np.linalg.norm(bez(ctrl, u) - pts, axis=1)
    i = int(np.argmax(d))
    return d[i], i


def unit(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-12 else v


def end_tangent(pts, from_start=True, span=6.0):
    """Direction leaving the end of a run, from a PCA line over `span` px."""
    if not from_start:
        pts = pts[::-1]
    d = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))])
    k = max(3, int(np.searchsorted(d, span)))
    sub = pts[: min(k, len(pts))]
    if len(sub) < 3:
        return unit(pts[min(1, len(pts) - 1)] - pts[0])
    _, v = pca_line(sub)
    if np.dot(v, sub[-1] - sub[0]) < 0:
        v = -v
    return v


def fit_cubic(pts, t1, t2, tol, depth=0):
    if len(pts) <= 3:
        seg = np.linalg.norm(pts[-1] - pts[0]) / 3
        return [np.array([pts[0], pts[0] + t1 * seg, pts[-1] + t2 * seg, pts[-1]])]
    u = chord_param(pts)
    ctrl = gen_bezier(pts, u, t1, t2)
    e, split = max_err(ctrl, pts, u)
    if e < tol:
        return [ctrl]
    if e < tol * 6:
        for _ in range(30):
            u = reparam(ctrl, pts, u)
            ctrl = gen_bezier(pts, u, t1, t2)
            e, split = max_err(ctrl, pts, u)
            if e < tol:
                return [ctrl]
    split = min(max(split, 2), len(pts) - 3)
    lo, hi = max(0, split - 8), min(len(pts), split + 9)
    _, tc = pca_line(pts[lo:hi])
    if np.dot(tc, pts[lo] - pts[hi - 1]) < 0:
        tc = -tc
    if depth > 40:
        return [ctrl]
    return fit_cubic(pts[: split + 1], t1, tc, tol, depth + 1) + fit_cubic(pts[split:], -tc, t2, tol, depth + 1)


def is_straight(pts, tol):
    a, b = pts[0], pts[-1]
    d = b - a
    L = np.linalg.norm(d)
    if L < 1e-9:
        return True
    n = np.array([-d[1], d[0]]) / L
    return np.max(np.abs((pts - a) @ n)) <= tol


def bezier_is_line(c, tol=0.25):
    return is_straight(np.array([c[0], c[1], c[2], c[3]]), tol) and \
        0 <= np.dot(c[1] - c[0], c[3] - c[0]) and 0 <= np.dot(c[2] - c[3], c[0] - c[3])



def find_lines(pts, tol=0.35, minlen=120.0):
    """Maximal straight sub-runs (>= minlen px) inside a corner-to-corner run.
    Edges that flow into a fillet without a corner become exact lines."""
    s = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))])
    M = len(pts)
    res = []
    i = 0
    while i < M - 1:
        lo, hi = i + 1, M - 1
        if is_straight(pts[i:hi + 1], tol):
            j = hi
        else:
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if is_straight(pts[i:mid + 1], tol):
                    lo = mid
                else:
                    hi = mid
            j = lo
        if s[j] - s[i] >= minlen:
            res.append((i, j))
            i = j
        else:
            i += 2
    return res


def fit_run(pts):
    """A corner-to-corner run -> list of ("L"|"C", points)."""
    lines = find_lines(pts)
    out = []
    pos = 0
    prev_dir = None
    def curve_piece(a, b, t_in, t_out):
        sub = pts[a:b + 1]
        if len(sub) < 4 or is_straight(sub, TOL):
            return [("L", [pts[b]])]
        t1 = t_in if t_in is not None else end_tangent(sub, True)
        t2 = t_out if t_out is not None else end_tangent(sub, False)
        res = []
        for c in fit_cubic(sub, t1, t2, TOL):
            res.append(("L", [c[3]]) if bezier_is_line(c) else ("C", [c[1], c[2], c[3]]))
        return res
    for (a, b) in lines:
        d = unit(pts[b] - pts[a])
        if a > pos:
            out += curve_piece(pos, a, prev_dir, -d)
        out.append(("L", [pts[b]]))
        prev_dir = d
        pos = b
    if pos < len(pts) - 1:
        out += curve_piece(pos, len(pts) - 1, prev_dir, None)
    return out

# ---------------------------------------------------------------- per contour
def vectorise_contour(raw: np.ndarray, hole: bool):
    p = resample_closed(raw, STEP)
    p = smooth_closed(p, sigma_samples=1.5)            # 0.75 px
    p = outward_offset(p, 0.5 / UP, hole)
    corners = find_corners(p)
    n = len(p)
    if not corners:                                     # smooth closed curve
        corners = [0]
    sharp = sharpen(p, corners)
    skip = int(2.0 / STEP)                              # ignore rounded-off zone next to corners
    segs = []
    for ci, i in enumerate(corners):
        j = corners[(ci + 1) % len(corners)]
        span = (j - i) % n or n
        inner = [(i + s) % n for s in range(skip, span - skip + 1)] if span > 2 * skip + 2 else []
        pts = np.vstack([sharp[i], p[inner] if inner else np.empty((0, 2)), sharp[j]])
        if is_straight(pts, TOL * 1.2):
            segs.append(("L", [sharp[j]]))
            continue
        segs.extend(fit_run(pts))
    start = sharp[corners[0]]
    return start, segs, len(corners)


def merge_lines(start, segs, tol=0.6):
    """Merge consecutive collinear L segments."""
    out = []
    cur = start
    for kind, pts in segs:
        if kind == "L" and out and out[-1][0] == "L":
            prev_start = out[-1][2]
            a, b = prev_start, pts[0]
            mid = out[-1][1][0]
            d = b - a
            L = np.linalg.norm(d)
            if L > 0 and abs((mid - a) @ np.array([-d[1], d[0]]) / L) < tol:
                out[-1] = ("L", [b], prev_start)
                cur = b
                continue
        out.append((kind, pts, cur))
        cur = pts[-1]
    return [(k, p) for k, p, _ in out]


def fmt(v):
    s = f"{v:.1f}"
    s = s.rstrip("0").rstrip(".") if "." in s else s
    return "0" if s in ("-0", "") else s


def path_d(start, segs, off):
    o = np.asarray(off)
    parts = [f"M{fmt(start[0]-o[0])} {fmt(start[1]-o[1])}"]
    for kind, pts in segs:
        coords = " ".join(f"{fmt(q[0]-o[0])} {fmt(q[1]-o[1])}" for q in pts)
        parts.append(f"{kind}{coords}")
    parts.append("Z")
    return "".join(parts)


def bbox_of(start, segs):
    xs, ys = [start[0]], [start[1]]
    cur = start
    for kind, pts in segs:
        if kind == "L":
            xs.append(pts[0][0]); ys.append(pts[0][1])
        else:
            c = np.array([cur, pts[0], pts[1], pts[2]])
            b = bez(c, np.linspace(0, 1, 200))
            xs += list(b[:, 0]); ys += list(b[:, 1])
        cur = pts[-1]
    return min(xs), min(ys), max(xs), max(ys)


def main():
    contours, (w, h) = subpixel_contours()
    shapes = []
    stats = []
    for raw, hole in contours:
        start, segs, nc = vectorise_contour(raw, hole)
        segs = merge_lines(start, segs)
        # The PNG is cropped to the glyph, so the glyph's true box is the canvas.
        # Clamp sub-pixel overshoot of the fit (<1 px) back onto the canvas.
        lim = np.array([w, h], float)
        start = np.clip(start, 0, lim)
        segs = [(k, [np.clip(q, 0, lim) for q in pts]) for k, pts in segs]
        shapes.append((start, segs))
        stats.append({"hole": bool(hole), "corners": nc,
                      "lines": sum(1 for k, _ in segs if k == "L"),
                      "curves": sum(1 for k, _ in segs if k == "C")})
    boxes = [bbox_of(s, g) for s, g in shapes]
    x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes)
    x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)
    off = (x0, y0)
    W = math.ceil((x1 - x0) * 10) / 10
    H = math.ceil((y1 - y0) * 10) / 10
    d = "".join(path_d(s, g, off) for s, g in shapes)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(W)} {fmt(H)}" '
        f'role="img" aria-label="ريال سعودي / Saudi Riyal">'
        f'<title>Saudi Riyal symbol (SAMA)</title>'
        f'<path fill="currentColor" fill-rule="evenodd" d="{d}"/></svg>\n'
    )
    OUT.write_text(svg, encoding="utf-8")
    meta = {"source": str(SRC.name), "source_size": [w, h], "offset_in_source": [round(x0, 3), round(y0, 3)],
            "viewBox": [0, 0, W, H], "aspect_w_over_h": round(W / H, 5), "contours": stats,
            "bytes": len(svg.encode("utf-8")), "tolerance_px": TOL}
    META.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
