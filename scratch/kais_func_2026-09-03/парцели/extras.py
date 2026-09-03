# -*- coding: utf-8 -*-
"""Допълнителни мерки върху plots_by_func.json + candidates.json.

    set PYTHONIOENCODING=utf-8
    python extras.py
"""
import json, os, re, sys, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, 'plots_by_func.json'), encoding='utf-8'))
C = json.load(open(os.path.join(HERE, 'candidates.json'), encoding='utf-8'))

out = []


def say(*a):
    t = ' '.join(str(x) for x in a)
    print(t)
    out.append(t)


GENERIC = re.compile(r'^гр\. Варна, район [^,]+(, (ж\.к\.|кв\.|м-ст|местност|с\.о\.|к\.к\.)[^,]*)?'
                     r'(, район No \d+)?$')


def kind_of_addr(addrs):
    if not addrs:
        return 'няма addr изобщо'
    if all(GENERIC.match(a) for a in addrs):
        return 'само район/квартал (без улица и номер)'
    if any(re.search(r'\d', a) for a in addrs):
        return 'улица + номер'
    return 'улица без номер'


say('== А. КАКВО НОСИ КАИС addr НА ПАРЦЕЛА (правило Б ≤45 m) ==')
say(f'  {"клас":24s} {"парцели":>8s}  разбивка по вид addr')
for cls, d in P['plots'].items():
    recs = d['link_45m']
    c = collections.Counter(kind_of_addr(r['addr']) for r in recs)
    say(f'  {cls:24s} {len(recs):8d}  ' +
        ' · '.join(f'{k}={v}' for k, v in c.most_common()))

say('')
say('== Б. ИЗТОЧНИК НА ИМЕТО ЗА КАНДИДАТИТЕ ==')
for cls, cands in C['candidates'].items():
    c = collections.Counter(x['name_src'] for x in cands)
    say(f'  {cls:24s} кандидати={len(cands):4d}  ' +
        ' · '.join(f'{k}={v}' for k, v in c.most_common()))

say('')
say('== В. КАНДИДАТИ, ЧИЕТО ЕДИНСТВЕНО ИМЕ ИДВА ОТ ПОИМЕННО ИЗКЛЮЧЕН OSM POI ==')
n = 0
for cls, cands in C['candidates'].items():
    for x in cands:
        b = x['channels']['b_osm']
        if x['name_src'].startswith('б · ') and b and all(o['excluded'] for o in b):
            n += 1
            say(f'  [{cls}] парцел #{x["plot"]} {x["lat"]},{x["lon"]} '
                f'{x["area_m2"]} m2 → {b[0]["name"]!r} ({b[0]["chip"]}, {b[0]["d_m"]} m)')
            say(f'        защо е изключен: {b[0]["why_excluded"][:150]}')
say(f'  общо: {n}')

say('')
say('== Г. НАЙ-ГОЛЕМИТЕ БЕЗИМЕННИ КАНДИДАТИ (по площ), по клас ==')
for cls, cands in C['candidates'].items():
    noname = sorted((x for x in cands if x['name_src'] == 'без име'),
                    key=lambda x: -x['area_m2'])[:6]
    if not noname:
        continue
    say(f'  --- {cls}')
    for x in noname:
        say(f'      #{x["plot"]:<4d} {x["area_m2"]:9.1f} m2 {x["n_bodies"]:3d} тела '
            f'ет.max={x["floors_max"]:<3d} {x["lat"]},{x["lon"]} {x["reg"]} '
            f'quar={x["quar"]} addr={x["addr"]}')

say('')
say('== Д. КАНДИДАТИ С ИМЕ ОТ РЕГИСТЪР — поименно ==')
for cls in ('детско заведение', 'образование', 'здравно заведение'):
    rows = [x for x in C['candidates'][cls] if x['name_src'].startswith('в')]
    say(f'  --- {cls}: {len(rows)}')
    for x in sorted(rows, key=lambda z: z['reg'][0] if z['reg'] else ''):
        ch = x['channels']
        d = ch['c_reg'][0]['d_m'] if ch['c_reg'] else None
        meth = ch['c_reg'][0]['method'] if ch['c_reg'] else 'улица от addr'
        say(f'      #{x["plot"]:<4d} {x["name"][:50]:52s} d={d} m [{meth}] '
            f'{x["area_m2"]} m2 {x["lat"]},{x["lon"]} {x["reg"]}')

say('')
say('== Е. КАНДИДАТИ С ИМЕ ОТ OSM — поименно (не изключени) ==')
for cls in ('детско заведение', 'образование', 'здравно заведение', 'хотел',
            'курортна/туристическа', 'общежитие', 'социални грижи'):
    rows = [x for x in C['candidates'][cls] if x['name_src'].startswith('б · ')]
    if not rows:
        continue
    say(f'  --- {cls}: {len(rows)}')
    for x in rows:
        b = x['channels']['b_osm'][0]
        say(f'      #{x["plot"]:<4d} {b["name"][:50]:52s} chip={b["chip"]:18s} '
            f'{b["d_m"]} m excl={b["excluded"]} {x["area_m2"]} m2 {x["lat"]},{x["lon"]} {x["reg"]}')

say('')
say('== Ж. ПРАВИЛО А срещу ПРАВИЛО Б — колко тела слепва всяко ==')
for cls, d in P['plots'].items():
    a, b = d['touch_1m'], d['link_45m']
    ma = collections.Counter(len(x['ids']) for x in a)
    mb = collections.Counter(len(x['ids']) for x in b)
    say(f'  {cls:24s} А: {len(a):4d} парцела (макс тела={max(len(x["ids"]) for x in a)}, '
        f'единични={ma[1]})   Б: {len(b):4d} парцела '
        f'(макс тела={max(len(x["ids"]) for x in b)}, единични={mb[1]})')

say('')
say('== З. ДОСТАВЕНИ МЕСТА НА ЧУЖДО ТЯЛО — извадка по клас ==')
W = P['wrong_body']
by = collections.defaultdict(list)
for w in W:
    by[w['kind']].append(w)
for k in sorted(by, key=lambda x: -len(by[x])):
    say(f'  --- {k}: {len(by[k])}')
    for w in by[k][:6]:
        say(f'      {w["name"][:46]:48s} → {w["got"]!r} d={w["d_m"]} m '
            f'{w["lat"]},{w["lon"]} zone={w.get("zone", "")}')

open(os.path.join(HERE, 'extras.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print()
print('written extras.txt')
