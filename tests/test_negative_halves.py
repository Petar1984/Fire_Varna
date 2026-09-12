# -*- coding: utf-8 -*-
"""Ф13 · ИБ1-Г20 — the meta-gate: every negative half has RUN and has FALLEN.

    python -m unittest tests.test_negative_halves

Red line 7 of the plan: "a gate that cannot return ≠ 0 is not a gate; every
negative half MUST have run and MUST have failed". A half that only stands written
in a report is self-attestation. This module is where the fifteen Fire_Varna gates
plus the crossed half of ИБ1-Г3 are actually killed — sixteen rows, each with its
own recipe, each demanded to exit with the number `tests/negative_halves_manifest.json`
(Ф14) declares.

Everything happens OUTSIDE the live tree (STOP 10, план §5 правило 5): the fixtures
live under `%IB_TMP%/ib_fixtures` when that short root is named, otherwise under
`%TEMP%/ib1_fixtures_fv`, and the two halves that need a repository build a CLONE
with the pinned command of §1.1 (`git clone --no-hardlinks`, never `--no-local`).
Not one byte is written into `C:/git/Fire_Varna` — the doctored payloads, the
doctored `index.html` and the staged geometry all live in the throw-away copies.

Coordinates and any cadastral-shaped string are ASSEMBLED at run time (О95,
ИБ1-О21): a tracked file of this repo carries neither.

Червено по конструкция до К8/К9 (ИНТЕРВАЛ А, план §4 стъпка 9): a dozen of the
sixteen recipes need the delivered payload (К8) or the markers of Т12 (К9). Until
both exist the module fails fast with the reason and runs NO half — a red gate may
not cost ten minutes of somebody's evening.

Run: python -m unittest discover -s tests
"""
import json
import os
import pathlib
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

MANIFEST = pathlib.Path(os.environ.get("FIRE_VARNA_HALVES_MANIFEST")
                        or (REPO / "tests" / "negative_halves_manifest.json"))

DELIVERED_REL = "data/address_quarters.json"
DELIVERED = REPO / DELIVERED_REL
AMENDMENT_REL = "docs/decisions/011a_амандамент_И-Б1_11.09.md"
CORPUS_REL = "scratch/places_search/ib_corpus_11.09.json"

# план §4 стъпка 3а — the pinned base of the lot.
BASE = os.environ.get("FIRE_VARNA_BASE_COMMIT") or "73dfc91"

SHORT_ROOT = os.environ.get("IB_TMP")
FIXTURES = (pathlib.Path(SHORT_ROOT) / "ib_fixtures" if SHORT_ROOT
            else pathlib.Path(tempfile.gettempdir()) / "ib1_fixtures_fv")

# план §3.А Ф14 — the closed set. Sixteen rows, sixteen gates, no repetition.
EXPECTED_GATES = {"ИБ1-Г3", "ИБ1-Г7", "ИБ1-Г8", "ИБ1-Г9к", "ИБ1-Г10", "ИБ1-Г11",
                  "ИБ1-Г12", "ИБ1-Г13", "ИБ1-Г14", "ИБ1-Г15", "ИБ1-Г17",
                  "ИБ1-Г19к", "ИБ1-Г20", "ИБ1-Г21", "ИБ1-Г22", "ИБ1-Г23"}
# ИБ1-О33 (К7в): sixteen + the TWO halves of the dotted class — Г19к on the
# client that still normalizes dot-blind, Г23 on the one whose dot-less token
# list is empty. The gate SET does not grow; two of its members now carry two
# rows each.
MANIFEST_LEN = 18
ROW_KEYS = {"gate", "fixture", "argv", "expected_exit"}

# Т12 — the marker that says the client of К9 is in the tree.
CLIENT_MARKER = "// IB1 address slice start"
# The five markers, and where they go into the BASE blob (план §1.1, one-based).
BASE_MARKERS = ((4835, "// IB1 shared quarter state start"),
                (4836, "// IB1 shared quarter state end"),
                (4840, "// IB1 address slice start"),
                (5424, "// IB1 address slice core end"),
                (6199, "// IB1 address slice end"))

RUN_TIMEOUT = 900


def git(*args, cwd=None):
    return subprocess.run(["git"] + list(args), cwd=str(cwd or REPO),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def _drop_readonly(func, path, _exc):
    """ИБ1-О27: on Windows git leaves its pack files read-only, so `rmtree` cannot
    unlink them. Clear the bit and retry — never swallow the error."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def fresh(root):
    """ИБ1-О27: `ignore_errors=True` left a RUIN behind (the read-only pack files
    survived), the ruin still carried a `.git` directory and the second call of the
    same recipe died with `git add -> 128`. A failed wipe must now raise."""
    if root.exists():
        shutil.rmtree(root, onerror=_drop_readonly)
    root.mkdir(parents=True, exist_ok=True)
    return root


def write_json(path, doc):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")), encoding="utf-8")
    return path


def delivered_doc():
    return json.loads(DELIVERED.read_text(encoding="utf-8"))


def other_digest(value):
    return ("f" + value[1:]) if not value.startswith("f") else ("0" + value[1:])


def make_clone(root, name="ib_clone"):
    """The pinned clone command of §1.1 — `--no-local` is a forbidden form here."""
    path = root / name
    # ИБ1-О27: a `.git` directory is not a repository — a ruin left by a half-done
    # wipe carries one too. Only a clone that answers `rev-parse HEAD` is reused.
    if (path / ".git").exists() and git("rev-parse", "HEAD", cwd=path).returncode == 0:
        return path
    fresh(path.parent)
    result = git("clone", "--no-hardlinks", "--branch", "main", str(REPO), str(path),
                 cwd=root.parent if root.parent.exists() else REPO)
    if result.returncode != 0:
        raise AssertionError("git clone -> %d: %s" % (result.returncode,
                             result.stderr.decode("utf-8", "replace")[:400]))
    return path


class Recipes:
    """One method per fixture of Ф14. Each returns {env, cwd, needle}."""

    def __init__(self, root):
        self.root = root

    def build(self, name):
        method = getattr(self, name, None)
        if method is None:
            raise AssertionError(u"няма рецепта за фикстурата %r" % name)
        return method(fresh(self.root / name)) or {}

    # ---- ИБ1-Г3: the crossed half — a naive serialization of a WHOLE coordinate
    def cross_digest_serialization(self, root):
        """`String(43)` ≠ `'%.7f' % 43.0` (ИБ1-О6): three Cyrillic rows and one
        whole-number coordinate are enough to make the two digests differ, and the
        runner exits 1 when they do — which is what a broken serialization must do.

        The coordinate is BUILT here, out of whole numbers, so neither this file
        nor the fixture carries a pair in prose."""
        lat = float(43)
        lng = float(28)
        rows = [u"кв. Чайка, бл. 11", u"ул. Студентска 7", u"в.з.Звездица"]
        payload = {"rows": rows, "lat": lat, "lng": lng}
        write_json(root / "rows.json", payload)
        naive = root / "naive.mjs"
        naive.write_text(
            "import { readFileSync } from 'node:fs';\n"
            "const doc = JSON.parse(readFileSync(process.argv[2], 'utf8'));\n"
            "function fnv(s) {\n"
            "  const bytes = new TextEncoder().encode(s);\n"
            "  let h = 0x811c9dc5;\n"
            "  for (const b of bytes) { h ^= b; h = Math.imul(h, 0x01000193) >>> 0; }\n"
            "  return h.toString(16).padStart(8, '0');\n"
            "}\n"
            "// THE DEFECT: the naked serialization the plan forbids.\n"
            "const joined = doc.rows.map((r) => r + '~' + String(doc.lat) + ',' + String(doc.lng)).join('|');\n"
            "process.stdout.write(fnv(joined));\n", encoding="utf-8")
        runner = root / "cross_digest.py"
        runner.write_text(
            "# -*- coding: utf-8 -*-\n"
            "import json, subprocess, sys, pathlib\n"
            "ROOT = pathlib.Path(__file__).resolve().parent\n"
            "doc = json.loads((ROOT / 'rows.json').read_text(encoding='utf-8'))\n"
            "def fnv(text):\n"
            "    h = 0x811c9dc5\n"
            "    for b in text.encode('utf-8'):\n"
            "        h ^= b\n"
            "        h = (h * 0x01000193) & 0xFFFFFFFF\n"
            "    return '%08x' % h\n"
            "canon = '|'.join(r + '~' + ('%.7f' % doc['lat']) + ',' + ('%.7f' % doc['lng'])\n"
            "                 for r in doc['rows'])\n"
            "mine = fnv(canon)\n"
            "out = subprocess.run(['node', str(ROOT / 'naive.mjs'), str(ROOT / 'rows.json')],\n"
            "                     capture_output=True)\n"
            "theirs = out.stdout.decode('ascii', 'replace').strip()\n"
            "print('python %s node %s' % (mine, theirs))\n"
            "sys.exit(0 if mine == theirs else 1)\n", encoding="utf-8")
        return {"cwd": root, "needle": "python "}

    # ---- ИБ1-Г7: a staged new data/*.json with a geometry key, inside a CLONE
    def clone_with_staged_geometry(self, root):
        clone = make_clone(root)
        payload = {"kind": "negative half", "coordinates": [0, 0]}
        write_json(clone / "data" / "ib_neg_coords.json", payload)
        staged = git("add", "--", "data/ib_neg_coords.json", cwd=clone)
        if staged.returncode != 0:
            raise AssertionError("git add in the clone -> %d" % staged.returncode)
        return {"cwd": clone, "clone": clone, "needle": "ib_neg_coords.json"}

    # ---- ИБ1-Г8: the delivery one row short
    def quarter_index_one_row_short(self, root):
        doc = delivered_doc()
        doc["entry_cell"] = doc["entry_cell"][:-1]
        path = write_json(root / "quarters_short.json", doc)
        return {"env": {"FIRE_VARNA_QUARTER_INDEX_PATH": str(path)},
                "needle": "FAILED"}

    # ---- ИБ1-Г9к: the slice of <БАЗА>, wearing the markers of Т12
    def base_slice_with_markers(self, root):
        blob = git("show", "%s:index.html" % BASE)
        if blob.returncode != 0:
            raise AssertionError(u"няма блоб %s:index.html" % BASE)
        lines = blob.stdout.decode("utf-8").split("\n")
        for number, marker in sorted(BASE_MARKERS, reverse=True):
            lines.insert(number - 1, "  " + marker)
        path = root / "index.html"
        path.write_text("\n".join(lines), encoding="utf-8")
        return {"env": {"FIRE_VARNA_INDEX_HTML_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г10: one changed digit in the pin, judged BY ITS REASON
    def clone_with_a_broken_sha_pin(self, root):
        """ИБ1-О29: the first shape of this recipe ran `gates/run_gates.py` as a
        SCRIPT, and both mirrors died on `from gates import coverage` — exit 1
        without ever reaching the pin, i.e. a half that fell for the wrong reason.
        The module form runs the gate, and the needle demands the pin's own line,
        so an import error can never be mistaken for a verdict again."""
        clone = make_clone(root)
        index = clone / "index.html"
        text = index.read_text(encoding="utf-8")
        import re
        match = re.search(r"const\s+ADDRESS_QUARTERS_SHA256\s*=\s*'([0-9a-f]{64})'", text)
        if not match:
            raise AssertionError(u"ADDRESS_QUARTERS_SHA256 липсва в клонинга (Т2 е в К9)")
        pinned = match.group(1)
        broken = ("0" if pinned[0] != "0" else "1") + pinned[1:]
        index.write_text(text.replace(pinned, broken, 1), encoding="utf-8")
        return {"cwd": clone, "clone": clone,
                "needle": u"ADDRESS_QUARTERS_SHA256: пин"}

    # ---- ИБ1-Г19к (ИБ1-О31): the client that normalizes DOT-BLIND again
    def client_before_the_dotted_fix(self, root):
        """Undo К9а in a copy: the dot goes back to being replaced by a space and
        the panel forgets the parent row. „ж.к. Възраждане“ then flattens to
        „ж к възраждане“, the lead word is „ж“, no type matches — and the row
        says the quarter twice. The half falls on THAT, by its message."""
        text = (REPO / "index.html").read_bytes().decode("utf-8")
        undo = ((u"replace(/\\./g, '').replace(/[,-]/g, ' ')",
                 u"replace(/[.,-]/g, ' ')"),
                (u"(' · част от ' + quarter.parent_display)", u"('')"))
        for anchor, instead in undo:
            if text.count(anchor) != 1:
                raise AssertionError(u"котвата на К9а липсва (%d попадения): %s"
                                     % (text.count(anchor), anchor))
            text = text.replace(anchor, instead, 1)
        path = root / "index.html"
        path.write_text(text, encoding="utf-8")
        return {"env": {"FIRE_VARNA_INDEX_HTML_PATH": str(path)},
                "needle": u"заглавието не е"}

    # ---- ИБ1-Г23 (§3.Д (д)): the client whose DOT-LESS token list is empty
    def client_without_the_dotless_token_list(self, root):
        """With `TOKEN_TYPES` empty the GPS branch cuts only when the WHOLE label
        spells the name, so „жк бриз 2“ keeps its written run and the line says
        „ж.к. Бриз, Жк бриз 2“ — the quarter twice."""
        text = (REPO / "index.html").read_bytes().decode("utf-8")
        start = text.find(u"    const TOKEN_TYPES = [")
        if start < 0:
            raise AssertionError(u"TOKEN_TYPES липсва (§3.Д (д) се ражда в К9а)")
        end = text.find(u"];", start)
        if end < 0:
            raise AssertionError(u"TOKEN_TYPES не е затворен масив")
        text = text[:start] + u"    const TOKEN_TYPES = [" + text[end:]
        path = root / "index.html"
        path.write_text(text, encoding="utf-8")
        return {"env": {"FIRE_VARNA_INDEX_HTML_PATH": str(path)},
                "needle": u"два пъти"}

    # ---- ИБ1-Г11: an eager literal fetch of the third payload
    def eager_quarter_fetch(self, root):
        text = (REPO / "index.html").read_bytes().decode("utf-8")
        needle = "window._hydrantDataReady"
        if needle not in text:
            raise AssertionError(u"котвата на нетърпеливия товар изчезна")
        text = text.replace(needle, "fetch('data/address_quarters.json');\n" + needle, 1)
        path = root / "index.html"
        path.write_text(text, encoding="utf-8")
        return {"env": {"FIRE_VARNA_INDEX_HTML_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г12: the kill switch left ON
    def kill_switch_left_on(self, root):
        return {"env": {"FIRE_VARNA_KILL_SWITCH_FLAG": "true"}, "needle": "FAILED"}

    # ---- ИБ1-Г13: a copy of tests/ with one red test in it
    def tests_copy_with_one_red(self, root):
        shutil.copytree(str(REPO / "tests"), str(root / "tests"),
                        ignore=shutil.ignore_patterns("__pycache__"))
        (root / "tests" / "test_ib1_declared_red.py").write_text(
            "# -*- coding: utf-8 -*-\n"
            "import unittest\n"
            "class DeclaredRed(unittest.TestCase):\n"
            "    def test_it_falls(self):\n"
            "        self.fail('ИБ1-Г13 negative half')\n", encoding="utf-8")
        return {"needle": "FAILED"}

    # ---- ИБ1-Г14: coverage without its base (Errno 2 -> EXIT_USAGE)
    def coverage_without_its_base(self, root):
        return {"needle": "coverage:"}

    # ---- ИБ1-Г15: a coordinate pair in prose, assembled here
    def coordinate_pair_in_prose(self, root):
        pair = u"%d.%s, %d.%s" % (43, "2141000", 27, "9147000")
        (root / "prose.md").write_text(
            u"# ИБ1-Г15 · отрицателна половина\n\nТочката е %s.\n" % pair,
            encoding="utf-8")
        return {"needle": "HIT "}

    # ---- ИБ1-Г17: a foreign entries_digest at the same length
    def foreign_entries_digest(self, root):
        doc = delivered_doc()
        meta = dict(doc["generated_from"])
        meta["entries_digest"] = other_digest(meta["entries_digest"])
        doc["generated_from"] = meta
        path = write_json(root / "quarters_digest.json", doc)
        return {"env": {"FIRE_VARNA_QUARTER_INDEX_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г19к: a locality cell that speaks (D6 broken on purpose)
    def locality_cell_that_speaks(self, root):
        doc = delivered_doc()
        if "zpz" not in doc["codes"]:
            raise AssertionError(u"клетката zpz изчезна от доставката")
        cell = doc["codes"].index("zpz")
        doc["entry_cell"] = [cell if v == -1 else v for v in doc["entry_cell"]]
        path = write_json(root / "quarters_locality.json", doc)
        return {"env": {"FIRE_VARNA_QUARTER_INDEX_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г20: the manifest with its OWN row taken out
    def manifest_without_its_own_row(self, root):
        doc = json.loads(MANIFEST.read_text(encoding="utf-8"))
        doc["halves"] = [row for row in doc["halves"] if row["gate"] != "ИБ1-Г20"]
        path = write_json(root / "manifest.json", doc)
        return {"env": {"FIRE_VARNA_HALVES_MANIFEST": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г21: the amendment without И-Б1-D5
    def amendment_without_d5(self, root):
        text = (REPO / AMENDMENT_REL).read_text(encoding="utf-8")
        kept = [line for line in text.split("\n") if u"И-Б1-D5" not in line]
        path = root / "amendment.md"
        path.write_text("\n".join(kept), encoding="utf-8")
        return {"env": {"FIRE_VARNA_AMENDMENT_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г22: the GPS surface silenced while the row still speaks
    def row_cells_all_silenced(self, root):
        doc = delivered_doc()
        doc["row_cell"] = [-1] * len(doc["row_cell"])
        path = write_json(root / "quarters_no_rows.json", doc)
        return {"env": {"FIRE_VARNA_QUARTER_INDEX_PATH": str(path)}, "needle": "FAILED"}

    # ---- ИБ1-Г23: row_cell one short — the document must be refused whole
    def row_cell_one_short(self, root):
        doc = delivered_doc()
        doc["row_cell"] = doc["row_cell"][:-1]
        path = write_json(root / "quarters_short_rows.json", doc)
        return {"env": {"FIRE_VARNA_QUARTER_INDEX_PATH": str(path)}, "needle": "FAILED"}


class NegativeHalvesTest(unittest.TestCase):
    """ИБ1-Г20 — sixteen rows, sixteen fallen halves, not one exit 0."""

    def manifest(self):
        if not MANIFEST.exists():
            self.fail(u"липсва манифестът Ф14: %s" % MANIFEST)
        return json.loads(MANIFEST.read_text(encoding="utf-8"))["halves"]

    def assert_shape(self):
        rows = self.manifest()
        self.assertEqual(len(rows), MANIFEST_LEN,
                         u"манифестът има %d реда, не %d" % (len(rows), MANIFEST_LEN))
        self.assertEqual({row["gate"] for row in rows}, EXPECTED_GATES,
                         u"множеството гейтове не е това на Ф14")
        for row in rows:
            self.assertEqual(set(row), ROW_KEYS, row)
            self.assertIsInstance(row["argv"], list)
            self.assertIsInstance(row["expected_exit"], int)
        return rows

    def require_client(self):
        """The recipes that doctor the delivery or the client cannot be built
        before К8 and К9. Fail fast and name the reason — never run half a table."""
        missing = []
        if not DELIVERED.exists():
            missing.append(DELIVERED_REL + u" (К8)")
        if CLIENT_MARKER not in (REPO / "index.html").read_bytes().decode("utf-8"):
            missing.append(u"маркерите на Т12 в index.html (К9)")
        if missing:
            self.fail(u"ИНТЕРВАЛ А: половините не могат да се построят — липсва %s"
                      % u", ".join(missing))

    def test_manifest_shape(self):
        self.assert_shape()

    def test_every_half_runs_and_falls(self):
        rows = self.assert_shape()
        self.require_client()
        if not shutil.which("node"):
            self.fail(u"node липсва — половините са гейт, не пропуснат тест")
        recipes = Recipes(FIXTURES)
        for row in rows:
            with self.subTest(gate=row["gate"], fixture=row["fixture"]):
                built = recipes.build(row["fixture"])
                place = {"python": sys.executable,
                         "node": shutil.which("node") or "node",
                         "repo": str(REPO),
                         "base": BASE,
                         "fixture": str(FIXTURES / row["fixture"]),
                         "clone": str(built.get("clone") or (FIXTURES / row["fixture"]))}
                argv = [arg.format(**place) for arg in row["argv"]]
                environment = dict(os.environ, PYTHONIOENCODING="utf-8")
                environment.update(built.get("env") or {})
                result = subprocess.run(argv, cwd=str(built.get("cwd") or REPO),
                                        capture_output=True, timeout=RUN_TIMEOUT,
                                        env=environment)
                out = (result.stdout + result.stderr).decode("utf-8", "replace")
                self.assertEqual(result.returncode, row["expected_exit"],
                                 u"%s: изход %d вместо %d\n%s"
                                 % (row["gate"], result.returncode,
                                    row["expected_exit"], out[-800:]))
                needle = built.get("needle")
                if needle:
                    self.assertIn(needle, out,
                                  u"%s: половината падна, но не по своята причина\n%s"
                                  % (row["gate"], out[-800:]))


if __name__ == "__main__":
    unittest.main()
