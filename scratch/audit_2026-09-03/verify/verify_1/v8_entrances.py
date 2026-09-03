# -*- coding: utf-8 -*-
# ОБОРИТЕЛ №1 / находка №8 — независимо възпроизвеждане.
# Правилата са портнати ДОСЛОВНО от C:/git/Fire_Varna/index.html:
#   norm/skel  -> index.html:4839-4840 (initAddressSearch)
#   prettyKey/baseAddressLabel/formatAddressHit -> index.html:4877-4886
#   dedupeDisplayRows ключ -> index.html:5085-5111  (norm(label)+'||'+(g||''))
import json, collections, math, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FV = "C:/git/Fire_Varna/"
si = json.load(open(FV+"data/search_index.json", encoding="utf-8"))
E  = si["entries"]; DN = si["district_names"]
ROWS = json.load(open(FV+"data/address_rows.json", encoding="utf-8"))
FO = ROWS["field_order"]; NA = FO.index("normalized_address"); rows = ROWS["rows"]

def norm(s):
    s = ('' if s is None else str(s)).lower()
    s = s.replace('блок','бл').replace('вход','вх')
    s = re.sub(r"[.№,'\"\-]", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
C = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def skel(w):
    w = w.lower(); o = ''.join(C.get(ch, ch) for ch in w)
    o = re.sub(r'[yj]', 'i', o)
    return re.sub(r'(\D)\1+', r'\1', o)
def prettyKey(s): return re.sub(r'\s+',' ', str(s).replace('|',' ')).strip()
def base_label(e):
    if e.get('label'): return prettyKey(e['label'])
    if e.get('display_id') is not None:
        r = rows[e['display_id']]
        if isinstance(r, list) and r[NA]: return r[NA]
    if e.get('d') is not None and DN[e['d']]: return DN[e['d']]
    return '(адрес)'
def fmt(e):
    b = base_label(e)
    return b + ' · вх. ' + str(e['en']) if (e.get('kind')=='mf' and e.get('en') is not None) else b
def dm(a,b):
    R=6371000.0; p1,p2=math.radians(a[0]),math.radians(b[0])
    h=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))

ENT = [e for e in E if e.get('kind')=='mf' and e.get('en') is not None]
print("входови записа (kind=mf & en) =", len(ENT))
print("от тях без g =", sum(1 for e in ENT if e.get('g') is None))

# --- сцена: една и съща изписана дума, различен dedupe-ключ => N реда един до друг
by_label = collections.defaultdict(list)
for e in ENT:
    by_label[norm(fmt(e))].append(e)

groups = {}
for lab, es in by_label.items():
    keys = collections.defaultdict(list)
    for e in es:
        keys[lab + '||' + (str(e['g']) if e.get('g') is not None else '')].append(e)
    if len(keys) > 1:
        groups[lab] = keys
print("A) групи входове с >1 ОТДЕЛЕН dropdown ред (различно g) =", len(groups))
print("A) записи в тях =", sum(len(e) for k in groups.values() for e in k.values()))
print("A) dropdown редове в тях =", sum(len(k) for k in groups.values()))

# същото, но по УНИКАЛЕН ПИН (мярката на черновата - check_dup.py)
g2 = {}
for lab, es in by_label.items():
    pins = set(tuple(e['pin']) for e in es)
    if len(pins) > 1: g2[lab] = es
print("B) групи входове с >1 РАЗЛИЧЕН ПИН =", len(g2), " записи =", sum(len(v) for v in g2.values()))

# --- разпределение по разстояние и топ
rep = []
for lab, keys in groups.items():
    pts = list({tuple(e['pin']) for k in keys.values() for e in k})
    mx = max((dm(a,b) for i,a in enumerate(pts) for b in pts[i+1:]), default=0.0)
    ents = [e for k in keys.values() for e in k]
    rep.append((mx, lab, fmt(ents[0]), len(keys), len(ents), len(pts),
                sorted({DN[e['d']] for e in ents if e.get('d') is not None})))
hist = collections.Counter()
for mx,*_ in rep:
    hist['<5' if mx<5 else '5-50' if mx<50 else '50-200' if mx<200 else '>200'] += 1
print("A) хистограма по макс. разделение =", dict(hist))
rep.sort(reverse=True)
print("\n--- топ 12 по разделение ---")
for mx,lab,disp,nk,ne,npn,dis in rep[:12]:
    print(f"{mx:8.0f} m  редове={nk:2d} записи={ne:2d} пинове={npn:2d}  {disp[:50]:50s} район={','.join(dis)}")
print("\n--- най-близките (кандидати за истински дублет) ---")
for mx,lab,disp,nk,ne,npn,dis in sorted(rep)[:10]:
    print(f"{mx:8.1f} m  редове={nk:2d} записи={ne:2d}  {disp[:60]}")
