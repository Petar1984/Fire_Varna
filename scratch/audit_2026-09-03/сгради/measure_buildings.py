# -*- coding: utf-8 -*-
"""
ODIT "SGRADI" — 2026-09-03. READ-ONLY izmervach.
HEAD Fire_Varna: 6460961 -> fd2c315 (index.html i data/ sa BAIT-IDENTICHNI mezhdu
            dvata; K2-komitat piptva samo tests/) | varna_3d: b89ac97 | Varna_buildings: 4c6b482

Chast 1  fizicheski dubleti (ADR-038 sidecar -> geocoder -> dostavka -> meniu)
Chast 2  geometrichni dubleti v varna_buildings_3d.geojson
Chast 3  pokritie s adres po raion / kvartal / funkciia
Chast 4  KAIS sgradi bez nito edin red v dostavkata (prostranstven join + adresen kliuch)

Pusk:  PYTHONIOENCODING=utf-8 python measure_buildings.py
Izhod: dup_physical.json  dup_geometry.json  coverage_by_region.json
       missing_from_delivery.json  measure_buildings.out.txt
Nishto ne se pishe v C:/git.
"""
import json, sys, os, re, math, hashlib, collections

sys.stdout.reconfigure(encoding='utf-8')
OUT = open("measure_buildings.out.txt", "w", encoding='utf-8')
def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s); OUT.write(s + "\n")

VB = r"C:/git/Varna_buildings/output/"
V3 = r"C:/git/varna_3d/web/"
FV = r"C:/git/Fire_Varna/data/"

SC   = json.load(open(VB + "physical_building_sidecar.json", encoding='utf-8'))
GEO  = json.load(open(VB + "geocoder_index.json", encoding='utf-8'))
DEL  = json.load(open(FV + "search_index.json", encoding='utf-8'))
AR   = json.load(open(FV + "address_rows.json", encoding='utf-8'))
GJ   = json.load(open(V3 + "varna_buildings_3d.geojson", encoding='utf-8'))
INFO = json.load(open(V3 + "varna_buildings_info.json", encoding='utf-8'))

F = GJ['features']
CI = {c: i for i, c in enumerate(INFO['columns'])}; DCT = INFO['dict']; IROWS = INFO['rows']
def val(j, c):
    x = IROWS[j][CI[c]]
    return (None if x == -1 else DCT[c][x]) if c in DCT else x

LAT0 = 43.21; MY = 110540.0; MX = 111320.0 * math.cos(math.radians(LAT0))
def toxy(lng, lat): return ((lng - 27.9) * MX, (lat - LAT0) * MY)
def tolnglat(x, y): return (round(x / MX + 27.9, 6), round(y / MY + LAT0, 6))
def hav(a, b, c, d):
    R = 6371000.0; p = math.pi / 180
    z = math.sin((c - a) * p / 2) ** 2 + math.cos(a * p) * math.cos(c * p) * math.sin((d - b) * p / 2) ** 2
    return 2 * R * math.asin(math.sqrt(z))

# =====================================================================
# replika na index.html @ HEAD 6460961:
#   norm 4839 · skel 4840 · baseAddressLabel 4878 · formatAddressHit 4890
#   labelBlockNumber 5079 · dedupeDisplayRows 5085-5110 · SEARCH_LIMIT 5122
# =====================================================================
SEARCH_LIMIT = 8
CMAP = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k',
        'л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
        'ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
PUNCT = re.compile("[.\u2116,'\"\\-]")
def norm(s):
    s = ('' if s is None else str(s)).lower().replace('\u0431\u043b\u043e\u043a', '\u0431\u043b').replace('\u0432\u0445\u043e\u0434', '\u0432\u0445')
    return re.sub(r'\s+', ' ', PUNCT.sub(' ', s)).strip()
def skel(w):
    o = ''.join(CMAP.get(ch, ch) for ch in w.lower())
    return re.sub(r'(\D)\1+', r'\1', re.sub(r'[yj]', 'i', o))
DN = DEL['district_names']; ROWS = AR['rows']; NAI = AR['field_order'].index('normalized_address')
def prettyKey(s): return re.sub(r'\s+', ' ', str(s).replace('|', ' ')).strip()
def baseAddressLabel(h):
    if h.get('label'): return prettyKey(h['label'])
    di = h.get('display_id')
    if di is not None and 0 <= di < len(ROWS) and ROWS[di][NAI]: return ROWS[di][NAI]
    d = h.get('d')
    if d is not None and d < len(DN): return DN[d]
    return '(\u0430\u0434\u0440\u0435\u0441)'
def formatAddressHit(h):
    b = baseAddressLabel(h)
    return b + ' \u00b7 \u0432\u0445. ' + str(h['en']) if (h.get('kind') == 'mf' and h.get('en') is not None) else b
def labelBlockNumber(label):
    toks = [skel(t) for t in norm(label).split(' ') if t]
    if 'bl' not in toks: return None
    i = toks.index('bl'); nx = toks[i + 1] if i + 1 < len(toks) else None
    return nx if (nx and re.search(r'[0-9]', nx)) else None
def dedupeDisplayRows(rows):
    if not rows: return rows
    labels = [str(formatAddressHit(r)) for r in rows]
    sgrada = set()
    for i, r in enumerate(rows):
        if r.get('kind') == 'mf' and r.get('en') is None:
            bn = labelBlockNumber(labels[i])
            if bn is not None: sgrada.add(bn)
    seen = set(); out = []
    for i, r in enumerate(rows):
        if r.get('kind') == 'address':
            bn = labelBlockNumber(labels[i])
            if bn is not None and bn in sgrada: continue
        key = norm(labels[i]) + '||' + (str(r['g']) if r.get('g') is not None else '')
        if key in seen: continue
        seen.add(key); out.append(r)
    return out

def mask(cad):
    """kadastralnite nomera sa CHASTNI -> maska za publichniia izhod."""
    return "10135.xxxx" if cad else None

# =====================================================================
# CHAST 1 — FIZICHESKI DUBLETI
# =====================================================================
P("=" * 78)
P("CHAST 1 — FIZICHESKI DUBLETI (ADR-038)")
P("=" * 78)
c2p = SC['cadnum_to_physical_building_id']
grp = collections.defaultdict(list)
for c, p in c2p.items(): grp[p].append(c)
sizes = collections.Counter(len(v) for v in grp.values())
P("sidecar _schema:", SC['_schema'])
P("sidecar stats  :", json.dumps(SC['stats'], ensure_ascii=False, sort_keys=True))
P("  sekcii v sidecara:", len(c2p), "| fizicheski sgradi:", len(grp),
  "| sgavaemi redove:", len(c2p) - len(grp))
P("  razmer na grupite:", dict(sorted(sizes.items())))
P("  pravilo:", SC['rule'][:150])

ge = GEO['entries']
has = [e for e in ge if e.get('physical_building_id') is not None]
bypb = collections.defaultdict(list)
for e in has: bypb[e['physical_building_id']].append(e)
P("")
P("GEOKODER geocoder_index.json: zapisi", len(ge), "| s physical_building_id", len(has),
  "| grupi", len(bypb), "| physical_building_reps", len(GEO.get('physical_building_reps') or {}))
P("  cadnum(geokoder) == cadnum(sidecar):", set(e['cadnum'] for e in has) == set(c2p.keys()))

de = DEL['entries']
def k(e): return (e.get('kind'), e['pin'][0], e['pin'][1], e.get('en'), tuple(e.get('tk') or ()))
dmap = collections.defaultdict(list)
for i, e in enumerate(de): dmap[k(e)].append(i)
P("")
P("DOSTAVKA Fire_Varna/data/search_index.json: zapisi", len(de),
  "| s physical_building_id", sum(1 for e in de if 'physical_building_id' in e),
  "| s life_safety_rank", sum(1 for e in de if 'life_safety_rank' in e))
P("  ot 483-te geokoderski zapisa s pbid — namereni v dostavkata:",
  sum(1 for e in has if dmap.get(k(e))))

res = []; folded = 0; hist = collections.Counter(); kindc = collections.Counter()
for pb, es in bypb.items():
    drows = []
    for e in es:
        idxs = dmap.get(k(e), [])
        if idxs: drows.append(de[idxs[0]])
    for r in drows: kindc[r.get('kind')] += 1
    out = dedupeDisplayRows(drows)
    hist[len(out)] += 1
    if len(out) == 1: folded += 1
    pins = [tuple(r['pin']) for r in drows]
    ext = 0.0
    for i in range(len(pins)):
        for j2 in range(i + 1, len(pins)):
            ext = max(ext, hav(pins[i][0], pins[i][1], pins[j2][0], pins[j2][1]))
    res.append({"pbid_masked": mask(pb), "sections": len(es), "delivery_rows": len(drows),
                "rows_after_dedupe": len(out), "visible_in_menu": min(len(out), SEARCH_LIMIT),
                "labels": sorted(set(formatAddressHit(r) for r in drows)),
                "kinds": sorted(set(r.get('kind') for r in drows)),
                "extent_m": round(ext), "pins": [list(p) for p in pins],
                "_pbid_private": pb, "_cadnums_private": sorted(x['cadnum'] for x in es)})
res.sort(key=lambda r: (-r['rows_after_dedupe'], -r['sections']))
P("")
P("MENIUTO (dedupeDisplayRows, index.html:5085-5110 @ fd2c315):")
P("  grupi:", len(res), "| svivat se do 1 red:", folded, "| ostavat >1 red:", len(res) - folded)
P("  hist. redove sled dedupe:", dict(sorted(hist.items())))
P("  vid na dostavenite redove:", dict(kindc))
P("  483 dostaveni redove -> ", sum(r['rows_after_dedupe'] for r in res), "sled dedupe;",
  "IZLISHNI:", sum(r['rows_after_dedupe'] for r in res) - len(res))
same_lbl = [r for r in res if r['rows_after_dedupe'] > 1 and len(r['labels']) == 1]
P("  grupi, koito pokazvat 2+ NAPALNO IDENTICHNI reda (edin i sasht tekst):", len(same_lbl))
P("  prostranstven obhvat na grupite: max", max(r['extent_m'] for r in res), "m | >50 m:",
  sum(1 for r in res if r['extent_m'] > 50), "| >100 m:", sum(1 for r in res if r['extent_m'] > 100))
P("")
P("  PRIMERI (kadastralnite nomera maskirani):")
for r in (same_lbl[:3] + [x for x in res if len(x['labels']) > 1][:3]):
    P("   sekcii=%2d dostaveni=%2d dedupe=%d obhvat=%3dm | %s | pin=%s" %
      (r['sections'], r['delivery_rows'], r['rows_after_dedupe'], r['extent_m'],
       (' / '.join(r['labels']))[:62], r['pins'][0]))
json.dump({"head_fire_varna": "6460961", "sidecar_stats": SC['stats'], "sidecar_rule": SC['rule'],
           "sidecar_sections": len(c2p), "sidecar_physical_buildings": len(grp),
           "collapsible_rows": len(c2p) - len(grp),
           "group_size_hist": {str(a): b for a, b in sorted(sizes.items())},
           "geocoder_entries": len(ge), "geocoder_with_pbid": len(has), "geocoder_groups": len(bypb),
           "geocoder_reps": len(GEO.get('physical_building_reps') or {}),
           "delivery_entries": len(de), "delivery_with_pbid": 0,
           "delivery_rows_for_the_483": sum(r['delivery_rows'] for r in res),
           "delivery_row_kinds": dict(kindc),
           "menu_groups_folding_to_one": folded, "menu_groups_still_multi": len(res) - folded,
           "menu_rows_after_dedupe": sum(r['rows_after_dedupe'] for r in res),
           "menu_surplus_rows": sum(r['rows_after_dedupe'] for r in res) - len(res),
           "menu_groups_identical_text": len(same_lbl),
           "survive_hist": {str(a): b for a, b in sorted(hist.items())},
           "groups": res},
          open("dup_physical.json", "w", encoding='utf-8'), ensure_ascii=False, indent=1)
P("-> dup_physical.json")

# =====================================================================
# CHAST 2 — GEOMETRICHNI DUBLETI
# =====================================================================
P("")
P("=" * 78)
P("CHAST 2 — GEOMETRICHNI DUBLETI v varna_buildings_3d.geojson")
P("=" * 78)
P("features:", len(F), "| info rows:", len(IROWS),
  "| properties.i == index:", all(F[j]['properties'].get('i') == j for j in range(len(F))))
h_full = collections.defaultdict(list); h_out = collections.defaultdict(list)
for j, f in enumerate(F):
    c = f['geometry']['coordinates']
    h_full[hashlib.sha1(json.dumps(c, separators=(',', ':')).encode()).hexdigest()].append(j)
    h_out[hashlib.sha1(json.dumps(c[0], separators=(',', ':')).encode()).hexdigest()].append(j)
dup_full = {a: b for a, b in h_full.items() if len(b) > 1}
dup_out = {a: b for a, b in h_out.items() if len(b) > 1}
P("A. BAIT-IDENTICHNI prasteni (cialata geometriia):", len(dup_full), "grupi /",
  sum(len(v) for v in dup_full.values()), "poligona")
P("A'. bait-identichen samo vanshen prasten:", len(dup_out), "grupi /",
  sum(len(v) for v in dup_out.values()), "poligona")

cx = [0.0] * len(F); cy = [0.0] * len(F); ar = [0.0] * len(F); bb = [None] * len(F); XY = [None] * len(F)
for j, f in enumerate(F):
    pts = [toxy(p[0], p[1]) for p in f['geometry']['coordinates'][0]]
    if len(pts) > 1 and pts[0] == pts[-1]: pts = pts[:-1]
    XY[j] = pts; n = len(pts); A2 = sx = sy = 0.0
    for i in range(n):
        x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % n]
        cr = x1 * y2 - x2 * y1; A2 += cr; sx += (x1 + x2) * cr; sy += (y1 + y2) * cr
    if abs(A2) < 1e-9:
        cx[j] = sum(p[0] for p in pts) / n; cy[j] = sum(p[1] for p in pts) / n; ar[j] = 0.0
    else:
        ar[j] = abs(A2) / 2.0; cx[j] = sx / (3 * A2); cy[j] = sy / (3 * A2)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    bb[j] = (min(xs), min(ys), max(xs), max(ys))

parent = list(range(len(F)))
def find(a):
    while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
    return a
CELL_C = 6.0   # >5 m => dvoika na <=5 m vinagi e v sasedna kletka (+-1)
cell = collections.defaultdict(list)
for j in range(len(F)): cell[(int(math.floor(cx[j] / CELL_C)), int(math.floor(cy[j] / CELL_C)))].append(j)
loose = collections.Counter(); loose_ex = collections.defaultdict(list); npairs = 0
for (gx, gy), ids in cell.items():
    cand = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1): cand.extend(cell.get((gx + dx, gy + dy), ()))
    for a in ids:
        for b in cand:
            if b <= a: continue
            d2 = (cx[a] - cx[b]) ** 2 + (cy[a] - cy[b]) ** 2
            if d2 > 25.0: continue
            ma = max(ar[a], ar[b])
            if ma <= 0: continue
            rel = abs(ar[a] - ar[b]) / ma; d = math.sqrt(d2)
            for dl, dm in (("<=1m", 1.0), ("<=3m", 3.0), ("<=5m", 5.0)):
                if d <= dm:
                    for al, am in (("area+-5%", .05), ("area+-20%", .20), ("area any", 9.9)):
                        if rel <= am:
                            key = dl + " & " + al; loose[key] += 1
                            if len(loose_ex[key]) < 12: loose_ex[key].append([a, b, round(d, 2), round(rel, 3)])
                    break
            if d <= 1.0 and rel <= 0.05:
                ra, rb = find(a), find(b)
                if ra != rb: parent[max(ra, rb)] = min(ra, rb)
                npairs += 1
gmap = collections.defaultdict(list)
for j in range(len(F)): gmap[find(j)].append(j)
near = {a: b for a, b in gmap.items() if len(b) > 1}
P("")
P("B. centroid <=1 m I ploshch +-5 %:", len(near), "grupi /", sum(len(v) for v in near.values()),
  "poligona (dvoiki:", npairs, ")")
P("   po-hlabavi pragove (kontrola):")
for key in ["<=1m & area+-5%", "<=1m & area any", "<=3m & area+-5%", "<=3m & area any",
            "<=5m & area+-5%", "<=5m & area any"]:
    P("     %-18s %6d" % (key, loose.get(key, 0)))

CELL2 = 60.0
gidx = collections.defaultdict(list)
for j in range(len(F)):
    x0, y0, x1, y1 = bb[j]
    for gx in range(int(math.floor(x0 / CELL2)), int(math.floor(x1 / CELL2)) + 1):
        for gy in range(int(math.floor(y0 / CELL2)), int(math.floor(y1 / CELL2)) + 1):
            gidx[(gx, gy)].append(j)
def inside(pt, poly):
    x, y = pt; n = len(poly); c = False; px, py = poly[n - 1]
    for i in range(n):
        qx, qy = poly[i]
        if ((qy > y) != (py > y)) and (x < (px - qx) * (y - qy) / (py - qy) + qx): c = not c
        px, py = qx, qy
    return c
contained = []; cand_n = 0
for b in range(len(F)):
    if ar[b] <= 0: continue
    gx = int(math.floor(cx[b] / CELL2)); gy = int(math.floor(cy[b] / CELL2)); seen = set()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for a in gidx.get((gx + dx, gy + dy), ()):
                if a == b or a in seen: continue
                seen.add(a)
                if ar[a] <= ar[b]: continue
                ax0, ay0, ax1, ay1 = bb[a]; bx0, by0, bx1, by1 = bb[b]
                if not (ax0 <= bx0 + 1e-9 and ay0 <= by0 + 1e-9 and ax1 >= bx1 - 1e-9 and ay1 >= by1 - 1e-9):
                    continue
                cand_n += 1
                if all(inside(p, XY[a]) for p in XY[b]): contained.append((b, a))
same_addr = [(b, a) for b, a in contained if val(b, 'addr') is not None and val(b, 'addr') == val(a, 'addr')]
P("")
P("C. poligon IZAALO vatre v drug:", len(contained), "dvoiki (bbox-kandidati", cand_n, ")")
P("   ot tiah sas SASHTIA adresen niz:", len(same_addr))
def desc(j):
    return {"i": j, "addr": val(j, 'addr'), "street": val(j, 'street'), "num": val(j, 'num'),
            "func": val(j, 'func'), "reg": val(j, 'reg'), "quar": val(j, 'quar'),
            "floors": val(j, 'floors'), "apps": val(j, 'apps'),
            "area_m2_info": val(j, 'area_m2'), "area_m2_geom": round(ar[j], 1),
            "centroid": list(tolnglat(cx[j], cy[j]))}
P("")
P("   PRIMERI B:")
for v in sorted(near.values(), key=lambda v: -len(v)):
    d = [desc(j) for j in v]
    P("     i=%s | %s | %s | %s | ploshch %s m2 | %s" %
      ([x['i'] for x in d], (d[0]['addr'] or '')[:34], (d[0]['func'] or '')[:26], d[0]['reg'],
       [x['area_m2_geom'] for x in d], d[0]['centroid']))
P("   PRIMERI C:")
for b, a in contained:
    P("     vatre i=%d (%.0f m2, %s) v i=%d (%.0f m2, %s) | %s | %s" %
      (b, ar[b], (val(b, 'func') or '')[:18], a, ar[a], (val(a, 'func') or '')[:18],
       (val(b, 'addr') or '')[:34], desc(b)['centroid']))
P("   PRIMERI <=1m & proizvolna ploshch (7 dvoiki — vgnezdeni pristroiki, NE dubleti):")
for a, b, d, rel in loose_ex.get("<=1m & area any", []):
    P("     i=%d/%d d=%s m dA=%s | %s | %s / %s m2 | %s" %
      (a, b, d, rel, (val(a, 'addr') or '')[:32], val(a, 'area_m2'), val(b, 'area_m2'), desc(a)['centroid']))
# --- D. TAVAN: sekcii, koito FIZICHESKI se dopirat (spodelen TOCHEN vrah) I nosiat
#     edin i sasht adresen niz (ulica+nomer). Tova e gorniiat predel na tova, koeto
#     edno slivane "sekcii -> fizicheska sgrada" bi moglo da svie. Sravni s 483/198.
vtx = collections.defaultdict(set)
for j in range(len(F)):
    for p in F[j]['geometry']['coordinates'][0]:
        vtx[(p[0], p[1])].add(j)
par2 = list(range(len(F)))
def f2(a):
    while par2[a] != a: par2[a] = par2[par2[a]]; a = par2[a]
    return a
touch_pairs = 0
for ids in vtx.values():
    if len(ids) < 2: continue
    ids = sorted(ids)
    for x in range(len(ids)):
        for y in range(x + 1, len(ids)):
            a, b2 = ids[x], ids[y]
            sa, na = val(a, 'street'), val(a, 'num')
            if not (sa and na): continue
            if val(b2, 'street') != sa or val(b2, 'num') != na: continue
            ra, rb = f2(a), f2(b2)
            if ra != rb: par2[max(ra, rb)] = min(ra, rb); touch_pairs += 1
gm2 = collections.defaultdict(list)
for j in range(len(F)): gm2[f2(j)].append(j)
touch = {a: b2 for a, b2 in gm2.items() if len(b2) > 1}
tsz = collections.Counter(len(v) for v in touch.values())
P("")
P("D. TAVAN — sekcii, dopirashti se po TOCHEN spodelen vrah I sas SASHTIA ulica+nomer:")
P("   grupi:", len(touch), "| sekcii v tiah:", sum(len(v) for v in touch.values()),
  "| sgavaemi redove:", sum(len(v) for v in touch.values()) - len(touch))
P("   razmeri:", dict(sorted(tsz.items())))
P("   za sravnenie sidecar ADR-038: 483 sekcii / 198 sgradi / 285 sgavaemi redove")
def eff_mf(j):
    """'effective-MF' po pravilото na sidecara: functype-MF ILI ednofam/vilna s apps>=5."""
    fn = val(j, 'func') or ''
    if fn.startswith('Жилищна сграда - много'): return True
    if fn.startswith('Жилищна сграда - едно') or fn.startswith('Вилна сграда'):
        return (val(j, 'apps') or 0) >= 5
    return False
mf_touch = sum(1 for v in touch.values() if any(eff_mf(j) for j in v))
mf2_touch = [v for v in touch.values() if sum(1 for j in v if eff_mf(j)) >= 2]
P("   ot tiah grupi s pone EDNA effective-MF sekciia:", mf_touch)
P("   grupi s >=2 effective-MF sekcii (sashtata populaciia, kakto sidecara):",
  len(mf2_touch), "| sekcii:", sum(len(v) for v in mf2_touch),
  "| sgavaemi:", sum(len(v) for v in mf2_touch) - len(mf2_touch))
P("   sidecarat pokriva 198 ot tiah -> nepokriti kandidati:", len(mf2_touch) - 198)
P("   PRIMERI D (nai-golemite):")
for v in sorted(touch.values(), key=lambda v: -len(v))[:6]:
    d0 = desc(v[0])
    P("     %2d sekcii | %s %s | %s | %s | i=%s | %s" %
      (len(v), (d0['street'] or '')[:28], d0['num'], (d0['func'] or '')[:22], d0['reg'],
       v[:6], d0['centroid']))

json.dump({"features": len(F),
           "D_touching_same_addr_groups": len(touch),
           "D_touching_sections": sum(len(v) for v in touch.values()),
           "D_collapsible_rows": sum(len(v) for v in touch.values()) - len(touch),
           "D_size_hist": {str(a): b2 for a, b2 in sorted(tsz.items())},
           "D_groups_with_effmf": mf_touch,
           "D_groups_with_2plus_effmf": len(mf2_touch),
           "D_groups_with_2plus_effmf_sections": sum(len(v) for v in mf2_touch),
           "D_examples_2plus_effmf": [[desc(j) for j in v] for v in sorted(mf2_touch, key=lambda v: -len(v))[:40]],
           "D_examples": [[desc(j) for j in v] for v in sorted(touch.values(), key=lambda v: -len(v))[:40]],
           "A_identical_geometry_groups": len(dup_full),
           "A_identical_geometry_features": sum(len(v) for v in dup_full.values()),
           "A_identical_outer_ring_groups": len(dup_out),
           "A_examples": [[desc(j) for j in v] for v in dup_full.values()],
           "B_centroid1m_area5pct_groups": len(near),
           "B_features": sum(len(v) for v in near.values()),
           "B_examples": [[desc(j) for j in v] for v in sorted(near.values(), key=lambda v: -len(v))],
           "B_loose_thresholds": dict(loose),
           "B_loose_examples": {a: b for a, b in loose_ex.items()},
           "C_contained_pairs": len(contained), "C_contained_same_addr": len(same_addr),
           "C_examples": [{"inner": desc(b), "outer": desc(a)} for b, a in contained]},
          open("dup_geometry.json", "w", encoding='utf-8'), ensure_ascii=False, indent=1)
P("-> dup_geometry.json")

# =====================================================================
# CHAST 3 — POKRITIE S ADRES
# =====================================================================
P("")
P("=" * 78)
P("CHAST 3 — POKRITIE S ADRES PO RAION / KVARTAL / FUNKCIIA")
P("=" * 78)
def blank(): return {"buildings": 0, "with_addr": 0, "with_street": 0, "with_num": 0,
                     "street_and_num": 0, "addr_is_stub": 0, "no_addr": 0}
by_reg = collections.defaultdict(blank); by_quar = collections.defaultdict(blank)
by_func = collections.defaultdict(blank); tot = blank()
for j in range(len(IROWS)):
    reg = val(j, 'reg') or "(\u0431\u0435\u0437 \u0440\u0430\u0439\u043e\u043d)"
    qr = val(j, 'quar') or "(\u0431\u0435\u0437 \u043a\u0432\u0430\u0440\u0442\u0430\u043b)"
    fn = val(j, 'func') or "(\u0431\u0435\u0437 \u0444\u0443\u043d\u043a\u0446\u0438\u044f)"
    a = val(j, 'addr'); s = val(j, 'street'); n = val(j, 'num')
    for d in (by_reg[reg], by_quar[qr], by_func[fn], tot):
        d["buildings"] += 1
        if a: d["with_addr"] += 1
        else: d["no_addr"] += 1
        if s: d["with_street"] += 1
        if n: d["with_num"] += 1
        if s and n: d["street_and_num"] += 1
        if a and not s and not n: d["addr_is_stub"] += 1
def pct(a, b): return (100.0 * a / b) if b else 0.0
def tbl(title, items, limit=None):
    P("")
    P("== " + title + " ==")
    P("%-46s %7s %7s %6s %7s %6s %7s %6s %8s" %
      ("", "sgradi", "adres", "%", "ulica", "%", "nomer", "%", "ul+nom%"))
    rr = sorted(items, key=lambda kv: -kv[1]['buildings'])
    if limit: rr = rr[:limit]
    for nm, d in rr:
        b = d['buildings']
        P("%-46s %7d %7d %5.1f%% %7d %5.1f%% %7d %5.1f%% %7.1f%%" %
          (str(nm)[:46], b, d['with_addr'], pct(d['with_addr'], b), d['with_street'],
           pct(d['with_street'], b), d['with_num'], pct(d['with_num'], b),
           pct(d['street_and_num'], b)))
    return rr
tbl("POKRITIE PO RAION", list(by_reg.items()))
b = tot['buildings']
P("%-46s %7d %7d %5.1f%% %7d %5.1f%% %7d %5.1f%% %7.1f%%" %
  ("OBSHTO", b, tot['with_addr'], pct(tot['with_addr'], b), tot['with_street'],
   pct(tot['with_street'], b), tot['with_num'], pct(tot['with_num'], b), pct(tot['street_and_num'], b)))
P("  ot tiah addr = SAMO raion/kvartal (bez ulica i bez nomer):", tot['addr_is_stub'],
  "(%.1f%%)" % pct(tot['addr_is_stub'], b), "| izobshto bez addr:", tot['no_addr'])
q30 = tbl("POKRITIE PO KVARTAL — TOP 30 po broi sgradi", list(by_quar.items()), 30)
f5 = tbl("POKRITIE PO FUNKCIIA — TOP 5", list(by_func.items()), 5)
worst = sorted([kv for kv in by_quar.items() if kv[1]['buildings'] >= 300],
               key=lambda kv: pct(kv[1]['street_and_num'], kv[1]['buildings']))[:10]
P("")
P("== TOP 10 kvartala s nai-nisko ul+nomer (>=300 sgradi) ==")
for nm, d in worst:
    P("  %-44s %6d sgradi | ul+nom %5.1f%%" % (str(nm)[:44], d['buildings'],
      pct(d['street_and_num'], d['buildings'])))
json.dump({"total": tot, "by_region": dict(by_reg),
           "by_quarter_top30": {str(a): b2 for a, b2 in q30},
           "by_quarter_all": {str(a): b2 for a, b2 in by_quar.items()},
           "by_func_top5": {str(a): b2 for a, b2 in f5},
           "by_func_all": {str(a): b2 for a, b2 in by_func.items()},
           "worst_quarters_ge300": [{"quar": a, **b2} for a, b2 in worst]},
          open("coverage_by_region.json", "w", encoding='utf-8'), ensure_ascii=False, indent=1)
P("-> coverage_by_region.json")

# =====================================================================
# CHAST 4 — SGRADI BEZ RED V DOSTAVKATA
# =====================================================================
P("")
P("=" * 78)
P("CHAST 4 — KAIS SGRADI BEZ NITO EDIN RED V DOSTAVKATA")
P("=" * 78)
pins = [toxy(e['pin'][1], e['pin'][0]) for e in de]
apins = [toxy(r[2], r[1]) for r in ROWS]
CELL3 = 25.0
def grid(pts):
    g = collections.defaultdict(list)
    for kk, (x, y) in enumerate(pts): g[(int(math.floor(x / CELL3)), int(math.floor(y / CELL3)))].append(kk)
    return g
G1 = grid(pins); G2 = grid(apins)
P("sgradi:", len(F), "| pinove v search_index.json:", len(pins), "| redove v address_rows.json:", len(apins))
inside_cnt = [0] * len(F); ainside_cnt = [0] * len(F)
for j in range(len(F)):
    poly = XY[j]; x0, y0, x1, y1 = bb[j]
    for gx in range(int(math.floor(x0 / CELL3)), int(math.floor(x1 / CELL3)) + 1):
        for gy in range(int(math.floor(y0 / CELL3)), int(math.floor(y1 / CELL3)) + 1):
            for kk in G1.get((gx, gy), ()):
                if inside(pins[kk], poly): inside_cnt[j] += 1
            for kk in G2.get((gx, gy), ()):
                if inside(apins[kk], poly): ainside_cnt[j] += 1
def blank4(): return {"buildings": 0, "full_addr": 0, "full_no_row": 0, "any_no_row": 0,
                      "full_no_addrrow": 0}
r4 = collections.defaultdict(blank4); t4 = blank4(); missing = []
for j in range(len(F)):
    reg = val(j, 'reg') or "(\u0431\u0435\u0437 \u0440\u0430\u0439\u043e\u043d)"
    s = val(j, 'street'); n = val(j, 'num'); full = bool(s and n)
    for d in (r4[reg], t4):
        d["buildings"] += 1
        if inside_cnt[j] == 0: d["any_no_row"] += 1
        if full:
            d["full_addr"] += 1
            if inside_cnt[j] == 0: d["full_no_row"] += 1
            if ainside_cnt[j] == 0: d["full_no_addrrow"] += 1
    if full and inside_cnt[j] == 0: missing.append(j)
P("")
P("%-30s %8s %9s %9s %7s %12s" % ("raion", "sgradi", "s ul+nom", "bez red", "%", "bez addr_row"))
for reg, d in sorted(r4.items(), key=lambda kv: -kv[1]['buildings']):
    P("%-30s %8d %9d %9d %6.2f%% %12d" % (str(reg)[:30], d['buildings'], d['full_addr'],
      d['full_no_row'], pct(d['full_no_row'], d['full_addr']), d['full_no_addrrow']))
P("%-30s %8d %9d %9d %6.2f%% %12d" % ("OBSHTO", t4['buildings'], t4['full_addr'],
  t4['full_no_row'], pct(t4['full_no_row'], t4['full_addr']), t4['full_no_addrrow']))
P("  VSICHKI sgradi (i bez adres) bez nito edin pin vatre:", t4['any_no_row'],
  "(%.2f%%)" % pct(t4['any_no_row'], t4['buildings']))
def nearest(x, y, maxr=250.0):
    best = 1e18; r = 1
    cx0 = int(math.floor(x / CELL3)); cy0 = int(math.floor(y / CELL3))
    while (r - 1) * CELL3 <= maxr:
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                if r > 1 and max(abs(dx), abs(dy)) != r - 1: continue
                for kk in G1.get((cx0 + dx, cy0 + dy), ()):
                    px, py = pins[kk]; d = (px - x) ** 2 + (py - y) ** 2
                    if d < best: best = d
        if r > 1 and best < ((r - 1) * CELL3) ** 2: break
        r += 1
    return math.sqrt(best) if best < 1e17 else None
buck = collections.Counter(); mex = []
for j in missing:
    d = nearest(cx[j], cy[j])
    lab = ">250 m" if d is None else ("<=5 m" if d <= 5 else ("5-15 m" if d <= 15 else
          ("15-50 m" if d <= 50 else "50-250 m")))
    buck[lab] += 1
    e = desc(j); e["nearest_delivery_pin_m"] = None if d is None else round(d, 1)
    mex.append(e)
P("  razstoianie do nai-blizkiia dostaven pin za %d-te:" % len(missing))
for kk in ["<=5 m", "5-15 m", "15-50 m", "50-250 m", ">250 m"]:
    P("    %-9s %5d" % (kk, buck.get(kk, 0)))
P("")
P("  PRIMERI (nai-otdalechenite):")
for e in sorted(mex, key=lambda e: -(e['nearest_delivery_pin_m'] or 0))[:6]:
    P("   i=%-6d %-34s | %s | %s | %s m2 | et.%s | najbliz pin %s m | %s" %
      (e['i'], ((e['street'] or '') + ' ' + str(e['num'] or ''))[:34], (e['func'] or '')[:22],
       e['reg'], e['area_m2_info'], e['floors'], e['nearest_delivery_pin_m'], e['centroid']))

# kontrola po normaliziran adresen kliuch
delivered = set(norm(r[NAI]) for r in ROWS if r[NAI])
kr = collections.defaultdict(lambda: {"full": 0, "hit": 0}); kt = {"full": 0, "hit": 0}
key_miss_with_pin = 0; key_miss = 0
for j in range(len(IROWS)):
    s = val(j, 'street'); n = val(j, 'num')
    if not (s and n): continue
    key = norm(str(s) + ' ' + str(n)); reg = val(j, 'reg') or "(\u0431\u0435\u0437 \u0440\u0430\u0439\u043e\u043d)"
    hit = key in delivered
    kr[reg]["full"] += 1; kt["full"] += 1
    if hit: kr[reg]["hit"] += 1; kt["hit"] += 1
    else:
        key_miss += 1
        if inside_cnt[j] > 0: key_miss_with_pin += 1
P("")
P("KONTROLA po normaliziran adresen kliuch (ulica+nomer -> address_rows.normalized_address):")
for reg, d in sorted(kr.items(), key=lambda kv: -kv[1]['full']):
    P("  %-30s %8d %8d %6.1f%%" % (str(reg)[:30], d['full'], d['hit'], pct(d['hit'], d['full'])))
P("  %-30s %8d %8d %6.1f%%" % ("OBSHTO", kt['full'], kt['hit'], pct(kt['hit'], kt['full'])))
P("  nesabrani po kliuch:", key_miss, "| OT TIAH imat dostaven pin VATRE v poligona:",
  key_miss_with_pin, "(%.1f%%)" % pct(key_miss_with_pin, key_miss),
  "-> raznicata e NORMALIZACIIA, ne lipsa")
json.dump({"buildings": len(F), "delivery_pins": len(pins), "address_rows": len(apins),
           "by_region": dict(r4), "total": t4, "missing_count": len(missing),
           "distance_buckets": dict(buck), "missing_examples": mex,
           "addrkey_check": {"by_region": {a: b2 for a, b2 in kr.items()}, "total": kt,
                             "key_miss": key_miss, "key_miss_but_pin_inside": key_miss_with_pin}},
          open("missing_from_delivery.json", "w", encoding='utf-8'), ensure_ascii=False, indent=1)
P("-> missing_from_delivery.json")
OUT.close()
