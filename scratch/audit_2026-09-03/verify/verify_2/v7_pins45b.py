# -*- coding: utf-8 -*-
"""Поправка: сравнението да е по БАЗОВИЯ етикет (без „· вх. X")."""
import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]; DN=si["district_names"]
ar=json.load(open(FV+"data/address_rows.json",encoding="utf-8")); rows=ar["rows"]; i_na=ar["field_order"].index("normalized_address")
WS=re.compile(r"\s+")
def pretty(s): return WS.sub(" ",str(s).replace("|"," ")).strip()
def base(e):
    if e.get("label"): return pretty(e["label"])
    if e.get("display_id") is not None and rows[e["display_id"]][i_na]: return rows[e["display_id"]][i_na]
    if e.get("d") is not None and DN[e["d"]]: return DN[e["d"]]
    return "(адрес)"
C={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht','ъ':'a','ь':'','ю':'yu','я':'ya'}
def norm(s):
    s=str(s or "").lower().replace("блок","бл").replace("вход","вх")
    s=re.sub(r"[.№,'\"\-]"," ",s); return WS.sub(" ",s).strip()
def skel(w):
    o="".join(C.get(ch,ch) for ch in w.lower()); o=re.sub(r"[yj]","i",o); return re.sub(r"(\D)\1+",r"\1",o)
def sk(s): return " ".join(sorted(skel(t) for t in norm(s).split()))
CYR=set("абвгдежзийклмнопрстуфхцчшщъьюя")
def al(s):
    t=s.lower(); c=any(ch in CYR for ch in t); l=any(ch in "abcdefghijklmnopqrstuvwxyz" for ch in t)
    return "mixed" if c and l else "cyr" if c else "lat" if l else "none"

pins=collections.defaultdict(list)
for e in E: pins[tuple(e["pin"])].append(base(e))
both=[(p,v) for p,v in pins.items() if any(al(s)=="lat" for s in v) and any(al(s)=="cyr" for s in v)]
same=0; ex=[]
for p,v in both:
    L={s for s in v if al(s)=="lat"}; Cy={s for s in v if al(s)=="cyr"}
    if any(sk(a)==sk(b) for a in L for b in Cy):
        same+=1
        if len(ex)<10: ex.append((list(p),sorted(L),sorted(Cy)))
print("пинове с lat И cyr (по БАЗОВ етикет) =",len(both))
print("  от тях СЪЩИЯТ адрес в двете азбуки (skel съвпада) =",same)
print("  различен адрес в двете азбуки на един пин       =",len(both)-same)
print("\nпримери 'един пин — един адрес, два реда в две азбуки':")
for x in ex: print("   ",x)
ex2=[(list(p),sorted({s for s in v if al(s)=="lat"}),sorted({s for s in v if al(s)=="cyr"})) for p,v in both
     if not any(sk(a)==sk(b) for a in {s for s in v if al(s)=="lat"} for b in {s for s in v if al(s)=="cyr"})]
print("\nпримери 'един пин — РАЗЛИЧНИ имена на улици в двете азбуки':")
for x in ex2[:6]: print("   ",x)

# по-справедливо: без типовите представки (ул/бул/жк/кв/м/с о/пл/ж к)
TYPE={"ul","bul","zhk","kv","m","so","s","o","pl","bl","zh","k","ta","gr","varna","raion"}
def sk2(s): return " ".join(sorted(t for t in (skel(x) for x in norm(s).split()) if t not in TYPE))
same2=0; ex3=[]
for p,v in both:
    L={s for s in v if al(s)=="lat"}; Cy={s for s in v if al(s)=="cyr"}
    if any(sk2(a)==sk2(b) for a in L for b in Cy):
        same2+=1
        if len(ex3)<6: ex3.append((list(p),sorted(L),sorted(Cy)))
print("\nбез типови представки: същият адрес в двете азбуки на един пин =",same2,"от",len(both))
for x in ex3: print("   ",x)
