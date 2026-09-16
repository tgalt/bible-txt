#!/usr/bin/env python3
"""Build 1-enoch.txt (and 1-enoch-greek-parallels.txt) from scrollmapper's
transcription of R. H. Charles's 1917 translation of 1 Enoch.

Usage:
    build_1enoch.py SOURCE.txt OUT_DIR

SOURCE.txt is txt/1-enoch/1-enoch.txt from
https://github.com/scrollmapper/bible_databases_deuterocanonical at commit
97e883ac0271923f852a3d78cb4124da867db1c4 (branch `2024`).  That file keeps
Charles's brackets and daggers, which the repository's later `master` copy
mostly strips.

The source marks verses as `[chapter:verse]` inline, and it reproduces the
1917 edition's page layout more or less literally: transposed verses appear
where Charles printed them, clauses he re-ordered carry his letters (5:6a,
5:7c ...), and where he printed the Ethiopic and the Gizeh Greek in parallel
columns (chapters 22, 27, 32) both columns appear one after the other.  It
also has a number of transcription faults: some verse markers are missing,
chapter 44 is absent, a few numerals in the text were mistaken for markers,
and there is a handful of typing errors.

This script applies the explicit, itemised repairs in REPAIRS below, then
reflows the text into the repository's one-verse-per-line format in plain
chapter-and-verse order.  Every repair is a literal string replacement that
must match exactly once, so the script fails loudly if the source changes.
No other wording is altered.  See ../README.md for the reasoning behind each
class of repair.
"""

import re
import sys
from collections import OrderedDict, defaultdict

BOOK = "1 Enoch"

# Each entry: (old, new, note).  Every `old` must occur exactly once.
REPAIRS = [
    # ---- title line -------------------------------------------------------
    ("1 Enoch\n\n[1:1]", "[1:1]", "drop the source's title line"),

    # ---- missing verse markers (text present, number lost) -----------------
    ("he shall be cast into the fire. And heal the earth which the angels have corrupted",
     "he shall be cast into the fire. [10:7] And heal the earth which the angels have corrupted", "10:7"),
    ("confined for ever. And whosoever shall be condemned",
     "confined for ever. [10:14] And whosoever shall be condemned", "10:14"),
    ("because they have wronged mankind. Destroy all wrong from the face",
     "because they have wronged mankind. [10:16] Destroy all wrong from the face", "10:16"),
    ("it began to affright me. And I went into the tongues of fire",
     "it began to affright me. [14:10] And I went into the tongues of fire", "14:10"),
    ('(say to them): "You have been in heaven, but',
     '(say to them): [16:3] "You have been in heaven, but', "16:3"),
    ("the firmament of the heaven above. And I proceeded and saw a place which burns",
     "the firmament of the heaven above. [18:6] And I proceeded and saw a place which burns", "18:6"),
    ("should assemble here. And these places have been made to receive them",
     "should assemble here. [22:4] And these places have been made to receive them", "22:4"),
    ("learn the truth?' Then I answered him",
     "learn the truth?' [25:2] Then I answered him", "25:2"),
    ("especially about this tree.' And he answered saying: 'This high mountain",
     "especially about this tree.' [25:3] And he answered saying: 'This high mountain", "25:3"),
    ("with the Head of Days? And he answered and said unto me: \nThis is the son of Man who hath",
     "with the Head of Days? [46:3] And he answered and said unto me: This is the Son of Man who hath",
     "46:3; the source also has 'son of Man' here against 'Son of Man' everywhere else"),
    ("the quaking of the heaven. And Michael said unto me:",
     "the quaking of the heaven. [60:5] And Michael said unto me:", "60:5"),
    ("many quarters of the earth. And the spirit of the sea is masculine",
     "many quarters of the earth. [60:16] And the spirit of the sea is masculine", "60:16"),
    ("and cold and snow and frost. And from the middle portal come forth dew and rain, and prosperity",
     "and cold and snow and frost. [76:13] And from the middle portal come forth dew and rain, and prosperity", "76:13"),
    ("[82:13] And the names of those who lead them",
     "[82:14] And the names of those who lead them", "82:14 was numbered 13"),
    ("make the division. And these are the names of the leaders who divide the four parts",
     "make the division. [82:13] And these are the names of the leaders who divide the four parts", "82:13"),
    ("recount from the books. And Enoch said: \n'Concerning the children",
     "recount from the books. [93:2] And Enoch said: 'Concerning the children", "93:2"),
    ("in all their ways. Semjâzâ taught enchantments",
     "in all their ways. [8:3] Semjâzâ taught enchantments", "8:3"),
    ("the course of the moon. And as men perished, they cried",
     "the course of the moon. [8:4] And as men perished, they cried", "8:4"),
    ("and all shall worship Me. And the earth shall be cleansed from all defilement",
     "and all shall worship Me. [10:22] And the earth shall be cleansed from all defilement", "10:22"),
    ("and cause offences. And these spirits shall rise up",
     "and cause offences. [15:12] And these spirits shall rise up", "15:12"),
    ("is named Phanuel.' And these are the four angels of the Lord of Spirits",
     "is named Phanuel.' [40:10] And these are the four angels of the Lord of Spirits", "40:10"),
    ("as if they were the Lord. Therefore all that is hidden shall come upon them",
     "as if they were the Lord. [68:5] Therefore all that is hidden shall come upon them", "68:5"),
    ("and they resembled him. And they began to beget many white bulls",
     "and they resembled him. [85:10] And they began to beget many white bulls", "85:10"),
    ("against all the shepherds. And he took the actual book",
     "against all the shepherds. [89:77] And he took the actual book", "89:77"),

    # ---- chapter 44 (one verse) is absent from the source -------------------
    ("[45:1]",
     "[44:1] Also another phenomenon I saw in regard to the lightnings: how some of the stars "
     "arise and become lightnings and cannot part with their new form.\n\n[45:1]",
     "44:1 supplied from the two other transcriptions, which agree verbatim"),

    # ---- numerals in the text that were mistaken for verse markers ---------
    ("in [74:5] years [74:6] days every year come to [74:30] days",
     "in 5 years 6 days every year come to 30 days", "74:11"),
    ("and in [74:5] years 1820 days", "and in 5 years 1820 days", "74:13"),
    ("And [106:1] said unto him", "And I said unto him", "106:8: the pronoun I was read as a marker"),

    # ---- parallel columns in chapter 22 ------------------------------------
    # Charles prints the Ethiopic (E) and the Gizeh Greek (Gg) side by side.
    # The source runs the columns one after the other, and splits 22:10 in
    # both columns at the page break.  Reunite each column's 22:10 with its
    # own marker; the parser then treats the second copy of a verse as Gg.
    ("[22:10] And such has \nGg", "\nGg", "22:10 (E) first half detached"),
    ("[22:10] And this has been made for sinners \n\n   \nE", "\nE", "22:10 (Gg) first half detached"),
    ("been made for sinners when they die and are buried in the earth and judgement has not been executed on them",
     "[22:10] And such has been made for sinners when they die and are buried in the earth and judgement has not been executed on them",
     "22:10 (E) reunited"),
    ("when they die and are buried in the earth and judgement has not been executed upon them",
     "[22:10] And this has been made for sinners when they die and are buried in the earth and judgement has not been executed upon them",
     "22:10 (Gg) reunited"),
    ("Here shall they be gathered together, and here shall be the place of their habitation.",
     "[27:2] Here shall they be gathered together, and here shall be the place of their habitation.",
     "27:2 (Gg): only its last sentence differs from E, and it carries no marker"),

    # ---- brackets that open at the end of one verse and belong to the next --
    ("eternity to eternity. \n⌈[69:22] And in like manner",
     "eternity to eternity. \n[69:22] ⌈And in like manner", "⌈ opening 69:22-24"),
    ("given unto them. \n[[91:11] And after", "given unto them. \n[91:11] [And after", "[ opening 91:11"),
    ("all His creation. \n[[93:11] For who", "all His creation. \n[93:11] [For who", "[ opening 93:11-14"),
    ("according to your desires.\n[[96:2] And in the day",
     "according to your desires.\n[96:2] [And in the day", "[ opening 96:2"),
    ("evil spirits shall they be called. [[15:10] As for",
     "evil spirits shall they be called. [15:10] [As for", "[ opening 15:10"),

    # ---- stray punctuation left at the start of a verse -----------------------
    ("[30:1] .And beyond these", "[30:1] And beyond these", "30:1"),
    ("[46:4], And this Son of Man", "[46:4] And this Son of Man", "46:4"),
    ("[100:2] .For a man shall not", "[100:2] For a man shall not", "100:2"),

    # ---- typing errors in the source, corrected where the other transcription
    #      has the evident reading ---------------------------------------------
    ("'Why as one separated from the other?'", "'Why is one separated from the other?'", "22:8"),
    ("in which there as the bright spring", "in which there is the bright spring", "22:9"),
    ("(there maybe) retribution", "(there may be) retribution", "22:11 (Gg)"),
    ("and of the transgressors. they shall be companions", "and of the transgressors they shall be companions", "22:13"),
    ("the Eternal Kin. ", "the Eternal King. ", "27:3 (Gg)"),
    ("And the spiritopt of those who have fallen asleep", "And the spirit of those who have fallen asleep", "49:3"),
    ("those six portals in the cast", "those six portals in the east", "72:6"),
    ("butted and kiled the wild beasts", "butted and killed the wild beasts", "89:49"),
    ("the first which had beer folded up", "the first which had been folded up", "90:29"),
    ("And there upon Methuselah went", "And thereupon Methuselah went", "91:2"),
    ("your godlessness as wrought", "your godlessness has wrought", "100:9"),
    ("And are complained to the rulers", "And we complained to the rulers", "103:14"),
    ("Tabââ\x91ĕt", "Tabââ'ĕt", "69:12: a Windows-1252 apostrophe byte"),
    ("because of you-and weep", "because of you--and weep", "96:2: dash typed as a hyphen"),
    ("with a loud voice, . . .with the spirit", "with a loud voice, . . . with the spirit", "71:11: spacing of the ellipsis"),
]

# Chapters in which Charles prints the Ethiopic and the Gizeh Greek in
# parallel.  A second copy of a verse number in these chapters is the Greek.
PARALLEL_CHAPTERS = {22, 27, 32}

MARKER = re.compile(r"\[(\d+):(\d+)([a-z]?)\]")
LABEL_LINE = re.compile(r"^[ \t]*(E|Gg)[ \t]*$", re.M)
# Charles's clause letters inside re-ordered verses: "b. And by you ..."
CLAUSE_LETTER = re.compile(r"(?<![A-Za-z])[b-j]\.?\s+(?=[A-Z(⌈\[])")


def apply_repairs(text):
    text = text.replace("\xa0", " ")   # the source uses no-break spaces around its column labels
    for old, new, note in REPAIRS:
        n = text.count(old)
        if n != 1:
            sys.exit(f"repair for {note!r} matched {n} times, expected 1: {old!r}")
        text = text.replace(old, new)
    return text


def tidy(s):
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse(text):
    """Return ({(ch, v): text}, {(ch, v): text}) for the main text and the
    Gizeh Greek parallels."""
    text = LABEL_LINE.sub("", text)
    pieces = MARKER.split(text)
    # pieces = [preamble, ch, v, letter, body, ch, v, letter, body, ...]
    if pieces[0].strip():
        sys.exit(f"text before first marker: {pieces[0]!r}")
    segments = []  # (ch, v, letter, body)
    for i in range(1, len(pieces), 4):
        ch, v, letter, body = int(pieces[i]), int(pieces[i + 1]), pieces[i + 2], pieces[i + 3]
        segments.append((ch, v, letter, body))

    main = OrderedDict()
    greek = OrderedDict()
    lettered = defaultdict(list)
    seen = defaultdict(set)
    for ch, v, letter, body in segments:
        if letter:
            lettered[(ch, v)].append((letter, body))
            continue
        key = (ch, v)
        if key in main:
            if ch not in PARALLEL_CHAPTERS:
                sys.exit(f"duplicate verse {ch}:{v} outside the parallel-column chapters")
            if key in greek:
                sys.exit(f"verse {ch}:{v} appears three times")
            greek[key] = body
        else:
            main[key] = body
    # Re-ordered clauses: put each verse's clauses back in letter order.  The
    # unlettered part of the verse (97:9, 89:48) comes first.
    for key, parts in lettered.items():
        parts.sort(key=lambda p: p[0])
        joined = " ".join(CLAUSE_LETTER.sub("", p[1]) for p in parts)
        joined = re.sub(r"(?m)^\s*j\s+(?=But on you all)", "", joined)  # "j But on you" (5:6)
        if key in main:
            main[key] = main[key] + " " + joined
        else:
            main[key] = joined
    main = OrderedDict((k, tidy(t)) for k, t in main.items())
    greek = OrderedDict((k, tidy(t)) for k, t in greek.items())
    for k, t in list(main.items()) + list(greek.items()):
        if not t:
            sys.exit(f"empty verse {k}")
    return main, greek


def check_structure(main):
    chapters = sorted({ch for ch, _ in main})
    if chapters != list(range(1, 109)):
        sys.exit(f"chapters are not 1..108: {chapters}")
    for ch in chapters:
        vs = sorted(v for c, v in main if c == ch)
        if vs != list(range(1, len(vs) + 1)):
            sys.exit(f"chapter {ch} verses are not contiguous: {vs}")


def write(path, verses):
    chapters = sorted({ch for ch, _ in verses})
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for i, ch in enumerate(chapters):
            if i:
                f.write("\n")
            for v in sorted(v for c, v in verses if c == ch):
                f.write(f"{BOOK} {ch}:{v} {verses[(ch, v)]}\n")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out_dir = sys.argv[1], sys.argv[2]
    text = open(src, encoding="utf-8").read()
    text = apply_repairs(text)
    verses, greek = parse(text)
    check_structure(verses)
    write(f"{out_dir}/1-enoch.txt", verses)
    write(f"{out_dir}/1-enoch-greek-parallels.txt", greek)
    print(f"{len(verses)} verses in {len({c for c, _ in verses})} chapters; "
          f"{len(greek)} Gizeh Greek parallel verses")


if __name__ == "__main__":
    main()
