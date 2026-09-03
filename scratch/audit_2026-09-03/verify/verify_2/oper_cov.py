# -*- coding: utf-8 -*-
"""ОПЕРАТИВНО покритие: за всеки регистров ред — има ли пин на картата
   (а) на <=150 m от адреса, геокодиран от СОБСТВЕНИЯ адресен слой на картата, или
   (б) очевидно същото заведение по име (ръчно засвидетелствано, с цитат).
   Всичко се смята наново, без да чета изходите на измервача."""
import json, math, re, collections

def hav(a,b,c,d):
    R=6371008.8
    p1,p2=math.radians(a),math.radians(c); dp=math.radians(c-a); dl=math.radians(d-b)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))

SI=json.load(open(r'C:/git/Fire_Varna/data/search_index.json',encoding='utf-8'))['entries']
PL=json.load(open(r'C:/git/Fire_Varna/data/places.json',encoding='utf-8'))['places']
HEALTH=[p for p in PL if p['kind'] in ('болница','ДКЦ','хоспис')]

by_street=collections.defaultdict(list)
for x in SI:
    l=x.get('label','')
    if '|' in l:
        s,n=l.rsplit('|',1); by_street[(s,n)].append(x['pin'])

def geo(street,num):
    v=by_street.get((street,num))
    if not v: return None
    la=sum(p[0] for p in v)/len(v); lo=sum(p[1] for p in v)/len(v)
    return (la,lo,len(v))

# регистров № -> (улица-ключ в индекса, номер)   [моят транслит, сверен ръчно]
ADDR={
 1:('slaveikov','1'), 2:None, 3:('tsar osvoboditel','100'), 4:('tsar osvoboditel','150'),
 5:('tsar osvoboditel','100'), 6:('republika','91'), 7:None, 8:('tsar osvoboditel','100'),
 9:('manush voivoda','11'), 10:None, 11:None, 12:('hristo popovich','18'),
 13:('aleko konstantinov','5'), 14:('hristo smirnenski','1'), 15:('doiran','15'),
 16:('bratia shkorpil','6'), 17:('saborni','40'), 18:('dubrovnik','58'),
 19:None, 20:('saborni','40'), 21:('sava','2'), 22:('nikola vaptsarov','2'),
 23:('narodni buditeli','5'), 24:('tsar osvoboditel','100'), 25:('hristo smirnenski','1'),
 26:('tsar osvoboditel','5'), 27:None,
 114:None, 115:None, 116:None, 117:None, 118:('shesta','2'), 119:None, 120:None,
}
REG=json.load(open(r'C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/места-покритие/registers.json',encoding='utf-8'))
rows=REG['hospitals']+REG['dkc']+REG['hospices']
MLADOST=(43.2309804,27.8785539)   # МК „Младост“ — геокодът на самия конвейер (varna_3d vn-lz-114 note)
print('ред | вид | адрес-геокод | най-близък пин от 135-те | m')
for r in rows:
    no=r['no']; key=ADDR.get(no)
    g=geo(*key) if key else None
    if no in (7,114,115,117,120,27): g=(MLADOST[0],MLADOST[1],'МК Младост (конвейерен геокод)')
    if not g:
        print('%3d | %-16s | НЯМА геокод | — | —'%(no,r.get('type','')[:16])); continue
    best=min(HEALTH,key=lambda p:hav(g[0],g[1],p['lat'],p['lon']))
    d=hav(g[0],g[1],best['lat'],best['lon'])
    print('%3d | %-16s | %.5f,%.5f (%s) | %-52s | %7.1f'%(no,r.get('type','')[:16],g[0],g[1],g[2],best['name'][:52],d))
