# -*- coding: utf-8 -*-
"""Search simulation: import the reference under its guard, then add records."""
import sys, json, io
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r'C:/git/Fire_Varna/scratch/places_search')
import recall_sweep as RS          # main() is under `if __name__ == "__main__"`

def show(q, n=8):
    rows, br = RS.search(q)
    print('  „%s“ → %d реда · клон %s' % (q, len(rows), br))
    for r in rows[:n]:
        print('       %-46s %-22s %s' % (r.name[:46], r.kind, r.zone))
    if not rows: print('       —')

print('=== БАЗА (361 записа, без нови)')
for q in ['детска градина владиславово','детска градина ниш 29','детска градина ниш',
          'детска градина шести септември 6','детско заведение','детско заведение владиславово',
          'ясла','детска ясла','детски градини владиславово']:
    show(q, 6)
print()
print('CLASS_OF непразни форми:', sum(1 for k,v in RS.CLASS_OF.items() if v), 'от', len(RS.CLASS_OF))
print('„детско заведение“ клас размер:', len(RS.CLASS_OF.get('detsko zavedenie',[])) if 'detsko zavedenie' in RS.CLASS_OF else 'няма такъв ключ')
print('форми в FORM_IDX за заведение:', [k for k in RS.FORM_IDX if 'zavedeni' in k])
print('П7 добавени за ж.к. Владислав Варненчик:', RS.P7_ADDED.get('ж.к. Владислав Варненчик'))
print('П7 добавени за кв. Владиславово:', RS.P7_ADDED.get('кв. Владиславово'))
