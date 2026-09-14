"""Canonical book names and OSIS identifier maps.

Book names match those used by ``kjv/kjv.txt`` so that references produced by
these tools line up with the KJV corpus and grep the same way.
"""

OT = [
    ("Gen", "Genesis"), ("Exod", "Exodus"), ("Lev", "Leviticus"),
    ("Num", "Numbers"), ("Deut", "Deuteronomy"), ("Josh", "Joshua"),
    ("Judg", "Judges"), ("Ruth", "Ruth"), ("1Sam", "1 Samuel"),
    ("2Sam", "2 Samuel"), ("1Kgs", "1 Kings"), ("2Kgs", "2 Kings"),
    ("1Chr", "1 Chronicles"), ("2Chr", "2 Chronicles"), ("Ezra", "Ezra"),
    ("Neh", "Nehemiah"), ("Esth", "Esther"), ("Job", "Job"),
    ("Ps", "Psalms"), ("Prov", "Proverbs"), ("Eccl", "Ecclesiastes"),
    ("Song", "Song of Solomon"), ("Isa", "Isaiah"), ("Jer", "Jeremiah"),
    ("Lam", "Lamentations"), ("Ezek", "Ezekiel"), ("Dan", "Daniel"),
    ("Hos", "Hosea"), ("Joel", "Joel"), ("Amos", "Amos"),
    ("Obad", "Obadiah"), ("Jonah", "Jonah"), ("Mic", "Micah"),
    ("Nah", "Nahum"), ("Hab", "Habakkuk"), ("Zeph", "Zephaniah"),
    ("Hag", "Haggai"), ("Zech", "Zechariah"), ("Mal", "Malachi"),
]

NT = [
    ("Matt", "Matthew"), ("Mark", "Mark"), ("Luke", "Luke"), ("John", "John"),
    ("Acts", "Acts"), ("Rom", "Romans"), ("1Cor", "1 Corinthians"),
    ("2Cor", "2 Corinthians"), ("Gal", "Galatians"), ("Eph", "Ephesians"),
    ("Phil", "Philippians"), ("Col", "Colossians"),
    ("1Thess", "1 Thessalonians"), ("2Thess", "2 Thessalonians"),
    ("1Tim", "1 Timothy"), ("2Tim", "2 Timothy"), ("Titus", "Titus"),
    ("Phlm", "Philemon"), ("Heb", "Hebrews"), ("Jas", "James"),
    ("1Pet", "1 Peter"), ("2Pet", "2 Peter"), ("1John", "1 John"),
    ("2John", "2 John"), ("3John", "3 John"), ("Jude", "Jude"),
    ("Rev", "Revelation"),
]

OSIS_TO_NAME = dict(OT + NT)
OT_NAMES = [name for _, name in OT]
NT_NAMES = [name for _, name in NT]
ALL_NAMES = OT_NAMES + NT_NAMES
ORDER = {name: i for i, name in enumerate(ALL_NAMES)}

# Numeric book order used by CNTR (40 = Matthew) and similar sources.
NT_BY_NUMBER = {40 + i: name for i, name in enumerate(NT_NAMES)}


def write_verses(path, verses):
    """Write ``(book, chapter, verse, text)`` rows in the repo's line format.

    One verse per line, prefixed with its reference; a blank line between
    chapters and between books, exactly as ``kjv/kjv.txt`` is laid out.
    """
    verses = sorted(verses, key=lambda r: (ORDER[r[0]], r[1], r[2]))
    with open(path, "w", encoding="utf-8") as fh:
        prev = None
        for book, chapter, verse, text in verses:
            if prev is not None and (book, chapter) != prev:
                fh.write("\n")
            fh.write(f"{book} {chapter}:{verse} {text}\n")
            prev = (book, chapter)
    return len(verses)
