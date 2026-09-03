# -*- coding: utf-8 -*-
"""45-те пина с двете азбуки: една и съща ли е адресата (skel-сравнение) и
   ще се слепят ли от dedupeDisplayRows (index.html:5085 → norm(formatAddressHit))."""
import json, re, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV="C:/git/Fire_Varna/"
si=json.load(open(FV+"data/search_index.json",encoding="utf-8")); E=si["entries"]; DN=si["district_names"]
ar=json.load(open(FV+"data/address_rows.json",encoding="utf-8")); rows=ar["rows"]; i_na=ar["field_order"].index("normalized_address")
WS=re.compile(r"\s+")
def pretty(s): return WS.sub(" ",str(s).replace("|"," ")).strip()
def fmt(e):
    if e.get("label"): b=pretty(e["label"])
    elif e.get("display_id") is not None and rows[e["display_id"]][i_na]: b=rows[e["display_id"]][i_na]
    elif e.get("d") is not None and DN[e["d"]]: b=DN[e["d"]]
    else: b="(адрес)"
    if e.get("kind")=="mf" and e.get("en") is not None: b=b+" · вх. "+str(e["en"])
    return b
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
for e in E: pins[tuple(e["pin"])].append(fmt(e))
both=[(p,v) for p,v in pins.items() if any(al(s)=="lat" for s in v) and any(al(s)=="cyr" for s in v)]
print("пинове с lat И cyr =",len(both))
same=0; diff=0; ex=[]
for p,v in both:
    L=[s for s in v if al(s)=="lat"]; Cy=[s for s in v if al(s)=="cyr"]
    hit=False
    for a in L:
        for b in Cy:
            if sk(a)==sk(b): hit=True; ex.append((p,a,b)) if len(ex)<10 else None
    if hit: same+=1
    else: diff+=1
print("  от тях: СЪЩИЯТ адрес в двете азбуки (skel съвпада) =",same,"; различни адреси =",diff)
print("\nпримери (пин | латински ред | кирилски ред) — двата се показват ЕДИН ДО ДРУГ, слепването не ги хваща:")
for x in ex: print("   ",x)
# всички 45 за протокола
out=[{"pin":list(p),"labels":sorted(set(v))} for p,v in both]
json.dump(out,open("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_2/v7_pins45.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
