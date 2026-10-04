"""Build data/catalogue.json and data/categories.json from the live Salla store.

Inputs (written by fetch steps, kept for provenance):
  data/raw/api/api_dump_2026-10-04.json  - Salla storefront API (product.index + every menu category)
  data/raw/pages/p<id>.html               - server-rendered product pages (JSON-LD, gallery, description, options)
Images are downloaded by scripts/download_images.py; this script records their local paths if present.
"""
import json, re, os, html as H, datetime
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
API = json.load(open(os.path.join(RAW, 'api', 'api_dump_2026-10-04.json'), encoding='utf-8'))
KSA = datetime.timezone(datetime.timedelta(hours=3))
VAT = 0.15

# ---------------------------------------------------------------- menu (from the live header, 2026-10-04)
MENU = [
    ('1704276239', 'المجموعة الكلاسيكية', None), ('1812386828', 'أشمغة حمراء', None),
    ('23035657', 'الغتر', None), ('1394974218', 'أشمغة بيضاء', None),
    ('1785129829', 'مجموعة حفاوة', None), ('1145244262', 'مجموعة الأصالة', None),
    ('2129648660', 'وثير للملابس الداخلية', None),
    ('1954429207', 'الأقمشة', None),
    ('190964591', 'سمير اميس', '1954429207'), ('2122362229', 'الاقمشه الاوروبيه', '1954429207'),
    ('270558993', 'تترونات', '1954429207'), ('1645118994', 'الأقمشة اليابانية', '1954429207'),
    ('162579484', 'أقطان طبيعية', '1954429207'), ('1537073949', 'الأقمشة السويسرية', '1954429207'),
    ('897188382', 'الأقمشة الإيطالية', '1954429207'), ('1361854488', 'مخلوط', '1954429207'),
    ('552669551', 'الأقمشة الكورية', '1954429207'),
    ('587820825', 'المنتجات الشتوية', None),
    ('2094501402', 'الشالات الفاخرة', '587820825'), ('371730791', 'شالات البيداء نص ترمه', '587820825'),
    ('1677019232', 'الأصواف', None),
    ('1037195105', 'الشالات', '1677019232'), ('1501926755', 'الأصواف الإنجليزية', '1677019232'),
    ('727889004', 'الأصواف الإيطالية', '1677019232'), ('978041972', 'أصواف متنوعه', '1677019232'),
    ('1337375602', 'اخرى', None),
    ('1180391440', 'اكسسوارات', '1337375602'), ('971240205', 'المنتجات المخفضة', '1337375602'),
    ('412732516', 'العطور', '1337375602'), ('2019914408', 'هدايا', '1337375602'),
]
NAME = {c: n for c, n, _ in MENU}
PARENT = {c: p for c, _, p in MENU}
SLUG_URL = {}
home = open(os.path.join(ROOT, 'data', 'raw', 'site', 'home.html'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'data', 'raw', 'site', 'home.html')) else ''
for href, cid in re.findall(r'href="(https://sirajattarbros\.com/ar/[^"]+?/c(\d+))"', home):
    if '/-/' not in href:
        SLUG_URL.setdefault(cid, href)


def path_of(cid):
    p = PARENT.get(cid)
    return (NAME[p] + ' › ' + NAME[cid]) if p else NAME[cid]


# ---------------------------------------------------------------- image URL -> original resolution
UUID = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'


def original_url(u):
    u = H.unescape(u.strip())
    u = re.sub(r'/cdn-cgi/image/[^/]+/', '/', u)                     # Cloudflare resize proxy
    u = re.sub(r'/' + UUID + r'-[\d.]+x[\d.]+-([A-Za-z0-9]+\.\w+)$', r'/\1', u)   # cdn.salla.sa thumbnails
    return u


# ---------------------------------------------------------------- description text
BLOCKS = {'p', 'li', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tr', 'ul', 'ol', 'table', 'article'}


def block_text(el):
    out = []

    def walk(n):
        for c in n.children:
            if isinstance(c, NavigableString):
                out.append(str(c))
            elif isinstance(c, Tag):
                if c.name == 'br':
                    out.append('\n'); continue
                if c.name in ('script', 'style'):
                    continue
                if c.name in BLOCKS:
                    out.append('\n')
                walk(c)
                if c.name in BLOCKS:
                    out.append('\n')
                elif c.name in ('td', 'th'):
                    out.append(' | ')
    walk(el)
    lines = [re.sub(r'[ \t\u00a0]+', ' ', l).strip() for l in ''.join(out).split('\n')]
    return '\n'.join(l for l in lines if l)


# ---------------------------------------------------------------- spec parsing
ORIGINS = [  # (regex, Arabic, English)
    (r'يابان', 'اليابان', 'Japan'), (r'سويسر', 'سويسرا', 'Switzerland'),
    (r'[إا]نجل[يت]ز|[إا]نجلتر|بريطان', 'إنجلترا', 'England'), (r'[إا]يطال', 'إيطاليا', 'Italy'),
    (r'كوري', 'كوريا', 'South Korea'), (r'تايوان', 'تايوان', 'Taiwan'), (r'[إاأ]سبان', 'إسبانيا', 'Spain'),
    (r'تشيك', 'التشيك', 'Czech Republic'), (r'مصري|مصر\b', 'مصر', 'Egypt'),
    (r'وطني|سعودي', 'السعودية (صناعة وطنية)', 'Saudi Arabia'), (r'ترك[يي]', 'تركيا', 'Turkey'),
    (r'ألمان|الماني', 'ألمانيا', 'Germany'), (r'فرنس', 'فرنسا', 'France'), (r'أورو|اورو|أوربي|الأوروبي', 'أوروبا (غير محدد)', 'Europe (unspecified)'),
    (r'يدوي', 'صناعة يدوية', 'Handmade'),
]
CAT_ORIGIN = {'1645118994': 'يابان', '1537073949': 'سويسر', '897188382': 'إيطال', '552669551': 'كوري',
              '1501926755': 'إنجليز', '727889004': 'إيطال'}
KEYS = {
    'color': r'(?:اللون|الالوان|الألوان|الوان|ألوان|الون)',
    'material': r'(?:الخامة|الخامه|خامة|الخامات|المادة|التركيب|مصنوعة|مصنوع|نسبة القطن|قطن)',
    'origin': r'(?:الصناعة|الصناعه|صناعة|صناعه|بلد الصنع|بلد المنشأ|المنشأ)',
    'size': r'(?:المقاسات|المقاس|مقاس|الحجم|عدد الأمتار)',
    'weight': r'(?:الوزن)',
    'category_note': r'(?:الفئة)',
}
KEY_LINE = {k: re.compile(r'^[\s\-_•*·o]*' + v + r'\s*(?:[:：]\s*-?|-\s*:)\s*(.*)$') for k, v in KEYS.items()}
KEY_NOCOLON = {k: re.compile(r'^[\s\-_•*·]*' + v + r'\s+(\S.{0,50})$') for k, v in KEYS.items() if k in ('material', 'size', 'origin')}
ANY_KEY = re.compile(r'^[\s\-_•*·]*(?:' + '|'.join(KEYS.values()) + r')\s*[:：]')
MATERIALS = [  # keyword -> label (Arabic)
    (r'نص ت[وو]?رم', 'صوف نص ترمة'), (r'زبدة الرخال', 'زبدة الرخال (باشمينا)'), (r'كشمير', 'خيوط كشميرية'),
    (r'صوف', 'صوف'), (r'قطن', 'قطن'), (r'بوليستر|البوليستر', 'بوليستر'), (r'تترون|الترون', 'تترون'),
    (r'توفسيل|تنسل', 'تنسل/توفسيل'), (r'سبان', 'سبان'), (r'ايلاست|إيلاست|نايلون', 'إيلاستين/نايلون'),
    (r'مرعز', 'صوف مرعز'), (r'فضة|فضي|ستانلس|معدن', 'معدن'),
]


def clean_val(v):
    v = re.sub(r'^[\s:\-_]+|[\s.،,]+$', '', v)
    if len(v) > 40:  # prose: keep the first clause only
        v = re.split(r'\s(?:مما|يضيف|ليعطيك|ويتميز|يتميز)\s|[،,]', v)[0]
    return v.strip()


def parse_specs(title, desc, options, cat_ids):
    lines = desc.split('\n') if desc else []
    found = {}
    for i, line in enumerate(lines):
        if len(line) > 160:
            continue
        for k, rx in KEY_LINE.items():
            m = rx.match(line)
            if not m:
                continue
            val = clean_val(m.group(1))
            if not val and i + 1 < len(lines) and not ANY_KEY.match(lines[i + 1]) and len(lines[i + 1]) < 60:
                val = clean_val(lines[i + 1])
            if k == 'material' and re.match(r'^(قطن|نسبة القطن)', line.strip(' -_')) and val and 'قطن' not in val:
                val = 'قطن ' + val
            if val and k not in found:
                found[k] = val
            break
        else:
            for k, rx in KEY_NOCOLON.items():
                m = rx.match(line)
                if m and k not in found and len(line) < 70:
                    found[k] = clean_val(m.group(1))
                    break
    text = (title + '\n' + (desc or ''))
    # ----- origin
    origin_src, origin_ar, origin_en = None, None, None

    def match_origin(probe):
        for rx, ar, en in ORIGINS:
            if re.search(rx, probe or ''):
                return ar, en
        return None, None

    candidates = []
    if found.get('origin'):
        candidates.append((found['origin'], 'description'))
    for m in re.finditer(r'(?:صناعة|صناعه|صنع في|صنعت في|صنع ب|مصنوعة في|مصنوع في)\s*[:\-]?\s*(?:ال)?(\S+(?:\s\S+)?)', text):
        candidates.append((m.group(1), 'description (inferred)'))
    for m in re.finditer(r'(?:قماش|شماغ|غترة|صوف|قطعة قماش|شال|قطن)\s+(?:\S+\s+)?(\S*(?:يابان|سويسر|إنجليز|انجليز|إيطال|ايطال|كوري|تايوان|إسبان|اسبان|أسبان|تشيك|أورو|اورو|أوربي)\S*)', text):
        candidates.append((m.group(1), 'description (inferred)'))
    for c in cat_ids:
        if c in CAT_ORIGIN:
            candidates.append((CAT_ORIGIN[c], 'category'))
    for probe, src in candidates:
        ar, en = match_origin(probe)
        if ar and en not in ('Handmade', 'Europe (unspecified)'):
            origin_ar, origin_en, origin_src = ar, en, src
            break
    if not origin_ar:
        m = re.search(r'التشيكي|تشيكي', text)
        if m:
            origin_ar, origin_en, origin_src = 'التشيك', 'Czech Republic', 'description (inferred)'
    if not origin_ar:
        for probe, src in candidates:
            ar, en = match_origin(probe)
            if ar:
                origin_ar, origin_en, origin_src = (ar + ' (البلد غير مذكور)', 'Handmade (country not stated)', src) if en == 'Handmade' else (ar, en, src)
                break
    # ----- material
    mat_kw = []
    for rx, lab in MATERIALS:
        if re.search(rx, text) and lab not in mat_kw:
            mat_kw.append(lab)
    if 'صوف نص ترمة' in mat_kw and 'صوف' in mat_kw:
        mat_kw.remove('صوف')
    MAT = r'(قطن|صوف|بوليستر|البوليستر|تترون|التترون|توفسيل|مودال|المودال|ايلاستتين|إيلاستين|نايلون|حرير)'
    comp = []
    for num, mat in re.findall(r'(\d{2,3})\s*[%٪]\s*(?:من\s*)?' + MAT, text):
        sx = mat.replace('ال', '', 1) if mat.startswith('ال') else mat
        if f'{sx} {num}%' not in comp: comp.append(f'{sx} {num}%')
    for mat, num in re.findall(MAT + r'\s*(?:(?:نقي|طبيعي|الطبيعي|المصري|مصري|بنسبة|:-|:)\s*){0,3}(\d{2,3})\s*[%٪]', text):
        sx = mat.replace('ال', '', 1) if mat.startswith('ال') else mat
        if f'{sx} {num}%' not in comp: comp.append(f'{sx} {num}%')
    material = found.get('material')
    if material and re.fullmatch(r'[:\-\s]*', material):
        material = None
    # ----- size
    size_opts = []
    for o in options:
        if re.search(r'مقاس|المقاس|size|الحجم', o.get('name', ''), re.I):
            size_opts = [d['name'] for d in o.get('details', [])]
    size = found.get('size')
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:متر|م\b|امتار|أمتار)', text)
    fabric_m = float(m.group(1).replace(',', '.')) if m else None
    sm = re.search(r'S\s?(5[0-9]|6[0-9])\b', title, re.I)
    if not size and sm:
        size = sm.group(1)
    INT2 = r'(?<![\d.,])(\d{2})(?![\d.,])'
    def nums(xs):
        n = []
        for x in xs:
            n += [int(v) for v in re.findall(INT2, x)]
        return n
    is_fabric = 'قماش' in title or any(c == '1954429207' or PARENT.get(c) == '1954429207' for c in cat_ids) \
        or (any(c in ('1677019232',) or PARENT.get(c) == '1677019232' for c in cat_ids) and 'شال' not in title)
    size_range = None
    if size_opts and any('متر' in x for x in size_opts):
        size_range = ' / '.join(size_opts)
    elif size_opts:
        nn = nums(size_opts)
        if nn and len(nn) == len([x for x in size_opts if x != 'قيمة']):
            size_range = f'{min(nn)}-{max(nn)}'
        else:
            size_range = ' / '.join(x for x in size_opts if x != 'قيمة')
    elif is_fabric and fabric_m:
        size_range = f'{fabric_m:g} متر'
    elif size:
        nn = [int(v) for v in re.findall(INT2, size)]
        if len(nn) >= 2:
            size_range = f'{min(nn)}-{max(nn)}'
        else:
            size_range = size
    color_opts = [d['name'] for o in options if o.get('type') == 'color' or re.search(r'لون|الوان|ألوان', o.get('name', ''))
                  for d in o.get('details', [])]
    return {
        'color_options': color_opts,
        'color': found.get('color'),
        'material': material,
        'material_keywords': mat_kw,
        'composition': comp,
        'origin': origin_ar, 'origin_en': origin_en, 'origin_source': origin_src,
        'size': size, 'size_options': size_opts, 'size_range': size_range,
        'fabric_length_m': fabric_m if any(c in ('1954429207',) or PARENT.get(c) == '1954429207' for c in cat_ids) or 'قماش' in title else None,
        'weight_note': found.get('weight'),
    }


# ---------------------------------------------------------------- product page parsing
def parse_page(pid):
    fn = os.path.join(RAW, 'pages', f'p{pid}.html')
    h = open(fn, encoding='utf-8').read()
    s = BeautifulSoup(h, 'html.parser')
    out = {'page_bytes': len(h)}
    for sc in s.find_all('script', type='application/ld+json'):
        try:
            j = json.loads(sc.string)
        except Exception:
            continue
        for g in j.get('@graph', [j]):
            if g.get('@type') == 'Product':
                out['ld'] = g
    meta = {m.get('property'): m.get('content') for m in s.find_all('meta') if m.get('property')}
    out['meta'] = {k: v for k, v in meta.items() if k.startswith(('product:', 'og:'))}
    out['gallery_raw'] = [a['href'] for a in s.find_all('a', attrs={'data-fslightbox': True})]
    if not out['gallery_raw']:
        out['gallery_raw'] = [i.get('data-src') or i.get('src') for i in s.select('.product-single__slider img')
                              if 's-empty' not in (i.get('data-src') or i.get('src') or '')]
    h1 = s.select_one('h1')
    out['h1'] = h1.get_text(' ', strip=True) if h1 else None
    d = s.select_one('.product-single-top-description article') or s.select_one('.product-single-top-description')
    out['description'] = block_text(d) if d else ''
    out['description'] = re.sub(r'\n?اقرأ المزيد$', '', out['description']).strip()
    opts = []
    for po in s.find_all('salla-product-options'):
        try:
            opts += json.loads(H.unescape(po.get('options') or '[]'))
        except Exception:
            pass
    out['options'] = [{'name': o.get('name'), 'type': o.get('type'),
                       'details': [{'name': d.get('name'), 'is_out': d.get('is_out'), 'additional_price': d.get('additional_price')}
                                   for d in o.get('details') or []]} for o in opts]
    return out


def ts(t):
    return datetime.datetime.fromtimestamp(t, KSA).isoformat() if t else None


def main():
    allp = {p['id']: p for p in API['_all']['products']}
    memb = {}
    for cid, _, _ in MENU:
        for p in API[cid]['products']:
            memb.setdefault(p['id'], []).append(cid)
    img_index = {}
    idx_path = os.path.join(ROOT, 'data', 'images', '_index.json')
    if os.path.exists(idx_path):
        img_index = json.load(open(idx_path, encoding='utf-8'))
    products = []
    order = list(allp.keys())
    for pid in order:
        a = allp[pid]
        pg = parse_page(pid)
        cats = memb.get(pid, [])
        # order categories as in the menu
        cats = [c for c, _, _ in MENU if c in cats]
        ld = pg.get('ld') or {}
        offer = ld.get('offers') or {}
        price = a['price']
        regular = a['regular_price']
        on_sale = bool(a['is_on_sale'] and a['sale_price'] and regular and a['sale_price'] < regular)
        compare = regular if on_sale else None
        ld_price = offer.get('price')
        gallery = []
        for g in pg['gallery_raw']:
            o = original_url(g)
            if o not in gallery:
                gallery.append(o)
        if not gallery and a.get('image', {}).get('url'):
            gallery = [original_url(a['image']['url'])]
        specs = parse_specs(a['name'], pg['description'] or (a.get('description') or ''), pg['options'], cats)
        files = img_index.get(pid, [])
        rec = {
            'id': pid,
            'title': a['name'],
            'url': a['url'],
            'sku': a.get('sku'),
            'type': a.get('type'),
            'categories': [NAME[c] for c in cats],
            'category_ids': cats,
            'category_paths': [path_of(c) for c in cats],
            'top_level_categories': sorted({NAME[PARENT[c] or c] for c in cats}, key=lambda n: [m[1] for m in MENU].index(n)),
            'primary_category': (a.get('category') or {}).get('name'),
            'in_menu_category': bool(cats),
            'price': price,
            'compare_at_price': compare,
            'currency': a.get('currency') or offer.get('priceCurrency'),
            'discount_pct': round(100 * (1 - price / compare), 1) if compare else None,
            'price_incl_vat_est': round(price * (1 + VAT), 2),
            'compare_at_incl_vat_est': round(compare * (1 + VAT), 2) if compare else None,
            'price_note': 'Displayed store price (pre-VAT; product:pretax_price == displayed price). *_incl_vat_est = x1.15.',
            'is_on_sale': on_sale,
            'sale_starts': ts(a.get('discount_starts')) if on_sale else None,
            'sale_ends': ts(a.get('discount_ends')) if on_sale else None,
            'promotion_title': a.get('promotion_title') or None,
            'subtitle': a.get('subtitle') or None,
            'availability': 'in_stock' if a.get('is_available') and not a.get('is_out_of_stock') else 'out_of_stock',
            'status': a.get('status'),
            'schema_availability': (offer.get('availability') or '').rsplit('/', 1)[-1] or None,
            'jsonld_price': ld_price,
            'price_verified_on_page': (ld_price is not None and abs(float(ld_price) - float(price)) < 0.011),
            'images': gallery,
            'image_count': len(gallery),
            'image_files': files,
            'description': pg['description'] or (a.get('description') or ''),
            'specs': specs,
            'options': pg['options'],
            'has_options': a.get('has_options'),
            'scraped_at': '2026-10-04',
            'source': 'Salla storefront API (api.salla.dev/store/v1, Store-Identifier 946211295) + server-rendered product page',
        }
        products.append(rec)
    # sort: menu order of first category, then API position
    menu_idx = {c: i for i, (c, _, _) in enumerate(MENU)}
    products.sort(key=lambda r: (menu_idx.get(r['category_ids'][0], 999) if r['category_ids'] else 999))
    json.dump(products, open(os.path.join(ROOT, 'data', 'catalogue.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cats_out = []
    for cid, name, parent in MENU:
        ids = [p['id'] for p in API[cid]['products']]
        cats_out.append({'id': cid, 'name': name, 'path': path_of(cid),
                         'url': SLUG_URL.get(cid, f'https://sirajattarbros.com/ar/-/c{cid}'),
                         'parent_id': parent, 'parent_name': NAME.get(parent) if parent else None,
                         'level': 2 if parent else 1, 'product_count': len(ids), 'product_ids': ids,
                         'api_pages': API[cid]['pages']})
    cats_out.append({'id': 'uncategorised', 'name': 'غير مصنف (خارج القائمة)', 'path': None, 'url': None,
                     'parent_id': None, 'parent_name': None, 'level': None,
                     'note': 'Listed by the store product index (source=product.index) but not in any menu category; reachable only via search/direct URL.',
                     'product_ids': [p['id'] for p in products if not p['in_menu_category']],
                     'product_count': sum(1 for p in products if not p['in_menu_category'])})
    cats_out.append({'id': '755154187', 'name': 'ويترك أثر مميز (رابط بانر)', 'url': 'https://sirajattarbros.com/ar/-/c755154187',
                     'note': 'Home-page banner link; category id no longer exists (redirects home, API 422). Not a category.',
                     'product_ids': [], 'product_count': 0})
    json.dump(cats_out, open(os.path.join(ROOT, 'data', 'categories.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('products', len(products), 'categories', len(MENU))


if __name__ == '__main__':
    main()
