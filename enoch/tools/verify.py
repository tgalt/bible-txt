#!/usr/bin/env python3
"""Check 1-enoch.txt (and the parallels file) for the repository's line format
and report the figures quoted in README.md.

Usage: verify.py [DIR]   (DIR defaults to the directory above this script)
"""

import os
import re
import sys
import unicodedata
from collections import Counter

LINE = re.compile(r"^1 Enoch (\d+):(\d+) (\S.*\S|\S)$")
PAIRS = [("⌈", "⌉"), ("〈", "〉"), ("[", "]"), ("(", ")")]


def read(path):
    verses, blanks, prev_ch = [], 0, None
    for n, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.rstrip("\n")
        if line == "":
            blanks += 1
            continue
        m = LINE.match(line)
        if not m:
            sys.exit(f"{path}:{n}: malformed line: {line[:80]!r}")
        ch, v, text = int(m.group(1)), int(m.group(2)), m.group(3)
        if "  " in text:
            sys.exit(f"{path}:{n}: double space")
        if prev_ch is not None and ch != prev_ch and blanks != 1:
            sys.exit(f"{path}:{n}: chapters must be separated by exactly one blank line")
        if ch == prev_ch and blanks:
            sys.exit(f"{path}:{n}: blank line inside a chapter")
        blanks, prev_ch = 0, ch
        verses.append((ch, v, text))
    return verses


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    main_v = read(os.path.join(d, "1-enoch.txt"))
    par_v = read(os.path.join(d, "1-enoch-greek-parallels.txt"))

    chapters = [ch for ch, _, _ in main_v]
    if sorted(set(chapters)) != list(range(1, 109)):
        sys.exit("chapters are not exactly 1..108")
    if chapters != sorted(chapters):
        sys.exit("chapters out of order")
    per_ch = Counter(chapters)
    for ch in range(1, 109):
        vs = [v for c, v, _ in main_v if c == ch]
        if vs != list(range(1, len(vs) + 1)):
            sys.exit(f"chapter {ch}: verses not 1..{len(vs)}: {vs}")
    for ch, v, _ in par_v:
        if (ch, v) not in {(c, x) for c, x, _ in main_v}:
            sys.exit(f"parallel {ch}:{v} has no counterpart in the main text")

    words = sum(len(t.split()) for _, _, t in main_v)
    print(f"1-enoch.txt: {len(main_v)} verses, 108 chapters, {words} words")
    print(f"1-enoch-greek-parallels.txt: {len(par_v)} verses in chapters "
          f"{sorted({c for c, _, _ in par_v})}")
    print("verses per chapter:", ", ".join(f"{c}:{per_ch[c]}" for c in range(1, 109)))

    alltext = " ".join(t for _, _, t in main_v + par_v)
    non_ascii = Counter(c for c in alltext if ord(c) > 127)
    print("non-ASCII characters:")
    for c, n in sorted(non_ascii.items(), key=lambda x: -x[1]):
        print(f"  {c}  U+{ord(c):04X} {unicodedata.name(c, '?')}: {n}")

    print("brackets and daggers (whole text):")
    for o, c in PAIRS:
        print(f"  {o} {alltext.count(o)}   {c} {alltext.count(c)}")
    print(f"  † {alltext.count(chr(0x2020))}")
    print("verses whose brackets do not balance within the verse (a bracket may span verses):")
    for ch, v, t in main_v + par_v:
        for o, c in PAIRS:
            if t.count(o) != t.count(c):
                print(f"  {ch}:{v}  {o}{t.count(o)} {c}{t.count(c)}")
    odd = [f"{ch}:{v}" for ch, v, t in main_v + par_v if t.count("\u2020") % 2]
    print("verses with an odd number of daggers (Charles also puts a single \u2020 before one word):")
    print("  " + ", ".join(odd))
    print("ok")


if __name__ == "__main__":
    main()
