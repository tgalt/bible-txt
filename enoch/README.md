# 1 Enoch (the Book of Enoch)

The Ethiopic Book of Enoch — 1 Enoch — in the English translation of
R. H. Charles, published by the SPCK in 1917, in the same plain-text line
format as [`kjv/`](../kjv): 108 chapters, 1,063 verses.

1 Enoch is not in the KJV or in any Western canon (it is Scripture only in
the Ethiopian Orthodox Church), but it stands behind the New Testament at
several points. Jude 14–15 quotes 1 Enoch 1:9 almost word for word, and the
"Son of Man" enthroned in judgement in the Parables (chapters 37–71) is the
closest Jewish parallel to the Gospels' use of the title:

```sh
grep '^1 Enoch 1:9 ' 1-enoch.txt
grep '^Jude 1:1[45] ' ../kjv/kjv.txt
```

## Layout

| Path | Contents |
| --- | --- |
| [`1-enoch.txt`](1-enoch.txt) | The whole book, one verse per line (1,063 lines, ~208 KB) |
| [`1-enoch-greek-parallels.txt`](1-enoch-greek-parallels.txt) | Charles's rendering of the Gizeh Greek text where he printed it in a column beside the Ethiopic (14 verses of chapters 22, 27 and 32) |
| [`tools/`](tools) | The build and verification scripts |

## Format

Every line is one verse, prefixed with its reference, exactly as in
[`kjv/kjv.txt`](../kjv/kjv.txt). Chapters are separated by a blank line and no
other lines appear:

```
1 Enoch 1:1 The words of the blessing of Enoch, wherewith he blessed the elect ⌈⌈and⌉⌉ righteous, who will be living in the day of tribulation, when all the wicked ⌈⌈and godless⌉⌉ are to be removed.
```

```sh
grep '^1 Enoch 1:9 ' 1-enoch.txt          # one verse
grep '^1 Enoch 22:' 1-enoch.txt           # one chapter
grep -c '^1 Enoch ' 1-enoch.txt           # count verses
grep -i 'son of man' 1-enoch.txt          # word search
```

The book is called `1 Enoch` (not `Enoch`), following the usual scholarly
citation, and on the pattern of `1 Samuel` in the KJV files. Single-verse
chapters (3, 4, 35, 44) are still referenced with a verse, e.g. `1 Enoch 44:1`.

Unlike the KJV corpus this text is **not ASCII**. It is UTF-8 for two reasons:

- Charles transliterates Ethiopic names with circumflexed vowels — `Azâzêl`,
  `Semjâzâ`, `Dûdâêl` — so a search for a name needs the accents (or
  `grep -i 'az.z.l'`). The file uses `â ê î ô û Ê Î ĕ` and no other letters
  outside ASCII.
- His critical brackets are kept (see the next section): half brackets `⌈ ⌉`,
  angle brackets `〈 〉` and the dagger `†`.

Quotation marks and dashes are plain ASCII (`'`, `"`, `--`), and Charles's
lacuna mark is a spaced ellipsis `. . .`, as printed.

## Charles's brackets and marks

The 1917 edition carries the apparatus of Charles's critical edition (Oxford,
1912) into the translation with a set of typographic marks, and this
transcription keeps them, since a plain-text reader has no other way to tell
a word Charles supplied from a word the manuscripts contain:

| Mark | Charles uses it for |
| --- | --- |
| `⌈ ⌉` and `⌈⌈ ⌉⌉` | words emended or restored — in chapters 1–32 largely on the evidence of the Greek |
| `〈 〉` | words restored |
| `[ ]` | words he judged an interpolation |
| `( )` | words supplied by the translator for the English sense |
| `†word†` or `†word` | a corrupt passage or word (a single dagger before one word is his usage too, e.g. 39:1, 75:5, 83:11) |
| `. . .` | a lacuna |

The exact key is in the front matter of the 1917 edition, which is not
reproduced here. Brackets may open in one verse and close in a later one
(39:1–2, 69:2–3, 69:22–24, 93:11–14). Two brackets are unmatched in the source
and are left as found: `⌈⌈` opens in 3:1 and never closes, and `]` closes 59:3
with no opening.

## The book

| Chapters | Section |
| --- | --- |
| 1–36 | The Book of the Watchers: introduction (1–5), the fall of the angels and Enoch's intercession (6–16), Enoch's journeys through the earth and Sheol (17–36) |
| 37–71 | The Parables (Similitudes) of Enoch: three parables (38–44, 45–57, 58–69) and Enoch's translation (70–71); the Son of Man chapters |
| 72–82 | The Astronomical Book (the Book of the Heavenly Luminaries) |
| 83–90 | The Dream Visions, including the Animal Apocalypse (85–90) |
| 91–105 | The Epistle of Enoch, including the Apocalypse of Weeks (93:1–10 with 91:11–17) |
| 106–107 | The birth of Noah (a fragment of a Book of Noah) |
| 108 | A concluding appendix |

Charles regarded 91:11–17 as displaced from after 93:10, 60:25 from after
60:6, and 106:17 from before 106:15, and printed them where he thought they
belonged; he also printed the two parallel accounts in 90:13–15 and 90:16–18
side by side, moved half of 89:48 to follow 89:49, and re-ordered the clauses
of 5:6–7, 39:6–7, 51:5, 91:14 and 97:9, lettering them (5:6a, 5:7c, 5:6d …).
**This file keeps every verse under its own number in plain numerical order**,
so that a reference always finds one line and a chapter is always one block.
Where he re-ordered clauses inside a verse, the verse's clauses are gathered
in his letter order (a, b, c …) and the letters dropped; 89:48 is one line
again. Anyone who wants to read the Apocalypse of Weeks in Charles's order
reads 93:1–10 and then 91:11–17.

Where Charles printed the Ethiopic (his `E`) and the Gizeh Greek papyrus (his
`Gg`) in two columns because they diverge — 22:2, 5–6, 8–14; 27:2–3; 32:1, 3 —
`1-enoch.txt` follows the Ethiopic column, which is his base text throughout,
and [`1-enoch-greek-parallels.txt`](1-enoch-greek-parallels.txt) has his
rendering of the Greek column under the same references. (For 27:2 only the
last sentence differs, and only that sentence is given.) The sentence *This is
the Third Parable of Enoch*, which Charles prints unnumbered after 69:29, is
kept at the end of that line.

## Provenance

The text was taken from
[`scrollmapper/bible_databases_deuterocanonical`](https://github.com/scrollmapper/bible_databases_deuterocanonical),
file `txt/1-enoch/1-enoch.txt` at commit
`97e883ac0271923f852a3d78cb4124da867db1c4` (branch `2024`). That copy keeps
Charles's brackets and daggers; the repository's current `master` carries a
later version of the same transcription with most of them stripped. The
repository publishes no licence file; the translation itself is in the public
domain everywhere (published 1917, Charles died 1931).

The source reproduces the 1917 page layout more or less literally — verse
numbers as `[1:1]`, Charles's transposed verses where he printed them, his
clause letters, both columns of the parallel passages — and it has a number of
transcription faults. Everything done to it is an explicit, itemised string
replacement in [`tools/build_1enoch.py`](tools/build_1enoch.py); the script
refuses to run if any of them stops matching exactly once. In full:

- **Reflow** into the line format above, in numerical order, as described in
  the previous section.
- **Verse numbers that the source had lost**, so that a verse ran on into the
  one before it, were restored at the boundary shown by the second
  transcription and by the Ethiopic verse division (below): 8:3, 8:4, 10:7,
  10:14, 10:16, 10:22, 14:10, 15:12, 16:3, 18:6, 22:4, 25:2, 25:3, 40:10, 46:3,
  60:5, 60:16, 68:5, 76:13, 82:13 (the source numbered 82:14 as 13), 85:10,
  89:77, 93:2.
- **Chapter 44**, a single verse, is absent from the source and was supplied
  from the two other transcriptions, which agree on it word for word.
- **Numerals mistaken for verse markers** were put back into the text: `5`,
  `6` and `30` in 74:11 and `5` in 74:13 (the source had them as `[74:5]` and
  so on), and the pronoun `I` in 106:8, which had become `[106:1]`.
- Verse **22:10** had been split in both columns at a page break and its halves
  parked in the wrong column; each half was rejoined to its own column.
- Five **brackets standing on a line of their own** were attached to the verse
  they open (15:10, 69:22, 91:11, 93:11, 96:2), and stray punctuation was
  removed from the start of 30:1, 46:4 and 100:2.
- **Typing errors** were corrected where the second transcription has the
  evident reading. Every one is listed here:

  | Verse | Source | Here |
  | --- | --- | --- |
  | 22:8 | `Why as one separated` | `Why is one separated` |
  | 22:9 | `in which there as the bright spring` | `there is` |
  | 22:11 (Greek) | `(there maybe) retribution` | `(there may be)` |
  | 22:13 | `of the transgressors. they shall be` | `of the transgressors they shall be` |
  | 27:3 (Greek) | `the Eternal Kin.` | `the Eternal King.` |
  | 46:3 | `This is the son of Man` | `This is the Son of Man` (as everywhere else) |
  | 49:3 | `the spiritopt of those` | `the spirit of those` |
  | 69:12 | a stray Windows-1252 byte in `Tabââ'ĕt` | the apostrophe |
  | 71:11 | `. . .with` | `. . . with` |
  | 72:6 | `six portals in the cast` | `in the east` |
  | 89:49 | `butted and kiled` | `butted and killed` |
  | 90:29 | `which had beer folded up` | `which had been folded up` |
  | 91:2 | `And there upon Methuselah` | `And thereupon Methuselah` |
  | 96:2 | `because of you-and weep` | `because of you--and weep` |
  | 100:9 | `your godlessness as wrought` | `has wrought` |
  | 103:14 | `And are complained to the rulers` | `And we complained` |

Nothing else was changed. In particular the source's spellings were kept even
where the second transcription differs (see the table under Verification),
`ought` stands at 89:49 (`robbed them no more of ought`) because every copy has
it, and the unmatched brackets at 3:1 and 59:3 are left as found.

### Verification

Structure, by [`tools/verify.py`](tools/verify.py): chapters run 1–108 with
no gap; within every chapter the verses run from 1 with no gap or repeat; no
verse is empty; every parallel verse has a counterpart in the main text.

Against the Ethiopic: the
[Online Critical Pseudepigrapha](https://github.com/OnlineCriticalPseudepigrapha/Online-Critical-Pseudepigrapha)
edition of 1 Enoch (`static/docs/1En.xml`, commit `c939dcb`, CC BY 4.0) gives
the Ethiopic text of Rylands Ethiopic MS 23 as edited by Knibb, versified, for
chapters 1–71. Its verse count agrees with this file in every one of those
chapters except 20, where it has 7 verses and Charles 8: 20:8 (*Remiel, one of
the holy angels, whom God set over those who rise*) survives only in the Greek,
and Charles includes it.

Against a second transcription of the same translation:
[`LPettay/ethiopian-bible`](https://github.com/LPettay/ethiopian-bible) at
commit `e7059fbbf403f7c94889ca0fa1ce03ac017f90a3` carries Charles's 1917 text
verse by verse (`public/data/chapters/1En/*.json`, field `translation`), from a
different line of transmission — it has curly quotes, British spellings and a
different set of faults (dropped verses, footnotes leaking into the text,
Charles's transposed verses copied twice). Comparing verse by verse, ignoring
capitalisation, punctuation and Charles's brackets:

- 984 of the 1,063 verses are identical word for word.
- 5 verses are missing from the second transcription altogether (20:8, 21:1,
  28:3, 98:16, 100:13), as is `〈of days〉` in 13:6; this text has them.
- In 6 places the second transcription draws a verse boundary one sentence
  later than the source here (7:3–4, 12:4–5, 18:9–10, 83:2–3, 91:3–4,
  103:1–2). Charles's poetic layout puts the sentence at the end of the earlier
  verse in each case, as this text does.
- The rest of the differing verses are the second transcription's own
  duplications and leaked notes, plus the spellings below, where this text
  follows its source and the other copy reads otherwise:

  | Verse | Here | Second transcription |
  | --- | --- | --- |
  | 6:7 | `Sêmîazâz` | `Samîazâz` |
  | 8:3 | `Ezêqêêl` | `Êzêqêêl` |
  | 9:2 | `crying` | `cryings` |
  | 14:22, 47:3 | `counselor(s)` | `counsellor(s)` |
  | 22:14 (Greek) | `who rulest` | `who ruleth` |
  | 26:6 | `marveled` | `marvelled` |
  | 60:1 | `five hundred` | `500` |
  | 61:10, 71:7 | `Cherubic` | `Cherubin` |
  | 65:6, 81:9, 95:2, 104:10 | `practice` | `practise` |
  | 69:2 | `Sîmâpêsîêl`, `Tûmâêl`, `Rumâêl` | `Simâpêsîêl`, `Tumâêl`, `Rûmâêl` |
  | 69:8 | `Pênêmûe` | `Pênemûe` |
  | 69:12 | `Tabââ'ĕt` | `Tabâ'ět` |
  | 69:23 | `hoarfrost` | `hoar frost` |
  | 81:6, 106:7, 106:12 | `mayest` | `mayst` |
  | 82:17 | `Hîlûjâsĕph` | `Hîlujâseph` |
  | 82:18 | `Hêl'emmêlêk` | `Hel'emmêlêk` |
  | 82:20 | `Gîdâ'îjal` | `Gîdâ'ijal` |
  | 99:9 | `worshiped` | `worshipped` |
  | 103:6 | `And how they have died` | `And now they have died` |
  | 104:4 | `cast not away your hopes` | `your hope` |

  Charles, writing in London, more likely printed `counsellor`, `marvelled`,
  `practise` and `worshipped`; the source's spellings are kept because there is
  no scan to check against and they are the one citable copy.

A third copy — the four 1 Enoch files in
[`TheoryofShadows/The-Book`](https://github.com/TheoryofShadows/The-Book)
(`docs/data/works/1-enoch-*.json`, commit `3c06d91`) — shares its ancestry
with the source (it has the same `Why as one`, `Eternal Kin` and `had beer`),
so it could not serve as an independent witness. It was used to supply 44:1
and to confirm which readings the common ancestor had.

## What is not here

- **Charles's introduction, chapter headings and notes.** The 1917 edition has
  an introduction by W. O. E. Oesterley, a heading over every section and
  footnotes on the text; only the translation is here.
- **2 Enoch and 3 Enoch.** The Slavonic (2 Enoch) and Hebrew (3 Enoch) books
  are different works; only the Ethiopic 1 Enoch is "the Book of Enoch".
- **The original languages.** 1 Enoch survives whole only in Ge'ez, with the
  Greek of chapters 1–32 and 97–107, Aramaic fragments from Qumran and a little
  Latin. All four are openly available in the Online Critical Pseudepigrapha
  file named above (CC BY 4.0); the Ge'ez is also in
  [`LPettay/ethiopian-bible`](https://github.com/LPettay/ethiopian-bible) from
  Beta maṣāḥǝft (CC BY-SA 4.0) and in
  [`geezorg/ebooks`](https://github.com/geezorg/ebooks) (CC BY-SA 4.0).

## Rebuilding

```sh
git clone --depth 1 --branch 2024 https://github.com/scrollmapper/bible_databases_deuterocanonical src/scrollmapper-2024
python3 tools/build_1enoch.py src/scrollmapper-2024/txt/1-enoch/1-enoch.txt .
python3 tools/verify.py
```

The build reads the file at commit `97e883a`; if the branch moves and the text
changes, one of the repairs will stop matching and the script will say which.
