#!/usr/bin/env python3
"""Build a word-level Greek-English interlinear for the New Testament.

Source is the Majority Standard Bible translation table, which pairs every
Greek word of the Byzantine/Majority text with its transliteration, parsing,
Strong's number and English rendering. The MSB text is public domain.

Usage: build_interlinear.py <path-to-msb-tables.tsv> <output-dir>
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import books

BOOK_LABELS = {name.replace(" ", ""): name for name in books.NT_NAMES}


def normalise_ref(raw):
    """``Matthew 1:1`` / ``1 Corinthians 1:1`` -> canonical repo reference."""
    m = re.match(r"^\s*(.+?)\s+(\d+):(\d+)\s*$", raw)
    if not m:
        return None
    label = BOOK_LABELS.get(m.group(1).replace(" ", ""))
    return f"{label} {int(m.group(2))}:{int(m.group(3))}" if label else None


def main(table, out_dir):
    rows, ref = [], None
    with open(table, encoding="utf-8-sig") as fh:
        reader = csv.reader(fh, delimiter="\t")
        next(reader)
        for row in reader:
            if len(row) < 19 or row[4].strip() != "Greek":
                continue
            # The reference is stamped only on the first word of each verse.
            new_ref = normalise_ref(row[12]) if row[12].strip() else None
            if new_ref:
                ref = new_ref
            if ref is None:
                continue
            greek = row[6].strip()
            if not greek:
                continue
            strongs = row[11].strip()
            # The table is laid out in English reading order; "Greek Sort"
            # restores the order the words stand in in the Greek.
            order = int(row[1]) if row[1].strip().isdigit() else 0
            rows.append([
                ref, order, greek, row[7].strip(), row[8].strip(),
                f"G{int(strongs):04d}" if strongs.isdigit() else "",
                " ".join(row[18].split()),
            ])

    # Put each verse into Greek word order, then number the words 1..n.
    by_verse = {}
    for r in rows:
        by_verse.setdefault(r[0], []).append(r)
    rows = []
    for ref in by_verse:
        for i, r in enumerate(sorted(by_verse[ref], key=lambda x: x[1]), 1):
            r[1] = i
            rows.append(r)
    rows.sort(key=lambda r: (books.ORDER[r[0].rsplit(" ", 1)[0]],
                             int(r[0].rsplit(" ", 1)[1].split(":")[0]),
                             int(r[0].rsplit(" ", 1)[1].split(":")[1]), r[1]))

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "nt-interlinear.tsv")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("reference\tn\tgreek\ttransliteration\tparsing\tstrongs\tenglish\n")
        for r in rows:
            fh.write("\t".join(str(c) for c in r) + "\n")
    verses = len({r[0] for r in rows})
    print(f"nt-interlinear.tsv  {len(rows):,} words across {verses:,} verses")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
