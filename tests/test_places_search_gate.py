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
# ADR 008 D7 — fail-closed, and the WHOLE list: F6-а added `gate_lot1v_a`
# ADDITIVELY (план §2г S3/S6) and F8 added `gate_lot1v_b` the same way, so the
# four above keep their anchor and each new lot answers in a bucket of its own. `REF_BUCKETS` is hand-kept on three sides —
# here, in scratch/places_search/probe_places_fv.mjs (the probe that replays the
# rows) and in scratch/places_search/recall_sweep.py (the reference, which refuses
# to WRITE an artefact with other keys). RefBucketsTest compares all three against
# the artefact, so a bucket added on one side alone is red without a browser.
# The bucket list itself is NOT delivery data: it is the fail-closed contract of
# ADR 008 D7, hand-kept on three sides (here, the probe, the reference). What the
# ARTEFACT carries is delivery data and is read from the signature below.
REF_BUCKETS = ("gate_m5_a8", "extra", "gate_p7", "gate_lot1",
               "gate_lot1v_a", "gate_lot1v_b")
PROBE = REPO / "scratch" / "places_search" / "probe_places_fv.mjs"
# F12-в: the two report-only manifests. An expectation typed into a test is an
# expectation nobody signed — the numbers below are read out of the manifest and
# the manifest is worthless until Petar's name is on it.
# A.2-4 (амандамент №4 т. 1): ONE signable body. Every expectation in this file
# that depends on the DELIVERY — a row count, a branch, a name, a zone, an
# anchor commit, a bucket list — is read from here, and it is worth exactly the
# signature on it. Until Petar signs, `require_signed` is the one thing that
# fails and it says why; after his signature and ONE freeze the whole suite is
# green. No number below is typed by an agent.
EXPECTATIONS = REPO / "scratch" / "places_search" / "expectations.json"
SIGNER = "Петър"


def expectations():
    """The signed body, or {} when it is not there at all (fail-closed)."""
    if not EXPECTATIONS.exists():
        return {}
    return json.loads(EXPECTATIONS.read_text(encoding="utf-8"))


EXP = expectations()
EXP_SIGNATURE = ((EXP.get("_meta") or {}).get("signed_by") or "").strip()
ANCHOR_BLOCK = (EXP.get("anchors") or {}).get("anchors") or {}


def require_expectations(case):
    """The tracked answers have to BE there — fail-closed, one message.

    План v2 §0.4/§A.2: whether Petar has SIGNED them is the release gate's
    question (`python -m gates.release`, проверка 6 of run_gates) and the
    condition `--freeze` refuses to write without; a test that goes red because
    a signature is pending is „червено по замисъл“, which the plan abolished.
    `ReleaseGateSignatureTest` below is the one place that reads `signed_by`."""
    case.assertTrue(EXP, "scratch/places_search/expectations.json липсва — "
                         "гейтовете нямат записани очаквания (fail-closed)")


def anchor_block(name):
    return ANCHOR_BLOCK.get(name) or {}


def claim(name):
    return (EXP.get("claims") or {}).get(name) or {}


def gate_answers(gate):
    """[{class, q, why, branch, hasKey, n, rows}] — the signed answers of a gate."""
    return ((EXP.get("gate_queries") or {}).get(gate)) or []


# The three anchors of the reference and the hashes that were rebased away: they
# are HISTORY, so they are named in the signed body and read from it here — this
# file carries no commit hash of its own any more (AnchorsReachableTest proves it).
LOT1_DATA_ANCHOR = anchor_block("lot1_data").get("commit")
LOT1V_A_ANCHOR = anchor_block("lot1v_a").get("commit")
LOT1V_B_ANCHOR = anchor_block("lot1v_b").get("commit")
ANCHORS = tuple([c for c in (LOT1_DATA_ANCHOR, LOT1V_A_ANCHOR, LOT1V_B_ANCHOR) if c]
                + list((EXP.get("anchors") or {}).get("retired") or ()))
REBASED_AWAY = tuple((EXP.get("anchors") or {}).get("rebased_away") or ())
# The four buckets the лот-1 anchor holds — measured, not typed.
BUCKETS = tuple(anchor_block("lot1_data").get("buckets") or ())


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

    def test_added_tokens_are_the_signed_measure(self):
        """Р5 says a zone that enters the delivery legitimately changes this —
        so the number is not typed here. It is measured, signed, and compared."""
        require_expectations(self)
        p7 = EXP["p7"]
        self.assertEqual(REF.P7_ADDED, p7["added"])
        self.assertEqual(sum(len(v) for v in REF.P7_ADDED.values()), p7["tokens"])
        self.assertEqual(len(REF.P7_ADDED), p7["zones"])

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
        require_expectations(self)
        self.assertEqual(sorted(added & aliases), EXP["p7"]["alias_intersection"])

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
        require_expectations(self)
        cats = json.loads((REPO / "data" / "place_categories.json").read_text(encoding="utf-8"))
        _, added, dropped = REF.zone_alias_tokens(cats, REF.ZONES_IN)
        # The tag is `foreign:<the foreign token>:<the candidate>`. WHICH zones
        # the guard bites on is delivery data, so the pairs come from the
        # signature; that there ARE such pairs is the claim of the rule.
        pairs = EXP["p7"]["foreign_guard"]
        self.assertTrue(pairs, "гардът не изхвърля нищо — П7 стъпка (д) е мъртва")
        for pair in pairs:
            zone, token, tag = pair["zone"], pair["token"], pair["tag"]
            self.assertNotIn(token, added.get(zone, []), zone)
            self.assertIn(tag, dropped.get(zone, []), zone)
        # …and the guard is fed by the OTHER zones: with one zone alone it has
        # nothing foreign to compare against and the same tokens come back.
        for zone, tokens in EXP["p7"]["guard_starved"].items():
            _, alone, _ = REF.zone_alias_tokens(cats, [zone])
            self.assertEqual(alone.get(zone), tokens, zone)

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
        queries = " ".join(q for _cls, q, _why in REF.GATE_QUERIES[u"p7"])
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
        return q in (anchor_block("lot1_data").get("moved") or {}).get(bucket, ())

    def added(self, bucket, q):
        return q in (anchor_block("lot1_data").get("added") or {}).get(bucket, ())

    def test_the_signed_lists_are_the_measured_counts(self):
        """The change list is MEASURED against the anchor and signed; it used to
        be 55 + 9 typed into this file, and after a re-freeze it is another
        number — which is exactly why it cannot live here."""
        require_expectations(self)
        block = anchor_block("lot1_data")
        self.assertEqual(sum(len(self.anchor[b]) for b in BUCKETS), block["queries"])
        self.assertEqual(sum(len(self.current[b]) for b in BUCKETS),
                         block["queries"] + sum(len(v) for v in (block.get("added") or {}).values()))
        for bucket in BUCKETS:
            anchored = set(e["q"] for e in self.anchor[bucket])
            live = set(e["q"] for e in self.current[bucket])
            self.assertEqual(anchored - live, set(),
                             "a row vanished from " + bucket)
            self.assertEqual(live - anchored,
                             set((anchor_block("lot1_data").get("added") or {}).get(bucket, ())),
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
        block = anchor_block("lot1_data")
        self.assertEqual(compared, block["unchanged"])

    def test_every_signed_row_really_moved(self):
        """The half that catches a stale list: a query that is on the signed list
        but answers exactly as it did at the anchor is red — the signature is
        then describing a change that no longer exists."""
        moved = 0
        for bucket in BUCKETS:
            anchor = dict((e["q"], e) for e in self.anchor[bucket])
            for q in (anchor_block("lot1_data").get("moved") or {}).get(bucket, ()):
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
        self.assertEqual(moved, sum(len(v) for v in
                                    (anchor_block("lot1_data").get("moved") or {}).values()))

    def test_the_live_engine_replays_the_artefact(self):
        """And the engine says what the artefact says — all 122 queries, ordered
        rows and branch, not a count."""
        require_expectations(self)
        compared, rows = 0, 0
        for bucket in BUCKETS:
            for entry in self.current[bucket]:
                got, branch = REF.search(entry["q"])
                self.assertEqual(branch, entry["branch"], entry["q"])
                self.assertEqual([(r.name, r.zone) for r in got],
                                 [(r["name"], r["zone"]) for r in entry["rows"]],
                                 entry["q"])
                if entry["ok"] is False:
                    # The §10 sweep keeps the rows the delivery broke; WHICH ones
                    # is signed, so a new one is red and an old one is not.
                    self.assertIn(entry["q"], EXP["replay"][bucket]["not_ok"], entry["q"])
                compared += 1
                rows += len(got)
        replay = EXP["replay"]
        self.assertEqual(compared, sum(replay[b]["queries"] for b in BUCKETS))
        self.assertEqual(rows, sum(replay[b]["rows"] for b in BUCKETS))

    def test_rows_carry_the_p7_measure(self):
        require_expectations(self)
        current, p7 = self.current, EXP["p7"]
        self.assertEqual(current["_meta"]["p7_added"], p7["added"])
        self.assertEqual(current["_meta"]["p7_tokens"], p7["tokens"])
        self.assertEqual(current["_meta"]["p7_zones_with_aliases"], p7["zones"])
        self.assertEqual(len(current["gate_p7"]), len(gate_answers(u"p7")))
        for entry in current["gate_p7"]:
            self.assertIsNot(entry["ok"], False, entry["q"])


class Lot1GateTest(unittest.TestCase):
    """ЛОТ 1 — the two client rules of решения 2 и 1, signed 03.09."""

    def test_gate(self):
        failures = REF.check_lot1_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_committed_artefact_carries_the_lot1_bucket(self):
        """F2-д: the re-frozen artefact carries the ЛОТ 1 bucket the probe replays
        — one row per signed query (18 = the 10 of F2-к plus the 6 gains and 2
        controls of Амандамент №8 П2/§В/§Г), every one of them green."""
        require_expectations(self)
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        bucket = current["gate_lot1"]
        self.assertEqual(len(bucket), len(REF.GATE_QUERIES[u"lot1"]))
        self.assertEqual(len(bucket), EXP["replay"]["gate_lot1"]["queries"])
        for entry in bucket:
            self.assertIsNot(entry["ok"], False, entry["q"])

    def test_the_exact_name_prepend_is_load_bearing(self):
        """Решение 2, inverted in place: with an empty exact-name index „градина“
        falls back to the 51 kindergartens. Restored, the hotel is first again."""
        require_expectations(self)
        want = claim("exact_name_prepend")
        saved = REF.EXACT_NAME
        try:
            REF.EXACT_NAME = {}
            rows, branch = REF.search(want["q"])
            self.assertEqual((branch, len(rows)),
                             (want["without"]["branch"], want["without"]["n"]))
        finally:
            REF.EXACT_NAME = saved
        rows, branch = REF.search(want["q"])
        self.assertEqual((branch, len(rows), [r.name.strip() for r in rows]),
                         (want["with"]["branch"], want["with"]["n"], want["with"]["rows"]))

    def test_the_zone_phrase_override_is_load_bearing(self):
        """Решение 1, inverted in place: with no phrase on any record the three
        moved rows fall back to the answers the frozen artefact holds."""
        require_expectations(self)
        # ЛОТ 1в-В renamed the phrase sets: one `zph` per record became `qph`
        # (quarter), `lph` (locality) and `gph` (the row's own old zone words).
        # Clearing the three is what „no phrase on any record“ means today.
        want = claim("zone_phrase_override")
        queries = want["queries"]
        saved = [(rec, rec.qph, rec.lph, rec.gph) for rec in REF.RECS]
        try:
            for rec in REF.RECS:
                rec.qph, rec.lph, rec.gph = set(), set(), set()
            self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                             [(a["branch"], a["n"]) for a in want["without"]])
        finally:
            for rec, qph, lph, gph in saved:
                rec.qph, rec.lph, rec.gph = qph, lph, gph
        self.assertEqual([(REF.search(q)[1], len(REF.search(q)[0])) for q in queries],
                         [(a["branch"], a["n"]) for a in want["with"]])

    def test_a_phrase_is_the_canonical_zone_or_an_accepted_p7_form(self):
        """The admissibility rule, measured: „Приморски парк“ is an alias of
        Морска градина that П7 threw out as foreign, so it is NOT a phrase there
        — which is the whole difference between „хотел приморски“ = 5 and = 23.
        „кв. Владиславово“ was accepted by П7, so it IS one."""
        # ЛОТ 1в-В: the phrases are per CLASS and per CODE now (`LOC_PHRASES`),
        # not per zone string — the rule is the same one, and which phrases the
        # delivery produces is signed data, so it is compared, not typed.
        require_expectations(self)
        signed_phrases = claim("location_phrases")
        got = dict((cls, dict((code, sorted(REF.LOC_PHRASES[cls][code]))
                              for code in REF.LOC_PHRASES[cls]))
                   for cls in REF.LOC_PHRASES)
        self.assertEqual(got, signed_phrases)
        for cls in REF.LOC_PHRASES:
            for code, phrases in REF.LOC_PHRASES[cls].items():
                for phrase in phrases:
                    for token in phrase.split(" "):
                        self.assertNotIn(token, ("raion", "kvartal", "kompleks", "zona",
                                                 "mestnost", "park", "chast"), code)

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

    def test_the_questions_and_the_signed_answers_agree(self):
        require_expectations(self)
        self.assertEqual(len(REF.GATE_QUERIES[u"lot1v_a"]), len(gate_answers(u"lot1v_a")))
        self.assertEqual(sorted(q for _c, q, _w in REF.GATE_QUERIES[u"lot1v_a"]),
                         sorted(e["q"] for e in gate_answers(u"lot1v_a")))

    def test_the_generic_word_filter_is_load_bearing(self):
        """G2 — a gate that cannot go red is not a gate. `варна` is put back into
        every alias token set in place; the control then finds rows that stand in
        the answer through an alias alone, and check_lot1v_a_gate() says so."""
        require_expectations(self)
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
        require_expectations(self)
        want = claim("two_token_floor")
        saved = REF.alias_significant
        try:
            REF.alias_significant = lambda qt: 2
            rows, branch = REF.search(want["q"])
            self.assertEqual((branch, rows[0].name.strip()),
                             (want["without_the_floor"]["branch"],
                              want["without_the_floor"]["rows"][0]))
        finally:
            REF.alias_significant = saved
        rows, branch = REF.search(want["q"])
        self.assertEqual((branch, rows[0].name.strip()),
                         (want["with"]["branch"], want["with"]["rows"][0]))

    def test_the_exact_alias_index_is_the_whole_alias_and_nothing_else(self):
        """D2: one key per delivered old name, keyed by the WHOLE normalised
        string. Measured 04.09: 82 aliases, 82 keys, and the only key that is also
        a current name belongs to the SAME record."""
        require_expectations(self)
        want = claim("exact_alias_index")
        delivered = sum(len(rec.old_names) for rec in REF.RECS)
        self.assertEqual(delivered, want["delivered_aliases"])
        self.assertEqual(len(REF.EXACT_ALIAS), want["keys"])
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
    # The spec is the SIGNED answer now, not a tuple that travels with the code
    # it judges: (branch, n, why, the whole ordered list of rows).
    spec = gate_answers(u"lot1v_a")
    bucket = doc.get("gate_lot1v_a")
    if not isinstance(bucket, list):
        return [u"gate_lot1v_a липсва от артефакта"]
    bad = []
    if not spec:
        return [u"gate_lot1v_a: няма подписани отговори в expectations.json"]
    if len(bucket) != len(spec):
        bad.append(u"gate_lot1v_a: %d реда, очаквани %d" % (len(bucket), len(spec)))
    by_q = {}
    for entry in bucket:
        by_q.setdefault(entry["q"], []).append(entry)
    for signed in spec:
        q, branch, n, why = (signed["q"], signed["branch"], signed["n"], signed["why"])
        want = [(r["name"], r["zone"], r["kind"]) for r in signed["rows"]]
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
        if entry["ok"] is False:
            bad.append(u"`%s`: редът е ЧЕРВЕН в артефакта" % q)
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

    def test_the_anchor_is_what_the_signature_says(self):
        require_expectations(self)
        block = anchor_block("lot1v_a")
        self.assertEqual(set(self.anchor.keys()) - {"_meta"}, set(block["buckets"]))
        self.assertEqual(sum(len(self.anchor[b]) for b in block["buckets"]),
                         block["queries"])
        self.assertNotIn("gate_lot1v_a", self.anchor)

    def test_the_movement_against_the_anchor_is_the_signed_one(self):
        """F6-а froze ADDITIVELY: nothing moved, so the signed list was empty.
        A re-freeze makes it a LIST, and the honest form of the claim is „the
        movement is exactly the one Petar signed“, never a hard-coded []."""
        require_expectations(self)
        block = anchor_block("lot1v_a")
        compared, moved = 0, {}
        for bucket in block["buckets"]:
            was_rows = dict((e["q"], e) for e in self.anchor[bucket])
            now_rows = dict((e["q"], e) for e in self.current[bucket])
            self.assertEqual(set(was_rows), set(now_rows), bucket)
            for q, was in was_rows.items():
                now = now_rows[q]
                compared += 1
                if ((was["branch"], [(r["name"], r["zone"]) for r in was["rows"]])
                        != (now["branch"], [(r["name"], r["zone"]) for r in now["rows"]])):
                    moved.setdefault(bucket, []).append(q)
        self.assertEqual({k: sorted(v) for k, v in moved.items()},
                         {k: sorted(v) for k, v in (block.get("moved") or {}).items()},
                         u"движение срещу %s, различно от подписаното" % LOT1V_A_ANCHOR)
        self.assertEqual(compared, block["queries"])

    def test_the_kind_of_every_frozen_record_is_unchanged(self):
        """The third member of the S6 triple. The rows name a record by
        (name, zone); `kind` lives in the delivery, so that is where it is
        compared — for every record any of the 122 rows stands on."""
        require_expectations(self)
        block = anchor_block("lot1v_a")
        was, now = delivery_kinds(LOT1V_A_ANCHOR), delivery_kinds()
        keys, changed, missing = set(), [], []
        for bucket in block["buckets"]:
            for entry in self.current[bucket]:
                for row in entry["rows"]:
                    keys.add((row["name"], row["zone"]))
        for key in sorted(keys):
            if key not in was or key not in now:
                missing.append(key[0])
            elif was[key] != now[key]:
                changed.append(u"%s: %s → %s" % (key[0], was[key], now[key]))
        self.assertEqual(missing, block["kind_missing"])
        self.assertEqual(changed, block["kind_changed"])
        self.assertEqual(len(was), block["delivery_records"]["anchor"])
        self.assertEqual(len(now), block["delivery_records"]["now"])

    def test_the_candidate_only_grew(self):
        # F8 (ЛОТ 1в-Б) states the contract the artefact reaches in F9: the two
        # gained buckets and 134 + 6 = 140 rows. Until the re-freeze this is one of
        # the NAMED red rows of the lot — the reference is the thing that moves,
        # never the anchor.
        require_expectations(self)
        block, replay = anchor_block("lot1v_a"), EXP["replay"]
        gained = [b for b in self.current if b != "_meta" and b not in self.anchor]
        self.assertEqual(gained, [b for b in EXP["artefact"]["buckets"]
                                  if b not in block["buckets"]])
        for bucket in EXP["artefact"]["buckets"]:
            self.assertEqual(len(self.current[bucket]), replay[bucket]["queries"], bucket)
            self.assertEqual(sum(len(e["rows"]) for e in self.current[bucket]),
                             replay[bucket]["rows"], bucket)


class Lot1vABucketTest(unittest.TestCase):
    """The new bucket, and the proof that its gate runs and falls."""

    @classmethod
    def setUpClass(cls):
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def test_the_bucket_is_the_signed_answers(self):
        require_expectations(self)
        self.assertEqual(lot1v_a_bucket_failures(self.current), [])
        self.assertEqual(len(self.current["gate_lot1v_a"]),
                         EXP["replay"]["gate_lot1v_a"]["queries"])
        self.assertEqual(len(REF.GATE_QUERIES[u"lot1v_a"]), len(gate_answers(u"lot1v_a")))

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
        require_expectations(self)
        spec = dict((e["q"], (e["branch"], e["n"],
                              [(r["name"], r["zone"], r["kind"]) for r in e["rows"]]))
                    for e in gate_answers(u"lot1v_a"))
        for entry in self.current["gate_lot1v_a"]:
            rows, branch = REF.search(entry["q"])
            self.assertEqual(branch, entry["branch"], entry["q"])
            self.assertEqual([(r.name, r.zone) for r in rows],
                             [(r["name"], r["zone"]) for r in entry["rows"]], entry["q"])
            want_branch, want_n, want = spec[entry["q"]]
            self.assertEqual((branch, len(rows)), (want_branch, want_n), entry["q"])
            self.assertEqual([(r.name.strip(), r.zone, r.kind) for r in rows],
                             list(want), entry["q"])


def lot1v_b_bucket_failures(doc):
    """The `gate_lot1v_b` bucket of an artefact against REF's measured spec.

    Sibling of lot1v_a_bucket_failures() and pure over the document it is given
    for the same reason: a test can delete a row or change a value in a COPY and
    watch the answer turn red.
    """
    # The spec is the SIGNED answer now, not a tuple that travels with the code
    # it judges: (branch, n, why, the whole ordered list of rows).
    spec = gate_answers(u"lot1v_b")
    bucket = doc.get("gate_lot1v_b")
    if not isinstance(bucket, list):
        return [u"gate_lot1v_b липсва от артефакта"]
    bad = []
    if not spec:
        return [u"gate_lot1v_b: няма подписани отговори в expectations.json"]
    if len(bucket) != len(spec):
        bad.append(u"gate_lot1v_b: %d реда, очаквани %d" % (len(bucket), len(spec)))
    by_q = {}
    for entry in bucket:
        by_q.setdefault(entry["q"], []).append(entry)
    for signed in spec:
        q, branch, n, why = (signed["q"], signed["branch"], signed["n"], signed["why"])
        want = [(r["name"], r["zone"], r["kind"]) for r in signed["rows"]]
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
        if entry["ok"] is False:
            bad.append(u"`%s`: редът е ЧЕРВЕН в артефакта" % q)
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

    def test_the_questions_and_the_signed_answers_agree(self):
        require_expectations(self)
        self.assertEqual(len(REF.GATE_QUERIES[u"lot1v_b"]), len(gate_answers(u"lot1v_b")))
        self.assertEqual(sorted(q for _c, q, _w in REF.GATE_QUERIES[u"lot1v_b"]),
                         sorted(e["q"] for e in gate_answers(u"lot1v_b")))

    def test_the_street_index_is_the_delivery_and_nothing_else(self):
        """D6: `spk`/`hkey` come from `address`, never from `text`.

        Measured on the P5 delivery: 190 of the 375 records carry an address over
        133 distinct street phrases, and the tokeniser collapses those to 131 KEYS
        — „8 ми приморски полк“ = „осми приморски полк“ and „45 та“ = „45“ are the
        same street written twice by two sources, and the ordinal rewriting is what
        unites them. Two spellings, one street: that is the point of the key.
        """
        require_expectations(self)
        want = claim("street_index")
        with_address = [rec for rec in REF.RECS if rec.address]
        self.assertEqual(len(with_address), want["records_with_address"])
        self.assertEqual(len(set(rec.address["street_phrase"] for rec in with_address)),
                         want["street_phrases"])
        self.assertEqual(len(REF.STREET), want["street_keys"])
        self.assertEqual(sum(len(v) for v in REF.STREET.values()),
                         want["rows_behind_the_keys"])
        collapsed = {}
        for rec in with_address:
            collapsed.setdefault(rec.spk, set()).add(rec.address["street_phrase"])
        self.assertEqual(sorted([sorted(v) for v in collapsed.values() if len(v) > 1]),
                         want["two_spellings_one_street"])
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
        # ЛОТ 1в-В replaced the single `ztk` with the three typed token sets:
        # `qtk` (quarter), `ltk` (locality) and `legtk` (the row's own old zone
        # words). The claim is unchanged — no street phrase and no house number
        # entered the sets the matcher scores on.
        for rec in REF.RECS:
            self.assertEqual(rec.nset, set(rec.ntk), rec.name)
            self.assertEqual(rec.zkset,
                             set(rec.qtk) | set(rec.ltk) | set(rec.legtk) | set(rec.ktk),
                             rec.name)

    def test_a_number_without_a_whole_street_never_takes_part(self):
        """S4 gate 4, inverted: „12“ is the house number of nobody's matched
        street here, so „детска градина 12“ stays a NAME query — and the branch
        answers None for a bare number as well."""
        require_expectations(self)
        want = claim("branch_order")["number_without_street"]
        self.assertIsNone(REF.street_rows(REF.place_tokens(u"12"), REF.RECS))
        self.assertIsNone(REF.street_rows(REF.place_tokens(u"9"), REF.RECS))
        rows, branch = REF.search(u"детска градина 12")
        self.assertEqual((branch, len(rows)), (want["branch"], want["n"]))

    def test_the_collision_rule_is_load_bearing(self):
        """G2 — a gate that cannot go red is not a gate.

        Measured 04.09: Сол's sixth query is protected by the ORDER of the branches
        (A3-record+zone-phrase answers „хотел приморски“ before the street is even
        asked), NOT by the collision rule — so the rule has three named rows of its
        own. Here the rule is disabled in place, by handing street_rows() a query
        that always carries „ул.“, and check_lot1v_b_gate() must go red on all
        three: „приморски“, „роза“, „владислав варненчик“.
        """
        require_expectations(self)
        broken = claim("collision_rule_disabled")
        signed_controls = claim("collision_controls")
        original = REF.street_rows
        try:
            REF.street_rows = (lambda R, cls:
                               original(list(R) + REF.place_tokens(u"ул"), cls))
            rows, branch = REF.search(broken["q"])
            self.assertEqual((branch, rows[0].name.strip()),
                             (broken["answer"]["branch"], broken["answer"]["rows"][0]))
            failures = REF.check_lot1v_b_gate()
            self.assertEqual(len(failures), broken["failures"], failures)
            # WHICH controls move is signed data: after М7 („голото място“)
            # „приморски“ and „владислав варненчик“ are answered by the bare
            # location branch before the street is asked, so only „роза“ still
            # differentiates the collision rule — measured 05.09, not assumed.
            self.assertEqual(sorted(REF.failing_queries(failures)),
                             broken["moved_queries"])
            self.assertTrue(broken["moved_queries"],
                            u"нито една контрола не мърда — правилото е мъртво")
        finally:
            REF.street_rows = original
        self.assertEqual(REF.check_lot1v_b_gate(), [])
        for control in signed_controls:
            rows, branch = REF.search(control["q"])
            self.assertEqual((branch, rows[0].name.strip()),
                             (control["branch"], control["first"]), control["q"])

    def test_the_branch_stands_after_the_zone_and_before_the_fuzzy_path(self):
        """ADR 008 D6, the ORDER — measured on the queries that prove each step:
        the exact alias wins over its own street, the zone phrase wins over the
        street it shares a name with, and the street wins over the fuzzy scoring
        that used to answer „болница дойран“ with eleven unrelated rows."""
        require_expectations(self)
        order = claim("branch_order")
        self.assertEqual(REF.search(u"алеко константинов")[1],
                         order["exact_alias"]["branch"])
        self.assertEqual(REF.search(u"училище владислав варненчик")[1],
                         order["zone_before_street"]["branch"])
        rows, branch = REF.search(u"болница дойран")
        self.assertEqual((branch, len(rows)), (order["street_before_fuzzy"]["branch"],
                                               order["street_before_fuzzy"]["n"]))
        self.assertEqual([r.name.strip() for r in rows],
                         order["street_before_fuzzy"]["rows"])


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
    @classmethod
    def setUpClass(cls):
        cls.anchor = frozen_rows(LOT1V_B_ANCHOR)
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))
        cls.frozen_buckets = tuple(anchor_block("lot1v_b").get("buckets") or ())

    def test_the_anchor_is_what_the_signature_says(self):
        require_expectations(self)
        block = anchor_block("lot1v_b")
        self.assertEqual(set(self.anchor.keys()) - {"_meta"}, set(self.frozen_buckets))
        self.assertEqual(sum(len(self.anchor[b]) for b in self.frozen_buckets),
                         block["queries"])
        self.assertNotIn("gate_lot1v_b", self.anchor)

    def test_the_movement_against_the_anchor_is_the_signed_one(self):
        require_expectations(self)
        block = anchor_block("lot1v_b")
        compared, moved = 0, {}
        for bucket in self.frozen_buckets:
            was_rows = dict((e["q"], e) for e in self.anchor[bucket])
            now_rows = dict((e["q"], e) for e in self.current[bucket])
            self.assertEqual(set(was_rows), set(now_rows), bucket)
            for q, was in was_rows.items():
                now = now_rows[q]
                compared += 1
                if ((was["branch"], [(r["name"], r["zone"]) for r in was["rows"]])
                        != (now["branch"], [(r["name"], r["zone"]) for r in now["rows"]])):
                    moved.setdefault(bucket, []).append(q)
        self.assertEqual({k: sorted(v) for k, v in moved.items()},
                         {k: sorted(v) for k, v in (block.get("moved") or {}).items()},
                         u"движение срещу %s, различно от подписаното" % LOT1V_B_ANCHOR)
        self.assertEqual(compared, block["queries"])

    def test_the_kind_of_every_frozen_record_is_unchanged(self):
        """The third member of the S6 triple, against THIS anchor: ЛОТ 1в-Б
        rewrote both delivered blobs (the addresses), so „the rows did not move“
        has to be said about the records they stand on as well."""
        require_expectations(self)
        block = anchor_block("lot1v_b")
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
        self.assertEqual(missing, block["kind_missing"])
        self.assertEqual(changed, block["kind_changed"])
        self.assertEqual((len(was), len(now)),
                         (block["delivery_records"]["anchor"], block["delivery_records"]["now"]))

    def test_haskey_could_not_have_moved_and_agrees_with_every_branch(self):
        """The fourth member. `hasKey` is derived from the class keys of
        data/place_categories.json — the blob ЛОТ 1в-Б did not touch (byte-equal
        to the anchor's) — and to keep that from being a claim, the key split is
        run again over all 134 queries and compared with the branch the ANCHOR
        recorded. A class key that had moved would flip one of them."""
        require_expectations(self)
        block = anchor_block("lot1v_b")
        # F12-а DID move `data/place_categories.json` (the dictionary followed
        # P7), so „byte-equal to the anchor“ is no longer the claim — the two
        # digests are measured and signed, and the key split is run again over
        # every query of the anchor and compared with the branch it recorded.
        got = subprocess.run(["git", "-C", str(REPO), "show",
                              LOT1V_B_ANCHOR + ":data/place_categories.json"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(got.returncode, 0, got.stderr.decode("utf-8", "replace"))
        anchor_cats = json.loads(got.stdout.decode("utf-8"))
        now_cats = json.loads((REPO / "data" / "place_categories.json").read_text(encoding="utf-8"))
        for label, doc in (("anchor", anchor_cats), ("now", now_cats)):
            self.assertEqual(
                hashlib.sha256(json.dumps(doc, ensure_ascii=False,
                                          sort_keys=True).encode("utf-8")).hexdigest(),
                block["categories_sha"][label], label)
        measured = REF.haskey_measure(self.anchor)
        self.assertEqual(measured["mismatches"], block["haskey"]["mismatches"])
        self.assertEqual(measured["checked"], block["haskey"]["checked"])

    def test_the_gained_buckets_are_the_signed_ones(self):
        require_expectations(self)
        block, replay = anchor_block("lot1v_b"), EXP["replay"]
        gained = [b for b in self.current if b != "_meta" and b not in self.anchor]
        self.assertEqual(gained, [b for b in EXP["artefact"]["buckets"]
                                  if b not in block["buckets"]])
        self.assertEqual(sum(len(self.current[b]) for b in EXP["artefact"]["buckets"]),
                         EXP["artefact"]["queries"])
        for bucket in gained:
            self.assertEqual(sum(len(e["rows"]) for e in self.current[bucket]),
                             replay[bucket]["rows"], bucket)


class Lot1vBBucketTest(unittest.TestCase):
    """The new bucket, and the proof that its gate runs and falls.

    Red until F9 by design: F8 does not re-freeze the reference (план §2г S6 —
    with 0 movements there is nothing to re-freeze, only to ADD), so the
    committed artefact does not carry `gate_lot1v_b` yet.
    """

    @classmethod
    def setUpClass(cls):
        cls.current = json.loads(ROWS.read_text(encoding="utf-8"))

    def test_the_bucket_is_the_signed_answers(self):
        require_expectations(self)
        self.assertEqual(lot1v_b_bucket_failures(self.current), [])
        self.assertEqual(len(self.current["gate_lot1v_b"]),
                         EXP["replay"]["gate_lot1v_b"]["queries"])
        self.assertEqual(len(REF.GATE_QUERIES[u"lot1v_b"]), len(gate_answers(u"lot1v_b")))

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
        require_expectations(self)
        spec = dict((e["q"], (e["branch"], e["n"],
                              [(r["name"], r["zone"], r["kind"]) for r in e["rows"]]))
                    for e in gate_answers(u"lot1v_b"))
        for entry in self.current.get("gate_lot1v_b", []):
            rows, branch = REF.search(entry["q"])
            self.assertEqual(branch, entry["branch"], entry["q"])
            self.assertEqual([(r.name, r.zone) for r in rows],
                             [(r["name"], r["zone"]) for r in entry["rows"]], entry["q"])
            want_branch, want_n, want = spec[entry["q"]]
            self.assertEqual((branch, len(rows)), (want_branch, want_n), entry["q"])
            self.assertEqual([(r.name.strip(), r.zone, r.kind) for r in rows],
                             list(want), entry["q"])


class RefBucketsTest(unittest.TestCase):
    """ADR 008 D7: the bucket list is fail-closed on all three sides."""

    def test_the_artefact_carries_exactly_the_named_buckets(self):
        """Two claims, and the second is the one a re-freeze moves: the artefact
        carries the six buckets of the fail-closed contract, and any bucket
        BEYOND them is one the signature promoted (план §3з)."""
        require_expectations(self)
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        carried = set(current.keys()) - {"_meta"}
        self.assertEqual(carried, set(EXP["artefact"]["buckets"]))
        self.assertEqual(set(REF_BUCKETS) - carried, set())
        for extra in carried - set(REF_BUCKETS):
            self.assertIn(extra, EXP["artefact"]["pending_promoted"], extra)

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


class Lot1vVGateTest(unittest.TestCase):
    """ЛОТ 1в-В (план §3г/§3ж, Gate 1-В) — the typed location fields.

    The delivery stopped carrying one `zone` string: every record now has
    `quarter` | `district` | `locality`, each `null` or {name, src, code}, and
    the client, the mirror and the dictionary have to agree on all three. This
    class is ADDITIVE — it neither reads nor re-freezes the reference of the
    earlier lots, which is red until the manifest is signed (план §3з).

    Every assertion below is measured on the P6 delivery of varna_3d — the one
    the three payloads in `data/` are pinned to by sha256.
    """

    @classmethod
    def setUpClass(cls):
        cls.places = json.loads((REPO / "data" / "places.json").read_text(encoding="utf-8"))
        cls.hotels = json.loads((REPO / "data" / "hotels.json").read_text(encoding="utf-8"))
        cls.cats = json.loads((REPO / "data" / "place_categories.json").read_text(encoding="utf-8"))
        cls.index = INDEX.read_text(encoding="utf-8")

    def js_list(self, name):
        """The literal array `name` out of index.html, as a set of strings."""
        match = re.search(r"const " + name + r" = \[([^\]]*)\]", self.index)
        self.assertIsNotNone(match, name + " is not a literal in index.html")
        return set(re.findall(r"'([^']+)'", match.group(1)))

    def test_gate(self):
        """The nine measured queries and the schema half — fail-loud, in the suite."""
        self.assertEqual(REF.check_lot1v_v_gate(), [])

    def test_the_client_keysets_are_the_delivered_ones(self):
        """G2 of the client: EXPECT_KEYS / EXPECT2_KEYS against the real rows."""
        for name, doc, key in (("EXPECT_KEYS", self.hotels, "hotels"),
                               ("EXPECT2_KEYS", self.places, "places")):
            match = re.search(r"const " + name + r" = \[(.*?)\];", self.index, re.S)
            self.assertIsNotNone(match, name + " is not a literal in index.html")
            listed = re.findall(r"'([^']+)'", match.group(1))
            self.assertEqual(listed, sorted(listed), name + " is not sorted")
            for rec in doc[key]:
                self.assertEqual(sorted(rec.keys()), listed, rec.get("name"))

    def test_the_client_closed_lists_are_the_delivered_codes(self):
        """S1: allow-listed codes — the client refuses a location nobody named."""
        codes = {"quarter": set(), "district": set(), "locality": set()}
        for doc, key in ((self.hotels, "hotels"), (self.places, "places")):
            for rec in doc[key]:
                for field in codes:
                    if rec[field]:
                        codes[field].add(rec[field]["code"])
        # Three sides, no fourth copy: the client's literal, the delivered
        # codes and the closed list the reference gates on.
        require_expectations(self)
        signed_codes = set(EXP["delivery"]["district_codes"])
        self.assertEqual(self.js_list("DISTRICT_CODES"), signed_codes)
        self.assertEqual(codes["district"], signed_codes)
        self.assertEqual(set(REF.DISTRICT_CODES), signed_codes)
        for field, name in (("quarter", "QUARTER_CODES"), ("locality", "LOCALITY_CODES")):
            listed = self.js_list(name)
            # the client's list is the DICTIONARY's list, and every delivered code
            # is in it: a code the dictionary does not name could never be searched.
            self.assertEqual(listed, set(self.cats["locations"][field]), name)
            self.assertEqual(codes[field] - listed, set(), name)

    def test_the_client_pins_the_dictionary_bundle_sha(self):
        """S2: the ordinals of `legacy_by_row` are pinned on the client too."""
        match = re.search(r"const LEGACY_BUNDLE_SHA = \{(.*?)\};", self.index, re.S)
        self.assertIsNotNone(match, "LEGACY_BUNDLE_SHA is not a literal in index.html")
        pinned = dict(re.findall(r"(\w+):\s*'([0-9a-f]{64})'", match.group(1)))
        self.assertEqual(pinned, self.cats["_meta"]["legacy_bundle_sha"])

    def test_the_district_fallback_is_load_bearing(self):
        """Runs and fails: inverted in place, the two schools Petar named vanish.

        `dph` empty = „the district answers for nobody“. „училище младост“ falls
        back to the two schools that carry the quarter itself, and СУ „Гео Милев“
        — the row that started this lot — is not among them.
        """
        require_expectations(self)
        want = claim("district_fallback")
        rows, branch = REF.search(want["q"])
        self.assertEqual((branch, len(rows)), (want["with"]["branch"], want["with"]["n"]))
        self.assertEqual([r.name.strip() for r in rows], want["with"]["rows"])
        saved = [(r, r.dph) for r in REF.RECS]
        try:
            for rec, _ in saved:
                rec.dph = set()
            without, _branch = REF.search(want["q"])
        finally:
            for rec, dph in saved:
                rec.dph = dph
        self.assertEqual([r.name.strip() for r in without], want["without"]["rows"])
        self.assertLess(len(without), len(rows))
        self.assertEqual(len(REF.search(want["q"])[0]), want["with"]["n"])

    def test_the_old_zone_words_are_load_bearing(self):
        """RED until Petar signs the manifest — by design (F12-в).

        The expectation used to be typed here: two rows for „училище възраждане“,
        the second one reached through the OLD zone word of ОУ „Свети Иван
        Рилски“. P7 rebuilt `legacy_by_row` (209 rows → 18) and the second row is
        gone, so the number in the code and the number in the delivery disagree —
        and a test that answers such a disagreement by rewriting itself is not a
        gate. The expectation now comes from the manifest Petar signs; while the
        manifest is unsigned this test FAILS and says why.

        The load-bearing half stays whatever the expectation is: with the old
        words switched off the engine must answer with strictly fewer rows, or
        `gph` carries nothing and the whole mechanism is dead code.
        """
        require_expectations(self)
        want = claim("old_zone_words")
        expected = want["with"]["rows"]
        rows, _ = REF.search(want["q"])
        self.assertEqual([r.name.strip() for r in rows], expected)
        saved = [(r, r.gph) for r in REF.RECS]
        try:
            for rec, _ in saved:
                rec.gph = set()
            without, _ = REF.search(want["q"])
        finally:
            for rec, gph in saved:
                rec.gph = gph
        self.assertEqual([r.name.strip() for r in without], want["without"]["rows"])
        self.assertLessEqual(len(without), len(rows))
        self.assertEqual(len(REF.search(want["q"])[0]), len(expected))

    def test_the_reference_is_not_frozen_and_the_candidate_bucket_is_pending(self):
        """§3з: the manifest is signed BEFORE anything is frozen.

        The tracked artefact must still carry exactly the six buckets of лот Б —
        a seventh here would mean the reference was re-frozen without a signature.
        """
        require_expectations(self)
        current = json.loads(ROWS.read_text(encoding="utf-8"))
        # WHETHER the pending bucket is in the artefact is the state of the
        # delivery — the signature says it, this file does not.
        self.assertEqual(set(current) - {"_meta"}, set(EXP["artefact"]["buckets"]))
        self.assertEqual(REF.PENDING_BUCKET in current,
                         REF.PENDING_BUCKET in EXP["artefact"]["buckets"])
        self.assertNotIn(REF.PENDING_BUCKET, REF_BUCKETS)
        # …and the drift gate itself still discriminates: a bucket nobody named
        # is refused, and it is allowed only when it is passed as `pending`.
        gained = dict((b, []) for b in REF_BUCKETS)
        gained[REF.PENDING_BUCKET] = []
        self.assertEqual(REF.bucket_drift(gained), [u"нов " + REF.PENDING_BUCKET])
        self.assertEqual(REF.bucket_drift(gained, pending=(REF.PENDING_BUCKET,)), [])


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
        require_expectations(self)
        for name in ("lot1_data", "lot1v_a", "lot1v_b"):
            block = anchor_block(name)
            doc = frozen_rows(block["commit"])
            self.assertEqual(set(doc.keys()) - {"_meta"}, set(block["buckets"]),
                             block["commit"])
            self.assertEqual(sum(len(doc[b]) for b in block["buckets"]),
                             block["queries"], block["commit"])

    def test_no_commit_hash_in_this_file_is_off_the_list(self):
        """The scan that keeps the list from going stale: every 7-hex word in this
        file is either an anchor or one of the pre-rebase hashes it replaced. A
        hash pasted into a docstring tomorrow is red until it is named here."""
        text = pathlib.Path(__file__).read_text(encoding="utf-8")
        found = set(re.findall(r"(?<![0-9a-zA-Z_])[0-9a-f]{7}(?![0-9a-zA-Z_])", text))
        # After A.2-4 this file carries NO hash of its own: the anchors are read
        # from the signed body. A hash pasted into a docstring tomorrow is red
        # until it is named there.
        self.assertEqual(found - (set(ANCHORS) | set(REBASED_AWAY)), set())


class M7GateTest(unittest.TestCase):
    """Амандамент №3 т. 4 и т. 6 — the М7 rule, gated in the suite.

    Until now the rule lived in `scratch/places_search/m7_significance_gate.py`
    and nothing in the suite could see it break. Three claims, all of them able
    to go red: a type prefix („к.к.“ → „к“) is not a place, a place a human
    types still answers through the branch, and with the dictionary gone the
    branch does not fire at all (fail-closed).
    """

    def test_the_gate_is_green(self):
        failures = REF.check_m7_gate()
        self.assertEqual(failures, [], "\n".join(failures))

    def test_the_engine_reproduces_the_trigger_list(self):
        """The signed `m7_trigger_tokens.json`, token by token — the file is the
        list Petar is asked to sign, so the engine has to still answer it."""
        path = REPO / "scratch" / "places_search" / "m7_trigger_tokens.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        tokens = doc["tokens"]
        self.assertEqual(len(tokens), doc["_meta"]["measured"]["tokens"])
        triggering = 0
        for entry in tokens:
            rows, branch = REF.search(entry["token"])[:2]
            self.assertEqual(branch, entry["branch"], entry["token"])
            self.assertEqual(len(rows), entry["rows_answered"], entry["token"])
            self.assertEqual(branch == "M7-bare-location", entry["triggers"],
                             entry["token"])
            triggering += 1 if entry["triggers"] else 0
        self.assertEqual(triggering, doc["_meta"]["measured"]["trigger_today"])
        self.assertEqual(sorted(e["token"] for e in tokens),
                         sorted(set(REF.m7_queries()) & set(e["token"] for e in tokens)))

    def test_without_a_dictionary_the_branch_does_not_fire(self):
        """Амандамент №3 т. 6, inverted in place: an EMPTY generic-word set means
        the dictionary did not load, and a branch that keeps answering then is a
        branch that invented its own significance rule."""
        place = REF.M7_PLACES[0]
        self.assertEqual(REF.search(place)[1], "M7-bare-location")
        saved = set(REF.GENERIC_TOKENS)
        try:
            REF.GENERIC_TOKENS.clear()
            self.assertNotEqual(REF.search(place)[1], "M7-bare-location")
        finally:
            REF.GENERIC_TOKENS.update(saved)
        self.assertEqual(REF.search(place)[1], "M7-bare-location")

    def test_the_client_asks_the_same_significance_question(self):
        """Амандамент №3 т. 5 и т. 6 on the client: `sigTokens` is
        `isSignificantToken`, and the М7 branch refuses to fire on an empty
        GENERIC_WORDS. One rule, one place, on both sides."""
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("const sigTokens = (s) => placeTokens(s).filter(isSignificantToken)",
                      html)
        self.assertIn("GENERIC_WORDS.size", html)


class ReleaseGateSignatureTest(unittest.TestCase):
    """ПЛАН v2 §A.2: „фикстура «неподписан манифест → BLOCKED» е тест“.

    The suite compares the engine with the TRACKED answers; whether Petar has
    SIGNED them is the release gate's question. This is the fixture that proves
    the gate asks it — and that the answer today is „not yet“, out loud, in the
    place the plan put it (проверка 6 of run_gates, the pre-push hook).
    """

    def test_the_signature_is_compared_exactly(self):
        from gates import coverage
        self.assertTrue(coverage.is_signed_by_petar(SIGNER))
        for impostor in ("pending — Петър", "Петърчо Иванов",
                         "Петър — pending, НЕ подписвам", None, ""):
            self.assertFalse(coverage.is_signed_by_petar(impostor), repr(impostor))

    def test_an_unsigned_artefact_blocks_the_release(self):
        """The real gate, on the real repository, right now."""
        from gates import coverage, release
        result = release.run()
        signed = coverage.is_signed_by_petar(EXP_SIGNATURE)
        if signed:
            # After Petar signs AND the queue covers every delta the gate is
            # green; before that it must name this artefact and block.
            self.assertNotIn(str(EXPECTATIONS.relative_to(REPO)).replace("\\", "/"),
                             " ".join(result["blocked"]))
        else:
            self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
            self.assertTrue(
                any("expectations.json" in line and "signed_by" in line
                    for line in result["blocked"]),
                result["blocked"])

    def test_the_gate_counter_counts_questions_not_complaints(self):
        """Амандамент №3 т. 7: the лот 1в-В counter printed „-3/10“ because it
        counted COMPLAINTS, and complaints about queries outside the gate at
        that. One query that fails on three fields is one question."""
        gate = u"lot1v_v"
        questions = [q for _cls, q, _why in REF.GATE_QUERIES[gate]]
        green, asked, other = REF.gate_score(gate, [])
        self.assertEqual((green, asked, other), (len(questions), len(questions), 0))
        three_complaints = ["gain `%s`: branch X" % questions[0],
                            "gain `%s`: n = 1" % questions[0],
                            "gain `%s`: редовете" % questions[0]]
        self.assertEqual(REF.gate_score(gate, three_complaints),
                         (len(questions) - 1, len(questions), 0))
        outside = ["колизия улица↔име/зона: `роза` дава друго"] * 4
        green, asked, other = REF.gate_score(gate, outside)
        self.assertEqual((green, asked, other), (len(questions), len(questions), 4))
        self.assertGreaterEqual(green, 0)


class RefusalSurvivesTheFreezeTest(unittest.TestCase):
    """Амандамент №5 т. 1–2 и №6 т. 2: what a freeze may not erase, what a pen
    may not write, and why the ORDER of the queue file does not vote.

    The freeze makes the reference equal to the candidate, so a delta Petar
    answered „не“ disappears from the comparison the moment it is frozen — the
    exact move the row forbade. `gates.release.refusal_survivors` reads the
    refusals the freeze wrote down and blocks on them afterwards; it is a pure
    function over two documents, so it is gated here, without a repository.

    The second half is the pen: `gates.sign.apply_signature` COMPUTES the signed
    body and writes nothing, so a refusal on a later row cannot leave an earlier
    artefact already changed — and `gates.sign.refusal_scope_complaint` refuses
    to write a „не“ that covers a whole bucket instead of a named query.
    """

    def rows(self, decision):
        return [self.row("R5", decision, ["gate_lot1/*"])]

    def row(self, row_id, decision, covers):
        return {"id": row_id, "decision": decision, "covers": list(covers),
                "artefact": "expectations", "date": "2026-09-05", "digest": "",
                "title": "", "ask": ""}

    def recorded(self):
        return {"_meta": {"refused": [{"bucket": "gate_lot1", "q": "градина",
                                       "row": "R5", "why": ["друг етикет"]}]}}

    def test_a_recorded_refusal_blocks_even_with_no_deltas_left(self):
        from gates import release
        complaints = release.refusal_survivors(self.recorded(), self.rows(release.NO))
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIn("R5", complaints[0])
        self.assertIn("gate_lot1/градина", complaints[0])

    def test_a_body_with_no_refusals_is_silent(self):
        from gates import release
        for doc in ({}, {"_meta": {}}, {"_meta": {"refused": []}}):
            self.assertEqual(release.refusal_survivors(doc, self.rows(release.NO)), [])

    def test_a_refusal_cannot_be_lifted_by_re_deciding_the_row(self):
        """„не“ is terminal: a row that came back as „да“ came back by hand."""
        from gates import release
        for decision in (release.YES, release.PENDING, ""):
            complaints = release.refusal_survivors(self.recorded(), self.rows(decision))
            self.assertEqual(len(complaints), 1, (decision, complaints))
        complaints = release.refusal_survivors(self.recorded(), [])
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIn("няма в опашката", complaints[0])

    def test_the_queue_row_may_carry_a_body_digest(self):
        """Проверка 7 accepts a digest Petar recorded; the parser must read it."""
        from gates import release
        queue = pathlib.Path(self.temp_queue())
        row = release.parse_queue(queue)[0]
        self.assertEqual(row["id"], "R5")
        self.assertEqual(row["digest"], "a" * 64)
        self.assertEqual(row["covers"], ["gate_lot1/*"])

    def temp_queue(self):
        """A queue fixture in a directory of its own, removed with the test.

        Амандамент №6 т. 5: it used to be one fixed name in the system temp, so
        two checkouts running the suite at the same time wrote over each other's
        fixture and the failure read as a parser bug."""
        import tempfile
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        path = pathlib.Path(holder.name) / "ЗА_ПОДПИС_фикстура.md"
        path.write_text("## R5 · фикстура\n"
                        "- **id:** R5\n"
                        "- **решение:** не\n"
                        "- **дата:** 2026-09-05\n"
                        "- **артефакт:** expectations\n"
                        "- **покрива:** gate_lot1/*\n"
                        "- **дайджест:** %s\n" % ("a" * 64),
                        encoding="utf-8", newline="\n")
        return str(path)

    # ---------------- амандамент №6 т. 2: the file order does not vote --------

    def refusal_and_class_rows(self):
        """The two rows of the defect: a „не“ by name and a class „да“ over the
        same bucket. Read in file order, whichever of them comes first decides —
        which is how a terminal refusal was silenced by an earlier allowance."""
        return (self.row("R9", u"не", [u"gate_lot1/градина"]),
                self.row("R1", u"да", ["gate_lot1/*"]))

    def test_a_refusal_wins_over_a_class_allowance_in_both_orders(self):
        from gates import release
        refusal, allowance = self.refusal_and_class_rows()
        for rows in ([refusal, allowance], [allowance, refusal]):
            decision, row, matched = release.decide_delta(rows, "gate_lot1", u"градина")
            order = [r["id"] for r in rows]
            self.assertEqual(decision, release.NO, order)
            self.assertEqual(row["id"], "R9", order)
            self.assertEqual(sorted(r["id"] for r in matched), ["R1", "R9"], order)

    def test_the_more_specific_row_is_the_one_that_speaks(self):
        """Two „да“ over the same delta: the named query, not the whole bucket."""
        from gates import release
        exact = self.row("R7", u"да", [u"gate_lot1/градина"])
        wide = self.row("R1", u"да", ["gate_lot1/*"])
        for rows in ([exact, wide], [wide, exact]):
            decision, row, matched = release.decide_delta(rows, "gate_lot1", u"градина")
            self.assertEqual(decision, release.YES)
            self.assertEqual(row["id"], "R7", [r["id"] for r in rows])
            self.assertEqual(len(matched), 2)

    def test_a_class_row_still_answers_the_queries_nobody_named(self):
        from gates import release
        refusal, allowance = self.refusal_and_class_rows()
        decision, row, matched = release.decide_delta(
            [refusal, allowance], "gate_lot1", u"детска ясла")
        self.assertEqual(decision, release.YES)
        self.assertEqual(row["id"], "R1")
        self.assertEqual([r["id"] for r in matched], ["R1"])

    def test_a_delta_no_row_touches_is_uncovered_and_nothing_is_used(self):
        from gates import release
        refusal, allowance = self.refusal_and_class_rows()
        decision, row, matched = release.decide_delta(
            [refusal, allowance], "gate_p7", u"градина")
        self.assertEqual((decision, row, matched), (None, None, []))

    def test_a_pending_row_covers_nothing_but_counts_as_touched(self):
        """`pending` is „not answered yet“, never „allowed“ — and the row is
        still the one that matched, so it is not read as a stale permission."""
        from gates import release
        rows = [self.row("R4", release.PENDING, ["gate_lot1/*"])]
        decision, row, matched = release.decide_delta(rows, "gate_lot1", u"градина")
        self.assertEqual((decision, row), (None, None))
        self.assertEqual([r["id"] for r in matched], ["R4"])

    def test_the_pen_refuses_a_refusal_written_over_a_whole_bucket(self):
        from gates import sign
        complaint = sign.refusal_scope_complaint(self.row("R9", u"не", ["gate_lot1/*"]))
        self.assertIsNotNone(complaint)
        self.assertIn("R9", complaint)
        self.assertIn("gate_lot1/*", complaint)
        named = self.row("R9", u"не", [u"gate_lot1/градина", u"gate_p7/градина"])
        self.assertIsNone(sign.refusal_scope_complaint(named))
        self.assertIsNone(sign.refusal_scope_complaint(self.row("Q7", u"не", [])))

    def test_the_pen_and_the_gate_read_the_same_wildcard(self):
        from gates import release
        self.assertEqual(release.wildcard_covers(["gate_lot1/*", u"gate_p7/градина",
                                                  "baseline"]),
                         ["gate_lot1/*"])

    # ------------- амандамент №7 т. 1: a refusal that covers nothing ---------

    def test_a_refusal_that_reaches_nothing_is_blocked(self):
        """The one-letter hole: `gate_lot1/Градината` for `gate_lot1/градина`.

        The row matched no delta, so it said nothing, so the gate went green
        over the very difference it refused — and the next freeze carried that
        difference into the reference. A „да“ that covers nothing has been
        blocked as a stale permission from the first day; this is its twin."""
        from gates import release
        typo = self.row("R9", u"не", [u"gate_lot1/Градината"])
        complaints = release.refusals_that_cover_nothing([typo], {}, {})
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIn("R9", complaints[0])
        self.assertIn(u"gate_lot1/Градината", complaints[0])
        self.assertIn(u"не съществува", complaints[0])
        self.assertIn(release.REFUSAL_UNREACHED, complaints[0])
        # A refusal that answers a LIVE delta, and one that answers a difference
        # against the queue's reference, are both doing their job — and both are
        # counted BY PATTERN (амандамент №8 т. 3), never by row.
        hit = {"R9": {u"gate_lot1/Градината"}}
        self.assertEqual(release.refusals_that_cover_nothing([typo], hit, {}), [])
        self.assertEqual(release.refusals_that_cover_nothing([typo], {}, hit), [])
        # No comparison, no accusation: `reached is None` means the anchor could
        # not be read, and that complaint is already on the table.
        self.assertEqual(release.refusals_that_cover_nothing([typo], {}, None), [])
        # And this rule speaks only about „не“ — the stale „да“ has its own.
        allowance = self.row("R1", u"да", [u"gate_lot1/Градината"])
        self.assertEqual(release.refusals_that_cover_nothing([allowance], {}, {}), [])

    def test_a_refusal_is_measured_per_pattern_over_the_raw_covers(self):
        """Амандамент №8 т. 1 и т. 3 — the two ways past the row-level check.

        (а) `gate_lot1градина` has no slash, so `delta_patterns` dropped it and
        a row whose only content was that word was skipped as „not about
        deltas“ — the queue refused, the gate said nothing at all;
        (б) a row that refuses three queries and misspells one of them reached
        something, so the whole row counted as doing its job while the third
        refusal was as mute as the row in (а).
        """
        from gates import release
        # (а) the malformed pattern is NAMED, not filtered away.
        malformed = self.row("R9", u"не", [u"gate_lot1градина"])
        complaints = release.refusals_that_cover_nothing([malformed], {}, {})
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIn(u"gate_lot1градина", complaints[0])
        self.assertIn(release.REFUSAL_MALFORMED, complaints[0])
        # …and it stays named even when the row reached something with it,
        # because a pattern a machine cannot read as a query never reaches.
        self.assertEqual(len(release.refusals_that_cover_nothing(
            [malformed], {"R9": {u"gate_lot1градина"}}, {})), 1)
        # (б) one misspelling among two: the good one is silent, the bad one is
        # named, and the row is not excused by the half that works.
        mixed = self.row("R9", u"не", [u"gate_lot1/градина", u"gate_lot1/Градината"])
        complaints = release.refusals_that_cover_nothing(
            [mixed], {"R9": {u"gate_lot1/градина"}}, {})
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIn(u"gate_lot1/Градината", complaints[0])
        self.assertNotIn(u"gate_lot1/градина —", complaints[0])
        # An empty `покрива` FIELD under a „не“ refuses nothing and says so —
        # the row is about deltas (it has the field), and it names none.
        blank = dict(self.row("Q7", u"не", []), has_covers=True)
        empty = release.refusals_that_cover_nothing([blank], {}, {})
        self.assertEqual(len(empty), 1, empty)
        self.assertIn("Q7", empty[0])
        self.assertIn(release.REFUSAL_EMPTY, empty[0])
        # A word that names an artefact instead of a query is malformed as a
        # refusal — амандамент №8 т. 1 makes „нула валидни шаблона“ a block.
        note = release.refusals_that_cover_nothing(
            [self.row("Q7", u"не", ["baseline"])], {}, {})
        self.assertEqual(len(note), 1, note)
        self.assertIn("baseline", note[0])
        self.assertIn(release.REFUSAL_MALFORMED, note[0])

    def test_the_patterns_that_covered_a_delta_are_named_one_by_one(self):
        """`patterns_that_cover` is the per-pattern bookkeeping of the gate."""
        from gates import release
        row = self.row("R9", u"не", [u"gate_lot1/градина", u"gate_lot1/Градината",
                                     u"gate_lot1градина"])
        deltas = [("gate_lot1", u"градина"), ("gate_p7", u"хотел приморски")]
        self.assertEqual(release.patterns_that_cover(row, deltas),
                         set([u"gate_lot1/градина"]))
        wide = self.row("R1", u"да", ["gate_lot1/*"])
        self.assertEqual(release.patterns_that_cover(wide, deltas), set(["gate_lot1/*"]))
        self.assertEqual(release.patterns_that_cover(wide, []), set())

    def test_the_pen_refuses_a_refusal_whose_query_does_not_exist(self):
        """Амандамент №7 т. 1, the other end: the typo is caught by the hand.

        `gates.sign` asks `gates.release` for the deltas of the moment and will
        not write a „не“ that names none of them — so the answer comes back
        while Petar is still at the keyboard, not one freeze later."""
        from gates import sign
        deltas = set([("gate_lot1", u"градина"), ("gate_p7", u"хотел приморски")])
        typo = self.row("R9", u"не", [u"gate_lot1/Градината"])
        complaint = sign.refusal_target_complaint(typo, deltas)
        self.assertIsNotNone(complaint)
        self.assertIn("R9", complaint)
        self.assertIn(u"gate_lot1/Градината", complaint)
        named = self.row("R9", u"не", [u"gate_lot1/градина"])
        self.assertIsNone(sign.refusal_target_complaint(named, deltas))
        # One misspelling among two is still a misspelling: the check is per
        # pattern, so a true refusal cannot carry a second one that is not — and
        # the complaint names the misspelling, not the pattern that works.
        mixed = self.row("R9", u"не", [u"gate_lot1/градина", u"gate_lot1/Градината"])
        complaint = sign.refusal_target_complaint(mixed, deltas)
        self.assertIsNotNone(complaint)
        self.assertIn(u"gate_lot1/Градината", complaint)
        self.assertNotIn(u"gate_lot1/градина (", complaint)

    def test_the_pen_measures_the_raw_covers_of_a_refusal(self):
        """Амандамент №8 т. 1: the pen asks the same question the gate does.

        `gate_lot1градина` never reached the measurement — `delta_patterns`
        dropped it — so the pen wrote the „не“ and the gate then skipped the row
        as „not about deltas“. Both halves of the barrier were open at once."""
        from gates import release, sign
        deltas = set([("gate_lot1", u"градина"), ("gate_p7", u"хотел приморски")])
        malformed = sign.refusal_target_complaint(
            self.row("R9", u"не", [u"gate_lot1градина"]), deltas)
        self.assertIsNotNone(malformed)
        self.assertIn(u"gate_lot1градина", malformed)
        self.assertIn(release.REFUSAL_MALFORMED, malformed)
        # A „не“ with nothing at all in `покрива` refuses nothing.
        empty = sign.refusal_target_complaint(self.row("Q7", u"не", []), deltas)
        self.assertIsNotNone(empty)
        self.assertIn("Q7", empty)
        self.assertIn(release.REFUSAL_EMPTY, empty)
        # …and a word that names an artefact is not a query either.
        note = sign.refusal_target_complaint(self.row("Q7", u"не", ["baseline"]), deltas)
        self.assertIsNotNone(note)
        self.assertIn("baseline", note)

    # ------------- амандамент №9: the parser, the classes, the body ----------

    def test_the_parser_reads_only_what_the_reader_sees(self):
        """Амандамент №9 т. 2: a row inside a comment or a fence is not a row.

        A „да“ written between `<!--` and `-->` is invisible in every markdown
        viewer and in the diff Petar signs off on, and it was authoritative for
        the gate that read the file — one queue, two readings, and the machine's
        was the one nobody could see. It is skipped now, and `hidden_decisions`
        makes the attempt loud instead of silently shorter."""
        from gates import release
        text = (u"## R1 · видим\n"
                u"- **id:** R1\n"
                u"- **решение:** pending\n"
                u"- **покрива:** gate_lot1/градина\n"
                u"\n"
                u"<!--\n"
                u"## R99 · скрит\n"
                u"- **id:** R99\n"
                u"- **решение:** да\n"
                u"- **покрива:** gate_lot1/*\n"
                u"-->\n"
                u"\n"
                u"```\n"
                u"## R98 · в ограда\n"
                u"- **решение:** да\n"
                u"```\n")
        rows = release.parse_queue_text(text)
        self.assertEqual([row["id"] for row in rows], ["R1"])
        self.assertEqual(rows[0]["decision"], release.PENDING)
        hidden = release.hidden_decisions(text)
        self.assertEqual(len(hidden), 2, hidden)
        self.assertEqual([n for n, _ in hidden], [9, 15])
        # A one-line comment closes itself: the line after it is visible again.
        self.assertEqual([row["id"] for row in release.parse_queue_text(
            u"<!-- бележка -->\n## R2 · видим\n- **решение:** да\n")], ["R2"])
        self.assertEqual(release.hidden_decisions(u"<!-- бележка -->\n"), [])

    def test_the_block_of_a_row_is_its_verbatim_text(self):
        """The needle `yes_row_authorship` gives `git log -S`.

        It runs from the heading to the row's LAST FIELD — a note appended
        afterwards is not part of the row, or the next hand to touch the file
        would inherit the authorship of every row above it. A line slipped
        BETWEEN the fields does change the block, and that is the point."""
        from gates import release
        text = (u"## R1 · първи\n- **id:** R1\n- **решение:** да\n"
                u"\n<!-- дописано после -->\n"
                u"## R2 · втори\n- **id:** R2\n- **решение:** pending\n")
        rows = release.parse_queue_text(text)
        self.assertEqual(rows[0]["block"],
                         u"## R1 · първи\n- **id:** R1\n- **решение:** да")
        self.assertIn(rows[0]["block"], text)
        self.assertIn(rows[1]["block"], text)
        self.assertNotIn(u"R2", rows[0]["block"])
        # …and an inserted line inside the fields makes it a different text
        between = release.parse_queue_text(
            u"## R1 · първи\n- **id:** R1\n<!-- вмъкнато -->\n"
            u"- **решение:** да\n")[0]
        self.assertIn(u"вмъкнато", between["block"])

    def test_a_field_written_twice_is_named_by_both_readers(self):
        """Амандамент №9 т. 2: the parser keeps the last, the human reads the
        first, and the pen would rewrite both lines at once."""
        from gates import release, sign
        rows = release.parse_queue_text(
            u"## R1 · два пъти\n- **id:** R1\n- **решение:** да\n"
            u"- **решение:** не\n- **покрива:** gate_lot1/*\n"
            u"- **покрива:** gate_p7/*\n")
        self.assertEqual(rows[0]["duplicates"],
                         [release.FIELD_DECISION, release.FIELD_COVERS])
        complaint = sign.duplicate_field_complaint(rows[0])
        self.assertIsNotNone(complaint)
        self.assertIn("R1", complaint)
        self.assertIn(release.FIELD_DECISION, complaint)
        self.assertIsNone(sign.duplicate_field_complaint(
            release.parse_queue_text(u"## R1\n- **решение:** да\n")[0]))

    def test_the_row_classes_decide_who_is_asked_about_queries(self):
        """Амандамент №9 т. 5 — the cost the executor named after A.2-9.

        „не“ on Q7 („break-glass: вън“) has no `покрива` and never had: under
        амандамент №8 that was „a refusal that covers nothing“ and it held the
        whole delivery. Three classes now: a question, an artefact and a delta,
        and only the delta is measured against queries."""
        from gates import release, sign
        question = {"id": "Q7", "decision": release.NO, "covers": [], "artefact": "",
                    "date": "2026-09-05", "digest": "", "body": "", "title": "",
                    "ask": "", "has_covers": False, "has_artefact": False}
        artefact = dict(question, id="R2", artefact="baseline", has_artefact=True)
        delta = dict(question, id="R9", covers=[u"gate_lot1/градина"],
                     has_covers=True)
        blank = dict(question, id="R8", has_covers=True)
        self.assertEqual(release.row_class(question), release.CLASS_QUESTION)
        self.assertEqual(release.row_class(artefact), release.CLASS_ARTEFACT)
        self.assertEqual(release.row_class(delta), release.CLASS_DELTA)
        self.assertEqual(release.row_class(blank), release.CLASS_DELTA)
        # Neither the question nor the artefact is accused of refusing nothing.
        self.assertEqual(release.refusals_that_cover_nothing(
            [question, artefact], {}, {}), [])
        # The delta row keeps every rule of амандаменти 6–8.
        self.assertEqual(len(release.refusals_that_cover_nothing([delta], {}, {})), 1)
        self.assertEqual(len(release.refusals_that_cover_nothing([blank], {}, {})), 1)
        # …and the pen asks the query questions of a delta row only.
        self.assertIsNone(sign.refusal_scope_complaint(question))
        self.assertIsNotNone(sign.refusal_target_complaint(delta, set()))

    def test_the_unconditional_refusal_reasons_survive_a_missing_anchor(self):
        """Амандамент №9 т. 3: `reached is None` silenced the whole function.

        „this pattern reached nothing“ cannot be said without the comparison —
        but „this is not a query at all“ and „there is no pattern“ are
        properties of the row, and a row that is malformed on its face is named
        with or without an anchor."""
        from gates import release
        malformed = self.row("R9", u"не", [u"gate_lot1градина"])
        empty = dict(self.row("R8", u"не", []), has_covers=True)
        typo = self.row("R7", u"не", [u"gate_lot1/Градината"])
        complaints = release.refusals_that_cover_nothing(
            [malformed, empty, typo], {}, None)
        self.assertEqual(len(complaints), 2, complaints)
        self.assertIn(release.REFUSAL_MALFORMED, complaints[0])
        self.assertIn(release.REFUSAL_EMPTY, complaints[1])
        self.assertFalse([c for c in complaints if release.REFUSAL_UNREACHED in c])

    def test_the_body_digest_ignores_the_signature_and_nothing_else(self):
        """Амандамент №9 т. 7: one number before and after the act of signing.

        The pen computes it while it prepares the buffer and the gate recomputes
        it from the blob afterwards, so the field the pen itself writes has to
        fall out of the sum — and every other byte of meaning has to stay in."""
        from gates import release
        pending = {"_meta": {"signed_by": "pending — Петър"}, "p7": {"tokens": 2}}
        signed = {"_meta": {"signed_by": SIGNER}, "p7": {"tokens": 2}}
        moved = {"_meta": {"signed_by": SIGNER}, "p7": {"tokens": 3}}
        one = release.body_digest(json.dumps(pending, ensure_ascii=False))
        self.assertEqual(one, release.body_digest(json.dumps(signed, indent=1)))
        self.assertNotEqual(one, release.body_digest(json.dumps(moved)))
        # bytes and text are the same question
        self.assertEqual(one, release.body_digest(
            json.dumps(signed, ensure_ascii=False).encode("utf-8")))
        # a top-level signature is dropped as well as one inside `_meta`
        self.assertEqual(release.body_digest(json.dumps({"signed_by": SIGNER, "n": 1})),
                         release.body_digest(json.dumps({"n": 1})))

    def test_the_pen_writes_the_body_digest_onto_the_row(self):
        """`decide_row` puts the number where the gate looks for it."""
        from gates import release, sign
        lines = (u"## R1 · фикстура\n- **id:** R1\n- **решение:** pending\n"
                 u"- **дата:** —\n- **артефакт:** expectations\n"
                 u"## R2 · друг\n- **решение:** pending\n- **дата:** —\n"
                 ).splitlines()
        row = release.parse_queue_text(u"\n".join(lines))[0]
        self.assertEqual(sign.decide_row(lines, row, release.YES, "2026-09-05",
                                         "b" * 64), 2)
        text = u"\n".join(lines)
        self.assertIn(u"- **%s:** %s" % (release.FIELD_BODY, "b" * 64), text)
        # …inside the row it belongs to, never in the next one
        self.assertLess(text.index(release.FIELD_BODY), text.index(u"## R2"))
        self.assertEqual(release.parse_queue_text(text)[0]["body"], "b" * 64)
        self.assertEqual(release.parse_queue_text(text)[1]["body"], "")
        # a row that already carries the field gets it REPLACED, not doubled
        again = release.parse_queue_text(text)[0]
        sign.decide_row(lines, again, release.YES, "2026-09-06", "c" * 64)
        self.assertEqual(u"\n".join(lines).count(release.FIELD_BODY + u":"), 1)
        self.assertEqual(release.parse_queue_text(u"\n".join(lines))[0]["body"],
                         "c" * 64)

    def test_the_dead_delta_filter_is_gone(self):
        """Амандамент №9 т. 4: `delta_patterns` had no caller left after №8."""
        from gates import release
        self.assertFalse(hasattr(release, "delta_patterns"))

    def test_the_pen_computes_the_body_and_writes_nothing(self):
        from gates import sign
        rel = "scratch/places_search/expectations.json"
        before = EXPECTATIONS.read_bytes()
        complaint, body = sign.apply_signature(rel)
        self.assertIsNone(complaint, complaint)
        self.assertEqual(before, EXPECTATIONS.read_bytes(),
                         "apply_signature е писала по файла — писането е в един блок накрая")
        if body is not None:
            self.assertIn('"%s"' % SIGNER, body)
            self.assertNotIn('"pending — %s"' % SIGNER, body)


class FreezeAndAnchorTest(unittest.TestCase):
    """Амандамент №7 т. 4: the three rules that were only ever proved by hand.

    Each of them had been measured once, in an isolated clone, and then lived on
    as a sentence in a report — which is a claim, not a gate. They are checked
    here instead:

      (а) a freeze on a verdict that is not green exits 1 and writes not one
          byte (амандамент №6 т. 1);
      (б) проверка 7 refuses a digest that reaches it through a queue an agent
          committed, and no line of the table then says „Петър записа“
          (амандамент №6 т. 3);
      (в) the anchor of a refusal is the explicit `_meta.queue_reference`, so a
          redirected `_meta.base` does not vote (амандамент №6 т. 4 / №7 т. 3).

    (б) and (в) run against a repository built in a temporary directory: they
    are about git authorship, and authorship cannot be faked with a fixture.
    """

    # ------------------------------------------------------------ helpers ----

    def temp_repo(self):
        """A git repository of its own, with the two identities of the plan."""
        import shutil
        import tempfile
        root = pathlib.Path(tempfile.mkdtemp(prefix="fv_gate_"))
        # `git` marks its object files read-only, so a plain rmtree can fail on
        # Windows — the fixture must not be able to break the suite.
        self.addCleanup(shutil.rmtree, str(root), True)
        self.git(root, "init", "-q")
        self.git(root, "config", "core.autocrlf", "false")
        return root

    def git(self, root, *args):
        out = subprocess.run(["git", "-C", str(root)] + list(args),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(out.returncode, 0,
                         "git %s: %s" % (" ".join(args),
                                         out.stderr.decode("utf-8", "replace")))
        return out.stdout.decode("utf-8", "replace")

    def commit_as(self, root, who, message):
        """One commit, authored by a name — the whole point of проверка 7."""
        self.git(root, "add", "-A")
        self.git(root, "-c", "user.name=%s" % who,
                 "-c", "user.email=%s@local" % who.split()[0].lower(),
                 "commit", "-q", "-m", message)
        return self.git(root, "rev-parse", "HEAD").strip()

    def use_repo(self, root, **fields):
        """Point the two gate modules at a repository of ours, and back again."""
        from gates import release, run_gates
        for module in (release, run_gates):
            old = module.REPO_ROOT
            module.REPO_ROOT = root
            self.addCleanup(setattr, module, "REPO_ROOT", old)
        for name, value in fields.items():
            old = getattr(release, name)
            setattr(release, name, value)
            self.addCleanup(setattr, release, name, old)

    def write(self, path, text):
        path.write_text(text, encoding="utf-8", newline="\n")

    def body_of(self, doc):
        return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"

    # ------------------------------------------- (а) the freeze and the bytes

    def test_a_verdict_that_is_not_green_blocks_the_freeze(self):
        """The verdict is read as a VERDICT, not as two of the lists behind it.

        A release blocked because a signed artefact was edited in the worktree
        has an empty `uncovered` and an empty `refused`; the freeze that read
        only those two lists went ahead with exit 0."""
        blocked = {"exit_code": 6, "verdict": u"BLOCKED: 2",
                   "blocked": [u"gates/baseline/MANIFEST.json: работното дърво "
                               u"носи друго тяло", u"ред R9 е ОТКАЗАН"],
                   "uncovered": [], "refused": []}
        blockers = REF.freeze_blockers(blocked)
        self.assertTrue(blockers)
        self.assertIn(u"САМО при зелена присъда", blockers[0])
        for line in blocked["blocked"]:
            self.assertIn(u"release: %s" % line, blockers)
        # A gate that did not answer at all is a gate that said no.
        self.assertTrue(REF.freeze_blockers(None))
        # …and a green verdict takes nothing away from the freeze.
        self.assertEqual(REF.freeze_blockers(
            {"exit_code": 0, "verdict": u"зелено", "blocked": []}), [])

    def test_a_blocked_freeze_writes_not_one_byte(self):
        """„ЗАМРАЗЯВАНЕТО НЕ Е ИЗВЪРШЕНО“ has to mean zero changed files."""
        import tempfile
        holder = tempfile.TemporaryDirectory()
        self.addCleanup(holder.cleanup)
        target = pathlib.Path(holder.name) / "frozen.json"

        def write_it():
            target.write_text("{}", encoding="utf-8")
            return "written"

        code, written = REF.freeze_writes([u"release-гейтът не е зелен"], [write_it])
        self.assertEqual((code, written), (1, []))
        self.assertFalse(target.exists(), u"замразяването е писало при блокер")
        # The other half of the differential: with no blocker the writes happen,
        # in order, and each of them reports itself.
        code, written = REF.freeze_writes([], [write_it])
        self.assertEqual((code, written), (0, ["written"]))
        self.assertEqual(target.read_text(encoding="utf-8"), "{}")

    # --------------------------------- (б) проверка 7 over an agent's queue --

    def test_check_7_takes_no_digest_from_a_queue_an_agent_committed(self):
        """The digest is Petar's word only where his commit put it.

        An agent rewrites the signed body AND writes the digest of its own
        result onto the queue row. The number matches the body perfectly — and
        it is worth nothing, because the newest commit on the queue is the
        agent's. The old check read the row first and blessed the body with the
        words „дайджестът, който Петър записа“ before it ever asked whose queue
        that was."""
        from gates import run_gates
        root = self.temp_repo()
        exp = root / "expectations.json"
        queue = root / "ЗА_ПОДПИС_фикстура.md"
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 1}))
        row = ("## R1 · фикстура\n- **id:** R1\n- **решение:** да\n"
               "- **дата:** 2026-09-05\n- **артефакт:** expectations\n"
               "- **покрива:** gate_lot1/*\n")
        self.write(queue, row)
        self.use_repo(root, SIGNABLE={"expectations": "expectations.json"},
                      QUEUE_DIR=".", QUEUE_GLOB="ЗА_ПОДПИС_*.md")
        self.commit_as(root, "Petar1984", "sign: R1 да")
        green = run_gates.check_signature_authorship()
        self.assertEqual(green.mark, run_gates.OK, green.lines)

        # …and now the agent rewrites the body and records its own digest.
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 2}))
        digest = hashlib.sha256(exp.read_bytes()).hexdigest()
        self.write(queue, row + "- **дайджест:** %s\n" % digest)
        self.commit_as(root, "Claude Executor", "gates: a small fix")
        check = run_gates.check_signature_authorship()
        self.assertEqual(check.mark, run_gates.BAD, check.lines)
        self.assertFalse([line for line in check.lines if u"Петър записа" in line],
                         check.lines)
        self.assertTrue([line for line in check.lines
                         if u"авторството на опашката не е потвърдено" in line],
                        check.lines)

    def test_check_7_says_who_wrote_the_digest_it_accepted(self):
        """The honest half: a digest on a queue Petar committed is accepted, and
        the words say whether HE wrote the number or merely committed the
        document that carries it (амандамент №7 т. 2)."""
        from gates import run_gates
        root = self.temp_repo()
        exp = root / "expectations.json"
        queue = root / "ЗА_ПОДПИС_фикстура.md"
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 1}))
        row = ("## R1 · фикстура\n- **id:** R1\n- **решение:** да\n"
               "- **дата:** 2026-09-05\n- **артефакт:** expectations\n"
               "- **покрива:** gate_lot1/*\n")
        self.write(queue, row)
        self.use_repo(root, SIGNABLE={"expectations": "expectations.json"},
                      QUEUE_DIR=".", QUEUE_GLOB="ЗА_ПОДПИС_*.md")
        self.commit_as(root, "Petar1984", "sign: R1 да")
        # The freeze rewrites the signed body; the agent commits it (the path
        # амандамент №6 replaced, kept here because the words about it are the
        # thing being tested).
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 2}))
        self.commit_as(root, "Claude Executor", "freeze: the bodies")
        digest = hashlib.sha256(exp.read_bytes()).hexdigest()
        self.write(queue, row + "- **дайджест:** %s\n" % digest)
        self.commit_as(root, "Petar1984", "sign: the digest of the frozen body")
        check = run_gates.check_signature_authorship()
        self.assertEqual(check.mark, run_gates.OK, check.lines)
        self.assertTrue([line for line in check.lines
                         if u"записа на опашката" in line], check.lines)

    # ------------------------------------------- (в) the anchor of a refusal --

    def test_the_queue_anchor_is_explicit_and_a_redirected_base_does_not_vote(self):
        """`_meta.base` is a commit constant of the engine; the queue is not.

        The refusal is measured against the reference the QUEUE was written
        against, and амандамент №7 т. 3 writes that down instead of deriving it:
        the derivation could be aimed by any commit that touches the signature
        string. Here the body names the signing commit explicitly while
        `_meta.base` points at an older one — and the anchor is the signing
        commit."""
        from gates import release
        root = self.temp_repo()
        rows = root / "rows.json"
        self.write(rows, self.body_of({"gate_lot1": []}))
        self.use_repo(root, REFERENCE_REL="rows.json")
        base = self.commit_as(root, "Claude Executor", "test: the лот-Б reference")
        base_digest = hashlib.sha256(rows.read_bytes()).hexdigest()
        self.write(rows, self.body_of({"gate_lot1": [{"q": u"градина"}]}))
        signing = self.commit_as(root, "Petar1984", "sign: R1 да")
        anchor = release.queue_reference_anchor()
        self.assertEqual(anchor["commit"], signing)
        doc = {"_meta": {"queue_reference": anchor,
                         "base": {"commit": base, "path": "rows.json",
                                  "sha256": base_digest}}}
        commit, path, sha, complaint = release.queue_reference(doc)
        self.assertIsNone(complaint)
        self.assertEqual((commit, path), (signing, "rows.json"))
        self.assertNotEqual(commit, base)
        self.assertEqual(sha, hashlib.sha256(rows.read_bytes()).hexdigest())

    def test_the_queue_anchor_of_a_foreign_commit_blocks(self):
        """An anchor is a claim about a hand: амандамент №7 т. 3 says whose.

        The reference a queue answers about is frozen in a commit of Petar's
        (амандамент №6), so an anchor that names anybody else's commit is a
        BLOCK with words — never a silent fallback to a commit of the engine."""
        from gates import release
        root = self.temp_repo()
        rows = root / "rows.json"
        self.write(rows, self.body_of({"gate_lot1": []}))
        self.use_repo(root, REFERENCE_REL="rows.json")
        agent = self.commit_as(root, "Claude Executor", "test: a reference")
        anchor = release.queue_reference_anchor()
        self.assertEqual(anchor["commit"], agent)
        commit, path, sha, complaint = release.queue_reference(
            {"_meta": {"queue_reference": anchor}})
        self.assertEqual((commit, path, sha), (None, None, None))
        self.assertIn("Claude Executor", complaint)
        self.assertIn(release.HUMAN_AUTHOR, complaint)
        # A body with no anchor at all is a body a refusal cannot be measured
        # against — the same block, different words, never silence.
        self.assertIsNotNone(release.queue_reference({"_meta": {}})[3])
        # …and the refusal path says so instead of guessing.
        rows_in = [{"id": "R9", "decision": release.NO, "covers": [u"gate_lot1/градина"],
                    "artefact": "expectations", "date": "2026-09-05", "digest": "",
                    "title": "", "ask": ""}]
        complaints, reached = release.refused_against_reference({"_meta": {}}, rows_in, {})
        self.assertEqual(len(complaints), 1, complaints)
        self.assertIsNone(reached)

    # ------------- амандамент №8 т. 2: whose hand wrote the digest -----------

    def test_check_7_fails_on_a_digest_an_agent_introduced(self):
        """The auditor's scenario, end to end, in a repository of its own.

        An agent rewrites the signed body; the SAME agent writes the digest of
        its own result onto Petar's queue row; then Petar makes one trivial
        commit to the queue — a typo fix, a note. The queue is now „his“ by its
        newest commit (амандамент №6 т. 3 is satisfied) and the digest matches
        the body perfectly, so the third branch of проверка 7 said „приет по
        опашка, комитната от Petar1984 ✓“ and the rewritten body went through.
        Амандамент №8 т. 2: only a digest HIS commit introduced counts, and the
        check now names the hand that actually typed the number."""
        from gates import run_gates
        root = self.temp_repo()
        exp = root / "expectations.json"
        queue = root / "ЗА_ПОДПИС_фикстура.md"
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 1}))
        row = ("## R1 · фикстура\n- **id:** R1\n- **решение:** да\n"
               "- **дата:** 2026-09-05\n- **артефакт:** expectations\n"
               "- **покрива:** gate_lot1/*\n")
        self.write(queue, row)
        self.use_repo(root, SIGNABLE={"expectations": "expectations.json"},
                      QUEUE_DIR=".", QUEUE_GLOB="ЗА_ПОДПИС_*.md")
        self.commit_as(root, "Petar1984", "sign: R1 да")

        # 1. the agent rewrites the signed body AND records its own digest.
        self.write(exp, self.body_of({"_meta": {"signed_by": SIGNER}, "n": 2}))
        digest = hashlib.sha256(exp.read_bytes()).hexdigest()
        self.write(queue, row + "- **дайджест:** %s\n" % digest)
        agent_commit = self.commit_as(root, "Claude Executor", "gates: a small fix")
        # 2. Petar touches the queue for something else entirely.
        self.write(queue, row + "- **дайджест:** %s\n\n<!-- бележка -->\n" % digest)
        self.commit_as(root, "Petar1984", "docs: a note on the queue")

        check = run_gates.check_signature_authorship()
        self.assertEqual(check.mark, run_gates.BAD, check.lines)
        named = [line for line in check.lines
                 if u"въведен в опашката от" in line and u"Claude Executor" in line]
        self.assertTrue(named, check.lines)
        self.assertIn(agent_commit[:7], named[0])
        self.assertIn(run_gates.HUMAN_AUTHOR, named[0])
        # Not one line of the table may claim this body was Petar's word.
        self.assertFalse([line for line in check.lines if u"Петър записа" in line],
                         check.lines)
        self.assertFalse([line for line in check.lines if u"приет по опашка" in line],
                         check.lines)

    # -------------- амандамент №8 т. 4: the anchor is the CARRIER ------------

    def test_the_anchor_is_the_reference_carrier_not_the_signing_commit(self):
        """Two different commits, and the anchor is the one with the bytes.

        The signing commit cannot be the anchor: it does not exist yet when
        `build_expectations` and `gates.sign` write the field. The anchor is the
        commit that CARRIES the frozen reference — амандамент №8 т. 4 — and this
        test keeps the two apart on purpose: Petar freezes and commits the
        reference, then signs in a LATER commit that does not touch it."""
        from gates import release
        root = self.temp_repo()
        rows = root / "rows.json"
        queue = root / "ЗА_ПОДПИС_фикстура.md"
        self.write(rows, self.body_of({"gate_lot1": []}))
        self.write(queue, "## R1 · фикстура\n- **id:** R1\n- **решение:** pending\n")
        self.use_repo(root, REFERENCE_REL="rows.json")
        self.commit_as(root, "Claude Executor", "test: the лот-Б reference")
        self.write(rows, self.body_of({"gate_lot1": [{"q": u"градина"}]}))
        carrier = self.commit_as(root, "Petar1984", "freeze: the bodies")
        # The signature lands afterwards, in a commit of its own.
        self.write(queue, "## R1 · фикстура\n- **id:** R1\n- **решение:** да\n")
        signing = self.commit_as(root, "Petar1984", "sign: R1 да")
        self.assertNotEqual(carrier, signing)
        anchor = release.queue_reference_anchor()
        self.assertEqual(anchor["commit"], carrier)
        self.assertEqual(anchor["sha256"],
                         hashlib.sha256(rows.read_bytes()).hexdigest())
        commit, path, sha, complaint = release.queue_reference(
            {"_meta": {"queue_reference": anchor}})
        self.assertIsNone(complaint)
        self.assertEqual((commit, path), (carrier, "rows.json"))

    # ---- амандамент №9: the queue is the blob and the rows have hands -------

    ENGINE_STUB = (
        "# A stand-in for recall_sweep.py. `gates.release` imports the engine to\n"
        "# get the candidate; a gate test has to be able to fail without three\n"
        "# thousand lines of search behind it.\n"
        "import json\n"
        "\n"
        "ROWS = {\"gate_lot1\": [{\"q\": \"garden\", \"branch\": \"A3\", \"hasKey\": True,\n"
        "                       \"n\": 1, \"rows\": [{\"name\": \"now\", \"zone\": \"z\",\n"
        "                                          \"kind\": \"place\"}]}]}\n"
        "\n"
        "\n"
        "def check_manifest_anchors(paths):\n"
        "    return []\n"
        "\n"
        "\n"
        "def reference_rows():\n"
        "    return json.loads(json.dumps(ROWS))\n"
        "\n"
        "\n"
        "def dump_rows(doc):\n"
        "    return json.dumps(doc, ensure_ascii=False, sort_keys=True)\n"
    )

    QUEUE_ROW = (u"## R1 · фикстура\n"
                 u"- **id:** R1\n"
                 u"- **питане:** делтата на доставката\n"
                 u"- **решение:** да\n"
                 u"- **дата:** 2026-09-05\n"
                 u"- **артефакт:** expectations\n"
                 u"- **покрива:** gate_lot1/*\n"
                 u"- **тяло:** <тяло>\n")

    def release_repo(self, queue_text, author="Petar1984"):
        """A repository `gates.release` runs GREEN on, end to end.

        Everything the gate binds is here and nothing else is: one signed
        artefact, one frozen reference, one engine, one queue — and exactly one
        delta between the reference and the engine, so the queue row has to do
        real work for the verdict to be green. Without a green baseline a
        „blocked“ proves nothing: every one of these tests is a differential.
        """
        from gates import release
        root = self.temp_repo()
        self.write(root / "index.html", "<html></html>\n")
        self.write(root / "engine.py", self.ENGINE_STUB)
        self.write(root / "rows.json", self.body_of(
            {"gate_lot1": [{"q": "garden", "branch": "A3", "hasKey": True, "n": 1,
                            "rows": [{"name": "was", "zone": "z",
                                      "kind": "place"}]}]}))
        self.use_repo(root, SIGNABLE={"expectations": "expectations.json"},
                      EXPECTATIONS_REL="expectations.json",
                      REFERENCE_REL="rows.json", ENGINE_REL="engine.py",
                      MANIFEST_RELS=(), SHA_PINS=(), ALLOW_DIR="no_allow_dir",
                      QUEUE_DIR=".", QUEUE_GLOB="ЗА_ПОДПИС_*.md")
        engine = release.load_engine()
        candidate = engine.dump_rows(engine.reference_rows())
        exp = {"_meta": {
                   "signed_by": SIGNER,
                   "reference": {"path": "rows.json",
                                 "sha256": hashlib.sha256(
                                     (root / "rows.json").read_bytes()).hexdigest()},
                   "candidate": {"sha256": hashlib.sha256(
                       candidate.encode("utf-8")).hexdigest()}},
               "p7": {"tokens": 2}}
        self.write(root / "expectations.json", self.body_of(exp))
        body = release.body_digest(self.body_of(exp))
        queue = root / "ЗА_ПОДПИС_фикстура.md"
        self.write(queue, queue_text.replace(u"<тяло>", body))
        self.commit_as(root, author, "sign: R1 да")
        return root, queue, body

    def blocked_lines(self, result, needle):
        return [line for line in result["blocked"] if needle in line]

    def test_the_release_judges_the_queue_of_the_blob_not_of_the_disk(self):
        """Амандамент №9 т. 1 — the hole that made all seven gates lie.

        `gates.sign` writes the decisions into the WORKTREE and Petar commits
        them; a gate that reads the file instead of the blob went green over a
        commit that carried not one signed row. The queue is now read exactly
        like every other body here — from `blob_at("HEAD", …)` — and a worktree
        that differs from it is blocked in the same words."""
        from gates import release
        root, queue, _body = self.release_repo(self.QUEUE_ROW)
        green = release.run()
        self.assertEqual(green["exit_code"], release.EXIT_OK, green["blocked"])
        self.write(queue, queue.read_text(encoding="utf-8") + u"- **бележка:** х\n")
        dirty = release.run()
        self.assertEqual(dirty["exit_code"], release.EXIT_BLOCKED)
        self.assertTrue(self.blocked_lines(
            dirty, u"работното дърво носи друго тяло от блоба на HEAD"),
            dirty["blocked"])

    def test_a_yes_on_the_disk_over_a_pending_blob_authorises_nothing(self):
        """The other half of т. 1: the ROWS come from the commit.

        The signature is on the disk, the commit says `pending`, and the delta
        the row would have covered is uncovered — which is what the push would
        publish."""
        from gates import release
        root, queue, _body = self.release_repo(
            self.QUEUE_ROW.replace(u"решение:** да", u"решение:** pending"))
        self.write(queue, queue.read_text(encoding="utf-8")
                   .replace(u"решение:** pending", u"решение:** да"))
        result = release.run()
        self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
        self.assertTrue(self.blocked_lines(result, u"непокрита делта gate_lot1/garden"),
                        result["blocked"])
        self.assertTrue(self.blocked_lines(result, u"работното дърво"), result["blocked"])

    def test_a_yes_row_an_agent_introduced_is_not_a_permission(self):
        """Амандамент №9 т. 2 — the auditor's scenario, exactly.

        The agent turns `pending` into „да“ and commits; Petar then makes one
        trivial commit to the queue (a note, outside the row). The FILE is his
        by its newest commit, so амандамент №6 т. 3 is satisfied and проверка 7
        used to be content — but the word „да“ was never written by his hand.
        Both readers say so now: the release gate and проверка 7, from one
        function."""
        from gates import release, run_gates
        root, queue, _body = self.release_repo(
            self.QUEUE_ROW.replace(u"решение:** да", u"решение:** pending"))
        self.write(queue, queue.read_text(encoding="utf-8")
                   .replace(u"решение:** pending", u"решение:** да"))
        agent = self.commit_as(root, "Claude Executor", "gates: a small fix")
        self.write(queue, queue.read_text(encoding="utf-8") + u"\n<!-- бележка -->\n")
        self.commit_as(root, "Petar1984", "docs: a note on the queue")
        result = release.run()
        self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
        named = self.blocked_lines(result, u"„да“ е въведено от")
        self.assertTrue(named, result["blocked"])
        self.assertIn("Claude Executor", named[0])
        self.assertIn(agent[:7], named[0])
        check = run_gates.check_signature_authorship()
        self.assertEqual(check.mark, run_gates.BAD, check.lines)
        self.assertTrue([line for line in check.lines if u"„да“ е въведено от" in line],
                        check.lines)

    def test_a_decision_hidden_from_the_reader_blocks(self):
        """Амандамент №9 т. 2: a „да“ in a comment or a fence is not a „да“.

        The row is invisible to the man who signs the file and authoritative to
        the machine that reads it. It authorises nothing now — and the attempt
        is named rather than silently dropped."""
        from gates import release
        hidden = (u"\n<!--\n## R9 · скрит\n- **id:** R9\n- **решение:** да\n"
                  u"- **покрива:** gate_lot1/*\n-->\n"
                  u"\n```\n- **решение:** да\n```\n")
        root, queue, _body = self.release_repo(
            self.QUEUE_ROW.replace(u"решение:** да", u"решение:** pending") + hidden)
        result = release.run()
        self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
        self.assertEqual(len(self.blocked_lines(result, u"в скрит регион")), 2,
                         result["blocked"])
        # …and the hidden row never became a row at all
        self.assertEqual([row["id"] for row in release.parse_queue_text(
            release.blob_at("HEAD", "ЗА_ПОДПИС_фикстура.md").decode("utf-8"))],
            ["R1"])
        self.assertTrue(self.blocked_lines(result, u"непокрита делта"), result["blocked"])

    def test_a_field_written_twice_blocks_the_release(self):
        """Амандамент №9 т. 2: one row, one decision.

        The parser keeps the last value and the reader reads the first, so
        „решение: не“ under „решение: да“ is a queue that says two things."""
        from gates import release
        doubled = self.QUEUE_ROW.replace(u"- **дата:**",
                                         u"- **решение:** не\n- **дата:**")
        root, queue, _body = self.release_repo(doubled)
        result = release.run()
        self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
        self.assertTrue(self.blocked_lines(result, u"написано два пъти"),
                        result["blocked"])

    def test_the_body_digest_catches_a_rewrite_no_other_field_binds(self):
        """Амандамент №9 т. 7 — what проверка 7 alone used to carry.

        The release gate binds fields: the reference digest, the candidate
        digest, the anchors. A rewrite that touches none of them — `p7.tokens`
        2 → 3, a number the SUITE reads — left this gate green, and `--freeze`
        reads this gate's verdict and nothing else. The digest of the whole body
        is on the row now, so the rewrite falls here too; and when the newest
        commit on the artefact is Petar's own, the difference is his freeze and
        the gate says which."""
        from gates import release
        root, queue, body = self.release_repo(self.QUEUE_ROW)
        exp = root / "expectations.json"
        rewritten = json.loads(exp.read_text(encoding="utf-8"))
        rewritten["p7"]["tokens"] = 3
        self.write(exp, self.body_of(rewritten))
        self.commit_as(root, "Claude Executor", "gates: a small fix")
        result = release.run()
        self.assertEqual(result["exit_code"], release.EXIT_BLOCKED)
        named = self.blocked_lines(result, u"подписаното тяло е пренаписано")
        self.assertTrue(named, result["blocked"])
        self.assertIn(body[:12], named[0])
        self.assertIn("Claude Executor", named[0])
        # The honest half: a body Petar's OWN commit produced is the freeze —
        # named out loud, not blocked, and not silent either.
        rewritten["p7"]["tokens"] = 4
        self.write(exp, self.body_of(rewritten))
        self.commit_as(root, "Petar1984", "freeze: the bodies")
        after = release.run()
        self.assertEqual(after["exit_code"], release.EXIT_OK, after["blocked"])
        self.assertTrue([line for line in after["lines"]
                         if u"пренаписано след подписа" in line], after["lines"])

    def test_the_pen_refuses_to_write_an_anchor_of_a_foreign_commit(self):
        """Амандамент №8 т. 4, the pen's half.

        `release.queue_reference` already BLOCKS an anchor whose commit is not
        Petar's. Without the same rule here the pen would write that anchor into
        the body as he signs it — a signature born already blocked, undoable
        only by editing a signed document by hand."""
        from gates import release, sign
        root = self.temp_repo()
        rows = root / "rows.json"
        self.write(rows, self.body_of({"gate_lot1": []}))
        self.use_repo(root, REFERENCE_REL="rows.json")
        agent = self.commit_as(root, "Claude Executor", "test: a reference")
        body = self.body_of({"_meta": {"signed_by": SIGNER}})
        text, note, complaint = sign.with_queue_anchor(release.EXPECTATIONS_REL, body)
        self.assertIsNotNone(complaint)
        self.assertIn(agent[:7], complaint)
        self.assertIn("Claude Executor", complaint)
        self.assertIn(release.HUMAN_AUTHOR, complaint)
        self.assertEqual(text, body, u"котвата е писана върху отказан комит")
        self.assertIsNone(note)
        # …and with Petar as the author of the carrier the field is written.
        self.write(rows, self.body_of({"gate_lot1": [{"q": u"градина"}]}))
        carrier = self.commit_as(root, "Petar1984", "freeze: the bodies")
        text, note, complaint = sign.with_queue_anchor(release.EXPECTATIONS_REL, body)
        self.assertIsNone(complaint)
        self.assertIn(carrier[:7], note)
        self.assertEqual(json.loads(text)["_meta"]["queue_reference"]["commit"], carrier)


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
        require_expectations(self)
        table = js_extra_forms(INDEX.read_text(encoding="utf-8"))
        self.assertEqual(table, REF.EXTRA_FORMS)
        self.assertEqual(table, claim("form_table")["table"])

    def test_the_form_answers_with_both_kinds_and_widens_nothing_else(self):
        """Measured on the ЛОТ 1 delivery: 61 = 51 kindergartens + 10 nurseries,
        M1-category, for both spellings — and П6/§Г, „детска градина“ still
        answers with 51 kindergartens and no nursery at all."""
        require_expectations(self)
        answers = claim("form_table")["answers"]
        for query in sorted(answers):
            rows, branch = REF.search(query)
            counts = {}
            for row in rows:
                counts[row.kind] = counts.get(row.kind, 0) + 1
            want = answers[query]
            self.assertEqual((branch, len(rows)), (want["branch"], want["n"]), query)
            self.assertEqual(counts, want["kinds"], query)
        # П6/§Г, the half that says the two single-kind words were NOT widened:
        # each of them still answers with one kind only.
        for query in (u"детска градина", u"детска ясла"):
            self.assertEqual(len(answers[query]["kinds"]), 1, query)


if __name__ == "__main__":
    unittest.main()
