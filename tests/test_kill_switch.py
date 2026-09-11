# -*- coding: utf-8 -*-
"""Ф12 · ИБ1-Г12 — the kill switch: one word off, and the DOM is yesterday's.

    python -m unittest tests.test_kill_switch

`ADDRESS_QUARTER_V2 = false` is the откат of Р7: with it the four address surfaces
must produce the DOM of `<БАЗА>:index.html` — byte for byte, not "about the same".
The reference is the PINNED blob, never HEAD (Кими К44-2): HEAD moves with every
commit of the lot, and a reference that moves proves nothing.

The corpus of Ф11 is the input: its twenty queries are the kill switch's cases,
and the entries beside them are what the data gates judge. The delivered payload
is handed to the client through the probe's fetch stub, exactly as the page gets
it — and one case takes it AWAY (О78): a refused `fetch` may never make the slice
throw, because `loadQuarterIndex` swallows it; the row must simply read as it does
today.

Coordinates are ASSEMBLED at runtime (О95): the GPS case builds its query out of a
pin read from `data/search_index.json` while the test runs.

Червено по конструкция до К9 (ИНТЕРВАЛ А): the markers of Т12 and the flag of Т2
are born in К9.

Negative halves (план §5 Г12): the corpus run with **FIRE_VARNA_KILL_SWITCH_FLAG=true**
(the switch left ON → the DOM differs → 1); a moved line inside `buildExactItem`
with the switch OFF (→ 1); a `fetch` stub that refuses (→ the row of today, and a
throw is 1).

Run: python -m unittest discover -s tests
"""
import json
import os
import pathlib
import re
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

# Ф8 owns the slice cutting, the probe call and the <БАЗА> reference; this gate is
# its sibling and borrows them rather than keeping a second, drifting copy.
from tests.test_address_quarter_render import (
    DELIVERED, FLAGSHIP_QUERY, ask_base, ask_client, client_slices,
    coordinate_query, corpus_doc, delivered_doc, flagship_index, run_probe,
    base_slice, search_entries, EXPORTS_QUARTER,
)

# Т2 — the flag is a const with a literal boolean, so the switch can be thrown
# from the outside without touching the tracked file.
FLAG_RE = re.compile(r"(const\s+ADDRESS_QUARTER_V2\s*=\s*)true")
# The half leaves the switch ON: the DOM then legitimately differs and the gate
# has to fall (план §5 Г12).
KEEP_FLAG_ON = (os.environ.get("FIRE_VARNA_KILL_SWITCH_FLAG") or "").lower() == "true"

RENDER_LIMIT = 5


def switched_off(test):
    """(shared, slice) with `ADDRESS_QUARTER_V2` forced to false."""
    shared, body = client_slices(test)
    if KEEP_FLAG_ON:
        return shared, body
    text = shared + body
    if len(FLAG_RE.findall(text)) != 1:
        test.fail(u"ADDRESS_QUARTER_V2 не е точно една константа с литерал true "
                  u"(Т2 я ражда в К9)")
    if FLAG_RE.search(shared):
        return FLAG_RE.sub(r"\1false", shared), body
    return shared, FLAG_RE.sub(r"\1false", body)


def ask_switched_off(test, asks, quarters_path=None):
    shared, body = switched_off(test)
    return run_probe(test, {"shared": shared, "slice": body,
                            "exports": EXPORTS_QUARTER, "asks": asks},
                     quarters_path=quarters_path or DELIVERED)


class KillSwitchTest(unittest.TestCase):
    """ИБ1-Г12 — with the switch off the DOM is the blob of <БАЗА>."""

    def corpus_asks(self, test_queries):
        return [{"ask": "render", "q": q, "limit": RENDER_LIMIT} for q in test_queries]

    def test_every_corpus_query_renders_the_dom_of_the_base(self):
        queries = corpus_doc(self)["queries"]
        asks = self.corpus_asks(queries)
        base = ask_base(self, asks)
        off = ask_switched_off(self, asks)
        self.assertEqual(len(base), len(off))
        for query, before, after in zip(queries, base, off):
            self.assertEqual([r["html"] for r in after], [r["html"] for r in before],
                             u"DOM-ът се различава при угасена дума за %r" % query)

    def test_the_gps_surface_is_the_dom_of_the_base(self):
        entries = search_entries()
        query = coordinate_query(entries[flagship_index(entries)]["pin"])
        base = ask_base(self, [{"ask": "coord", "q": query}])[0]
        off = ask_switched_off(self, [{"ask": "coord", "q": query}])[0]
        self.assertEqual(off["html"], base["html"],
                         u"GPS-редът се различава при угасена дума")
        self.assertEqual(off["popup"], base["popup"],
                         u"GPS-попъпът се различава при угасена дума")


class RefusedPayloadTest(unittest.TestCase):
    """О78 — `loadQuarterIndex` never rejects: a 404 leaves today's row standing."""

    def test_a_refused_payload_keeps_todays_row(self):
        asks = [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1},
                {"ask": "ensure"}]
        base = ask_base(self, [{"ask": "render", "q": FLAGSHIP_QUERY, "limit": 1}])[0]
        # No payload file for the quarters url -> the stub answers 404.
        shared, body = client_slices(self)
        answers = run_probe(self, {"shared": shared, "slice": body,
                                   "exports": EXPORTS_QUARTER, "asks": asks})
        rendered, ensured = answers
        self.assertTrue(ensured.get("ok"), u"срезът хвърли при отказан товар: %s"
                        % json.dumps(ensured, ensure_ascii=False))
        self.assertEqual(ensured.get("quarter"), False,
                         u"quarterIndex не е угасен при 404")
        self.assertEqual([r["html"] for r in rendered], [r["html"] for r in base],
                         u"редът не е днешният при отказан товар")

    def test_a_broken_document_is_refused_fail_closed(self):
        """§3.Г — a document that fails ONE invariant silences the word on all
        four surfaces at once, and throws nothing."""
        doc = delivered_doc(self)
        doc["codes"] = doc["codes"][:-1]          # one cell short: the white list falls
        with tempfile.TemporaryDirectory(prefix="ib1_kill_") as tmp:
            path = pathlib.Path(tmp) / "quarters_short.json"
            path.write_text(json.dumps(doc, ensure_ascii=False, sort_keys=True,
                                       separators=(",", ":")), encoding="utf-8")
            answers = ask_client(self, [{"ask": "ensure"}], quarters_path=path)
        self.assertTrue(answers[0].get("ok"), u"кривият документ хвърли нагоре")
        self.assertEqual(answers[0].get("quarter"), False,
                         u"кривият документ не е отхвърлен (fail-closed)")


if __name__ == "__main__":
    unittest.main()
