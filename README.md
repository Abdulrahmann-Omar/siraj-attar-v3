# Siraj Attar v3: 40 marketing assets + business proposal

Creative and media-buying work for **محمد سراج عطار وأخويه (M. Siraj Attar & Bros)**, sirajattarbros.com, a Saudi men's
traditional-wear house (80+ years). Prepared by Everyside, produced only with **Claude Code + the Higgsfield CLI**.

## Start here

| What | Where |
|---|---|
| Proposal (Arabic / English, 17 slides) | `deliverables/Siraj-Attar-Proposal-AR.pdf`, `deliverables/Siraj-Attar-Proposal-EN.pdf` |
| The 40 assets | `deliverables/` (index in `deliverables/README.md`) |
| Contact sheets | `deliverables/00_overview/` |
| Brief and client feedback | `ref/BRIEF.md`, `ref/FEEDBACK.md` |
| Research | `research/MARKET.md` (KSA market, calendar, media buying, riyal rules), `research/OLD_REVIEW.md` (critique of the previous pitch) |
| Store data | `data/catalogue.json` (137 products), `data/images/`, `data/SCRAPE_REPORT.md`, `data/campaign_prices.json` (VAT-inclusive) |

## The 40 assets

- **16 product shots** (`01_product_shots/`): one perspective each, realistic, product only, minimal sets.
- **9 catalogue posters** (`02_catalogue_posters/`) and **15 campaign pieces** «موسم الوسم» (`03_campaign_mawsim_al_wasm/`):
  every poster ships twice with the identical design, `fusha/` (فصحى) and `saudi/` (سعودي), never mixed.
- Prices are VAT-inclusive (store price x 1.15) and use the official Saudi Riyal symbol (`brand/riyal.svg`).

## Creative constraints (client hard rules)

Realistic photography that shows the real product; minimal environment and few poster components; no people or hands;
no reels or video; the whole product always visible in frame; campaign launches 15 November 2026.

## How it was made

1. `data/`: live scrape of the Salla store (all categories, prices, 348 original photos).
2. `research/`: market, calendar, platform, cultural and copy-register research.
3. `plan/`: asset list (`assets.json`), copy in both registers (`copy.json`), Higgsfield manifests (`gen_manifest*.json`).
4. `gen/run.py`: budget-guarded Higgsfield runner; every credit is a line in `gen/ledger.jsonl`. Final engine:
   Seedream 5.0 Flash image-to-image from the store's own photos (Nano Banana Pro for a few fixes). Outputs in `gen/out/`;
   rejected/earlier rounds in `gen/unused/` and earlier `gen/out` ids (v1 GPT Image 2.5 round kept for reference).
5. `tools/posters.py`: composes every poster in HTML/CSS (Cairo, riyal SVG, client logo) and renders PNGs with Edge.
6. `proposal/build.py`: builds both PDF editions from `proposal/content.json`.
7. `tools/package.py`: assembles `deliverables/`.

Rebuild (Windows, Python 3.13 venv with pillow, pymupdf, playwright, opencv): `python tools/posters.py`,
`python proposal/build.py`, `python tools/package.py`.

## Rights

Product photos, logo and product names belong to M. Siraj Attar & Bros. Fonts in `fonts/` are SIL OFL 1.1 (licence files
included). The riyal symbol is SAMA's official mark. Generated imagery was made from the client's own product photos.
