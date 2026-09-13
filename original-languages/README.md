# Original languages

Hebrew and Greek resources for reading behind the KJV, in the same plain-text
line format as [`kjv/`](../kjv). Every file here is built from an openly
licensed source by a script in [`tools/`](tools), and every source is named
below with its licence.

## Layout

| Path | Contents |
| --- | --- |
| [`hebrew/`](hebrew) | The Hebrew Old Testament (Westminster Leningrad Codex) with lemmas and morphology |
| [`greek/`](greek) | Six editions of the Greek New Testament, four of them tagged with Strong's numbers |
| [`lexicons/`](lexicons) | Strong's Hebrew and Greek dictionaries, Brown-Driver-Briggs, Dodson |
| [`interlinear/`](interlinear) | A word-level Greek-English interlinear of the New Testament |
| [`tools/`](tools) | The build and verification scripts |
| [`fetch-more.sh`](fetch-more.sh) | Fetches the open resources this repo does not vendor |

The whole tree is about 84 MB.

## Format

Reading texts use the repo's line format, so they grep exactly like
[`kjv/kjv.txt`](../kjv/kjv.txt) and the references line up:

```sh
grep '^John 3:16 ' ../kjv/kjv.txt
grep '^John 3:16 ' greek/tr-scrivener.txt
```

Word-level data is tab-separated with a header row, keyed by the same
reference plus a word number:

```
reference	n	word	strongs	morphology	tvm_code
John 1:1	1	εν	G1722	PREP
John 1:1	2	αρχη	G0746	N-DSF
```

Strong's numbers are written zero-padded with their language prefix — `H0430`,
`G2424` — everywhere, in the texts and in the lexicons alike, so the two join
directly. Looking up every Greek word of a verse:

```sh
join -t"$(printf '\t')" -1 4 -2 1 \
  <(grep '^John 1:1	' greek/tr-scrivener-words.tsv | sort -k4,4) \
  <(sort -k1,1 lexicons/strongs-greek.tsv)
```

Unlike the KJV corpus, these files are **not ASCII** — Hebrew and Greek need
Unicode, and the Hebrew is right-to-left, which will look scrambled in editors
that do not handle bidirectional text.

## What is here, and under what licence

### Hebrew Old Testament

| Resource | Licence |
| --- | --- |
| Westminster Leningrad Codex text | Public domain |
| Open Scriptures Hebrew Bible lemma and morphology tagging | CC BY 4.0 |

From [`openscriptures/morphhb`](https://github.com/openscriptures/morphhb) at
commit `3d15126`. See [`hebrew/README.md`](hebrew/README.md).

### Greek New Testament

| Edition | What it is | Licence |
| --- | --- | --- |
| Scrivener 1894 Textus Receptus | The Greek behind the KJV, parsed, with Strong's numbers | Public domain |
| CNTR KJTR | A reconstruction of the Greek implied by the 1769 KJV | CC BY 4.0 |
| Robinson-Pierpont 2018 | Byzantine/Majority text, parsed, with Strong's numbers | Public domain |
| SBLGNT | Critically edited modern text | CC BY 4.0 |
| MorphGNT | Morphological parse of the SBLGNT | CC BY-SA 3.0 |
| Nestle 1904 | Early critical text, with Strong's numbers and lemmas | Public domain |
| CNTR SR | Statistical restoration from the earliest manuscripts | CC BY 4.0 |

Sources: [`byztxt/greektext-textus-receptus`](https://github.com/byztxt/greektext-textus-receptus)
`7fd4d02`, [`byztxt/byzantine-majority-text`](https://github.com/byztxt/byzantine-majority-text)
`27a45ff`, [`LogosBible/SBLGNT`](https://github.com/LogosBible/SBLGNT) `c4d241a`,
[`morphgnt/sblgnt`](https://github.com/morphgnt/sblgnt) `aaed91e`,
[`biblicalhumanities/Nestle1904`](https://github.com/biblicalhumanities/Nestle1904) `713f28a`,
[`Center-for-New-Testament-Restoration/SR`](https://github.com/Center-for-New-Testament-Restoration/SR) `4be18e6`,
[`Center-for-New-Testament-Restoration/KJTR`](https://github.com/Center-for-New-Testament-Restoration/KJTR) `2af135d`.
See [`greek/README.md`](greek/README.md).

Note that MorphGNT's parse is **CC BY-SA 3.0**, the one share-alike licence in
this tree: a derivative of `sblgnt-words.tsv` has to carry the same licence.
The SBLGNT text itself is CC BY 4.0 — it was relicensed from a restrictive
EULA in December 2022, and a good deal of writing about it is still out of date
on that point.

### Lexicons

| Resource | Licence |
| --- | --- |
| Strong's Hebrew and Greek dictionaries (1890) | Public domain; the digitisations are CC BY 4.0 / CC BY-SA |
| Brown-Driver-Briggs (1906) | Public domain; the markup is CC BY 4.0 |
| Dodson's Greek lexicon | Public domain |

Sources: [`openscriptures/HebrewLexicon`](https://github.com/openscriptures/HebrewLexicon)
`21c9add`, [`openscriptures/strongs`](https://github.com/openscriptures/strongs)
`0acd2f2`, [`biblicalhumanities/Dodson-Greek-Lexicon`](https://github.com/biblicalhumanities/Dodson-Greek-Lexicon)
`74f7035`. See [`lexicons/README.md`](lexicons/README.md).

### Interlinear

The Majority Standard Bible translation table, which pairs every Greek word of
the New Testament with a transliteration, parsing, Strong's number and English
rendering. Public domain, from
[`BSB-publishing/bsb2usfm`](https://github.com/BSB-publishing/bsb2usfm) `78c59ad`.
See [`interlinear/README.md`](interlinear/README.md).

## Not vendored

[`fetch-more.sh`](fetch-more.sh) downloads these into `external/`. They are all
open; they are just not a good fit for committing here.

- **STEPBible** ([TAHOT, TAGNT and friends](https://github.com/STEPBible/STEPBible-Data),
  CC BY 4.0) — word-by-word Hebrew and Greek with translations, grammar and,
  for the New Testament, a marker on every word saying which editions carry
  it, including `K` for "the Greek the KJV translators used". Also the Tyndale
  brief lexicons, full LSJ entries for biblical words, and **TVTMS**, a mapping
  between versification traditions, which is the thing to reach for when the
  Hebrew and the KJV disagree about verse numbers. The licence permits
  redistribution, but the data asks that STEPBible stay the single point of
  distribution, so this repo links rather than copies.
- **MACULA** ([Hebrew](https://github.com/Clear-Bible/macula-hebrew),
  [Greek](https://github.com/Clear-Bible/macula-greek), CC BY 4.0) — syntax
  trees, semantic roles, UBS MARBLE word senses, participant reference. Left
  out for size.
- **ETCBC BHSA** ([`ETCBC/bhsa`](https://github.com/ETCBC/bhsa)) — the richest
  syntactic database of the Hebrew Bible. The tooling is MIT but **the data is
  CC BY-NC 4.0**, which does not match the rest of this tree; keep it separate
  and check the terms before redistributing.
- **unfoldingWord** UHB and UGNT (CC BY-SA 4.0) — tagged and parsed Hebrew and
  Greek in USFM, with alignment data. Hosted on Door43, not GitHub.
- **Swete's Septuagint** ([`eliranwong/LXX-Swete-1930`](https://github.com/eliranwong/LXX-Swete-1930),
  CC BY-SA 4.0).
- **Abbott-Smith** ([TEI XML](https://github.com/translatable-exegetical-tools/Abbott-Smith),
  public domain) — left out because the checkout is mostly a large scan.
- **Sefaria** ([`Sefaria/Sefaria-Export`](https://github.com/Sefaria/Sefaria-Export))
  — Hebrew Tanakh with the Jewish commentary tradition. Licences vary per text;
  the text data is a ~26 GB bucket.

## Gaps worth knowing about

- **There is no openly licensed KJV tagged with Strong's numbers here.** Strong's
  Concordance was compiled from the KJV, so a word-level English-to-Strong's
  map for it plainly exists — CrossWire's KJV2006 OSIS module is the canonical
  one — but the copies that are easy to find on GitHub are either scraped with
  no licence at all or have had the tags stripped on export. What this repo
  gives you instead is the other direction, which is well licensed and just as
  usable: every Hebrew and Greek word carries its Strong's number, and the
  Strong's entries themselves carry a `kjv_usage` field listing how the KJV
  renders that word.
- **Versification does not line up in the Old Testament.** See
  [`hebrew/README.md`](hebrew/README.md).
- **No apparatus.** These are reading texts. The variants that ByzTxt marks in
  the Textus Receptus are kept in `greek/tr-variants.tsv`, but nothing else
  here carries a critical apparatus; STEPBible's TAGNT does.
- **No Apocrypha**, matching [`kjv/`](../kjv).

## Rebuilding

```sh
git clone --depth 1 https://github.com/openscriptures/morphhb.git src/morphhb
# ...and the other sources listed above, into src/
python3 tools/build_hebrew.py      src/morphhb .
python3 tools/build_greek.py       src greek
python3 tools/build_lexicons.py    src lexicons
python3 tools/build_interlinear.py src/bsb2usfm/temp/msb_nt_tables.tsv interlinear
python3 tools/verify.py ..
```

`tools/verify.py` prints the report quoted in the per-directory READMEs: it
checks that every reference parses and no verse is empty, counts everything,
compares each corpus against the KJV's versification, and confirms that the
Strong's numbers used by the texts resolve in the lexicons.
