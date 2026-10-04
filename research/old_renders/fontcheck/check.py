import base64, pathlib
from playwright.sync_api import sync_playwright
F = pathlib.Path(r"C:/Users/a0109/code/everyside/apps/render/assets/fonts")
faces = [("Cairo","Cairo-Black.ttf",900),("Cairo","Cairo-Bold.ttf",700),("Cairo","Cairo-Regular.ttf",400),
         ("Tajawal","Tajawal-Bold.ttf",700),("Alexandria","Alexandria-Bold.ttf",700),("Plex","IBMPlexSansArabic-Bold.ttf",700),("Inter","Inter-Regular.ttf",400)]
css = ""
for fam,f,w in faces:
    b = base64.b64encode((F/f).read_bytes()).decode()
    css += f"@font-face{{font-family:'{fam}';src:url(data:font/ttf;base64,{b});font-weight:{w};}}\n"
rows = ""
for fam,w,label in [("Cairo",900,"Cairo Black 900"),("Cairo",700,"Cairo Bold 700"),("Tajawal",700,"Tajawal Bold"),("Alexandria",700,"Alexandria Bold"),("Plex",700,"IBM Plex Sans Arabic Bold")]:
    rows += f"<div class=r><span class=l>{label}</span><span dir=rtl style=\"font-family:'{fam}';font-weight:{w}\">بيت العطار، أكثر من ثمانين سنة &nbsp; 157.82 ر.س &nbsp; لشتاك</span></div>"
rows += "<div class=r><span class=l>Inter 400</span><span style=\"font-family:'Inter';letter-spacing:.1em\">SIRAJATTARBROS.COM</span></div>"
html = f"<html><head><style>{css} body{{background:#fff;margin:20px}} .r{{display:flex;gap:30px;align-items:center;font-size:46px;margin:6px 0}} .l{{font:14px sans-serif;width:200px;color:#888}}</style></head><body>{rows}</body></html>"
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width":1500,"height":560})
    pg.set_content(html); pg.wait_for_timeout(500)
    pg.screenshot(path=r"research/old_renders/fontcheck/specimens.png")
    b.close()
print("ok")
