kimi version 0.34.0
• Let me start by reading the key files. This is a big analysis task. Let me read the plan, verdict, excerpts, tests, and run in-memory measurements.

  Files to read:
  - ПЛАН_Б3_07.09.md
  - K28_verdict.md
  - recall_sweep.py
  - recall_sweep_excerpts_M7.txt
  - index_M7_branch.txt
  - test_granitsi_fixtures.py
  - granitsi_fixtures_06.09.json
  - index_excerpts.txt
  - expectations.json
  - old_data/, new_data/ JSONs

  Let me read in parallel.

• Ще прочета плана v3, присъдата K28 и подкрепящите файлове паралелно.

• The plan file is large (890 lines). I need to read it fully, particularly §1.8, §3.5, §8, §9, О22, §13. Let me page through the full output file. The Read tool result is stored at output_path. Let me read the plan in chunks directly with line_offset.Interesting — the M7_PREFIXES in the excerpt includes digits "1" and "2" as well: `(u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")`. The task says "буквените M7_PREFIXES (k, kv, zh, m, s, o, t, i)" — so variant Б in §9 т. 1 skips only the letter prefixes, NOT the digits, which would explain why „възраждане 2"/„младост 2" remain 0 (the "2" token is not significant).

  Wait, but significant_token excludes t.num — "2" would be parsed as number so t.num true → not significant. So M7_PREFIXES digits might be for something else. Let me continue reading the plan and other files.Continue reading the plan from line 546 onwards.Now I need to:
  1. Read recall_sweep.py to understand its API (search function, significant_token, bare_location_query, M7_PREFIXES, location_alias_tokens etc.)
  2. Read expectations.json (p7 / foreign_guard)
  3. Read test_granitsi_fixtures.py (apply_ops)
  4. Read index_M7_branch.txt, index_excerpts.txt
  5. Do in-memory measurements with patched copy of recall_sweep.py.

  The file recall_sweep.py is large. Let me grep for key parts first, then do the measurements via a Python script (read-only — running python that only reads files is fine; user forbids writes. I must be careful: "не изпълнявай команди, които пишат по диска". Importing recall_sweep may write __pycache__! Python writes .pyc files. I can avoid that with `sys.dont_write_bytecode = True` or PYTHONDONTWRITEBYTECODE=1. Also recall_sweep.py may write files on import (OUTDIR = %TEMP%/fv_measures) — need to check module-level side effects. Let me examine the file first.51:import datetime
52:import hashlib
53:import json
54:import math
55:import re
56:import sys
57:import io
58:import pathlib
59:import tempfile
68:REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
73:HOTELS = str(REPO_ROOT / "data" / "hotels.json")
74:PLACES2 = str(REPO_ROOT / "data" / "places.json")
75:CATS = str(REPO_ROOT / "data" / "place_categories.json")
79:REPO_PARITY_OUT = str(REPO_ROOT / "scratch" / "places_search" / "probe_out"
84:OUTDIR = (pathlib.Path(tempfile.gettempdir()) / "fv_measures").as_posix() + "/"
424:def significant_token(t):
434:def significant_tokens(s):
1136:def bare_location_rows(R, cls):
1172:def bare_location_query(R):
1228:def search(q):
3093:M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
3782:def main():
Now let me read the relevant sections of recall_sweep.py: significant_token (~424), bare_location_rows (1136), bare_location_query (1172), search (1228), M7_PREFIXES usage context (~3080-3100), and module-level side effects (lines 60-110, and check what happens at import — lines near end, and lines 4240-4260).Now check module-level side effects: does importing recall_sweep.py build RECS etc. at module level? Let me check where RECS/CLASS_OF are defined, and whether any writes happen at import. OUTDIR writes happen in main presumably. Also `REPO_PARITY_OUT` writes at :4249-4253 — need to check if that's inside a function. Let me grep.418:GENERIC_TOKENS = set()
692:RECS = ([Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
698:EXACT_NAME = {}
803:CLASS_OF = {}
1133:M7_ENABLED = True
3683:def build_expectations(artefact_text, candidate_doc, sweep, refused=None):
---
            _refused = _release["refused"]
            print(u"release: %s ; непокрити делти %d ; отказани %d"
                  % (_release["verdict"], len(_release["uncovered"]), len(_refused)))

    # ---------------------------------------------------------------- the writes
    # Амандамент №4 т. 2: the gates are computed ABOVE; the tracked bodies are
    # written HERE, last, and only when there is nothing red and the signature is
    # on the manifests. The old order wrote the reference first and measured
    # afterwards, so a red run left a frozen artefact behind.
    if not FREEZE:
        # A report-only run gates nothing and publishes nothing; its tracked
        # parity corpus is written here, at the end, with the other writes.
        pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                 newline=chr(10))
    if MANIFEST and not FREEZE:
        _doc = build_expectations(blob_text(u"HEAD", ROWS_REL), ROWS,
                                  measure_sweep(M5, EXTRA), refused=_refused)
        _path, _signature = write_expectations(_doc, frozen=False)
        print(u"REPORT-ONLY: очаквания -> %s (signed_by: %s)" % (_path, _signature))

    if FREEZE:
        blockers = []
        if red:
            blockers.append(u"гейтовете не са зелени — %d оплаквания"
                            % sum(len(x) for x in (sweep_bad, p7_bad, lot1_bad,
                                                   lot1v_bad, lot1v_b_bad,
                                                   lot1v_v_bad, m7_bad)))
        if _drift:
            blockers.append(u"REF_BUCKETS (ADR 008 D7): " + u", ".join(_drift))
        for complaint in (unsigned_expectations(), unsigned_for_release()):
            if complaint:
---
                         u"\n  ".join(complaints))
    return written



# ------------------------------------------------- М7, the durable gate (A.2-4)
# Амандамент №3 т. 4: the М7 rule gets a gate that lives WITH the engine and
# runs in the suite, instead of a script in somebody's scratchpad. The questions
# are the two halves of the rule, and both halves can go red:
#   · a TYPE PREFIX is not a place — „к.к.“, „кв.“, „ж.к.“, „м-т“, „с.о.“ and the
#     ordinals of „Възраждане 1/2“ all reach `qtk`/`ltk` as tokens of their own,
#     and before F12-е „к“ answered with 163 rows and „кв“ with 36;
#   · a place a human really types must still answer through the branch.
M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
M7_PLACES = (u"zlatni", u"mladost", u"chaika", u"zpz", u"vilite",
             u"златни пясъци", u"младост")
M7_BRANCH = u"M7-bare-location"


def failing_queries(bad):
    """The unique queries a gate complains about.
Module-level: RECS built at line 692 — loading happens at module level (reads files). Writes only in main(). Import is safe if I set PYTHONDONTWRITEBYTECODE=1.

  Wait — recall_sweep.py is in the working directory root (not scratch/places_search). REPO_ROOT = parents[2] of __file__. The file here is at C:\Users\Petar\AppData\Local\Temp\tmp.FYNNZjK02u\recall_sweep.py — parents[2] would be C:\Users\Petar\AppData\Local... wait: file = <cwd>/recall_sweep.py → parents[0] = cwd, parents[1] = Temp, parents[2] = Local. So REPO_ROOT/data/hotels.json doesn't exist. The task says: patch a copy in memory with paths to new_data/; main() not called. So I'll load the source as text, patch the three path constants, exec it in memory with __file__ set appropriately. That avoids any writes.

  Also need to handle `sys.argv` — FREEZE/MANIFEST checks look at sys.argv. Running python -c "..." → argv = ['-c'], fine.

  Also sys.stdout.reconfigure — fine.

  Plan for measurements:

  1. Variant B (§9 т.1): skip only letter M7_PREFIXES (k, kv, zh, m, s, o, t, i) before significance test in M7 branch. Implement: in bare_location_query and bare_location_rows, filter R = [t for t in R if t.s not in LETTER_PREFIXES]. Then measure "кв. Левски" → 14/12? "кв. Тракия" → 4/4? "кв. Христо Ботев" → 4/3? "ж.к. Св. Иван Рилски" → 4/2? And "възраждане 2"/"младост 2" remain 0.

  2. §13 т.5: with numbers also in the skip list, "възраждане 2" → 5 and "младост 2" → 20.

  3. §13 т.3: "чайка" after renaming the 10 chaika_kv rows = 21 (not 20). Rename both quarter.name and zone of all 10 chaika_kv rows → expect 21.

  4. Fixture 8 (asparuhovo/druzhba): mutation ЦДГ 43 "Пинокио" set quarter {name: "кв. Аспарухово", code: "druzhba", src: "SIGNED_POLYGON"}, zone "кв. Аспарухово" → "аспарухово" 16→17 and "дружба" 2→1. Also check whether plan's claimed "възраждане" 5→4 mutation works (fixture 6): ДГ№34 „Лястовичка“ quarter name "ж.к. Лястовиче".

  Wait — fixture 6 mutation in plan keeps code "vazrazhdane1" but changes name to "ж.к. Лястовиче". Hmm, but that keeps the code valid. Then "възраждане" should return 4. Let me also verify fixture 7 counts: "чайка" 30 → 21.

  5. §9 т.17... actually §9 т. 17 P7_ADDED drift: count tokens in new vs old place_categories.json: new adds gratska, gratski, varnenchik, vladislav, vasil — count against expectations.json p7/foreign_guard. Need to read expectations.json.

  Also verify baseline numbers for measurements: plan claims today "кв. Левски" → 4 rows, "кв. Тракия" 1, "кв. Христо Ботев" 24 (1 with code by name), "ж.к. Св. Иван Рилски" 22; "левски" bare → 14/12; "възраждане" → 5; "младост" → 20; "чайка" → 30; "аспарухово" → 16, "дружба" → 2; "възраждане 2"/"младост 2" → 0; "бриз" → 4.

  Also check §3.5 fixture 6 mutation and fixture 7 (chaika 30→21) and fixture 8.

  Also check K28 conditions application:
  - К28-1: §1.8.4 — plan now says 1 row with code by name ✓ (verify measured: "кв. Христо Ботев" 24 rows, 1 with hristo_botev code).
  - К28-2: fixture 6 name mutation, assert_case multi-query, fails_on.
  - К28-3: 8 rows named ✓ — verify the 8 names and their new quarters against data.
  - К28-4: §8 proba 5 "бриз" 4 ✓ — verify 4 rows named.
  - К28-5: §9 т.1 variant B present ✓ — verify measured numbers.
  - К28-6: О22 semantics of 138 ✓ — plan records semantics "lost/changed" and §4 step 2 requires the f06ac06↔f00dd78 diff (150). I can't verify coverage numbers (needs gates/coverage.py which isn't in the copy). Check expectations.json / old_data vs new_data zone_named changes: K28 said old→new gives zone_named lost 0 / changed 0, 57 gains. Verify: count rows where old zone was "район X" and new zone is quarter name — 57 (42+15). But 138 vs baseline f06ac06 can't be verified here — the plan now records semantics and the 150 diff, which addresses К28-6 as best possible in this copy. But wait — can I verify the claim "доставката връща 12"? No, that needs the baseline data. The copy has old_data = f00dd78 data presumably. 138 vs 150 semantics: plan says against f00dd78 uncovered = 150, against f06ac06 = 138, meaning the delivery "returns 12". Hmm, actually that's odd: uncovered against f00dd78 (150) is larger than against f06ac06 (138). coverage "uncovered" = rows covered in base but not in candidate... wait no. Actually uncovered = rows in candidate lacking coverage relative to base+allow? If base = f06ac06 (older, fewer named rows?), uncovered 138; if base = f00dd78, uncovered 150. And 150 - 138 = 12 means 12 rows that were "uncovered" against f00dd78 are now covered by the older baseline's allow... This is confusing but not measurable here. I can only check that the plan's semantic definition is consistent: 138 = 44+44+39+11. old→new in the copy: rows that changed zone from "район X" to quarter name = 57. Those are "changed" only if the base already had a named zone. Against f06ac06 the counts differ. I can note what's verifiable.

  Actually wait — I should check whether old_data corresponds to f00dd78. K28 verdict says "По old_data→new_data: zone_named lost 0 / changed 0, 57 печалби". The plan's О22 semantics: "lost" = row had named zone in base and none in candidate; "changed" = had a different one. Against f00dd78 (old_data), lost 0/changed 0 — but plan claims 150 uncovered against f00dd78 with places 78+18=96, hotels 47+7=54. That's contradictory unless uncovered ≠ lost+changed — uncovered is "rows in candidate not covered by base/allow", i.e. NEW named rows. So against f00dd78: 57 new quarter-named rows? No, 150... hmm. Actually uncovered could include rows present in candidate with zone that base didn't have named... 57 gains vs 150 uncovered. Doesn't add up either. This is unverifiable without gates/coverage.py and the baseline blobs. I'll note this.

  Hmm, wait. Let me reconsider: 1.8.1б claims base=f06ac06, candidate=f00dd78 → uncovered 150. So candidate is the OLD data (f00dd78 = current HEAD data = old_data presumably). uncovered = candidate rows not present/covered in base. So f00dd78 vs f06ac06 has 150 rows whose zone_named status isn't in the signed baseline. And new delivery vs f06ac06 = 138. So delivery "returns 12" rows to baseline-covered state. And against old→new directly (K28): 57 gains. OK, plausible. Not measurable here; fine.

  Now K28-7: fixture 7 — plan enumerates 10 ops by name, claims 30→21. K28 said renaming all 10 chaika_kv rows gives 30→20 (21 with zone too). Plan §13 т.3 says measured 21 in both variants. I need to measure: rename quarter.name and zone of all 10 chaika_kv rows to "кв. Крайморие" → "чайка" returns 21. Also the plan's survivor claim: 19 chaika_kk + 4 ОДЗ Чайка (name contains chaika) + „ДКЦ Чайка" ЕООД = 21. Note K28 said "преименуване на всичките 10 реда chaika_kv (по един op на ред) дава 30→20 (измерено: 21 при смяна и на zone)". So K28 measured 20 with name-only, 21 with name+zone? And plan claims 21 for both variants. Need to measure both: (a) name-only → ? (b) name+zone → ?

  Wait, actually careful: plan fixture 7 mutation changes quarter.name AND zone to "кв. Крайморие". §13 т.3 claims 21 measured in both variants ("и при смяна само на quarter.name, и при смяна на quarter.name + zone"). I measure both.

  Hmm, but why would name-only give 20 vs 21? The "4 ОДЗ Чайка" row: it has chaika in name, so name_has_phrase keeps it regardless. „ДКЦ Чайка" ЕООД has no quarter. Survivors = 19 + 1 + 1 = 21. Unless with name-only mutation, one more row survives via qtk? qtk is built from quarter name; changing quarter.name to "кв. Крайморие" removes "chaika" from qtk. So name-only should also give 21. K28's "20" was perhaps with mutation not hitting all 10 rows (e.g. hotels AMIRAL name difference). The plan lists 10 names including АМИРАЛ (hotels). I'll measure.

  Also verify the 10 chaika_kv row names exist exactly (apply_ops mutates by unique name — check test_granitsi_fixtures.py apply_ops).

  Now the M7 patch. Let me define: LETTER_PREFIXES = ("k","kv","zh","m","s","o","t","i"). Patch bare_location_query: replace `return all(significant_token(t) for t in R)` with filtered R. But bare_location_rows also needs filtered tokens, otherwise tokens include "kv" and "жк" etc. and quarter_hit requires all tokens in qtk. Note: qtk for "кв. Левски" quarter includes tokens of the name "ж.к. Васил Левски"? Quarter names like "кв. Левски" → place_tokens → ["kv", "levski"]? qtk probably contains both "kv" and "levski"? Hmm, actually qtk might include prefix tokens. Let me check Rec class qtk construction (~672). If qtk includes "kv", then bare_location_rows with R unfiltered would match via kv too... but bare_location_query returns False since "kv" isn't significant. Variant B: filter R before both. The plan says: "Пропускат се само буквените префикси ... преди теста за значимост в М7 клона" and mentions recall_sweep.py:1257+:1263 (2 lines) — i.e. in search(), filter R before the M7 branch calls. That handles both bare_location_query and bare_location_rows.

  For the client: index_M7_branch.txt — client has no list; plan acknowledges.

  Implementation for measurement: in search(), after computing R in the no-key branch (and also key branch? The M7 branch only fires when not has_key), insert:
  R = [t for t in R if t.s not in M7_LETTER_PREFIXES]
  before `if not has_key and bare_location_query(R):`.

  Also variant А′/§13 т.5: skip list = full M7_PREFIXES including "1","2". But note tokens "2" are numbers (t.num=True) so t.s == "2". significant_token already excludes them. But if we skip them from R, then "възраждане 2" → R = ["vazrazhdane"] → bare_location_rows returns parent's 5 rows. Measure: "възраждане 2" → 5, "младост 2" → 20.

  Now let me check qtk construction and Rec, and whether "възраждане" returns 5 on new data. Also need name_has_phrase, dph. I'll just run the measurements.

  Approach: python script that reads recall_sweep.py source, patches HOTELS/PLACES2/CATS paths to new_data/, execs in a module namespace, then runs queries. Must set sys.dont_write_bytecode and ensure no writes: exec doesn't write. But module-level code at line ~90 FREEZE check — fine.

  Careful: module-level code loads data files (RECS built at :692 from hotels/places). That's reads only. Are there any module-level writes? grep for write_text at module level — the ones found are inside main() region (4240+). Let me double check there's no other top-level write. I'll grep for "write" lines.

• Сега проверявам за странични ефекти на модулно ниво и чета `test_granitsi_fixtures.py` и `expectations.json`.2144:                       % (r.name, json.dumps(r.district, ensure_ascii=False)))
2182:                   % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
2662:    pathlib.Path(out).write_text(
2663:        json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=False) + chr(10),
2938:        return json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False) + chr(10)
3073:        path.write_text(dump(doc), encoding="utf-8", newline="\n")
3551:                    json.dumps(blob_json(commit, u"data/place_categories.json"),
3554:                    json.dumps(cats, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest(),
3601:    same function — a second `json.dumps` with a different `indent` would be a
3603:    return json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False) + chr(10)
---
621:        self.qtk = self._loc_tokens(u"quarter", self.quarter)
622:        self.ltk = self._loc_tokens(u"locality", self.locality)
625:        self.dph = self._loc_phrases(u"district", self.district)
633:        self.zkset = set(self.qtk) | set(self.ltk) | set(self.legtk) | set(self.ktk)
1104:    rows = [r for r in cls if phrase in r.dph]
1123:    d_rows = [r for r in cls if r.quarter is None and phrase in r.dph]
1143:    rows of a KIND. So the trigger reads `qtk` and `ltk` and nothing else:
1159:    quarter_hit = [r for r in cls if all(t in r.qtk for t in tokens)]
1160:    locality_hit = [r for r in cls if all(t in r.ltk for t in tokens)]
1167:    district_hit = [r for r in cls if r.quarter is None and phrase in r.dph]
1182:    reached `qtk`/`ltk` as tokens of their own and answered as places: measured
2374:            out.update(rec.qtk)
2376:            out.update(rec.ltk)
3090:#     ordinals of „Възраждане 1/2“ all reach `qtk`/`ltk` as tokens of their own,
3345:    saved_dph = [(rec, rec.dph) for rec in RECS]
3347:        for rec, _ in saved_dph:
3348:            rec.dph = set()
3351:        for rec, dph in saved_dph:
3352:            rec.dph = dph


• Good — module writes nothing on import ("the module writes not one byte on import"). test_granitsi_fixtures.py's reindex pattern is exactly what I need. But REFERENCE path is scratch/places_search/recall_sweep.py which doesn't exist in this copy — I'll build my own loader with patched path constants.

  Now read expectations.json p7/foreign_guard and check place_categories old vs new for P7_ADDED tokens. Let me look at expectations.json.['_meta', 'gate_queries', 'sweep', 'claims', 'p7', 'delivery', 'before', 'artefact', 'replay', 'anchors']
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "C:\Program Files\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u043a' in position 19: character maps to <undefined>
Set up a todo list and fix the encoding issue (PYTHONIOENCODING=utf-8).{
 "added": {
  "к.к. Св. Св. Константин и Елена": [
   "konstanin"
  ],
  "кв. Изгрев": [
   "zhkizgrev"
  ]
 },
 "tokens": 2,
 "zones": 2,
 "records_touched": 48,
 "alias_intersection": [],
 "foreign_guard": [
  {
   "zone": "ж.к. Дружба",
   "token": "asparuhovo",
   "tag": "foreign:asparuhovo:asparuhovo"
  },
  {
   "zone": "кв. Владиславово",
   "token": "vladislav",
   "tag": "foreign:vladislav:vladislav"
  },
  {
   "zone": "кв. Владиславово",
   "token": "varnenchik",
   "tag": "foreign:varnenchik:varnenchik"
  }
 ],
 "guard_starved": {
  "ж.к. Дружба": [
   "asparuhovo"
  ],
  "кв. Владиславово": [
   "varnenchik",
   "vladislav"
  ]
 }
}
Now count the P7_ADDED in new vs old place_categories.json. The plan claims new dictionary adds gratska, gratski, varnenchik, vladislav, vasil (5 new tokens) and 7 tokens in 5 zones: Гръцката махала: gratska, gratski; к.к. Св.Св. Константин и Елена: konstanin; кв. Владиславово: varnenchik, vladislav; кв. Изгрев: zhkizgrev; кв. Левски: vasil. Records touched 48 → 64.

  Wait — the plan's §9 т.17 says "Новият речник добавя 5 нови токена (gratska, gratski, varnenchik, vladislav, vasil)". The 7 tokens in 5 zones include konstanin and zhkizgrev which are already in the signed p7 (added: 2 tokens in 2 zones). So the drift = 7 tokens in 5 zones total vs signed 2 in 2. And the 5 genuinely new = gratska, gratski, varnenchik, vladislav, vasil.

  I need to compute P7_ADDED the way recall_sweep does. P7_ADDED is computed at line ~2182 — let me find how P7_ADDED is computed. It's probably module-level. Let me look around line 2100-2200.

  Actually simpler: use the in-memory patched module and read its P7_ADDED for both old and new data. The module builds P7_ADDED at import? Line 2182 references it in a complaint string. Let me check where P7_ADDED is assigned.405:ZONE_EXTRA, P7_ADDED, P7_DROPPED = zone_alias_tokens(cats, ZONES_IN)
2176:    n_tok = sum(len(v) for v in P7_ADDED.values())
2177:    if n_tok != p7.get("tokens") or len(P7_ADDED) != p7.get("zones"):
2179:                   % (n_tok, len(P7_ADDED), p7.get("tokens"), p7.get("zones")))
2180:    if P7_ADDED != p7.get("added"):
2182:                   % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
2693:            "p7_added": P7_ADDED,
2695:            "p7_zones_with_aliases": len(P7_ADDED),
2696:            "p7_tokens": sum(len(v) for v in P7_ADDED.values()),
2697:            "p7_records_touched": sum(1 for r in RECS if r.p7),
3439:    added_tokens = set(t for tokens in P7_ADDED.values() for t in tokens)
3455:        "added": P7_ADDED,
3456:        "tokens": sum(len(v) for v in P7_ADDED.values()),
3457:        "zones": len(P7_ADDED),
3458:        "records_touched": sum(1 for r in RECS if r.p7),
3460:        "foreign_guard": pairs,
3461:        "guard_starved": alone,
4165:          % (sum(len(v) for v in P7_ADDED.values()), len(P7_ADDED),
4167:    print(u"П7 added: %s" % json.dumps(P7_ADDED, ensure_ascii=False, sort_keys=True))
        return 2
    return 0 if len(t.orig) <= 3 else (1 if lev(t.s, v, 2) <= 2 else 0)


def zone_alias_tokens(cats_doc, zones):
    """\u00a711 steps (\u0430)-(\u0435) + (\u0434\u2032) \u2014 the per-zone CANDIDATES, before step (\u0436).

    Fail-soft (\u04217\u2032): without a well-formed `zones` object \u041f7 is simply off.
    Returns (extra, added, dropped): extra {zone: [Tok]}, added {zone: [str]},
    dropped {zone: ["reason:token"]}."""
    zdict = (cats_doc or {}).get("zones")
    if not isinstance(zdict, dict):
        return {}, {}, {}
    meta = (cats_doc or {}).get("_meta") or {}

    def family(z):
        e = zdict.get(z)
        return (e.get("family") or z) if isinstance(e, dict) else z

    own = dict((z, set(t.s for t in place_tokens(z))) for z in zones)
    generic = set()
    for word in (meta.get("zone_generic_words") or []):
        for t in place_tokens(word):
            generic.add(t.s)
    # (\u0434\u2032) \u04201: a token that IS, or is within lev<=2 of, an own token of a zone
    # from ANOTHER family is a foreign name \u2014 `primorski`/`primorskiat` fall here.
    # The >=3 floor is mandatory: without it `zpz` dies against \u201ezh\u201c.
    foreign = {}
    for z in zones:
        foreign[z] = set(tok for z2 in zones if family(z2) != family(z)
                         for tok in own[z2] if len(tok) >= 3)

    extra, added, dropped = {}, {}, {}
    for z in zones:
        e = zdict.get(z)
        aliases = e.get("aliases") if isinstance(e, dict) else None
        if not isinstance(aliases, list):
            continue
        for alias in aliases:
            if not isinstance(alias, str):
                continue
            for t in place_tokens(alias):
                why = None
                if t.num:                                        # (\u0430)
                    why = "num"
                elif len(t.orig) <= 2 or len(t.s) <= 2:          # (\u0431)
                    why = "short"
                elif t.orig in ADDR:                             # (\u0432)
                    why = "addr"
                elif t.s in generic:                             # (\u0433)
                    why = "generic"
                elif t.s in own[z]:                              # (\u0435)
                    why = "own"
                else:
                    for fk in foreign[z]:                        # (\u0434) + (\u0434\u2032)
                        if fk == t.s or lev(t.s, fk, 2) <= 2:
                            why = "foreign:" + fk
                            break
                if why:
                    tag = why + ":" + t.s
                    if tag not in dropped.setdefault(z, []):
                        dropped[z].append(tag)
                elif t.s not in added.setdefault(z, []):
                    added[z].append(t.s)
                    extra.setdefault(z, []).append(t)
    for z in added:
        added[z].sort()
    return extra, added, dropped


ZONES_IN = sorted(set([h["zone"] for h in hotels] + [p["zone"] for p in places2]))
# ЛОТ 1в-В: `zones` + П7 are SUPERSEDED by the three typed dictionaries below and
# feed nothing but `check_p7_gate()`, which pins the old flat zone list and is
# RED until Petar signs the manifest. They are kept so that gate can fail loudly
# with a named difference instead of crashing on a missing name.
ZONE_EXTRA, P7_ADDED, P7_DROPPED = zone_alias_tokens(cats, ZONES_IN)

# ============================================== ЛОТ 1в-В (план §3г, §3ж S3/S6)
# The delivery stopped carrying ONE „zone“ string: every record now has three
# TYPED fields — `quarter` | `district` | `locality`, each `null` or
# {name, src, code} — and the dictionary answers with three SEPARATE (class,
# code) dictionaries plus `legacy_by_row`. The class travels with the word
# because „младост“ is a quarter AND a district; one flat token set could not
# tell them apart, and that is exactly what put СУ „Гео Милев“ in a drawn
# industrial-zone hull. `zone` stays as the compat label (quarter?.name ??
# „район “ + district.name) until G-ZERO-ZONE.
LOC_CLASSES = (u"quarter", u"district", u"locality")

GENERIC_TOKENS = set()
for _w in ((cats.get("_meta") or {}).get("zone_generic_words") or []):
    for _t in place_tokens(_w):
====
        return [complaint]
    signed = (expectations() or {}).get("sweep") or {}
    bad = []
    for name, rows in ((u"m5_a8", m5), (u"extra", extra)):
        want = dict((e.get("q"), e) for e in (signed.get(name) or []))
        for q, _expect, n, branch, _label, ok in rows:
            entry = want.get(q)
            if entry is None:
                bad.append(u"%s `%s`: няма подписан отговор" % (name, q))
                continue
            if (branch, n, bool(ok)) != (entry.get("branch"), entry.get("n"), entry.get("ok")):
                bad.append(u"%s `%s`: %s/%d/%s, подписано е %s/%s/%s"
                           % (name, q, branch, n, bool(ok), entry.get("branch"),
                              entry.get("n"), entry.get("ok")))
    return bad


def measure_p7():
    """The П7 measure, including the guard that can be starved."""
    added_tokens = set(t for tokens in P7_ADDED.values() for t in tokens)
    aliases = set()
    for rec in RECS:
        aliases |= rec.aset
    _extra, added, dropped = zone_alias_tokens(cats, ZONES_IN)
    pairs, alone = [], {}
    for zone in sorted(dropped):
        for tag in dropped[zone]:
            if not tag.startswith(u"foreign:"):
                continue
            token = tag.rsplit(u":", 1)[-1]
            pairs.append({"zone": zone, "token": token, "tag": tag})
            if zone not in alone:
                _e, only, _d = zone_alias_tokens(cats, [zone])
                alone[zone] = list(only.get(zone) or [])
    return {
        "added": P7_ADDED,
        "tokens": sum(len(v) for v in P7_ADDED.values()),
        "zones": len(P7_ADDED),
        "records_touched": sum(1 for r in RECS if r.p7),
        "alias_intersection": sorted(added_tokens & aliases),
        "foreign_guard": pairs,
        "guard_starved": alone,
    }


def measure_delivery():
Now I can compute P7_ADDED for old vs new data by loading the module in-memory twice with patched path constants (HOTELS, PLACES2, CATS). Note ZONES_IN depends on zones of records, and records_touched depends on RECS. To measure "48 → 64" for records_touched and foreign_guard differences.

  Plan for the measurement script: read recall_sweep.py source, patch the three path constants lines:
  - `HOTELS = str(REPO_ROOT / "data" / "hotels.json")` → absolute path to new_data/hotels.json (or old_data)
  - same for PLACES2, CATS.

  Then exec with a module namespace, __file__ set to something. Then run queries.

  Note: `sys.argv` — running via stdin, sys.argv = ['-'], fine (no --freeze/--manifest).

  Also note line 61-62 reconfigure stdout — fine.

  Also `REPO_PARITY_OUT` and writes only in main(). Import safe.

  Now build a comprehensive measurement script. Steps:

  A. Load module with new_data paths. Measure baseline queries:
  - "кв. Левски", "кв. Тракия", "кв. Христо Ботев", "ж.к. Св. Иван Рилски" → branch, n, count rows with quarter.code == expected code.
  - "левски" → 14/12
  - "възраждане" → 5, names
  - "възраждане 2", "ж.к. възраждане 2", "младост 2" → 0
  - "чайка" → 30 (19 chaika_kk + 10 chaika_kv + 1 none)
  - "аспарухово" → 16 (9 asparuhovo + 7 without quarter), "дружба" → 2
  - "бриз" → 4
  - "младост" → 20 (8/12), "училище младост" → 6 (3), "училище район младост" → 12 (9)
  - P7_ADDED + records_touched for new.

  B. Variant B patch: modify source: in search(), before `if not has_key and bare_location_query(R):` insert filtering of R. Actually simpler to patch via string replacement on source text:

  Old:
  ```
      if not has_key and bare_location_query(R):
  ```
  Insert before it:
  ```
      if not has_key:
          R = [t for t in R if t.s not in M7_LETTER_PREFIXES]
  ```
  But wait — that mutates R used later too (M3 gate etc.) if M7 doesn't fire. The plan says 2 lines at :1257+:1263. Hmm, in search the M7 block is at :1257-1265. Patching only the branch: better to patch inside bare_location_query and bare_location_rows to filter internally. To keep semantics "skip prefixes before significance test in M7 branch", patch:

  In bare_location_query: `return all(significant_token(t) for t in R)` → `return all(significant_token(t) for t in R if t.s not in M7_LETTER_PREFIXES)`. But also need to ensure R nonempty after filtering? E.g. query "кв" alone → filtered empty → all() True → then bare_location_rows with tokens filtered... Careful. The plan's variant presumably filters R itself before both calls. For measurement, patch search():

  ```
      if not has_key and bare_location_query(R):
  ```
  →
  ```
      R = [t for t in R if t.s not in M7_LETTER_PREFIXES] if not has_key else R
      if not has_key and R and bare_location_query(R):
  ```

  Hmm, but this changes downstream behavior for non-M7 queries with prefix tokens (e.g. "ж.к. Младост 2" has prefix "zhk"? Actually "ж.к." normalizes to... place_tokens of "ж.к. младост 2" → "zhk"? Let me check: norm replaces [.№,'"-] with space, so "ж.к." → "ж к" → tokens "zh", "k" probably transliterated. So "ж.к. младост 2" → tokens zh, k, mladost, 2. Under variant B with R filtered in search before M7 only, R becomes [mladost, 2]... wait no, if we filter only letters: [mladost, 2]. Then bare_location_query requires all significant → "2" not significant → False → falls to M3 gate with R = [mladost, 2]! That changes downstream behavior of queries that don't fire M7. Hmm. That's why the plan says skip ONLY letters — so "възраждане 2" keeps "2" and stays 0 because significance test fails... no wait, if R filtered = [vazrazhdane, 2], significance test on 2 fails → M7 not taken → falls through to M3 with R including or excluding?

  To measure exactly what the plan claims, I should implement it as the plan describes: "пропускане САМО на буквените M7_PREFIXES преди теста за значимост в М7 клона" — i.e. inside the M7 branch only: both bare_location_query(R) and bare_location_rows(R) get called with filtered R. If M7 doesn't fire, R unchanged downstream.

  Implementation: patch search():
  ```
      if not has_key and bare_location_query(R):
          bare = bare_location_rows(R, cls)
  ```
  →
  ```
      R7 = [t for t in R if t.s not in M7_LETTER_PREFIXES]
      if not has_key and R7 and bare_location_query(R7):
          bare = bare_location_rows(R7, cls)
  ```

  That's clean and matches "в М7 клона". Measure: кв. Левски → expect 14/12; кв. Тракия → 4/4; кв. Христо Ботев → 4/3; ж.к. Св. Иван Рилски → 4/2; възраждане 2 → 0; младост 2 → 0.

  Wait "ж.к. Св. Иван Рилски" tokens: zh, k, sv?, ivan, rilski. "Св." → "sv" which is... t.s = "sv", len 2 → not significant anyway. Letter prefixes list doesn't include "sv", fine. Filtered: [sv, ivan, rilski]. Significance: sv len ≤2 → not significant → M7 fails?? Hmm. Then how would the plan get 4 rows for "ж.к. Св. Иван Рилски"? Let me check: maybe transliteration maps "св" → "sv" len 2. significant_token requires len>2. So "sv" fails. Unless "св." normalizes differently. Hmm — maybe the query token "св" is dropped by place_tokens entirely? Or maybe it's in ADDR? Let me just measure and see.

  Actually wait, maybe quarter name is "кв. Св. Иван Рилски" and its qtk includes "sv"? If significant_token("sv") is False, then bare_location_query fails and we'd get M3 fallback, not 4. But the plan claims measured 22→4 with 2/4 having code. Hmm, "ж.к. Св. Иван Рилски" today gives 22 rows via M3? Plan 1.8.4 says all four queries → M3. After variant B → 4 rows (2 with sv_ivan_rilski). For that to be M7-bare, R7 = [sv, ivan, rilski] must all be significant. "sv" len 2 fails... unless transliteration of "св" gives something longer, or the token is "sv" but... Let me check place_tokens/norm/transliteration. Let me look at how tokens are formed (lines 109-140) and whether there's a step removing short tokens or expanding abbreviations.

  Let me just run the measurement and see what happens. If mismatch, investigate.

  C. §13 т.5: variant with numbers skipped too: R7 = [t for t in R if t.s not in M7_PREFIXES] (full list incl "1","2"). Measure "възраждане 2" → 5? "младост 2" → 20?

  D. §13 т.3 / fixture 7: mutate 10 chaika_kv rows: set quarter.name & zone = "кв. Крайморие" (keep code chaika_kv? plan keeps code, changes name and zone). Measure "чайка" → expect 21. Also name-only variant (change quarter.name only) → 21 per plan (K28 said 20). Need reindex like test does. I'll replicate reindex() logic in my script using the module's Rec etc.

  E. Fixture 8: mutate ЦДГ 43 "Пинокио": set quarter {name:"кв. Аспарухово", code:"druzhba", src:"SIGNED_POLYGON"}, zone "кв. Аспарухово". Measure "аспарухово" → 17? "дружба" → 1? Also check fixture 6 mutation: ДГ№34 „Лястовичка“ quarter {name:"ж.к. Лястовиче", code:"vazrazhdane1", src:"SIGNED_POLYGON"}, zone "ж.к. Лястовиче" → "възраждане" 5→4, and "възраждане 2"/"ж.к. възраждане 2" stay 0.

  F. K28-3 verification: the 8 lost rows of "младост" old vs new. I can measure with old_data module: "младост" → 28 rows names; new_data → 20; diff names should be the 8 listed with their new quarters. K28 already did this; verify quickly.

  G. P7_ADDED old vs new: tokens/zones/records_touched, foreign_guard. Old should be 2 tokens/2 zones/48; new 7 tokens/5 zones/64; foreign_guard in new: does vladislav/varnenchik disappear from foreign_guard (now accepted)? Check new dropped/foreign_guard for gratska etc. Plan says new dictionary ADDS gratska, gratski, varnenchik, vladislav, vasil as aliases — meaning in new place_categories.json these aliases exist in zones entries. Let me also directly inspect old/new place_categories.json zone aliases diff.

  Also verify "бриз" = 4 with the named rows (K28-4) and "кв. Христо Ботев" 24 with 1 code row (K28-1, §1.8.4).

  Note fixture 8 question (4): "планът намери ли мутация, която реално променя отговора, и пада ли" — the mutation changes "аспарухово" 16→17 and "дружба" 2→1. Also verify plan's claim that alias "Аспарухово" → druzhba is dropped as foreign (location_alias_tokens dropped["druzhba"] contains "foreign:asparuhovo:asparuhovo"). In new_data dictionary, does druzba entry have alias "Аспарухово"? The plan says measured location_alias_tokens drops it. I can check via module: location dicts for quarter, and compute location_alias_tokens for quarter entries to see dropped["druzhba"].

  Let me now check place_tokens/transliteration quickly (lines 109-180) to understand "св".

• Сега търся как се токенизира „св.“ и после правя измерванията.    return s.strip()

# index.html:4787 skel()
_SKEL = {
    "\u0430": "a", "\u0431": "b", "\u0432": "v", "\u0433": "g", "\u0434": "d",
    "\u0435": "e", "\u0436": "zh", "\u0437": "z", "\u0438": "i", "\u0439": "i",
    "\u043a": "k", "\u043b": "l", "\u043c": "m", "\u043d": "n", "\u043e": "o",
    "\u043f": "p", "\u0440": "r", "\u0441": "s", "\u0442": "t", "\u0443": "u",
    "\u0444": "f", "\u0445": "h", "\u0446": "ts", "\u0447": "ch", "\u0448": "sh",
    "\u0449": "sht", "\u044a": "a", "\u044c": "", "\u044e": "yu", "\u044f": "ya",
}

def skel(w):
    w = w.lower()
    o = "".join(_SKEL.get(ch, ch) for ch in w)
    o = re.sub(r"[yj]", "i", o)
    o = re.sub(r"([^0-9])\1+", r"\1", o)   # JS /(\D)\1+/g ; \D == [^0-9]
    return o

# index.html:4788 lev()
def lev(a, b, cap):
    la, lb = len(a), len(b)
    if abs(la - lb) > cap:
        return cap + 1
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] * (lb + 1)
        best = i
        for j in range(1, lb + 1):
            v = min(prev[j] + 1, cur[j - 1] + 1,
                    prev[j - 1] + (0 if a[i - 1] == b[j - 1] else 1))
            cur[j] = v
            if v < best:
                best = v
        if best > cap:
            return cap + 1
        prev = cur
    return prev[lb]

# ------------------------------------------------------------------- T1 tokens
TYPO = re.compile(u"[\u201e\u201c\u201d\u201a\u2018\u2019\u00ab\u00bb\u2013\u2014/()]")

LET = u"\u0410-\u042f\u0430-\u044fA-Za-z"
NOL = u"(?<![" + LET + u"])"
NOR = u"(?![" + LET + u"])"
MARKERS = [
    (re.compile(NOL + u"\u0445\\s*-\\s*\u043b" + NOR, re.I), u" \u0445\u043e\u0442\u0435\u043b "),
    (re.compile(NOL + u"\u043a\\s*-\\s*\u0441" + NOR, re.I), u" \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 "),
    (re.compile(NOL + u"\u0434\\s*-\\s*\u0440" + NOR, re.I), u" \u0434\u043e\u043a\u0442\u043e\u0440 "),
    (re.compile(NOL + u"\u0441\u0432\\." , re.I), u" \u0441\u0432\u0435\u0442\u0438 "),
    (re.compile(NOL + u"\u0441\u0432" + NOR, re.I), u" \u0441\u0432\u0435\u0442\u0438 "),
]
ORD_SUF = re.compile(
    u"(\\d+)\\s*-?\\s*(\u043c\u0438|\u043c\u0430|\u043c\u043e|\u0442\u0438|\u0442\u0430|\u0442\u043e|"
    u"\u0432\u0438|\u0432\u0430|\u0432\u043e|\u0440\u0438|\u0440\u0430|\u0440\u043e)(?![" + LET + u"])", re.I)

_ORD_STEM = {
    u"\u043f\u044a\u0440\u0432": 1, u"\u0432\u0442\u043e\u0440": 2, u"\u0442\u0440\u0435\u0442": 3,
    u"\u0447\u0435\u0442\u0432\u044a\u0440\u0442": 4, u"\u043f\u0435\u0442": 5, u"\u0448\u0435\u0441\u0442": 6,
    u"\u0441\u0435\u0434\u043c": 7, u"\u043e\u0441\u043c": 8, u"\u0434\u0435\u0432\u0435\u0442": 9,
    u"\u0434\u0435\u0441\u0435\u0442": 10, u"\u0435\u0434\u0438\u043d\u0430\u0434\u0435\u0441\u0435\u0442": 11,
    u"\u0435\u0434\u0438\u043d\u0430\u0439\u0441\u0435\u0442": 11,
    u"\u0434\u0432\u0430\u043d\u0430\u0434\u0435\u0441\u0435\u0442": 12,
    u"\u0434\u0432\u0430\u043d\u0430\u0439\u0441\u0435\u0442": 12,
}
_ORD_END = [u"\u0438", u"\u0430", u"\u043e", u"\u0438\u044f\u0442", u"\u0438\u044f",
====
                add(form.split(u" "))
    return words, tokens, phrases


class Rec(object):
    def __init__(self, h, bundle=u"", ordinal=-1):
        self.name = h["name"]
        self.kind = h["kind"]
        self.zone = h["zone"]
        self.status = h.get("status") or ""
        self.lat = h["lat"]
        self.lon = h["lon"]
        self.ntk = [t.s for t in place_tokens(self.name)]
        self.nset = set(self.ntk)
        self.ktk = [t.s for t in place_tokens(self.kind)]
        # ЛОТ 1в-В: the three TYPED fields of the delivery, each with its own
        # token set and its own phrase set. `zone` is only the compat label now.
        self.quarter = h.get("quarter") or None
        self.district = h.get("district") or None
        self.locality = h.get("locality") or None
        self.p7 = []
        self.qtk = self._loc_tokens(u"quarter", self.quarter)
        self.ltk = self._loc_tokens(u"locality", self.locality)
        self.qph = self._loc_phrases(u"quarter", self.quarter)
        self.lph = self._loc_phrases(u"locality", self.locality)
        self.dph = self._loc_phrases(u"district", self.district)
        self.bundle = bundle                              # „hotels“ | „places“
        self.ordinal = ordinal                            # its row in THAT bundle
        self.legacy, self.legtk, self.gph = legacy_of(bundle, ordinal)
        # The token set the matcher reads as „zone/kind“: kind + quarter +
        # locality + the row's own legacy words. The DISTRICT is deliberately
        # out of it — „младост“ must not filter every school of the district
        # through A3′; the district has a branch of its own (план §3ж S3).
        self.zkset = set(self.qtk) | set(self.ltk) | set(self.legtk) | set(self.ktk)
        self.kkey = " ".join(self.ktk)
        # A6: old_names are NAME TOKENS, minus <=2 chars and address markers.
        # ЛОТ 1в А4 т. 1: minus the generic geographic words as well — the class
        # words stay, which is what puts the ВВМУ first on „военноморско училище“.
        # D1/D3: the alias STRINGS and their sources travel with the record, so the
        # index below can key the whole phrase and the card can name its source.
        self.old_names = list(h.get("old_names") or [])
        self.old_src = list(h.get("old_names_src") or [])
        self.aset = set()
        for o in self.old_names:
            for t in place_tokens(o):
                if t.num:
                    continue
                if len(t.orig) <= 2 or t.orig in ADDR:
                    continue
                if t.s in ALIAS_GENERIC:
                    continue
                self.aset.add(t.s)
        # ЛОТ 1в-Б (ADR 008 D6, план §2г S4): the ORDERED street phrase and the
        # house number as the DELIVERY wrote them. 1:1 with the client, and OUTSIDE
        # nset/aset/zkset — the name path and П7 neither see them nor are moved
        # by them. The client does not parse `text` either; both read these fields.
        _addr = h.get("address") or None
        self.address = _addr
        self.spk = key_of(_addr["street_phrase"]) if _addr else u""
        self.hkey = key_of(_addr["house_key"]) if _addr else u""
        dy = (self.lat - CENTER[0]) * 110574.0
        dx = (self.lon - CENTER[1]) * 81152.0
        self.dist = math.hypot(dx, dy)

    def _loc_tokens(self, cls, field):
        """Own tokens of a typed field + the ACCEPTED aliases of its code.

        П7 step (ж) survives whole: an alias token that touches a NAME token of
        THIS record (exact, prefix or fuzzy) is dropped for this record alone,
        so a location word can never displace the name path."""
        if not field:
            return []
        out = [t.s for t in place_tokens(field.get("name") or u"")]
        for t in LOC_EXTRA.get(cls, {}).get(field.get("code"), ()):
            if any(name_quality(t, v) > 0 for v in self.ntk):
                continue
            if t.s not in out:
                out.append(t.s)
                if cls == u"quarter":
                    self.p7.append(t.s)
        return out

    def _loc_phrases(self, cls, field):
        """The phrase forms of a typed field — {} when the field is null."""
        if not field:
            return set()
        return set(LOC_PHRASES.get(cls, {}).get(field.get("code")) or set())


# Phase 2: ONE index, two deliveries. `kind` carries the class of every record
# (hotels: 4 kinds; places: school/university/hospital/DKC/hospice/kindergarten).
# Nothing else in the matcher knows which file a row came from.
RECS = ([Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
        + [Rec(p, u"places", n) for n, p in enumerate(places2)])

# ЛОТ 1, decision 2 — the exact-CURRENT-name index: joined name tokens -> records.
# old_names stay out of it on purpose (measured: 0 old-name keys coincide with a
# populated category key, and a global alias index would wake „ИУ“/„МУ“).
EXACT_NAME = {}
for _rec in RECS:
    EXACT_NAME.setdefault(u" ".join(_rec.ntk), []).append(_rec)


• MARKERS: "св." or "св" (not followed by a letter) → " свети ". So "ж.к. Св. Иван Рилски" → "ж к свети иван рилски" → tokens: zh, k, sveti, ivan, rilski. All significant except zh, k. So filtered R7 = [sveti, ivan, rilski] — all significant → M7 fires → matches qtk of "кв. Св. Иван Рилски" whose tokens = place_tokens(name) = kv, sveti, ivan, rilski + aliases. So expected 4 rows with 2 having code sv_ivan_rilski. Plausible.

  Now write the measurement script. I'll create a Python script via heredoc (read-only, no disk writes — heredoc pipes to python stdin, no files written; PYTHONDONTWRITEBYTECODE=1 prevents pyc).

  The script:

  ```python
  import json, pathlib, copy, sys
  sys.dont_write_bytecode = True

  ROOT = pathlib.Path.cwd()  # working dir
  src = pathlib.Path("recall_sweep.py").read_text(encoding="utf-8")

  def load(tag, data_dir):
      patched = (src
          .replace('HOTELS = str(REPO_ROOT / "data" / "hotels.json")', 'HOTELS = r"%s"' % (data_dir/"hotels.json"))
          ...)
  ```

  Careful with backslashes on Windows paths in exec'd code: use as_posix().

  Patch lines:
  - `HOTELS = str(REPO_ROOT / "data" / "hotels.json")` → `HOTELS = "<abs posix>"`
  - same PLACES2, CATS.

  Also REPO_PARITY_OUT points to REPO_ROOT/scratch/... — but writes only happen in main; safe.

  Exec: 
  ```python
  mod = types.ModuleType("rs_"+tag)
  mod.__file__ = str(pathlib.Path("recall_sweep.py").resolve())
  exec(compile(patched, mod.__file__, "exec"), mod.__dict__)
  ```

  Then reindex function replicating test_granitsi_fixtures.reindex using module attributes.

  Queries measurement helper:

  ```python
  def measure(mod, q, ops=()):
      hotels = json.loads(pathlib.Path(mod.HOTELS).read_text(encoding="utf-8"))["hotels"]
      places = json.loads(pathlib.Path(mod.PLACES2).read_text(encoding="utf-8"))["places"]
      if ops: apply ops
      reindex(mod, hotels, places)
      rows, branch = mod.search(q)
      ...
      reindex back
  ```

  Since exec of module already built RECS from the files, and reindex is needed only for mutations. For plain queries, module is ready.

  Variant B patch: create second source variant with the M7 branch patched:

  ```
  old_block = """    if not has_key and bare_location_query(R):"""
  new_block = """    R7 = [t for t in R if t.s not in M7_LETTER_PREFIXES]
      if not has_key and R7 and bare_location_query(R7):"""
  ```
  and inside the block, `bare = bare_location_rows(R, cls)` → `bare = bare_location_rows(R7, cls)`.

  Define M7_LETTER_PREFIXES by injecting before use: add line `M7_LETTER_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i")` — but M7_PREFIXES is defined at line 3093, AFTER search definition at 1228. Since it's used at call time (inside function), module-level name just needs to exist before search() is called. But my patched line `R7 = ...` references M7_LETTER_PREFIXES at call time — fine, as long as the name is defined by module exec end. I'll append a definition at the end of the patched source, or define near the patch: since exec runs top to bottom, defining at end is fine for runtime calls. I'll append `\nM7_LETTER_PREFIXES = (...)` at the end. But careful: `if __name__ == "__main__"` at end might call main()? Let me check the tail of the file. Line 3782 def main, and module ends at 4334. Check whether main() is invoked at import.            pathlib.Path(REPO_PARITY_OUT).write_text(_parity_text, encoding="utf-8",
                                                     newline=chr(10))
            return u"FREEZE: паритет на токенизатора -> %s" % REPO_PARITY_OUT

        _code, _written = freeze_writes(blockers, [_write_reference,
                                                   _write_expectations,
                                                   _write_parity])
        if _code:
            return _code

    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
====
1761:    Same shape and same fail-loud contract as check_p7_gate(): main() exits 1 on
1813:    Same fail-loud contract as check_p7_gate()/check_lot1_gate(): main() exits 1
2168:    Р7: this is what makes the reference able to FAIL. main() exits 1 on any
2342:# main() refuses to write an artefact whose keys are not exactly this list.
2385:    reference (main() passes nothing when it writes the tracked file)."""
2675:    It was inline in main() until F12-в: the two manifests have to build the
3782:def main():
4334:    sys.exit(main())
Good — main() only under __main__; exec with a module whose __name__ != "__main__" won't run it. 

  Now write the big measurement script. One script, several phases, all in-memory. Print results compactly.

  Key queries & checks:

  Phase 0 (new_data, unpatched): baseline numbers
  - кв. Левски / кв. Тракия / кв. Христо Ботев / ж.к. Св. Иван Рилски → branch, n, count with code
  - левски → n, with kv_levski
  - възраждане → 5 + names; възраждане 2 → 0; ж.к. възраждане 2 → 0; младост 2 → 0
  - чайка → 30 (split by code)
  - аспарухово → 16 (9/7), ЦДГ 43 Пинокио absent; дружба → 2
  - бриз → 4 + names/codes
  - младост → 20 (8/12); училище младост → 6 (3); училище район младост → 12 (9)
  - P7_ADDED, tokens, zones, records_touched, foreign_guard for new
  - location_alias_tokens for quarter dict: dropped["druzhba"] contains foreign:asparuhovo:asparuhovo

  Phase 1 (variant B patched): the four queries + възраждане 2/младост 2 → expect 14/12, 4/4, 4/3, 4/2, 0, 0.

  Phase 2 (variant with numbers): възраждане 2 → 5, младост 2 → 20.

  Phase 3 (mutations on new_data, unpatched engine):
  - Fixture 6: ДГ№34 „Лястовичка“ → quarter {name:"ж.к. Лястовиче", code:"vazrazhdane1", src:"SIGNED_POLYGON"}, zone "ж.к. Лястовиче" → "възраждане" 4, queries б/в still 0.
    - Also code-only mutation (vazrazhdane1_new) → still 5 (prove fixture needs name change) — plan documents this; verify.
  - Fixture 7: 10 ops renaming chaika_kv rows (name+zone) → "чайка" 21; name-only variant → ? (plan claims 21 too, K28 claimed 20 for name-only). Measure both. Which 10 rows: find rows with quarter.code == chaika_kv in both bundles.
  - Fixture 8: ЦДГ 43 "Пинокио" → quarter {name:"кв. Аспарухово", code:"druzhba", src:"SIGNED_POLYGON"}, zone "кв. Аспарухово" → "аспарухово" 17, "дружба" 1.

  Phase 4 (old_data): младост → 28 names; diff vs new 20 names → the 8 lost; check each lost row's new quarter code (from new places.json); P7 old: tokens 2, zones 2, records 48; foreign_guard old has vladislav/varnenchik; new foreign_guard — do they disappear? And check new cats aliases contain gratska, gratski, varnenchik, vladislav, vasil.

  Also for P7: plan claims 5 NEW tokens vs signed expectations: gratska, gratski, varnenchik, vladislav, vasil. Signed p7.added = {konstanin, zhkizgrev}. New P7_ADDED = 7 tokens in 5 zones. So new tokens beyond signed: gratska, gratski (Гръцката махала), varnenchik, vladislav (Владиславово), vasil (Левски) = 5. Verify.

  Also check old place_categories aliases: did old cats have gratska alias for Гръцката махала but it was dropped as foreign? Old P7_ADDED only had 2 zones. In old data, Гръцката махала might not be a zone at all (zones 20→28). New zones = 28 (includes new quarter names as zones since zone==quarter.name). Гръцката махала is a new zone in new data. OK just measure.

  Note: `hotels` and `places2` and `cats` are module-level variables loaded from the patched paths. Let me check how module loads them — grep "hotels = " near 680-692.            if t.s not in out:
                out.append(t.s)
                if cls == u"quarter":
                    self.p7.append(t.s)
        return out

    def _loc_phrases(self, cls, field):
        """The phrase forms of a typed field — {} when the field is null."""
        if not field:
            return set()
        return set(LOC_PHRASES.get(cls, {}).get(field.get("code")) or set())


# Phase 2: ONE index, two deliveries. `kind` carries the class of every record
# (hotels: 4 kinds; places: school/university/hospital/DKC/hospice/kindergarten).
# Nothing else in the matcher knows which file a row came from.
RECS = ([Rec(h, u"hotels", n) for n, h in enumerate(hotels)]
        + [Rec(p, u"places", n) for n, p in enumerate(places2)])

# ЛОТ 1, decision 2 — the exact-CURRENT-name index: joined name tokens -> records.
# old_names stay out of it on purpose (measured: 0 old-name keys coincide with a
# populated category key, and a global alias index would wake „ИУ“/„МУ“).
EXACT_NAME = {}
for _rec in RECS:
    EXACT_NAME.setdefault(u" ".join(_rec.ntk), []).append(_rec)
258:cats = json.load(open(CATS, encoding="utf-8"))
259:hotels = json.load(open(HOTELS, encoding="utf-8"))["hotels"]
260:places2 = json.load(open(PLACES2, encoding="utf-8"))["places"]
2016:        _EXPECTATIONS = (json.loads(path.read_text(encoding="utf-8"))
2511:            doc = json.loads(got.stdout.decode("utf-8"))
2526:    base_doc = json.loads(pathlib.Path(REPO_ROWS_OUT).read_text(encoding="utf-8"))
2880:        doc = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
2926:    base_doc = json.loads(pathlib.Path(REPO_ROWS_OUT).read_text(encoding="utf-8"))
3179:        doc = (json.loads(pathlib.Path(str(REPO_ROOT / rel)).read_text(encoding="utf-8"))
3207:    return json.loads(got.stdout.decode("utf-8"))
3685:    artefact_doc = json.loads(artefact_text)
3770:        old = json.loads(path.read_text(encoding="utf-8"))
4276:                _sig = ((json.loads(_p.read_text(encoding="utf-8")).get("_meta") or {})
The paths are used at lines 258-260. I'll patch the constants at 73-75.

  Now write the measurement script. It's long; run it via heredoc with PYTHONIOENCODING=utf-8 and PYTHONDONTWRITEBYTECODE=1.

  Let me write carefully.

  ```python
  import json, pathlib, types, copy, sys

  sys.dont_write_bytecode = True
  ROOT = pathlib.Path.cwd()
  SRC = (ROOT / "recall_sweep.py").read_text(encoding="utf-8")

  def patch_paths(src, data_dir):
      d = data_dir.resolve().as_posix()
      out = src.replace(
          'HOTELS = str(REPO_ROOT / "data" / "hotels.json")',
          'HOTELS = "%s/hotels.json"' % d)
      out = out.replace(
          'PLACES2 = str(REPO_ROOT / "data" / "places.json")',
          'PLACES2 = "%s/places.json"' % d)
      out = out.replace(
          'CATS = str(REPO_ROOT / "data" / "place_categories.json")',
          'CATS = "%s/place_categories.json"' % d)
      return out

  def load(tag, src):
      mod = types.ModuleType(tag)
      mod.__dict__["__file__"] = str((ROOT / "recall_sweep.py").resolve())
      exec(compile(src, mod.__file__, "exec"), mod.__dict__)
      return mod
  ```

  Watch: module code does `sys.stdout.reconfigure(encoding="utf-8")` — ok.

  Variant B patch:
  ```
  old = "    if not has_key and bare_location_query(R):"
  new = ("    R7 = [t for t in R if t.s not in M7_LETTER_PREFIXES]\n"
         "    if not has_key and R7 and bare_location_query(R7):")
  assert SRC.count(old) == 1
  ```
  and `        bare = bare_location_rows(R, cls)` → `        bare = bare_location_rows(R7, cls)` (count==1).
  Then append: `M7_LETTER_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i")`.

  Variant A′ (numbers too): use M7_PREFIXES full list — but M7_PREFIXES defined at 3093, after search def but before any call; fine at call time. Patch same lines with t.s not in M7_PREFIXES.

  reindex replication:
  ```
  def reindex(mod, hotels, places):
      mod.hotels = hotels; mod.places2 = places
      mod.RECS = ([mod.Rec(h, "hotels", n) for n,h in enumerate(hotels)] + [mod.Rec(p,"places",n) for n,p in enumerate(places)])
      mod.EXACT_NAME = {}
      for rec in mod.RECS: mod.EXACT_NAME.setdefault(" ".join(rec.ntk), []).append(rec)
      mod.EXACT_ALIAS = {}
      for rec in mod.RECS:
          for index, old in enumerate(rec.old_names):
              key = mod.key_of(old)
              if not key: continue
              bucket = mod.EXACT_ALIAS.setdefault(key, [])
              if not any(other is rec for other,_i in bucket): bucket.append((rec,index))
      mod.STREET = {}
      for rec in mod.RECS:
          if rec.spk: mod.STREET.setdefault(rec.spk, []).append(rec)
      mod.CLASS_OF = {}
      for form_key in mod.FORM_IDX:
          mod.CLASS_OF[form_key] = [r for r in mod.RECS if mod.in_class(r, form_key)]
      mod.GROUP_SIZE = {}
      for rec in mod.RECS:
          g = mod.group_of(rec); mod.GROUP_SIZE[g] = mod.GROUP_SIZE.get(g,0)+1
  ```

  Wait: Rec construction uses module-level globals like LOC_EXTRA, legacy_of(bundle, ordinal) — legacy_of reads module-level LEGACY dict presumably keyed bundle:ordinal; using mod.Rec uses mod globals — fine since data unchanged.

  answer():
  ```
  def base(mod):
      h = json.loads(pathlib.Path(mod.HOTELS).read_text(encoding="utf-8"))["hotels"]
      p = json.loads(pathlib.Path(mod.PLACES2).read_text(encoding="utf-8"))["places"]
      return h, p

  def apply_ops(h, p, ops): (as in test)

  def answer(mod, q, ops=()):
      h, p = base(mod)
      if ops: h, p = apply_ops(h, p, ops)
      reindex(mod, h, p)
      rows, branch = mod.search(q)
      res = {"branch": branch, "n": len(rows),
             "with_code": {},
             "names": [(r.name, r.zone, (r.quarter or {}).get("code")) for r in rows]}
      reindex(mod, *base(mod))
      return res
  ```

  For code counts: count rows where r.quarter and r.quarter["code"] == target.

  Note: search uses module-level RECS, CLASS_OF etc. — reindex sets them. Also GROUP_SIZE, STREET, EXACT_ALIAS, EXACT_NAME. OK.

  Now queries.

  For "count with code": I'll print n and per-code counts.

  Also old vs new "младост" names diff.

  P7 for old and new modules: mod.P7_ADDED, sum tokens, len zones, records_touched = sum(1 for r in mod.RECS if r.p7), foreign_guard = mod.measure_p7()["foreign_guard"] (measure_p7 is module function — check it's not inside main; it's a def at module level, yes ~3439).

  Also check dropped for druzhba: mod.location_alias_tokens(mod.LOC_DICTS? ...). How are LOC_EXTRA/LOC_PHRASES built? There's location_dicts(cats_doc) and location_alias_tokens(entries). Module-level probably LOC_DICTS = location_dicts(cats) and LOC_EXTRA etc. Let me just call: entries = mod.location_dicts(mod.cats)["quarter"]; extra, added, dropped = mod.location_alias_tokens(entries); print dropped.get("druzhba"). Also check whether "Аспарухово" is an alias of druzhba in new cats.

  Also verify new cats quarter aliases contain the 5 tokens: zones? No — P7_ADDED is about zones (flat zones list), keys are zone names like "Гръцката махала". The plan's §9 т.17 wording: "Новият речник добавя 5 нови токена (gratska, gratski, varnenchik, vladislav, vasil)". These are P7 zone aliases. Let me diff old vs new cats["zones"] aliases directly too.

  Also verify counts: zones 20→28 (ZONES_IN from records). new P7 zones 5, tokens 7, records 64; old 2/2/48.

  Now the "чайка" fixture-7 measurement. Find all rows with quarter code chaika_kv:
  ops name-only: set quarter.name = "кв. Крайморие" (keep code chaika_kv, src). 
  ops name+zone: also zone = "кв. Крайморие".
  Plan keeps code "chaika_kv"? Plan says: каждый получава quarter.name и zone = "кв. Крайморие" — code unchanged (chaika_kv). OK.

  Then "чайка" → count. Expect 21 both variants per plan (K28 said 20 name-only).

  Also fixture 6 code-only variant: set quarter {name:"ж.к. Възраждане 1", code:"vazrazhdane1_new", src:"SIGNED_POLYGON"} (zone unchanged? K28 said zone also changed? K28 measured "връща 5" for code mutation with quarter name unchanged... The v2 mutation changed only code. Measure: expect 5 still).

  Also baseline "възраждане" 5 names should match the 5 listed: ДГ 29 „Звънче“, ДГ 31 „Крилатко“, II ОУ „Никола Йонков Вапцаров“, ДГ 33 „Делфинче“, ДГ№34 „Лястовичка“.

  Fixture 8: ЦДГ 43 "Пинокио" — need exact name in data: 'ЦДГ 43 "Пинокио"'. Check existence.

  Also verify K28-1: "кв. Христо Ботев" 24 rows, exactly 1 with code hristo_botev, named ЦДГ 8 - Христо Ботев.

  Also §8 proba 5 "бриз" 4 rows named: ПАРК ХОТЕЛ БРИЗ (zlatni_pyasatsi by name), IV ЕГ Жолио Кюри (briz new), ПГ „Д. И. Менделеев“ (briz new), Камелия (briz).

  Also К28-3: verify 8 lost names + new quarters match table.

  Also verify "левски" 14/12.

  Also plan 1.8.5: „левски“ M7-bare 14, 12 с kv_levski. §9 т.1 variant B claims кв. Левски → 14 (12 with kv_levski) — same as голо левски.

  Let me now also double check `in_class`, `FORM_IDX`, `key_of`, `group_of` exist at module level. reindex in test uses them, so yes.

  One more: variant B — "ж.к. Св. Иван Рилски": tokens after markers: "ж.к." → norm → "ж к" → zh, k; "Св." → "свети" → sveti; иван; рилски. R7 = [sveti, ivan, rilski]. bare_location_rows: quarter_hit: rows whose qtk contains sveti, ivan, rilski. qtk of rows in "кв. Св. Иван Рилски" — place_tokens(name) of quarter name "кв. Св. Иван Рилски" → kv, sveti, ivan, rilski. Rows with that quarter: expect 2 (ДГ№53 Слънчево зайче, ОУ Отец Паисий). Plus head (name_has_phrase) and district_hit. Plan expects 4 total, 2 with code. Which other 2? Possibly ОУ „Свети Иван Рилски" (name contains phrase: sveti ivan rilski in ntk) and СУ? Name "ОУ „Свети Иван Рилски"" → tokens ou?, sveti, ivan, rilski — name_has_phrase checks if phrase in name tokens presumably. That row is in район Младост. So head = 1 row + quarter_hit 2 + maybe ДКЦ? Total 4 plausible.

  Now write and run the script. It'll be long — that's fine. Print compactly.

  Also need "with_code" counts per query: count by quarter code.

  Edge: `search` may print to stdout (module prints during import? The import itself may print things — measure functions print only in main. Import might print nothing. But exec might produce output like gates? No, gates run in main. Good.

  Also make sure patched module doesn't accidentally write: REPO_PARITY_OUT only in main; line 3073 path.write_text inside a function (freeze-related). OK.

  Let me write the script now. To keep it manageable I'll do it in two runs: run 1 = baselines + P7 + K28 checks; run 2 = variants B/A′ + mutations. Actually combine, it's fine, but output could be long. Keep prints terse.

• Модулът не пише при import (`main()` е само под `__main__`). Пускам първото in-memory измерване — базови числа върху `new_data/`.кв. Левски               -> M3                 n=4   with kv_levski: 0 | codes={'asparuhovo': 1, '-': 2, 'vladislavovo': 1}
кв. Тракия               -> M3                 n=1   with trakia: 0 | codes={'dolna_traka': 1}
кв. Христо Ботев         -> M3                 n=24  with hristo_botev: 1 | codes={'asparuhovo': 1, 'hristo_botev': 1, '-': 7, 'vladislavovo': 1, 'kolhozen_pazar': 1, 'tsentar': 1, 'kk_konstantin_elena': 2, 'chaika_kk': 1, 'zlatni_pyasatsi': 9}
ж.к. Св. Иван Рилски     -> M3                 n=22  with sv_ivan_rilski: 0 | codes={'-': 9, 'asparuhovo': 3, 'pobeda': 1, 'mladost2': 1, 'kk_konstantin_elena': 3, 'tsentar': 1, 'vladislavovo': 1, 'hristo_botev': 1, 'zlatni_pyasatsi': 2}
левски                   -> M7-bare-location   n=14  with kv_levski: 12 | codes={'-': 1, 'asparuhovo': 1, 'kv_levski': 12}
възраждане             -> M7-bare-location   n=5   codes={'vazrazhdane': 3, 'vazrazhdane2': 1, 'vazrazhdane1': 1}
възраждане 2           -> M3                 n=0   codes={}
ж.к. възраждане 2      -> M3                 n=0   codes={}
младост 2              -> M3                 n=0   codes={}
чайка                  -> M7-bare-location   n=30  codes={'chaika_kv': 10, '-': 1, 'chaika_kk': 19}
аспарухово             -> M7-bare-location   n=16  codes={'asparuhovo': 9, '-': 7}
дружба                 -> M7-bare-location   n=2   codes={'kv_levski': 1, 'druzhba': 1}
бриз                   -> M7-bare-location   n=4   codes={'zlatni_pyasatsi': 1, 'briz': 3}
младост                -> M7-bare-location   n=20  codes={'-': 12, 'mladost2': 3, 'mladost': 5}
училище младост        -> A3-location        n=6   codes={'mladost': 1, 'mladost2': 2, '-': 3}
училище район младост  -> A3-district        n=12  codes={'pobeda': 3, '-': 3, 'sv_ivan_rilski': 1, 'troshevo': 1, 'mladost': 1, 'mladost2': 2, 'vazrazhdane2': 1}
възраждане names: ['ДГ 29 "Звънче"', 'ДГ 31 "Крилатко"', 'II ОУ „Никола Йонков Вапцаров“', 'ДГ 33 „Делфинче“', 'ДГ№34 „Лястовичка“']
бриз names: [('ПАРК ХОТЕЛ БРИЗ', 'zlatni_pyasatsi'), ('IV ЕГ Жолио Кюри', 'briz'), ('Професионална гимназия по химични и хранително-вкусови технологии "Д. И. Менделеев"', 'briz'), ('Камелия', 'briz')]
кв.ХристоБотев hristo_botev rows: ['ЦДГ 8 - Христо Ботев']
аспарухово has Пинокио: False | no-quarter: 7
чайка split: {'chaika_kv': 10, '-': 1, 'chaika_kk': 19} | no-quarter rows: ['„ДКЦ Чайка“ ЕООД']
младост old=28 new=20 lost=8: ['ОУ „Иван Вазов“', 'Професионална гимназия по електротехника', 'Професионална Техническа Гимназия', 'ДГ№53 „Слънчево зайче“', 'ОУ Отец Паисий', 'ДГ№26 „Изворче"', 'ОУ Добри Чинтулов', 'ДГ 24 "Детско градче"']
   ОУ „Иван Вазов“ -> pobeda | ж.к. Победа
   Професионална гимназия по електротехника -> pobeda | ж.к. Победа
   Професионална Техническа Гимназия -> pobeda | ж.к. Победа
   ДГ№53 „Слънчево зайче“ -> sv_ivan_rilski | кв. Св. Иван Рилски
   ОУ Отец Паисий -> sv_ivan_rilski | кв. Св. Иван Рилски
   ДГ№26 „Изворче" -> troshevo | кв. Трошево
   ОУ Добри Чинтулов -> troshevo | кв. Трошево
   ДГ 24 "Детско градче" -> troshevo | кв. Трошево


• Excellent — all baseline numbers confirmed: 1.8.4 (4/1/24/22, 1 code row for Христо Ботев), 1.8.5 (14/12), 1.8.6 (0/0/0), 1.8.7 (30 = 19+10+1), 1.8.8 (16 = 9+7, без Пинокио; дружба 2), бриз 4 with the named rows, младост 20 (8/12), училище младост 6 (3 с квартал), училище район младост 12 (9 с квартал — codes show 9 non-"-": 3+1+1+1+2+1 = 9 ✓). The 8 lost rows match §1.7 exactly with the right new quarters.

  Note "училище младост" codes: mladost 1, mladost2 2, - 3 → 3 с квартал ✓.

  Now variant B and variant with numbers, then mutations, then P7.=== Вариант Б (само буквени префикси) ===
кв. Левски               -> M7-bare-location   n=14  with kv_levski: 12
кв. Тракия               -> M7-bare-location   n=4   with trakia: 4
кв. Христо Ботев         -> M7-bare-location   n=4   with hristo_botev: 3
ж.к. Св. Иван Рилски     -> M7-bare-location   n=4   with sv_ivan_rilski: 2
възраждане 2             -> M3                 n=0
младост 2                -> M3                 n=0
ж.к. възраждане 2        -> M3                 n=0
=== Вариант А′ (и числата 1/2) — §13 т.5 ===
възраждане 2             -> M7-bare-location   n=5
младост 2                -> M7-bare-location   n=20
ж.к. възраждане 2        -> M7-bare-location   n=5
Variant B confirmed exactly: 14/12, 4/4, 4/3, 4/2, and детските заявки остават 0. Variant A′ confirmed: възраждане 2 → 5 (родителя), младост 2 → 20.

  Note: plan §9 т.1 says variant A′ gives "5 and 20" — confirmed. Also §13 т.5 confirmed.

  Now mutations (fixtures 6, 7, 8) and P7 counts.F6 code-only: възраждане -> ('M7-bare-location', 5)
F6 name-mut:  възраждане -> ('M7-bare-location', 4)
F6 name-mut:  възраждане 2 -> ('M3', 0) | ж.к. възраждане 2 -> ('M3', 0)
chaika_kv rows (10):
   [hotels] АМИРАЛ
   [places] Математическа гимназия „Доктор Петър Берон“
   [places] ОУ "Г.С.Раковски"
   [places] ОУ "Захари Стоянов"
   [places] Спортно училище Георги Бенковски
   [places] 4 ОДЗ Чайка
   [places] ДГ№21 „Калина Малина“
   [places] ДГ№22 „Мечо Пух“
   [places] Оздравителна Детска Градина №9 "Ален Мак"
   [places] ДЯ №2 „Моряче“
F7 name+zone: чайка -> M7-bare-location 21 | survivors: ['4 ОДЗ Чайка', '„ДКЦ Чайка“ ЕООД']
F7 name-only: чайка -> M7-bare-location 21
Пинокио row: [('ЦДГ 43 "Пинокио"', 'ж.к. Дружба', 'druzhba')]
F8: аспарухово -> ('M7-bare-location', 17) | дружба -> ('M3', 1)
druzhba aliases in dict: {'name': 'ж.к. Дружба', 'aliases': ['ж.к. Дружба-Аспарухово', 'Дружба']}
dropped[druzhba]: ['short:zh', 'short:k', 'own:druzhba', 'foreign:asparuhovo:asparuhovo']
All confirmed:
  - F6: code-only mutation → still 5 (fixture wouldn't fail); name mutation → 4; б/в stay 0. ✓
  - F7: the 10 rows match the plan's by-name list exactly (АМИРАЛ in hotels + 9 places). 30→21 in both variants (name-only and name+zone). ✓ Plan §13 т.3 says 21 for both — correct; K28's "20" for name-only was wrong (K28 itself admitted 21 with zone). ✓ Survivors: 19 chaika_kk + 4 ОДЗ Чайка (name) + ДКЦ Чайка = 21 ✓.
  - F8: mutation gives аспарухово 16→17, дружба 2→1 ✓ — real change, fixture fails. Alias path impossible: dropped["druzhba"] includes "foreign:asparuhovo:asparuhovo" ✓.

  Wait — "дружба" after mutation → branch M3, n=1. Today it's M7-bare-location n=2. So the branch changed too — fixture fails on branch and n. Fine.

  Now P7_ADDED old vs new and the cats diff. Also records_touched 48→64, foreign_guard changes.

• Всички мутации потвърдени. Остава P7_ADDED дрейфът (О28) — стар срещу нов речник.OLD: tokens=2 zones=2 records_touched=48
  added: {"к.к. Св. Св. Константин и Елена": ["konstanin"], "кв. Изгрев": ["zhkizgrev"]}
  foreign_guard: [{"zone": "ж.к. Дружба", "token": "asparuhovo", "tag": "foreign:asparuhovo:asparuhovo"}, {"zone": "кв. Владиславово", "token": "vladislav", "tag": "foreign:vladislav:vladislav"}, {"zone": "кв. Владиславово", "token": "varnenchik", "tag": "foreign:varnenchik:varnenchik"}]
  zones_in: 25
NEW: tokens=7 zones=5 records_touched=64
  added: {"Гръцката махала": ["gratska", "gratski"], "к.к. Св. Св. Константин и Елена": ["konstanin"], "кв. Владиславово": ["varnenchik", "vladislav"], "кв. Изгрев": ["zhkizgrev"], "кв. Левски": ["vasil"]}
  foreign_guard: [{"zone": "ж.к. Дружба", "token": "asparuhovo", "tag": "foreign:asparuhovo:asparuhovo"}]
  zones_in: 32
SIGNED p7: tokens=2 zones=2 records_touched=48
  signed added: {"к.к. Св. Св. Константин и Елена": ["konstanin"], "кв. Изгрев": ["zhkizgrev"]}
  signed foreign_guard tokens: ['asparuhovo', 'varnenchik', 'vladislav']
new beyond signed: ['gratska', 'gratski', 'varnenchik', 'vasil', 'vladislav']
zone 'Гръцката махала': +['Гръцка махала', 'Гръцки квартал', 'кв. Гръцки квартал'] -[]
zone 'кв. Левски': +['Васил Левски', 'Левски', 'кв. Васил Левски'] -[]
zone 'кв. Св. Иван Рилски': +['ж.к. Св. Иван Рилски', 'кв. Свети Иван Рилски'] -[]
zone 'кв. Тракия': +['Тракия'] -[]


• P7 confirmed: OLD matches signed expectations exactly (2/2/48, same added, same foreign_guard). NEW: 7 tokens / 5 zones / 64 records; new beyond signed = gratska, gratski, varnenchik, vasil, vladislav — exactly the 5 the plan names. foreign_guard shrinks to only asparuhovo — vladislav/varnenchik no longer rejected. All plan claims verified.

  One caveat: plan 1.8.17 says "засегнати записи 48 → 64" ✓.

  Also plan 1.5 says zones 20→28 in the dictionary — I measured ZONES_IN 25→32 (that's distinct zone strings in records, different thing). Dictionary zones count: len(oz) vs len(nz) — didn't print but plan claims 20→28; minor. Not required.

  Now mark todos done and also double-check a couple of K28 application points in the plan text:

  - К28-1 §1.8.4: plan now says "Поправка на v2 (К28-1): „кв. Христо Ботев“ носи ЕДИН ред с търсения код — ЦДГ 8 - Христо Ботев (hristo_botev), и то по ИМЕ" — verified: 24 rows, 1 with code (ЦДГ 8 - Христо Ботев) ✓. Other three zero ✓.
  - К28-2: §3.5 fixture 6 with name mutation, measured 5→4, code-only proven not to fail (still 5); assert_case multi-query with fails_on ✓ (textually present at §3.5 lines 440-455, 463-464).
  - К28-3: §1.7 names 8 rows with new quarters ✓ verified by measurement; STOP 19 requires 8 delta rows ✓; §4 step 11 lists them ✓.
  - К28-4: §8 proba 5 „бриз“ 4 rows named ✓ verified.
  - К28-5: §9 т.1 variant B with measured numbers ✓ verified exactly (14/12, 4/4, 4/3, 4/2, zeros stay 0). Client parity cost honestly named (client has no M7_PREFIXES — confirmed by index_M7_branch.txt: no prefix list; recall_sweep_excerpts confirm M7_PREFIXES at ~3093).
  - К28-6: О22 records semantics of 138 (lost/changed definitions, 44+44+39+11) and §4 step 2 requires the f06ac06↔f00dd78 diff (150) ✓ textually. Cannot verify coverage numbers here (no gates/coverage.py, no f06ac06 blobs) — but the semantic fix is what's checkable; also internal consistency: 108+30=138 ✓ arithmetic.
  - К28-7: fixture 7 enumerates 10 ops by name ✓ — and the 10 names measured to exist exactly (each op hits exactly 1 row — my apply_ops asserted that). Number 21 (not 20) ✓ measured both variants 21.

  Fixture 8: plan found working mutation (Пинокио op) → аспарухово 16→17, дружба 2→1, fails ✓. Alias route proven dead: dropped["druzhba"] contains "foreign:asparuhovo:asparuhovo" ✓ (plan §3.5 row 8 cites recall_sweep.py:477 (д)/(д′) — measured true).

  О28/P7: 5 new tokens ✓, 7 tokens/5 zones ✓, 48→64 ✓, foreign_guard had vladislav/varnenchik as rejected and new dictionary admits them ✓.

  Minor discrepancies worth noting:
  1. §1.8.21/§9 т.1 claims "кв. Левски 4 → 14 (12 с kv_levski)" — today "кв. Левски" is 4 rows all CHUZHDI (0 with kv_levski); measured variant B: 14/12 ✓.
  2. ZONES_IN measured 25→32 (record zone strings), while plan §1.5 says dictionary zones 20→28 — different metric, no contradiction; I didn't verify dictionary zones count. Actually let me quickly check len(oz), len(nz)? Not printed. Plan §1.5: "Речник: зони 20→28, псевдоними 39→48". I could verify quickly but it's tangential to the K28 conditions. K28 already confirmed 20→28. Skip — or do a tiny check? Cheap: len of zones dicts and alias counts. Let me not run another command... Actually it's one-liner; but I've confirmed all required items. The task asks specifically about the listed items. I'll skip.

  3. One point to check: plan §9 т.1 (Б) says patch points "recall_sweep.py:1257+:1263 (2 реда)". The excerpt shows the M7 branch at those lines. My patch touched exactly the branch gate and the rows call — 2-3 lines. Consistent.

  4. Also verify the client's M7 branch has no prefix list — index_M7_branch.txt confirms (only isSignificantToken check). ✓

  5. О22 semantics — check the plan text: О22 row in §2 and §9 т.9 both record the semantics ("lost" = had named zone/quarter in base, none in candidate; "changed" = had different). ✓. And §4 step 2 includes the f00dd78 diff command with expected exit 2/uncovered 150 ✓.

  Everything checks out. Any remaining doubts?

  - §3.5 fixture 6: plan's mutation sets quarter.name "ж.к. Лястовиче" keeping code vazrazhdane1. My measurement used exactly that: 5→4 ✓, б/в stay 0 ✓.
  - Fixture 7 ops: 10 by name, all hit exactly 1 row ✓ (assert in my apply_ops would have failed otherwise). The plan's list matches the actual 10 rows ✓.
  - The plan claims for fixture 7 "и двата варианта дават 21" — measured ✓.

  One thing to double check: §1.8.4 states today "кв. Тракия" → 1 row which is dolna_traka — measured codes={'dolna_traka': 1} ✓. "кв. Левски" 4 rows: asparuhovo 1, vladislavovo 1, 2 without — plan §8 proba 4 names them: НУ Васил Левски [Аспарухово], ПГ „Васил Левски", ДГ№40 [Владиславово], болница. 4 rows ✓ (I didn't print names but count and codes match).

  Verdict: ГОДНО за подпис. All 7 K28 conditions applied correctly with verified measurements; all five special measurements requested match the plan's claims exactly.

  Word limit: 700 words. Write verdict in Bulgarian, concise. Cite paths relative to the copy root.

• # К29 · Присъда: **ГОДНО за подпис**

  Метод: `recall_sweep.py` е зареден in-memory от изходния си текст с пачнати константи `HOTELS`/`PLACES2`/`CATS` → `new_data/` (и `old_data/` за сравненията); `main()` не е викан (той е само под `if __name__ == "__main__"`, а модулът не пише при import — `test_granitsi_fixtures.py:18` го пинва). Мутациите минават през копие на `reindex()`/`apply_ops()` от `test_granitsi_fixtures.py:67-122`, с твърдението „точно 1 ред на op“. Нула писане по диска.

  **К28-1 · §1.8.4 — приложено и измерено вярно.** „кв. Христо Ботев“ → `M3`, 24 реда, точно **1** с `hristo_botev` (`ЦДГ 8 - Христо Ботев`). Другите три: „кв. Левски“ 4 (0 с кода; asparuhovo/vladislavovo/2 без), „кв. Тракия“ 1 (`dolna_traka`), „ж.к. Св. Иван Рилски“ 22 (0 с кода). Планът носи поправката и в 1.8.4, и в §8 проба 4.

  **К28-2 · фикстура 6 — приложено и измерено.** Код-само мутация (`vazrazhdane1_new` при непипнато име) → „възраждане“ пак **5**, фикстурата НЕ пада. Мутацията по име на `ДГ№34 „Лястовичка“` (`quarter.name`/`zone` = „ж.к. Лястовиче“, кодът запазен) → **5 → 4**; заявки (б) и (в) остават 0 → `fails_on: "възраждане"` е точен. Многозаявъчният `assert_case` е описан в §3.5.

  **К28-3 · §1.7 — измерено поименно.** old→new на „младост“: 28→20, загубените са ТОЧНО осемте изброени, с точните нови квартали (3×`pobeda`, 2×`sv_ivan_rilski`, 3×`troshevo`). STOP 19 и §4 стъпка 11 искат 8 делта-реда.

  **К28-4 · §8 проба 5 — измерено: „бриз“ = 4**, поименно както в плана (ПАРК ХОТЕЛ БРИЗ/`zlatni_pyasatsi`, Жолио Кюри, Менделеев, Камелия — трите с `briz`).

  **К28-5 · §9 т. 1 — вариант Б измерен сам с пач в М7 клона** (`R7 = [t for t in R if t.s not in (k,kv,zh,m,s,o,t,i)]` преди `bare_location_query`/`bare_location_rows`): „кв. Левски“ **4→14 (12 с `kv_levski`)**, „кв. Тракия“ **1→4 (4/4)**, „кв. Христо Ботев“ **24→4 (3/4)**, „ж.к. Св. Иван Рилски“ **22→4 (2/4)** — дословно числата на плана; „възраждане 2“/„младост 2“/„ж.к. възраждане 2“ остават **0** (`M3`). Клиентът наистина няма префиксен списък (`index_M7_branch.txt:9-10` — само `R.every(isSignificantToken)`); цената на паритета е назована честно.

  **К28-6 · О22 — семантиката е записана** (§2 О22 и §9 т. 9: „lost“/„changed“, 44+44+39+11=138; §4 стъпка 2 иска и дифа `f06ac06`↔`f00dd78` = 150, аритметиката 108+30=138 се сгъва). Самите 138/150 не са преизмерими тук (няма `gates/coverage.py` и блобове на `f06ac06` в копието) — това е граница на копието, не на плана.

  **К28-7 · фикстура 7 — измерено.** Десетте `chaika_kv` реда съществуват точно по един веднъж под имената от плана (АМИРАЛ в hotels + 9 в places — всеки op улучва точно 1 ред). Преименуване на всичките 10: **30 → 21 и при име+`zone`, и при само име** — числото 21 на плана е вярното; оцелели: 19 `chaika_kk` + `4 ОДЗ Чайка` (по име) + `„ДКЦ Чайка“ ЕООД`.

  **Специалните измервания:**

  1. **§13 т. 5 — вярно.** С пълния `M7_PREFIXES` (и „1“/„2“): „възраждане 2“ → **5**, „младост 2“ → **20** — детето получава отговора на родителя; отхвърлянето на А′ е измерено правилно.
  2. **§13 т. 3 — вярно** (21, не 20 — вж. К28-7).
  3. **Фикстура 8 — планът е намерил реална мутация.** `ЦДГ 43 "Пинокио"` (днес `druzhba`) с `quarter.name`/`zone` = „кв. Аспарухово“ → „аспарухово“ **16→17** И „дружба“ **2→1** (и клонът се сменя `M7`→`M3`) — `fails_on: "аспарухово"` пада реално. Alias-пътят е доказано мъртъв: `druzhba` носи alias „ж.к. Дружба-Аспарухово“, но `location_alias_tokens` го изхвърля — измерено `dropped["druzhba"] = ["short:zh","short:k","own:druzhba","foreign:asparuhovo:asparuhovo"]`.
  4. **О28 / P7_ADDED — измерено срещу `expectations.json.p7`.** Старите данни възпроизвеждат подписаното ТОЧНО (2 токена/2 зони/48 записа; същият `foreign_guard`: asparuhovo, vladislav, varnenchik отхвърлени). Новите: **7 токена в 5 зони, 64 записа**; новите токени над подписаните са точно `gratska, gratski, varnenchik, vladislav, vasil`; в новия `foreign_guard` остава само `asparuhovo` — `vladislav`/`varnenchik` вече се ДОПУСКАТ. Дифът на зоновите aliases в `new_data/place_categories.json` потвърждава източника (Гръцката махала, кв. Левски и др.).

  Остатъкът от §1 (28 кода, 8-те липсващи, 57-те преписани реда, `_meta` 10/8, картите 14/7, нула `DISTRICT_FALLBACK`, 258/258 `zone == quarter.name`) не е оборен от нито едно мое измерване; цитатите към двата двигателя (`recall_sweep.py:424-431`, `:1159-1198`, `:3093`; `index_M7_branch.txt`) пасват на извадките.

  **Нито едно условие К28-1…7 не е приложено погрешно; и петте специални измервания потвърждават числата на плана. Условия К29-* няма.**

To resume this session: kimi -r session_83c1e67f-7a2a-4251-968d-ae1437554c96
