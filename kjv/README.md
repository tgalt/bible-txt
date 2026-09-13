# King James Version (KJV)

The complete King James Version of the Bible in plain text — all 66 books of the
Protestant canon, 1,189 chapters, 31,102 verses.

## Layout

| Path | Contents |
| --- | --- |
| [`kjv.txt`](kjv.txt) | The whole Bible in one file (31,102 verse lines, ~4.4 MB) |
| [`books/`](books) | The same text split into one file per book, numbered in canonical order |

## Format

Every line of scripture is a single verse, prefixed with its full reference:

```
Genesis 1:1 In the beginning God created the heaven and the earth.
John 3:16 For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.
```

The format is identical in `kjv.txt` and in the per-book files, so any line you
copy out carries its own reference. Chapters are separated by a blank line (and
in `kjv.txt`, so are books); no other lines appear in the files.

Because references are anchored at the start of the line, the text greps cleanly:

```sh
grep '^John 3:16 ' kjv.txt              # one verse
grep '^Psalms 23:' kjv.txt              # one chapter
grep -c '^Romans ' kjv.txt              # count verses in a book
grep -i 'lovingkindness' kjv.txt        # word search across the whole Bible
grep -i 'faith without works' books/59-James.txt
```

Book names are spelled as in the table below — note `Psalms` (not `Psalm`),
`Song of Solomon`, and `Revelation` (not `Revelations`). Single-chapter books
(Obadiah, Philemon, 2 John, 3 John, Jude) are still referenced with an explicit
chapter, e.g. `Jude 1:3`.

## Provenance

The text was taken from [`aruljohn/Bible-kjv`](https://github.com/aruljohn/Bible-kjv)
at commit `a9aa4e55afbb3e095f57e4b14cd1f22c5ee8d7c9`, which publishes the KJV as
one JSON file per book under the MIT license. Reflowing it into the line format
above, and the apostrophe normalisation noted below, were the only changes made;
no wording was altered. The King James Version is in the public domain in the
United States. (In the United Kingdom it remains under perpetual Crown copyright,
administered by Cambridge University Press.)

### Verification

The conversion was checked structurally, and the text was checked against a
second, independent transcription — the CrossWire/haiola OSIS edition published
in [`seven1m/open-bibles`](https://github.com/seven1m/open-bibles) as
`eng-kjv.osis.xml`.

- Book, chapter and verse counts match the canonical KJV exactly: 66 books,
  1,189 chapters, 31,102 verses (Old Testament 39 / 929 / 23,145; New Testament
  27 / 260 / 7,957). Per-book chapter counts and the usual landmarks check out
  (Psalm 119 has 176 verses, Psalm 117 has 2, Jude has 25).
- Every one of the 31,102 verse references is present in both sources — none in
  one and missing from the other — and no verse is empty.
- Ignoring capitalisation and punctuation, the two transcriptions agree
  word-for-word on 30,992 of 31,102 verses (99.6%); 29,993 verses (96.4%) are
  identical character for character.
- Both texts carry the distinctive KJV vocabulary in identical counts —
  `shew` 217, `shewed` 135, `Saviour` 29, `enquire` 48, `musick` 16, `basons` 18,
  `astonied` 10, `strawed` 5 — confirming both are genuine transcriptions of the
  1769 Blayney text rather than a modernised revision.

Differences of this kind are normal between digital KJV editions, which descend
from different printings (the Oxford and Cambridge settings differ in punctuation
and in a few spellings) and from different transcription efforts. Of the 1,109
verses that differ at all, 999 differ only in capitalisation or punctuation:
mostly the divine name (`LORD's` here against `LORD'S` there, plus about 116
places where the two disagree between `LORD` and `Lord`, such as `Psalms 3:1`)
and comma or colon placement.

That leaves 110 verses differing in wording, and each is a single word. This text
reads `Cherubims` at Genesis 3:24, `thoroughly` at Genesis 11:3, `chestnut` at
Genesis 30:37 and Ezekiel 31:8, and `honor` at Leviticus 19:15, where the OSIS
edition reads `Cherubim`, `throughly`, `chesnut` and `honour`; conversely the
OSIS edition drops a word at Genesis 50:23 (`the son Manasseh`) and Leviticus
8:16, where this text has the fuller reading. Neither transcription is flawless.
The text here is reproduced exactly as its source publishes it rather than merged
with the other, so that it stays a single citable transcription; where a reading
matters, check a printed edition.

## What this text does and does not include

- **No Apocrypha.** This is the 66-book Protestant canon. The 1611 KJV also
  printed the Apocrypha, and some online KJV editions still carry it — including
  the OSIS edition used for verification above, which adds a further 5,718
  verses across Tobit, Judith, Wisdom, Sirach, Baruch, 1–2 Maccabees, 1–2 Esdras
  and the Greek additions to Esther. None of that is included here.
- **No Psalm superscriptions.** Titles such as *"A Psalm of David, when he fled
  from Absalom his son"* are printed unnumbered above Psalm 3 in the KJV and are
  not part of this text; `Psalms 3:1` begins at *"Lord, how are they increased"*.
- **No italics for supplied words.** Printed KJVs italicise words the translators
  added for English sense ("and *there* was light"). Plain text cannot carry that
  distinction, so those words are indistinguishable from the rest here.
- **No chapter or section headings, no cross-references, no translator's notes** —
  verse text only.
- **ASCII only.** The source used the typographic apostrophe `’` in 1,997 places;
  these were converted to the ASCII `'` so the corpus is 7-bit ASCII throughout
  and searches for terms like `God's` behave predictably. No other character was
  changed.

## Books

| # | Book | File | Chapters | Verses |
| ---: | --- | --- | ---: | ---: |
| 1 | Genesis | [`01-Genesis.txt`](books/01-Genesis.txt) | 50 | 1,533 |
| 2 | Exodus | [`02-Exodus.txt`](books/02-Exodus.txt) | 40 | 1,213 |
| 3 | Leviticus | [`03-Leviticus.txt`](books/03-Leviticus.txt) | 27 | 859 |
| 4 | Numbers | [`04-Numbers.txt`](books/04-Numbers.txt) | 36 | 1,288 |
| 5 | Deuteronomy | [`05-Deuteronomy.txt`](books/05-Deuteronomy.txt) | 34 | 959 |
| 6 | Joshua | [`06-Joshua.txt`](books/06-Joshua.txt) | 24 | 658 |
| 7 | Judges | [`07-Judges.txt`](books/07-Judges.txt) | 21 | 618 |
| 8 | Ruth | [`08-Ruth.txt`](books/08-Ruth.txt) | 4 | 85 |
| 9 | 1 Samuel | [`09-1Samuel.txt`](books/09-1Samuel.txt) | 31 | 810 |
| 10 | 2 Samuel | [`10-2Samuel.txt`](books/10-2Samuel.txt) | 24 | 695 |
| 11 | 1 Kings | [`11-1Kings.txt`](books/11-1Kings.txt) | 22 | 816 |
| 12 | 2 Kings | [`12-2Kings.txt`](books/12-2Kings.txt) | 25 | 719 |
| 13 | 1 Chronicles | [`13-1Chronicles.txt`](books/13-1Chronicles.txt) | 29 | 942 |
| 14 | 2 Chronicles | [`14-2Chronicles.txt`](books/14-2Chronicles.txt) | 36 | 822 |
| 15 | Ezra | [`15-Ezra.txt`](books/15-Ezra.txt) | 10 | 280 |
| 16 | Nehemiah | [`16-Nehemiah.txt`](books/16-Nehemiah.txt) | 13 | 406 |
| 17 | Esther | [`17-Esther.txt`](books/17-Esther.txt) | 10 | 167 |
| 18 | Job | [`18-Job.txt`](books/18-Job.txt) | 42 | 1,070 |
| 19 | Psalms | [`19-Psalms.txt`](books/19-Psalms.txt) | 150 | 2,461 |
| 20 | Proverbs | [`20-Proverbs.txt`](books/20-Proverbs.txt) | 31 | 915 |
| 21 | Ecclesiastes | [`21-Ecclesiastes.txt`](books/21-Ecclesiastes.txt) | 12 | 222 |
| 22 | Song of Solomon | [`22-SongofSolomon.txt`](books/22-SongofSolomon.txt) | 8 | 117 |
| 23 | Isaiah | [`23-Isaiah.txt`](books/23-Isaiah.txt) | 66 | 1,292 |
| 24 | Jeremiah | [`24-Jeremiah.txt`](books/24-Jeremiah.txt) | 52 | 1,364 |
| 25 | Lamentations | [`25-Lamentations.txt`](books/25-Lamentations.txt) | 5 | 154 |
| 26 | Ezekiel | [`26-Ezekiel.txt`](books/26-Ezekiel.txt) | 48 | 1,273 |
| 27 | Daniel | [`27-Daniel.txt`](books/27-Daniel.txt) | 12 | 357 |
| 28 | Hosea | [`28-Hosea.txt`](books/28-Hosea.txt) | 14 | 197 |
| 29 | Joel | [`29-Joel.txt`](books/29-Joel.txt) | 3 | 73 |
| 30 | Amos | [`30-Amos.txt`](books/30-Amos.txt) | 9 | 146 |
| 31 | Obadiah | [`31-Obadiah.txt`](books/31-Obadiah.txt) | 1 | 21 |
| 32 | Jonah | [`32-Jonah.txt`](books/32-Jonah.txt) | 4 | 48 |
| 33 | Micah | [`33-Micah.txt`](books/33-Micah.txt) | 7 | 105 |
| 34 | Nahum | [`34-Nahum.txt`](books/34-Nahum.txt) | 3 | 47 |
| 35 | Habakkuk | [`35-Habakkuk.txt`](books/35-Habakkuk.txt) | 3 | 56 |
| 36 | Zephaniah | [`36-Zephaniah.txt`](books/36-Zephaniah.txt) | 3 | 53 |
| 37 | Haggai | [`37-Haggai.txt`](books/37-Haggai.txt) | 2 | 38 |
| 38 | Zechariah | [`38-Zechariah.txt`](books/38-Zechariah.txt) | 14 | 211 |
| 39 | Malachi | [`39-Malachi.txt`](books/39-Malachi.txt) | 4 | 55 |
| 40 | Matthew | [`40-Matthew.txt`](books/40-Matthew.txt) | 28 | 1,071 |
| 41 | Mark | [`41-Mark.txt`](books/41-Mark.txt) | 16 | 678 |
| 42 | Luke | [`42-Luke.txt`](books/42-Luke.txt) | 24 | 1,151 |
| 43 | John | [`43-John.txt`](books/43-John.txt) | 21 | 879 |
| 44 | Acts | [`44-Acts.txt`](books/44-Acts.txt) | 28 | 1,007 |
| 45 | Romans | [`45-Romans.txt`](books/45-Romans.txt) | 16 | 433 |
| 46 | 1 Corinthians | [`46-1Corinthians.txt`](books/46-1Corinthians.txt) | 16 | 437 |
| 47 | 2 Corinthians | [`47-2Corinthians.txt`](books/47-2Corinthians.txt) | 13 | 257 |
| 48 | Galatians | [`48-Galatians.txt`](books/48-Galatians.txt) | 6 | 149 |
| 49 | Ephesians | [`49-Ephesians.txt`](books/49-Ephesians.txt) | 6 | 155 |
| 50 | Philippians | [`50-Philippians.txt`](books/50-Philippians.txt) | 4 | 104 |
| 51 | Colossians | [`51-Colossians.txt`](books/51-Colossians.txt) | 4 | 95 |
| 52 | 1 Thessalonians | [`52-1Thessalonians.txt`](books/52-1Thessalonians.txt) | 5 | 89 |
| 53 | 2 Thessalonians | [`53-2Thessalonians.txt`](books/53-2Thessalonians.txt) | 3 | 47 |
| 54 | 1 Timothy | [`54-1Timothy.txt`](books/54-1Timothy.txt) | 6 | 113 |
| 55 | 2 Timothy | [`55-2Timothy.txt`](books/55-2Timothy.txt) | 4 | 83 |
| 56 | Titus | [`56-Titus.txt`](books/56-Titus.txt) | 3 | 46 |
| 57 | Philemon | [`57-Philemon.txt`](books/57-Philemon.txt) | 1 | 25 |
| 58 | Hebrews | [`58-Hebrews.txt`](books/58-Hebrews.txt) | 13 | 303 |
| 59 | James | [`59-James.txt`](books/59-James.txt) | 5 | 108 |
| 60 | 1 Peter | [`60-1Peter.txt`](books/60-1Peter.txt) | 5 | 105 |
| 61 | 2 Peter | [`61-2Peter.txt`](books/61-2Peter.txt) | 3 | 61 |
| 62 | 1 John | [`62-1John.txt`](books/62-1John.txt) | 5 | 105 |
| 63 | 2 John | [`63-2John.txt`](books/63-2John.txt) | 1 | 13 |
| 64 | 3 John | [`64-3John.txt`](books/64-3John.txt) | 1 | 14 |
| 65 | Jude | [`65-Jude.txt`](books/65-Jude.txt) | 1 | 25 |
| 66 | Revelation | [`66-Revelation.txt`](books/66-Revelation.txt) | 22 | 404 |
