import json, time, requests, sys, os, random
from concurrent.futures import ThreadPoolExecutor
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0"
r=json.load(open('data/raw/api/api_dump_2026-10-04.json',encoding='utf-8'))
prods=r['_all']['products']
S=requests.Session(); S.headers.update({"User-Agent":UA,"Accept-Language":"ar"})
def fetch(p):
    pid=p['id']; out=f'data/raw/pages/p{pid}.html'
    if os.path.exists(out) and os.path.getsize(out)>20000: return pid,'cached'
    url=p['url']
    for a in range(4):
        try:
            resp=S.get(url,timeout=40)
            if resp.status_code==200:
                open(out,'w',encoding='utf-8').write(resp.text); time.sleep(0.8+random.random()*0.6); return pid,200
            last=resp.status_code
        except Exception as e: last=str(e)
        time.sleep(3*(a+1))
    return pid,last
with ThreadPoolExecutor(3) as ex:
    res=list(ex.map(fetch,prods))
bad=[x for x in res if x[1] not in (200,'cached')]
print(len(res),'bad',bad)
