# -*- coding: utf-8 -*-
"""Коя КАИС сграда стои под пиновете (независим PIP + най-близък ръб)."""
import json, math, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
V3 = r'C:/git/varna_3d'
info = json.load(open(V3+'/web/varna_buildings_info.json', encoding='utf-8'))
gj = json.load(open(V3+'/web/varna_buildings_3d.geojson', encoding='utf-8'))
feats = gj['features']
print('features:', len(feats), 'rows:', len(info['rows']))
D = info['dict']; C = info['columns']

def val(i, col):
    r = info['rows'][i]; j = C.index(col); k = r[j]
    if k == -1: return ''
    dd = D.get(col)
    if isinstance(dd, list): return dd[k]
    return k

def poly_pts(f):
    g = f['geometry']; out = []
    cs = g['coordinates']
    if g['type'] == 'Polygon': rings = [cs[0]]
    elif g['type'] == 'MultiPolygon': rings = [p[0] for p in cs]
    else: return []
    for r in rings: out.append(r)
    return out

def bbox(rings):
    xs = [p[0] for r in rings for p in r]; ys = [p[1] for r in rings for p in r]
    return min(xs), min(ys), max(xs), max(ys)

def inside(rings, x, y):
    for r in rings:
        c = False; n = len(r)
        for a in range(n):
            x1,y1 = r[a][0], r[a][1]; x2,y2 = r[(a+1)%n][0], r[(a+1)%n][1]
            if (y1 > y) != (y2 > y):
                xin = (x2-x1)*(y-y1)/(y2-y1)+x1
                if x < xin: c = not c
        if c: return True
    return False

def hav(a,b):
    R=6371008.8
    la1,lo1,la2,lo2=map(math.radians,[a[0],a[1],b[0],b[1]])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))

targets = {
 'Кардиолайф/СБАЛК Варна (пин)': (43.213541, 27.91808),
 'Хоспис Царица Елеонора (пин)': (43.231009, 27.878521),
 'бул република 91 (адр. машина)': (43.230927, 27.878757),
}
for nm,(la,lo) in targets.items():
    best = None; hit = []
    for i,f in enumerate(feats):
        rings = poly_pts(f)
        if not rings: continue
        x0,y0,x1,y1 = bbox(rings)
        if lo < x0-0.0012 or lo > x1+0.0012 or la < y0-0.0012 or la > y1+0.0012: continue
        if inside(rings, lo, la):
            hit.append(i)
        d = min(hav((la,lo),(p[1],p[0])) for r in rings for p in r)
        if best is None or d < best[1]: best = (i, d)
    print('---', nm, la, lo)
    for i in hit:
        print('   ВЪТРЕ i=%d | func=%s | addr=%s | quar=%s | area=%s' % (i, val(i,'func'), val(i,'addr'), val(i,'quar'), val(i,'area_m2')))
    if best:
        i,d = best
        print('   най-близък възел: i=%d на %.1f m | func=%s | addr=%s' % (i, d, val(i,'func'), val(i,'addr')))
print()
print('d(Ц.Елеонора пин, бул република 91) = %.1f m' % hav((43.231009,27.878521),(43.230927,27.878757)))
