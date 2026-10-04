"""Compare the 2026-10-04 live scrape with the 2026-09-28 scrape (everyside-review/siraj_case_v2/catalogue, read-only).

Writes data/compare_2026-09-28_vs_2026-10-04.json. Prices on both sides are the store's displayed (pre-VAT) prices
from the Salla listing API, so they compare like for like.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = r'C:\Users\a0109\OneDrive\Desktop\everyside-review\siraj_case_v2\catalogue'
old = json.load(open(os.path.join(OLD, 'products.json'), encoding='utf-8'))
old_cats = json.load(open(os.path.join(OLD, 'categories.json'), encoding='utf-8'))
new = json.load(open(os.path.join(ROOT, 'data', 'catalogue.json'), encoding='utf-8'))
O = {p['external_id']: p for p in old}
N = {p['id']: p for p in new}


def old_price(p):
    l = p.get('listing') or {}
    return l.get('price', float(p['price']) if p.get('price') else None), l.get('regular_price'), bool(l.get('is_on_sale')), l.get('is_available')


rows = {'new_products': [], 'removed_products': [], 'price_changes': [], 'offers_ended': [], 'offers_started': [],
        'offers_continuing': [], 'availability_changes': [], 'title_changes': [], 'category_changes': [], 'image_changes': []}
for pid, n in N.items():
    if pid not in O:
        rows['new_products'].append({'id': pid, 'title': n['title'], 'price': n['price'], 'categories': n['categories'],
                                     'in_menu_category': n['in_menu_category'], 'availability': n['availability'],
                                     'url': n['url']})
        continue
    o = O[pid]
    op, oreg, osale, oavail = old_price(o)
    if op is not None and abs(op - n['price']) > 0.005:
        rows['price_changes'].append({'id': pid, 'title': n['title'], 'old_price': op, 'new_price': n['price'],
                                      'old_regular': oreg, 'new_regular': n['compare_at_price'] or n['price'],
                                      'change_pct': round(100 * (n['price'] - op) / op, 1)})
    if osale and not n['is_on_sale']:
        rows['offers_ended'].append({'id': pid, 'title': n['title'], 'old_sale_price': op, 'old_regular': oreg,
                                     'price_now': n['price'], 'old_discount_pct': round(100 * (1 - op / oreg), 1) if oreg else None})
    elif not osale and n['is_on_sale']:
        rows['offers_started'].append({'id': pid, 'title': n['title'], 'price': n['price'], 'compare_at': n['compare_at_price']})
    elif osale and n['is_on_sale']:
        rows['offers_continuing'].append({'id': pid, 'title': n['title'], 'price': n['price'], 'compare_at': n['compare_at_price'],
                                          'discount_pct': n['discount_pct'], 'sale_ends': n['sale_ends']})
    navail = n['availability'] == 'in_stock'
    if oavail is not None and bool(oavail) != navail:
        rows['availability_changes'].append({'id': pid, 'title': n['title'], 'was_available': oavail, 'now': n['availability']})
    if o['title'].strip() != n['title'].strip():
        rows['title_changes'].append({'id': pid, 'old': o['title'], 'new': n['title'],
                                      'whitespace_only': ' '.join(o['title'].split()) == ' '.join(n['title'].split())})
    # the 09-28 scrape named sub-categories 'parent | child'; normalise to the child name
    oc = {c.split(' | ')[-1] for c in (o.get('listing_categories') or o.get('categories') or [])}
    nc = set(n['categories'])
    if oc != nc:
        rows['category_changes'].append({'id': pid, 'title': n['title'], 'old': sorted(oc), 'new': sorted(nc)})
    ou = [f['url'] for f in o.get('files', [])] or o.get('images', [])
    if ou != n['images']:
        rows['image_changes'].append({'id': pid, 'title': n['title'], 'old_count': len(ou), 'new_count': len(n['images']),
                                      'added': [u for u in n['images'] if u not in ou], 'removed': [u for u in ou if u not in n['images']]})
for pid, o in O.items():
    if pid not in N:
        rows['removed_products'].append({'id': pid, 'title': o['title']})
oc_counts = {c['id']: len(c['product_ids']) for c in old_cats}
newc = json.load(open(os.path.join(ROOT, 'data', 'categories.json'), encoding='utf-8'))
rows['category_count_changes'] = [{'id': c['id'], 'name': c['name'], 'old': oc_counts.get(c['id']), 'new': c['product_count']}
                                  for c in newc if c['id'] in oc_counts and oc_counts[c['id']] != c['product_count']]
rows['summary'] = {k: len(v) for k, v in rows.items() if isinstance(v, list)}
rows['summary'].update({'old_products': len(O), 'new_products_total': len(N), 'old_scrape': '2026-09-28', 'new_scrape': '2026-10-04',
                        'old_on_sale': sum(1 for p in old if (p.get('listing') or {}).get('is_on_sale')),
                        'new_on_sale': sum(1 for p in new if p['is_on_sale']),
                        'new_on_sale_among_previous_123': sum(1 for p in new if p['is_on_sale'] and p['id'] in O),
                        'sale_end_dates': sorted({str(p['sale_ends']) for p in new if p['is_on_sale']})})
json.dump(rows, open(os.path.join(ROOT, 'data', 'compare_2026-09-28_vs_2026-10-04.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(rows['summary'], ensure_ascii=False, indent=1))
