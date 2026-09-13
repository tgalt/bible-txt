# Hebrew Old Testament

The Westminster Leningrad Codex — the standard digital edition of the Masoretic
Text, following the Leningrad Codex of 1008 CE — with the Open Scriptures
Hebrew Bible's lemma and morphology tagging.

| File | Contents |
| --- | --- |
| [`wlc.txt`](wlc.txt) | Pointed Hebrew, one verse per line, 23,213 verses |
| [`wlc-words.tsv`](wlc-words.tsv) | One row per word, 305,507 words |

## Format

`wlc.txt` follows the repo's line format, with vowel points and cantillation
marks as the source carries them:

```
Genesis 1:1 בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃
```

A maqqef joins the words it hyphenates (`עַל־פְּנֵי`), a paseq stands separated
(`יְהוָה ׀ אֶחָד`), and the sof pasuq closes the verse. Enlarged, small and
suspended letters — the ע of שְׁמַע and the ד of אֶחָד at Deuteronomy 6:4 — are
present as ordinary letters; plain text cannot carry their size.

`wlc-words.tsv` adds the analysis:

```
reference	n	word	strongs	oshb_lemma	morphology
Genesis 1:1	1	בְּ/רֵאשִׁ֖ית	H7225	b/7225	HR/Ncfsa
Genesis 1:1	2	בָּרָ֣א	H1254a	1254 a	HVqp3ms
Genesis 1:1	3	אֱלֹהִ֑ים	H0430	430	HNcmpa
```

The `/` in the word and morphology columns divides a word into its morphemes:
`בְּ/רֵאשִׁית` is the preposition בְּ plus the noun רֵאשִׁית, parsed `HR/Ncfsa`
as preposition plus common noun, feminine singular absolute. The reading text
in `wlc.txt` has these dividers removed.

`oshb_lemma` is OSHB's own lemma, which prefixes inseparable particles with a
letter (`b` = בְּ, `c` = וְ, `d` = הַ, `k` = כְּ, `l` = לְ, `m` = מִן, `s` = שֶׁ)
and disambiguates homonyms with a trailing one (`1254 a`). `strongs` is that
normalised to the padded form used across this tree; the homonym letter is
kept, so `H1254a` looks up as `H1254` in
[`../lexicons/strongs-hebrew.tsv`](../lexicons/strongs-hebrew.tsv).

## Versification

**Hebrew verse numbers do not line up with the KJV's.** Of 23,213 Hebrew verses
and 23,145 KJV Old Testament verses, 23,011 references are shared; 202 exist
only in the Hebrew and 134 only in the KJV. Three causes, in order of size:

- **Psalm superscriptions.** In the Hebrew, *"A Psalm of David"* is verse 1, so
  the rest of the psalm is shifted by one. The KJV prints the superscription
  unnumbered above the psalm. This alone accounts for 66 verses. `Psalms 23:1`
  here is מִזְמוֹר לְדָוִד; in [`../../kjv/kjv.txt`](../../kjv/kjv.txt) it is
  *"The LORD is my shepherd"*.
- **Different chapter divisions.** Joel is 4 chapters in the Hebrew and 3 in
  the KJV; Malachi is 3 and 4. Both renumber wholesale (21 and 6 verses).
- **Verses split differently at a chapter boundary**, chiefly in Numbers (17),
  1 Chronicles (16), 1 Kings (15), Nehemiah, Job, Leviticus.

So a reference cannot be carried across blindly. For a full mapping, STEPBible's
TVTMS dataset covers this directly — see
[`../fetch-more.sh`](../fetch-more.sh). OSHB also ships `wlc/VerseMap.xml`.

## What this text does and does not include

- **Ketiv and qere are not distinguished.** The word given is the one OSHB
  prints in the running text; the marginal reading is in an apparatus note that
  this conversion drops.
- **No apparatus, no notes.** OSHB carries 4,499 editorial notes recording where
  it reads the Leningrad Codex differently from BHS; none are here.
- **Section markers are kept.** A trailing `ס` or `פ` marks a closed or open
  paragraph in the Masoretic layout, as at Isaiah 9:6.
- **Not ASCII, and right-to-left.**

## Provenance

Built by [`../tools/build_hebrew.py`](../tools/build_hebrew.py) from
[`openscriptures/morphhb`](https://github.com/openscriptures/morphhb) at commit
`3d15126fb1ef74867fc1434be1942e837932691f`, which publishes the WLC as OSIS XML.

The WLC text is in the public domain. The lemma and morphology data is
licensed **CC BY 4.0**; credit the Open Scriptures Hebrew Bible Project.

### Verification

`../tools/verify.py` checks that every line parses to a known book, chapter and
verse and that no verse is empty, and reports:

- 23,213 verses, 305,507 words, across all 39 books.
- Every one of the 9,248 distinct Strong's numbers used resolves in
  [`../lexicons/strongs-hebrew.tsv`](../lexicons/strongs-hebrew.tsv).
