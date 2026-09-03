# -*- coding: utf-8 -*-
"""Контрафакт: ако A6 пускаше ЧИСЛАТА в old_names (само това), какво става?"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as RS
BASE=list(RS.RECS)
Z='ж.к. Владислав Варненчик'
G_REC=dict(name='ДЯ №6 „Мечо Пух“',kind='детска градина',lat=43.24709,lon=27.85397,
           zone=Z,old_names=['ул. Ниш 29','Детска ясла 6'],status='')
def build(extra, keep_numbers=False):
    recs=[]
    for h_ in extra:
        r=RS.Rec(h_)
        if keep_numbers:
            for o in (h_.get('old_names') or []):
                for t in RS.place_tokens(o):
                    if t.orig in RS.ADDR or len(t.orig)<=2 and not t.num: continue
                    if t.num: r.aset.add(t.s)
        recs.append(r)
    RS.RECS=BASE+recs
    RS.CLASS_OF={fk:[x for x in RS.RECS if RS.in_class(x,fk)] for fk in RS.FORM_IDX}
    gs={}
    for x in RS.RECS: gs[RS.group_of(x)]=gs.get(RS.group_of(x),0)+1
    RS.GROUP_SIZE=gs
def show(q,want):
    rows,br=RS.search(q); k=None
    for j,x in enumerate(rows):
        if x.name==want: k=j+1;break
    print('   %-34s -> %2d реда · %-18s място %s' % ('„%s“'%q,len(rows),br,k or '—'))
for keep in (False,True):
    print('=== A6 пуска числата от old_names:', keep)
    build([G_REC], keep)
    for q in ['детска градина ниш 29','ниш 29','детска градина ниш','мечо пух','ясла 6']:
        show(q, G_REC['name'])
