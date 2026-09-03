# -*- coding: utf-8 -*-
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('placement.json',encoding='utf-8'))
p=d['placement']
def okb(x):
    v=x['ok_d']
    return '0' if v==0 else '<=10' if v<=10 else '<=30' if v<=30 else '<=60' if v<=60 else '<=200' if v<=200 else '>200'
g=collections.Counter((x['func_class'],okb(x)) for x in p)
B=['0','<=10','<=30','<=60','<=200','>200']
print('%-9s|%s' % ('func_class',''.join('%7s'%b for b in B)))
for c in ['вярна','двор','помощна','друга']:
    print('%-9s|%s  общо %d' % (c,''.join('%7d'%g[(c,b)] for b in B),sum(g[(c,b)] for b in B)))
print()
print('двор:',[x['name'] for x in p if x['func_class']=='двор'])
print('помощна:',[(x['name'],x['func'],x['ok_d']) for x in p if x['func_class']=='помощна'])
print()
print('=== „друга“ и вярно тяло на >200 m (%d) — Г2-ГРЕШКА кандидати' % sum(1 for x in p if x['func_class']=='друга' and x['ok_d']>200))
for x in sorted((x for x in p if x['func_class']=='друга' and x['ok_d']>200),key=lambda x:-x['ok_d']):
    print('   %-40s %-26s %-22s func=%-30s ok_d=%7.1f' % (x['name'][:40],x['kind'],x['zone'][:22],x['func'][:30],x['ok_d']))
print()
print('=== „друга“ и вярно тяло ≤30 m (%d) — Г2-ФЛАГ „щракни“' % sum(1 for x in p if x['func_class']=='друга' and x['ok_d']<=30))
for x in sorted((x for x in p if x['func_class']=='друга' and x['ok_d']<=30),key=lambda x:x['ok_d']):
    print('   %-40s %-26s func=%-30s ok_d=%6.1f' % (x['name'][:40],x['kind'],x['func'][:30],x['ok_d']))
print()
print('кумулативно по dist: вътре %d · ≤10 %d · ≤30 %d · ≤60 %d' % (
  sum(1 for x in p if x['dist_m']==0), sum(1 for x in p if x['dist_m']<=10),
  sum(1 for x in p if x['dist_m']<=30), sum(1 for x in p if x['dist_m']<=60)))
