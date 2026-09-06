#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gate for lot Н5 of the night plan "Границите" (06->07.09.2026).

Contract (plan §2а, last row):
    python scratch/places_search/qa_night_acceptance.py --report docs/audits/ДОКЛАД_07.09_нощна_смяна.md
exit 0 means: every lot of the plan's §2 table has a block in the report and that block
carries the sha256 values of its write-set, the exit code of its gate and of every negative
fixture (each != 0), the author of its commit and the commit message verbatim.

Negative fixtures (each MUST exit != 0):
  * a copy of the report with the block of one lot removed,
  * a copy in which the exit codes of a lot's negative fixtures are set to 0
    (a gate without a failing fixture),
  * a copy with one flipped hex character in a write-set sha256,
  * a copy with a tampered commit author.

Every recorded exit code must carry the name and the command it was measured with (an exit
code nobody can re-run is not evidence), and the report must quote the sha256 of the signed
plan body.

The gate does not trust the report: every sha256 is recomputed from the file on disk and
every commit sha, author and message is re-read from git. The verbatim messages and the
write-set paths are parsed out of the SIGNED plan, so a report that renames a lot's message
or drops a path is red as well.

The gate reads only; it never writes into any of the three repositories.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys

# stdout carries Bulgarian text; Windows consoles default to cp1252 without this.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CHUNK = 1024 * 1024

PLAN_PATH = "docs/plans/ПЛАН_НОЩНА_СМЯНА_Границите_06.09.md"

# Roots of the three repositories the plan works in.
REPO_ROOTS = {
    "varna_3d": "C:/git/varna_3d",
    "Varna_buildings": "C:/git/Varna_buildings",
}

STATUS_GREEN = "ЗЕЛЕН"
STATUS_RED = "ЧЕРВЕН"
STATUS_NOT_RUN = "НЕИЗПЪЛНЕН"
STATUSES = (STATUS_GREEN, STATUS_RED, STATUS_NOT_RUN)

SELF_SHA_MARKER = "самореферентен (този доклад)"
NO_FILE_MARKER = "не съществува (лотът не е изпълнен)"
NO_COMMIT_MARKER = "няма"
PENDING_COMMIT_MARKER = "предстои (този комит)"

MORNING_HEADING = "Какво прави Петър сутринта"

# The AGKK national code must never appear in a public deliverable (plan §4).
# Assembled from parts so that this gate is not itself an occurrence of the string.
FORBIDDEN_CODE = "101" + "35"

# GeoJSON keys: geometry travels as a key or as numbers, never as an English noun.
GEOJSON_KEYS = ('"coordinates"', "'coordinates'", '"geometry"', "'geometry'")

# Coordinate-looking decimals inside the Varna box; the report must carry none (plan §0.2).
COORD_PATTERNS = (
    re.compile(r"\b4[23]\.\d{4,}"),
    re.compile(r"\b2[78]\.\d{4,}"),
)

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def run(args, cwd=None):
    """Run a git command and return (exit_code, stdout, stderr) as text."""
    proc = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (
        proc.returncode,
        proc.stdout.decode("utf-8", "replace"),
        proc.stderr.decode("utf-8", "replace"),
    )


class Report(object):
    """Collects the verdict lines; any red line makes the gate red."""

    def __init__(self):
        self.failed = 0
        self.checks = 0

    def check(self, name, ok, detail=""):
        self.checks += 1
        if ok:
            print("[ЗЕЛЕНО] %s%s" % (name, (" — " + detail) if detail else ""))
        else:
            self.failed += 1
            print("[ЧЕРВЕНО] %s%s" % (name, (" — " + detail) if detail else ""))
        return ok


def strip_parentheticals(text):
    """Drop '(...)' spans: the plan uses them for outputs that are NOT in the write-set."""
    out = []
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth:
                depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def parse_plan(plan_text):
    """Parse the §2 lot table of the signed plan.

    Returns {code: {"repo": str, "paths": [str], "message": str}} in plan order.
    """
    lots = {}
    order = []
    in_table = False
    for line in plan_text.split("\n"):
        if line.startswith("| Лот |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            if set(cells[0]) <= set("-: "):
                continue
            code = cells[0].split()[0]
            repo = cells[1]
            paths = [
                p
                for p in re.findall(r"`([^`]+)`", strip_parentheticals(cells[2]))
                if "/" in p and not p.endswith("/")
            ]
            message = cells[3].strip().strip("`")
            lots[code] = {"repo": repo, "paths": paths, "message": message}
            order.append(code)
    return lots, order


def parse_report(report_text):
    """Parse the ```лот blocks of the report into dictionaries."""
    blocks = []
    current = None
    for raw in report_text.split("\n"):
        line = raw.rstrip()
        if current is None:
            if line.strip() == "```лот":
                current = {
                    "код": None,
                    "статус": None,
                    "комит": None,
                    "автор": None,
                    "съобщение": None,
                    "причина": None,
                    "files": [],
                    "gates": [],
                    "negatives": [],
                    "probes": [],
                    "unknown": [],
                }
            continue
        if line.strip() == "```":
            blocks.append(current)
            current = None
            continue
        if not line.strip():
            continue
        if ":" not in line:
            current["unknown"].append(line)
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "файл":
            if "=" in value:
                path, sha = value.split("=", 1)
                current["files"].append((path.strip(), sha.strip()))
            else:
                current["files"].append((value, ""))
        elif key in ("гейт", "фикстура", "проба"):
            parts = [p.strip() for p in value.split("|")]
            entry = {"exit": parts[0], "rest": parts[1:]}
            if key == "гейт":
                current["gates"].append(entry)
            elif key == "фикстура":
                current["negatives"].append(entry)
            else:
                current["probes"].append(entry)
        elif key in current:
            current[key] = value
        else:
            current["unknown"].append(line)
    return blocks


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def main():
    parser = argparse.ArgumentParser(description="Гейт Н5: приемане на нощния доклад.")
    parser.add_argument("--report", required=True, help="път до доклада (MD)")
    parser.add_argument("--plan", default=PLAN_PATH, help="път до подписания план")
    args = parser.parse_args()

    code, out, _ = run(["git", "rev-parse", "--show-toplevel"])
    if code != 0:
        print("[ЧЕРВЕНО] гейтът не се пуска извън git дърво")
        return 2
    fire_varna = out.strip()
    roots = dict(REPO_ROOTS)
    roots["Fire_Varna"] = fire_varna

    rep = Report()

    # --- C1: the report itself -------------------------------------------------
    if not os.path.isfile(args.report):
        print("[ЧЕРВЕНО] C1 доклад — липсва файл: %s" % args.report)
        return 2
    with open(args.report, "rb") as fh:
        raw = fh.read()
    rep.check("C1 доклад·BOM", not raw.startswith(b"\xef\xbb\xbf"), "UTF-8 без BOM")
    rep.check("C1 доклад·LF", b"\r" not in raw, "нула CR знака")
    try:
        report_text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print("[ЧЕРВЕНО] C1 доклад — не е валиден UTF-8: %s" % exc)
        return 2

    plan_full = os.path.join(fire_varna, args.plan)
    if not os.path.isfile(plan_full):
        print("[ЧЕРВЕНО] C2 план — липсва: %s" % args.plan)
        return 2
    with open(plan_full, "rb") as fh:
        plan_text = fh.read().decode("utf-8")
    lots, order = parse_plan(plan_text)
    rep.check(
        "C2 план·таблица",
        len(order) >= 7,
        "лотове в §2: %s" % ", ".join(order),
    )

    # --- C3: attribution and the morning section -------------------------------
    head = "\n".join(report_text.split("\n")[:12])
    rep.check(
        "C3 атрибуция·ToS §1.G",
        "Wikimapia.org" in head and "http://wikimapia.org" in head,
        "заглавният ред носи „Wikimapia.org“ и връзката",
    )
    rep.check(
        "C3 сутринта",
        MORNING_HEADING in report_text,
        "раздел „%s“" % MORNING_HEADING,
    )

    # --- C4: nothing forbidden travels in a public tracked file ----------------
    rep.check(
        "C4 публичност·код на извора",
        FORBIDDEN_CODE not in report_text,
        "нула срещания на забранения низ",
    )
    coord_hits = []
    for pattern in COORD_PATTERNS:
        coord_hits.extend(pattern.findall(report_text))
    rep.check("C4 публичност·координати", not coord_hits, "нула координатни числа")
    # The bare English word may legitimately appear inside a verbatim commit message
    # ("measure: derive place coordinates read-only"); a GeoJSON KEY may not.
    geo_keys = [k for k in GEOJSON_KEYS if k in report_text]
    rep.check(
        "C4 публичност·геометрия",
        not geo_keys,
        "нула геометрични ключове (намерени: %s)" % (", ".join(geo_keys) or "няма"),
    )

    # --- C5..C9: the lot blocks -------------------------------------------------
    blocks = parse_report(report_text)
    by_code = {}
    for block in blocks:
        lot = block["код"]
        if lot in by_code:
            rep.check("C5 блокове·%s" % lot, False, "два блока за един лот")
        by_code[lot] = block
    rep.check(
        "C5 блокове·брой",
        len(blocks) == len(order),
        "намерени %d блока за %d лота от плана" % (len(blocks), len(order)),
    )

    for lot in order:
        spec = lots[lot]
        block = by_code.get(lot)
        if block is None:
            rep.check("C5 лот·%s" % lot, False, "няма блок в доклада")
            continue

        status = block["статус"]
        rep.check(
            "C6 %s·статус" % lot,
            status in STATUSES,
            "статус „%s“" % status,
        )
        rep.check(
            "C6 %s·неразпознати редове" % lot,
            not block["unknown"],
            "нула неразпознати реда",
        )
        rep.check(
            "C6 %s·съобщение дословно" % lot,
            block["съобщение"] == spec["message"],
            "срещу плана: „%s“" % spec["message"],
        )
        if status in (STATUS_RED, STATUS_NOT_RUN):
            rep.check(
                "C6 %s·причина" % lot,
                bool(block["причина"]),
                "причината е записана",
            )

        # --- write-set: every plan path present, every sha recomputed ---
        declared = dict(block["files"])
        missing = [p for p in spec["paths"] if p not in declared]
        rep.check(
            "C7 %s·write-set пълен" % lot,
            not missing,
            "липсват пътища: %s" % (", ".join(missing) if missing else "няма"),
        )
        extra = [p for p in declared if p not in spec["paths"]]
        unjustified = [p for p in extra if p not in plan_text]
        rep.check(
            "C7 %s·write-set без чужди пътища" % lot,
            not unjustified,
            "необоснован излишък: %s" % (", ".join(unjustified) if unjustified else "няма"),
        )

        root = roots.get(spec["repo"], fire_varna)
        for path, sha in block["files"]:
            full = os.path.join(root, path)
            label = "C8 %s·%s" % (lot, path)
            if sha == SELF_SHA_MARKER:
                rep.check(
                    label,
                    lot == "Н5" and path == "docs/audits/ДОКЛАД_07.09_нощна_смяна.md",
                    "самореферентният маркер е допустим само за самия доклад",
                )
                continue
            if sha == NO_FILE_MARKER:
                rep.check(
                    label,
                    status == STATUS_NOT_RUN and not os.path.exists(full),
                    "лотът не е изпълнен и файлът наистина липсва",
                )
                continue
            if not SHA256_RE.match(sha):
                rep.check(label, False, "не е sha256 и не е признат маркер: „%s“" % sha)
                continue
            if not os.path.isfile(full):
                rep.check(label, False, "пинат sha, а файлът липсва")
                continue
            measured = sha256_of_file(full)
            rep.check(
                label,
                measured == sha,
                "пинато %s, измерено %s" % (sha, measured),
            )

        # --- gates and negative fixtures ---
        gate_exits = [as_int(g["exit"]) for g in block["gates"]]
        neg_exits = [as_int(n["exit"]) for n in block["negatives"]]

        # An exit code nobody can re-run is not evidence: every recorded line must
        # carry a name AND the command it was measured with.
        recorded = block["gates"] + block["negatives"] + block["probes"]
        without_command = [
            entry
            for entry in recorded
            if len(entry["rest"]) < 2 or not all(part.strip() for part in entry["rest"][:2])
        ]
        rep.check(
            "C9 %s·всеки изход с име и команда" % lot,
            not without_command,
            "редове без команда: %d от %d" % (len(without_command), len(recorded)),
        )

        if status == STATUS_NOT_RUN:
            rep.check(
                "C9 %s·без гейт" % lot,
                not block["gates"] and not block["negatives"],
                "неизпълнен лот не отчита гейт и фикстури",
            )
            rep.check(
                "C9 %s·без комит" % lot,
                block["комит"] == NO_COMMIT_MARKER,
                "комит: %s" % block["комит"],
            )
            continue

        rep.check(
            "C9 %s·гейт присъства" % lot,
            bool(gate_exits) and None not in gate_exits,
            "изходни кодове: %s" % ", ".join(str(e) for e in gate_exits),
        )
        rep.check(
            "C9 %s·падаща фикстура" % lot,
            bool(neg_exits) and None not in neg_exits and all(e != 0 for e in neg_exits),
            "изходни кодове: %s" % ", ".join(str(e) for e in neg_exits),
        )
        if status == STATUS_GREEN:
            rep.check(
                "C9 %s·зелен гейт" % lot,
                all(e == 0 for e in gate_exits if e is not None),
                "всеки гейт е 0",
            )
        elif status == STATUS_RED:
            rep.check(
                "C9 %s·червен гейт" % lot,
                any(e != 0 for e in gate_exits if e is not None),
                "поне един гейт е ≠ 0",
            )

        # --- commit: author and verbatim message re-read from git ---
        commit = block["комит"]
        if status == STATUS_RED:
            rep.check(
                "C10 %s·без комит" % lot,
                commit == NO_COMMIT_MARKER,
                "паднал гейт спира лота без комит",
            )
            continue
        if commit == PENDING_COMMIT_MARKER:
            code, out, _ = run(
                ["git", "log", "-1", "--format=%H", "--"] + [p for p, _s in block["files"]],
                cwd=root,
            )
            resolved = out.strip()
            if not resolved:
                rep.check(
                    "C10 %s·комит" % lot,
                    lot == "Н5",
                    "докладът още не е комитнат — допустимо само за Н5",
                )
                continue
            commit = resolved
        if not COMMIT_RE.match(commit or ""):
            rep.check("C10 %s·комит" % lot, False, "не е sha на комит: „%s“" % commit)
            continue
        code, out, err = run(
            ["git", "log", "-1", "--format=%H%x1f%an <%ae>%x1f%B", commit], cwd=root
        )
        if code != 0:
            rep.check("C10 %s·комит" % lot, False, "git не познава комита: %s" % err.strip())
            continue
        parts = out.split("\x1f")
        real_author = parts[1]
        real_message = parts[2].strip("\n")
        rep.check(
            "C10 %s·автор" % lot,
            block["автор"] == real_author,
            "в доклада „%s“, в git „%s“" % (block["автор"], real_author),
        )
        rep.check(
            "C10 %s·съобщение в git" % lot,
            real_message == spec["message"],
            "git носи „%s“" % real_message,
        )
        code, out, _ = run(
            [
                "git",
                "-c",
                "core.quotepath=false",
                "show",
                "--name-only",
                "--format=",
                commit,
            ],
            cwd=root,
        )
        touched = sorted(p for p in out.split("\n") if p.strip())
        rep.check(
            "C10 %s·комитът е write-set-ът" % lot,
            touched == sorted(p for p, _s in block["files"]),
            "комитнати: %s" % ", ".join(touched),
        )

    # --- C11: the report is tied to the SIGNED body of the plan ----------------
    # The plan records the sha256 of the body Petar signed; a report that does not
    # quote it cannot be attributed to a signed plan.
    signed_sha = None
    for line in plan_text.split("\n"):
        if "Подписаното тяло" in line:
            found = re.findall(r"[0-9a-f]{64}", line)
            if found:
                signed_sha = found[0]
            break
    rep.check(
        "C11 подпис·тялото на плана",
        bool(signed_sha) and signed_sha in report_text,
        "подписано тяло: %s" % (signed_sha or "планът не обявява sha"),
    )

    print("")
    if rep.failed:
        print(
            "ГЕЙТ Н5: ЧЕРВЕН — паднали проверки: %d от %d" % (rep.failed, rep.checks)
        )
        return 1
    print("ГЕЙТ Н5: ЗЕЛЕН — %d проверки" % rep.checks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
