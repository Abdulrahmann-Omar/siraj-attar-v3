# Fonts for Siraj Attar v3

## Summary

| Use | Pick | Weights |
|---|---|---|
| 1. Poster display | **Cairo** | 800–900 |
| 2. Poster body | **Cairo** | 400–600 |
| 3. Proposal Arabic headings | **El Messiri** | 600–700 |
| 4. Proposal Arabic body | **Cairo** | 400 (600 for subheads) |
| 5. Latin pair | **Playfair Display** 600 + **Manrope** 400/500 | — |

One family carries the posters. The proposal reuses that family for body text and adds a Naskh-flavoured display face by the same designer. The aim is that the deck "matches the quality and character of the visuals" (client feedback, General 4).

Files in this folder:

- `specimen.html` and `specimen.png`: every family with the same four samples, plus three proofs of the recommended system.
- `metrics.json`: measured cap, x-height and digit heights.
- `manifest.json`: files, licences, sha256 hashes and source URLs.

Scripts: `tools/fonts_download.py` and `tools/build_specimen.py`.

## Which face the old posters used (read-only check of the Everyside repo)

- `backend/app/services/images/template_composer.py`. This module was last changed on 2026-09-29, the same day as the old assets. `_run_attrs()` returns `"Cairo"` for any Arabic run and `"Inter"` for Latin. `_FONT_FACES` loads Cairo 400/600/700, plus Cairo-Black 900 for the Arabic display line. The render service bundles these files in `apps/render/assets/fonts/Cairo-*.ttf`.
- The poster images confirm it: their letterforms and digits match Cairo Black/Bold, and the URL is set in Inter caps.
- The other route, `overlay.py` (the Pillow fallback), uses Noto Naskh Arabic plus `Guesswhat-Exceptional.otf`. Everyside's own audit says that font has no licence metadata. Do not use it.
- The old proposal PDF embeds Playfair Display, Manrope ExtraLight, **IBM Plex Sans Arabic** Regular and Bold (body and subheads) and **Amiri Bold** (Arabic slide headings). The client's "reconsider the presentation font" note is aimed at this mix.

**So the face the client liked inside the images is Cairo.** It is downloaded as `fonts/cairo/Cairo[slnt,wght].ttf`. google/fonts now ships Cairo only as a variable font with weights 200–1000; the old static Cairo-Black is the wght 900 instance.

## What was downloaded

Every family comes from `github.com/google/fonts/ofl/<dir>` and is under the **SIL Open Font License 1.1**. The licence allows commercial use, embedding in PNG/JPG and PDF, and self-hosted web use. If the fonts are redistributed, keep `OFL.txt` with them and do not sell the fonts on their own. Each folder has the TTFs, `OFL.txt` (the licence), `METADATA.pb` (designer and licence) and `DESCRIPTION.en_us.html`. The total is 25 MB.

| Family | Folder | TTF files | Licence |
|---|---|---|---|
| **Cairo** (old posters) | `fonts/cairo/` | `Cairo[slnt,wght].ttf` (wght 200–1000) | OFL 1.1 |
| IBM Plex Sans Arabic | `fonts/ibmplexsansarabic/` | Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold | OFL 1.1 |
| Alexandria | `fonts/alexandria/` | `Alexandria[wght].ttf` (100–900) | OFL 1.1 |
| Readex Pro | `fonts/readexpro/` | `ReadexPro[HEXP,wght].ttf` (160–700) | OFL 1.1 |
| Noto Kufi Arabic | `fonts/notokufiarabic/` | `NotoKufiArabic[wght].ttf` (100–900) | OFL 1.1 |
| Noto Naskh Arabic | `fonts/notonaskharabic/` | `NotoNaskhArabic[wght].ttf` (400–700) | OFL 1.1 |
| Noto Sans Arabic (extra) | `fonts/notosansarabic/` | `NotoSansArabic[wdth,wght].ttf` | OFL 1.1 |
| Amiri | `fonts/amiri/` | Regular, Bold, Italic, BoldItalic | OFL 1.1 |
| Aref Ruqaa | `fonts/arefruqaa/` | Regular, Bold | OFL 1.1 |
| Reem Kufi | `fonts/reemkufi/` | `ReemKufi[wght].ttf` (400–700) | OFL 1.1 |
| Tajawal | `fonts/tajawal/` | ExtraLight to Black (7 files) | OFL 1.1 |
| Almarai | `fonts/almarai/` | Light, Regular, Bold, ExtraBold | OFL 1.1 |
| Changa | `fonts/changa/` | `Changa[wght].ttf` (200–800) | OFL 1.1 |
| Rubik | `fonts/rubik/` | `Rubik[wght].ttf`, `Rubik-Italic[wght].ttf` | OFL 1.1 |
| Lalezar | `fonts/lalezar/` | Regular | OFL 1.1 |
| Marhey | `fonts/marhey/` | `Marhey[wght].ttf` (300–700) | OFL 1.1 |
| Baloo Bhaijaan 2 | `fonts/baloobhaijaan2/` | `BalooBhaijaan2[wght].ttf` (400–800) | OFL 1.1 |
| El Messiri | `fonts/elmessiri/` | `ElMessiri[wght].ttf` (400–700) | OFL 1.1 |
| Zain | `fonts/zain/` | ExtraLight to Black, plus 2 italics (8 files) | OFL 1.1 |
| Kufam | `fonts/kufam/` | `Kufam[wght].ttf`, `Kufam-Italic[wght].ttf` | OFL 1.1 |
| Lateef | `fonts/lateef/` | ExtraLight to ExtraBold (7 files) | OFL 1.1 |
| Scheherazade New | `fonts/scheherazadenew/` | Regular, Medium, SemiBold, Bold | OFL 1.1 |
| Harmattan | `fonts/harmattan/` | Regular, Medium, SemiBold, Bold | OFL 1.1 |
| Mada | `fonts/mada/` | `Mada[wght].ttf` (200–900) | OFL 1.1 |
| Vazirmatn | `fonts/vazirmatn/` | `Vazirmatn[wght].ttf` (100–900) | OFL 1.1 |
| Beiruti (extra) | `fonts/beiruti/` | `Beiruti[wght].ttf` (200–900) | OFL 1.1 |
| Manrope | `fonts/manrope/` | `Manrope[wght].ttf` (200–800) | OFL 1.1 |
| Inter | `fonts/inter/` | `Inter[opsz,wght].ttf`, italic | OFL 1.1 |
| Playfair Display | `fonts/playfairdisplay/` | `PlayfairDisplay[wght].ttf`, italic | OFL 1.1 |
| Cormorant | `fonts/cormorant/` | `Cormorant[wght].ttf`, italic | OFL 1.1 |
| Cormorant Garamond | `fonts/cormorantgaramond/` | `CormorantGaramond[wght].ttf`, italic | OFL 1.1 |
| Fraunces | `fonts/fraunces/` | `Fraunces[SOFT,WONK,opsz,wght].ttf`, italic | OFL 1.1 |

**Thmanyah (Sans, Serif Display, Serif Text): not downloaded.** Its licence (font.thmanyah.com/licenses-en) does allow commercial use, including logos, print, PDFs and apps. But it also forbids three things:

- modifying or renaming the fonts;
- redistributing or re-hosting them;
- web embedding except inside compiled products. A self-hosted `@font-face` is therefore not allowed.

The only official download sits behind an e-mail form, and submitting it is the user's call. If you download it yourself, Thmanyah Serif Display is worth a test against El Messiri for the proposal headings, since embedding it in the PDF is allowed. Keep its files out of any shared folder or repo.

## What the specimen showed

| Finding | Consequence |
|---|---|
| **Zain** maps the Arabic-Indic code points (U+0660–0669) to Western digit shapes: `١٥٧٫٨٢` renders as "157,82". | Do not use Zain where Arabic-Indic numerals are needed. |
| **El Messiri** has rounded Arabic-Indic digits (٧ looks like "U", ٨ like "∩"). They are elegant but ambiguous at small sizes. | Set prices and figures in Cairo, or in Western digits, even in El Messiri headings. |
| **Cairo**'s harakat are small: a tanween has about 55 % of the ink of IBM Plex's. | Fine for unvocalised poster copy. Vocalise only where it matters, and only at display sizes. |
| **Lateef, Harmattan and Beiruti** look 15–30 % smaller than the others at the same px size (alef height 0.53–0.63em against 0.72em for Cairo). **Amiri and Scheherazade New** have Naskh proportions with small bowls, so they also read smaller. | They need a size bump to sit beside Cairo. |
| **Alexandria and Kufam** have tall Arabic-Indic digits (0.81 and 0.78em); Tajawal and Amiri have short ones (0.58 and 0.57em). | The riyal height token has to come per font: see `metrics.json` and `brand/RIYAL.md`. |
| **Playfair Display and both Cormorants** default to old-style figures. | Add `font-variant-numeric: lining-nums` for prices. |
| Only **Noto Naskh Arabic and Scheherazade New** contain U+20C1 (the riyal sign). | Use the SVG everywhere. |
| All 26 Arabic families draw the test diacritics (عامًا، الحِرفة، يُلبس، إرثٌ), with no missing marks. | — |

## Ranked recommendations

The brand is an 80-year Saudi house selling shemagh, ghutra and thobe, with a deep green and gold identity and a calligraphic roundel logo. The type should feel crafted, calm and confident. It should not look like a promo, a tech product or a toy. It must never compete with the calligraphic logo. The client also asked for two specific things: keep the face from the images, and lift the proposal's Arabic to the same level.

### 1. Poster display face

1. **Cairo 800–900.** The client named it as "a wise choice", so continuity is the safe and correct move. Its contemporary Kufi structure reads as modern Saudi without looking techy. It has a 200–1000 weight range: 900 for headlines and 800 for prices. Its Latin digits come from the same face, so price lines never switch font. Use leading 1.15–1.25 and no tracking.
2. **Alexandria 700–800.** It is by the same designer, Mohamed Gaber, so the voice is the same, but it is more open and geometric and gives a more editorial "premium" feel. Use it for hero key visuals only if Cairo feels too familiar. Its Arabic-Indic digits are tall (0.81em).
3. **Noto Kufi Arabic 800.** A sturdy, neutral fallback with full Arabic coverage.
4. **El Messiri 700.** Only for heritage or occasion editions (Ramadan, Eid, National Day), and only for short lines, never for prices.

Avoid:

- **Lalezar, Marhey, Baloo Bhaijaan 2, Changa:** playful or sporty, wrong for heritage-premium.
- **Reem Kufi, Kufam:** look like logotypes and compete with the roundel.
- **Aref Ruqaa:** a signature accent at most.
- **Zain:** its digits fail (see the specimen findings).

### 2. Poster body face

1. **Cairo 400–600.** It keeps one voice with the headline. The letters are tall (alef 0.72em) and the counters are open, so text holds up at 22–36 px on a 1080 px canvas over photography. Cairo also has the old posters' look the client approved.
2. **Noto Kufi Arabic 400–500.** Sturdier on busy photos (alef 0.76em, heavier strokes) and neutral.
3. **Readex Pro 400.** Very legible for spec lines such as fabric, sizes and care. It is wide, so budget for width.

### 3. Proposal Arabic headings

1. **El Messiri 600–700.** Mohamed Gaber also drew Cairo, so El Messiri shares its proportions and rhythm, and the deck headings "rhyme" with the poster headlines. That is exactly the match the client asked for. Its Naskh-inspired strokes add calligraphic warmth, so it reads as a heritage house rather than retail promo. That is the gap left by the old mix of Amiri Bold and IBM Plex. Use 40–56 px on slides, line-height 1.35, and set any figures in Cairo.
2. **Cairo 700–800.** Maximum consistency, because it is the poster face itself, but louder and more promotional on a document page.
3. **Alexandria 600–700.** A clean, geometric editorial alternative.
4. **Amiri 700.** Only for a cover epigraph or a pull quote. As the old deck's heading face, its bookish classical Naskh fights the Kufi-sans images.

Optional: Thmanyah Serif Display, but only after a licensed manual download (see above).

### 4. Proposal Arabic body

1. **Cairo 400** (300 for large intros, 600 for subheads and labels). It ties the reading text to the visuals the client praised and replaces IBM Plex Sans Arabic, whose corporate character and proportions were flagged. Set it at 10.5–12 pt, line-height 1.8, on ivory.
2. **Readex Pro 300–400.** The most legible choice for dense pages such as tables, timelines and media plans.
3. **Noto Naskh Arabic 400.** For long-form reading such as terms or an appendix. It has the classic book feel and is the one candidate that includes U+20C1.

Not recommended:

- **IBM Plex Sans Arabic:** flagged by the client.
- **Tajawal:** small digits (0.58em) and a light colour.
- **Almarai:** so common in Saudi apps that it reads as generic.

### 5. Latin pair

1. **Playfair Display 600** for headings (with `lining-nums` for figures) and **Manrope 400/500** for body text, labels and tracked caps. The client accepted the old deck's Latin, so keep the pair. Move Manrope body from ExtraLight to Regular for print legibility. Playfair's high contrast carries the fashion and heritage note; Manrope's geometric grotesque matches Cairo's construction. Manrope's Latin x-height (0.54em) is a little larger than Cairo's own Latin (0.50em), so in mixed lines set Manrope at about 0.93 of the Arabic size. On posters keep **Inter 500**, tracked +0.16em, for the URL and CTA caps, as in the approved images.
2. **Cormorant Garamond 600** (28 px and up only) with **Inter**. A more couture, literary feel, but too delicate for small sizes.
3. **Fraunces** (opsz, 600) with **Inter**. A warmer, softer serif for a less formal variant.

## Drop-in `@font-face` for the recommended set

The paths below are relative to the project root. Adjust them when the page lives in a subfolder.

```css
@font-face { font-family:'Cairo';            src:url('fonts/cairo/Cairo%5Bslnt,wght%5D.ttf') format('truetype'); font-weight:200 1000; }
@font-face { font-family:'El Messiri';       src:url('fonts/elmessiri/ElMessiri%5Bwght%5D.ttf') format('truetype'); font-weight:400 700; }
@font-face { font-family:'Playfair Display'; src:url('fonts/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf') format('truetype'); font-weight:400 900; }
@font-face { font-family:'Manrope';          src:url('fonts/manrope/Manrope%5Bwght%5D.ttf') format('truetype'); font-weight:200 800; }
@font-face { font-family:'Inter';            src:url('fonts/inter/Inter%5Bopsz,wght%5D.ttf') format('truetype'); font-weight:100 900; }
:lang(ar) { font-family:'Cairo', sans-serif; }
.ar-h { font-family:'El Messiri','Cairo',serif; font-weight:700; line-height:1.35; }
.en-h { font-family:'Playfair Display',serif; font-weight:600; font-variant-numeric:lining-nums; }
body  { font-family:'Manrope','Cairo',sans-serif; }
```

Set `font-synthesis: none` so that a missing weight is never faked. For the riyal tokens and component, see `brand/RIYAL.md`.
