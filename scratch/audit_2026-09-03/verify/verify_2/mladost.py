import json,math
def hav(a,b,c,d):
    R=6371008.8; p1,p2=math.radians(a),math.radians(c); dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
C=json.load(open(r'C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/места-покритие/kais_centroids_all.json',encoding='utf-8'))
print('пример:',list(C.items())[0])
INFO=json.load(open(r'C:/git/varna_3d/web/varna_buildings_info.json',encoding='utf-8'))
print('info type',type(INFO), (list(INFO.keys())[:4] if isinstance(INFO,dict) else len(INFO)))
E=(43.2309804,27.8785539)
near=[]
for k,v in C.items():
    la,lo = (v[0],v[1]) if isinstance(v,(list,tuple)) else (v['lat'],v['lon'])
    d=hav(E[0],E[1],la,lo)
    if d<80: near.append((d,k,la,lo))
near.sort()
for d,k,la,lo in near[:12]:
    rec=INFO[k] if isinstance(INFO,dict) and k in INFO else (INFO[int(k)] if isinstance(INFO,list) and int(k)<len(INFO) else None)
    print('%6.1f m  i=%-7s %s'%(d,k,json.dumps(rec,ensure_ascii=False)[:200] if rec else '—'))
