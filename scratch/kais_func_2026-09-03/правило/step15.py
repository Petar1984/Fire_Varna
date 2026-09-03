# -*- coding: utf-8 -*-
"""Full placement with func-match + nearest correct-function body."""
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
from shapely.geometry import Point
from shapely.strtree import STRtree
info,cols=load_info(); polys=load_geoms(); rows=info['rows']
dl=load_delivered()
dictf=info['dict']['func']; fi=cols['func']
MATCH={'детска градина':['Сграда за детско заведение'],
 'училище':['Сграда за образование'],'университет':['Сграда за образование'],
 'болница':['Здравно заведение'],'ДКЦ':['Здравно заведение'],'хоспис':['Здравно заведение'],
 'Хотел':['Хотел','Апартаментен хотел','Курортна, туристическа сграда'],
 'Семеен хотел':['Хотел','Апартаментен хотел','Курортна, туристическа сграда'],
 'апарт-хотел':['Хотел','Апартаментен хотел','Курортна, туристическа сграда'],
 'хотел · без категоризация':['Хотел','Апартаментен хотел','Курортна, туристическа сграда']}
# per-function subtrees
SUB={}
for f in set(x for v in MATCH.values() for x in v):
    k=dictf.index(f); idx=[i for i,r in enumerate(rows) if r[fi]==k]
    SUB[f]=(idx, STRtree([polys[i] for i in idx]))
tree=STRtree(polys)
out=[]
for r in dl:
    pt=Point(*to_m(r['lon'],r['lat']))
    ins=[int(i) for i in tree.query(pt) if polys[int(i)].covers(pt)]
    ok=set(MATCH[r['kind']])
    if ins:
        good=[i for i in ins if field(info,cols,rows[i],'func') in ok]
        b=(sorted(good,key=lambda i:(polys[i].area,i))[0] if good
           else sorted(ins,key=lambda i:(polys[i].area,i))[0])
        d=0.0
    else:
        cand=[(polys[int(i)].distance(pt),int(i)) for i in tree.query(pt.buffer(300.0))]
        if not cand:
            cand=[(polys[int(i)].distance(pt),int(i)) for i in tree.query(pt.buffer(3000.0))]
        d,b=min(cand)
    f=field(info,cols,rows[b],'func')
    # nearest body of a CORRECT function
    best=(1e9,None)
    for fn in ok:
        idx,t=SUB[fn]
        for rad in (10,30,60,120,300,1000,5000):
            c=[(t.geometries[int(j)].distance(pt), idx[int(j)]) for j in t.query(pt.buffer(rad))]
            if c: best=min(best,min(c)); break
    out.append(dict(rid=r['rid'],file=r['file'],name=r['name'],kind=r['kind'],zone=r['zone'],
        src=r['src'],lat=r['lat'],lon=r['lon'],i=b,dist_m=round(d,2),n_inside=len(ins),
        func=f,func_ok=(f in ok),area_m2=rows[b][cols['area_m2']],
        prop=field(info,cols,rows[b],'prop'),reg=field(info,cols,rows[b],'reg'),
        addr=field(info,cols,rows[b],'addr'),
        ok_i=best[1],ok_d=round(best[0],2)))
json.dump(out,open('_step15.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)

def bucket(d):
    return 'вътре' if d==0 else ('≤10 m' if d<=10 else ('≤30 m' if d<=30 else ('≤60 m' if d<=60 else '>60 m')))
B=collections.Counter(); BF=collections.Counter()
for x in out:
    b=bucket(x['dist_m']); B[b]+=1; BF[(b, 'вярна' if x['func_ok'] else 'друга')]+=1
print('=== 361 записа: кофи × функция')
for b in ['вътре','≤10 m','≤30 m','≤60 m','>60 m']:
    print('  %-7s общо %3d | вярна функция %3d | друга %3d' % (b,B[b],BF[(b,'вярна')],BF[(b,'друга')]))
print('  ОБЩО    %3d | вярна %3d | друга %3d' % (len(out),sum(1 for x in out if x['func_ok']),
      sum(1 for x in out if not x['func_ok'])))
print()
print('=== по клас')
for k in ['детска градина','училище','университет','болница','ДКЦ','хоспис']:
    s=[x for x in out if x['kind']==k]
    print('  %-16s n=%3d вътре=%3d вярна=%3d >60m=%d ok_d медиана=%.1f m' % (k,len(s),
      sum(1 for x in s if x['dist_m']==0),sum(1 for x in s if x['func_ok']),
      sum(1 for x in s if x['dist_m']>60), sorted(x['ok_d'] for x in s)[len(s)//2]))
s=[x for x in out if x['file']=='hotels.json']
print('  %-16s n=%3d вътре=%3d вярна=%3d >60m=%d ok_d медиана=%.1f m' % ('хотели',len(s),
  sum(1 for x in s if x['dist_m']==0),sum(1 for x in s if x['func_ok']),
  sum(1 for x in s if x['dist_m']>60), sorted(x['ok_d'] for x in s)[len(s)//2]))
print()
print('=== >60 m (поименно)')
for x in sorted(out,key=lambda x:-x['dist_m']):
    if x['dist_m']>60: print('   %6.1f m  %-40s %-14s %-22s ok_d=%.1f' % (x['dist_m'],x['name'][:40],x['kind'],x['zone'][:22],x['ok_d']))
print()
print('=== ДРУГА функция (поименно, места)')
for x in out:
    if not x['func_ok'] and x['file']=='places.json':
        print('   %-40s %-14s d=%5.1f  →%-32s ok_d=%6.1f' % (x['name'][:40],x['kind'],x['dist_m'],x['func'][:32],x['ok_d']))
