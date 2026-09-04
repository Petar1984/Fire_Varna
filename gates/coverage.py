#!/usr/bin/env python3
"""Coverage delta per (file, field) between a base delivery and a candidate one.

Why this exists: лот 1в-В moved 103 hotels from a named resort to a bare
"район X" and nobody noticed until Petar opened the map. The tests could not
notice either — they assert the shape of a row, never the *coverage* of the
delivery as a whole. This gate compares two deliveries row by row and refuses
the candidate unless every lost or changed row is listed by name in a signed
allow-file.

The join is `(file, name)`; the ordinal (the position in the array) is only a
tie-breaker inside a duplicated name (РОЯЛ ×2 in the hotels delivery). A row
that moved keeps its comparison — the first round of this gate joined by
ordinal, so a full reorder made every comparison meaningless while the gate
still reported zero.

Classes per (file, field), over the joined pairs:
  lost       a named value in the base became null / "район X" in the candidate
  changed    a named value became a *different* named value
  gained     a null in the base became a named value
  unchanged  the same named value on both sides
  reordered  the pair exists but the candidate carries it at another ordinal
`before` and `after` are counted over ALL rows of each side, not over the
pairs: they are the coverage of the delivery itself, and they see a deletion
that a join could hide.

Structural classes per file, from the join itself:
  row_missing  a name the base carried and the candidate no longer carries
  row_added    a name the candidate carries and the base did not

The allow-file is the only way any of this becomes green:

    {"signed_by": "Петър", "date": "2026-09-05",
     "rows": [{"file","name","field","from","to","why"}]}

A structural row is listed with `field` = "row_missing" | "row_added" |
"reordered" and without `from`/`to`. `signed_by`/`date` are read and judged: a
missing key is red, a signature that is not Petar's ("pending — Петър") is
yellow, and yellow blocks the push exactly like red (Амандамент №1, т. 8).

Exit codes:
  0  green: nothing lost/changed/missing/added/reordered, or every such row is
     covered by an allow-file signed by Petar
  2  red: an uncovered row, a (file, field) whose `after` is below `before`,
     or an allow-file without `signed_by`/`date`
  3  the allow-file lists a row that did not move ("listed but unchanged")
  4  usage / input error
  5  yellow: an allow-file that is not signed by Petar — blocks like red
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

FILES = ("places", "hotels")
ARRAY_KEY = {"places": "places", "hotels": "hotels"}

# The compat label: `zone` is a named zone unless it is the bare district word.
DISTRICT_MARK = "район "

FIELDS = ("zone_named", "quarter", "locality", "district")

# The only signature that grants anything.
SIGNER = "Петър"

EXIT_OK = 0
EXIT_UNCOVERED = 2
EXIT_ALLOW_STALE = 3
EXIT_USAGE = 4
EXIT_ALLOW_UNSIGNED = 5


def read_source(spec: str) -> str:
    """Read a delivery from the worktree or from git: `git:<rev>:<path>`."""
    if spec.startswith("git:"):
        rest = spec[len("git:"):]
        rev, _, path = rest.partition(":")
        if not rev or not path:
            raise ValueError("git spec must be git:<rev>:<path>, got %r" % spec)
        out = subprocess.run(
            ["git", "show", "%s:%s" % (rev, path)],
            capture_output=True,
        )
        if out.returncode != 0:
            raise ValueError(
                "git show %s:%s failed: %s" % (rev, path, out.stderr.decode("utf-8", "replace").strip())
            )
        return out.stdout.decode("utf-8")
    return Path(spec).read_text(encoding="utf-8")


def load_rows(spec: str, file_key: str) -> list:
    data = json.loads(read_source(spec))
    rows = data.get(ARRAY_KEY[file_key])
    if not isinstance(rows, list):
        raise ValueError("%s: no %r array" % (spec, ARRAY_KEY[file_key]))
    return rows


def field_value(row: dict, field: str):
    """The comparable value of a field, or None when the row carries nothing.

    A typed field is compared by its `code` (the closed-list identity), not by
    its printed name. `zone_named` is the compat label and counts only when it
    is a real zone name — "район Приморски" is the honest absence, not a value.
    """
    if field == "zone_named":
        zone = row.get("zone")
        if not isinstance(zone, str) or not zone or zone.startswith(DISTRICT_MARK):
            return None
        return zone
    value = row.get(field)
    if not isinstance(value, dict):
        return None
    code = value.get("code")
    return code if isinstance(code, str) and code else None


def row_src(row: dict) -> str:
    src = row.get("src")
    return src if isinstance(src, str) and src else "?"


def name_positions(rows: list) -> dict:
    """name -> the ordinals that carry it, in array order."""
    index: dict = {}
    for i, row in enumerate(rows):
        index.setdefault(row.get("name"), []).append(i)
    return index


def join_by_name(base_rows: list, cand_rows: list) -> tuple:
    """Pair the two deliveries by name; the ordinal only splits a duplicated name.

    Returns (pairs, missing, added): pairs is a list of (base_ordinal,
    candidate_ordinal); missing/added are the rows one side carries and the
    other does not — the deletion the first round of this gate was blind to.
    """
    base_index = name_positions(base_rows)
    cand_index = name_positions(cand_rows)
    pairs, missing, added = [], [], []
    for name, base_ordinals in base_index.items():
        cand_ordinals = cand_index.get(name, [])
        for k, base_ordinal in enumerate(base_ordinals):
            if k < len(cand_ordinals):
                pairs.append((base_ordinal, cand_ordinals[k]))
            else:
                missing.append({"name": name, "ordinal": base_ordinal})
    for name, cand_ordinals in cand_index.items():
        base_ordinals = base_index.get(name, [])
        for k, cand_ordinal in enumerate(cand_ordinals):
            if k >= len(base_ordinals):
                added.append({"name": name, "ordinal": cand_ordinal})
    pairs.sort()
    missing.sort(key=lambda r: r["ordinal"])
    added.sort(key=lambda r: r["ordinal"])
    return pairs, missing, added


def structural_row(file_key: str, name, field: str, ordinal: int, extra=None) -> dict:
    """A row-level (not field-level) finding, in the allow-file's own shape."""
    row = {
        "file": file_key,
        "name": name,
        "field": field,
        "from": None,
        "to": None,
        "src": "?",
        "ordinal": ordinal,
    }
    if extra:
        row.update(extra)
    return row


def compare(base_rows: list, cand_rows: list, file_key: str) -> dict:
    """Row-by-row comparison of one delivery pair, joined by name."""
    pairs, missing, added = join_by_name(base_rows, cand_rows)

    reordered_rows = [
        structural_row(
            file_key,
            cand_rows[cand_ordinal].get("name"),
            "reordered",
            cand_ordinal,
            {"base_ordinal": base_ordinal, "src": row_src(cand_rows[cand_ordinal])},
        )
        for base_ordinal, cand_ordinal in pairs
        if base_ordinal != cand_ordinal
    ]
    missing_rows = [
        structural_row(file_key, r["name"], "row_missing", r["ordinal"]) for r in missing
    ]
    added_rows = [
        structural_row(file_key, r["name"], "row_added", r["ordinal"]) for r in added
    ]

    fields = {}
    for field in FIELDS:
        counts = {
            # before/after are the coverage of the whole delivery — they do not
            # depend on the join, so a deletion cannot hide inside them.
            "before": sum(1 for row in base_rows if field_value(row, field) is not None),
            "after": sum(1 for row in cand_rows if field_value(row, field) is not None),
            "lost": 0,
            "changed": 0,
            "gained": 0,
            "unchanged": 0,
            "reordered": len(reordered_rows),
        }
        lost_rows, changed_rows = [], []
        for base_ordinal, cand_ordinal in pairs:
            before = field_value(base_rows[base_ordinal], field)
            after = field_value(cand_rows[cand_ordinal], field)
            if before is not None and after is None:
                counts["lost"] += 1
                lost_rows.append(
                    {
                        "file": file_key,
                        "name": cand_rows[cand_ordinal].get("name"),
                        "field": field,
                        "from": before,
                        "to": None,
                        "src": row_src(cand_rows[cand_ordinal]),
                        "ordinal": cand_ordinal,
                    }
                )
            elif before is not None and after is not None and before != after:
                counts["changed"] += 1
                changed_rows.append(
                    {
                        "file": file_key,
                        "name": cand_rows[cand_ordinal].get("name"),
                        "field": field,
                        "from": before,
                        "to": after,
                        "src": row_src(cand_rows[cand_ordinal]),
                        "ordinal": cand_ordinal,
                    }
                )
            elif before is None and after is not None:
                counts["gained"] += 1
            elif before is not None and after is not None:
                counts["unchanged"] += 1
        fields[field] = {"counts": counts, "lost_rows": lost_rows, "changed_rows": changed_rows}

    return {
        "rows_base": len(base_rows),
        "rows_candidate": len(cand_rows),
        "compared": len(pairs),
        "reordered_rows": reordered_rows,
        "missing_rows": missing_rows,
        "added_rows": added_rows,
        "fields": fields,
    }


def load_allow(path: str | None) -> tuple:
    """Read the allow-file and judge its signature. Absent path = no allowance."""
    if not path:
        return [], {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = data.get("rows")
    if not isinstance(rows, list):
        raise ValueError("%s: no `rows` array" % path)
    signed_by = data.get("signed_by")
    date = data.get("date")
    missing_keys = [key for key, value in (("signed_by", signed_by), ("date", date)) if value is None]
    if missing_keys:
        # An allow-file without a signature does not carry a weaker signature —
        # it carries none, and it can never make a lost row green.
        signature = "missing"
    elif isinstance(signed_by, str) and signed_by.strip().startswith(SIGNER):
        signature = "signed"
    else:
        signature = "unsigned"
    meta = {
        "path": path,
        "signed_by": signed_by,
        "date": date,
        "rows": len(rows),
        "signature": signature,
        "missing_keys": missing_keys,
    }
    return rows, meta


def allow_key(row: dict) -> tuple:
    return (row.get("file"), row.get("name"), row.get("field"), row.get("from"), row.get("to"))


SIGNATURE_WORD = {
    "signed": "приет",
    "unsigned": "ЖЪЛТО — не е Петър",
    "missing": "ЧЕРВЕНО — липсва ключ",
}


def render_md(result: dict) -> str:
    out = ["# Покритие по (файл, поле) — гейт `gates/coverage.py`", ""]
    out.append("Base: `%s`" % result["base_spec_text"])
    out.append("")
    out.append("Candidate: `%s`" % result["candidate_spec_text"])
    out.append("")
    allow = result["allow"]
    if allow:
        out.append(
            "Allow-файл: `%s` · подписал: **%s** · дата: %s · редове: %d · подпис: **%s**"
            % (
                allow.get("path"),
                allow.get("signed_by"),
                allow.get("date"),
                allow.get("rows"),
                SIGNATURE_WORD.get(allow.get("signature"), "?"),
            )
        )
    else:
        out.append("Allow-файл: няма")
    out.append("")
    out.append("| файл | редове base | редове candidate | сдвоени | липсващи | нови | пренаредени |")
    out.append("|---|---:|---:|---:|---:|---:|---:|")
    for file_key in FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        out.append(
            "| %s | %d | %d | %d | %d | %d | %d |"
            % (
                file_key,
                block["rows_base"],
                block["rows_candidate"],
                block["compared"],
                len(block["missing_rows"]),
                len(block["added_rows"]),
                len(block["reordered_rows"]),
            )
        )
    out.append("")
    out.append("| файл | поле | before | after | lost | changed | gained | unchanged | reordered |")
    out.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for file_key in FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        for field in FIELDS:
            c = block["fields"][field]["counts"]
            out.append(
                "| %s | %s | %d | %d | %d | %d | %d | %d | %d |"
                % (
                    file_key,
                    field,
                    c["before"],
                    c["after"],
                    c["lost"],
                    c["changed"],
                    c["gained"],
                    c["unchanged"],
                    c["reordered"],
                )
            )
    if result["net_loss"]:
        out.append("")
        out.append("## Нетен спад на покритието (after < before) — ЧЕРВЕНО")
        out.append("")
        for item in result["net_loss"]:
            out.append(
                "- %s · %s: %d → %d (−%d)"
                % (item["file"], item["field"], item["before"], item["after"], item["before"] - item["after"])
            )
    for file_key in FILES:
        block = result["files"].get(file_key)
        if not block:
            continue
        for field in FIELDS:
            for kind, key in (("Загубени", "lost_rows"), ("Сменени", "changed_rows")):
                rows = block["fields"][field][key]
                if not rows:
                    continue
                out.append("")
                out.append("## %s · %s · %s (%d)" % (kind, file_key, field, len(rows)))
                out.append("")
                out.append("| # | име | преди | след | src | покрит от allow |")
                out.append("|---:|---|---|---|---|---|")
                for n, r in enumerate(rows, 1):
                    out.append(
                        "| %d | %s | %s | %s | %s | %s |"
                        % (
                            n,
                            r["name"],
                            r["from"],
                            "—" if r["to"] is None else r["to"],
                            r["src"],
                            "да" if r.get("allowed") else "НЕ",
                        )
                    )
        for kind, key in (
            ("Липсващи редове (изтрити от доставката)", "missing_rows"),
            ("Нови редове", "added_rows"),
            ("Пренаредени редове", "reordered_rows"),
        ):
            rows = block[key]
            if not rows:
                continue
            out.append("")
            out.append("## %s · %s (%d)" % (kind, file_key, len(rows)))
            out.append("")
            out.append("| # | име | ordinal | покрит от allow |")
            out.append("|---:|---|---|---|")
            for n, r in enumerate(rows, 1):
                position = (
                    "%s → %s" % (r["base_ordinal"], r["ordinal"]) if "base_ordinal" in r else str(r["ordinal"])
                )
                out.append("| %d | %s | %s | %s |" % (n, r["name"], position, "да" if r.get("allowed") else "НЕ"))
    if result["allow_stale"]:
        out.append("")
        out.append("## Изброени в allow, но непроменени (грешка 3)")
        out.append("")
        for r in result["allow_stale"]:
            out.append(
                "- %s · %s · %s: %s → %s" % (r.get("file"), r.get("name"), r.get("field"), r.get("from"), r.get("to"))
            )
    out.append("")
    out.append("**Изход: %d** (%s)" % (result["exit_code"], result["verdict"]))
    out.append("")
    return "\n".join(out)


def run(
    places_base: str | None,
    places_candidate: str | None,
    hotels_base: str | None,
    hotels_candidate: str | None,
    allow_path: str | None,
    out_dir: str | None,
) -> dict:
    specs = {
        "places": (places_base, places_candidate),
        "hotels": (hotels_base, hotels_candidate),
    }
    files = {}
    for file_key in FILES:
        base_spec, cand_spec = specs[file_key]
        if not base_spec or not cand_spec:
            continue
        files[file_key] = compare(
            load_rows(base_spec, file_key), load_rows(cand_spec, file_key), file_key
        )
    if not files:
        raise ValueError("nothing to compare: give --places-base/--places-candidate and/or the hotels pair")

    allow_rows, allow_meta = load_allow(allow_path)
    signature = allow_meta.get("signature")
    # A signature that is not Petar's grants nothing: the rows stay uncovered
    # and the verdict says why.
    grants = signature == "signed"
    allowed_keys = {}
    if grants:
        for r in allow_rows:
            allowed_keys.setdefault(allow_key(r), []).append(r)
    used_keys = set()

    uncovered = 0
    uncovered_structural = 0
    for file_key, block in files.items():
        field_groups = [
            block["fields"][field][key] for field in FIELDS for key in ("lost_rows", "changed_rows")
        ]
        structural_groups = [block[key] for key in ("missing_rows", "added_rows", "reordered_rows")]
        for rows, is_structural in [(g, False) for g in field_groups] + [(g, True) for g in structural_groups]:
            for row in rows:
                key = allow_key(row)
                if key in allowed_keys:
                    row["allowed"] = True
                    used_keys.add(key)
                else:
                    row["allowed"] = False
                    if is_structural:
                        uncovered_structural += 1
                    else:
                        uncovered += 1

    # Сол S6: a row listed in the allow-file that did not actually move is a
    # stale signature — it must be removed, not carried forward silently.
    allow_stale = [r for k, rs in allowed_keys.items() if k not in used_keys for r in rs]

    # The backstop that does not depend on the join at all: the delivery may
    # never carry less of a field than the base did.
    net_loss = []
    for file_key in FILES:
        block = files.get(file_key)
        if not block:
            continue
        for field in FIELDS:
            c = block["fields"][field]["counts"]
            if c["after"] < c["before"]:
                net_loss.append(
                    {"file": file_key, "field": field, "before": c["before"], "after": c["after"]}
                )

    reasons = []
    if signature == "missing":
        reasons.append("allow-файл без %s" % "/".join(allow_meta.get("missing_keys") or []))
    if uncovered:
        reasons.append("%d непокрити загубени/сменени реда" % uncovered)
    if uncovered_structural:
        reasons.append("%d непокрити липсващи/нови/пренаредени реда" % uncovered_structural)
    if net_loss:
        reasons.append("нетен спад по %s" % ", ".join("%s.%s" % (i["file"], i["field"]) for i in net_loss))

    if reasons:
        exit_code, verdict = EXIT_UNCOVERED, "; ".join(reasons)
    elif allow_stale:
        exit_code, verdict = EXIT_ALLOW_STALE, "allow-файл с изброен, но непроменен ред"
    elif signature == "unsigned":
        exit_code, verdict = (
            EXIT_ALLOW_UNSIGNED,
            "жълто: allow-файлът е подписан от %r, не от %s" % (allow_meta.get("signed_by"), SIGNER),
        )
    else:
        exit_code, verdict = EXIT_OK, "нула непокрити загубени/сменени реда"

    result = {
        "base_spec_text": "places=%s hotels=%s" % (places_base, hotels_base),
        "candidate_spec_text": "places=%s hotels=%s" % (places_candidate, hotels_candidate),
        "files": files,
        "allow": allow_meta,
        "allow_stale": allow_stale,
        "uncovered": uncovered,
        "uncovered_structural": uncovered_structural,
        "net_loss": net_loss,
        "exit_code": exit_code,
        "verdict": verdict,
    }

    if out_dir:
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "coverage.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        (out / "coverage.md").write_text(render_md(result), encoding="utf-8", newline="\n")
    return result


def use_utf8_console() -> None:
    """The gate must print its full table on a cp1252 console too.

    A UnicodeEncodeError before the first row reads like "the gate did not
    complain" — the crash is silent evidence, which is the opposite of a gate.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str]) -> int:
    use_utf8_console()

    ap = argparse.ArgumentParser(description="coverage delta per (file, field)")
    ap.add_argument("--places-base")
    ap.add_argument("--places-candidate")
    ap.add_argument("--hotels-base")
    ap.add_argument("--hotels-candidate")
    ap.add_argument("--allow", help="gates/allow/<ГГГГ-ММ-ДД>_<тема>.json")
    ap.add_argument("--out", default="gates/out", help="output directory (default gates/out)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    try:
        result = run(
            args.places_base,
            args.places_candidate,
            args.hotels_base,
            args.hotels_candidate,
            args.allow,
            args.out,
        )
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        sys.stderr.write("coverage: %s\n" % exc)
        return EXIT_USAGE

    if not args.quiet:
        for file_key in FILES:
            block = result["files"].get(file_key)
            if not block:
                continue
            sys.stdout.write(
                "%-7s rows base=%-5d candidate=%-5d paired=%-5d missing=%-4d added=%-4d reordered=%d\n"
                % (
                    file_key,
                    block["rows_base"],
                    block["rows_candidate"],
                    block["compared"],
                    len(block["missing_rows"]),
                    len(block["added_rows"]),
                    len(block["reordered_rows"]),
                )
            )
            for field in FIELDS:
                c = block["fields"][field]["counts"]
                sys.stdout.write(
                    "%-7s %-10s before=%-4d after=%-4d lost=%-4d changed=%-4d gained=%-4d reordered=%d\n"
                    % (file_key, field, c["before"], c["after"], c["lost"], c["changed"], c["gained"], c["reordered"])
                )
        allow = result["allow"]
        if allow:
            sys.stdout.write(
                "allow=%s signed_by=%r date=%r → %s\n"
                % (allow.get("path"), allow.get("signed_by"), allow.get("date"), allow.get("signature"))
            )
        sys.stdout.write("uncovered=%d exit=%d (%s)\n" % (result["uncovered"], result["exit_code"], result["verdict"]))
    return result["exit_code"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
