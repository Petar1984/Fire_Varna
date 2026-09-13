# -*- coding: utf-8 -*-
"""Лот 1 · Г1-Г8 — one standard for every report form made AT a hydrant.

    python -m unittest tests.test_report_form_operational

The three forms made at an existing hydrant (`exists_confirmed`, `wrong_location`,
`damaged`) carry the SAME block of pickers: the type row, pre-selected from the
record, and the operational row, never pre-selected, with the stored status shown
as a readable label above it. Both answers are required (Petar, 13.09; issue #769).
The ingest applies both fields for `wrong_location` and `damaged`.

How this gate works, so no reader has to guess:

  * The client is raised HEADLESS. `tests/granitsi_client_probe.mjs` gets a SLICE of
    `index.html` on STDIN and answers on STDOUT; the probe answers, THIS file judges.
    The slice is cut by the NAME of each function (`block`), never by line number and
    never by a marker planted in the production code - a marker in `index.html` would
    be scope the plan does not carry.
  * The reference is not a retyped string but the SAME slice at the BASE commit, which
    is pinned as a literal under its own environment name (`FIRE_VARNA_LOT1_BASE`),
    never as `merge-base`: a moving reference cannot prove that the untouched branches
    did not move. A base whose blob equals the working file is a dead reference and
    fails loud.
  * Nothing is read at module level and no git runs there: ИБ1-Г13 copies `tests/`
    into a bare tree and runs `discover`, and a failure there has to be a NAMED one.
  * The four negative halves run the gate against DOCTORED copies of `index.html`
    under the temp root - never inside the repository - and demand exit 1 plus the
    gate's own reason in the output.

Coordinates are assembled at run time out of one-decimal numbers, as
`tests/test_hydrant_core.py` already does; no coordinate pair stands in this file.
"""
import copy
import json
import math
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
PROBE = REPO / "tests" / "granitsi_client_probe.mjs"
INDEX = pathlib.Path(os.environ.get("FIRE_VARNA_INDEX_HTML_PATH") or (REPO / "index.html"))
HYDRANTS = REPO / "data" / "hydrants.json"

# The base is a LITERAL with its own name (план §5 К3.3): not the merge-base and not
# `FIRE_VARNA_BASE_COMMIT`, which other gates move for their own reasons.
BASE = os.environ.get("FIRE_VARNA_LOT1_BASE") or "8512ab6"

# The doctored copies of the negative halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot1_fixtures"

MODULE = "tests.test_report_form_operational"

# The seven blocks of the slice, in the order they have to be raised in.
ANCHORS = (
    "const OPERATIONAL_LABELS = {",
    "function escapeHtml(s) {",
    "function radioRowHTML(field, options, selected) {",
    "const NOTE_HINT_HTML =",
    "const AT_HYDRANT_TYPES =",
    "function hydrantPickersHTML(d) {",
    "function typeFieldsHTML(t, d) {",
)
# The two blocks that are BORN in this lot: at the base they are missing by
# construction, and only there is their absence allowed.
BASE_OPTIONAL = ("const AT_HYDRANT_TYPES =", "function hydrantPickersHTML(d) {")

# The regions the lot is allowed to move; everything else is byte-compared.
CHANGED_BLOCKS = (
    "function showReportModal(",
    "function onSubmitClicked(",
    "function buildReportObject(",
    "function reportTypeToSemanticPatch(",
)
# The functions the plan pins as untouched (план §5 "Нула промяна другаде").
PINNED_BLOCKS = (
    "function locationFieldHTML(t, placedCoord) {",
    "function readDraftFromForm() {",
    "function wireFormHandlers(",
    "function hydrantStatusClass(",
    "function escapeHtml(s) {",
)

FORMS = ("exists_confirmed", "wrong_location", "damaged")
STATUSES = ("not_tested", "works", "not_working")
UNTOUCHED_FORMS = ("missing", "new_hydrant")

SIGNED_GATE = "if (AT_HYDRANT_TYPES.has(reportType) || reportType === 'new_hydrant') {"
PAYLOAD_CONDITION = "(AT_HYDRANT_TYPES.has(reportType) || reportType === 'new_hydrant')"
OPERATIONAL_ROW = u"radioRowHTML('operational', ['да','не','не съм проверявал'], d.operational) +"
MISSING_BRANCH_BYTE = u"би трябвало да е тук?"
TAIL_LINE = "function refreshMarkerIconsForHydrant(h) {"

# Ingest fixtures - the coordinate is BUILT out of these two numbers at run time.
TIMESTAMP = "2026-09-13T00:00:00+03:00"
APPROVER = "petar"
LON = 27.9
LAT = 43.2


# --------------------------------------------------------------------------
# Reading the two texts - inside a method, never at import
# --------------------------------------------------------------------------

def index_text(test):
    """The bytes of the candidate `index.html`, decoded. Read per method."""
    if not INDEX.is_file():
        test.fail(u"липсва index.html: %s" % INDEX)
    return INDEX.read_bytes().decode("utf-8")


def base_text(test):
    """The blob of `<BASE>:index.html`. A dead reference is a failure, not a skip."""
    proc = subprocess.run(["git", "-C", str(REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html — базата е неразрешима: %s"
                  % (BASE, proc.stderr.decode("utf-8", "replace")[:300]))
    text = proc.stdout.decode("utf-8")
    if text == index_text(test):
        test.fail(u"base equals candidate — базата %s е равна на работния файл" % BASE)
    return text


# --------------------------------------------------------------------------
# The cutter: a block is found by NAME and closed by its own braces
# --------------------------------------------------------------------------

def span(test, text, anchor, required=True):
    """(first, last) line index of the block whose first line starts with `anchor`."""
    if text.count(anchor) == 0 and not required:
        return None
    if text.count(anchor) != 1:
        test.fail(u"котвата %r стои %d пъти, не веднъж" % (anchor, text.count(anchor)))
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if line.strip().startswith(anchor)]
    if len(hits) != 1:
        test.fail(u"котвата %r не започва точно един ред (%d)" % (anchor, len(hits)))
    depth = 0
    for j in range(hits[0], len(lines)):
        depth += lines[j].count("{") - lines[j].count("}")
        if depth == 0 and lines[j].rstrip().endswith((";", "}")):
            return (hits[0], j)
    test.fail(u"блокът на %r не се затваря" % anchor)


def block(test, text, anchor, required=True):
    found = span(test, text, anchor, required=required)
    if found is None:
        return None
    return "\n".join(text.split("\n")[found[0]:found[1] + 1])


def first_difference(left, right):
    """Where two texts part - the LINE NUMBER only, never the line itself."""
    a, b = left.split("\n"), right.split("\n")
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return u"първата разлика е на ред %d" % (i + 1)
    return u"различна дължина: %d срещу %d реда" % (len(a), len(b))


# --------------------------------------------------------------------------
# The headless harness
# --------------------------------------------------------------------------

def build_slice(test, text, base=False):
    parts = []
    for anchor in ANCHORS:
        piece = block(test, text, anchor,
                      required=not (base and anchor in BASE_OPTIONAL))
        if piece is not None:
            parts.append(piece)
    return "\n".join(parts)


def ask_client(test, text, asks, base=False):
    """Raise the slice in `tests/granitsi_client_probe.mjs` and return its answers."""
    node = shutil.which("node")
    if node is None:
        test.fail(u"node липсва — гейтът е гейт, не пропуснат тест")
    payload = {"slice": build_slice(test, text, base=base),
               "exports": ["typeFieldsHTML", "OPERATIONAL_LABELS"],
               "asks": asks}
    proc = subprocess.run([node, str(PROBE)],
                          input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          cwd=str(REPO), timeout=300)
    out = proc.stdout.decode("utf-8", "replace")
    try:
        doc = json.loads(out)
    except ValueError:
        test.fail(u"пробата не върна json (изход %d): %s | %s"
                  % (proc.returncode, out[:300],
                     proc.stderr.decode("utf-8", "replace")[:300]))
    if not doc.get("ok"):
        test.fail(u"пробата падна: %s" % json.dumps(doc, ensure_ascii=False)[:600])
    return doc["answers"]


def call(form, draft):
    return {"ask": "call", "name": "typeFieldsHTML", "args": [form, draft]}


LABELS_ASK = {"ask": "value", "name": "OPERATIONAL_LABELS"}


# --------------------------------------------------------------------------
# Form fixtures - what `showReportModal` hands to `typeFieldsHTML`
# --------------------------------------------------------------------------

def form_draft(hydrant, hydrant_type=""):
    """An untouched draft: nothing typed, nothing chosen (the two picker keys and
    the three free-text keys are empty), the two `missing`-only keys at their
    production defaults so that branch renders what the page renders."""
    return {"hydrant": hydrant,
            "hydrant_type": hydrant_type,
            "operational": "",
            "free_text": "",
            "description": "",
            "damage_description": "",
            "terrain_description": "",
            "hydrant_type_at_location": u"не знам"}


def with_status(status):
    """Ф-със-състояние: a record that already carries an operational status."""
    return form_draft({"operational_status": status})


def with_type_and_status():
    """Ф-с-тип-и-състояние: the type is pre-selected, the status never is."""
    return form_draft({"type": u"надземен", "operational_status": "works"},
                      hydrant_type=u"надземен")


def without_status():
    """Ф-без-състояние: an imported record with nothing on it yet."""
    return form_draft({})


def all_fixtures():
    return [(u"със състояние", with_status("works")),
            (u"с тип и състояние", with_type_and_status()),
            (u"без състояние", without_status())]


def field(test, html, field_id):
    """The one `<div class="field" id="...">` block of the rendered form."""
    head = '<div class="field" id="%s">' % field_id
    if html.count(head) != 1:
        test.fail(u"полето %s стои %d пъти в изхода" % (field_id, html.count(head)))
    start = html.index(head)
    nxt = html.find('<div class="field"', start + len(head))
    return html[start:] if nxt < 0 else html[start:nxt]


# --------------------------------------------------------------------------
# Г1 · the pickers of the three forms
# --------------------------------------------------------------------------

class OperationalPickerTest(unittest.TestCase):

    def test_the_question_is_emitted_for_every_known_status(self):
        text = index_text(self)
        cases, asks = [], []
        for status in STATUSES:
            for form in FORMS:
                cases.append((form, status))
                asks.append(call(form, with_status(status)))
        answers = ask_client(self, text, asks)
        for (form, status), html in zip(cases, answers):
            seg = field(self, html, "fld_operational")
            reason = (u"%s / %s: формата не носи реда с трите чипа на „Работи ли?“"
                      % (form, status))
            self.assertIn('data-radio="operational"', seg, reason)
            self.assertEqual(seg.count('class="radio-chip'), 3, reason)

    def test_no_chip_is_preselected_and_the_type_row_keeps_its_own(self):
        text = index_text(self)
        cases, asks = [], []
        for form in FORMS:
            for name, draft in all_fixtures():
                cases.append((form, name, draft["hydrant_type"] != ""))
                asks.append(call(form, draft))
        answers = ask_client(self, text, asks)
        for (form, name, typed), html in zip(cases, answers):
            op = field(self, html, "fld_operational")
            self.assertEqual(op.count("radio-chip selected"), 0,
                             u"%s / %s: състояние е предизбрано" % (form, name))
            row = field(self, html, "fld_hydrant_type")
            self.assertEqual(row.count("radio-chip selected"), 1 if typed else 0,
                             u"%s / %s: редът на типа не носи своя избор" % (form, name))

    def test_the_current_status_is_shown_as_a_readable_label(self):
        text = index_text(self)
        cases, asks = [], [LABELS_ASK]
        for status in STATUSES:
            for form in FORMS:
                cases.append((form, status))
                asks.append(call(form, with_status(status)))
        for form in FORMS:
            cases.append((form, None))
            asks.append(call(form, without_status()))
        answers = ask_client(self, text, asks)
        labels = answers[0]
        self.assertTrue(isinstance(labels, dict) and labels,
                        u"клиентът не даде OPERATIONAL_LABELS")
        for (form, status), html in zip(cases, answers[1:]):
            if status is None:
                self.assertNotIn(u"сега: ", html,
                                 u"%s: надпис при запис без състояние" % form)
                continue
            seg = field(self, html, "fld_operational")
            expected = u'<div class="hint">сега: ' + labels[status] + u"</div>"
            self.assertIn(expected, seg,
                          u"%s / %s: текущото състояние не стои като четим надпис"
                          % (form, status))

    def test_the_required_marker_is_present_on_every_form(self):
        text = index_text(self)
        cases, asks = [], []
        for form in FORMS:
            for name, draft in all_fixtures():
                cases.append((form, name))
                asks.append(call(form, draft))
        answers = ask_client(self, text, asks)
        for (form, name), html in zip(cases, answers):
            for field_id in ("fld_hydrant_type", "fld_operational"):
                seg = field(self, html, field_id)
                reason = u"%s / %s / %s: въпросът не е задължителен (Р1б)" % (form, name, field_id)
                self.assertIn('<span class="req">*</span>', seg, reason)
                self.assertIn('<div class="err">', seg, reason)

    def test_the_untouched_branches_and_the_status_less_case_are_byte_equal_to_the_base(self):
        text = index_text(self)
        base = base_text(self)
        cases, asks = [], []
        for form in UNTOUCHED_FORMS:
            for name, draft in all_fixtures():
                cases.append((form, name))
                asks.append(call(form, draft))
        cases.append(("exists_confirmed", u"без състояние"))
        asks.append(call("exists_confirmed", without_status()))
        candidate = ask_client(self, text, asks)
        reference = ask_client(self, base, asks, base=True)
        for (form, name), got, want in zip(cases, candidate, reference):
            self.assertTrue(got == want,
                            u"%s / %s: клонът не е байт за байт равен на базата %s"
                            % (form, name, BASE))

    def test_every_status_in_the_dataset_gets_a_picker_and_a_label(self):
        text = index_text(self)
        if not HYDRANTS.is_file():
            self.fail(u"липсва %s" % HYDRANTS)
        records = json.loads(HYDRANTS.read_bytes().decode("utf-8"))
        statuses = sorted({r.get("operational_status") for r in records
                           if r.get("operational_status")})
        if not statuses:
            self.fail(u"нула състояния в записа — гейтът щеше да е вакуумен")
        # The COUNT travels to stderr and is not pinned: the dataset grows.
        sys.stderr.write(u"[лот 1] различни състояния в записа: %d\n" % len(statuses))
        asks = [LABELS_ASK] + [call("exists_confirmed", with_status(s)) for s in statuses]
        answers = ask_client(self, text, asks)
        labels = answers[0]
        for status, html in zip(statuses, answers[1:]):
            seg = field(self, html, "fld_operational")
            self.assertIn('data-radio="operational"', seg,
                          u"състояние %s остава без пикер" % status)
            self.assertIn(u'<div class="hint">сега: ' + labels.get(status, status) + u"</div>",
                          seg, u"състояние %s остава без надпис" % status)

    def test_the_validation_gate_is_the_signed_line(self):
        text = index_text(self)
        self.assertEqual(text.count(SIGNED_GATE), 1,
                         u"подписаният ред на валидацията не стои точно веднъж")
        for dead in ("opVisible", "showOpPicker", "whichever pickers are",
                     u"reportType === 'damaged' ? 'не съм проверявал'"):
            self.assertNotIn(dead, text, u"мъртъв код остана: %s" % dead)

    def test_the_payload_and_the_patch_emit_both_fields_for_the_three_forms(self):
        text = index_text(self)
        payload = block(self, text, "function buildReportObject(")
        self.assertEqual(payload.count(PAYLOAD_CONDITION), 2,
                         u"полезният товар не излъчва двете полета за трите форми")
        for key in ("type:", "operational_status:"):
            self.assertIn(key + "\n        " + PAYLOAD_CONDITION, payload,
                          u"ключът %s не стои под подписаното условие" % key)
        patch = block(self, text, "function reportTypeToSemanticPatch(")
        for tail in ("AT_HYDRANT_TYPES.has(t) && report.type)",
                     "AT_HYDRANT_TYPES.has(t) && report.operational_status)"):
            self.assertEqual(patch.count(tail), 1,
                             u"клиентската кръпка не слива %s" % tail)


# --------------------------------------------------------------------------
# Г2 · the perimeter inside index.html
# --------------------------------------------------------------------------

class PerimeterTest(unittest.TestCase):

    def remainder(self, text):
        """Everything OUTSIDE the regions the lot is allowed to move."""
        lines = text.split("\n")
        killed = set()
        note_end = span(self, text, "const NOTE_HINT_HTML =")[1]
        fields_end = span(self, text, "function typeFieldsHTML(t, d) {")[1]
        if fields_end <= note_end:
            self.fail(u"областта на формите е обърната")
        killed.update(range(note_end + 1, fields_end + 1))
        for anchor in CHANGED_BLOCKS:
            first, last = span(self, text, anchor)
            killed.update(range(first, last + 1))
        return "\n".join(line for n, line in enumerate(lines) if n not in killed)

    def test_everything_outside_the_changed_regions_is_byte_equal_to_the_base(self):
        candidate = self.remainder(index_text(self))
        reference = self.remainder(base_text(self))
        self.assertTrue(candidate == reference,
                        u"извън променените области нещо е мръднало срещу %s (%s)"
                        % (BASE, first_difference(reference, candidate)))

    def test_the_pinned_functions_are_byte_equal_to_the_base(self):
        text = index_text(self)
        base = base_text(self)
        for anchor in PINNED_BLOCKS:
            got = block(self, text, anchor)
            want = block(self, base, anchor)
            self.assertTrue(got == want,
                            u"пинованата функция %r се е променила срещу %s" % (anchor, BASE))


# --------------------------------------------------------------------------
# Г3 · the ingest applies both fields for wrong_location and damaged
# --------------------------------------------------------------------------

def ingest_core(test):
    """`scripts/lib/hydrant_core` - imported inside the method, never at import."""
    lib = str(REPO / "scripts" / "lib")
    if lib not in sys.path:
        sys.path.insert(0, lib)
    try:
        import hydrant_core
    except ImportError as exc:
        test.fail(u"не мога да внеса hydrant_core: %s" % exc)
    return hydrant_core


def point_north(core, lon, lat, meters):
    """A point exactly `meters` due north - the pair is BUILT here, never written."""
    return (lon, lat + math.degrees(meters / core.EARTH_RADIUS_M))


def make_state(core, records):
    records = copy.deepcopy(records)
    return {"records": records,
            "provenance": {r["id"]: {"source_refs": []} for r in records},
            "alias": core.build_alias_index(records)}


def stored_record(core):
    """A verified record that already carries a type and a working status."""
    return {"id": core.canonical_coord_id(LON, LAT),
            "coords": [LON, LAT],
            "origin": "vik",
            "legacy_ids": [],
            "existence_status": "verified",
            "type": u"подземен",
            "operational_status": "works"}


class IngestTest(unittest.TestCase):

    def test_wrong_location_applies_type_and_status_under_the_new_id(self):
        core = ingest_core(self)
        record = stored_record(core)
        old_id = record["id"]
        state = make_state(core, [record])
        moved = point_north(core, LON, LAT, 50.0)
        report = {"issue_number": 769, "report_type": "wrong_location",
                  "hydrant_id": old_id, "reported_coord": [moved[0], moved[1]],
                  "type": u"надземен", "operational_status": "not_working"}
        result = core.apply_wrong_location(state, report, TIMESTAMP, APPROVER)
        new_id = core.canonical_coord_id(moved[0], moved[1])
        self.assertEqual(result["action"], "applied", u"докладът не влезе")
        self.assertNotEqual(new_id, old_id, u"идентификаторът не се смени")
        self.assertEqual(result["target_id_after"], new_id)
        got = state["records"][0]
        self.assertEqual(got["id"], new_id)
        self.assertEqual(got["type"], u"надземен", u"типът не е приложен")
        self.assertEqual(got["operational_status"], "not_working",
                         u"състоянието не е приложено")
        self.assertIn(new_id, state["provenance"],
                      u"провенансът не легна под новия идентификатор")
        ref = state["provenance"][new_id]["source_refs"][-1]
        self.assertEqual(ref["manual_field"], "multiple")
        self.assertEqual(ref["old_value"]["type"], u"подземен")
        self.assertEqual(ref["old_value"]["operational_status"], "works")

    def test_wrong_location_without_answers_changes_only_coords_and_id(self):
        core = ingest_core(self)
        record = stored_record(core)
        old_id = record["id"]
        state = make_state(core, [record])
        moved = point_north(core, LON, LAT, 50.0)
        report = {"issue_number": 770, "report_type": "wrong_location",
                  "hydrant_id": old_id, "reported_coord": [moved[0], moved[1]],
                  "type": None, "operational_status": None}
        result = core.apply_wrong_location(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(sorted(result["changes"]), ["coords", "id"],
                         u"null промени нещо извън координатите и идентификатора")
        got = state["records"][0]
        self.assertEqual(got["type"], u"подземен", u"типът беше понижен от null")
        self.assertEqual(got["operational_status"], "works",
                         u"състоянието беше понижено от null")

    def test_damaged_applies_type_and_status_and_ignores_null(self):
        core = ingest_core(self)
        record = stored_record(core)
        hydrant_id = record["id"]
        state = make_state(core, [record])
        report = {"issue_number": 716, "report_type": "damaged",
                  "hydrant_id": hydrant_id, "type": u"надземен",
                  "operational_status": "not_working"}
        result = core.apply_damaged(state, report, TIMESTAMP, APPROVER)
        self.assertEqual(result["action"], "applied")
        got = state["records"][0]
        self.assertEqual(got["type"], u"надземен", u"повреден: типът не е приложен")
        self.assertEqual(got["operational_status"], "not_working",
                         u"повреден: състоянието не е приложено")
        quiet = make_state(core, [record])
        silent = {"issue_number": 731, "report_type": "damaged",
                  "hydrant_id": hydrant_id, "type": None, "operational_status": None}
        result = core.apply_damaged(quiet, silent, TIMESTAMP, APPROVER)
        self.assertEqual(result["changes"], {},
                         u"повреден: null промени запис")
        untouched = quiet["records"][0]
        self.assertEqual(untouched["type"], u"подземен")
        self.assertEqual(untouched["operational_status"], "works")


# --------------------------------------------------------------------------
# Г4-Г8 · the four negative halves - each RUNS and each FALLS
# --------------------------------------------------------------------------

def replace_once(test, text, needle, value):
    if text.count(needle) != 1:
        test.fail(u"котвата на половината стои %d пъти, не веднъж: %r"
                  % (text.count(needle), needle))
    return text.replace(needle, value)


class NegativeHalfTest(unittest.TestCase):

    def doctored(self, name, text):
        """A doctored copy of `index.html` under the temp root - never in the tree."""
        root = FIXTURES / name
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)
        path = root / "index.html"
        path.write_bytes(text.encode("utf-8"))
        return path

    def run_half(self, path, target, needle):
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_INDEX_HTML_PATH=str(path))
        proc = subprocess.run([sys.executable, "-m", "unittest", target],
                              cwd=str(REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=600)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"половината не падна: изход %d\n%s"
                         % (proc.returncode, out[-800:]))
        self.assertIn(needle, out,
                      u"половината падна, но не по своята причина\n%s" % out[-800:])

    def test_removing_the_operational_row_turns_the_gate_red(self):
        text = index_text(self)
        lines = text.split("\n")
        first, last = span(self, text, "function hydrantPickersHTML(d) {")
        body = replace_once(self, "\n".join(lines[first:last + 1]), OPERATIONAL_ROW, "'' +")
        doctored = "\n".join(lines[:first] + body.split("\n") + lines[last + 1:])
        path = self.doctored("no_operational_row", doctored)
        self.run_half(path, MODULE + ".OperationalPickerTest."
                      "test_the_question_is_emitted_for_every_known_status",
                      u"не носи реда с трите чипа")

    def test_restoring_the_old_validation_gate_turns_the_gate_red(self):
        text = replace_once(self, index_text(self), SIGNED_GATE,
                            "if (reportType === 'new_hydrant') {")
        path = self.doctored("old_validation_gate", text)
        self.run_half(path, MODULE + ".OperationalPickerTest."
                      "test_the_validation_gate_is_the_signed_line",
                      u"подписаният ред на валидацията")

    def test_a_byte_in_an_untouched_branch_turns_the_gate_red(self):
        text = replace_once(self, index_text(self), MISSING_BRANCH_BYTE,
                            MISSING_BRANCH_BYTE[:-1] + u"!")
        path = self.doctored("missing_branch_byte", text)
        self.run_half(path, MODULE + ".OperationalPickerTest."
                      "test_the_untouched_branches_and_the_status_less_case_are_byte_equal_to_the_base",
                      u"не е байт за байт равен на базата")

    def test_a_byte_in_the_tail_segment_turns_the_perimeter_gate_red(self):
        text = replace_once(self, index_text(self), TAIL_LINE,
                            TAIL_LINE.replace(") {", ")  {"))
        path = self.doctored("tail_segment_byte", text)
        self.run_half(path, MODULE + ".PerimeterTest."
                      "test_everything_outside_the_changed_regions_is_byte_equal_to_the_base",
                      u"извън променените области нещо е мръднало")


if __name__ == "__main__":
    unittest.main()
