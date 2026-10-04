"""Download every gallery image of every product at original resolution.

Reads data/catalogue.json (images = original URLs), writes data/images/<productid>_<n>.<ext> (n = 1 is the main photo)
and data/images/_index.json (per product: n, url, path, bytes, width, height). Polite: 3 workers, retries, skip existing.
"""
import json, os, re, time, random, io, hashlib
from concurrent.futures import ThreadPoolExecutor
import requests
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data', 'images')
os.makedirs(OUT, exist_ok=True)
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0'
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Referer': 'https://sirajattarbros.com/'})
EXT = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/webp': 'webp', 'image/gif': 'gif', 'image/avif': 'avif'}


def get(url, tries=4):
    last = None
    for a in range(tries):
        try:
            r = S.get(url, timeout=60)
            if r.status_code == 200 and r.headers.get('content-type', '').startswith('image/'):
                return r
            last = r.status_code
            if r.status_code == 404:
                return None
        except Exception as e:
            last = e
        time.sleep(2 * (a + 1))
    print('FAIL', url, last)
    return None


def candidates(url):
    """Try the un-suffixed original first for cdn.files.salla.network '_WxH' names."""
    m = re.match(r'^(.*/[0-9a-f-]{36})_(\d+)x(\d+)\.(\w+)$', url)
    if m:
        return [f'{m.group(1)}.{m.group(4)}', url]
    return [url]


def job(args):
    pid, n, url = args
    existing = [f for f in os.listdir(OUT) if f.startswith(f'{pid}_{n}.')]
    if existing:
        path = os.path.join(OUT, existing[0])
        b = open(path, 'rb').read()
        used = url
    else:
        r, used = None, None
        for c in candidates(url):
            r = get(c, tries=1 if c != url else 4)
            if r is not None:
                used = c
                break
        if r is None:
            return pid, n, {'n': n, 'url': url, 'error': 'download failed'}
        ext = EXT.get(r.headers['content-type'].split(';')[0], url.rsplit('.', 1)[-1].lower())
        path = os.path.join(OUT, f'{pid}_{n}.{ext}')
        b = r.content
        open(path, 'wb').write(b)
        time.sleep(0.4 + random.random() * 0.5)
    im = Image.open(io.BytesIO(b))
    return pid, n, {'n': n, 'url': url, 'downloaded_from': used,
                    'path': os.path.relpath(path, ROOT).replace('\\', '/'),
                    'bytes': len(b), 'width': im.size[0], 'height': im.size[1], 'format': im.format,
                    'mode': im.mode, 'sha1': hashlib.sha1(b).hexdigest()[:16]}


def main():
    cat = json.load(open(os.path.join(ROOT, 'data', 'catalogue.json'), encoding='utf-8'))
    jobs = [(p['id'], i + 1, u) for p in cat for i, u in enumerate(p['images'])]
    print('images to fetch', len(jobs))
    index = {}
    with ThreadPoolExecutor(3) as ex:
        for pid, n, rec in ex.map(job, jobs):
            index.setdefault(pid, []).append(rec)
    for pid in index:
        index[pid].sort(key=lambda r: r['n'])
    json.dump(index, open(os.path.join(OUT, '_index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    errs = [r for v in index.values() for r in v if 'error' in r]
    print('done', sum(len(v) for v in index.values()), 'errors', len(errs))


if __name__ == '__main__':
    main()
