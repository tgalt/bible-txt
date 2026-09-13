# Interlinear

A word-level Greek-English interlinear of the New Testament: every Greek word
with its transliteration, parsing, Strong's number and English rendering.

| File | Contents |
| --- | --- |
| [`nt-interlinear.tsv`](nt-interlinear.tsv) | 140,147 words across 7,953 verses |

```
reference	n	greek	transliteration	parsing	strongs	english
John 3:16	1	Οὕτως	outwv	ADV	G3779	so
John 3:16	2	γὰρ	gar	CONJ	G1063	For
John 3:16	3	ἠγάπησεν	hgaphsen	V-AAI-3S	G0025	loved
John 3:16	4	ὁ	o	T-NSM	G3588	-
John 3:16	5	θεὸς	qeov	N-NSM	G2316	God
```

Words are numbered in **Greek** word order, not English. The source table is
laid out in English reading order; the build restores the Greek order from the
table's own sort key. An `english` value of `-` marks a Greek word the
translation leaves unrendered, usually the article.

The transliteration is ASCII beta code as the source gives it, not a
pronunciation guide.

## What the English is

The English is the **Majority Standard Bible**, not the KJV, and the Greek
underlying it is the Byzantine/Majority text — which is why the verse count
matches [`../greek/byzantine.txt`](../greek/byzantine.txt) exactly rather than
the KJV's 7,957.

That makes this a good gloss for reading the Greek, and a reasonable proxy for
the KJV's text tradition, since the Byzantine text and the Textus Receptus are
close. It is not a KJV interlinear. For the KJV's own wording, join on the
Strong's number to `kjv_usage` in
[`../lexicons/strongs-greek.tsv`](../lexicons/strongs-greek.tsv).

Only the New Testament is here. The equivalent Old Testament table is published
by the Berean Bible at `bereanbible.com/bsb_tables.tsv`, also public domain.

## Provenance

Built by [`../tools/build_interlinear.py`](../tools/build_interlinear.py) from
the Majority Standard Bible translation table in
[`BSB-publishing/bsb2usfm`](https://github.com/BSB-publishing/bsb2usfm) at
commit `78c59ad`. The Berean and Majority Standard Bible texts are in the
**public domain**; the repo's tooling is MIT.

### Verification

`../tools/verify.py` reports 140,147 words across 7,953 verses, of which 5,376
of the 5,377 distinct Strong's numbers resolve in
[`../lexicons/strongs-greek.tsv`](../lexicons/strongs-greek.tsv). The one that
does not is `G0000`, the source's placeholder for a word it assigns no number
to — fourteen words, mostly numerals.
