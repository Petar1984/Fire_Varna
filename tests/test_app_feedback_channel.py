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

# The doctored copies of the four halves live here - never in the tree (план §0.6).
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
                 "function feedbackErrorLine(message, filename, lineno) {")

EXPORTS = ["typeFieldsHTML", "FEEDBACK_KINDS", "feedbackKind", "maskFeedbackQuery",
           "buildFeedbackContext", "renderFeedbackContext", "dedupHash",
           "labelsForType", "buildIssueTitle", "buildReportYAML", "buildIssueBody",
           "feedbackErrorLine"]

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
    u"https://maps.google.com/?q=" + A + u"." + A + u"," + B + u"." + B,
    GPS_ROW_TITLE,                                         # what the GPS row SHOWS
)
PLAIN_QUERIES = (PLAIN_QUERY, u"бл 5 аспарухово", u"ул. Струга 12")
# A value that carries two decimal numbers is a position whatever its key is.
COORD_VALUE_RE = r"\d[.,]\d[\s\S]*?\d[.,]\d"


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
        Bulgarian comma pair, degrees-minutes-seconds, a `geo:` URI and a map
        link. Each of them, and the title the GPS row shows, is the whole query
        now; a normal address goes through untouched."""
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
        self.assertIn(u"er.field || er.resource || er.code", block,
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
                       u"query: isCoordRow(rows[0]) ? COORD_MARK :",
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
        asks = [call("feedbackErrorLine", [u"първи ред\nвтори ред\nтрети", u"index.html", 12]),
                call("feedbackErrorLine", [u"boom ?token=CANARY&lat=" + COORD_LOOKING_QUERY,
                                           u"https://example.org/app.js?token=CANARY", 7]),
                call("feedbackErrorLine", [u"при " + COORD_LOOKING_QUERY, u"index.html", 3]),
                call("feedbackErrorLine", [u"A" * 300, u"index.html", 1])]
        one, token, coord, long_line = ask(self, text, asks)
        self.assertEqual(one, u"първи ред @index.html:12",
                         u"%s носи повече от първия ред: %r" % (NEEDLE_ERRLINE, one))
        self.assertNotIn(u"CANARY", token,
                         u"%s носи query string: %r" % (NEEDLE_ERRLINE, token))
        self.assertEqual(token, u"boom @app.js:7",
                         u"%s: %r" % (NEEDLE_ERRLINE, token))
        self.assertEqual(coord, COORD_MARK + u" @index.html:3",
                         u"%s носи координата: %r" % (NEEDLE_ERRLINE, coord))
        self.assertEqual(len(long_line), 200,
                         u"%s не е ограничен на 200 знака (%d)"
                         % (NEEDLE_ERRLINE, len(long_line)))
        for anchor in ERROR_LISTENERS:
            self.assertIn(u"feedbackErrorLine(", lot1.block(self, text, anchor),
                          u"слушателят не минава през %s" % NEEDLE_ERRLINE)

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
