# -*- coding: utf-8 -*-
"""Фокус: район Владислав Варненчик — всички парцели от четирите класа,
регистровите редове на района и взаимно-най-близките двойки.

    set PYTHONIOENCODING=utf-8
    python focus_vv.py
"""
import json, os, sys, math, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

P = json.load(open(os.path.join(HERE, 'plots_by_func.json'), encoding='utf-8'))
C = json.load(open(os.path.join(HERE, 'candidates.json'), encoding='utf-8'))
REGROWS = C['registers_geocoded']

TARGET = 'район Владислав Варненчик'
CLASSES = ['детско заведение', 'образование', 'здравно заведение', 'хотел',
           'общежитие', 'социални грижи']


def hav(la1, lo1, la2, lo2):
    return math.hypot((la1 - la2) * 110574, (lo1 - lo2) * 81186)


out = []


def say(*a):
    t = ' '.join(str(x) for x in a)
    print(t)
    out.append(t)


for cls in CLASSES:
    plots = [p for p in P['plots'][cls]['link_45m'] if TARGET in p['reg']]
    cands = {c['plot']: c for c in C['candidates'].get(cls, [])}
    say('')
    say('=' * 78)
    say(f'КЛАС „{cls}“ — {TARGET}: {len(plots)} парцела (правило Б ≤45 m)')
    idx = {id(p): k for k, p in enumerate(P['plots'][cls]['link_45m'])}
    for k, p in enumerate(P['plots'][cls]['link_45m']):
        if TARGET not in p['reg']:
            continue
        st = 'ДОСТАВЕН' if p['delivered'] else 'КАНДИДАТ'
        say(f'  #{k:<4d} {st}  {p["n_bodies"]} тела  {p["area_m2"]:9.1f} m2  '
            f'ет.max={p["floors_max"]}  {p["lat"]},{p["lon"]}  prop={p["prop"]}')
        say(f'        quar={p["quar"]}  addr={p["addr"]}')
        if p['delivered']:
            for d in p['delivered']:
                say(f'        доставено: {d["name"]!r} ({d["kind"]}, {d["d_m"]} m, '
                    f'zone={d.get("zone", "")}, src={d.get("src", "")})')
        else:
            c = cands.get(k)
            if c:
                say(f'        име: {c["name"]!r}  ← {c["name_src"]}')
                ch = c['channels']
                if ch['b_osm']:
                    say(f'        (б) OSM: {[(o["name"], o["d_m"], o["excluded"]) for o in ch["b_osm"][:3]]}')
                if ch['c_reg']:
                    say(f'        (в) регистър ≤150 m: '
                        f'{[(r["name"], r["d_m"], r["method"]) for r in ch["c_reg"][:4]]}')
                if ch['c_reg_street']:
                    say(f'        (в2) по улица: {[r["name"] for r in ch["c_reg_street"][:4]]}')
                n = ch['c_reg_nearest']
                if n:
                    say(f'        най-близък регистров ред: {n["name"]!r} '
                        f'{n["d_m"]} m [{n["method"]}] годен={n["usable"]}')

# mutual nearest for kindergartens in the district
say('')
say('=' * 78)
say('ВЗАИМНО-НАЙ-БЛИЗКИ ДВОЙКИ · детско заведение · целият град')
plots = P['plots']['детско заведение']['link_45m']
regs = [r for r in REGROWS if r['cls'] == 'детско заведение' and r.get('usable')]
# distance plot centroid <-> register point (centroid approximation, reported as such)
D = {}
for ri, r in enumerate(regs):
    for pi, p in enumerate(plots):
        D[(ri, pi)] = hav(r['geo']['lat'], r['geo']['lon'], p['lat'], p['lon'])
best_r = {ri: min(range(len(plots)), key=lambda pi: D[(ri, pi)]) for ri in range(len(regs))}
best_p = {pi: min(range(len(regs)), key=lambda ri: D[(ri, pi)]) for pi in range(len(plots))}
mutual = [(ri, pi) for ri, pi in best_r.items() if best_p[pi] == ri]
say(f'  регистрови реда (годни) = {len(regs)}, парцели = {len(plots)}, '
    f'взаимно-най-близки двойки = {len(mutual)}')
for ri, pi in sorted(mutual, key=lambda x: D[x]):
    r, p = regs[ri], plots[pi]
    st = 'ДОСТАВЕН' if p['delivered'] else 'КАНДИДАТ'
    dn = p['delivered'][0]['name'] if p['delivered'] else ''
    say(f'    {D[(ri, pi)]:7.1f} m  {st:9s} #{pi:<4d} {r["name"][:44]:46s} '
        f'[{r["geo"]["method"]}]  {p["reg"]}  {dn}')

open(os.path.join(HERE, 'focus_vv.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print()
print('written focus_vv.txt')
