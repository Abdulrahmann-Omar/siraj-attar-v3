"""Generate data/SCRAPE_REPORT.md from catalogue.json, categories.json, photo_classes.json and the comparison file."""
import json, os, statistics
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda f: json.load(open(os.path.join(ROOT, 'data', f), encoding='utf-8'))
P = {p['id']: p for p in D('catalogue.json')}
C = D('categories.json')
PC = {o['id']: o for o in D('photo_classes.json')}
CMP = D('compare_2026-09-28_vs_2026-10-04.json')

# ---- curated by eye from the contact sheets (scratch/sheets*, scratch/hero_*.jpg)
HEROES = {
    '1704276239': [('966965063_3.jpg', 'Model, Yaqoot red shemagh, symmetrical front pose, clean white sweep'),
                   ('1983204219_3.jpg', 'Model adjusting the Aqeeq shemagh (gesture shot)'),
                   ('502827333_2.jpg', 'Model in the white Classic ghutra'),
                   ('1983204219_1.jpg', 'Best green-box packshot of the range (2020 px)')],
    '1812386828': [('966965063_2.jpg', 'Model, Yaqoot shemagh, three-quarter'),
                   ('1604079293_3.jpg', 'Model, Audemar 4 shemagh'),
                   ('24078165_3.jpg', 'Model, Khatm 26 red, shemagh thrown back'),
                   ('1988908934_2.jpg', 'High-res weave detail (3803 px)')],
    '23035657': [('502827333_2.jpg', 'Model in the Classic ghutra'),
                 ('1740470085_2.jpg', '"100% COTTON VOILE BY M.SIRAJ ATTAR" selvedge detail, 3859 px'),
                 ('1740470085_1.jpg', 'Green-box packshot, 6000 px'),
                 ('1499162789_3.jpg', 'Fringed edge detail, 6000 px')],
    '1394974218': [('2124457749_7.jpg', 'Model in the laser-patterned white Zumurrud shemagh'),
                   ('2124457749_6.jpg', 'Laser pattern detail, 3456 px'),
                   ('1211546059_1.jpg', 'Green-box packshot, 2020 px')],
    '1785129829': [('99351912_2.jpg', 'Weave close-up (1250 px; best available)'),
                   ('1471159401_1.jpg', 'Green-box packshot (1125 px)')],
    '1145244262': [('1546150268_4.jpg', 'Wisam 26 weave close-up (1500 px)'),
                   ('160018205_1.jpg', 'Green-box packshot (1250 px)')],
    '2129648660': [('892978768_2.jpg', 'Wathir gift packaging in raking light (only lifestyle frame)'),
                   ('931289172_1.jpg', 'Ghost-mannequin undershirt, 2020 px'),
                   ('230109116_1.png', 'Four-colour sock fan, 1080 px')],
    '1954429207': [('512779702_1.jpg', 'Pinked swatch fan, cream to white, 2020 px'),
                   ('1292393513_1.jpg', 'Lilac-white drape with gold "MADE IN JAPAN 909" selvedge print, 2048 px'),
                   ('2029457986_1.jpg', 'Gold-foil "العطار 913" branded fabric, 2020 px'),
                   ('1146743451_1.jpg', 'Soft white drape, 2048 px'),
                   ('795805893_1.jpg', 'Sharpest fabric texture in the store (taupe Swiss cotton, 2048 px), reference only')],
    '587820825': [('821325048_1.jpg', 'Embroidered pashmina flat-lay, 4484 px (retouch gold pins)'),
                  ('663088504_2.jpg', 'Navy-embroidered Al-Baidaa shawl, 5184 px'),
                  ('1449104353_4.jpg', 'Italian striped wool, folded, 4032 px')],
    '1677019232': [('1449104353_4.jpg', 'Italian striped wool, folded, 4032 px'),
                   ('47352825_1.jpg', 'Pashmina embroidery fills frame, 4660 px'),
                   ('1449104353_5.jpg', 'Navy pinstripe wool folds, 3566 px')],
    '1037195105': [('821325048_1.jpg', 'Embroidered pashmina flat-lay, 4484 px (retouch gold pins)'),
                   ('47352825_1.jpg', 'Embroidery detail, 4660 px'),
                   ('681314293_3.jpg', 'Navy paisley close-up, 5184 px')],
    '1501926755': [('1029444903_1.jpg', 'Solid navy wool drape (1500 px; one photo per product)'),
                   ('1419600434_1.jpg', 'Wool bolt with selvedge (1500 px)')],
    '727889004': [('1449104353_4.jpg', 'Striped wool folds, 4032 px'),
                  ('1449104353_1.jpg', 'Main photo, 3670 px')],
    '1180391440': [('265256366_2.jpg', 'Silver cufflinks on white plinths, 2020 px'),
                   ('1610956716_1.jpg', 'Blue cufflinks, 2020 px')],
    '971240205': [('2125369422_4.jpg', 'Close portrait, Bernini red (product OUT OF STOCK)'),
                  ('1842109012_3.jpg', 'Model, Bernini gold (OUT OF STOCK)')],
    '412732516': [('189452492_1.jpg', 'Attar 3 bottle on wood with flowers, 3450 px'),
                  ('14237135_2.jpg', 'Hand holding Attar 1 against thobe and shemagh (1329 px)'),
                  ('672063087_1.jpg', 'Three-bottle set in the green box, 5000 px')],
    '2019914408': [('672063087_1.jpg', 'Perfume trio in the green box, 5000 px'),
                   ('1381142749_3.webp', 'Gift box: shemagh + perfume + cufflinks (900 px only)')],
}
WEAK = [
    ('مجموعة حفاوة', 'No model shot; max 1250 px; 3 near-identical green-box shots; two of three products have no description.'),
    ('مجموعة الأصالة', '6 of 9 main photos under 1200 px; no model shot; all box packshots.'),
    ('الأقمشة الكورية', 'All 5 products: one 1000 px gold-foil text shot + one plain white drape; layouts identical, nothing shows the cloth made up.'),
    ('الاقمشه الاوروبيه / سمير اميس', 'One or four 900 px WebP images per product; soft (lowest sharpness in the store).'),
    ('الأقمشة الإيطالية', 'Main photos 900 to 1400 px; 1 of 2 products out of stock.'),
    ('الأصواف الإنجليزية', 'One photo per product, 999 to 1500 px, plain drapes only.'),
    ('الشالات / المنتجات الشتوية', 'High resolution (up to 5184 px) but every shot is the same white flat-lay; gold push-pins and black hang-tags are visible in many frames; no shawl is shown worn (over a bisht or thobe).'),
    ('اكسسوارات (عقال)', 'Agal: main 1000 px, gallery shots 370 px.'),
    ('هدايا (صندوق الإهداء)', 'Gift box only 900 px WebP.'),
    ('الأقمشة (all)', 'No photograph links a fabric to a finished thobe; 18 of 39 main photos under 1200 px.'),
    ('غير مصنف', '10 of 13 main photos at 900 to 1000 px.'),
]


def fmt(x):
    return '-' if x is None else (f'{x:,.2f}'.rstrip('0').rstrip('.') if isinstance(x, float) else str(x))


def main():
    L = []
    w = L.append
    prods = list(P.values())
    on_sale = [p for p in prods if p['is_on_sale']]
    w('# Siraj Attar store scrape report')
    w('')
    w('Live scrape of https://sirajattarbros.com/ar on **2026-10-04** (Salla store id 946211295). Machine-readable data: '
      '`data/catalogue.json` (137 products), `data/categories.json`, `data/photo_classes.json`, '
      '`data/compare_2026-09-28_vs_2026-10-04.json`; images in `data/images/` (`<productid>_<n>`, n = 1 is the main photo).')
    w('')
    w('## How it was scraped')
    w('')
    w('- The live site did **not** block us. The Salla storefront API (`api.salla.dev/store/v1/products`, header `Store-Identifier: 946211295`) '
      'answered 200 without a session, both for the full product index (`source=product.index`, 10 pages) and for every menu category (`source=categories`).')
    w('- All 137 product pages were fetched (3 workers, 0.8 to 1.4 s pauses). Prices were cross-checked against the schema.org Product JSON-LD on each page: '
      '136 of 137 match exactly. The exception is the gift bundle `1381142749` (type `group_products`), whose JSON-LD price is 0. The page shows 307.25.')
    w('- Gallery images come from the product-page lightbox links. They are already originals: cdn.salla.sa thumbnails (`<uuid>-WxH-name.jpg`) and the Cloudflare '
      '`/cdn-cgi/image/` proxy were stripped. On cdn.files.salla.network the `_600x900`-style suffix is part of the stored original file name. '
      'Removing it returns 404, and the API `original_image` points to the suffixed file, so those files were kept. 348 images, 0 failures, 198 MB.')
    w('- A rendered DOM check of category pages (Edge, Playwright) shows only the first 15 cards before lazy loading, so category membership comes from the API, not the DOM.')
    w('- **Price basis:** the displayed price equals Salla `product:pretax_price`. About half of the regular prices become whole riyals when multiplied by 1.15, so the store likely '
      'shows prices before VAT and adds 15% at checkout. This was not verified, because we did not go through checkout. `price` = displayed price; `price_incl_vat_est` = x1.15.')
    w('')
    w('## Headline numbers')
    w('')
    w(f'- **137 products** in the store index; **124** sit in at least one menu category; **13 are in no menu category** and can be reached only by search or a direct URL.')
    w(f'- 30 menu categories (11 top level + 19 sub-categories). 3 are empty: الشالات الفاخرة, شالات البيداء نص ترمه, أصواف متنوعه. '
      'The home-page banner link `c755154187` ("ويترك أثر مميز") is dead. It redirects home and the API returns 422.')
    w(f'- In stock: {sum(1 for p in prods if p["availability"] == "in_stock")}; out of stock: {sum(1 for p in prods if p["availability"] != "in_stock")}.')
    w(f'- **On sale now: {len(on_sale)}** products. 97 are in the National Day campaign, which runs from 2026-09-01 and **ends 2026-10-06 02:59 (+03), i.e. the night of 5 Oct**. '
      'The product page shows a live countdown, and the site banner still reads "الآن عروض اليوم الوطني تبدأ من 15%". The other 12 are uncategorised items with an open-ended discount.')
    w(f'- Main photographs: {", ".join(f"{k} {v}" for k, v in Counter(o["class"] for o in PC.values()).most_common())}. **No main photograph shows the product worn.** '
      f'{sum(len(o["model_shots"]) for o in PC.values())} model shots exist, all deeper in the galleries of headwear products, and all are on the same white studio sweep.')
    w('')
    w('## Products and prices per category')
    w('')
    w('Prices in SAR as displayed (pre-VAT). "Current" = what the customer pays now; "Regular" = struck price, or the price when the item is not discounted.')
    w('')
    w('| Category | Products | In stock | On sale | Current min-max | Median current | Regular min-max | Discount range |')
    w('|---|---:|---:|---:|---|---:|---|---|')
    for c in C:
        ids = c['product_ids']
        name = c.get('path') or c['name']
        if not ids:
            w(f'| {name} | 0 | - | - | - | - | - | - |')
            continue
        ps = [P[i] for i in ids]
        cur = [p['price'] for p in ps]
        reg = [p['compare_at_price'] or p['price'] for p in ps]
        ds = [p['discount_pct'] for p in ps if p['discount_pct']]
        w(f'| {name} | {len(ps)} | {sum(1 for p in ps if p["availability"] == "in_stock")} | {len(ds)} | '
          f'{fmt(min(cur))} - {fmt(max(cur))} | {fmt(round(statistics.median(cur), 2))} | {fmt(min(reg))} - {fmt(max(reg))} | '
          f'{(fmt(min(ds)) + "% - " + fmt(max(ds)) + "%") if ds else "-"} |')
    w('')
    w('Products sit in several categories (e.g. a red shemagh can be in المجموعة الكلاسيكية, أشمغة حمراء and المنتجات المخفضة), so the rows do not add up to 137.')
    w('')
    w('## Changes since the 2026-09-28 scrape')
    w('')
    s = CMP['summary']
    w(f'- **No products removed** (all 123 still live). **No offer has ended yet**: all 97 discounts seen on 09-28 are still running at the same price, with one exception below. They all end on the night of 5 Oct.')
    w('- **One price change:** شماغ الوسام 26 الأحمر (1546150268) went from 195.50 to **207.00**. The struck price stays 243.48, so the discount is now 15% (was 19.7%).')
    w('- **Two items went out of stock:** شماغ العطار الذهبي (333921099) and شماغ برنيني ذهبي (1842109012).')
    w('- **New in a menu category:** غترة زفير (196810152, الغتر, 152.17; Salla sync 2026-09-30). الغتر grew from 7 to 8 products.')
    w('- **13 products found that the 09-28 run missed.** They are in the store index but in no menu category, and the 09-28 run walked categories only. Salla sync dates '
      'for 8 of them fall between 2026-09-08 and 09-22, and 4 have no sync record, so they are most likely older hidden or uncategorised listings rather than launches. `910` (987219575) synced on 2026-09-30 and may be genuinely new. '
      'They are 10 thobe fabrics (قماش999, 9426, ارزونا, 933, تيستا بوارنو, تيستا بالميرول, رومنسي, قماش العطار 404, 910, 906) and 3 shawls (Q2S55, Q6S55, البيداء m7s60). 12 of the 13 carry a discount with no end date.')
    w('- 8 title edits are whitespace-only clean-ups (double spaces removed). Category membership and gallery images are otherwise unchanged.')
    w('- Discount oddities in the running campaign: شماغ نقش العطار 25 الاحمر (437508308) is "on sale" at 272.00, down from 278.26 (2.2%, and out of stock). '
      'غترة العطار العصرية is 10% off and شماغ العطار كلاسيك عنبر is 13.6% off. Both are below the "from 15%" promise on the banner.')
    w('')
    w('## Products on sale now')
    w('')
    w('Sorted by discount. "Ends" is the scheduled end of the discount; "open" = no end date set.')
    w('')
    w('| ID | Product | Category | Now | Was | Off | Ends | Stock |')
    w('|---|---|---|---:|---:|---:|---|---|')
    for p in sorted(on_sale, key=lambda p: -p['discount_pct']):
        cat = p['categories'][0] if p['categories'] else 'غير مصنف'
        end = p['sale_ends'][:10] if p['sale_ends'] else 'open'
        w(f'| {p["id"]} | {p["title"]} | {cat} | {fmt(p["price"])} | {fmt(p["compare_at_price"])} | {fmt(p["discount_pct"])}% | {end} | '
          f'{"in" if p["availability"] == "in_stock" else "**OUT**"} |')
    w('')
    w('## Photography: main-photo classes per category')
    w('')
    w('Classes: packshot_plain, packshot_in_box, worn_by_model, lifestyle, fabric_closeup. The PIL/OpenCV heuristic agreed with the eye review on '
      f'{sum(1 for o in PC.values() if o["heuristic_agrees"])}/137; the eye review is final (see `data/photo_classes.json`).')
    w('')
    w('| Category | Main-photo classes | Median main long edge (px) | Mains < 1200 px | Model shots in galleries |')
    w('|---|---|---:|---:|---:|')
    for c in C:
        ids = c['product_ids']
        if not ids:
            continue
        cl = Counter(PC[i]['class'] for i in ids)
        le = [PC[i]['main_long_edge'] for i in ids]
        w(f'| {c.get("path") or c["name"]} | {", ".join(f"{k} {v}" for k, v in cl.most_common())} | {int(statistics.median(le))} | '
          f'{sum(1 for x in le if x < 1200)} | {sum(len(PC[i]["model_shots"]) for i in ids)} |')
    w('')
    w('## Best hero candidates per category')
    w('')
    w('Picked by eye from the contact sheets: clean background, sharp, high resolution, product in stock unless marked. Paths are relative to the project root.')
    w('')
    for c in C:
        if c['id'] not in HEROES:
            continue
        w(f'**{c.get("path") or c["name"]}**')
        w('')
        for f, why in HEROES[c['id']]:
            pid = f.split('_')[0]
            p = P[pid]
            g = next(x for x in PC[pid]['gallery'] if x['path'].endswith('/' + f))
            stock = '' if p['availability'] == 'in_stock' else ' **(out of stock)**'
            w(f'- `data/images/{f}` ({g["width"]}x{g["height"]}), {p["title"]}{stock}: {why}')
        w('')
    w('Notes for hero use:')
    w('- The best model shots of the Bernini, Zafeer and Golden shemaghs (2125369422, 1842109012, 2024205944, 333921099) and the Asriya ghutra (1712185778) are **out of stock**. Avoid them for campaigns, or check stock first.')
    w('- In-stock products with model shots: 966965063, 1983204219, 502827333, 2124457749, 1604079293, 24078165.')
    w('- Location and lifestyle imagery with people exists only in the home-page banners (`brand/site_banners/`): a falconer in the dunes, and an elderly man with younger men in front of a lantern-lit mud-brick wall under the "تميّز متوارث" campaign. No product page has it.')
    w('')
    w('## Categories with weak photography')
    w('')
    for n, why in WEAK:
        w(f'- **{n}**: {why}')
    w('')
    w('Store-wide gaps: no main image shows the product worn; no thobe-fabric image shows a finished thobe; shawls are never shown draped; perfume is the only range with styled lifestyle sets. '
      'Fabric main photos are mostly gold-foil branded swatches. They are consistent, but they all look alike across 39 products.')
    w('')
    w('## Out of stock (20)')
    w('')
    for p in prods:
        if p['availability'] != 'in_stock':
            w(f'- {p["id"]} {p["title"]} ({", ".join(p["categories"][:2]) or "غير مصنف"})')
    w('')
    open(os.path.join(ROOT, 'data', 'SCRAPE_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('wrote SCRAPE_REPORT.md', len(L), 'lines')


if __name__ == '__main__':
    main()
