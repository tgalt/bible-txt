# Greek New Testament

Six editions. They differ because the manuscript evidence differs, and the
differences are the point: the Textus Receptus is what the KJV translators
worked from, the SBLGNT and Nestle are what most modern translations follow,
and comparing them shows where the KJV's wording comes from.

| Edition | File | Verses | Words | Tagged | Accents |
| --- | --- | ---: | ---: | --- | --- |
| Scrivener 1894 Textus Receptus | [`tr-scrivener.txt`](tr-scrivener.txt) | 7,957 | 140,658 | Strong's + morphology | no |
| CNTR KJTR | [`kjtr.txt`](kjtr.txt) | 7,957 | 140,591 | lemma + extended Strong's | yes |
| Robinson-Pierpont 2018 | [`byzantine.txt`](byzantine.txt) | 7,953 | 140,149 | Strong's + morphology | yes |
| SBLGNT | [`sblgnt.txt`](sblgnt.txt) | 7,939 | 137,554 | lemma + parse (MorphGNT) | yes |
| Nestle 1904 | [`nestle1904.txt`](nestle1904.txt) | 7,943 | 137,779 | Strong's + morphology | yes |
| CNTR SR | [`sr.txt`](sr.txt) | 7,957 | 137,361 | lemma + extended Strong's | yes |

Each `<name>.txt` has a matching `<name>-words.tsv` with one row per word.

## Which one do you want?

- **Reading behind the KJV**: `tr-scrivener.txt`, or `kjtr.txt` if you want
  accents. John 3:16 in the TR reads τὸν υἱὸν **αὐτοῦ** τὸν μονογενῆ, which is
  why the KJV has *"his only begotten Son"*; the SBLGNT has no αὐτοῦ.
- **Looking up a word**: any of the four Strong's-tagged files. `tr-scrivener`
  is the one keyed to the text the KJV translates.
- **Comparing against a modern translation**: `sblgnt.txt` or `nestle1904.txt`.
- **Earliest recoverable text**: `sr.txt`.

## Format

Reading texts use the repo's line format. Word tables are tab-separated:

```
reference	n	word	strongs	morphology	tvm_code
John 1:1	1	εν	G1722	PREP
John 1:1	3	ην	G1510	V-IAI-3S	5707
```

`tvm_code` is the Online Bible tense/voice/mood number that the Robinson and
Nestle sources append to verbs; the `morphology` column already carries the
same information in readable form, and the column is empty for everything else.

The `kjtr` and `sr` tables use CNTR's own columns: `lemma`, `extended_strongs`
(CNTR's five-digit scheme, **not** Strong's numbers), `role` and `morphology`.

Two markers come through from the sources: `¶` starts a paragraph in the
Byzantine, KJTR and SR texts, and `˚` marks a divine name in the SR.

## The Textus Receptus conversion

ByzTxt publishes Robinson's parsed Textus Receptus as unaccented ASCII beta
code, so `tr-scrivener.txt` is machine-converted by
[`../tools/betacode.py`](../tools/betacode.py) and is **unaccented**. Use
`kjtr.txt` for an accented text of the same tradition.

That source also marks variants as two alternatives fenced by three standalone
pipes — `| euron 2147 {V-2AAI-3P} | eidon 3708 {V-2AAI-3P} |` — across 246
verses. Which alternative is the Textus Receptus is not documented upstream,
but it is decidable: taking the second reproduces the independently produced
CNTR KJTR reading in 62% of affected verses against 21% for the first. So the
second is taken as the Receptus reading and the first as the Byzantine one.
Matthew 2:11 accordingly reads εἶδον, matching the KJV's *"they saw"*, and
Revelation 7:10 keeps τῷ θεῷ ἡμῶν, matching *"to our God"*.

Nothing is discarded: every dropped alternative is recorded in
[`tr-variants.tsv`](tr-variants.tsv), 261 readings in all.

```
reference	byzantine_reading	receptus_reading
Matthew 2:11	ευρον	ειδον
Matthew 2:23	ναζαρετ	ναζαρεθ
```

## Versification

The New Testament lines up with the KJV far better than the Old does. Against
the KJV's 7,957 verses:

| Edition | Shared | Only here | Only in KJV |
| --- | ---: | ---: | ---: |
| Scrivener TR | 7,957 | 0 | 0 |
| CNTR KJTR | 7,955 | 2 | 2 |
| CNTR SR | 7,955 | 2 | 2 |
| Byzantine RP2018 | 7,950 | 3 | 7 |
| Nestle 1904 | 7,940 | 3 | 17 |
| SBLGNT | 7,937 | 2 | 20 |

The Textus Receptus matches the KJV's versification exactly, which is what you
would expect of the text it was translated from. The verses "only in KJV" for
the critical editions are the passages those editions judge later additions and
omit — Matthew 17:21, 18:11, 23:14, Mark 7:16 and the rest.

## Provenance

Built by [`../tools/build_greek.py`](../tools/build_greek.py) from:

| Edition | Source | Commit | Licence |
| --- | --- | --- | --- |
| Scrivener TR | [`byztxt/greektext-textus-receptus`](https://github.com/byztxt/greektext-textus-receptus) | `7fd4d02` | Public domain |
| Byzantine | [`byztxt/byzantine-majority-text`](https://github.com/byztxt/byzantine-majority-text) | `27a45ff` | Public domain (Unlicense) |
| SBLGNT | [`LogosBible/SBLGNT`](https://github.com/LogosBible/SBLGNT) | `c4d241a` | CC BY 4.0 |
| MorphGNT parse | [`morphgnt/sblgnt`](https://github.com/morphgnt/sblgnt) | `aaed91e` | **CC BY-SA 3.0** |
| Nestle 1904 | [`biblicalhumanities/Nestle1904`](https://github.com/biblicalhumanities/Nestle1904) | `713f28a` | Public domain |
| CNTR SR | [`Center-for-New-Testament-Restoration/SR`](https://github.com/Center-for-New-Testament-Restoration/SR) | `4be18e6` | CC BY 4.0 |
| CNTR KJTR | [`Center-for-New-Testament-Restoration/KJTR`](https://github.com/Center-for-New-Testament-Restoration/KJTR) | `2af135d` | CC BY 4.0 |

Attribution: the SBLGNT is copyright 2010 the Society of Biblical Literature and
Logos Bible Software; the SR and KJTR are by Alan Bunning, Center for New
Testament Restoration; the Byzantine and Textus Receptus texts are Maurice A.
Robinson's, maintained by Ulrik Sandborg-Petersen.

`sblgnt-words.tsv` is **CC BY-SA 3.0**, unlike everything else here: a
derivative of that file has to carry the same licence. The SBLGNT text itself
is CC BY 4.0, relicensed from a restrictive EULA in December 2022.

### What is not included

- **No apparatus.** SBLGNT sigla marking where its apparatus discusses a
  variant (`⸀⸂⸃` and the rest) are stripped from the reading text.
- **Two files skipped** from the Byzantine source: `PA`, a separate copy of the
  pericope adulterae, and `ACT24`, an alternative text of Acts.

### Verification

`../tools/verify.py` checks that every line parses to a known book, chapter and
verse and that no verse is empty, and reports:

- The counts in the tables above.
- Scrivener TR against CNTR KJTR, ignoring accents and punctuation: 7,241 of
  7,955 verses identical (91.0%), 136,699 of 140,914 words agreeing (97.0%).
  The residue is genuine disagreement between two reconstructions of the same
  tradition — Δαβίδ against Δαυίδ 54 times, Μωσῆς against Μωϋσῆς, the numeral
  ιβ against δώδεκα.
- Zero converted word forms containing a non-Greek character, which is the
  check on the beta-code conversion.
- Every distinct Strong's number used by the TR (5,401), Byzantine (5,380) and
  Nestle 1904 (5,331) tables resolves in
  [`../lexicons/strongs-greek.tsv`](../lexicons/strongs-greek.tsv).
