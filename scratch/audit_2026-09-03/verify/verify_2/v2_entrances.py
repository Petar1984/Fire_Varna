# -*- coding: utf-8 -*-
"""Independent replication of finding #8 (entrance labels colliding across buildings).
Read-only. Writes only into verify_2/."""
import json, os, math, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
FV = r"C:/git/Fire_Varna"
OUT = os.path.dirname(os.path.abspath(__file__))
SEP = " \u00b7 \u0432\u0445. "

SI = json.load(open(FV + "/data/search_index.json", encoding="utf-8"))
AR = json.load(open(FV + "/data/address_rows.json", encoding="utf-8"))
E, ROWS = SI["entries"], AR["rows"]
FO = AR["field_order"]
NA_I = FO.index("normalized_address")
LAT_I, LNG_I = FO.index("lat"), FO.index("lng")
DN = SI["district_names"]

def prettyKey(s):
    return " ".join(str(s).replace("|", " ").split())

def baseAddressLabel(e):
    if e.get("label"):
        return prettyKey(e["label"])
    did = e.get("display_id")
    if did is not None and 0 <= did < len(ROWS):
        na = ROWS[did][NA_I]
        if na:
            return na
    d = e.get("d")
    if d is not None and 0 <= d < len(DN) and DN[d]:
        return DN[d]
    return "(\u0430\u0434\u0440\u0435\u0441)"

def formatAddressHit(e):
    b = baseAddressLabel(e)
    if e.get("kind") == "mf" and e.get("en") is not None:
        return b + SEP + str(e["en"])
    return b

def hav(a, b):
    R = 6371000.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = p2 - p1
    dl = math.radians(b[1] - a[1])
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(min(1.0, math.sqrt(h)))

LAB = [formatAddressHit(e) for e in E]
ents = [i for i, e in enumerate(E) if e.get("en") is not None]
res = {"head": None, "entrance_entries": len(ents), "total_entries": len(E)}

lab_ent = collections.defaultdict(list)
for i in ents:
    lab_ent[LAB[i]].append(i)
dup = {k: v for k, v in lab_ent.items() if len(v) > 1}
same_g = {k: v for k, v in dup.items() if len({E[i].get("g") for i in v}) == 1}
cross_g = {k: v for k, v in dup.items() if len({E[i].get("g") for i in v}) > 1}

def sep(v):
    return round(max((hav(E[a]["pin"], E[b]["pin"]) for a in v for b in v), default=0.0), 1)

res["dup_label_groups"] = len(dup)
res["dup_label_entries"] = sum(len(v) for v in dup.values())
res["same_g_groups"] = len(same_g); res["same_g_entries"] = sum(len(v) for v in same_g.values())
res["cross_g_groups"] = len(cross_g); res["cross_g_entries"] = sum(len(v) for v in cross_g.values())

# what actually survives dedupeDisplayRows: key = norm(label)+'||'+g
# -> rows kept per group = number of distinct g in the group
kept = collections.Counter()
for k, v in dup.items():
    kept[len({E[i].get("g") for i in v})] += 1
res["kept_rows_per_dup_group_histogram"] = dict(sorted(kept.items()))
res["extra_rows_on_screen"] = sum((n-1)*c for n, c in kept.items())

# separation histogram for cross-building groups
BUCK = ["<5m", "5-50m", "50-200m", ">200m"]
def buck(m):
    return BUCK[0] if m < 5 else BUCK[1] if m < 50 else BUCK[2] if m < 200 else BUCK[3]
hist = collections.Counter()
rows = []
for k, v in cross_g.items():
    s = sep(v)
    hist[buck(s)] += 1
    rows.append({"label": k, "count": len(v), "distinct_g": len({E[i].get("g") for i in v}),
                 "distinct_display_id": len({E[i].get("display_id") for i in v}),
                 "separation_m": s,
                 "pins": [[E[i]["pin"][0], E[i]["pin"][1]] for i in v],
                 "g": [E[i].get("g") for i in v],
                 "display_id": [E[i].get("display_id") for i in v]})
res["cross_g_separation_histogram"] = {b: hist.get(b, 0) for b in BUCK}
rows.sort(key=lambda r: (-r["count"], -r["separation_m"], r["label"]))
res["cross_g_top20_by_count"] = rows[:20]
res["cross_g_closest15"] = sorted(rows, key=lambda r: (r["separation_m"], r["label"]))[:15]

# named checks from the finding
for name in ["\u043a\u0432. \u041b\u0435\u0432\u0441\u043a\u0438, \u0431\u043b. 2" + SEP + "\u0410"]:
    pass
want = [k for k in dup if "\u041b\u0435\u0432\u0441\u043a\u0438" in k and "\u0431\u043b. 2" in k]
res["levski_bl2"] = [{"label": k, "count": len(dup[k]), "separation_m": sep(dup[k]),
                      "g": [E[i].get("g") for i in dup[k]],
                      "display_id": [E[i].get("display_id") for i in dup[k]],
                      "pins": [E[i]["pin"] for i in dup[k]]} for k in want]
for probe in ["\u0446\u0430\u0440 \u0441\u0438\u043c\u0435\u043e\u043d 36", "\u0431\u0440\u0430\u0442\u044f \u0433\u0435\u043e\u0440\u0433\u0438\u0435\u0432\u0438\u0447 15"]:
    hits = [k for k in dup if probe in k]
    res["probe_" + probe] = [{"label": k, "count": len(dup[k]), "separation_m": sep(dup[k]),
                              "g": [E[i].get("g") for i in dup[k]],
                              "display_id": [E[i].get("display_id") for i in dup[k]],
                              "pins": [E[i]["pin"] for i in dup[k]]} for k in hits]

json.dump(res, open(OUT + "/v2_entrances.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if not isinstance(v, list)}, ensure_ascii=False, indent=1))
print("levski:", json.dumps(res["levski_bl2"], ensure_ascii=False))
