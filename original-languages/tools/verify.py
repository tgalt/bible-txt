#!/usr/bin/env python3
"""Check the built corpora and print the report quoted in the READMEs.

Verifies structure (references parse, nothing empty), counts them, measures how
far each corpus agrees with the KJV's versification, and checks that the
Strong's numbers used by the texts actually resolve in the lexicons.

Usage: verify.py <repo-root>
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import books

REF = re.compile(r"^(.+?) (\d+):(\d+) (.*)$")

GREEK_TEXTS = ["sblgnt", "nestle1904", "tr-scrivener", "byzantine", "sr", "kjtr"]


def load_text(path):
    """Read a verse-per-line corpus into ``{reference: text}``."""
    out = {}
    for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        m = REF.match(line)
        if not m:
            raise SystemExit(f"{path}:{lineno}: unparseable line: {line[:60]!r}")
        book, chapter, verse, text = m.groups()
        if book not in books.ORDER:
            raise SystemExit(f"{path}:{lineno}: unknown book {book!r}")
        if not text.strip():
            raise SystemExit(f"{path}:{lineno}: empty verse")
        out[f"{book} {chapter}:{verse}"] = text
    return out


def load_words(path):
    """Read a word table, returning its rows as dicts."""
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        return [dict(zip(header, line.rstrip("\n").split("\t"))) for line in fh]


def fold(s):
    """Bare letters only: no accents, breathings, punctuation or case."""
    s = s.replace("ʼ", "").replace("’", "").replace("'", "")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip().lower().replace("ς", "σ")


def main(root):
    ol = os.path.join(root, "original-languages")
    kjv = load_text(os.path.join(root, "kjv", "kjv.txt"))
    kjv_ot = {r for r in kjv if r.rsplit(" ", 1)[0] in books.OT_NAMES}
    kjv_nt = {r for r in kjv if r.rsplit(" ", 1)[0] in books.NT_NAMES}

    print("== structure and size ==")
    corpora = {}
    wlc = load_text(os.path.join(ol, "hebrew", "wlc.txt"))
    corpora["wlc"] = wlc
    print(f"  {'wlc.txt':22s} {len(wlc):>6,} verses  "
          f"{len(load_words(os.path.join(ol, 'hebrew', 'wlc-words.tsv'))):>7,} words")
    for stem in GREEK_TEXTS:
        text = load_text(os.path.join(ol, "greek", stem + ".txt"))
        corpora[stem] = text
        words = load_words(os.path.join(ol, "greek", stem + "-words.tsv"))
        print(f"  {stem + '.txt':22s} {len(text):>6,} verses  {len(words):>7,} words")

    print("\n== versification against kjv/kjv.txt ==")
    print(f"  KJV Old Testament          {len(kjv_ot):>6,} verses")
    shared = len(set(wlc) & kjv_ot)
    print(f"  WLC                        {len(wlc):>6,} verses  "
          f"({shared:,} references shared, {len(set(wlc) - kjv_ot):,} only in WLC, "
          f"{len(kjv_ot - set(wlc)):,} only in KJV)")
    print(f"  KJV New Testament          {len(kjv_nt):>6,} verses")
    for stem in GREEK_TEXTS:
        text = corpora[stem]
        extra, missing = set(text) - kjv_nt, kjv_nt - set(text)
        print(f"  {stem:26s} {len(text):>6,} verses  "
              f"({len(set(text) & kjv_nt):,} shared, {len(extra):,} extra, "
              f"{len(missing):,} absent)")

    print("\n== Textus Receptus conversion check (beta code -> Unicode) ==")
    tr, kjtr = corpora["tr-scrivener"], corpora["kjtr"]
    common = sorted(set(tr) & set(kjtr))
    same = sum(1 for r in common if fold(tr[r]) == fold(kjtr[r]))
    total = agree = 0
    for r in common:
        a, b = fold(tr[r]).split(), fold(kjtr[r]).split()
        total += max(len(a), len(b))
        agree += sum(1 for x, y in zip(a, b) if x == y)
    print(f"  Scrivener TR vs CNTR KJTR, accents and punctuation ignored:")
    print(f"    {same:,}/{len(common):,} verses identical "
          f"({same / len(common) * 100:.1f}%)")
    print(f"    {agree:,}/{total:,} words agree ({agree / total * 100:.1f}%)")
    greek_block = re.compile(r"^[Ͱ-Ͽἀ-῿]+$")
    bad = {w for r in common for w in fold(tr[r]).split()
           if not greek_block.match(w)}
    print(f"    {len(bad)} converted word forms contain a non-Greek character")

    print("\n== Strong's coverage ==")
    lex = {}
    for name, path in [("hebrew", "strongs-hebrew.tsv"), ("greek", "strongs-greek.tsv")]:
        rows = load_words(os.path.join(ol, "lexicons", path))
        lex[name] = {r["strongs"] for r in rows}
        print(f"  {path:22s} {len(rows):>7,} entries")
    for path in ("bdb.tsv", "dodson-greek.tsv"):
        rows = load_words(os.path.join(ol, "lexicons", path))
        print(f"  {path:22s} {len(rows):>7,} entries")

    def coverage(label, codes, table):
        used = {c for c in codes if c}
        # OSHB augments Strong's with a homonym letter (H1254a); the lexicon is
        # keyed to the base number.
        hit = {c for c in used if c in table or re.sub(r"[a-z]$", "", c) in table}
        pct = len(hit) / len(used) * 100
        # Don't round a shortfall up to a clean 100%.
        shown = f"{pct:.1f}" if hit == used or pct < 99.9 else f"{pct:.2f}"
        print(f"  {label:34s} {len(hit):>5,}/{len(used):,} distinct numbers resolve "
              f"({shown}%)")

    hebrew_codes = set()
    for row in load_words(os.path.join(ol, "hebrew", "wlc-words.tsv")):
        hebrew_codes.update(row["strongs"].split("/"))
    coverage("wlc-words.tsv -> Strong's Hebrew", hebrew_codes, lex["hebrew"])
    for stem in ("tr-scrivener", "byzantine", "nestle1904"):
        rows = load_words(os.path.join(ol, "greek", stem + "-words.tsv"))
        coverage(f"{stem}-words.tsv -> Strong's Greek",
                 {r["strongs"] for r in rows}, lex["greek"])
    inter = load_words(os.path.join(ol, "interlinear", "nt-interlinear.tsv"))
    print(f"\n  {'nt-interlinear.tsv':22s} {len(inter):>7,} words, "
          f"{len({r['reference'] for r in inter}):,} verses")
    coverage("nt-interlinear.tsv -> Strong's Greek",
             {r["strongs"] for r in inter}, lex["greek"])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
