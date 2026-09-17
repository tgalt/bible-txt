# bible-txt

Bible text and study notes.

## Contents

- **[`kjv/`](kjv)** — the complete King James Version in plain text: the whole
  Bible in [`kjv/kjv.txt`](kjv/kjv.txt), plus one file per book under
  [`kjv/books/`](kjv/books). One verse per line, prefixed with its reference, so
  it can be read or grepped directly:

  ```sh
  grep '^John 3:16 ' kjv/kjv.txt
  ```

  See [`kjv/README.md`](kjv/README.md) for the format, the source it was built
  from, and how it was verified.

- **[`original-languages/`](original-languages)** — Hebrew and Greek behind the
  KJV, in the same line format so the references line up:

  ```sh
  grep '^John 3:16 ' kjv/kjv.txt
  grep '^John 3:16 ' original-languages/greek/tr-scrivener.txt
  ```

  The Hebrew Old Testament with lemmas and morphology, six editions of the
  Greek New Testament (including Scrivener's Textus Receptus, the text the KJV
  translators worked from), Strong's dictionaries, Brown-Driver-Briggs, Dodson,
  and a word-level interlinear. Every word carries its Strong's number, and
  every Strong's entry lists how the KJV renders it.

  See [`original-languages/README.md`](original-languages/README.md) for the
  sources, their licences, and what is deliberately left out.

- **[`enoch/`](enoch)** — 1 Enoch, the Ethiopic Book of Enoch, in R. H.
  Charles's 1917 translation, in the same line format: 108 chapters, 1,063
  verses in [`enoch/1-enoch.txt`](enoch/1-enoch.txt). Not in the KJV or any
  Western canon, but quoted in Jude 14–15:

  ```sh
  grep '^1 Enoch 1:9 ' enoch/1-enoch.txt
  grep '^Jude 1:1[45] ' kjv/kjv.txt
  ```

  See [`enoch/README.md`](enoch/README.md) for the source, what was repaired
  in it, and how the text was checked against a second transcription and the
  Ethiopic.

### Study notes

- [`jude-bible-study-outline.md`](jude-bible-study-outline.md) — study guide for the book of Jude
- [`nicolaitans-explanation.md`](nicolaitans-explanation.md) — background on the Nicolaitans
- [`faith-vs-works-living-christian-letter.txt`](faith-vs-works-living-christian-letter.txt) — notes on faith and works
- [`fasting-in-the-bible.md`](fasting-in-the-bible.md) — what Scripture says about fasting, how it was practised, and where it fits in a Christian life
- [`jewish-holidays-2026-2027.md`](jewish-holidays-2026-2027.md) — every Jewish festival, fast, and observance in 2026 and 2027, with Hebrew dates and the evening each begins
- [`praying-for-the-dead.md`](praying-for-the-dead.md) — what Scripture says about praying for the dead, how the practice arose and why the churches divided over it, and what a grieving Christian can pray
- [`once-saved-always-saved.md`](once-saved-always-saved.md) — whether a Christian can be finally lost: the security texts and the warning passages side by side, how the traditions from Augustine to Dort to Wesley have answered, and how the New Testament says you can know where you stand
- [`if-any-would-not-work.md`](if-any-would-not-work.md) — 2 Thessalonians 3:10, the one verse that says the unwilling should not eat: what the Greek requires, how narrow the rule is, the texts about the poor that stand alongside it, and what nineteen centuries of use and misuse have shown about applying it
