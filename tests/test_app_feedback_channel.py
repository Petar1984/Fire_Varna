# -*- coding: utf-8 -*-
u"""Лот О · Г-О1…Г-О9 — the app-feedback channel: a sixth report type about the APP.

    python -m unittest tests.test_app_feedback_channel

The „+“ menu gains a sixth entry — „Проблем или идея за приложението“ — behind the
report modal it already owns: six tiles for the kind, a read-only box that says
exactly what the app will send, and one sentence, required only for an idea or
„Друго“. No name is asked and none is sent (Р1): on a public repository a name adds
nothing to an app bug, so `reporter` travels as null and the 2..50 check is skipped
for this type alone. The labels are `app-feedback` / `fb-<kind>` / `pending-review`
and never `report`, which is what keeps the issue out of the map's pipe — the Worker
fetches only `labels=report` (`docs/audits/амандамент_подаване_15.09.md`).

How this gate works, so no reader has to guess:

  * The client is raised HEADLESS through the harness of лот 1. This file IMPORTS
    `tests/test_report_form_operational` as a module (never a copy) and reuses its
    cutter (`span`/`block`), its `index_text` and its form fixtures, so the mechanics
    of the client stay ONE source of truth; the slice, its exports and `ask()` below
    are this lot's own, because it raises other blocks.
  * The blocks are cut by the NAME of each function, never by a line number and never
    by a marker planted in the production code.
  * That split is also WHY the collector is two functions: `feedbackEnvSnapshot()` is
    the only place that touches the browser (typeof-guarded, because the probe has no
    `navigator` and its `getElementById` returns `null`), while
    `buildFeedbackContext(kind, env)` is pure and is driven here with a synthetic
    environment.
  * The reference is the SAME slice at the BASE commit, pinned as a LITERAL under this
    lot's own environment name (`FIRE_VARNA_LOTO_BASE`) — never `FIRE_VARNA_BASE_COMMIT`,
    which other gates move for their own reasons. A base whose blob equals the working
    file is a dead reference and fails loud.
  * Nothing is read at module level and no git runs there.
  * The negative halves doctor COPIES of `index.html` under the temp root — never
    inside the repository — and demand exit 1 plus the text of the assertion they break.

К5 (Gate 2, 15.09) adds the pins the audit found missing: the GPS row of the dropdown
carries the coordinate IN ITS TITLE, so the recorder marks that row while it is drawn
(the chip `.asr-kind.gps` is its marker) and the mask now accepts every shape the
app's own `parseCoordQuery` accepts; a render that found nothing is recorded too; the
error line is one masked, capped line built by a pure function; the 422 answer is read
out of `errors[]` as well and the offline queue keeps a feedback report instead of
dropping it; the feedback form has its own cooldown stamp; `location_method` travels
as null; the two gate holes the audit opened (a deleted `APPLY_TYPES` definition, a
deleted `feedbackOption +` line) each have a pin and a half; and the fourth consumer
of the issue stream, `scripts/build_reports_dashboard.py`, keeps the five hydrant
types only.

К6 (the re-audit of К5) closes the last door the mask left open and three edges
around it: `parseCoordQuery` accepts FOUR and SIX bare numbers as well (degrees
and minutes, with and without seconds, written without one symbol), and a single
word in front of them stopped the parser — no GPS row, no lock — while the empty
render still recorded the numbers; the lock now reads every drawn row, not the
first; ONE function reads a 422 for both the live submit and the queue, so only a
LABEL error parks a feedback report; and the error line loses a query string only
where a query string can live, on a URL-like token, never at a bare „?“.

К7 (the final audit) takes two edges off the mask itself. An ASCII quote is not a
seconds mark: 16 of the 150 place names — a number and a patron in quotes — came back
as the marker and the context box hid the very row the colleague meant, so a real
degree or prime sign, or a hemisphere letter right after the quote, is what makes a
coordinate. And a map link is a position whether or not it carries a digit — the OSM
short link carries none and used to travel verbatim — so every http(s) token is
`[линк]`.

No coordinate stands in this file in any shape: every coordinate-looking string the
mask is measured against is built out of repeated digits.
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
TESTS = REPO / "tests"
if str(TESTS) not in sys.path:        # the лот 1 harness travels as a module, not as a copy
    sys.path.insert(0, str(TESTS))
import test_report_form_operational as lot1   # noqa: E402 - the path has to come first

# The base of THIS lot, as a literal under its own name (план §0.7).
BASE_LITERAL = "758f35e"
BASE = os.environ.get("FIRE_VARNA_LOTO_BASE") or BASE_LITERAL

# The doctored copies of the eight halves live here - never in the tree (план §0.6).
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lotO"

MODULE = "tests.test_app_feedback_channel"

TYPE = "app_feedback"
OLD_TYPES = ("exists_confirmed", "missing", "wrong_location", "damaged", "new_hydrant")
KINDS = ("address", "report", "map", "freeze", "idea", "other")
KIND_LABELS = {
    "address": u"Адрес / търсене",
    "report": u"Доклад за хидрант",
    "map": u"Картата",
    "freeze": u"Замръзва / не се отваря",
    "idea": u"Предложение",
    "other": u"Друго",
}
REQUIRED_KINDS = ("idea", "other")

# The head of the issue, in the order the contract fixes it: the two new keys sit
# right after `description` (амандамент 15.09 §1).
HEAD_ORDER = ("report_id", "report_type", "timestamp", "reporter", "hydrant_ref",
              "expected_coord", "reported_coord", "location_method", "app_version",
              "free_text", "terrain_description", "description",
              "feedback_kind", "feedback_context", "damage_description",
              "hydrant_type_at_location", "type", "operational_status")
# What may never stand in the context, under any name.
FORBIDDEN_CONTEXT_KEYS = ("lat", "lon", "coords", "latitude", "longitude")

# The blocks of the slice, in the order they are raised in.
ANCHORS = (
    "const OPERATIONAL_LABELS = {",
    "function escapeHtml(s) {",
    "function radioRowHTML(field, options, selected) {",
    "const NOTE_HINT_HTML =",
    "const AT_HYDRANT_TYPES =",
    "function hydrantPickersHTML(d) {",
    "const FEEDBACK_KINDS = [",
    "function feedbackKind(id) {",
    "const COORD_MARK = '[координати]';",
    "const COORD_SHAPES = [",
    "function maskFeedbackQuery(q) {",
    "function feedbackEnvSnapshot() {",
    "function buildFeedbackContext(kind, env) {",
    "const FB_CTX_LABELS = {",
    "function renderFeedbackContext(kind, env) {",
    "function feedbackErrorLine(message, filename, lineno) {",
    "function isLabelError(json) {",
    "function typeFieldsHTML(t, d) {",
    "function dedupHash(report) {",
    "function labelsForType(",
    "function hydrantTypeLabel(typeValue) {",
    "function buildIssueTitle(report) {",
    "function yamlValue(v) {",
    "function buildReportYAML(report) {",
    "function buildIssueBody(report) {",
)
# The blocks BORN in this lot: at the base they are missing by construction, and
# only there is their absence allowed.
BASE_OPTIONAL = ("const FEEDBACK_KINDS = [",
                 "function feedbackKind(id) {",
                 "const COORD_MARK = '[координати]';",
                 "const COORD_SHAPES = [",
                 "function maskFeedbackQuery(q) {",
                 "function feedbackEnvSnapshot() {",
                 "function buildFeedbackContext(kind, env) {",
                 "const FB_CTX_LABELS = {",
                 "function renderFeedbackContext(kind, env) {",
                 "function feedbackErrorLine(message, filename, lineno) {",
                 "function isLabelError(json) {")

EXPORTS = ["typeFieldsHTML", "FEEDBACK_KINDS", "feedbackKind", "maskFeedbackQuery",
           "buildFeedbackContext", "renderFeedbackContext", "dedupHash",
           "labelsForType", "buildIssueTitle", "buildReportYAML", "buildIssueBody",
           "feedbackErrorLine", "isLabelError"]

# The source lines this lot pins by hand, with the shape the base carries.
FEEDBACK_OPTION_HEAD = u"const feedbackOption = hydrant ? '' :"
FEEDBACK_DATA_TYPE = u'data-type="%s"' % TYPE
NAME_FIELD_NEW = u"      (reportType === 'app_feedback' ? '' : nameFieldHTML(reportDraft.reporter)) +"
NAME_FIELD_OLD = u"      nameFieldHTML(reportDraft.reporter) +"
NAME_CHECK_NEW = (u"    if (reportType !== 'app_feedback' && "
                  u"(!r || r.length < MIN_NAME_LEN || r.length > MAX_NAME_LEN)) {")
NAME_CHECK_OLD = u"    if (!r || r.length < MIN_NAME_LEN || r.length > MAX_NAME_LEN) {"
REPORTER_NEW = u"      reporter: reportType === 'app_feedback' ? null : d.reporter,"
REPORTER_OLD = u"      reporter: d.reporter,"
APPLY_GUARD = u"      if (!APPLY_TYPES.has(type)) continue;"
TYPE_GUARD = u"      if (!type) continue;"
NOTE_CALL = u"extractReportNote"
RETRY_WITHOUT_LABELS = u"postIssue(url, payload, true)"
RELEASE_FINGERPRINT = u"String(ADDRESS_QUARTERS_SHA256).slice(0, 12)"

# К3 — the two always-on recorders.
ERROR_LISTENERS = (u"window.addEventListener('error', function (e) {",
                   u"window.addEventListener('unhandledrejection', function (e) {")
LAST_ERROR = u"__fvLastError"
LAST_SEARCH = u"__fvLastSearch"
WATCHER = u"function watchLastSearch() {"
SEARCH_IIFE = u"(function initAddressSearch() {"

# К4 — the title, the name of the type and the guarded recorder of the picker.
TITLE_ADDRESS = u"[app_feedback] " + KIND_LABELS["address"]
TITLE_UNKNOWN_KIND = u"[app_feedback] ?"
TITLE_AT_BASE = u"[app_feedback] unknown"
TYPE_NAME = u"Проблем или идея за приложението"
LAST_REPORT_TYPE = u"__fvLastReportType = t"
PICKER_RECORDER = u"        if (t !== 'app_feedback') window.__fvLastReportType = t;"

# К5 — the source lines of the Gate 2 fixes.
APPLY_DEF = u"const APPLY_TYPES = new Set(["
FEEDBACK_OPTION_USE = u"          feedbackOption +"
THROTTLE_STAMP = u"  let lastFeedbackSubmitTs = 0;"
THROTTLE_ARM = u"    if (isFeedback) lastFeedbackSubmitTs = now; else lastSubmitTs = now;"
THROTTLE_ARM_OLD = u"    lastSubmitTs = now;"
LOCATION_METHOD_OLD = (u"    const location_method = (reportType === 'new_hydrant' "
                       u"|| reportType === 'wrong_location')")
LOCATION_METHOD_NEW = u"    const location_method = reportType === 'app_feedback' ? null"
GPS_CHIP = u"'asr-kind gps'"
GPS_MARKER = u"querySelector('.asr-kind.gps')"
COORD_ITEM = u"function buildCoordItem(r, idx) {"
COORD_TITLE_LINE = u"title.textContent = coordTitle(r)"
SHOW_STATUS_LINE = (u"      const d = document.createElement('div'); "
                    u"d.className = 'asr-status'; d.textContent = text;")
HIDE_RESULTS_LINE = (u"    function hideResults() { resultsEl.classList.remove('visible'); "
                     u"resultsEl.replaceChildren(); currentResults = []; }")
ERROR_LINE_FN = u"function feedbackErrorLine(message, filename, lineno) {"
GENERAL_422 = u"      flashStatus('Системна грешка 422."
QUEUE_422 = u"res.status === 422 && item.report"
QUEUE_FLASH = u"Докладът за приложението чака етикетите в GitHub — пази се локално"
SKIPPED_LINE = u"прескочени (не са доклади за хидрант): %d"

# К6 — the source lines of the re-audit's fixes.
BARE_RULE_LINE = u"    if (bare) return COORD_MARK;"
ANY_COORD_ROW = u"    const anyCoordRow = (rows) => Array.from(rows).some(isCoordRow);"
ANY_COORD_USE = u"query: anyCoordRow(rows) ? COORD_MARK :"
FIRST_ROW_ONLY = u"isCoordRow(rows[0])"
LABEL_ERROR_FN = u"function isLabelError(json) {"
LABEL_ERROR_CALL = u"isLabelError(res.json)"
QUEUE_LABEL_ONLY = u"                   && isLabelError(res.json)) {"
PROMISE_PREFIX = u"    window.__fvLastError = ('promise: ' +"

# What the halves hunt for: the text of the assertion, never a method name.
NEEDLE_LABELS = u"етикетите на обратната връзка"
NEEDLE_MASK = u"маската на заявката"
NEEDLE_APPLY = u"APPLY_TYPES"
NEEDLE_CONTEXT = u"feedback_context"
NEEDLE_APPLY_DEF = u"дефиницията на APPLY_TYPES"
NEEDLE_PICKER_USE = u"шестият бутон не влиза в менюто"
NEEDLE_THROTTLE = u"собствен дросел"
NEEDLE_GPS_ROW = u"GPS редът"
NEEDLE_EMPTY = u"празното изчертаване"
NEEDLE_ERRLINE = u"редът на грешката"
NEEDLE_422 = u"етикетната грешка в errors[]"
NEEDLE_QUEUE = u"опашката изхвърля обратната връзка"
NEEDLE_LOCATION = u"location_method"
NEEDLE_DASHBOARD = u"дневникът брои"
NEEDLE_BARE = u"правилото за четири голи числа"
NEEDLE_EVERY_ROW = u"ключалката гледа само първия ред"
NEEDLE_ONE_READING = u"четенето на 422"
NEEDLE_QUOTE = u"кавичката на името"
NEEDLE_LINK = u"линкът в заявката"


# --------------------------------------------------------------------------
# The base blob - read inside a method, never at import
# --------------------------------------------------------------------------

def base_text(test):
    u"""The blob of `<BASE>:index.html`. A dead reference is a failure, not a skip."""
    proc = subprocess.run(["git", "-C", str(REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html — базата е неразрешима: %s"
                  % (BASE, proc.stderr.decode("utf-8", "replace")[:300]))
    text = proc.stdout.decode("utf-8")
    if text == lot1.index_text(test):
        test.fail(u"база равна на кандидата — базата %s е равна на работния файл" % BASE)
    return text


# --------------------------------------------------------------------------
# The headless harness - this lot's own slice, the лот 1 cutter
# --------------------------------------------------------------------------

def build_slice(test, text, base=False):
    parts = []
    for anchor in ANCHORS:
        piece = lot1.block(test, text, anchor,
                           required=not (base and anchor in BASE_OPTIONAL))
        if piece is not None:
            parts.append(piece)
    return "\n".join(parts)


def ask(test, text, asks, base=False):
    u"""Raise the slice in `tests/granitsi_client_probe.mjs` and return its answers."""
    node = shutil.which("node")
    if node is None:
        test.fail(u"node липсва — гейтът е гейт, не пропуснат тест")
    payload = {"slice": build_slice(test, text, base=base),
               "exports": EXPORTS, "asks": asks}
    proc = subprocess.run([node, str(lot1.PROBE)],
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


def call(name, args):
    return {"ask": "call", "name": name, "args": args}


def one_line(test, text, needle, where):
    u"""The ONE line that carries `needle`. Anything else is a failure, not a guess."""
    lines = [line for line in text.split("\n") if needle in line]
    if len(lines) != 1:
        test.fail(u"%s: редът с %r стои %d пъти, не веднъж" % (where, needle, len(lines)))
    return lines[0]


# --------------------------------------------------------------------------
# Fixtures - a draft, a synthetic environment, a synthetic report
# --------------------------------------------------------------------------

def fb_draft(kind=u"", description=u"", worked_before=u""):
    u"""What `showReportModal` hands to `typeFieldsHTML` for this type."""
    return {"feedback_kind": kind, "description": description,
            "worked_before": worked_before}


# The one coordinate-looking string of the lot, BUILT out of repeated digits so no
# pair in Varna's range stands in a tracked file (план §0.6).
COORD_LOOKING_QUERY = (u"1" * 2 + u"." + u"1" * 6 + u", " + u"2" * 2 + u"." + u"2" * 6)
PLAIN_QUERY = u"бл. 5 Аспарухово"

# К5 (а) — every shape the app's own `parseCoordQuery` accepts, built the same way.
A, B = u"1" * 2, u"2" * 2
COORD_MARK = u"[координати]"
# The title of the GPS row: `coordTitle` prints five decimals (index.html).
GPS_ROW_TITLE = A + u"." + u"1" * 5 + u", " + B + u"." + u"2" * 5
COORD_SHAPE_QUERIES = (
    COORD_LOOKING_QUERY,                                   # the six-decimal pair
    A + u"." + A + u", " + B + u"." + B,                   # a pair with two decimals
    A + u"," + A + u" " + B + u"," + B,                    # the Bulgarian comma pair
    A + u"°12'50.8\"N " + B + u"°54'52.9\"E",   # degrees-minutes-seconds
    u"geo:" + A + u"." + A + u"," + B + u"." + B,          # the geo: URI of a phone
    GPS_ROW_TITLE,                                         # what the GPS row SHOWS
)
PLAIN_QUERIES = (PLAIN_QUERY, u"бл 5 аспарухово", u"ул. Струга 12")
# К6 (а) — the BARE degrees-minutes(-seconds) `parseCoordQuery` takes as well,
# built out of repeated digits like every other coordinate-looking string here.
BARE_NUMBER_QUERIES = (
    A + u" 12 50.8 " + B + u" 54 52.9",          # six numbers, two with a fraction
    A + u" 12.846 " + B + u" 54.882",            # four numbers, two with a fraction
    A + u" 12 51 " + B + u" 54 53",              # six whole numbers
    u"Варна " + A + u" 12 50.8 " + B + u" 54 52.9",   # a word in front stops the parser
)
# What a colleague really types: three numbers, and four whole ones.
ADDRESS_QUERIES = (u"ул. Струга 12 вх. 2 ет. 3", u"бл 5 вх 2 ап 12 ет 4")
# К7 (а) — a number and a patron in quotes is a NAME. Both shapes stand in the
# delivered payload; the mask used to read the quote after them as a seconds mark.
QUOTED_NAME_QUERIES = (u'ОУ 5 "Проф. Марин Дринов"', u"ДГ 12 'Слънце'")
# ... while degrees-minutes(-seconds) written WITHOUT a degree sign stays a
# coordinate: the quote counts when a hemisphere letter stands right after it.
QUOTE_DMS_QUERIES = (
    A + u" 12'50.8\"N " + B + u" 54'52.9\"E",    # the seconds mark, no degree sign
    A + u" 12'N " + B + u" 54'E",                # four whole numbers - the letters name them
)
# К7 (б) — every http(s) token, with or without a digit in it.
LINK_MARK = u"[линк]"
MAP_LINK = u"https://maps.google.com/?q=" + A + u"." + A + u"," + B + u"." + B
LINK_QUERIES = (u"https://osm.org/go/xcXbHf", MAP_LINK)
LINK_IN_TEXT = (u"виж " + MAP_LINK + u" тук", u"виж " + LINK_MARK + u" тук")
# The two delivered payloads whose names the mask meets in the search box.
PAYLOAD_FILES = ((u"data/places.json", u"places"), (u"data/hotels.json", u"hotels"))
# A value that carries two decimal numbers is a position whatever its key is.
COORD_VALUE_RE = r"\d[.,]\d[\s\S]*?\d[.,]\d"


def payload_names(test):
    u"""Every `name` the two delivered payloads carry (375 today). Read inside a
    method, from the repository's own files - a missing one is a failure."""
    names = []
    for relative, key in PAYLOAD_FILES:
        path = REPO / relative
        if not path.is_file():
            test.fail(u"липсва %s — пробата на имената няма върху какво да тича" % relative)
        rows = json.loads(path.read_text(encoding="utf-8")).get(key) or []
        names += [row.get("name") or u"" for row in rows if isinstance(row, dict)]
    names = [name for name in names if name]
    if len(names) < 300:
        test.fail(u"пробата на имената е празна: %d имена" % len(names))
    return names


def env_fixture(query=PLAIN_QUERY, **over):
    u"""A synthetic environment: what `feedbackEnvSnapshot()` would hand the builder."""
    env = {
        "app_version": "merged-2026-05-05",
        "online": True,
        "device": "Android / Chrome",
        "screen": "375x812",
        "mode": "top",
        "basemap": "osm",
        "release": "abcdef123456",
        "worked_before": u"работеше преди",
        "last_search": {"query": query, "rows_shown": 3,
                        "first_row": u"ул. Дрин 5", "selected_row": u"ул. Дрин 7"},
        "last_error": u"TypeError: x is not a function @index.html:1",
        "last_report_type": "damaged",
        "queued": 0,
        "hydrant_id": "vik_0001",
        "zoom": 15,
        "points": 7400,
        "sw": "active",
        "memory_gb": 4,
        "where": u"карта",
    }
    env.update(over)
    return env


def feedback_report(kind="address", description=u"Търсенето дава друг блок.",
                    context=u"{}"):
    u"""A report of this type in the shape `buildReportObject` emits it."""
    return {
        "report_id": "00000000-0000-4000-8000-000000000000",
        "report_type": TYPE,
        "timestamp": "2026-09-15T12:00:00+03:00",
        "reporter": None,
        "hydrant_ref": None,
        "expected_coord": None,
        "reported_coord": None,
        # К5 (е) — this type carries no location at all (амандамент §1 v1.1).
        "location_method": None,
        "app_version": "merged-2026-05-05",
        "free_text": None,
        "terrain_description": None,
        "description": description,
        "feedback_kind": kind,
        "feedback_context": context,
        "damage_description": None,
        "hydrant_type_at_location": None,
        "type": None,
        "operational_status": None,
    }


def hydrant_report(report_type="damaged"):
    u"""A report of one of the FIVE old types, in the shape `buildReportObject`
    emits it — the other half of the dashboard's pair (К5 (з))."""
    return {
        "report_id": "00000000-0000-4000-8000-000000000001",
        "report_type": report_type,
        "timestamp": "2026-09-15T12:05:00+03:00",
        "reporter": u"Петър",
        "hydrant_ref": "vik_0001",
        "expected_coord": None,
        "reported_coord": None,
        "location_method": "hydrant_ref",
        "app_version": "merged-2026-05-05",
        "free_text": None,
        "terrain_description": None,
        "description": None,
        "feedback_kind": None,
        "feedback_context": None,
        "damage_description": u"Капачката липсва.",
        "hydrant_type_at_location": None,
        "type": u"надземен",
        "operational_status": "not_working",
    }


def head_of(test, body):
    u"""The YAML head of an issue body as an ordered list of (key, raw value)."""
    marker = "\n---\n"
    if marker not in body:
        test.fail(u"тялото на issue-то няма затваряща черта на главата")
    head = body[:body.index(marker)]
    rows = []
    for line in head.split("\n"):
        if line == "---" or not line.strip():
            continue
        if ": " not in line:
            test.fail(u"ред в главата без ключ: %r" % line[:80])
        key, value = line.split(": ", 1)
        rows.append((key, value))
    return rows


def markdown_of(body):
    marker = "\n---\n"
    return body[body.index(marker) + len(marker):]


# --------------------------------------------------------------------------
# Г-О1…Г-О7 · the form, the labels, the head, the mask, the dedup
# --------------------------------------------------------------------------

class AppFeedbackFormTest(unittest.TestCase):

    def test_the_six_tiles_and_the_one_sentence(self):
        u"""Г-О1 — six kinds, one textarea of 500, the star only where a sentence IS
        the content, and the box that says what the app will send."""
        text = lot1.index_text(self)
        asks = [call("typeFieldsHTML", [TYPE, fb_draft(kind)]) for kind in ("",) + KINDS]
        answers = ask(self, text, asks)
        for kind, html in zip(("",) + KINDS, answers):
            where = u"вид %r" % (kind or u"без избор")
            for other in KINDS:
                self.assertEqual(html.count(u'data-val="%s"' % other), 1,
                                 u"%s: плочката %s не стои точно веднъж" % (where, other))
                self.assertIn(KIND_LABELS[other], html,
                              u"%s: липсва българският етикет на %s" % (where, other))
            self.assertEqual(html.count(u'data-radio="feedback_kind"'), 1,
                             u"%s: редът с плочките не стои точно веднъж" % where)
            self.assertEqual(html.count(u'id="fbCtx"'), 1,
                             u"%s: кутията „Какво ще изпратим автоматично“ липсва" % where)
            self.assertEqual(html.count(u'maxlength="500"'), 1,
                             u"%s: изречението не е ограничено на 500 знака (Р6)" % where)
            self.assertIn(u"Без имена и лични данни", html,
                          u"%s: подсказката за лични данни липсва (Р6)" % where)
            self.assertEqual(html.count(u'data-radio="worked_before"'), 1,
                             u"%s: редът „Работеше ли преди?“ липсва (Р4)" % where)
            self.assertNotIn(u'data-field="reporter"', html,
                             u"%s: формата иска име (Р1)" % where)
            star = u'<span class="req" id="fbReq">*</span>'
            if kind in REQUIRED_KINDS:
                self.assertIn(star, html, u"%s: изречението не е задължително" % where)
            else:
                self.assertNotIn(star, html, u"%s: изречението е обявено за задължително" % where)
                self.assertIn(u"(по желание)", html, u"%s: липсва „(по желание)“" % where)
            selected = html.count(u"radio-chip fb-tile selected")
            self.assertEqual(selected, 1 if kind else 0,
                             u"%s: избраните плочки са %d" % (where, selected))
            # Р4 — the question is meaningless for an idea, so it is hidden there.
            hidden = u'<div class="field hidden" id="fld_worked_before">' in html
            self.assertEqual(hidden, kind == "idea",
                             u"%s: видимостта на „Работеше ли преди?“ е обърната" % where)

    def test_the_five_old_branches_are_byte_equal_to_the_base(self):
        u"""Г-О2 — the five forms that existed before this lot did not move."""
        text = lot1.index_text(self)
        base = base_text(self)
        cases, asks = [], []
        for form in OLD_TYPES:
            for name, draft in lot1.all_fixtures():
                cases.append((form, name))
                asks.append(lot1.call(form, draft))
        candidate = ask(self, text, asks)
        reference = ask(self, base, asks, base=True)
        for (form, name), got, want in zip(cases, candidate, reference):
            self.assertTrue(got == want,
                            u"%s / %s: клонът не е байт за байт равен на базата %s"
                            % (form, name, BASE))

    def test_the_sixth_button_stands_once_and_only_without_a_hydrant(self):
        u"""Г-О3 — the sixth entry exists on ONE line, and the four hydrant buttons
        of the picker are byte-equal to the base."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(FEEDBACK_DATA_TYPE), 0,
                         u"мъртъв пин: базата %s вече носи %s" % (BASE, FEEDBACK_DATA_TYPE))
        line = one_line(self, text, FEEDBACK_DATA_TYPE, u"шестият бутон")
        self.assertIn(FEEDBACK_OPTION_HEAD, line,
                      u"шестият бутон не виси на `hydrant ? '' :` — виждат го и при хидрант")
        # К5 (ж) — Д2 на одита: a declared button that nothing concatenates
        # disappears from the rendered menu with every test still green.
        self.assertEqual(text.count(FEEDBACK_OPTION_HEAD), 1,
                         u"декларацията на шестия бутон стои %d пъти, не веднъж"
                         % text.count(FEEDBACK_OPTION_HEAD))
        self.assertEqual(text.count(FEEDBACK_OPTION_USE), 1,
                         u"%s: редът `feedbackOption +` стои %d пъти, не веднъж"
                         % (NEEDLE_PICKER_USE, text.count(FEEDBACK_OPTION_USE)))
        for old in OLD_TYPES:
            marker = u'data-type="%s"' % old
            self.assertEqual(one_line(self, text, marker, u"бутон %s" % old),
                             one_line(self, base, marker, u"бутон %s" % old),
                             u"бутонът %s в пикера се е променил срещу базата %s" % (old, BASE))

    def test_the_labels_carry_the_kind_and_never_report(self):
        u"""Г-О4 — app-feedback / fb-<kind> / pending-review, and the five old sets
        byte-equal to the base."""
        text = lot1.index_text(self)
        base = base_text(self)
        asks = [call("labelsForType", [{"report_type": TYPE, "feedback_kind": kind}])
                for kind in KINDS]
        asks += [call("labelsForType", [{"report_type": old}]) for old in OLD_TYPES]
        answers = ask(self, text, asks)
        reference = ask(self, base, [call("labelsForType", [old]) for old in OLD_TYPES],
                        base=True)
        for kind, labels in zip(KINDS, answers[:len(KINDS)]):
            self.assertEqual(labels, ["app-feedback", "fb-" + kind, "pending-review"],
                             u"%s: %s не са трите подписани (%r)"
                             % (kind, NEEDLE_LABELS, labels))
            self.assertNotIn("report", labels,
                             u"%s: %s носят „report“ — докладът влиза в тръбата на картата"
                             % (kind, NEEDLE_LABELS))
        for old, got, want in zip(OLD_TYPES, answers[len(KINDS):], reference):
            self.assertEqual(got, want,
                             u"етикетите на %s се промениха срещу базата %s" % (old, BASE))

    def test_the_head_carries_the_two_keys_and_no_coordinate(self):
        u"""Г-О5 — the head of the issue, its order, its parseable context and the
        one sentence that stands exactly once in the markdown."""
        text = lot1.index_text(self)
        sentence = u"Търсенето дава друг блок."
        built = ask(self, text, [call("buildFeedbackContext", ["address", env_fixture()])])[0]
        report = feedback_report(context=json.dumps(built, ensure_ascii=False),
                                 description=sentence)
        body = ask(self, text, [call("buildIssueBody", [report])])[0]
        rows = head_of(self, body)
        keys = [key for key, _ in rows]
        self.assertEqual(tuple(keys), HEAD_ORDER,
                         u"редът на главата не е подписаният — %s не стои след description"
                         % NEEDLE_CONTEXT)
        head = dict(rows)
        self.assertEqual(head["reporter"], "null", u"главата носи подател (Р1)")
        for key in ("hydrant_ref", "expected_coord", "reported_coord",
                    "location_method", "type", "operational_status"):
            self.assertEqual(head[key], "null",
                             u"главата носи %s за доклад, който не е за хидрант" % key)
        self.assertEqual(head["feedback_kind"], '"address"', u"главата не носи вида")
        # Double parse: the head carries a JSON STRING, on ONE line (the Worker
        # reads the head line by line).
        context = json.loads(json.loads(head[NEEDLE_CONTEXT]))
        self.assertTrue(isinstance(context, dict) and context,
                        u"%s не се парсва в речник" % NEEDLE_CONTEXT)
        for forbidden in FORBIDDEN_CONTEXT_KEYS:
            self.assertNotIn(forbidden, context,
                             u"%s носи ключ %s — координата в контекста"
                             % (NEEDLE_CONTEXT, forbidden))
        # К5 (а) — Б1 на одита: the gate read the NAMES of the keys and was green
        # over a payload whose VALUES carried the coordinate. Now the values are
        # judged too, over a context built from a search that WAS a coordinate.
        rows = {"query": GPS_ROW_TITLE, "rows_shown": 1,
                "first_row": GPS_ROW_TITLE, "selected_row": GPS_ROW_TITLE}
        leaky = ask(self, text, [call("buildFeedbackContext",
                                      ["address", env_fixture(last_search=rows)])])[0]
        for key, value in leaky.items():
            self.assertIsNone(re.search(COORD_VALUE_RE, u"%s" % (value,)),
                              u"%s носи стойност с две десетични числа: %s = %r"
                              % (NEEDLE_CONTEXT, key, value))
        markdown = markdown_of(body)
        self.assertEqual(markdown.count(sentence), 1,
                         u"текстът на подателя стои %d пъти в markdown-а"
                         % markdown.count(sentence))
        self.assertNotIn(u"**Подател:**", markdown,
                         u"markdown-ът печата „Подател“ за доклад без подател")

    def test_a_coordinate_looking_query_is_masked(self):
        u"""Г-О6 — the mask, the release fingerprint and the per-kind keys."""
        text = lot1.index_text(self)
        asks = [call("buildFeedbackContext", ["address", env_fixture(query=COORD_LOOKING_QUERY)]),
                call("buildFeedbackContext", ["address", env_fixture()]),
                call("buildFeedbackContext", ["idea", env_fixture()]),
                call("buildFeedbackContext", ["freeze", env_fixture()])]
        masked, plain, idea, freeze = ask(self, text, asks)
        self.assertEqual(masked["query"], u"[координати]",
                         u"%s пропуска координатна заявка: %r"
                         % (NEEDLE_MASK, masked["query"]))
        self.assertEqual(plain["query"], PLAIN_QUERY,
                         u"%s изяде обикновен адрес: %r" % (NEEDLE_MASK, plain["query"]))
        self.assertNotIn("query", idea, u"предложението носи заявка от търсачката")
        self.assertNotIn("worked_before", idea,
                         u"предложението носи „работеше ли преди“ (Р4)")
        self.assertIn("worked_before", freeze, u"замръзването губи „работеше ли преди“ (Р4)")
        self.assertEqual(freeze["last_error"], env_fixture()["last_error"],
                         u"замръзването не носи последната грешка")
        for context in (masked, plain, idea, freeze):
            for forbidden in FORBIDDEN_CONTEXT_KEYS:
                self.assertNotIn(forbidden, context,
                                 u"контекстът носи ключ %s" % forbidden)
        # Н6 — the fingerprint of the release is the index the gates already pin.
        self.assertEqual(text.count(RELEASE_FINGERPRINT), 1,
                         u"отпечатъкът на изданието не стои точно веднъж")

    def test_two_different_texts_are_two_reports(self):
        u"""Г-О7 — Р5: the kind, the sentence and the query separate two reports."""
        text = lot1.index_text(self)
        first = feedback_report(description=u"Първо изречение.")
        second = feedback_report(description=u"Второ изречение.")
        other_kind = feedback_report(kind="map", description=u"Първо изречение.")
        one_query = feedback_report(description=u"Едно и също.",
                                    context=json.dumps({"query": u"Аспарухово"},
                                                       ensure_ascii=False))
        two_query = feedback_report(description=u"Едно и също.",
                                    context=json.dumps({"query": u"Чайка"},
                                                       ensure_ascii=False))
        same = feedback_report(description=u"Първо изречение.")
        asks = [call("dedupHash", [r]) for r in
                (first, second, other_kind, one_query, two_query, same)]
        h1, h2, h3, h4, h5, h6 = ask(self, text, asks)
        self.assertNotEqual(h1, h2, u"два различни текста дават един и същ отпечатък")
        self.assertNotEqual(h1, h3, u"два различни вида дават един и същ отпечатък")
        self.assertNotEqual(h4, h5, u"две различни заявки дават един и същ отпечатък")
        self.assertEqual(h1, h6, u"същият доклад дава два различни отпечатъка")

    def test_apply_reports_refuses_a_type_outside_the_allowlist(self):
        u"""Г-О8 — the third guard: the allowlist is checked before any note is written."""
        text = lot1.index_text(self)
        base = base_text(self)
        block = lot1.block(self, text, "function applyReports(reports) {")
        reference = lot1.block(self, base, "function applyReports(reports) {")
        self.assertNotIn(NEEDLE_APPLY, reference,
                         u"мъртъв пин: базата %s вече носи %s" % (BASE, NEEDLE_APPLY))
        self.assertEqual(block.count(APPLY_GUARD), 1,
                         u"%s не пази applyReports" % NEEDLE_APPLY)
        self.assertLess(block.index(TYPE_GUARD), block.index(APPLY_GUARD),
                        u"%s стои преди проверката за вид" % NEEDLE_APPLY)
        self.assertLess(block.index(APPLY_GUARD), block.index(NOTE_CALL),
                        u"%s стои СЛЕД писането на бележката" % NEEDLE_APPLY)
        # К5 (ж) — Д1 на одита: the guard alone was pinned, so deleting the
        # DEFINITION left thirteen green tests and a ReferenceError on the first
        # poll of the live map.
        self.assertEqual(base.count(APPLY_DEF), 0,
                         u"мъртъв пин: базата %s вече носи %s" % (BASE, APPLY_DEF))
        self.assertEqual(text.count(APPLY_DEF), 1,
                         u"%s стои %d пъти, не веднъж"
                         % (NEEDLE_APPLY_DEF, text.count(APPLY_DEF)))
        definition = one_line(self, text, APPLY_DEF, NEEDLE_APPLY_DEF)
        for old in OLD_TYPES:
            self.assertIn(u"'%s'" % old, definition,
                          u"%s губи %s" % (NEEDLE_APPLY_DEF, old))
        self.assertNotIn(TYPE, definition,
                         u"%s пуска и обратната връзка до бележката" % NEEDLE_APPLY_DEF)

    def test_the_422_branch_queues_instead_of_dropping_the_labels(self):
        u"""Г-О9 — Н4: the labels are the channel, so they are never stripped."""
        text = lot1.index_text(self)
        base = base_text(self)
        block = lot1.block(self, text, "function handleSubmitResult(")
        reference = lot1.block(self, base, "function handleSubmitResult(")
        self.assertEqual(reference.count(RETRY_WITHOUT_LABELS), 1,
                         u"мъртъв пин: базата %s няма безусловния повторен опит" % BASE)
        self.assertNotIn(TYPE, reference,
                         u"мъртъв пин: базата %s вече познава вида" % BASE)
        guard = u"if (report.report_type === 'app_feedback') {"
        self.assertEqual(block.count(guard), 1,
                         u"422 няма свой клон за обратната връзка")
        self.assertLess(block.index(guard), block.index(RETRY_WITHOUT_LABELS),
                        u"обратната връзка минава през повторния опит без етикети")
        self.assertIn(u"queueReport(report);", block[block.index(guard):
                                                     block.index(RETRY_WITHOUT_LABELS)],
                      u"422 изхвърля доклада вместо да го запази локално")

    def test_every_shape_the_parser_accepts_is_masked(self):
        u"""К5 (а) — Б2 на одита: the mask was measured against ONE six-decimal
        pair while `parseCoordQuery` accepts a pair with a single decimal, the
        Bulgarian comma pair, degrees-minutes-seconds and a `geo:` URI. Each of
        them, and the title the GPS row shows, is the whole query now; a normal
        address goes through untouched. The map link left this list in К7: it is
        marked as a LINK now, with or without a digit (the pin below)."""
        text = lot1.index_text(self)
        asks = [call("maskFeedbackQuery", [q])
                for q in COORD_SHAPE_QUERIES + PLAIN_QUERIES]
        answers = ask(self, text, asks)
        for q, got in zip(COORD_SHAPE_QUERIES, answers):
            self.assertEqual(got, COORD_MARK,
                             u"%s пропуска %r: %r" % (NEEDLE_MASK, q, got))
        for q, got in zip(PLAIN_QUERIES, answers[len(COORD_SHAPE_QUERIES):]):
            self.assertEqual(got, q,
                             u"%s изяде обикновен адрес %r: %r" % (NEEDLE_MASK, q, got))

    def test_four_and_six_bare_numbers_are_masked(self):
        u"""К6 (а) — Б-1 на повторния одит: `parseCoordQuery` accepts FOUR and SIX
        bare numbers too (degrees and minutes, with and without seconds, written
        without one symbol), while the mask knew pairs only; and one word in front
        of them stopped the PARSER, not the leak — no GPS row is drawn, the empty
        render records the query, and ~30 m of accuracy went into a public issue.
        Four numbers with a fraction among them, or six numbers at all, are the
        whole marker now; an address with three of them, or with four whole ones,
        stays exactly as it was typed."""
        text = lot1.index_text(self)
        asks = [call("maskFeedbackQuery", [q])
                for q in BARE_NUMBER_QUERIES + ADDRESS_QUERIES]
        answers = ask(self, text, asks)
        for q, got in zip(BARE_NUMBER_QUERIES, answers):
            self.assertEqual(got, COORD_MARK,
                             u"%s пропуска %r: %r" % (NEEDLE_BARE, q, got))
        for q, got in zip(ADDRESS_QUERIES, answers[len(BARE_NUMBER_QUERIES):]):
            self.assertEqual(got, q,
                             u"%s изяде адрес %r: %r" % (NEEDLE_BARE, q, got))

    def test_a_name_in_quotes_is_not_a_coordinate(self):
        u"""К7 (а) — дефект 2 на финалния одит: the degrees shape read the ASCII
        quote as a seconds mark, so 16 of the 150 place names came back as the
        marker and the context box hid the very row the colleague meant. A real
        degree or prime sign, or a hemisphere letter right after the quote, is
        what makes a coordinate now: the two names stay as they were typed,
        degrees-minutes(-seconds) written without a degree sign stays masked, and
        not one name of the two delivered payloads is touched."""
        text = lot1.index_text(self)
        names = payload_names(self)
        kept, dms = len(QUOTED_NAME_QUERIES), len(QUOTE_DMS_QUERIES)
        asks = [call("maskFeedbackQuery", [q])
                for q in QUOTED_NAME_QUERIES + QUOTE_DMS_QUERIES + tuple(names)]
        answers = ask(self, text, asks)
        for q, got in zip(QUOTED_NAME_QUERIES, answers[:kept]):
            self.assertEqual(got, q,
                             u"%s изяде име в кавички %r: %r" % (NEEDLE_QUOTE, q, got))
        for q, got in zip(QUOTE_DMS_QUERIES, answers[kept:kept + dms]):
            self.assertEqual(got, COORD_MARK,
                             u"%s пропуска %r: %r" % (NEEDLE_QUOTE, q, got))
        eaten = [name for name, got in zip(names, answers[kept + dms:]) if got != name]
        self.assertEqual(eaten, [],
                         u"%s: %d от %d доставени имена са маскирани — %s"
                         % (NEEDLE_QUOTE, len(eaten), len(names), u"; ".join(eaten[:5])))

    def test_a_map_link_is_marked_whatever_it_carries(self):
        u"""К7 (б) — дефект 3 на финалния одит: the shape hunted for a DIGIT
        inside the link, so an OSM short link — which carries none — went into
        the record of a search that drew no GPS row, verbatim. A link is a
        position whatever it is written with: every http(s) token is the link
        marker now, with its query string and its fragment, wherever it stands in
        the query; a query without a link is not touched."""
        text = lot1.index_text(self)
        asks = [call("maskFeedbackQuery", [q])
                for q in LINK_QUERIES + (LINK_IN_TEXT[0],) + PLAIN_QUERIES]
        answers = ask(self, text, asks)
        for q, got in zip(LINK_QUERIES, answers):
            self.assertEqual(got, LINK_MARK,
                             u"%s пропуска %r: %r" % (NEEDLE_LINK, q, got))
        in_text = answers[len(LINK_QUERIES)]
        self.assertEqual(in_text, LINK_IN_TEXT[1],
                         u"%s не маркира линка в изречение: %r" % (NEEDLE_LINK, in_text))
        for got in answers[:len(LINK_QUERIES) + 1]:
            self.assertIsNone(re.search(r"\d", got),
                              u"%s оставя цифра от линка: %r" % (NEEDLE_LINK, got))
        for q, got in zip(PLAIN_QUERIES, answers[len(LINK_QUERIES) + 1:]):
            self.assertEqual(got, q,
                             u"%s изяде заявка без линк %r: %r" % (NEEDLE_LINK, q, got))

    def test_one_reading_of_the_422_serves_both_paths(self):
        u"""К6 (в) — дефект 1 на повторния одит: the queue kept an `app_feedback`
        report on ANY 422 and promised labels for it, so a broken body or title
        parked the record forever under a message that was not true. ONE function
        reads the answer — the same one `handleSubmitResult` reads it with — and
        only a LABEL error waits; every other 422 falls into the drop the five old
        types have always fallen into."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(LABEL_ERROR_FN), 0,
                         u"мъртъв пин: базата %s вече има %s" % (BASE, NEEDLE_ONE_READING))
        self.assertEqual(text.count(LABEL_ERROR_FN), 1,
                         u"%s не стои на едно място" % NEEDLE_ONE_READING)
        shared = lot1.block(self, text, LABEL_ERROR_FN)
        self.assertIn(u"er.field || er.resource || er.code", shared,
                      u"%s не чете %s" % (NEEDLE_ONE_READING, NEEDLE_422))
        self.assertIn(u"/label/i.test(msg)", shared,
                      u"%s не чете съобщението" % NEEDLE_ONE_READING)
        for anchor in ("function handleSubmitResult(", "function retryQueuedReports() {"):
            self.assertIn(LABEL_ERROR_CALL, lot1.block(self, text, anchor),
                          u"%s не минава през %s" % (anchor[:34], NEEDLE_ONE_READING))
        queue = lot1.block(self, text, "function retryQueuedReports() {")
        self.assertIn(QUEUE_LABEL_ONLY, queue,
                      u"опашката пази обратната връзка при ВСЕКИ 422, не само етикетен")
        # Both answers GitHub really sends, through the probe.
        asks = [call("isLabelError", [{"message": u"Validation Failed",
                                       "errors": [{"field": "labels"}]}]),
                call("isLabelError", [{"message": u"Validation Failed",
                                       "errors": [{"field": "body"}]}]),
                call("isLabelError", [{"message": u"Label does not exist"}]),
                call("isLabelError", [{"message": u"Validation Failed"}]),
                call("isLabelError", [None])]
        labels, body, in_message, generic, nothing = ask(self, text, asks)
        self.assertTrue(labels, u"%s: етикетна грешка в errors[] не се познава"
                        % NEEDLE_ONE_READING)
        self.assertFalse(body, u"%s: грешка за тялото минава за етикетна"
                         % NEEDLE_ONE_READING)
        self.assertTrue(in_message, u"%s: етикет в съобщението не се познава"
                        % NEEDLE_ONE_READING)
        self.assertFalse(generic, u"%s: голото „Validation Failed“ минава за етикетна"
                         % NEEDLE_ONE_READING)
        self.assertFalse(nothing, u"%s: празен отговор минава за етикетна"
                         % NEEDLE_ONE_READING)

    def test_the_422_branch_reads_the_errors_array(self):
        u"""К5 (г) — GitHub answers an unknown label with the generic „Validation
        Failed“ and names the label only in `errors[]`, so the message alone let
        the feedback fall through to the general 422 line. The five old types keep
        their branch byte for byte."""
        text = lot1.index_text(self)
        base = base_text(self)
        block = lot1.block(self, text, "function handleSubmitResult(")
        reference = lot1.block(self, base, "function handleSubmitResult(")
        self.assertEqual(reference.count(u"const labelError ="), 0,
                         u"мъртъв пин: базата %s вече чете errors[]" % BASE)
        self.assertEqual(block.count(u"const labelError ="), 1,
                         u"422 не разпознава %s" % NEEDLE_422)
        # К6 (в) — the reading itself moved into `isLabelError`, which the queue
        # shares; the branch has to hang on THAT function and on nothing else.
        self.assertIn(u"const labelError = isLabelError(res.json);", block,
                      u"422 не чете %s през общата функция" % NEEDLE_422)
        self.assertIn(u"er.field || er.resource || er.code",
                      lot1.block(self, text, LABEL_ERROR_FN),
                      u"422 не чете %s" % NEEDLE_422)
        self.assertEqual(block.count(u"if (labelError) {"), 1,
                         u"клонът на етикетите не виси на labelError")
        self.assertEqual(block.count(u"if (msg && /label/i.test(msg)) {"), 0,
                         u"старото условие само по съобщението стои още")
        # The old path — the retry without labels and everything after it —
        # is byte-equal to the base.
        tail = reference[reference.index(RETRY_WITHOUT_LABELS):
                         reference.index(GENERAL_422)]
        self.assertIn(tail, block,
                      u"клонът на петте стари вида при 422 не е байт-равен на базата %s"
                      % BASE)

    def test_the_queue_keeps_a_feedback_report_on_422(self):
        u"""К5 (г) — Д4 на одита: `retryQueuedReports` sent the same labels again
        and threw the record away on 422 with a console line, while the modal had
        promised the opposite. It waits now, and the colleague is told once."""
        text = lot1.index_text(self)
        base = base_text(self)
        block = lot1.block(self, text, "function retryQueuedReports() {")
        reference = lot1.block(self, base, "function retryQueuedReports() {")
        self.assertNotIn(TYPE, reference,
                         u"мъртъв пин: базата %s вече познава вида в опашката" % BASE)
        self.assertEqual(block.count(QUEUE_422), 1,
                         u"%s при 422" % NEEDLE_QUEUE)
        self.assertEqual(block.count(u"remaining.push(item);"), 2,
                         u"%s: записът не остава в опашката" % NEEDLE_QUEUE)
        self.assertEqual(block.count(QUEUE_FLASH), 1,
                         u"%s мълчи пред колегата" % NEEDLE_QUEUE)
        self.assertEqual(block.count(u"let labelsPending = false;"), 1,
                         u"съобщението няма ключ, за да се каже веднъж на обиколка")
        self.assertEqual(block.count(u"if (!labelsPending) {"), 1,
                         u"съобщението се казва на всеки запис, не веднъж на обиколка")
        # The three old outcomes stand byte for byte as the base wrote them.
        old = reference[reference.index(u"        if (res.status === 201) {"):
                        reference.index(u"        } else {")]
        self.assertIn(old, block,
                      u"старите изходи на опашката не са байт-равни на базата %s" % BASE)
        self.assertIn(u"console.warn('[report] queue drop', res.status, item);", block,
                      u"старите видове вече не падат в „queue drop“")

    def test_feedback_has_its_own_cooldown(self):
        u"""К5 (д) — the largest risk to the crew the audit named: feedback armed
        the shared 30 s throttle, so a real hydrant report filed right after it was
        refused with „Изчакай 30 сек“. The two stamps never cross."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(u"lastFeedbackSubmitTs"), 0,
                         u"мъртъв пин: базата %s вече носи %s"
                         % (BASE, u"lastFeedbackSubmitTs"))
        self.assertEqual(text.count(THROTTLE_STAMP), 1,
                         u"обратната връзка няма %s" % NEEDLE_THROTTLE)
        submit = lot1.block(self, text, "function onSubmitClicked(reportType) {")
        lines = [line for line in submit.split("\n") if u"lastSubmitTs" in line]
        self.assertEqual(len(lines), 2,
                         u"%s: редовете с времеви печат в onSubmitClicked са %d, не два\n%s"
                         % (NEEDLE_THROTTLE, len(lines), u"\n".join(lines)))
        for line in lines:
            self.assertIn(u"isFeedback", line,
                          u"%s: общият печат се чете или въоръжава безусловно: %r"
                          % (NEEDLE_THROTTLE, line))
        self.assertEqual(submit.count(THROTTLE_ARM), 1,
                         u"%s: въоръжаването не е разделено" % NEEDLE_THROTTLE)
        base_submit = lot1.block(self, base, "function onSubmitClicked(reportType) {")
        self.assertEqual(base_submit.count(THROTTLE_ARM_OLD), 1,
                         u"мъртъв пин: базата %s няма безусловното въоръжаване" % BASE)
        painter = lot1.block(self, text, "function remainingCooldownMs() {")
        self.assertIn(u"reportDraft.type === 'app_feedback'", painter,
                      u"%s: обратният брояч рисува чуждото чакане" % NEEDLE_THROTTLE)

    def test_location_method_is_null_for_this_type(self):
        u"""К5 (е) — the head said `location_method: "hydrant_ref"` beside a null
        `hydrant_ref`; the amendment says null. The old expression is untouched."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(LOCATION_METHOD_OLD), 1,
                         u"мъртъв пин: старият израз за %s не стои веднъж в базата %s"
                         % (NEEDLE_LOCATION, BASE))
        self.assertEqual(text.count(LOCATION_METHOD_NEW), 1,
                         u"%s не е условен за този вид" % NEEDLE_LOCATION)
        self.assertEqual(text.count(LOCATION_METHOD_OLD), 0,
                         u"%s стои и в стария си безусловен вид" % NEEDLE_LOCATION)
        for line in (u"      ? 'manual_placement'", u"      : 'hydrant_ref';"):
            self.assertEqual(text.count(line), base.count(line),
                             u"клонът %r на %s се е променил срещу базата %s"
                             % (line.strip(), NEEDLE_LOCATION, BASE))

    def test_no_name_is_asked_and_none_is_sent(self):
        u"""Р1 — the name field, the 2..50 check and the payload, all three at once."""
        text = lot1.index_text(self)
        base = base_text(self)
        for old, new, what in ((NAME_FIELD_OLD, NAME_FIELD_NEW, u"полето за име"),
                               (NAME_CHECK_OLD, NAME_CHECK_NEW, u"проверката 2..50"),
                               (REPORTER_OLD, REPORTER_NEW, u"подателят в товара")):
            self.assertEqual(base.count(old), 1,
                             u"мъртъв пин: %s не стои веднъж в базата %s" % (what, BASE))
            self.assertEqual(text.count(new), 1,
                             u"%s не е условна за този вид" % what)
            self.assertEqual(text.count(old), 0,
                             u"%s стои и в стария си безусловен вид" % what)

    def test_the_title_carries_the_kind_and_not_the_hydrant_fallback(self):
        u"""К4 — the issue is titled by the kind's label; the base, which had no
        branch for this type, fell through to the hydrant fallback."""
        text = lot1.index_text(self)
        base = base_text(self)
        asks = [call("buildIssueTitle", [feedback_report(kind="address")]),
                call("buildIssueTitle", [feedback_report(kind="no_such_kind")])]
        titled, unknown = ask(self, text, asks)
        self.assertEqual(titled, TITLE_ADDRESS,
                         u"заглавието не носи името на вида: %r" % titled)
        self.assertEqual(unknown, TITLE_UNKNOWN_KIND,
                         u"непознат вид не дава „?“: %r" % unknown)
        # The pin is alive only because the base answers otherwise.
        at_base = ask(self, base, [asks[0]], base=True)[0]
        self.assertEqual(at_base, TITLE_AT_BASE,
                         u"мъртъв пин: базата %s вече заглавява %r" % (BASE, at_base))

    def test_the_markdown_names_the_sixth_type_in_bulgarian(self):
        u"""К4 — „Тип“ prints the Bulgarian name of the type, like the other
        five, and the raw identifier never reaches the markdown."""
        text = lot1.index_text(self)
        body = ask(self, text, [call("buildIssueBody", [feedback_report()])])[0]
        markdown = markdown_of(body)
        line = u"**Тип:** " + TYPE_NAME
        self.assertEqual(markdown.count(line), 1,
                         u"редът „Тип“ с името на вида стои %d пъти, не веднъж"
                         % markdown.count(line))
        self.assertNotIn(TYPE, markdown,
                         u"markdown-ът печата суровия вид %s вместо името му" % TYPE)

    def test_the_picker_recorder_skips_the_feedback_form_itself(self):
        u"""К4 — the „Доклад за хидрант“ kind has to carry the report the
        colleague came from, never the feedback form he is standing in."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(LAST_REPORT_TYPE), 0,
                         u"мъртъв пин: базата %s вече записва вида на формата" % BASE)
        self.assertEqual(one_line(self, text, LAST_REPORT_TYPE, u"записвачът на пикера"),
                         PICKER_RECORDER,
                         u"записвачът не е предпазен — формата за обратна връзка записва сама себе си")


# --------------------------------------------------------------------------
# К3 · the two always-on recorders, pinned in the source
# --------------------------------------------------------------------------

class RecorderTest(unittest.TestCase):

    def test_the_error_recorder_keeps_one_line_and_no_stack(self):
        u"""Р3 — message plus file basename and line, the LAST one only."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(LAST_ERROR), 0,
                         u"мъртъв пин: базата %s вече записва грешки" % BASE)
        for anchor in ERROR_LISTENERS:
            self.assertEqual(text.count(anchor), 1,
                             u"слушателят %r не стои точно веднъж" % anchor[:40])
            block = lot1.block(self, text, anchor)
            self.assertEqual(block.count(LAST_ERROR), 1,
                             u"слушателят не записва в %s" % LAST_ERROR)
            for forbidden in ("stack", "Stack"):
                self.assertNotIn(forbidden, block,
                                 u"записвачът на грешки носи стек — %r" % forbidden)

    def test_the_recorder_marks_the_gps_row_as_it_is_drawn(self):
        u"""К5 (а) — Б1 на одита: a coordinate query draws a GPS row whose title IS
        the coordinate, and the context sent that title as `first_row` /
        `selected_row` unmasked. The marker of the row is the chip
        `.asr-kind.gps` — the one place the class is drawn — so the row is known
        while it is drawn and the raw value never enters `__fvLastSearch`."""
        text = lot1.index_text(self)
        base = base_text(self)
        # The marker is measured in the code that DRAWS the row, and that code is
        # byte-equal to the base: the lot does not touch the search (ADR 006 D12).
        drawn = lot1.block(self, text, COORD_ITEM)
        self.assertEqual(drawn, lot1.block(self, base, COORD_ITEM),
                         u"%s се рисува другояче от базата %s" % (NEEDLE_GPS_ROW, BASE))
        self.assertEqual(text.count(GPS_CHIP), 1,
                         u"%s: чипът %s стои %d пъти, не веднъж"
                         % (NEEDLE_GPS_ROW, GPS_CHIP, text.count(GPS_CHIP)))
        self.assertIn(COORD_TITLE_LINE, drawn,
                      u"%s вече не носи координатата в заглавието си" % NEEDLE_GPS_ROW)
        block = lot1.block(self, text, WATCHER)
        self.assertIn(GPS_MARKER, block,
                      u"записвачът не разпознава %s" % NEEDLE_GPS_ROW)
        for needed in (u"const markOf = (row) => (isCoordRow(row) ? COORD_MARK : titleOf(row));",
                       ANY_COORD_USE,
                       u"first_row: markOf(rows[0])",
                       u"window.__fvLastSearch.selected_row = markOf(row);"):
            self.assertIn(needed, block,
                          u"%s: %r не се маркира при изчертаването"
                          % (NEEDLE_GPS_ROW, needed[:44]))
        # The builder masks the two titles as well - the second lock, on the value.
        builder = lot1.block(self, text, "function buildFeedbackContext(kind, env) {")
        for key in ("first_row", "selected_row"):
            self.assertIn(u"ctx.%s = search.%s ? maskFeedbackQuery(search.%s) : null;"
                          % (key, key, key), builder,
                          u"%s: %s не минава през маската" % (NEEDLE_MASK, key))

    def test_the_gps_lock_looks_at_every_row(self):
        u"""К6 (б) — дефект 5 на повторния одит: the lock asked `rows[0]` only, so
        a GPS row drawn anywhere but first would have left the raw query in the
        record. Every drawn row is asked now, through the ONE marker the drawing
        code paints."""
        text = lot1.index_text(self)
        block = lot1.block(self, text, WATCHER)
        self.assertIn(ANY_COORD_ROW, block,
                      u"%s: няма проверка по всички редове" % NEEDLE_EVERY_ROW)
        self.assertIn(ANY_COORD_USE, block,
                      u"%s: заявката виси на друга проверка" % NEEDLE_EVERY_ROW)
        self.assertEqual(block.count(FIRST_ROW_ONLY), 0,
                         u"%s (%s стои още)" % (NEEDLE_EVERY_ROW, FIRST_ROW_ONLY))
        self.assertEqual(block.count(GPS_MARKER), 1,
                         u"%s: маркерът на %s стои %d пъти в записвача, не веднъж"
                         % (NEEDLE_EVERY_ROW, NEEDLE_GPS_ROW, block.count(GPS_MARKER)))

    def test_an_empty_render_is_recorded_with_zero_rows(self):
        u"""К5 (б) — Д5 на одита: a search that found nothing was never recorded,
        so the feedback described an EARLIER, successful query. Hiding the list
        still records nothing: `hideResults` empties the container and takes the
        `visible` class off, while `showStatus` leaves one `.asr-status` in it."""
        text = lot1.index_text(self)
        base = base_text(self)
        # Both lines are the search's own and byte-equal to the base: the guard is
        # measured against the code it guards, not against a retyped idea of it.
        for line in (SHOW_STATUS_LINE, HIDE_RESULTS_LINE):
            self.assertEqual(text.count(line), 1,
                             u"%s: редът %r стои %d пъти, не веднъж"
                             % (NEEDLE_EMPTY, line.strip()[:40], text.count(line)))
            self.assertEqual(base.count(line), 1,
                             u"мъртъв пин: базата %s не носи реда %r"
                             % (BASE, line.strip()[:40]))
        self.assertEqual(text.count(u"showStatus('Няма съвпадения')"),
                         base.count(u"showStatus('Няма съвпадения')"),
                         u"%s: изчертаването „Няма съвпадения“ се е променило" % NEEDLE_EMPTY)
        block = lot1.block(self, text, WATCHER)
        self.assertIn(u"results.querySelector('.asr-status')", block,
                      u"%s не се разпознава" % NEEDLE_EMPTY)
        self.assertIn(u"results.classList.contains('visible')", block,
                      u"%s: скритият списък също би записал" % NEEDLE_EMPTY)
        self.assertIn(u"rows_shown: 0", block,
                      u"%s не се записва с нула реда" % NEEDLE_EMPTY)
        self.assertIn(u"first_row: null, selected_row: null", block,
                      u"%s носи редове, каквито не е имало" % NEEDLE_EMPTY)

    def test_the_error_line_is_one_line_masked_and_capped(self):
        u"""К5 (в) — the recorder kept a multi-line message, a URL with its query
        string and numbers that look like a position. One pure function builds the
        line now, and both listeners call it."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(ERROR_LINE_FN), 0,
                         u"мъртъв пин: базата %s вече строи %s" % (BASE, NEEDLE_ERRLINE))
        # К6 (г) — the query string is cut where a query string can live: on the
        # URL in the message and on the file, never at a bare „?“ of a sentence.
        # К7 (б) — and the mask the line goes through marks the URL itself, so
        # what reaches the issue is the marker, never the address of the script.
        asks = [call("feedbackErrorLine", [u"първи ред\nвтори ред\nтрети", u"index.html", 12]),
                call("feedbackErrorLine", [u"boom https://example.org/a.js?token=CANARY",
                                           u"https://example.org/app.js?token=CANARY", 7]),
                call("feedbackErrorLine", [u"при " + COORD_LOOKING_QUERY, u"index.html", 3]),
                call("feedbackErrorLine", [u"A" * 300, u"index.html", 1])]
        one, token, coord, long_line = ask(self, text, asks)
        self.assertEqual(one, u"първи ред @index.html:12",
                         u"%s носи повече от първия ред: %r" % (NEEDLE_ERRLINE, one))
        self.assertNotIn(u"CANARY", token,
                         u"%s носи query string: %r" % (NEEDLE_ERRLINE, token))
        self.assertEqual(token, u"boom " + LINK_MARK + u" @app.js:7",
                         u"%s: %r" % (NEEDLE_ERRLINE, token))
        self.assertEqual(coord, COORD_MARK + u" @index.html:3",
                         u"%s носи координата: %r" % (NEEDLE_ERRLINE, coord))
        self.assertEqual(len(long_line), 200,
                         u"%s не е ограничен на 200 знака (%d)"
                         % (NEEDLE_ERRLINE, len(long_line)))
        for anchor in ERROR_LISTENERS:
            self.assertIn(u"feedbackErrorLine(", lot1.block(self, text, anchor),
                          u"слушателят не минава през %s" % NEEDLE_ERRLINE)

    def test_the_error_line_cuts_only_url_tokens(self):
        u"""К6 (г) — дефекти 2 и 3 на повторния одит: the line was cut at the
        FIRST „?“ of the whole text, so „Защо? няма връзка“ reached the issue as
        „Защо“, and the file never went through the mask, so a `#lat=…` fragment
        survived on it. A query string and a fragment live on a URL: they are cut
        from URL-like tokens in the message and from the file token, and the file
        goes through the mask like the message."""
        text = lot1.index_text(self)
        fragment = u"#lat=" + A + u"." + u"1" * 5
        url = u"https://x.example/app.js" + fragment
        asks = [call("feedbackErrorLine", [u"Защо? няма връзка", u"index.html", 4]),
                call("feedbackErrorLine", [u"boom @" + url, u"index.html", 3]),
                call("feedbackErrorLine", [u"boom", url, 3]),
                call("feedbackErrorLine", [u"boom", u"app.js?token=CANARY", 9]),
                call("feedbackErrorLine", [u"грешка",
                                           u"https://x.example/" + GPS_ROW_TITLE + u".js", 2])]
        question, in_message, in_file, token, coord_file = ask(self, text, asks)
        self.assertEqual(question, u"Защо? няма връзка @index.html:4",
                         u"%s е отрязан на гол въпросителен знак: %r"
                         % (NEEDLE_ERRLINE, question))
        for got in (in_message, in_file):
            self.assertNotIn(u"lat=", got,
                             u"%s носи фрагмент: %r" % (NEEDLE_ERRLINE, got))
            self.assertNotIn(A + u"." + u"1" * 5, got,
                             u"%s носи координата от фрагмент: %r" % (NEEDLE_ERRLINE, got))
        self.assertEqual(in_file, u"boom @app.js:3",
                         u"%s: файлът не се чисти: %r" % (NEEDLE_ERRLINE, in_file))
        self.assertNotIn(u"CANARY", token,
                         u"%s: голото име на файл пази query string: %r"
                         % (NEEDLE_ERRLINE, token))
        self.assertEqual(coord_file, u"грешка @" + COORD_MARK + u":2",
                         u"%s: файлът не минава през маската: %r"
                         % (NEEDLE_MASK, coord_file))
        self.assertEqual(text.count(PROMISE_PREFIX), 1,
                         u"%s губи представката на отказаното обещание" % NEEDLE_ERRLINE)

    def test_the_search_recorder_watches_the_container_from_outside(self):
        u"""Н5 — the observer hangs on the CONTAINER, never on a function of
        initAddressSearch (ADR 006 D12)."""
        text = lot1.index_text(self)
        base = base_text(self)
        self.assertEqual(base.count(LAST_SEARCH), 0,
                         u"мъртъв пин: базата %s вече записва търсения" % BASE)
        block = lot1.block(self, text, WATCHER)
        self.assertIn(u"document.getElementById('addrSearchResults')", block,
                      u"наблюдателят не виси на контейнера на резултатите")
        self.assertIn(u"new MutationObserver(", block, u"няма наблюдател")
        for needed in (u"'.asr-item'", u"'.asr-title'", u"rows_shown", u"first_row",
                       u"selected_row"):
            self.assertIn(needed, block, u"записвачът на търсенето губи %s" % needed)
        for forbidden in ("renderResults", "selectResult"):
            self.assertNotIn(forbidden, block,
                             u"записвачът пипа %s — функция на initAddressSearch (D12)"
                             % forbidden)
        # The block itself has to stand OUTSIDE the IIFE of the address search.
        watcher = lot1.span(self, text, WATCHER)
        search = lot1.span(self, text, SEARCH_IIFE)
        self.assertTrue(watcher[1] < search[0] or watcher[0] > search[1],
                        u"записвачът е ВЪТРЕ в initAddressSearch (редове %s срещу %s)"
                        % (watcher, search))
        self.assertEqual(text.count(u"document.addEventListener('DOMContentLoaded', watchLastSearch);"), 1,
                         u"записвачът не се закача, ако документът още се чете")
        self.assertEqual(text.count(u"    watchLastSearch();"), 1,
                         u"записвачът не се закача, ако документът вече е прочетен")


# --------------------------------------------------------------------------
# К5 (з) · the fourth consumer of the issue stream
# --------------------------------------------------------------------------

class DashboardTest(unittest.TestCase):

    def test_the_dashboard_keeps_the_five_hydrant_types_only(self):
        u"""Д3 на одита: `scripts/build_reports_dashboard.py` fetches every issue
        without a label filter and counted any body carrying a `report_type`, so a
        feedback issue would have inflated the totals, the type split and the
        roster of reporters. It keeps the five hydrant types now and says how many
        bodies it skipped instead of dropping them silently."""
        scripts = str(REPO / "scripts")
        if scripts not in sys.path:
            sys.path.insert(0, scripts)
        import build_reports_dashboard as dash   # noqa: E402 - never at import time
        self.assertEqual(set(dash.KNOWN_REPORT_TYPES), set(OLD_TYPES),
                         u"%s друг набор от видове, не петте на hydrant_core"
                         % NEEDLE_DASHBOARD)
        text = lot1.index_text(self)
        # The two bodies are the ones the client REALLY emits, not retyped heads.
        feedback_body, hydrant_body = ask(self, text, [
            call("buildIssueBody", [feedback_report()]),
            call("buildIssueBody", [hydrant_report()])])
        issues = {101: {"body": feedback_body, "created_at": "2026-09-15T09:00:00Z"},
                  102: {"body": hydrant_body, "created_at": "2026-09-15T09:05:00Z"}}
        rows, skipped = dash.normalise(issues)
        self.assertEqual([r["n"] for r in rows], [102],
                         u"%s и обратната връзка: %r" % (NEEDLE_DASHBOARD, rows))
        self.assertEqual(rows[0]["t"], "damaged",
                         u"%s друг вид: %r" % (NEEDLE_DASHBOARD, rows[0]["t"]))
        self.assertEqual(skipped, 1,
                         u"%s: прескочените са %d, не един" % (NEEDLE_DASHBOARD, skipped))
        source = (REPO / "scripts" / "build_reports_dashboard.py").read_bytes().decode("utf-8")
        self.assertEqual(source.count(SKIPPED_LINE), 1,
                         u"%s: редът с прескочените не се отпечатва точно веднъж"
                         % NEEDLE_DASHBOARD)


# --------------------------------------------------------------------------
# The negative halves - each RUNS and each FALLS with its own needle
# --------------------------------------------------------------------------

class NegativeHalfTest(unittest.TestCase):

    def doctored(self, name, text):
        u"""A doctored copy of `index.html` under the temp root - never in the tree."""
        root = FIXTURES / name
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)
        path = root / "index.html"
        path.write_bytes(text.encode("utf-8"))
        return path

    def run_half(self, path, target, needle):
        # The base travels as the LITERAL: a child that inherited a foreign
        # FIRE_VARNA_LOTO_BASE would fall for somebody else's reason.
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_INDEX_HTML_PATH=str(path),
                           FIRE_VARNA_LOTO_BASE=BASE_LITERAL)
        proc = subprocess.run([sys.executable, "-m", "unittest", target],
                              cwd=str(REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=600)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"половината не падна: изход %d\n%s"
                         % (proc.returncode, out[-900:]))
        self.assertIn(needle, out,
                      u"половината падна, но не по своята причина\n%s" % out[-900:])

    def test_giving_the_report_label_back_turns_the_gate_red(self):
        text = lot1.replace_once(
            self, lot1.index_text(self),
            u"      return ['app-feedback', 'fb-' + kind, 'pending-review'];",
            u"      return ['report', 'fb-' + kind, 'pending-review'];")
        path = self.doctored("label_report_back", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_the_labels_carry_the_kind_and_never_report", NEEDLE_LABELS)

    def test_removing_the_mask_turns_the_gate_red(self):
        text = lot1.index_text(self)
        block = lot1.block(self, text, "function maskFeedbackQuery(q) {")
        text = lot1.replace_once(
            self, text, block,
            u"  function maskFeedbackQuery(q) {\n"
            u"    return String(q == null ? '' : q).trim();\n"
            u"  }")
        path = self.doctored("no_mask", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_a_coordinate_looking_query_is_masked", NEEDLE_MASK)

    def test_removing_the_four_number_rule_turns_the_gate_red(self):
        u"""К6 (е): the shapes stay, the count of bare numbers goes — exactly the
        mask К5 delivered, and exactly the door Б-1 walked through."""
        text = lot1.replace_once(self, lot1.index_text(self),
                                 BARE_RULE_LINE + "\n", u"")
        path = self.doctored("no_bare_number_rule", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_four_and_six_bare_numbers_are_masked", NEEDLE_BARE)

    def test_removing_the_allowlist_turns_the_gate_red(self):
        text = lot1.replace_once(self, lot1.index_text(self), APPLY_GUARD + "\n", u"")
        path = self.doctored("no_apply_types", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_apply_reports_refuses_a_type_outside_the_allowlist", NEEDLE_APPLY)

    def test_deleting_the_allowlist_definition_turns_the_gate_red(self):
        u"""К5 (ж) — Д1: the guard stays, the definition goes."""
        text = lot1.index_text(self)
        line = one_line(self, text, APPLY_DEF, NEEDLE_APPLY_DEF)
        text = lot1.replace_once(self, text, line + "\n", u"")
        path = self.doctored("no_apply_definition", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_apply_reports_refuses_a_type_outside_the_allowlist",
                      NEEDLE_APPLY_DEF)

    def test_deleting_the_sixth_button_from_the_menu_turns_the_gate_red(self):
        u"""К5 (ж) — Д2: the declaration stays, the concatenation goes."""
        text = lot1.replace_once(self, lot1.index_text(self),
                                 FEEDBACK_OPTION_USE + "\n", u"")
        path = self.doctored("no_feedback_option_use", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_the_sixth_button_stands_once_and_only_without_a_hydrant",
                      NEEDLE_PICKER_USE)

    def test_arming_the_shared_cooldown_turns_the_gate_red(self):
        u"""К5 (д): feedback arms the shared stamp again."""
        text = lot1.replace_once(self, lot1.index_text(self),
                                 THROTTLE_ARM, THROTTLE_ARM_OLD)
        path = self.doctored("shared_cooldown", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_feedback_has_its_own_cooldown", NEEDLE_THROTTLE)

    def test_dropping_the_context_from_the_head_turns_the_gate_red(self):
        text = lot1.replace_once(
            self, lot1.index_text(self),
            u"'description','feedback_kind','feedback_context','damage_description',",
            u"'description','feedback_kind','damage_description',")
        path = self.doctored("no_context_key", text)
        self.run_half(path, MODULE + ".AppFeedbackFormTest."
                      "test_the_head_carries_the_two_keys_and_no_coordinate", NEEDLE_CONTEXT)


if __name__ == "__main__":
    unittest.main()
