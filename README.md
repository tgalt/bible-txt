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

### Study notes

- [`jude-bible-study-outline.md`](jude-bible-study-outline.md) — study guide for the book of Jude
- [`nicolaitans-explanation.md`](nicolaitans-explanation.md) — background on the Nicolaitans
- [`faith-vs-works-living-christian-letter.txt`](faith-vs-works-living-christian-letter.txt) — notes on faith and works
