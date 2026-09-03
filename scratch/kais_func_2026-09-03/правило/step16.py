# -*- coding: utf-8 -*-
import sys, json, collections
sys.stdout.reconfigure(encoding='utf-8')
out=json.load(open('_step15.json',encoding='utf-8'))
print('=== (30,60] m — 4 записа')
for x in sorted(out,key=lambda x:-x['dist_m'])[:4]:
    print('   %6.2f m %-40s %-14s func=%-28s ok_d=%.1f' % (x['dist_m'],x['name'][:40],x['kind'],x['func'][:28],x['ok_d']))
print()
print('=== (10,30] m — 19 записа')
for x in sorted((x for x in out if 10<x['dist_m']<=30),key=lambda x:-x['dist_m']):
    print('   %6.2f m %-40s %-14s func=%-28s ok_d=%.1f' % (x['dist_m'],x['name'][:40],x['kind'],x['func'][:28],x['ok_d']))
print()
print('=== ok_d (разстояние до НАЙ-БЛИЗКОТО тяло с ВЯРНА функция) — разпределение')
c=collections.Counter()
for x in out:
    d=x['ok_d']
    c['0 (вътре/допира)' if d==0 else ('≤10 m' if d<=10 else ('≤30 m' if d<=30 else ('≤60 m' if d<=60 else ('≤200 m' if d<=200 else '>200 m'))))]+=1
for k in ['0 (вътре/допира)','≤10 m','≤30 m','≤60 m','≤200 m','>200 m']: print('   %-18s %3d' % (k,c[k]))
print()
print('=== хотели с ДРУГА функция и ok_d > 60 m (кандидати за проверка)')
n=0
for x in sorted((x for x in out if x['file']=='hotels.json' and not x['func_ok']),key=lambda x:-x['ok_d']):
    if x['ok_d']>60:
        n+=1
        if n<=14: print('   %-38s %-24s d=%5.1f func=%-30s ok_d=%7.1f' % (x['name'][:38],x['zone'][:24],x['dist_m'],x['func'][:30],x['ok_d']))
print('   ... общо', n)
print()
print('=== хотели с ДРУГА функция, но вярно тяло ≤10 m (кандидати за „щракване“)')
m=[x for x in out if x['file']=='hotels.json' and not x['func_ok'] and x['ok_d']<=10]
for x in m[:10]: print('   %-38s d=%5.1f func=%-28s ok_d=%.1f' % (x['name'][:38],x['dist_m'],x['func'][:28],x['ok_d']))
print('   общо', len(m))
