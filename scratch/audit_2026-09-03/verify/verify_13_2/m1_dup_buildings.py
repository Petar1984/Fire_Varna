# -*- coding: utf-8 -*-
"""M1: дублиращи се СГРАДИ като геометрия в доставения 3D слой (varna_3d).
READ-ONLY. Изход: m1_dup_buildings.json"""
import json, hashlib, collections, sys, io
sys.stdout.reconfigure(encoding='utf-8')
P = r"C:/git/varna_3d/web/varna_buildings_3d.geojson"
gj = json.load(open(P, encoding='utf-8'))
feats = gj['features']
print("features:", len(feats))
print("props sample:", json.dumps(feats[0]['properties'], ensure_ascii=False)[:400])

def ring_of(g):
    t = g['type']; c = g['coordinates']
    if t == 'Polygon': return c[0]
    if t == 'MultiPolygon': return c[0][0]
    return None

geom_hash = collections.defaultdict(list)
cen_hash  = collections.defaultdict(list)
for idx, f in enumerate(feats):
    r = ring_of(f['geometry'])
    if not r: continue
    key = hashlib.sha1(json.dumps([[round(x,7),round(y,7)] for x,y in [(p[0],p[1]) for p in r]],
                                  separators=(',',':')).encode()).hexdigest()
    geom_hash[key].append(idx)
    xs = [p[0] for p in r]; ys = [p[1] for p in r]
    cx = round(sum(xs)/len(xs), 6); cy = round(sum(ys)/len(ys), 6)
    cen_hash[(cx,cy)].append(idx)

dup_geom = {k:v for k,v in geom_hash.items() if len(v)>1}
dup_cen  = {k:v for k,v in cen_hash.items() if len(v)>1}
print("групи с ИДЕНТИЧЕН пръстен:", len(dup_geom), "· засегнати features:", sum(len(v) for v in dup_geom.values()))
print("групи с ИДЕНТИЧЕН центроид (6 dp ~0.1m):", len(dup_cen), "· засегнати features:", sum(len(v) for v in dup_cen.values()))

ex = []
for k,v in list(dup_cen.items())[:400]:
    if len(v) > 1:
        ex.append({"centroid": list(k), "n": len(v),
                   "i": [feats[j]['properties'].get('i') for j in v[:6]],
                   "props": [ {kk:vv for kk,vv in feats[j]['properties'].items() if kk in ('i','func','addr','h','name')} for j in v[:3] ]})
ex.sort(key=lambda e:-e['n'])
for e in ex[:10]:
    print(json.dumps(e, ensure_ascii=False))
json.dump({"features": len(feats),
           "identical_ring_groups": len(dup_geom),
           "identical_ring_features": sum(len(v) for v in dup_geom.values()),
           "identical_centroid_groups": len(dup_cen),
           "identical_centroid_features": sum(len(v) for v in dup_cen.values()),
           "examples": ex[:60]},
          open("m1_dup_buildings.json","w",encoding='utf-8'), ensure_ascii=False, indent=1)
