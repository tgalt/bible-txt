#!/usr/bin/env python3
"""Build the Hebrew Old Testament corpus from the Open Scriptures Hebrew Bible.

Reads the OSHB OSIS XML (a morphologically tagged Westminster Leningrad Codex)
and writes two files:

  hebrew/wlc.txt        pointed Hebrew, one verse per line, repo line format
  hebrew/wlc-words.tsv  one row per word: reference, position, segmented form,
                        Strong's numbers, OSHB lemma, morphology code

Usage: build_hebrew.py <path-to-morphhb-checkout> <output-dir>
"""
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import books

OSIS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"

# Punctuation that attaches to the preceding word rather than standing alone.
# The paseq (׀) is deliberately absent: it separates words and is conventionally
# set off by spaces, unlike the maqqef, which hyphenates them into one unit.
JOINING_SEGS = {"x-maqqef", "x-sof-pasuq"}


def strongs_from_lemma(lemma):
    """Turn an OSHB lemma such as ``b/7225`` or ``1254 a`` into ``H7225``.

    OSHB lemmas prefix inseparable particles with a letter (``b`` = בְּ,
    ``c`` = וְ, ``d`` = הַ, ``l`` = לְ, ``k`` = כְּ, ``m`` = מִן, ``s`` = שֶׁ)
    and disambiguate homonyms with a trailing letter (``1254 a``). Numbers are
    returned in Strong's ``H`` form, slash-separated in their original order;
    non-numeric prefixes are dropped.
    """
    out = []
    for part in lemma.split("/"):
        part = part.strip()
        m = re.match(r"^(\d+)\s*([a-z]?)$", part)
        if m:
            out.append("H{:04d}{}".format(int(m.group(1)), m.group(2)))
    return "/".join(out)


def parse_verse(verse_el):
    """Return ``(text, words)`` for one OSIS verse element."""
    pieces = []
    words = []
    # A maqqef or paseq binds the words on either side of it, so the word that
    # follows one is written without an intervening space.
    join_next = False
    for child in verse_el:
        tag = child.tag.replace(OSIS, "")
        if tag == "w":
            # <w> can wrap a <seg> marking an enlarged, small or suspended
            # letter (the ע of שְׁמַע, the ד of אֶחָד), so take the whole subtree.
            surface = "".join(child.itertext()).strip()
            if not surface:
                continue
            lemma = child.get("lemma", "")
            morph = child.get("morph", "")
            words.append({
                "surface": surface,
                "lemma": lemma,
                "morph": morph,
                "strongs": strongs_from_lemma(lemma),
            })
            # Reading text drops the morpheme dividers.
            pieces.append(("" if join_next else " ") + surface.replace("/", ""))
            join_next = False
        elif tag == "seg":
            mark = "".join(child.itertext())
            if child.get("type") in JOINING_SEGS:
                pieces.append(mark)
                join_next = child.get("type") != "x-sof-pasuq"
            else:
                pieces.append(" " + mark)
                join_next = False
        # <note> and its children are apparatus, not text.
    text = "".join(pieces).strip()
    text = re.sub(r"[ \t]+", " ", text)
    return text, words


def main(src, out_dir):
    wlc = os.path.join(src, "wlc")
    verses, rows = [], []
    for osis_id, name in books.OT:
        path = os.path.join(wlc, osis_id + ".xml")
        tree = ET.parse(path)
        for verse_el in tree.iter(OSIS + "verse"):
            ref = verse_el.get("osisID")
            if not ref:
                continue
            _, chapter, verse_no = ref.split(".")
            chapter, verse_no = int(chapter), int(verse_no)
            text, words = parse_verse(verse_el)
            verses.append((name, chapter, verse_no, text))
            for i, w in enumerate(words, 1):
                rows.append((f"{name} {chapter}:{verse_no}", i, w["surface"],
                             w["strongs"], w["lemma"], w["morph"]))

    os.makedirs(out_dir, exist_ok=True)
    n_verses = books.write_verses(os.path.join(out_dir, "wlc.txt"), verses)

    rows.sort(key=lambda r: (books.ORDER[r[0].rsplit(" ", 1)[0]],
                             int(r[0].rsplit(" ", 1)[1].split(":")[0]),
                             int(r[0].rsplit(" ", 1)[1].split(":")[1]), r[1]))
    with open(os.path.join(out_dir, "wlc-words.tsv"), "w", encoding="utf-8") as fh:
        fh.write("reference\tn\tword\tstrongs\toshb_lemma\tmorphology\n")
        for row in rows:
            fh.write("\t".join(str(c) for c in row) + "\n")

    print(f"wlc.txt        {n_verses:,} verses")
    print(f"wlc-words.tsv  {len(rows):,} words")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
