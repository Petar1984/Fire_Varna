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
     equal by (q, branch, name, zone) to `git show 6032023:…rows.json` EXCEPT
     the 55 rows Petar signed (Амандамент №8 П1 — `LOT1_DATA_CHANGED`, the list
     in `scratch/places_search/lot1_reference_preview_v2.md` §А+§Б) and the 9
     rows F1-д added (`LOT1_DATA_ADDED`). A row on the signed list that did NOT
     move is red as well, so the list cannot go stale in silence;
  5. ЛОТ 1 (решения 2 и 1, signed 03.09): the gate itself, and the proof that
     each rule is load-bearing — inverted in place, the old answer comes back;
  6. RETIRED anchors: `FROZEN_COMMIT = 9c89463` (buckets gate_m5_a8 + extra,
     exception `LOT1_PREPENDED`) and `P7_ANCHOR_COMMIT = a42be4c` (bucket
     gate_p7, exceptions `LOT1_MOVED_P7` — „хотел приморски“, „училище свети
     никола“, „хотел зеленика“) are gone. 6032023 INHERITS them: that commit is
     the artefact frozen against both of them and green on both, so the chain
     9c89463 → a42be4c → 6032023 is unbroken, and one anchor now covers all
     four buckets and all 122 rows instead of two anchors over 103;
  7. Амандамент №8 П2 („детско заведение“): the form table `EXTRA_FORMS` is
     kept by hand on BOTH sides — the places IIFE of index.html and the
     reference — and the ЛОТ 1 audit proved that deleting „детска ясла“ from
     the client copy left this suite green while only the browser probe went
     red. `Lot1FormTableTest` reads the client literal out of index.html and
     compares the two tables, then measures the answer itself;
  8. REACHABLE anchors (амандамент А5 (2), F9): every commit this file names
     is an ANCESTOR of HEAD. The rebase of 04.09 rewrote the three it used to
     name and rewritten commits survive in the reflog of ONE checkout only, so
     the suite was green here and red in a fresh clone — it was measuring the
     machine. Each hash was replaced by its rewritten twin, and the twins carry
     the same artefact byte for byte (23af63f → 6032023 even share one tree),
     so not one expectation, exception or bucket sum moved with the re-anchoring.
     `AnchorsReachableTest` is the gate, and it names the pre-rebase hashes as
     the differential: those three must NOT resolve as ancestors.

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
# The four buckets the 6032023 anchor holds — the ЛОТ 1 reference, 122 rows.
BUCKETS = ("gate_m5_a8", "extra", "gate_p7", "gate_lot1")
# ADR 008 D7 — fail-closed, and the WHOLE list: F6-а added `gate_lot1v_a`
# ADDITIVELY (план §2г S3/S6) and F8 added `gate_lot1v_b` the same way, so the
# four above keep their anchor and each new lot answers in a bucket of its own. `REF_BUCKETS` is hand-kept on three sides —
# here, in scratch/places_search/probe_places_fv.mjs (the probe that replays the
# rows) and in scratch/places_search/recall_sweep.py (the reference, which refuses
# to WRITE an artefact with other keys). RefBucketsTest compares all three against
# the artefact, so a bucket added on one side alone is red without a browser.
REF_BUCKETS = BUCKETS + ("gate_lot1v_a", "gate_lot1v_b")
PROBE = REPO / "scratch" / "places_search" / "probe_places_fv.mjs"
# The ONE anchor (Амандамент №11): the artefact as it stood before the ЛОТ 1
# DATA landed — 113 rows over the four buckets, itself frozen against 9c89463
# and a42be4c (docstring 6).
LOT1_DATA_ANCHOR = "6032023"       # C30 — the last artefact before the ЛОТ 1 data
# F6-а (план §2г S6): the SECOND anchor, and the one with no exception list
# at all. a58010e is ЛОТ 1 as it was pushed; the aliases and the curated class
# words of F5-а were measured against it and moved NOTHING, so every one of the
# 122 rows must still equal it. A movement here is a STOP, never a re-freeze.
LOT1V_A_ANCHOR = "a58010e"         # C37 — main == origin/main, the ЛОТ 1 anchor
# F9 (план §2г S6): the THIRD anchor — the artefact as ЛОТ 1в-А froze it, five
# buckets and 134 rows. ЛОТ 1в-Б (the addresses and the A3-street branch) moved
# none of them, so лот Б ADDS a bucket instead of re-freezing; a movement here is
# a STOP with a named list, exactly as it is against a58010e.
LOT1V_B_ANCHOR = "3e169c2"         # F6-а — the last frozen artefact before лот Б
# Амандамент А5 (2): every anchor the suite reads must be an ANCESTOR of HEAD.
# The rebase of 04.09 rewrote the three hashes this file used to carry, and a
# rewritten commit lives on in the reflog of THIS checkout only — `git show` found
# them here and nowhere else. The twins below are the same commits rewritten in
# place: each pair shares the artefact blob (23af63f ↔ 6032023 share the whole
# tree), so re-anchoring moved no expectation, no exception and no bucket sum.
ANCHORS = (LOT1_DATA_ANCHOR, LOT1V_A_ANCHOR, LOT1V_B_ANCHOR, "9c89463", "a42be4c")
# The pre-rebase hashes (7a6ea1d → 9c89463, 378a844 → a42be4c, 23af63f → 6032023).
# They are named for two reasons: the scan in AnchorsReachableTest stays exact,
# and the ancestry check is PROVED to discriminate — these three are not ancestors.
REBASED_AWAY = ("7a6ea1d", "378a844", "23af63f")
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
    the ARTEFACT the probe replays must differ from 6032023 in exactly the 55
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
        nor new must be equal to 6032023 by (q, branch, name, zone)."""
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


# --- F6-а: the additive freeze -----------------------------------------------
# ADR 008 D4/D7 and план §2г S3/S6. Two claims, one file: the 122 rows of ЛОТ 1
# did NOT move when the aliases and the curated class words landed, and the
# twelve measured rows of ЛОТ 1в-А arrived as a bucket of their own. The first
# is checked against a COMMITTED blob (a58010e), the second against the
# reference's own spec — and both are checked in a way that can go red.


def lot1v_a_bucket_failures(doc):
    """The `gate_lot1v_a` bucket of an artefact against REF's measured spec.

    Pure over the document it is given, so a test can delete a row or change a
    value in a COPY and watch the answer turn red. A gate that cannot go red is
    not a gate (docs/audits — „гейтовете лъжат по-често от кода“).
    """
    spec = list(REF.LOT1V_A_GAINS) + list(REF.LOT1V_A_CONTROLS)
    bucket = doc.get("gate_lot1v_a")
    if not isinstance(bucket, list):
        return [u"gate_lot1v_a липсва от артефакта"]
    bad = []
    if len(bucket) != len(spec):
        bad.append(u"gate_lot1v_a: %d реда, очаквани %d" % (len(bucket), len(spec)))
    by_q = {}
    for entry in bucket:
        by_q.setdefault(entry["q"], []).append(entry)
    for q, branch, n, why, want in spec:
        entries = by_q.pop(q, [])
        if len(entries) != 1:
            bad.append(u"`%s`: %d реда в артефакта, очакван 1" % (q, len(entries)))
            continue
        entry = entries[0]
        if entry["branch"] != branch:
            bad.append(u"`%s`: клон %s, очакван %s" % (q, entry["branch"], branch))
        if entry["n"] != n or len(entry["rows"]) != n:
            bad.append(u"`%s`: %d реда (n=%s), очаквани %d"
                       % (q, len(entry["rows"]), entry["n"], n))
        if entry["expect"] != why:
            bad.append(u"`%s`: причината не е тази на референцията" % q)
        got = [(r["name"].strip(), r["zone"]) for r in entry["rows"]][:len(want)]
        if got != [(w[0], w[1]) for w in want]:
            bad.append(u"`%s`: първите %d реда са %s" % (q, len(want), got))
        if not entry["ok"]:
            bad.append(u"`%s`: редът не е зелен в артефакта" % q)
    for q in by_q:
        bad.append(u"`%s`: ред в артефакта, който референцията не мери" % q)
    return bad


def delivery_kinds(commit=None):
    """(name, zone) -> kind over the two delivered blobs; `None` = working tree.

    The artefact holds (name, zone) per row and never held `kind`, on either
    side of the anchor — so the third member of the S6 triple is measured here,
    on the delivery itself, instead of being claimed.
    """
    out = {}
    for name in ("data/places.json", "data/hotels.json"):
        if commit is None:
            doc = json.loads((REPO / name).read_text(encoding="utf-8"))
        else:
            got = subprocess.run(["git", "-C", str(REPO), "show", commit + ":" + name],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if got.returncode != 0:
                raise AssertionError("git show %s:%s failed" % (commit, name))
            doc = json.loads(got.stdout.decode("utf-8"))
        for row in (doc["places"] if "places" in doc else doc["hotels"]):
            out[(row["name"], row["zone"])] = row["kind"]
    return out


class Lot1vAdditiveFreezeTest(unittest.TestCase):
    """The freeze of F6-а: additive, and nothing else.

    S6 compares the candidate with the committed anchor by (bucket, q, branch,
    ordered rows). Zero movements means no re-freeze — so this test carries no
    exception list at all: the day one of the 122 rows moves, it is a STOP with
    a named list, not a new signature buried in a constant.
    """

    @classmethod
    def setUpClass(cls):
        cls.anchor = frozen_rows(LOT1V_A_ANCHOR)
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def test_the_anchor_is_the_four_buckets_and_122_rows(self):
        self.assertEqual(set(self.anchor.keys()) - {"_meta"}, set(BUCKETS))
        self.assertEqual(sum(len(self.anchor[b]) for b in BUCKETS), 122)
        self.assertNotIn("gate_lot1v_a", self.anchor)

    def test_not_one_of_the_122_rows_moved(self):
        compared, moved = 0, []
        for bucket in BUCKETS:
            anchor = dict((e["q"], e) for e in self.anchor[bucket])
            current = dict((e["q"], e) for e in self.current[bucket])
            self.assertEqual(set(anchor), set(current), bucket)
            for q, was in anchor.items():
                now = current[q]
                compared += 1
                if ((was["branch"], [(r["name"], r["zone"]) for r in was["rows"]])
                        != (now["branch"], [(r["name"], r["zone"]) for r in now["rows"]])):
                    moved.append(bucket + "/" + q)
        self.assertEqual(moved, [], u"движение срещу %s: %s"
                         % (LOT1V_A_ANCHOR, u", ".join(moved)))
        self.assertEqual(compared, 122)

    def test_the_kind_of_every_frozen_record_is_unchanged(self):
        """The third member of the S6 triple. The rows name a record by
        (name, zone); `kind` lives in the delivery, so that is where it is
        compared — for every record any of the 122 rows stands on."""
        was, now = delivery_kinds(LOT1V_A_ANCHOR), delivery_kinds()
        keys, changed, missing = set(), [], []
        for bucket in BUCKETS:
            for entry in self.current[bucket]:
                for row in entry["rows"]:
                    keys.add((row["name"], row["zone"]))
        for key in sorted(keys):
            if key not in was or key not in now:
                missing.append(key[0])
            elif was[key] != now[key]:
                changed.append(u"%s: %s → %s" % (key[0], was[key], now[key]))
        self.assertEqual(missing, [])
        self.assertEqual(changed, [])
        self.assertEqual(len(was), 375)
        self.assertEqual(len(now), 375)

    def test_the_candidate_only_grew(self):
        # F8 (ЛОТ 1в-Б) states the contract the artefact reaches in F9: the two
        # gained buckets and 134 + 6 = 140 rows. Until the re-freeze this is one of
        # the NAMED red rows of the lot — the reference is the thing that moves,
        # never the anchor.
        gained = [b for b in self.current if b != "_meta" and b not in self.anchor]
        self.assertEqual(gained, ["gate_lot1v_a", "gate_lot1v_b"])
        self.assertEqual(sum(len(self.current[b]) for b in REF_BUCKETS), 140)
        self.assertEqual(sum(len(e["rows"]) for b in BUCKETS
                             for e in self.current[b]), 1998)
        self.assertEqual(sum(len(e["rows"]) for e in self.current["gate_lot1v_a"]), 108)
        self.assertEqual(sum(len(e["rows"]) for e in self.current["gate_lot1v_b"]), 15)


class Lot1vABucketTest(unittest.TestCase):
    """The new bucket, and the proof that its gate runs and falls."""

    @classmethod
    def setUpClass(cls):
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def test_the_bucket_is_the_twelve_measured_rows(self):
        self.assertEqual(lot1v_a_bucket_failures(self.current), [])
        self.assertEqual(len(self.current["gate_lot1v_a"]), 12)
        self.assertEqual(len(REF.LOT1V_A_GAINS) + len(REF.LOT1V_A_CONTROLS), 12)

    def test_removing_any_row_turns_the_bucket_red(self):
        """Remove a row and the bucket goes red — for each of the twelve."""
        for entry in self.current["gate_lot1v_a"]:
            doc = dict(self.current)
            doc["gate_lot1v_a"] = [e for e in self.current["gate_lot1v_a"]
                                   if e["q"] != entry["q"]]
            failures = lot1v_a_bucket_failures(doc)
            self.assertNotEqual(failures, [], entry["q"])
            self.assertTrue(any(entry["q"] in f for f in failures), entry["q"])

    def test_changing_any_value_turns_the_bucket_red(self):
        """Change a value and the bucket goes red: the branch, the count, the
        rows, the name, the zone, the reason, the green flag — one at a time,
        on a copy, for every one of the twelve rows."""
        for index in range(len(self.current["gate_lot1v_a"])):
            original = self.current["gate_lot1v_a"][index]
            mutations = [
                ("branch", lambda e: dict(e, branch=e["branch"] + "-x")),
                ("n", lambda e: dict(e, n=e["n"] + 1)),
                ("rows", lambda e: dict(e, rows=e["rows"][1:], n=e["n"] - 1)),
                ("name", lambda e: dict(e, rows=[dict(e["rows"][0], name=u"друго име")]
                                        + e["rows"][1:])),
                ("zone", lambda e: dict(e, rows=[dict(e["rows"][0], zone=u"друга зона")]
                                        + e["rows"][1:])),
                ("expect", lambda e: dict(e, expect=u"друга причина")),
                ("ok", lambda e: dict(e, ok=False)),
            ]
            for label, mutate in mutations:
                bucket = list(self.current["gate_lot1v_a"])
                bucket[index] = mutate(original)
                doc = dict(self.current)
                doc["gate_lot1v_a"] = bucket
                self.assertNotEqual(lot1v_a_bucket_failures(doc), [],
                                    u"%s / %s остана зелено" % (original["q"], label))

    def test_the_live_engine_replays_the_new_bucket(self):
        """And the engine says what the bucket says — branch, ordered rows and
        the `kind` the artefact schema does not carry."""
        spec = dict((q, (branch, n, want)) for q, branch, n, why, want
                    in list(REF.LOT1V_A_GAINS) + list(REF.LOT1V_A_CONTROLS))
        for entry in self.current["gate_lot1v_a"]:
            rows, branch = REF.search(entry["q"])
            self.assertEqual(branch, entry["branch"], entry["q"])
            self.assertEqual([(r.name, r.zone) for r in rows],
                             [(r["name"], r["zone"]) for r in entry["rows"]], entry["q"])
            want_branch, want_n, want = spec[entry["q"]]
            self.assertEqual((branch, len(rows)), (want_branch, want_n), entry["q"])
            self.assertEqual([(r.name.strip(), r.zone, r.kind) for r in rows][:len(want)],
                             list(want), entry["q"])


def lot1v_b_bucket_failures(doc):
    """The `gate_lot1v_b` bucket of an artefact against REF's measured spec.

    Sibling of lot1v_a_bucket_failures() and pure over the document it is given
    for the same reason: a test can delete a row or change a value in a COPY and
    watch the answer turn red.
    """
    spec = list(REF.LOT1V_B_GAINS) + list(REF.LOT1V_B_CONTROLS)
    bucket = doc.get("gate_lot1v_b")
    if not isinstance(bucket, list):
        return [u"gate_lot1v_b липсва от артефакта"]
    bad = []
    if len(bucket) != len(spec):
        bad.append(u"gate_lot1v_b: %d реда, очаквани %d" % (len(bucket), len(spec)))
    by_q = {}
    for entry in bucket:
        by_q.setdefault(entry["q"], []).append(entry)
    for q, branch, n, why, want in spec:
        entries = by_q.pop(q, [])
        if len(entries) != 1:
            bad.append(u"`%s`: %d реда в артефакта, очакван 1" % (q, len(entries)))
            continue
        entry = entries[0]
        if entry["branch"] != branch:
            bad.append(u"`%s`: клон %s, очакван %s" % (q, entry["branch"], branch))
        if entry["n"] != n or len(entry["rows"]) != n:
            bad.append(u"`%s`: %d реда (n=%s), очаквани %d"
                       % (q, len(entry["rows"]), entry["n"], n))
        if entry["expect"] != why:
            bad.append(u"`%s`: причината не е тази на референцията" % q)
        got = [(r["name"].strip(), r["zone"]) for r in entry["rows"]][:len(want)]
        if got != [(w[0], w[1]) for w in want]:
            bad.append(u"`%s`: първите %d реда са %s" % (q, len(want), got))
        if not entry["ok"]:
            bad.append(u"`%s`: редът не е зелен в артефакта" % q)
    for q in by_q:
        bad.append(u"`%s`: ред в артефакта, който референцията не мери" % q)
    return bad


class Lot1vBGateTest(unittest.TestCase):
    """ЛОТ 1в-Б — адресите и клонът A3-street (04.09), ADR 008 D5/D6.

    Сол's six queries (план §2г S4) are the acceptance gate: three gains of the
    new branch („детска градина дойран“, „дойран 9“, „ул. дойран“) and three
    controls that must NOT move — the number without a street, the zone phrase
    ahead of the street, and the name/street collision that keeps ПАНОРАМА out of
    „хотел приморски“.
    """

    def test_gate(self):
        failures = REF.check_lot1v_b_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_measured_rows_are_six(self):
        self.assertEqual(len(REF.LOT1V_B_GAINS), 3)
        self.assertEqual(len(REF.LOT1V_B_CONTROLS), 3)

    def test_the_street_index_is_the_delivery_and_nothing_else(self):
        """D6: `spk`/`hkey` come from `address`, never from `text`.

        Measured on the P5 delivery: 190 of the 375 records carry an address over
        133 distinct street phrases, and the tokeniser collapses those to 131 KEYS
        — „8 ми приморски полк“ = „осми приморски полк“ and „45 та“ = „45“ are the
        same street written twice by two sources, and the ordinal rewriting is what
        unites them. Two spellings, one street: that is the point of the key.
        """
        with_address = [rec for rec in REF.RECS if rec.address]
        self.assertEqual(len(with_address), 190)
        self.assertEqual(len(set(rec.address["street_phrase"] for rec in with_address)), 133)
        self.assertEqual(len(REF.STREET), 131)
        self.assertEqual(sum(len(v) for v in REF.STREET.values()), 190)
        collapsed = {}
        for rec in with_address:
            collapsed.setdefault(rec.spk, set()).add(rec.address["street_phrase"])
        self.assertEqual(sorted(tuple(sorted(v)) for v in collapsed.values() if len(v) > 1),
                         [(u"45", u"45 та"),
                          (u"8 ми приморски полк", u"осми приморски полк")])
        for rec in with_address:
            self.assertEqual(rec.spk, REF.key_of(rec.address["street_phrase"]),
                             rec.name)
            self.assertEqual(rec.hkey, REF.key_of(rec.address["house_key"]), rec.name)
            self.assertIn(rec, REF.STREET[rec.spk])
        for rec in REF.RECS:
            if not rec.address:
                self.assertEqual((rec.spk, rec.hkey), ("", ""), rec.name)

    def test_the_street_tokens_stay_out_of_the_name_and_zone_sets(self):
        """S4's own condition: the branch must not be able to move A4, A5 or П7.
        The proof is structural — `nset` is still exactly the name tokens and
        `zkset` still exactly the zone and kind tokens, so not one street phrase
        and not one house number entered the sets the matcher scores on."""
        for rec in REF.RECS:
            self.assertEqual(rec.nset, set(rec.ntk), rec.name)
            self.assertEqual(rec.zkset, set(rec.ztk) | set(rec.ktk), rec.name)

    def test_a_number_without_a_whole_street_never_takes_part(self):
        """S4 gate 4, inverted: „12“ is the house number of nobody's matched
        street here, so „детска градина 12“ stays a NAME query — and the branch
        answers None for a bare number as well."""
        self.assertIsNone(REF.street_rows(REF.place_tokens(u"12"), REF.RECS))
        self.assertIsNone(REF.street_rows(REF.place_tokens(u"9"), REF.RECS))
        rows, branch = REF.search(u"детска градина 12")
        self.assertEqual((branch, len(rows)), ("M2", 1))

    def test_the_collision_rule_is_load_bearing(self):
        """G2 — a gate that cannot go red is not a gate.

        Measured 04.09: Сол's sixth query is protected by the ORDER of the branches
        (A3-record+zone-phrase answers „хотел приморски“ before the street is even
        asked), NOT by the collision rule — so the rule has three named rows of its
        own. Here the rule is disabled in place, by handing street_rows() a query
        that always carries „ул.“, and check_lot1v_b_gate() must go red on all
        three: „приморски“, „роза“, „владислав варненчик“.
        """
        original = REF.street_rows
        try:
            REF.street_rows = (lambda R, cls:
                               original(list(R) + REF.place_tokens(u"ул"), cls))
            rows, branch = REF.search(u"приморски")
            self.assertEqual((branch, rows[0].name), ("A3-street", u"Бел Епок"))
            failures = REF.check_lot1v_b_gate()
            self.assertEqual(len(failures), 3, failures)
            for query in (u"приморски", u"роза", u"владислав варненчик"):
                self.assertTrue(any(query in f for f in failures), query)
        finally:
            REF.street_rows = original
        self.assertEqual(REF.check_lot1v_b_gate(), [])
        rows, branch = REF.search(u"приморски")
        self.assertEqual((branch, rows[0].name), ("M3", u"ПРИМОРСКИ"))

    def test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path(self):
        """ADR 008 D6, the ORDER — measured on the queries that prove each step:
        the exact alias wins over its own street, the zone phrase wins over the
        street it shares a name with, and the street wins over the fuzzy scoring
        that used to answer „болница дойран“ with eleven unrelated rows."""
        self.assertEqual(REF.search(u"алеко константинов")[1], "A0-exact-alias")
        self.assertEqual(REF.search(u"училище владислав варненчик")[1],
                         "A3-category+zone/kind")
        rows, branch = REF.search(u"болница дойран")
        self.assertEqual((branch, len(rows)), ("A3-street", 1))
        self.assertEqual(rows[0].name,
                         u"„Университетска специализирана болница по очни болести "
                         u"за активно лечение – Варна“ ЕООД")


class Lot1vBAdditiveFreezeTest(unittest.TestCase):
    """The freeze of F9 — F6-а's shape, one lot later, and against F6-а itself.

    план §2г S6: the candidate is compared with the LAST frozen artefact
    (`3e169c2`, five buckets, 134 rows) by (bucket, q, branch, hasKey, ordered
    rows) — plus `kind`, which the artefact schema does not carry and which is
    therefore measured on the delivery. Zero movements is what makes „add a
    bucket“ legitimate instead of a re-freeze, so this class carries no exception
    list either: the day one of the 134 moves, it is a STOP with a named list.
    """

    # The fourth member of the S6 tuple is not a column of the artefact. It is
    # `splitKeys()` over the class keys (index.html „const sk = splitKeys(qt)“,
    # recall_sweep.search()), and every branch name below says what it was for the
    # query that produced it. „empty“ (no tokens at all) and „A3-street“ (the new
    # branch answers with or without a key) are the two that do not — they are
    # named here, and a branch that is on neither list is red.
    HASKEY_BY_BRANCH = {
        "M1-category": True,
        "M2": True,
        "M2-failopen": True,
        "A3-record+zone-phrase": True,
        "A3-category+zone/kind": True,
        "M3": False,
        "M3-too-big": False,
        "A0-exact-alias": False,
    }
    HASKEY_NOT_DECIDED_BY_BRANCH = ("empty", "A3-street")

    @classmethod
    def setUpClass(cls):
        cls.anchor = frozen_rows(LOT1V_B_ANCHOR)
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))
        cls.frozen_buckets = BUCKETS + ("gate_lot1v_a",)

    def test_the_anchor_is_the_five_buckets_and_134_rows(self):
        self.assertEqual(set(self.anchor.keys()) - {"_meta"}, set(self.frozen_buckets))
        self.assertEqual(sum(len(self.anchor[b]) for b in self.frozen_buckets), 134)
        self.assertNotIn("gate_lot1v_b", self.anchor)

    def test_not_one_of_the_134_rows_moved(self):
        compared, moved = 0, []
        for bucket in self.frozen_buckets:
            anchor = dict((e["q"], e) for e in self.anchor[bucket])
            current = dict((e["q"], e) for e in self.current[bucket])
            self.assertEqual(set(anchor), set(current), bucket)
            for q, was in anchor.items():
                now = current[q]
                compared += 1
                if ((was["branch"], [(r["name"], r["zone"]) for r in was["rows"]])
                        != (now["branch"], [(r["name"], r["zone"]) for r in now["rows"]])):
                    moved.append(bucket + "/" + q)
        self.assertEqual(moved, [], u"движение срещу %s: %s"
                         % (LOT1V_B_ANCHOR, u", ".join(moved)))
        self.assertEqual(compared, 134)

    def test_the_kind_of_every_frozen_record_is_unchanged(self):
        """The third member of the S6 triple, against THIS anchor: ЛОТ 1в-Б
        rewrote both delivered blobs (the addresses), so „the rows did not move“
        has to be said about the records they stand on as well."""
        was, now = delivery_kinds(LOT1V_B_ANCHOR), delivery_kinds()
        keys, changed, missing = set(), [], []
        for bucket in self.frozen_buckets:
            for entry in self.current[bucket]:
                for row in entry["rows"]:
                    keys.add((row["name"], row["zone"]))
        for key in sorted(keys):
            if key not in was or key not in now:
                missing.append(key[0])
            elif was[key] != now[key]:
                changed.append(u"%s: %s → %s" % (key[0], was[key], now[key]))
        self.assertEqual(missing, [])
        self.assertEqual(changed, [])
        self.assertEqual((len(was), len(now)), (375, 375))

    def test_haskey_could_not_have_moved_and_agrees_with_every_branch(self):
        """The fourth member. `hasKey` is derived from the class keys of
        data/place_categories.json — the blob ЛОТ 1в-Б did not touch (byte-equal
        to the anchor's) — and to keep that from being a claim, the key split is
        run again over all 134 queries and compared with the branch the ANCHOR
        recorded. A class key that had moved would flip one of them."""
        got = subprocess.run(["git", "-C", str(REPO), "show",
                              LOT1V_B_ANCHOR + ":data/place_categories.json"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(got.returncode, 0, got.stderr.decode("utf-8", "replace"))
        self.assertEqual(
            hashlib.sha256(got.stdout).hexdigest(),
            hashlib.sha256((REPO / "data" / "place_categories.json").read_bytes()).hexdigest(),
            "the class keys moved — hasKey is not comparable without a measure")
        checked = 0
        for bucket in self.frozen_buckets:
            for entry in self.anchor[bucket]:
                branch = entry["branch"]
                if branch in self.HASKEY_NOT_DECIDED_BY_BRANCH:
                    continue
                self.assertIn(branch, self.HASKEY_BY_BRANCH, entry["q"])
                tokens = REF.place_tokens(entry["q"])
                has_key = (bool(tokens) and not REF.exact_alias(tokens)
                           and bool(REF.split_keys(tokens)[0]))
                self.assertEqual(has_key, self.HASKEY_BY_BRANCH[branch],
                                 u"%s/%s" % (bucket, entry["q"]))
                checked += 1
        self.assertEqual(checked, 133)

    def test_the_only_gained_bucket_is_the_six_new_rows(self):
        gained = [b for b in self.current if b != "_meta" and b not in self.anchor]
        self.assertEqual(gained, ["gate_lot1v_b"])
        self.assertEqual(len(self.current["gate_lot1v_b"]), 6)
        self.assertEqual(sum(len(e["rows"]) for e in self.current["gate_lot1v_b"]), 15)
        self.assertEqual(sum(len(self.current[b]) for b in REF_BUCKETS), 140)


class Lot1vBBucketTest(unittest.TestCase):
    """The new bucket, and the proof that its gate runs and falls.

    Red until F9 by design: F8 does not re-freeze the reference (план §2г S6 —
    with 0 movements there is nothing to re-freeze, only to ADD), so the
    committed artefact does not carry `gate_lot1v_b` yet.
    """

    @classmethod
    def setUpClass(cls):
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def test_the_bucket_is_the_six_measured_rows(self):
        self.assertEqual(lot1v_b_bucket_failures(self.current), [])
        self.assertEqual(len(self.current["gate_lot1v_b"]), 6)
        self.assertEqual(len(REF.LOT1V_B_GAINS) + len(REF.LOT1V_B_CONTROLS), 6)

    def test_removing_any_row_turns_the_bucket_red(self):
        for entry in self.current.get("gate_lot1v_b", []):
            doc = dict(self.current)
            doc["gate_lot1v_b"] = [e for e in self.current["gate_lot1v_b"]
                                   if e["q"] != entry["q"]]
            failures = lot1v_b_bucket_failures(doc)
            self.assertNotEqual(failures, [], entry["q"])
            self.assertTrue(any(entry["q"] in f for f in failures), entry["q"])

    def test_changing_any_value_turns_the_bucket_red(self):
        for index in range(len(self.current.get("gate_lot1v_b", []))):
            original = self.current["gate_lot1v_b"][index]
            mutations = [
                ("branch", lambda e: dict(e, branch=e["branch"] + "-x")),
                ("n", lambda e: dict(e, n=e["n"] + 1)),
                ("rows", lambda e: dict(e, rows=e["rows"][1:], n=e["n"] - 1)),
                ("name", lambda e: dict(e, rows=[dict(e["rows"][0], name=u"друго име")]
                                        + e["rows"][1:])),
                ("zone", lambda e: dict(e, rows=[dict(e["rows"][0], zone=u"друга зона")]
                                        + e["rows"][1:])),
                ("expect", lambda e: dict(e, expect=u"друга причина")),
                ("ok", lambda e: dict(e, ok=False)),
            ]
            for label, mutate in mutations:
                bucket = list(self.current["gate_lot1v_b"])
                bucket[index] = mutate(original)
                doc = dict(self.current)
                doc["gate_lot1v_b"] = bucket
                self.assertNotEqual(lot1v_b_bucket_failures(doc), [],
                                    u"%s / %s остана зелено" % (original["q"], label))

    def test_the_live_engine_replays_the_new_bucket(self):
        spec = dict((q, (branch, n, want)) for q, branch, n, why, want
                    in list(REF.LOT1V_B_GAINS) + list(REF.LOT1V_B_CONTROLS))
        for entry in self.current.get("gate_lot1v_b", []):
            rows, branch = REF.search(entry["q"])
            self.assertEqual(branch, entry["branch"], entry["q"])
            self.assertEqual([(r.name, r.zone) for r in rows],
                             [(r["name"], r["zone"]) for r in entry["rows"]], entry["q"])
            want_branch, want_n, want = spec[entry["q"]]
            self.assertEqual((branch, len(rows)), (want_branch, want_n), entry["q"])
            self.assertEqual([(r.name.strip(), r.zone, r.kind) for r in rows][:len(want)],
                             list(want), entry["q"])


class RefBucketsTest(unittest.TestCase):
    """ADR 008 D7: the bucket list is fail-closed on all three sides."""

    def test_the_artefact_carries_exactly_the_named_buckets(self):
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        self.assertEqual(set(current.keys()) - {"_meta"}, set(REF_BUCKETS))

    def test_the_probe_names_the_same_buckets_in_the_same_order(self):
        probe = PROBE.read_text(encoding="utf-8")
        match = re.search(r"const REF_BUCKETS = \[([^\]]*)\];", probe)
        self.assertIsNotNone(match, "REF_BUCKETS is not a literal in the probe")
        self.assertEqual(tuple(re.findall(r'"([^"]+)"', match.group(1))), REF_BUCKETS)
        # The fail-open form this replaced filtered the list by what the FILE
        # happens to hold, so a bucket the file had lost was simply skipped.
        # A `.filter(` hung on the literal itself brings that back.
        self.assertIsNone(
            re.search(r"const REF_BUCKETS = \[[^\]]*\]\s*\.filter\(", probe),
            "REF_BUCKETS is filtered by the file again (fail-open)")

    def test_the_reference_names_the_same_buckets_in_the_same_order(self):
        """The third side: the generator. A bucket that lives in the artefact
        alone would be a hand edit nobody can regenerate."""
        self.assertEqual(tuple(REF.REF_BUCKETS), REF_BUCKETS)

    def test_the_reference_refuses_an_artefact_with_other_buckets(self):
        """Runs and fails: `bucket_drift()` is what stops main() from writing."""
        good = dict((b, []) for b in REF_BUCKETS)
        good["_meta"] = {}
        self.assertEqual(REF.bucket_drift(good), [])
        lost = dict(good)
        del lost["gate_lot1v_a"]
        self.assertEqual(REF.bucket_drift(lost), [u"липсва gate_lot1v_a"])
        gained = dict(good)
        gained["gate_lot1v_v"] = []
        self.assertEqual(REF.bucket_drift(gained), [u"нов gate_lot1v_v"])
        broken = dict(good)
        broken["extra"] = {"not": "a list"}
        self.assertEqual(REF.bucket_drift(broken), [u"липсва extra"])


class AnchorsReachableTest(unittest.TestCase):
    """Амандамент А5 (2): the anchors are ANCESTORS of HEAD, not reflog ghosts.

    `git show <commit>:<path>` resolves a rewritten commit for as long as the
    reflog of that one checkout remembers it — so the anchor tests were green
    here and red in a fresh clone, which is the definition of a gate that lies.
    Three things are gated: every anchor is an ancestor, every anchor really
    hands over its artefact, and no OTHER commit hash hides in this file.
    """

    def ancestry(self, commit):
        """0 = ancestor of HEAD, anything else = not (128 = does not resolve)."""
        return subprocess.run(["git", "-C", str(REPO), "merge-base",
                               "--is-ancestor", commit, "HEAD"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode

    def test_every_anchor_is_an_ancestor_of_head(self):
        unreachable = [c for c in ANCHORS if self.ancestry(c) != 0]
        self.assertEqual(unreachable, [], u"котви извън историята на main: %s"
                         % u", ".join(unreachable))

    def test_the_check_discriminates(self):
        """The differential — a gate that cannot go red is not a gate. The three
        pre-rebase hashes are exactly what the debt was about, and they must NOT
        pass the check above (in this checkout they still resolve, through the
        reflog; in a fresh clone they do not resolve at all)."""
        for commit in REBASED_AWAY:
            self.assertNotEqual(self.ancestry(commit), 0, commit)

    def test_the_live_anchors_hand_over_their_artefact(self):
        """Reachable is not the same as usable: the three anchors the suite reads
        must answer with an artefact of the shape their tests expect."""
        for commit, buckets in ((LOT1_DATA_ANCHOR, BUCKETS),
                                (LOT1V_A_ANCHOR, BUCKETS),
                                (LOT1V_B_ANCHOR, BUCKETS + ("gate_lot1v_a",))):
            doc = frozen_rows(commit)
            self.assertEqual(set(doc.keys()) - {"_meta"}, set(buckets), commit)
        self.assertEqual(sum(len(frozen_rows(LOT1_DATA_ANCHOR)[b]) for b in BUCKETS), 113)
        self.assertEqual(sum(len(frozen_rows(LOT1V_A_ANCHOR)[b]) for b in BUCKETS), 122)

    def test_no_commit_hash_in_this_file_is_off_the_list(self):
        """The scan that keeps the list from going stale: every 7-hex word in this
        file is either an anchor or one of the pre-rebase hashes it replaced. A
        hash pasted into a docstring tomorrow is red until it is named here."""
        text = pathlib.Path(__file__).read_text(encoding="utf-8")
        found = set(re.findall(r"(?<![0-9a-zA-Z_])[0-9a-f]{7}(?![0-9a-zA-Z_])", text))
        self.assertEqual(found, set(ANCHORS) | set(REBASED_AWAY))


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
