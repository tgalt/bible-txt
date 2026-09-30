# The Lord's Prayer
## What Jesus Taught His Disciples to Pray: The Two Texts, the Greek Behind Every Petition, the Old Testament and Synagogue Prayers It Grew From, and How the Church Has Prayed It for Two Thousand Years

---

## How to Use This Document

This document answers three questions, in order:

1. **What exactly did Jesus say?** — the prayer as Matthew and Luke record it, where each of them puts it, the Greek behind the King James wording, and where the closing "For thine is the kingdom" came from (Part I)
2. **What does each line mean?** — the prayer petition by petition, with the Old Testament passages each one draws on, the rest of Jesus' teaching on the same subject, and the questions each has raised: what "daily" bread is, whether "as we forgive" is a condition, why we ask God not to lead us into temptation when he tempts no one, and whether the last word is "evil" or "the evil one" (Part II)
3. **How should it be prayed?** — as a fixed text or as a pattern, what its order and its plurals teach, how the church from the *Didache* to the present has used it, and a practical way to pray it slowly (Part III)

Part I is reference material. Part II is the heart of the document. Part III is the practical payoff. A reader who wants only to understand the prayer they already say can go straight to Part II; the reason Part I comes first is that the prayer exists in two forms and one disputed ending, and it is worth knowing which words are certainly the Lord's before weighing them.

**The short answer,** for a reader who wants it before the evidence: the Lord's Prayer is the only prayer Jesus ever told his disciples to pray, and every clause of it is built from the Scriptures he grew up on and the prayers of the synagogue he prayed in. It is not a formula that works by being recited, and it is not merely an outline that need never be said aloud; it is both a text and a pattern, and the church has always used it as both. Its first half asks for God's honour, reign, and will before it asks for anything of ours, and its second half asks for exactly three things — food for today, forgiveness for what is past, and protection for what is ahead — in the plural, on behalf of every other disciple as well as oneself. One petition carries a condition, and Jesus himself stops to underline it: the one who will not forgive is asking not to be forgiven. The prayer's ending, "For thine is the kingdom, and the power, and the glory, for ever," was almost certainly not written by Matthew, but it was prayed by Christians within a generation of the apostles, and every word of it is from the Old Testament.

### The source of the quotations

Scripture is quoted from the **King James Version (1769)**, the text carried in [`kjv/`](kjv) in this repository. Every quotation was taken directly from that file, so any verse can be checked at its source:

```sh
grep '^Matthew 6:9 ' kjv/kjv.txt
grep -E '^Matthew 6:(9|10|11|12|13) ' kjv/kjv.txt
grep -E '^Luke 11:[1-4] ' kjv/kjv.txt
```

Greek words, their parsing, and their Strong's numbers are from [`original-languages/`](original-languages), and where a count or a form is stated the command that produced it is given. Six editions of the Greek New Testament are carried there; this document quotes the accented Textus Receptus ([`kjtr.txt`](original-languages/greek/kjtr.txt)), the text the KJV translators worked from, and compares it where it matters with the SBLGNT and Nestle, which follow the oldest manuscripts. Where the KJV's English has drifted far enough to mislead, the modern sense is supplied: *which art* means *who is*; *hallowed* means *made holy, treated as holy*; *in earth* means *on earth*; *debts* means what is owed, and by extension sins; *temptation* covers both a trial and an enticement; *closet* in Matthew 6:6 is an inner room; *vain repetitions* is one Greek verb meaning to babble.

**The Apocrypha.** One verse from Sirach (Ecclesiasticus), a book the 1611 King James Bible printed between the Testaments, is quoted in Part II for the forgiveness petition. It is not in the 66-book text in [`kjv/`](kjv), cannot be checked against this repository, and is marked *(Apocrypha)* where it appears. Nothing rests on it.

**The Jewish prayers.** The Kaddish, the Eighteen Benedictions, and a Talmudic morning prayer are quoted in Part II because they stand so close to the Lord's Prayer. They are quoted in standard English renderings, and their wording in Jesus' own day cannot be fixed with certainty; see [Appendix F](#f-honest-caveats).

### A note on what this document is not

This is a study of the biblical material and of how it has been prayed, not a ruling from a church. On the questions where the traditions differ — whether the doxology should be said, whether the prayer has six petitions or seven, whether "evil" or "the evil one" is meant, how "lead us not into temptation" should be translated — the disagreement is laid out and the reasons on each side are given. Where this document takes a position, it says so and shows its work. On the substance of the prayer there is no disagreement to lay out: every Christian tradition prays it, and has since the first century.

---

## Contents

**[Part I — The Text](#part-i--the-text)**

- [Two versions, one prayer](#two-versions-one-prayer)
- [Where each evangelist puts it](#where-each-evangelist-puts-it)
- [The two texts side by side](#the-two-texts-side-by-side)
- [The Greek behind the KJV](#the-greek-behind-the-kjv)
- [The shape of the prayer](#the-shape-of-the-prayer)
- [The doxology: where "For thine is the kingdom" came from](#the-doxology-where-for-thine-is-the-kingdom-came-from)
- [The other variants](#the-other-variants)

**[Part II — The Prayer Line by Line](#part-ii--the-prayer-line-by-line)**

- ["Our Father which art in heaven"](#our-father-which-art-in-heaven)
- ["Hallowed be thy name"](#hallowed-be-thy-name)
- ["Thy kingdom come"](#thy-kingdom-come)
- ["Thy will be done in earth, as it is in heaven"](#thy-will-be-done-in-earth-as-it-is-in-heaven)
- ["Give us this day our daily bread"](#give-us-this-day-our-daily-bread)
- ["And forgive us our debts, as we forgive our debtors"](#and-forgive-us-our-debts-as-we-forgive-our-debtors)
- ["And lead us not into temptation"](#and-lead-us-not-into-temptation)
- ["But deliver us from evil"](#but-deliver-us-from-evil)
- ["For thine is the kingdom, and the power, and the glory, for ever. Amen"](#for-thine-is-the-kingdom-and-the-power-and-the-glory-for-ever-amen)

**[Part III — Praying It](#part-iii--praying-it)**

- [Pattern or formula?](#pattern-or-formula)
- [What the prayer assumes](#what-the-prayer-assumes)
- [The order of the petitions](#the-order-of-the-petitions)
- [The plural](#the-plural)
- [The petition with a condition in it](#the-petition-with-a-condition-in-it)
- [How the church has prayed it](#how-the-church-has-prayed-it)
- [The English words: from Wycliffe to "trespasses"](#the-english-words-from-wycliffe-to-trespasses)
- [A practical way to pray it](#a-practical-way-to-pray-it)
- [Ten common mistakes](#ten-common-mistakes)

**[Appendices](#appendices)**

- [A. The two texts in six Greek editions](#a-the-two-texts-in-six-greek-editions)
- [B. Every word of the prayer](#b-every-word-of-the-prayer)
- [C. The Old Testament behind each petition](#c-the-old-testament-behind-each-petition)
- [D. Six petitions or seven?](#d-six-petitions-or-seven)
- [E. Textual notes](#e-textual-notes)
- [F. Honest caveats](#f-honest-caveats)
- [G. Further reading](#g-further-reading)

---
---

# Part I — The Text

## Two versions, one prayer

The prayer appears twice in the New Testament, in Matthew 6:9–13 and Luke 11:2–4, and nowhere else. Mark does not have it. John does not have it — John 17, the long prayer Jesus prays on the night of his arrest, is sometimes called the true "Lord's Prayer," because it is the prayer the Lord himself prayed, whereas the prayer in Matthew and Luke is the one he gave his disciples to pray. The distinction is worth keeping. Jesus could not have prayed "forgive us our debts" for himself (Hebrews 4:15), and he never once says "our Father" as though he and the disciples stood in the same relation to God; he says "my Father, and your Father" (John 20:17). The prayer is the Lord's because he is its author, not its speaker. Some writers have accordingly called it "the Disciples' Prayer." The name "the Lord's Prayer" is not in Scripture at all; it is the church's, from the Latin *Oratio Dominica*, and the prayer has been known through most of its history by its first two words, *Pater noster*, "Our Father."

That the prayer stands in two Gospels, in two forms, on two occasions, is the first thing to notice about it. It was not delivered once and filed. In Matthew it is part of a sermon; in Luke it is the answer to a request. The two settings tell you two different things about what the prayer is for, and they are worth reading before the prayer itself.

---

## Where each evangelist puts it

**Matthew** places the prayer at the exact centre of the Sermon on the Mount (chapters 5–7), inside a passage on three acts of piety — alms, prayer, and fasting (6:1–18) — each of which is handled in the same way: do not do it as the hypocrites do, to be seen; do it in secret; "thy Father which seeth in secret shall reward thee openly." The prayer is embedded in the middle section, on prayer, and it is introduced by a warning that the reader should hold in mind through everything that follows:

> **Matthew 6:5** — And when thou prayest, thou shalt not be as the hypocrites are: for they love to pray standing in the synagogues and in the corners of the streets, that they may be seen of men. Verily I say unto you, They have their reward.

> **Matthew 6:6** — But thou, when thou prayest, enter into thy closet, and when thou hast shut thy door, pray to thy Father which is in secret; and thy Father which seeth in secret shall reward thee openly.

> **Matthew 6:7** — But when ye pray, use not vain repetitions, as the heathen do: for they think that they shall be heard for their much speaking.

> **Matthew 6:8** — Be not ye therefore like unto them: for your Father knoweth what things ye have need of, before ye ask him.

> **Matthew 6:9** — After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.

Two things about that introduction shape the prayer. First, the prayer is given as the alternative to two wrong kinds of praying: the showy prayer of the hypocrite, whose audience is other people, and the wordy prayer of the pagan, who thinks the gods must be worn down. The Lord's Prayer is short because it is addressed to a Father who already knows. Second, the word "Father" has been sounding through the whole passage before the prayer begins — "thy Father which seeth in secret," "your Father knoweth what things ye have need of" — so that when the prayer opens with "Our Father," it opens on a note the Sermon has been striking since 5:16. The word *Father*, capitalised for God, occurs seventeen times in the three chapters of the Sermon, twelve of them in chapter 6:

```sh
grep -E '^Matthew [5-7]:' kjv/kjv.txt | grep -o 'Father' | wc -l    # 17
grep -E '^Matthew 6:' kjv/kjv.txt | grep -o 'Father' | wc -l        # 12
```

And when the prayer ends, Matthew does not move on. He adds two verses in which Jesus comments on one petition and one only:

> **Matthew 6:14** — For if ye forgive men their trespasses, your heavenly Father will also forgive you:

> **Matthew 6:15** — But if ye forgive not men their trespasses, neither will your Father forgive your trespasses.

That is the only clause of the prayer Jesus explains, and the explanation is a warning. Part II returns to it.

**Luke** places the prayer in a different scene, in the middle of Jesus' journey to Jerusalem:

> **Luke 11:1** — And it came to pass, that, as he was praying in a certain place, when he ceased, one of his disciples said unto him, Lord, teach us to pray, as John also taught his disciples.

Luke is the evangelist who most often shows Jesus at prayer — at his baptism (3:21), in the wilderness (5:16), all night on the mountain before choosing the Twelve (6:12), alone before asking who men said he was (9:18), on the mountain of the transfiguration (9:28–29), and in Gethsemane (22:41–44). Here the disciples have watched him and want what he has. Their request assumes something about how a rabbi's followers were marked out: John the Baptist had evidently given his disciples a prayer of their own, and Jesus' disciples ask for the same. The prayer that follows is therefore, in Luke, a badge of belonging as well as a lesson — the prayer of *this* teacher's people.

Luke's Jesus then continues on prayer for another nine verses, and what he adds is not about sincerity, as in Matthew, but about persistence and the Father's willingness:

> **Luke 11:9** — And I say unto you, Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you.

> **Luke 11:13** — If ye then, being evil, know how to give good gifts unto your children: how much more shall your heavenly Father give the Holy Spirit to them that ask him?

Between those lies the parable of the friend at midnight (11:5–8), who gets his three loaves "because of his importunity" — a word that means shamelessness. So Matthew's setting teaches the *manner* of the prayer: secret, brief, sincere, forgiving. Luke's setting teaches its *confidence*: keep asking, because the one you ask is a Father.

Whether the two Gospels record two occasions or two tellings of one is a question this document does not need to settle. The simplest reading of the texts as they stand is that Jesus taught the prayer more than once — a teacher who travelled for three years and had a fixed prayer for his followers would hardly have given it only once — and that Luke's disciple asked for it again, or for the first time, at a later point. Readers who hold that Matthew and Luke drew the prayer from a common written source will read the differences between them as two editions of one text. Either way, the church received two versions and has always prayed Matthew's.

---

## The two texts side by side

Here is the prayer in the King James Version, first as Matthew gives it and then as Luke gives it.

> **Matthew 6:9** — After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.

> **Matthew 6:10** — Thy kingdom come. Thy will be done in earth, as it is in heaven.

> **Matthew 6:11** — Give us this day our daily bread.

> **Matthew 6:12** — And forgive us our debts, as we forgive our debtors.

> **Matthew 6:13** — And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen.

> **Luke 11:2** — And he said unto them, When ye pray, say, Our Father which art in heaven, Hallowed be thy name. Thy kingdom come. Thy will be done, as in heaven, so in earth.

> **Luke 11:3** — Give us day by day our daily bread.

> **Luke 11:4** — And forgive us our sins; for we also forgive every one that is indebted to us. And lead us not into temptation; but deliver us from evil.

In the King James text the differences are four:

| | Matthew 6:9–13 | Luke 11:2–4 |
| --- | --- | --- |
| Introduction | "After this manner therefore pray ye" | "When ye pray, say" |
| Bread | "Give us this day" | "Give us day by day" |
| Forgiveness | "forgive us our debts, as we forgive our debtors" | "forgive us our sins; for we also forgive every one that is indebted to us" |
| Ending | "For thine is the kingdom, and the power, and the glory, for ever. Amen." | none |

In the oldest Greek manuscripts the differences are larger. Luke's version there is shorter still: it begins simply "Father," has no "Thy will be done, as in heaven, so in earth," and ends at "lead us not into temptation," without "but deliver us from evil." The King James translators worked from a Greek text in which Luke's prayer had been filled out to match Matthew's, a process that had happened in the copying centuries before; [The other variants](#the-other-variants) below shows the evidence from the editions in this repository. Nothing in Luke's shorter form contradicts Matthew's longer one. Luke's five clauses are all in Matthew's; Matthew adds the address "which art in heaven," the will petition, and the deliverance clause.

The difference in the introductions is the one with the most to say. Matthew's οὕτως προσεύχεσθε, "pray *thus*, pray *in this way*," presents the prayer as a model; Luke's ὅταν προσεύχησθε, λέγετε, "when you pray, *say*," presents it as a text. Both are true and the church has always done both. Part III takes this up.

---

## The Greek behind the KJV

The Greek that the King James translators worked from — Scrivener's reconstruction of the Textus Receptus, printed with accents in the CNTR's KJTR edition in this repository — reads as follows for Matthew 6:9–13:

```sh
grep -E '^Matthew 6:(9|10|11|12|13) ' original-languages/greek/kjtr.txt
```

> Οὕτως οὖν προσεύχεσθε ὑμεῖς: Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς, Ἁγιασθήτω τὸ ὄνομά σου.
> Ἐλθέτω ἡ βασιλεία σου. Γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῷ καὶ ἐπὶ τῆς γῆς.
> Τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δὸς ἡμῖν σήμερον.
> Καὶ ἄφες ἡμῖν τὰ ὀφειλήματα ἡμῶν, ὡς καὶ ἡμεῖς ἀφίεμεν τοῖς ὀφειλέταις ἡμῶν.
> Καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν, ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ: Ὅτι σοῦ ἐστιν ἡ βασιλεία, καὶ ἡ δύναμις, καὶ ἡ δόξα, εἰς τοὺς αἰῶνας. Ἀμήν.

[Appendix B](#b-every-word-of-the-prayer) gives every word with its parsing and Strong's number. Several features of the Greek are invisible in English and worth knowing before the line-by-line study.

**The prayer is a string of commands.** Every clause of the first half is an imperative in the third person, a form English does not have: ἁγιασθήτω, "let it be hallowed"; ἐλθέτω, "let it come"; γενηθήτω, "let it be done." These are not wishes ("I hope your name will be hallowed") but orders directed at a state of affairs, of the kind a king gives: *let this be so*. The second half is imperatives in the second person addressed to God directly — δός, "give"; ἄφες, "forgive"; ῥῦσαι, "deliver" — and one prohibition, μὴ εἰσενέγκῃς, "do not bring." Prayer in the Bible is bold. The disciples are taught to tell their Father what to do, and the boldness is sanctioned by the fact that everything asked is what God has already promised.

**The imperatives are aorist.** Greek distinguishes an action viewed as a whole (aorist) from an action viewed as ongoing (present). Every imperative in Matthew's prayer is aorist: hallow, come, be done, give, forgive, deliver — each asked as a single, decisive act. Luke's prayer has one exception, and it is instructive. Where Matthew has δὸς ἡμῖν σήμερον, "give us today" (aorist, one act), Luke has δίδου ἡμῖν τὸ καθ' ἡμέραν, "keep giving us, day by day" (present, ongoing). Each evangelist's verb matches his adverb. The KJV renders the difference exactly: "this day" against "day by day."

**The first half is "thy," the second half is "us."** In Greek the three opening petitions each end with the same word, σου, "thy": τὸ ὄνομά σου, ἡ βασιλεία σου, τὸ θέλημά σου. The three closing petitions each carry the first person plural — ἡμῶν, ἡμῖν, ἡμᾶς: "our," "us." The structure is audible in Greek in a way the English only partly preserves; the prayer turns on its hinge between verse 10 and verse 11, from God's concerns to ours.

**The passive has no agent.** "Hallowed be thy name" does not say by whom. This is what grammarians call the divine passive, common in the Gospels: a way of speaking of God's action without naming him, out of reverence. But the passive also leaves room for the one praying. The Old Testament says both that God will sanctify his own name and that his people must sanctify it, and the petition, being passive, asks for both. Part II returns to this.

**Two words are ambiguous in a way English cannot be.** The adjective ἐπιούσιος, "daily," occurs nowhere else in Greek literature and its derivation is uncertain. The last word of the petitions, τοῦ πονηροῦ, is a genitive that could be masculine ("the evil one") or neuter ("evil"); the two forms are identical. Neither can be settled by grammar. Both are discussed at their place in Part II.

**"Lead us not" is a prohibition, not a negated command.** Greek does not use the aorist imperative with a negative; it uses the aorist subjunctive, μὴ εἰσενέγκῃς. The verb is εἰσφέρω, "carry in, bring into." The sense is "do not bring us into," and the question of what that asks is the hardest in the prayer.

---

## The shape of the prayer

Laid out by its clauses, Matthew's prayer has a visible architecture:

| | Clause | Addressed to |
| --- | --- | --- |
| Invocation | Our Father which art in heaven | — |
| 1 | Hallowed be thy name | God's honour |
| 2 | Thy kingdom come | God's reign |
| 3 | Thy will be done in earth, as it is in heaven | God's purpose |
| 4 | Give us this day our daily bread | our present need |
| 5 | And forgive us our debts, as we forgive our debtors | our past |
| 6 | And lead us not into temptation, but deliver us from evil | our future |
| Doxology | For thine is the kingdom, and the power, and the glory, for ever. Amen | God's honour again |

Several observations about this shape are old and sound.

**God comes first.** Three petitions about God before one about us. The prayer does not begin with need, though need is what usually drives people to pray; it begins with adoration and with the longing that God be treated as God. This is the order of the Ten Commandments — duties toward God, then duties toward neighbour — and Augustine and Calvin both drew the parallel. It is also the order of the Sermon itself: "seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you" (Matthew 6:33). The prayer's second petition is the Sermon's central command turned into a request.

**The "us" petitions cover all of time.** Bread is for today. Forgiveness is for what has already been done. Keeping from temptation and deliverance from evil are for what has not yet come. Whoever prays the prayer has prayed for the whole of their life, as it stands at that moment.

**The "us" petitions cover the whole person.** Bread for the body; forgiveness for the conscience; protection for the will. Nothing a disciple needs falls outside them. Augustine's remark, in his letter to the widow Proba, was that if you go through every prayer in Scripture you will find nothing that this prayer does not contain — a claim that has been tested against the Psalms for sixteen centuries and has held.

**Whether the last clause is one petition or two** is the oldest argument about the prayer's form, and it is only about counting. Augustine counted seven petitions, treating "lead us not into temptation" and "deliver us from evil" separately, and the Latin West, Luther, and the Roman Catechism followed him. The Greek commentators generally treated the two clauses together, since the ἀλλά, "but," binds them into one movement — not into danger, but out of it — and the Reformed catechisms (Calvin, Heidelberg, Westminster) count six. Nothing hangs on it except the numbering of catechism questions; [Appendix D](#d-six-petitions-or-seven) sets it out.

**The doxology answers the first half.** "Thine is the kingdom" answers "thy kingdom come"; "the power" answers "thy will be done"; "the glory" answers "hallowed be thy name." Whoever added the ending to the prayer as the church said it built it to mirror the beginning. Whether it belongs to Matthew's text is the next question.

---

## The doxology: where "For thine is the kingdom" came from

The King James Version ends the prayer with a sentence most modern translations print in a footnote:

> **Matthew 6:13** — And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen.

The six Greek editions in this repository divide exactly on this sentence, and the division is the whole story in miniature:

```sh
for e in tr-scrivener kjtr byzantine sblgnt nestle1904 sr; do
  printf '%-12s ' $e; grep '^Matthew 6:13 ' original-languages/greek/$e.txt | grep -c 'αμην\|Ἀμήν'
done
```

The Textus Receptus (both files) and the Byzantine text have the doxology; the SBLGNT, Nestle 1904, and the Statistical Restoration end at τοῦ πονηροῦ, "from evil." The first three represent the manuscripts that were numerous and available in the sixteenth century, when the printed Greek text was fixed and the KJV translated from it; the last three represent the manuscripts that are oldest.

The evidence is not close. The doxology is absent from the fourth-century codices Sinaiticus and Vaticanus, from Codex Bezae, from the Old Latin and Jerome's Vulgate, from the Bohairic Coptic, and — this is the decisive point — from the earliest Christian commentaries on the prayer. Tertullian (about AD 200), Origen (about 233), and Cyprian (about 252) each wrote a treatise expounding the Lord's Prayer clause by clause, and each one stops at "deliver us from evil." They did not skip the doxology; they did not have it. It is present in the great mass of later Greek manuscripts, in the Syriac versions, and — in a shorter form, without "the kingdom" — in the *Didache*, a church manual usually dated around AD 100, which gives the prayer thus:

> *...and lead us not into temptation, but deliver us from the evil one; for thine is the power and the glory for ever. Pray thus three times a day.* — Didache 8:2–3

So the doxology was not written by Matthew, but it was being said by Christians at the end of the prayer within a generation or two of the apostles. That is the ordinary explanation of how it entered the manuscripts: a scribe who prayed the prayer daily with its ending wrote the ending into the Gospel, or a marginal liturgical note was taken into the text, and the fuller form, once in circulation, was naturally preferred by copyists to the shorter — no one wants to be the copyist who left out the doxology. The reverse process, a scribe deleting a doxology that stood in his exemplar, has no motive.

Why did the church add one? Because Jewish prayer did not end without a blessing. Every prayer of the synagogue closes with a *berakah*, a sentence of praise; the Psalter itself is divided into five books, and each of the first four ends in exactly this way:

> **Psalms 41:13** — Blessed be the LORD God of Israel from everlasting, and to everlasting. Amen, and Amen.

> **Psalms 72:19** — And blessed be his glorious name for ever: and let the whole earth be filled with his glory; Amen, and Amen.

> **Psalms 89:52** — Blessed be the LORD for evermore. Amen, and Amen.

> **Psalms 106:48** — Blessed be the LORD God of Israel from everlasting to everlasting: and let all the people say, Amen. Praise ye the LORD.

A prayer that ended on the word "evil" would have felt unfinished to anyone raised on this, and Matthew's prayer, prayed aloud in the assembly, was given the ending Jewish prayers had. And the words chosen were not invented. They are David's, from the last public prayer of his life:

> **1 Chronicles 29:10** — Wherefore David blessed the LORD before all the congregation: and David said, Blessed be thou, LORD God of Israel our father, for ever and ever.

> **1 Chronicles 29:11** — Thine, O LORD, is the greatness, and the power, and the glory, and the victory, and the majesty: for all that is in the heaven and in the earth is thine; thine is the kingdom, O LORD, and thou art exalted as head above all.

*Thine is the kingdom*; *the power*; *the glory*; *for ever* — every term of the doxology is in that one verse. The New Testament letters end the same way, again and again, because their writers had the same habit:

> **Romans 11:36** — For of him, and through him, and to him, are all things: to whom be glory for ever. Amen.

> **Philippians 4:20** — Now unto God and our Father be glory for ever and ever. Amen.

> **1 Peter 4:11** — If any man speak, let him speak as the oracles of God; if any man minister, let him do it as of the ability which God giveth: that God in all things may be glorified through Jesus Christ, to whom be praise and dominion for ever and ever. Amen.

> **Jude 1:25** — To the only wise God our Saviour, be glory and majesty, dominion and power, both now and ever. Amen.

And one verse of Paul's, written near the end of his life, runs through the last petition of the prayer and its doxology in a single breath, as though he were praying it:

> **2 Timothy 4:18** — And the Lord shall deliver me from every evil work, and will preserve me unto his heavenly kingdom: to whom be glory for ever and ever. Amen.

**What follows for praying it.** The doxology is not the Lord's words, on the best evidence. It is the church's words, prayed since the first century, taken from Scripture, and true. There is no reason to stop saying it and no reason to insist on it. The Eastern churches have always said it, with the priest speaking it after the people finish the petitions. The Reformation churches said it because their Greek text had it, and kept it when they learned better, because it was in Scripture anyway. The Roman church omitted it in the Mass for centuries, following the Vulgate, and restored it after the Second Vatican Council, placing it after a short prayer that expands the last petition. All of them are praying David's prayer. The Presbyterian says "for ever," the Anglican "for ever and ever"; both are in 1 Chronicles 29.

---

## The other variants

Apart from the doxology, the manuscripts of the prayer differ in four places, none of which changes what is asked.

**Luke's shorter text.** The critical editions give Luke 11:2–4 as follows:

```sh
grep -E '^Luke 11:(2|3|4) ' original-languages/greek/sblgnt.txt
```

> εἶπεν δὲ αὐτοῖς· Ὅταν προσεύχησθε, λέγετε· Πάτερ, ἁγιασθήτω τὸ ὄνομά σου· ἐλθέτω ἡ βασιλεία σου·
> τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δίδου ἡμῖν τὸ καθʼ ἡμέραν·
> καὶ ἄφες ἡμῖν τὰς ἁμαρτίας ἡμῶν, καὶ γὰρ αὐτοὶ ἀφίομεν παντὶ ὀφείλοντι ἡμῖν· καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν.

"Father"; "hallowed be thy name"; "thy kingdom come"; bread; forgiveness; "lead us not into temptation." Five clauses. The Byzantine text and the Textus Receptus, and so the KJV, have the full Matthean form — "Our Father which art in heaven," "Thy will be done, as in heaven, so in earth," "but deliver us from evil" — in Luke as well. The shorter reading is supported by the oldest witnesses (the papyrus P75 of about AD 200, Vaticanus, Sinaiticus), and it is the reading that explains the other: scribes who knew Matthew's prayer by heart, and said it daily, assimilated Luke's to it, a clause at a time. The alternative — that Luke's copyists deliberately cut the Lord's Prayer down — has never been seriously proposed. The King James translators were not careless here; they translated the text they had.

**The Holy Spirit in Luke 11:2.** Two Greek minuscules (numbered 700 and 162) and two Greek fathers (Gregory of Nyssa, in the fourth century, and Maximus the Confessor, in the seventh) read, in place of "thy kingdom come," "let thy Holy Spirit come upon us and cleanse us." The reading is almost certainly a liturgical adaptation, perhaps for use at baptism, and it is not the original text. It is worth knowing for two reasons: it shows how freely the prayer was adapted in some places, and it shows how early Christians understood what "thy kingdom come" would mean in practice — and Luke's own teaching ends, nine verses later, with the Father giving "the Holy Spirit to them that ask him" (11:13).

**"As we forgive" or "as we have forgiven."** In Matthew 6:12 the Textus Receptus and the Byzantine text read ἀφίεμεν, present tense, "as we forgive"; the oldest manuscripts read ἀφήκαμεν, aorist, "as we have forgiven":

```sh
grep '^Matthew 6:12 ' original-languages/greek/kjtr.txt      # ἀφίεμεν
grep '^Matthew 6:12 ' original-languages/greek/sblgnt.txt    # ἀφήκαμεν
```

The aorist makes our forgiving prior to our asking: *forgive us, as we have already forgiven*. The present makes it habitual: *as we forgive, as is our practice*. Luke has the present, with a "for": "for we also forgive." All three make the disciple's forgiving real, and none makes it the price of God's. Part II weighs what the clause means.

**Spelling.** Nestle prints ἐλθάτω for ἐλθέτω, "come," in both Gospels. It is the same word with a later Greek ending, the difference between two spellings of one form, and it means nothing.

A few late manuscripts expand the doxology to "for thine is the kingdom, and the power, and the glory, of the Father, and of the Son, and of the Holy Spirit, for ever," which shows the same liturgical growth at a later stage. The full list is in [Appendix E](#e-textual-notes).

---
---

# Part II — The Prayer Line by Line

## "Our Father which art in heaven"

> **Matthew 6:9** — After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.

*Which art* is the English of 1611 for *who is*; the KJV uses *which* of persons throughout. The Greek is Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς — "Father of ours, the one in the heavens." The noun is plural, as the Hebrew word for heaven always is; nothing turns on it.

**The word "Father" was not new.** The Old Testament calls God the father of Israel, and Israel his son, from the Exodus on:

> **Exodus 4:22** — And thou shalt say unto Pharaoh, Thus saith the LORD, Israel is my son, even my firstborn:

> **Deuteronomy 32:6** — Do ye thus requite the LORD, O foolish people and unwise? is not he thy father that hath bought thee? hath he not made thee, and established thee?

> **Psalms 103:13** — Like as a father pitieth his children, so the LORD pitieth them that fear him.

> **Isaiah 63:16** — Doubtless thou art our father, though Abraham be ignorant of us, and Israel acknowledge us not: thou, O LORD, art our father, our redeemer; thy name is from everlasting.

> **Isaiah 64:8** — But now, O LORD, thou art our father; we are the clay, and thou our potter; and we all are the work of thy hand.

> **Jeremiah 31:9** — They shall come with weeping, and with supplications will I lead them: I will cause them to walk by the rivers of waters in a straight way, wherein they shall not stumble: for I am a father to Israel, and Ephraim is my firstborn.

> **Malachi 2:10** — Have we not all one father? hath not one God created us? why do we deal treacherously every man against his brother, by profaning the covenant of our fathers?

Isaiah 63:16 is the closest the Old Testament comes to the prayer's opening: "thou, O LORD, art our father" — Hebrew אָבִינוּ, *avinu*, "our father," the very word the synagogue's prayers use. But notice how the Old Testament uses the word. It is rare — something over a dozen times in the whole of it — and it is nearly always *corporate*: God is the father of the nation, not of the individual Israelite, and where an individual is called his son it is the king (2 Samuel 7:14; Psalm 89:26). It is also, with the exceptions in Isaiah, said *about* God rather than *to* him. What Jesus did was to take a word Israel used sparingly and make it the ordinary way of speaking to God. The counts from the King James text make the point:

```sh
for b in Matthew Mark Luke John; do printf "%s: " $b; grep -E "^$b " kjv/kjv.txt | grep -o 'Father' | wc -l; done
# Matthew: 44   Mark: 5   Luke: 21   John: 122
```

Nearly two hundred times in the four Gospels, against a dozen or so in the thirty-nine books before them. Matthew in particular loves the fuller form the prayer uses — "your Father which is in heaven" thirteen times, "heavenly Father" five — and it runs like a thread through the Sermon on the Mount: 5:16, 5:45, 5:48, 6:1, 6:9, 6:14, 6:26, 6:32, 7:11, 7:21.

**The word Jesus actually said** was almost certainly Aramaic, *Abba*. It survives untranslated three times in the New Testament:

> **Mark 14:36** — And he said, Abba, Father, all things are possible unto thee; take away this cup from me: nevertheless not what I will, but what thou wilt.

> **Romans 8:15** — For ye have not received the spirit of bondage again to fear; but ye have received the Spirit of adoption, whereby we cry, Abba, Father.

> **Galatians 4:6** — And because ye are sons, God hath sent forth the Spirit of his Son into your hearts, crying, Abba, Father.

The first is Jesus' own prayer in Gethsemane; the other two are Paul telling Gentile churches, in Greek, that the Spirit puts this Aramaic word in their mouths — which is only intelligible if the word was known to be Jesus' own and had been handed on with the prayer. It was sometimes claimed in the last century that *Abba* meant "Daddy," a small child's word. That was overstated: *abba* was the ordinary word for one's father, used by grown children as well as small ones, and it carried respect as well as intimacy. What is true is that it was a family word, not a formal or liturgical one, and that there is little or no evidence of Jews of the period addressing God with it in prayer. The prayer opens with a word from the home.

**The right to say it.** Jesus does not say "our Father" of himself and the disciples together. He says "my Father" and "your Father," and on Easter morning he puts the two side by side without merging them:

> **John 20:17** — Jesus saith unto her, Touch me not; for I am not yet ascended to my Father: but go to my brethren, and say unto them, I ascend unto my Father, and your Father; and to my God, and your God.

The disciples call God Father because Jesus does, and because they are his brethren. The New Testament is explicit that this standing is given, not natural:

> **John 1:12** — But as many as received him, to them gave he power to become the sons of God, even to them that believe on his name:

> **Galatians 4:4** — But when the fulness of the time was come, God sent forth his Son, made of a woman, made under the law,

> **Galatians 4:5** — To redeem them that were under the law, that we might receive the adoption of sons.

> **Romans 8:14** — For as many as are led by the Spirit of God, they are the sons of God.

> **1 John 3:1** — Behold, what manner of love the Father hath bestowed upon us, that we should be called the sons of God: therefore the world knoweth us not, because it knew him not.

This is why the early church taught the Lord's Prayer to converts only at the end of their preparation, in the last weeks before baptism, and why the newly baptised said it aloud for the first time at their first communion: the first word of the prayer was understood as something one had to be given. Part III returns to that practice. Its logic is Paul's in Romans 8:15 — the word *Abba* is the cry of the Spirit of adoption, and one cannot cry it without him.

**"Which art in heaven."** The second half of the address balances the first. *Father* is nearness; *in heaven* is majesty. Heaven in Scripture is God's throne — the place from which he rules and hears:

> **1 Kings 8:30** — And hearken thou to the supplication of thy servant, and of thy people Israel, when they shall pray toward this place: and hear thou in heaven thy dwelling place: and when thou hearest, forgive.

> **Psalms 11:4** — The LORD is in his holy temple, the LORD's throne is in heaven: his eyes behold, his eyelids try, the children of men.

> **Psalms 115:3** — But our God is in the heavens: he hath done whatsoever he hath pleased.

> **Isaiah 66:1** — Thus saith the LORD, The heaven is my throne, and the earth is my footstool: where is the house that ye build unto me? and where is the place of my rest?

> **Ecclesiastes 5:2** — Be not rash with thy mouth, and let not thine heart be hasty to utter any thing before God: for God is in heaven, and thou upon earth: therefore let thy words be few.

That last verse stands directly behind Matthew 6:7–8. "God is in heaven, and thou upon earth: therefore let thy words be few" is the Preacher's version of "use not vain repetitions... for your Father knoweth what things ye have need of." The address "in heaven" is not about distance. It is about *ability*. Psalm 115:3 gives the point exactly: our God is in the heavens — therefore he has done whatever he pleased. A father on earth may love his child and be unable to help; the Father in heaven is the one who can. Jesus makes the same argument from the lesser to the greater at the end of the Sermon:

> **Matthew 7:11** — If ye then, being evil, know how to give good gifts unto your children, how much more shall your Father which is in heaven give good things to them that ask him?

**What the address does.** It settles, before a single request is made, who is being asked and on what footing. The Westminster Shorter Catechism's answer (Question 100) is as good a summary as exists: the preface "teacheth us to draw near to God with all holy reverence and confidence, as children to a father, able and ready to help us; and that we should pray with and for others." *Father* rules out fear; *in heaven* rules out doubt; *our* rules out solitude. The prayer is not addressed to a force, a principle, or a distant judge, and it is not addressed by an individual. It is a family's address to its head.

---

## "Hallowed be thy name"

> **Matthew 6:9** — After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.

**The word.** Ἁγιασθήτω is the aorist passive imperative of ἁγιάζω (Strong's G37), "to make holy, to treat as holy, to sanctify." The KJV translates the same verb *sanctify* everywhere else it occurs — twenty-nine times in the Textus Receptus — and *hallow* only here and in Luke 11:2:

```sh
grep -cP '\tG0037\t' original-languages/greek/tr-scrivener-words.tsv    # 29
grep -E '^(Matthew|Luke) ' kjv/kjv.txt | grep -i 'hallow' | cut -d' ' -f1-2
# Matthew 6:9
# Luke 11:2
```

*Hallowed* is Tyndale's word, kept by every English version since because the prayer was already known by heart in that form; "sanctified be thy name" would be the same Greek. John 17:17, "Sanctify them through thy truth," and 1 Peter 3:15, "sanctify the Lord God in your hearts," use the verb the prayer uses.

**The name.** In Hebrew thought a name is not a label but the person as known and revealed. When Moses asks God's name at the bush, he is asking who God is (Exodus 3:13–15), and the answer — "I AM THAT I AM... this is my name for ever, and this is my memorial unto all generations" — makes the name the standing form of God's self-disclosure. The third commandment protects it:

> **Exodus 20:7** — Thou shalt not take the name of the LORD thy God in vain; for the LORD will not hold him guiltless that taketh his name in vain.

And the Psalms praise it as holy in itself:

> **Psalms 8:1** — O LORD, our Lord, how excellent is thy name in all the earth! who hast set thy glory above the heavens.

> **Psalms 99:3** — Let them praise thy great and terrible name; for it is holy.

> **Psalms 111:9** — He sent redemption unto his people: he hath commanded his covenant for ever: holy and reverend is his name.

**Who does the hallowing?** This is the question the passive raises. God's name cannot be made more holy than it is; Isaiah's seraphim already cry "Holy, holy, holy" (Isaiah 6:3), and the four living creatures in Revelation never stop (Revelation 4:8). The Old Testament answers in two ways, and the petition needs both.

*God sanctifies his own name.* The prophets say it repeatedly, and always against the background of its having been profaned by his people's conduct:

> **Ezekiel 36:20** — And when they entered unto the heathen, whither they went, they profaned my holy name, when they said to them, These are the people of the LORD, and are gone forth out of his land.

> **Ezekiel 36:22** — Therefore say unto the house of Israel, Thus saith the Lord GOD; I do not this for your sakes, O house of Israel, but for mine holy name's sake, which ye have profaned among the heathen, whither ye went.

> **Ezekiel 36:23** — And I will sanctify my great name, which was profaned among the heathen, which ye have profaned in the midst of them; and the heathen shall know that I am the LORD, saith the Lord GOD, when I shall be sanctified in you before their eyes.

The Hebrew of "I will sanctify my great name" is וְקִדַּשְׁתִּי אֶת־שְׁמִי הַגָּדוֹל, *ve-qiddashti et-shemi ha-gadol* — the verb קָדַשׁ, *qadash* (Strong's H6942), which is the Hebrew behind the Greek ἁγιάζω throughout the Septuagint. "Hallowed be thy name" is Ezekiel 36:23 turned into a request: *do what you said you would do; sanctify your great name; let the nations know.* Notice how God says he will do it: "when I shall be sanctified *in you* before their eyes." God hallows his name by what he does in and through his people.

*The people sanctify God's name.* The same verb is used of Israel's duty:

> **Leviticus 22:32** — Neither shall ye profane my holy name; but I will be hallowed among the children of Israel: I am the LORD which hallow you,

> **Isaiah 29:23** — But when he seeth his children, the work of mine hands, in the midst of him, they shall sanctify my name, and sanctify the Holy One of Jacob, and shall fear the God of Israel.

> **Isaiah 8:13** — Sanctify the LORD of hosts himself; and let him be your fear, and let him be your dread.

And it is used of Moses' failure at the rock, the one sin that kept him out of the land:

> **Numbers 20:12** — And the LORD spake unto Moses and Aaron, Because ye believed me not, to sanctify me in the eyes of the children of Israel, therefore ye shall not bring this congregation into the land which I have given them.

Jewish tradition built on these texts the paired ideas of *kiddush ha-Shem*, "sanctification of the Name" — honouring God by conduct, and in the last resort by martyrdom — and *hillul ha-Shem*, "profanation of the Name," bringing God into contempt by the behaviour of those who bear it. The Sermon on the Mount says the same thing in its own words, and says it before the prayer:

> **Matthew 5:16** — Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.

So the passive "hallowed be" holds both together, and that is its wisdom. It asks God to act — to vindicate his name, to make himself known, to bring the day when "the earth shall be full of the knowledge of the LORD, as the waters cover the sea" (Isaiah 11:9). And it commits the one praying, because the way God has said he will hallow his name is "in you." Luther's catechism answer (1529) has never been bettered: "God's name is indeed holy in itself; but we pray in this petition that it may be holy among us also." Asked how that happens, he answers: when the Word of God is taught purely and we live according to it; and it is profaned when anyone teaches or lives otherwise "from which preserve us, heavenly Father!"

**The synagogue parallel.** The Kaddish, the Aramaic prayer of the synagogue, opens: *Magnified and sanctified be his great name in the world which he created according to his will; and may he establish his kingdom in your lifetime and in your days...* Sanctified be his name; may his kingdom come; according to his will. The first three petitions of the Lord's Prayer are here in the same order, and Jesus' hearers would have recognised them. What the Lord's Prayer adds is the first word: the Kaddish speaks of "his" name; the disciple says "thy," to a Father.

**What it asks.** That God be known as who he is, and treated accordingly — by the world, and first by the one praying. It is the first petition because it is the end the others serve. The kingdom comes and the will is done *so that* the name is hallowed; bread, pardon, and protection are asked *so that* the one asking can go on hallowing it. It is a petition against every casual, cheap, or contemptuous use of God: against swearing by him lightly (Matthew 5:34–37), against praying to be seen (6:5), against calling him Lord and not doing what he says (Luke 6:46). And it commits the one praying to holiness, on the plain logic of 1 Peter:

> **1 Peter 1:15** — But as he which hath called you is holy, so be ye holy in all manner of conversation;

> **1 Peter 1:16** — Because it is written, Be ye holy; for I am holy.

---

## "Thy kingdom come"

> **Matthew 6:10** — Thy kingdom come. Thy will be done in earth, as it is in heaven.

**The words.** Ἐλθέτω ἡ βασιλεία σου — "let come the kingdom of thee." Βασιλεία (Strong's G932) means, first, kingship: "royalty, i.e. rule," in Strong's definition; "kingship, sovereignty, authority, rule, especially of God... hence: kingdom, in the concrete sense," in Dodson's. It is God's *reign* — his active ruling — more than his realm. And the verb is "come": ἔρχομαι, the ordinary word for arriving. The petition treats God's reign as something that *arrives*, an event to be waited for and asked for.

**The theme of Jesus' preaching.** Nothing is nearer the centre of what Jesus said than this. His first recorded sermon and John the Baptist's before him were one sentence:

> **Matthew 3:2** — And saying, Repent ye: for the kingdom of heaven is at hand.

> **Matthew 4:17** — From that time Jesus began to preach, and to say, Repent: for the kingdom of heaven is at hand.

> **Mark 1:15** — And saying, The time is fulfilled, and the kingdom of God is at hand: repent ye, and believe the gospel.

The phrase "kingdom of heaven" occurs thirty-three times in Matthew, and "kingdom of God" fifty times in Mark, Luke, and John; they are the same thing, Matthew using "heaven" where a Jewish writer would avoid the divine name:

```sh
grep -E '^Matthew ' kjv/kjv.txt | grep -o 'kingdom of heaven' | wc -l       # 33
grep -E '^(Mark|Luke|John) ' kjv/kjv.txt | grep -o 'kingdom of God' | wc -l  # 50
```

The Sermon on the Mount opens and closes its Beatitudes with it (5:3, 5:10), makes it the first thing to seek (6:33), and ends with the warning that not everyone who says "Lord, Lord" will enter it (7:21). The parables are parables of the kingdom: the mustard seed and the leaven (13:31–33), the treasure and the pearl (13:44–46). To pray "thy kingdom come" is to pray for the thing Jesus came announcing.

**God is king already.** The Old Testament never doubts it:

> **Psalms 103:19** — The LORD hath prepared his throne in the heavens; and his kingdom ruleth over all.

> **Psalms 145:13** — Thy kingdom is an everlasting kingdom, and thy dominion endureth throughout all generations.

> **Daniel 4:34** — And at the end of the days I Nebuchadnezzar lifted up mine eyes unto heaven, and mine understanding returned unto me, and I blessed the most High, and I praised and honoured him that liveth for ever, whose dominion is an everlasting dominion, and his kingdom is from generation to generation:

So the petition cannot mean *become king*. It means: let the reign that is already absolute in heaven become effective on earth, where it is contested. That is why the prayer's next clause — "in earth, as it is in heaven" — is often read as governing all three of the "thy" petitions, not only the third: hallowed be thy name, on earth as in heaven; thy kingdom come, on earth as in heaven; thy will be done, on earth as in heaven. The Greek permits it, and the sense demands it. The prophets had promised exactly this:

> **Daniel 2:44** — And in the days of these kings shall the God of heaven set up a kingdom, which shall never be destroyed: and the kingdom shall not be left to other people, but it shall break in pieces and consume all these kingdoms, and it shall stand for ever.

> **Daniel 7:14** — And there was given him dominion, and glory, and a kingdom, that all people, nations, and languages, should serve him: his dominion is an everlasting dominion, which shall not pass away, and his kingdom that which shall not be destroyed.

> **Zechariah 14:9** — And the LORD shall be king over all the earth: in that day shall there be one LORD, and his name one.

> **Isaiah 52:7** — How beautiful upon the mountains are the feet of him that bringeth good tidings, that publisheth peace; that bringeth good tidings of good, that publisheth salvation; that saith unto Zion, Thy God reigneth!

Isaiah's "good tidings" is the word that became *gospel*, and its content is "Thy God reigneth." The gospel is the announcement that the kingdom has come. The Kaddish, again, asks the same: *may he establish his kingdom in your lifetime and in your days, and in the lifetime of all the house of Israel, speedily and soon.*

**Already, and not yet.** Jesus taught that the kingdom had arrived in his own person and works, and that it was still to come in fulness. Both are true, and the prayer holds both:

> **Matthew 12:28** — But if I cast out devils by the Spirit of God, then the kingdom of God is come unto you.

> **Luke 17:20** — And when he was demanded of the Pharisees, when the kingdom of God should come, he answered them and said, The kingdom of God cometh not with observation:

> **Luke 17:21** — Neither shall they say, Lo here! or, lo there! for, behold, the kingdom of God is within you.

> **Luke 12:32** — Fear not, little flock; for it is your Father's good pleasure to give you the kingdom.

> **Matthew 25:34** — Then shall the King say unto them on his right hand, Come, ye blessed of my Father, inherit the kingdom prepared for you from the foundation of the world:

> **1 Corinthians 15:24** — Then cometh the end, when he shall have delivered up the kingdom to God, even the Father; when he shall have put down all rule and all authority and power.

> **Revelation 11:15** — And the seventh angel sounded; and there were great voices in heaven, saying, The kingdoms of this world are become the kingdoms of our Lord, and of his Christ; and he shall reign for ever and ever.

So "thy kingdom come" is prayed in three tenses at once. It asks that God's rule take hold *now*, in the one praying and in the church — that the kingdom "within you" grow. It asks that it spread — that the gospel of the kingdom "be preached in all the world for a witness unto all nations" (Matthew 24:14). And it asks for the end: for Christ's return and the day when every rival rule is put down. In that last sense the petition is the same prayer as the oldest Christian prayer we know, the Aramaic *Maranatha*, "Our Lord, come" (1 Corinthians 16:22), and the last prayer in the Bible:

> **Revelation 22:20** — He which testifieth these things saith, Surely I come quickly. Amen. Even so, come, Lord Jesus.

**What it asks of the one praying.** To pray for the kingdom to come is to want it, and wanting it has consequences. The kingdom is "not of this world" (John 18:36) and it is "not meat and drink; but righteousness, and peace, and joy in the Holy Ghost" (Romans 14:17). It admits no rival: "No man can serve two masters... Ye cannot serve God and mammon" (Matthew 6:24), which Jesus says fourteen verses after the prayer. Whoever prays "thy kingdom come" has asked for the end of their own kingdom — their own rule over their life — and every day the petition is prayed honestly, some of that ground is given up. It is also a prayer for the kingdom to come to *others*, which is to say a missionary prayer; it cannot be prayed by anyone content that the world stay as it is.

---

## "Thy will be done in earth, as it is in heaven"

> **Matthew 6:10** — Thy kingdom come. Thy will be done in earth, as it is in heaven.

**The words.** Γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῷ καὶ ἐπὶ τῆς γῆς — "let be done the will of thee, as in heaven, also on earth." Θέλημα (Strong's G2307) is "will" in the sense of what one wants and has determined: Dodson gives "an act of will, will; plural: wishes, desires." The verb is γίνομαι, "to come to be, to happen"; the KJV's "be done" is right, but "come to pass" is nearer. *In earth* is simply *on earth*, the preposition ἐπί.

This petition is missing from the shorter, older text of Luke. Luke's prayer goes straight from "thy kingdom come" to bread, and loses nothing by it: where God's kingdom has come his will is done. Matthew's third petition spells out what the second implies.

**"As it is in heaven."** The standard is set by the angels:

> **Psalms 103:20** — Bless the LORD, ye his angels, that excel in strength, that do his commandments, hearkening unto the voice of his word.

> **Psalms 103:21** — Bless ye the LORD, all ye his hosts; ye ministers of his, that do his pleasure.

In heaven God's will is done immediately, completely, and gladly; nobody there negotiates. The petition asks that the same obedience come to be on earth — which is to say, among people, and first in the one praying. It is a prayer for earth to become like heaven, not for the one praying to escape earth for heaven. The whole horizon of the prophets is in it:

> **Habakkuk 2:14** — For the earth shall be filled with the knowledge of the glory of the LORD, as the waters cover the sea.

> **Philippians 2:10** — That at the name of Jesus every knee should bow, of things in heaven, and things in earth, and things under the earth;

> **Philippians 2:11** — And that every tongue should confess that Jesus Christ is Lord, to the glory of God the Father.

**Two senses of "will."** Scripture speaks of God's will in two ways, and only one of them needs praying for. There is the will by which he governs, which nothing can stop:

> **Psalms 115:3** — But our God is in the heavens: he hath done whatsoever he hath pleased.

> **Daniel 4:35** — And all the inhabitants of the earth are reputed as nothing: and he doeth according to his will in the army of heaven, and among the inhabitants of the earth: and none can stay his hand, or say unto him, What doest thou?

That will is done on earth whether anyone prays or not. And there is the will by which he *commands* — what he wants people to do — which is done in heaven and very largely not done on earth:

> **Psalms 40:8** — I delight to do thy will, O my God: yea, thy law is within my heart.

> **Psalms 143:10** — Teach me to do thy will; for thou art my God: thy spirit is good; lead me into the land of uprightness.

> **Matthew 7:21** — Not every one that saith unto me, Lord, Lord, shall enter into the kingdom of heaven; but he that doeth the will of my Father which is in heaven.

> **Matthew 12:50** — For whosoever shall do the will of my Father which is in heaven, the same is my brother, and sister, and mother.

> **John 6:40** — And this is the will of him that sent me, that every one which seeth the Son, and believeth on him, may have everlasting life: and I will raise him up at the last day.

The petition asks for the second. It is not a request that God's decrees be carried out — they will be — but that his commands be obeyed and his saving purpose accomplished, on earth, in people, in me. Luther's catechism again: "The good and gracious will of God is done indeed without our prayer; but we pray in this petition that it may be done among us also." And he names what stands against it: "the devil, the world, and our own flesh."

**Jesus prays it himself.** The one time we hear Jesus pray the third petition in his own words, it is the hardest hour of his life:

> **Matthew 26:39** — And he went a little farther, and fell on his face, and prayed, saying, O my Father, if it be possible, let this cup pass from me: nevertheless not as I will, but as thou wilt.

> **Matthew 26:42** — He went away again the second time, and prayed, saying, O my Father, if this cup may not pass away from me, except I drink it, thy will be done.

> **Mark 14:36** — And he said, Abba, Father, all things are possible unto thee; take away this cup from me: nevertheless not what I will, but what thou wilt.

"Abba, Father... thy will be done." The prayer's first word and its third petition, in Gethsemane, from the one who gave them. And in the same hour he tells the sleeping disciples to pray its sixth: "Watch and pray, that ye enter not into temptation" (Matthew 26:41). Gethsemane is the Lord's Prayer prayed under the greatest possible weight, and it shows what the third petition costs and what it is for. It was the pattern of Jesus' whole life:

> **John 4:34** — Jesus saith unto them, My meat is to do the will of him that sent me, and to finish his work.

> **John 6:38** — For I came down from heaven, not to do mine own will, but the will of him that sent me.

> **Hebrews 10:7** — Then said I, Lo, I come (in the volume of the book it is written of me,) to do thy will, O God.

**Submission and petition.** The petition has two faces and both are needed. It is submission: *not my will, but thine* — the surrender of one's own plans, including one's plans for how God should answer the rest of the prayer. But it is not resignation, the shrug that says "whatever will be, will be." It is a *request*, made with the same aorist imperative force as "give us" and "forgive us": *let it be done* — bring it about, accomplish it, in me and in the world. Whoever prays it is not stepping back from the fight but enlisting in it. The one who has prayed "thy will be done" has volunteered to do it.

---

## "Give us this day our daily bread"

> **Matthew 6:11** — Give us this day our daily bread.

> **Luke 11:3** — Give us day by day our daily bread.

**The turn.** Here the prayer changes direction. The three petitions about God are finished; the three about us begin, and the first thing asked for is the most ordinary thing there is. Not wisdom, not strength, not holiness — bread. Whoever supposes that the Lord's Prayer is a spiritual exercise above bodily needs has not read its fourth line. The Father who made bodies is asked to feed them, and the asking is placed before the asking for forgiveness.

**The words.** Τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δὸς ἡμῖν σήμερον — "the bread of ours, the *epiousios*, give us today." Ἄρτος (Strong's G740) is bread, a loaf, and by extension food; the Hebrew לֶחֶם, *lechem*, which it translates throughout the Septuagint, is "food (for man or beast), especially bread" (Strong's H3899). The petition is for food, and bread stands for it as the staple. In Matthew the verb is aorist, δός, "give," one act, with σήμερον, "today"; in Luke it is present, δίδου, "keep giving," with τὸ καθ' ἡμέραν, "day by day." Either way the horizon is one day.

**The word nobody else ever used.** Ἐπιούσιος (Strong's G1967), translated *daily*, is the most discussed word in the prayer, because it exists nowhere else. It occurs twice in the New Testament, in the two versions of this petition:

```sh
grep -P '\tG1967\t' original-languages/greek/tr-scrivener-words.tsv | cut -f1
# Matthew 6:11
# Luke 11:3
```

It occurs nowhere in the Septuagint. Origen, writing about AD 233 and one of the most widely read men of the ancient world, said that the word "is not used by any of the Greeks, nor by the learned, nor is it current in ordinary speech, but seems to have been coined by the evangelists" (*On Prayer* 27.7). Eighteen centuries of reading have not overturned him. One occurrence was reported in the nineteenth century in a fifth-century Egyptian household account — a shopping list — but a re-examination published in 1999 concluded that the word had been misread, the line most likely recording a quantity of oil. So the word remains, as far as anyone knows, a coinage made to translate something Jesus said in Aramaic, and its meaning has to be reconstructed from its parts. Four reconstructions have been proposed.

1. **From ἐπί + οὐσία, "for being," "for existence."** The bread that is *necessary for subsistence* — needful bread. This is Strong's preference ("for subsistence, i.e. needful"), it is what the Syriac Peshitta translated (*lachma d-sunqanan*, "the bread of our need"), and it fits Proverbs 30:8, quoted below, exactly.
2. **From ἐπὶ τὴν οὖσαν [ἡμέραν], "for the current day."** Bread for *today* — "daily" in the plainest sense. This is the reading the English word "daily" assumes, and the Old Latin *quotidianum* behind it.
3. **From ἡ ἐπιοῦσα [ἡμέρα], "the coming day," "tomorrow."** Bread for *the day ahead*. Jerome reports that the Aramaic-speaking Christians' "Gospel according to the Hebrews" had here the word *mahar*, "tomorrow": *give us today our bread for tomorrow*. If the prayer was said in the morning, tomorrow's bread is today's; if in the evening, it is the next day's. The petition would then be for the next day's need, and no further — the manna principle.
4. **From ἐπιέναι, "to come," in a larger sense: "the bread that is coming," the bread of the age to come.** On this reading the petition is for the bread of the kingdom, the messianic banquet, and by extension for the Eucharist. Jerome, unable to decide, translated Matthew's word *supersubstantialem*, "super-substantial," and Luke's *cotidianum*, "daily," and the Latin church prayed the second while its Bible read the first. Wycliffe's English followed Jerome: "oure breed ouer othir substaunce."

**How much turns on this?** Less than the volume of discussion suggests. Whichever derivation is right, the petition's sense is fixed by the words around it: *give*, *us*, *our*, *this day* / *day by day*. It asks for bread — food — enough for the present, asked for as a gift, and asked for daily. The first three derivations all yield that; the fourth, the eschatological or eucharistic reading, is a real dimension of the petition — Jesus himself extends bread that way in John 6 — but as an application, not as the meaning of the word. Augustine, faced with the same uncertainty, allowed three senses at once: the bread of the body, the bread of the sacrament, and the bread of the Word. That is a fair place to rest. The KJV's "daily" came through Tyndale from the Latin, and it has been the English word for five centuries; it is not wrong, and there is no better one.

**The manna.** Behind the petition stands the wilderness. Israel was fed for forty years on bread it did not grow, given each morning, one day's portion at a time:

> **Exodus 16:4** — Then said the LORD unto Moses, Behold, I will rain bread from heaven for you; and the people shall go out and gather a certain rate every day, that I may prove them, whether they will walk in my law, or no.

> **Exodus 16:18** — And when they did mete it with an omer, he that gathered much had nothing over, and he that gathered little had no lack; they gathered every man according to his eating.

> **Exodus 16:19** — And Moses said, Let no man leave of it till the morning.

> **Exodus 16:20** — Notwithstanding they hearkened not unto Moses; but some of them left of it until the morning, and it bred worms, and stank: and Moses was wroth with them.

"A certain rate every day" is the KJV's rendering of דְּבַר־יוֹם בְּיוֹמוֹ, *devar-yom be-yomo*, "the matter of a day in its day" — the phrase the Old Testament uses for a daily allowance (it is the same phrase behind "a daily rate for every day" in 2 Kings 25:30). "Our daily bread" is manna language. And notice why God gave it that way: "that I may prove them." The Hebrew verb is נָסָה, *nasah* (Strong's H5254), "to test" — the word the KJV elsewhere renders *tempt*, and the Old Testament word behind the sixth petition. Daily bread was Israel's daily test: would they trust God for tomorrow, or hoard? Moses drew the lesson at the end of the forty years:

> **Deuteronomy 8:3** — And he humbled thee, and suffered thee to hunger, and fed thee with manna, which thou knewest not, neither did thy fathers know; that he might make thee know that man doth not live by bread only, but by every word that proceedeth out of the mouth of the LORD doth man live.

That is the verse Jesus quoted when, after forty days without bread, he was told to make some (Matthew 4:4). The one who taught the fourth petition had lived it.

**The Old Testament's own prayer for daily bread.** Agur's prayer in Proverbs is the nearest thing in the Old Testament to this petition, and it gives the reason for the petition's modesty:

> **Proverbs 30:8** — Remove far from me vanity and lies: give me neither poverty nor riches; feed me with food convenient for me:

> **Proverbs 30:9** — Lest I be full, and deny thee, and say, Who is the LORD? or lest I be poor, and steal, and take the name of my God in vain.

"Food convenient for me" — the food that is *fitting*, my portion, no more and no less. Too much and I forget God; too little and I dishonour him. Enough, and I am kept. The Lord's Prayer asks for enough. It does not ask for plenty, for security, for next year's bread, or for the means to stop having to ask. It asks for today's, and it asks again tomorrow. The Psalms are full of the same confidence:

> **Psalms 145:15** — The eyes of all wait upon thee; and thou givest them their meat in due season.

> **Psalms 145:16** — Thou openest thine hand, and satisfiest the desire of every living thing.

> **Psalms 104:14** — He causeth the grass to grow for the cattle, and herb for the service of man: that he may bring forth food out of the earth;

**The Sermon's commentary.** Matthew places, fourteen verses after the prayer, the longest passage in the Gospels on the subject of the fourth petition, and it ends with a sentence that is the petition's "this day" turned into a rule of life:

> **Matthew 6:25** — Therefore I say unto you, Take no thought for your life, what ye shall eat, or what ye shall drink; nor yet for your body, what ye shall put on. Is not the life more than meat, and the body than raiment?

> **Matthew 6:26** — Behold the fowls of the air: for they sow not, neither do they reap, nor gather into barns; yet your heavenly Father feedeth them. Are ye not much better than they?

> **Matthew 6:32** — (For after all these things do the Gentiles seek:) for your heavenly Father knoweth that ye have need of all these things.

> **Matthew 6:33** — But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.

> **Matthew 6:34** — Take therefore no thought for the morrow: for the morrow shall take thought for the things of itself. Sufficient unto the day is the evil thereof.

"Take no thought" means *do not be anxious*, not *do not plan*. But the passage is the fourth petition's own explanation: the Father knows, the Father feeds, seek the kingdom first — which is the prayer's order — and live a day at a time. And in Luke's setting the teaching that follows the prayer is about a man asking a neighbour for three loaves at midnight (11:5–8), and a son asking his father for bread (11:11) — bread again, both times, and both times given.

**What the petition asks and what it assumes.** It assumes that bread is a gift. Every loaf is grown from rain and sun no one made and grain no one designed — "he left not himself without witness, in that he did good, and gave us rain from heaven, and fruitful seasons, filling our hearts with food and gladness" (Acts 14:17). To ask for it daily is to be reminded daily that one did not make it. It assumes dependence, one day at a time. It asks for enough, not excess; the word "our" and the word "us" put the one praying in a company, and one cannot honestly pray "give *us* our daily bread" and be indifferent to the brother beside one who has none:

> **James 2:15** — If a brother or sister be naked, and destitute of daily food,

> **James 2:16** — And one of you say unto them, Depart in peace, be ye warmed and filled; notwithstanding ye give them not those things which are needful to the body; what doth it profit?

Luther's catechism explanation of "daily bread" is famous for its list, and the list is the point: "everything that belongs to the support and wants of the body, such as meat, drink, clothing, shoes, house, homestead, field, cattle, money, goods, a pious spouse, pious children, pious servants, pious and faithful magistrates, good government, good weather, peace, health, discipline, honour, good friends, faithful neighbours, and the like." Bread is the whole economy of an ordinary life, and the petition puts it all in the Father's hands.

And Jesus himself takes the word further, in the discourse that follows his feeding of five thousand with bread:

> **John 6:32** — Then Jesus said unto them, Verily, verily, I say unto you, Moses gave you not that bread from heaven; but my Father giveth you the true bread from heaven.

> **John 6:35** — And Jesus said unto them, I am the bread of life: he that cometh to me shall never hunger; and he that believeth on me shall never thirst.

> **John 6:51** — I am the living bread which came down from heaven: if any man eat of this bread, he shall live for ever: and the bread that I will give is my flesh, which I will give for the life of the world.

The church has never been wrong to hear this in the fourth petition, so long as it does not stop hearing the loaf.

---

## "And forgive us our debts, as we forgive our debtors"

> **Matthew 6:12** — And forgive us our debts, as we forgive our debtors.

> **Luke 11:4** — And forgive us our sins; for we also forgive every one that is indebted to us. And lead us not into temptation; but deliver us from evil.

**The words.** Καὶ ἄφες ἡμῖν τὰ ὀφειλήματα ἡμῶν, ὡς καὶ ἡμεῖς ἀφίεμεν τοῖς ὀφειλέταις ἡμῶν — "and remit to us the debts of ours, as also we remit to the debtors of ours." Two words need attention.

Ὀφείλημα (Strong's G3783) is "something owed," a debt, and in its literal sense it is a business word. It occurs only twice in the New Testament, here and in Romans 4:4, where it is the opposite of grace:

> **Romans 4:4** — Now to him that worketh is the reward not reckoned of grace, but of debt.

```sh
grep -P '\tG3783\t' original-languages/greek/tr-scrivener-words.tsv | cut -f1
# Matthew 6:12
# Romans 4:4
```

The related noun ὀφειλέτης (G3781), "debtor," occurs seven times, and one of them shows how the word could slide from money to sin. When Jesus speaks of the eighteen killed by the tower of Siloam, the KJV reads:

> **Luke 13:4** — Or those eighteen, upon whom the tower in Siloam fell, and slew them, think ye that they were sinners above all men that dwelt in Jerusalem?

*Sinners* there is ὀφειλέται, *debtors*. The reason is the language underneath. In Aramaic, the language Jesus taught in, one word — *ḥôbâ* — meant both "debt" and "sin," and a "debtor" was a sinner. Matthew, translating, kept the metaphor: *debts*. Luke, writing for Greeks who would hear only a ledger, gave the sense in the first half — ἁμαρτίας, "sins" (G266) — and kept the debt-word in the second: "every one that is indebted to us," παντὶ ὀφείλοντι ἡμῖν. The two evangelists are not disagreeing. They are rendering one Aramaic petition into Greek by two methods. Hebrew has the same noun, חוֹב, *ḥôb* (Strong's H2326), "debt"; it occurs once, in Ezekiel's portrait of the just man who "hath restored to the debtor his pledge" (Ezekiel 18:7).

The verb is ἀφίημι (G863), whose root sense is to send away, let go, release. The KJV renders it *forgive*, *remit*, *leave*, *let go*, *put away*, and it is the same verb whether the thing let go is a debt or a sin. When the king in Jesus' parable "forgave him the debt" (Matthew 18:27) it is ἀφῆκεν; when the prayer says "forgive us," it is ἄφες. Forgiveness in this petition is *remission*: the cancelling of what is owed, by the one to whom it is owed, so that it is no longer held against the debtor.

**Sin as debt.** The picture is exact and worth keeping. A sin is something owed to God and not paid — an obligation defaulted on, a claim he has against us. And a debtor cannot forgive his own debt. Only the creditor can remit, and the debtor can only ask. So the petition is not a request for help in making things right; it is a request that the account be cancelled, which is what God had been promising to do since Sinai:

> **Exodus 34:6** — And the LORD passed by before him, and proclaimed, The LORD, The LORD God, merciful and gracious, longsuffering, and abundant in goodness and truth,

> **Exodus 34:7** — Keeping mercy for thousands, forgiving iniquity and transgression and sin, and that will by no means clear the guilty; visiting the iniquity of the fathers upon the children, and upon the children's children, unto the third and to the fourth generation.

> **Psalms 32:1** — Blessed is he whose transgression is forgiven, whose sin is covered.

> **Psalms 103:10** — He hath not dealt with us after our sins; nor rewarded us according to our iniquities.

> **Psalms 103:12** — As far as the east is from the west, so far hath he removed our transgressions from us.

> **Psalms 130:3** — If thou, LORD, shouldest mark iniquities, O Lord, who shall stand?

> **Psalms 130:4** — But there is forgiveness with thee, that thou mayest be feared.

> **Isaiah 43:25** — I, even I, am he that blotteth out thy transgressions for mine own sake, and will not remember thy sins.

> **Micah 7:18** — Who is a God like unto thee, that pardoneth iniquity, and passeth by the transgression of the remnant of his heritage? he retaineth not his anger for ever, because he delighteth in mercy.

> **Micah 7:19** — He will turn again, he will have compassion upon us; he will subdue our iniquities; and thou wilt cast all their sins into the depths of the sea.

Israel was also a nation whose law cancelled debts. Every seventh year every creditor released what he was owed, and it was called *the LORD's release*:

> **Deuteronomy 15:1** — At the end of every seven years thou shalt make a release.

> **Deuteronomy 15:2** — And this is the manner of the release: Every creditor that lendeth ought unto his neighbour shall release it; he shall not exact it of his neighbour, or of his brother; because it is called the LORD's release.

The Jubilee, every fiftieth year, went further (Leviticus 25:10), and Nehemiah made the people swear to it again on their return from exile (Nehemiah 5:10–11; 10:31). A people whose God cancelled debts by statute could hear "forgive us our debts, as we forgive our debtors" and know exactly what was being said. The synagogue's own prayer, the sixth of the Eighteen Benedictions, ran: *Forgive us, our Father, for we have sinned; pardon us, our King, for we have transgressed.* And one book of the Apocrypha had already tied God's forgiveness to ours in almost the prayer's words:

> **Sirach 28:2** *(Apocrypha)* — Forgive thy neighbour the hurt that he hath done unto thee, so shall thy sins also be forgiven when thou prayest.

**The commentary Jesus attached.** This is the only petition Jesus explains, and he explains it immediately, before the Sermon moves on to fasting:

> **Matthew 6:14** — For if ye forgive men their trespasses, your heavenly Father will also forgive you:

> **Matthew 6:15** — But if ye forgive not men their trespasses, neither will your Father forgive your trespasses.

The word here is a third one, παραπτώματα (G3900), "trespasses" — literally false steps, lapses, side-slips. It is from these two verses that the English Prayer Book's "forgive us our trespasses" comes, though the prayer itself says "debts." Mark records the same teaching in the same words, attached to prayer in general:

> **Mark 11:25** — And when ye stand praying, forgive, if ye have ought against any: that your Father also which is in heaven may forgive you your trespasses.

> **Mark 11:26** — But if ye do not forgive, neither will your Father which is in heaven forgive your trespasses.

And when Peter asks how often he must forgive, Jesus answers with a parable that is the fifth petition dramatised, down to its vocabulary:

> **Matthew 18:24** — And when he had begun to reckon, one was brought unto him, which owed him ten thousand talents.

> **Matthew 18:27** — Then the lord of that servant was moved with compassion, and loosed him, and forgave him the debt.

> **Matthew 18:28** — But the same servant went out, and found one of his fellowservants, which owed him an hundred pence: and he laid hands on him, and took him by the throat, saying, Pay me that thou owest.

> **Matthew 18:32** — Then his lord, after that he had called him, said unto him, O thou wicked servant, I forgave thee all that debt, because thou desiredst me:

> **Matthew 18:33** — Shouldest not thou also have had compassion on thy fellowservant, even as I had pity on thee?

> **Matthew 18:35** — So likewise shall my heavenly Father do also unto you, if ye from your hearts forgive not every one his brother their trespasses.

Ten thousand talents was a sum beyond any private person's imagining, the revenue of a province; a hundred pence was a hundred days' wages. The proportions are the point. What God remits to any one of us is of a different order from anything anyone owes us, and the servant who has been remitted the greater and then seizes his brother by the throat for the lesser has not understood what happened to him.

**What "as" means.** The word ὡς, "as," has been read in three ways, and the first must be ruled out. It does not mean *in proportion to* — that God forgives us to the extent that we forgive, so that our forgiving earns his. The debt picture itself makes that impossible: a debtor does not earn remission, he receives it, and Romans 4:4 uses this very word to say that what is earned is "of debt" and not "of grace." Nor is our forgiving the *model* for God's, as though he learned it from us; Paul says the opposite, "forgiving one another, even as God for Christ's sake hath forgiven you" (Ephesians 4:32).

What the "as" states is a *likeness* and a *condition of reception*. A likeness: we ask to be treated as we treat — the same measure, the same kind of thing; Jesus says elsewhere "forgive, and ye shall be forgiven" (Luke 6:37) and "Blessed are the merciful: for they shall obtain mercy" (5:7), and James puts it negatively, "he shall have judgment without mercy, that hath shewed no mercy" (James 2:13). And a condition of reception, in exactly the sense the parable shows: forgiveness received is forgiveness that changes the one receiving it, so that a person who will not forgive is a person who has not received. The petition does not say "forgive us *because* we forgive." It says: we, who are ourselves creditors of small sums, remit them; do thou, to whom we owe everything, remit ours. Luke's version makes this plainer with its "for": "forgive us our sins; *for* we also forgive every one that is indebted to us" — not a merit pleaded but a fact stated, the fact that the one praying is standing in the position of a forgiver and asking to be forgiven. And the manuscript variant in Matthew, "as we *have* forgiven" (see [The other variants](#the-other-variants)), makes the forgiving prior to the asking. On any reading, the disciple's forgiving is real, and the prayer cannot be honestly prayed by someone who refuses it.

The Fathers noticed something else: the petition, prayed by an unforgiving person, is a prayer against himself. Augustine and Chrysostom both warned their congregations that whoever says "forgive us as we forgive" while holding a grudge is asking God, in so many words, not to forgive him. There is no way to soften that. The remedy is not to stop praying the petition but to stop holding the grudge, and the Sermon has already said the same thing about worship in general:

> **Matthew 5:23** — Therefore if thou bring thy gift to the altar, and there rememberest that thy brother hath ought against thee;

> **Matthew 5:24** — Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift.

**What the petition assumes.** It assumes that disciples sin, daily, after they have been forgiven. It is the fifth petition of a prayer given to those who already call God Father; it is not the prayer of a stranger asking to be admitted but the prayer of a child asking to be cleaned. The apostle John says the same to the church:

> **1 John 1:8** — If we say that we have no sin, we deceive ourselves, and the truth is not in us.

> **1 John 1:9** — If we confess our sins, he is faithful and just to forgive us our sins, and to cleanse us from all unrighteousness.

Augustine called the fifth petition the church's daily washing: baptism once, for the whole debt; this petition every day, for the day's. The question of what confession the petition implies, and to whom, is taken up in [`confession-in-the-bible.md`](confession-in-the-bible.md); the bearing of Matthew 6:14–15 on whether a Christian can finally fall is taken up in [`once-saved-always-saved.md`](once-saved-always-saved.md). What is not in doubt is what the petition itself does: it puts, every day, into the mouth of every Christian, both the admission that they are a debtor and the undertaking that they will not be a creditor.

---

## "And lead us not into temptation"

> **Matthew 6:13** — And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen.

> **Luke 11:4** — And forgive us our sins; for we also forgive every one that is indebted to us. And lead us not into temptation; but deliver us from evil.

This is the petition that has drawn the most objection, for an obvious reason: it seems to ask God not to do something Scripture says he never does.

> **James 1:13** — Let no man say when he is tempted, I am tempted of God: for God cannot be tempted with evil, neither tempteth he any man:

> **James 1:14** — But every man is tempted, when he is drawn away of his own lust, and enticed.

The answer lies in the two words the petition uses.

**"Temptation."** Πειρασμός (Strong's G3986) means *a test*. Strong's definition is careful about the breadth: "a putting to proof (by experiment (of good), experience (of evil), solicitation, discipline or provocation); by implication, adversity." Dodson: "(a) trial, probation, testing, being tried, (b) temptation, (c) calamity, affliction." The word does not say which way the test will go. James uses it in both senses in one paragraph, and the KJV has to change the English to keep up:

> **James 1:2** — My brethren, count it all joy when ye fall into divers temptations;

> **James 1:12** — Blessed is the man that endureth temptation: for when he is tried, he shall receive the crown of life, which the Lord hath promised to them that love him.

The "temptations" of verse 2 are trials, to be counted joy; the "tempted" of verse 13 is enticement to sin, which is never from God. Same word. The difference is in who is doing it and to what end.

The Old Testament word behind it, נָסָה, *nasah* (H5254), "to test, to prove," has the same breadth, and the KJV translates it *tempt* without embarrassment when God is the subject:

> **Genesis 22:1** — And it came to pass after these things, that God did tempt Abraham, and said unto him, Abraham: and he said, Behold, here I am.

> **Deuteronomy 8:2** — And thou shalt remember all the way which the LORD thy God led thee these forty years in the wilderness, to humble thee, and to prove thee, to know what was in thine heart, whether thou wouldest keep his commandments, or no.

> **Deuteronomy 13:3** — Thou shalt not hearken unto the words of that prophet, or that dreamer of dreams: for the LORD your God proveth you, to know whether ye love the LORD your God with all your heart and with all your soul.

> **Psalms 26:2** — Examine me, O LORD, and prove me; try my reins and my heart.

God tested Abraham on Moriah; he tested Israel in the wilderness, with hunger and with the manna; David asks to be tested. God tests. What God does not do is *entice* — draw a person toward sin with the intention that they fall. The devil does that, and the Gospels call him by the name: "the tempter" (Matthew 4:3). Both can be present in the same event. Jesus "was led up of the Spirit into the wilderness to be tempted of the devil" (Matthew 4:1): the Spirit led, the devil tempted, God tested, and one event was all three. Job is the same: God permits ("Behold, all that he hath is in thy power," Job 1:12), Satan afflicts, and Job is tried. Hezekiah is the same: "God left him, to try him, that he might know all that was in his heart" (2 Chronicles 32:31). Israel, in the wilderness, turned it round and tested *God* (Exodus 17:7; Psalm 95:8–9), which Jesus refused to do when the devil proposed it: "Thou shalt not tempt the Lord thy God" (Matthew 4:7, quoting Deuteronomy 6:16).

So the petition's "temptation" is the test — the situation in which one may stand or fall. It is not asking God not to entice, which he does not do. It is asking him not to bring us to the trial.

**"Lead us not into."** Μὴ εἰσενέγκῃς ἡμᾶς εἰς, from εἰσφέρω (G1533), "carry in, bring into" (the KJV elsewhere: "bring in," "lead into"). Three things can be said about what this asks.

*First,* it is the very prayer Jesus told the disciples to pray in Gethsemane, and the noun is the same:

> **Matthew 26:41** — Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak.

> **Luke 22:40** — And when he was at the place, he said unto them, Pray that ye enter not into temptation.

> **Luke 22:46** — And said unto them, Why sleep ye? rise and pray, lest ye enter into temptation.

"That ye *enter not into* temptation" — εἰσέλθητε εἰς πειρασμόν — is the sixth petition in the second person. The disciples had been told to pray it, that night; they slept instead, and within hours every one of them had entered and fallen. Peter, who a few hours earlier had said "Though all men shall be offended because of thee, yet will I never be offended" (Matthew 26:33), fell furthest. The sixth petition is the opposite of Peter's boast. It is the prayer of someone who knows what they are made of and would rather not find out.

*Second,* the form "do not bring us into" can carry a permissive sense: *do not let us be brought into, do not allow us to enter.* Hebrew and Aramaic causative verbs often mean "let happen" as well as "make happen," and Semitic prayer freely attributes to God's will what happens under his permission. A Jewish morning prayer preserved in the Talmud asks, in words strikingly close to the petition, that God "bring me not into the power of sin, nor into the power of iniquity, nor into the power of temptation." Isaiah prays in the same idiom, and more starkly:

> **Isaiah 63:17** — O LORD, why hast thou made us to err from thy ways, and hardened our heart from thy fear? Return for thy servants' sake, the tribes of thine inheritance.

The earliest Latin-speaking Christians read the petition permissively. Tertullian, around AD 200, glosses it "do not suffer us to be led into temptation," and Cyprian, fifty years later, quotes it as *ne nos patiaris induci in tentationem* — "suffer us not to be led into"; Augustine notes that many Latin copies in his day read the same. In 2017 the French Catholic bishops changed their liturgical text from "do not submit us to temptation" to "do not let us enter into temptation," and in 2020 the Italian bishops adopted "do not abandon us to temptation," after Pope Francis had said publicly that "lead us not" was not a good translation, since a father does not lead his children into temptation. The ecumenical English text of 1988 has "Save us from the time of trial." None of these is a mistranslation of the Greek, and none is exactly what the Greek says. The Greek says "bring." The permissive reading is a judgment about what the Aramaic behind the Greek meant, supported by the idiom, by Isaiah 63:17, and by the fact that Scripture elsewhere denies that God entices. The plain reading — that God, who tests, is asked not to bring us to the test — needs no such help, and is what the petition has meant to most of the people who have prayed it.

*Third,* the petition is not a request never to be tried. Trials are promised, and the same James who says God tempts no one says to count them joy; Peter says believers are "in heaviness through manifold temptations" for a season, "if need be" (1 Peter 1:6). What the petition asks is two things. It asks, in humility, not to be brought to the test: *I know my weakness; do not put it to the proof.* And it asks, for the test that comes anyway, not to be brought *into* it in the sense of entering and staying — not to fall. The Psalms pray this in form as well as substance:

> **Psalms 141:4** — Incline not my heart to any evil thing, to practise wicked works with men that work iniquity: and let me not eat of their dainties.

> **Psalms 19:13** — Keep back thy servant also from presumptuous sins; let them not have dominion over me: then shall I be upright, and I shall be innocent from the great transgression.

> **Psalms 119:133** — Order my steps in thy word: and let not any iniquity have dominion over me.

"Incline not my heart to any evil thing" is the sixth petition in the Psalter's words, and it does not trouble anyone that David asks God not to incline his heart to evil. He is asking the one who governs hearts to govern his toward good. So is the disciple.

**The promise behind the petition.** The petition is prayed against the background of a guarantee, and the guarantee uses the same word:

> **1 Corinthians 10:13** — There hath no temptation taken you but such as is common to man: but God is faithful, who will not suffer you to be tempted above that ye are able; but will with the temptation also make a way to escape, that ye may be able to bear it.

> **2 Peter 2:9** — The Lord knoweth how to deliver the godly out of temptations, and to reserve the unjust unto the day of judgment to be punished:

> **Hebrews 2:18** — For in that he himself hath suffered being tempted, he is able to succour them that are tempted.

> **Hebrews 4:15** — For we have not an high priest which cannot be touched with the feeling of our infirmities; but was in all points tempted like as we are, yet without sin.

And when the test does come to one of his own, the Gospels show what Jesus does about it:

> **Luke 22:31** — And the Lord said, Simon, Simon, behold, Satan hath desired to have you, that he may sift you as wheat:

> **Luke 22:32** — But I have prayed for thee, that thy faith fail not: and when thou art converted, strengthen thy brethren.

Satan asked; God permitted; Peter was sifted; Jesus had prayed; Peter fell and was restored. That is the sixth petition, answered.

**One last link.** The prayer that asks for bread also asks not to be led into the test, and Exodus 16:4 ties the two together: the daily bread *was* the test — "that I may prove them" — and the ones who failed it were the ones who tried to keep tomorrow's. Whoever has learned to ask for one day's bread has already learned most of what the sixth petition teaches.

---

## "But deliver us from evil"

> **Matthew 6:13** — And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen.

**The words.** Ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ — "but rescue us from the evil." Ῥύομαι (Strong's G4506) is a strong word: "to rush or draw (for oneself), i.e. rescue" — to drag someone out of danger. It occurs eighteen times in the Textus Receptus and the KJV renders it *deliver* every time. Paul uses it for the great rescues:

> **Romans 7:24** — O wretched man that I am! who shall deliver me from the body of this death?

> **Colossians 1:13** — Who hath delivered us from the power of darkness, and hath translated us into the kingdom of his dear Son:

> **Galatians 1:4** — Who gave himself for our sins, that he might deliver us from this present evil world, according to the will of God and our Father:

The ἀλλά, "but," binds this clause to the one before it: not *into* the trial, but *out of* the evil. The sixth and seventh clauses are one movement, which is why so many count them as one petition.

**"Evil" or "the evil one."** Τοῦ πονηροῦ is a genitive singular, and the masculine and neuter forms are identical. The phrase can mean "from evil" (the thing) or "from the evil one" (the person), and the grammar cannot decide. Strong's own entry for πονηρός lists both: in the neuter, "mischief, malice"; in the masculine, "the devil." The evidence has to come from usage, and the usage points one way more than the other.

Matthew uses ὁ πονηρός, with the article, as a name for the devil:

> **Matthew 13:19** — When any one heareth the word of the kingdom, and understandeth it not, then cometh the wicked one, and catcheth away that which was sown in his heart. This is he which received seed by the way side.

> **Matthew 13:38** — The field is the world; the good seed are the children of the kingdom; but the tares are the children of the wicked one;

The KJV's "the wicked one" in both places is the same Greek as the prayer's "evil." John uses the phrase the same way, and in his first letter the personal sense is beyond doubt:

> **1 John 2:14** — I have written unto you, fathers, because ye have known him that is from the beginning. I have written unto you, young men, because ye are strong, and the word of God abideth in you, and ye have overcome the wicked one.

> **1 John 3:12** — Not as Cain, who was of that wicked one, and slew his brother. And wherefore slew he him? Because his own works were evil, and his brother's righteous.

> **1 John 5:18** — We know that whosoever is born of God sinneth not; but he that is begotten of God keepeth himself, and that wicked one toucheth him not.

And in two places the New Testament uses almost the prayer's exact phrase, and the KJV, uncertain, translated it two different ways:

> **John 17:15** — I pray not that thou shouldest take them out of the world, but that thou shouldest keep them from the evil.

> **2 Thessalonians 3:3** — But the Lord is faithful, who shall stablish you, and keep you from evil.

John 17:15 is Jesus' own prayer for the disciples on the night before he died, and it is the seventh petition prayed by its author for his people: "keep them from *the* evil" — the translators kept the article, sensing a person. Ephesians 6:16, "the fiery darts of the wicked," is the same word, and there it can only be the devil, who shoots. Add that the previous clause has just spoken of temptation, whose agent is "the tempter," and that the Greek fathers — Chrysostom says flatly, "here he calls the devil the wicked one" — read it personally, and the case for "the evil one" is strong. The Latin *a malo* is as ambiguous as the Greek; Luther's catechism took it as "every evil of body and soul"; Calvin thought it made little difference; modern English versions divide, some printing "the evil one" and some "evil" with a note.

The right conclusion is probably "the evil one," and it is certainly not a mistake to say "evil." In Scripture evil is never impersonal for long — "your adversary the devil, as a roaring lion, walketh about, seeking whom he may devour" (1 Peter 5:8) — and the devil is never anything but evil. Whoever prays "deliver us from evil" and remembers the lion has prayed the petition rightly. Whoever prays "deliver us from the evil one" and forgets that evil also lives in their own heart (Matthew 15:19; James 1:14) has prayed it too narrowly.

**The Old Testament behind it.** The Psalms are the school of this petition, and the Hebrew word is רַע, *ra* (H7451), which is as broad as the Greek: "bad or (as noun) evil (natural or moral)."

> **Psalms 121:7** — The LORD shall preserve thee from all evil: he shall preserve thy soul.

> **Psalms 23:4** — Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.

> **Psalms 34:19** — Many are the afflictions of the righteous: but the LORD delivereth him out of them all.

> **Psalms 91:3** — Surely he shall deliver thee from the snare of the fowler, and from the noisome pestilence.

> **Psalms 97:10** — Ye that love the LORD, hate evil: he preserveth the souls of his saints; he delivereth them out of the hand of the wicked.

> **Psalms 140:1** — Deliver me, O LORD, from the evil man: preserve me from the violent man;

> **2 Samuel 22:2** — And he said, The LORD is my rock, and my fortress, and my deliverer;

**What it asks.** Rescue — now, daily, and finally. The petition covers the evil that is in the world, the evil that is in the one praying, and the evil one who works through both, and it asks the Father to pull his children out of all three. Its answer is promised in the same terms:

> **2 Timothy 4:18** — And the Lord shall deliver me from every evil work, and will preserve me unto his heavenly kingdom: to whom be glory for ever and ever. Amen.

> **Jude 1:24** — Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory with exceeding joy,

And it asks the one praying to take the side they have prayed for: "Be not overcome of evil, but overcome evil with good" (Romans 12:21); "Put on the whole armour of God, that ye may be able to stand against the wiles of the devil" (Ephesians 6:11). The petitions of the prayer end here, on the far side of the last danger, with the Father's rescue. That is where the gospel ends too. The prayer has moved from heaven (the name, the kingdom, the will) to earth (bread) to the depths (debt, trial, the evil one), and from the depths it looks up.

---

## "For thine is the kingdom, and the power, and the glory, for ever. Amen"

> **Matthew 6:13** — And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen.

[Part I](#the-doxology-where-for-thine-is-the-kingdom-came-from) showed that this sentence is the church's and not Matthew's, that it was being said within a generation of the apostles, and that its words are David's from 1 Chronicles 29:11. What remains is to say what it does.

**"For."** Ὅτι — "because." The doxology is not a separate act of praise tacked on; it is the *ground* of everything asked. We ask for the kingdom to come because the kingdom is his. We ask for his will to be done and for deliverance because the power is his. We ask for his name to be hallowed because the glory is his. The three nouns answer the three "thy" petitions in reverse, and the "for" says that the petitions were never presumptuous, because they only asked God to be what he is. The Westminster Shorter Catechism (Question 107) puts it in one sentence: the conclusion "teacheth us to take our encouragement in prayer from God only, and in our prayers to praise him, ascribing kingdom, power, and glory to him."

**The words are heaven's.** What the church added to the prayer on earth is what John heard being sung above:

> **Revelation 4:11** — Thou art worthy, O Lord, to receive glory and honour and power: for thou hast created all things, and for thy pleasure they are and were created.

> **Revelation 5:13** — And every creature which is in heaven, and on the earth, and under the earth, and such as are in the sea, and all that are in them, heard I saying, Blessing, and honour, and glory, and power, be unto him that sitteth upon the throne, and unto the Lamb for ever and ever.

> **Revelation 7:12** — Saying, Amen: Blessing, and glory, and wisdom, and thanksgiving, and honour, and power, and might, be unto our God for ever and ever. Amen.

> **Revelation 12:10** — And I heard a loud voice saying in heaven, Now is come salvation, and strength, and the kingdom of our God, and the power of his Christ: for the accuser of our brethren is cast down, which accused them before our God day and night.

Revelation 12:10 is the doxology with the seventh petition answered inside it: the kingdom, the power — and the accuser cast down.

**"Amen."** Ἀμήν (G281) is the Hebrew אָמֵן, *amen* (H543), untranslated: "sure; faithfulness; truly." It is the word by which a congregation makes a prayer its own:

> **Deuteronomy 27:26** — Cursed be he that confirmeth not all the words of this law to do them. And all the people shall say, Amen.

> **1 Chronicles 16:36** — Blessed be the LORD God of Israel for ever and ever. And all the people said, Amen, and praised the LORD.

> **Nehemiah 8:6** — And Ezra blessed the LORD, the great God. And all the people answered, Amen, Amen, with lifting up their hands: and they bowed their heads, and worshipped the LORD with their faces to the ground.

> **1 Corinthians 14:16** — Else when thou shalt bless with the spirit, how shall he that occupieth the room of the unlearned say Amen at thy giving of thanks, seeing he understandeth not what thou sayest?

It is also the word Jesus used, alone among the teachers of his day, at the *beginning* of his sentences — "Verily I say unto you" is ἀμὴν λέγω ὑμῖν — and the name he is given in the last book:

> **2 Corinthians 1:20** — For all the promises of God in him are yea, and in him Amen, unto the glory of God by us.

> **Revelation 3:14** — And unto the angel of the church of the Laodiceans write; These things saith the Amen, the faithful and true witness, the beginning of the creation of God;

At the end of the Lord's Prayer, then, "Amen" is the signature of the one praying: *so be it — and it is sure.* It is not a sigh of hope. Luther's catechism: "Amen, Amen; that is, Yea, yea, it shall be so." The Heidelberg Catechism's last answer (Question 129) is the best of all: "Amen signifies, it shall truly and certainly be: for my prayer is more assuredly heard of God, than I feel in my heart that I desire these things of him."

---
---

# Part III — Praying It

## Pattern or formula?

Matthew introduces the prayer with "After this manner therefore pray ye" — οὕτως, *thus, in this way*. Luke introduces it with "When ye pray, say" — λέγετε, *say*. The first makes it a pattern, the second a text, and Christians have sometimes divided over which it is. The division is false. The church that wrote the *Didache*, about AD 100, quoted Matthew's introduction and then told its readers to *say* the prayer three times a day; it read "thus" and did "say." Both were right.

**As a text.** The prayer is the only one Jesus gave, and it was given to be prayed. The disciples asked "teach us to pray" and were given words. Luke's "say" is not a slip. There is no evidence that any Christian body before the modern period doubted that the words themselves should be said, and every liturgy in existence says them.

**As a pattern.** The prayer is also a rule for all prayer, and the ancient writers valued it most for this. Tertullian called it "a summary of the whole gospel." Augustine told Proba that if she went through every prayer in Scripture she would find nothing that this prayer did not contain. Calvin taught that it lays down what may be asked, in what order, and with what confidence, and that a prayer which asks for something the Lord's Prayer excludes is not a Christian prayer — while adding that Christians are not bound to its syllables, only to its substance. The Westminster Shorter Catechism (Question 99): "The whole Word of God is of use to direct us in prayer; but the special rule of direction is that form of prayer which Christ taught his disciples, commonly called the Lord's Prayer." So the prayer is prayed in its own words, and it is also the measure of every other prayer: what to ask for, what to ask for first, who is being asked, and on whose behalf.

**The objection from Matthew 6:7.** It is sometimes said that a prayer given as the alternative to "vain repetitions" cannot have been meant to be repeated, and that the most repeated words in human history are therefore a standing misuse of the passage that contains them. The objection misreads the verse. "Use not vain repetitions" is one Greek verb, βατταλογέω, whose sense is to babble, to pile up words — and the reason is given: "for they think that they shall be heard for their much speaking." The fault is not saying the same words twice; it is the belief that volume moves God. Elijah's contest on Carmel is the picture:

> **1 Kings 18:26** — And they took the bullock which was given them, and they dressed it, and called on the name of Baal from morning even until noon, saying, O Baal, hear us. But there was no voice, nor any that answered. And they leaped upon the altar which was made.

> **1 Kings 18:29** — And it came to pass, when midday was past, and they prophesied until the time of the offering of the evening sacrifice, that there was neither voice, nor any to answer, nor any that regarded.

Six hours of "O Baal, hear us." Elijah's prayer that follows is two verses long. Meanwhile Jesus himself, in Gethsemane, "prayed the third time, saying the same words" (Matthew 26:44); Paul "besought the Lord thrice" about one thing (2 Corinthians 12:8); and the two parables Luke attaches to prayer — the friend at midnight (11:5–8) and the widow before the judge (18:1–8) — commend exactly the persistence the objection would forbid. The vice is not repetition. It is emptiness: words said to be heard for their number, or said with no one listening on the speaker's side either.

**The real test.** A pattern that is never said becomes a theory; a text that is only said becomes a charm. The test of either use is the one Jesus gives at the end of the Sermon, and Luke puts it in one sentence:

> **Luke 6:46** — And why call ye me, Lord, Lord, and do not the things which I say?

> **Matthew 7:21** — Not every one that saith unto me, Lord, Lord, shall enter into the kingdom of heaven; but he that doeth the will of my Father which is in heaven.

Whoever says "thy will be done" and does not do it has said the words and not prayed the prayer. Whoever has never said the words but does the will has come nearer. The prayer is meant to be said, understood, meant, and then done.

---

## What the prayer assumes

A prayer reveals what the one praying believes about the one prayed to. Read as a set of assumptions, the Lord's Prayer is a short creed.

**About God.** He is *Father*: near, kind, and giving, and the relation is a family one. He is *in heaven*: able to do what is asked. His name is *holy*, and the one praying wants it treated so. He is *king*, and his reign is coming. He has a *will*, and it is good. He *feeds*, and the bread comes from his hand. He *forgives*, and the forgiving is his to give. He *leads*, and the way runs through trials he governs. He *delivers*, and the enemy is real and is his enemy. And the kingdom, the power, and the glory are *his*, which is why any of it can be asked.

**About the one praying.** They are a *child*, with a right to speak that was given them. They are *not alone*: every "our" and "us" places them in a company. Their needs are *no greater than bread*: the prayer asks for nothing beyond a day's food. They are a *debtor*, and know it. They are *weak*: they would rather not be tested. They are *in danger*: there is an evil to be rescued from. And they are *bound*: they have undertaken, in the act of asking pardon, to grant it.

**What is not in it.** There is no *I*, *me*, or *my* anywhere in the prayer. The first person appears nine times in Matthew's five verses and it is plural every time:

```sh
grep -E '^Matthew 6:(9|10|11|12|13) ' kjv/kjv.txt | grep -oiE '\b(our|us|we)\b' | sort | uniq -c
#   1 Our    3 our    4 us    1 we
```

There is also no mention of the one praying's merits, standing, works, or feelings — nothing of what the Pharisee in the temple listed, "I fast twice in the week, I give tithes of all that I possess" (Luke 18:12). The prayer that Jesus commends in that parable is seven words long and asks for one thing: "God be merciful to me a sinner" (18:13). The Lord's Prayer is its longer form.

Cyprian, in the third century, made the point that has been repeated ever since: "We do not say *My* Father, which art in heaven, nor *Give me this day my* daily bread... Our prayer is public and common; and when we pray, we pray not for one, but for the whole people, because we the whole people are one."

---

## The order of the petitions

The prayer begins with God and ends with us, and the order is the lesson. Three petitions for God's honour, reign, and will come before a single word about food. This is not because bread does not matter — it is the first thing asked for once the turn comes — but because the prayer trains desire. Whoever prays it daily is taught daily what to want first. The Sermon states the same order as a command fourteen verses later:

> **Matthew 6:33** — But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.

The Psalms do not always keep this order; many begin from the pit and reach God's glory only at the end, and no one is forbidden to cry for bread first when the need is sharp. But the prayer given as the pattern begins from the top, and a person whose ordinary praying began there would find, over time, that their wanting had been rearranged.

Within the second half there is an order too: bread for the body and the present; forgiveness for the conscience and the past; keeping and deliverance for the will and the future. The three petitions descend from the simplest need to the deepest, and the last of them is prayed from the edge of the pit, looking up — which is where the doxology comes in.

---

## The plural

The prayer cannot be prayed by a Christian alone, even when they are alone. Every petition is "our" and "us," and the one praying in a closed room (Matthew 6:6) prays it with the whole church, for the whole church.

This has three practical edges. **It is intercession.** "Give us this day our daily bread" is prayed for the hungry; "forgive us our debts" for the whole company of debtors; "lead us not into temptation" for the brother who is at that moment being tested. Whoever prays the prayer has prayed for everyone in it. **It is obligation.** One who asks the Father for "our" bread and has more than a day's worth is, by the prayer, made responsible for the one who has less; the prayer cannot be said in good faith over a full table by someone indifferent to the empty one next door (James 2:15–16; Deuteronomy 15:9–10). **It is company.** No one prays "our Father" as an orphan. The prayer assumes brothers and sisters, and it is one of the reasons the church has always said it together, aloud, in one voice.

---

## The petition with a condition in it

One clause of the prayer is unlike the others: it states something about the one praying as a fact — "as we forgive our debtors" — and Jesus stops to say what follows if the fact is not true (Matthew 6:14–15; 18:35; Mark 11:25–26). Part II examined the clause. This section is about what to do with it.

**Examine before praying.** The liturgies have always placed the prayer with this in mind. The Prayer Book's Morning and Evening Prayer put it after the confession and absolution; the Communion service puts it just before the bread is broken, and the ancient practice of exchanging the peace before communion rests on Matthew 5:23–24 — be reconciled, then come. Gregory the Great fixed the prayer's place in the Mass at the end of the great thanksgiving, so that the people asked forgiveness with the sacrifice before them. The wisdom of these arrangements is available to anyone: before saying "forgive us our debts, as we forgive our debtors," name to yourself whom you have not forgiven. The petition cannot be prayed around that name. It can only be prayed through it.

**The clause is a promise as much as a warning.** The same Jesus who says the unforgiving will not be forgiven says that the forgiving will be — "forgive, and ye shall be forgiven" (Luke 6:37) — and the ten-thousand-talent parable exists to show what has already been remitted before any of us is asked to remit anything. The person who finds the clause impossible has usually not yet felt the weight of the first debt. The remedy is to look at it.

---

## How the church has prayed it

The history of the prayer's use is longer than the history of any other Christian words, and a sketch of it shows what each age found in it.

**The first century.** The *Didache*, a church manual of about AD 100, gives Matthew's text with the short doxology and directs: "Pray thus three times a day." Three times a day was the Jewish rule — "Evening, and morning, and at noon, will I pray" (Psalm 55:17); Daniel "kneeled upon his knees three times a day" (Daniel 6:10); Peter and John went up "at the hour of prayer, being the ninth hour" (Acts 3:1) — and the Jewish Christians who wrote the *Didache* apparently put the Lord's Prayer where the Eighteen Benedictions had been.

**The second and third centuries.** Tertullian in North Africa (about 200) wrote the first commentary, *On Prayer*, and called the prayer "a summary of the whole gospel." Origen in Alexandria (about 233) wrote *On Prayer* and gave us the note on ἐπιούσιος. Cyprian of Carthage (about 252) wrote *On the Lord's Prayer* and made the point about "our." All three expound the prayer petition by petition, and all three end at "deliver us from evil."

**The fourth century: the prayer handed over.** In the great churches of this period the Lord's Prayer was taught to converts only at the end of their preparation, in the weeks before their baptism at Easter, in a rite the Latins called the *traditio orationis*, the "handing over of the prayer." The reason was Romans 8:15: no one could say "Father" until the Spirit of adoption had been given. The newly baptised said the prayer aloud for the first time at their first communion, immediately before receiving. Four of Augustine's sermons (56–59) were preached at this handing-over; Cyril of Jerusalem's last lecture to the newly baptised walks them through the prayer as they will say it at the Lord's table; Gregory of Nyssa preached five homilies on it and Chrysostom expounded it in his nineteenth homily on Matthew. Augustine wrote on it three times more: in his commentary on the Sermon on the Mount (about 394), where he counted seven petitions; in the letter to Proba (412), where he said it contained all prayer; and in the *Enchiridion*, where he called the fifth petition the church's daily washing for daily sins.

**The Mass.** About the year 600 Gregory the Great moved the prayer to the place it has held in the Western liturgy ever since, immediately after the great thanksgiving and before communion, remarking that the apostles had consecrated with this prayer alone. The Eastern liturgies place it in the same position, the people singing the petitions and the priest alone the doxology. In the West the doxology was not said in the Mass — the Vulgate did not have it — until the reformed Missal of 1970 restored it, after a short prayer that expands "deliver us from evil."

**The Middle Ages.** The *Pater noster* was, with the Creed and the Hail Mary, the whole of what every Christian was required to know, and it was known in Latin. Strings of beads for counting it were called *paternosters* and the London street where they were made is still Paternoster Row; the English word *patter*, for rapid meaningless speech, is what the prayer sounded like said fast in a language the sayer did not understand — a fate Matthew 6:7 had warned against. The rosary as it took shape in this period begins each of its decades with the Our Father. Wycliffe's followers put the prayer into English in the 1380s, and were prosecuted for it.

**The Reformation.** Luther's *Small Catechism* (1529) made the prayer one of the three things every household was to learn — the Ten Commandments, the Creed, the Lord's Prayer — and gave each petition the question "What does this mean?" with an answer a child could repeat; his *Large Catechism* expounded it at length, and his 1535 tract *A Simple Way to Pray*, written for his barber, showed how to pray through it slowly (see [A practical way to pray it](#a-practical-way-to-pray-it)). Calvin's *Institutes* (III.xx.34–49) treated it as the rule of all prayer and counted six petitions. Cranmer's Book of Common Prayer (1549) put it in every service — Morning and Evening Prayer, the Litany, Holy Communion, Baptism, Confirmation, Matrimony, the Visitation of the Sick, Burial — and every English-speaking Christian for four centuries learned it in the Prayer Book's words. The Heidelberg Catechism (1563) and the Westminster Shorter Catechism (1647) both end with the Lord's Prayer, question by question, as the last thing a Christian is taught; the Roman Catechism of Trent (1566) expounded it in the same three-part frame. The three-part core — Creed, Commandments, Lord's Prayer: what to believe, what to do, what to ask — was common to all of them.

**The present.** The Catechism of the Catholic Church (1992) closes, as the Reformation catechisms had, with the Lord's Prayer, in a section of over a hundred paragraphs that opens by quoting Tertullian's "summary of the whole gospel" and Aquinas' "the most perfect of prayers." The English-Language Liturgical Consultation's ecumenical text (1988) gave the churches a shared modern version. Every Christian body that prays at all prays these words; it is the one prayer said, in some form, at nearly every Christian service on earth, every day.

---

## The English words: from Wycliffe to "trespasses"

The prayer has been in English for over a thousand years, and the version most people know is a patchwork of several. The samples below are given in normalised spelling, since the manuscripts and early printings vary.

**About the year 1000**, the West Saxon Gospels:

> Fæder ure þu þe eart on heofonum, si þin nama gehalgod. To becume þin rice. Gewurþe ðin willa on eorðan swa swa on heofonum. Urne gedæghwamlican hlaf syle us to dæg. And forgyf us ure gyltas, swa swa we forgyfað urum gyltendum. And ne gelæd þu us on costnunge, ac alys us of yfele. Soþlice.

*Gehalgod* is "hallowed"; *rice* is "kingdom" (the word survives in *bishopric*); *gyltas* is "guilts"; *costnunge* is "temptation"; *soþlice* is "truly," the Old English for Amen.

**About 1390**, the Wycliffe Bible:

> Oure fadir that art in heuenes, halewid be thi name; thi kyngdoom come to; be thi wille don in erthe as in heuene; gyue to vs this dai oure breed ouer othir substaunce; and foryyue to vs oure dettis, as we foryyuen to oure dettouris; and lede vs not in to temptacioun, but delyuere vs fro yuel. Amen.

"Oure breed ouer othir substaunce" is Jerome's *supersubstantialem* — the one time the English prayer tried to carry the eucharistic reading of ἐπιούσιος into the words themselves. It did not last.

**1526**, Tyndale's New Testament, the first printed English translation from the Greek:

> Our Father which art in heaven, hallowed be thy name. Let thy kingdom come. Thy will be fulfilled, as well in earth, as it is in heaven. Give us this day our daily bread. And forgive us our trespasses, even as we forgive our trespassers. And lead us not into temptation, but deliver us from evil. For thine is the kingdom and the power, and the glory for ever. Amen.

Tyndale is the source of most of the prayer as English speakers say it — "hallowed," "daily bread," "lead us not into temptation," "deliver us from evil" — and of the word *trespasses*, which he took from Matthew 6:14–15 and put into 6:12 in place of "debts."

**1549**, the first Book of Common Prayer, followed Tyndale, with "which art," "trespasses," and "them that trespass against us," and without the doxology; the 1662 revision added "For thine is the kingdom..." at some points in the services and not at others, and it is the 1662 wording — "Our Father, which art in heaven, Hallowed be thy Name; Thy kingdom come; Thy will be done, in earth as it is in heaven. Give us this day our daily bread. And forgive us our trespasses, As we forgive them that trespass against us. And lead us not into temptation; But deliver us from evil. For thine is the kingdom, the power, and the glory, For ever and ever. Amen." — that most English-speaking Protestants outside the Reformed churches still say.

**1611**, the King James Version, followed the Geneva Bible (1560) in Matthew 6:12 and printed "debts" and "debtors," which is why Presbyterian and Reformed congregations, whose worship followed the Bible's text rather than the Prayer Book's, say "debts" to this day. Roman Catholics in English say "who art" (from the eighteenth-century revision of the Douay-Rheims Bible) and "trespasses," and, until 1970, stopped at "deliver us from evil."

**1988**, the English Language Liturgical Consultation's ecumenical text, now used in many churches of every tradition:

> Our Father in heaven, hallowed be your name, your kingdom come, your will be done, on earth as in heaven. Give us today our daily bread. Forgive us our sins as we forgive those who sin against us. Save us from the time of trial and deliver us from evil. For the kingdom, the power, and the glory are yours now and for ever. Amen.

"Sins" is Luke's word; "the time of trial" is the permissive reading of the sixth petition, and the one line of the text that is widely resisted.

So there are three English families — *debts* (from the KJV), *trespasses* (from Tyndale through the Prayer Book), *sins* (from Luke through the ecumenical text) — and none is more correct than the others. All three translate one Greek petition, and the Greek is not in doubt.

---

## A practical way to pray it

The prayer takes twenty seconds to say and a lifetime to pray. The oldest and best advice on the difference is Luther's, in the tract he wrote for his barber in 1535, and it comes to this: say the prayer through once, and then take it a petition at a time, saying in your own words what each petition asks, for yourself and for those you are praying with. He gives a sample for each petition, and each of his samples does three things: it *thanks* God that the petition is already true of him, it *confesses* where the one praying has stood against it, and it *asks* for it, naming particulars. Applied to the first petition, that means something like: *Father, your name is holy; you have made it known to me and I thank you for it. I have used it lightly this week, and I have let people think less of you because of how I have lived. Make your name holy in me today, in this house, in this church, and in the places where it is despised.* Then the second petition, and so on to the end. Luther adds one warning, and it is the best thing in the tract: if while you are praying one petition the Spirit begins to preach to you, stop, be quiet, and listen — "one word of such a sermon is worth more than a thousand of our prayers."

A second help is to know which Scriptures stand behind each petition, so that the prayer opens outward into the Bible instead of closing in on its own words. The table in [Appendix C](#c-the-old-testament-behind-each-petition) is built for this; a short version for daily use:

| Petition | Pray it with |
| --- | --- |
| Our Father which art in heaven | Psalm 103; Romans 8:14–17; Matthew 7:7–11 |
| Hallowed be thy name | Isaiah 6:1–8; Ezekiel 36:22–28; Matthew 5:13–16 |
| Thy kingdom come | Psalm 145; Daniel 7:9–14; Luke 17:20–21; Revelation 11:15 |
| Thy will be done | Psalm 40:1–8; Matthew 26:36–46; Hebrews 10:5–10 |
| Give us this day our daily bread | Exodus 16; Proverbs 30:7–9; Matthew 6:25–34 |
| Forgive us our debts | Psalm 32; Psalm 130; Matthew 18:21–35 |
| Lead us not into temptation | Psalm 141; James 1:2–15; 1 Corinthians 10:13 |
| Deliver us from evil | Psalm 91; Psalm 121; Ephesians 6:10–18; 2 Timothy 4:18 |
| For thine is the kingdom | 1 Chronicles 29:10–13; Revelation 5:9–14 |

A third help is regularity. The *Didache*'s three times a day was the Jewish rhythm and it has never been improved on; morning and evening is the least the church has ever assumed. Said slowly, aloud, with the petitions expanded as above, the prayer will take ten minutes and will cover, as Augustine said, everything.

---

## Ten common mistakes

1. **Saying it fast.** The prayer given against "much speaking" is more often ruined by speed than by length. Each petition is a sentence; give each one the pause a sentence gets.
2. **Saying "thy will be done" as resignation.** The petition is a request that God's will be *accomplished*, in the same voice as "give us" and "forgive us." Said with a shrug it means the opposite of what it says.
3. **Praying it in the singular.** There is no "I" in it. Whoever prays "give us" and "forgive us" has prayed for everyone in the room and everyone out of it.
4. **Praying for bread while hoarding it.** Exodus 16 is the commentary: what is kept back from the day's need "bred worms, and stank."
5. **Praying "as we forgive" while refusing to.** The Fathers are right: that is praying against oneself. The name of the person one has not forgiven should come to mind at the fifth petition, and should not be prayed past.
6. **Hearing "lead us not into temptation" as an accusation of God.** It is the humility of someone who knows their weakness, prayed to the one who governs their trials; James 1:13 is not contradicted by it.
7. **Treating it as a charm.** The words do not work by being said. Matthew 7:21 stands directly after the Sermon that contains them.
8. **Never saying it,** for fear of rote. Luke's "when ye pray, say" is as much Scripture as Matthew's "after this manner," and the church that first received the prayer said it three times a day.
9. **Only saying it,** as though it replaced one's own words. It is the pattern for them, not the substitute; "in every thing by prayer and supplication with thanksgiving let your requests be made known unto God" (Philippians 4:6).
10. **Dropping the Amen,** or saying it as a full stop. It is a verdict: *it is sure*. The Heidelberg Catechism's last answer is the right one to end on — "my prayer is more assuredly heard of God, than I feel in my heart that I desire these things of him."

---
---

# Appendices

## A. The two texts in six Greek editions

The six Greek New Testaments in [`original-languages/greek/`](original-languages/greek) can be compared at any verse with one loop:

```sh
for e in tr-scrivener kjtr byzantine sblgnt nestle1904 sr; do
  echo "== $e"; grep -E '^Matthew 6:(9|10|11|12|13) ' original-languages/greek/$e.txt
done
```

Two of them suffice to show every difference that matters. **The Textus Receptus** (KJTR, accented), the text behind the KJV:

> Matthew 6:9 — Οὕτως οὖν προσεύχεσθε ὑμεῖς: Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς, Ἁγιασθήτω τὸ ὄνομά σου.
> Matthew 6:10 — Ἐλθέτω ἡ βασιλεία σου. Γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῷ καὶ ἐπὶ τῆς γῆς.
> Matthew 6:11 — Τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δὸς ἡμῖν σήμερον.
> Matthew 6:12 — Καὶ ἄφες ἡμῖν τὰ ὀφειλήματα ἡμῶν, ὡς καὶ ἡμεῖς ἀφίεμεν τοῖς ὀφειλέταις ἡμῶν.
> Matthew 6:13 — Καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν, ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ: Ὅτι σοῦ ἐστιν ἡ βασιλεία, καὶ ἡ δύναμις, καὶ ἡ δόξα, εἰς τοὺς αἰῶνας. Ἀμήν.
> Luke 11:2 — Εἷπεν δὲ αὐτοῖς, Ὅταν προσεύχησθε, λέγετε, Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοις, Ἁγιασθήτω τὸ ὄνομά σου. Ἐλθέτω ἡ βασιλεία σου. Γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῳ, καὶ ἐπὶ τὴς γὴς.
> Luke 11:3 — Τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δίδου ἡμῖν τὸ καθʼ ἡμέραν.
> Luke 11:4 — Καὶ ἄφες ἡμῖν τὰς ἁμαρτίας ἡμῶν· καὶ γὰρ αὐτοὶ ἀφίεμεν παντὶ ὀφείλοντι ἡμῖν. Καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν· ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ.

**The SBLGNT**, following the oldest manuscripts:

> Matthew 6:9 — Οὕτως οὖν προσεύχεσθε ὑμεῖς· Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς· ἁγιασθήτω τὸ ὄνομά σου,
> Matthew 6:10 — ἐλθέτω ἡ βασιλεία σου, γενηθήτω τὸ θέλημά σου, ὡς ἐν οὐρανῷ καὶ ἐπὶ γῆς·
> Matthew 6:11 — τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δὸς ἡμῖν σήμερον·
> Matthew 6:12 — καὶ ἄφες ἡμῖν τὰ ὀφειλήματα ἡμῶν, ὡς καὶ ἡμεῖς ἀφήκαμεν τοῖς ὀφειλέταις ἡμῶν·
> Matthew 6:13 — καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν, ἀλλὰ ῥῦσαι ἡμᾶς ἀπὸ τοῦ πονηροῦ.
> Luke 11:2 — εἶπεν δὲ αὐτοῖς· Ὅταν προσεύχησθε, λέγετε· Πάτερ, ἁγιασθήτω τὸ ὄνομά σου· ἐλθέτω ἡ βασιλεία σου·
> Luke 11:3 — τὸν ἄρτον ἡμῶν τὸν ἐπιούσιον δίδου ἡμῖν τὸ καθʼ ἡμέραν·
> Luke 11:4 — καὶ ἄφες ἡμῖν τὰς ἁμαρτίας ἡμῶν, καὶ γὰρ αὐτοὶ ἀφίομεν παντὶ ὀφείλοντι ἡμῖν· καὶ μὴ εἰσενέγκῃς ἡμᾶς εἰς πειρασμόν.

How the six editions line up on the four points of difference:

| Reading | TR (Scrivener, KJTR) | Byzantine | SBLGNT | Nestle 1904 | SR |
| --- | --- | --- | --- | --- | --- |
| Matthew 6:13 doxology | present | present | absent | absent | absent |
| Matthew 6:12 "we forgive" | ἀφίεμεν (present) | ἀφίεμεν | ἀφήκαμεν (aorist) | ἀφήκαμεν | ἀφήκαμεν |
| Luke 11:2 "Our... which art in heaven" | present | present | absent | absent | absent |
| Luke 11:2 "Thy will be done..." | present | present | absent | absent | absent |
| Luke 11:4 "but deliver us from evil" | present | present | absent | absent | absent |

The Byzantine text is the majority of the medieval Greek manuscripts; the Textus Receptus is the sixteenth-century printed text drawn from a handful of them; the other three are modern reconstructions from the earliest witnesses. On every one of the five points the line runs between the two groups, and on every one the KJV follows the first.

---

## B. Every word of the prayer

Matthew 6:9–13, word by word, from the interlinear in [`original-languages/interlinear/`](original-languages/interlinear), which follows the Byzantine text (so it reads ἀφίεμεν in verse 12, with the KJV). The English is a gloss, not the KJV. To reproduce:

```sh
grep -E '^Matthew 6:(9|10|11|12|13)\b' original-languages/interlinear/nt-interlinear.tsv
```

| Verse | Greek | Transliteration | Parsing | Strong's | Gloss |
| --- | --- | --- | --- | --- | --- |
| 6:9 | Οὕτως | houtōs | adverb | G3779 | thus, in this way |
| | οὖν | oun | conjunction | G3767 | therefore |
| | προσεύχεσθε | proseuchesthe | pres. imperative, 2 pl. | G4336 | pray |
| | ὑμεῖς | hymeis | pronoun, nom. 2 pl. | G4771 | you |
| | Πάτερ | Pater | noun, vocative | G3962 | Father |
| | ἡμῶν | hēmōn | pronoun, gen. 1 pl. | G1473 | of us, our |
| | ὁ | ho | article | G3588 | the one |
| | ἐν | en | preposition | G1722 | in |
| | τοῖς οὐρανοῖς | tois ouranois | noun, dat. pl. | G3772 | the heavens |
| | ἁγιασθήτω | hagiasthētō | aor. passive imperative, 3 sg. | G0037 | let it be hallowed |
| | τὸ ὄνομά | to onoma | noun, nom. sg. | G3686 | the name |
| | σου | sou | pronoun, gen. 2 sg. | G4771 | of thee, thy |
| 6:10 | ἐλθέτω | elthetō | aor. active imperative, 3 sg. | G2064 | let it come |
| | ἡ βασιλεία | hē basileia | noun, nom. sg. | G0932 | the kingdom |
| | σου | sou | | G4771 | thy |
| | γενηθήτω | genēthētō | aor. passive imperative, 3 sg. | G1096 | let it come to pass |
| | τὸ θέλημά | to thelēma | noun, nom. sg. | G2307 | the will |
| | σου | sou | | G4771 | thy |
| | ὡς | hōs | adverb | G5613 | as |
| | ἐν οὐρανῷ | en ouranō | | G3772 | in heaven |
| | καὶ | kai | conjunction | G2532 | also, and |
| | ἐπὶ τῆς γῆς | epi tēs gēs | preposition + noun, gen. | G1093 | on the earth |
| 6:11 | τὸν ἄρτον | ton arton | noun, acc. sg. | G0740 | the bread |
| | ἡμῶν | hēmōn | | G1473 | our |
| | τὸν ἐπιούσιον | ton epiousion | adjective, acc. sg. | G1967 | the daily / needful |
| | δὸς | dos | aor. active imperative, 2 sg. | G1325 | give |
| | ἡμῖν | hēmin | pronoun, dat. 1 pl. | G1473 | to us |
| | σήμερον | sēmeron | adverb | G4594 | today |
| 6:12 | καὶ | kai | | G2532 | and |
| | ἄφες | aphes | aor. active imperative, 2 sg. | G0863 | remit, forgive |
| | ἡμῖν | hēmin | | G1473 | to us |
| | τὰ ὀφειλήματα | ta opheilēmata | noun, acc. pl. | G3783 | the debts |
| | ἡμῶν | hēmōn | | G1473 | our |
| | ὡς | hōs | | G5613 | as |
| | καὶ | kai | | G2532 | also |
| | ἡμεῖς | hēmeis | pronoun, nom. 1 pl. | G1473 | we |
| | ἀφίεμεν | aphiemen | pres. active indicative, 1 pl. | G0863 | remit, forgive |
| | τοῖς ὀφειλέταις | tois opheiletais | noun, dat. pl. | G3781 | the debtors |
| | ἡμῶν | hēmōn | | G1473 | our |
| 6:13 | καὶ | kai | | G2532 | and |
| | μὴ | mē | negative particle | G3361 | not |
| | εἰσενέγκῃς | eisenenkēs | aor. active subjunctive, 2 sg. | G1533 | bring into |
| | ἡμᾶς | hēmas | pronoun, acc. 1 pl. | G1473 | us |
| | εἰς | eis | preposition | G1519 | into |
| | πειρασμόν | peirasmon | noun, acc. sg. | G3986 | trial, temptation |
| | ἀλλὰ | alla | conjunction | G0235 | but |
| | ῥῦσαι | rhysai | aor. middle imperative, 2 sg. | G4506 | rescue, deliver |
| | ἡμᾶς | hēmas | | G1473 | us |
| | ἀπὸ | apo | preposition | G0575 | from |
| | τοῦ πονηροῦ | tou ponērou | adjective, gen. sg. (masc. or neut.) | G4190 | the evil / the evil one |
| | ὅτι | hoti | conjunction | G3754 | for, because |
| | σοῦ | sou | pronoun, gen. 2 sg. | G4771 | thine |
| | ἐστιν | estin | pres. indicative, 3 sg. | G1510 | is |
| | ἡ βασιλεία | hē basileia | | G0932 | the kingdom |
| | καὶ ἡ δύναμις | kai hē dynamis | noun, nom. sg. | G1411 | and the power |
| | καὶ ἡ δόξα | kai hē doxa | noun, nom. sg. | G1391 | and the glory |
| | εἰς τοὺς αἰῶνας | eis tous aiōnas | preposition + noun, acc. pl. | G0165 | unto the ages, for ever |
| | Ἀμήν | Amēn | Hebrew | G0281 | Amen |

Luke's differences, in the same terms: 11:3 δίδου (*didou*, present imperative, "keep giving") for δός, and τὸ καθ' ἡμέραν (*to kath' hēmeran*, "each day," G2596 + G2250) for σήμερον; 11:4 τὰς ἁμαρτίας (*tas hamartias*, "the sins," G0266) for τὰ ὀφειλήματα, and καὶ γὰρ αὐτοὶ ἀφίεμεν παντὶ ὀφείλοντι ἡμῖν (*kai gar autoi aphiemen panti opheilonti hēmin*, "for we ourselves also forgive everyone owing to us," with G3784 ὀφείλω) for the second half of the petition.

The lexicon entries for the principal words can be pulled directly:

```sh
grep -E '^G(0037|0932|2307|0740|1967|0863|3783|3781|1533|3986|4506|4190|0281)\b' original-languages/lexicons/strongs-greek.tsv
grep -E '^G(0037|0932|2307|0740|1967|0863|3783|3781|1533|3986|4506|4190|0281)\b' original-languages/lexicons/dodson-greek.tsv
```

---

## C. The Old Testament behind each petition

| Petition | Old Testament roots | Synagogue parallel |
| --- | --- | --- |
| Our Father which art in heaven | Exodus 4:22; Deuteronomy 32:6; Psalm 103:13; Isaiah 63:16; 64:8; Jeremiah 3:19; 31:9; Malachi 2:10 (Father). 1 Kings 8:30; Psalm 11:4; 115:3; Ecclesiastes 5:2; Isaiah 66:1 (in heaven) | Sixth Benediction: "Forgive us, *our Father*"; the *Avinu Malkeinu*, "Our Father, our King" |
| Hallowed be thy name | Exodus 3:13–15; 20:7; Leviticus 22:32; Numbers 20:12; Psalm 8:1; 99:3; 111:9; Isaiah 6:3; 8:13; 29:23; Ezekiel 20:9; 36:20–23; 38:23; 39:7 | Kaddish: "Magnified and sanctified be his great name" |
| Thy kingdom come | Psalm 103:19; 145:11–13; Isaiah 52:7; Daniel 2:44; 4:34; 7:13–14, 27; Obadiah 21; Zechariah 14:9 | Kaddish: "may he establish his kingdom in your lifetime" |
| Thy will be done in earth, as it is in heaven | Psalm 40:8; 103:20–21; 115:3; 143:10; Daniel 4:35; Isaiah 55:8–9; Habakkuk 2:14 | Kaddish: "which he created according to his will" |
| Give us this day our daily bread | Exodus 16:4, 16–21; Deuteronomy 8:2–3; 2 Kings 25:30; Psalm 104:14–15; 145:15–16; Proverbs 30:8–9 | Ninth Benediction: "Bless this year... and satisfy us with thy goodness" |
| And forgive us our debts, as we forgive our debtors | Exodus 34:6–7; Deuteronomy 15:1–2; Leviticus 25:10; Nehemiah 5:10–11; 10:31; Psalm 32:1, 5; 51:1–2; 103:3, 10, 12; 130:3–4; Isaiah 1:18; 43:25; 55:7; Jeremiah 31:34; Micah 7:18–19; Daniel 9:9, 19; Sirach 28:2 *(Apocrypha)* | Sixth Benediction: "Forgive us, our Father, for we have sinned; pardon us, our King, for we have transgressed" |
| And lead us not into temptation | Genesis 22:1; Exodus 16:4; 17:7; Deuteronomy 6:16; 8:2; 13:3; 2 Chronicles 32:31; Job 1:12; 2:6; Psalm 19:13; 26:2; 95:8–9; 119:133; 139:23–24; 141:4; Isaiah 63:17 | Morning prayer (b. Berakhot 60b): "bring me not into the power of sin... nor into the power of temptation" |
| But deliver us from evil | 2 Samuel 22:2–3; Psalm 23:4; 34:19; 37:40; 91:1–3; 97:10; 121:7; 140:1 | — |
| For thine is the kingdom, and the power, and the glory, for ever. Amen | 1 Chronicles 29:10–13; 16:36; Psalm 41:13; 72:19; 89:52; 106:48; Nehemiah 8:6; Deuteronomy 27:26 | The closing *berakah* of every synagogue prayer; the Temple's response, "Blessed be the name of his glorious kingdom for ever and ever" |

---

## D. Six petitions or seven?

The prayer has been divided in three ways, and the division is only a matter of counting.

| Tradition | Petitions | How the last clause is counted |
| --- | --- | --- |
| Augustine (*On the Sermon on the Mount*, c. 394); Luther's Catechisms (1529); the Roman Catechism (1566); the Catechism of the Catholic Church (1992) | seven | "lead us not into temptation" and "deliver us from evil" counted separately |
| The Greek commentators (Gregory of Nyssa, Chrysostom); Calvin (*Institutes* III.xx.35); the Heidelberg Catechism (1563); the Westminster Catechisms (1647) | six | the two clauses counted as one, joined by "but" |
| Luke 11:2–4 in the oldest manuscripts | five | no will-petition and no deliverance clause |

Augustine found the sevenfold division congenial because he matched the seven petitions to the seven beatitudes and the seven gifts of the Spirit in Isaiah 11. Calvin objected that "lead us not into temptation, but deliver us from evil" is one thought expressed negatively and positively and should not be pulled apart. Both are reading the same Greek; ἀλλά, "but," binds the clauses but does not forbid counting them. Nothing in the prayer's meaning depends on the answer, and a reader of Luther's catechism and of Westminster's will find them saying the same things under different numbers.

---

## E. Textual notes

All variants that affect the wording of the prayer, with the editions in this repository that carry each reading. Manuscript sigla follow the standard critical apparatus.

**Matthew 6:12, ἀφήκαμεν / ἀφίεμεν.** "As we have forgiven" (aorist): א* B Z, the Vulgate, the Syriac. "As we forgive" (present, ἀφίεμεν or ἀφίομεν): D L W Θ, the Byzantine text, the *Didache*. The TR, Byzantine, and KJTR files read ἀφίεμεν; SBLGNT, Nestle, and SR read ἀφήκαμεν. Sense is unaffected; see Part I.

**Matthew 6:13, the doxology.** Absent: א B D Z 0170, family 1, most Old Latin, the Vulgate, the Bohairic Coptic, and the commentaries of Tertullian, Origen, and Cyprian. Present: L W Δ Θ 0233, family 13, the Byzantine majority, the Peshitta and Harclean Syriac, and — without "the kingdom" — the *Didache* (8:2). The Curetonian Syriac has a shorter form ("the kingdom and the glory"); a few late minuscules expand it with "of the Father, and of the Son, and of the Holy Spirit." The TR, Byzantine, and KJTR files have it; SBLGNT, Nestle, and SR do not. Its wording is from 1 Chronicles 29:11.

**Matthew 6:10 and Luke 11:2, ἐλθέτω / ἐλθάτω.** Two spellings of the same aorist imperative; Nestle prints the Hellenistic ending ἐλθάτω. No difference in sense.

**Luke 11:2, "Our Father which art in heaven."** The short "Father" (Πάτερ alone): P75 א B, family 1, the Vulgate, the Sinaitic Syriac, Origen. The Matthean expansion: A C D W Θ Ψ, family 13, the Byzantine majority. The KJV follows the expansion.

**Luke 11:2, "Thy will be done, as in heaven, so in earth."** Absent: P75 B L, family 1, the Vulgate, the Sinaitic Syriac. Present: א A C D W Θ Ψ, family 13, the Byzantine majority. The KJV follows the longer reading. The Byzantine and TR order, "as in heaven, so in earth," differs slightly from Matthew's, which the KJV preserves in its translation.

**Luke 11:2, "Thy Holy Spirit come upon us and cleanse us."** In place of "thy kingdom come": minuscules 700 and 162, Gregory of Nyssa, Maximus the Confessor; Marcion (second century) may have had a form of it. A liturgical adaptation, not the original text.

**Luke 11:4, "but deliver us from evil."** Absent: P75 א* B L, family 1, the Vulgate, the Sinaitic Syriac, Origen. Present: א² A C D W Θ Ψ, family 13, the Byzantine majority. The KJV follows the longer reading.

**Luke 11:4, ἀφίεμεν / ἀφίομεν.** Two spellings of the same present indicative. No difference in sense.

**Not varied.** Ἐπιούσιος stands in every manuscript of both Gospels; whatever the word means, it is what the evangelists wrote. Τοῦ πονηροῦ is likewise unvaried; the "evil / evil one" question is one of interpretation, not of text. The *Didache*'s τὴν ὀφειλὴν ἡμῶν, "our debt" (singular), is a variation in that document, not in any manuscript of Matthew.

---

## F. Honest caveats

**The Jewish parallels are not dated.** The Kaddish is attested in its present form only in the early Middle Ages, though its opening sentences are widely thought to be much older; the Eighteen Benedictions were given fixed wording after AD 70; the morning prayer quoted from the Talmud was written down centuries after Jesus. That the Lord's Prayer resembles these prayers is certain; that Jesus' hearers knew them in these words is likely for the Kaddish and the Benedictions and unproven for the rest. The parallels show the prayer's world, not its sources.

**The two settings.** This document reads Matthew and Luke as recording two occasions. Readers who hold that both evangelists drew on a common written source will read them as two forms of one, and nothing in Part II depends on the choice.

**Ἐπιούσιος is undecidable.** Four derivations are set out and one is preferred; none can be proved, because the word exists nowhere else. The preferred sense ("needful, for the day") is the majority view and the traditional English rendering, and no more.

**Τοῦ πονηροῦ is undecidable by grammar.** The case for "the evil one" is made from usage and is, in this document's judgment, the stronger; it is not certain, and "evil" is not wrong.

**"Lead us not" is translated as it stands.** The permissive reading ("do not let us be brought into") is an interpretation of the Aramaic behind the Greek, with early and respectable support; the Greek says "bring." Both readings are set out. Readers who follow the 1988 ecumenical text or the recent French and Italian translations are not mistranslating; they are choosing an interpretation, and so is everyone who keeps the traditional words.

**The doxology.** The judgment that it is not part of Matthew's original text is the settled view of textual scholarship and is followed here; readers who hold the Byzantine text to be original will disagree, and the evidence for both positions is given in Part I and Appendix E.

**The counts are of English words.** Where a number of occurrences is given from `kjv/kjv.txt`, it counts the KJV's words (for instance, "Father" capitalised), not the Greek; Greek counts are taken from the word tables and marked as such. The commands are given so any count can be rerun.

**The historical sketch is a sketch.** Twenty centuries in two pages leave out nearly everything, including the whole of the Eastern tradition after Chrysostom, the medieval commentaries, and the Puritan and Methodist expositions. Patristic and confessional works are quoted from standard English editions and, where a phrase is famous, in its familiar English form; page and section references are given so they can be checked, and a reader who finds a quotation misremembered should trust the source.

**The Old and Middle English samples** are given in normalised spelling. The manuscripts and early printings differ from one another and from what is printed here in small ways.

**Sirach 28:2** is from the Apocrypha, is not in this repository's text, and could not be checked against it.

---

## G. Further reading

**Primary — read these first, in this order:**

1. **Matthew 6:1–34** — the prayer with everything Matthew set around it: secrecy, brevity, the forgiveness warning, and the teaching on bread and anxiety
2. **Luke 11:1–13** — the prayer with Luke's frame: the request, the friend at midnight, ask-seek-knock, the Father who gives the Spirit
3. **Matthew 18:21–35** — the fifth petition as a parable
4. **Matthew 26:36–46** with **Mark 14:32–42** — the first word, the third petition, and the sixth, in Gethsemane
5. **Exodus 16** with **Deuteronomy 8:1–5** — the fourth petition's origin
6. **Ezekiel 36:16–38** — the first petition's origin
7. **1 Chronicles 29:10–19** — the doxology's origin
8. **Psalm 103** — the whole prayer, in the Psalter's words
9. **James 1:2–15** with **1 Corinthians 10:13** — the sixth petition's grammar
10. **Romans 8:12–17** — why anyone may say the first word

**Related material in this repository:**

- [`kjv/`](kjv) — the full King James text, greppable by reference
- [`original-languages/`](original-languages) — the Greek editions, interlinear, and lexicons used throughout
- [`fasting-in-the-bible.md`](fasting-in-the-bible.md) — Matthew 6:16–18, the third member of the triad in which the prayer sits
- [`confession-in-the-bible.md`](confession-in-the-bible.md) — what the fifth petition implies about confessing sin, and to whom
- [`once-saved-always-saved.md`](once-saved-always-saved.md) — Matthew 6:14–15 and 18:35 among the warning passages
- [`progressive-sainthood.md`](progressive-sainthood.md) — ἁγιάζω, the verb of the first petition, and what it means to be made holy
- [`praying-for-the-dead.md`](praying-for-the-dead.md) — on prayer more generally, and its limits
- [`ot-allusions-to-christ.md`](ot-allusions-to-christ.md) — the kingdom and the bread of life in their Old Testament roots

**Beyond Scripture,** the shortest and best are old. The *Didache*, chapter 8, is one paragraph and shows the prayer in use a generation after the apostles. Tertullian's *On Prayer* (chapters 1–9), Cyprian's *On the Lord's Prayer*, and Origen's *On Prayer* (chapters 18–30) are the three earliest commentaries and are all freely available in English. Augustine's Letter 130, to Proba, is the classic statement that the prayer contains all prayer. Gregory of Nyssa's five homilies and Chrysostom's nineteenth homily on Matthew give the Greek reading. Luther's *Small Catechism* on the prayer can be read in ten minutes and his *A Simple Way to Pray* in thirty; Calvin's treatment is *Institutes* III.xx.34–49; the Heidelberg Catechism's is Lord's Days 45–52 and the Westminster Shorter Catechism's is Questions 98–107; the Catechism of the Catholic Church's is paragraphs 2759–2865. The ecumenical text and its rationale are in the English Language Liturgical Consultation's *Praying Together* (1988).

---

*Scripture quoted from the King James Version (1769), public domain in the United States, as carried in [`kjv/kjv.txt`](kjv/kjv.txt) in this repository; every quotation was taken directly from that file. Greek and Hebrew words, parsing, and Strong's numbers are from [`original-languages/`](original-languages), and every count and form stated was produced from those files by the commands shown. The Didache, the Fathers, the Reformers, and the catechisms are quoted in standard English editions and are named where used; see [Appendix F](#f-honest-caveats).*
