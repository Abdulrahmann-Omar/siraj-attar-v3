import json, asyncio, sys
from playwright.async_api import async_playwright
JS=r'''()=>[...new Set([...document.querySelectorAll('a[href*="/p"]')].map(a=>(a.href.match(/\/p(\d+)(?:$|[?#])/)||[])[1]).filter(Boolean))]'''
async def main(cats):
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='msedge',headless=True)
        ctx=await b.new_context(viewport={'width':1440,'height':900},locale='ar-SA')
        pg=await ctx.new_page()
        api=[]
        pg.on('response', lambda r: api.append((r.status,r.url[:160])) if 'api.salla.dev' in r.url else None)
        res={}
        for cid,url in cats:
            api.clear()
            try:
                await pg.goto(url,wait_until='domcontentloaded',timeout=60000)
            except Exception as e: print('goto',cid,e)
            await pg.wait_for_timeout(5000)
            for _ in range(8):
                await pg.mouse.wheel(0,3000); await pg.wait_for_timeout(1500)
            ids=await pg.evaluate(JS)
            res[cid]={'dom_ids':ids,'api':api[:]}
            print(cid,len(ids),[a[0] for a in api])
        json.dump(res,open('data/raw/site/category_render.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
        await b.close()
cats=[('1812386828','https://sirajattarbros.com/ar/أشمغة-حمراء/c1812386828'),('23035657','https://sirajattarbros.com/ar/الغتر/c23035657'),('1954429207','https://sirajattarbros.com/ar/الأقمشة/c1954429207')]
asyncio.run(main(cats))
