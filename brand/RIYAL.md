# Saudi Riyal symbol: vector and usage

## Files

| File | What it is |
|---|---|
| `brand/riyal.png` | Source: SAMA's official symbol, 3000 x 3353 px. The glyph is stored in the alpha channel (17 anti-aliasing levels, colour #232020). |
| `brand/riyal.svg` | The vector. 1 KB, one `<path>` with `fill="currentColor"`, `viewBox="0 0 3000 3353"`. The viewBox is the glyph's tight bounding box: the PNG is already cropped to the glyph. |
| `brand/riyal_compare.png` | Verification sheet. It overlays the SVG rendered by Edge on the PNG mask and adds 1.6 to 3x crops of the curved terminals and the fillet. |
| `brand/riyal_vector_meta.json` | Fit parameters and verification numbers. |
| `brand/riyal_test.html` / `.png` | Type test. Shows the symbol with Arabic-Indic and Western numerals at 12 to 48 px in Cairo, Noto Naskh Arabic, Manrope and Playfair Display, with alignment proofs, prices in running text, and do/don't examples. |
| `tools/riyal_vectorise.py`, `tools/riyal_verify.py`, `tools/build_riyal_test.py` | Scripts to rebuild all of the above. |

## How it was vectorised

1. The alpha channel was upsampled 4x (bilinear) and thresholded at 50 % coverage, which gives a contour at quarter-pixel precision.
2. `cv2.findContours` ran with `RETR_CCOMP`, so holes would be kept. The glyph has 2 outer contours and no holes.
3. Corners were found from the turning angle over an 8 px window. Each corner was then made sharp again by intersecting lines fitted on both sides of it.
4. Straight runs became `L` segments. This includes edges that flow into a fillet with no corner between them. Curved terminals and fillets were fitted as cubic Béziers (Schneider's method) with a tolerance of 0.5 px at 3000 px.
5. Result: 21 lines and 12 cubic curves. Stem edges land within about 0.05 px of the PNG's 50 % coverage edge (for example x = 1058.5 and 1411.8).

**Verification.** The SVG was rendered by Microsoft Edge through Playwright at 3000 x 3353 and compared with the PNG mask:

| Metric | Value |
|---|---|
| IoU (50 % masks) | **0.9984** (target ≥ 0.985) |
| Soft IoU (coverage-weighted) | 0.9995 |
| Pixels in the PNG only / in the SVG only | 5,491 / 165 out of 3,544,910 |
| Edge deviation | p99 1.0 px, max 3.0 px (at 3000 px; under 0.01 px at text sizes) |

## SAMA rules applied

The rules come from SAMA's usage guidelines, as reported by Wikipedia and the press:

- The symbol goes to the **left of the number in every language**, with a **space** between them.
- The symbol's **height matches the text height**. For prices this means the height of the numerals.
- Keep the proportions and the geometry. Never stretch, slant or outline the symbol.
- Keep **clear space of ⅓ of the symbol's height** around it, and enough contrast with the background.
- Never write `ر.س` or `SAR` (see the client feedback).

Unicode 17.0 (September 2025) encodes the sign as **U+20C1 SAUDI RIYAL SIGN**. Of the fonts we downloaded, only Noto Naskh Arabic and Scheherazade New contain it. Cairo, El Messiri, Manrope, Playfair Display and Inter do not, so we always use the SVG rather than the character.

## Recommended CSS

```html
<!-- once per page -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="riyal" viewBox="0 0 3000 3353"><path fill="currentColor" d="…from brand/riyal.svg…"/></symbol>
</defs></svg>

<!-- Arabic copy (RTL paragraph): the dir="ltr" isolate puts the symbol on the LEFT -->
<span class="sar" dir="ltr" data-d="ar"><svg class="riyal" viewBox="0 0 3000 3353" role="img" aria-label="ريال سعودي"><use href="#riyal"/></svg>١٥٧٫٨٢</span>

<!-- English copy -->
<span class="sar" dir="ltr" data-d="lat"><svg class="riyal" viewBox="0 0 3000 3353" role="img" aria-label="Saudi riyals"><use href="#riyal"/></svg>157.82</span>
```

```css
.sar {
  display: inline-flex;
  align-items: baseline;              /* the svg's bottom edge sits on the text baseline */
  gap: calc(var(--riyal-h) / 3);      /* the space = SAMA's 1/3-height clear space (about one word space) */
  direction: ltr; unicode-bidi: isolate;  /* symbol on the left in Arabic and in English */
  white-space: nowrap;                /* never break between symbol and amount */
}
.sar[data-d="ar"]  { --riyal-h: var(--riyal-ar, 0.68em); }   /* Arabic-Indic digits */
.sar[data-d="lat"] { --riyal-h: var(--riyal-lat, 0.72em); }  /* Western digits */
.riyal {
  height: var(--riyal-h);             /* = digit height of the current font */
  width: calc(var(--riyal-h) * 3000 / 3353);
  flex: none; fill: currentColor; overflow: visible;
}
/* per-font tokens (measured ink height of the digits, in em) */
.f-cairo   { --riyal-ar: 0.677em; --riyal-lat: 0.670em; }
.f-messiri { --riyal-lat: 0.680em; }      /* set El Messiri prices in Western digits or in Cairo */
.f-naskh   { --riyal-ar: 0.640em; --riyal-lat: 0.723em; }
.f-manrope { --riyal-lat: 0.733em; }
.f-playfair{ --riyal-lat: 0.723em; font-variant-numeric: lining-nums; } /* Playfair defaults to old-style figures */
.f-inter   { --riyal-lat: 0.740em; }
```

Summary of the settings:

| Setting | Value | Why |
|---|---|---|
| Height | The font's digit height in em: Cairo 0.677 (Arabic-Indic) / 0.670 (Western), Manrope 0.733, Inter 0.740, Noto Naskh 0.640 (Arabic-Indic). | SAMA says to match the height of the text. Digits are the text next to a price. |
| Generic fallback | `height: 1cap`, or 0.70em where `cap` is unsupported (Edge/Chrome 118+, Safari 17.2+ and Firefox 97+ support it). | Within ±5 % of the Western digit height in every face tested. It can be about 12 % too tall for Arabic-Indic digits (IBM Plex Sans Arabic digits are 0.62em against a 0.70em cap), so prefer the per-font token. |
| `vertical-align` | Baseline: `align-items: baseline` in the flex group, or `vertical-align: baseline` on a plain inline `<svg>`. | The symbol's lowest point (the bottom bar) sits on the baseline and its top lines up with the tops of the digits. The baseline/top proofs in `riyal_test.png` were measured at 0.00 px offset. |
| Gap | `calc(var(--riyal-h) / 3)`, about 0.22 to 0.25em. | It equals SAMA's ⅓-height clear space and is close to a normal word space. |
| Order | The symbol comes first inside an LTR isolate. | It appears on the left of the amount in both RTL and LTR text, and bidi reordering cannot move it. |
| Minimum size | About 8 px symbol height, which is 12 px text. | Below that the three bars merge. |

In posters, set the symbol at the same digit-height ratio as the price and in the same ink: `currentColor` picks up ivory on green, gold on green, or ink on ivory. When the price sits in a pill or badge, the badge's inner padding should be at least ⅓ of the symbol's height. For a struck-through old price, draw the strike through the symbol and the amount together, at a smaller size and a muted colour.

Rebuild everything with:

```
.venv\Scripts\python tools\riyal_vectorise.py
.venv\Scripts\python tools\riyal_verify.py
.venv\Scripts\python tools\build_riyal_test.py   # needs fonts\ and fonts\metrics.json (tools\build_specimen.py)
```
