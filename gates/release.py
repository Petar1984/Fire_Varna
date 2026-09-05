#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check 6 — the release gate: the delivery is exactly what Petar signed.

    python -m gates.release [--queue <path>]

`coverage.py` (check 4) answers one question: did the DELIVERY lose a label.
This gate answers the other one: is the ENGINE that reads the delivery still
answering what the signed reference says, and is every difference covered by a
signed row of the queue. Four bodies are bound to each other here, by digest:

  * the frozen reference — the BLOB at HEAD of
    `scratch/places_search/recall_sweep_rows.json`, never the copy on disk
    (F12-ж: the CRLF twin in a Windows worktree is the same OID and different
    bytes, so a disk digest is a property of one machine, not of the commit);
  * the engine candidate — `recall_sweep.reference_rows()` run report-only, in
    memory: nothing is written, so the gate can never bless a file it produced;
  * the pinned inputs — the three delivered blobs at HEAD and the three SHA
    constants of `index.html` the browser checks before it renders anything;
  * the manifests and `expectations.json` — the documents Petar signs, with
    every commit-named anchor re-derived from the blob it names.

Then every exact delta between the reference and the candidate — a query that
moved, vanished, appeared, was reordered, changed branch, count or label — must
be covered BY ROW ID by a queue row whose decision is „да“. No row: BLOCKED. A
row whose decision is „не“ (terminal) covering a live delta: BLOCKED. A signed
row that covers nothing: BLOCKED — a stale permission is not a permission (the
same rule gates/coverage.py applies with exit 3).

The comparison is FULL and ORDERED: all rows of every query, in their order,
with their labels; never a head, never a count alone — a count cannot see a
swap of two rows.

Exit code: 0 only when nothing is blocked, 6 otherwise — one number for the
pre-push hook, the words in the table.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

from gates import coverage

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

ENGINE_REL = "scratch/places_search/recall_sweep.py"
REFERENCE_REL = "scratch/places_search/recall_sweep_rows.json"
EXPECTATIONS_REL = "scratch/places_search/expectations.json"
M7_TOKENS_REL = "scratch/places_search/m7_trigger_tokens.json"
MANIFEST_RELS = (
    "scratch/places_search/lot1v_v_manifest_BASE_P7.json",
    "scratch/places_search/lot1v_v_manifest_P7_F12.json",
    "scratch/places_search/lot1v_v_reference_manifest.json",
)
# (constant in index.html, delivered blob) — check 1 compares the pins with the
# worktree; here they are compared with the BLOB at HEAD, which is what a push
# publishes.
SHA_PINS = (
    ("HOTELS_SHA256", "data/hotels.json"),
    ("PLACES2_SHA256", "data/places.json"),
    ("CATS_SHA256", "data/place_categories.json"),
)
QUEUE_DIR = "scratch/places_search"
QUEUE_GLOB = "ЗА_ПОДПИС_*.md"

# The artefacts a queue row may govern. `gates.sign` writes the signature into
# exactly these and the gate reads it back from exactly these — one list, so a
# signature can never land somewhere the gate does not look.
SIGNABLE = {
    "expectations": EXPECTATIONS_REL,
    "manifest_base_p7": MANIFEST_RELS[0],
    "manifest_p7_f12": MANIFEST_RELS[1],
    "manifest_reference": MANIFEST_RELS[2],
    "m7_tokens": M7_TOKENS_REL,
    "baseline": "gates/baseline/MANIFEST.json",
}

ALLOW_DIR = "gates/allow"


def signable():
    """{name: path} — the artefacts a queue row may govern.

    The six fixed ones are the table above; the allow-file is found by glob
    because its name carries the date of the delivery. `gates.sign` calls THIS
    function, so the pen and the gate can never disagree about what is signable.
    """
    table = dict(SIGNABLE)
    found = sorted((REPO_ROOT / ALLOW_DIR).glob("*.json"))
    if len(found) == 1:
        table["allow"] = str(found[0].relative_to(REPO_ROOT)).replace("\\", "/")
    return table


YES, NO, PENDING = u"да", u"не", u"pending"
DECISIONS = (YES, NO, PENDING)

EXIT_OK = 0
EXIT_USAGE = 4
EXIT_BLOCKED = 6


# ------------------------------------------------------------------ primitives

def blob_at(commit, rel):
    """The bytes a commit delivers for a path. Fail-loud: no blob, no verdict."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "show", "%s:%s" % (commit, rel)],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git show %s:%s: %s"
                         % (commit, rel, out.stderr.decode("utf-8", "replace").strip()))
    return out.stdout


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_engine():
    """Import the reference engine. Importing it writes not one byte (§11 Р9)."""
    spec = importlib.util.spec_from_file_location(
        "recall_sweep_release", str(REPO_ROOT / ENGINE_REL))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signed_by_of(doc):
    """`signed_by` wherever the artefact keeps it — top level or inside `_meta`."""
    if not isinstance(doc, dict):
        return None
    if "signed_by" in doc:
        return doc.get("signed_by")
    meta = doc.get("_meta")
    if isinstance(meta, dict):
        return meta.get("signed_by")
    return None


# -------------------------------------------------------------------- the queue

QUEUE_HEAD = re.compile(r"^##\s+(\S+)\s*(?:·\s*(.*))?$")
# `- **ключ:** стойност` — the bold spans the colon, which is how a human writes
# it and how the queue reads in a browser; the plain `- ключ: стойност` is read
# as well, so the parser never depends on the emphasis.
QUEUE_KEY = re.compile(r"^\s*[-*]\s+(?:\*\*)?([^:*]+?)\s*:(?:\*\*)?\s*(.*?)\s*$")

FIELD_ID = u"id"
FIELD_ASK = u"питане"
FIELD_DECISION = u"решение"
FIELD_DATE = u"дата"
FIELD_ARTEFACT = u"артефакт"
FIELD_COVERS = u"покрива"


def find_queue(explicit):
    """The one queue of the delivery: named, or the only file in the folder."""
    if explicit:
        return pathlib.Path(explicit)
    found = sorted((REPO_ROOT / QUEUE_DIR).glob(QUEUE_GLOB))
    if not found:
        return None
    if len(found) > 1:
        # Two queues for one delivery is exactly the ambiguity the gate exists
        # to remove (the same rule run_gates applies to the allow-files).
        raise ValueError(u"повече от една опашка: %s"
                         % u", ".join(p.name for p in found))
    return found[0]


def parse_queue(path):
    """The rows of the queue file, as data.

    The queue is MARKDOWN because a human reads it and signs it; the shape is
    fixed so a machine can read it too (план v2 §0.6):

        ## R3 · манифест BASE→P7
        - **id:** R3
        - **питане:** …
        - **решение:** pending
        - **дата:** —
        - **артефакт:** manifest_base_p7
        - **покрива:** gate_lot1v_v/*, gate_m7_bare/*
    """
    rows, current = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        head = QUEUE_HEAD.match(line)
        if head:
            if current:
                rows.append(current)
            current = {"id": head.group(1), "title": (head.group(2) or "").strip(),
                       "fields": {}}
            continue
        if current is None:
            continue
        pair = QUEUE_KEY.match(line)
        if pair:
            current["fields"][pair.group(1).strip()] = pair.group(2).strip()
    if current:
        rows.append(current)
    out = []
    for row in rows:
        fields = row["fields"]
        covers = [c.strip() for c in (fields.get(FIELD_COVERS) or "").split(",") if c.strip()]
        out.append({
            "id": (fields.get(FIELD_ID) or row["id"]).strip(),
            "title": row["title"],
            "ask": fields.get(FIELD_ASK) or "",
            "decision": (fields.get(FIELD_DECISION) or "").strip(),
            "date": (fields.get(FIELD_DATE) or "").strip(),
            "artefact": (fields.get(FIELD_ARTEFACT) or "").strip(),
            "covers": covers,
        })
    return out


def covers_delta(pattern, bucket, query):
    """One `покрива` pattern against one delta: `bucket/query` or `bucket/*`."""
    if "/" not in pattern:
        return False
    where, _, what = pattern.partition("/")
    if where != bucket:
        return False
    return what == "*" or what == (query or "")


# --------------------------------------------------------- reference ↔ candidate

def entries_of(doc):
    """{(bucket, q): entry} over a reference-shaped document."""
    out = {}
    for bucket, rows in doc.items():
        if bucket == "_meta" or not isinstance(rows, list):
            continue
        for entry in rows:
            out[(bucket, entry.get("q"))] = {
                "branch": entry.get("branch"),
                "hasKey": entry.get("hasKey"),
                "n": entry.get("n"),
                "rows": [(r.get("name"), r.get("zone"), r.get("kind"))
                         for r in (entry.get("rows") or [])],
            }
    return out


def compare(reference, candidate):
    """Every exact delta between the two — ordered rows, labels, branch, count.

    `kind` is compared only where BOTH sides carry it: the лот-Б artefact was
    written before that column existed, and „the base cannot say“ is not a
    difference (the rule `base_adapter` follows in the engine).
    """
    deltas = []
    for key in sorted(set(reference) | set(candidate), key=lambda k: (k[0], k[1] or u"")):
        bucket, query = key
        was, now = reference.get(key), candidate.get(key)
        if was is None:
            deltas.append({"bucket": bucket, "q": query, "why": [u"нова заявка"]})
            continue
        if now is None:
            deltas.append({"bucket": bucket, "q": query,
                           "why": [u"заявката я няма в кандидата"]})
            continue
        why = []
        if was["branch"] != now["branch"]:
            why.append(u"клон %s → %s" % (was["branch"], now["branch"]))
        if was["hasKey"] is not None and was["hasKey"] != now["hasKey"]:
            why.append(u"hasKey %s → %s" % (was["hasKey"], now["hasKey"]))
        if len(was["rows"]) != len(now["rows"]):
            why.append(u"редове %d → %d" % (len(was["rows"]), len(now["rows"])))
        else:
            old_names = [r[0] for r in was["rows"]]
            new_names = [r[0] for r in now["rows"]]
            if old_names != new_names:
                why.append(u"пренаредени редове" if sorted(old_names) == sorted(new_names)
                           else u"други записи")
            elif [r[1] for r in was["rows"]] != [r[1] for r in now["rows"]]:
                why.append(u"друг етикет на зоната")
            else:
                kinds = [(a[2], b[2]) for a, b in zip(was["rows"], now["rows"])
                         if a[2] is not None and b[2] is not None and a[2] != b[2]]
                if kinds:
                    why.append(u"друг вид: %s" % (kinds[:3],))
        for side, entry in ((u"референцията", was), (u"кандидатът", now)):
            if entry["n"] is not None and entry["n"] != len(entry["rows"]):
                why.append(u"%s брои %s, а носи %d реда"
                           % (side, entry["n"], len(entry["rows"])))
        if why:
            deltas.append({"bucket": bucket, "q": query, "why": why})
    return deltas


# --------------------------------------------------------------------- the gate

def run(queue_override=None):
    """Runs every part, always: the table is written for the human, not stopped
    at the first mark. Returns {exit_code, verdict, lines, blocked, deltas, …}."""
    lines, bad = [], []

    def say(text):
        lines.append(text)

    def block(text):
        bad.append(text)
        lines.append(u"✗ " + text)

    # --- 1. the artefacts and their signatures -------------------------------
    artefacts = {}
    table = signable()
    for name in sorted(table):
        rel = table[name]
        path = REPO_ROOT / rel
        if not path.exists():
            block(u"липсва %s (%s)" % (rel, name))
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            block(u"%s: %s" % (rel, exc))
            continue
        signature = signed_by_of(doc)
        artefacts[name] = {"rel": rel, "doc": doc, "signed_by": signature}
        if coverage.is_signed_by_petar(signature):
            say(u"%s: подписан ✓" % rel)
        else:
            block(u"%s: signed_by = %r — не е подписът на Петър" % (rel, signature))

    # --- 2. the pinned inputs, read from the blobs ---------------------------
    try:
        html = blob_at("HEAD", "index.html").decode("utf-8")
    except ValueError as exc:
        block(str(exc))
        html = u""
    for const_name, rel in SHA_PINS:
        match = re.search(r"const\s+%s\s*=\s*'([0-9a-f]{64})'" % re.escape(const_name), html)
        if not match:
            block(u"%s: константата липсва в index.html (блоб на HEAD)" % const_name)
            continue
        try:
            raw = blob_at("HEAD", rel).replace(b"\r\n", b"\n")
        except ValueError as exc:
            block(str(exc))
            continue
        got = digest(raw)
        if got == match.group(1):
            say(u"%s = %s ✓ %s (блоб на HEAD)" % (const_name, got[:12], rel))
        else:
            block(u"%s: пин %s ≠ блоба %s (%s)"
                  % (const_name, match.group(1)[:12], got[:12], rel))

    # --- 3. the reference: worktree == blob, blob == the signed digest -------
    try:
        reference_doc = json.loads(blob_at("HEAD", REFERENCE_REL).decode("utf-8"))
    except ValueError as exc:
        block(str(exc))
        return verdict(lines, bad, [], [], [])
    worktree = (REPO_ROOT / REFERENCE_REL).read_bytes().decode("utf-8")
    if json.loads(worktree) != reference_doc:
        block(u"%s: работното дърво носи друга референция от блоба на HEAD"
              % REFERENCE_REL)
    expectations = (artefacts.get("expectations") or {}).get("doc")
    if expectations is None:
        block(u"няма подписваеми очаквания (%s)" % EXPECTATIONS_REL)
    else:
        anchor = ((expectations.get("_meta") or {}).get("reference") or {})
        try:
            want = digest(blob_at(anchor.get("commit") or "HEAD",
                                  anchor.get("path") or REFERENCE_REL))
        except ValueError as exc:
            block(str(exc))
            want = None
        if want is not None and anchor.get("sha256") != want:
            # The injection nothing else catches: an engine and a reference
            # mutated TOGETHER stay equal to each other and differ from the
            # digest the signature was given.
            block(u"expectations._meta.reference: подписаният дайджест %s ≠ блоба %s"
                  % ((anchor.get("sha256") or u"—")[:12], want[:12]))
        elif want is not None:
            say(u"референция: %s = подписаният дайджест ✓" % want[:12])

    # --- 4. the manifests: every commit-named anchor is the blob -------------
    engine = load_engine()
    present = [str(REPO_ROOT / rel) for rel in MANIFEST_RELS if (REPO_ROOT / rel).exists()]
    complaints = engine.check_manifest_anchors(present)
    for complaint in complaints:
        block(u"котва: " + complaint)
    if present and not complaints:
        say(u"котвите на %d манифеста = блобовете, които назовават ✓" % len(present))

    # --- 5. reference ↔ engine candidate, full and ordered ------------------
    candidate_doc = engine.reference_rows()
    # The candidate the signature was given to. Without this the queue patterns
    # are a blank cheque: a row that covers `gate_lot1/*` would authorise every
    # future change of that bucket, and an engine moved after the signature
    # would ride a permission given for another delivery.
    if expectations is not None:
        want = ((expectations.get("_meta") or {}).get("candidate") or {})
        got = digest(engine.dump_rows(candidate_doc).encode("utf-8"))
        if want.get("sha256") != got:
            block(u"двигателят не е кандидатът, който е подписан: %s ≠ %s"
                  % (got[:12], (want.get("sha256") or u"—")[:12]))
        else:
            say(u"кандидат: %s = подписаният двигател ✓" % got[:12])
    reference = entries_of(reference_doc)
    candidate = entries_of(candidate_doc)
    deltas = compare(reference, candidate)
    say(u"референция %d заявки / %d реда · кандидат %d / %d · делти %d"
        % (len(reference), sum(len(e["rows"]) for e in reference.values()),
           len(candidate), sum(len(e["rows"]) for e in candidate.values()), len(deltas)))

    # --- 6. every delta needs a signed queue row, by id ---------------------
    rows = []
    try:
        queue_path = find_queue(queue_override)
    except ValueError as exc:
        block(str(exc))
        queue_path = None
    if queue_path is None:
        block(u"няма опашка %s/%s — нищо не е разрешено" % (QUEUE_DIR, QUEUE_GLOB))
    elif not queue_path.exists():
        block(u"опашката %s липсва" % queue_path)
    else:
        rows = parse_queue(queue_path)
        say(u"опашка: %s — %d реда" % (queue_path.name, len(rows)))
        for row in rows:
            if row["decision"] not in DECISIONS:
                block(u"ред %s: решение %r — само да/не/pending"
                      % (row["id"], row["decision"]))
            if row["decision"] == YES and not row["date"].strip(u"— -"):
                block(u"ред %s: подписан без дата" % row["id"])
            if row["decision"] == YES and row["artefact"]:
                name = row["artefact"]
                if name not in table:
                    block(u"ред %s: непознат артефакт %r (познати: %s)"
                          % (row["id"], name, u", ".join(sorted(table))))
                elif name in artefacts and not coverage.is_signed_by_petar(
                        artefacts[name]["signed_by"]):
                    block(u"ред %s е „да“, а %s не носи подписа"
                          % (row["id"], table[name]))

    used, uncovered = set(), []
    for delta in deltas:
        owner = None
        for row in rows:
            if not any(covers_delta(p, delta["bucket"], delta["q"]) for p in row["covers"]):
                continue
            if row["decision"] == NO:
                block(u"%s/%s: ред %s е ОТКАЗАН (терминално)"
                      % (delta["bucket"], delta["q"], row["id"]))
                owner = row["id"]
                used.add(row["id"])
                break
            if row["decision"] == YES:
                owner = row["id"]
                used.add(row["id"])
                break
        if owner is None:
            uncovered.append(delta)
    for delta in uncovered[:10]:
        block(u"непокрита делта %s/%s: %s"
              % (delta["bucket"], delta["q"], u"; ".join(delta["why"])))
    if len(uncovered) > 10:
        block(u"… още %d непокрити делти" % (len(uncovered) - 10))

    # A signed row that covers nothing is a STALE permission — but only while
    # there is still something to permit. When the candidate and the reference
    # are equal (the freeze has happened and been committed) every authorisation
    # has been consumed, and „consumed“ is not „stale“: demanding that Petar
    # empty the `покрива` of every row before he may push would make the freeze
    # itself unpushable.
    stale = ([row["id"] for row in rows
              if row["decision"] == YES and row["covers"] and row["id"] not in used]
             if deltas else [])
    for row_id in stale:
        block(u"ред %s е подписан, а не покрива нито една жива делта" % row_id)
    if rows and not deltas:
        say(u"0 делти — всяко разрешение е приложено (замразяването е в HEAD)")

    return verdict(lines, bad, deltas, uncovered, stale)


def verdict(lines, bad, deltas, uncovered, stale):
    return {
        "exit_code": EXIT_BLOCKED if bad else EXIT_OK,
        "verdict": (u"BLOCKED: %d" % len(bad)) if bad else u"зелено",
        "lines": lines,
        "blocked": bad,
        "deltas": deltas,
        "uncovered": uncovered,
        "stale": stale,
    }


def main(argv):
    coverage.use_utf8_console()
    ap = argparse.ArgumentParser(description=u"Fire_Varna release gate (проверка 6)")
    ap.add_argument("--queue", help=u"scratch/places_search/ЗА_ПОДПИС_<дата>.md")
    args = ap.parse_args(argv)
    try:
        result = run(args.queue)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        sys.stdout.write(u"✗ release: %s\n" % exc)
        return EXIT_BLOCKED
    for line in result["lines"]:
        sys.stdout.write(u"  %s\n" % line)
    sys.stdout.write(u"%s\n" % (u"⛔ BLOCKED (%d)" % len(result["blocked"])
                                if result["blocked"] else u"✓ release: зелено"))
    return result["exit_code"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
