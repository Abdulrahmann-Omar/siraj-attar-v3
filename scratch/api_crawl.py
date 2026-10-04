import json, time, requests, sys
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 Edg/130.0"
H={"User-Agent":UA,"Store-Identifier":"946211295","Accept":"application/json","Origin":"https://sirajattarbros.com","Referer":"https://sirajattarbros.com/ar","Accept-Language":"ar"}
S=requests.Session(); S.headers.update(H)
def get(url):
    for a in range(4):
        try:
            r=S.get(url,timeout=30)
            if r.status_code==200: return r.json()
            print('status',r.status_code,url[:120],file=sys.stderr)
        except Exception as e: print('err',e,file=sys.stderr)
        time.sleep(2*(a+1))
    return None
def crawl(first):
    out=[];url=first;pages=0
    while url:
        d=get(url)
        if not d: return out,pages,False
        pages+=1
        out+=d['data']
        url=(d.get('cursor') or {}).get('next')
        time.sleep(0.6)
    return out,pages,True
res={}
allp,pg,ok=crawl("https://api.salla.dev/store/v1/products?source=product.index")
res['_all']={'pages':pg,'ok':ok,'products':allp}
print('all',len(allp),pg,ok)
cats=["1704276239","1812386828","23035657","1394974218","1785129829","1145244262","2129648660","1954429207","190964591","2122362229","270558993","1645118994","162579484","1537073949","897188382","1361854488","552669551","587820825","2094501402","371730791","1677019232","1037195105","1501926755","727889004","978041972","1337375602","1180391440","971240205","412732516","2019914408","755154187"]
for c in cats:
    ps,pg,ok=crawl(f"https://api.salla.dev/store/v1/products?source=categories&source_value[]={c}")
    res[c]={'pages':pg,'ok':ok,'products':ps}
    print(c,len(ps),pg,ok)
json.dump(res,open('scratch/api/api_dump.json','w',encoding='utf-8'),ensure_ascii=False)
