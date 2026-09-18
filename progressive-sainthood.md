# Progressive Sainthood
## Holiness Given and Holiness Grown: What Scripture Means by "Saint," How a Saint Is Made Over a Lifetime, and What the Churches Did With the Word

---

## How to Use This Document

### What "progressive sainthood" means

Two different things travel under that phrase, and this document covers both, because they turn out to be the same question asked from opposite ends.

**The first is biblical.** The New Testament calls every believer a saint — from the beginning, before any achievement, including believers it is about to rebuke. And then it spends the rest of its pages telling saints to become holy. The same letter that greets the Corinthians as "sanctified in Christ Jesus, called to be saints" goes on to accuse them of incest, lawsuits, drunkenness at the Lord's table, and faction. Sainthood in Scripture is therefore a status conferred in a moment *and* a character formed over a lifetime *and* a completion granted at the end. That threefold shape — given, grown, finished — is what most Christian traditions call sanctification, and it is what this document means by progressive sainthood in its primary sense. **Part I.**

**The second is institutional.** In the Roman Catholic Church a person becomes a saint through a process with named stages: Servant of God, then Venerable, then Blessed, then Saint. That is progressive sainthood in the most literal sense — sainthood advanced by degrees through a procedure, each stage with its own evidentiary bar. The Orthodox churches do something related and call it glorification. **Part II.**

The two senses are joined by a history. The word that the apostles used for every Christian alive became, over roughly four centuries, a title for a few Christians dead. Part II traces how that happened, what was gained and lost in it, and how each tradition describes the growth itself — infused grace and merit, *theosis*, mortification and vivification, entire sanctification, the higher life.

**Part III** is the practical payoff: whether you are a saint, how to tell whether you are growing, why mature Christians usually think they are getting worse, what to do when there is no progress at all, and what finally finishes the work.

### The source of the quotations

Scripture is quoted from the **King James Version (1769)**, the text carried in [`kjv/`](kjv) in this repository. Every quotation was taken from that file, so any verse can be checked at its source:

```sh
grep '^Hebrews 10:14 ' kjv/kjv.txt
```

Every count in this document was made from those files rather than from memory, and the command that produced it is given so you can re-run it. The word *saints* appears in 95 verses of the KJV — 34 in the Old Testament, 61 in the New:

```sh
grep -cw 'saints' kjv/kjv.txt
```

Greek and Hebrew are cited from [`original-languages/`](original-languages) with Strong's numbers, and where the tense of a verb carries the argument — and in this subject it constantly does — the parsing comes from the interlinear there:

```sh
grep '^Hebrews 10:14	' original-languages/interlinear/nt-interlinear.tsv
grep '^G0037	' original-languages/lexicons/strongs-greek.tsv
```

Where the KJV's English has drifted far enough to mislead, the modern sense is given in brackets or in the comment around it — *conversation* (1 Peter 1:15) means conduct, the whole manner of life; *concupiscence* is craving; *mortify* (Colossians 3:5) means put to death; *charity* is love; *peculiar* (1 Peter 2:9) means belonging to someone, not odd; *perfect* usually renders a word meaning complete or mature rather than flawless; *simplicity*, *temperance*, *longsuffering*, and *meekness* all mean roughly what an English reader now calls single-mindedness, self-control, patience, and gentleness; *prevent* means go before; *let* can mean hinder; *wants* means lacks.

### A note on one word family

English hides the argument. In Greek, *saint*, *holy*, *sanctify*, *sanctification*, and *holiness* are all one root — ἅγιος (*hagios*) and its relatives. A saint is simply a holy one; to sanctify is to make holy; sanctification is holy-making. The English reader meets four unrelated-looking words where Paul wrote one family, and so the connection that carries the whole doctrine — *the saints are the sanctified, and the sanctified are being sanctified* — is nearly invisible in translation. Keeping that family in view is most of the work of Part I. The full inventory is in [Appendix C](#c-the-holiness-word-families).

### A note on the names

*Sanctification* is the standard term, but the traditions divide it differently, and the divisions matter more than the word. This document uses:

- **Definitive (or positional) sanctification** — the once-for-all setting apart that happens when a person is joined to Christ. Past tense, complete, not a matter of degree.
- **Progressive sanctification** — the lifelong, uneven, Spirit-worked, effort-involving growth in actual holiness. Present tense, incomplete, entirely a matter of degree.
- **Final sanctification (glorification)** — the completion of the work at Christ's appearing. Future tense, instantaneous, universal among the saved.

Not every tradition slices it this way. Roman Catholic theology folds the first into justification itself and describes the second as an increase of the grace already infused; Eastern Orthodoxy resists the separation altogether and speaks of one movement, *theosis*; Lutherans insist on keeping justification and sanctification distinct precisely so that the first is never made to depend on the second; Wesleyans add a decisive second work within the progressive stage. Where a tradition would object to the framing, [Part II](#part-ii--what-the-church-did-with-the-word) says so in its own words.

### A note on what this document is not

This is a study of the biblical and historical material, not a ruling from a church, and not a devotional. It does not tell you that you are growing when the evidence says otherwise, and it does not treat a disagreement fifteen centuries old as though it were settled last week. Where the traditions divide, both sides are quoted from their own documents. Where this document takes a position, it says so and shows its work — see [Honest caveats](#h-honest-caveats).

It is also not a verdict on any canonized person. Part II describes how canonization works and how it came to work that way; it does not adjudicate particular causes.

---

## Contents

**[Part I — What the Bible Says](#part-i--what-the-bible-says)**

- [The whole doctrine in one verse](#the-whole-doctrine-in-one-verse)
- [The words themselves](#the-words-themselves)
- [Who the Old Testament calls a saint](#who-the-old-testament-calls-a-saint)
- [Holy things and a holy people: the Levitical pattern](#holy-things-and-a-holy-people-the-levitical-pattern)
- [Every Christian a saint: the address of the letters](#every-christian-a-saint-the-address-of-the-letters)
- [The three tenses](#the-three-tenses)
- [Become what you are: the grammar of the gospel](#become-what-you-are-the-grammar-of-the-gospel)
- [Who does the work?](#who-does-the-work)
- [The means](#the-means)
- [The shape of growth: what the metaphors say](#the-shape-of-growth-what-the-metaphors-say)
- [What growth is not](#what-growth-is-not)
- [Can a Christian be perfect in this life?](#can-a-christian-be-perfect-in-this-life)
- [Degrees among the saints](#degrees-among-the-saints)
- [The saints in Revelation: the word under persecution](#the-saints-in-revelation-the-word-under-persecution)
- [What Part I establishes](#what-part-i-establishes)

**[Part II — What the Church Did With the Word](#part-ii--what-the-church-did-with-the-word)**

- [The martyrs: the first saints](#the-martyrs-the-first-saints)
- [From the graveside to the calendar](#from-the-graveside-to-the-calendar)
- [Rome takes control](#rome-takes-control)
- [The machinery](#the-machinery)
- [The modern stages](#the-modern-stages)
- [The East: glorification](#the-east-glorification)
- [The Reformation: the word given back](#the-reformation-the-word-given-back)
- [What the two senses have in common](#what-the-two-senses-have-in-common)
- [How each tradition describes the growth](#how-each-tradition-describes-the-growth)
- [Where the real disagreements are](#where-the-real-disagreements-are)

**[Part III — What It Means for You](#part-iii--what-it-means-for-you)**

- [Start with what is settled](#start-with-what-is-settled)
- [Are you a saint?](#are-you-a-saint)
- [How to tell whether you are growing](#how-to-tell-whether-you-are-growing)
- [Why mature Christians think they are getting worse](#why-mature-christians-think-they-are-getting-worse)
- [Plateau, backsliding, and the difference](#plateau-backsliding-and-the-difference)
- [The practices, in the proportion Scripture gives them](#the-practices-in-the-proportion-scripture-gives-them)
- [The sin you will fight all your life](#the-sin-you-will-fight-all-your-life)
- [Addiction, compulsion, and illness](#addiction-compulsion-and-illness)
- [When you have hurt somebody](#when-you-have-hurt-somebody)
- [What to do with the canonized saints](#what-to-do-with-the-canonized-saints)
- [What finishes the work](#what-finishes-the-work)
- [One page to keep](#one-page-to-keep)

**[Appendices](#appendices)**

- [A. Every New Testament occurrence of "saints"](#a-every-new-testament-occurrence-of-saints)
- [B. Every Old Testament occurrence of "saints"](#b-every-old-testament-occurrence-of-saints)
- [C. The holiness word families](#c-the-holiness-word-families)
- [D. The three tenses at a glance](#d-the-three-tenses-at-a-glance)
- [E. The stages of a Roman Catholic cause](#e-the-stages-of-a-roman-catholic-cause)
- [F. A timeline](#f-a-timeline)
- [G. Where the traditions stand](#g-where-the-traditions-stand)
- [H. Honest caveats](#h-honest-caveats)
- [I. Further reading](#i-further-reading)

---
---

# Part I — What the Bible Says

## The whole doctrine in one verse

> **Hebrews 10:14** — For by one offering he hath perfected for ever them that are sanctified.

Read in English, that is a flat sentence about finished business. Read in Greek, it is two different tenses deliberately set against each other, and the whole of this subject sits in the gap between them:

```sh
grep '^Hebrews 10:14	' original-languages/interlinear/nt-interlinear.tsv
```

| Greek | Parsing | Force |
| --- | --- | --- |
| τετελείωκεν (*teteleiōken*) | perfect active indicative | he **has perfected** — done, standing done, nothing pending |
| ἁγιαζομένους (*hagiazomenous*) | present passive participle | **those being sanctified** — in progress, incomplete, ongoing |

The same people, in the same clause, are *already perfected* and *currently being made holy*. Not two groups; not two stages one after the other; two true descriptions of one set of people at one moment. Everything in Part I is an unfolding of that sentence.

The same writer had already put the two halves side by side four verses earlier and two chapters back:

> **Hebrews 10:10** — By the which will we are sanctified through the offering of the body of Jesus Christ once for all.

There *sanctified* is a perfect passive participle — a completed act with standing results, and the phrase *once for all* (ἐφάπαξ) makes repetition unthinkable.

> **Hebrews 2:11** — For both he that sanctifieth and they who are sanctified are all of one: for which cause he is not ashamed to call them brethren,

There both verbs are present — *the one sanctifying* and *the ones being sanctified*, an activity under way on both sides.

One writer, one book, one word, three tenses, no embarrassment. Hebrews does not think it has a paradox on its hands.

Now put beside it the address of the most difficult letter in the New Testament:

> **1 Corinthians 1:2** — Unto the church of God which is at Corinth, to them that are sanctified in Christ Jesus, called to be saints, with all that in every place call upon the name of Jesus Christ our Lord, both theirs and ours:

*Sanctified* here is again a perfect passive participle — ἡγιασμένοις, *having been made holy, and remaining so*. And *called to be saints* is κλητοῖς ἁγίοις, two words, literally **called saints** or *saints by calling*; the words *to be* are the translators' supplement, printed in italics in the original KJV, and they slightly weaken the sense. Paul is not saying the Corinthians have been invited to become saints someday. He is saying they *are* saints, by God's summons, as their standing description.

Then he tells them what they are doing: dividing the church into personality parties (1:11–12), tolerating a man sleeping with his father's wife (5:1), suing each other in pagan courts (6:1–8), visiting prostitutes (6:15–16), getting drunk at the Lord's Supper while the poor go hungry (11:21), and disbelieving the resurrection (15:12). The New Testament's fullest catalogue of congregational scandal is addressed to *the sanctified, called saints*.

Whatever *saint* means in the New Testament, therefore, it cannot mean *an unusually good Christian*, because it is used for some of the worst-behaved Christians on record — and used as a fact about them, not a hope for them. And whatever it means, it cannot mean *someone who has arrived*, because the same letters that hand out the title spend their remaining chapters demanding change.

---

## The words themselves

### Hebrew

| Strong's | Word | Sense | KJV renderings |
| --- | --- | --- | --- |
| [H6918](original-languages/lexicons/strongs-hebrew.tsv) | קָדוֹשׁ *qādôš* | sacred, set apart; as a noun, a holy one (God, an angel, a consecrated person) | holy, Holy One, saint |
| H6942 | קָדַשׁ *qādaš* | to be, make, pronounce, or treat as holy | sanctify, hallow, consecrate, dedicate, be holy |
| H6944 | קֹדֶשׁ *qōdeš* | holiness; a sacred thing or place | holiness, holy, sanctuary, hallowed thing, saint |
| H2623 | חָסִיד *ḥāsîd* | loyal, devoted, bound in covenant faithfulness (from *ḥesed*, steadfast love) | saint, godly, holy one, merciful |
| H6922 | קַדִּישׁ *qaddîš* (Aramaic) | holy one | saint, holy one |

The root idea of *qādaš* is not moral excellence but **separation for a purpose** — a pot can be holy (Zechariah 14:20–21), a day can be holy, a piece of ground can be holy. Holiness begins as a relation (this belongs to God, and is therefore not available for ordinary use) and only then becomes a quality (what belongs to God must be like God).

*ḥāsîd* is a different idea altogether, and English blurs the two by rendering both as *saint*. A *ḥāsîd* is someone in a bond of loyal love — the covenant-keeping, God-committed person. Where the Psalms say *saints*, they usually mean this: not the ritually consecrated, but the faithful.

### Greek

| Strong's | Word | Sense | KJV renderings | NT occurrences |
| --- | --- | --- | --- | --- |
| [G0040](original-languages/lexicons/strongs-greek.tsv) | ἅγιος *hagios* | sacred, set apart, pure | holy, saint, most holy | 240 |
| G0037 | ἁγιάζω *hagiazō* | to make holy, consecrate, purify | sanctify, hallow, be holy | 29 |
| G0038 | ἁγιασμός *hagiasmos* | the process or state of being made holy | sanctification, holiness | 10 |
| G0041 | ἁγιότης *hagiotēs* | holiness as a state | holiness | 1 |
| G0042 | ἁγιωσύνη *hagiōsynē* | holiness as a quality | holiness | 3 |
| G0039 | ἅγιον *hagion* | a holy thing or place | sanctuary, holy place, holiest of all | — |
| G3741 | ὅσιος *hosios* | pious, devout, right by divine character | holy, mercy | — |
| G2513 | καθαρός *katharos* | clean, pure | clean, clear, pure | — |
| G5046 | τέλειος *teleios* | complete, finished, mature, full-grown | perfect, of full age, man | — |

Counts are from the interlinear in this repository:

```sh
awk -F'\t' '$6=="G0040"' original-languages/interlinear/nt-interlinear.tsv | wc -l
```

Three observations govern everything that follows.

**First, *hagios* is a word about God before it is a word about people.** Of its 240 occurrences, the largest single block — 89, better than a third — stands next to πνεῦμα in the phrase *Holy Ghost*. Human holiness in the New Testament is derivative by construction: people are holy because they have been attached to the Holy One, and the Spirit who makes them holy is called the Holy Spirit far more often than they are called holy.

**Second, ἁγιασμός is a process noun.** Greek nouns ending in ‑μος typically name an action or its result rather than a static quality; its cousin ἁγιωσύνη (‑σύνη) names the quality. The New Testament has both and uses them differently: you are called *unto* ἁγιασμός (1 Thessalonians 4:7) — something you move toward; you are established *in* ἁγιωσύνη (1 Thessalonians 3:13) — something you are found in. Every one of the ten occurrences of ἁγιασμός is in the letters, and every one of them is about Christians; none is about a ceremony.

**Third, *teleios* is not the English word *perfect*.** It means finished, complete, having reached its end or purpose. A *teleios* man in James 3:2 is one who has his tongue under control; in 1 Corinthians 14:20 it is contrasted with *children*; in Hebrews 5:14 the *teleios* are those on solid food rather than milk. Translating it *perfect* has probably caused more grief in this subject than any other single translation decision in the English Bible, because it makes Matthew 5:48 sound like a demand for flawlessness where the Greek asks for completeness — a love that, like the Father's, does not stop at the boundary of one's own people.

---

## Who the Old Testament calls a saint

The KJV has *saints* in 34 Old Testament verses. Which Hebrew word is underneath makes a considerable difference, and the two main ones point in nearly opposite directions:

```sh
grep -w 'saints' kjv/kjv.txt | head -34
```

| Hebrew | Verses | Where |
| --- | --- | --- |
| חָסִיד *ḥāsîd* — the loyal, the covenant-faithful | 19 | 1 Samuel 2:9; 2 Chronicles 6:41; Psalms 30:4; 31:23; 37:28; 50:5; 52:9; 79:2; 85:8; 97:10; 116:15; 132:9; 132:16; 145:10; 148:14; 149:1; 149:5; 149:9; Proverbs 2:8 |
| קָדוֹשׁ *qādôš* — holy ones (often angels) | 9 | Deuteronomy 33:3; Job 5:1; 15:15; Psalms 16:3; 34:9; 89:5; 89:7; Hosea 11:12; Zechariah 14:5 |
| קֹדֶשׁ *qōdeš* — holiness | 1 | Deuteronomy 33:2 |
| קַדִּישׁ *qaddîš* (Aramaic) | 5 | Daniel 7:18, 21, 22, 25, 27 |

(The Hebrew verse numbers in the Psalms run one ahead of the English wherever a psalm has a superscription, because Hebrew counts the superscription as verse 1. Psalm 30:4 in the KJV is Psalm 30:5 in [`original-languages/hebrew/wlc-words.tsv`](original-languages/hebrew/wlc-words.tsv). The table accounts for that.)

Four things are worth carrying forward.

**The saints are a group, not a rank.** Every Old Testament use is plural except three: Aaron is *the saint of the LORD* (Psalms 106:16), and Daniel 8:13 has an angelic conversation between *saints*. There is no Old Testament procedure for making someone a saint and no list of who qualifies. The saints are simply God's people, considered as his.

**Some of the saints are not human.** Several *qādôš* passages are about the heavenly court — *the assembly of the saints* in Psalm 89:5–7 is parallel to *the sons of the mighty*; Job 15:15 says God *putteth no trust in his saints*, a statement that only makes sense of angels; Zechariah 14:5 and Deuteronomy 33:2 describe God arriving with his holy ones. The overlap is not sloppiness. It indicates that *saint* names membership in God's own company, and that company includes more than earth.

**God is chiefly interested in the saints' safety, not their achievements.** Read the *ḥāsîd* passages in a row and a single note dominates: *He will keep the feet of his saints* (1 Samuel 2:9); *he forsaketh not his saints; they are preserved for ever* (Psalms 37:28); *he preserveth the souls of his saints* (Psalms 97:10); *he keepeth the paths of judgment, and preserveth the way of his saints* (Proverbs 2:8). The saints are those God holds on to.

> **Psalms 116:15** — Precious in the sight of the LORD is the death of his saints.

**And in Daniel the saints are a persecuted body that wins.** The Aramaic *qaddîšîn* of Daniel 7 are made war upon and worn out by a hostile power for a set time, and then the verdict goes in their favour:

> **Daniel 7:18** — But the saints of the most High shall take the kingdom, and possess the kingdom for ever, even for ever and ever.

> **Daniel 7:27** — And the kingdom and dominion, and the greatness of the kingdom under the whole heaven, shall be given to the people of the saints of the most High, whose kingdom is an everlasting kingdom, and all dominions shall serve and obey him.

Revelation will pick up that vocabulary almost untouched, and for the same reason. See [The saints in Revelation](#the-saints-in-revelation-the-word-under-persecution).

---

## Holy things and a holy people: the Levitical pattern

Before Israel is told to be holy, Israel is *made* holy, and the order is never reversed. The pattern set at Sinai is the skeleton of everything the New Testament says about sanctification.

> **Exodus 19:5–6** — Now therefore, if ye will obey my voice indeed, and keep my covenant, then ye shall be a peculiar treasure unto me above all people: for all the earth is mine: And ye shall be unto me a kingdom of priests, and an holy nation.

The holiness is conferred by relation — *unto me* — and it is corporate before it is personal. Israel is a holy nation before any Israelite is a holy man.

Then the commands, in the two forms they always take:

> **Leviticus 19:2** — Speak unto all the congregation of the children of Israel, and say unto them, Ye shall be holy: for I the LORD your God am holy.

> **Leviticus 11:44** — For I am the LORD your God: ye shall therefore sanctify yourselves, and ye shall be holy; for I am holy...

And then, immediately, the balance that keeps the command from becoming a religion of self-improvement:

> **Leviticus 20:7–8** — Sanctify yourselves therefore, and be ye holy: for I am the LORD your God. And ye shall keep my statutes, and do them: **I am the LORD which sanctify you.**

Two verses. *Sanctify yourselves* and *I am the LORD which sanctify you*, with no attempt to reconcile them. That double statement appears throughout Leviticus (20:8; 21:8; 21:15; 21:23; 22:9; 22:16; 22:32) and it is the Old Testament form of Philippians 2:12–13. Israel is to work at a holiness that God is producing.

The content of that holiness in Leviticus is startlingly ordinary. Leviticus 19, the chapter that begins *Ye shall be holy*, goes on to require leaving the edges of the harvest for the poor, paying a hired man before nightfall, not cursing the deaf or tripping the blind, not gossiping, not hating your brother in your heart, loving your neighbour as yourself, and using honest weights. Holiness in the Torah is not primarily ecstatic or ascetic. It is largely a matter of how you treat people who cannot make you pay for mistreating them.

Three features of the Levitical pattern carry straight into the New Testament:

1. **Holiness is graded in things and places** — the camp, the court, the Holy Place, the Holy of Holies; common, clean, holy, most holy. Degrees of holiness are native to the Bible's vocabulary long before anyone asks whether one Christian can be holier than another.
2. **Holiness is contagious in both directions, but not symmetrically.** Uncleanness spreads by contact easily; holiness is communicated by consecration, deliberately. Haggai 2:11–13 makes the point explicitly. This is why the New Testament is so insistent that association with sin is dangerous while also insisting that Christ's holiness is stronger than the defilement he touches — he touches the leper and the leper is cleansed, rather than the reverse (Mark 1:41–42).
3. **Holiness terminates in the presence of God.** The whole apparatus exists so that a holy God can live in the middle of an unholy people without destroying them. That is why Hebrews 12:14 can say *holiness, without which no man shall see the Lord* — it is not an arbitrary entrance requirement but a statement about what it takes to survive the sight.

---

## Every Christian a saint: the address of the letters

Here is the New Testament's usage in full. *Saints* occurs in 61 verses ([Appendix A](#a-every-new-testament-occurrence-of-saints) lists every one), and the pattern is the most striking in the whole subject:

- **It is a form of address to living congregations.** Romans 1:7 — *To all that be in Rome, beloved of God, called to be saints*. Ephesians 1:1, Philippians 1:1, Colossians 1:2, and 2 Corinthians 1:1 open the same way. The word is on the envelope.
- **It is how Christians are described in ordinary church business.** The collection for Jerusalem is *the collection for the saints* (1 Corinthians 16:1), taken up from churches for believers who are hungry. Phoebe is to be received *as becometh saints* (Romans 16:2). Church disputes should be settled *before the saints* (1 Corinthians 6:1). Hospitality is *given to hospitality* toward the saints (Romans 12:13). Widows are commended for having *washed the saints' feet* (1 Timothy 5:10). The saints, in the New Testament, are people you feed, lodge, argue with, and wash.
- **It is never a posthumous title in the letters.** Not once does a New Testament writer refer to a dead Christian as *Saint So-and-so*. There is no *Saint Stephen* in Acts, though Stephen is the first martyr; Acts 22:20 calls him *thy martyr Stephen*.
- **It is almost never singular.** Exactly one New Testament verse uses it of an individual, and it is a universal, not an honour:

> **Philippians 4:21** — Salute every saint in Christ Jesus. The brethren which are with me greet you.

*Every saint* means every Christian in Philippi. The only individual saint in the New Testament is whoever you happen to be greeting.

- **The one narrative exception proves the point.** Matthew 27:52 says that at the crucifixion *many bodies of the saints which slept arose* — dead believers of Israel, raised. Even that is a plural crowd, unnamed.
- **Paul's self-description runs the other way from a ranking.** *Unto me, who am less than the least of all saints, is this grace given* (Ephesians 3:8). The apostle who wrote a quarter of the New Testament puts himself at the bottom of the class he is addressing, which is difficult to do if the word marks attainment.

And the three descriptions that the letters attach to sainthood are all about position, never merit:

> **Ephesians 2:19** — Now therefore ye are no more strangers and foreigners, but fellowcitizens with the saints, and of the household of God;

> **Acts 26:18** — ...that they may receive forgiveness of sins, and inheritance among them which are sanctified by faith that is in me.

> **Jude 1:1** — Jude, the servant of Jesus Christ, and brother of James, to them that are sanctified by God the Father, and preserved in Jesus Christ, and called:

In Acts 26:18 and Acts 20:32, *them which are sanctified* is a perfect passive participle used as a simple designation for Christians — the sanctified, as a class, the way one might say *the enrolled*. Sanctification there is not what advanced believers achieve; it is what makes somebody a believer at all.

So the New Testament's answer to *who is a saint?* is: everyone in Christ, immediately, including the immature, the failing, and the ones under discipline. Which makes the rest of the New Testament's demands considerably more pointed, not less.

---

## The three tenses

Put every sanctification text in the New Testament on a table and sort by tense, and they fall into three piles that do not overlap. This is the single most useful thing to know about the subject, because nearly every confusion about it comes from applying a text from one pile to a question belonging to another.

| | **Definitive** | **Progressive** | **Final** |
| --- | --- | --- | --- |
| **Tense** | past — done | present — under way | future — promised |
| **Question it answers** | Am I God's? | Am I becoming like him? | Will it be finished? |
| **Degrees?** | No. You are either set apart or not | Yes, entirely. Some have more, some less | No. All the saved, alike, at once |
| **Basis** | Christ's one offering | The Spirit's work through the means, with your effort | Christ's appearing |
| **Certainty** | Absolute | Real but uneven, and reversible in stretches | Absolute |
| **Key texts** | 1 Corinthians 1:2; 6:11; Hebrews 10:10; Acts 20:32; 26:18; Jude 1:1 | Hebrews 10:14; 12:14; 1 Thessalonians 4:3; 2 Corinthians 3:18; 7:1; Romans 6:19, 22 | 1 Thessalonians 5:23; 1 John 3:2; Ephesians 5:27; Jude 1:24; Colossians 1:22 |
| **If you confuse it with the others** | You will think holiness is optional | You will think God's acceptance of you fluctuates with your week | You will expect completion now and despair when it does not come |

### Past: you were sanctified

> **1 Corinthians 6:11** — And such were some of you: but ye are washed, but ye are sanctified, but ye are justified in the name of the Lord Jesus, and by the Spirit of our God.

*Ye are sanctified* is ἡγιάσθητε — aorist passive indicative, **you were sanctified**, a single completed event done to you. And notice its position in the sentence: *sanctified* stands **before** *justified*. Whatever Paul means, he is not describing a moral improvement programme that follows conversion; he is describing what happened at conversion, and he lists it among the things that make a Christian a Christian.

Note also what precedes it. Verses 9–10 have just listed the fornicators, idolaters, adulterers, thieves, covetous, drunkards, revilers, and extortioners who will not inherit the kingdom, and then: *and such were some of you*. The definitively sanctified are ex-members of that list.

> **Hebrews 10:10** — By the which will we are sanctified through the offering of the body of Jesus Christ once for all.

The basis is external: not what the sanctified did, but what was offered for them, *once for all*.

Definitive sanctification is not a stage you graduate from. It is the permanent fact about a Christian that makes progressive sanctification possible, and it is the reason the New Testament can call failing people saints without irony.

### Present: you are being sanctified

> **1 Thessalonians 4:3** — For this is the will of God, even your sanctification, that ye should abstain from fornication:

People agonise over finding *the will of God* for their lives. Here it is, stated flatly, with an immediate and very specific application. Paul does not say sanctification is *part* of God's will; he says *this is the will of God, even your sanctification* — and then he spends four verses on sexual conduct and one on not defrauding your brother in business.

> **2 Corinthians 7:1** — Having therefore these promises, dearly beloved, let us cleanse ourselves from all filthiness of the flesh and spirit, perfecting holiness in the fear of God.

*Perfecting holiness* — a present participle; bringing holiness toward completeness, an unfinished job. And it begins with *having therefore these promises*: the motive comes from what God has already said, not from anxiety about what he may yet do.

> **Romans 6:19** — ...even so now yield your members servants to righteousness unto holiness.

*Unto holiness* — εἰς ἁγιασμόν, holiness as the direction of travel, the destination of the yielding.

> **2 Corinthians 3:18** — But we all, with open face beholding as in a glass the glory of the Lord, are changed into the same image from glory to glory, even as by the Spirit of the LORD.

*Are changed* is μεταμορφούμεθα — present passive, **we are being transformed**, the same verb used of the transfiguration. Four things in that one sentence: it happens to *all* Christians (*we all*), it happens by *looking* rather than striving, it is done *to* us (passive), and it is incremental (*from glory to glory*).

> **Hebrews 12:14** — Follow peace with all men, and holiness, without which no man shall see the Lord:

*Follow* is a strong verb — pursue, chase. And the clause attached to it is the hardest sentence in the New Testament on this subject for anyone inclined to treat progressive sanctification as optional.

### Future: he shall sanctify you wholly

> **1 Thessalonians 5:23–24** — And the very God of peace sanctify you wholly; and I pray God your whole spirit and soul and body be preserved blameless unto the coming of our Lord Jesus Christ. Faithful is he that calleth you, who also will do it.

*Sanctify you wholly* — ὁλοτελεῖς, complete through and through. It is a prayer, not a command, and verse 24 answers it before anyone can worry: *Faithful is he that calleth you, who also will do it*.

> **1 John 3:2** — Beloved, now are we the sons of God, and it doth not yet appear what we shall be: but we know that, when he shall appear, we shall be like him; for we shall see him as he is.

*Now* and *not yet* in a single verse, with the mechanism of the final change stated: seeing him. It is the same mechanism as 2 Corinthians 3:18, without the glass.

> **Ephesians 5:26–27** — That he might sanctify and cleanse it with the washing of water by the word, That he might present it to himself a glorious church, not having spot, or wrinkle, or any such thing; but that it should be holy and without blemish.

> **Jude 1:24** — Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory with exceeding joy,

Both of those are about a presentation, and in both the one doing the presenting is Christ, not the presented.

The practical value of the third tense is that it removes the pressure from the second without removing the duty. You are not required to finish. You are required to move, and the finishing is guaranteed by someone else.

---

## Become what you are: the grammar of the gospel

The New Testament almost never issues a moral command without first stating a fact. The fact is called the indicative; the command is the imperative; and the imperative is always built on the indicative, never the reverse. Once you see the pattern you cannot stop seeing it.

| Indicative (what is true) | Imperative (therefore do this) |
| --- | --- |
| *Christ our passover is sacrificed for us... as ye are unleavened* | *Purge out therefore the old leaven* (1 Corinthians 5:7) |
| *Ye are dead, and your life is hid with Christ in God* | *Mortify therefore your members which are upon the earth* (Colossians 3:3–5) |
| *Ye have put off the old man... and have put on the new* | *Put on therefore... bowels of mercies, kindness* (Colossians 3:9–12) |
| *If we live in the Spirit* | *let us also walk in the Spirit* (Galatians 5:25) |
| *They that are Christ's have crucified the flesh* | *Walk in the Spirit, and ye shall not fulfil the lust of the flesh* (Galatians 5:24, 16) |
| *God which worketh in you both to will and to do* | *Work out your own salvation with fear and trembling* (Philippians 2:12–13) |
| *He which hath called you is holy* | *so be ye holy in all manner of conversation* (1 Peter 1:15) |
| *Having therefore these promises* | *let us cleanse ourselves from all filthiness* (2 Corinthians 7:1) |
| *I am the LORD which sanctify you* | *Sanctify yourselves therefore, and be ye holy* (Leviticus 20:7–8) |

Note the striking case in 1 Corinthians 5:7: *purge out the old leaven... as ye are unleavened*. Become what you already are. That is not a contradiction; it is the structure of the whole Christian ethic. The moral demands of the New Testament are not requirements for entry. They are descriptions of what a person in Christ actually is, addressed to people who do not yet fully look like it.

> **Romans 6:11–13** — Likewise reckon ye also yourselves to be dead indeed unto sin, but alive unto God through Jesus Christ our Lord. Let not sin therefore reign in your mortal body, that ye should obey it in the lusts thereof. Neither yield ye your members as instruments of unrighteousness unto sin: but yield yourselves unto God, as those that are alive from the dead...

*Reckon yourselves to be dead unto sin* is not pretending. It is counting as true what Romans 6:1–10 has just established as true, and then acting on the count.

Two errors follow from getting the order backwards.

**Reverse the order and you get moralism** — holiness attempted as the price of acceptance, which produces either despair or pride depending on temperament, and usually both in rotation.

**Drop the imperative and you get presumption** — the indicative treated as making the commands unnecessary, which the New Testament answers with an incredulous question (*What shall we say then? Shall we continue in sin, that grace may abound? God forbid*, Romans 6:1–2) and the flat statement of Hebrews 12:14.

---

## Who does the work?

The New Testament gives two answers, puts them next to each other, and never resolves them:

> **Philippians 2:12–13** — Wherefore, my beloved, as ye have always obeyed, not as in my presence only, but now much more in my absence, work out your own salvation with fear and trembling. For it is God which worketh in you both to will and to do of his good pleasure.

The *for* is the whole problem. It is not *but*; it is not *although*; it is **because**. God's working is given as the reason for your working, not as its substitute. The same logic appears in Colossians 1:29 — Paul labours *according to his working, which worketh in me mightily* — and in 1 Corinthians 15:10, *I laboured more abundantly than they all: yet not I, but the grace of God which was with me*.

Set out plainly:

| What Scripture attributes to God | What Scripture attributes to you |
| --- | --- |
| *the very God of peace sanctify you wholly* (1 Thessalonians 5:23) | *let us cleanse ourselves* (2 Corinthians 7:1) |
| *it is God which worketh in you both to will and to do* (Philippians 2:13) | *work out your own salvation* (Philippians 2:12) |
| *he which hath begun a good work in you will perform it* (Philippians 1:6) | *I press toward the mark* (Philippians 3:14) |
| *we... are changed into the same image* — passive (2 Corinthians 3:18) | *mortify therefore your members* (Colossians 3:5) |
| *he for our profit, that we might be partakers of his holiness* (Hebrews 12:10) | *follow... holiness* (Hebrews 12:14) |
| *Sanctify them through thy truth* (John 17:17) | *I keep under my body, and bring it into subjection* (1 Corinthians 9:27) |
| *God, that giveth the increase* (1 Corinthians 3:7) | *we are labourers together with God* (1 Corinthians 3:9) |

Every attempt to relieve the tension by cancelling one column has produced a recognisable error, and church history has run the experiment repeatedly:

- **Cancel the right column** and you get quietism — the teaching that effort is fleshly and the believer must simply cease striving and let God act. Part II tracks the version of this that entered English-speaking evangelicalism through the Keswick movement, and the sharp reaction against it.
- **Cancel the left column** and you get moralism and burnout — sanctification as self-improvement with religious vocabulary, in which failure has no remedy but more resolve.

The New Testament's own posture is that the *more* God works, the *harder* you work, and the more certainly you attribute the work to him. That is not a compromise between the columns. It is what both columns say when they are left standing.

---

## The means

Scripture is not vague about how holiness comes. It names the instruments, and they are strikingly ordinary and strikingly corporate — most of them cannot be done alone.

**1. The word.** The single most-named means.

> **John 17:17** — Sanctify them through thy truth: thy word is truth.

> **Ephesians 5:26** — That he might sanctify and cleanse it with the washing of water by the word,

> **1 Peter 2:2** — As newborn babes, desire the sincere milk of the word, that ye may grow thereby:

Note the assumption in 1 Peter: what makes a Christian grow is the same thing that fed them at the beginning, taken in continually. There is no advanced diet.

**2. The Spirit.** Sanctification is repeatedly attributed to him directly — *sanctification of the Spirit* (2 Thessalonians 2:13; 1 Peter 1:2), *sanctified by the Holy Ghost* (Romans 15:16), *by the Spirit of the LORD* (2 Corinthians 3:18) — and the fruit of holiness is *the fruit of the Spirit* (Galatians 5:22–23), a singular fruit with nine aspects, not nine achievements to collect separately.

**3. Affliction and discipline.** The New Testament's least popular means and one of its most emphasised.

> **Hebrews 12:10–11** — ...but he for our profit, that we might be partakers of his holiness. Now no chastening for the present seemeth to be joyous, but grievous: nevertheless afterward it yieldeth the peaceable fruit of righteousness unto them which are exercised thereby.

> **Romans 5:3–5** — And not only so, but we glory in tribulations also: knowing that tribulation worketh patience; And patience, experience; and experience, hope: And hope maketh not ashamed...

> **James 1:2–4** — ...count it all joy when ye fall into divers temptations; Knowing this, that the trying of your faith worketh patience. But let patience have her perfect work, that ye may be perfect and entire, wanting nothing.

Two qualifications that this passage is constantly made to carry and does not: it does not say that every affliction is a punishment, and it does not say that suffering sanctifies automatically. Hebrews 12:11 restricts the harvest to *them which are exercised thereby* — trained by it. The same trouble makes one person gentler and another bitter.

**4. The church.** Sanctification in the New Testament is a group project, and the texts are blunt about it.

> **Ephesians 4:11–13** — And he gave some, apostles... For the perfecting of the saints, for the work of the ministry, for the edifying of the body of Christ: Till we all come in the unity of the faith... unto a perfect man, unto the measure of the stature of the fulness of Christ:

*The perfecting of the saints* — καταρτισμός, the word used for setting a bone or mending a net. And the goal is corporate: *till we all come*, singular *perfect man*. Ephesians 4:16 makes the mechanism explicit — the body grows *by that which every joint supplieth*, so that the growth of each depends on the functioning of the rest. On this account a Christian who has withdrawn from the church has removed themselves from a named means of their own sanctification.

**5. Obedience itself.** Doing the thing forms the person who does it. *Exercise thyself rather unto godliness* (1 Timothy 4:7); *by reason of use have their senses exercised* (Hebrews 5:14); the fruit of the Spirit grows in people who are walking in the Spirit (Galatians 5:16, 25). Scripture assumes what everyone knows from ordinary life: habits shape character, and there is no way to become a patient person without repeatedly not losing your temper.

**6. Confession and cleansing.**

> **1 John 1:9** — If we confess our sins, he is faithful and just to forgive us our sins, and to cleanse us from all unrighteousness.

Written to Christians, in the present tense, as a normal and repeated part of Christian life. A doctrine of progress that has no place for ongoing confession is not the New Testament's.

**7. The hope itself.**

> **1 John 3:3** — And every man that hath this hope in him purifieth himself, even as he is pure.

> **Titus 2:11–14** — For the grace of God that bringeth salvation hath appeared to all men, Teaching us that, denying ungodliness and worldly lusts, we should live soberly, righteously, and godly, in this present world; Looking for that blessed hope...

Expecting to see him changes what you do on Tuesday. The doctrine of final sanctification is itself one of the engines of progressive sanctification.

---

## The shape of growth: what the metaphors say

The New Testament almost never describes sanctification abstractly. It reaches for pictures, and each picture carries a claim about what growth is like.

| Metaphor | Texts | What it implies |
| --- | --- | --- |
| **Infancy to adulthood** | 1 Corinthians 3:1–3; Hebrews 5:12–14; Ephesians 4:13–14; 1 Peter 2:2 | Growth is normal and expected; failure to grow is a rebuke, not a neutral fact. It takes years. You cannot skip stages |
| **Seed and harvest** | Mark 4:26–28; Galatians 6:7–9 | Growth is gradual, mostly invisible while happening, and not under the grower's direct control — *he knoweth not how* |
| **A building under construction** | Ephesians 2:20–22; 1 Corinthians 3:9–15 | It is put together from outside, piece by piece, to a plan not drawn by the building |
| **A walk** | Galatians 5:16, 25; Colossians 1:10; 1 Thessalonians 4:1 | Ordinary, repetitive, forward, slow; measured in direction, not speed |
| **A race** | 1 Corinthians 9:24–27; Philippians 3:13–14; Hebrews 12:1–2 | Effort, discipline, sacrifice of legitimate things, and a finish line that is not here |
| **Pruning a vine** | John 15:1–5 | The fruitful branch is cut — improvement often feels like loss, and abiding, not striving, is the condition of fruit |
| **Glory to glory** | 2 Corinthians 3:18 | Change by beholding; the increments are real and the destination is a likeness |
| **Dawn to noon** | Proverbs 4:18 | *The path of the just is as the shining light, that shineth more and more unto the perfect day* — the direction is settled even when the light is faint |
| **Childbirth** | Galatians 4:19 | *until Christ be formed in you* — costly to those who labour for it, and the thing formed is a person, not a set of behaviours |
| **Renewal against decay** | 2 Corinthians 4:16 | *though our outward man perish, yet the inward man is renewed day by day* — the two curves run in opposite directions at once |

Two features are common to nearly all of them.

**Growth is organic, not mechanical.** Nothing in the New Testament's imagery suggests a linear schedule, a technique, or a guaranteed rate. Living things grow in fits, respond to season and injury, and are largely opaque to themselves while doing it.

**Growth is measured against a person, not a standard.** The goal is never *moral excellence* in the abstract. It is *conformed to the image of his Son* (Romans 8:29), *till Christ be formed in you* (Galatians 4:19), *unto the measure of the stature of the fulness of Christ* (Ephesians 4:13), *changed into the same image* (2 Corinthians 3:18). This is why sanctification cannot be reduced to rule-keeping, and also why it cannot be reduced to sincerity: there is a definite shape it is heading toward, and we know what he was like.

---

## What growth is not

Scripture rules out several things that are commonly mistaken for progress. Each of these has wrecked people's assurance or inflated their self-estimate, usually by giving them the wrong measuring stick.

**It is not linear.** The Bible's own examples of mature believers include Abraham lying about his wife twice, Moses striking the rock after forty years of leadership, David committing adultery and murder at the height of his reign, Elijah collapsing into suicidal despair immediately after Carmel, Peter refusing to eat with Gentiles years after Pentecost and being rebuked to his face (Galatians 2:11–14), and Barnabas going with him. If sanctification were a straight line, the Bible would need different heroes.

**It is not sinlessness.** See the next section. Every New Testament writer who addresses the question assumes ongoing sin in believers and provides for it.

**It is not feeling.** Nothing in the New Testament measures growth by emotional intensity. Some of the most spiritually advanced passages in Scripture are written out of darkness — Psalm 88 ends without relief, and Paul writes 2 Corinthians out of *troubled on every side... perplexed... persecuted... cast down*.

**It is not gifting, knowledge, or usefulness.** Corinth had every gift (*ye come behind in no gift*, 1 Corinthians 1:7) and was the least sanctified church in the New Testament. 1 Corinthians 13:1–3 says explicitly that tongues, prophecy, all knowledge, mountain-moving faith, giving away everything, and being burned are all compatible with being nothing. Public usefulness is not a measurement of private holiness, and the New Testament nowhere treats it as one.

**It is not respectability.** The sins that most exercise the New Testament writers — pride, censoriousness, greed, gossip, faction, contempt for the poor — are almost all socially invisible or socially rewarded. It is quite possible to become more respectable and less holy at the same time, and the Pharisees are in the Gospels partly to make sure nobody misses it.

**It is not the absence of temptation.** Christ was *in all points tempted like as we are, yet without sin* (Hebrews 4:15). Temptation felt is not sin committed, and a mature Christian may feel more of it, not less, because they are fighting on ground they used to concede.

---

## Can a Christian be perfect in this life?

This is the one place where the traditions divide sharply on exegesis rather than on vocabulary. Both sides have real texts. They are set out here in full, because the argument is usually conducted with half of them.

### Texts urged for perfection

> **Matthew 5:48** — Be ye therefore perfect, even as your Father which is in heaven is perfect.

> **1 John 3:6** — Whosoever abideth in him sinneth not: whosoever sinneth hath not seen him, neither known him.

> **1 John 3:9** — Whosoever is born of God doth not commit sin; for his seed remaineth in him: and he cannot sin, because he is born of God.

> **1 Thessalonians 5:23** — And the very God of peace sanctify you wholly...

> **Romans 6:14** — For sin shall not have dominion over you: for ye are not under the law, but under grace.

Also urged: 2 Corinthians 7:1 (*perfecting holiness*), Hebrews 6:1 (*let us go on unto perfection*), Titus 2:14 (*purify unto himself a peculiar people*), Ephesians 5:27 (*not having spot, or wrinkle*), and 1 John 4:17–18 (*perfect love casteth out fear*).

### Texts urged against it

> **1 John 1:8** — If we say that we have no sin, we deceive ourselves, and the truth is not in us.

> **1 John 1:10** — If we say that we have not sinned, we make him a liar, and his word is not in us.

> **Philippians 3:12** — Not as though I had already attained, either were already perfect: but I follow after...

> **James 3:2** — For in many things we offend all. If any man offend not in word, the same is a perfect man, and able also to bridle the whole body.

> **Galatians 5:17** — For the flesh lusteth against the Spirit, and the Spirit against the flesh: and these are contrary the one to the other: so that ye cannot do the things that ye would.

Also urged: 1 Kings 8:46 (*there is no man that sinneth not*), Ecclesiastes 7:20, Proverbs 20:9, Romans 7:14–25, and the Lord's Prayer itself, which teaches disciples to ask daily for forgiveness (Matthew 6:12).

### How the arguments actually run

**On *teleios* (Matthew 5:48).** The word means complete, whole, having reached its intended end — not flawless. Look at the paragraph it concludes: Matthew 5:43–47 is about loving enemies and greeting more than your own people, on the ground that the Father *maketh his sun to rise on the evil and on the good*. The *perfection* required is a love that, like God's, is not restricted to those who return it. Luke's parallel says *Be ye therefore merciful, as your Father also is merciful* (Luke 6:36), which is almost certainly the sense.

**On 1 John 3:6, 9.** The verbs are present tense, which in Greek characteristically describes ongoing or habitual action rather than a single act. The contrast in the context is between two settled ways of life — *he that doeth righteousness is righteous... he that committeth sin is of the devil* — not between a believer who never slips and one who does. This reading is also required by the letter's own internal consistency: the same author, two chapters earlier, says that claiming to have no sin is self-deception (1:8) and provides a standing remedy for a Christian's sin (1:9; 2:1 — *if any man sin, we have an advocate with the Father*). Any interpretation of 3:9 that contradicts 1:8 has made John contradict himself inside five pages.

**On Romans 7.** Whether Paul in *the good that I would I do not* describes his present Christian experience, his pre-conversion life read with Christian hindsight, or a rhetorical figure for anyone under law, is a genuinely open question with serious defenders on all sides — set out at length in [`romans-7-study.md`](romans-7-study.md) in this repository. What is not in dispute is that the passage ends in verse 25 with thanks and Romans 8:1 with *no condemnation*, and that the man in it *delights in the law of God after the inward man* — a thing the unregenerate are nowhere said to do (Romans 8:7).

**On Philippians 3:12.** Paul explicitly disclaims the thing at issue, in the past-tense verb, decades into his ministry — and then, four verses later, says *Let us therefore, as many as be perfect, be thus minded* (3:15), using the same word he has just denied. He can do that because *teleios* means mature, and being mature consists partly in knowing you have not arrived.

### Where that leaves it

The historic Wesleyan position is not what it is usually accused of being. Wesley defined sin *properly so called* as "a voluntary transgression of a known law," and explicitly denied that anyone in this life is free from ignorance, mistake, infirmity, or temptation. What he claimed was possible — as a gift to be received by faith, often after conversion, and losable — was a heart so filled with love to God and neighbour that no known sin remained in it. That is a much narrower claim than *sinless perfection*, and much of the heat in three centuries of argument has come from not stating it accurately. It remains a real disagreement: Reformed and Lutheran readers hold that even so qualified it is not what the texts promise for this life, and that Galatians 5:17 and 1 John 1:8 describe the normal Christian condition until death.

What all sides agree on is worth stating, because it is most of what matters practically:

- Sin remaining in a believer is never excusable, never to be made peace with, and always to be fought.
- Real and substantial change is promised and normal, and a professed Christian in whom nothing changes has cause for concern.
- Whatever is unfinished at death is finished at Christ's appearing, not before, and not by us.
- Nobody may claim to have reached a state that puts them beyond the need of daily forgiveness.

---

## Degrees among the saints

If sainthood is conferred equally on everyone in Christ, is there any sense in which one saint is further on than another? Scripture says plainly that there is, and equally plainly that it is not a difference in standing.

**Maturity differs, and the difference is named.** Paul divides Corinth into *spiritual* and *carnal... babes in Christ* (1 Corinthians 3:1), and says that after enough time they should have been past milk. Hebrews 5:12–14 rebukes readers who *ought to be teachers* for still needing the first principles. John writes to *little children... young men... fathers* (1 John 2:12–14), three stages in one congregation. Growth is uneven between Christians and the New Testament says so without embarrassment.

**Faith and love can be measured and can increase.** *Your faith groweth exceedingly, and the charity of every one of you all toward each other aboundeth* (2 Thessalonians 1:3); *that ye would abound more and more* (1 Thessalonians 4:1); *increasing in the knowledge of God* (Colossians 1:10); *that thy profiting may appear to all* (1 Timothy 4:15). Paul expects visible improvement and thanks God when he sees it.

**There are differences at the judgment, and they concern reward, not acceptance.**

> **1 Corinthians 3:13–15** — Every man's work shall be made manifest: for the day shall declare it, because it shall be revealed by fire; and the fire shall try every man's work of what sort it is. If any man's work abide which he hath built thereupon, he shall receive a reward. If any man's work shall be burned, he shall suffer loss: but he himself shall be saved; yet so as by fire.

> **1 Corinthians 15:41–42** — There is one glory of the sun, and another glory of the moon, and another glory of the stars: for one star differeth from another star in glory. So also is the resurrection of the dead.

> **Daniel 12:3** — And they that be wise shall shine as the brightness of the firmament; and they that turn many to righteousness as the stars for ever and ever.

Matthew 5:19 speaks of being *called the least in the kingdom of heaven* and *great in the kingdom*; the parable of the pounds gives rule over ten cities and over five (Luke 19:16–19); 2 Corinthians 5:10 has every believer appearing before the judgment seat of Christ to receive according to what they have done.

**But the differences never touch who belongs.** Nobody in the New Testament is more or less a saint. The thief on the cross had no sanctification to speak of and was told *To day shalt thou be with me in paradise* (Luke 23:43). The labourers hired at the eleventh hour receive the same penny (Matthew 20:1–16), and the parable exists specifically to offend the expectation that they should not. Paul, whose achievement is unmatched, calls himself *less than the least of all saints* (Ephesians 3:8) and *the chief* of sinners (1 Timothy 1:15).

This distinction — real degrees of maturity and reward, no degrees of membership — is the hinge on which Part II turns. A church that keeps both halves can honour exemplary Christians without creating a caste. A church that lets the first half swallow the second ends with two classes of Christian, which is precisely what the New Testament vocabulary was constructed to prevent.

---

## The saints in Revelation: the word under persecution

Thirteen of the New Testament's sixty-one *saints* verses are in Revelation, more than in any other book, and the usage there is distinct enough to deserve its own note. It is Daniel's usage, resumed.

In Revelation the saints are a body under attack:

> **Revelation 13:7** — And it was given unto him to make war with the saints, and to overcome them: and power was given him over all kindreds, and tongues, and nations.

> **Revelation 13:10** — ...Here is the patience and the faith of the saints.

> **Revelation 14:12** — Here is the patience of the saints: here are they that keep the commandments of God, and the faith of Jesus.

Their prayers are the incense on the heavenly altar (5:8; 8:3–4). Their blood is what the persecuting power is drunk with (16:6; 17:6; 18:24). They are the ones the beast is permitted to defeat, the ones whose camp is surrounded at the very end (20:9), and the ones whose reward is named when judgment is finally rendered (11:18).

And what they are given at the end is clothing:

> **Revelation 19:8** — And to her was granted that she should be arrayed in fine linen, clean and white: for the fine linen is the righteousness of saints.

Two things about that verse. The linen is *granted* — given, not earned; and the word behind *righteousness* is plural, δικαιώματα, the righteous acts or deeds of the saints. The bride's dress is made of what the saints actually did, and the whole of it is a gift. Progressive sainthood, in a single image.

One more, the last word of the Bible on the subject, and a surprising one:

> **Revelation 22:11** — He that is unjust, let him be unjust still: and he which is filthy, let him be filthy still: and he that is righteous, let him be righteous still: and he that is holy, let him be holy still.

*Let him be holy still* translates ἁγιασθήτω — an aorist passive imperative of ἁγιάζω, *let him be sanctified still*. Scripture's closing statement about holiness is not a description of a completed class but a command to keep being made holy, issued to people who already are.

---

## What Part I establishes

1. **Every Christian is a saint from the beginning.** The title is a description of position, not a reward for attainment, and the New Testament applies it to congregations it is in the middle of rebuking.
2. **Sanctification has three tenses, and they answer different questions.** You *were* sanctified (definitive), you *are being* sanctified (progressive), you *will be* sanctified wholly (final). Hebrews 10:14 holds the first two together in one clause.
3. **Only the middle tense admits degrees.** That is where growth, failure, effort, and measurable change live.
4. **The command always follows the fact.** Become what you are — never become in order to be.
5. **God works and you work, and the second is because of the first.** Cancel either and you get a recognisable error with a long history.
6. **The means are ordinary and largely corporate** — word, Spirit, affliction, the church, obedience, confession, hope.
7. **Growth is organic, uneven, slow, and measured against a person** rather than a standard.
8. **No Christian reaches the end of it in this life**, and the New Testament assumes ongoing sin and provides a standing remedy for it.
9. **There are real degrees of maturity and reward, and no degrees of belonging.**

---
---

# Part II — What the Church Did With the Word

The New Testament's word for every living Christian became, within a few centuries, a title conferred on a few dead ones by a formal process. That shift is worth understanding on its own terms, because it was not a conspiracy and not a simple corruption: it began in grief, at gravesides, among people being killed.

## The martyrs: the first saints

Christians died under Roman persecution, and Christians buried them. The earliest surviving account of a martyr's death outside the New Testament, the *Martyrdom of Polycarp* — describing the burning of the bishop of Smyrna, usually dated to the mid-150s — records what the church at Smyrna did afterward: they gathered his bones, "more precious than costly stones and more valuable than gold," laid them in a suitable place, and resolved to gather there on the anniversary of his death to celebrate "the birthday of his martyrdom." It also records a careful disclaimer: they worship Christ, whereas the martyrs they love as disciples and imitators of the Lord.

Three practices are already present in that one document, a century before there is any such thing as canonization:

1. **A grave treated as holy ground**, with relics kept.
2. **An annual commemoration**, dated by the day of death, called a *birthday* — *dies natalis*, the day of birth into the presence of God.
3. **An explicit distinction between worship and honour**, defended because it was already being questioned.

The martyrs were the obvious candidates for this because their case needed no adjudication. A person who died rather than deny Christ had given the one proof no one could argue with. Cyprian of Carthage, writing in the 250s, asks his clergy to note the days on which the confessors die so that the anniversaries can be observed, and the church is already keeping records.

## From the graveside to the calendar

Then persecution stopped, and a question arrived that the martyrs' cult had never had to answer: who counts when nobody is being killed?

The fourth century answered it by extending the honour in stages — first to *confessors*, those who had suffered for the faith without dying; then to ascetics, whose renunciation was understood as a slower martyrdom; then to bishops, missionaries, virgins, and teachers of exceptional standing. The Roman list known as the *Depositio Martyrum*, part of a compilation from 354, is essentially a calendar: dates, names, burial places. Once you have a calendar, you have a list, and once you have a list, someone has to decide what goes on it.

For several centuries the decision was local and largely spontaneous. A holy person died; the people venerated them; the local bishop approved or restrained the cult; the name entered the diocesan calendar, and might or might not spread. This is why so many early saints are obscure, why some turn out on investigation to be duplicated or legendary, and why the modern Roman calendar has been pruned more than once — most substantially in the revision that followed the Second Vatican Council, which removed or demoted commemorations whose historical basis could not be established.

Augustine, preaching in the early fifth century, defends the practice against pagan critics who called it a new polytheism, and the terms of his defence are the ones the Western church has used ever since: the martyrs have memorials, not temples; the sacrifice at their memorials is offered to God, not to them; they are honoured as friends of God and imitated, not adored.

Whether that distinction survived contact with popular practice is exactly what the Reformation would later dispute. But the structure of the argument was set by 400: honour the holy dead, imitate them, ask their prayers, worship God alone.

## Rome takes control

The medieval church's problem with saints was not scepticism; it was inflation. Local cults multiplied, relics were bought and sold, and some venerated figures were of doubtful existence or doubtful character. The papacy's growing involvement is best understood as quality control.

- **993** — Pope John XV declares Ulrich, bishop of Augsburg, a saint. This is generally reckoned the first recorded papal canonization, though it did not immediately displace local practice.
- **Twelfth century** — Alexander III asserts that no one may be venerated as a saint without the authority of the Roman church, in a letter occasioned by an unauthorised cult.
- **1234** — Gregory IX incorporates papal reservation of canonization into the *Decretals*, the West's canon law. From this point, in law, only the pope makes saints in the Latin church.

The result was a legal process with a standard of proof. Causes were argued, witnesses examined, miracles investigated, objections entertained. The medieval canonization process was, among other things, one of the earliest systematic evidentiary procedures in European law, and it treated sanctity as a factual claim that could be tested.

## The machinery

- **1588** — Sixtus V reorganises the Roman curia and establishes the Sacred Congregation of Rites, which is given charge of causes of saints along with liturgical matters. Canonization now has a permanent bureaucracy.
- **1587** — the office of *Promotor Fidei*, Promoter of the Faith, is established: the official whose duty is to argue against the cause, scrutinise the evidence, and press every objection. Popular English gave the office its lasting name, the devil's advocate. The institution is a striking admission — that piety is not self-authenticating and that the strongest case for a saint is one that has survived an adversary.
- **1625 and 1634** — Urban VIII issues decrees forbidding public cult of anyone not approved by Rome, with an exception for cults of immemorial standing, and imposing a waiting period between death and the opening of a cause. The waiting period is the key innovation: enthusiasm at a funeral is not evidence.
- **1734–1738** — Prospero Lambertini, who had served as Promoter of the Faith and would become Benedict XIV, publishes *De Servorum Dei Beatificatione et Beatorum Canonizatione*, the great treatise on the subject. It sets out what heroic virtue means, how miracles are to be assessed, what natural explanations must be excluded, and how much weight testimony can bear. Its framework governed Catholic practice into the twentieth century and is still the background of the modern norms.

Notice what the machinery is *for*. The stages exist because the church decided that a claim about someone's holiness is a claim about facts: that this person really did live this way, that these things really did happen, that this account is not embellishment. Whatever one thinks of the conclusions, the instinct is not credulous.

## The modern stages

The current Roman Catholic process rests on John Paul II's apostolic constitution *Divinus Perfectionis Magister* (1983), which replaced the older adversarial trial with a documentary and historical-critical model, and on the instruction *Sanctorum Mater* (2007) governing diocesan inquiries. The Congregation (now Dicastery) for the Causes of Saints administers it.

| Stage | Title | What is required | Who decides |
| --- | --- | --- | --- |
| 1 | **Servant of God** | Normally at least five years after death (the pope may waive it); the local bishop opens an inquiry, gathers testimony, and collects all the candidate's writings | Local bishop, with Rome's consent |
| 2 | **Venerable** | A decree that the person practised the theological and cardinal virtues to a **heroic degree** — or, for a martyr, that death was accepted for the faith | The pope, on the Dicastery's recommendation |
| 3 | **Blessed** (beatification) | One verified miracle after death through the candidate's intercession. **Martyrs need no miracle for this step.** Public veneration is permitted, but restricted — typically to a diocese, region, or religious order | The pope |
| 4 | **Saint** (canonization) | A further verified miracle, occurring after beatification. Veneration is extended to the universal church and the name may enter the general calendar | The pope |

Refinements worth knowing:

- **Miracles are usually healings, and they are assessed medically first.** A board of physicians — who need not be Catholic — is asked a narrow question: is there a natural explanation for this recovery? Only if the medical panel finds none does the case go to theologians to judge whether it is attributable to the intercession invoked. The bar is deliberately high: the cure must be complete, lasting, and without adequate medical explanation.
- **Martyrdom short-circuits the virtue enquiry** but not the process.
- **A third path was added in 2017.** Francis's *Maiorem hac dilectionem* recognises the *oblatio vitae* — the free offering of one's life for others, accepted in charity, leading to death — as a distinct route, with its own requirements including a miracle for beatification.
- **Equivalent (equipollent) canonization** lets a pope extend the cult of a long-venerated figure to the whole church without the full process, where ancient veneration, a reputation for virtue or martyrdom, and continuous report of favours are established. Recent popes have used it more than their predecessors.
- **The pace changed dramatically in the late twentieth century.** John Paul II canonized and beatified more people than any predecessor — several hundred saints and well over a thousand blessed — partly through the 1983 streamlining and partly by deliberate policy, on the argument that the church needed examples from every nation and state of life rather than mostly clergy and religious from a handful of European countries.

Two theological notes, to avoid the two common misunderstandings:

**Canonization is not thought to make anyone holy or to get anyone into heaven.** Catholic teaching is that it *declares* what God has already done: this person is with God, and may be publicly venerated and invoked with confidence. The stages measure the church's certainty, not the person's progress.

**The infallibility of canonizations is a theological opinion, widely held but not itself a defined dogma.** Most Catholic theologians have held that a formal canonization is protected from error as a secondary object of the church's infallibility; the question has been discussed again in recent decades, particularly in connection with the faster modern pace.

## The East: glorification

The Orthodox churches do something parallel and describe it differently. The usual term is *glorification* (Greek ἁγιοκατάστασις; Slavonic *proslavlenie*), and the emphasis falls on recognition rather than declaration: God glorifies his saints, and the church acknowledges what has been shown. A local synod of bishops normally performs the act, so the Russian, Greek, Serbian, Romanian and other churches each glorify saints for themselves, with veneration spreading by reception rather than by promulgation.

The evidence looked for overlaps with the Western list without matching it: Orthodoxy of faith and life; a widespread and spontaneous veneration among the faithful; miracles or answered prayers; sometimes the incorruption of the relics, though this is treated as a sign rather than a requirement. There is no equivalent of the Promoter of the Faith, no fixed number of required miracles, and no formal intermediate rank corresponding to *Blessed* — though there are categories of saint (martyr, confessor, hierarch, venerable monastic, fool-for-Christ, passion-bearer, unmercenary) that describe the *kind* of holiness rather than a stage in a process.

The Oriental Orthodox churches, the Assyrian Church of the East, and the various Eastern Catholic churches each have their own practice, and none of them reproduces the Roman stages exactly.

## The Reformation: the word given back

The Reformers attacked the cult of the saints on three fronts, and it is worth separating them, because Protestants often assume all three were settled together and they were not.

**On invocation.** The Reformers argued that Scripture directs prayer to God through the one mediator (1 Timothy 2:5), that no biblical text instructs anyone to pray to a departed believer, and that the practice had in fact become for many people a substitute for approaching Christ. The Augsburg Confession (1530), Article XXI, concedes that the saints should be remembered so that we may imitate their faith and good works, but denies that Scripture teaches invoking them or seeking help from them. Calvin argues the case at length in the *Institutes* (III.20). The Church of England's Article XXII calls the "Romish doctrine concerning... Invocation of Saints" a fond thing vainly invented and grounded upon no warranty of Scripture.

**On merit and the treasury.** The Reformers rejected the idea of a store of superabundant merit accumulated by the saints and applicable to others, as cutting against justification by faith alone. This was the issue that produced the indulgence controversy and with it the Reformation itself.

**On the word itself.** This is the recovery, and it is the part most relevant to this document. The Reformers pressed the New Testament usage back into service: a saint is any Christian. Luther used the word this way constantly and provocatively, applying it to ordinary believers — and describing the Christian life not as a state achieved but as a movement, in a much-quoted passage from 1521: this life is not godliness but the process of becoming godly, not health but healing, not being but becoming, not rest but exercise; we are not yet what we shall be, but we are on the way.

What the Reformers did *not* do, for the most part, was abolish the calendar. The 1662 *Book of Common Prayer* retained a substantial list of commemorations. Lutheran churches kept saints' days as occasions for thanksgiving and example. Modern Anglican, Lutheran, and Methodist calendars have added figures without any canonization process — which is, in effect, the pre-medieval practice of local commemoration by acclamation, resumed without the legal apparatus.

The result today is that a Protestant may quite consistently say all three of these: every Christian is a saint; some Christians are conspicuously holy and worth studying; and there is no biblical warrant for a process that confers the title on a few, or for addressing prayer to them.

One further development is worth a line, because it is the most direct modern appropriation of the New Testament plural: the Church of Jesus Christ of Latter-day Saints took the apostolic designation for all believers as a name for its own membership. Whatever one makes of the theology, the usage is closer to Romans 1:7 than to the medieval calendar.

## What the two senses have in common

It would be easy to treat Parts I and II as simply opposed — the biblical sense against the institutional one. That is too quick, and misses the most interesting thing about the canonization process.

Look at what the process actually investigates. Not miracles first: **virtue**. And not virtue in the abstract, but the theological virtues (faith, hope, charity) and the cardinal virtues (prudence, justice, fortitude, temperance) practised to a *heroic degree* — meaning, in Lambertini's analysis, promptly, joyfully, consistently, under difficulty, over time. Strip the Latin and the legal form away, and the church is asking the question of Part I: *did progressive sanctification actually happen in this person, and can we show it?*

The stages, read this way, are not stages of becoming holy. They are stages of the church's **certainty** about a holiness that was completed at death. That is why the vocabulary of the process is evidentiary — inquiry, testimony, positio, decree — rather than developmental.

Where Protestants object is not usually to that investigation. It is to three consequences: that the outcome is a title restricted to a few, when the New Testament gives it to all; that the declared saint becomes an object of invocation, which the New Testament does not authorise; and that the standard applied — heroic virtue, verified by miracle — quietly implies that ordinary sanctification is second-class. The Second Vatican Council's fifth chapter of *Lumen Gentium* (1964), on the universal call to holiness, addresses the third objection from inside Catholicism and in strikingly New Testament terms: all the faithful of every rank and state are called to the fullness of the Christian life and to the perfection of charity, not merely those in religious life.

That chapter is, in effect, Part I rejoining Part II.

## How each tradition describes the growth

Every tradition affirms that Christians ought to become holier. They differ on the mechanism, the relation to justification, the possibility of completion, and what to do about the gap.

### Roman Catholic

Justification is understood not merely as the remission of sins but as sanctification and renewal of the inner person, by the infusion of grace and the theological virtues. The Council of Trent (Session 6, 1547) devotes a chapter to *the increase of justification received*: the justified, going from virtue to virtue, are renewed day by day and increase in the very justice they have received. Growth is therefore not a separate track running alongside justification but the increase of the same grace, cooperated with, and it is meritorious in the specific sense Trent defines — merit itself being God's gift crowning his own gifts. What remains unfinished at death is completed in purgatory, a doctrine that on this account is not about punishment so much as about final purification: nothing unclean enters God's presence, and most people die with something still owing. The *Catechism of the Catholic Church* (1989–2029, 2012–2016) sets this out, and *Lumen Gentium* V insists the call is universal.

### Eastern Orthodox

Orthodoxy resists dividing the process into justification and sanctification at all and speaks of one movement: **theosis**, deification, the creature becoming by grace what God is by nature. Its charter text is 2 Peter 1:4 — *partakers of the divine nature* — and its slogan is Athanasius's, that he became man that we might be made divine. Gregory Palamas's distinction between God's essence (forever unknowable) and his energies (genuinely communicated) is what keeps this from pantheism: the saint does not become God in essence, but really participates in God's uncreated life. Growth is **synergy**, a cooperation of divine grace and human freedom in which grace is always first, and the path is ascetic and sacramental — the prayer of the heart, fasting, the Jesus Prayer, confession, the Eucharist, obedience to a spiritual father. The *Philokalia*, compiled in the eighteenth century from a thousand years of monastic writing, is its practical manual.

### Lutheran

Lutherans hold justification and sanctification apart with unusual firmness, because the whole Reformation turned on not letting the second be smuggled into the first as a condition. The believer is *simul iustus et peccator*, at once righteous and a sinner — righteous in Christ, entirely and now; sinful in himself, until death. Good works follow justification necessarily but contribute nothing to it. The Formula of Concord (1577) defends a use of the law for believers — to show them what pleases God — while insisting that the motive power is the gospel, not the law. The characteristic Lutheran pastoral move is to send the struggling Christian back to their baptism rather than to their progress.

### Reformed

The Reformed confessions treat sanctification as a distinct work following inseparably from justification. The Westminster Confession (1646), chapter XIII, is the classic statement: the dominion of sin is destroyed and the believer is enabled more and more to die to sin and live to righteousness, yet remnants of corruption abide in every part, producing a continual and irreconcilable war; in which war corruption may for a time much prevail, yet through the continual supply of strength from the sanctifying Spirit the regenerate part overcomes, and the saints grow in grace, perfecting holiness in the fear of God. The Heidelberg Catechism, asked whether the converted can keep the commandments perfectly, answers: no — even the holiest have only a small beginning of this obedience. The characteristic practical literature is on **mortification** (the active killing of sin) and **vivification** (the cultivation of its opposite): John Owen's *Of the Mortification of Sin in Believers* (1656), with its famous instruction to be killing sin or it will be killing you, and J. C. Ryle's *Holiness* (1877).

### Wesleyan and Holiness

Wesley accepted the Reformation on justification and then pressed further on sanctification than any of the Reformers would. He taught that after justification a believer may receive, by faith, a second definite work — entire sanctification, Christian perfection, perfect love — in which the heart is cleansed from sin properly so called and filled with love to God and neighbour. He defined sin narrowly (a voluntary transgression of a known law), explicitly excluded freedom from ignorance, mistake, infirmity, and temptation, held that the state could be lost, and insisted growth continued afterward. His *A Plain Account of Christian Perfection* is the primary document. In nineteenth-century America the teaching spread through camp meetings and the writing of Phoebe Palmer, whose *altar theology* made the second blessing more immediately accessible, and produced the Holiness denominations; from that soil, at the beginning of the twentieth century, Pentecostalism grew, adding baptism in the Holy Spirit with the evidence of tongues as a further distinct experience.

### Keswick and the "higher life"

From the Keswick Convention (from 1875) came a distinct English and American teaching: the believer's problem is self-effort, and victory comes by surrender and faith rather than struggle — "let go and let God." It produced enormous missionary energy and much devotional literature. It also drew sustained criticism: B. B. Warfield's *Perfectionism* argued that it misread the New Testament's calls to effort, and J. I. Packer, who had tried to live by it as a young man, wrote afterward that its promise of victory through passivity had driven him to despair before he found the Puritans on mortification. The debate matters because the Keswick instinct — that effort is unspiritual — recurs constantly in popular teaching under other names.

### Contemporary evangelical debate

The recurring modern argument is about the place of effort and of the law in sanctification. One side warns that exhorting Christians to work at holiness slides into a performance religion and that the remedy for sin is always a deeper grasp of justification; the other answers that the New Testament plainly commands effort, that Philippians 2:12 means what it says, and that grace produces work rather than replacing it. A parallel recovery has emphasised **union with Christ** as the category that holds justification and sanctification together: both are benefits of being joined to Christ, so neither can be pitted against the other and neither is the ground of the other.

---

## Where the real disagreements are

| | **Catholic** | **Orthodox** | **Lutheran** | **Reformed** | **Wesleyan** |
| --- | --- | --- | --- | --- | --- |
| **Relation to justification** | Sanctification is included in justification; grace infused | Not sharply distinguished; one movement of theosis | Sharply distinct; sanctification follows, never grounds | Distinct but inseparable; both from union with Christ | Distinct; sanctification pressed further than the Reformers |
| **Can it be completed before death?** | Rarely, by extraordinary grace; normally completed in purgatory | The saints attain great heights; completion is eschatological | No | No | Yes — entire sanctification, as defined |
| **Is it meritorious?** | Yes, in the defined sense: God crowning his own gifts | Language of merit is largely avoided; synergy preferred | No | No | No |
| **Chief means** | Sacraments, grace, cooperation, charity | Sacraments, asceticism, prayer of the heart, obedience | Word and sacrament; return to baptism | Word, Spirit, prayer, church, mortification | Word, Spirit, means of grace, and the second blessing |
| **What finishes it** | Purgatory, then the beatific vision | Union with God, unending | Death and resurrection | Glorification | Glorification |
| **Characteristic danger** | Treating grace as a quantity to be accumulated | Treating the path as for monks | Treating sanctification as optional | Introspection that undermines assurance | Claiming more than is true |
| **Characteristic strength** | Takes real change with full seriousness | Sets the goal as high as Scripture does | Protects the conscience absolutely | Realism about indwelling sin | Expects God to do something now |

Two observations across the table.

**The disagreements are mostly about the relation to justification, not about the necessity of holiness.** No tradition in the table says a Christian may remain unchanged. What they are protecting differs: the Lutheran is protecting the troubled conscience from ever having to look at itself for comfort; the Catholic is protecting the reality of the change God works; the Wesleyan is protecting the expectation that God does something now; the Reformed is protecting both the necessity of the fight and the certainty of its outcome.

**Each tradition's characteristic danger is its characteristic strength overrun.** That is worth remembering before adopting any of them as a slogan.

---
---

# Part III — What It Means for You

## Start with what is settled

Before anything in this part can be used, four things have to be in place, and all four are agreed by every tradition described in Part II:

1. **You do not become a saint by becoming holy.** You are made one by being joined to Christ, and the New Testament addresses you as one from that point forward.
2. **God's acceptance of you does not fluctuate with your week.** Definitive sanctification is past tense and complete. Progress and failure move the second tense, not the first.
3. **You are nevertheless commanded to change**, and the command is not optional, softened, or aimed at somebody more advanced than you.
4. **The work will be finished, and not by you.** *Faithful is he that calleth you, who also will do it* (1 Thessalonians 5:24).

Anyone who holds 1, 2, and 4 but drops 3 becomes complacent. Anyone who holds 3 without 1, 2, and 4 becomes exhausted. Both failures are extremely common and neither is necessary.

## Are you a saint?

The New Testament's test is not a threshold of behaviour. It is whether you are in Christ — *sanctified in Christ Jesus* (1 Corinthians 1:2), *them that are sanctified by God the Father, and preserved in Jesus Christ, and called* (Jude 1:1). If that is true of you, the title is yours today, and it was yours on your worst day last year.

Three consequences follow immediately, and each removes a familiar anxiety:

- **You cannot be a better or worse saint.** You can be a more or less mature one. Those are different measurements, and confusing them is the source of a great deal of unnecessary misery.
- **Nobody canonizes you and nobody can withhold it.** The word in the New Testament is on the envelope, not on a certificate.
- **The people in your congregation who irritate you are also saints.** Paul's use of the word is at its most pointed when he applies it to people in the middle of behaving badly, and he applies it to them precisely when telling them to stop.

## How to tell whether you are growing

Scripture gives real marks, and they are almost all relational rather than internal. Note how few of them are about feelings, and how many of them other people would notice before you did.

| Mark | Text | The question to ask |
| --- | --- | --- |
| **Love for other Christians, including the inconvenient ones** | 1 John 3:14; John 13:35 | Am I more willing than I was to be put out for people I did not choose? |
| **Hatred of your own sin, not just its consequences** | Romans 7:15–24; 2 Corinthians 7:10–11 | When I sin now, do I grieve, or only calculate the damage? |
| **Quicker repentance** | 1 John 1:9; Psalm 32:3–5 | How long is it now between the sin and the confession? Weeks? Hours? |
| **Fruit of the Spirit in ordinary conditions** | Galatians 5:22–23 | Am I more patient with the same people who have always tried my patience? |
| **Speech** | James 3:2; Ephesians 4:29; Colossians 3:8 | Fewer cutting remarks? Less gossip? Fewer things I wish I had not said? |
| **Endurance without bitterness** | Romans 5:3–5; James 1:2–4 | Has trouble made me kinder or harder over the last five years? |
| **Generosity** | 2 Corinthians 8:1–7; 1 Timothy 6:17–19 | Is my giving increasing as my income does, or only my standard of living? |
| **Treatment of people who can do nothing for you** | Leviticus 19:9–18; James 2:1–9 | Am I the same person to a waiter as to a client? |
| **Hunger for Scripture and prayer** | 1 Peter 2:2; Psalm 119:97 | Do I go to it as food, or only as duty and emergency? |
| **Response to correction** | Proverbs 9:8–9; 15:31–32 | When somebody tells me I am wrong, what happens in the first five seconds? |
| **Humility about your own progress** | Philippians 3:12–14; Ephesians 3:8 | Would I describe myself as someone who has largely got this sorted? |

Four rules for using that table honestly.

**Measure over years, not days.** Sanctification is not perceptible at daily resolution, any more than a child's height is. Compare yourself with yourself five years ago, and expect the comparison to be noisy.

**Ask somebody.** Most of the marks in the table are more visible from the outside than the inside. A spouse, an old friend, or a fellow church member who has known you a long time will answer more accurately than your own introspection — and their answer is data, not an insult.

**Direction beats position.** A person of violent temperament who has become merely irritable has travelled further than a placid person who has stayed placid. God grades on movement from a starting point he knows and you do not.

**The last row is a check on the other ten.** If the honest answer to the humility question is yes, something has gone wrong, whatever the other rows say.

## Why mature Christians think they are getting worse

This is nearly universal among people far along, and it is not a malfunction. Paul's self-descriptions get *worse* as his ministry goes on: least of the apostles (1 Corinthians, mid-50s), less than the least of all saints (Ephesians, early 60s), chief of sinners (1 Timothy, later still, in the present tense — *of whom I am chief*). Either the greatest missionary in history was deteriorating, or something else explains it.

The something else has three parts.

**The light increases.** Sanctification is largely a matter of seeing more of God, and the more of him you see, the more of yourself you see by contrast. Isaiah is undone in the temple (Isaiah 6:5) and Job repents in dust and ashes (Job 42:5–6) — both after seeing God, not after failing.

**The standard internalises.** A new Christian measures by conduct; a mature one has learned that the commandments reach motive, and so is now failing a test they did not previously know was being administered.

**Old sins go quiet and new ones surface.** The disciplined person stops committing the disorderly sins and starts committing the respectable ones. Pride, self-satisfaction, censoriousness, and contempt are the characteristic sins of the spiritually advanced, and they are hard to see precisely because they feel like discernment.

The practical implication: **a growing sense of your own sinfulness, combined with a growing love for Christ, is evidence of progress, not of decline.** The danger sign is the opposite combination — a sense that you are doing rather well, coupled with impatience toward Christians who are not.

## Plateau, backsliding, and the difference

Not every flat stretch is a fall. Distinguishing them matters, because the remedies differ.

**A plateau** looks like: no dramatic sin; prayer dry; Scripture flat; church attended without much engagement; a general sense of going through the motions. Causes are frequently physical or circumstantial — exhaustion, grief, a new baby, illness, depression, overwork. Elijah's collapse in 1 Kings 19 is answered first with food and sleep, twice, before any word from God. The New Testament nowhere treats a dry season as apostasy, and the Psalms are full of them.

**Backsliding** looks different: a known sin being managed rather than fought; withdrawal from Christians who would ask questions; the conscience arguing cases it used to concede; prayer avoided rather than difficult. The distinguishing mark is not intensity of feeling but **direction of the will** — whether you still want to be rid of the sin.

| | Plateau | Backsliding |
| --- | --- | --- |
| Known sin | Fought, unsuccessfully or wearily | Protected, excused, hidden |
| Other Christians | Missed | Avoided |
| Conscience | Tender, often oversensitive | Increasingly quiet |
| Prayer | Hard | Unwelcome |
| Response to this list | Fear | Irritation |
| First remedy | Rest, food, patience, means of grace, time | Confession to God and to a person, and a change of course |

The one thing not to do with either is to face it alone. Both remedies in the table's last row involve another human being.

## The practices, in the proportion Scripture gives them

Devotional books have their own hierarchy. Scripture's is not the same, and it is worth noticing the difference.

**Very heavily emphasised:**

- **Scripture, taken regularly and in quantity.** Named more often than any other means.
- **Prayer, including with others.** The New Testament's prayers are strikingly corporate; the model prayer is in the plural throughout.
- **The gathered church.** Not optional in the New Testament, and named as a means of your own maturing (Ephesians 4:11–16; Hebrews 10:24–25).
- **Obedience in the specific matters already known to you.** *If ye know these things, happy are ye if ye do them* (John 13:17).
- **Confession** — to God always, and to other people where the New Testament directs it (James 5:16).
- **Generosity and care for the poor**, which the Bible treats as a spiritual discipline and most modern devotional literature does not.

**Present but less emphasised than popular practice suggests:**

- **Fasting.** Assumed (*when ye fast*, Matthew 6:16) rather than commanded, and never systematised. See [`fasting-in-the-bible.md`](fasting-in-the-bible.md) in this repository.
- **Solitude and silence.** Modelled by Christ, rarely commanded.

**Absent from Scripture as prescribed methods**, though many Christians have found them useful and none is forbidden: the quiet time as a fixed daily format, journalling, retreats, spiritual direction, rules of life, devotional reading plans. They are tools, not commands, and treating them as the measure of progress reliably produces guilt without holiness.

The point of the distinction is not to discourage anyone's practice. It is that if you are doing the six heavily emphasised things and none of the optional ones, you are doing what Scripture asks; and if you are doing all the optional ones and none of the six, you are not.

## The sin you will fight all your life

Most Christians have one — a temper, a particular appetite, cowardice, envy, a tongue, self-pity — that never fully goes away. Hebrews 12:1 has a phrase for it: *the sin which doth so easily beset us*.

Four things Scripture and long experience say about it.

**Reduced frequency is real progress.** A sin that used to happen weekly and now happens twice a year has not been defeated, but something has changed, and it is not nothing. God knows the difference even when you cannot feel it.

**The fight itself is evidence.** *The flesh lusteth against the Spirit, and the Spirit against the flesh* (Galatians 5:17) describes a battlefield, and battlefields require two armies. A person with no conflict has either finished — which Scripture does not expect here — or stopped fighting.

**Fight it with the ordinary means, not a special technique.** Killing sin in the New Testament is not an esoteric skill. It is confession, avoidance of the occasions, honesty with someone who will ask again next week, filling the space with something better, and asking God for help repeatedly.

**Do not negotiate with it.** The vocabulary Scripture uses is violent — mortify, crucify, cut off, flee. There is no text anywhere that recommends managing a besetting sin at a tolerable level.

## Addiction, compulsion, and illness

Three distinctions worth making explicitly, because bad teaching here does real damage.

**Temptation is not sin.** Christ was tempted (Hebrews 4:15). An intrusive thought, a craving, an unwanted desire, or an impulse resisted is not a fall, and treating it as one produces despair and a paralysing scrupulosity — which is itself a recognised spiritual affliction, not a sign of tenderness.

**Depression, anxiety, and compulsive disorders are not simply failures of sanctification.** Scripture shows godly people in profound darkness without ever suggesting the darkness proves sin — Elijah under the juniper tree, Job, Jeremiah, the psalmist of Psalm 88, and Christ himself in Gethsemane. Treating an illness as a sin makes the ill person's suffering worse and their recovery less likely. Growth in holiness and improvement in mental health are related but distinct, and neither is a proxy for the other.

**Addiction usually requires help beyond the ordinary means.** Nothing in Scripture forbids a Christian from using medicine, professional treatment, or a structured programme, and nothing in the doctrine of sanctification suggests that God's ordinary way of delivering people is without instruments. The New Testament's own means include other people; extending that to people with training is not a failure of faith.

What sanctification does promise in every one of these cases is not the removal of the condition but the presence of God within it, and the slow forming of Christ in a person whose circumstances may not improve at all.

## When you have hurt somebody

The New Testament will not let repentance stay inward. Zacchaeus repays fourfold (Luke 19:8); the thief is to steal no more *but rather let him labour... that he may have to give* (Ephesians 4:28); worship is to be interrupted to go and be reconciled with the brother who has something against you (Matthew 5:23–24); confession is to be made to one another (James 5:16).

Three practical notes. Confess the thing you actually did, without the softening clauses that turn an apology into a defence. Make restitution where restitution is possible, and where it is not, say so plainly rather than substituting words for it. And do not require the other person's forgiveness as the price of your peace — that is asking them to do the work of your conscience.

## What to do with the canonized saints

Readers of this document will be in different churches, and the honest answer differs.

**If you are Catholic or Orthodox**, the practice is yours and this document has no business relitigating it. The observation worth keeping from Part I is the one your own tradition has emphasised most strongly in the last sixty years: the call to holiness is universal, the canonized are exemplars and not a separate species, and their usefulness to you lies mostly in the ordinary parts of their lives rather than the extraordinary ones.

**If you are Protestant**, you are free to do what Christians did for the first three centuries: read the lives, learn from them, be provoked by them, and pray to God alone. The lives of exemplary Christians are among the most useful things you can read, precisely because holiness is more easily caught than analysed, and because a biography shows what the doctrine of progressive sanctification looks like at ground level over sixty years. What Article XXII and the Augsburg Confession object to is invocation and merit, not admiration or imitation.

**For everyone**, there is a specific danger in reading the lives of exceptional Christians, and it is worth naming: they are selected for being exceptional, and comparing your interior life to somebody else's edited biography is a reliable way to become discouraged about a perfectly normal rate of growth. Read them the way you would read accounts of any craft practised at the highest level — for the direction, not for the score.

## What finishes the work

Not you, and not this life.

> **1 John 3:2** — Beloved, now are we the sons of God, and it doth not yet appear what we shall be: but we know that, when he shall appear, we shall be like him; for we shall see him as he is.

> **Philippians 1:6** — Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ:

> **Hebrews 12:23** — ...and to the spirits of just men made perfect,

Christian traditions differ on what happens in between — whether there is a purification after death, as Catholic teaching holds, or whether the change is immediate at death and completed at the resurrection, as Protestant confessions hold. See [`praying-for-the-dead.md`](praying-for-the-dead.md) in this repository for that argument set out at length. They do not differ on the outcome: what is unfinished will be finished, by God, in the presence of Christ, and the sight of him is what does it.

This is the answer to the anxiety that this whole subject generates. You are not required to complete your own sanctification, or to reach any particular point by any particular age. You are required to keep moving in a direction, by ordinary means, with other people, from a standing that was settled before you started and does not depend on how far you get.

## One page to keep

- **You are a saint now.** Not becoming one. The New Testament puts the word on the envelope.
- **You are also being sanctified now.** Both clauses of Hebrews 10:14 are true of you simultaneously.
- **The command follows the fact.** Become what you are; never become in order to be.
- **God works, therefore you work** — not instead of you, and not so that you need not.
- **The means are ordinary**: Scripture, prayer, the church, obedience, confession, hardship, hope. There is no advanced method.
- **Growth is slow, uneven, and mostly invisible to you.** Measure in years. Ask somebody who knows you.
- **Feeling worse about yourself while loving Christ more is a sign of progress**, not decline.
- **Your besetting sin is not evidence that you are unsaved.** Fighting it is evidence that you are.
- **There are no degrees of belonging** — only degrees of maturity, and God knows your starting point.
- **He will finish it.** *Faithful is he that calleth you, who also will do it.*

---
---

# Appendices

## A. Every New Testament occurrence of "saints"

Every verse in the New Testament containing the word *saints*, generated from [`kjv/kjv.txt`](kjv/kjv.txt):

```sh
grep -w 'saints' kjv/kjv.txt
```

There are **61** of them, in **15** books. Every one translates ἅγιος (*hagios*, [G0040](original-languages/lexicons/strongs-greek.tsv)) — with one textual exception noted at the end.

### Matthew

- **27:52** — And the graves were opened; and many bodies of the saints which slept arose,

### Acts

- **9:13** — Then Ananias answered, Lord, I have heard by many of this man, how much evil he hath done to thy saints at Jerusalem:
- **9:32** — And it came to pass, as Peter passed throughout all quarters, he came down also to the saints which dwelt at Lydda.
- **9:41** — And he gave her his hand, and lifted her up, and when he had called the saints and widows, presented her alive.
- **26:10** — Which thing I also did in Jerusalem: and many of the saints did I shut up in prison, having received authority from the chief priests; and when they were put to death, I gave my voice against them.

### Romans

- **1:7** — To all that be in Rome, beloved of God, called to be saints: Grace to you and peace from God our Father, and the Lord Jesus Christ.
- **8:27** — And he that searcheth the hearts knoweth what is the mind of the Spirit, because he maketh intercession for the saints according to the will of God.
- **12:13** — Distributing to the necessity of saints; given to hospitality.
- **15:25** — But now I go unto Jerusalem to minister unto the saints.
- **15:26** — For it hath pleased them of Macedonia and Achaia to make a certain contribution for the poor saints which are at Jerusalem.
- **15:31** — That I may be delivered from them that do not believe in Judaea; and that my service which I have for Jerusalem may be accepted of the saints;
- **16:2** — That ye receive her in the Lord, as becometh saints, and that ye assist her in whatsoever business she hath need of you: for she hath been a succourer of many, and of myself also.
- **16:15** — Salute Philologus, and Julia, Nereus, and his sister, and Olympas, and all the saints which are with them.

### 1 Corinthians

- **1:2** — Unto the church of God which is at Corinth, to them that are sanctified in Christ Jesus, called to be saints, with all that in every place call upon the name of Jesus Christ our Lord, both theirs and ours:
- **6:1** — Dare any of you, having a matter against another, go to law before the unjust, and not before the saints?
- **6:2** — Do ye not know that the saints shall judge the world? and if the world shall be judged by you, are ye unworthy to judge the smallest matters?
- **14:33** — For God is not the author of confusion, but of peace, as in all churches of the saints.
- **16:1** — Now concerning the collection for the saints, as I have given order to the churches of Galatia, even so do ye.
- **16:15** — I beseech you, brethren, (ye know the house of Stephanas, that it is the firstfruits of Achaia, and that they have addicted themselves to the ministry of the saints,)

### 2 Corinthians

- **1:1** — Paul, an apostle of Jesus Christ by the will of God, and Timothy our brother, unto the church of God which is at Corinth, with all the saints which are in all Achaia:
- **8:4** — Praying us with much intreaty that we would receive the gift, and take upon us the fellowship of the ministering to the saints.
- **9:1** — For as touching the ministering to the saints, it is superfluous for me to write to you:
- **9:12** — For the administration of this service not only supplieth the want of the saints, but is abundant also by many thanksgivings unto God;
- **13:13** — All the saints salute you.

### Ephesians

- **1:1** — Paul, an apostle of Jesus Christ by the will of God, to the saints which are at Ephesus, and to the faithful in Christ Jesus:
- **1:15** — Wherefore I also, after I heard of your faith in the Lord Jesus, and love unto all the saints,
- **1:18** — The eyes of your understanding being enlightened; that ye may know what is the hope of his calling, and what the riches of the glory of his inheritance in the saints,
- **2:19** — Now therefore ye are no more strangers and foreigners, but fellowcitizens with the saints, and of the household of God;
- **3:8** — Unto me, who am less than the least of all saints, is this grace given, that I should preach among the Gentiles the unsearchable riches of Christ;
- **3:18** — May be able to comprehend with all saints what is the breadth, and length, and depth, and height;
- **4:12** — For the perfecting of the saints, for the work of the ministry, for the edifying of the body of Christ:
- **5:3** — But fornication, and all uncleanness, or covetousness, let it not be once named among you, as becometh saints;
- **6:18** — Praying always with all prayer and supplication in the Spirit, and watching thereunto with all perseverance and supplication for all saints;

### Philippians

- **1:1** — Paul and Timotheus, the servants of Jesus Christ, to all the saints in Christ Jesus which are at Philippi, with the bishops and deacons:
- **4:22** — All the saints salute you, chiefly they that are of Caesar's household.

### Colossians

- **1:2** — To the saints and faithful brethren in Christ which are at Colosse: Grace be unto you, and peace, from God our Father and the Lord Jesus Christ.
- **1:4** — Since we heard of your faith in Christ Jesus, and of the love which ye have to all the saints,
- **1:12** — Giving thanks unto the Father, which hath made us meet to be partakers of the inheritance of the saints in light:
- **1:26** — Even the mystery which hath been hid from ages and from generations, but now is made manifest to his saints:

### 1 Thessalonians

- **3:13** — To the end he may stablish your hearts unblameable in holiness before God, even our Father, at the coming of our Lord Jesus Christ with all his saints.

### 2 Thessalonians

- **1:10** — When he shall come to be glorified in his saints, and to be admired in all them that believe (because our testimony among you was believed) in that day.

### 1 Timothy

- **5:10** — Well reported of for good works; if she have brought up children, if she have lodged strangers, if she have washed the saints' feet, if she have relieved the afflicted, if she have diligently followed every good work.

### Philemon

- **1:5** — Hearing of thy love and faith, which thou hast toward the Lord Jesus, and toward all saints;
- **1:7** — For we have great joy and consolation in thy love, because the bowels of the saints are refreshed by thee, brother.

### Hebrews

- **6:10** — For God is not unrighteous to forget your work and labour of love, which ye have shewed toward his name, in that ye have ministered to the saints, and do minister.
- **13:24** — Salute all them that have the rule over you, and all the saints. They of Italy salute you.

### Jude

- **1:3** — Beloved, when I gave all diligence to write unto you of the common salvation, it was needful for me to write unto you, and exhort you that ye should earnestly contend for the faith which was once delivered unto the saints.
- **1:14** — And Enoch also, the seventh from Adam, prophesied of these, saying, Behold, the Lord cometh with ten thousands of his saints,

### Revelation

- **5:8** — And when he had taken the book, the four beasts and four and twenty elders fell down before the Lamb, having every one of them harps, and golden vials full of odours, which are the prayers of saints.
- **8:3** — And another angel came and stood at the altar, having a golden censer; and there was given unto him much incense, that he should offer it with the prayers of all saints upon the golden altar which was before the throne.
- **8:4** — And the smoke of the incense, which came with the prayers of the saints, ascended up before God out of the angel's hand.
- **11:18** — And the nations were angry, and thy wrath is come, and the time of the dead, that they should be judged, and that thou shouldest give reward unto thy servants the prophets, and to the saints, and them that fear thy name, small and great; and shouldest destroy them which destroy the earth.
- **13:7** — And it was given unto him to make war with the saints, and to overcome them: and power was given him over all kindreds, and tongues, and nations.
- **13:10** — He that leadeth into captivity shall go into captivity: he that killeth with the sword must be killed with the sword. Here is the patience and the faith of the saints.
- **14:12** — Here is the patience of the saints: here are they that keep the commandments of God, and the faith of Jesus.
- **15:3** — And they sing the song of Moses the servant of God, and the song of the Lamb, saying, Great and marvellous are thy works, Lord God Almighty; just and true are thy ways, thou King of saints.
- **16:6** — For they have shed the blood of saints and prophets, and thou hast given them blood to drink; for they are worthy.
- **17:6** — And I saw the woman drunken with the blood of the saints, and with the blood of the martyrs of Jesus: and when I saw her, I wondered with great admiration.
- **18:24** — And in her was found the blood of prophets, and of saints, and of all that were slain upon the earth.
- **19:8** — And to her was granted that she should be arrayed in fine linen, clean and white: for the fine linen is the righteousness of saints.
- **20:9** — And they went up on the breadth of the earth, and compassed the camp of the saints about, and the beloved city: and fire came down from God out of heaven, and devoured them.

**The exception.** At Revelation 15:3 the KJV's *thou King of saints* follows Scrivener's Textus Receptus, which reads ὁ βασιλεὺς τῶν ἁγίων. The other editions in this repository do not: the Byzantine text reads τῶν ἐθνῶν, *King of nations*, and the SBLGNT reads τῶν αἰώνων, *King of the ages*. The line is a quotation of Jeremiah 10:7, which has *King of the nations*. The variant can be seen directly:

```sh
grep '^Revelation 15:3 ' original-languages/greek/tr-scrivener.txt
grep '^Revelation 15:3 ' original-languages/greek/byzantine.txt
grep '^Revelation 15:3 ' original-languages/greek/sblgnt.txt
```

**Singular.** The New Testament uses the singular exactly once, and not as a title: *Salute every saint in Christ Jesus* (Philippians 4:21).

---

## B. Every Old Testament occurrence of "saints"

Every verse in the Old Testament containing the word *saints*, with the Hebrew or Aramaic word underneath it, from [`original-languages/hebrew/wlc-words.tsv`](original-languages/hebrew/wlc-words.tsv).

There are **34**, in **9** books, and they do not all translate the same word — which is why the Old Testament's *saints* are sometimes the covenant-faithful, sometimes angels, and sometimes a besieged people awaiting a verdict.

| Hebrew | Sense | Verses |
| --- | --- | --- |
| חָסִיד *ḥāsîd* (H2623) | loyal, devoted, bound in covenant love | 19 |
| קָדוֹשׁ *qādôš* (H6918) | holy one — God, an angel, or a consecrated person | 9 |
| קַדִּישׁ *qaddîš* (H6922) | holy one (Aramaic) | 5 |
| קֹדֶשׁ *qōdeš* (H6944) | holiness; a holy thing | 1 |

### Deuteronomy

- **33:2** — *qōdeš* — And he said, The LORD came from Sinai, and rose up from Seir unto them; he shined forth from mount Paran, and he came with ten thousands of saints: from his right hand went a fiery law for them.
- **33:3** — *qādôš* — Yea, he loved the people; all his saints are in thy hand: and they sat down at thy feet; every one shall receive of thy words.

### 1 Samuel

- **2:9** — *ḥāsîd* — He will keep the feet of his saints, and the wicked shall be silent in darkness; for by strength shall no man prevail.

### 2 Chronicles

- **6:41** — *ḥāsîd* — Now therefore arise, O LORD God, into thy resting place, thou, and the ark of thy strength: let thy priests, O LORD God, be clothed with salvation, and let thy saints rejoice in goodness.

### Job

- **5:1** — *qādôš* — Call now, if there be any that will answer thee; and to which of the saints wilt thou turn?
- **15:15** — *qādôš* — Behold, he putteth no trust in his saints; yea, the heavens are not clean in his sight.

### Psalms

- **16:3** — *qādôš* — But to the saints that are in the earth, and to the excellent, in whom is all my delight.
- **30:4** — *ḥāsîd* — Sing unto the LORD, O ye saints of his, and give thanks at the remembrance of his holiness.
- **31:23** — *ḥāsîd* — O love the LORD, all ye his saints: for the LORD preserveth the faithful, and plentifully rewardeth the proud doer.
- **34:9** — *qādôš* — O fear the LORD, ye his saints: for there is no want to them that fear him.
- **37:28** — *ḥāsîd* — For the LORD loveth judgment, and forsaketh not his saints; they are preserved for ever: but the seed of the wicked shall be cut off.
- **50:5** — *ḥāsîd* — Gather my saints together unto me; those that have made a covenant with me by sacrifice.
- **52:9** — *ḥāsîd* — I will praise thee for ever, because thou hast done it: and I will wait on thy name; for it is good before thy saints.
- **79:2** — *ḥāsîd* — The dead bodies of thy servants have they given to be meat unto the fowls of the heaven, the flesh of thy saints unto the beasts of the earth.
- **85:8** — *ḥāsîd* — I will hear what God the LORD will speak: for he will speak peace unto his people, and to his saints: but let them not turn again to folly.
- **89:5** — *qādôš* — And the heavens shall praise thy wonders, O LORD: thy faithfulness also in the congregation of the saints.
- **89:7** — *qādôš* — God is greatly to be feared in the assembly of the saints, and to be had in reverence of all them that are about him.
- **97:10** — *ḥāsîd* — Ye that love the LORD, hate evil: he preserveth the souls of his saints; he delivereth them out of the hand of the wicked.
- **116:15** — *ḥāsîd* — Precious in the sight of the LORD is the death of his saints.
- **132:9** — *ḥāsîd* — Let thy priests be clothed with righteousness; and let thy saints shout for joy.
- **132:16** — *ḥāsîd* — I will also clothe her priests with salvation: and her saints shall shout aloud for joy.
- **145:10** — *ḥāsîd* — All thy works shall praise thee, O LORD; and thy saints shall bless thee.
- **148:14** — *ḥāsîd* — He also exalteth the horn of his people, the praise of all his saints; even of the children of Israel, a people near unto him. Praise ye the LORD.
- **149:1** — *ḥāsîd* — Praise ye the LORD. Sing unto the LORD a new song, and his praise in the congregation of saints.
- **149:5** — *ḥāsîd* — Let the saints be joyful in glory: let them sing aloud upon their beds.
- **149:9** — *ḥāsîd* — To execute upon them the judgment written: this honour have all his saints. Praise ye the LORD.

### Proverbs

- **2:8** — *ḥāsîd* — He keepeth the paths of judgment, and preserveth the way of his saints.

### Daniel

- **7:18** — *qaddîš* — But the saints of the most High shall take the kingdom, and possess the kingdom for ever, even for ever and ever.
- **7:21** — *qaddîš* — I beheld, and the same horn made war with the saints, and prevailed against them;
- **7:22** — *qaddîš* — Until the Ancient of days came, and judgment was given to the saints of the most High; and the time came that the saints possessed the kingdom.
- **7:25** — *qaddîš* — And he shall speak great words against the most High, and shall wear out the saints of the most High, and think to change times and laws: and they shall be given into his hand until a time and times and the dividing of time.
- **7:27** — *qaddîš* — And the kingdom and dominion, and the greatness of the kingdom under the whole heaven, shall be given to the people of the saints of the most High, whose kingdom is an everlasting kingdom, and all dominions shall serve and obey him.

### Hosea

- **11:12** — *qādôš* — Ephraim compasseth me about with lies, and the house of Israel with deceit: but Judah yet ruleth with God, and is faithful with the saints.

### Zechariah

- **14:5** — *qādôš* — And ye shall flee to the valley of the mountains; for the valley of the mountains shall reach unto Azal: yea, ye shall flee, like as ye fled from before the earthquake in the days of Uzziah king of Judah: and the LORD my God shall come, and all the saints with thee.

**On the verse numbers.** Hebrew counts a psalm's superscription as verse 1 (and Psalm 52's two-line superscription as verses 1–2), so the KJV's number runs one or two behind the Hebrew wherever a psalm is titled; and KJV Hosea 11:12 is Hebrew Hosea 12:1. The lookups above account for both:

```sh
grep -P '^Psalms 30:5\t' original-languages/hebrew/wlc-words.tsv
grep -P '^Hosea 12:1\t' original-languages/hebrew/wlc-words.tsv
```

**Singular.** Three verses use it: Aaron is *the saint of the LORD* (Psalms 106:16), and in Daniel 8:13 *one saint* speaks to *another saint* — angels, in a vision.

---

## C. The holiness word families

### The Hebrew family

| Strong's | Word | Sense | KJV renderings |
| --- | --- | --- | --- |
| H6942 | קָדַשׁ *qādaš* | to be, make, pronounce, or treat as holy | sanctify, hallow, consecrate, dedicate, be holy, prepare, proclaim, purify |
| H6944 | קֹדֶשׁ *qōdeš* | holiness; a sacred place or thing | holiness, holy, most holy, sanctuary, hallowed thing, dedicated thing, saint |
| H6918 | קָדוֹשׁ *qādôš* | sacred; as a noun, a holy one | holy, Holy One, saint |
| H6922 | קַדִּישׁ *qaddîš* | holy one (Aramaic) | holy one, saint |
| H2623 | חָסִיד *ḥāsîd* | loyal in covenant love | saint, godly, holy one, merciful |
| H2616 | חָסַד *ḥāsad* | to be kind; the root behind *ḥāsîd* | shew self merciful, put to shame |

```sh
grep -P '^H(6918|6942|6944|2623)\t' original-languages/lexicons/strongs-hebrew.tsv
```

### The Greek family

| Strong's | Word | Sense | KJV renderings | NT count |
| --- | --- | --- | --- | --- |
| G0040 | ἅγιος *hagios* | sacred, set apart, pure | holy, saint, most holy | 240 |
| G0037 | ἁγιάζω *hagiazō* | to make holy, consecrate | sanctify, hallow, be holy | 29 |
| G0038 | ἁγιασμός *hagiasmos* | holy-making, as process or result | sanctification, holiness | 10 |
| G0042 | ἁγιωσύνη *hagiōsynē* | holiness as a quality | holiness | 3 |
| G0041 | ἁγιότης *hagiotēs* | holiness as a state | holiness | 1 |
| G0039 | ἅγιον *hagion* | a holy thing or place | sanctuary, holy place, holiest of all | — |
| G0053 | ἁγνός *hagnos* | clean, innocent, chaste | chaste, clean, pure | — |
| G3741 | ὅσιος *hosios* | pious, right by divine character | holy, mercy | — |
| G2513 | καθαρός *katharos* | clean, pure | clean, clear, pure | — |
| G2511 | καθαρίζω *katharizō* | to cleanse | cleanse, purge, purify, make clean | — |
| G5046 | τέλειος *teleios* | complete, mature, finished | perfect, of full age, man | — |
| G5048 | τελειόω *teleioō* | to complete, consummate | make perfect, finish, fulfil, consecrate | — |

### Where ἁγιασμός occurs — all ten

| Reference | Sense in context |
| --- | --- |
| Romans 6:19 | the goal of yielding your members to righteousness |
| Romans 6:22 | the fruit of being freed from sin |
| 1 Corinthians 1:30 | Christ himself *is made unto us... sanctification* |
| 1 Thessalonians 4:3 | the will of God for you |
| 1 Thessalonians 4:4 | how to possess your own vessel |
| 1 Thessalonians 4:7 | what God called you *unto* |
| 2 Thessalonians 2:13 | *sanctification of the Spirit* — the means of salvation |
| 1 Timothy 2:15 | continuing in faith, charity, and holiness |
| Hebrews 12:14 | what no one will see the Lord without |
| 1 Peter 1:2 | *through sanctification of the Spirit, unto obedience* |

Note 1 Corinthians 1:30. Before sanctification is anything you do, it is a person: *Christ Jesus, who of God is made unto us wisdom, and righteousness, and sanctification, and redemption*.

### Every occurrence of ἁγιάζω, with its tense

This is the evidence for [The three tenses](#the-three-tenses), set out in full. Parsing is from [`original-languages/interlinear/nt-interlinear.tsv`](original-languages/interlinear/nt-interlinear.tsv).

| Reference | Greek | Parsing | Force |
| --- | --- | --- | --- |
| Matthew 6:9 | ἁγιασθήτω | `V-APM-3S` | aorist passive imperative |
| Matthew 23:17 | ἁγιάζων | `V-PAP-NSM` | present active participle |
| Matthew 23:19 | ἁγιάζον | `V-PAP-NSN` | present active participle |
| Luke 11:2 | ἁγιασθήτω | `V-APM-3S` | aorist passive imperative |
| John 10:36 | ἡγίασεν | `V-AAI-3S` | aorist active indicative |
| John 17:17 | Ἁγίασον | `V-AAM-2S` | aorist active imperative |
| John 17:19 | ἁγιάζω | `V-PAI-1S` | present active indicative |
| John 17:19 | ἡγιασμένοι | `V-RPP-NPM` | perfect passive participle |
| Acts 20:32 | ἡγιασμένοις | `V-RPP-DPM` | perfect passive participle |
| Acts 26:18 | ἡγιασμένοις | `V-RPP-DPM` | perfect passive participle |
| Romans 15:16 | ἡγιασμένη | `V-RPP-NSF` | perfect passive participle |
| 1 Corinthians 1:2 | ἡγιασμένοις | `V-RPP-DPM` | perfect passive participle |
| 1 Corinthians 6:11 | ἡγιάσθητε | `V-API-2P` | aorist passive indicative |
| 1 Corinthians 7:14 | Ἡγίασται | `V-RPI-3S` | perfect passive indicative |
| 1 Corinthians 7:14 | ἡγίασται | `V-RPI-3S` | perfect passive indicative |
| Ephesians 5:26 | ἁγιάσῃ | `V-AAS-3S` | aorist active subjunctive |
| 1 Thessalonians 5:23 | ἁγιάσαι | `V-AAO-3S` | aorist active optative |
| 1 Timothy 4:5 | ἁγιάζεται | `V-PPI-3S` | present passive indicative |
| 2 Timothy 2:21 | ἡγιασμένον | `V-RPP-NSN` | perfect passive participle |
| Hebrews 2:11 | ἁγιάζων | `V-PAP-NSM` | present active participle |
| Hebrews 2:11 | ἁγιαζόμενοι | `V-PPP-NPM` | present passive participle |
| Hebrews 9:13 | ἁγιάζει | `V-PAI-3S` | present active indicative |
| Hebrews 10:10 | ἡγιασμένοι | `V-RPP-NPM` | perfect passive participle |
| Hebrews 10:14 | ἁγιαζομένους | `V-PPP-APM` | present passive participle |
| Hebrews 10:29 | ἡγιάσθη | `V-API-3S` | aorist passive indicative |
| Hebrews 13:12 | ἁγιάσῃ | `V-AAS-3S` | aorist active subjunctive |
| 1 Peter 3:15 | ἁγιάσατε | `V-AAM-2P` | aorist active imperative |
| Jude 1:1 | ἡγιασμένοις | `V-RPP-DPM` | perfect passive participle |
| Revelation 22:11 | ἁγιασθήτω | `V-APM-3S` | aorist passive imperative |

Tense distribution: **aorist** 11, **perfect** 10, **present** 8 (of 29 occurrences).

Two things stand out in that table.

**The perfect passive participle is the standard way of naming Christians.** Acts 20:32, Acts 26:18, 1 Corinthians 1:2, and Jude 1:1 all use ἡγιασμένοι(ς) as a simple designation — *the sanctified*, the way one might say *the enrolled*. That is definitive sanctification functioning as a name.

**The first and last uses in the Bible are the same form.** *Hallowed be thy name* (Matthew 6:9) and *let him be holy still* (Revelation 22:11) are both ἁγιασθήτω — aorist passive imperative, third person singular. The Lord's Prayer opens by asking that God's name be treated as holy; Scripture closes by commanding that the holy person keep being made holy. The word has the same shape at both ends of the New Testament.

---

## D. The three tenses at a glance

| | **Definitive** | **Progressive** | **Final** |
| --- | --- | --- | --- |
| **Sentence** | You were sanctified | You are being sanctified | You will be sanctified wholly |
| **Greek example** | ἡγιάσθητε, aorist passive (1 Corinthians 6:11) | ἁγιαζομένους, present passive (Hebrews 10:14) | ἁγιάσαι, aorist optative in a prayer for the future (1 Thessalonians 5:23) |
| **Agent** | God, through Christ's one offering | The Spirit, through the means, with your cooperation | God, at Christ's appearing |
| **Your part** | None — it is done to you | Real effort, commanded throughout | None — it is done to you |
| **Degrees** | None | Every degree | None |
| **Reversible** | No | In stretches, yes; a believer can lose ground | No |
| **Evidence it is true of you** | Union with Christ | Change over years, measured by the marks | The promise of God |
| **Texts** | 1 Corinthians 1:2; 6:11; Hebrews 10:10; Acts 20:32; 26:18; Jude 1:1 | Hebrews 10:14; 2:11; 12:14; 1 Thessalonians 4:3; 2 Corinthians 3:18; 7:1; Romans 6:19, 22; 2 Peter 3:18 | 1 Thessalonians 5:23; 1 John 3:2; Ephesians 5:27; Colossians 1:22; Jude 1:24; Philippians 1:6 |

---

## E. The stages of a Roman Catholic cause

| Stage | Title | Requirement | Effect |
| --- | --- | --- | --- |
| Diocesan inquiry opens | **Servant of God** | Normally five years after death (dispensable by the pope); reputation for holiness; all writings gathered; witnesses examined | None liturgically; the case is under investigation |
| Decree of heroic virtue | **Venerable** | Theological and cardinal virtues practised to a heroic degree — or martyrdom established | No public cult yet permitted |
| Beatification | **Blessed** | One miracle after death attributed to intercession; **waived for martyrs** | Public veneration permitted, usually limited to a diocese, nation, or religious order |
| Canonization | **Saint** | A further miracle, after beatification | Veneration extended to the universal church; may be entered in the general calendar |

Additional routes and notes:

- **Oblatio vitae** — since *Maiorem hac dilectionem* (2017), the free offering of one's life for others, ending in death, is a distinct path alongside martyrdom and heroic virtue, with its own requirements.
- **Equivalent canonization** — the pope may extend an ancient and continuous cult to the universal church without the full process.
- **Miracles** are examined by a medical panel first, on the narrow question of whether a natural explanation exists, before theologians consider attribution.
- **Governing documents** — *Divinus Perfectionis Magister* (1983) for the procedure; *Sanctorum Mater* (2007) for diocesan inquiries; the Dicastery for the Causes of Saints administers both.
- **What the stages measure** is the church's certainty, not the person's progress. Catholic teaching holds that canonization declares a state already reached, and does not confer it.

---

## F. A timeline

| Date | Event |
| --- | --- |
| c. AD 50–95 | The New Testament uses *saints* 61 times, always of living or recently living believers as a class; never as a personal title |
| c. 155 | *The Martyrdom of Polycarp* records relics kept, an annual commemoration on the day of death, and an explicit distinction between worship of Christ and love for the martyrs |
| 250s | Cyprian instructs his clergy to record the days martyrs die, so anniversaries can be kept |
| 313 | The Edict of Milan ends persecution; the question of who counts when nobody is dying begins to press |
| 354 | The Roman *Depositio Martyrum* — a dated calendar of commemorations |
| 4th–5th c. | Honour extended from martyrs to confessors, ascetics, bishops, virgins; Augustine defends the practice against the charge of polytheism |
| 993 | John XV declares Ulrich of Augsburg a saint — the first recorded papal canonization |
| 12th c. | Alexander III asserts that veneration requires the authority of the Roman church |
| 1234 | Gregory IX's *Decretals* reserve canonization to the Holy See in canon law |
| 1517–1563 | The Reformation disputes invocation, merit, and the restriction of the word; Augsburg XXI (1530), Calvin's *Institutes* III.20, Article XXII of the Thirty-nine Articles |
| 1547 | Trent, Session 6, defines justification as including sanctification and renewal, with a chapter on its increase |
| 1587–1588 | The office of Promoter of the Faith is established; Sixtus V creates the Congregation of Rites |
| 1625, 1634 | Urban VIII forbids unauthorised public cult and imposes a waiting period after death |
| 1646 | The Westminster Confession, chapter XIII, on sanctification as a lifelong war with a certain outcome |
| 1656 | John Owen, *Of the Mortification of Sin in Believers* |
| 1734–38 | Prospero Lambertini's treatise sets the standard for heroic virtue and the assessment of miracles |
| 1741–1777 | Wesley's sermons and *A Plain Account of Christian Perfection* |
| 1843–1867 | Phoebe Palmer's writing and the American holiness camp meetings |
| 1875 | The first Keswick Convention; the "higher life" teaching spreads |
| 1877 | J. C. Ryle, *Holiness*, written against the Keswick teaching |
| 1906 | The Azusa Street revival; Pentecostalism grows from holiness soil |
| 1931 | B. B. Warfield's *Perfectionism* criticises the higher-life movement |
| 1964 | *Lumen Gentium* V — the universal call to holiness: all the faithful of every rank are called to the fullness of Christian life |
| 1969 | The Roman calendar is revised; commemorations without historical basis are removed or demoted; the Congregation for the Causes of Saints is established |
| 1983 | *Divinus Perfectionis Magister* replaces the adversarial trial with a documentary and historical-critical process |
| 1983–2005 | John Paul II canonizes and beatifies more people than any predecessor, by policy as well as by procedure |
| 2007 | *Sanctorum Mater* regulates the diocesan phase |
| 2017 | *Maiorem hac dilectionem* adds the *oblatio vitae* as a third route |

---

## G. Where the traditions stand

| Tradition | Who is a "saint"? | How growth is described | Can it be finished here? | On invoking the saints |
| --- | --- | --- | --- | --- |
| **Roman Catholic** | All the baptised in grace are holy; *Saint* as a title is conferred by canonization | Increase of infused grace, cooperated with, meritorious in the defined sense | Normally no; completed in purgatory | Yes — asking their prayers, distinguished from worship |
| **Eastern Orthodox** | All the faithful; glorified saints are recognised, not made | *Theosis* by synergy with the uncreated energies | The process is unending, even in glory | Yes |
| **Oriental Orthodox / Assyrian** | Similar to Orthodox, with their own calendars and processes | Ascetic and sacramental | No | Yes |
| **Lutheran** | Every believer; the canonized are remembered as examples | Fruit of justification; *simul iustus et peccator* | No | No — remembrance and thanksgiving, not invocation |
| **Anglican** | Every believer; the calendar is kept for commemoration | Growth in grace through word, sacrament, and discipline | No | Article XXII rejects the invocation of saints; practice varies by province |
| **Reformed / Presbyterian** | Every believer, without exception | Mortification and vivification; a war with a certain outcome | No | No |
| **Baptist** | Every believer | Growth in grace; no second work | No | No |
| **Methodist / Wesleyan** | Every believer | Growth, plus a second definite work of entire sanctification | Yes, as Wesley defined it — and losable | No |
| **Holiness churches** | Every believer | Entire sanctification, sought and received by faith | Yes | No |
| **Pentecostal** | Every believer | Growth, with Spirit baptism as a distinct empowering | Varies by body | No |
| **Latter-day Saints** | The membership, by self-designation, on the New Testament plural | Distinct from the above; outside the scope of this document | — | — |

---

## H. Honest caveats

**Where this document takes a position.** On four points it argues for a view rather than merely reporting the options:

1. That *saint* in the New Testament is a universal designation and not an honorific — this is not seriously contested by any tradition's exegetes, including Catholic ones, and is stated in Catholic teaching itself.
2. That 1 John 3:9 must be read consistently with 1 John 1:8, which rules out any interpretation making the letter contradict itself within five pages.
3. That *teleios* in Matthew 5:48 means complete rather than flawless, on the basis of its context and of Luke's parallel.
4. That progressive sanctification involves genuine human effort, on the basis of Philippians 2:12–13 and the imperatives generally, against the quietist reading.

Each is argued in the text and the contrary evidence is quoted.

**Where it declines to settle.** Whether Romans 7:14–25 describes Paul's Christian experience; whether entire sanctification as Wesley defined it is attainable in this life; whether there is a purification after death; whether canonizations are infallible. These are live disagreements between serious readers of the same texts, and this document sets them out rather than adjudicating them.

**On the history.** Part II's dates and documents are given as they are standardly reported. Several are approximate or disputed in the scholarly literature — the date of Polycarp's martyrdom (mid-150s or as late as the 160s), the exact scope of Alexander III's twelfth-century claim, and the precise figures for modern canonizations, which vary by source and by whether group causes are counted individually. Where a number could not be checked against a primary source from within this repository, it is given in words rather than as a precise figure.

**On the traditions.** The summaries in Part II and in [Appendix G](#g-where-the-traditions-stand) are compressed, and every tradition contains internal variety that a single table row cannot hold. They are meant to orient a reader, not to substitute for the confessional documents, which are named so they can be read directly.

**On the counts.** Every count of a word or verse in this document was produced from the files in this repository by the command shown next to it, and reflects the KJV and the particular Greek and Hebrew editions carried here. Counts from a different Greek text will differ slightly — Revelation 15:3 in [Appendix A](#a-every-new-testament-occurrence-of-saints) is the clearest example.

**What is missing.** This document does not treat: the holiness of places, times, and objects beyond the brief Levitical section; the relation of sanctification to church discipline; the sanctification of institutions and societies; the extensive monastic literature on the stages of the spiritual life (purgative, illuminative, unitive), which deserves its own study; and the substantial modern literature on spiritual formation.

---

## I. Further reading

**Primary sources named in Part II**, in rough chronological order, so the traditions can be read in their own words rather than in summary: *The Martyrdom of Polycarp*; Athanasius, *On the Incarnation*; Augustine, *City of God* VIII and XXII, and *Confessions* X; the Philokalia; Gregory Palamas, *Triads*; Thomas Aquinas, *Summa Theologiae* I-II qq. 109–114 (on grace); the Council of Trent, Session 6 (1547); the Augsburg Confession XX–XXI (1530); Calvin, *Institutes* III.3 (repentance and regeneration) and III.20 (prayer); the Heidelberg Catechism (1563), Lord's Days 32–44; the Westminster Confession XIII (1646); John Owen, *Of the Mortification of Sin in Believers* (1656); Wesley, *A Plain Account of Christian Perfection* (1777); J. C. Ryle, *Holiness* (1877); B. B. Warfield, *Perfectionism* (1931); *Lumen Gentium* V (1964); *Divinus Perfectionis Magister* (1983); the *Catechism of the Catholic Church* 1987–2029 and 2012–2016 (1992).

**On the disputed questions**, the most useful format is the multi-view collection, in which advocates state their own position and answer each other — several exist covering the Reformed, Lutheran, Wesleyan, Pentecostal, Keswick, and Catholic views of sanctification side by side.

**In this repository:**

- [`once-saved-always-saved.md`](once-saved-always-saved.md) — the closely related question of whether a Christian can be finally lost, and how assurance works
- [`praying-for-the-dead.md`](praying-for-the-dead.md) — the argument over purification after death, the communion of saints, and the invocation of the departed, set out at length
- [`romans-7-study.md`](romans-7-study.md) — the chapter that sits underneath the whole argument about indwelling sin in the believer, verse by verse, with the case for each reading of the "I"
- [`fasting-in-the-bible.md`](fasting-in-the-bible.md) — one of the practices, examined on its own
- [`if-any-would-not-work.md`](if-any-would-not-work.md) — a worked example of reading a single contested verse carefully
- [`kjv/`](kjv) and [`original-languages/`](original-languages) — the texts every claim in this document was checked against
