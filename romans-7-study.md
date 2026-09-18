# Romans 7
## The Law, the Flesh, and the Divided "I"

---

## How to Use This Document

Romans 7 is the most argued-over chapter in the most argued-over letter in the
New Testament. The argument is not about a detail. It is about who is speaking
in verses 14–25 — the man who cannot do the good he wants and does the evil he
hates. If that man is a Christian, the chapter is a description of normal
Christian life and a comfort. If he is not, the chapter is a description of
life without Christ and a warning. Nearly everything people take from Romans 7
depends on which of those they assume before they start reading.

This document works in four parts:

1. **Part I — Getting the chapter in view.** Where Romans 7 sits in Paul's
   argument, the shape of the chapter, and the handful of words that carry it.
   Read this first; most misreadings of Romans 7 are really misreadings of
   Romans 5–8.
2. **Part II — The exposition.** Verse by verse through all twenty-five verses,
   with the Greek where the Greek decides something and the KJV's 1611 English
   translated into 2026 English where it has drifted.
3. **Part III — Who is the "I"?** The question laid out properly: the evidence
   that is actually on the page, the four readings that have been given, who
   held them and why, and an honest weighing. This is the longest part because
   it is the part people come for.
4. **Part IV — Living with Romans 7.** What the chapter will and will not bear
   pastorally, the two opposite errors it gets used to license, and how to pray
   it.

**If you are here because Romans 7 describes you** — because you recognise
yourself in *"what I would, that do I not; but what I hate, that do I"* — go to
Part IV first. It does not require you to settle the argument in Part III, and
the argument, as Part III concludes, turns out to change less about how you
should live than the heat of it suggests.

### The source of the quotations

Scripture is quoted from the **King James Version (1769)**, the text carried in
[`kjv/`](kjv) in this repository. Every quotation was taken directly from that
file, so any verse can be checked at its source:

```sh
grep '^Romans 7:24 ' kjv/kjv.txt
```

Greek is quoted from [`original-languages/greek/`](original-languages/greek).
Where the wording of the Greek matters, two editions are given: **Scrivener's
1894 Textus Receptus** ([`tr-scrivener.txt`](original-languages/greek/tr-scrivener.txt)),
which is the text the KJV translators worked from, and the **SBLGNT**
([`sblgnt.txt`](original-languages/greek/sblgnt.txt)), which is close to what
most modern translations follow. The Scrivener text in this repository is
unaccented; accented forms in this document are taken from the accented
editions of the same tradition, and the differences between the six editions
are set out in [Appendix B](#appendix-b--the-textual-variants).

```sh
grep '^Romans 7:14 ' original-languages/greek/tr-scrivener.txt
grep '^Romans 7:14 ' original-languages/greek/sblgnt.txt
```

Word counts, parsings and Strong's numbers come from the word tables and
lexicons in the same directory, and the commands that produce them are given in
[Appendix D](#appendix-d--the-verb-data) so every number here can be checked.

### Where the KJV's English has drifted

The KJV is quoted throughout because it is the text this repository carries,
but five of its words in this chapter now mean something different from what
they meant in 1611, and four of the five are load-bearing. They are flagged
again where they occur:

| KJV, Romans 7 | 1611 sense | Greek |
| --- | --- | --- |
| *motions* (v. 5) | impulses, promptings | παθήματα, *passions* |
| *concupiscence* (v. 8) | strong desire, craving | ἐπιθυμία — the same word as *lust* in v. 7 |
| *allow* (v. 15) | approve, sanction | γινώσκω, *know, understand* |
| *carnal* (v. 14) | belonging to the flesh | σαρκικός / σάρκινος — see Appendix B |
| *God forbid* (vv. 7, 13) | an emphatic refusal; God is not named | μὴ γένοιτο, *may it never be!* |

*Allow* in verse 15 is the one that most often derails a first reading. The KJV's
*"that which I do I allow not"* sounds like a man permitting or forbidding
himself things. Paul wrote *"what I bring about, I do not understand"* — the
complaint is bewilderment, not permission.

---

## Contents

**[Part I — Getting the Chapter in View](#part-i--getting-the-chapter-in-view)**

- [Where Romans 7 sits](#where-romans-7-sits)
- [The problem Paul has made for himself](#the-problem-paul-has-made-for-himself)
- [The shape of the chapter](#the-shape-of-the-chapter)
- [Five words that carry the chapter](#five-words-that-carry-the-chapter)
- [The chapter in full](#the-chapter-in-full)

**[Part II — The Exposition](#part-ii--the-exposition)**

- [7:1–6 — Death dissolves the bond](#71-6--death-dissolves-the-bond)
- [7:7–12 — Is the law sin?](#77-12--is-the-law-sin)
- [7:13 — The hinge](#713--the-hinge)
- [7:14–17 — Sold under sin](#714-17--sold-under-sin)
- [7:18–20 — Nothing good dwells in me](#718-20--nothing-good-dwells-in-me)
- [7:21–23 — Four laws and a war](#721-23--four-laws-and-a-war)
- [7:24 — The cry](#724--the-cry)
- [7:25 — The answer, and the sentence that will not lie down](#725--the-answer-and-the-sentence-that-will-not-lie-down)

**[Part III — Who Is the "I"?](#part-iii--who-is-the-i)**

- [Why the question cannot be dodged](#why-the-question-cannot-be-dodged)
- [The evidence on the page](#the-evidence-on-the-page)
- [Reading 1: Paul's autobiography](#reading-1-pauls-autobiography)
- [Reading 2: The unbeliever](#reading-2-the-unbeliever)
- [Reading 3: The Christian](#reading-3-the-christian)
- [Reading 4: Adam, Israel, and speech-in-character](#reading-4-adam-israel-and-speech-in-character)
- [How the church argued it](#how-the-church-argued-it)
- [Weighing it](#weighing-it)
- [What actually hangs on it](#what-actually-hangs-on-it)

**[Part IV — Living With Romans 7](#part-iv--living-with-romans-7)**

- [The two errors the chapter gets used to license](#the-two-errors-the-chapter-gets-used-to-license)
- [What the chapter does not say](#what-the-chapter-does-not-say)
- [What it does say to a struggling Christian](#what-it-does-say-to-a-struggling-christian)
- [Romans 7 and besetting sin](#romans-7-and-besetting-sin)
- [Praying Romans 7](#praying-romans-7)

**[Appendices](#appendices)**

- [Appendix A — The KJV and the Greek side by side](#appendix-a--the-kjv-and-the-greek-side-by-side)
- [Appendix B — The textual variants](#appendix-b--the-textual-variants)
- [Appendix C — Word tables](#appendix-c--word-tables)
- [Appendix D — The verb data](#appendix-d--the-verb-data)
- [Appendix E — Cross-reference index](#appendix-e--cross-reference-index)
- [Appendix F — Where the positions are argued](#appendix-f--where-the-positions-are-argued)
- [Appendix G — Questions for study and discussion](#appendix-g--questions-for-study-and-discussion)

---

# Part I — Getting the Chapter in View

## Where Romans 7 sits

Romans 1–4 argues that no one is put right with God by keeping the law: Jew and
Gentile alike are under sin, and righteousness comes by faith in Christ, as it
came to Abraham. Romans 5 turns from how a person is justified to what
justification secures — peace with God, and a standing in Adam's race reversed
by Christ's obedience. Romans 6 answers the objection that hangs over all of
this: *if grace abounds where sin abounds, why not sin?* Paul's answer is that
in baptism the believer died with Christ, and a dead person is not available for
the old service.

Then, at the end of Romans 6, Paul says something that sets up chapter 7:

> **Romans 6:14** — For sin shall not have dominion over you: for ye are not
> under the law, but under grace.

*Not under the law.* Paul has now said, or strongly implied, several things
about the law that sound damaging:

| Where | What Paul has said about the law |
| --- | --- |
| Romans 3:20 | *"by the law is the knowledge of sin"* — it diagnoses, it does not cure |
| Romans 4:15 | *"the law worketh wrath"* |
| Romans 5:20 | *"the law entered, that the offence might abound"* |
| Romans 6:14 | believers are *"not under the law"* |
| Romans 7:5 | sinful passions were *"by the law"* |

Stack those up and an obvious conclusion presents itself, and Paul knows it:
**the law is the problem.** Chapter 7 exists to deny that conclusion without
retracting anything that led to it. That is the whole job of the chapter, and
it is why the chapter is hard: Paul is defending the law while conceding almost
everything his opponent would want to say about its effects.

Then Romans 8 opens the release: *"There is therefore now no condemnation."*

Romans 7 is therefore not a detour. It is the low point of a deliberate descent
between two summits — Romans 6's *"dead to sin"* and Romans 8's *"no
condemnation"* — and any reading that leaves the reader stranded in it has
misread the structure.

## The problem Paul has made for himself

It helps to state the difficulty as a syllogism, because Paul's imagined
objector is not stupid:

1. The law came from God, and God is good.
2. But the law produces knowledge of sin, wrath, increased transgression, and
   death.
3. Therefore either God is not good, or the law is not from God, or —

Paul's answer is the third horn, and it takes the whole chapter to state:
**the law is good and the law kills, because what the law meets in us is not
neutral.** The law is a straight edge laid against a warped board. The warp is
in the board. What the straight edge does is make the warp measurable, and — this
is Paul's genuinely uncomfortable claim — *provoke it*. Sin uses the commandment
as a foothold.

Twice in the chapter Paul states the objection as a flat question and answers it
with μὴ γένοιτο, the strongest negation Greek has for a proposition someone has
just floated:

> **Romans 7:7** — *Is the law sin? God forbid.*
>
> **Romans 7:13** — *Was then that which is good made death unto me? God forbid.*

The KJV's *"God forbid"* is an idiom, not a translation; God is not named in the
Greek. μὴ γένοιτο is literally *"may it not come to be"* — closer to *"absolutely
not"* or *"perish the thought."* Paul uses it ten times in Romans, always to
kill a false inference his own argument has just made available
([Appendix E](#appendix-e--cross-reference-index) lists all ten).

## The shape of the chapter

Romans 7 divides cleanly, and the divisions are marked by the grammar, not just
by the sense.

| Verses | Subject | Person and tense | Spirit mentioned? |
| --- | --- | --- | --- |
| 1–6 | The marriage analogy: death ends the law's claim | "we," past and present | yes, v. 6 |
| 7–12 | Is the law sin? The commandment and the first offence | "I," **past** (aorist/imperfect) | no |
| 13 | The hinge question restated | "I," past | no |
| 14–25 | The divided self | "I," **present** | **no** |

Two of those columns do the heavy lifting in every argument about this chapter,
so they are worth establishing before anything is built on them.

**The tense changes at verse 14, and it changes completely.** In verses 7–13
Paul narrates: *I had not known* (ἔγνων, aorist), *sin wrought* (κατειργάσατο,
aorist), *I was alive* (ἔζων, imperfect), *sin revived* (ἀνέζησεν, aorist),
*I died* (ἀπέθανον, aorist), *sin deceived me* (ἐξηπάτησεν, aorist), *and slew
me* (ἀπέκτεινεν, aorist). From verse 14 to verse 25 every finite verb in the
first person is present: *I am* (εἰμι), *I do* (κατεργάζομαι, πράσσω, ποιῶ),
*I know not* (γινώσκω), *I would* (θέλω), *I hate* (μισῶ), *I consent*
(σύμφημι), *I find* (εὑρίσκω), *I delight* (συνήδομαι), *I see* (βλέπω),
*I thank* (εὐχαριστῶ), *I serve* (δουλεύω). The only exceptions are the two
perfects that function as presents (οἶδα, *I know*; πέπραμενος, *having been
sold* — a state) and the one future, ῥύσεται, *shall deliver*, in the cry of
verse 24. The full table is in [Appendix D](#appendix-d--the-verb-data).

Something changes at verse 14. Paul stops telling a story and starts describing
a condition.

**The Spirit is absent from the disputed section, and that absence is total.**
The word πνεῦμα occurs **once** in Romans 7 — in verse 6, before the "I" section
begins, in the phrase *"newness of spirit."* It does not occur again in the
chapter. In Romans 8 it occurs **twenty-two times**. There is no reference to the
Holy Spirit anywhere in Romans 7:7–25.

```sh
awk -F'\t' '$1 ~ /^Romans 7:/ && $4=="G4151"' \
  original-languages/greek/tr-scrivener-words.tsv
```

Whatever the man of Romans 7:14–25 has, he does not have the Spirit named as his
resource. He fights with his νοῦς, his *mind* — and he loses.

## Five words that carry the chapter

### 1. νόμος — *law*

Twenty-three occurrences in twenty-five verses. That is the densest
concentration of νόμος anywhere in the New Testament: more than Romans 2 (19),
which is nearly a third longer, and almost a third of all seventy-five uses in
the letter.

| Romans | νόμος | | Romans | νόμος |
| ---: | ---: | --- | ---: | ---: |
| 2 | 19 | | 7 | **23** |
| 3 | 11 | | 8 | 5 |
| 4 | 5 | | 9 | 3 |
| 5 | 3 | | 10 | 2 |
| 6 | 2 | | 13 | 2 |

The difficulty is that Paul does not use the word in one sense. In verses 1–12
and 22 it is plainly the Mosaic law, the Torah — the thing that said *Thou shalt
not covet*. But in verse 21 (*"I find then a law"*), verse 23 (*"another law in
my members... the law of my mind... the law of sin"*), and in Romans 8:2 (*"the
law of the Spirit of life"* against *"the law of sin and death"*), Paul is using
νόμος in a second sense: a governing principle, a regime, something that holds
and operates. English keeps them apart with *law* and *principle*; Greek did not
have to, and Paul is plainly enjoying the overlap. Sorting out which sense is in
play in each of the twenty-three is most of the work of reading verses 21–25, and
[the exposition](#721-23--four-laws-and-a-war) does it verse by verse.

### 2. ἁμαρτία — *sin*

Fifteen occurrences. What is striking is not the number but the **grammar**: in
Romans 7 sin is, over and over, the *subject of active verbs*. Sin takes
occasion (v. 8, v. 11), works (v. 8), revives (v. 9), deceives (v. 11), slays
(v. 11), works death (v. 13), dwells (vv. 17, 20). Paul is not describing sins —
acts, in the plural, that a person commits. He is describing *Sin*, singular,
as an occupying power with its own agency and address. The man in this chapter
is not primarily a wrongdoer; he is a **captured territory**.

This is continuous with Romans 5:12–21 and 6:12–23, where sin *reigns*, *has
dominion*, and holds *slaves*. Romans 7 is what that dominion feels like from
the inside.

### 3. σάρξ — *flesh*

Three occurrences in Romans 7 (vv. 5, 18, 25), fourteen in Romans 8. In Paul,
σάρξ is not the body and it is not physicality; it is not a claim that matter is
bad. It is human nature considered as weak, mortal, and turned in on itself —
humanity as it is apart from God's Spirit. Verse 18 gives Paul's own gloss:
*"in me (that is, in my flesh,)"*. The parenthesis is a restriction, and it is
doing careful work: Paul does not say nothing good dwells in *him*. He says
nothing good dwells in his **flesh**, which implies there is something in him
that is not flesh.

### 4. ἐπιθυμία — *desire, craving*

The word at the centre of verses 7–8. The KJV renders it three different ways in
two verses — *lust* (v. 7), the verb *covet* (v. 7, ἐπιθυμήσεις), and
*concupiscence* (v. 8) — which conceals from an English reader that it is one
word hammered four times. It is not a sexual term in itself; it is desire aimed
at what is not yours. Paul chose the tenth commandment for a reason: it is the
one commandment in the Decalogue that no external observance can satisfy and no
observer can audit. A man can be *"touching the righteousness which is in the
law, blameless"* (Philippians 3:6) on the other nine. The tenth goes inside.

### 5. ἐγώ — *I*

The pronoun ἐγώ appears in the nominative eight times in Romans 7 (vv. 9 twice,
14, 17, 20 twice, 24, 25), plus twenty-one other first-person pronoun forms. In
Greek the nominative pronoun is normally unnecessary — the verb ending already
carries the person — so writing it is **emphatic**. Paul is not merely using
first-person verbs; he is repeatedly, deliberately putting the pronoun in.
*I* was alive. *I* am carnal. It is no longer *I*. Wretched man *I* am. *I
myself* serve.

Who that emphatic *I* is, is [Part III](#part-iii--who-is-the-i).

## The chapter in full

Read straight through before the exposition breaks it up. The section headings
are added; the KJV's own verse numbers are as in [`kjv/kjv.txt`](kjv/kjv.txt).

> ### The marriage analogy (1–6)
>
> **1** Know ye not, brethren, (for I speak to them that know the law,) how that
> the law hath dominion over a man as long as he liveth? **2** For the woman
> which hath an husband is bound by the law to her husband so long as he liveth;
> but if the husband be dead, she is loosed from the law of her husband. **3** So
> then if, while her husband liveth, she be married to another man, she shall be
> called an adulteress: but if her husband be dead, she is free from that law; so
> that she is no adulteress, though she be married to another man. **4**
> Wherefore, my brethren, ye also are become dead to the law by the body of
> Christ; that ye should be married to another, even to him who is raised from
> the dead, that we should bring forth fruit unto God. **5** For when we were in
> the flesh, the motions of sins, which were by the law, did work in our members
> to bring forth fruit unto death. **6** But now we are delivered from the law,
> that being dead wherein we were held; that we should serve in newness of
> spirit, and not in the oldness of the letter.
>
> ### Is the law sin? (7–12)
>
> **7** What shall we say then? Is the law sin? God forbid. Nay, I had not known
> sin, but by the law: for I had not known lust, except the law had said, Thou
> shalt not covet. **8** But sin, taking occasion by the commandment, wrought in
> me all manner of concupiscence. For without the law sin was dead. **9** For I
> was alive without the law once: but when the commandment came, sin revived, and
> I died. **10** And the commandment, which was ordained to life, I found to be
> unto death. **11** For sin, taking occasion by the commandment, deceived me,
> and by it slew me. **12** Wherefore the law is holy, and the commandment holy,
> and just, and good.
>
> ### The hinge (13)
>
> **13** Was then that which is good made death unto me? God forbid. But sin,
> that it might appear sin, working death in me by that which is good; that sin
> by the commandment might become exceeding sinful.
>
> ### The divided self (14–23)
>
> **14** For we know that the law is spiritual: but I am carnal, sold under sin.
> **15** For that which I do I allow not: for what I would, that do I not; but
> what I hate, that do I. **16** If then I do that which I would not, I consent
> unto the law that it is good. **17** Now then it is no more I that do it, but
> sin that dwelleth in me. **18** For I know that in me (that is, in my flesh,)
> dwelleth no good thing: for to will is present with me; but how to perform that
> which is good I find not. **19** For the good that I would I do not: but the
> evil which I would not, that I do. **20** Now if I do that I would not, it is
> no more I that do it, but sin that dwelleth in me. **21** I find then a law,
> that, when I would do good, evil is present with me. **22** For I delight in
> the law of God after the inward man: **23** But I see another law in my members,
> warring against the law of my mind, and bringing me into captivity to the law
> of sin which is in my members.
>
> ### The cry and the answer (24–25)
>
> **24** O wretched man that I am! who shall deliver me from the body of this
> death? **25** I thank God through Jesus Christ our Lord. So then with the mind
> I myself serve the law of God; but with the flesh the law of sin.

---

# Part II — The Exposition

## 7:1-6 — Death dissolves the bond

> **Romans 7:1** — Know ye not, brethren, (for I speak to them that know the
> law,) how that the law hath dominion over a man as long as he liveth?

Paul opens with a principle so obvious he expects assent before he has finished
the sentence: **law binds the living.** A statute has no claim on a corpse. The
parenthesis — *"for I speak to them that know the law"* — tells us something
about the Roman congregation: it contained people, Jewish believers and Gentile
God-fearers, who knew the Torah well enough to follow a rabbinic-style argument
about it.

The verb *hath dominion* is κυριεύει, from κύριος, *lord*. It is the same verb
Paul used in Romans 6:14, *"sin shall not have dominion over you,"* and in
Romans 6:9 of death having no more dominion over the risen Christ. The chapter
opens by putting the law in the same grammatical position Paul has just put sin
and death: **a lord whose lordship has a term limit.**

> **Romans 7:2–3** — For the woman which hath an husband is bound by the law to
> her husband so long as he liveth; but if the husband be dead, she is loosed
> from the law of her husband. So then if, while her husband liveth, she be
> married to another man, she shall be called an adulteress: but if her husband
> be dead, she is free from that law; so that she is no adulteress, though she be
> married to another man.

The illustration. A married woman is bound while her husband lives; if he dies
she is free to remarry, and no one calls her an adulteress.

*Loosed* and *free from that law* in verses 2–3 translate κατήργηται — the same
verb (καταργέω) that will translate as *delivered* in verse 6. It is a strong
word: to render inoperative, to put out of action, to nullify. The KJV renders
καταργέω twenty-odd different ways across the New Testament (*abolish, cease,
destroy, do away, make void, bring to nought*), and it is worth noticing that
Paul has chosen a word of demolition for what happens to the law's claim.

**A caution about the analogy.** Readers regularly try to make the parts line up
and find they will not. If the husband is the law, then in verse 4 it should be
the law that dies — but Paul says *"ye also are become dead to the law."* The
wrong party dies. Commentators have proposed ingenious repairs; none is fully
convincing, and the honest conclusion is that Paul is not building an allegory
in which each element has a fixed referent. He is illustrating **one point**:
*death terminates the law's jurisdiction, and the survivor is free to belong to
someone else without disgrace.* That single point is what verse 4 applies.
Analogies in Paul are usually like this — a single axis of comparison, not a
key.

> **Romans 7:4** — Wherefore, my brethren, ye also are become dead to the law by
> the body of Christ; that ye should be married to another, even to him who is
> raised from the dead, that we should bring forth fruit unto God.

The application, and it is startling. *Ye also are become dead* is ἐθανατώθητε,
a passive — *"you were put to death."* Not *you died*; **you were killed.** The
same verb is used of executions.

*By the body of Christ* means by his crucified body — the same reality Romans
6:3–6 described as being baptised into his death and crucified with him. Paul's
logic runs: the law binds the living; in Christ's death you were put to death;
therefore the law's claim on you has lapsed, as a husband's claim lapses at a
funeral.

And the purpose is not freedom in the abstract. It is remarriage: *"that ye
should be married to another, even to him who is raised from the dead."* The
believer is not released into autonomy. The believer is released into a second
marriage, to the risen Christ. Freedom from the law is not freedom from
belonging — it is a **transfer of belonging**, which is precisely the argument
of Romans 6:16–22, where the only question is which master you serve.

*Bring forth fruit* (καρποφορήσωμεν) makes the marriage image do one more thing:
the new union is meant to be fertile. Compare Galatians 5:22, where the fruit is
the Spirit's.

> **Romans 7:5** — For when we were in the flesh, the motions of sins, which were
> by the law, did work in our members to bring forth fruit unto death.

*When we were.* Past tense, and Paul includes himself. There was a time; it is
over.

*The motions of sins* is τὰ παθήματα τῶν ἁμαρτιῶν, *the passions of sins* —
sinful passions. *Motions* in 1611 meant inward impulses or promptings, and the
modern sense of the word has drained the phrase of exactly what Paul meant by
it.

*Which were by the law* (τὰ διὰ τοῦ νόμου) is the scandalous half of the verse
and the reason chapter 7 has to be written: the sinful passions operated
**through the law**. And *did work* is ἐνηργεῖτο, from which English gets
*energy* — they were energised, activated, set in motion.

*In our members* (ἐν τοῖς μέλεσιν ἡμῶν) — the body parts, the concrete organs of
action. The phrase returns twice in verse 23, where the war is fought in the
same territory.

The verse ends with the dark mirror of verse 4: there, fruit *unto God*; here,
fruit *unto death*. Two marriages, two harvests.

> **Romans 7:6** — But now we are delivered from the law, that being dead wherein
> we were held; that we should serve in newness of spirit, and not in the oldness
> of the letter.

*But now* (νυνὶ δέ) — Paul's standard pivot from the old state to the new; the
same phrase opens Romans 3:21.

*We are delivered* is κατηργήθημεν, the demolition verb again, now in the aorist
passive: *we were rendered inoperative with respect to the law.*

**The KJV's distinctive rendering here rests on a textual variant, and it is the
only recorded variant in the chapter.** The Scrivener Textus Receptus reads
ἀποθανόντος, a genitive singular participle, which makes the *law* the thing
that died — hence the KJV's *"that being dead wherein we were held."* Every
other edition in this repository, including the Byzantine text of the same broad
tradition, reads ἀποθανόντες, nominative plural: *"we having died to that
wherein we were held."* The repository's own variant table records it:

```sh
grep '^Romans 7:6 ' original-languages/greek/tr-variants.tsv
```
```
Romans 7:6	αποθανοντες	αποθανοντος
```

The difference is real but small in effect: on either reading the bond is
dissolved by a death, and Paul has just spent five verses saying so. It is worth
knowing because it explains why the KJV reads differently from every modern
translation at this point, and because it is a clean, checkable example of how a
single letter changes a clause. See [Appendix B](#appendix-b--the-textual-variants).

*That we should serve* — δουλεύειν, *to serve as slaves*. Again: not released
from service, transferred to a new one.

*Newness of spirit... oldness of the letter* (καινότητι πνεύματος... παλαιότητι
γράμματος). The same contrast as 2 Corinthians 3:6, *"the letter killeth, but
the spirit giveth life."* This is the **one mention of πνεῦμα in Romans 7**, and
it is worth marking where it falls: at the end of the section Paul is closing,
before the "I" opens its mouth. After verse 6 the Spirit does not appear again
until Romans 8:2.

### What verses 1–6 have established

1. The law's authority is real, and it is bounded by death.
2. The believer has died — in Christ's death, not their own.
3. Therefore the law's claim has lapsed, and the believer belongs to the risen
   Christ instead.
4. The old life bore fruit unto death, and the law was somehow implicated in
   that.

Point 4 is the loose thread. Paul pulls it in verse 7.

## 7:7-12 — Is the law sin?

> **Romans 7:7** — What shall we say then? Is the law sin? God forbid. Nay, I had
> not known sin, but by the law: for I had not known lust, except the law had
> said, Thou shalt not covet.

*What shall we say then?* (Τί οὖν ἐροῦμεν) is Paul's flag for an objection he is
about to voice on his opponent's behalf — he uses it at Romans 4:1, 6:1, 8:31,
9:14 and 9:30.

*Is the law sin?* Given verse 5, the question is fair. Paul's answer, μὴ γένοιτο,
is absolute. Then the rest of the verse concedes as much as can be conceded
without granting the point: the law did not *make* him sin, it **made him know**
sin.

And here, at verse 7, the first person singular arrives and does not leave. Up
to this point the chapter has said *we*. From here to verse 25 it says *I*.

The two verbs of knowing are worth separating: *I had not known sin* is ἔγνων
(ginōskō, aorist — to come to know, to recognise), *I had not known lust* is
ᾔδειν (oida, pluperfect — to be aware of, to have in view). The law brought the
recognition; it also brought the awareness of a particular thing.

*Thou shalt not covet* — οὐκ ἐπιθυμήσεις — is the tenth commandment, Exodus
20:17 and Deuteronomy 5:21:

> **Exodus 20:17** — Thou shalt not covet thy neighbour's house, thou shalt not
> covet thy neighbour's wife, nor his manservant, nor his maidservant, nor his
> ox, nor his ass, nor any thing that is thy neighbour's.

Note what Paul quotes: the bare prohibition, without a single one of the
objects. Not *do not covet your neighbour's house* — just **do not covet**. He
has stripped the commandment to the verb, which is to say to the interior act.

Why the tenth, of all ten? Because it is the one that cannot be kept externally
and cannot be audited by anyone. Murder, theft, adultery and false witness all
have visible forms; a man can avoid the act and be publicly blameless. Coveting
happens where no one can see, including — until the commandment names it — the
man himself. Paul, who could say he was *"touching the righteousness which is in
the law, blameless"* (Philippians 3:6), chose the one commandment that
blamelessness of that kind cannot reach.

> **Romans 7:8** — But sin, taking occasion by the commandment, wrought in me all
> manner of concupiscence. For without the law sin was dead.

*Taking occasion* is ἀφορμὴν λαβοῦσα, and ἀφορμή is a vivid word. Strong's gives
*"a starting-point... an opportunity"*; in classical and military usage it is a
**base of operations** — the place an expedition launches from. Sin is being
described as a force that was waiting for somewhere to attack from, and the
commandment handed it one.

*Wrought* is κατειργάσατο (katergazomai), *worked out, brought about,
accomplished fully*. This verb is the spine of the second half of the chapter: it
returns in verses 13, 15, 17, 18 and 20, where it is what the man does and what
sin does through him.

*All manner of concupiscence* — πᾶσαν ἐπιθυμίαν, *every kind of craving*. The
same noun as *lust* in verse 7. The prohibition of desire produced desire of
every kind.

This is the observation that makes Romans 7 ring true to almost everyone who
reads it, whatever their theology. A rule against a thing can make the thing
interesting. The forbidden acquires a gravity the merely available never had.
Paul's point is not psychological cleverness for its own sake — it is that the
reaction reveals what was already there. A command provokes rebellion only in
someone already disposed to rebel.

*For without the law sin was dead.* Not non-existent — Romans 5:13 has already
said *"until the law sin was in the world."* Dormant. Unprovoked, unexposed,
uncounted.

> **Romans 7:9** — For I was alive without the law once: but when the commandment
> came, sin revived, and I died.

The most autobiographical-sounding sentence in the chapter, and the one that
does the most work in every argument about it.

*I was alive without the law once* (ἐγὼ δὲ ἔζων χωρὶς νόμου ποτέ) — with the
emphatic ἐγώ. The imperfect ἔζων describes a continuing past state.

*When the commandment came* (ἐλθούσης δὲ τῆς ἐντολῆς) — a genitive absolute
marking a decisive moment.

*Sin revived* is ἀνέζησεν (ana-zaō, *to live again*), and *I died* is ἀπέθανον.
The exchange is exact and it is a swap: sin came to life, and the *I* went down.
There is only room for one living thing here.

But when was Paul — or anyone — *"alive without the law"*? The candidates are
where the readings of the chapter divide, and they are set out in
[Part III](#part-iii--who-is-the-i). Briefly: childhood before bar mitzvah; Adam
in Eden before the prohibition; Israel before Sinai; or a self-satisfied
pre-conversion religiousness that the law eventually shattered.

> **Romans 7:10–11** — And the commandment, which was ordained to life, I found
> to be unto death. For sin, taking occasion by the commandment, deceived me, and
> by it slew me.

*Ordained to life* — Leviticus 18:5 promised that the man who does these things
*"shall live in them."* The law's own advertised purpose was life. Paul does not
dispute the advertisement; he reports the outcome.

**Verse 11 is where Genesis 3 comes through the floor.** *Deceived* is
ἐξηπάτησεν, and this verb is uncommon — it occurs five times in the Textus
Receptus New Testament. One of the other four is this:

> **2 Corinthians 11:3** — But I fear, lest by any means, as the serpent beguiled
> Eve through his subtilty, so your minds should be corrupted from the simplicity
> that is in Christ.

*Beguiled* there is ἐξηπάτησεν — the identical form, aorist active third
singular. Paul uses of Sin in Romans 7:11 the exact word he uses of the serpent
in 2 Corinthians 11:3.

```sh
awk -F'\t' '$4=="G1818" {print $1"\t"$3}' \
  original-languages/greek/tr-scrivener-words.tsv
```

Line the pieces up and the Eden pattern is unmistakable: a commandment given; a
deceiver taking the commandment as its opening; the promise that life will
follow; death instead. *"Taking occasion by the commandment, deceived me, and by
it slew me"* is the serpent's method described in the abstract. Whoever the *I*
of Romans 7 is, **Adam's story is being told through him.** This matters enormously
for Part III, and it is the single strongest piece of evidence that the *I* is
not simply Paul recounting his own adolescence.

> **Romans 7:12** — Wherefore the law is holy, and the commandment holy, and
> just, and good.

The verdict, and the answer to verse 7. The law is acquitted — completely, and
in four words: ἅγιος, ἁγία, δικαία, ἀγαθή. **Holy, holy, just, good.** Nothing is
retracted. Paul has said that sin used the law as a base of operations and that
the commandment ordained to life proved to be unto death, and he concludes from
all of it that the law is *holy*.

Everything wrong in verses 7–11 has been laid at sin's door, and the grammar has
been doing that quietly all along. Go back and check who the subjects are: *sin*
takes occasion, *sin* works, *sin* revives, *sin* deceives, *sin* slays. The law
does nothing in the passage except *say* (v. 7) and *come* (v. 9). It is present
at the crime and it is not the criminal.

## 7:13 — The hinge

> **Romans 7:13** — Was then that which is good made death unto me? God forbid.
> But sin, that it might appear sin, working death in me by that which is good;
> that sin by the commandment might become exceeding sinful.

The second μὴ γένοιτο, and the second acquittal — but this one adds something
new. Paul has been arguing defensively, clearing the law of blame. Verse 13
turns and states a **purpose**: the whole grim mechanism was for something.

*That it might appear sin* — ἵνα φανῇ ἁμαρτία, *so that it might be shown up as
sin*, might be seen for what it is.

*Exceeding sinful* is καθ' ὑπερβολὴν ἁμαρτωλός. ὑπερβολή is the word English
took as *hyperbole* — excess, throwing beyond. *Sinful beyond measure.*

So the answer to *why did God give a law that sin could weaponise?* is: **to
make sin show itself.** Sin's nature is concealment; it thrives dormant and
unnamed. The law forces it into the open, provokes it into acting, and makes it
visible as what it is. The commandment is a reagent. It does not create the
poison; it makes the poison change colour.

This is why the law can be holy, just and good *and* be the occasion of death.
A diagnosis that kills the patient's illusions is not a bad diagnosis.

**Verse 13 is the hinge of the chapter** for a second reason. Everything before
it is in the past tense; everything after it is in the present. Paul has finished
the narrative of how sin used the commandment. Now he turns to the condition
that narrative produced.

## 7:14-17 — Sold under sin

> **Romans 7:14** — For we know that the law is spiritual: but I am carnal, sold
> under sin.

*The law is spiritual* — πνευματικός, belonging to the Spirit, of divine origin.
One more commendation of the law on top of verse 12's four.

*But I am carnal.* The contrast is total and it is the turn of the chapter. And
the tense has changed: **εἰμι, present.** Not *I was*. *I am.*

*Carnal* here is where the manuscripts divide, and the division is clean. The
Textus Receptus, the Byzantine text and the CNTR KJTR read **σαρκικός** —
*fleshly in character, belonging to the flesh*. The SBLGNT, Nestle 1904 and the
CNTR SR read **σάρκινος** — *made of flesh, fleshy*, the material adjective.

```sh
for f in tr-scrivener sblgnt; do
  grep '^Romans 7:14 ' original-languages/greek/$f.txt
done
```

The two words differ by two letters and the sense they carry pulls in different
directions. σαρκικός is a moral characterisation: *I am a fleshly sort of
person.* σάρκινος is closer to a statement of constitution: *I am made of
flesh* — creaturely, weak, of the same stuff that dies. The critical reading is
in this sense the milder one, and a number of readers have thought it tells
against the harshest interpretations of the verse. The KJV's *carnal* follows
σαρκικός. Full details in [Appendix B](#appendix-b--the-textual-variants).

*Sold under sin* — πεπραμένος ὑπὸ τὴν ἁμαρτίαν. πεπραμένος is a perfect passive
participle: *having been sold, and remaining in that condition.* The verb is the
ordinary one for selling a slave.

The phrase has a hard Old Testament ring:

> **1 Kings 21:20** — ...because thou hast sold thyself to work evil in the sight
> of the LORD.
>
> **2 Kings 17:17** — ...and sold themselves to do evil in the sight of the LORD,
> to provoke him to anger.

But notice the difference, and it is the difference the whole chapter turns on.
Ahab and Israel **sold themselves** — the verb is active and reflexive. Paul's
participle is **passive**. He was sold. The chapter's man is not a volunteer.

This is the verse that makes the Christian reading hardest, and everyone who
holds that reading has to account for it, because Paul has just written in the
previous chapter:

> **Romans 6:17–18** — But God be thanked, that ye were the servants of sin, but
> ye have obeyed from the heart that form of doctrine which was delivered you.
> Being then made free from sin, ye became the servants of righteousness.

*Made free from sin* (6:18), *sold under sin* (7:14). The two statements sit
about twenty verses apart. [Part III](#part-iii--who-is-the-i) takes up how each
reading handles that.

> **Romans 7:15** — For that which I do I allow not: for what I would, that do I
> not; but what I hate, that do I.

The first statement of the famous impasse, and the KJV's *allow* actively
misleads a modern reader. The Greek is οὐ γινώσκω — *I do not know*, *I do not
understand*, *I do not recognise*. **The complaint is incomprehension, not
permission.** *"What I bring about, I do not understand."* The man is a stranger
to his own conduct; he watches himself act and does not recognise the actor.

Three verbs of doing appear in the verse and Paul distributes them carefully:
κατεργάζομαι (*bring about, accomplish* — the verb from v. 8), πράσσω
(*practise*), ποιῶ (*do, make*). Commentators have tried to build distinctions
between them; more probably Paul is varying his vocabulary for emphasis, as he
does with the four words for the law's goodness in verse 12. The force is
cumulative, not analytic.

*What I would, that do I not* — θέλω is the verb of willing, wanting, intending.
The man's **will is on the right side.** That is the whole pathos of the passage
and it is why it cannot simply be a description of a hardened rebel. A person
indifferent to the good does not experience this. Only someone who wants the
good and cannot reach it does.

*But what I hate, that do I.* μισῶ — *I hate*. Not *what I am tempted by* or
*what I enjoy against my better judgement*. He hates it. And does it.

> **Romans 7:16** — If then I do that which I would not, I consent unto the law
> that it is good.

A small logical step with a large payoff for Paul's argument. If I do what I do
not want to do, then my wanting is aligned with the law that forbids it.
*I consent* is σύμφημι — literally *I speak together with*, I agree with, I say
the same thing. My very failure is testimony for the prosecution's opponent: it
proves I think the law is right.

The chapter's defence of the law has not stopped. It is now being conducted from
inside the experience of failure.

> **Romans 7:17** — Now then it is no more I that do it, but sin that dwelleth in
> me.

The most easily abused verse in the chapter.

*It is no more I* — οὐκέτι ἐγὼ κατεργάζομαι αὐτό, with the emphatic pronoun. *No
longer do I bring it about.*

*Sin that dwelleth in me* — ἡ οἰκοῦσα ἐν ἐμοὶ ἁμαρτία. οἰκέω is the verb for
*living in a house*; the noun οἶκος is a house. Sin has taken up **residence**.
It is not a visitor. It has an address.

Read carelessly, verse 17 is an excuse: *it wasn't me, it was the sin living in
me.* That reading is impossible, for three reasons that the text itself
supplies:

1. Paul has just said in verse 16 that he *does* the thing — the doing is not in
   question, only what the doing proves.
2. He says the identical thing again in verse 20 and then, in verse 24, cries
   *"O wretched man that I am!"* Nobody who has successfully shifted the blame
   ends up there.
3. Verse 25 concludes *"I myself"* (αὐτὸς ἐγώ) serve two laws. The *I* is still
   holding the bag.

What verse 17 is actually doing is **distinguishing the self from what occupies
the self**. Paul is not saying *I am innocent*; he is saying *the thing producing
this is not the real me, the me that wills the good in verse 15 and delights in
God's law in verse 22 — it is the squatter.* That is a statement about
identity, and identity is the disputed ground of the whole chapter. It is also
the reason the chapter is either a great comfort or a great danger, depending on
whether the reader takes it as a diagnosis or an alibi.

## 7:18-20 — Nothing good dwells in me

> **Romans 7:18** — For I know that in me (that is, in my flesh,) dwelleth no
> good thing: for to will is present with me; but how to perform that which is
> good I find not.

**The parenthesis is the most important punctuation in the chapter.** *"In me
(that is, in my flesh,)"* — τοῦτ' ἔστιν ἐν τῇ σαρκί μου. Paul begins to say
*nothing good dwells in me*, stops, and narrows it. Not *in me*. In my **flesh**.

He would not need the correction if *me* and *my flesh* were the same thing. The
parenthesis implies a remainder — something in the *I* that is not σάρξ, and
which verse 22 will call the *inward man* and verse 23 the *mind*. This is the
verse most often quoted as total depravity in a sentence, and it is very nearly
that; but the clause Paul actually wrote is more careful than the one usually
quoted, and the care is deliberate.

*To will is present with me* — τὸ θέλειν παράκειταί μοι. παράκειμαι means *to lie
beside, to be at hand, ready to hand*. The willing is right there, within reach.

*But how to perform that which is good I find not.* The KJV's *I find not*
(οὐχ εὑρίσκω) is in the Textus Receptus; the critical editions end the sentence
with a bare negative, *"but to do the good, no."* Either way: the willing is at
hand, the performing is not. The gap between them is the subject of the whole
passage.

> **Romans 7:19** — For the good that I would I do not: but the evil which I
> would not, that I do.

Verse 15 restated, tighter, with the moral terms named: ἀγαθόν and κακόν, good
and evil. The repetition is not padding; it is the rhythm of the passage. Paul
states the impasse (15), draws the inference (16), locates the cause (17),
grounds it (18), states the impasse again (19), and draws the inference again
(20). It circles because the experience circles.

> **Romans 7:20** — Now if I do that I would not, it is no more I that do it, but
> sin that dwelleth in me.

Verse 17 repeated almost word for word — with one addition. The Greek of verse
20 adds the emphatic ἐγώ that verse 17 lacks in the protasis: *"if what I do not
will, this **I** do."* Two nominative ἐγώ forms in one verse, on both sides of
the distinction. Paul is pressing hard on the pronoun precisely where he is
pulling the self apart.

## 7:21-23 — Four laws and a war

> **Romans 7:21** — I find then a law, that, when I would do good, evil is
> present with me.

*A law* — νόμον, but here almost certainly in the second sense: a **principle**,
a regularity, something he keeps finding to be the case. *"I find, then, this
rule: that when I want to do the good, the evil lies ready to hand."*

*Is present with me* is παράκειται — the same verb as verse 18, where *willing*
was what lay ready to hand. Now *evil* lies ready to hand too. Both are within
reach, and that is the situation.

> **Romans 7:22** — For I delight in the law of God after the inward man:

*I delight* is συνήδομαι — *I rejoice together with, I take pleasure in
along with*. It occurs nowhere else in the New Testament. Whatever else is true
of this man, **he loves God's law and takes pleasure in it.**

This is the verse that makes the unbeliever reading hardest, just as verse 14
makes the Christian reading hardest. It stands very close to the Psalms:

> **Psalms 1:2** — But his delight is in the law of the LORD; and in his law doth
> he meditate day and night.
>
> **Psalms 119:97** — O how love I thy law! it is my meditation all the day.

And it stands in flat tension with Paul's own verdict one chapter later:

> **Romans 8:7** — Because the carnal mind is enmity against God: for it is not
> subject to the law of God, neither indeed can be.

Enmity against God's law, in 8:7. Delight in God's law, in 7:22. The same
author, a few sentences apart. Any reading of Romans 7 has to hold those two
together, and how each reading does it is the substance of
[Part III](#part-iii--who-is-the-i).

*After the inward man* — κατὰ τὸν ἔσω ἄνθρωπον. Paul uses *the inward man*
elsewhere of the believer's renewed interior life (2 Corinthians 4:16, Ephesians
3:16), which is a real argument for the Christian reading; against that, the
phrase was also current in Greek moral philosophy for the rational self as
against the appetites, and Paul may be using it in that more general sense here.

> **Romans 7:23** — But I see another law in my members, warring against the law
> of my mind, and bringing me into captivity to the law of sin which is in my
> members.

Three occurrences of νόμος in one verse, and they are not all the same law.
Counting verse 22's, the passage has **four**:

| | The law | What it is |
| --- | --- | --- |
| 1 | *the law of God* (v. 22) | the Torah, delighted in |
| 2 | *another law in my members* (v. 23) | the operative principle of sin in the body |
| 3 | *the law of my mind* (v. 23) | the governing principle of the renewed/rational self, aligned with 1 |
| 4 | *the law of sin* (v. 23) | the same as 2, now named |

*Another* is ἕτερον — *of a different kind*, not merely a second one of the same
sort.

*Warring against* is ἀντιστρατευόμενον, and it is a military compound: *to
campaign against, to take the field against*. This is not skirmishing. It is
organised war, and the *law of my mind* is the position being assaulted.

*Bringing me into captivity* is αἰχμαλωτίζοντα, from αἰχμάλωτος, a **prisoner of
war** — a captive taken at spear-point. The metaphor is consistent: an army
campaigns, the defence fails, and the defender is led away as a prisoner.

And the battlefield is named twice in one verse: *in my members*, ἐν τοῖς μέλεσίν
μου — the same phrase as verse 5. The war is not abstract. It is fought in the
hands and the eyes and the tongue.

Note where the man's resource is located: *the law of my **mind***, τοῦ νοός μου.
Not his spirit. Not the Spirit of God. **His mind** — and his mind is overrun.
Set that beside Galatians:

> **Galatians 5:17** — For the flesh lusteth against the Spirit, and the Spirit
> against the flesh: and these are contrary the one to the other: so that ye
> cannot do the things that ye would.

The conflict in Galatians is closely parallel — *"ye cannot do the things that
ye would"* is almost Romans 7:15 — and it is unambiguously addressed to
Spirit-indwelt Christians. But the combatants are different. In Galatians the
flesh fights **the Spirit**. In Romans 7 the flesh fights **the mind**, and wins.
That single difference is the most substantial argument in the whole debate, and
it is weighed in Part III.

## 7:24 — The cry

> **Romans 7:24** — O wretched man that I am! who shall deliver me from the body
> of this death?

The chapter breaks. Argument stops and a cry comes out.

*Wretched* is ταλαίπωρος — *miserable, afflicted, enduring hardship*. It occurs
only twice in the New Testament; the other is Revelation 3:17, of the Laodiceans
who think they are rich. The word sits first in the Greek sentence, which is
where Greek puts what it wants shouted: **ταλαίπωρος ἐγὼ ἄνθρωπος** — *wretched
man, I!* And there is the emphatic pronoun again.

*Who shall deliver me* — τίς με ῥύσεται. ῥύομαι is *to rescue, to snatch out of
danger*, the verb of pulling someone from a current or out of a fire. It is a
**future**: *who will rescue me?* In a passage of unbroken present tenses, the
one future verb is the plea for rescue. The grammar itself says that the man's
hope is not in his present condition.

And the question is *who*, not *what*. Not *how do I get out of this*. **A person
is needed.**

*The body of this death* — ἐκ τοῦ σώματος τοῦ θανάτου τούτου. The genitives can
be read two ways: *this body of death* (this dying body) or *the body belonging
to this death* (the body that this death has claimed). Either way the cry is for
release from an existence in which the body has been commandeered — the same
body whose *members* have been the battlefield since verse 5.

There is an old story, probably legend, that Etruscan pirates executed captives
by binding them face to face with a corpse and leaving them to die of it. Preachers
have used it on this verse for centuries. It may well be a fabrication, and it is
not needed: Paul's own phrase is vivid enough without borrowed horror. What
matters is the direction of the cry — outward, upward, to a rescuer.

## 7:25 — The answer, and the sentence that will not lie down

> **Romans 7:25** — I thank God through Jesus Christ our Lord. So then with the
> mind I myself serve the law of God; but with the flesh the law of sin.

**The first half is the answer to verse 24**, and it comes instantly — no
transition, no argument, just the name.

*I thank God* is εὐχαριστῶ τῷ θεῷ in the Textus Receptus and the Byzantine text,
which is what the KJV translates. The critical editions read χάρις τῷ θεῷ,
*"thanks be to God."* Both are thanksgiving; the TR reading is personal, the
critical reading is a formula. See [Appendix B](#appendix-b--the-textual-variants).

*Through Jesus Christ our Lord* — διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν. The
question of verse 24 was *who?* The answer is a name, and the rescue comes
*through* him.

**The second half is the problem.** After the thanksgiving, Paul does not move
on to Romans 8. He restates the division: *"So then with the mind I myself serve
the law of God; but with the flesh the law of sin."*

Why go back? The thanksgiving has been given; the answer has been named. And
then the very next clause returns the man to the two-fold service he was
lamenting.

The proposals are these:

1. **It is a summary, not a relapse.** ἄρα οὖν (*so then*) is Paul's regular
   marker for drawing a conclusion — he uses it at 7:3 and 7:21 in this chapter
   alone. On this view verse 25b sums up verses 14–24 before chapter 8 answers
   it, and the order is rhetorical rather than chronological. This is the
   majority view and the most natural reading of ἄρα οὖν.
2. **It is a displaced gloss.** Bultmann and others proposed that 25b was
   originally a marginal note that migrated into the text, or that it belongs
   before 25a. There is **no manuscript support for this** — all six editions in
   this repository carry the clause in the same place — and it is a conjecture
   made to relieve a difficulty rather than to explain evidence.
3. **It is the deliberate point.** On this reading the awkwardness is the
   message: deliverance is certain and named, and the tension is not yet
   abolished. The Christian is rescued and still waiting for the body's
   redemption — which is precisely what Paul says a few paragraphs later:

   > **Romans 8:23** — And not only they, but ourselves also, which have the
   > firstfruits of the Spirit, even we ourselves groan within ourselves, waiting
   > for the adoption, to wit, the redemption of our body.

   Believers who *have the firstfruits of the Spirit* still **groan**, and what
   they are waiting for is *the redemption of our body* — the same unfinished
   business as the *body of this death* in 7:24.

Readings 1 and 3 are compatible and together they account for the verse without
emending it. Reading 2 should be set aside: conjectural emendation against the
entire manuscript tradition, to remove a difficulty the author may have intended,
is a counsel of despair.

*I myself* is αὐτὸς ἐγώ — the strongest way Greek has of saying *I*, pronoun plus
intensifier. Whoever is speaking in this chapter, Paul ends it by insisting that
it is a self, undivided in responsibility even while divided in service.

### And then

> **Romans 8:1–2** — There is therefore now no condemnation to them which are in
> Christ Jesus, who walk not after the flesh, but after the Spirit. For the law
> of the Spirit of life in Christ Jesus hath made me free from the law of sin and
> death.

*Therefore* (ἄρα) ties it directly to what precedes. And notice what 8:2 does
with the vocabulary of 7:23: the **law of sin**, which took the man captive, is
answered by the **law of the Spirit of life**, which sets him free. Paul has kept
the terms and changed the outcome. The νόμος that was a captor is overmatched by
a νόμος that liberates, and the difference between them is the Spirit — the
person who has been missing from the chapter since verse 6.

Romans 7 does not end at Romans 7. It ends at Romans 8:2, and any reading that
stops at 7:25 has stopped one verse early.

---

# Part III — Who Is the "I"?

## Why the question cannot be dodged

Some readers, faced with the length of this argument, reasonably ask whether it
matters. It matters, and here is the test. Take a Christian who has struggled for
years with the same sin and comes to Romans 7. Two pastors quote the same
chapter:

- **Pastor A:** "This is Paul. This is the apostle, writing as a mature
  believer. What you are experiencing is normal Christian life. Do not despair
  of your salvation because you still lose."
- **Pastor B:** "This is Paul describing life *without* Christ, or life under the
  law. If this is your settled condition, the chapter is not describing your
  Christian life — it is asking whether you have one."

Both are quoting Romans 7 accurately as far as the words go. They are giving
opposite counsel, and both kinds of counsel have done real good and real harm:
A has comforted the despairing and excused the complacent; B has woken the
complacent and crushed the despairing. The question is not academic.

It is also not new. It is one of the oldest live disputes in Christian
interpretation, and — this is worth saying plainly at the outset — **it has never
been settled, and serious, orthodox, careful readers have landed on every side of
it.** Anyone who tells you it is obvious has not felt the weight of the evidence
against their position.

## The evidence on the page

Before the readings, the data. Everything in these two tables is checkable
against the text, and the commands that produce the counts are in
[Appendix D](#appendix-d--the-verb-data).

### Evidence that the "I" is *not* a Christian

| | Evidence | Where |
| --- | --- | --- |
| 1 | *"sold under sin"* — a perfect passive: sold, and still in that state | 7:14 |
| 2 | Paul has just said believers are *"made free from sin"* and *"dead to sin"* | 6:2, 6:18, 6:22 |
| 3 | *"brought into captivity to the law of sin"* — a prisoner of war | 7:23 |
| 4 | **The Holy Spirit is never mentioned in 7:7–25** | see below |
| 5 | The conflict is flesh vs. *mind* (νοῦς), not flesh vs. *Spirit* as in Galatians 5:17 | 7:23, 7:25 |
| 6 | *"in me... dwelleth no good thing"* sits oddly beside *"Christ in you"* | 7:18; 8:10 |
| 7 | The section is unrelieved defeat; Romans 6 and 8 describe victory | 7:14–24 |
| 8 | Romans 8:9 says flatly that believers are *"not in the flesh, but in the Spirit"* | 8:9 |

On point 4, the count is absolute and it is the most objective datum in the
debate:

```sh
# one occurrence in Romans 7, and it is in verse 6
awk -F'\t' '$1 ~ /^Romans 7:/ && $4=="G4151" {print $1}' \
  original-languages/greek/tr-scrivener-words.tsv
# twenty-two in Romans 8
awk -F'\t' '$1 ~ /^Romans 8:/ && $4=="G4151"' \
  original-languages/greek/tr-scrivener-words.tsv | wc -l
```

A chapter about the Christian life that never once mentions the Spirit, standing
immediately before a chapter that mentions the Spirit twenty-two times, is a
strange thing.

### Evidence that the "I" *is* a Christian

| | Evidence | Where |
| --- | --- | --- |
| 1 | **The tenses are present throughout 7:14–25**, after a past-tense narrative in 7:7–13 | see Appendix D |
| 2 | *"I delight in the law of God after the inward man"* — Paul says the unregenerate mind *cannot* be subject to God's law | 7:22; cf. 8:7 |
| 3 | *"I consent unto the law that it is good"* | 7:16 |
| 4 | *"what I would, that do I not"* — the will is on God's side | 7:15, 19, 21 |
| 5 | *"the inward man"* is Paul's phrase elsewhere for the believer's renewed interior | 7:22; 2 Cor 4:16; Eph 3:16 |
| 6 | Galatians 5:17 describes a closely parallel conflict in undisputed Christians | Gal 5:17 |
| 7 | Believers *"groan within ourselves"* awaiting the body's redemption — the same unfinished business as 7:24 | 8:23 |
| 8 | The hatred of one's own sin in 7:15 is not a mark of the unconverted | 7:15 |

Point 2 is the sharpest. Paul writes in Romans 8:7 that *"the carnal mind is
enmity against God: for it is not subject to the law of God, neither indeed can
be."* If the *I* of 7:22 delights in God's law *"after the inward man,"* and the
unregenerate mind *cannot* do that, then by Paul's own statement the *I* of 7:22
is not unregenerate. That is a genuine difficulty for the non-Christian readings
and they have to answer it.

### The honest summary of the data

**Both lists are strong.** That is the actual state of the evidence, and it is
why the debate has lasted seventeen centuries. Anyone whose reading makes one of
these lists disappear has stopped reading the text and started defending a
position.

## Reading 1: Paul's autobiography

**The claim.** Romans 7 is Paul's own spiritual autobiography — the young Saul
of Tarsus discovering, under the tenth commandment, that his outward
blamelessness concealed a heart full of craving; then the tormented years of a
conscience the law could not quiet, ending on the Damascus road.

**What supports it.** The relentless first person, with eight emphatic ἐγώ. The
specificity of verse 9, *"I was alive without the law once"* — which sounds like
a man remembering a date. And the sheer psychological particularity of verses
15–24, which does not read like a constructed illustration.

**The difficulties, and they are severe.**

First, **Paul's own account of his pre-Christian conscience contradicts it:**

> **Philippians 3:5–6** — Circumcised the eighth day, of the stock of Israel, of
> the tribe of Benjamin, an Hebrew of the Hebrews; as touching the law, a
> Pharisee; Concerning zeal, persecuting the church; touching the righteousness
> which is in the law, **blameless**.

That is not the self-portrait of a man whose pre-conversion years were spent in
the anguish of Romans 7:24. Paul remembers his life under the law as
*blameless* — and he says so in a passage whose whole purpose is to devalue his
Jewish credentials. If his conscience had been in torment, that passage is where
he would have said so; it would have strengthened his argument.

This is the observation that reshaped twentieth-century study of the chapter.
Krister Stendahl, in a 1963 essay on "the introspective conscience of the West,"
argued that reading Romans 7 as Paul's tortured pre-conversion conscience
projects backwards onto a first-century Jew a species of interiority that belongs
to Augustine and Luther — that we have been reading Paul through the *Confessions*
and the monastery. Whatever one makes of the whole of Stendahl's case, the
Philippians 3 datum has to be answered.

Second, **verse 9 does not fit Paul's biography.** *"I was alive without the law
once"* — when? A boy raised in a devout diaspora Pharisaic household was never
*"without the law."* The common repair is bar mitzvah, the age at which a Jewish
boy becomes responsible for the commandments, but that is a later institution
than Paul and the text says nothing about it.

Third, **the description is too extreme for anyone's literal autobiography.**
*Sold under sin*, *nothing good dwells in me*, *taken captive* — as a description
of Saul the Pharisee this is not modesty, it is a different person.

**Where it stands.** Almost no one now holds the strictly autobiographical
reading in its pure form, and the decisive study was W. G. Kümmel's, published in
1929, which argued that the *I* of Romans 7 is a rhetorical figure rather than a
record of Paul's inner history. That conclusion has been broadly accepted even by
scholars who disagree with Kümmel about nearly everything else.

But two qualifications keep it from being simply wrong:

- **Rhetorical does not mean impersonal.** Paul writes in the first person
  because he includes himself in what he describes, even if he is not narrating
  his own calendar. The *I* is representative, and Paul is one of those it
  represents.
- **Conversion changes the past.** It is entirely possible for Paul to have
  experienced his Pharisaic years as blameless *at the time* and to look back on
  them from the other side of Damascus and see a man who had never once kept the
  tenth commandment. Philippians 3:6 reports how it felt then; Romans 7 may
  report what it was. Those are not contradictory, and the second is the sort of
  thing only conversion reveals.

## Reading 2: The unbeliever

**The claim.** Romans 7:14–25 describes a person outside Christ — either anyone
under conviction of sin, or more specifically the Jew under the law, brought by
the commandment to the end of self-effort. The chapter is the law's proper work:
to drive a person to despair of themselves so they will cry *"who shall deliver
me?"*

**What supports it.** The whole of the first list above, and especially the four
statements that appear flatly incompatible with Romans 6 and 8: *sold under sin*,
*captive*, *nothing good dwells in me*, and *"they that are in the flesh cannot
please God"* set against *"I am carnal."* On this reading the chapter's silence
about the Spirit is not an oddity to be explained but the single most eloquent
fact in it — **the Spirit is missing from Romans 7 because the man is.**

It also makes sense of the structure: Paul is showing what the law can and cannot
do, and the answer is that the law can bring a man to verse 24 and no further.
The cry of verse 24 is then a conversion cry, and verse 25a is its answer.

**The difficulties.**

First, **the tenses**. Paul told the story of his past in verses 7–13 in the
aorist. At verse 14 he switches to the present and stays there for twelve verses.
If he were still narrating a past condition, the natural thing — the thing he was
doing three verses earlier — would be to keep the past tense. The switch has to
be explained as a vivid historic present, which is possible but is a strain over
twelve consecutive verses.

Second, **verse 22, against Romans 8:7**. An unbeliever who *delights* in God's
law after the inward man is, on Paul's own account in 8:7, not something that
exists.

Third, **the moral psychology is too good**. Hating one's sin, willing the good,
agreeing that the law is good, delighting in it — Paul's description of the
unconverted elsewhere in Romans is considerably darker (1:32, where they not only
do such things but have pleasure in those who do them; 3:10–18; 8:7).

**A stronger version of the reading** avoids most of this. Rather than "the
unbeliever in general," it takes the *I* as **the Jew under the Torah**, or
*Israel*, viewed from the far side of the gospel. On that version the delight in
the law is genuine — it is the delight of Psalm 119, real and pious — and the
tragedy is precisely that sincere delight in a holy law cannot produce obedience
in flesh. This is the reading Douglas Moo has argued at length in his commentary
on Romans, and it is considerably harder to refute than the simpler form. It also
connects the chapter to the argument Paul is actually running in Romans, which is
about the law and Israel, not about the interior life in general.

## Reading 3: The Christian

**The claim.** Romans 7:14–25 describes the normal experience of a believer — not
a carnal or backslidden one, but any Christian honestly examining themselves
against God's holy law. Sin no longer reigns, but it still dwells. The believer
is free from sin's dominion and not yet free from its presence.

**What supports it.** The whole of the second list. The present tenses are the
backbone. Verse 22 is the keystone: delight in God's law after the inward man is
something Paul elsewhere says the unregenerate cannot manage.

It also has a strong argument from **spiritual perception**: the more mature a
believer is, the more sin they see in themselves, because they see more of God's
holiness to measure against. On this view verse 24 is not a pre-conversion cry
but the cry of a saint, and the chapter is the most honest self-assessment in the
New Testament precisely because it comes from someone far along.

And Romans 8:23 supports it directly. Believers who have *the firstfruits of the
Spirit* still *groan*, waiting for *the redemption of our body*. That is 7:24's
question — *who shall deliver me from the body of this death?* — asked by
unambiguous Christians in chapter 8.

**The difficulties.**

First, **"sold under sin" (7:14)**. Paul has just written that believers were
*"made free from sin"* (6:18, 6:22). The standard reply is that 7:14 describes
sin's continuing presence, not its dominion, and that the perfect participle
looks back to a state entered in Adam. That is a possible reading; it is also a
considerable softening of πεπραμένος, which is the language of the slave market.

Second, **Romans 8:9**: *"But ye are not in the flesh, but in the Spirit."* Flat.
And 8:8: *"they that are in the flesh cannot please God."* If the Romans 7 man is
*carnal, sold under sin*, chapter 8 appears to say he is not a believer.

Third, **the missing Spirit**, which on this reading becomes genuinely odd. If
this is the normal Christian life, why is the Christian's chief resource absent
for nineteen verses?

Fourth, **the unrelieved defeat**. Romans 6 is emphatic that sin *shall not* have
dominion. Romans 7:14–24 is a record of sin having it, continuously.

**A stronger version of this reading**, associated with James Dunn among others,
frames it as **eschatological tension** rather than ordinary defeat. The believer
lives in the overlap of the ages: already justified, already indwelt, not yet
raised. Romans 7:14–25 describes the believer *considered under one aspect* — as
still in a mortal body not yet redeemed — while Romans 8 describes the same
believer under the aspect of the Spirit. The two chapters are not sequential
stages in a life but two true descriptions of one person in the overlap. On this
version the absence of the Spirit in chapter 7 is deliberate: Paul is
**abstracting**, showing what the believer would be if considered apart from the
Spirit, in order to make chapter 8's answer land.

That is an elegant solution and it accounts for more of the data than the simple
form. Its cost is that the abstraction has to be inferred; Paul does not signal
it.

## Reading 4: Adam, Israel, and speech-in-character

**The claim.** The *I* is not a report of anyone's inner life, Paul's or the
reader's. It is a **rhetorical persona**. Paul is speaking in character — telling
the story of humanity under the commandment, in the first person, as a way of
making the reader inhabit it.

This is not a modern invention to escape the difficulty. Ancient rhetorical
handbooks name and teach the device: **προσωποποιία** (*prosōpopoeia*),
speech-in-character, in which a speaker takes on another's voice. Ancient readers
were trained to recognise it. Stanley Stowers and others have argued at length
that a first-century audience hearing Romans read aloud would have identified the
shift at verse 7 as exactly this.

**What supports it.**

*Verse 9 fits Adam and fits nobody else.* Who was ever *"alive without the law
once"*, then received a commandment, and died?

| Romans 7 | Genesis 2–3 |
| --- | --- |
| *"I was alive without the law once"* (v. 9) | Adam in the garden before the prohibition |
| *"when the commandment came"* (v. 9) | *"of the tree of the knowledge of good and evil, thou shalt not eat"* |
| *"sin, taking occasion by the commandment, deceived me"* (v. 11) | the serpent using the commandment as its opening |
| *"and by it slew me"* (v. 11) | *"in the day that thou eatest thereof thou shalt surely die"* |
| *"the commandment, which was ordained to life"* (v. 10) | the tree of life in the same garden |

And the verb clinches it. *Deceived* in 7:11 is ἐξηπάτησεν — the same word, in
the same form, that Paul uses of the serpent and Eve in 2 Corinthians 11:3. Of
the five occurrences of ἐξαπατάω in the Textus Receptus New Testament, one is
Romans 7:11 and one is the serpent.

*The chapter's argument is about Israel and the law, not about introspection.*
Romans 7 sits inside an argument running from chapter 2 to chapter 11 about the
Torah, Israel, and God's faithfulness. On this reading, verses 7–13 retell
Genesis 3 as it was repeated at Sinai: Israel received the commandment, sin took
its occasion, and *"Israel was alive without the law once"* in the sense that the
nation existed before Sinai. N. T. Wright has argued this at length — the *I* is
Israel, telling Adam's story again, because Israel recapitulated Adam's failure
with a better commandment.

*It explains the shape.* On this reading the tense change at verse 14 is not a
change of person but a change of vantage: verses 7–13 narrate the event, verses
14–25 describe the resulting condition — which is a *standing* condition and
therefore present tense. That explains the tenses without making the *I* a
Christian, which is the single most useful thing this reading does.

**The difficulties.**

First, the elements do not map perfectly onto Adam. Adam was not *"sold under
sin"* before he sinned, and the tenth commandment is not the prohibition in
Eden — Paul quotes Sinai, not Genesis.

Second, if it is Israel, the delight of verse 22 and the captivity of verse 23
have to be corporate, and verses 15–20 read very personally for a national
history.

Third — the honest objection — **this reading can become a way of not being
addressed by the chapter.** If the *I* is a persona, a literary device belonging
to an argument about Israel, the reader is off the hook. That is not a
refutation, but it is worth naming, because the pastoral history of the chapter
suggests Paul wrote it to be inhabited.

## How the church argued it

The debate has a history, and knowing it helps, because most of what people
today assume about Romans 7 they inherited from one of these figures without
knowing it.

### The Greek fathers: not the believer

The early Greek-speaking commentators broadly read the *I* as a rhetorical figure
for humanity under the law, not as the Christian. **Origen** (c. 185–254) took
the *I* as a persona rather than Paul himself. **John Chrysostom** (c. 347–407)
read the passage as describing human life before grace, and was explicit that
Paul was not describing himself as an apostle. This is the older consensus, and
it is worth registering that the reading which is now often treated as novel or
liberal is in fact the patristic one.

### Augustine changes his mind, and the West follows

The single most consequential event in the history of this chapter.

**Early Augustine** read Romans 7:14–25 of a man *under the law*, not yet under
grace. He said so in his commentaries on Romans in the 390s.

**Later Augustine** — in the thick of the Pelagian controversy — reversed. He
came to read the passage of Paul himself, as a mature Christian, in whom
*concupiscentia* remained after baptism, and he records the change of mind
explicitly in the *Retractationes* (426–427), the remarkable work in which he
went back over his own writings and corrected them.

The context of the reversal matters. Augustine was arguing against Pelagius, who
held that human beings can keep God's commandments by the power of free will.
Romans 7, read of the *Christian*, is a devastating text against that position:
if even the apostle cannot do the good he wills, perfectionism is finished. The
reading was forged in a controversy, and the controversy shaped it.

Whether that makes the reading suspect or well-tested is exactly what people
disagree about. What is not in dispute is that **the Christian reading became the
Western default because Augustine adopted it**, and that it did so for reasons
partly polemical.

### The Reformers: the believer, emphatically

**Luther** read Romans 7 as the Christian, and it became load-bearing for him. His
formula *simul iustus et peccator* — at the same time righteous and a sinner — is
Romans 7 compressed to four words. Luther's own experience in the monastery,
straining after a righteousness he could not reach, made the chapter read like a
description of his life, and through him it has read that way to much of
Protestantism ever since.

**Calvin** argued the Christian reading exegetically rather than experientially.
His case rests on verse 22: only a regenerate person delights in the law of God
after the inward man. He thought the alternative reading made nonsense of the
verse.

The **Reformed confessional tradition** followed, and the doctrine of remaining
sin in the believer became standard — with Romans 7 as its principal proof text.

### Arminius, and then Wesley

**Jacobus Arminius** (1560–1609) wrote a dissertation specifically on Romans 7
arguing that the passage describes a man *not* under grace. Coming from a
Reformed minister, this was provocative, and it was among the things that made
him controversial in his own church.

**John Wesley** took a similar line for different reasons. Wesley taught that a
believer could, by grace, be freed from the dominion of sin in a way Romans 7
does not describe; he read the chapter as the state of a person under conviction
— awakened by the law, not yet delivered by the gospel. The Wesleyan and Holiness
traditions have generally followed.

The pattern is worth noticing: **traditions that expect more of sanctification in
this life tend to read Romans 7 as pre-Christian; traditions that emphasise
remaining sin tend to read it as Christian.** The chapter is read, to a
considerable extent, in the light of what a tradition already believes about
holiness. That is a reason for humility on all sides.

### The twentieth century onward

- **W. G. Kümmel** (1929) argued that the *I* is rhetorical rather than
  autobiographical. This reshaped the field and is now broadly assumed.
- **Rudolf Bultmann** proposed that 7:25b is a gloss — a proposal with no
  manuscript support (see [7:25](#725--the-answer-and-the-sentence-that-will-not-lie-down)).
- **Krister Stendahl** (1963) argued that the introspective reading imports
  Augustine's and Luther's interiority into a text written by a man who described
  his own conscience under the law as blameless.
- **C. E. B. Cranfield** (ICC, 1975) mounted a full defence of the Christian
  reading against the tide.
- **James D. G. Dunn** developed the eschatological-tension version of the
  Christian reading: already and not yet.
- **Douglas Moo** argued the non-Christian reading in its strong form: the *I* is
  Israel, or the Jew, under the law.
- **N. T. Wright** argued the Israel-recapitulating-Adam version of the persona
  reading.
- **Stanley Stowers** and others pressed the case for *prosōpopoeia* on
  rhetorical-historical grounds.

**The state of play.** There is no consensus. The autobiographical reading in its
naive form is effectively dead; everything else is live. If anything has shifted
in recent decades, it is that the Israel/Adam readings have gained ground against
both of the older options, and that the "which one is it?" framing is increasingly
seen as a false choice.

## Weighing it

Here is an assessment, with the reasoning shown.

### What the four readings get right

Each of them is responding to something really in the text:

- **Autobiography** is right that the passage is personal. Paul did not write
  eight emphatic ἐγώ by accident, and the passage has the texture of something
  known from the inside.
- **The unbeliever reading** is right about the missing Spirit, and right that
  the chapter's function in the argument is to show the law's limit.
- **The Christian reading** is right about the tenses and right about verse 22,
  and those are the two hardest data points in the chapter.
- **The persona reading** is right about Genesis 3, and the ἐξηπάτησεν evidence
  is as hard as evidence gets in this kind of question.

A reading that requires any of those four to be an illusion is probably wrong.

### The shape of a better answer

The question *"is the I a Christian or not?"* assumes Paul is describing a
**person**. The evidence fits better if he is describing a **condition** — what
human beings are under the law and in the flesh, considered apart from the
Spirit.

On that account:

1. **Verses 7–13 tell the story** of how the commandment met sin — Adam's story
   first, retold in Israel, and true of every person since. Past tense, because
   it is a narrative.
2. **Verses 14–25 describe the resulting condition** — what it is to be a human
   being confronted by a holy law with nothing but a willing mind to meet it.
   Present tense, because a condition is present.
3. **The Spirit is absent because Paul has excluded him from the frame**, not
   because the speaker is unconverted. Paul is showing what the law meets when
   the Spirit is not in the picture. That is why chapter 8's opening lands with
   such force: the missing person arrives.
4. **The *I* is inhabited, not merely performed.** Paul writes in the first
   person because the condition is his too — not as a former biography but as a
   present possibility. A Christian who tries to live by the law in their own
   strength is in Romans 7 that day, whatever their standing in Christ.

This is close to the persona reading in its mechanics and close to the Christian
reading in its pastoral application, and it accounts for both lists of evidence
without deleting either.

### Saying where this lands

On the narrow question — *is the speaker in 7:14–25 a regenerate person?* — the
most defensible answer is: **the question is slightly wrong, and to the extent it
can be answered, the passage describes a condition Christians can be in but which
is not the normative Christian life.**

Three reasons for that conclusion:

1. **The Spirit's absence is decisive about something.** Nineteen verses without
   the Spirit, followed by twenty-two mentions in the next chapter, is not
   accidental in a writer this deliberate. Whatever 7:14–25 describes, it is not
   life in the Spirit, because life in the Spirit is what chapter 8 is for.
2. **But the tenses and verse 22 are equally stubborn.** A man who delights in
   God's law after the inward man is not, on Paul's own account in 8:7, an
   unregenerate man. So the passage is not simply pre-Christian either.
3. **Paul's placement settles the pastoral question even if it does not settle
   the exegetical one.** He did not end the letter at 7:25. He wrote 8:1 next.
   Whatever the chapter describes, the author's own verdict on it is *"there is
   therefore now no condemnation."*

This is a conclusion held with real tentativeness on point 1 and 2, and with
confidence on point 3. Readers who land elsewhere on the first two are in
excellent company, and Appendix F points to where their case is made properly.

## What actually hangs on it

Less than the heat of the argument suggests. Here is what changes and what does
not.

**What does not change, on any reading:**

- The law is holy, just and good (7:12) — every reading agrees, because the text
  says it four times.
- Sin, not the law, is the problem (7:7–13) — this is the chapter's thesis and it
  is not disputed by anyone.
- Human beings cannot produce obedience out of willing alone (7:15–19).
- Deliverance is a person, not a method (7:24–25).
- There is now no condemnation for those in Christ (8:1).

**What does change:**

- Whether a Christian should expect Romans 7 to describe their week.
- Whether prolonged defeat is evidence about one's standing before God.
- How much the New Testament expects sanctification to deliver in this life.

Those are real questions. But notice that **none of them is settled by Romans 7
alone on any reading**, because Romans 8 follows in every Bible, and Romans 6
precedes it in every Bible. A Christian who takes Romans 6, 7 and 8 together
arrives at roughly the same place regardless of how they resolve the identity of
the *I*:

> Sin no longer reigns (6). Sin still dwells, and the law cannot dislodge it (7).
> The Spirit does what the law could not, and the body's redemption is still
> future (8).

That is the argument of the three chapters, and it is not in dispute.

---

# Part IV — Living With Romans 7

## The two errors the chapter gets used to license

Romans 7 is quoted in support of two opposite mistakes, and both of them work by
stopping reading at a convenient point.

### Error 1: "Romans 7 is normal, so don't expect change"

The chapter becomes a permanent excuse. *"It is no more I that do it, but sin
that dwelleth in me"* (7:17, 20) is repeated as a formula for not taking
responsibility, and the settled expectation becomes defeat.

**Why it fails:**

- Verse 17 is not an alibi. The man who says it cries *"O wretched man that I
  am!"* seven verses later. He has not exonerated himself; he has diagnosed
  himself.
- The chapter is a **cry for rescue**, not a description of a settled
  arrangement. The one future verb in the passage is *shall deliver*.
- Romans 6 has already ruled it out: *"Shall we continue in sin, that grace may
  abound? God forbid"* (6:1–2). The identical μὴ γένοιτο that defends the law in
  chapter 7 demolishes this use of chapter 7.
- Romans 8:12–13 is explicit: *"ye are not debtors to the flesh... if ye through
  the Spirit do mortify the deeds of the body, ye shall live."* There is work to
  do and a power to do it with.

### Error 2: "Romans 7 is sub-Christian, so a real believer isn't there"

The chapter becomes a test that the struggling fail. If you recognise yourself
in verses 15–24, you are carnal, or unconverted, or have not yet had some second
experience.

**Why it fails:**

- The man of Romans 7 **hates his sin** (v. 15), **wills the good** (v. 15, 19),
  **agrees the law is good** (v. 16), and **delights in God's law in his inmost
  self** (v. 22). None of that is a portrait of someone far from God. Every one
  of those four is a work of grace.
- Paul says believers with *the firstfruits of the Spirit* **groan** (8:23). The
  New Testament does not promise a struggle-free interior.
- Using the chapter to make people doubt their salvation inverts its destination.
  Paul's own next sentence is *"There is therefore now no condemnation."* A use
  of Romans 7 that produces condemnation is being read against the grain of the
  text it stands in.

**The rule of thumb.** Romans 7 describes a real experience and prescribes
nothing. It is a diagnosis, and diagnoses are neither excuses nor verdicts. The
prescription is in chapter 8.

## What the chapter does not say

It is worth being explicit, because each of these is commonly read into it:

- **It does not say the body is evil.** σάρξ is not the physical body; Paul's
  hope in 8:23 is the body's *redemption*, not its disposal. The members are
  where the war is fought, not the enemy.
- **It does not say the law has been abolished.** It says the law is holy, just
  and good (7:12), spiritual (7:14), and the object of the speaker's delight
  (7:22). What has changed is the believer's relation to it (7:4, 7:6).
- **It does not say Christians have two natures fighting like two dogs.** That is
  a later theological framework which may or may not be true, but Paul's terms
  here are *flesh*, *mind*, *inward man* and *members*, not *natures*. The
  language is of an occupied territory, not a partitioned personality.
- **It does not say the will is free and merely weak, or that it is bound and
  merely willing.** It says both in the same breath — *"to will is present with
  me; but how to perform that which is good I find not."* Theological systems
  have been built on each half. The verse holds them together.
- **It does not say deliverance is a technique.** The question of 7:24 is *who*,
  and the answer of 7:25 is a name.

## What it does say to a struggling Christian

Five things, and they hold on any of the readings in Part III.

**1. Your experience is not evidence that the gospel has failed.**
The gap between willing and performing is described in Scripture, at length, by
an apostle. Whatever else that gap is, it is not a surprise to God and not a
sign that you have been given something defective.

**2. The fact that you hate it is itself significant.**
*"What I hate, that do I."* A person genuinely indifferent to God does not hate
their sin; they manage it, excuse it, or enjoy it. The hatred is not the problem.
It is evidence of something working in you that was not there before.

**3. The willing is real even when the performing is not.**
*"To will is present with me."* Paul does not dismiss the will as hypocrisy. He
treats it as genuine and grieves that it is not enough. If you want to be holy
and keep failing, the wanting is not a sham.

**4. Your resource is not your mind.**
This is the chapter's most practical lesson and it is embedded in the vocabulary.
The man of Romans 7 fights with his νοῦς — his understanding, his resolve, his
grasp of what is right — and is taken prisoner. More information, more resolve,
more determination: these are what he has, and they lose. Romans 8 introduces
what he lacks. If your strategy against sin is entirely a matter of trying
harder and knowing better, you are fighting Romans 7's war with Romans 7's
weapons, and the chapter tells you how that ends.

**5. The cry is the right response.**
*"O wretched man that I am! who shall deliver me?"* is not despair, and it is not
failure. It is the correct thing to say, and it is immediately answered. The
chapter models what to do when you reach the end of yourself: stop asking *how*
and start asking *who*.

## Romans 7 and besetting sin

A practical word, since this is what brings most people to the chapter.

**Romans 7 explains why willpower alone does not work.** It does not explain why
*nothing* works, and it does not counsel passivity. Set the chapter beside what
the New Testament says elsewhere and a picture emerges that is neither "try
harder" nor "let go and let God":

| Romans 7 shows | The rest of the New Testament adds |
| --- | --- |
| the mind alone loses (7:23) | *"if ye through the Spirit do mortify the deeds of the body"* (8:13) |
| sin dwells within (7:17, 20) | *"the Spirit of God dwell in you"* (8:9) |
| the body is contested (7:5, 23) | *"yield your members as instruments of righteousness"* (6:13) |
| the law cannot deliver (7:10–11) | *"what the law could not do... God sending his own Son"* (8:3) |
| the cry for rescue (7:24) | *"the Spirit also helpeth our infirmities"* (8:26) |

Notice that Romans 8:13 gives real work to do — *mortify* is an active verb, and
it is addressed to the believer — but specifies the power to do it with: *through
the Spirit*. That is the combination Romans 7 lacks and Romans 8 supplies. The
chapter's lesson for besetting sin is not "stop trying." It is **stop trying
alone, with only your understanding and your resolve, against something that
outguns both.**

And one further observation from the structure of the letter: Paul does not
address the problem of indwelling sin by telling anyone to look harder at
themselves. Romans 7 is where self-examination gets you, and it gets you to
verse 24. What comes next is not deeper introspection but a look outward — *"no
condemnation,"* *"the Spirit of him that raised up Jesus,"* *"who shall separate
us from the love of Christ?"* The chapter that has taught generations to examine
themselves is followed immediately by a chapter that tells them to stop.

## Praying Romans 7

The chapter gives words to people who have run out of them. Four of its
sentences can be prayed almost as they stand.

**When you cannot understand yourself:**

> *That which I do I allow not: for what I would, that do I not; but what I hate,
> that do I.* (7:15)

Prayed simply as description. There is no request in it, and it does not need
one. Telling God the truth about a conflict you cannot resolve is a prayer.

**When you need to name where the trouble is:**

> *For I know that in me (that is, in my flesh,) dwelleth no good thing: for to
> will is present with me; but how to perform that which is good I find not.*
> (7:18)

Both halves. Not only the confession, but the claim that the willing is real —
because the willing is a gift and worth acknowledging as one.

**When you are at the end:**

> *O wretched man that I am! who shall deliver me from the body of this death?*
> (7:24)

The permission this verse gives is worth stating plainly: a Christian is allowed
to say this. It is in the Bible, in the first person, from an apostle. It is not
a lapse of faith to pray it; it is the last honest step before the answer.

**And then, without waiting:**

> *I thank God through Jesus Christ our Lord.* (7:25)

Paul puts no interval between the cry and the thanksgiving, and neither should
the prayer. The answer does not have to be felt before it is thanked for.

**Then keep reading.** The best use of Romans 7 in prayer is to refuse to end
there. Pray verse 24, pray verse 25, and go straight on into Romans 8:1 — *there
is therefore now no condemnation to them which are in Christ Jesus* — because
that is what Paul did with it, and he wrote it.

---

# Appendices

## Appendix A — The KJV and the Greek side by side

The KJV of 1769 from [`kjv/kjv.txt`](kjv/kjv.txt); the Greek is Scrivener's 1894
Textus Receptus from
[`original-languages/greek/tr-scrivener.txt`](original-languages/greek/tr-scrivener.txt),
which is the text the KJV translators worked from. That text is unaccented in
this repository, as its README explains. To reproduce either column:

```sh
grep '^Romans 7:' kjv/kjv.txt
grep '^Romans 7:' original-languages/greek/tr-scrivener.txt
```

| v. | KJV (1769) | Scrivener TR (1894) |
| ---: | --- | --- |
| 1 | Know ye not, brethren, (for I speak to them that know the law,) how that the law hath dominion over a man as long as he liveth? | η αγνοειτε αδελφοι γινωσκουσιν γαρ νομον λαλω οτι ο νομος κυριευει του ανθρωπου εφ οσον χρονον ζη |
| 2 | For the woman which hath an husband is bound by the law to her husband so long as he liveth; but if the husband be dead, she is loosed from the law of her husband. | η γαρ υπανδρος γυνη τω ζωντι ανδρι δεδεται νομω εαν δε αποθανη ο ανηρ κατηργηται απο του νομου του ανδρος |
| 3 | So then if, while her husband liveth, she be married to another man, she shall be called an adulteress: but if her husband be dead, she is free from that law; so that she is no adulteress, though she be married to another man. | αρα ουν ζωντος του ανδρος μοιχαλις χρηματισει εαν γενηται ανδρι ετερω εαν δε αποθανη ο ανηρ ελευθερα εστιν απο του νομου του μη ειναι αυτην μοιχαλιδα γενομενην ανδρι ετερω |
| 4 | Wherefore, my brethren, ye also are become dead to the law by the body of Christ; that ye should be married to another, even to him who is raised from the dead, that we should bring forth fruit unto God. | ωστε αδελφοι μου και υμεις εθανατωθητε τω νομω δια του σωματος του χριστου εις το γενεσθαι υμας ετερω τω εκ νεκρων εγερθεντι ινα καρποφορησωμεν τω θεω |
| 5 | For when we were in the flesh, the motions of sins, which were by the law, did work in our members to bring forth fruit unto death. | οτε γαρ ημεν εν τη σαρκι τα παθηματα των αμαρτιων τα δια του νομου ενηργειτο εν τοις μελεσιν ημων εις το καρποφορησαι τω θανατω |
| 6 | But now we are delivered from the law, that being dead wherein we were held; that we should serve in newness of spirit, and not in the oldness of the letter. | νυνι δε κατηργηθημεν απο του νομου αποθανοντος εν ω κατειχομεθα ωστε δουλευειν ημας εν καινοτητι πνευματος και ου παλαιοτητι γραμματος |
| 7 | What shall we say then? Is the law sin? God forbid. Nay, I had not known sin, but by the law: for I had not known lust, except the law had said, Thou shalt not covet. | τι ουν ερουμεν ο νομος αμαρτια μη γενοιτο αλλα την αμαρτιαν ουκ εγνων ει μη δια νομου την τε γαρ επιθυμιαν ουκ ηδειν ει μη ο νομος ελεγεν ουκ επιθυμησεις |
| 8 | But sin, taking occasion by the commandment, wrought in me all manner of concupiscence. For without the law sin was dead. | αφορμην δε λαβουσα η αμαρτια δια της εντολης κατειργασατο εν εμοι πασαν επιθυμιαν χωρις γαρ νομου αμαρτια νεκρα |
| 9 | For I was alive without the law once: but when the commandment came, sin revived, and I died. | εγω δε εζων χωρις νομου ποτε ελθουσης δε της εντολης η αμαρτια ανεζησεν εγω δε απεθανον |
| 10 | And the commandment, which was ordained to life, I found to be unto death. | και ευρεθη μοι η εντολη η εις ζωην αυτη εις θανατον |
| 11 | For sin, taking occasion by the commandment, deceived me, and by it slew me. | η γαρ αμαρτια αφορμην λαβουσα δια της εντολης εξηπατησεν με και δι αυτης απεκτεινεν |
| 12 | Wherefore the law is holy, and the commandment holy, and just, and good. | ωστε ο μεν νομος αγιος και η εντολη αγια και δικαια και αγαθη |
| 13 | Was then that which is good made death unto me? God forbid. But sin, that it might appear sin, working death in me by that which is good; that sin by the commandment might become exceeding sinful. | το ουν αγαθον εμοι γεγονεν θανατος μη γενοιτο αλλα η αμαρτια ινα φανη αμαρτια δια του αγαθου μοι κατεργαζομενη θανατον ινα γενηται καθ υπερβολην αμαρτωλος η αμαρτια δια της εντολης |
| 14 | For we know that the law is spiritual: but I am carnal, sold under sin. | οιδαμεν γαρ οτι ο νομος πνευματικος εστιν εγω δε σαρκικος ειμι πεπραμενος υπο την αμαρτιαν |
| 15 | For that which I do I allow not: for what I would, that do I not; but what I hate, that do I. | ο γαρ κατεργαζομαι ου γινωσκω ου γαρ ο θελω τουτο πρασσω αλλ ο μισω τουτο ποιω |
| 16 | If then I do that which I would not, I consent unto the law that it is good. | ει δε ο ου θελω τουτο ποιω συμφημι τω νομω οτι καλος |
| 17 | Now then it is no more I that do it, but sin that dwelleth in me. | νυνι δε ουκετι εγω κατεργαζομαι αυτο αλλ η οικουσα εν εμοι αμαρτια |
| 18 | For I know that in me (that is, in my flesh,) dwelleth no good thing: for to will is present with me; but how to perform that which is good I find not. | οιδα γαρ οτι ουκ οικει εν εμοι τουτ εστιν εν τη σαρκι μου αγαθον το γαρ θελειν παρακειται μοι το δε κατεργαζεσθαι το καλον ουχ ευρισκω |
| 19 | For the good that I would I do not: but the evil which I would not, that I do. | ου γαρ ο θελω ποιω αγαθον αλλ ο ου θελω κακον τουτο πρασσω |
| 20 | Now if I do that I would not, it is no more I that do it, but sin that dwelleth in me. | ει δε ο ου θελω εγω τουτο ποιω ουκετι εγω κατεργαζομαι αυτο αλλ η οικουσα εν εμοι αμαρτια |
| 21 | I find then a law, that, when I would do good, evil is present with me. | ευρισκω αρα τον νομον τω θελοντι εμοι ποιειν το καλον οτι εμοι το κακον παρακειται |
| 22 | For I delight in the law of God after the inward man: | συνηδομαι γαρ τω νομω του θεου κατα τον εσω ανθρωπον |
| 23 | But I see another law in my members, warring against the law of my mind, and bringing me into captivity to the law of sin which is in my members. | βλεπω δε ετερον νομον εν τοις μελεσιν μου αντιστρατευομενον τω νομω του νοος μου και αιχμαλωτιζοντα με τω νομω της αμαρτιας τω οντι εν τοις μελεσιν μου |
| 24 | O wretched man that I am! who shall deliver me from the body of this death? | ταλαιπωρος εγω ανθρωπος τις με ρυσεται εκ του σωματος του θανατου τουτου |
| 25 | I thank God through Jesus Christ our Lord. So then with the mind I myself serve the law of God; but with the flesh the law of sin. | ευχαριστω τω θεω δια ιησου χριστου του κυριου ημων αρα ουν αυτος εγω τω μεν νοι δουλευω νομω θεου τη δε σαρκι νομω αμαρτιας |

---

## Appendix B — The textual variants

Romans 7 is textually calm. There is no disputed paragraph, no bracketed verse,
and nothing that touches doctrine. But three places show the two text traditions
parting, and they explain most of the differences between the KJV and a modern
translation of this chapter. All three can be checked in the six editions in
[`original-languages/greek/`](original-languages/greek):

```sh
for f in tr-scrivener kjtr byzantine sblgnt nestle1904 sr; do
  printf '%-14s ' "$f"
  grep '^Romans 7:14 ' original-languages/greek/$f.txt
done
```

### 1. Verse 6 — who died?

| Edition | Reading |
| --- | --- |
| Scrivener TR | ἀποθανόντος (genitive singular) |
| CNTR KJTR | ἀποθανόντες |
| Byzantine RP2018 | ἀποθανόντες |
| SBLGNT | ἀποθανόντες |
| Nestle 1904 | ἀποθανόντες |
| CNTR SR | ἀποθανόντες |

The genitive ἀποθανόντος makes *the law* the thing that died: the KJV's *"that
being dead wherein we were held."* The nominative plural ἀποθανόντες makes *us*
the ones who died: *"having died to that wherein we were held."*

**Scrivener's Textus Receptus stands alone here** — even the Byzantine text of the
same tradition reads with the critical editions. This is the only variant in the
chapter recorded in the repository's own variant table:

```sh
grep '^Romans 7:' original-languages/greek/tr-variants.tsv
```
```
Romans 7:6	αποθανοντες	αποθανοντος
```

**Effect on sense:** small. Paul has spent verses 1–5 establishing that a death
dissolves the bond, and both readings say a death dissolved it. The variant does
explain why the KJV reads differently from every modern version at this point.

### 2. Verse 14 — σαρκικός or σάρκινος?

| Edition | Reading | Sense |
| --- | --- | --- |
| Scrivener TR | σαρκικός | fleshly in character |
| CNTR KJTR | σαρκικός | fleshly in character |
| Byzantine RP2018 | σαρκικός | fleshly in character |
| SBLGNT | σάρκινός | made of flesh |
| Nestle 1904 | σάρκινός | made of flesh |
| CNTR SR | σάρκινός | made of flesh |

A clean split between the Byzantine tradition and the critical editions. Strong's
distinguishes them: G4559 σαρκικός, *"pertaining to flesh... by implication,
animal, unregenerate"*; G4560 σάρκινος, *"similar to flesh, i.e. by analogy,
soft."* Adjectives in **-ικος** describe character or ethical quality; adjectives
in **-ινος** describe material.

**Effect on sense:** real, and it bears on Part III. σαρκικός is a moral
self-characterisation (*I am a fleshly sort of person*); σάρκινος is closer to a
statement about constitution (*I am made of flesh* — creaturely and weak). The
critical reading is the milder, and some have argued it fits the Christian
reading of the chapter more easily. The KJV's *carnal* renders σαρκικός.

### 3. Verse 25 — εὐχαριστῶ or χάρις?

| Edition | Reading | Sense |
| --- | --- | --- |
| Scrivener TR | εὐχαριστῶ τῷ θεῷ | *I thank God* |
| CNTR KJTR | Ἐυχάριστῶ τῷ Θεῷ | *I thank God* |
| Byzantine RP2018 | Εὐχαριστῶ τῷ θεῷ | *I thank God* |
| SBLGNT | χάρις τῷ θεῷ | *thanks be to God* |
| Nestle 1904 | χάρις τῷ Θεῷ | *thanks be to God* |
| CNTR SR | Χάρις τῷ ˚Θεῷ | *thanks be to God* |

The same split. **Effect on sense:** small but not nil. The TR's first-person
verb keeps the personal voice of the whole passage unbroken into the
thanksgiving — the *I* who cried in verse 24 is the *I* who gives thanks in verse
25. The critical reading is a liturgical formula, the same construction as
1 Corinthians 15:57 and 2 Corinthians 2:14.

### 4. Verse 18 — a minor addition

The Textus Receptus ends verse 18 with οὐχ εὑρίσκω, *"I find not"* — hence the
KJV's *"but how to perform that which is good I find not."* The critical
editions end with a bare οὔ: *"but to do the good, no."* Nothing doctrinal turns
on it.

### Verse division at 9/10

Not a textual variant but a versification difference, and worth knowing if you
compare editions. The words are identical; the verse break is not:

| | End of v. 9 | Start of v. 10 |
| --- | --- | --- |
| KJV / TR | *...sin revived, and I died.* | *And the commandment...* |
| SBLGNT / critical | *...ἡ ἁμαρτία ἀνέζησεν* | *ἐγὼ δὲ ἀπέθανον, καὶ εὑρέθη...* |

The TR puts *"and I died"* at the end of verse 9; the critical editions put it at
the start of verse 10. Same text, different fence.

---

## Appendix C — Word tables

Definitions are from
[`original-languages/lexicons/strongs-greek.tsv`](original-languages/lexicons/strongs-greek.tsv)
and [`dodson-greek.tsv`](original-languages/lexicons/dodson-greek.tsv). To look
up any entry:

```sh
grep -P '^G0874\t' original-languages/lexicons/strongs-greek.tsv
```

### The chapter's key vocabulary

| Greek | Strong's | KJV in Rom. 7 | Sense |
| --- | --- | --- | --- |
| νόμος | G3551 | law | law; also *principle, regime* |
| ἁμαρτία | G0266 | sin | sin as a power, not acts |
| σάρξ | G4561 | flesh | human nature as weak and self-turned |
| ἐπιθυμία | G1939 | lust, concupiscence | craving; *"a longing (especially for what is forbidden)"* |
| ἐντολή | G1785 | commandment | a specific precept |
| ἀφορμή | G0874 | occasion | *"a starting-point"*; a base of operations |
| κατεργάζομαι | G2716 | do, work, perform | *"to work fully, accomplish"* |
| θέλω | G2309 | would, will | to will, want, intend |
| οἰκέω | G3611 | dwelleth | to inhabit, to live in as a house |
| παράκειμαι | G3873 | is present | *"to lie near, be at hand"* |
| νοῦς | G3563 | mind | *"the intellect... in thought, feeling, or will"* |
| ἀντιστρατεύομαι | G0497 | warring against | to campaign against militarily |
| αἰχμαλωτίζω | G0163 | bringing into captivity | to take prisoner of war |
| ταλαίπωρος | G5005 | wretched | *"enduring trial, miserable"* |
| ῥύομαι | G4506 | deliver | to rescue, snatch from danger |
| καταργέω | G2673 | loosed, delivered | to render inoperative, nullify |
| ἐξαπατάω | G1818 | deceived | to deceive thoroughly |
| συνήδομαι | G4913 | delight | *"to rejoice in with oneself"*; **only here in the NT** |

### Counts within Romans 7

| Word | Strong's | Count | Notes |
| --- | ---: | ---: | --- |
| νόμος | G3551 | 23 | densest chapter in the NT; 75 in Romans, 197 in the NT |
| ἁμαρτία | G0266 | 15 | usually the subject of active verbs |
| ἐγώ (nominative) | G1473 | 8 | emphatic; vv. 9 ×2, 14, 17, 20 ×2, 24, 25 |
| σάρξ | G4561 | 3 | vv. 5, 18, 25 — against 14 in Romans 8 |
| πνεῦμα | G4151 | **1** | v. 6 only — against 22 in Romans 8 |

Reproduce any of these:

```sh
awk -F'\t' '$1 ~ /^Romans 7:/ && $4=="G3551"' \
  original-languages/greek/tr-scrivener-words.tsv | wc -l
```

### νόμος verse by verse in Romans 7

| Verse | Count | | Verse | Count |
| ---: | ---: | --- | ---: | ---: |
| 1 | 2 | | 12 | 1 |
| 2 | 2 | | 14 | 1 |
| 3 | 1 | | 16 | 1 |
| 4 | 1 | | 21 | 1 |
| 5 | 1 | | 22 | 1 |
| 6 | 1 | | 23 | 3 |
| 7 | 3 | | 25 | 2 |
| 8 | 1 | | | |
| 9 | 1 | | **Total** | **23** |

Verses 10, 11, 13, 15, 17, 18, 19, 20 and 24 contain no occurrence.

---

## Appendix D — The verb data

The tense change at verse 14 is the most objective fact in the chapter and the
one most often asserted without evidence. Here it is in full, from
[`tr-scrivener-words.tsv`](original-languages/greek/tr-scrivener-words.tsv). The
morphology codes are the source's own: `V-2AAI-1S` is second aorist active
indicative first person singular, `V-PAI-1S` present active indicative first
singular, and so on.

```sh
awk -F'\t' '$1 ~ /^Romans 7:/ && $5 ~ /^V-/ {print $1"\t"$3"\t"$5}' \
  original-languages/greek/tr-scrivener-words.tsv
```

### Verses 7–13 — past narrative

| Verse | Form | Parsing | Gloss |
| --- | --- | --- | --- |
| 7 | ἐροῦμεν | V-FAI-1P | shall we say |
| 7 | γένοιτο | V-2ADO-3S | may it be (optative, negated) |
| 7 | ἔγνων | V-2AAI-1S | **I knew** (aorist) |
| 7 | ᾔδειν | V-2LAI-1S | **I had known** (pluperfect) |
| 7 | ἔλεγεν | V-IAI-3S | **it was saying** (imperfect) |
| 7 | ἐπιθυμήσεις | V-FAI-2S | thou shalt covet (in the quotation) |
| 8 | λαβοῦσα | V-2AAP-NSF | having taken (aorist participle) |
| 8 | κατειργάσατο | V-ADI-3S | **it worked** (aorist) |
| 9 | ἔζων | V-IAI-1S | **I was living** (imperfect) |
| 9 | ἐλθούσης | V-2AAP-GSF | having come (aorist participle) |
| 9 | ἀνέζησεν | V-AAI-3S | **it revived** (aorist) |
| 9 | ἀπέθανον | V-2AAI-1S | **I died** (aorist) |
| 10 | εὑρέθη | V-API-3S | **it was found** (aorist passive) |
| 11 | λαβοῦσα | V-2AAP-NSF | having taken (aorist participle) |
| 11 | ἐξηπάτησεν | V-AAI-3S | **it deceived** (aorist) |
| 11 | ἀπέκτεινεν | V-AAI-3S | **it slew** (aorist) |
| 13 | γέγονεν | V-2RAI-3S | has become (perfect) |
| 13 | γένοιτο | V-2ADO-3S | may it be (optative, negated) |
| 13 | φανῇ | V-2APS-3S | it might appear (aorist subjunctive) |
| 13 | κατεργαζομένη | V-PNP-NSF | working (present participle) |
| 13 | γένηται | V-2ADS-3S | it might become (aorist subjunctive) |

Every first-person indicative in this section is aorist, imperfect or pluperfect.
There is not one present.

### Verses 14–25 — present condition

| Verse | Form | Parsing | Gloss |
| --- | --- | --- | --- |
| 14 | οἴδαμεν | V-RAI-1P | we know (perfect, used as present) |
| 14 | ἐστιν | V-PAI-3S | is |
| 14 | εἰμι | V-PAI-1S | **I am** |
| 14 | πεπραμένος | V-RPP-NSM | having been sold (perfect passive participle) |
| 15 | κατεργάζομαι | V-PNI-1S | **I bring about** |
| 15 | γινώσκω | V-PAI-1S | **I understand** |
| 15 | θέλω | V-PAI-1S | **I will** |
| 15 | πράσσω | V-PAI-1S | **I practise** |
| 15 | μισῶ | V-PAI-1S | **I hate** |
| 15 | ποιῶ | V-PAI-1S | **I do** |
| 16 | θέλω | V-PAI-1S | **I will** |
| 16 | ποιῶ | V-PAI-1S | **I do** |
| 16 | σύμφημι | V-PAI-1S | **I agree** |
| 17 | κατεργάζομαι | V-PNI-1S | **I bring about** |
| 17 | οἰκοῦσα | V-PAP-NSF | dwelling (present participle) |
| 18 | οἶδα | V-RAI-1S | I know (perfect, used as present) |
| 18 | οἰκεῖ | V-PAI-3S | dwells |
| 18 | ἐστιν | V-PAI-3S | is |
| 18 | θέλειν | V-PAN | to will (present infinitive) |
| 18 | παράκειται | V-PNI-3S | is at hand |
| 18 | κατεργάζεσθαι | V-PNN | to bring about (present infinitive) |
| 18 | εὑρίσκω | V-PAI-1S | **I find** |
| 19 | θέλω | V-PAI-1S | **I will** |
| 19 | ποιῶ | V-PAI-1S | **I do** |
| 19 | θέλω | V-PAI-1S | **I will** |
| 19 | πράσσω | V-PAI-1S | **I practise** |
| 20 | θέλω | V-PAI-1S | **I will** |
| 20 | ποιῶ | V-PAI-1S | **I do** |
| 20 | κατεργάζομαι | V-PNI-1S | **I bring about** |
| 20 | οἰκοῦσα | V-PAP-NSF | dwelling (present participle) |
| 21 | εὑρίσκω | V-PAI-1S | **I find** |
| 21 | θέλοντι | V-PAP-DSM | willing (present participle) |
| 21 | ποιεῖν | V-PAN | to do (present infinitive) |
| 21 | παράκειται | V-PNI-3S | is at hand |
| 22 | συνήδομαι | V-PNI-1S | **I delight** |
| 23 | βλέπω | V-PAI-1S | **I see** |
| 23 | ἀντιστρατευόμενον | V-PNP-ASM | campaigning against (present participle) |
| 23 | αἰχμαλωτίζοντα | V-PAP-ASM | taking captive (present participle) |
| 23 | ὄντι | V-PAP-DSM | being (present participle) |
| 24 | ῥύσεται | V-FDI-3S | **shall deliver** (future) |
| 25 | εὐχαριστῶ | V-PAI-1S | **I thank** |
| 25 | δουλεύω | V-PAI-1S | **I serve** |

**Summary.** In verses 14–25 there is no aorist, no imperfect and no pluperfect
anywhere. Every finite first-person verb is present indicative, with three
exceptions: two perfects that function as presents (οἶδα *I know*, and the
participle πεπραμένος *having been sold*, a resulting state), and one future —
ῥύσεται, *shall deliver*, the cry for rescue in verse 24.

That the only future tense in the passage is the appeal for a rescuer is worth
sitting with.

---

## Appendix E — Cross-reference index

Every passage cited in this document, with the KJV text, so the argument can be
checked without leaving the page. All are in [`kjv/kjv.txt`](kjv/kjv.txt).

### The commandment Paul quotes

| Reference | Text |
| --- | --- |
| Exodus 20:17 | Thou shalt not covet thy neighbour's house, thou shalt not covet thy neighbour's wife, nor his manservant, nor his maidservant, nor his ox, nor his ass, nor any thing that is thy neighbour's. |
| Deuteronomy 5:21 | Neither shalt thou desire thy neighbour's wife, neither shalt thou covet thy neighbour's house, his field, or his manservant, or his maidservant, his ox, or his ass, or any thing that is thy neighbour's. |

### The law's promise of life (7:10)

| Reference | Text |
| --- | --- |
| Leviticus 18:5 | Ye shall therefore keep my statutes, and my judgments: which if a man do, he shall live in them: I am the LORD. |

### "Sold" to do evil (7:14)

| Reference | Text |
| --- | --- |
| 1 Kings 21:20 | ...because thou hast sold thyself to work evil in the sight of the LORD. |
| 1 Kings 21:25 | But there was none like unto Ahab, which did sell himself to work wickedness in the sight of the LORD, whom Jezebel his wife stirred up. |
| 2 Kings 17:17 | ...and sold themselves to do evil in the sight of the LORD, to provoke him to anger. |

In all three the verb is active and reflexive — *sold themselves*. Romans 7:14 is
passive.

### Delight in the law (7:22)

| Reference | Text |
| --- | --- |
| Psalms 1:2 | But his delight is in the law of the LORD; and in his law doth he meditate day and night. |
| Psalms 119:97 | O how love I thy law! it is my meditation all the day. |

### The argument leading into Romans 7

| Reference | Text |
| --- | --- |
| Romans 3:20 | Therefore by the deeds of the law there shall no flesh be justified in his sight: for by the law is the knowledge of sin. |
| Romans 4:15 | Because the law worketh wrath: for where no law is, there is no transgression. |
| Romans 5:13 | (For until the law sin was in the world: but sin is not imputed when there is no law. |
| Romans 5:20 | Moreover the law entered, that the offence might abound. But where sin abounded, grace did much more abound: |
| Romans 6:2 | God forbid. How shall we, that are dead to sin, live any longer therein? |
| Romans 6:6 | Knowing this, that our old man is crucified with him, that the body of sin might be destroyed, that henceforth we should not serve sin. |
| Romans 6:13 | Neither yield ye your members as instruments of unrighteousness unto sin: but yield yourselves unto God, as those that are alive from the dead, and your members as instruments of righteousness unto God. |
| Romans 6:14 | For sin shall not have dominion over you: for ye are not under the law, but under grace. |
| Romans 6:17–18 | But God be thanked, that ye were the servants of sin, but ye have obeyed from the heart that form of doctrine which was delivered you. Being then made free from sin, ye became the servants of righteousness. |
| Romans 6:22 | But now being made free from sin, and become servants to God, ye have your fruit unto holiness, and the end everlasting life. |

### The answer in Romans 8

| Reference | Text |
| --- | --- |
| Romans 8:1 | There is therefore now no condemnation to them which are in Christ Jesus, who walk not after the flesh, but after the Spirit. |
| Romans 8:2 | For the law of the Spirit of life in Christ Jesus hath made me free from the law of sin and death. |
| Romans 8:3 | For what the law could not do, in that it was weak through the flesh, God sending his own Son in the likeness of sinful flesh, and for sin, condemned sin in the flesh: |
| Romans 8:4 | That the righteousness of the law might be fulfilled in us, who walk not after the flesh, but after the Spirit. |
| Romans 8:7 | Because the carnal mind is enmity against God: for it is not subject to the law of God, neither indeed can be. |
| Romans 8:8 | So then they that are in the flesh cannot please God. |
| Romans 8:9 | But ye are not in the flesh, but in the Spirit, if so be that the Spirit of God dwell in you. Now if any man have not the Spirit of Christ, he is none of his. |
| Romans 8:13 | For if ye live after the flesh, ye shall die: but if ye through the Spirit do mortify the deeds of the body, ye shall live. |
| Romans 8:23 | And not only they, but ourselves also, which have the firstfruits of the Spirit, even we ourselves groan within ourselves, waiting for the adoption, to wit, the redemption of our body. |
| Romans 8:26 | Likewise the Spirit also helpeth our infirmities: for we know not what we should pray for as we ought: but the Spirit itself maketh intercession for us with groanings which cannot be uttered. |

### Paul on his own past

| Reference | Text |
| --- | --- |
| Philippians 3:5–6 | Circumcised the eighth day, of the stock of Israel, of the tribe of Benjamin, an Hebrew of the Hebrews; as touching the law, a Pharisee; Concerning zeal, persecuting the church; touching the righteousness which is in the law, blameless. |
| Philippians 3:9 | And be found in him, not having mine own righteousness, which is of the law, but that which is through the faith of Christ, the righteousness which is of God by faith: |

### The parallel conflict in Galatians

| Reference | Text |
| --- | --- |
| Galatians 2:19–20 | For I through the law am dead to the law, that I might live unto God. I am crucified with Christ: nevertheless I live; yet not I, but Christ liveth in me: and the life which I now live in the flesh I live by the faith of the Son of God, who loved me, and gave himself for me. |
| Galatians 5:16 | This I say then, Walk in the Spirit, and ye shall not fulfil the lust of the flesh. |
| Galatians 5:17 | For the flesh lusteth against the Spirit, and the Spirit against the flesh: and these are contrary the one to the other: so that ye cannot do the things that ye would. |

### ἐξαπατάω — the Genesis 3 echo

Five occurrences in the Textus Receptus New Testament:

```sh
awk -F'\t' '$4=="G1818" {print $1"\t"$3}' \
  original-languages/greek/tr-scrivener-words.tsv
```

| Reference | Form | KJV |
| --- | --- | --- |
| Romans 7:11 | ἐξηπάτησεν | deceived me |
| Romans 16:18 | ἐξαπατῶσιν | deceive the hearts of the simple |
| 1 Corinthians 3:18 | ἐξαπατάτω | let no man deceive himself |
| **2 Corinthians 11:3** | **ἐξηπάτησεν** | **as the serpent beguiled Eve** |
| 2 Thessalonians 2:3 | ἐξαπατήσῃ | let no man deceive you |

Romans 7:11 and 2 Corinthians 11:3 share the identical form.

### μὴ γένοιτο — "God forbid" in Romans

All ten:

| Reference | The inference Paul is killing |
| --- | --- |
| Romans 3:4 | that human unbelief makes God's faithfulness void |
| Romans 3:6 | that God is unrighteous to judge |
| Romans 3:31 | that faith makes the law void |
| Romans 6:2 | that we should continue in sin so grace may abound |
| Romans 6:15 | that we may sin because we are under grace |
| **Romans 7:7** | **that the law is sin** |
| **Romans 7:13** | **that the good thing became death to me** |
| Romans 9:14 | that there is unrighteousness with God |
| Romans 11:1 | that God has cast away his people |
| Romans 11:11 | that Israel has stumbled so as to fall |

```sh
grep -c 'God forbid' <(grep '^Romans ' kjv/kjv.txt)
```

### The "inward man"

| Reference | Text |
| --- | --- |
| 2 Corinthians 4:16 | For which cause we faint not; but though our outward man perish, yet the inward man is renewed day by day. |
| Ephesians 3:16 | That he would grant you, according to the riches of his glory, to be strengthened with might by his Spirit in the inner man; |

### ταλαίπωρος — "wretched"

Only twice in the New Testament:

| Reference | Text |
| --- | --- |
| Romans 7:24 | O wretched man that I am! who shall deliver me from the body of this death? |
| Revelation 3:17 | Because thou sayest, I am rich, and increased with goods, and have need of nothing; and knowest not that thou art wretched, and miserable, and poor, and blind, and naked: |

The one man knows he is wretched and cries for rescue; the other does not know
it and thinks he needs nothing.

---

## Appendix F — Where the positions are argued

For readers who want the cases made properly by those who hold them. This is a
map, not a bibliography of everything written on the chapter, and the
characterisations are brief enough to be unfair — go to the sources.

### The Christian reading

- **Augustine**, *Retractationes* (426–427), where he records changing his mind,
  and the anti-Pelagian writings where he uses the changed reading. The origin of
  the Western default.
- **Martin Luther**, *Lectures on Romans* (1515–16) and throughout. *Simul iustus
  et peccator* is Romans 7 as a doctrine.
- **John Calvin**, *Commentary on Romans*, and *Institutes* III. Calvin's case
  rests on verse 22 and is the most purely exegetical of the classic defences.
- **C. E. B. Cranfield**, *The Epistle to the Romans* (ICC, 1975). The most
  thorough modern defence.
- **James D. G. Dunn**, *Romans 1–8* (WBC, 1988). The eschatological-tension
  version: already and not yet.

### The non-Christian reading

- **John Chrysostom**, *Homilies on Romans*. The patristic reading, explicit that
  Paul is not describing himself as an apostle.
- **Jacobus Arminius**, *A Dissertation on the True and Genuine Sense of Chapter
  VII of the Epistle to the Romans* (published posthumously). A sustained
  argument against the Reformed consensus of his own church.
- **John Wesley**, *Explanatory Notes upon the New Testament* and the sermons on
  sin in believers. The state of a person under conviction, not yet delivered.
- **Douglas J. Moo**, *The Epistle to the Romans* (NICNT). The strongest modern
  form: the *I* is the Jew, or Israel, under the law.

### The rhetorical / persona readings

- **W. G. Kümmel**, *Römer 7 und die Bekehrung des Paulus* (1929). The study that
  ended the naive autobiographical reading.
- **Krister Stendahl**, "The Apostle Paul and the Introspective Conscience of the
  West" (1963). Short, and it changed how a generation read the chapter.
- **Stanley K. Stowers**, *A Rereading of Romans* (1994). The case for
  *prosōpopoeia* on rhetorical-historical grounds.
- **N. T. Wright**, *The Climax of the Covenant* (1991) and the Romans commentary
  in *The New Interpreter's Bible* (2002). Israel recapitulating Adam.

### On the textual questions

- The six editions in [`original-languages/greek/`](original-languages/greek) and
  their README, which explains what each is and why they differ.
- [`tr-variants.tsv`](original-languages/greek/tr-variants.tsv) for the Romans 7:6
  reading.

---

## Appendix G — Questions for study and discussion

Ordered so that a group can work through the chapter in four sessions, one per
part. The questions are meant to send people back to the text rather than to
opinions about it.

### Session 1 — The setting (Part I; Romans 6:1–7:6)

1. List everything Paul has said about the law before chapter 7 (the table in
   [Where Romans 7 sits](#where-romans-7-sits) is a start). If you had heard only
   those statements, what would you conclude about the law? Is the conclusion
   unreasonable?
2. In the marriage analogy (7:1–3), who corresponds to whom in verse 4? Where
   does the correspondence break down, and does that matter?
3. Romans 7:4 says believers were *put to death* — a passive. Who did it, and
   when? Compare Romans 6:3–6.
4. Paul says freedom from the law is *for* remarriage to Christ (7:4) and *for*
   a new kind of service (7:6). What does that say about what Christian freedom
   is and is not?

### Session 2 — The law and sin (Part II; Romans 7:7–13)

5. Why does Paul choose the tenth commandment rather than any of the other nine?
   What could a person do about murder or theft that they cannot do about
   coveting?
6. Paul says sin took the commandment as an ἀφορμή — a base of operations
   (7:8, 11). Where have you seen a prohibition make something more attractive
   rather than less? What does that reveal?
7. Line up Romans 7:9–11 against Genesis 2–3. How many elements correspond? What
   does the correspondence suggest about who is speaking?
8. Verse 13 says the whole mechanism was so that sin *might appear sin* and
   become *exceeding sinful*. In what sense is that a merciful purpose?

### Session 3 — The divided self (Part II; Romans 7:14–25)

9. Read 7:15, 19 and 21 aloud. Do you recognise the experience? Describe it in
   your own words before reaching for any explanation of it.
10. What exactly is Paul claiming in 7:17 and 20 — *"it is no more I that do
    it"*? What is he **not** claiming? How do verses 16 and 24 constrain the
    answer?
11. Look at the parenthesis in 7:18: *"in me (that is, in my flesh,)"*. Why the
    correction? What does it imply about the rest of the *I*?
12. In 7:23 the man fights with *the law of my mind*. What resource is missing
    that Romans 8 will supply? What difference does that make to how he fares?
13. Why does Paul, having given thanks in 7:25a, immediately restate the division
    in 7:25b? Which of the three explanations in the exposition do you find most
    likely?

### Session 4 — The identity question and its uses (Parts III and IV)

14. Before reading Part III: read 7:14–25 straight through and decide whether the
    speaker sounds like a Christian. Write down the verse that most influenced
    you. Then read the two evidence tables and see whether your verse is on the
    other list.
15. Romans 8:7 says the carnal mind *cannot* be subject to God's law. Romans 7:22
    says the speaker delights in God's law in his inmost self. How do you hold
    those together?
16. There is no mention of the Spirit in 7:7–25, and twenty-two mentions in
    chapter 8. What do you make of that? Consider at least two explanations
    before settling.
17. Consider the two pastoral errors in Part IV. Which one is your own tradition
    more prone to? Which one are **you** more prone to, and why?
18. Someone in your church says, "I've been fighting the same sin for ten years
    and I'm starting to wonder whether I'm saved at all." What do you say, and
    which verses do you use? Would your answer change depending on how you
    resolved question 14?

---

## A closing note

The chapter has been fought over for seventeen hundred years, and nothing in this
document settles it. But it is worth ending where Paul ends, because the shape of
his argument is itself an answer of a kind.

He describes the condition at length — twelve verses of it, in the present tense,
without relief. He does not soften it, does not offer a technique, and does not
tell the reader to try harder. He lets it run all the way to *"O wretched man
that I am!"*

And then he does not linger. The thanksgiving comes in the same breath as the
cry, before anything has visibly changed, and the next sentence he writes is
*"There is therefore now no condemnation to them which are in Christ Jesus."*

Whoever the *I* of Romans 7 turns out to be, that is what Paul thought should be
said to him.

