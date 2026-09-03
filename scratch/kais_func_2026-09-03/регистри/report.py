# -*- coding: utf-8 -*-
"""Read registry_geocoded.json and print every number that goes into summary.md."""
import json, math, os, statistics, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(HERE + '/registry_geocoded.json', encoding='utf-8'))
KA = json.load(open(HERE + '/kais_cache.json', encoding='utf-8'))
PL = json.load(open('C:/git/Fire_Varna/data/places.json', encoding='utf-8'))['places']
BYNAME = {p['name']: p for p in PL}
GR = ['детски градини (общински)', 'детски ясли', 'детски градини (частни)',
      'училища', 'ЦПЛР', 'болници', 'ДКЦ', 'хосписи']


def dm(a, b):
    Rr = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    h = (math.sin((p2 - p1) / 2) ** 2 +
         math.cos(p1) * math.cos(p2) * math.sin(math.radians(b[1] - a[1]) / 2) ** 2)
    return 2 * Rr * math.asin(math.sqrt(h))


def mask(a):
    """cadastral numbers are private -> 10135.xxxx"""
    import re
    return re.sub(r'\b(\d{4,5})\.\d+(\.\d+)*', r'\1.xxxx', str(a))


print('=' * 78)
print('1. КОЛКО ТОЧЕН Е ГЕОКОДЪТ (проверка срещу доставените пинове със същото име)')
print('=' * 78)
byconf = defaultdict(list)
for lbl in GR:
    for r in R[lbl]:
        g = r['geo']
        if not g.get('ok'):
            continue
        nm = r['delivered_by_name_anywhere']
        if len(nm) != 1:
            continue
        p = BYNAME[nm[0]]
        byconf[g['confidence']].append(dm((g['lat'], g['lon']), (p['lat'], p['lon'])))
tot = [d for v in byconf.values() for d in v]
print('контролни двойки: %d' % len(tot))
for c in sorted(byconf, key=lambda c: -len(byconf[c])):
    v = sorted(byconf[c])
    print('  %-18s n=%3d  медиана %6.0f m  <=60 m %2d  <=150 m %2d' %
          (c, len(v), statistics.median(v), sum(1 for d in v if d <= 60),
           sum(1 for d in v if d <= 150)))

print()
print('=' * 78)
print('2. ТАБЛИЦА ПО КЛАС')
print('=' * 78)
hdr = ('клас', 'реда', 'дост.', 'ЛИПСВА едн.', 'ЛИПСВА спорн', 'без тяло', 'село', 'негеок')
print('%-26s %5s %6s %12s %13s %9s %5s %7s' % hdr)
T = Counter()
detail = {}
for lbl in GR:
    rows = R[lbl]
    delivered = [r for r in rows if r['delivered_status'] != 'НЕ е доставено']
    miss = [r for r in rows if r not in delivered]
    m1 = [r for r in miss if r['verdict'] == 'еднозначно']
    m2 = [r for r in miss if r['verdict'] == 'спорно']
    m0 = [r for r in miss if r['verdict'] == 'без тяло']
    mv = [r for r in miss if 'село' in r['verdict']]
    mn = [r for r in miss if r['verdict'].startswith('адресът')]
    detail[lbl] = dict(delivered=delivered, m1=m1, m2=m2, m0=m0, mv=mv, mn=mn)
    print('%-26s %5d %6d %12d %13d %9d %5d %7d' %
          (lbl, len(rows), len(delivered), len(m1), len(m2), len(m0), len(mv), len(mn)))
    for k, v in (('rows', len(rows)), ('dl', len(delivered)), ('m1', len(m1)),
                 ('m2', len(m2)), ('m0', len(m0)), ('mv', len(mv)), ('mn', len(mn))):
        T[k] += v
print('%-26s %5d %6d %12d %13d %9d %5d %7d' %
      ('ОБЩО', T['rows'], T['dl'], T['m1'], T['m2'], T['m0'], T['mv'], T['mn']))

print()
print('=' * 78)
print('3. ЛИПСВАЩИ РЕГИСТРОВИ РЕДОВЕ С ЕДНОЗНАЧНО КАИС ТЯЛО (поименно)')
print('=' * 78)
for lbl in GR:
    d = detail[lbl]['m1']
    if not d:
        continue
    print('-- %s (%d)' % (lbl, len(d)))
    for r in sorted(d, key=lambda x: (x['no'] or 0)):
        s = r['sites'][0]
        g = r['geo']
        print('  №%-4s %-46s | %s' % (r['no'], r['name'][:46], r['address'][:70]))
        print('        геокод %s (%s) | тяло: %.5f, %.5f  %d тела, %.0f m2, %s ет., %s'
              % (g['confidence'], g['method'][:46], s['lat'], s['lon'], s['n_bodies'],
                 s['area_m2'], s['floors_max'], s['prop']))
        print('        КАИС адрес: %s | район %s | на %.0f m от геокода'
              % (mask(s['addr'])[:70], s['reg'], s['d_m']))

print()
print('=' * 78)
print('4. ЛИПСВАЩИ СЪС СПОРНО ТЯЛО (2+ КАИС места в 150 m)')
print('=' * 78)
for lbl in GR:
    d = detail[lbl]['m2']
    if not d:
        continue
    print('-- %s (%d)' % (lbl, len(d)))
    for r in sorted(d, key=lambda x: (x['no'] or 0)):
        print('  №%-4s %-42s | %s | %d места: %s' %
              (r['no'], r['name'][:42], r['address'][:52], len(r['sites']),
               ', '.join('%.0fm/%.0fm2' % (s['d_m'], s['area_m2']) for s in r['sites'][:4])))

print()
print('=' * 78)
print('5. ЛИПСВАЩИ БЕЗ ТЯЛО / БЕЗ ГЕОКОД')
print('=' * 78)
for lbl in GR:
    for tag, key in (('без тяло', 'm0'), ('негеокодируем', 'mn'), ('село', 'mv')):
        d = detail[lbl][key]
        if not d:
            continue
        print('-- %s · %s (%d)' % (lbl, tag, len(d)))
        for r in sorted(d, key=lambda x: (x['no'] or 0)):
            extra = ''
            nb = r.get('nearest_beyond_150')
            if nb:
                extra = ' | най-близко тяло %.0f m (%d тела, %.0f m2)' % (
                    nb['d_m'], nb['n_bodies'], nb['area_m2'])
            print('  №%-4s %-40s | %s%s' % (r['no'], r['name'][:40], r['address'][:56], extra))

print()
print('=' * 78)
print('6. ОБРАТНО: ДОСТАВЕНИ МЕСТА БЕЗ РЕГИСТРОВ РЕД')
print('=' * 78)
rv = R['ОБРАТНО: доставени места без регистров ред']
for kind, lst in sorted(rv.items(), key=lambda kv: -len(kv[1])):
    print('-- %s (%d)' % (kind, len(lst)))
    for p in sorted(lst, key=lambda x: x['name']):
        s = p.get('kais_site_80m')
        b = ('КАИС място на %.0f m (%d тела, %.0f m2)' % (s['d_m'], s['n_bodies'], s['area_m2'])
             if s else 'НЯМА КАИС тяло от класа в 80 m')
        print('   %-58s src=%-9s %s | %s' % (p['name'][:58], p['src'][:9], p['zone'][:22], b))

print()
print('=' * 78)
print('7. КАИС МЕСТА, КОИТО НИКОЙ НЕ Е ДОСТАВИЛ (целият град, по район)')
print('=' * 78)
gap = R['КАИС места по клас (целият град)']
for cls, lst in gap.items():
    per = defaultdict(lambda: [0, 0])
    for s in lst:
        k = s['reg'] or '(без район)'
        per[k][0] += 1
        if not s['delivered_80m']:
            per[k][1] += 1
    print('-- %s: %d места, без доставено място на <=80 m: %d' %
          (cls, len(lst), sum(v[1] for v in per.values())))
    for k in sorted(per):
        print('     %-28s места %3d  без доставено %3d' % (k, per[k][0], per[k][1]))

print()
print('=' * 78)
print('8. ВЛАДИСЛАВ ВАРНЕНЧИК — ВСИЧКИ КАИС МЕСТА ОТ ТРИТЕ КЛАСА')
print('=' * 78)
for cls, lst in gap.items():
    sel = [s for s in lst if s['reg'] == 'район Владислав Варненчик']
    print('-- %s: %d места' % (cls, len(sel)))
    for s in sorted(sel, key=lambda x: -x['area_m2']):
        d = s['delivered_80m']
        print('   %.5f,%.5f  тела=%d  %7.0f m2  ет.%s  %-22s %-46s | %s' %
              (s['lat'], s['lon'], s['n_bodies'], s['area_m2'], s['floors_max'],
               s['prop'][:22], mask(s['addr'])[:46],
               ('ДОСТАВЕНО: ' + d[0][1] + ' %.0f m' % d[0][0]) if d else 'НЯМА доставено място'))

print()
print('=' * 78)
print('9. КОНТРОЛНИТЕ ТОЧКИ НА ПЕТЪР')
print('=' * 78)
CP = {'а ул. Шести септември 6 (1191 m2)': (43.24473, 27.85411),
      'б ж.к. Вл. Варненчик (203 m2)': (43.24456, 27.84592),
      'в ж.к. Владислав Валненчик (190 m2)': (43.24946, 27.84414),
      'г ул. Ниш 29 (558 m2)': (43.24709, 27.85397)}
rows_all = [(lbl, r) for lbl in GR for r in R[lbl]]
for label, pt in CP.items():
    print('== %s  %.5f,%.5f' % (label, pt[0], pt[1]))
    cand = []
    for lbl, r in rows_all:
        g = r['geo']
        if not g.get('ok'):
            continue
        d = dm(pt, (g['lat'], g['lon']))
        if d <= 400:
            cand.append((d, lbl, r))
    for d, lbl, r in sorted(cand)[:4]:
        print('   %6.0f m  %-26s №%-4s %-40s [%s | %s]' %
              (d, lbl, r['no'], r['name'][:40], r['geo']['confidence'], r['verdict']))
    if not cand:
        print('   няма регистров ред с геокод на <=400 m')


print()
print('=' * 78)
print('10. КАИС МЕСТА БЕЗ ДОСТАВЕНО МЯСТО — с и без регистров ред')
print('=' * 78)
site_rows = defaultdict(list)
CLS = {'детски градини (общински)': 'детско заведение', 'детски ясли': 'детско заведение',
       'детски градини (частни)': 'детско заведение', 'училища': 'образование',
       'ЦПЛР': 'образование', 'болници': 'здравно', 'ДКЦ': 'здравно', 'хосписи': 'здравно'}
for lbl in GR:
    for r in R[lbl]:
        for s in (r.get('sites') or [])[:1]:
            site_rows[(CLS[lbl], s['site_id'])].append(
                (lbl, r['no'], r['name'], r['geo']['confidence'], s['d_m'], r['delivered_status']))
print('%-18s %6s %10s %28s %22s' % ('клас', 'места', 'доставени', 'без дост., но с регистров ред',
                                    'без дост. и без ред'))
for cls, lst in gap.items():
    dl = [s for s in lst if s['delivered_80m']]
    nod = [s for s in lst if not s['delivered_80m']]
    wr = [s for s in nod if (cls, s['site_id']) in site_rows]
    nr = [s for s in nod if (cls, s['site_id']) not in site_rows]
    print('%-18s %6d %10d %28d %22d' % (cls, len(lst), len(dl), len(wr), len(nr)))
print()
print('--- поименно: КАИС места без доставено място, но с регистров ред ---')
for cls in ['детско заведение', 'образование', 'здравно']:
    lst = [s for s in gap[cls] if not s['delivered_80m'] and (cls, s['site_id']) in site_rows]
    print('== %s (%d)' % (cls, len(lst)))
    for s in sorted(lst, key=lambda x: -x['area_m2']):
        print('  %.5f,%.5f %6.0f m2 тела=%d ет.%-2s %-20s %-20s %s' %
              (s['lat'], s['lon'], s['area_m2'], s['n_bodies'], s['floors_max'],
               s['prop'][:20], s['reg'].replace('район ', '')[:20], mask(s['addr'])[:38]))
        for lbl, no, nm, cf, d, ds in site_rows[(cls, s['site_id'])]:
            print('       <- %s №%s %s [геокод %s, %.0f m, %s]' % (lbl, no, nm[:44], cf, d, ds))
print()
print('--- най-големите КАИС места без доставено място И без регистров ред ---')
for cls in ['детско заведение', 'образование', 'здравно']:
    lst = [s for s in gap[cls] if not s['delivered_80m'] and (cls, s['site_id']) not in site_rows]
    print('== %s (%d)' % (cls, len(lst)))
    for s in sorted(lst, key=lambda x: -x['area_m2'])[:12]:
        print('  %.5f,%.5f %6.0f m2 тела=%d ет.%-2s %-20s %-20s %s' %
              (s['lat'], s['lon'], s['area_m2'], s['n_bodies'], s['floors_max'],
               s['prop'][:20], s['reg'].replace('район ', '')[:20], mask(s['addr'])[:40]))


print()
print('=' * 78)
print('11. НЕЗАВИСИМ КАНАЛ: съвпадение по ТЕКСТА на КАИС адресното поле')
print('=' * 78)
import re as _re
src = open(HERE + '/geocode_registers.py', encoding='utf-8').read()
_g = {'__file__': HERE + '/geocode_registers.py', '__name__': '_g'}
exec(compile(src[:src.index('GROUPS = [')], '_g', 'exec'), _g)
_norm, _clean, _var = _g['norm'], _g['clean'], _g['variants']
STOPW = {'гр', 'варна', 'район', 'жк', 'кв', 'ул', 'бул', 'пл', 'площад', 'кк', 'со', 'м',
         'местност', 'бл', 'до', 'ет', 'вх'}


def words(a):
    out = set()
    for v in _var(_clean(a or '')):
        out |= {x for x in _norm(v).split()
                if x not in STOPW and not x.isdigit() and len(x) >= 4}
    return out


hits = 0
for lbl in GR:
    cls = CLS[lbl]
    for r in R[lbl]:
        if r['delivered_status'] != 'НЕ е доставено':
            continue
        rk = words(r['address'])
        if not rk:
            continue
        cands = [(s, sorted(rk & words(s['addr']))) for s in gap[cls]
                 if any(len(w) >= 5 for w in (rk & words(s['addr'])))]
        if len(cands) == 1:
            s, inter = cands[0]
            hits += 1
            print('  %-24s №%-4s %s' % (lbl[:24], r['no'], r['name'][:44]))
            print('      регистър: %s' % r['address'][:74])
            print('      КАИС    : %-40s %.5f,%.5f %d тела %.0f m2 | общи думи %s' %
                  (mask(s['addr'])[:40], s['lat'], s['lon'], s['n_bodies'], s['area_m2'], inter))
print('еднозначни съвпадения по адресен текст:', hits)

print()
print('=' * 78)
print('12. НОСИ ЛИ КАИС ИМЕНА? (адресното поле на телата от трите класа)')
print('=' * 78)
NAMEPAT = _re.compile(r'(ЦДГ|ОДЗ|ОДГ|\bДГ\b|\bДЯ\b|\bОУ\b|\bСУ\b|\bСОУ\b|\bНУ\b|ГИМНАЗИЯ|'
                      r'УЧИЛИЩ|БОЛНИЦ|МБАЛ|ДКЦ|ПОЛИКЛИНИК|ХОСПИС|ДИСПАНСЕР)', _re.I)
tot_b = 0
for cls, fname in (('детско заведение', 'Сграда за детско заведение'),
                   ('образование', 'Сграда за образование'),
                   ('здравно', 'Здравно заведение')):
    z = KA['func_dict'].index(fname)
    idx = [i for i, f in enumerate(KA['func']) if f == z]
    hit = [i for i in idx if NAMEPAT.search(KA['addr'][i] or '')]
    tot_b += len(idx)
    print('  %-18s тела %3d | адресно поле с име на заведение: %d %s' %
          (cls, len(idx), len(hit), [mask(KA['addr'][i]) for i in hit]))
print('  ОБЩО тела в трите класа:', tot_b)
