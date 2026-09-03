# -*- coding: utf-8 -*-
"""Оборител №2 / находка №7 — независима реплика на веригата baseAddressLabel/formatAddressHit
   (index.html:4878-4893) върху HEAD-а на Fire_Varna."""
import json, collections, re, sys, io
sys.stdout.reconfigure(encoding="utf-8")
FV = "C:/git/Fire_Varna/"
si = json.load(open(FV+"data/search_index.json", encoding="utf-8"))
E = si["entries"]; DN = si["district_names"]
ar = json.load(open(FV+"data/address_rows.json", encoding="utf-8"))
rows = ar["rows"]; order = ar["field_order"]
i_na = order.index("normalized_address")

WS = re.compile(r"\s+")
def prettyKey(s):  # точно index.html:4877
    return WS.sub(" ", str(s).replace("|", " ")).strip()

def base_label(e):
    if e.get("label"):
        return prettyKey(e["label"]), "label"
    if e.get("display_id") is not None:
        r = rows[e["display_id"]]
        na = r[i_na]
        if na:
            return na, "rows"
    if e.get("d") is not None and DN[e["d"]]:
        return DN[e["d"]], "district"
    return "(адрес)", "none"

def fmt(e):
    b, src = base_label(e)
    if e.get("kind") == "mf" and e.get("en") is not None:   # точно index.html:4892
        b = b + " · вх. " + str(e["en"])
    return b, src

CYR = set("абвгдежзийклмнопрстуфхцчшщъьюяѝ")
LAT = set("abcdefghijklmnopqrstuvwxyz")
def alpha(s):
    t = s.lower()
    c = any(ch in CYR for ch in t); l = any(ch in LAT for ch in t)
    return "mixed" if (c and l) else "cyr" if c else "lat" if l else "none"

shown = []; srcs = collections.Counter()
for e in E:
    s, src = fmt(e); srcs[src] += 1; shown.append((e, s, alpha(s), src))

ab = collections.Counter(a for _, _, a, _ in shown)
print("HEAD-реплика на веригата")
print("  записи            =", len(E))
print("  label_source      =", dict(srcs))
print("  азбука(записи)    =", dict(ab))
tot = len(E)
print("  lat  %%           = %.2f%%" % (100.0*ab['lat']/tot))
print("  lat+mixed %%      = %.2f%%" % (100.0*(ab['lat']+ab['mixed'])/tot))

uniq = sorted(set(s for _, s, _, _ in shown))
ua = collections.Counter(alpha(s) for s in uniq)
print("  уникални показани =", len(uniq), "→", dict(ua))

# азбука по източник
by = collections.defaultdict(collections.Counter)
for _, _, a, src in shown: by[src][a] += 1
print("  по източник:", {k: dict(v) for k, v in by.items()})

# пинове с двете азбуки
pins = collections.defaultdict(set)
for e, s, a, _ in shown:
    if a in ("lat", "cyr", "mixed"):
        pins[tuple(e["pin"])].add("lat" if a in ("lat",) else "cyr" if a == "cyr" else "mixed")
both = [p for p, v in pins.items() if ("lat" in v and "cyr" in v)]
print("  пинове с lat И cyr =", len(both))
pins2 = collections.defaultdict(set)
for e, s, a, _ in shown:
    if a != "none": pins2[tuple(e["pin"])].add(a)
both2 = [p for p, v in pins2.items() if len(v & {"lat","cyr","mixed"}) >= 2 and ("lat" in v or "mixed" in v) and ("cyr" in v or "mixed" in v) and v != {"mixed"}]
print("  пинове с >=2 различни класа (вкл. mixed) =", len(both2))

# address_rows кирилица?
ra = collections.Counter(alpha(r[i_na]) for r in rows if r[i_na])
print("  address_rows.normalized_address азбука =", dict(ra), "от", len(rows))

# по kind
bk = collections.defaultdict(collections.Counter)
for e, s, a, _ in shown: bk[e.get("kind")][a] += 1
print("  по kind:", {k: dict(v) for k, v in bk.items()})

json.dump({
 "entries": len(E), "label_source": dict(srcs), "alphabet_records": dict(ab),
 "unique_shown": len(uniq), "alphabet_unique": dict(ua),
 "pins_lat_and_cyr": len(both), "address_rows_alphabet": dict(ra),
 "by_source": {k: dict(v) for k, v in by.items()},
 "by_kind": {k: dict(v) for k, v in bk.items()},
}, open("C:/Users/Petar/AppData/Local/Temp/claude/C--git/fb0c0608-7fdb-4635-a8fc-44575d26700a/scratchpad/audit_2026-09-03/verify_2/v7_alpha.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)

# --- ДОПЪЛНЕНИЕ (оборител №2): има ли ВЕЧЕ кирилски низ за латинските записи? ---
print("\n--- покритие на латинските записи от address_rows ---")
lat_e = [e for e,s,a,src in shown if a in ("lat","mixed")]
have_did = sum(1 for e in lat_e if e.get("display_id") is not None)
print("  латински/смесени записи =", len(lat_e), "; от тях С display_id =", have_did)
ok = 0
for e in lat_e:
    di = e.get("display_id")
    if di is not None and rows[di][i_na] and alpha(rows[di][i_na]) == "cyr": ok += 1
print("  от тях с КИРИЛСКИ normalized_address в address_rows =", ok)
