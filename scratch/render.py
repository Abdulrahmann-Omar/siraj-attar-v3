import json, asyncio, re
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='msedge',headless=True)
        ctx=await b.new_context(viewport={'width':1440,'height':900},locale='ar-SA',user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0")
        pg=await ctx.new_page()
        api=[]
        pg.on('response', lambda r: api.append((r.status,r.url)) if 'api.salla.dev' in r.url else None)
        await pg.goto('https://sirajattarbros.com/ar',wait_until='networkidle',timeout=90000)
        await pg.wait_for_timeout(4000)
        await pg.screenshot(path='data/raw/screens/home_top.png')
        await pg.screenshot(path='data/raw/screens/home_full.png',full_page=True)
        info=await pg.evaluate('''()=>{
          const cs=getComputedStyle(document.documentElement);
          const vars={}; for(const n of ['--color-primary','--color-primary-dark','--color-primary-light','--color-primary-reverse','--main-text-color','--bg-color','--font-main','--color-text']) vars[n]=cs.getPropertyValue(n).trim();
          const body=getComputedStyle(document.body);
          const hdr=document.querySelector('header'); const hcs=hdr?getComputedStyle(hdr):null;
          const ftr=document.querySelector('footer'); const fcs=ftr?getComputedStyle(ftr):null;
          const ann=[...document.querySelectorAll('.announcement, salla-advertisement, .top-navbar, [class*=announce], [class*=advert]')].map(e=>e.innerText.trim()).filter(Boolean);
          const banners=[...document.querySelectorAll('img')].map(i=>({src:i.currentSrc||i.src,alt:i.alt,w:i.naturalWidth,h:i.naturalHeight})).filter(i=>i.w>=800);
          const pay=[...document.querySelectorAll('footer img, .payment img, [class*=payment] img')].map(i=>i.alt||i.src);
          const fonts=[...new Set([...document.querySelectorAll('h1,h2,h3,p,a,span')].slice(0,300).map(e=>getComputedStyle(e).fontFamily))];
          const btn=document.querySelector('.btn--primary, .s-button-primary, salla-button button, button');
          return {vars, bodyBg:body.backgroundColor, bodyColor:body.color, bodyFont:body.fontFamily, header: hcs&&{bg:hcs.backgroundColor,color:hcs.color}, footer: fcs&&{bg:fcs.backgroundColor,color:fcs.color}, ann, banners, pay, fonts, btn: btn&&{bg:getComputedStyle(btn).backgroundColor, color:getComputedStyle(btn).color}};
        }''')
        info['api_calls']=api[:40]
        json.dump(info,open('data/raw/site/home_render.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
        html=await pg.content(); open('data/raw/site/home_rendered.html','w',encoding='utf-8').write(html)
        # one category page: verify DOM count vs API
        res={}
        for cid,url in [('1812386828','https://sirajattarbros.com/ar/أشمغة-حمراء/c1812386828'),('23035657','https://sirajattarbros.com/ar/الغتر/c23035657')]:
            api.clear()
            await pg.goto(url,wait_until='networkidle',timeout=90000)
            await pg.wait_for_timeout(3000)
            for _ in range(6):
                await pg.mouse.wheel(0,4000); await pg.wait_for_timeout(1200)
            ids=await pg.evaluate('''()=>[...new Set([...document.querySelectorAll('a[href*="/p"]')].map(a=>(a.href.match(/\/p(\d+)(?:$|[?#])/)||[])[1]).filter(Boolean))]''')
            res[cid]={'dom_ids':ids,'api':[(s,u[:150]) for s,u in api]}
            await pg.screenshot(path=f'data/raw/screens/cat_{cid}.png')
        json.dump(res,open('data/raw/site/category_render.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
        await b.close()
asyncio.run(main())
