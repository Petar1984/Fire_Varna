# -*- coding: utf-8 -*-
"""The П7 gate in the suite — §11 Р7 of docs/plans/places_phase2_plan.md.

Until C16 nothing here could go red without a human reading a report:
`recall_sweep.py` always exited 0 and the probe only failed on a console error
(C14 finding 3 / §11 Р7). This module makes the reference itself the gate:

  1. importing `scratch/places_search/recall_sweep.py` must write NOT ONE BYTE
     (the `if __name__` guard) — measured in a subprocess, sha before/after;
  2. the П7 gains and controls of §11 Р3/С2′–С4′ — {name, zone, kind} AND the
     branch, not a row count. К2 (§12, д) had made „детска градина приморски“
     the differential control of the foreign-token guard; ЛОТ 1 brought a
     legitimate row (ДГ№19 „Славейче“, район Приморски) that turned it into a
     plain one-row A3 answer, so the control no longer differentiates —
     Амандамент №2 (ж). Its job passed to В1/В2 („детска ясла аспарухово“,
     „университет приморски“) in the ЛОТ 1 controls; the guard itself is still
     gated directly, in `test_the_foreign_token_guard_is_load_bearing`;
  3. `p7_added` is exactly the seven tokens in six zones measured (§11 v2.1 plus
     the seventh, `konstanin`, that the renamed resort zone unlocked — Амандамент №10);
  4. ONE data anchor (Амандамент №11): every row of the committed artefact is
     equal by (q, branch, name, zone) to `git show 23af63f:…rows.json` EXCEPT
     the 55 rows Petar signed (Амандамент №8 П1 — `LOT1_DATA_CHANGED`, the list
     in `scratch/places_search/lot1_reference_preview_v2.md` §А+§Б) and the 9
     rows F1-д added (`LOT1_DATA_ADDED`). A row on the signed list that did NOT
     move is red as well, so the list cannot go stale in silence;
  5. ЛОТ 1 (решения 2 и 1, signed 03.09): the gate itself, and the proof that
     each rule is load-bearing — inverted in place, the old answer comes back;
  6. RETIRED anchors: `FROZEN_COMMIT = 7a6ea1d` (buckets gate_m5_a8 + extra,
     exception `LOT1_PREPENDED`) and `P7_ANCHOR_COMMIT = 378a844` (bucket
     gate_p7, exceptions `LOT1_MOVED_P7` — „хотел приморски“, „училище свети
     никола“, „хотел зеленика“) are gone. 23af63f INHERITS them: that commit is
     the artefact frozen against both of them and green on both, so the chain
     7a6ea1d → 378a844 → 23af63f is unbroken, and one anchor now covers all
     four buckets and all 122 rows instead of two anchors over 103;
  7. Амандамент №8 П2 („детско заведение“): the form table `EXTRA_FORMS` is
     kept by hand on BOTH sides — the places IIFE of index.html and the
     reference — and the ЛОТ 1 audit proved that deleting „детска ясла“ from
     the client copy left this suite green while only the browser probe went
     red. `Lot1FormTableTest` reads the client literal out of index.html and
     compares the two tables, then measures the answer itself.

Read-only: it runs `git show` through subprocess and touches nothing on disk.
"""
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
INDEX = REPO / "index.html"
REFERENCE = REPO / "scratch" / "places_search" / "recall_sweep.py"
ROWS = REPO / "scratch" / "places_search" / "recall_sweep_rows.json"
FROZEN_PATH = "scratch/places_search/recall_sweep_rows.json"
BUCKETS = ("gate_m5_a8", "extra", "gate_p7", "gate_lot1")
# ADR 008 D7 — fail-closed. `REF_BUCKETS` in scratch/places_search/probe_places_fv.mjs
# is the probe's hand-kept copy of the very same list; RefBucketsTest below compares
# the two and the artefact against both, so a bucket added on one side alone is red
# without a browser.
PROBE = REPO / "scratch" / "places_search" / "probe_places_fv.mjs"
# The ONE anchor (Амандамент №11): the artefact as it stood before the ЛОТ 1
# DATA landed — 113 rows over the four buckets, itself frozen against 7a6ea1d
# and 378a844 (docstring 6).
LOT1_DATA_ANCHOR = "23af63f"       # C30 — the last artefact before the ЛОТ 1 data
# The signed change list: Petar's П1 „да“ of Амандамент №8 over
# scratch/places_search/lot1_reference_preview_v2.md — §А (18 rows where only the
# spelling of a label moved: the renamed zone „к.к. Св. Константин“ →
# „к.к. Св. Св. Константин и Елена“ and the 9 canonised registry names) and §Б
# (37 rows where the branch, the count or the records themselves moved). 55 in
# all; the queries repeat across buckets, so the unique queries are 50.
LOT1_DATA_CHANGED = {
    # §А 11 + §Б 23
    "gate_m5_a8": (
        u"хотел адмирал", u"адмирал", u"хотел адмиралл", u"хотел амирал",
        u"адмирал златни", u"хотел адмирал златни пясъци", u"роял", u"royal",
        u"русалка", u"хелиос спа", u"спа хелиос",
        u"хотели", u"хотел", u"хотелите", u"семеен хотел", u"хотел златни",
        u"берлин голдън бийч", u"лти берлин", u"бонита", u"bonita", u"парк",
        u"градина", u"училище", u"училища", u"болница", u"детска градина",
        u"дкц", u"хоспис", u"болница света марина", u"св марина",
        u"градина 12", u"дг 12", u"детска градина 12", u"ввму",
    ),
    # §А 3 + §Б 3
    "extra": (
        u"хотел йо", u"хотел адмирал", u"йо",
        u"хотел градина", u"хотел семеен", u"ritsa",
    ),
    # §А 4 + §Б 6
    "gate_p7": (
        u"хотел приморският", u"приморският хотел", u"приморският хотел варна",
        u"хотел приморски",
        u"владиславово детска градина", u"детска градина владислав варненчик",
        u"хотел марина парк", u"хотел чайка", u"болница изгрев",
        u"детска градина приморски",
    ),
    # §А 0 + §Б 5
    "gate_lot1": (
        u"ГРАДИНА", u"градина", u"хотел градина", u"хотел златни",
        u"детска градина",
    ),
}
# The rows F1-д ADDED — they cannot be compared with the anchor because they do
# not exist there: the seventh П7 token (Амандамент №10 (3)) and the eight ЛОТ 1
# gate rows of Амандамент №8 П2/§В/§Г (the three new words, Владиславово, В1/В2).
LOT1_DATA_ADDED = {
    "gate_p7": (u"хотел констанин",),
    "gate_lot1": (
        u"детско заведение", u"детски заведения", u"ясла", u"детска ясла",
        u"общежитие", u"детска градина владиславово",
        u"детска ясла аспарухово", u"университет приморски",
    ),
}


def load_reference():
    """Import the reference as a module. The guard is what makes this safe."""
    spec = importlib.util.spec_from_file_location("recall_sweep_gate", REFERENCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frozen_rows(commit=LOT1_DATA_ANCHOR):
    """The baseline as git holds it — never as the working tree holds it."""
    out = subprocess.run(["git", "-C", str(REPO), "show",
                          commit + ":" + FROZEN_PATH],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise AssertionError("git show %s:%s failed: %s"
                             % (commit, FROZEN_PATH,
                                out.stderr.decode("utf-8", "replace")))
    return json.loads(out.stdout.decode("utf-8"))


REF = load_reference()


class ImportGuardTest(unittest.TestCase):
    """§11 Р9 / C14 finding 3: the module is a module, not a script."""

    def test_import_writes_nothing(self):
        before = hashlib.sha256(ROWS.read_bytes()).hexdigest()
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        # argv[1] is a lie the runner tells: on import the module must ignore it
        # and keep the signed default instead of raising SystemExit.
        proc = subprocess.run([sys.executable, "-c",
                               "import importlib.util,sys;"
                               "spec=importlib.util.spec_from_file_location('rs', sys.argv[1]);"
                               "m=importlib.util.module_from_spec(spec);"
                               "spec.loader.exec_module(m);"
                               "print(m.CAPMODE, len(m.RECS))",
                               str(REFERENCE), "discover"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
        self.assertEqual(proc.returncode, 0,
                         proc.stderr.decode("utf-8", "replace"))
        self.assertEqual(proc.stdout.decode("utf-8").split(), ["plan", "375"])
        after = hashlib.sha256(ROWS.read_bytes()).hexdigest()
        self.assertEqual(before, after, "importing recall_sweep.py rewrote the reference rows")

    def test_capmode_is_an_explicit_list(self):
        self.assertEqual(REF.CAPMODES, ("plan", "poi"))
        with self.assertRaises(SystemExit):
            REF.set_capmode(["recall_sweep.py", "cap_poi"])
        REF.set_capmode(["recall_sweep.py"])          # back to the signed default
        self.assertEqual(REF.CAPMODE, "plan")


class P7RuleTest(unittest.TestCase):
    """§11 v2.1: seven tokens, six zones — and nothing in the name path.

    Six were signed as the rule; the seventh (`konstanin`, к.к. Св. Св. Константин
    и Елена) came with ЛОТ 1's data, not with a rule change, and is signed in
    Амандамент №10 (3). Р5 says exactly this is allowed — with a measure."""

    def test_added_tokens_are_the_measured_seven(self):
        self.assertEqual(REF.P7_ADDED, REF.P7_EXPECTED)
        self.assertEqual(sum(len(v) for v in REF.P7_ADDED.values()), 7)
        self.assertEqual(len(REF.P7_ADDED), 6)

    def test_no_added_token_is_a_name_token(self):
        """Р4: the claim holds for `nset`; `varnenchik` IS an old-name token of
        one hotel (КАРНИВАЛ) and that is accepted explicitly, with the measure."""
        added = set(t for tokens in REF.P7_ADDED.values() for t in tokens)
        names = set()
        for rec in REF.RECS:
            names |= rec.nset
        self.assertEqual(added & names, set())
        aliases = set()
        for rec in REF.RECS:
            aliases |= rec.aset
        self.assertEqual(added & aliases, {"varnenchik"})

    def test_added_tokens_are_zone_tokens_only(self):
        """The whole safety of П7: never ntk/nset/aset, only ztk/zkset."""
        for rec in REF.RECS:
            for token in rec.p7:
                self.assertIn(token, rec.zkset, rec.name)
                self.assertNotIn(token, rec.nset, rec.name)
                self.assertNotIn(token, rec.aset, rec.name)

    def test_the_foreign_token_guard_is_load_bearing(self):
        """К2 (§12, д): the guard of step (д)/(д′), measured instead of asserted.

        The replaced control („детска градина приморски“) differentiates because
        of this: the foreign-token step is the ONLY thing that keeps `primorski`
        and `primorskiat` (own tokens of район Приморски) out of the zone tokens
        of Морска градина, and `asparuhovo` (кв. Аспарухово) out of ж.к. Дружба.
        The guard is fed by the OTHER zones of the delivery, so it can be starved
        without editing one byte of it — a call with a single zone has nothing
        foreign to compare against. Measured 03.09; the same four tokens that a
        copy of the reference with the step cut out adds back."""
        cats = json.loads((REPO / "data" / "place_categories.json").read_text(encoding="utf-8"))
        _, added, dropped = REF.zone_alias_tokens(cats, REF.ZONES_IN)
        # the tag is `foreign:<the foreign token>:<the candidate>` — „primorskiat“
        # falls against „primorski“ through the lev<=2 step (д′) of §11 Р1.
        for zone, token, tag in (
                (u"Морска градина", "primorski", "foreign:primorski:primorski"),
                (u"Морска градина", "primorskiat", "foreign:primorski:primorskiat"),
                (u"м-т Салтанат", "primorski", "foreign:primorski:primorski"),
                (u"ж.к. Дружба", "asparuhovo", "foreign:asparuhovo:asparuhovo")):
            self.assertNotIn(token, added.get(zone, []), zone)
            self.assertIn(tag, dropped.get(zone, []), zone)
        _, alone, _ = REF.zone_alias_tokens(cats, [u"Морска градина"])
        self.assertEqual(alone.get(u"Морска градина"), ["primorski", "primorskiat"])
        _, alone, _ = REF.zone_alias_tokens(cats, [u"ж.к. Дружба"])
        self.assertEqual(alone.get(u"ж.к. Дружба"), ["asparuhovo"])

    def test_fail_soft_without_a_dictionary(self):
        """С7′: no `zones`, a `zones` that is not an object, aliases that are not
        a list of strings — П7 switches off, nothing raises."""
        zones = REF.ZONES_IN
        for doc in (None, {}, {"zones": None}, {"zones": []}, {"zones": "x"},
                    {"zones": {"кв. Изгрев": None}},
                    {"zones": {"кв. Изгрев": {"aliases": "ж.к. Изгрев"}}},
                    {"zones": {"кв. Изгрев": {"aliases": [1, None]}}}):
            extra, added, dropped = REF.zone_alias_tokens(doc, zones)
            self.assertEqual(added, {}, repr(doc))
            self.assertEqual(extra, {}, repr(doc))


class P7GateTest(unittest.TestCase):
    """§11 Р3/С2′–С4′ — the gains and the controls, branch included."""

    def test_gate(self):
        failures = REF.check_p7_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_gate_actually_covers_every_added_token(self):
        """С2′: one query per added token, or the parity proves nothing."""
        queries = " ".join(q for q, _, _, _, _ in REF.P7_GAINS)
        for tokens in REF.P7_ADDED.values():
            for token in tokens:
                self.assertTrue(
                    any(t.s == token for t in REF.place_tokens(queries)),
                    "no gate query exercises the added token " + token)


class FrozenDiffTest(unittest.TestCase):
    """С5′ + Амандамент №11: ONE anchor for all four buckets.

    Two things have to hold at once, or the re-freeze proves nothing:
    the ARTEFACT the probe replays must differ from 23af63f in exactly the 55
    signed rows (plus the 9 rows that did not exist there), and the LIVE engine
    must answer exactly what the artefact holds. Either half alone can be fooled
    — a row moving in the engine and in the artefact together would stay green
    against the artefact, and an artefact edited by hand would stay green
    against the anchor only if the engine agreed with it."""

    @classmethod
    def setUpClass(cls):
        cls.anchor = frozen_rows()
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def signed(self, bucket, q):
        return q in LOT1_DATA_CHANGED.get(bucket, ())

    def added(self, bucket, q):
        return q in LOT1_DATA_ADDED.get(bucket, ())

    def test_the_signed_lists_are_the_measured_counts(self):
        """55 signed + 9 added over 113 anchored rows = the 122 of the delivery."""
        self.assertEqual(sum(len(v) for v in LOT1_DATA_CHANGED.values()), 55)
        self.assertEqual(sum(len(v) for v in LOT1_DATA_ADDED.values()), 9)
        self.assertEqual(sum(len(self.anchor[b]) for b in BUCKETS), 113)
        self.assertEqual(sum(len(self.current[b]) for b in BUCKETS), 122)
        for bucket in BUCKETS:
            anchored = set(e["q"] for e in self.anchor[bucket])
            live = set(e["q"] for e in self.current[bucket])
            self.assertEqual(anchored - live, set(),
                             "a row vanished from " + bucket)
            self.assertEqual(live - anchored, set(LOT1_DATA_ADDED.get(bucket, ())),
                             "unsigned new rows in " + bucket)

    def test_every_row_outside_the_signed_list_equals_the_anchor(self):
        """The half that catches a silent drift: any row that is neither signed
        nor new must be equal to 23af63f by (q, branch, name, zone)."""
        compared = 0
        for bucket in BUCKETS:
            anchor = dict((e["q"], e) for e in self.anchor[bucket])
            for entry in self.current[bucket]:
                if self.added(bucket, entry["q"]) or self.signed(bucket, entry["q"]):
                    continue
                was = anchor[entry["q"]]
                self.assertEqual(
                    (entry["branch"], [(r["name"], r["zone"]) for r in entry["rows"]]),
                    (was["branch"], [(r["name"], r["zone"]) for r in was["rows"]]),
                    "%s/%s moved against %s and is not on the signed list"
                    % (bucket, entry["q"], LOT1_DATA_ANCHOR))
                compared += 1
        self.assertEqual(compared, 113 - 55)

    def test_every_signed_row_really_moved(self):
        """The half that catches a stale list: a query that is on the signed list
        but answers exactly as it did at the anchor is red — the signature is
        then describing a change that no longer exists."""
        moved = 0
        for bucket in BUCKETS:
            anchor = dict((e["q"], e) for e in self.anchor[bucket])
            for q in LOT1_DATA_CHANGED[bucket]:
                entry = [e for e in self.current[bucket] if e["q"] == q]
                self.assertEqual(len(entry), 1, "%s/%s" % (bucket, q))
                entry = entry[0]
                was = anchor[q]
                self.assertNotEqual(
                    (entry["branch"], [(r["name"], r["zone"]) for r in entry["rows"]]),
                    (was["branch"], [(r["name"], r["zone"]) for r in was["rows"]]),
                    "%s/%s is on the signed list but did not move against %s"
                    % (bucket, q, LOT1_DATA_ANCHOR))
                moved += 1
        self.assertEqual(moved, 55)

    def test_the_live_engine_replays_the_artefact(self):
        """And the engine says what the artefact says — all 122 queries, ordered
        rows and branch, not a count."""
        compared, rows = 0, 0
        for bucket in BUCKETS:
            for entry in self.current[bucket]:
                got, branch = REF.search(entry["q"])
                self.assertEqual(branch, entry["branch"], entry["q"])
                self.assertEqual([(r.name, r.zone) for r in got],
                                 [(r["name"], r["zone"]) for r in entry["rows"]],
                                 entry["q"])
                self.assertTrue(entry["ok"], entry["q"])
                compared += 1
                rows += len(got)
        self.assertEqual(compared, 122)
        self.assertEqual(rows, 1998)

    def test_rows_carry_the_p7_measure(self):
        current = self.current
        self.assertEqual(current["_meta"]["p7_added"], REF.P7_EXPECTED)
        # Амандамент №10 (3): six tokens were signed as the rule, the seventh came
        # with the renamed resort zone — 7 tokens in 6 zones, measured.
        self.assertEqual(current["_meta"]["p7_tokens"], 7)
        self.assertEqual(current["_meta"]["p7_zones_with_aliases"], 6)
        self.assertEqual(len(current["gate_p7"]),
                         len(REF.P7_GAINS) + len(REF.P7_CONTROLS))
        for entry in current["gate_p7"]:
            self.assertTrue(entry["ok"], entry["q"])


class Lot1GateTest(unittest.TestCase):
    """ЛОТ 1 — the two client rules of решения 2 и 1, signed 03.09."""

    def test_gate(self):
        failures = REF.check_lot1_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_committed_artefact_carries_the_lot1_bucket(self):
        """F2-д: the re-frozen artefact carries the ЛОТ 1 bucket the probe replays
        — one row per signed query (18 = the 10 of F2-к plus the 6 gains and 2
        controls of Амандамент №8 П2/§В/§Г), every one of them green."""
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        bucket = current["gate_lot1"]
        self.assertEqual(len(bucket), len(REF.LOT1_GAINS) + len(REF.LOT1_CONTROLS))
        self.assertEqual(len(bucket), 18)
        for entry in bucket:
            self.assertTrue(entry["ok"], entry["q"])

    def test_the_exact_name_prepend_is_load_bearing(self):
        """Решение 2, inverted in place: with an empty exact-name index „градина“
        falls back to the 51 kindergartens. Restored, the hotel is first again."""
        saved = REF.EXACT_NAME
        try:
            REF.EXACT_NAME = {}
            rows, branch = REF.search(u"градина")
            self.assertEqual((branch, len(rows)), ("M1-category", 51))
        finally:
            REF.EXACT_NAME = saved
        rows, branch = REF.search(u"градина")
        self.assertEqual((branch, len(rows), rows[0].name), ("M1-category", 52, u"ГРАДИНА"))

    def test_the_zone_phrase_override_is_load_bearing(self):
        """Решение 1, inverted in place: with no phrase on any record the three
        moved rows fall back to the answers the frozen artefact holds."""
        queries = (u"хотел приморски", u"училище свети никола", u"хотел зеленика")
        saved = [(rec, rec.zph) for rec in REF.RECS]
        try:
            for rec in REF.RECS:
                rec.zph = set()
            self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                             [("M2", 1), ("M2", 8), ("M2", 1)])
        finally:
            for rec, zph in saved:
                rec.zph = zph
        self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                         [("A3-record+zone-phrase", 5), ("A3-record+zone-phrase", 1),
                          ("A3-record+zone-phrase", 2)])

    def test_a_phrase_is_the_canonical_zone_or_an_accepted_p7_form(self):
        """The admissibility rule, measured: „Приморски парк“ is an alias of
        Морска градина that П7 threw out as foreign, so it is NOT a phrase there
        — which is the whole difference between „хотел приморски“ = 5 and = 23.
        „кв. Владиславово“ was accepted by П7, so it IS one."""
        self.assertEqual(REF.ZONE_PHRASES[u"Морска градина"], {"morska gradina"})
        self.assertEqual(REF.ZONE_PHRASES[u"район Приморски"], {"primorski"})
        self.assertEqual(REF.ZONE_PHRASES[u"район Одесос"], {"odesos"})
        self.assertIn("vladislavovo", REF.ZONE_PHRASES[u"ж.к. Владислав Варненчик"])
        self.assertIn("zpz", REF.ZONE_PHRASES[u"Западна промишлена зона"])
        for zone, phrases in REF.ZONE_PHRASES.items():
            for phrase in phrases:
                for token in phrase.split(" "):
                    self.assertNotIn(token, ("raion", "kvartal", "kompleks", "zona",
                                             "mestnost", "park", "chast"), zone)

    def test_the_exact_index_carries_current_names_only(self):
        """Решение 2 and the data judge: old_names stay OUT of the exact index."""
        aliases = set()
        for rec in REF.RECS:
            aliases |= rec.aset
        for key, recs in REF.EXACT_NAME.items():
            for rec in recs:
                self.assertEqual(key, u" ".join(rec.ntk), rec.name)
        for token in aliases:
            if token in REF.EXACT_NAME:
                self.assertTrue(any(rec.ntk == [token] for rec in REF.EXACT_NAME[token]),
                                token)


# --- Амандамент №8 П2: the client's own copy of the form table -----------------
# The places IIFE of index.html and the reference each hold a hand-kept
# `EXTRA_FORMS`; both comments already call a drift between them a failed gate,
# but until now only the browser probe could see one.
PLACES_IIFE_START = "(function initPlacesSearch() {"
PLACES_IIFE_END = "\n  })();"


def js_extra_forms(text):
    """The EXTRA_FORMS literal of index.html, read out of the places IIFE.

    Built like the other index.html pins in the suite (ShaPinTest in
    tests/test_places_search_primitives.py): find the marker, take the literal,
    and account for every byte of it — an entry this parser cannot read is a
    loud failure, never a silently dropped key.
    """
    start = text.find(PLACES_IIFE_START)
    if start == -1:
        raise AssertionError(PLACES_IIFE_START + " is gone from index.html")
    end = text.find(PLACES_IIFE_END, start)
    if end == -1:
        raise AssertionError("the places IIFE does not close")
    match = re.search(r"const EXTRA_FORMS = \{(.*?)\n\s*\};", text[start:end], re.S)
    if match is None:
        raise AssertionError("EXTRA_FORMS is not a literal inside initPlacesSearch")
    rest, table = match.group(1), {}
    for entry in re.finditer(r"'([^']+)'\s*:\s*\[([^\]]*)\]\s*,?", match.group(1)):
        table[entry.group(1)] = re.findall(r"'([^']*)'", entry.group(2))
        rest = rest.replace(entry.group(0), "", 1)
    if rest.strip():
        raise AssertionError("unread bytes in the EXTRA_FORMS literal: %r" % rest.strip())
    return table


class Lot1vAGateTest(unittest.TestCase):
    """ЛОТ 1в-А — псевдоними с извор + курираните думи на видовете (04.09).

    Twelve measured rows: nine gains (the Wikidata string of the ВВМУ, the two
    ЕГ, the class words of ЗПУО/ЗЛЗ/ЗВО, the МДУ) and three controls (the known
    hole „морско училище“, the generic „варна“, the two-token floor „синчец“).
    """

    def test_gate(self):
        failures = REF.check_lot1v_a_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_measured_rows_are_twelve(self):
        self.assertEqual(len(REF.LOT1V_A_GAINS), 9)
        self.assertEqual(len(REF.LOT1V_A_CONTROLS), 3)

    def test_the_generic_word_filter_is_load_bearing(self):
        """G2 — a gate that cannot go red is not a gate. `варна` is put back into
        every alias token set in place; the control then finds rows that stand in
        the answer through an alias alone, and check_lot1v_a_gate() says so."""
        token = REF.skel(u"варна")
        saved = [(rec, rec.aset) for rec in REF.RECS]
        try:
            for rec in REF.RECS:
                if rec.old_names and any(token in REF.key_of(o).split(u" ")
                                         for o in rec.old_names):
                    rec.aset = set(rec.aset) | {token}
            self.assertNotEqual(REF.check_lot1v_a_gate(), [])
        finally:
            for rec, aset in saved:
                rec.aset = aset
        self.assertEqual(REF.check_lot1v_a_gate(), [])

    def test_the_two_token_floor_is_load_bearing(self):
        """Амандамент А4 т. 2, inverted in place: without the floor the one-word
        „синчец“ reaches EXACT_ALIAS and the hotel whose OLD name is „СИНЧЕЦ“
        takes the answer away from ДГ 30 „Синчец“, whose CURRENT name it is."""
        saved = REF.alias_significant
        try:
            REF.alias_significant = lambda qt: 2
            rows, branch = REF.search(u"синчец")
            self.assertEqual((branch, rows[0].name), ("A0-exact-alias", u"ДАНА ПАЛАС"))
        finally:
            REF.alias_significant = saved
        rows, branch = REF.search(u"синчец")
        self.assertEqual((branch, rows[0].name), ("M3", u'ДГ 30 "Синчец"'))

    def test_the_exact_alias_index_is_the_whole_alias_and_nothing_else(self):
        """D2: one key per delivered old name, keyed by the WHOLE normalised
        string. Measured 04.09: 82 aliases, 82 keys, and the only key that is also
        a current name belongs to the SAME record."""
        delivered = sum(len(rec.old_names) for rec in REF.RECS)
        self.assertEqual(delivered, 82)
        self.assertEqual(len(REF.EXACT_ALIAS), 82)
        for key, hits in REF.EXACT_ALIAS.items():
            for rec, i in hits:
                self.assertEqual(key, REF.key_of(rec.old_names[i]), rec.name)
        both = set(REF.EXACT_ALIAS) & set(REF.EXACT_NAME)
        for key in both:
            self.assertEqual(set(r.name for r, _i in REF.EXACT_ALIAS[key]),
                             set(r.name for r in REF.EXACT_NAME[key]), key)

    def test_every_delivered_alias_carries_a_source(self):
        """D1 in the engine, not only in the payload: same length, closed list."""
        allowed = {"OSM", "REG", "NTR", "WD", "WEB", "KAIS", "CUR"}
        for rec in REF.RECS:
            self.assertEqual(len(rec.old_src), len(rec.old_names), rec.name)
            for code in rec.old_src:
                self.assertIn(code, allowed, rec.name)


class RefBucketsTest(unittest.TestCase):
    """ADR 008 D7: the bucket list is fail-closed on all three sides."""

    def test_the_artefact_carries_exactly_the_named_buckets(self):
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        self.assertEqual(set(current.keys()) - {"_meta"}, set(BUCKETS))

    def test_the_probe_names_the_same_buckets_in_the_same_order(self):
        probe = PROBE.read_text(encoding="utf-8")
        match = re.search(r"const REF_BUCKETS = \[([^\]]*)\];", probe)
        self.assertIsNotNone(match, "REF_BUCKETS is not a literal in the probe")
        self.assertEqual(tuple(re.findall(r'"([^"]+)"', match.group(1))), BUCKETS)
        self.assertNotIn("REF_BUCKETS = [\"gate_m5_a8\", \"extra\", \"gate_p7\", "
                         "\"gate_lot1\"]\n  .filter(", probe)


class PlacesCacheNameTest(unittest.TestCase):
    """ADR 008 D8: the cache namespace is a hand-kept copy on two sides.

    `index.html` owns the name and changes it with every change of the blobs; the
    probe WRITES a stale body into that namespace (the В7 staleCache refusal) and
    reads it back (the warm scenario). A stale copy in the probe turns the refusal
    scenario into a plain 404 in silence — measured on F5-а, where the constant
    moved to v3-225. `sw.js` must NOT protect it (D8): the SW does not cache it.
    """

    def test_the_probe_uses_the_name_index_html_owns(self):
        index = re.search(r"const PLACES_CACHE = '([^']+)'", INDEX.read_text(encoding="utf-8"))
        probe = re.search(r'const PLACES_CACHE = "([^"]+)"', PROBE.read_text(encoding="utf-8"))
        self.assertIsNotNone(index, "PLACES_CACHE is gone from index.html")
        self.assertIsNotNone(probe, "PLACES_CACHE is gone from the probe")
        self.assertEqual(index.group(1), probe.group(1))

    def test_the_service_worker_does_not_protect_the_places_cache(self):
        name = re.search(r"const PLACES_CACHE = '([^']+)'",
                         INDEX.read_text(encoding="utf-8")).group(1)
        self.assertNotIn(name, (REPO / "sw.js").read_text(encoding="utf-8"))


class Lot1FormTableTest(unittest.TestCase):
    """Амандамент №8 П2 („детско заведение“) — gated WITHOUT a browser.

    The ЛОТ 1 audit deleted „детска ясла“ from the client table and the whole
    suite stayed green while the probe went red (М5 121/122): the signed form
    was carried by the browser gate alone. These two tests carry it here —
    (a) the two tables are the same table, (b) the word really answers with
    both kinds, and the two single-kind words are NOT widened with it.
    """

    def test_the_client_table_equals_the_reference_table(self):
        table = js_extra_forms(INDEX.read_text(encoding="utf-8"))
        self.assertEqual(table, REF.EXTRA_FORMS)
        self.assertEqual(table, {
            u"детско заведение": [u"детска градина", u"детска ясла"],
            u"детски заведения": [u"детска градина", u"детска ясла"],
        })

    def test_the_form_answers_with_both_kinds_and_widens_nothing_else(self):
        """Measured on the ЛОТ 1 delivery: 61 = 51 kindergartens + 10 nurseries,
        M1-category, for both spellings — and П6/§Г, „детска градина“ still
        answers with 51 kindergartens and no nursery at all."""
        for query in (u"детско заведение", u"детски заведения"):
            rows, branch = REF.search(query)
            counts = {}
            for row in rows:
                counts[row.kind] = counts.get(row.kind, 0) + 1
            self.assertEqual((branch, len(rows)), ("M1-category", 61), query)
            self.assertEqual(counts, {u"детска градина": 51, u"детска ясла": 10}, query)
        rows, branch = REF.search(u"детска градина")
        self.assertEqual((branch, len(rows)), ("M1-category", 51))
        self.assertEqual(set(row.kind for row in rows), set([u"детска градина"]))
        rows, branch = REF.search(u"детска ясла")
        self.assertEqual((branch, len(rows)), ("M1-category", 10))
        self.assertEqual(set(row.kind for row in rows), set([u"детска ясла"]))


if __name__ == "__main__":
    unittest.main()
