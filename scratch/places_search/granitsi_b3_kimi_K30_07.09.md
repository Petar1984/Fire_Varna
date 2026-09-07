kimi version 0.34.0
• This is a read-only analysis task. The working directory contains staged/, head/, plan docs, COMMIT_MSG_B3.txt, K29_previous.md. I need to verify execution of plan B3 against staged/ with measurements. No parallel agents, no internet. I can run read-only bash commands (loading modules in memory, running python without writing to disk — but careful: running staged/recall_sweep.py logic "in memory with patched paths, without main()" — that's a computation, doesn't write to disk).

  Let me start by exploring the structure and reading the key files.

• Започвам с разглеждане на структурата на копието и ключовите файлове../COMMIT_MSG_B3.txt
./head/scratch/places_search/granitsi_fixtures_06.09.json
./head/scratch/places_search/recall_sweep.py
./head/tests/test_granitsi_fixtures.py
./K29_previous.md
./staged/data/hotels.json
./staged/data/places.json
./staged/data/place_categories.json
./staged/gates/probe/b3_g11.py
./staged/scratch/places_search/granitsi_fixtures_07.09.json
./staged/scratch/places_search/recall_sweep.py
./staged/tests/test_b3_gates.py
./staged/tests/test_granitsi_fixtures.py
./staged/tests/test_hotels_public_bundle.py
./staged/tests/test_places_public_bundle.py
./ПЛАН_Б3_07.09.md
./ПЛАН_Б3_07.09_амандамент_1.md
./ПЛАН_Б3_07.09_амандамент_2.md
---
    7 COMMIT_MSG_B3.txt
 1152 K29_previous.md
 1159 total


• staged_diff.patch wasn't found by find? It's supposed to exist per the task. Also staged/index.html missing from find output — find output was truncated at head -60 but there are only ~17 files. Hmm, staged/index.html is not in the list! Let me re-check. The find output shows all files (only 18 lines). staged/index.html is missing. Also staged_diff.patch missing. Wait — the command failed with exit code 1, maybe because wc on staged_diff.patch failed (file missing). Let me look more carefully..:
total 2829
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:59 ..
-rw-r--r-- 1 Petar 197121    474 Sep  7 12:58 COMMIT_MSG_B3.txt
-rw-r--r-- 1 Petar 197121  90255 Sep  7 12:58 K29_previous.md
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 head
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 staged
-rw-r--r-- 1 Petar 197121 135877 Sep  7 12:58 ПЛАН_Б3_07.09.md
-rw-r--r-- 1 Petar 197121  28087 Sep  7 12:58 ПЛАН_Б3_07.09_амандамент_1.md
-rw-r--r-- 1 Petar 197121   4877 Sep  7 12:58 ПЛАН_Б3_07.09_амандамент_2.md

head:
total 4
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 ..
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 scratch
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 tests

head/scratch:
total 0
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 ..
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 places_search

head/scratch/places_search:
total 260
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121  32133 Sep  7 12:58 granitsi_fixtures_06.09.json
-rw-r--r-- 1 Petar 197121 229775 Sep  7 12:58 recall_sweep.py

head/tests:
total 12
drwxr-xr-x 1 Petar 197121     0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121     0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121 11279 Sep  7 12:58 test_granitsi_fixtures.py

staged:
total 8
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 ..
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 data
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 gates
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 scratch
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 tests

staged/data:
total 356
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121 151263 Sep  7 12:58 hotels.json
-rw-r--r-- 1 Petar 197121  77998 Sep  7 12:58 place_categories.json
-rw-r--r-- 1 Petar 197121 128401 Sep  7 12:58 places.json

staged/gates/probe:
total 4
drwxr-xr-x 1 Petar 197121    0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121    0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121 3573 Sep  7 12:58 b3_g11.py

staged/scratch:
total 0
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 ..
drwxr-xr-x 1 Petar 197121 0 Sep  7 12:58 places_search

staged/scratch/places_search:
total 280
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121      0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121  51875 Sep  7 12:58 granitsi_fixtures_07.09.json
-rw-r--r-- 1 Petar 197121 232691 Sep  7 12:58 recall_sweep.py

staged/tests:
total 128
drwxr-xr-x 1 Petar 197121     0 Sep  7 12:58 .
drwxr-xr-x 1 Petar 197121     0 Sep  7 12:58 ..
-rw-r--r-- 1 Petar 197121 10134 Sep  7 12:58 test_b3_gates.py
-rw-r--r-- 1 Petar 197121 34389 Sep  7 12:58 test_granitsi_fixtures.py
-rw-r--r-- 1 Petar 197121 40386 Sep  7 12:58 test_hotels_public_bundle.py
-rw-r--r-- 1 Petar 197121 34824 Sep  7 12:58 test_places_public_bundle.py
Critical findings already:
  - `staged_diff.patch` — MISSING
  - `staged/index.html` — MISSING
  - `head/index.html` — MISSING (task says head/ should contain index.html)
  - `tests/granitsi_client_probe.mjs` — MISSING (task mentions it as part of staged)
  - head/tests contains only test_granitsi_fixtures.py (old harness OK)

  So several items of the assignment cannot be verified: (2) index.html M7 branch / M7_PREFIXES — file absent; (3) client isFallbackQuarter/ownQuarter/validTypedLocation — absent; (4) validators in staged/index.html — absent; (5) popupFor — absent.

  But the data files, recall_sweep.py, fixtures exist — I can verify (1), partially (2) engine-side, (6), (7).

  This likely means НЕГОДНО with findings. But wait — maybe the copy is just partial for the review and staged/index.html genuinely absent means the commit can't include it. Let me verify the rest carefully before concluding.

  Let me look at the plan docs briefly (§4 steps 0–7, §6 commit message), fixtures, recall_sweep.py, and run measurements.

  Plan: 
  1. Read fixtures JSON (11 fixtures).
  2. Read recall_sweep.py relevant parts (it's 232KB — need targeted greps).
  3. Load module in memory with patched paths, without main(), run fixture checks.
  4. Check data files: 57 rows with quarter/zone, 201 unchanged, etc.
  5. Check COMMIT_MSG vs §6.
  6. Check gates/probe/b3_g11.py, test_b3_gates.py.

  This is a big task; the instruction says no parallel agents. I'll do it myself with careful targeted reads and a Python measurement script (read-only — but "не изпълнявай команди, които пишат по диска" — running python that computes in memory is fine; avoid __pycache__ writes by using importlib with source loader in memory, or PYTHONDONTWRITEBYTECODE=1).

  Let me start reading the fixture file and the plan amendments.Let me read the rest of the fixtures file (lines 1000-1572).Now I have all 11 fixtures:
  1. street_collision — „детска градина дойран" n=1
  2. district_retention — „училище район младост" n=12
  3. mladost_kind_collision — „младост" n=20
  4. order_identity — „младост" n=20 (same set, different order)
  5. parent_child — „училище младост" n=6
  6. parent_child_vazrazhdane — „възраждане" n=5, „възраждане 2" 0, „ж.к. възраждане 2" 0
  7. chaika_sibling_merge — „чайка" n=30
  8. asparuhovo_no_child_rows — „аспарухово" 16, „дружба" 2
  9. client_cache_matrix (node kind)
  10. district_fallback_typed — synthetic DISTRICT_FALLBACK row, three queries 6/20/12
  11. client_reference_parity (node kind)

  Wait — the task mentions "ф.4 order_identity пренасочена към 27 ДГ Успех — същото множество, друга подредба". Fixture 4's _broken sets quarter on 27 ДГ Успех. Yes.

  Now I need to verify with measurements. Key steps:
  - Load staged/recall_sweep.py in memory with patched paths, without main().
  - For each fixture: run the positive queries over staged/data, check n/with_quarter/without_quarter/identities.
  - Apply each _broken mutation (ops or engine_patch) and verify it fails exactly on fails_on queries with observed values.

  First I need to understand recall_sweep.py's API. It's 232KB. Let me grep for the key functions: def search, apply_ops, own_quarter, DISTRICT_CODES, M7_PREFIXES, MR filter, data loading paths.24:      HEAD word (place_categories.json chips[].head)  -> "хотели" = 226
75:CATS = str(REPO_ROOT / "data" / "place_categories.json")
262:# --- A2: chip -> head  (place_categories.json chips[] carries "head")
612:    return bool(q) and q.get(u"src") == u"DISTRICT_FALLBACK"
615:def own_quarter(rec):
618:    1:1 with the client (`index.html` ownQuarter). A DISTRICT_FALLBACK row is a
1117:def district_rows(R, cls):
1254:def search(q):
1285:    # through М7 to М3 and answered with 4 FOREIGN rows. `M7_PREFIXES` already names
1290:    MR = [t for t in R if t.num or t.s not in M7_PREFIXES]
2160:DISTRICT_CODES = (u"primorski", u"odesos", u"mladost", u"asparuhovo",
2164:def check_lot1v_v_gate():
2176:        if not r.district or r.district.get("code") not in DISTRICT_CODES:
2181:        # О20: a DISTRICT_FALLBACK row is ONE district in TWO forms — the bare name
2191:            if (r.quarter.get("code") not in DISTRICT_CODES
2194:                bad.append(u"%s: DISTRICT_FALLBACK кварталът не е собственият район (%s)"
2550:    for key, path in ((u"hotels", u"data/hotels.json"), (u"places", u"data/places.json")):
2728:            "data": ["Fire_Varna/data/hotels.json",
2729:                     "Fire_Varna/data/places.json",
2730:                     "Fire_Varna/data/place_categories.json"],
2861:INPUT_RELS = (u"data/places.json", u"data/hotels.json",
2862:              u"data/place_categories.json")
3139:M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
3176:    for q in M7_PREFIXES:
3224:    for rel, key in ((u"data/places.json", "places"), (u"data/hotels.json", "hotels")):
3441:        "prefixes": dict((q, answer_of(q)["branch"]) for q in M7_PREFIXES),
3597:                    json.dumps(blob_json(commit, u"data/place_categories.json"),
3828:def main():
3887:      u"`varna_3d/data/place_categories.json` (%d форми, %d чипа с `head`)."
4255:          % (len(M7_PREFIXES) + len(M7_PLACES) - len(m7_bad),
4256:             len(M7_PREFIXES) + len(M7_PLACES), len(M7_PREFIXES), len(M7_PLACES)))
1133:M7_ENABLED = True
1185:    if not M7_ENABLED or not R:
1265:            return bare, "M7-bare-location"
2126:DISTRICT_CODES = (u"primorski", u"odesos", u"mladost", u"asparuhovo",
2142:        if not r.district or r.district.get("code") not in DISTRICT_CODES:
2354:M7_BUCKET = "gate_m7_bare"
2749:        ROWS[M7_BUCKET].append({
2755:            "ok": _b == "M7-bare-location",
2925:    global M7_ENABLED
2930:    M7_ENABLED = False
2934:        M7_ENABLED = True
3015:               for m in m7_moved if m["bucket"] != M7_BUCKET]
3018:        M7_ENABLED = False
3023:            M7_ENABLED = True
3044:            "m7_bucket": M7_BUCKET,
3047:                1 for e in rows_with_m7[M7_BUCKET] if e["branch"] == "M7-bare-location"),
3048:            "m7_rows": sum(len(e["rows"]) for e in rows_with_m7[M7_BUCKET]),
3055:            "extra": [e for e in m7_extra if e["bucket"] != M7_BUCKET],
3064:                         for e in rows_with_m7[M7_BUCKET]],
3093:M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2")
3094:M7_PLACES = (u"zlatni", u"mladost", u"chaika", u"zpz", u"vilite",
3096:M7_BRANCH = u"M7-bare-location"
3130:    for q in M7_PREFIXES:
3132:        if branch == M7_BRANCH:
3134:    for q in M7_PLACES:
3136:        if branch != M7_BRANCH:
3143:        for q in M7_PLACES[:1]:
3145:            if branch == M7_BRANCH:
3395:        "prefixes": dict((q, answer_of(q)["branch"]) for q in M7_PREFIXES),
3396:        "places": dict((q, answer_of(q)["branch"]) for q in M7_PLACES),
3567:# „A3-street“/„M7-bare-location“ answer with or without a class key.
3568:HASKEY_FREE_BRANCHES = ("empty", "A3-street", "M7-bare-location")
4046:    _promoted = ((PENDING_BUCKET, M7_BUCKET) if not FREEZE
4209:          % (len(M7_PREFIXES) + len(M7_PLACES) - len(m7_bad),
4210:             len(M7_PREFIXES) + len(M7_PLACES), len(M7_PREFIXES), len(M7_PLACES)))
===
  4380 staged/scratch/places_search/recall_sweep.py
  4334 head/scratch/places_search/recall_sweep.py
  8714 total
Interesting. In staged/recall_sweep.py, `M7_PREFIXES = ("k","kv","zh","m","s","o","t","i","1","2")` at line 3139 — includes numbers "1","2"! But the task says variant B: the MR filter for M7 keeps only letter prefixes (k,kv,zh,m,s,o,t,i; numbers stay). Wait — re-read task item (2): „филтърът MR за М7 (само буквените префикси k,kv,zh,m,s,o,t,i; числата остават)". Hmm — so M7_PREFIXES as gate list may include "1","2" (places starting with numbers), but the MR filter in search() (line 1290) should only strip letter prefixes. Let me read the search function and own_quarter and district_rows regions in staged.I see the MR filter at line 1290: `MR = [t for t in R if t.num or t.s not in M7_PREFIXES]`. But M7_PREFIXES = ("k","kv","zh","m","s","o","t","i","1","2") — includes "1" and "2"! Since `t.num` keeps numbers anyway, "1","2" in M7_PREFIXES only matter for non-num tokens whose s == "1" or "2"... hmm, actually a token with s "1" or "2" would be num anyway. Wait — tokens like "1" have num=True presumably. So including "1","2" in the tuple is harmless for MR. But the task's claim (2): „филтърът MR за М7 (само буквените префикси k,kv,zh,m,s,o,t,i; числата остават)". The M7_PREFIXES tuple at line 3139 includes digits "1","2" — but those are used by the gate at line 3176 (`for q in M7_PREFIXES`) as single-word queries like "1", "2" presumably to gate that they don't go M7? Let me check head's M7_PREFIXES: line 3093 head: same ("k",...,"1","2"). Hmm wait — was M7_PREFIXES present in head? Line 3093 in head shows M7_PREFIXES = (u"k", u"kv", u"zh", u"m", u"s", u"o", u"t", u"i", u"1", u"2"). So the constant existed in head too (as gate list). The staged adds the MR filter in search(). Task says the MR filter uses "само буквените префикси" — in code, the filter drops tokens whose s is in M7_PREFIXES unless t.num. Since "1","2" tokens are num, they stay. So effectively only letter prefixes dropped. OK.

  Note the docstring at line 1287 says digits stay (§13 т. 5). Good.

  Now I need to run measurements. Plan: write a python harness? No — I cannot create files. I must run python inline via `python -c` or heredoc without writing. Loading the module "in memory with patched paths, without main()": the module at import time may read REPO_ROOT paths. Let me check the top of the file for REPO_ROOT and how data is loaded at import.staged/tests/test_granitsi_fixtures.py:104:def apply_ops(hotels, places, ops):
staged/tests/test_granitsi_fixtures.py:186:        hotels, places = apply_ops(hotels, places, ops)
staged/tests/test_granitsi_fixtures.py:317:            apply_ops(hotels, places, [{"bundle": "hotels", "name": u"РОЯЛ",
staged/tests/test_granitsi_fixtures.py:319:        h2, _p2 = apply_ops(hotels, places,
staged/tests/test_granitsi_fixtures.py:401:        hotels, places = apply_ops(*base_bundles(self.reference) + (case["ops"],))
staged/tests/test_granitsi_fixtures.py:420:            hotels, places = apply_ops(*base_bundles(self.reference) + (ops,))
staged/tests/test_granitsi_fixtures.py:440:        _hotels, places = apply_ops(*base_bundles(self.reference) + (case["ops"],))
staged/tests/test_granitsi_fixtures.py:442:        _h2, bad_places = apply_ops(*base_bundles(self.reference) + (broken["ops"],))
===
61:if hasattr(sys.stdout, "reconfigure"):
68:REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
73:HOTELS = str(REPO_ROOT / "data" / "hotels.json")
74:PLACES2 = str(REPO_ROOT / "data" / "places.json")
75:CATS = str(REPO_ROOT / "data" / "place_categories.json")
76:REPO_ROWS_OUT = str(REPO_ROOT / "scratch" / "places_search" / "recall_sweep_rows.json")
79:REPO_PARITY_OUT = str(REPO_ROOT / "scratch" / "places_search" / "probe_out"
96:if MANIFEST and FREEZE:
564:if not isinstance(LEGACY_BY_ROW, dict):
2026:EXPECTATIONS_OUT = str(REPO_ROOT / "scratch" / "places_search" / "expectations.json")
2551:        got = subprocess.run(["git", "-C", str(REPO_ROOT), "show",
2707:    out = str(REPO_ROOT / "scratch" / "places_search" / "lot1v_v_reference_manifest.json")
2878:    got = subprocess.run(["git", "-C", str(REPO_ROOT), "show",
3114:    out_dir = pathlib.Path(REPO_ROOT) / "scratch" / "places_search"
3225:        doc = (json.loads(pathlib.Path(str(REPO_ROOT / rel)).read_text(encoding="utf-8"))
3235:    got = subprocess.run(["git", "-C", str(REPO_ROOT), "show",
3247:    got = subprocess.run(["git", "-C", str(REPO_ROOT), "show",
3670:    if str(REPO_ROOT) not in sys.path:
3671:        sys.path.insert(0, str(REPO_ROOT))
3684:    if str(REPO_ROOT) not in sys.path:
3685:        sys.path.insert(0, str(REPO_ROOT))
4319:            _p = REPO_ROOT / "scratch" / "places_search" / _name
4379:if __name__ == "__main__":
Good. The test harness `staged/tests/test_granitsi_fixtures.py` already contains `apply_ops` and presumably a loader that imports recall_sweep with patched paths. Let me read that test harness — it will tell me how to load the module in memory, and it's itself part of the delivery that I need to review.The harness depends on `REPO / "index.html"` and `tests/granitsi_client_probe.mjs` — both missing in the copy. The reference fixtures (1–8, 10) can be measured in memory here.

  Note `load_reference` reads REFERENCE path and executes it — the module computes REPO_ROOT from `__file__`... actually `module.__file__ = str(REFERENCE)` and `exec(compile(text, module.__file__, "exec"), module.__dict__)` — inside the module, `__file__` is set in module.__dict__, so REPO_ROOT = parents[2] of staged/scratch/places_search/recall_sweep.py = staged/. Good — data paths resolve to staged/data.

  But wait: does the module body at import time write anything? Line 43 says "READ-ONLY. Writes nothing but its own report next to itself" — writing happens in main(). Import should be safe. But check for module-level data loads: LEGACY_BY_ROW at line 564, FORM_IDX, GENERIC_TOKENS load — presumably read-only. Also `sys.stdout.reconfigure` fine. FREEZE flag checks sys.argv — running under `python -c`, argv won't contain --freeze.

  I'll write my measurement as inline `python -c` scripts that import the test harness functions (tests.test_granitsi_fixtures can't be imported directly because REPO = parents[1] of staged/tests = staged/ — but staged/ lacks index.html; that's only read at client test setUpClass, not import). Actually importing the test module is fine; I can reuse load_reference, answer, apply_ops, answers_of.

  But careful: importing tests.test_granitsi_fixtures requires `tests` package — is there an __init__.py? Not listed. The harness itself does `sys.path.insert(0, REPO)` and `from tests import test_places_public_bundle` inside a test. Without __init__.py, unittest discovery still works in py3 (namespace packages). For my inline script, I can just load the harness by path with importlib or replicate the needed functions. Simplest: exec the harness file in a namespace? It imports unittest etc. and defines classes — class bodies don't run tests at import. setUpClass of client tests reads index.html — but only when tests run.

  Also `from tests import test_places_public_bundle` inside a test method — not at import.

  Plan for measurement script (inline, read-only):
  1. cd to repo root copy; use importlib.util.spec_from_file_location to load staged/tests/test_granitsi_fixtures.py as a module. But its REPO = parents[1] = staged — good.
  2. reference = load_reference()
  3. Verify sha256 of the three data files and engine against _meta (LF-normalized).
  4. For each of the 9 reference fixtures (1-8,10): answers_of(reference, case, case.get("ops",[])) and compare with case["queries"] expectations (like assert_case).
  5. For each _broken: apply engine_patch or ops, measure answers, compute changed set vs clean, compare to fails_on, and check observed matches.
  6. Fixture 10 extra: qtk/qph empty, own_quarter None, gate quiet/loud.
  7. Variant B checks: queries „кв. Левски" 14/12? Task says „кв. Левски" 14/12 — hmm, that's with_quarter/without? Task: „кв. Левски" 14/12, „кв. Тракия" 4/4, „кв. Христо Ботев" 4/3, „ж.к. Св. Иван Рилски" 4/2, „възраждане 2"/„младост 2" 0. Probably n/with_quarter? For „кв. Тракия" names list has 4 entries so 4/4 could be n=4, with_quarter=4? And „кв. Левски" names list has 14 → n=14, with_quarter=12. „ж.к. Св. Иван Рилски" names 4 → 4/2 (n=4, with 2). So format is n/with_quarter presumably. I'll measure n, with, without for those queries plus „възраждане 2", „младост 2", plus „кв. Христо Ботев" (not in fixture 11 — measure directly).
  8. R\MR unchanged vs head: load head engine over staged data? Task says „R\MR непроменено спрямо head/recall_sweep.py над същите данни" — i.e., queries where MR == R (no M7 prefixes) give same answers with head engine and staged engine over the same data. But head engine can't read staged data directly since its REPO_ROOT would be head/... I'd patch paths: load head source with patched HOTELS/PLACES2/CATS strings, or exec head text with module.__file__ pointing to staged location. Simpler: exec head text but override HOTELS etc after exec and reindex. The Rec construction happens at import of the module body presumably building RECS. If I override after exec, need reindex. The harness reindex does that. I can load head engine via load_reference-like exec, then use harness's reindex on it with staged data. But harness reindex references reference.hotels etc. Fine.

  Also legacy_of(bundle, ordinal) — legacy words may come from a file LEGACY_BY_ROW loaded at import; check line ~560 where it's loaded — maybe from data or a constant. If from REPO_ROOT file, head engine loading needs that file... Let me check around line 540-570 in staged.

  Also GENERIC_TOKENS loaded from CATS (place_categories.json) — staged data fine for both engines if I patch paths.

  Data checks (item 6): 57 rows with quarter/zone changed? "57 реда с quarter/zone, 201 непроменени, нула геометрия/кадастър, лицензните низове". 375 total records; 57 with quarter... Actually task (6): данните: 57 реда с quarter/zone, 201 непроменени — hmm 375-57=318, not 201. Maybe 201 refers to something else (rows with zone unchanged?). Wait 150 places + 225 hotels = 375. 57 rows with quarter/zone per cache bump rationale "57 сменени квартала при непроменен брой". 201 непроменени... unclear — maybe 201 = rows without quarter? Let me check data: count records with quarter field, compare with git? No git repo here — it's a copy without .git (Glob skips .git; find showed no .git). Without git history, "непроменени" can't be verified against the previous delivery... unless K29_previous.md contains measurements. The task says verify "201 непроменени" — perhaps from the data itself: count records where zone/quarter present etc. Hmm. Actually maybe: 57 rows carry quarter, and 201 = 375-174? Not clear. Let me look at plan §4 steps and K29 for the definition.

  Let me first check what the plan says (§4, §6) and K29_previous.md for context on "201". Also verify counts: records with quarter, src distribution, geometry/cadastre absence, license strings.

  Let me now run the measurements. First a quick structural scan of the data files.top keys hotels: ['_meta', 'hotels']
top keys places: ['_meta', 'places']
top keys cats: ['_meta', 'chips', 'forms', 'zones', 'locations', 'legacy_by_row']
counts: 225 150
places quarter: (91, Counter({'SIGNED_POLYGON': 42, 'REG': 39, 'KAIS': 10}))
hotels quarter: (167, Counter({'REG': 115, 'KAIS': 25, 'SIGNED_POLYGON': 15, 'SIGNED_OVERRIDE': 12}))
all keys: {'name': 375, 'kind': 375, 'no_uin': 225, 'cat': 225, 'beds': 225, 'lat': 375, 'lon': 375, 'zone': 375, 'quarter': 375, 'district': 375, 'locality': 375, 'uins': 225, 'old_names': 375, 'old_names_src': 375, 'status': 375, 'src': 375, 'address': 375}
143:  - К28-6: О22 semantics of 138 ✓ — plan records semantics "lost/changed" and §4 step 2 requires the f06ac06↔f00dd78 diff (150). I can't verify coverage numbers (needs gates/coverage.py which isn't in the copy). Check expectations.json / old_data vs new_data zone_named changes: K28 said old→new gives zone_named lost 0 / changed 0, 57 gains. Verify: count rows where old zone was "район X" and new zone is quarter name — 57 (42+15). But 138 vs baseline f06ac06 can't be verified here — the plan now records semantics and the 150 diff, which addresses К28-6 as best possible in this copy. But wait — can I verify the claim "доставката връща 12"? No, that needs the baseline data. The copy has old_data = f00dd78 data presumably. 138 vs 150 semantics: plan says against f00dd78 uncovered = 150, against f06ac06 = 138, meaning the delivery "returns 12". Hmm, actually that's odd: uncovered against f00dd78 (150) is larger than against f06ac06 (138). coverage "uncovered" = rows covered in base but not in candidate... wait no. Actually uncovered = rows in candidate lacking coverage relative to base+allow? If base = f06ac06 (older, fewer named rows?), uncovered 138; if base = f00dd78, uncovered 150. And 150 - 138 = 12 means 12 rows that were "uncovered" against f00dd78 are now covered by the older baseline's allow... This is confusing but not measurable here. I can only check that the plan's semantic definition is consistent: 138 = 44+44+39+11. old→new in the copy: rows that changed zone from "район X" to quarter name = 57. Those are "changed" only if the base already had a named zone. Against f06ac06 the counts differ. I can note what's verifiable.
145:  Actually wait — I should check whether old_data corresponds to f00dd78. K28 verdict says "По old_data→new_data: zone_named lost 0 / changed 0, 57 печалби". The plan's О22 semantics: "lost" = row had named zone in base and none in candidate; "changed" = had a different one. Against f00dd78 (old_data), lost 0/changed 0 — but plan claims 150 uncovered against f00dd78 with places 78+18=96, hotels 47+7=54. That's contradictory unless uncovered ≠ lost+changed — uncovered is "rows in candidate not covered by base/allow", i.e. NEW named rows. So against f00dd78: 57 new quarter-named rows? No, 150... hmm. Actually uncovered could include rows present in candidate with zone that base didn't have named... 57 gains vs 150 uncovered. Doesn't add up either. This is unverifiable without gates/coverage.py and the baseline blobs. I'll note this.
147:  Hmm, wait. Let me reconsider: 1.8.1б claims base=f06ac06, candidate=f00dd78 → uncovered 150. So candidate is the OLD data (f00dd78 = current HEAD data = old_data presumably). uncovered = candidate rows not present/covered in base. So f00dd78 vs f06ac06 has 150 rows whose zone_named status isn't in the signed baseline. And new delivery vs f06ac06 = 138. So delivery "returns 12" rows to baseline-covered state. And against old→new directly (K28): 57 gains. OK, plausible. Not measurable here; fine.
283:    """\u00a711 steps (\u0430)-(\u0435) + (\u0434\u2032) \u2014 the per-zone CANDIDATES, before step (\u0436).
302:    # (\u0434\u2032) \u04201: a token that IS, or is within lev<=2 of, an own token of a zone
303:    # from ANOTHER family is a foreign name \u2014 `primorski`/`primorskiat` fall here.
304:    # The >=3 floor is mandatory: without it `zpz` dies against \u201ezh\u201c.
547:TYPO = re.compile(u"[\u201e\u201c\u201d\u201a\u2018\u2019\u00ab\u00bb\u2013\u2014/()]")
822:2016:        _EXPECTATIONS = (json.loads(path.read_text(encoding="utf-8"))
===
582:**9. [П] Атомният комит** — §6.
725:## 6 · Комити (кой какво комитва)
Data: places 150, hotels 225 → 375. Rows with quarter: places 91 + hotels 167 = 258. Hmm. Task item (6): "57 реда с quarter/zone, 201 непроменени" — maybe 57 rows whose zone changed from район to quarter name (42 SIGNED_POLYGON places + 15 hotels = 57!). Yes: 42+15=57 SIGNED_POLYGON rows. And "201 непроменени" — 375 - 57 = 318, not 201. Hmm. Maybe 201 = rows with quarter from REG/KAIS/SIGNED_OVERRIDE unchanged? 39+10+115+25+12 = 201! Yes! REG+KAIS+SIGNED_OVERRIDE quarters = 39+10 (places) + 115+25+12 (hotels) = 201. So "201 непроменени" = the 201 rows that already had quarters from previous channels, unchanged. And 57 new SIGNED_POLYGON rows (42 places + 15 hotels). Total quarter rows 258; 375-258 = 117 without quarter.

  "нула геометрия/кадастър" — hmm, but keys include 'uins' on 225 hotels and lat/lon on all 375. Wait — "нула геометрия/кадастър" in the fixtures context means the fixture file carries zero coordinates (that's stated in fixtures _meta: "нула координати"). For the data item (6), "нула геометрия/кадастър" likely means the DELTA adds no geometry/cadastre — but we can't diff without old data. But `uins` key exists in hotels (cadastral identifiers!). Hmm, the recall_sweep says "NEVER prints cadastral identifiers (record["uins"] is not read at all)". Task (6) says "нула геометрия/кадастър" — need to check what plan §4 says about the data delivery. Let me read the plan §4 and §6.

  Also license strings — check _meta of data files for license fields.

  Let me read the plan around §4 and §6, and data _meta blocks.Traceback (most recent call last):
  File "<string>", line 6, in <module>
  File "C:\Program Files\Python310\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
== data/hotels.json
UnicodeEncodeError: 'charmap' codec can't encode characters in position 234-240: character maps to <undefined>
files = [f for f in subprocess.run(["git","ls-files","data/"],capture_output=True,text=True).stdout.split() if f.endswith(".json")]
bad = []
for f in files:
    hits = []
    walk(json.loads(pathlib.Path(f).read_text(encoding="utf-8")), "", hits)
    if hits: bad.append((f, hits[:3]))
print(len(files), bad)
sys.exit(0 if not bad else 1)
```
**Измерено: 18 файла, 0 попадения.** Плюс **инвентар на НОВИТЕ проследени файлове** на комита срещу неговия родител:
```powershell
git diff --name-status --diff-filter=A <parent> HEAD
```
Позволени НОВИ пътища, поименно: `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (при `git mv` върви като R, не A), `scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md`, `gates/allow/2026-09-07_b3.json`, `scratch/places_search/архив/АРХИВ_A_05.09.md`. **Всеки друг нов проследен файл = STOP.**
Отрицателна половина (измерена): файл с ключ `"\u0063oordinates"` — `grep -c coordinates` → **0** (exit 1), структурната проверка → **`/a/coordinates`** (exit 1 на гейта).

**G17 — дословно (S28-6, О17):** четирите отрицателни мутации, **всяка със СЪЩИЯ брой ключове**, всяка трябва да даде `false`:
1. `_meta.generated` преименуван на `unexpected` — **10 ключа, но друго множество** → `metaKeysAre` трябва да върне `false`. (v2 броеше и минаваше: измерено `true`.)
2. `quarter_attribution["kv_levski"].src = "openstreetmap"` при непроменен wikimapia url → `false` по правилото за извора.
3. Измислен `src: "wikidata"` с валиден url → `false` по затвореното множество `ATTRIB_SRC`.
4. Добавен запис `quarter_attribution["galata"]` (никой `SIGNED_POLYGON` ред не го носи) → `false` по **равенството** (v2 проверяваше само „всеки код има запис“ и това минаваше).
Положителните твърдения: places 10 ключа / 14 кода, hotels 8 ключа / 7 кода, всичките 21 записа с ключовото множество `{label, licence, src, url}`, `mladost2` с `url === 'https://www.openstreetmap.org/copyright'`.

---

## 6 · Комити (кой какво комитва)

Причината за атомността е механична: `index.html` пинва sha на данните — при какъвто и да е разрез съществува HEAD, в който пиновете и блобовете не си съответстват и търсенето на места умира.

| # | автор (наложен) | съдържание | съобщение (дословно) |
|---|---|---|---|
| 1 | `Claude Executor <executor@local>` (флагове, О24) | `docs/plans/ПЛАН_Б3_07.09.md` | `docs(plan): Б3 quarter search delivery plan v3 (signed 07.09)` |
| 2 | **`Petar1984`** (неговата ръка) | `data/places.json`, `data/hotels.json`, `data/place_categories.json`, `index.html`, `tests/test_places_public_bundle.py`, `tests/test_hotels_public_bundle.py`, `tests/test_granitsi_fixtures.py`, `tests/granitsi_client_probe.mjs`, `scratch/places_search/granitsi_fixtures_07.09.json` (+ изтритият `…_06.09.json`), `scratch/places_search/recall_sweep.py` | виж по-долу |
| 3 | `Claude Executor` | опашката Б3, **преименуваната `архив/АРХИВ_A_05.09.md`**, трите манифеста, новият `gates/allow/2026-09-07_b3.json` (138 реда, pending), махнатият стар allow. **`gates/baseline/MANIFEST.json` НЕ се пипа (О22).** | `docs: queue and manifests for the Б3 delivery signatures (07.09)` |
| 4 | **`Petar1984`** | каквото `gates.sign` е записало | съобщението, което писалката **отпечатва** |
| 4б | **`Petar1984`** (само ако низът се подписва отделно) | `index.html` (И11) | `feat(map): signed quarter-boundary line in the map attribution (decision 8)` |
| 5 | **`Petar1984`** | `recall_sweep_rows.json`, `expectations.json`, `probe_out/token_parity.json` | `freeze: reference + expectations + parity (Б3)` |
| 6 | `Claude Executor` (след пуша) | `docs/activeContext.md`, `docs/sessions/СЪСТОЯНИЕ_Границите_06.09.md` | `docs: activeContext — Б3 delivery published, published hashes verified equal to local` |

Съобщението на комит 2, дословно (`scratch/places_search/COMMIT_MSG_B3.txt`):

```
feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)

data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
commit, because a HEAD whose pins and blobs disagree kills the place search.
tests: S17 fixtures fail on broken candidates
```

Командите за комит 2 (PowerShell, по една на ред, без `&&`):
```powershell
cd C:\git\Fire_Varna
git status --short
git diff --cached --stat
git commit -F scratch\places_search\COMMIT_MSG_B3.txt
git log -1 --pretty='%h %an <%ae> · %cn <%ce> · %s'
```
**Следпроверка (О24):** последният ред трябва да върне `Petar1984 <petar.dikov2019@gmail.com>` и като автор, и като комитър. Предварителното `git config user.name` **не доказва нищо**.

---

## 7 · STOP условия

1. **Всяко число от §1, премерено различно** — трите sha, шестте байта/gzip, осемте липсващи кода, числата на фикстурите, **и новите: 138 / 150 / (30 + 42) на покритието, 1 878 210 B първо зареждане, 1 опашка в HEAD, деветте заявки 1.8.4–1.8.9, двете `_meta` множества, двете карти 14/7**.
2. `gates.release` дава делта, която опашката не покрива, или ред „не“ (терминален).
3. `gates/out/coverage.json` иска allow-ред, който не се извежда механично.
4. Паднал тест **извън** записания D19/G20 набор.
5. `python -m gates.run_gates` жълто, третирано като зелено.
6. Дифът на кандидата преди/след промяната в `recall_sweep.py` е ≠ 0 байта (G7).
7. Липсващ `node`, липсващ маркер за среза, или Node-фикстура, минала **без** `map`/`fetch`/**`crypto`** стъб.
8. Опит за комит на данни от агент · `push` от агент · `--no-verify` · пипане на `.git/hooks`.
9. Работното дърво не е чисто по проследен файл при старта, или чужд стейджнат диф.
10. Решение 10 / резервът за Перчемлията (О6) не е подписан и одиторът настоява.
11. Износът е сменил лицензен низ, а константата в теста и README не са в същия комит.
12. Петър не е видял картата локално преди пуша.
13. **Повече от една опашка в HEAD** (по семантиката на `queues_in_head`, не по `grep`) или повече от един allow-json.
14. **`_meta.inputs` не съдържа обявеното множество**, или `INPUT_RELS` е пипнат.
15. **Комит с автор `Petar1984`, направен не от неговата ръка** (О24).
16. **Низът за атрибуция е влязъл в `index.html` преди подписания ред с двата му дайджеста** (О21).
17. **`gates/baseline/MANIFEST.json` е пипнат** (О22).
18. Проследеният `probe_out/token_parity.json` се появи в комит 2 вместо в комит 5 (О26).
19. 🔴 **Опашката носи по-малко от ОСЕМ делта-реда за загубените на „младост“** (1.7, К28-3).
20. 🔴 **`--manifest` е пуснат повече от веднъж преди подписите** (1.8.16, О30) — второто число е вакуумно зелено и не е доказателство.
21. 🔴 **Стар/нов файл със `SIGNED_POLYGON` код, който `quarter_attribution` не носи, ИЛИ запис в картата без такъв ред** — равенството е гейт и в двете посоки (G17).
22. 🔴 **Нов проследен файл извън поименния списък на G11.**

---

## 8 · Локален преглед (как Петър гледа)

```powershell
cd C:\git\Fire_Varna
python -m http.server 8000
```
`http://localhost:8000/index.html`, отворена конзола, ширина 375 px, Hard reload (кешът вече е v7). Първо: конзолата е чиста и **няма** реда `legacy_by_row: друг пакет…`.

| # | пишеш | очакваш (числата са измерени 07.09) |
|---|---|---|
| 1 | `Кайсиева градина` | в нашата секция — **3 реда `M2-failopen`**, нито един квартален; в адресната търсачка отгоре — 9 реда. |
| 2 | `училище Възраждане 3` | **2 реда по ИМЕТО**: `3 ОУ Ангел Кънчев` [**кв. Левски**] и `III ПМГ` [**кв. Тракия**] — **нито един не е във Възраждане 3**. Шум по името, не отговор по квартал. |
| 3 | `възраждане`, после `възраждане 2` | **5** реда (`ДГ 29 „Звънче“`, `ДГ 31 „Крилатко“`, `II ОУ „Никола Йонков Вапцаров“`, `ДГ 33 „Делфинче“`, `ДГ№34 „Лястовичка“`) и **0 реда** за детето. **Половината „дете → детето“ НЕ работи** (О16) — това подписваш. |
| 4 | `левски`, после `кв. Левски` | голото `левски` → **14 реда, 12 с код `kv_levski`**. `кв. Левски` → **4 ЧУЖДИ реда** (`НУ Васил Левски` [кв. Аспарухово], `ПГ „Васил Левски“`, `ДГ№40` [кв. Владиславово], болница). Същото за `кв. Тракия` (**1**, и той е `dolna_traka`), `кв. Христо Ботев` (**24**, от които **точно 1** е `hristo_botev` — `ЦДГ 8 - Христо Ботев`, и то по име), `ж.к. Св. Иван Рилски` (**22**, нула с кода). **Ако избереш вариант Б по §9 т. 1, тези четири стават 14 / 4 / 4 / 4 с 12 / 4 / 3 / 2 верни реда.** |
| 5 | `бриз` | 🔴 **4 реда** (не 2): `ПАРК ХОТЕЛ БРИЗ` [к.к. Златни пясъци — **по име**], `IV ЕГ Жолио Кюри` [ж.к. Бриз, нов], `ПГ „Д. И. Менделеев“` [ж.к. Бриз, нов], `Камелия` [ж.к. Бриз, заварен]. Двата нови са `SIGNED_POLYGON`. |
| 6 | `чайка` | **30 реда** — 19 `chaika_kk` + 10 `chaika_kv` + `„ДКЦ Чайка“ ЕООД` (без квартал). Фразата слива двата кода без подписано родство (О16). |
| 7 | `аспарухово`, после `дружба` | **16** реда (9 с `asparuhovo`, 7 „район Аспарухово“) **без** `ЦДГ 43 „Пинокио“`, и **2** реда. Подписаното родство `druzhba ⊂ asparuhovo` **не действа**. |
| 8 | `Никея` (хотел в Чайка) → картончето | ред **„вид · к.к. Чайка · район Приморски“**; **НЯМА ред за извор** (измерено: 375/375 картончета без нито един от забранените низове); долу вляво, до `© OpenStreetMap`, стои низът за границите. |
| 9 | `училище район Младост` / `младост` | **12** / **20**. Изричното районно търсене задържа и петте училища със собствен квартал. |
| 10 | **надписът при 375 px** | низът е **338 знака** и застава в същия долен ляв ъгъл, където са бутоните `+`/`−` (`:1900` и `:1917`). Проверява се **на екрана**: бутоните `+`/`−` и локацията остават **видими и натискаеми** при трите базови карти. Ако не са — §9 т. 7, вариант „къс низ“. |
| 11 🔴 | **отказът, който мълчи** (О27) | ако някога доставка донесе код извън списъка, в нашата секция ще има **225 реда вместо 375 и НУЛА съобщение**. Днес това не се вижда — подписваш го като известно поведение. |

---

## 9 · Решения за Петър

1. 🔴 **Типовият префикс („кв. Левски“ и трите му близнака).** Измерено (1.8.4): `кв. Левски` 4 чужди, `кв. Тракия` 1, `кв. Христо Ботев` 24 (1 верен по име), `ж.к. Св. Иван Рилски` 22. Причина: `index.html:6495-6496` / `recall_sweep.py:424-431` — токен ≤ 2 знака не е значещ, а М7 иска `R.every(isSignificantToken)`. **Три варианта:**
   - **(А) Отлагане** (позицията на v2): D12 + `locationKey` в паритетния корпус са лот **Б5**. Цена: осемте нови квартала се търсят само с голото си име. Цена днес: 0.
   - **(Б) Евтината поправка (К28-5), ПРЕПОРЪЧАНА.** Двигателят вече назовава затворения списък `M7_PREFIXES` (`recall_sweep.py:3093` = `("k","kv","zh","m","s","o","t","i","1","2")`). Пропускат се **само буквените** префикси (`k, kv, zh, m, s, o, t, i`) преди теста за значимост в М7 клона, в **двата двигателя**: `recall_sweep.py:1257`+`:1263` (2 реда) и `index.html:7058-7069` (клиентът **няма** такъв списък — иска новата константа + филтриран `R`, ~5 реда). **Измерено върху копие в скрачпада:** `кв. Левски` **4 → 14** (12 с `kv_levski`), `кв. Тракия` **1 → 4** (4/4), `кв. Христо Ботев` **24 → 4** (3/4), `ж.к. Св. Иван Рилски` **22 → 4** (2/4). **Цена на презамразяване: НУЛА** — 156-заявъчният подписан корпус дава **0 промени**, а дъмпът на референцията е **байт-еднакъв** (1 273 012 B). Остава честната цена: **паритетът** (клиентът трябва да получи същите ~5 реда, иначе двата двигателя се разминават) и **един нов кръг на фикстурите/паритетната сонда**. Числата (`2`, `1`) остават извън списъка: **„възраждане 2“ и „младост 2“ пак дават 0** — детската заявка не оживява.
   - **(В) Пълният D12** (нормализатор + `locationKey` в паритета): измерено, че вариант **А′** (пропускане и на числата `1`/`2`) прави „възраждане 2“ и „младост 2“ да върнат **5** и **20** — тоест ДЕТСКАТА заявка получава РОДИТЕЛСКИЯ отговор. Това е по-лошо от 0 и планерът го **отхвърля** (§13 т. 5).
   **Препоръка: (Б).** Ако Петър каже (А), §8 проба 4 остава както е и О15 се подписва изрично.
Let me set up a todo list and continue. I need to:

  1. Verify data _meta (license strings, closed sets) — rerun python with UTF-8 stdout.
  2. Run the fixture measurements (positive + broken) using staged harness logic inline.
  3. Variant B measurements (M7 MR filter) — staged vs head engine over staged data.
  4. Verify commit message vs §6 — already have: §6 says the message verbatim should match scratch/places_search/COMMIT_MSG_B3.txt. Compare COMMIT_MSG_B3.txt content to the quoted block. The plan's quoted block:

  ```
  feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)

  data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
  varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
  closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
  commit, because a HEAD whose pins and blobs disagree kills the place search.
  tests: S17 fixtures fail on broken candidates
  ```

  The file COMMIT_MSG_B3.txt has exactly 7 lines matching. Need to check trailing newline and byte equality. Let me extract the plan's block and diff.

  Also item (4) validators in index.html — file missing, so that check is blocked; but the plan quotes the closed sets (places 10 keys/14 codes, hotels 8 keys/7 codes). I can verify the DATA side: quarter_attribution in data files: count keys and codes, and the mutation that passes wrongly (G17 mentions mutations that must fail). I can verify data-level: quarter_attribution entries, key sets {label, licence, src, url}, src ∈ {wikimapia, openstreetmap}, url rule, and map↔SIGNED_POLYGON codes equality (places 14, hotels 7).

  Also (6): 57 rows with quarter/zone — 42+15 SIGNED_POLYGON = 57 ✓ measured. 201 unchanged = REG/KAIS/SIGNED_OVERRIDE quarters 201 ✓ measured. Zero geometry/cadastre: check for keys like coordinates/geometry/uins in the NEW parts? Hotels carry uins (225) and lat/lon on all — but those are pre-existing fields. The plan G16(?) check: grep coordinates = 0. Let me check 'coordinates'/'geometry' strings in data files. License strings: quarter_attribution licence fields.

  Let me set up todos and run the main measurement script now. The big one: load staged reference in memory via harness, verify all 9 reference fixtures positive and broken halves. I'll import the harness module by path.== data/hotels.json sha256: eb8fa85cbb67265a bytes: 151263
 meta keys: ['by_zone_src', 'count', 'excluded', 'generated', 'licence', 'licence_address', 'licence_osm', 'quarter_attribution']
   licence = Имената и регистровите данни: отделни факти от Националния туристически регистър (чл. 4 ЗАПСП; без масово копиране на регистъра). Координатите: собствена геолок
  quarter_attribution codes: ['chaika_kk', 'dolna_traka', 'kolhozen_pazar', 'kv_levski', 'tsentar', 'vinitsa', 'zlatni_pyasatsi']
  entry key sets: {('label', 'licence', 'src', 'url'): 7}
  src values: {'wikimapia': 7}
    chaika_kk | wikimapia | http://wikimapia.org/5461405/bg/Комплекс_Чайка | CC BY-SA
    dolna_traka | wikimapia | http://wikimapia.org/5729426/bg/Селищно_образувание_Долна_Трака | CC BY-SA
    kolhozen_pazar | wikimapia | http://wikimapia.org/37746523/bg/Квартал_„Колхозен_пазар“ | CC BY-SA
    kv_levski | wikimapia | http://wikimapia.org/900042/bg/ж.к._Васил_Левски | CC BY-SA
    tsentar | wikimapia | http://wikimapia.org/34550058/bg/Център | CC BY-SA
    vinitsa | wikimapia | http://wikimapia.org/2357709/bg/Квартал_„Виница“ | CC BY-SA
    zlatni_pyasatsi | wikimapia | http://wikimapia.org/72694/bg/Златни_пясъци | CC BY-SA
== data/places.json sha256: 3dffc2649b75792a bytes: 128401
 meta keys: ['by_kind', 'by_zone_src', 'count', 'excluded', 'generated', 'licence_address', 'licence_osm', 'licence_registry', 'licence_wikidata', 'quarter_attribution']
  quarter_attribution codes: ['asparuhovo', 'briz', 'grackata_mahala', 'hristo_botev', 'izgrev_kv', 'kolhozen_pazar', 'kv_levski', 'mladost2', 'pobeda', 'sv_ivan_rilski', 'trakia', 'troshevo', 'tsentar', 'vladislavovo']
  entry key sets: {('label', 'licence', 'src', 'url'): 14}
  src values: {'wikimapia': 13, 'openstreetmap': 1}
    asparuhovo | wikimapia | http://wikimapia.org/899730/bg/Квартал_„Аспарухово“ | CC BY-SA
    briz | wikimapia | http://wikimapia.org/3710735/bg/кв._Бриз_(кв._Почивка) | CC BY-SA
    grackata_mahala | wikimapia | http://wikimapia.org/34550032/bg/Гръцката_махала | CC BY-SA
    hristo_botev | wikimapia | http://wikimapia.org/7010973/bg/Квартал_„Христо_Ботев“ | CC BY-SA
    izgrev_kv | wikimapia | http://wikimapia.org/17153506/bg/Селищно_образувание_Изгрев | CC BY-SA
    kolhozen_pazar | wikimapia | http://wikimapia.org/37746523/bg/Квартал_„Колхозен_пазар“ | CC BY-SA
    kv_levski | wikimapia | http://wikimapia.org/900042/bg/ж.к._Васил_Левски | CC BY-SA
    mladost2 | openstreetmap | https://www.openstreetmap.org/copyright | ODbL
    pobeda | wikimapia | http://wikimapia.org/900033/bg/жк._Победа | CC BY-SA
    sv_ivan_rilski | wikimapia | http://wikimapia.org/15276583/bg/кв._Св._Иван_Рилски | CC BY-SA
    trakia | wikimapia | http://wikimapia.org/37746532/bg/квартал_„Тракия“ | CC BY-SA
    troshevo | wikimapia | http://wikimapia.org/8281415/bg/кв._Трошево | CC BY-SA
    tsentar | wikimapia | http://wikimapia.org/34550058/bg/Център | CC BY-SA
    vladislavovo | wikimapia | http://wikimapia.org/899999/bg/Квартал_„Владислав_Варненчик“ | CC BY-SA
== data/place_categories.json sha256: 9064705a06477c1a bytes: 77998
 meta keys: ['contains_cadastral_id', 'contains_personal_data', 'curated_forms', 'generated', 'generator', 'legacy_bundle_sha', 'legacy_dropped_by_m3', 'n_chips', 'n_forms', 'n_legacy_dropped_by_m3', 'n_legacy_rows', 'n_locations', 'rule', 'rule_curated', 'rule_legacy', 'rule_legacy_m3', 'rule_locations', 'rule_sha', 'rule_zone_overrides', 'rule_zones', 'schema', 'sources', 'what', 'zone_alias_overrides', 'zone_alias_skipped', 'zone_generic_words', 'zones_unmatched']
The three data sha256 match the _meta pins in fixtures (eb8fa85c…, 3dffc264…, 9064705a…) ✓. Wait — fixtures _meta.inputs says data/places.json: 3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66 — matches prefix. Good.

  quarter_attribution: places 14 codes, hotels 7 codes ✓ (matches "14/7"). All entries {label, licence, src, url} ✓. src ∈ {wikimapia, openstreetmap} ✓. mladost2 url = osm copyright ✓. Licence strings: CC BY-SA / ODbL.

  Now check SIGNED_POLYGON codes used in rows vs attribution map equality: places rows SIGNED_POLYGON codes (42 rows) — distinct codes should equal the 14 map keys; hotels 15 rows → 7 keys. Also check geometry/cadastre: search for 'coordinates', 'geometry', 'polygon', 'uin' in data files. Note hotels rows carry 'uins' key — cadastral? Plan says recall_sweep never reads uins. G16 says grep -c coordinates → 0. Check "uins" presence — it's a pre-existing field (225 hotels). The task item (6) says "нула геометрия/кадастър" — presumably no NEW geometry/cadastre in delivery; check for keys named geometry/coordinates/polygon.

  Also count rows with quarter+zone changed: SIGNED_POLYGON rows 42+15=57. And verify each of those has zone == quarter name? Check.

  Then categories _meta: contains_cadastral_id — check value. Also licence strings in places/hotels _meta — "лицензните низове" — compare with constants in tests? test_places_public_bundle has license constants. Check.

  Let me run these data checks now.hotels SIGNED_POLYGON rows: 15 distinct codes: 7
  codes==map: True | codes-not-in-map: set() | map-not-used: set()
  zone==quarter.name: 15 of 15
places SIGNED_POLYGON rows: 42 distinct codes: 14
  codes==map: True | codes-not-in-map: set() | map-not-used: set()
  zone==quarter.name: 42 of 42
data/hotels.json coordinates: 0 geometry: 0 polygon_key: 0 uins: 230
data/places.json coordinates: 0 geometry: 0 polygon_key: 0 uins: 0
data/place_categories.json coordinates: 0 geometry: 0 polygon_key: 0 uins: 0
cats contains_cadastral_id: False personal: False
hotels district src: {'KAIS': 225} locality src: {'REG': 3, 'KAIS': 4}
places district src: {'KAIS': 150} locality src: {'REG': 1, 'KAIS': 4}
tests/test_places_public_bundle.py:16:identifier, both licence lines verbatim (§6 К8 ships two of them inside `_meta`: ODbL 1.0
tests/test_places_public_bundle.py:21:English) must quote BOTH licence lines byte for byte.
tests/test_places_public_bundle.py:104:META_KEYS = {"generated", "count", "by_kind", "by_zone_src", "licence_osm",
tests/test_places_public_bundle.py:105:             "licence_registry", "licence_wikidata", "licence_address",
tests/test_places_public_bundle.py:112:ATTRIB_KEYS = {"src", "url", "label", "licence"}
tests/test_places_public_bundle.py:141:LICENCE_OSM = 'Имената от OpenStreetMap: „имена на обекти © OpenStreetMap contributors, ODbL“ — дословната атрибуция на web/varna_poi_names.json; лиценз ODbL 1.0. Самият пакет е производна база (систематична извадка) и се публикува под ODbL 1.0 — share-alike. Показването на един ред в попъп е Produced Work и за него атрибуцията стига (К8).'
tests/test_places_public_bundle.py:142:LICENCE_WIKIDATA = 'Разгърнати имена (псевдоними за търсене) на 3 места: Wikidata Q7035695, Q12291800, Q12299161, CC0 1.0 Universal, достъп 03.09.2026. Низовете са зафиксирани с датата на достъп (снапшотът), не се теглят живо; изворът на всеки псевдоним стои в `old_names_src`.'
tests/test_places_public_bundle.py:143:LICENCE_ADDRESS = 'Адресите: КАИС адресното поле на тялото под пина (© АГКК — отворените данни, върху които стоят и координатите; условията на ФАЗА_0_лицензи.md); регистровите адреси (Община Варна, МОН/НЕИСПУО, ИАМН) и Националният туристически регистър: отделни факти от регистрите (чл. 4 ЗАПСП), не копие на регистър; адресите от OpenStreetMap: „© OpenStreetMap contributors, ODbL“ — лиценз ODbL 1.0. Изворът на всеки адрес стои в `address.src`; токени за собственост не влизат в адреса.'
tests/test_places_public_bundle.py:144:LICENCE_REGISTRY = 'Имената и регистровите данни: отделни факти от регистрите (чл. 4 ЗАПСП; без масово копиране на регистър) — Регистър на лечебните заведения (ИАМН), Регистър на училищата и детските заведения (Община Варна), Регистър на училищата (МОН/НЕИСПУО, одобрено 21.08); източникът на всеки ред стои в `src`. Координатите: собствена геолокация върху отворените данни на КАИС (условията на ФАЗА_0_лицензи.md).'
tests/test_places_public_bundle.py:151:# over the address values, so a token that slips into a licence line, a zone or a
tests/test_places_public_bundle.py:285:    def test_the_wikidata_licence_line_is_verbatim(self):
tests/test_places_public_bundle.py:289:        self.assertEqual(self.doc["_meta"]["licence_wikidata"], LICENCE_WIKIDATA)
tests/test_places_public_bundle.py:290:        self.assertIn("CC0 1.0 Universal", LICENCE_WIKIDATA)
tests/test_places_public_bundle.py:291:        self.assertIn("достъп 03.09.2026", LICENCE_WIKIDATA)
tests/test_places_public_bundle.py:293:            self.assertIn(qid, LICENCE_WIKIDATA)
tests/test_places_public_bundle.py:381:        openstreetmap entry points at the ODbL copyright page and matches no
tests/test_places_public_bundle.py:471:    def test_the_address_licence_line_is_verbatim(self):
tests/test_places_public_bundle.py:474:        # ODbL. Not one of them is new to this delivery (план §2 т. 5), so the README
tests/test_places_public_bundle.py:475:        # licence table is untouched and the line itself is pinned right here.
tests/test_places_public_bundle.py:476:        self.assertEqual(self.doc["_meta"]["licence_address"], LICENCE_ADDRESS)
tests/test_places_public_bundle.py:477:        self.assertIn("ODbL 1.0", LICENCE_ADDRESS)
tests/test_places_public_bundle.py:478:        self.assertIn("`address.src`", LICENCE_ADDRESS)
tests/test_places_public_bundle.py:481:        # Unlike the hotels licence, neither licence line here names cadastral address
tests/test_places_public_bundle.py:485:    def test_both_licence_lines_are_verbatim(self):
tests/test_places_public_bundle.py:486:        # §6 К8: one file, two licence notes — the OSM rows travel under ODbL 1.0
Data checks pass:
  - 57 SIGNED_POLYGON rows (42 places + 15 hotels), each with zone==quarter.name.
  - 201 quarter rows from REG/KAIS/SIGNED_OVERRIDE (39+10+115+25+12).
  - Zero coordinates/geometry/polygon keys; hotels keep legacy `uins` field (230 occurrences — 225 rows + probably _meta mention). Note: hotels carry `uins` — pre-existing, not new geometry.
  - Map↔codes equality exact both directions (14/7).
  - Licence constants in tests match the _meta lines? I should verify equality byte-for-byte — run the bundle tests? They read REPO/data paths. tests/test_places_public_bundle.py — how does it locate data? Let me check quickly whether I can run those two bundle tests + b3_gates test. They may need gates/ or other files. Actually running unittest is read-only (mostly). Let me check what test_places_public_bundle.py reads.

  Then the fixtures measurement — the big one. Then variant B.

  Let me look at test_places_public_bundle.py header to see path resolution and whether it's runnable here.

• Данните потвърдени. Сега пускам bundle тестовете и фикстурния харнес в паметта."""Phase-2 plan §2 Д1/Д2 + §5 G1/G2 — SHA-pinned gate for the places payload.

Guards `data/places.json`: the 135-record delivery of schools, universities, hospitals,
ДКЦ, hospices and kindergartens exported from varna_3d (`src/export_fire_varna_places.py`,
HEAD ba78a25 on branch rezhimi, 02.09.2026), which the places branch of the search
lazy-loads next to `data/hotels.json`. Sibling of tests/test_hotels_public_bundle.py: every
rule below has its twin there unless a comment says why it cannot.

What "SHA-pinned" means here (search plan §14, v2.5): the pinned bytes are the TRACKED
blob — `.gitattributes` (`* text=auto eol=lf`) normalizes the delivery to LF on commit, so
the blob GitHub Pages serves and a clone checks out is the LF one. A delivery sha is
measured on `git show HEAD:…`, never on a Windows working tree.

Beyond the bytes the gate asserts the publish contract of phase-2 plan §2 Д1: exactly the
eight record keys, closed enumerations for kind/src/status, the delivery bbox, no cadastral
identifier, both licence lines verbatim (§6 К8 ships two of them inside `_meta`: ODbL 1.0
for the OSM rows, "separate facts" for the registry rows), no personal data in the free
text, and unique (skeleton(name), zone).

Plan §5 G9 (phase-2 plan §4 C13) adds one more: both README mirrors (Български /
English) must quote BOTH licence lines byte for byte.

The doctor rule (§2 Д1 + §6 К7) is the one place this gate cannot copy its sibling. The
hotel gate treats any "д-р" as a personal datum; here ten of the 135 names carry a doctor's
name that IS the institution's name (ОУ „Д-р Никола Димитров“, Медицински университет
„Проф. д-р Параскев Стоянов“, СБАГАЛ „Проф. д-р Д. Стаматов“…). So a hit counts only when
no institutional word stands in the same string — the К7 list, matched as a word PREFIX.
A private practice ("д-р Иванов", no institution) still goes red.

G2 ("the test RUNS and FAILS") needs the gate pointed at a deliberately corrupted copy. Set
the environment variable **FIRE_VARNA_PLACES_PATH** to an alternative places file and every
assertion below runs against it; unset, the gate reads `data/places.json`.

Run: python -m unittest discover -s tests
"""
import gzip
import hashlib
import json
import os
import pathlib
import re
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
# G2 override: the corrupted copy is fed in through the environment, not by editing data/.
PLACES = pathlib.Path(os.environ.get("FIRE_VARNA_PLACES_PATH") or (REPO / "data" / "places.json"))

# The tracked LF blob, measured at C11 (varna_3d HEAD ba78a25, branch rezhimi):
#   git -C ../varna_3d show HEAD:data/fire_varna_places.json > data/places.json
# F12 (P7 = М2 + М3 + М6, commit adad6b0): the delivery was re-exported — М2 stopped
# dropping a typed location on `map_label: false`, so five more places carry a quarter
# — and the three numbers are re-measured on the NEW blob. The docstring rule holds:
# a drift is a re-delivery, and this IS the re-delivery.
# 121 621 B / 35aaf0cd5811… → the values below.
# Б3 (07.09, varna_3d 05f485e `data/fire_varna_places.json`): the quarter
# delivery re-exports the typed fields — 42 rows gain a SIGNED_POLYGON quarter
# and `_meta` gains `quarter_attribution` — so the three numbers are re-measured
# on the NEW blob. A drift is a re-delivery, and this IS the re-delivery.
PLACES_SHA256 = "3dffc2649b75792aaa94ede70cf9f3a0805d3f53c4721be48375c3e1a1533e66"
PLACES_BYTES = 128401
PLACES_GZIP9 = 14748

EXPECTED_COUNT = 150
TOP_LEVEL_KEYS = {"_meta", "places"}
# Phase-2 plan §2 Д1 + ЛОТ 1в (ADR 008 D1/S2): exactly these TEN keys on every
# record — no `i`, no notes, no cadastral identifier. `old_names_src` is the ninth,
# `address` (ЛОТ 1в-Б, ADR 008 D5) the tenth.
RECORD_KEYS = {"address", "district", "kind", "lat", "locality", "lon", "name",
               "old_names", "old_names_src", "quarter", "src", "status", "zone"}
# ЛОТ 1в-В (ADR 008 D9, план §3г/§3ж S1/S4/S6) — the three TYPED location fields.
# Each is `null` or EXACTLY {name, src, code}; the district is the one field that is
# never null, because „район X“ is the honest answer when nothing else can be
# sourced. The code lists are CLOSED: a public row may carry no location that the
# dictionary of the same delivery does not name.
LOCATION_KEYS = {"name", "src", "code"}
# Б3 (план §3.2 И4/И4б, О18): the quarter list gains the two signed sources; the
# LOCALITY keeps a list of its OWN, because sharing the quarter's list silently
# widened the locality too — a `locality` by DISTRICT_FALLBACK is a thing no
# decision allows (G16). A DISTRICT_FALLBACK quarter is the DISTRICT wearing the
# quarter field: its code comes from DISTRICT_CODES, never from QUARTER_CODES.
QUARTER_SRC = {"REG", "KAIS", "SIGNED_OVERRIDE", "SIGNED_POLYGON", "DISTRICT_FALLBACK"}
LOCALITY_SRC = {"REG", "KAIS", "SIGNED_OVERRIDE", "SIGNED_POLYGON"}
DISTRICT_SRC = {"KAIS", "SIGNED_OVERRIDE"}
DISTRICT_CODES = {"primorski", "odesos", "mladost", "asparuhovo", "vladislav_varnenchik"}
# F12: the lists are the codes of THIS delivery, the same 20 + 5 + 5 the dictionary
# names and `index.html` accepts — `briz` and `mladost` in, `manastirski_rid` out,
# `morska_gradina` a locality. A code the client's closed list does not know makes
# it reject the whole file, so the three lists here, the dictionary and the client
# have to stay one set.
QUARTER_CODES = {"asparuhovo", "borovets_yug", "briz", "chaika_kk", "chaika_kv",
                 "dolna_traka", "druzhba", "galata", "grackata_mahala",
                 "hristo_botev", "izgrev_kv", "kk_konstantin_elena",
                 "kolhozen_pazar", "kv_levski", "mladost", "mladost2", "pobeda",
                 "priboy", "sv_ivan_rilski", "trakia", "troshevo", "tsentar",
                 "vazrazhdane", "vazrazhdane1", "vazrazhdane2", "vinitsa",
                 "vladislavovo", "zlatni_pyasatsi"}
LOCALITY_CODES = {"morska_gradina", "sveti_nikola", "vilite", "zelenika", "zpz"}
# F12: М2 gave five more places a REG quarter (44 → 49 rows), and one place moved
# into the „Морска градина“ locality (4 → 5).
QUARTER_BY_SRC = {"REG": 39, "KAIS": 10, "SIGNED_POLYGON": 42}
LOCALITY_COUNT = 5
# Б3 (план §1.5б) — the EXACT `_meta` key set of this bundle: ten keys, the
# tenth being the provenance map this delivery adds. G17 is the SET, not the count.
META_KEYS = {"generated", "count", "by_kind", "by_zone_src", "licence_osm",
             "licence_registry", "licence_wikidata", "licence_address",
             "quarter_attribution", "excluded"}
# Б3 (решение 8 + G17, О17) — the provenance map of the signed quarter
# polygons: per bundle, EQUAL to the set of SIGNED_POLYGON codes it carries, four
# keys per entry, a CLOSED source set and a URL rule per source. Measured 07.09:
# places 14 codes (13 wikimapia + 1 openstreetmap), hotels 7 (all wikimapia); the


• Bundle tests are runnable in this copy (they read REPO/data). They might check README mirrors — G9 needs README file, which is not in the copy. That test would fail due to missing README — expected in this partial copy, not a defect of the commit. Let me just run the two bundle tests and see.

  Then the fixtures. Then variant B. Let me run bundle tests first.Traceback (most recent call last):
  File "C:\Users\Petar\AppData\Local\Temp\tmp.ZgNtqY5ZQ3\staged\tests\test_places_public_bundle.py", line 499, in test_readme_carries_licence_lines
    readme = (REPO / "README.md").read_text(encoding="utf-8")
  File "C:\Program Files\Python310\lib\pathlib.py", line 1134, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
  File "C:\Program Files\Python310\lib\pathlib.py", line 1119, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Petar\\AppData\\Local\\Temp\\tmp.ZgNtqY5ZQ3\\staged\\README.md'

======================================================================
ERROR: test_readme_carries_licence_line (tests.test_hotels_public_bundle.HotelsBundleTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Petar\AppData\Local\Temp\tmp.ZgNtqY5ZQ3\staged\tests\test_hotels_public_bundle.py", line 507, in test_readme_carries_licence_line
    readme = (REPO / "README.md").read_text(encoding="utf-8")
  File "C:\Program Files\Python310\lib\pathlib.py", line 1134, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
  File "C:\Program Files\Python310\lib\pathlib.py", line 1119, in open
    return self._accessor.open(self, mode, buffering, encoding, errors,
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Petar\\AppData\\Local\\Temp\\tmp.ZgNtqY5ZQ3\\staged\\README.md'

----------------------------------------------------------------------
Ran 66 tests in 0.042s

FAILED (errors=2)
66 tests ran, only 2 errors — both are README.md missing in this partial copy (a copy artifact, not a delivery defect). 64 passed. That covers licence lines verbatim, closed sets, QUARTER_CODES, map equality etc. Good.

  Now the fixtures harness measurement. I'll write an inline python that loads the harness module from staged/tests/test_granitsi_fixtures.py and runs:
  - positive assertions for the 9 reference fixtures (assert_case against answers_of)
  - broken halves: changed set == fails_on, observed matches
  - fixture 10 extras: qtk/qph empty, own_quarter None, gate quiet/loud

  Instead of running unittest (which would invoke Node tests and fail on missing index.html), I'll drive the functions directly.=== POSITIVE (fixture's own ops applied) ===
street_collision OK
district_retention OK
mladost_kind_collision OK
order_identity OK
parent_child OK
parent_child_vazrazhdane OK
chaika_sibling_merge OK
asparuhovo_no_child_rows OK
district_fallback_typed OK
=== BROKEN halves ===
street_collision street_named_quarter changed==fails_on: True  | observed: True | assert raises: True
district_retention fallback_over_the_district_field changed==fails_on: True  | observed: True | assert raises: True
mladost_kind_collision fallback_plus_unsigned_code changed==fails_on: True  | observed: True | assert raises: True
order_identity correct_quarter_moves_the_row_up changed==fails_on: True  | observed: True | assert raises: True
parent_child child_code_outside_the_dictionary changed==fails_on: True  | observed: True | assert raises: True
parent_child_vazrazhdane child_renamed_by_name changed==fails_on: True  | observed: True | assert raises: True
chaika_sibling_merge ten_rows_renamed_one_op_each changed==fails_on: True  | observed: True | assert raises: True
asparuhovo_no_child_rows child_row_wears_the_parent_name changed==fails_on: True  | observed: True | assert raises: True
district_fallback_typed engine_without_own_quarter changed==fails_on: True  | observed: True | assert raises: True
district_fallback_typed district_null changed==fails_on: True  | observed: True | assert raises: True
district_fallback_typed foreign_district -> gate-asserted (skip search)
All 9 reference fixtures: positive numbers reproduce exactly (including identities order), and every _broken moves exactly fails_on with observed values, and assert raises. 

  Now fixture 10 extras: gate quiet/loud, qtk/qph empty. And item (2) variant B measurements: „кв. Левски" 14/12 etc. on staged engine; and head engine over same data for R\MR parity; also verify „възраждане 2"/„младост 2" = 0.

  For the head engine: exec head text with module.__file__ set to staged path so REPO_ROOT resolves to staged/. Actually REPO_ROOT = pathlib.Path(__file__).resolve().parents[2] — if I set module.__file__ = staged recall_sweep path, both engines read staged/data. That gives "head engine over the same data" cleanly. legacy_by_row comes from CATS (place_categories.json legacy_by_row). Fine.

  Note: module body executes main-only under __name__ guard; but module-level code might write? Earlier docstring says read-only except report; also line 90 FREEZE flag; no writes at import. OUTDIR writes happen in functions only.

  One concern: harness's answer() calls reindex using reference.Rec etc. For head engine, I can use the same harness reindex — but harness reindex references reference.hotels attribute assignment etc. It should work with any module having Rec, FORM_IDX, in_class, group_of, key_of. Head engine has same API (it's the older version). Let me check head has same names: FORM_IDX, in_class, group_of, key_of, Rec, search, EXACT_NAME... Head line 1133 M7_ENABLED exists. Probably same. Also head engine lacks own_quarter? Head at 2126 has DISTRICT_CODES, check own_quarter in head: earlier grep for head showed no own_quarter match (grep pattern included own_quarter — output for head didn't show def own_quarter). Right, head does NOT have own_quarter (that's new in staged). So harness answer() uses reference.own_quarter — would fail on head module. I'll compute with_quarter using r.quarter directly for head, or use a custom answer. For R\MR parity, I just need branch + names for non-prefixed queries — compare staged vs head over same data. Choose queries without M7 letter prefixes: e.g. the fixture queries (младост, чайка, възраждане, аспарухово, дружба, училище младост, училище район младост, детска градина дойран) plus a set of random-ish queries. Note: staged changed more than MR? diff staged vs head recall_sweep: check what else changed. The diff between head and staged versions — let me diff them to see all changes (MR filter, own_quarter, is_fallback_quarter, M7_PREFIXES moved?, etc.). That's part of review anyway.

  Also variant B measurements on staged: кв. Левски (14 n, 12 with_quarter), кв. Тракия 4/4, кв. Христо Ботев 4/3, ж.к. Св. Иван Рилски 4/2, възраждане 2 → 0, младост 2 → 0. Fixture 11 lists кв. Левски 14 names, кв. Тракия 4, ж.к. Св. Иван Рилски 4 — and I already verified those identities match in fixture 11? No — fixture 11 is "node" kind, skipped in my run. But I can verify its reference-side expectations via ref.search directly (branch + names). Let me do that too.

  Also gate checks for fixture 10 (д): check_lot1v_v_gate quiet for own fallback, loud for foreign. The harness test does it; I replicate.

  Let me write the second measurement script.f10: quarter==ops: True | own_quarter None: True | qtk empty: True | qph empty: True | dph kept: True
f10 gate: quiet on own fallback: True | loud on foreign: True ['ПГГСД „Николай Хайтов“: DISTRICT_FALLBACK кварталът не е собственият район ({"name": "Одесос", "code": "odesos", "src": "DISTRICT_FALLBACK"})']
=== variant B (staged engine) ===
кв. Левски             branch=M7-bare-location   n=14 with=13 without=1
кв. Тракия             branch=M7-bare-location   n=4 with=4 without=0
кв. Христо Ботев       branch=M7-bare-location   n=4 with=4 without=0
ж.к. Св. Иван Рилски   branch=M7-bare-location   n=4 with=3 without=1
възраждане 2           branch=M3                 n=0 with=0 without=0
младост 2              branch=M3                 n=0 with=0 without=0
левски                 branch=M7-bare-location   n=14 with=13 without=1
=== fixture 11 reference side ===
Traceback (most recent call last):
  File "<stdin>", line 38, in <module>
AttributeError: module 'harness' has no attribute 'has_key_of'
Variant B discrepancy! Task says: „кв. Левски" 14/12, „ж.к. Св. Иван Рилски" 4/2. I measured 14/13 and 4/3. Hmm. Wait — maybe the task's format is n/with? Plan §8 проба 4: "голото `левски` → 14 реда, 12 с код `kv_levski`" — 12 with CODE kv_levski, not with own_quarter! And variant Б: "стават 14 / 4 / 4 / 4 с 12 / 4 / 3 / 2 верни реда" — "верни реда" = rows with the right code. So the second number is rows carrying the expected quarter code, not own_quarter count.

  Check: кв. Левски n=14, rows with code kv_levski should be 12 (I measured with=13 own_quarter — one row has another quarter, e.g. ОДГ №14 "Дружба" has kv_levski? Actually fixture 7: ОДГ №14 "Дружба" is кв. Левски. Let me count by code). ж.к. Св. Иван Рилски: 4 rows, 2 with code sv_ivan_rilski? Task says 4/2. My own_quarter count was 3. So the plan's "верни реда" = rows with the matching code: 12/4/3/2. кв. Христо Ботев 4/3 → 3 with hristo_botev code.

  So measure: n and count of rows whose quarter.code == expected code. Let me redo with code counts. Also fixture 11 reference side — use ref.has_key_of (it's in the engine module, not harness).

  Also need head-engine parity. Let me run that now.=== variant B, code-count form (plan §9: 14/12, 4/4, 4/3, 4/2) ===
кв. Левски             n=14 code=12
кв. Тракия             n=4 code=4
кв. Христо Ботев       n=4 code=3
ж.к. Св. Иван Рилски   n=4 code=2
=== fixture 11 reference side ===
кв. Левски OK
кв. Тракия OK
ж.к. Св. Иван Рилски OK
чайка OK
училище младост OK
училище район младост OK
=== R\MR parity: staged vs head over same data (queries WITHOUT letter prefixes) ===
queries compared: 18 mismatches: 0
=== queries WITH prefixes: head behaves old way (4/1/24/22 foreign) ===
head кв. Левски             branch=M3 n=4
head кв. Тракия             branch=M3 n=1
head кв. Христо Ботев       branch=M3 n=24
head ж.к. Св. Иван Рилски   branch=M3 n=22
Excellent. Variant B fully verified on the engine side:
  - кв. Левски 14/12 ✓, кв. Тракия 4/4 ✓, кв. Христо Ботев 4/3 ✓, ж.к. Св. Иван Рилски 4/2 ✓, възраждане 2 / младост 2 → 0 ✓.
  - R\MR unchanged: 18 prefix-free queries identical staged vs head over same data, 0 mismatches.
  - Head on prefixed queries gives the old foreign behavior (4/1/24/22 via M3) — confirming the MR filter is what changed.
  - Fixture 11 reference side OK.

  But note: head engine lacks own_quarter — harness reindex(head,...) worked because harness.reindex uses reference.Rec etc. — it worked. But wait: head doesn't have own_quarter; H.reindex(head, ...) — reindex just builds RECS etc. via head.Rec — head.Rec's __init__ may not use own_quarter (head Rec reads quarter directly). Fine, and search results identical for R queries. But is that a fair parity check? The staged engine ALSO changed Rec (qtk uses own_quarter) and location_rows/bare_location_rows d_rows condition (own_quarter). Since the delivery has zero DISTRICT_FALLBACK rows, own_quarter(r) is None iff quarter is None — so behavior identical on this data. Good; the 18/0 confirms.

  Also the "6 места" own_quarter claim (item 3 engine side): "шестте места" — count own_quarter usages in staged engine: Rec init (qtk, qph), location_rows d_rows, bare_location_rows district_hit... let me count. And DISTRICT_FALLBACK semantics in check_lot1v_v_gate (code in DISTRICT_CODES and == own district by code and name). Let me read the gate function at 2160-2200. Also engine_patch anchor from fixture 10 matched exactly once (load_reference asserts count==1 — it ran fine).

  Remaining:
  - diff staged vs head recall_sweep to enumerate all engine changes (to confirm only intended changes).
  - own_quarter six places count.
  - Gates: staged/gates/probe/b3_g11.py — check ALLOWED_NEW includes tests/test_b3_gates.py (амандамент 2, А2-2 — draft, unsigned!). Amendment 2 is a DRAFT (status: ⏳ за подпис). The fix A2-2 says ALLOWED_NEW must gain "tests/test_b3_gates.py". Check staged/gates/probe/b3_g11.py whether it has it. Also A2-1 (probe_places_fv.mjs v7) — that file is not in the copy. A2-3 О26.
  - test_b3_gates.py content — check what it tests.
  - COMMIT_MSG vs §6: byte-compare the quoted block in the plan vs COMMIT_MSG_B3.txt.
  - Item (5) popupFor / И11 — index.html missing, cannot verify. Item (4) validators — missing. Item (2) client M7 branch — missing. Item (3) client ownQuarter — missing.

  Also check staged file count vs the plan's commit-2 list: data 3 + index.html + 2 bundle tests + test_granitsi_fixtures + granitsi_client_probe.mjs + fixtures 07.09 (+ deleted 06.09) + recall_sweep.py = 11 paths + deletion. Task says staged_diff.patch has 13 paths. The patch file is missing entirely.

  Let me diff engines and check gates files, commit message.603a604,629
> def is_fallback_quarter(q):
>     """Б3 (О19): is this `quarter` the DISTRICT wearing the quarter field?
> 
>     1:1 with the client (`index.html` isFallbackQuarter). The delivery of 07.09
>     carries ZERO such rows (measured: quarter srcs = REG/KAIS/SIGNED_OVERRIDE/
>     SIGNED_POLYGON), which is exactly why the rule needs a SYNTHETIC fixture —
>     it guards a channel that is open and unused, not one that is closed.
>     """
>     return bool(q) and q.get(u"src") == u"DISTRICT_FALLBACK"
> 
> 
> def own_quarter(rec):
>     """The quarter a row really HAS — never the district in the quarter field.
> 
>     1:1 with the client (`index.html` ownQuarter). A DISTRICT_FALLBACK row is a
>     район row: its only home is the district branch, and that branch reaches a
>     row ONLY while it has no quarter of its own (`d_rows`, `district_hit`). Read
>     naively, the fallback would (а) turn district words into QUARTER tokens and
>     phrases and (б) push the row out of „район X“ — the row would vanish from the
>     one query that can still find it, silently. Six places ask this question and
>     all six read it here.
>     """
>     q = getattr(rec, "quarter", None)
>     return q if (q and not is_fallback_quarter(q)) else None
> 
> 
621c647
<         self.qtk = self._loc_tokens(u"quarter", self.quarter)
---
>         self.qtk = self._loc_tokens(u"quarter", own_quarter(self))
623c649
<         self.qph = self._loc_phrases(u"quarter", self.quarter)
---
>         self.qph = self._loc_phrases(u"quarter", own_quarter(self))
1123c1149
<     d_rows = [r for r in cls if r.quarter is None and phrase in r.dph]
---
>     d_rows = [r for r in cls if own_quarter(r) is None and phrase in r.dph]
1167c1193
<     district_hit = [r for r in cls if r.quarter is None and phrase in r.dph]
---
>     district_hit = [r for r in cls if own_quarter(r) is None and phrase in r.dph]
1257c1283,1291
<     if not has_key and bare_location_query(R):
---
>     # Б3 (§9 т. 1 вариант Б, подписан 07.09 §14): the TYPE PREFIX a human types
>     # („кв.“, „ж.к.“) is not a place and is not significant, so `кв. Левски` fell
>     # through М7 to М3 and answered with 4 FOREIGN rows. `M7_PREFIXES` already names
>     # the closed list; М7 — and ONLY М7 — reads the query with its LETTER prefixes
>     # dropped. The DIGITS stay in (§13 т. 5): dropping „2“ makes „възраждане 2“
>     # answer with the PARENT's rows, which is worse than the measured 0. Every other
>     # branch below keeps the untouched `R`.
>     MR = [t for t in R if t.num or t.s not in M7_PREFIXES]
>     if not has_key and bare_location_query(MR):
1263c1297
<         bare = bare_location_rows(R, cls)
---
>         bare = bare_location_rows(MR, cls)
2146,2147c2180,2185
<         want = (r.quarter or {}).get("name") or (u"район " + r.district["name"])
<         if r.zone != want:
---
>         want = (own_quarter(r) or {}).get("name") or (u"район " + r.district["name"])
>         # О20: a DISTRICT_FALLBACK row is ONE district in TWO forms — the bare name
>         # the exporter writes today for 375/375 rows, and the honest „район X“.
>         # Both are accepted; a third label is a different delivery, not a row.
>         labels = [want, r.quarter["name"]] if is_fallback_quarter(r.quarter) else [want]
>         if r.zone not in labels:
2149,2150c2187,2196
<                        % (r.name, r.zone, want))
<         if r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]:
---
>                        % (r.name, r.zone, u" / ".join(labels)))
>         if is_fallback_quarter(r.quarter):
>             # О19: the fallback code is a DISTRICT code and it has to BE this row's
>             # own district — name and code — or the row wears somebody else's район.
>             if (r.quarter.get("code") not in DISTRICT_CODES
>                     or r.quarter.get("code") != r.district.get("code")
>                     or r.quarter.get("name") != r.district.get("name")):
>                 bad.append(u"%s: DISTRICT_FALLBACK кварталът не е собственият район (%s)"
>                            % (r.name, json.dumps(r.quarter, ensure_ascii=False)))
>         elif r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]:
=== diff line count:
83
615:def own_quarter(rec):
647:        self.qtk = self._loc_tokens(u"quarter", own_quarter(self))
649:        self.qph = self._loc_phrases(u"quarter", own_quarter(self))
1149:    d_rows = [r for r in cls if own_quarter(r) is None and phrase in r.dph]
1193:    district_hit = [r for r in cls if own_quarter(r) is None and phrase in r.dph]
2180:        want = (own_quarter(r) or {}).get("name") or (u"район " + r.district["name"])
===
DISTRICT_CODES = (u"primorski", u"odesos", u"mladost", u"asparuhovo",
                  u"vladislav_varnenchik")


def check_lot1v_v_gate():
    """The ЛОТ 1в-В gate: the typed schema, the guards and the nine queries.

    Same fail-loud contract as the four gates above. The schema half is what
    makes „100 % с извор“ measurable — a record without a district, a code
    outside the closed lists or a compat label that does not follow from the
    typed fields is red here, in the суite, without a browser."""
    bad = []
    if not LEGACY_SHA_OK:
        bad.append(u"legacy_bundle_sha: речникът е строен срещу друг пакет — "
                   u"старите зонови думи са изключени (fail-closed)")
    for r in RECS:
        if not r.district or r.district.get("code") not in DISTRICT_CODES:
            bad.append(u"%s: район извън затворения списък (%s)"
                       % (r.name, json.dumps(r.district, ensure_ascii=False)))
            continue
        want = (own_quarter(r) or {}).get("name") or (u"район " + r.district["name"])
        # О20: a DISTRICT_FALLBACK row is ONE district in TWO forms — the bare name
        # the exporter writes today for 375/375 rows, and the honest „район X“.
        # Both are accepted; a third label is a different delivery, not a row.
        labels = [want, r.quarter["name"]] if is_fallback_quarter(r.quarter) else [want]
        if r.zone not in labels:
            bad.append(u"%s: `zone` = %s, а типовите полета дават %s"
                       % (r.name, r.zone, u" / ".join(labels)))
        if is_fallback_quarter(r.quarter):
            # О19: the fallback code is a DISTRICT code and it has to BE this row's
            # own district — name and code — or the row wears somebody else's район.
            if (r.quarter.get("code") not in DISTRICT_CODES
                    or r.quarter.get("code") != r.district.get("code")
                    or r.quarter.get("name") != r.district.get("name")):
                bad.append(u"%s: DISTRICT_FALLBACK кварталът не е собственият район (%s)"
                           % (r.name, json.dumps(r.quarter, ensure_ascii=False)))
        elif r.quarter and r.quarter.get("code") not in LOCATIONS[u"quarter"]:
            bad.append(u"%s: квартал извън речника (%s)" % (r.name, r.quarter.get("code")))
        if r.locality and r.locality.get("code") not in LOCATIONS[u"locality"]:
            bad.append(u"%s: допълнително място извън речника (%s)"
                       % (r.name, r.locality.get("code")))
        if r.zone in r.legacy:
            bad.append(u"%s: старата зонова дума е и показваната зона (%s)"
                       % (r.name, r.zone))
    bad += gate_query_failures(u"lot1v_v")
    if has_key_of(u"бул. владислав варненчик 225"):
        bad.append(u"„бул. владислав варненчик 225“ носи класов ключ — адресната "
                   u"търсачка на сградите вече не е отгоре")
    return bad


The engine diff is exactly the intended set:
  1. is_fallback_quarter + own_quarter added (О19).
  2. Rec.qtk/qph read own_quarter (2 places).
  3. location_rows d_rows → own_quarter.
  4. bare_location_rows district_hit → own_quarter.
  5. search(): MR filter for M7 only (variant B), bare_location_query(MR), bare_location_rows(MR).
  6. check_lot1v_v_gate: label forms (О20) + fallback code/name check (О19) using own_quarter for label.

  own_quarter "six places": definition + usages: qtk, qph, d_rows (location_rows), district_hit (bare_location_rows), gate label (want) — that's 5 use sites + the fixture-10 patch target line 1149... Wait, the docstring says "Six places ask this question and all six read it here." Grep shows uses at 647, 649, 1149, 1193, 2180 = 5 use sites in engine. Hmm, plus is_fallback_quarter uses at 2185, 2188... "six places" maybe counts the client's six? Task item (3): "own_quarter на шестте места" — engine docstring says six places. Grep found 5 `own_quarter(` call sites (647, 649, 1149, 1193, 2180). Plus maybe LOCATIONS... Let me count again: lines 615 (def), 647, 649, 1149, 1193, 2180. That's 5 calls. Hmm. In the client there may be 6. Or maybe the harness `answer()` counts as the sixth? Actually the harness answer() uses reference.own_quarter for with/without split — that's the sixth reader. Plausible. But note the engine_patch in fixture 10 replaces line 1149's d_rows — "махни ownQuarter от :7118" refers to client line. The fixture's patch anchor `    d_rows = [r for r in cls if own_quarter(r) is None and phrase in r.dph]` appears exactly once (location_rows) — but line 1193 district_hit is similar yet distinct text. OK.

  Hmm wait — is there a sixth use in the engine? Check gate line 2180 uses own_quarter for label. That's the 5th. The docstring's claim of six is engine+? Can't verify client. I'll note: 5 call sites in engine + 1 in harness (with_quarter split) = 6 readers in this copy; client side unverifiable.

  Now check b3_g11.py ALLOWED_NEW (amendment 2 A2-2) and test_b3_gates.py. And COMMIT_MSG byte-compare with plan §6.b3_g11.py ALLOWED_NEW does NOT include "tests/test_b3_gates.py" — exactly the defect amendment 2 (A2-2) describes, and amendment 2 is still a DRAFT (unsigned, "поправките НЕ са приложени през нощта"). So at commit time, `python gates/probe/b3_g11.py HEAD --cached` would report stray_new: ["tests/test_b3_gates.py"] → exit 1 → STOP 22. This is a known, declared blocker awaiting Petar's signature on amendment 2. So the staged state is NOT committable as-is without the amendment-2 fix — the verdict must be НЕГОДНО (or "годно само след подписания амандамент 2 и прилагането на А2-1/А2-2"). Also A2-1 (probe_places_fv.mjs v7) — that file isn't in the copy; can't verify, but amendment says not applied.

  Also note b3_g11.py includes itself in ALLOWED_NEW ("gates/probe/b3_g11.py") but not tests/test_b3_gates.py. Consistent with А2-2.

  Also G9 test depends on gates/release.py, queues — not in copy. Can't run.

  Now COMMIT_MSG_B3.txt vs plan §6. The plan's quoted block:

  ```
  feat(search): quarter search over signed boundaries, QUARTER_CODES +8, cache v7 (D13 atomic delivery)

  data: places delivery with quarter_attribution (D13 ordered) — the three blobs of
  varna_3d 05f485e (places 3dffc264, hotels eb8fa85c, categories 9064705a), with the
  closed lists, the three pins, LEGACY_BUNDLE_SHA and PLACES_CACHE v7 in this very
  commit, because a HEAD whose pins and blobs disagree kills the place search.
  tests: S17 fixtures fail on broken candidates
  ```

  File has exactly these 7 lines. Extract plan block and diff byte-wise. Note plan §6 says the message lives at scratch/places_search/COMMIT_MSG_B3.txt and commit 2 contents include... The plan's commit-2 file list includes tests/granitsi_client_probe.mjs and index.html — both missing from the staged copy. The task said the copy's staged/ has 13 paths in staged_diff.patch — but the patch is absent, and staged/ has only 11 files. So either the copy is incomplete or the staging is incomplete. In this copy I can't tell which; but per instructions I review what's here: index.html absent means the atom commit cannot satisfy the plan (index.html is in commit 2 write-set) and checks (2)-client, (3)-client, (4), (5) are unverifiable.

  Wait — also head/ was supposed to contain index.html (old version). Missing too. And tests/granitsi_client_probe.mjs missing. So the copy omits them — maybe deliberately (too big?), maybe not. My verdict: НЕГОДНО за потвърждаване на пълния обхват; the measured parts all pass, but: (a) index.html, probe, staged_diff.patch absent — 4 of 7 assigned checks unverifiable; (b) b3_g11 ALLOWED_NEW missing test_b3_gates.py → STOP 22 at commit (draft amendment 2 not applied/unsigned).

  Hmm, but careful: the verdict is "ГОДНО за атомния комит на Петър / НЕГОДНО с К30-1…". The known А2-2 defect is already declared in draft amendment 2 and the plan's STOP conditions make it terminal at commit. Given the task asks me to verify and issue a verdict, I should say НЕГОДНО with precise findings: К30-1 (missing index.html/probe/patch in the copy — or if the copy is authoritative, the staging is incomplete), К30-2 (ALLOWED_NEW lacks tests/test_b3_gates.py → G11 stray_new → STOP 22; fix = add the line, pending signed amendment 2). Everything measured passes.

  Let me do the COMMIT_MSG byte comparison and check the _meta key sets of the bundles match the closed META_KEYS in tests (places 10 keys, hotels 8 keys — hotels meta keys: by_zone_src, count, excluded, generated, licence, licence_address, licence_osm, quarter_attribution = 8 ✓; places 10 ✓ — already verified by the 64 passing bundle tests).

  Also "mutation that passes wrongly" for item (4): invent a mutation that passes the validators incorrectly. Since index.html is absent, I can only reason at data level with the bundle-test validators (which I have). The bundle tests enforce: META_KEYS exact set, ATTRIB_KEYS {src,url,label,licence}, ATTRIB_SRC closed {wikimapia, openstreetmap} presumably, url rule per src, map==codes equality. A mutation that would pass wrongly: e.g., rename a SIGNED_POLYGON code in BOTH the rows and the attribution map key simultaneously (e.g. kv_levski → levski_signed everywhere) — equality preserved, closed-src preserved, key sets preserved — but the code is outside QUARTER_CODES closed list... would that be caught? In bundle tests yes (QUARTER_CODES closed). In the client validator? Unknown (file missing). The task asks: "равенство карта↔SIGNED_POLYGON кодове (14/7) — измисли мутация, която минава погрешно" — a mutation that wrongly passes: swap the url of two wikimapia entries (both wikimapia, both valid wikimapia urls) — equality, key set, src, url rule all still hold, but provenance is wrong. E.g. `kv_levski.url` ↔ `tsentar.url`: passes every mechanical check in both validators (closed src, url rule only checks host/pattern presumably). That's a genuinely-passing-wrong mutation. Good example.

  Let me byte-compare COMMIT_MSG with the plan block. Extract lines from plan between the ``` fences after "Съобщението на комит 2, дословно".plan block bytes: 474 | file bytes: 474
plan block repr tail: 'place search.\ntests: S17 fixtures fail on broken candidates\n'
file repr tail: 'place search.\ntests: S17 fixtures fail on broken candidates\n'
file == block: True
file == block.rstrip+'
': True
url-swap passes keyset/src/url-rule/map-equality: True
All measurements done. Update todos to done and write the verdict. Also confirm _meta pins in fixtures match (sha of engine 5a051c8f...). Let me verify engine sha quickly — I can do it mentally? No, do one quick check along with verifying the fixtures _meta engine sha and whether test_granitsi_fixtures test for inputs passes — my harness run already implicitly used the data; but sha check: quick command. Also should I verify the fixture _meta.inputs pins match staged data — I computed prefixes earlier: places 3dffc2649b75792a ✓, hotels eb8fa85cbb67265a ✓, cats 9064705a06477c1a ✓. Engine sha not yet verified. Quick check.5a051c8f1080142896822125300b94cf6bce854e52aa67dcfa95bc93293382cb
want 5a051c8f1080142896822125300b94cf6bce854e52aa67dcfa95bc93293382cb
Write the verdict, ≤700 words, Bulgarian, relative paths (relative to the copy root — e.g. `staged/scratch/places_search/recall_sweep.py:1290`).

• # К30 · Присъда: **НЕГОДНО** (две находки; всичко измеримо мина)

  ## Какво измерих (всичко в паметта, без писане)

  **(1) Фикстурите — напълно възпроизводими.** Заредих `staged/scratch/places_search/recall_sweep.py` като частен модел (`exec` върху текста, `__file__` → staged/, без `main()`; пътищата се резолват към `staged/data` сами). Деветте reference фикстури (1–8, 10): позитивните числа + подредените идентичности се възпроизвеждат **точно**, включително ф.10 със синтетичния DISTRICT_FALLBACK ред (6/20/12 по трите заявки). Всеки `_broken` мести ТОЧНО `fails_on` и `observed` съвпада: ф.1 (1→2 чужди), ф.2 (12→11), ф.3 (20→21), ф.4 (същите 20, `27 ДГ Успех` скача в кварталния блок — множеството непоменато), ф.5 (6→5), ф.6 („възраждане“ 5→4 по име; детските 0/0 не мърдат), ф.7 (30→21, десет op-а), ф.8 (16→17 и 2→1 с падане M7→M3), ф.10 engine_patch котвата улучва веднъж и дава 6→5. Допълнително: qtk/qph празни при fallback, гейтът мълчи за собствен и вие за чужд район.

  **(2) Вариант Б — потвърден.** `staged/.../recall_sweep.py:1290` `MR = [t for t in R if t.num or t.s not in M7_PREFIXES]` — само М7 чете MR, всички останали клонове четат R. Измерено: `кв. Левски` 14/12, `кв. Тракия` 4/4, `кв. Христо Ботев` 4/3, `ж.к. Св. Иван Рилски` 4/2 (второто число = редове с кода, както §9), `възраждане 2`/`младост 2` → 0 (M3). Head двигателят върху **същите** данни: 18 заявки без буквен префикс — 0 разлики (R\MR непроменено); с префикс дава старото 4/1/24/22 чужди. Дифът head→staged е само подписаният набор (own_quarter/is_fallback_quarter, qtk/qph, d_rows, district_hit, MR, гейт О19/О20) — 83 реда, нищо странично.

  **(3) `own_quarter` — 5 четения в двигателя + 1 в харнеса (сплитът with/without) = 6; DISTRICT_FALLBACK семантиката в `check_lot1v_v_gate` (:2188–2195) е точно „код ∈ DISTRICT_CODES И == собствен район по код и име“; етикетът приема двете форми (О20). Клиентската половина (`isFallbackQuarter`/`ownQuarter`/`validTypedLocation`) — неверифицируема, виж К30-1.

  **(4)–(5)** Bundle тестовете: 64/66 зелени; двете грешки са липсващ `README.md` в копието (артефакт на копието). Затворените `_meta` (places 10/hotels 8), `src ∈ {wikimapia, openstreetmap}` + url правило, равенство карта↔SIGNED_POLYGON кодове (14/7, двете посоки) — потвърдени от данните. Мутация, която минава погрешно: размяна на `url` между два wikimapia записа (`kv_levski`↔`tsentar`) — ключове, затворен src, url правило и равенството остават зелени, а произходът е объркан. Валидаторите и `popupFor`/И11 в `staged/index.html` — неверифицируеми, виж К30-1.

  **(6) Данни:** 57 SIGNED_POLYGON реда (42+15, всички с `zone == quarter.name`); 201 реда с REG/KAIS/SIGNED_OVERRIDE квартал; sha256 на трите блоба и на двигателя съвпадат с пиновете в `_meta.inputs`/`engine`; `coordinates/geometry/polygon` — 0; `uins` само заварен при hotels. Лицензните низове — байт-равни на константите в тестовете (минаха).

  **(7) `COMMIT_MSG_B3.txt` — побайтово равен (474 B) на блока в §6.**

  ## Находки

  **К30-1 (блокиращо за пълния преглед):** в копието липсват `staged_diff.patch`, `staged/index.html`, `staged/tests/granitsi_client_probe.mjs` и `head/index.html`. Точна поправка: допълни копието с тези четири пътя (index.html е в write-set-а на комит 2 по §6 — без него точки (2)-клиент, (3)-клиент, (4), (5) и И11 са невериﬁцируеми, а фикстури 9 и 11 не могат да се прогонят). Ако копието е пълно — стейджът е непълен и комитът е невъзможен.

  **К30-2 (STOP 22 при комита):** `staged/gates/probe/b3_g11.py:18-23` — `ALLOWED_NEW` не съдържа `"tests/test_b3_gates.py"` (същият файл, който S29-8 иска) → `stray_new` → exit 1. Точна поправка (вече описана като А2-2 в черновата `ПЛАН_Б3_07.09_амандамент_2.md`, неподписана): добави реда `"tests/test_b3_gates.py"` в `ALLOWED_NEW`. Заедно с А2-1 (v7 в `probe_places_fv.mjs`, невериﬁцируемо тук) чака подписа на амандамент 2.

  Измерената половина на доставката е безукорна; комитът е годен едва след К30-1 (пълен стейдж) и К30-2 (подписан и приложен амандамент 2).

To resume this session: kimi -r session_0a33a872-d6a7-42b3-9694-4146576da098
