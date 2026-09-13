#!/usr/bin/env python3
"""Build the Greek New Testament corpora from six open editions.

Each edition yields a reading text in the repo's line format and, where the
source is tagged, a word-level TSV carrying Strong's numbers and morphology.

Usage: build_greek.py <path-to-src-checkouts> <output-dir>
"""
import csv
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import books
from betacode import convert

# Book abbreviations used by the ByzTxt file names.
BYZ_CODES = {
    "MAT": "Matthew", "MAR": "Mark", "LUK": "Luke", "JOH": "John",
    "ACT": "Acts", "ROM": "Romans", "1CO": "1 Corinthians",
    "2CO": "2 Corinthians", "GAL": "Galatians", "EPH": "Ephesians",
    "PHP": "Philippians", "COL": "Colossians", "1TH": "1 Thessalonians",
    "2TH": "2 Thessalonians", "1TI": "1 Timothy", "2TI": "2 Timothy",
    "TIT": "Titus", "PHM": "Philemon", "HEB": "Hebrews", "JAM": "James",
    "1PE": "1 Peter", "2PE": "2 Peter", "1JO": "1 John", "2JO": "2 John",
    "3JO": "3 John", "JUD": "Jude", "REV": "Revelation",
    # The Textus Receptus checkout spells several books differently.
    "MT": "Matthew", "MR": "Mark", "LU": "Luke", "AC": "Acts", "RO": "Romans",
    "GA": "Galatians", "JAS": "James", "JUDE": "Jude", "RE": "Revelation",
}

# Files that are not books of the canon: a separate copy of the pericope
# adulterae and an alternative text of Acts.
BYZ_SKIP = {"PA", "ACT24"}

SBLGNT_FILES = {
    "Matt": "Matthew", "Mark": "Mark", "Luke": "Luke", "John": "John",
    "Acts": "Acts", "Rom": "Romans", "1Cor": "1 Corinthians",
    "2Cor": "2 Corinthians", "Gal": "Galatians", "Eph": "Ephesians",
    "Phil": "Philippians", "Col": "Colossians", "1Thess": "1 Thessalonians",
    "2Thess": "2 Thessalonians", "1Tim": "1 Timothy", "2Tim": "2 Timothy",
    "Titus": "Titus", "Phlm": "Philemon", "Heb": "Hebrews", "Jas": "James",
    "1Pet": "1 Peter", "2Pet": "2 Peter", "1John": "1 John",
    "2John": "2 John", "3John": "3 John", "Jude": "Jude", "Rev": "Revelation",
}

# Editorial sigla the SBLGNT uses to point into its apparatus. They mark where
# a variant is discussed; they are not part of the text.
SBL_SIGLA = "⸀⸁⸂⸃⸄⸅⸆⸇⟦⟧"


def write_words(path, header, rows):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\t".join(header) + "\n")
        for row in rows:
            fh.write("\t".join(str(c) for c in row) + "\n")
    return len(rows)


def sort_words(rows):
    def key(row):
        ref = row[0]
        book, cv = ref.rsplit(" ", 1)
        chapter, verse = cv.split(":")
        return (books.ORDER[book], int(chapter), int(verse), row[1])
    return sorted(rows, key=key)


def build_sblgnt(src, out):
    """SBLGNT reading text plus the MorphGNT parse of the same text."""
    verses = []
    for code, name in SBLGNT_FILES.items():
        path = os.path.join(src, "SBLGNT", "data", "sblgnt", "text", code + ".txt")
        for line in open(path, encoding="utf-8-sig"):
            if "\t" not in line:
                continue  # book title line
            ref, text = line.split("\t", 1)
            m = re.match(r"^\S+\s+(\d+):(\d+)$", ref.strip())
            if not m:
                continue
            text = text.strip().translate({ord(c): None for c in SBL_SIGLA})
            verses.append((name, int(m.group(1)), int(m.group(2)),
                           re.sub(r"\s+", " ", text).strip()))
    n = books.write_verses(os.path.join(out, "sblgnt.txt"), verses)

    rows = []
    for path in sorted(glob.glob(os.path.join(src, "sblgnt", "*-morphgnt.txt"))):
        idx = int(os.path.basename(path).split("-")[0]) - 61
        name = books.NT_NAMES[idx]
        counter = {}
        for line in open(path, encoding="utf-8"):
            parts = line.split()
            if len(parts) != 7:
                continue
            bcv, pos, parse, text, word, norm, lemma = parts
            chapter, verse = int(bcv[2:4]), int(bcv[4:6])
            ref = f"{name} {chapter}:{verse}"
            counter[ref] = counter.get(ref, 0) + 1
            rows.append((ref, counter[ref], word, norm, lemma, pos, parse))
    w = write_words(os.path.join(out, "sblgnt-words.tsv"),
                    ["reference", "n", "word", "normalized", "lemma",
                     "part_of_speech", "parse"], sort_words(rows))
    return n, w


def build_nestle1904(src, out):
    """Nestle 1904 with morphology, Strong's numbers and lemmas."""
    path = os.path.join(src, "Nestle1904", "morph", "Nestle1904.csv")
    label_to_name = dict(SBLGNT_FILES)
    verses, rows = {}, []
    counter = {}
    with open(path, encoding="utf-8-sig") as fh:
        reader = csv.reader(fh, delimiter="\t")
        next(reader)
        for row in reader:
            if len(row) < 7 or not row[0].strip():
                continue
            bcv, text, func_morph, _form, strongs, lemma, norm = row[:7]
            label, cv = bcv.rsplit(" ", 1)
            name = label_to_name[label]
            chapter, verse = (int(x) for x in cv.split(":"))
            ref = f"{name} {chapter}:{verse}"
            verses.setdefault((name, chapter, verse), []).append(text.strip())
            counter[ref] = counter.get(ref, 0) + 1
            # Verbs carry an Online Bible tense/voice/mood code appended to the
            # Strong's number as "1080&5656"; keep the two apart.
            number, _, tvm = strongs.strip().partition("&")
            rows.append((ref, counter[ref], text.strip(), norm.strip(),
                         lemma.strip(),
                         f"G{int(number):04d}" if number else "",
                         func_morph.strip(), tvm))
    n = books.write_verses(
        os.path.join(out, "nestle1904.txt"),
        [(b, c, v, " ".join(w)) for (b, c, v), w in verses.items()])
    w = write_words(os.path.join(out, "nestle1904-words.tsv"),
                    ["reference", "n", "word", "normalized", "lemma",
                     "strongs", "morphology", "tvm_code"], sort_words(rows))
    return n, w


# ``word 1234 {MORPH}``, or for verbs ``word 1234 5656 {MORPH}`` where the
# second number is an Online Bible tense/voice/mood code. The word itself is
# never numeric, which keeps the Strong's number from being read as the word.
TAGGED_WORD = re.compile(r"(?<!\S)(\d*[^\W\d_]\S*)\s+(\d+)((?:\s+\d+)*)\s+\{([^}]*)\}")


def _parse_tagged(body, scheme=None):
    """Split ``word 1234 [5656] {MORPH}`` groups out of a Robinson-style line."""
    out = []
    for word, strongs, extra, morph in TAGGED_WORD.findall(body):
        if scheme:
            word = convert(word, scheme)
        codes = extra.split()
        # A leading 0 is a placeholder: the real Strong's number follows it
        # (five words do this, e.g. "simewn 0 4826").
        if int(strongs) == 0 and codes:
            strongs, codes = codes[0], codes[1:]
        out.append((word, f"G{int(strongs):04d}", morph, " ".join(codes)))
    return out


def _render_alternative(body):
    """Greek for one side of a variant, tagged or not.

    Most alternatives carry their own Strong's number and parse; some are bare
    words that share the tag printed after the group (``| nazaret | nazareq |
    3478 {N-PRI}``), so fall back to converting the tokens directly.
    """
    words = [w for w, _, _, _ in _parse_tagged(body, "UTR")]
    if not words:
        words = [convert(t, "UTR") for t in body.split()
                 if not t.isdigit() and not t.startswith("{")]
    return " ".join(words)


def _resolve_variants(body):
    """Pick the Textus Receptus reading out of ``| A | B |`` variant groups.

    Robinson marks a variant as two alternatives fenced by three standalone
    pipes. The convention is not documented upstream, but it is decidable from
    the data: taking the second alternative reproduces the CNTR KJTR reading in
    62% of the 246 affected verses against 21% for the first, so the second is
    the Textus Receptus reading and the first is the Byzantine one.

    Returns the resolved text and the ``(byzantine, receptus)`` pairs dropped.
    """
    tokens = body.split()
    out, variants, i = [], [], 0
    while i < len(tokens):
        if tokens[i] != "|":
            out.append(tokens[i])
            i += 1
            continue
        alternatives, seen, i = [[], []], 0, i + 1
        while i < len(tokens) and seen < 2:
            if tokens[i] == "|":
                seen += 1
            else:
                alternatives[seen].append(tokens[i])
            i += 1
        out.extend(alternatives[1])
        variants.append((" ".join(alternatives[0]), " ".join(alternatives[1])))
    return " ".join(out), variants


def build_textus_receptus(src, out):
    """Scrivener 1894 Textus Receptus, parsed, with Strong's numbers."""
    verses, rows, variant_rows = [], [], []
    for path in sorted(glob.glob(os.path.join(
            src, "greektext-textus-receptus", "parsed", "*.UTR"))):
        code = os.path.basename(path).split(".")[0].upper()
        if code in BYZ_SKIP:
            continue
        name = BYZ_CODES[code]
        current, buf = None, []

        def flush():
            if current is None:
                return
            chapter, verse = current
            body, variants = _resolve_variants(" ".join(buf))
            for byz, tr in variants:
                variant_rows.append((f"{name} {chapter}:{verse}",
                                     _render_alternative(byz),
                                     _render_alternative(tr)))
            words = _parse_tagged(body, "UTR")
            verses.append((name, chapter, verse,
                           " ".join(w for w, _, _, _ in words)))
            ref = f"{name} {chapter}:{verse}"
            for i, (word, strongs, morph, tvm) in enumerate(words, 1):
                rows.append((ref, i, word, strongs, morph, tvm))

        for line in open(path, encoding="utf-8", newline=""):
            line = line.replace("\r", "")
            m = re.match(r"^\s*(\d+):(\d+)\s+(.*)$", line)
            if m:
                flush()
                current = (int(m.group(1)), int(m.group(2)))
                buf = [m.group(3)]
            elif current is not None:
                buf.append(line.strip())
        flush()

    n = books.write_verses(os.path.join(out, "tr-scrivener.txt"), verses)
    w = write_words(os.path.join(out, "tr-scrivener-words.tsv"),
                    ["reference", "n", "word", "strongs", "morphology",
                     "tvm_code"], sort_words(rows))
    write_words(os.path.join(out, "tr-variants.tsv"),
                ["reference", "byzantine_reading", "receptus_reading"],
                sorted(variant_rows,
                       key=lambda r: (books.ORDER[r[0].rsplit(" ", 1)[0]],
                                      int(r[0].rsplit(" ", 1)[1].split(":")[0]),
                                      int(r[0].rsplit(" ", 1)[1].split(":")[1]))))
    return n, w


def build_byzantine(src, out):
    """Robinson-Pierpont 2018: accented reading text plus a tagged word list."""
    verses = []
    base = os.path.join(src, "byzantine-majority-text", "csv-unicode")
    for path in sorted(glob.glob(os.path.join(base, "ccat", "no-variants", "*.csv"))):
        code = os.path.basename(path).split(".")[0].upper()
        if code in BYZ_SKIP:
            continue
        name = BYZ_CODES[code]
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                verses.append((name, int(row["chapter"]), int(row["verse"]),
                               re.sub(r"\s+", " ", row["text"]).strip()))
    n = books.write_verses(os.path.join(out, "byzantine.txt"), verses)

    rows = []
    for path in sorted(glob.glob(os.path.join(
            base, "strongs", "with-parsing", "*.csv"))):
        code = os.path.basename(path).split(".")[0].upper()
        if code in BYZ_SKIP:
            continue
        name = BYZ_CODES[code]
        with open(path, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                ref = f"{name} {int(row['chapter'])}:{int(row['verse'])}"
                for i, (word, strongs, morph, tvm) in enumerate(
                        _parse_tagged(row["text"]), 1):
                    rows.append((ref, i, word, strongs, morph, tvm))
    w = write_words(os.path.join(out, "byzantine-words.tsv"),
                    ["reference", "n", "word", "strongs", "morphology",
                     "tvm_code"], sort_words(rows))
    return n, w


def build_cntr(src, out, repo, stem):
    """CNTR editions (SR, KJTR): numeric refs, Unicode text, tagged TSV."""
    verses = []
    for line in open(os.path.join(src, repo, repo + ".txt"), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        ref, text = line.split(" ", 1)
        name = books.NT_BY_NUMBER[int(ref[:2])]
        verses.append((name, int(ref[2:5]), int(ref[5:8]), text.strip()))
    n = books.write_verses(os.path.join(out, stem + ".txt"), verses)

    rows, counter = [], {}
    with open(os.path.join(src, repo, repo + ".tsv"), encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            ref_num = row["Verse"]
            name = books.NT_BY_NUMBER[int(ref_num[:2])]
            ref = f"{name} {int(ref_num[2:5])}:{int(ref_num[5:8])}"
            counter[ref] = counter.get(ref, 0) + 1
            rows.append((ref, counter[ref], row["Modern"], row["Lemma"],
                         row["ESN"], row["Role"], row["Morphology"]))
    w = write_words(os.path.join(out, stem + "-words.tsv"),
                    ["reference", "n", "word", "lemma", "extended_strongs",
                     "role", "morphology"], sort_words(rows))
    return n, w


def main(src, out):
    os.makedirs(out, exist_ok=True)
    for label, result in [
            ("SBLGNT", build_sblgnt(src, out)),
            ("Nestle 1904", build_nestle1904(src, out)),
            ("Scrivener TR", build_textus_receptus(src, out)),
            ("Byzantine RP2018", build_byzantine(src, out)),
            ("CNTR SR", build_cntr(src, out, "SR", "sr")),
            ("CNTR KJTR", build_cntr(src, out, "KJTR", "kjtr")),
    ]:
        print(f"{label:20s} {result[0]:>6,} verses  {result[1]:>7,} words")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
