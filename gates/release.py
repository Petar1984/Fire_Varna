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

A REFUSAL THAT COVERS NOTHING IS BLOCKED TOO (амандамент №7 т. 1). The stale
rule above used to speak only about „да“, and that asymmetry was a hole with a
one-letter key: a „не“ written over `gate_lot1/Градината` when the delta is
`gate_lot1/градина` matched nothing, said nothing, and left the gate green over
the very difference Petar had refused — after which the freeze carried it into
the reference. A „не“ that reaches neither a live delta nor a difference
between the queue's reference and the frozen one is now BLOCKED, in the same
words as the stale permission: a decision about a query that does not exist is
not a decision. `gates.sign` applies the same test where the refusal is
written, so the typo is caught by the hand that makes it.

AND IT IS MEASURED PER PATTERN, OVER THE RAW `покрива` (амандамент №8 т. 1 и
т. 3). Reading the row as a whole left two ways through. A pattern with no
slash at all — `gate_lot1градина` — was not a delta pattern, so it was dropped
before the measurement and the row it was the ONLY content of was skipped
entirely: the queue said „не“, the gate said nothing. And a row that refuses
three queries and misspells one of them reached something, so the whole row
counted as doing its job while the misspelled third refusal was mute. Every
pattern of a „не“ row must therefore hit by itself; the ones that do not are
named one by one, with the reason — „шаблонът не е във вида кофа/заявка“ or
„не улучва нито жива делта, нито разлика спрямо котвата“ — and an empty
`покрива` under a „не“ is the same block with the same words.

THE ORDER OF THE FILE DOES NOT VOTE (амандамент №6 т. 2). Every row that
matches a delta is collected, never the first one that answers: a „не“ wins over
any „да“, and among rows that agree the exact `кофа/заявка` is the one the table
names, so a class row `кофа/*` never speaks for a query somebody answered by
name. Moving two rows past each other in the file cannot change a verdict.

A REFUSAL SURVIVES THE FREEZE (амандамент №5 т. 1). A freeze makes the
reference equal to the candidate, so afterwards there is no delta left for the
queue to refuse and a row Petar answered „не“ would be erased by the very act
it forbade. Two things stop that here: `expectations._meta.refused` — what the
freeze SAW, written down by `build_expectations` — is read back and blocks; and
every „не“ row is re-derived independently against the FROZEN reference, from
the reference THE QUEUE WAS WRITTEN AGAINST forward, so a hand-assembled body
with an empty `refused` list is caught by the bytes rather than by its own
bookkeeping.

THE QUEUE IS THE BLOB, NOT THE WORKTREE (амандамент №9 т. 1). A push publishes
commits, so the rows this gate judges come out of `blob_at("HEAD", <опашка>)`
like every other body here. Reading the file on disk let all seven gates go
green over a commit that carried NOT ONE signed row: the pen writes the
decisions into the worktree, the table read them there, and the blob the push
would have sent still said `pending`. A queue whose worktree differs from its
blob is blocked in the same words the signed artefacts get — „работното дърво
носи друго тяло от блоба на HEAD (пушът праща блоба)“.

AND A „да“ IS WORTH THE HAND THAT WROTE IT (амандамент №9 т. 2). Проверка 7 has
always asked who introduced a signature and who introduced a digest; nobody
asked who introduced the WORD „да“. `yes_row_authorship` asks it per row:
`git log -S` over the verbatim block of the row (`## <id>` up to the next
heading) has to name a commit of Petar's, or the row is an agent's permission
with a human's name on the file. The same rule is applied by `run_gates`
проверка 7, from this function, so the two readers cannot drift.

AND THE MACHINE READS ONLY WHAT THE HUMAN SEES (амандамент №9 т. 2). Markdown
hides two kinds of region — a ``` fence and an `<!-- -->` comment — and the old
parser read rows out of both. A „да“ inside a comment is invisible to the man
who signs the file and authoritative to the gate that reads it, which is the
whole attack. `parse_queue_text` now skips those regions, and a decision found
inside one BLOCKS: an invisible answer is not an answer, and hiding one is not
a typo. A field written twice in one row (`решение:`, `покрива:`) blocks for the
neighbouring reason — the parser would keep the last of them and the human would
read the first.

THREE CLASSES OF ROW, ONE QUEUE (амандамент №9 т. 5). Not every row is about a
delta, and the refusal rules of амандаменти 6–8 are about deltas only:

  * „въпрос“ — no `артефакт` and no `покрива` (Q7 „break-glass: вън“): „не“ is
    a decision, it is recorded, and it never enters the release;
  * „артефакт“ — an `артефакт` and no `покрива` (the baseline, the codes): „не“
    means the artefact is NOT signed, and the release then blocks on the
    artefact, not on a pattern;
  * „делта“ — a `покрива` field (present, even empty): the rules of амандаменти
    6–8 in full, and an empty `покрива` under a „не“ is still the block it was.

THE SIGNATURE PROTECTS THE WHOLE BODY (амандамент №9 т. 7). This gate binds
fields — the reference digest, the candidate digest, the anchors — and a rewrite
that touches none of them used to pass it and be caught by проверка 7 alone. So
`gates.sign` writes the digest of the body it signed onto the row (`- **тяло:**
<sha256>`, the values without the signature fields) and check 6 recompares it
with the blob at HEAD. A body that no longer matches has been rewritten after
the signature; that is Petar's freeze only when his own commit is the newest on
that path — the rule проверка 7 applies to the same question, now applied here
too, which is what makes `--freeze` (it reads this verdict, never проверка 7)
stop as well.

THAT ANCHOR IS WRITTEN DOWN, NOT GUESSED (амандамент №7 т. 3). The reference
the queue was written against is named explicitly in
`expectations._meta.queue_reference` — commit, path and digest — by the two
tools that measure it (`recall_sweep.build_expectations` and `gates.sign`).
Deriving it with `git log -S` was aimable: one agent commit that adds a SECOND
occurrence of `"signed_by": "Петър"` becomes the newest commit the pickaxe
reports, the anchor moves to a body the agent controls and the refusal goes
with it. The commit in the field must be Petar's own — амандамент №6 makes him
the author of every freeze — and a foreign anchor BLOCKS with words instead of
falling back to a commit constant of the engine.

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

# The string that says Petar signed a body. `run_gates` проверка 7 looks for
# the commit that INTRODUCED it; the refusal anchor no longer derives anything
# from it (амандамент №7 т. 3), it is written down.
SIGNATURE_NEEDLE = u'"signed_by": "%s"' % coverage.SIGNER

# The only author whose commit may carry a signature or a signed reference
# (план v2 §0.5). One string, read by this module, by `run_gates` проверка 7 and
# by the pen — three readers of one rule.
HUMAN_AUTHOR = u"Petar1984"

# `_meta.queue_reference` — the explicit anchor of a refusal (амандамент №7 т. 3).
QUEUE_REFERENCE_KEY = u"queue_reference"

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


def introduced_by(rel, needle):
    """(hash, author) of the newest commit that changed the count of `needle`.

    `git log -S` is the pickaxe: it lists exactly the commits where the number
    of occurrences of the string moved, so the newest of them is the commit that
    put the signature in. None = the string is in no commit at all. It lives
    here, next to `blob_at`, because two readers need it — `run_gates` проверка 7
    for the authorship and this module for the body Petar actually signed."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-S" + needle,
                          "--format=%H\t%an", "--", rel],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git log -S -- %s: %s"
                         % (rel, out.stderr.decode("utf-8", "replace").strip()))
    lines = out.stdout.decode("utf-8", "replace").splitlines()
    if not lines:
        return None
    parts = lines[0].split("\t", 1)
    return (parts[0], parts[1] if len(parts) > 1 else "")


def introduced_by_text(rel, needle):
    """(hash, author) of the OLDEST commit that changed the count of `needle`.

    The twin of `introduced_by`, asked from the other end. For a signature there
    is one occurrence and the question is „who put it there last“; for the block
    of a queue row the question is „who wrote this text FIRST“, and the oldest
    commit the pickaxe reports is that hand. Fail-closed on purpose: a block an
    agent wrote, Petar deleted and an agent wrote again names the agent.

    None = no commit carries the text at all — it lives in the worktree, and the
    worktree is nobody's word."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-S" + needle,
                          "--format=%H\t%an", "--", rel],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git log -S -- %s: %s"
                         % (rel, out.stderr.decode("utf-8", "replace").strip()))
    lines = out.stdout.decode("utf-8", "replace").splitlines()
    if not lines:
        return None
    parts = lines[-1].split("\t", 1)
    return (parts[0], parts[1] if len(parts) > 1 else "")


def newest_commit_on(rel):
    """(hash, author) of the NEWEST commit that touched a path — None if none.

    One truth for the two gates that ask the same question about a signed body:
    check 6 here (амандамент №9 т. 7) and `run_gates` проверка 7 (амандамент №5
    т. 3), which calls this one."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-1",
                          "--format=%H\t%an", "--", rel],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git log -1 -- %s: %s"
                         % (rel, out.stderr.decode("utf-8", "replace").strip()))
    lines = out.stdout.decode("utf-8", "replace").splitlines()
    if not lines:
        return None
    parts = lines[0].split("\t", 1)
    return (parts[0], parts[1] if len(parts) > 1 else "")


def repo_relative(path):
    """The path as the repository names it, or None when it is outside it.

    Both ends are resolved before they are compared: `--queue` may arrive
    relative to the current directory, and a gate that judges the blob of a path
    has to know the name git keeps it under."""
    try:
        return str(pathlib.Path(path).resolve()
                   .relative_to(pathlib.Path(str(REPO_ROOT)).resolve())).replace("\\", "/")
    except (ValueError, OSError):
        return None


def worktree_differs(rel):
    """True when `git status --porcelain -- <rel>` says anything at all.

    Modified, staged, untracked — all three mean the same thing for a gate that
    judges what a push sends: the bytes on this disk are not the bytes in the
    commit."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "status", "--porcelain", "--", rel],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError("git status --porcelain -- %s: %s"
                         % (rel, out.stderr.decode("utf-8", "replace").strip()))
    return bool(out.stdout.decode("utf-8", "replace").strip())


def commit_author(commit):
    """The author of one commit — None when git cannot resolve it at all.

    An anchor that names a commit is a claim about a hand: амандамент №7 т. 3
    asks who committed the body a refusal is measured against, and a name git
    refuses to give is an answer too (fail-closed at the call site)."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-1",
                          "--format=%an", commit, "--"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        return None
    return out.stdout.decode("utf-8", "replace").strip() or None


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_engine():
    """Import the reference engine. Importing it writes not one byte (§11 Р9)."""
    spec = importlib.util.spec_from_file_location(
        "recall_sweep_release", str(REPO_ROOT / ENGINE_REL))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SIGNATURE_FIELD = "signed_by"


def signed_by_of(doc):
    """`signed_by` wherever the artefact keeps it — top level or inside `_meta`."""
    if not isinstance(doc, dict):
        return None
    if SIGNATURE_FIELD in doc:
        return doc.get(SIGNATURE_FIELD)
    meta = doc.get("_meta")
    if isinstance(meta, dict):
        return meta.get(SIGNATURE_FIELD)
    return None


def body_without_signature(doc):
    """The artefact body with the SIGNATURE field removed, wherever it lives.

    The digest of a body has to be the same number before and after the act of
    signing: the pen computes it while it prepares the buffer (compute first,
    write last) and the gate recomputes it from the blob afterwards. Dropping
    `signed_by` — the one field `gates.sign` writes — is what makes those two
    numbers the same."""
    if not isinstance(doc, dict):
        return doc
    out = dict(doc)
    out.pop(SIGNATURE_FIELD, None)
    meta = out.get("_meta")
    if isinstance(meta, dict):
        meta = dict(meta)
        meta.pop(SIGNATURE_FIELD, None)
        out["_meta"] = meta
    return out


def body_digest(raw):
    """sha256 of an artefact BODY — its values, without the signature field.

    Амандамент №9 т. 7. Canonical (sorted keys, no spaces) on purpose: the
    number is about what the document SAYS, so re-indenting a signed body is not
    a rewrite and changing one measurement inside it is. `raw` is bytes (a blob)
    or text (the buffer the pen is about to write)."""
    text = raw.decode("utf-8") if isinstance(raw, bytes) else raw
    canonical = json.dumps(body_without_signature(json.loads(text)),
                           ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return digest(canonical.encode("utf-8"))


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
# Optional: the digest of the body Petar signed off on. Проверка 7 accepts it
# instead of his authorship on the NEWEST commit that touched the artefact —
# the freeze rewrites the body after the signature, and the number he recorded
# is what says he saw the result (амандамент №5 т. 3).
FIELD_DIGEST = u"дайджест"
# The digest of the BODY the pen signed — the values without the signature
# field (амандамент №9 т. 7). Check 6 recompares it with the blob at HEAD.
FIELD_BODY = u"тяло"

# Every field this parser understands. A field written twice in one row is a
# block (амандамент №9 т. 2): the parser keeps the last of them, a human reads
# the first, and „решение: не“ under „решение: да“ is that difference weaponised.
KNOWN_FIELDS = (FIELD_ID, FIELD_ASK, FIELD_DECISION, FIELD_DATE, FIELD_ARTEFACT,
                FIELD_COVERS, FIELD_DIGEST, FIELD_BODY)

# The three classes of row (амандамент №9 т. 5).
CLASS_QUESTION = u"въпрос"
CLASS_ARTEFACT = u"артефакт"
CLASS_DELTA = u"делта"


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
    """The rows of the queue FILE — `parse_queue_text` over its bytes."""
    return parse_queue_text(path.read_text(encoding="utf-8"))


# The two regions markdown does not show: a fenced block and an HTML comment.
FENCE = re.compile(r"^\s*(?:```|~~~)")
COMMENT_OPEN, COMMENT_CLOSE = u"<!--", u"-->"
# A `решение` field, with or without the bullet and the emphasis — what a hidden
# region may not contain (амандамент №9 т. 2).
DECISION_LINE = re.compile(r"(?:\*\*)?\s*%s\s*:" % re.escape(FIELD_DECISION))


def visible_and_hidden(text):
    """([(n, line)], [(n, line)]) — what a reader sees, and what markdown hides.

    Амандамент №9 т. 2: the machine reads only what the human reads. A ```/~~~
    fence and an `<!-- -->` comment are invisible in every markdown viewer and
    in the diff Petar signs off on, so a row written inside one is a row he
    cannot see. Both are tracked line by line rather than with a regex over the
    whole text, because a queue is edited by hand and an unclosed fence must
    swallow the rest of the file rather than reopen the parser to it.

    A line that merely CONTAINS `<!--` is hidden whole. That over-reaches by the
    few characters in front of the marker, and it over-reaches fail-closed: the
    alternative is a parser that reads half a line the reader sees as prose."""
    visible, hidden = [], []
    in_fence, in_comment = False, False
    for n, line in enumerate(text.splitlines(), 1):
        if in_comment:
            hidden.append((n, line))
            if COMMENT_CLOSE in line:
                in_comment = False
            continue
        if in_fence:
            hidden.append((n, line))
            if FENCE.match(line):
                in_fence = False
            continue
        if FENCE.match(line):
            hidden.append((n, line))
            in_fence = True
            continue
        if COMMENT_OPEN in line:
            hidden.append((n, line))
            if COMMENT_CLOSE not in line.split(COMMENT_OPEN, 1)[1]:
                in_comment = True
            continue
        visible.append((n, line))
    return visible, hidden


def hidden_decisions(text):
    """[(n, line)] — every `решение:` written where the human cannot see it.

    Not a parse: a complaint. The parser above simply ignores these lines, which
    is what makes the hidden row powerless; this function is what makes it LOUD,
    so a queue that carries one is blocked instead of being quietly shorter than
    it looks."""
    return [(n, line) for n, line in visible_and_hidden(text)[1]
            if DECISION_LINE.search(line)]


def parse_queue_text(text):
    """The rows of a queue, as data, from the text of one.

    Проверка 7 and the release gate both read the queue out of the BLOB of a
    commit rather than off the disk (амандамент №7 т. 2, №9 т. 1): a decision is
    Petar's word only where his commit put it, and the worktree is nobody's
    word. Both readers share this parser, so the blob and the file can never be
    read by two different rules.

    The queue is MARKDOWN because a human reads it and signs it; the shape is
    fixed so a machine can read it too (план v2 §0.6):

        ## R3 · манифест BASE→P7
        - **id:** R3
        - **питане:** …
        - **решение:** pending
        - **дата:** —
        - **артефакт:** manifest_base_p7
        - **покрива:** gate_lot1v_v/*, gate_m7_bare/*

    Only the VISIBLE lines are read (амандамент №9 т. 2) — see
    `visible_and_hidden`. Each row also carries:

      * `block` — its verbatim text, from `## <id>` down to its LAST field line,
        every line in between included whether the reader sees it or not. That
        is the needle `yes_row_authorship` gives `git log -S`, so a line slipped
        between the fields of a row moves the authorship of the whole row to
        that hand. It stops at the last field on purpose: a note appended after
        a row is not part of the row, and a block that ran to the next heading
        would let the next hand that touches the file inherit the row;
      * `duplicates` — the fields written twice in it;
      * `has_covers` / `has_artefact` — whether the FIELD is there at all, which
        is what decides the class of the row: `покрива:` with nothing after it is
        a delta row that refuses nothing, not a question.
    """
    lines = text.splitlines()
    visible = set(n for n, _ in visible_and_hidden(text)[0])
    rows, current = [], None

    def close(row):
        row["block"] = u"\n".join(lines[row["start"] - 1:row["last"]])
        rows.append(row)

    for n, line in enumerate(lines, 1):
        if n not in visible:
            continue
        head = QUEUE_HEAD.match(line)
        if head:
            if current:
                close(current)
            current = {"id": head.group(1), "title": (head.group(2) or "").strip(),
                       "fields": {}, "duplicates": [], "start": n, "last": n}
            continue
        if current is None:
            continue
        pair = QUEUE_KEY.match(line)
        if pair:
            key = pair.group(1).strip()
            if key in current["fields"] and key not in current["duplicates"]:
                current["duplicates"].append(key)
            current["fields"][key] = pair.group(2).strip()
            current["last"] = n
    if current:
        close(current)
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
            "digest": (fields.get(FIELD_DIGEST) or "").strip(),
            "body": (fields.get(FIELD_BODY) or "").strip(),
            "block": row["block"],
            "duplicates": list(row["duplicates"]),
            "has_covers": FIELD_COVERS in fields,
            "has_artefact": FIELD_ARTEFACT in fields,
        })
    return out


def row_class(row):
    """„въпрос“ · „артефакт“ · „делта“ — амандамент №9 т. 5.

    The refusal rules of амандаменти 6–8 („не“ names an exact query, a refusal
    that reaches nothing blocks) are rules about DELTAS, and applying them to
    every row made Q7 („break-glass: вън“) unanswerable: a political „не“ with
    no `покрива` was read as a refusal about nothing and held the delivery.

    The class is decided by the FIELDS, not by their values: `покрива:` with
    nothing after it is a delta row whose refusal is empty — still a block —
    while a row with no `покрива` line at all was never about a delta. A row
    built by hand (a fixture, a caller that never parsed a file) has no
    `has_covers`, and then the parsed list answers for it."""
    if row.get("has_covers", bool(row["covers"])):
        return CLASS_DELTA
    if row.get("has_artefact", bool(row.get("artefact"))) and row.get("artefact"):
        return CLASS_ARTEFACT
    return CLASS_QUESTION


def yes_row_authorship(queue_rel, rows):
    """Complaints for every „да“ no commit of Petar's ever wrote.

    Амандамент №9 т. 2. Проверка 7 asked who introduced a SIGNATURE and who
    introduced a DIGEST; nobody asked who introduced the word „да“. An agent
    that edits the queue, commits it and lets Petar commit anything at all
    afterwards used to hand itself every permission in the file.

    The needle is the verbatim block of the row, so the question is not „did the
    string да ever appear“ but „whose commit brought THIS row, as it stands, into
    the file“ — and a line somebody else slipped into the block makes the block a
    different text with a different author. `git log -S` per row costs one git
    call per „да“; the queue of a delivery is a dozen rows, and the price of the
    other answer was measured in A.2-10."""
    out = []
    for row in rows:
        if row["decision"] != YES:
            continue
        block_text = row.get("block")
        if not block_text:
            out.append(u"ред %s: „да“ без тяло на реда — авторството не може да "
                       u"се провери" % row["id"])
            continue
        try:
            origin = introduced_by_text(queue_rel, block_text)
        except (ValueError, OSError) as exc:
            out.append(u"ред %s: авторството не можа да се измери: %s" % (row["id"], exc))
            continue
        if origin is None:
            out.append(u"ред %s: „да“, което не е въведено от нито един комит — "
                       u"пушът праща блоба, не работното дърво" % row["id"])
        elif origin[1] != HUMAN_AUTHOR:
            out.append(u"ред %s: „да“ е въведено от %r в %s, а подписва само %s"
                       % (row["id"], origin[1], origin[0][:7], HUMAN_AUTHOR))
    return out


# How closely a `покрива` pattern speaks about one delta. The numbers only ever
# get compared with each other: EXACT is the query written out by name, WIDE is
# the whole bucket in one word.
NO_MATCH, WIDE, EXACT = 0, 1, 2


def match_strength(pattern, bucket, query):
    """NO_MATCH · WIDE (`кофа/*`) · EXACT (`кофа/точната заявка`)."""
    if "/" not in pattern:
        return NO_MATCH
    where, _, what = pattern.partition("/")
    if where != bucket:
        return NO_MATCH
    if what == (query or ""):
        return EXACT
    return WIDE if what == "*" else NO_MATCH


def covers_delta(pattern, bucket, query):
    """One `покрива` pattern against one delta: `bucket/query` or `bucket/*`."""
    return match_strength(pattern, bucket, query) != NO_MATCH


def row_strength(row, bucket, query):
    """The closest thing a whole row says about one delta (0 = it is silent)."""
    return max([match_strength(p, bucket, query) for p in row["covers"]] or [NO_MATCH])


def wildcard_covers(covers):
    """The patterns of a row that name a whole bucket at once (`кофа/*`).

    Амандамент №6 т. 2: a „не“ is a decision about a named query, so it is
    written as `кофа/точната заявка`. A refusal spelled `кофа/*` refuses a whole
    bucket in one word — which reads as a class permission that happens to say
    „не“, and is exactly the shape that made the verdict depend on the order of
    the file. `gates.sign` refuses to write one; the gate reads one fail-closed.
    """
    out = []
    for pattern in covers:
        where, sep, what = pattern.partition("/")
        if sep and what == "*":
            out.append(pattern)
    return out


# Why one `покрива` pattern of a „не“ row refuses nothing (амандамент №8 т. 1).
# The two reasons are different mistakes: the first is a pattern a machine
# cannot even read as a query, the second is a query nobody delivered.
REFUSAL_MALFORMED = u"шаблонът не е във вида кофа/заявка"
REFUSAL_UNREACHED = u"не улучва нито жива делта, нито разлика спрямо котвата"
# An empty `покрива` under a „не“ is neither of the two — there is no pattern
# to name, so the row itself is named.
REFUSAL_EMPTY = u"„покрива“ е празно — „не“ се пише по ТОЧНАТА заявка (кофа/заявка)"


def refusal_pattern_reason(pattern, hit):
    """Why this pattern of a „не“ row covers nothing — or None when it does.

    `hit` is the set of patterns of that row which reached something. The two
    readers of this rule — the gate and `gates.sign` — get their words from
    here, so a refusal is refused with the same sentence wherever it is caught.
    """
    if "/" not in pattern:
        return REFUSAL_MALFORMED
    return None if pattern in hit else REFUSAL_UNREACHED


def patterns_that_cover(row, deltas):
    """The `покрива` patterns of one row that hit at least one of these deltas.

    `deltas` is any iterable of `(кофа, заявка)` pairs. Per PATTERN, because
    амандамент №8 т. 3 asks which of them did the work, not whether the row
    did."""
    return set(pattern for pattern in row["covers"]
               if any(covers_delta(pattern, bucket, query) for bucket, query in deltas))


def decide_delta(rows, bucket, query):
    """The verdict of the WHOLE queue on one delta — never of the first row.

    Амандамент №6 т. 2. Every matching row is collected, then:

      * a „не“ wins, whatever the order of the file and however wide the „да“
        that also matches — a refusal that can be out-voted is not terminal;
      * among rows that agree, the more specific pattern is the one named, so a
        class row `кофа/*` never speaks for a query somebody answered by name;
      * only `pending` (or nothing) matching means the delta is uncovered.

    Returns `(decision, row, matched)`: `matched` is every row that touches this
    delta, because a row that matched is a row that was used — marking only the
    winner would turn the loser into a „stale permission“ on the next line.
    """
    matched = []
    for row in rows:
        strength = row_strength(row, bucket, query)
        if strength != NO_MATCH:
            matched.append((strength, row))
    everyone = [row for _, row in matched]
    for decision in (NO, YES):
        same = [pair for pair in matched if pair[1]["decision"] == decision]
        if same:
            return (decision, max(same, key=lambda pair: pair[0])[1], everyone)
    return (None, None, everyone)


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


# ------------------------------------------------- a refusal survives the freeze

def refusal_survivors(expectations_doc, rows):
    """Complaints for every refusal the freeze WROTE DOWN (`_meta.refused`).

    `--freeze` refuses to run while a „не“ row covers a live delta, so a frozen
    body should carry an empty list. If it carries anything, that is the freeze
    saying what it saw, and it blocks — including after the delta itself has
    been erased by the freeze, which is the whole point (амандамент №5 т. 1).
    A recorded refusal whose row has since been re-decided blocks as well: „не“
    is terminal (план v2 §0.6), so a row that changed its mind changed it by
    hand, and a hand belongs in a new round, not in this gate.
    """
    out = []
    recorded = (((expectations_doc or {}).get("_meta") or {}).get("refused") or [])
    by_id = dict((row["id"], row) for row in rows)
    for item in recorded:
        row_id = item.get("row")
        where = u"%s/%s" % (item.get("bucket"), item.get("q"))
        row = by_id.get(row_id)
        if row is None:
            out.append(u"%s: записан отказ по ред %s, а такъв ред няма в опашката"
                       % (where, row_id))
        elif row["decision"] == NO:
            out.append(u"%s: ред %s е ОТКАЗАН (терминално) — записано в очакванията"
                       % (where, row_id))
        else:
            out.append(u"%s: записан отказ по ред %s, а редът сега е %r — отказът "
                       u"не се сваля с ново решение" % (where, row_id, row["decision"]))
    return out


def queue_reference(expectations_doc):
    """(commit, path, sha256, complaint) — the reference THE QUEUE was written against.

    Амандамент №7 т. 3: the anchor is a FIELD, `_meta.queue_reference`, written
    by the two tools that measure it — `recall_sweep.build_expectations` when it
    produces the body and `gates.sign` when Petar signs one. Until now it was
    derived: „the newest commit that moved the signature string, then read
    `_meta.reference` out of its blob“. That derivation can be aimed. An agent
    commit that adds a SECOND occurrence of `"signed_by": "Петър"` is the newest
    commit `git log -S` reports, so the anchor moves to a body the agent chose —
    and with it every refusal the queue was carrying.

    Two things are demanded of the field and both BLOCK rather than fall back:
    the anchor exists at all, and its commit is Petar's own (амандамент №6 makes
    him the author of every freeze, so the reference a queue answers about is
    always in a commit of his). `_meta.base` never votes here: it is a commit
    constant of the engine and knows nothing about which queue is being answered.
    """
    anchor = ((expectations_doc or {}).get("_meta") or {}).get(QUEUE_REFERENCE_KEY) or {}
    commit, rel, want = anchor.get("commit"), anchor.get("path"), anchor.get("sha256")
    if not commit or not rel:
        return (None, None, None,
                u"подписаните очаквания нямат изрична котва „_meta.%s“ (комит + "
                u"път + дайджест) — отказът няма срещу какво да се провери"
                % QUEUE_REFERENCE_KEY)
    author = commit_author(commit)
    if author is None:
        return (None, None, None,
                u"котвата „_meta.%s“ сочи комит %s, който git не разпознава"
                % (QUEUE_REFERENCE_KEY, commit[:7]))
    if author != HUMAN_AUTHOR:
        return (None, None, None,
                u"котвата „_meta.%s“ сочи комит %s на %r — референцията, срещу "
                u"която е писана опашката, стои в комит на %s"
                % (QUEUE_REFERENCE_KEY, commit[:7], author, HUMAN_AUTHOR))
    return (commit, rel, want, None)


def reference_commit():
    """The commit that CARRIES the frozen reference right now.

    `git log -1 -- <reference>`: the newest commit that changed those bytes. It
    is the commit a queue is answered against, because the deltas Petar reads
    are measured from exactly that body forward — and амандамент №6 makes him
    the author of every freeze, so it is his commit, which is what
    `queue_reference` then demands of the anchor."""
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "log", "-1", "--format=%H",
                          "--", REFERENCE_REL],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise ValueError(u"git log -- %s: %s"
                         % (REFERENCE_REL, out.stderr.decode("utf-8", "replace").strip()))
    lines = out.stdout.decode("utf-8", "replace").splitlines()
    if not lines:
        raise ValueError(u"%s не е в нито един комит" % REFERENCE_REL)
    return lines[0].strip()


def queue_reference_anchor():
    """The value `_meta.queue_reference` must carry right now — commit and bytes.

    ONE truth for the two writers of that field (амандамент №7 т. 3):
    `recall_sweep.build_expectations`, which measures the body, and
    `gates.sign`, which refreshes it under Petar's hand as he signs. Same shape
    as every other commit anchor in this delivery — path, commit, digest, size —
    so the structural anchor walk reads it like the rest."""
    commit = reference_commit()
    raw = blob_at(commit, REFERENCE_REL)
    return {"sha256": digest(raw), "bytes": len(raw), "path": REFERENCE_REL,
            "commit": commit,
            "what": u"референцията, срещу която е писана опашката"}


def refused_against_reference(expectations_doc, rows, reference):
    """(complaints, reached) — the refusals re-derived from the BYTES.

    Independent of `_meta.refused`: anything a „не“ row covers that still differs
    between the reference the queue was written against and the reference at
    HEAD is a refusal the delivery is carrying anyway. A body that simply forgot
    to write its refusals down does not get past this.

    `reached` is `{row id: {pattern that answered such a difference}}` — what
    амандамент №7 т. 1 needs to tell „this refusal covers nothing“ apart from
    „this refusal is doing its job“, PER PATTERN since амандамент №8 т. 3: a row
    that reached a difference with one of its three patterns has still written
    the other two about nothing. It is None when the comparison could not be
    made at all (no anchor, foreign anchor, unreadable blob): then the complaint
    on the table is about the anchor, and no row may be called empty on the
    strength of a comparison that never happened.
    """
    refused_rows = [row for row in rows if row["decision"] == NO and row["covers"]]
    if not refused_rows:
        return ([], {})
    commit, rel, want, complaint = queue_reference(expectations_doc)
    if complaint:
        return ([u"опашката отказва %d реда, а %s" % (len(refused_rows), complaint)],
                None)
    try:
        raw = blob_at(commit, rel)
    except (ValueError, OSError) as exc:
        return ([u"референцията на опашката (%s:%s): %s" % (commit, rel, exc)], None)
    if want and digest(raw) != want:
        return ([u"референцията на опашката (%s:%s): %s ≠ подписаното %s"
                 % (commit, rel, digest(raw)[:12], want[:12])], None)
    try:
        base_doc = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        return ([u"референцията на опашката (%s:%s): %s" % (commit, rel, exc)], None)
    out, reached = [], {}
    for delta in compare(entries_of(base_doc), reference):
        spoke = None
        for row in refused_rows:
            hits = [p for p in row["covers"]
                    if covers_delta(p, delta["bucket"], delta["q"])]
            if not hits:
                continue
            # Every row that reaches this difference is recorded, with the
            # patterns that did it; only the first one is complained about, so
            # the table keeps one line per difference as it always has.
            reached.setdefault(row["id"], set()).update(hits)
            if spoke is None:
                spoke = row
        if spoke is not None:
            out.append(u"%s/%s: ред %s е ОТКАЗАН, а разликата спрямо "
                       u"референцията на опашката (%s) е в замразената "
                       u"референция (%s)"
                       % (delta["bucket"], delta["q"], spoke["id"], commit[:7],
                          u"; ".join(delta["why"])))
    return (out, reached)


def refusals_that_cover_nothing(rows, used, reached):
    """Complaints, PER PATTERN, for every „не“ that refuses nothing.

    Амандамент №7 т. 1 — the twin of the stale-permission rule. A „да“ that
    covers nothing is blocked because a permission for a delta nobody delivered
    is not a permission; a „не“ that covers nothing was simply MUTE, and mute is
    worse: `gate_lot1/Градината` for `gate_lot1/градина` refused nothing, the
    gate went green, and one freeze later the refused difference was inside the
    reference. A refusal has to reach something — a live delta (`used`) or a
    difference between the queue's reference and the frozen one (`reached`).

    Амандамент №8 т. 1 и т. 3 close the two remaining ways past it. `used` and
    `reached` are `{row id: {pattern that hit}}`, so the question is asked of
    every pattern separately: a row that refuses three queries and misspells one
    of them is a row with a typo in it, and the two true refusals do not make
    the third one true. The measurement is over the RAW `покрива`, so a pattern
    with no slash (`gate_lot1градина`) is named as malformed instead of being
    filtered away before anybody looks — and a „не“ with an empty `покрива` is
    named too, because refusing nothing at all is the same silence.

    ONLY A DELTA ROW IS ASKED (амандамент №9 т. 5): a „не“ on a question or on
    an artefact is a decision about something that is not a query, and the
    release answers it elsewhere (by the artefact, or not at all).

    THE UNCONDITIONAL REASONS ARE GIVEN EVEN WITHOUT AN ANCHOR (амандамент №9
    т. 3). `reached is None` means the comparison against the queue's reference
    never happened, so „this pattern reached nothing“ cannot be said — but „this
    pattern is not a query at all“ and „there is no pattern“ are properties of
    the row itself, and a row that is malformed on its face is named whether or
    not the anchor could be read."""
    out = []
    for row in rows:
        if row["decision"] != NO or row_class(row) != CLASS_DELTA:
            continue
        if not row["covers"]:
            out.append(u"ред %s отказва заявка, която не съществува: %s"
                       % (row["id"], REFUSAL_EMPTY))
            continue
        hit = set(used.get(row["id"]) or ()) | set((reached or {}).get(row["id"]) or ())
        for pattern in row["covers"]:
            reason = refusal_pattern_reason(pattern, hit)
            if reason is None:
                continue
            if reason == REFUSAL_UNREACHED and reached is None:
                continue
            out.append(u"ред %s отказва заявка, която не съществува: %s — %s"
                       % (row["id"], pattern, reason))
    return out


def refusable_deltas(expectations_doc=None):
    """({(bucket, q)}, complaint) — every delta a „не“ could be about right now.

    The union of what this gate judges: the LIVE deltas (the frozen reference at
    HEAD ↔ the engine candidate) and the differences between the reference the
    queue was written against and the frozen one — the second half is what a
    refusal still reaches after a freeze has erased the first. `gates.sign` asks
    THIS function before it writes a „не“ (амандамент №7 т. 1), so the pen and
    the gate measure a refusal against one and the same set, and a typo is
    refused by the hand that makes it instead of going mute in the gate.

    The complaint is about the second half only: without a readable anchor the
    live deltas are still the honest answer for a queue nobody has frozen yet.
    """
    try:
        reference_doc = json.loads(blob_at("HEAD", REFERENCE_REL).decode("utf-8"))
    except (ValueError, OSError, UnicodeDecodeError) as exc:
        return (set(), u"референцията (%s) не може да се прочете: %s"
                % (REFERENCE_REL, exc))
    reference = entries_of(reference_doc)
    try:
        candidate = entries_of(load_engine().reference_rows())
    except (ValueError, OSError, SystemExit) as exc:
        return (set(), u"двигателят не отговори: %s" % exc)
    out = set((delta["bucket"], delta["q"]) for delta in compare(reference, candidate))
    if expectations_doc is None:
        try:
            expectations_doc = json.loads(
                blob_at("HEAD", EXPECTATIONS_REL).decode("utf-8"))
        except (ValueError, OSError, UnicodeDecodeError) as exc:
            return (out, u"очакванията (%s) не могат да се прочетат: %s"
                    % (EXPECTATIONS_REL, exc))
    commit, rel, _want, complaint = queue_reference(expectations_doc)
    if complaint:
        return (out, complaint)
    try:
        base_doc = json.loads(blob_at(commit, rel).decode("utf-8"))
    except (ValueError, OSError, UnicodeDecodeError) as exc:
        return (out, u"референцията на опашката (%s:%s): %s" % (commit, rel, exc))
    out |= set((delta["bucket"], delta["q"])
               for delta in compare(entries_of(base_doc), reference))
    return (out, None)


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

    # --- 1. the artefacts and their signatures, READ FROM THE BLOB -----------
    # Амандамент №5 т. 5: a push publishes the blob at HEAD, so the gate judges
    # the blob at HEAD. The worktree copy is compared with it as a body (not as
    # bytes: `.gitattributes` gives a Windows checkout the CRLF twin of the same
    # OID), and a difference is blocked — that is „signed on my disk, unsigned
    # in the commit“, which is exactly how an unsigned delivery gets published.
    artefacts = {}
    table = signable()
    for name in sorted(table):
        rel = table[name]
        path = REPO_ROOT / rel
        if not path.exists():
            block(u"липсва %s (%s)" % (rel, name))
            continue
        try:
            raw = blob_at("HEAD", rel)
            doc = json.loads(raw.decode("utf-8"))
        except (ValueError, OSError) as exc:
            block(u"%s (%s): няма го в блоба на HEAD — %s" % (rel, name, exc))
            continue
        try:
            on_disk = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            block(u"%s: %s" % (rel, exc))
            continue
        if on_disk != doc:
            block(u"%s: работното дърво носи друго тяло от блоба на HEAD "
                  u"(пушът праща блоба)" % rel)
        signature = signed_by_of(doc)
        artefacts[name] = {"rel": rel, "doc": doc, "signed_by": signature, "blob": raw}
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
        # THE BLOB, never the file (амандамент №9 т. 1). The pen writes the
        # decisions into the worktree; what a push publishes is the commit, and
        # a gate that reads the disk goes green over a commit with no signed row
        # in it at all.
        queue_rel = repo_relative(queue_path)
        queue_text = None
        if queue_rel is None:
            block(u"опашката %s е извън това репо — гейтът съди блоба на HEAD"
                  % queue_path)
        else:
            try:
                queue_text = blob_at("HEAD", queue_rel).decode("utf-8")
            except (ValueError, OSError, UnicodeDecodeError) as exc:
                block(u"%s: няма я в блоба на HEAD — %s" % (queue_rel, exc))
        if queue_text is not None:
            if worktree_differs(queue_rel):
                block(u"%s: работното дърво носи друго тяло от блоба на HEAD "
                      u"(пушът праща блоба)" % queue_rel)
            rows = parse_queue_text(queue_text)
            say(u"опашка: %s — %d реда (блобът на HEAD)"
                % (queue_path.name, len(rows)))
            # A decision written where the reader cannot see it (амандамент №9
            # т. 2). The parser already ignores it; this is what makes it loud.
            for line_no, line in hidden_decisions(queue_text):
                block(u"%s ред %d: „решение“ в скрит регион (коментар или code "
                      u"fence) — машината чете само каквото човекът вижда: %s"
                      % (queue_rel, line_no, line.strip()[:60]))
        for row in rows:
            for field in row.get("duplicates") or []:
                if field in KNOWN_FIELDS:
                    block(u"ред %s: полето „%s“ е написано два пъти — един ред, "
                          u"едно решение" % (row["id"], field))
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
            # The two classes that are not about deltas say so out loud, so a
            # „не“ Petar wrote on a question is visible as a decision rather
            # than as silence (амандамент №9 т. 5).
            if row["decision"] == NO:
                kind = row_class(row)
                if kind == CLASS_QUESTION:
                    say(u"ред %s: „не“ по въпрос — решението е записано, в "
                        u"release не влиза" % row["id"])
                elif kind == CLASS_ARTEFACT:
                    say(u"ред %s: „не“ по артефакта %r — артефактът не се "
                        u"подписва (release съди по него)"
                        % (row["id"], row["artefact"]))

        # Whose hand wrote the „да“ (амандамент №9 т. 2).
        if queue_rel is not None and queue_text is not None:
            for complaint in yes_row_authorship(queue_rel, rows):
                block(u"%s: %s" % (queue_rel, complaint))

        # …and what the signature was given to (амандамент №9 т. 7): the digest
        # of the BODY, recorded on the row by the pen, recompared with the blob.
        for row in rows:
            want = row.get("body")
            entry = artefacts.get(row["artefact"]) if row["artefact"] else None
            if not want or entry is None:
                continue
            try:
                got = body_digest(entry["blob"])
            except (ValueError, UnicodeDecodeError) as exc:
                block(u"%s: тялото не може да се смята — %s" % (entry["rel"], exc))
                continue
            if got == want:
                say(u"%s: тялото %s = дайджеста на ред %s ✓"
                    % (entry["rel"], got[:12], row["id"]))
                continue
            # The body moved after the signature. That is the freeze — which
            # Petar commits (амандамент №6) — or it is a rewrite. The newest
            # commit on the path is what tells the two apart, exactly as
            # проверка 7 tells them apart; the difference is that `--freeze`
            # reads THIS verdict and never reads проверка 7.
            try:
                newest = newest_commit_on(entry["rel"])
            except (ValueError, OSError) as exc:
                newest = None
                say(u"%s: последният комит не можа да се прочете — %s"
                    % (entry["rel"], exc))
            if newest is not None and newest[1] == HUMAN_AUTHOR:
                say(u"%s: тялото %s ≠ дайджеста на ред %s (%s) — пренаписано "
                    u"след подписа, но последният комит по него е %s на %s "
                    u"(замразяването)"
                    % (entry["rel"], got[:12], row["id"], want[:12],
                       newest[0][:7], newest[1]))
            else:
                block(u"%s: тялото %s ≠ дайджеста %s на ред %s — подписаното "
                      u"тяло е пренаписано (последен комит %s на %r)"
                      % (entry["rel"], got[:12], want[:12], row["id"],
                         (newest[0][:7] if newest else u"—"),
                         (newest[1] if newest else u"—")))

    # {row id: {pattern that covered a live delta}} — the id half answers the
    # stale-permission rule below, the patterns answer амандамент №8 т. 3.
    used, uncovered, refused = {}, [], []
    for delta in deltas:
        # The whole queue answers, not the first row that happens to match
        # (амандамент №6 т. 2). Every matching row counts as used: a „да“ that
        # lost to a „не“ still covers a live delta and is not a stale permission.
        decision, row, matched = decide_delta(rows, delta["bucket"], delta["q"])
        for other in matched:
            used.setdefault(other["id"], set()).update(
                patterns_that_cover(other, [(delta["bucket"], delta["q"])]))
        if decision == NO:
            block(u"%s/%s: ред %s е ОТКАЗАН (терминално)"
                  % (delta["bucket"], delta["q"], row["id"]))
            refused.append({"bucket": delta["bucket"], "q": delta["q"],
                            "row": row["id"], "why": delta["why"]})
        elif decision != YES:
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

    # --- 7. the refusals, after the freeze has erased the deltas -------------
    survivors = refusal_survivors(expectations, rows)
    for complaint in survivors:
        block(u"отказ: " + complaint)
        refused.append({"bucket": None, "q": None, "row": None, "why": [complaint]})
    rederived, reached = refused_against_reference(expectations, rows, reference)
    for complaint in rederived[:10]:
        block(u"отказ (от байтовете): " + complaint)
    if len(rederived) > 10:
        block(u"… още %d отказани разлики в замразената референция"
              % (len(rederived) - 10))
    if rederived:
        refused.extend({"bucket": None, "q": None, "row": None, "why": [c]}
                       for c in rederived)

    # --- 8. and a refusal that reaches nothing (амандамент №7 т. 1) ---------
    empty = refusals_that_cover_nothing(rows, used, reached)
    for complaint in empty:
        block(complaint)
    if not survivors and not rederived and not empty and rows:
        say(u"отказите: 0 записани, 0 в замразената референция, 0 празни ✓")

    return verdict(lines, bad, deltas, uncovered, stale, refused)


def verdict(lines, bad, deltas, uncovered, stale, refused=None):
    return {
        "exit_code": EXIT_BLOCKED if bad else EXIT_OK,
        "verdict": (u"BLOCKED: %d" % len(bad)) if bad else u"зелено",
        "lines": lines,
        "blocked": bad,
        "deltas": deltas,
        "uncovered": uncovered,
        "stale": stale,
        "refused": list(refused or []),
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
