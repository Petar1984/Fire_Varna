# -*- coding: utf-8 -*-
"""ЗАДАЧА „парцели“ — ФУНКЦИЯ НА СГРАДАТА → ПАРЦЕЛИ → ДОСТАВЕНИ / КАНДИДАТИ.

READ-ONLY.  Reads only C:/git sources; writes only into this scratch folder.

    set PYTHONIOENCODING=utf-8
    python measure_plots.py

Outputs (same folder):
    func_table.json      37-те func стойности с броя им
    plots_by_func.json   парцелите по клас, по двете правила + „чуждо тяло“
    candidates.json      кандидат-парцелите с трите канала за име
    control_points.json  четирите контролни точки на Петър
    summary.md           докладът
"""
from __future__ import annotations

import json, math, os, pickle, re, sys, collections

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from geolib import (to_xy, bbox, bbox_gap, ring_ring_dist, pt_ring_dist, UF,
                    LAT0, LON0, MX, MY)
from namelib import scan_name, norm_addr
from geocode import Geocoder
from quarters import Quarters

GIT = 'C:/git'
P_INFO = GIT + '/varna_3d/web/varna_buildings_info.json'
P_GEO = GIT + '/varna_3d/web/varna_buildings_3d.geojson'
P_POI = GIT + '/varna_3d/web/varna_poi_names.json'
P_FVP = GIT + '/varna_3d/data/fire_varna_places.json'
P_PLACES = GIT + '/Fire_Varna/data/places.json'
P_HOTELS = GIT + '/Fire_Varna/data/hotels.json'
P_REG = GIT + '/Fire_Varna/scratch/audit_2026-09-03/places_registers.json'
P_MISS = GIT + '/Fire_Varna/scratch/audit_2026-09-03/places_missing.json'

TOUCH_M = 1.0
LINK_M = 45.0
DELIV_M = 30.0
OSM_M = 40.0
REG_M = 150.0
SPREAD_MAX = 300.0     # a geocode averaging rows further apart than this is weak

OUT = []


def say(*a):
    line = ' '.join(str(x) for x in a)
    print(line)
    OUT.append(line)


# ---------------------------------------------------------------- 1. sources
say('== 1. ИЗВОРИ ==')
info = json.load(open(P_INFO, encoding='utf-8'))
ROWS, DICT, COL = info['rows'], info['dict'], info['columns']
say('varna_buildings_info.json rows =', len(ROWS), 'columns =', COL)

CACHE = os.path.join(HERE, '_rings.pkl')
if not os.path.exists(CACHE):
    gj = json.load(open(P_GEO, encoding='utf-8'))
    c = {}
    for f in gj['features']:
        g = f['geometry']
        c[f['properties']['i']] = ([g['coordinates'][0]] if g['type'] == 'Polygon'
                                   else [p[0] for p in g['coordinates']])
    pickle.dump(c, open(CACHE, 'wb'))
RAW = pickle.load(open(CACHE, 'rb'))
say('varna_buildings_3d.geojson polygons =', len(RAW))

XY, BB, CEN = {}, {}, {}
for i, rs in RAW.items():
    r = rs[0]
    pr = [to_xy(p[0], p[1]) for p in r]
    XY[i] = pr
    BB[i] = bbox(pr)
    CEN[i] = (sum(p[0] for p in r) / len(r), sum(p[1] for p in r) / len(r))

IC = {c: k for k, c in enumerate(COL)}


def s(idx, col):
    v = ROWS[idx][IC[col]]
    return DICT[col][v] if v >= 0 else ''


def num(idx, col):
    return ROWS[idx][IC[col]]


def mask_cad(t):
    """Cadastral numbers are private: 10135.xxxx -> 10135.xxxx."""
    return re.sub(r'\b(\d{5})\.[0-9.]+', r'\1.xxxx', t or '')


# ---------------------------------------------------------------- 2. func table
say('')
say('== 2. FUNC — всичките 37 стойности с броя тела ==')
cf = collections.Counter(r[IC['func']] for r in ROWS)
func_table = [{'idx': k, 'func': n, 'n': cf.get(k, 0)} for k, n in enumerate(DICT['func'])]
for f in sorted(func_table, key=lambda x: -x['n']):
    say(f'  {f["n"]:7d}  {f["func"]}')
json.dump(func_table, open(os.path.join(HERE, 'func_table.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- 3. classes
CLASSES = collections.OrderedDict([
    ('детско заведение', {'func': ['Сграда за детско заведение'],
                          'kinds': ['детска градина'], 'src': 'places'}),
    ('образование', {'func': ['Сграда за образование'],
                     'kinds': ['училище', 'университет'], 'src': 'places'}),
    ('здравно заведение', {'func': ['Здравно заведение'],
                           'kinds': ['болница', 'ДКЦ', 'хоспис'], 'src': 'places'}),
    ('хотел', {'func': ['Хотел', 'Апартаментен хотел'], 'kinds': ['*'], 'src': 'hotels'}),
    ('курортна/туристическа', {'func': ['Курортна, туристическа сграда'],
                               'kinds': ['*'], 'src': 'hotels'}),
    ('общежитие', {'func': ['Общежитие'], 'kinds': ['училище', 'университет'],
                   'src': 'places'}),
    ('социални грижи', {'func': ['Заведение за социални грижи'],
                        'kinds': ['хоспис', 'болница'], 'src': 'places'}),
])
FIDX = {n: k for k, n in enumerate(DICT['func'])}
for c in CLASSES.values():
    c['fidx'] = [FIDX[f] for f in c['func']]

say('')
say('== 3. ИЗБРАНИТЕ КЛАСОВЕ ==')
BY_CLASS = {}
for cname, c in CLASSES.items():
    BY_CLASS[cname] = [i for i, r in enumerate(ROWS) if r[IC['func']] in c['fidx']]
    say(f'  {cname:24s} func={c["func"]}  kind={c["kinds"]}  тела={len(BY_CLASS[cname])}')


# ---------------------------------------------------------------- 4. plots
def group(ids, thr):
    uf = UF(len(ids))
    pos = {b: k for k, b in enumerate(ids)}
    cell = max(thr, 20.0) * 2
    grid = collections.defaultdict(list)
    for b in ids:
        x0, y0, x1, y1 = BB[b]
        for gx in range(int((x0 - thr) // cell), int((x1 + thr) // cell) + 1):
            for gy in range(int((y0 - thr) // cell), int((y1 + thr) // cell) + 1):
                grid[(gx, gy)].append(b)
    pairs = set()
    for ci in grid.values():
        n = len(ci)
        for a in range(n):
            for b in range(a + 1, n):
                pairs.add((ci[a], ci[b]) if ci[a] < ci[b] else (ci[b], ci[a]))
    for a, b in pairs:
        if bbox_gap(BB[a], BB[b]) > thr:
            continue
        if ring_ring_dist(XY[a], XY[b], BB[a], BB[b], cutoff=thr) <= thr:
            uf.union(pos[a], pos[b])
    comp = collections.defaultdict(list)
    for b in ids:
        comp[uf.find(pos[b])].append(b)
    return sorted(comp.values(), key=lambda g: min(g))


def plot_record(members):
    addrs = sorted({s(i, 'addr') for i in members if s(i, 'addr')})
    lons = [CEN[i][0] for i in members]
    lats = [CEN[i][1] for i in members]
    xs, ys = [], []
    for i in members:
        b = BB[i]
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    return {
        'ids': sorted(members), 'n_bodies': len(members),
        'reg': sorted({s(i, 'reg') for i in members if s(i, 'reg')}),
        'quar': sorted({s(i, 'quar') for i in members if s(i, 'quar')}),
        'prop': sorted({s(i, 'prop') for i in members if s(i, 'prop')}),
        'addr': addrs,
        'area_m2': round(sum(num(i, 'area_m2') or 0 for i in members), 1),
        'floors_max': max((num(i, 'floors') or 0) for i in members),
        'apps': sum((num(i, 'apps') or 0) for i in members),
        'lat': round(sum(lats) / len(lats), 6), 'lon': round(sum(lons) / len(lons), 6),
        'bbox_wgs84': [round(min(lons), 6), round(min(lats), 6),
                       round(max(lons), 6), round(max(lats), 6)],
        'span_m': [round(max(xs) - min(xs), 1), round(max(ys) - min(ys), 1)],
    }


say('')
say('== 4. ПАРЦЕЛИ — двете правила ==')
say(f'  правило А: допир/разстояние между полигоните ≤ {TOUCH_M:.0f} m (свързани компоненти)')
say(f'  правило Б: single-link ≤ {LINK_M:.0f} m (както предишният измервач)')
PLOTS = {}
for cname, ids in BY_CLASS.items():
    ga, gb = group(ids, TOUCH_M), group(ids, LINK_M)
    PLOTS[cname] = {'touch_1m': [plot_record(g) for g in ga],
                    'link_45m': [plot_record(g) for g in gb]}
    say(f'  {cname:24s} тела={len(ids):5d}  парцели А(≤1 m)={len(ga):5d}  '
        f'парцели Б(≤45 m)={len(gb):5d}')

# ---------------------------------------------------------------- 5. delivery
places = json.load(open(P_PLACES, encoding='utf-8'))['places']
hotels = json.load(open(P_HOTELS, encoding='utf-8'))['hotels']
for p in places:
    p['_xy'] = to_xy(p['lon'], p['lat'])
    p['_src'] = 'places'
for h in hotels:
    h['_xy'] = to_xy(h['lon'], h['lat'])
    h['_src'] = 'hotels'
say('')
say('== 5. ДОСТАВКАТА ==')
say('  places.json =', len(places),
    dict(collections.Counter(p['kind'] for p in places)))
say('  hotels.json =', len(hotels),
    dict(collections.Counter(h.get('kind', '') for h in hotels)))


def plot_pt_dist(rec, xy):
    best = float('inf')
    for i in rec['ids']:
        b = BB[i]
        if bbox_gap(b, (xy[0], xy[1], xy[0], xy[1])) >= best:
            continue
        d = pt_ring_dist(xy, XY[i])
        if d < best:
            best = d
            if best == 0.0:
                break
    return best


def join(cname, rule):
    c = CLASSES[cname]
    pool = places if c['src'] == 'places' else hotels
    if c['kinds'] != ['*']:
        pool = [p for p in pool if p['kind'] in c['kinds']]
    recs = PLOTS[cname][rule]
    for rec in recs:
        rec['delivered'] = []
    for p in pool:
        hits = sorted((plot_pt_dist(rec, p['_xy']), k) for k, rec in enumerate(recs))
        hits = [h for h in hits if h[0] <= DELIV_M]
        if hits:
            recs[hits[0][1]]['delivered'].append(
                {'name': p['name'], 'kind': p.get('kind', ''), 'd_m': round(hits[0][0], 1),
                 'lat': p['lat'], 'lon': p['lon'], 'src': p.get('src', ''),
                 'zone': p.get('zone', '')})
            p.setdefault('_plot', {})[cname] = hits[0][1]
    return pool


POOLS = {}
for cname in CLASSES:
    join(cname, 'touch_1m')
    POOLS[cname] = join(cname, 'link_45m')

# ---------------------------------------------------------------- 6. name channels
poi = json.load(open(P_POI, encoding='utf-8'))
POI_SRC = poi['src']
fvp = json.load(open(P_FVP, encoding='utf-8'))
EXCL = {e['name']: e for e in fvp['_meta']['excluded']}
POI = []
for k, r in enumerate(poi['rows']):
    POI.append({'k': k, 'name': r[0], 'chip': r[1], 'lat': r[2], 'lon': r[3],
                'i': r[4], 'xy': to_xy(r[3], r[2]),
                'src': POI_SRC[k] if k < len(POI_SRC) else '',
                'excluded': r[0] in EXCL,
                'why_excluded': EXCL.get(r[0], {}).get('why', '')})
say('')
say('== 6. ТРИТЕ КАНАЛА ЗА ИМЕ ==')
say('  varna_poi_names.json rows =', len(POI),
    ' от тях поименно изключени (fire_varna_places._meta.excluded) =',
    sum(1 for r in POI if r['excluded']), ' (списъкът е', len(EXCL), 'имена)')

# (a) KAIS-carried names over ALL addr strings
addr_cnt = collections.Counter(r[IC['addr']] for r in ROWS if r[IC['addr']] >= 0)
kais_named, kais_noise = {}, []
for k, txt in enumerate(DICT['addr']):
    hits, noisy = scan_name(txt)
    if not hits:
        continue
    (kais_noise.append((txt, addr_cnt.get(k, 0))) if noisy
     else kais_named.__setitem__(k, hits))
say(f'  (а) КАИС addr: {len(kais_named)} низа носят институционална дума '
    f'(+ {len(kais_noise)} улично-шумни: „Академик…“, „Здравец“, „Ботаническа градина“), '
    f'от общо {len(DICT["addr"])} различни addr низа')
say(f'      тела с такова име: {sum(addr_cnt.get(k, 0) for k in kais_named)} от {len(ROWS)}')
for k, h in sorted(kais_named.items(), key=lambda x: -addr_cnt.get(x[0], 0)):
    say(f'        {addr_cnt.get(k, 0):3d} тела · {DICT["addr"][k]!r} · {h}')

# (c) registers
G = Geocoder()
Q = Quarters()
REG = json.load(open(P_REG, encoding='utf-8'))
REG_CLASS = {'dg_municipal': 'детско заведение', 'nurseries': 'детско заведение',
             'dg_private': 'детско заведение', 'schools': 'образование',
             'cplr': 'образование', 'hospitals': 'здравно заведение',
             'dkc': 'здравно заведение', 'hospices': 'здравно заведение'}
REG_ROWS = []
for grp, lst in REG.items():
    if grp == '_meta':
        continue
    for r in lst:
        g = G.geocode(r.get('address', '') or '')
        rec = {'group': grp, 'cls': REG_CLASS.get(grp, ''), 'name': r.get('name', ''),
               'no': r.get('no'), 'address': r.get('address', ''), 'geo': g}
        if g:
            rec['xy'] = to_xy(g['lon'], g['lat'])
            rec['usable'] = bool(g['strong'] or g['spread_m'] <= SPREAD_MAX)
        else:
            rec['usable'] = False
        # street core of the register address, for the addr-string channel
        a = norm_addr(re.sub(r'\(.*?\)', ' ', r.get('address', '') or ''))
        m = re.match(r'^(?:.*?\b)?(ул|бул|пл|ал)\s+(.+)$', a)
        core = m.group(2) if m else a
        core = re.sub(r'\bбл\s*[0-9].*$|\b[0-9]+\s*[а-я]?\s*$', '', core).strip()
        rec['street_core'] = core
        REG_ROWS.append(rec)
ngc = sum(1 for r in REG_ROWS if r['geo'])
say(f'  (в) регистрови реда: {len(REG_ROWS)}; геокодирани {ngc}; '
    f'годни за мярка (силен метод или разсейване ≤{SPREAD_MAX:.0f} m): '
    f'{sum(1 for r in REG_ROWS if r["usable"])}')
say('      по група: ' + ', '.join(
    f'{g}={sum(1 for r in REG_ROWS if r["group"] == g and r["usable"])}/'
    f'{sum(1 for r in REG_ROWS if r["group"] == g)}'
    for g in dict.fromkeys(r['group'] for r in REG_ROWS)))


def reg_street_match(rec, r):
    """Register street core appears as whole words in one of the plot's KAIS addrs."""
    core = r['street_core']
    if not core or len(core) < 3:
        return False
    toks = [t for t in core.split() if len(t) >= 3]
    if not toks:
        return False
    for a in rec['addr']:
        words = set(norm_addr(a).split())
        if all(t in words for t in toks):
            return True
    return False


def name_for(cname, rec):
    out = {'a_kais': None, 'b_osm': [], 'c_reg': [], 'c_reg_street': [],
           'c_reg_nearest': None}
    for i in rec['ids']:
        k = ROWS[i][IC['addr']]
        if k in kais_named:
            out['a_kais'] = {'i': i, 'addr': DICT['addr'][k], 'hits': kais_named[k]}
            break
    for r in POI:
        d = plot_pt_dist(rec, r['xy'])
        if d <= OSM_M:
            out['b_osm'].append({'name': r['name'], 'chip': r['chip'],
                                 'd_m': round(d, 1), 'excluded': r['excluded'],
                                 'why_excluded': r['why_excluded'], 'src': r['src'],
                                 'poi_row': r['k']})
    out['b_osm'].sort(key=lambda x: x['d_m'])
    best = None
    for r in REG_ROWS:
        if r['cls'] != cname:
            continue
        if reg_street_match(rec, r):
            out['c_reg_street'].append({'name': r['name'], 'no': r['no'],
                                        'group': r['group'], 'address': r['address']})
        if 'xy' not in r:
            continue
        d = plot_pt_dist(rec, r['xy'])
        item = {'name': r['name'], 'no': r['no'], 'group': r['group'],
                'address': r['address'], 'd_m': round(d, 1),
                'method': r['geo']['method'], 'spread_m': r['geo']['spread_m'],
                'usable': r['usable']}
        if best is None or d < best['d_m']:
            best = item
        if d <= REG_M and r['usable']:
            out['c_reg'].append(item)
    out['c_reg'].sort(key=lambda x: x['d_m'])
    out['c_reg_nearest'] = best
    return out


say('')
say('== 7. ДОСТАВЕНИ / КАНДИДАТИ (правило Б, ≤45 m) ==')
CAND = {}
for cname in CLASSES:
    recs = PLOTS[cname]['link_45m']
    cands = []
    for k, rec in enumerate(recs):
        if rec['delivered']:
            continue
        nm = name_for(cname, rec)
        if nm['a_kais']:
            src, name = 'а · КАИС addr', nm['a_kais']['addr']
        elif nm['b_osm']:
            src, name = 'б · OSM POI', nm['b_osm'][0]['name']
        elif nm['c_reg']:
            src, name = 'в · регистър (геокод ≤150 m)', nm['c_reg'][0]['name']
        elif nm['c_reg_street']:
            src, name = 'в2 · регистър (улица от КАИС addr)', nm['c_reg_street'][0]['name']
        else:
            src, name = 'без име', ''
        d = dict(rec)
        d.update({'plot': k, 'name': name, 'name_src': src, 'channels': nm})
        cands.append(d)
    CAND[cname] = cands
    named = sum(1 for c in cands if c['name_src'] != 'без име')
    say(f'  {cname:24s} парцели={len(recs):5d}  доставени={len(recs) - len(cands):4d}  '
        f'кандидати={len(cands):5d}  с име={named:4d}  без име={len(cands) - named:5d}')

# ---------------------------------------------------------------- 8. wrong body
say('')
say('== 8. МЯСТО НА ЧУЖДО ТЯЛО ==')
CELL = 120.0
grid_all = collections.defaultdict(list)
for i in range(len(ROWS)):
    b = BB[i]
    for gx in range(int(b[0] // CELL), int(b[2] // CELL) + 1):
        for gy in range(int(b[1] // CELL), int(b[3] // CELL) + 1):
            grid_all[(gx, gy)].append(i)


def nearest_building(xy, rmax=30.0):
    best = (float('inf'), None)
    for gx in range(int((xy[0] - rmax) // CELL), int((xy[0] + rmax) // CELL) + 1):
        for gy in range(int((xy[1] - rmax) // CELL), int((xy[1] + rmax) // CELL) + 1):
            for i in grid_all.get((gx, gy), ()):
                b = BB[i]
                if not (b[0] - rmax <= xy[0] <= b[2] + rmax
                        and b[1] - rmax <= xy[1] <= b[3] + rmax):
                    continue
                d = pt_ring_dist(xy, XY[i])
                if d < best[0]:
                    best = (d, i)
    return best


KIND2CLASS = {'детска градина': 'детско заведение', 'училище': 'образование',
              'университет': 'образование', 'болница': 'здравно заведение',
              'ДКЦ': 'здравно заведение', 'хоспис': 'здравно заведение'}
HOTEL_OK = ('Хотел', 'Апартаментен хотел', 'Курортна, туристическа сграда')
WRONG = []
for p in places + hotels:
    want = KIND2CLASS.get(p.get('kind', ''), 'хотел' if p['_src'] == 'hotels' else '?')
    d, i = nearest_building(p['_xy'])
    if i is None:
        WRONG.append({'name': p['name'], 'kind': p.get('kind', p['_src']), 'want': want,
                      'got': 'НЯМА СГРАДА ≤30 m', 'd_m': None,
                      'lat': p['lat'], 'lon': p['lon'], 'zone': p.get('zone', '')})
        continue
    got = s(i, 'func')
    ok = (got in HOTEL_OK) if want == 'хотел' else (got in CLASSES.get(want, {}).get('func', []))
    if not ok:
        WRONG.append({'name': p['name'], 'kind': p.get('kind', 'хотел'), 'want': want,
                      'got': got, 'd_m': round(d, 1), 'i': i, 'lat': p['lat'],
                      'lon': p['lon'], 'reg': s(i, 'reg'), 'quar': s(i, 'quar'),
                      'addr': s(i, 'addr'), 'area_m2': num(i, 'area_m2'),
                      'zone': p.get('zone', '')})
say(f'  доставени места/хотели, чието тяло НЕ е от класа (или няма тяло ≤30 m): '
    f'{len(WRONG)} от {len(places) + len(hotels)}')
for (k, g), n in collections.Counter((w['kind'], w['got']) for w in WRONG).most_common(40):
    say(f'    {n:4d}  {k:22s} → {g}')

# ---------------------------------------------------------------- 9. tables
say('')
say('== 9. ТАБЛИЦИ: КЛАС × РАЙОН ==')
BY_REG = {}
for cname in CLASSES:
    recs = PLOTS[cname]['link_45m']
    tab = collections.defaultdict(lambda: [0, 0, 0, 0])
    cmap = {c['plot']: c for c in CAND[cname]}
    for k, rec in enumerate(recs):
        rg = rec['reg'][0] if rec['reg'] else '(без район)'
        t = tab[rg]
        t[0] += 1
        if rec['delivered']:
            t[1] += 1
        elif cmap[k]['name_src'] != 'без име':
            t[2] += 1
        else:
            t[3] += 1
    BY_REG[cname] = {k: list(v) for k, v in tab.items()}
    say(f'  --- {cname}')
    say(f'      {"район":30s} {"парцели":>8s} {"доставени":>10s} {"канд.с име":>11s} {"канд.без име":>13s}')
    for rg in sorted(tab, key=lambda x: -tab[x][0]):
        t = tab[rg]
        say(f'      {rg:30s} {t[0]:8d} {t[1]:10d} {t[2]:11d} {t[3]:13d}')

# ---------------------------------------------------------------- 10. control pts
CP = [('а', 'ул. Шести септември 6', 43.24473, 27.85411, 1191, 'Общинска публична'),
      ('б', 'ж.к. Владислав Варненчик (розовите тела до жълтото училище)',
       43.24456, 27.84592, 203, ''),
      ('в', 'ж.к. „Владислав Валненчик“ (typo в КАИС)', 43.24946, 27.84414, 190, ''),
      ('г', 'ул. Ниш 29', 43.24709, 27.85397, 558, 'Общинска частна')]
say('')
say('== 10. КОНТРОЛНИТЕ ТОЧКИ НА ПЕТЪР ==')
CPOUT = []
for tag, label, la, lo, ar, prop in CP:
    xy = to_xy(lo, la)
    d, i = nearest_building(xy, 40)
    hit = {}
    for rule in ('touch_1m', 'link_45m'):
        for k, rec in enumerate(PLOTS['детско заведение'][rule]):
            if i in rec['ids']:
                hit[rule] = (k, rec)
                break
    k45, rec45 = hit['link_45m']
    nm = name_for('детско заведение', rec45)
    CPOUT.append({'tag': tag, 'label': label, 'lat': la, 'lon': lo,
                  'area_hint_m2': ar, 'prop_hint': prop, 'i': i, 'd_m': round(d, 1),
                  'body_area_m2': num(i, 'area_m2'), 'body_floors': num(i, 'floors'),
                  'body_addr': mask_cad(s(i, 'addr')),
                  'func': s(i, 'func'), 'prop': s(i, 'prop'), 'reg': s(i, 'reg'),
                  'plot_A_1m': hit['touch_1m'][0],
                  'plot_A_bodies': hit['touch_1m'][1]['n_bodies'],
                  'plot_A_area': hit['touch_1m'][1]['area_m2'],
                  'plot_B_45m': k45, 'plot': rec45, 'channels': nm,
                  'delivered': rec45['delivered']})
    say(f'  ({tag}) {label}')
    say(f'      тяло i={i} (d={d:.1f} m от точката) func={s(i, "func")!r} '
        f'prop={s(i, "prop")!r} area={num(i, "area_m2")} m2 етажи={num(i, "floors")}')
    say(f'      парцел А(≤1 m) #{hit["touch_1m"][0]}: {hit["touch_1m"][1]["n_bodies"]} тела, '
        f'{hit["touch_1m"][1]["area_m2"]} m2')
    say(f'      парцел Б(≤45 m) #{k45}: {rec45["n_bodies"]} тела, {rec45["area_m2"]} m2, '
        f'{rec45["reg"]}, quar={rec45["quar"]}, prop={rec45["prop"]}')
    say(f'      КАИС addr: {[mask_cad(a) for a in rec45["addr"]]}')
    say(f'      (а) КАИС-носено име: {nm["a_kais"]}')
    say(f'      (б) OSM POI ≤{OSM_M:.0f} m: {nm["b_osm"][:3] or "НЯМА"}')
    say(f'      (в) регистър ≤{REG_M:.0f} m: '
        f'{[(r["name"], r["d_m"], r["method"]) for r in nm["c_reg"][:4]] or "НЯМА"}')
    say(f'      (в2) регистър по улица от addr: '
        f'{[(r["name"], r["address"]) for r in nm["c_reg_street"][:3]] or "НЯМА"}')
    n0 = nm['c_reg_nearest']
    say(f'      най-близък регистров ред (без праг): '
        f'{(n0["name"], n0["d_m"], n0["method"], "годен" if n0["usable"] else "негоден") if n0 else "НЯМА"}')
    say(f'      доставени места в парцела: {rec45["delivered"] or "НЯМА → кандидат"}')

# ---------------------------------------------------------------- 11. missing regs
say('')
say('== 11. РЕГИСТРОВИ РЕДОВЕ БЕЗ ДОСТАВЕНО МЯСТО → най-близкият кандидат-парцел ==')
MISS = json.load(open(P_MISS, encoding='utf-8'))
missing_names = set()
for k, v in MISS.items():
    if 'ЛИПСВАЩИ' in k:
        for r in v:
            missing_names.add(r.get('name', ''))
say(f'  липсващи по предишния одит (places_missing.json): {len(missing_names)}')
MISSING_LINK = []
for r in REG_ROWS:
    if r['name'] not in missing_names or 'xy' not in r or not r['usable']:
        continue
    cname = r['cls']
    best = None
    for c in CAND.get(cname, []):
        d = plot_pt_dist(c, r['xy'])
        if best is None or d < best[0]:
            best = (d, c)
    if best and best[0] <= REG_M:
        MISSING_LINK.append({'reg_name': r['name'], 'group': r['group'],
                             'address': r['address'], 'cls': cname,
                             'method': r['geo']['method'], 'd_m': round(best[0], 1),
                             'plot': best[1]['plot'], 'lat': best[1]['lat'],
                             'lon': best[1]['lon'], 'area_m2': best[1]['area_m2'],
                             'reg': best[1]['reg'], 'quar': best[1]['quar'],
                             'addr': [mask_cad(a) for a in best[1]['addr']],
                             'n_bodies': best[1]['n_bodies']})
MISSING_LINK.sort(key=lambda x: (x['cls'], x['d_m']))
say(f'  от тях с кандидат-парцел на ≤{REG_M:.0f} m: {len(MISSING_LINK)}')
for m in MISSING_LINK:
    say(f'    {m["cls"]:18s} {m["reg_name"][:52]:54s} d={m["d_m"]:6.1f} m  '
        f'парцел #{m["plot"]} ({m["n_bodies"]} тела, {m["area_m2"]} m2) '
        f'{m["lat"]},{m["lon"]}  {m["reg"]}')

# ---------------------------------------------------------------- 12. write
json.dump({'_meta': {'touch_m': TOUCH_M, 'link_m': LINK_M, 'deliver_m': DELIV_M,
                     'osm_m': OSM_M, 'reg_m': REG_M, 'spread_max_m': SPREAD_MAX,
                     'src': {'info': P_INFO, 'geo': P_GEO, 'places': P_PLACES,
                             'hotels': P_HOTELS, 'poi': P_POI, 'reg': P_REG,
                             'quarters': 'C:/git/Varna_buildings/config/quarter_registry.json'},
                     'projection': f'equirectangular LAT0={LAT0} LON0={LON0} '
                                   f'MX={MX:.1f} m/deg MY={MY:.1f} m/deg'},
           'func_table': func_table,
           'classes': {c: {'func': CLASSES[c]['func'], 'kinds': CLASSES[c]['kinds'],
                           'n_bodies': len(BY_CLASS[c]),
                           'n_plots_touch_1m': len(PLOTS[c]['touch_1m']),
                           'n_plots_link_45m': len(PLOTS[c]['link_45m']),
                           'by_reg': BY_REG[c]} for c in CLASSES},
           'plots': PLOTS,
           'wrong_body': WRONG},
          open(os.path.join(HERE, 'plots_by_func.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

json.dump({'_meta': {'rule': 'link_45m', 'osm_m': OSM_M, 'reg_m': REG_M},
           'registers_geocoded': REG_ROWS,
           'kais_named_addr': {DICT['addr'][k]: {'hits': v, 'n_bodies': addr_cnt.get(k, 0)}
                               for k, v in kais_named.items()},
           'kais_noise_addr': kais_noise,
           'missing_register_to_plot': MISSING_LINK,
           'candidates': CAND},
          open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

json.dump(CPOUT, open(os.path.join(HERE, 'control_points.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
open(os.path.join(HERE, 'run_log.txt'), 'w', encoding='utf-8').write('\n'.join(OUT))
print()
print('written: func_table.json, plots_by_func.json, candidates.json, '
      'control_points.json, run_log.txt')
