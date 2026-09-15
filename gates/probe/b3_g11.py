# -*- coding: utf-8 -*-
"""G11 — нула геометрия, СТРУКТУРНО, по ЦЕЛИЯ комит (S29-4).

Usage: python gates/probe/b3_g11.py <parent> [--cached]

The body below is the script of амандамент №1 S29-4 with THREE declared extensions:

1. `--cached` (амандамент №2 А2-4) makes `changed()` diff <parent> against the INDEX
   (`git diff --cached --name-status -z --find-renames --diff-filter=AMR <parent>`)
   instead of against HEAD. Reason: the Б3 data commit is made by Petar's own hand
   (план §6, О4), so the gate has to be runnable on the STAGED write-set, before that
   commit exists. Without the flag the behaviour is the signed one: <parent> against HEAD.

2. Astra S30-1/S30-2 — the gate reads ONE snapshot and fails loud:
   * S30-1: both the inventory and the CONTENT come from the snapshot the diff selected
     — the index under `--cached` (`git ls-files --cached`, `git show :<path>`), the
     commit under test otherwise (`git ls-tree -r HEAD`, `git show HEAD:<path>`).
     The signed script read `pathlib.Path(f).read_text()`, i.e. the WORKING TREE, so a
     staged geometry with a clean local file scored `geo_hits: []` · exit 0 and a
     missing local file was skipped in silence. An object that cannot be read or parsed
     is now `unreadable` → exit 1, never a skip.
   * S30-2: every git call is `check=True`. A failed git process used to become a green
     gate (`b3_g11.py DOES_NOT_EXIST` → `{"scope": 18, …}` · exit 0); it now prints
     git's own stderr and exits 2 (infrastructure failure ≠ 0 ≠ a clean gate).
   * S30-3: the inventory pathspec was CWD-relative, so the very same gate run from a
     subdirectory silently narrowed its scope (19 → 4 tracked `data/*.json`, without
     changing the exit code). `main()` now moves to `git rev-parse --show-toplevel`
     first and the pathspec is anchored with `:(top)`; an EMPTY inventory is an
     infrastructure failure → message · exit 2, never a silently smaller scope.

3. D-25 (лот 6 „Проблемите“) — `named_ring()`, a SECOND judge beside `walk()`:
   a list of `RING_MIN` or more dicts whose keys are a subset of the lat/lon
   vocabulary is geometry too. Measured at 37db9ca (план §1 редове 10-12): the
   rule the backlog calls "a list of >= 4 numbers" was never delivered — it stands
   in `docs/plans/ПЛАН_Картата_imot_08.09.md:122,:130,:273` and nowhere in the
   code, so `walk()` judged by three key NAMES alone and a polygon serialised as
   `[{"lat": …, "lon": …}, …]` under a harmless key walked straight through.
   The rule judges the SHAPE of the list and not the NAME of the key on purpose:
   `data/places.json`, `data/hotels.json` and `data/removed_hydrants.json` carry
   `lat`/`lon` lawfully, so widening `GEO` would make the gate red over the live
   tree, and a row with a `name` key is not a vertex. The BARE numeric ring stays
   out — it fires on `data/address_rows.json` and `data/approx_addresses_v1.json`,
   i.e. red by construction; that is its own backlog row (D-25b).

`GEO`, `LEGACY`, `ALLOWED_NEW`, `walk` and the printed JSON keep the signed shape byte
for byte; in `changed` the PARSE is kept verbatim and only its pipe to git goes through
the checked `git()` helper (S30-2). `pathlib` is gone because nothing reads the working
tree any more.
"""
import json, os, subprocess, sys
GEO = {"coordinates", "geometry", "geometries"}
# D-25: the vocabulary of a NAMED point and how many of them make a ring.
RING_MIN = 4
LAT_NAMES = {"lat", "latitude", "y"}
LON_NAMES = {"lon", "lng", "longitude", "x"}
# ТОЧНИТЕ наследени изключения: (път, JSON-указател, тип на стойността).
LEGACY = {("scratch/places_search/granitsi_fixtures_07.09.json", "/_meta/geometry", str)}
ALLOWED_NEW = {"tests/granitsi_client_probe.mjs",
               "scratch/places_search/granitsi_fixtures_07.09.json",
               "scratch/places_search/ЗА_ПОДПИС_Б3_07.09.md",
               "gates/allow/2026-09-07_b3.json",
               "scratch/places_search/архив/АРХИВ_A_05.09.md",
               "gates/probe/b3_g11.py",
               "tests/test_b3_gates.py",
               # Т13 (под-лот И-Б1) — ДВАНАЙСЕТ нови пътя, поименно и затворено:
               # доставеният квартален индекс, десетте нови тела на К7 (Ф6–Ф15,
               # вкл. корпусът Ф11) и амандаментът на К4, който се ражда СЛЕД
               # <БАЗА> и без този ред пали гейта за грешна причина (ИБ1-О23).
               "data/address_quarters.json",
               "tests/test_quarter_index_bundle.py",
               "tests/test_first_load_budget.py",
               "tests/test_address_quarter_render.py",
               "tests/address_slice_probe.mjs",
               "gates/probe/ib1_g15.py",
               "scratch/places_search/ib_corpus_11.09.json",
               "tests/test_kill_switch.py",
               "tests/test_negative_halves.py",
               "tests/negative_halves_manifest.json",
               "tests/test_adr_amendment.py",
               "docs/decisions/011a_амандамент_И-Б1_11.09.md",
               # Лот 1 „Проблемите“ (един стандарт за всяка форма при хидрант) —
               # ТРИ нови пътя: гейтът на формите (К3), планът (К1) и амандаментът
               # на договора от 09.05 (К2). Всички се раждат СЛЕД базата 8512ab6.
               "tests/test_report_form_operational.py",
               "docs/plans/ПЛАН_Проблемите_лот1_Ф-а_13.09.md",
               "docs/audits/амандамент_подаване_13.09.md",
               # Лот 4б „Проблемите“ (класовата дума в адресния клон): гейтът и
               # пробата на периметъра при доставката (К3), планът (К1) и
               # амандаментът 006a на ADR 006 D12 (К2).
               "tests/test_address_search_class_words.py",
               "gates/probe/lot_perimeter.py",
               "docs/plans/ПЛАН_Проблемите_лот4б_хотел_13.09.md",
               "docs/decisions/006a_амандамент_4б_13.09.md",
               # Лот 4в-А „Проблемите“ (класоподобната дума в адресния клон): новият
               # гейт с трите отрицателни половини (К3), планът (К1) и амандаментът
               # 006b, който разширява същото изключение на D12 (К2).
               "tests/test_address_search_class_like.py",
               "docs/plans/ПЛАН_Проблемите_лот4в_квартал_13.09.md",
               "docs/decisions/006b_амандамент_4в_13.09.md",
               # Лот 1г „Проблемите“ (бележката при „Грешна локация“ става по желание):
               # ДВА нови пътя — гейтът с двете отрицателни половини (К3) и планът (К1).
               # Двата се раждат СЛЕД базата на лота 2d18377; лотът няма амандамент.
               "tests/test_report_form_note_optional.py",
               "docs/plans/ПЛАН_Проблемите_лот1г_бележката_14.09.md",
               # Лот 4в-Б „Проблемите“ (полигонният квартал в адресния клон): новият
               # гейт с трите отрицателни половини (К3), планът (К1) и амандаментът 006c,
               # който разширява същото изключение на D12 за трети път (К2).
               "tests/test_address_search_polygon_quarter.py",
               "docs/plans/ПЛАН_Проблемите_лот4в-Б_бл11_14.09.md",
               "docs/decisions/006c_амандамент_4в-Б_14.09.md",
               # Лот 5 „Проблемите“ (входовете под сградата): новият гейт с трите
               # отрицателни половини (К3b), планът (К1) и ADR 012, който урежда
               # лентата под адресния ред (К2). И трите се раждат СЛЕД базата 134039c.
               "tests/test_address_entrances_under_building.py",
               "docs/plans/ПЛАН_Проблемите_лот5_входовете_14.09.md",
               "docs/decisions/012_entrances_under_the_building.md",
               # Лот 6 „Проблемите“ (петте дребни реда на беклога): планът (К1),
               # гейтът на чистия импорт на машината за места (К2) и гейтът на
               # именувания пръстен (К6). И трите се раждат СЛЕД базата на лота
               # 37db9ca; лотът няма амандамент.
               "docs/plans/ПЛАН_Проблемите_лот6_дребните_15.09.md",
               "tests/test_recall_sweep_import_clean.py",
               "tests/test_b3_g11_named_ring.py",
               # Лот О „Проблемите“ (каналът за обратна връзка за приложението):
               # ТРИ нови пътя — планът (К1), амандаментът на договора от 09.05
               # и на амандамента от 13.09 (К1б) и гейтът с осемте отрицателни
               # половини (К2 четири, К5 три, К6 една). И трите се раждат СЛЕД
               # базата на лота 758f35e.
               "docs/plans/ПЛАН_Проблемите_лотО_обратна_връзка_15.09.md",
               "docs/audits/амандамент_подаване_15.09.md",
               "tests/test_app_feedback_channel.py",
               # чужд: модерация #38, 20c1efe
               "scratch/apply_c38.py",
               # запис на Архитекта: Кими К45 (О46), Кими К46 (О52)
               "scratch/places_search/tiles_kimi_K45_12.09.md",
               "scratch/places_search/tiles_kimi_K46_12.09.md"}
def git(*args):
    """S30-2: a failed git process is a FAILED gate, never a green one."""
    try:
        return subprocess.run(("git",) + args, capture_output=True, check=True).stdout
    except subprocess.CalledProcessError as exc:
        sys.stderr.write("git %s -> exit %d\n%s\n" % (" ".join(args), exc.returncode,
                         (exc.stderr or b"").decode("utf-8", "replace").strip()))
        sys.exit(2)
def blob(path, cached):
    """S30-1: the bytes of <path> in the snapshot under test — never the working tree."""
    ref = (":" if cached else "HEAD:") + path
    proc = subprocess.run(("git", "show", ref), capture_output=True)
    if proc.returncode != 0:
        return None, "git show %s -> exit %d: %s" % (ref, proc.returncode,
                     (proc.stderr or b"").decode("utf-8", "replace").strip())
    return proc.stdout, None
def walk(o, path, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in GEO: hits.append((path + "/" + k, type(v)))
            walk(v, path + "/" + k, hits)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, path + "[%d]" % i, hits)
def named_point(v):
    """D-25: a dict that is a vertex and NOTHING else — subset of the vocabulary."""
    if not isinstance(v, dict): return False
    keys = set(v)
    return keys <= LAT_NAMES | LON_NAMES and bool(keys & LAT_NAMES) and bool(keys & LON_NAMES)
def named_ring(o, path, hits):
    """D-25: a list of >= RING_MIN named points is geometry, whatever it is called."""
    if isinstance(o, dict):
        for k, v in o.items(): named_ring(v, path + "/" + k, hits)
    elif isinstance(o, list):
        if len(o) >= RING_MIN and all(named_point(v) for v in o): hits.append((path, type(o)))
        for i, v in enumerate(o): named_ring(v, path + "[%d]" % i, hits)
def judged_hits(doc):
    """The ONE path main() judges a document by, so a test can pin it.

    Both judges run over the same document and the duplicates are dropped IN
    ORDER, which is a property of the GATE and not of the caller: a test that
    de-duplicated the hits itself would pin the standard library instead.
    """
    hits = []; walk(doc, "", hits); named_ring(doc, "", hits)
    return list(dict.fromkeys(hits))          # a ring under a GEO key: both judges see it
def changed(parent, cached=False):
    cmd = ["diff", "--name-status", "-z", "--find-renames",
           "--diff-filter=AMR", parent, "HEAD"]
    if cached:                                # the staged write-set, before the commit
        cmd = ["diff", "--cached", "--name-status", "-z", "--find-renames",
               "--diff-filter=AMR", parent]
    parts = [p for p in git(*cmd).decode("utf-8").split(chr(0)) if p != ""]
    files, new, i = [], [], 0
    while i < len(parts):                     # R носи ДВА пътя, A и M — по един
        if parts[i][0] == "R": files.append(parts[i + 2]); i += 3
        else:
            if parts[i][0] == "A": new.append(parts[i + 1])
            files.append(parts[i + 1]); i += 2
    return files, new
def inventory(cached):
    """S30-1: the tracked data/*.json list of the SAME snapshot as the contents.

    S30-3: `:(top)` anchors the pathspec at the repo root, so the scope cannot shrink
    with the current directory; `main()` also chdirs there, which keeps the returned
    paths root-relative — `git show :<path>` then resolves against the same root.
    """
    out = (git("ls-files", "-z", "--cached", "--", ":(top)data/") if cached
           else git("ls-tree", "-r", "-z", "--name-only", "HEAD", "--", ":(top)data/"))
    return [f for f in out.decode("utf-8").split(chr(0)) if f.endswith(".json")]
def main(parent, cached=False):
    # S30-3: run from the top of the working tree, so every pathspec and every path in
    # the output means the same thing whichever directory the gate was invoked from.
    os.chdir(git("rev-parse", "--show-toplevel").decode("utf-8").strip())
    tracked = inventory(cached)
    if not tracked:                           # a gate with nothing to inspect is broken
        sys.stderr.write("empty inventory: no tracked data/*.json in the snapshot "
                         "under test (cached=%s) - infrastructure failure, not a "
                         "clean gate%s" % (cached, chr(10)))
        sys.exit(2)
    touched, new = changed(parent, cached)
    scope = sorted(set(tracked) | set(f for f in touched
                   if f.lower().endswith((".json", ".geojson"))))
    bad, unread = [], []
    for f in scope:
        raw, err = blob(f, cached)
        if raw is None: unread.append((f, err)); continue
        try: doc = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as exc: unread.append((f, str(exc))); continue
        hits = judged_hits(doc)
        bad += [(f, ptr, typ.__name__) for ptr, typ in hits
                if (f, ptr, typ) not in LEGACY]
    stray = sorted(set(new) - ALLOWED_NEW)
    print(json.dumps({"scope": len(scope), "geo_hits": bad, "unreadable": unread,
                      "stray_new": stray}, ensure_ascii=False))
    sys.exit(0 if not bad and not unread and not stray else 1)
if __name__ == "__main__":
    main(sys.argv[1], "--cached" in sys.argv[2:])
