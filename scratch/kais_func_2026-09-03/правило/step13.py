# -*- coding: utf-8 -*-
import sys, json, copy
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as RS

BASE_RECS = list(RS.RECS)

def rebuild(extra):
    RS.RECS = BASE_RECS + [RS.Rec(h) for h in extra]
    RS.CLASS_OF = {fk: [r for r in RS.RECS if RS.in_class(r, fk)] for fk in RS.FORM_IDX}
    gs = {}
    for r in RS.RECS: gs[RS.group_of(r)] = gs.get(RS.group_of(r), 0) + 1
    RS.GROUP_SIZE = gs

def show(q, want=None, n=6):
    rows, br = RS.search(q)
    rank = None
    if want:
        for k, r in enumerate(rows):
            if r.name == want: rank = k+1; break
    print('  „%s“ → %d реда · %s%s' % (q, len(rows), br,
          ('' if want is None else ('  · „%s“ на място %s' % (want[:34], rank or '—')))))
    for r in rows[:n]:
        print('       %-52s %-16s %s' % (r.name[:52], r.kind, r.zone))

Z='ж.к. Владислав Варненчик'
FORMS = {
 'A · КАИС функция + КАИС адрес': [
   dict(name='Детско заведение (без име в регистъра), ул. Ниш 29', kind='детска градина',
        lat=43.24709, lon=27.85397, zone=Z, src='КАИС', old_names=[], status=''),
   dict(name='Детско заведение (без име в регистъра), ул. Шести септември 6', kind='детска градина',
        lat=43.24473, lon=27.85411, zone=Z, src='КАИС', old_names=[], status=''),
 ],
 'B · регистрово име (ИАМН/Община)': [
   dict(name='ДЯ №6 „Мечо Пух“', kind='детска градина', lat=43.24709, lon=27.85397, zone=Z,
        src='Регистър', old_names=['ул. Ниш 29'], status=''),
   dict(name='ДГ №40 „Детски свят“', kind='детска градина', lat=43.24473, lon=27.85411, zone=Z,
        src='Регистър', old_names=['ул. Шести септември 6'], status=''),
 ],
 'C · нов клас „детска ясла“': [
   dict(name='ДЯ №6 „Мечо Пух“', kind='детска ясла', lat=43.24709, lon=27.85397, zone=Z,
        src='Регистър', old_names=['ул. Ниш 29'], status=''),
 ],
}
Q=['детска градина владиславово','детска градина ниш 29','детска градина ниш',
   'детска градина шести септември 6','мечо пух','детска ясла владиславово',
   'ясла владиславово','детско заведение владиславово','ниш 29']
for label, extra in FORMS.items():
    print('=== %s  (+%d записа)' % (label, len(extra)))
    rebuild(extra)
    want = extra[0]['name']
    for q in Q: show(q, want, 5)
    print()
