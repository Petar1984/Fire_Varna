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
  * The four negative halves doctor COPIES of `index.html` under the temp root — never
    inside the repository — and demand exit 1 plus the text of the assertion they break.

No coordinate stands in this file in any shape: the one coordinate-looking string the
mask is measured against is built out of repeated digits.
"""
import json
import os
import pathlib
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
    "function maskFeedbackQuery(q) {",
    "function feedbackEnvSnapshot() {",
    "function buildFeedbackContext(kind, env) {",
    "const FB_CTX_LABELS = {",
    "function renderFeedbackContext(kind, env) {",
    "function typeFieldsHTML(t, d) {",
    "function dedupHash(report) {",
    "function labelsForType(",
    "function hydrantTypeLabel(typeValue) {",
    "function yamlValue(v) {",
    "function buildReportYAML(report) {",
    "function buildIssueBody(report) {",
)
# The blocks BORN in this lot: at the base they are missing by construction, and
# only there is their absence allowed.
BASE_OPTIONAL = ("const FEEDBACK_KINDS = [",
                 "function feedbackKind(id) {",
                 "function maskFeedbackQuery(q) {",
                 "function feedbackEnvSnapshot() {",
                 "function buildFeedbackContext(kind, env) {",
                 "const FB_CTX_LABELS = {",
                 "function renderFeedbackContext(kind, env) {")

EXPORTS = ["typeFieldsHTML", "FEEDBACK_KINDS", "feedbackKind", "maskFeedbackQuery",
           "buildFeedbackContext", "renderFeedbackContext", "dedupHash",
           "labelsForType", "buildReportYAML", "buildIssueBody"]

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

# What the four halves hunt for: the text of the assertion, never a method name.
NEEDLE_LABELS = u"етикетите на обратната връзка"
NEEDLE_MASK = u"маската на заявката"
NEEDLE_APPLY = u"APPLY_TYPES"
NEEDLE_CONTEXT = u"feedback_context"


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
        "location_method": "hydrant_ref",
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
                    "type", "operational_status"):
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


# --------------------------------------------------------------------------
# The four negative halves - each RUNS and each FALLS with its own needle
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
