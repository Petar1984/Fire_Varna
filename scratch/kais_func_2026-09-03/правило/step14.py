# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as RS
BASE=list(RS.RECS)
def rebuild(extra):
    RS.RECS = BASE + [RS.Rec(h) for h in extra]
    RS.CLASS_OF = {fk:[r for r in RS.RECS if RS.in_class(r,fk)] for fk in RS.FORM_IDX}
    gs={}
    for r in RS.RECS: gs[RS.group_of(r)]=gs.get(RS.group_of(r),0)+1
    RS.GROUP_SIZE=gs
def show(q,want,n=4):
    rows,br=RS.search(q); rank=None
    for k,r in enumerate(rows):
        if r.name==want: rank=k+1;break
    print('   %-40s → %3d реда · %-22s място %s | топ: %s' % ('„%s“'%q,len(rows),br,rank or '—',
          ' · '.join(r.name[:26] for r in rows[:2]) or '—'))
Z='ж.к. Владислав Варненчик'
FORMS={
 'D · регистрово име + КАИС адрес В ИМЕТО':[
   dict(name='ДЯ №6 „Мечо Пух“ (ул. Ниш 29)',kind='детска градина',lat=43.24709,lon=27.85397,zone=Z,old_names=[],status=''),
 ],
 'E · КАИС-носено име (addr полето)':[
   dict(name='ЦДГ 10 - ПРИКАЗКА',kind='детска градина',lat=43.24709,lon=27.85397,zone=Z,old_names=[],status=''),
 ],
 'F · само функция + адрес, кратко':[
   dict(name='Детска градина, ул. Ниш 29',kind='детска градина',lat=43.24709,lon=27.85397,zone=Z,old_names=[],status=''),
 ],
 'G · регистрово име, адресът в old_names':[
   dict(name='ДЯ №6 „Мечо Пух“',kind='детска градина',lat=43.24709,lon=27.85397,zone=Z,
        old_names=['ул. Ниш 29','Детска ясла 6'],status=''),
 ],
}
Q=['детска градина владиславово','детска градина ниш 29','ниш 29','мечо пух','детска градина ниш',
   'ясла 6','детска градина 6','приказка']
for lab,ex in FORMS.items():
    print('=== '+lab); rebuild(ex); w=ex[0]['name']
    for q in Q: show(q,w)
    print()
