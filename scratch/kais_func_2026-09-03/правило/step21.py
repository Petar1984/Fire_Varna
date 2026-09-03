# -*- coding: utf-8 -*-
"""Колко от свободните площадки носят ГОДЕН адрес в КАИС (улица+номер)?"""
import sys, json, collections, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,'.')
from lib_kais import *
info,cols=load_info(); rows=info['rows']
doc=json.load(open('placement.json',encoding='utf-8'))
si,ni=cols['street'],cols['num']
CAD=re.compile(r'\b\d{4,5}\.\d+\.\d+')
tot=collections.Counter()
for f,e in doc['hole'].items():
    n_street=n_quar=n_none=n_cad=0
    ex=[]
    for s in e['free60']:
        best=None
        for i in s['bodies']:
            st=field(info,cols,rows[i],'street'); nu=field(info,cols,rows[i],'num')
            if st and nu: best=('%s %s'%(st,nu)); break
        if best: n_street+=1; ex.append(best)
        else:
            q=None
            for i in s['bodies']:
                q=field(info,cols,rows[i],'quar') or field(info,cols,rows[i],'addr')
                if q: break
            if q: n_quar+=1
            else: n_none+=1
        for i in s['bodies']:
            a=field(info,cols,rows[i],'addr') or ''
            if '10135' in a or CAD.search(a): n_cad+=1; break
    print('%-32s непокрити %3d | улица+номер %3d | само квартал/адрес %3d | нищо %2d | с „10135“ %2d'
          % (f,len(e['free60']),n_street,n_quar,n_none,n_cad))
    print('     примери (улица+номер): ' + ' · '.join(ex[:6]))
