# -*- coding: utf-8 -*-
"""Лот 1г · Г1-Г2 — the note of the wrong-location form is OPTIONAL.

    python -m unittest tests.test_report_form_note_optional

"Защо е грешна локацията? - ами защото не е на правилното място" (Petar, 14.09):
a wrong-location report IS the corrected coordinate, so the description is the
extra, not the requirement. The label now reads "Описание (по желание)", the same
words the note of the other three forms carries, and the four-line validation
block of `onSubmitClicked` is gone together with the `.err` div and the field id
that only that block ever needed.

How this gate works, so no reader has to guess:

  * The harness is NOT retyped. `test_report_form_operational` (lot 1) already
    raises a SLICE of `index.html` headless through `tests/granitsi_client_probe.mjs`,
    cuts each block by its NAME and builds the three form fixtures. This file
    imports it as a module and reuses all of it, so the mechanics of the client
    stay ONE source of truth and cannot drift between two gates.
  * The reference is the SAME render at the BASE commit, pinned as a literal under
    this lot's OWN environment name (`FIRE_VARNA_LOT1G_BASE`) - never `merge-base`,
    never the base of lot 1: one base per file. A base whose blob equals the
    candidate is a dead reference and fails loud instead of passing vacuously.
  * Nothing is read at module level and no git runs there.
  * The two negative halves run this gate against DOCTORED copies of `index.html`
    under the temp root - never inside the repository - and demand exit 1 plus the
    text of the very assertion they break. The child is handed both its index path
    AND the base literal, so the base can never be inherited from a foreign shell.

No coordinate stands in this file, in any shape.
"""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
TESTS = REPO / "tests"
if str(TESTS) not in sys.path:        # the lot 1 harness travels as a module, not as a copy
    sys.path.insert(0, str(TESTS))
import test_report_form_operational as lot1   # noqa: E402 - the path has to come first

# The base of THIS lot, as a literal under its own name: never the base of lot 1
# (`FIRE_VARNA_LOT1_BASE`), which stays on its own file.
BASE_LITERAL = "2d18377"
BASE = os.environ.get("FIRE_VARNA_LOT1G_BASE") or BASE_LITERAL

# The doctored copies of the two halves live here - never in the tree.
FIXTURES = pathlib.Path(tempfile.gettempdir()) / "fv_lot1g_fixtures"

MODULE = "tests.test_report_form_note_optional"

FORM = "wrong_location"
OTHER_FORMS = ("exists_confirmed", "damaged", "missing", "new_hydrant")

NEW_LABEL = u'<label>Описание (по желание)</label>'
NEW_LABEL_LINE = u"        '<label>Описание (по желание)</label>' +"
OLD_LABEL_LINE = u"        '<label>Описание <span class=\"req\">*</span></label>' +"
OLD_STARRED_LABEL = u'Описание <span'
DEAD_FIELD_ID = 'id="fld_description"'
FIELD_ID = "fld_description"
ERR_MESSAGE = u"Моля въведи описание."
REQ_MARKER = '<span class="req">*</span>'
ERR_DIV = '<div class="err">'
PICKER_FIELDS = ("fld_hydrant_type", "fld_operational")

# The four lines that used to forbid an empty description, verbatim.
OLD_VALIDATION = (
    "    if (reportType === 'wrong_location' && !reportDraft.description) {\n"
    "      const f = document.getElementById('fld_description');"
    " if (f) f.classList.add('invalid');\n"
    "      invalid = true;\n"
    "    }\n")
# The two neighbours that STAY required; the first is also where the half of the
# validation puts the deleted block back.
DAMAGE_VALIDATION = "    if (reportType === 'damaged' && !reportDraft.damage_description) {"
PLACED_VALIDATION = ("    if ((reportType === 'wrong_location' || reportType === 'new_hydrant')"
                     " && !reportDraft.placedCoord) {")

TEXTAREA_HEAD = '<textarea data-field="description"'
TEXTAREA_TAIL = '</textarea>'

# What the two halves hunt for: the text of the assertion, never a method name.
NEEDLE_FORM = u"формата още иска описание"
NEEDLE_VALIDATION = u"валидацията на описанието още стои"


# --------------------------------------------------------------------------
# The base blob - read inside a method, never at import
# --------------------------------------------------------------------------

def base_text(test):
    """The blob of `<BASE>:index.html`. A dead reference is a failure, not a skip."""
    proc = subprocess.run(["git", "-C", str(REPO), "show", "%s:index.html" % BASE],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        test.fail(u"няма блоб %s:index.html — базата е неразрешима: %s"
                  % (BASE, proc.stderr.decode("utf-8", "replace")[:300]))
    text = proc.stdout.decode("utf-8")
    if text == lot1.index_text(test):
        test.fail(u"база равна на кандидата — базата %s е равна на работния файл" % BASE)
    return text


def render(test, text, forms):
    """`typeFieldsHTML` for every (form, fixture) pair, raised in ONE client call."""
    cases, asks = [], []
    for form in forms:
        for name, draft in lot1.all_fixtures():
            cases.append((form, name))
            asks.append(lot1.call(form, draft))
    return cases, lot1.ask_client(test, text, asks)


def textarea_slice(test, where, html):
    """The description textarea of a rendered form, opening tag to closing tag."""
    if html.count(TEXTAREA_HEAD) != 1:
        test.fail(u"%s: полето за описание стои %d пъти, не веднъж"
                  % (where, html.count(TEXTAREA_HEAD)))
    start = html.index(TEXTAREA_HEAD)
    end = html.index(TEXTAREA_TAIL, start)
    return html[start:end + len(TEXTAREA_TAIL)]


# --------------------------------------------------------------------------
# Г1 · the form itself
# --------------------------------------------------------------------------

class NoteOptionalTest(unittest.TestCase):

    def test_the_wrong_location_note_is_optional(self):
        text = lot1.index_text(self)
        cases, answers = render(self, text, (FORM,))
        for (form, name), html in zip(cases, answers):
            where = u"%s / %s" % (form, name)
            self.assertEqual(html.count(NEW_LABEL), 1,
                             u"%s: %s — етикетът „Описание (по желание)“ не стои веднъж"
                             % (where, NEEDLE_FORM))
            self.assertEqual(html.count(REQ_MARKER), 2,
                             u"%s: %s — звездичка извън двата пикера" % (where, NEEDLE_FORM))
            self.assertEqual(html.count(ERR_DIV), 2,
                             u"%s: %s — .err див извън двата пикера" % (where, NEEDLE_FORM))
            self.assertNotIn(DEAD_FIELD_ID, html,
                             u"%s: %s — мъртвият id на полето остана" % (where, NEEDLE_FORM))
            self.assertNotIn(OLD_STARRED_LABEL, html,
                             u"%s: %s — старият звезден етикет остана" % (where, NEEDLE_FORM))
        # The base render comes LAST on purpose: when the candidate IS the base blob,
        # the assertions above have to be the ones that speak (Г1 „червено ПРЕДИ“),
        # not the dead-reference guard.
        base = base_text(self)
        _, reference = render(self, base, (FORM,))
        for (form, name), html, want in zip(cases, answers, reference):
            where = u"%s / %s" % (form, name)
            self.assertTrue(textarea_slice(self, where, html)
                            == textarea_slice(self, where, want),
                            u"%s: плейсхолдърът на описанието се е променил срещу базата %s"
                            % (where, BASE))

    def test_the_validation_of_the_description_is_gone(self):
        text = lot1.index_text(self)
        self.assertEqual(text.count(OLD_VALIDATION), 0,
                         u"%s: четирите реда в onSubmitClicked не са махнати"
                         % NEEDLE_VALIDATION)
        self.assertEqual(text.count(FIELD_ID), 0,
                         u"%s: %s още стои в index.html" % (NEEDLE_VALIDATION, FIELD_ID))
        self.assertEqual(text.count(ERR_MESSAGE), 0,
                         u"%s: съобщението на грешката още стои" % NEEDLE_VALIDATION)
        self.assertEqual(text.count(DAMAGE_VALIDATION), 1,
                         u"редът на повредата не стои точно веднъж в кандидата")
        self.assertEqual(text.count(PLACED_VALIDATION), 1,
                         u"редът на поставената локация не стои точно веднъж в кандидата")
        self.assertEqual(text.count(lot1.SIGNED_GATE), 1,
                         u"подписаният ред на лот 1 не стои точно веднъж в кандидата")
        # A pin whose old shape is no longer in the base is a DEAD pin: the gate
        # would go green because there is nothing left to compare against.
        base = base_text(self)
        if base.count(OLD_VALIDATION) != 1:
            self.fail(u"мъртъв пин: четирите реда на валидацията стоят %d пъти в базата %s"
                      % (base.count(OLD_VALIDATION), BASE))
        if base.count(FIELD_ID) != 2:
            self.fail(u"мъртъв пин: %s стои %d пъти в базата %s, не 2"
                      % (FIELD_ID, base.count(FIELD_ID), BASE))
        if base.count(ERR_MESSAGE) != 1:
            self.fail(u"мъртъв пин: съобщението на грешката стои %d пъти в базата %s, не 1"
                      % (base.count(ERR_MESSAGE), BASE))
        self.assertEqual(base.count(DAMAGE_VALIDATION), 1,
                         u"редът на повредата не стои точно веднъж в базата")
        self.assertEqual(base.count(PLACED_VALIDATION), 1,
                         u"редът на поставената локация не стои точно веднъж в базата")
        self.assertEqual(base.count(lot1.SIGNED_GATE), 1,
                         u"подписаният ред на лот 1 не стои точно веднъж в базата")

    def test_the_other_four_branches_are_byte_equal_to_the_base(self):
        text = lot1.index_text(self)
        base = base_text(self)
        cases, candidate = render(self, text, OTHER_FORMS)
        _, reference = render(self, base, OTHER_FORMS)
        for (form, name), got, want in zip(cases, candidate, reference):
            self.assertTrue(got == want,
                            u"%s / %s: клонът не е байт за байт равен на базата %s"
                            % (form, name, BASE))

    def test_the_two_required_pickers_still_stand_on_the_wrong_location_form(self):
        text = lot1.index_text(self)
        cases, answers = render(self, text, (FORM,))
        for (form, name), html in zip(cases, answers):
            for field_id in PICKER_FIELDS:
                seg = lot1.field(self, html, field_id)
                reason = (u"%s / %s / %s: пикерът вече не е задължителен — звездичката "
                          u"е взета от грешния етикет" % (form, name, field_id))
                self.assertIn(REQ_MARKER, seg, reason)
                self.assertIn(ERR_DIV, seg, reason)


# --------------------------------------------------------------------------
# Г2 · the two negative halves - each RUNS and each FALLS
# --------------------------------------------------------------------------

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
        # The base travels as the LITERAL: a child that inherited a foreign
        # FIRE_VARNA_LOT1G_BASE would fall for somebody else's reason.
        environment = dict(os.environ, PYTHONIOENCODING="utf-8",
                           FIRE_VARNA_INDEX_HTML_PATH=str(path),
                           FIRE_VARNA_LOT1G_BASE=BASE_LITERAL)
        proc = subprocess.run([sys.executable, "-m", "unittest", target],
                              cwd=str(REPO), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, env=environment, timeout=600)
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace")
        self.assertEqual(proc.returncode, 1,
                         u"половината не падна: изход %d\n%s"
                         % (proc.returncode, out[-800:]))
        self.assertIn(needle, out,
                      u"половината падна, но не по своята причина\n%s" % out[-800:])

    def test_restoring_the_validation_block_turns_the_gate_red(self):
        text = lot1.replace_once(self, lot1.index_text(self), DAMAGE_VALIDATION,
                                 OLD_VALIDATION + DAMAGE_VALIDATION)
        path = self.doctored("restored_validation", text)
        self.run_half(path, MODULE + ".NoteOptionalTest."
                      "test_the_validation_of_the_description_is_gone",
                      NEEDLE_VALIDATION)

    def test_putting_the_asterisk_back_turns_the_gate_red(self):
        text = lot1.replace_once(self, lot1.index_text(self), NEW_LABEL_LINE, OLD_LABEL_LINE)
        path = self.doctored("asterisk_back", text)
        self.run_half(path, MODULE + ".NoteOptionalTest."
                      "test_the_wrong_location_note_is_optional",
                      NEEDLE_FORM)


if __name__ == "__main__":
    unittest.main()
