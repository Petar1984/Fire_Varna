# -*- coding: utf-8 -*-
import json, math, re
FV = "C:/git/Fire_Varna/"
si = json.load(open(FV+"data/search_index.json", encoding="utf-8"))
E  = si["entries"]; DN = si["district_names"]
_R = json.load(open(FV+"data/address_rows.json", encoding="utf-8"))
NA = _R["field_order"].index("normalized_address"); rows = _R["rows"]
def norm(s):
    s = ('' if s is None else str(s)).lower().replace('блок','бл').replace('вход','вх')
    s = re.sub(r"[.№,'\"\-]", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()
C = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def skel(w):
    o = ''.join(C.get(ch, ch) for ch in w.lower())
    return re.sub(r'(\D)\1+', r'\1', re.sub(r'[yj]', 'i', o))
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
