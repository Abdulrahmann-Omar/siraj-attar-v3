"""Classify every product's MAIN photograph (image n=1) and tag notable gallery shots.

Method: PIL/OpenCV heuristics (scratch/photo_features.json from scripts/photo_features.py) give a first guess;
every main photo was then reviewed by eye on labelled contact sheets (scratch/sheets/*.jpg, scratch/sheets2/*.jpg)
and the reviewed label is final. Writes data/photo_classes.json.

Classes: packshot_plain (product alone on plain white/grey), packshot_in_box (product presented in/with its box or
packaging), worn_by_model, lifestyle (styled set / props / hands / location), fabric_closeup (cloth or embroidery
fills the frame).
"""
import json, os
import numpy as np, cv2
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cat = json.load(open(os.path.join(ROOT, 'data', 'catalogue.json'), encoding='utf-8'))
F = json.load(open(os.path.join(ROOT, 'scratch', 'photo_features.json'), encoding='utf-8'))


FABRIC_CATS = {'1954429207', '190964591', '2122362229', '270558993', '1645118994', '162579484', '1537073949',
               '897188382', '1361854488', '552669551', '1501926755', '727889004', '978041972'}
SHAWL_CATS = {'1037195105', '587820825', '2094501402', '371730791'}


def heuristic_v2(pid, f, title, cats):
    """Category prior + pixel statistics. Pure white cloth reads as 'plain background' to pixel stats,
    so product type is used as a prior; pixel stats then separate the sub-cases."""
    cats = set(cats)
    if f.get('dark_green_frac', 0) > 0.03:
        return 'packshot_in_box'          # the house box is a deep green and takes >3% of the frame
    fabricish = (('قماش' in title or 'صوف' in title or (cats & FABRIC_CATS) or not cats) and 'شال' not in title
                 and not (cats & SHAWL_CATS))
    if fabricish:
        return 'fabric_closeup'
    if 'شال' in title or (cats & SHAWL_CATS):
        # folded/flat shawl with the white sweep showing vs embroidery filling the frame
        return 'packshot_plain' if f['border_plain_frac'] > 0.7 else 'fabric_closeup'
    if f['skin_frac'] > 0.08 and f['skin_frac_upper_half'] > 0.06 and f['mean_sat'] < 50:
        return 'worn_by_model'
    if f['border_plain_frac'] > 0.6 and f['border_std'] < 30:
        return 'packshot_plain'
    if f['edge_border'] > 0.05 and f['border_plain_frac'] < 0.3:
        return 'fabric_closeup'
    return 'lifestyle'


IN_BOX = '''337691313 1740470085 1357196057 2124457749 1211546059 2120850122 1499162789 193975872 966965063 502827333
1983204219 333921099 1604079293 24078165 160018205 1949762576 470478398 1664674203 1546150268 1471159401 99351912
1988908934 437508308 2024205944 196810152 1782560358 1316325476 1176249105 1712185778 290704026 1721304177
1381142749 672063087 1113769137'''.split()
LIFESTYLE = '1842109012 2125369422 14237135 1696071629 189452492'.split()
PLAIN = '''230109116 931289172 1705326923 2012800981 117892433 892978768 870973619 1744147328 916844931 1691931266
493049478 668731835 285519455 1053178443 320666697 630038350 4977729 663088504 1438174847 144922964 2085637336
821325048 1629527017 1239830174 579546591 1353584350 113373149 1062495185 1838105808 329393623 265256366 1610956716
183743361 2049055147 1129261946'''.split()
CLOSE_SHAWL = '957781120 1870697154 47352825 531874291 681314293 1341059308'.split()   # embroidery fills the frame
NOTES = {
    '1842109012': 'Shemagh draped over a white marble plinth (styled studio set).',
    '2125369422': 'Shemagh draped over marble blocks (styled studio set).',
    '14237135': 'Perfume bottle on a wood slice with pine cone and dried citrus (props).',
    '1696071629': 'Perfume bottle on driftwood with lavender (props).',
    '189452492': 'Perfume bottle on wood slice with flowers (props).',
    '2012800981': 'Trousers laid flat with the green Wathir pouch on a lavender-grey sweep.',
    '1744147328': 'Plain shawl hung on a black display rack, light grey sweep.',
    '1499162789': 'Ghutra with the white/silver Swiss-made box (not the green box).',
    '1604079293': 'Shemagh with a light grey box (not the green box).',
    '1381142749': 'Open black/green presentation box with shemagh, perfume and cufflinks.',
    '672063087': 'Three perfume bottles in an open green box.',
    '1113769137': 'Black agal lying on the green box lid.',
    '265256366': 'Cufflinks on white stepped plinths.', '1610956716': 'Cufflinks on white stepped plinths.',
    '931289172': 'Ghost-mannequin undershirt on near-white.', '892978768': 'Ghost-mannequin undershirt on near-white.',
}
# Model / lifestyle shots found in the galleries (reviewed by eye): product_id -> [(n, kind)]
GALLERY_TAGS = {
    '2124457749': [(7, 'worn_by_model')], '966965063': [(2, 'worn_by_model'), (3, 'worn_by_model')],
    '502827333': [(2, 'worn_by_model')], '1983204219': [(3, 'worn_by_model'), (4, 'worn_by_model')],
    '333921099': [(3, 'worn_by_model'), (4, 'worn_by_model')], '1604079293': [(3, 'worn_by_model')],
    '24078165': [(3, 'worn_by_model')], '1842109012': [(2, 'lifestyle'), (3, 'worn_by_model'), (5, 'worn_by_model'), (6, 'packshot_in_box')],
    '2125369422': [(3, 'worn_by_model'), (4, 'worn_by_model'), (5, 'packshot_in_box')],
    '2024205944': [(3, 'worn_by_model')], '1712185778': [(3, 'worn_by_model')],
    '14237135': [(2, 'lifestyle'), (3, 'packshot_in_box')], '1696071629': [(2, 'lifestyle'), (3, 'packshot_in_box')],
    '189452492': [(2, 'lifestyle'), (3, 'packshot_in_box')], '892978768': [(2, 'lifestyle')],
    '931289172': [(2, 'packshot_plain')], '1705326923': [(2, 'packshot_plain')],
}


def sharp(path):
    im = Image.open(path).convert('L')
    w, h = im.size
    if w > 1200:
        im = im.resize((1200, int(h * 1200 / w)))
    return float(cv2.Laplacian(np.asarray(im), cv2.CV_64F).var())


def main():
    out = []
    agree = 0
    for p in cat:
        pid = p['id']
        f = F[pid]
        h = heuristic_v2(pid, f, p['title'], p['category_ids'])
        if pid in IN_BOX: final = 'packshot_in_box'
        elif pid in LIFESTYLE: final = 'lifestyle'
        elif pid in PLAIN: final = 'packshot_plain'
        elif pid in CLOSE_SHAWL: final = 'fabric_closeup'
        else: final = 'fabric_closeup'   # remaining = all thobe fabrics and suit wools (reviewed: cloth fills frame)
        agree += (h == final)
        gal = []
        for fi in p['image_files']:
            tags = dict(GALLERY_TAGS.get(pid, []))
            gal.append({'n': fi['n'], 'path': fi['path'], 'width': fi['width'], 'height': fi['height'],
                        'long_edge': max(fi['width'], fi['height']),
                        'tag': final if fi['n'] == 1 else tags.get(fi['n']),
                        'sharpness': round(sharp(os.path.join(ROOT, fi['path'])), 1)})
        main = gal[0]
        out.append({
            'id': pid, 'title': p['title'], 'categories': p['categories'],
            'main_image': main['path'], 'main_width': main['width'], 'main_height': main['height'],
            'main_long_edge': main['long_edge'], 'main_sharpness': main['sharpness'],
            'class': final, 'heuristic_class': h, 'heuristic_agrees': h == final,
            'method': 'heuristic (PIL/OpenCV) + visual review of contact sheet',
            'note': NOTES.get(pid),
            'heuristic_features': {k: f[k] for k in ('border_plain_frac', 'border_lum', 'border_std', 'skin_frac',
                                                     'edge_centre', 'edge_border', 'mean_sat', 'dark_green_frac')},
            'gallery': gal,
            'model_shots': [g['path'] for g in gal if g['tag'] == 'worn_by_model'],
            'lifestyle_shots': [g['path'] for g in gal if g['tag'] == 'lifestyle'],
        })
    json.dump(out, open(os.path.join(ROOT, 'data', 'photo_classes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(o['class'] for o in out), 'heuristic agreement', agree, '/', len(out))


if __name__ == '__main__':
    main()
