# Lexicons

| File | Contents | Entries |
| --- | --- | ---: |
| [`strongs-hebrew.tsv`](strongs-hebrew.tsv) | Strong's Hebrew and Aramaic dictionary (1890) | 8,674 |
| [`strongs-greek.tsv`](strongs-greek.tsv) | Strong's Greek dictionary (1890) | 5,523 |
| [`bdb.tsv`](bdb.tsv) | Brown-Driver-Briggs Hebrew and English Lexicon (1906) | 11,845 |
| [`dodson-greek.tsv`](dodson-greek.tsv) | Dodson's Greek lexicon | 5,410 |

All four are tab-separated with a header row, one entry per line, so they grep
and `join` cleanly. Definitions that run to paragraphs in print are flattened
to a single line.

## Strong's

Keyed by the same padded numbers the texts use, so they join directly:

```sh
grep '^G0026	' strongs-greek.tsv
```

```
strongs	word	transliteration	derivation	definition	kjv_usage
G0026	ἀγάπη	agápē	from G25 (ἀγαπάω);	love, i.e. affection or benevolence…	(feast of) charity(-ably), dear, love
```

The `kjv_usage` column is the useful one for this repo. Strong's was compiled
from the KJV, so that field lists every way the KJV renders the word — `G0025`
ἀγαπάω gives `(be-)love(-ed)`. It is the closest thing here to a word-level
bridge between [`../../kjv/kjv.txt`](../../kjv/kjv.txt) and the Greek and
Hebrew, and it runs in both directions: grep it to find which numbers the KJV
translates with a given English word.

The Hebrew table adds `pronunciation`, `part_of_speech` and `language` — `heb`
or `arc`, the latter marking the Aramaic portions of Daniel and Ezra.

Homonyms: OSHB writes `H1254a` where the lexicon has `H1254`. Strip a trailing
letter before looking a number up.

## Brown-Driver-Briggs

The standard scholarly Hebrew lexicon, keyed by BDB's own entry ids and cross
referenced to Strong's where the mapping exists:

```
bdb_id	strongs	headword	type	entry
a.ab.ab	H0003	אֵב		[אֵב] n.[m.] freshness, fresh green (Lag BN 207…
```

BDB is organised by root, so `type=root` marks a root entry and the ids sort
into its family. About 8,800 of the entries carry a Strong's number; the rest
are roots, cross-references and sub-entries Strong's does not number
separately. A handful map to an inseparable particle (`b`, `c`, `d`, `k`, `l`,
`m`, `s`, `i`) rather than a number, and are recorded that way.

Flattening loses BDB's typography — its nested senses, small caps and citation
formatting all become running text. For close work, consult the source markup.

## Dodson

A concise Greek lexicon with a short and a longer gloss per word, keyed to
Strong's. Useful when Strong's own definitions, which are terse and Victorian,
are not enough.

## Provenance

Built by [`../tools/build_lexicons.py`](../tools/build_lexicons.py) from:

| Source | Commit | Licence |
| --- | --- | --- |
| [`openscriptures/HebrewLexicon`](https://github.com/openscriptures/HebrewLexicon) | `21c9add` | CC BY 4.0 (texts themselves public domain) |
| [`openscriptures/strongs`](https://github.com/openscriptures/strongs) | `0acd2f2` | CC BY-SA on the JSON conversion; Strong's 1890 is public domain |
| [`biblicalhumanities/Dodson-Greek-Lexicon`](https://github.com/biblicalhumanities/Dodson-Greek-Lexicon) | `74f7035` | Public domain |

Strong's Hebrew here comes from `HebrewStrong.xml` in the HebrewLexicon repo,
which carries structured fields; the Greek comes from the JSON in
`openscriptures/strongs`. Credit the Open Scriptures Hebrew Bible Project for
the Hebrew markup.

For fuller lexicons — the Tyndale brief lexicons, and full Liddell-Scott-Jones
entries for biblical words — see STEPBible via [`../fetch-more.sh`](../fetch-more.sh).
Abbott-Smith's *Manual Greek Lexicon* is fetched by the same script.
