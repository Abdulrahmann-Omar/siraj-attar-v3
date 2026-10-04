import base64, pathlib
from playwright.sync_api import sync_playwright
F = pathlib.Path(r"C:/Users/a0109/code/everyside/apps/render/assets/fonts")
b = base64.b64encode((F/"Cairo-Bold.ttf").read_bytes()).decode()
css = f"@font-face{{font-family:'C';src:url(data:font/ttf;base64,{b});font-weight:700;}}"
html = f"<html><head><style>{css} body{{background:#777;color:#fff;margin:20px;font-family:'C';font-weight:700;font-size:90px}}</style></head><body><div dir=rtl>بيت العطار، (arabic comma)</div><div dir=rtl>بيت العطار, (latin comma)</div></body></html>"
with sync_playwright() as p:
    br = p.chromium.launch(channel="msedge"); pg = br.new_page(viewport={"width":1000,"height":330})
    pg.set_content(html); pg.wait_for_timeout(400); pg.screenshot(path="research/old_renders/fontcheck/comma.png"); br.close()
