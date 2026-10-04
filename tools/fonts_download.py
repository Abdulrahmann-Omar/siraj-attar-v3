"""Download OFL font families from the official google/fonts GitHub repo into
fonts/<slug>/ (TTF as published by Google Fonts, plus OFL.txt and METADATA.pb).

Writes fonts/manifest.json: family, files, licence, designer, source URLs.
Only directories under ofl/ are fetched (SIL Open Font License 1.1: free for
commercial use, embedding in images/PDFs and self-hosted web use).

Run:  .venv\\Scripts\\python tools\\fonts_download.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

import requests

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "fonts"
API = "https://api.github.com/repos/google/fonts/contents/ofl/{d}"
RAW = "https://raw.githubusercontent.com/google/fonts/main/ofl/{d}/{f}"

ARABIC = {
    "Cairo": "cairo",                       # used inside the old poster images
    "IBM Plex Sans Arabic": "ibmplexsansarabic",
    "Alexandria": "alexandria",
    "Readex Pro": "readexpro",
    "Noto Kufi Arabic": "notokufiarabic",
    "Noto Naskh Arabic": "notonaskharabic",
    "Noto Sans Arabic": "notosansarabic",
    "Amiri": "amiri",
    "Aref Ruqaa": "arefruqaa",
    "Reem Kufi": "reemkufi",
    "Tajawal": "tajawal",
    "Almarai": "almarai",
    "Changa": "changa",
    "Rubik": "rubik",
    "Lalezar": "lalezar",
    "Marhey": "marhey",
    "Baloo Bhaijaan 2": "baloobhaijaan2",
    "El Messiri": "elmessiri",
    "Zain": "zain",
    "Kufam": "kufam",
    "Lateef": "lateef",
    "Scheherazade New": "scheherazadenew",
    "Harmattan": "harmattan",
    "Mada": "mada",
    "Vazirmatn": "vazirmatn",
    "Beiruti": "beiruti",
}
LATIN = {
    "Manrope": "manrope",
    "Inter": "inter",
    "Playfair Display": "playfairdisplay",
    "Cormorant": "cormorant",
    "Cormorant Garamond": "cormorantgaramond",
    "Fraunces": "fraunces",
}

S = requests.Session()
S.headers["User-Agent"] = "siraj-attar-v3 font fetch (local research)"


def gh_token() -> str | None:
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=20)
        tok = out.stdout.strip()
        return tok or None
    except Exception:
        return None


def list_dir(d: str, token: str | None):
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        r = S.get(API.format(d=d), headers=h, timeout=60)
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            return None
        time.sleep(2 + attempt * 3)
    r.raise_for_status()


def parse_metadata(text: str) -> dict:
    out = {}
    for key in ("name", "designer", "license", "category", "date_added"):
        m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', text, re.M)
        if m:
            out[key] = m.group(1)
    out["subsets"] = re.findall(r'^subsets:\s*"([^"]+)"', text, re.M)
    out["axes"] = [
        {"tag": t, "min": float(a), "max": float(b)}
        for t, a, b in re.findall(r'axes\s*{\s*tag:\s*"(\w+)"\s*min_value:\s*([\d.]+)\s*max_value:\s*([\d.]+)', text)
    ]
    return out


def main():
    token = gh_token()
    manifest = {"source": "https://github.com/google/fonts (ofl/)", "families": []}
    for group, table in (("arabic", ARABIC), ("latin", LATIN)):
        for fam, d in table.items():
            items = list_dir(d, token)
            if items is None:
                print(f"!! {fam}: ofl/{d} not found", file=sys.stderr)
                manifest["families"].append({"family": fam, "group": group, "status": "not found"})
                continue
            dest = FONTS / d
            dest.mkdir(parents=True, exist_ok=True)
            files = []
            meta = {}
            for it in items:
                name = it["name"]
                if it["type"] != "file":
                    continue
                if not (name.endswith(".ttf") or name in ("OFL.txt", "METADATA.pb", "DESCRIPTION.en_us.html")):
                    continue
                url = RAW.format(d=d, f=quote(name))
                path = dest / name
                if not path.exists() or path.stat().st_size != it.get("size", -1):
                    r = S.get(url, timeout=120)
                    r.raise_for_status()
                    path.write_bytes(r.content)
                data = path.read_bytes()
                if name == "METADATA.pb":
                    meta = parse_metadata(data.decode("utf-8", "replace"))
                files.append({"file": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()[:16],
                              "url": url})
            lic = meta.get("license", "OFL")
            entry = {"family": fam, "group": group, "dir": f"fonts/{d}", "license": lic,
                     "license_file": f"fonts/{d}/OFL.txt" if (dest / "OFL.txt").exists() else None,
                     "designer": meta.get("designer"), "category": meta.get("category"),
                     "subsets": meta.get("subsets"), "axes": meta.get("axes"),
                     "files": files, "status": "ok"}
            manifest["families"].append(entry)
            ttfs = [f["file"] for f in files if f["file"].endswith(".ttf")]
            print(f"ok {fam:22s} {lic:5s} {len(ttfs)} ttf  {sum(f['bytes'] for f in files)//1024} KB")
    (FONTS / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
