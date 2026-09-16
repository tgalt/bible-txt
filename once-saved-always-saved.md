# Once Saved, Always Saved?
## What Scripture Says About Whether a Christian Can Be Lost, What the Church Has Made of It, and What It Means for Your Own Assurance

---

## How to Use This Document

This document answers three questions, in order:

1. **What does the Bible actually say?** — every passage that bears on whether a person who has been saved can be finally lost, quoted and read in context, with the way each side reads the other side's texts (Part I)
2. **How has the church answered?** — from the fathers who assumed a Christian could fall, through Augustine, Trent, Luther, Calvin, Dort, Wesley and the Baptists, to the modern debate, with the actual words of the people on each side (Part II)
3. **What does it mean for you?** — how the New Testament says a Christian can know they are saved, what to do if you are afraid you have fallen away, and what to say to someone who is sure they are fine (Part III)

Part I is the reference material. Part II explains why the question divides Christians roughly along the line between Calvinist and Arminian, and why the popular slogan "once saved, always saved" is not quite what either of the great traditions teaches. Part III is the practical payoff.

**If you are reading this because you are afraid you have lost your salvation, or because someone you love has walked away from the faith,** go to Part III first. Everything there is either agreed by every Christian tradition or clearly labelled as belonging to one of them, and none of it requires you to settle the argument in Parts I and II first.

### The source of the quotations

Scripture is quoted from the **King James Version (1769)**, the text carried in [`kjv/`](kjv) in this repository. Every quotation was taken directly from that file, so any verse can be checked at its source:

```sh
grep '^John 10:28 ' kjv/kjv.txt
```

Where the KJV's English has drifted far enough to mislead, the modern sense is given in brackets or in the surrounding comment — *castaway* (1 Corinthians 9:27) means disqualified, rejected after testing; *reprobates* (2 Corinthians 13:5) is the same word; *dureth* means endures; *anon* and *by and by* mean at once; *graffed* is grafted; *without repentance* (Romans 11:29) means irrevocable, not "without regret"; *let them slip* (Hebrews 2:1) means drift away from them; *conversation* means conduct; *the earnest* is a down payment.

Greek words are cited from the texts and lexicons in [`original-languages/`](original-languages), with their Strong's numbers, and the parsing of a verb (its tense and mood) is taken from the interlinear there. Any word can be checked:

```sh
grep '^Hebrews 6:6	' original-languages/interlinear/nt-interlinear.tsv
grep '^G3895	' original-languages/lexicons/strongs-greek.tsv
```

### A note on the names

"Once saved, always saved" is a slogan, not a confession. It is the popular name for a family of views, and it hides a real difference inside that family. The Reformed churches teach the *perseverance of the saints*: everyone God has truly saved will be kept by him and will persevere in faith and holiness to the end. A good deal of popular teaching, especially in American Baptist and dispensationalist circles, teaches something stronger and simpler, often called *eternal security* or *Free Grace*: a person who has once believed is saved forever, whatever happens afterward. The two agree that the saved cannot be lost. They disagree sharply about what to say of the church member who stops believing and dies in unbelief. Part I keeps the two apart throughout, because most confusion on this subject comes from running them together.

The alternative, held by Catholics, Orthodox, Lutherans, Methodists, Pentecostals, Free Will Baptists and many others, is usually called *conditional security*: a person who has truly been saved can, by unbelief or persistent wilful sin, fall away and be finally lost. It too comes in versions, and they are distinguished where it matters.

### A note on what this document is not

This is a study of the biblical and historical material, not a ruling from a church. On this question the churches have ruled, in opposite directions, and the rulings are quoted. Where sincere Christians have disagreed for fifteen hundred years, the disagreement is laid out rather than settled, and the passages that drive each side are quoted so you can weigh them. Where this document does take a position, it says so and shows its work (see [Honest caveats](#e-honest-caveats)).

---

## Contents

**[Part I — What the Bible Says](#part-i--what-the-bible-says)**

- [Three positions, not two](#three-positions-not-two)
- [The words themselves](#the-words-themselves)
- [Saved: past, present, and future](#saved-past-present-and-future)
- [The Old Testament: a covenant with conditions, and a God who does not let go](#the-old-testament-a-covenant-with-conditions-and-a-god-who-does-not-let-go)
- [Saul, David, and Solomon](#saul-david-and-solomon)
- [Ezekiel's righteous man](#ezekiels-righteous-man)
- [Israel in the wilderness: the New Testament's own example](#israel-in-the-wilderness-the-new-testaments-own-example)
- [Texts cited for security](#texts-cited-for-security)
- [Texts cited for the possibility of falling](#texts-cited-for-the-possibility-of-falling)
- [The warning passages of Hebrews](#the-warning-passages-of-hebrews)
- [The New Testament's apostates](#the-new-testaments-apostates)
- [How each side reads the other's texts](#how-each-side-reads-the-others-texts)
- [What both sides agree Scripture teaches](#what-both-sides-agree-scripture-teaches)
- [What the question turns on](#what-the-question-turns-on)

**[Part II — What the Church Has Taught](#part-ii--what-the-church-has-taught)**

- [The first four centuries: falling assumed](#the-first-four-centuries-falling-assumed)
- [Augustine: the gift of perseverance](#augustine-the-gift-of-perseverance)
- [The medieval West and Trent](#the-medieval-west-and-trent)
- [The East](#the-east)
- [Luther and the Lutherans](#luther-and-the-lutherans)
- [Calvin](#calvin)
- [Arminius, the Remonstrants, and Dort](#arminius-the-remonstrants-and-dort)
- [England, Westminster, and the Baptists](#england-westminster-and-the-baptists)
- [Wesley](#wesley)
- [The twentieth century: "once saved, always saved" and the Free Grace debate](#the-twentieth-century-once-saved-always-saved-and-the-free-grace-debate)

**[Part III — What It Means for You](#part-iii--what-it-means-for-you)**

- [Start with what is certain](#start-with-what-is-certain)
- [Two ditches](#two-ditches)
- [Assurance: how the New Testament says you can know](#assurance-how-the-new-testament-says-you-can-know)
- [If you are afraid you have fallen away](#if-you-are-afraid-you-have-fallen-away)
- [If you are sure you are fine](#if-you-are-sure-you-are-fine)
- [If someone you love has walked away](#if-someone-you-love-has-walked-away)
- [What the warnings are for](#what-the-warnings-are-for)
- [The one thing everyone agrees on](#the-one-thing-everyone-agrees-on)

**[Appendices](#appendices)**

- [A. Every passage that bears on the question](#a-every-passage-that-bears-on-the-question)
- [B. The two great warnings of Hebrews in full](#b-the-two-great-warnings-of-hebrews-in-full)
- [C. A timeline](#c-a-timeline)
- [D. Where the traditions stand](#d-where-the-traditions-stand)
- [E. Honest caveats](#e-honest-caveats)
- [F. Further reading](#f-further-reading)

---
---

# Part I — What the Bible Says

## Three positions, not two

The question is usually put as a choice between two answers: either "once saved, always saved" or "you can lose your salvation." There are in fact three main positions, and the difference between the first two matters as much as the difference between either of them and the third.

Take one case and hold it steady through everything that follows. A man professes faith in Christ, is baptised, joins a church, lives as a Christian for ten years, and then renounces Christ, lives the rest of his life as an unbeliever, and dies one. What happened?

**Position A — the perseverance of the saints (Reformed).** Everyone God has truly regenerated will be kept by God and will persevere in faith and holiness to the end. They may fall into grievous sin and remain in it for a time, but they cannot totally or finally fall away. The man in the example was therefore never regenerate. His experience was real as an experience — Calvin himself called it "temporary faith" — but it was not the new birth. "They went out from us, but they were not of us." This is the position of the Synod of Dort (1619), the Westminster Confession (1646), the Reformed and Presbyterian churches, the Particular and Reformed Baptists, and a large part of evangelicalism. Note what it does *not* say: it does not say a saved person will be saved however they live. It says a saved person will not, in the end, live that way. Perseverance is both a promise (God will keep you) and a necessity (you must persevere), and continuing in faith is the evidence that the beginning was real.

**Position B — unconditional eternal security ("once saved, always saved" in its strict form; "Free Grace").** A person who has once believed is saved forever, whether or not they continue in faith or holiness. Eternal life is a gift given on the single condition of faith at a moment, and a gift once given is not taken back. The man in the example was saved and is still saved. He will lose reward at the judgment seat of Christ, may have suffered God's discipline in this life up to and including an early death, and may have been miserable, but he cannot lose eternal life, because eternal life that could be lost would not have been eternal. "If we believe not, yet he abideth faithful." This is the position of the Free Grace movement (Zane Hodges, Charles Ryrie, Charles Stanley), of much dispensationalist teaching, and of a great deal of American Baptist preaching whether or not it has a name for itself.

**Position C — conditional security.** A person who has truly been born again can, by unbelief or by persistent wilful sin, fall away and be finally lost. The man in the example was saved, and is now lost. Within this position there are real differences about *how* one falls and whether one can come back: the Wesleyan says by unbelief or by persistent sin, and the fallen can be restored; the Reformed Arminian (Free Will Baptist) says only by a settled renunciation of faith, and that such apostasy is final; the Lutheran says faith and the Holy Spirit are lost by wilful sin and regained by repentance, while adding that God's elect will not finally be lost; the Catholic says sanctifying grace is lost by any mortal sin and restored by the sacrament of penance; the Orthodox decline to define it and say salvation is a lifelong cooperation with grace that a person can abandon. But all of these agree that the man in the example was once genuinely in Christ and is not now.

| | **A — Perseverance of the saints** | **B — Unconditional security** | **C — Conditional security** |
| --- | --- | --- | --- |
| **Can a truly saved person be finally lost?** | No | No | Yes |
| **Will a truly saved person necessarily persevere in faith?** | Yes | No | No |
| **The man who renounced Christ and died an unbeliever was** | Never saved | Saved, and still saved | Saved, and now lost |
| **What keeps the believer** | God, by sustaining faith and holiness | God, by his promise, irrespective of the believer's later faith | God, through the believer's continuing faith, which can be abandoned |
| **How the warnings are read** | Means by which God keeps his own; addressed to the mixed church | Loss of reward, fellowship, or temporal life, never of salvation | Real dangers to real Christians |
| **How the promises are read** | Unconditional guarantees to the elect | Unconditional guarantees to every believer | Promises to believers as long as they believe |
| **Assurance rests on** | Christ's promise, the Spirit's witness, and the fruit of a changed life | Christ's promise alone; looking at one's life undermines assurance | Christ's promise and the Spirit's witness, for one presently believing |
| **Held by** | Reformed, Presbyterian, Reformed Baptist, much of evangelicalism | Free Grace, much dispensationalist and popular Baptist teaching | Catholic, Orthodox, Lutheran, Anglican (Article 16), Methodist, Wesleyan, Pentecostal, Free Will Baptist, Restorationist |
| **Governing texts** | Dort, Fifth Head; Westminster 17 | No confession; Hodges, *Absolutely Free!* (1989) | Trent, Session 6; Formula of Concord; Remonstrance, Article 5; Wesley, *Serious Thoughts* (1751) |

Three things follow from the table.

First, **each pair of positions shares a premise against the third.** A and B agree that the saved cannot be lost. A and C agree that a person who ends in unbelief is lost. B and C agree that the apostate was genuinely saved. Nobody in this argument is alone, and nobody's opponents agree with each other.

Second, **the practical difference between A and C is much smaller than the theoretical one.** Both tell the believer to persevere, both warn the wanderer, both say the one who ends in unbelief is lost. Their disagreement is about the *description* of that person: whether he was ever alive. The practical difference between B and both of the others is larger, because B alone tells the man in the example that he is going to heaven.

Third, **"once saved, always saved" is not the fifth point of Calvinism.** The Reformed doctrine is that the saints persevere; the slogan, taken strictly, says the saved need not. Reformed writers have spent as much ink against B as against C, and Part II shows why.

---

## The words themselves

None of the names is in Scripture. "Once saved, always saved," "eternal security," "perseverance of the saints," and "conditional security" are all later coinages. What Scripture has is a vocabulary on both sides of the question, and it is worth having the words in view before the arguments, because much of the argument is about which words control.

**Saved.** Greek **σῴζω** (*sōzō*, G4982), "to save, deliver, protect." The KJV uses *saved* in 104 verses, 57 of them in the New Testament, and the word is used of rescue from drowning, healing from disease, and deliverance from sin and wrath alike. Its tenses are the subject of the next section.

**Eternal life** or **everlasting life** (the same Greek, **ζωὴ αἰώνιος**) appears in 37 verses of the KJV, nineteen of them in John's Gospel and First Epistle. In John it is a present possession: the believer *hath* it. The Free Grace argument rests almost entirely on this word: life that is eternal cannot end. The conditional reply is that *eternal* describes the life, not the believer's hold on it — the branch cut from the vine had the vine's life while it was in the vine.

**Perish, lose.** Greek **ἀπόλλυμι** (*apollymi*, G0622), "to destroy fully; reflexively, to perish, or lose." This is the word in John 3:16 (*should not perish*), John 10:28 (*shall never perish*), John 17:12 (*none of them is lost*), and Luke 15 (*was lost, and is found*). The same verb covers the sheep perishing and the shepherd losing it; the question is whether either can happen.

**Abide, continue, remain.** Greek **μένω** (*menō*, G3306), "to stay in a given place, state, relation." The word of John 15 (*abide in me*), of 1 John 2:19 (*they would no doubt have continued with us*), and of 2 Timothy 2:13 (*he abideth faithful*). John's Gospel uses it in 34 verses and his First Epistle in 18, which between them account for 64 of its 120 occurrences in the New Testament — more than half. That is one reason so much of this argument is conducted in John's vocabulary.

**Fall away, depart.** Greek **ἀφίστημι** (*aphistēmi*, G0868), "to remove; to desist, desert" — Luke 8:13 (*in time of temptation fall away*), 1 Timothy 4:1 (*some shall depart from the faith*), Hebrews 3:12 (*departing from the living God*). Its noun **ἀποστασία** (*apostasia*, G0646), "defection from truth," is the *falling away* of 2 Thessalonians 2:3 and the origin of the English *apostasy*. A different verb, **παραπίπτω** (*parapiptō*, G3895), "to fall aside, i.e. to apostatize," occurs once in the New Testament, at Hebrews 6:6. A third, **ἐκπίπτω** (*ekpiptō*, G1601), "to drop away, fall from," gives *ye are fallen from grace* in Galatians 5:4 and *fall from your own stedfastness* in 2 Peter 3:17. The KJV's phrase *fall away* occurs in only three verses (Luke 8:13; 2 Thessalonians 2:3; Hebrews 6:6).

**Shipwreck.** Greek **ναυαγέω** (*nauageō*, G3489), used literally of Paul's three shipwrecks (2 Corinthians 11:25) and figuratively once, of Hymenaeus and Alexander, who "concerning faith have made shipwreck" (1 Timothy 1:19).

**Castaway, reprobate.** Greek **ἀδόκιμος** (*adokimos*, G0096), "unapproved, rejected; worthless." Paul fears becoming one (1 Corinthians 9:27, *castaway*), tells the Corinthians to examine themselves lest they be ones (2 Corinthians 13:5, *reprobates*), and Hebrews 6:8 uses it of the ground that bears thorns (*rejected*).

**Endure.** Greek **ὑπομένω** (*hypomenō*, G5278), "to stay under; to bear trials, have fortitude, persevere." *He that endureth to the end shall be saved* occurs three times (Matthew 10:22; 24:13; Mark 13:13), and 2 Timothy 2:12 has *if we suffer* [endure], *we shall also reign with him*.

**Sealed; the earnest.** Greek **σφραγίζω** (*sphragizō*, G4972), "to stamp with a signet for security or preservation," and **ἀρραβών** (*arrabōn*, G0728), "a pledge; part of the purchase-money given in advance as security for the rest." Both are used of the Holy Spirit given to believers (2 Corinthians 1:22; Ephesians 1:13–14; 4:30).

**Keep.** Three Greek verbs. **τηρέω** (*tēreō*, G5083), "to guard from loss or injury by keeping the eye upon," is what Jesus did for the disciples (John 17:11–12), what God has done for Jude's readers (Jude 1:1, *preserved*), and what Jude tells them to do for themselves (Jude 1:21, *keep yourselves in the love of God*) — the same verb, twenty verses apart, with God and the believer each as subject. **φυλάσσω** (*phylassō*, G5442), "to watch, be on guard," is what Christ did for the disciples (John 17:12, *kept*) and what God is able to do for us (Jude 1:24, *to keep you from falling*). **φρουρέω** (*phroureō*, G5432), "to mount guard as a sentinel," is 1 Peter 1:5, *kept by the power of God*.

**Pluck.** Greek **ἁρπάζω** (*harpazō*, G0726), "to seize, take by force" — the verb of John 10:28–29 (*neither shall any man pluck them out of my hand*) and of 1 Thessalonians 4:17 (*caught up*).

**Blot out.** Greek **ἐξαλείφω** (*exaleiphō*, G1813), "to smear out, obliterate" — Revelation 3:5, *I will not blot out his name out of the book of life*. The *book of life* appears in eight verses of the KJV, all but one in Revelation.

**Backsliding.** An Old Testament word: the KJV has *backslider*, *backsliding*, or *backslidings* in sixteen verses, fifteen of them in Jeremiah and Hosea. It describes Israel turning from God and is always paired with a call to return, which is why Part III leans on it.

---

## Saved: past, present, and future

The New Testament uses *saved* of something that has happened, something that is happening, and something that will happen, and the three tenses are the first thing to fix, because the slogan "once saved" assumes salvation is a completed event and Scripture uses the word in more than one way.

> Ephesians 2:8 — For by grace are ye saved through faith; and that not of yourselves: it is the gift of God:

The Greek is a perfect participle, **σεσῳσμένοι** — "you are in the state of having been saved." Salvation as a completed act with continuing result.

> 1 Corinthians 1:18 — For the preaching of the cross is to them that perish foolishness; but unto us which are saved it is the power of God.

Here it is a present participle, **σῳζομένοις** — "those who are being saved," set against **ἀπολλυμένοις**, "those who are perishing." Salvation as a process under way, and perishing as a process too.

> Romans 5:9 — Much more then, being now justified by his blood, we shall be saved from wrath through him.

A future, **σωθησόμεθα**. Justification is past ("being now justified"); salvation from wrath is still ahead. So too Matthew 24:13, *he that shall endure unto the end, the same shall be saved*, and 1 Peter 1:5, *salvation ready to be revealed in the last time*.

All three positions accept all three tenses. Their disagreement is whether the past tense guarantees the future one — whether "having been saved" entails "shall be saved." Position B says yes, by the nature of the gift. Position A says yes, by the faithfulness of God who will complete the process. Position C says the future tense is future because it is not yet settled, and that the present tense — *being saved* — is exactly the state in which a person can stop.

**One grammatical point that both sides use.** The promises of John are made to *he that believeth*: John 3:16, 3:36, 5:24, 6:40, 6:47, 11:26. In every case the Greek is a present participle, **ὁ πιστεύων**, "the one believing." The conditional side reads the present tense as continuous: the promise attaches to the one who is, and goes on, believing. The Reformed side replies that the present participle with the article is Greek's ordinary way of saying "a believer," with no stress on continuity, and that in any case God sustains the believing. Both are right about the grammar, which is to say the grammar does not decide it. This document will not pretend otherwise, here or anywhere below.

---

## The Old Testament: a covenant with conditions, and a God who does not let go

The Old Testament does not ask the question in its New Testament form. It has no doctrine of regeneration to ask it about. But it supplies both sides with their oldest texts, and the two strands run side by side through the whole of it.

**The conditional strand.** The covenant with Israel is a covenant with conditions, and the conditions are stated with blessing on one side and cursing on the other.

> Deuteronomy 30:19–20 — I call heaven and earth to record this day against you, that I have set before you life and death, blessing and cursing: therefore choose life, that both thou and thy seed may live: That thou mayest love the LORD thy God, and that thou mayest obey his voice, and that thou mayest cleave unto him: for he is thy life, and the length of thy days: that thou mayest dwell in the land which the LORD sware unto thy fathers, to Abraham, to Isaac, and to Jacob, to give them.

> 2 Chronicles 15:2 — And he went out to meet Asa, and said unto him, Hear ye me, Asa, and all Judah and Benjamin; The LORD is with you, while ye be with him; and if ye seek him, he will be found of you; but if ye forsake him, he will forsake you.

The book of God's people can be written in and blotted out of:

> Exodus 32:32–33 — Yet now, if thou wilt forgive their sin--; and if not, blot me, I pray thee, out of thy book which thou hast written. And the LORD said unto Moses, Whosoever hath sinned against me, him will I blot out of my book.

> Psalms 69:28 — Let them be blotted out of the book of the living, and not be written with the righteous.

**The unconditional strand.** Alongside the conditions runs a set of promises in which God undertakes not merely to reward faithfulness but to *produce* it. The covenant with David is the pattern: his sons may sin and be chastened, and the covenant holds.

> Psalms 89:30–34 — If his children forsake my law, and walk not in my judgments; If they break my statutes, and keep not my commandments; Then will I visit their transgression with the rod, and their iniquity with stripes. Nevertheless my lovingkindness will I not utterly take from him, nor suffer my faithfulness to fail. My covenant will I not break, nor alter the thing that is gone out of my lips.

The Reformed side's Old Testament text above all others is the new covenant of Jeremiah and Ezekiel, in which God promises not only to forgive his people but to keep them from departing:

> Jeremiah 32:40 — And I will make an everlasting covenant with them, that I will not turn away from them, to do them good; but I will put my fear in their hearts, that they shall not depart from me.

> Ezekiel 36:26–27 — A new heart also will I give you, and a new spirit will I put within you: and I will take away the stony heart out of your flesh, and I will give you an heart of flesh. And I will put my spirit within you, and cause you to walk in my statutes, and ye shall keep my judgments, and do them.

> Jeremiah 24:7 — And I will give them an heart to know me, that I am the LORD: and they shall be my people, and I will be their God: for they shall return unto me with their whole heart.

*Cause you to walk*; *that they shall not depart*. If the new covenant is God's promise to produce the perseverance he requires, the argument runs, then the requirement is not in doubt for those in the covenant. The conditional reply is that these promises are to the people as a whole, that the same prophets warn individuals within that people (Ezekiel 18, below), and that "I will put my fear in their hearts" describes what God does for those who walk with him, not a guarantee against their walking away.

Then there are the psalms of preservation, which both sides sing:

> Psalms 37:23–24 — The steps of a good man are ordered by the LORD: and he delighteth in his way. Though he fall, he shall not be utterly cast down: for the LORD upholdeth him with his hand.

> Psalms 37:28 — For the LORD loveth judgment, and forsaketh not his saints; they are preserved for ever: but the seed of the wicked shall be cut off.

> Psalms 94:14 — For the LORD will not cast off his people, neither will he forsake his inheritance.

> Psalms 138:8 — The LORD will perfect that which concerneth me: thy mercy, O LORD, endureth for ever: forsake not the works of thine own hands.

> Isaiah 54:10 — For the mountains shall depart, and the hills be removed; but my kindness shall not depart from thee, neither shall the covenant of my peace be removed, saith the LORD that hath mercy on thee.

> Proverbs 24:16 — For a just man falleth seven times, and riseth up again: but the wicked shall fall into mischief.

> Job 17:9 — The righteous also shall hold on his way, and he that hath clean hands shall be stronger and stronger.

*Though he fall, he shall not be utterly cast down.* Every tradition takes this to describe the true believer's experience of sin: falls, not final falls. The question is whether "he shall not be utterly cast down" is a promise about every believer or a description of the righteous, and Proverbs 24:16 shows how the two readings sit in one verse: the just man rises again — and the reason he is called just is that he rises.

**The call to return.** The Old Testament's most characteristic word on the subject is neither strand but a summons. Israel is a *backsliding* people, and God does not say the backslider was never his; he says come back.

> Jeremiah 3:22 — Return, ye backsliding children, and I will heal your backslidings. Behold, we come unto thee; for thou art the LORD our God.

> Hosea 14:4 — I will heal their backsliding, I will love them freely: for mine anger is turned away from him.

> Malachi 3:7 — Even from the days of your fathers ye are gone away from mine ordinances, and have not kept them. Return unto me, and I will return unto you, saith the LORD of hosts. But ye said, Wherein shall we return?

Whatever one decides about the man who never returns, the Old Testament's counsel to the one who has gone away is the same on every view of the doctrine, and it is Part III's.

---

## Saul, David, and Solomon

Three kings, and the Old Testament's three case studies.

**Saul** is the one the conditional side reaches for. God gave him his Spirit and a new heart, and at the end God had left him.

> 1 Samuel 10:6 — And the Spirit of the LORD will come upon thee, and thou shalt prophesy with them, and shalt be turned into another man.

> 1 Samuel 10:9 — And it was so, that when he had turned his back to go from Samuel, God gave him another heart: and all those signs came to pass that day.

> 1 Samuel 16:14 — But the Spirit of the LORD departed from Saul, and an evil spirit from the LORD troubled him.

> 1 Samuel 28:16 — Then said Samuel, Wherefore then dost thou ask of me, seeing the LORD is departed from thee, and is become thine enemy?

A man given "another heart" by God, who ends as God's enemy. The Reformed reply is that the Spirit's coming on Saul was the Spirit's equipping for kingship, as on Samson, on Balaam, and on the seventy elders — a gift of office, not the new birth — and that Saul's heart is never described as David's is. The conditional side answers that "another heart" is stronger language than office, and that the text gives no hint Saul's beginning was false. What both sides agree Saul teaches is that a good beginning guarantees nothing about the end, and that is a lesson for the reader whichever doctrine is true.

**David** is the one the Reformed side reaches for, and Dort names him. After adultery and murder, he prays:

> Psalms 51:11–12 — Cast me not away from thy presence; and take not thy holy spirit from me. Restore unto me the joy of thy salvation; and uphold me with thy free spirit.

The conditional side reads this as a regenerate man who knows the Spirit can be taken, praying against it. The Reformed side reads it as a man who had watched it happen to Saul, praying with Saul in view, and notes that David's faith did not fail through the whole episode: he does not pray to be converted again but to have his *joy* restored. Dort's Fifth Head (Article 4) takes David and Peter as the two cases of a saint's "melancholy fall" — grievous sin, loss of the *sense* of God's favour for a time, and restoration — and holds that this, not final apostasy, is what befalls the elect.

**Solomon** is the case the Bible leaves unresolved, and it is worth noticing that it does.

> 1 Kings 11:4 — For it came to pass, when Solomon was old, that his wives turned away his heart after other gods: and his heart was not perfect with the LORD his God, as was the heart of David his father.

> 1 Kings 11:9 — And the LORD was angry with Solomon, because his heart was turned from the LORD God of Israel, which had appeared unto him twice,

A man to whom God appeared twice, whose heart turned from God in old age. Kings never tells us whether he turned back. Some read Ecclesiastes as his repentance; the text of Kings does not say so, and it does not say the opposite. The Bible records the fall and withholds the verdict, and it will do the same with Demas.

---

## Ezekiel's righteous man

The conditional side's Old Testament text above all others, quoted by Wesley as his first proof and by the Council of Trent before him.

> Ezekiel 18:24 — But when the righteous turneth away from his righteousness, and committeth iniquity, and doeth according to all the abominations that the wicked man doeth, shall he live? All his righteousness that he hath done shall not be mentioned: in his trespass that he hath trespassed, and in his sin that he hath sinned, in them shall he die.

> Ezekiel 33:12–13 — Therefore, thou son of man, say unto the children of thy people, The righteousness of the righteous shall not deliver him in the day of his transgression: as for the wickedness of the wicked, he shall not fall thereby in the day that he turneth from his wickedness; neither shall the righteous be able to live for his righteousness in the day that he sinneth. When I shall say to the righteous, that he shall surely live; if he trust to his own righteousness, and commit iniquity, all his righteousnesses shall not be remembered; but for his iniquity that he hath committed, he shall die for it.

> Ezekiel 3:20 — Again, When a righteous man doth turn from his righteousness, and commit iniquity, and I lay a stumbling-block before him, he shall die: because thou hast not given him warning, he shall die in his sin, and his righteousness which he hath done shall not be remembered; but his blood will I require at thine hand.

The passage is symmetrical. The same chapter says the wicked man who turns from his sin *shall surely live* and none of his transgressions will be mentioned (Ezekiel 18:21–22), and ends with the plea *turn yourselves, and live ye* (18:32). God judges a person by where they end, not where they began, in both directions.

**What it shows.** That a man God himself calls *righteous* can turn, and that if he does, his past righteousness counts for nothing. Ezekiel does not say the man was never righteous. He says he *turned*.

**What the Reformed side says.** That Ezekiel is speaking of righteousness in the covenant community and of life and death in the land under the covenant's sanctions, not of regeneration and eternal life; that "the righteous" is the man righteous in conduct, whom the Old Testament can call righteous without any claim about his heart; and that the principle — the end is what counts — is one the Reformed hold as firmly as anyone, since on their view the end *reveals* what a person was.

**A fair reading.** Ezekiel does not have the New Testament's categories and cannot be made to answer a question about the new birth. But the passage does establish something all three positions have to accommodate: God does not credit a person at the judgment for a righteousness they abandoned. Position A accommodates it by saying the abandonment shows the righteousness was not from God. Position C accommodates it by taking it as it stands. Position B has the hardest time with it, and its writers generally confine Ezekiel to the temporal life of Israel.

---

## Israel in the wilderness: the New Testament's own example

When the New Testament wants a picture of people who began with God and did not arrive, it reaches for the exodus generation, four times.

> Psalms 95:7–8 — For he is our God; and we are the people of his pasture, and the sheep of his hand. To day if ye will hear his voice, Harden not your heart, as in the provocation, and as in the day of temptation in the wilderness:

> 1 Corinthians 10:1–6 — Moreover, brethren, I would not that ye should be ignorant, how that all our fathers were under the cloud, and all passed through the sea; And were all baptized unto Moses in the cloud and in the sea; And did all eat the same spiritual meat; And did all drink the same spiritual drink: for they drank of that spiritual Rock that followed them: and that Rock was Christ. But with many of them God was not well pleased: for they were overthrown in the wilderness. Now these things were our examples, to the intent we should not lust after evil things, as they also lusted.

> 1 Corinthians 10:11–12 — Now all these things happened unto them for ensamples: and they are written for our admonition, upon whom the ends of the world are come. Wherefore let him that thinketh he standeth take heed lest he fall.

> Jude 1:5 — I will therefore put you in remembrance, though ye once knew this, how that the Lord, having saved the people out of the land of Egypt, afterward destroyed them that believed not.

> Hebrews 4:1 — Let us therefore fear, lest, a promise being left us of entering into his rest, any of you should seem to come short of it.

> Hebrews 4:11 — Let us labour therefore to enter into that rest, lest any man fall after the same example of unbelief.

*All* were baptised, *all* ate, *all* drank of Christ — and most died in the desert. Jude says it in the sharpest form: *the Lord, having saved the people … afterward destroyed them that believed not.* Saved, then destroyed. The conditional side takes this as the New Testament's own model of apostasy, deliberately applied to the church: *these things were our examples*.

The Reformed side reads the same texts and points to the last clause of each. Those who fell "believed not" (Jude 1:5); the word "did not profit them, not being mixed with faith" (Hebrews 4:2); they "could not enter in because of unbelief" (Hebrews 3:19). Israel was *saved* from Egypt as a nation, outwardly, by the same water that drowned Pharaoh; that did not make each Israelite a believer, and it was the unbelievers who fell. The wilderness generation is, on this reading, the Old Testament's picture of the mixed visible church: everyone shares the sacraments and only some have faith.

Both readings are possible. What is not possible is to read these passages as saying nothing to Christians, since Paul says in so many words that they were written for us. Whatever the exodus generation was, the apostles held it up to the church as a warning about ending where you did not intend to.

---

## Texts cited for security

The passages most often brought forward for Position A, Position B, or both, each with the reading it is given and the rejoinder it receives. The texts are grouped, and the strongest come first.

**1. The sheep who shall never perish (John 10:27–30).**

> John 10:27–30 — My sheep hear my voice, and I know them, and they follow me: And I give unto them eternal life; and they shall never perish, neither shall any man pluck them out of my hand. My Father, which gave them me, is greater than all; and no man is able to pluck them out of my Father's hand. I and my Father are one.

The strongest single text for security. The Greek of *they shall never perish* is **οὐ μὴ ἀπόλωνται**, the emphatic double negative, "they shall by no means ever perish," and *pluck* is **ἁρπάζω**, to seize by force. The security of the sheep is tied not to their grip but to the Father, "greater than all." Calvin's whole doctrine can be drawn from this passage and he drew it.

The rejoinder is in two parts. First, the sheep are defined in verse 27 by three present-tense verbs — they *hear*, are *known*, and *follow* — so the promise is made to those doing these things. Second, the promise is that no one can *snatch* them; it says nothing about a sheep wandering off, and Scripture is full of sheep that go astray (Isaiah 53:6; 1 Peter 2:25). The Reformed answer is that "shall never perish" is unconditional and is said of the sheep as such, that a sheep that perished by wandering would have perished, which Jesus says cannot happen, and that the wandering-sheep rejoinder makes the promise depend on exactly the thing the passage says does not matter: the sheep's own strength.

**2. All that the Father gives (John 6:37–40, 44).**

> John 6:37–40 — All that the Father giveth me shall come to me; and him that cometh to me I will in no wise cast out. For I came down from heaven, not to do mine own will, but the will of him that sent me. And this is the Father's will which hath sent me, that of all which he hath given me I should lose nothing, but should raise it up again at the last day. And this is the will of him that sent me, that every one which seeth the Son, and believeth on him, may have everlasting life: and I will raise him up at the last day.

> John 6:44 — No man can come to me, except the Father which hath sent me draw him: and I will raise him up at the last day.

*I will in no wise cast out* is again the emphatic **οὐ μὴ ἐκβάλω ἔξω**. The Father gives; the given come; the Son loses none of them and raises them up. The chain runs from the Father's gift to the last day without a break, and the Son's own obedience to the Father's will is what guarantees it.

The rejoinder: verse 40 states the condition — *every one which seeth the Son, and believeth on him* — in the present tense; the promise not to cast out is a promise about Christ's welcome, not about the believer's staying; and the same chapter ends with many disciples going back (verses 66–71, below). The Reformed reply is that those who went back are precisely the ones Jesus said had not been given (6:64–65: "there are some of you that believe not … therefore said I unto you, that no man can come unto me, except it were given unto him of my Father").

**3. Everlasting life as a present possession (John 3:16, 36; 5:24; 6:47; 11:25–26; 1 John 5:11–13).**

> John 5:24 — Verily, verily, I say unto you, He that heareth my word, and believeth on him that sent me, hath everlasting life, and shall not come into condemnation; but is passed from death unto life.

> John 11:25–26 — Jesus said unto her, I am the resurrection, and the life: he that believeth in me, though he were dead, yet shall he live: And whosoever liveth and believeth in me shall never die. Believest thou this?

> 1 John 5:11–13 — And this is the record, that God hath given to us eternal life, and this life is in his Son. He that hath the Son hath life; and he that hath not the Son of God hath not life. These things have I written unto you that believe on the name of the Son of God; that ye may know that ye have eternal life, and that ye may believe on the name of the Son of God.

The believer *hath* everlasting life now, *shall not come into condemnation*, and *is passed* (a perfect tense: has crossed over) from death to life. This is the heart of Position B's case, and its writers press it hard: if this life could be lost, it was not eternal, and if the believer could come into condemnation, "shall not come into condemnation" was false. First John was written so that believers *may know* they have it.

The rejoinder from both A and C is that all of these are said of *the one believing*, and that John's own Gospel says a branch *in me* can be cut off and burned (15:6). Eternal life is the life of God shared with the believer; the question is not whether the life is eternal but whether the sharing is. And 1 John 5:13 sits in a letter whose tests of life — keeping the commandments, loving the brethren, not continuing in sin — are what Part III is built on.

**4. Nothing shall separate (Romans 8:28–39).**

> Romans 8:28–30 — And we know that all things work together for good to them that love God, to them who are the called according to his purpose. For whom he did foreknow, he also did predestinate to be conformed to the image of his Son, that he might be the firstborn among many brethren. Moreover whom he did predestinate, them he also called: and whom he called, them he also justified: and whom he justified, them he also glorified.

> Romans 8:33–34 — Who shall lay any thing to the charge of God's elect? It is God that justifieth. Who is he that condemneth? It is Christ that died, yea rather, that is risen again, who is even at the right hand of God, who also maketh intercession for us.

> Romans 8:35–39 — Who shall separate us from the love of Christ? shall tribulation, or distress, or persecution, or famine, or nakedness, or peril, or sword? As it is written, For thy sake we are killed all the day long; we are accounted as sheep for the slaughter. Nay, in all these things we are more than conquerors through him that loved us. For I am persuaded, that neither death, nor life, nor angels, nor principalities, nor powers, nor things present, nor things to come, Nor height, nor depth, nor any other creature, shall be able to separate us from the love of God, which is in Christ Jesus our Lord.

The "golden chain" of verse 30 is the Reformed side's Pauline text: foreknown, predestinated, called, justified, *glorified*, all in the same tense (the Greek aorist, **ἐδόξασεν**), as if the last were as done as the first, and the same "them" at every link. No one drops out between justified and glorified. Then verses 35–39: nothing in creation can separate. The conditional reply is that Paul's list is a list of *external* things — death, life, angels, powers, height, depth — and does not include the believer's own unbelief; the believer is not separated *by* anything, but may separate *himself*. The Reformed answer that *nor any other creature* (**κτίσις ἑτέρα**, "any other created thing") includes the believer, who is a creature; that Paul's point is the impossibility of separation as such; and that verse 13 of the same chapter ("if ye live after the flesh, ye shall die") is the warning by which the elect are kept from living so.

**5. The gifts and calling of God (Romans 11:29).**

> Romans 11:29 — For the gifts and calling of God are without repentance.

*Without repentance* means irrevocable: God does not take back what he gives or un-call whom he calls. The verse is about God's election of Israel, which Paul says survives their present unbelief. The conditional side notes that the same chapter, nine verses earlier, tells the Gentile believer *thou standest by faith … if thou continue in his goodness: otherwise thou also shalt be cut off* (11:20–22, below). God's gifts are irrevocable; the branch can still be cut.

**6. Sealed, and given the earnest (Ephesians 1:13–14; 4:30; 2 Corinthians 1:21–22; 5:5).**

> Ephesians 1:13–14 — In whom ye also trusted, after that ye heard the word of truth, the gospel of your salvation: in whom also after that ye believed, ye were sealed with that holy Spirit of promise, Which is the earnest of our inheritance until the redemption of the purchased possession, unto the praise of his glory.

> Ephesians 4:30 — And grieve not the holy Spirit of God, whereby ye are sealed unto the day of redemption.

> 2 Corinthians 1:21–22 — Now he which stablisheth us with you in Christ, and hath anointed us, is God; Who hath also sealed us, and given the earnest of the Spirit in our hearts.

A seal marks ownership and secures the thing sealed *unto the day of redemption*; an earnest is a deposit that binds the payer to the rest. The Spirit is both. The rejoinder is that a seal is a mark, not a chain — and that Ephesians 4:30 warns the sealed not to grieve the Spirit, while 5:5–6 tells them that no covetous person has any inheritance in the kingdom. The Reformed reply that a seal set by God is not one man breaks, and that warnings to the sealed are the ordinary means by which the sealed are kept.

**7. He who began will finish (Philippians 1:6; 1 Corinthians 1:8–9; 1 Thessalonians 5:23–24; 2 Thessalonians 3:3; 2 Timothy 1:12; 4:18; Jude 1:24–25).**

> Philippians 1:6 — Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ:

> 1 Corinthians 1:8–9 — Who shall also confirm you unto the end, that ye may be blameless in the day of our Lord Jesus Christ. God is faithful, by whom ye were called unto the fellowship of his Son Jesus Christ our Lord.

> 1 Thessalonians 5:23–24 — And the very God of peace sanctify you wholly; and I pray God your whole spirit and soul and body be preserved blameless unto the coming of our Lord Jesus Christ. Faithful is he that calleth you, who also will do it.

> 2 Timothy 1:12 — For the which cause I also suffer these things: nevertheless I am not ashamed: for I know whom I have believed, and am persuaded that he is able to keep that which I have committed unto him against that day.

> Jude 1:24–25 — Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory with exceeding joy, To the only wise God our Saviour, be glory and majesty, dominion and power, both now and ever. Amen.

The work is God's from beginning to end; he is faithful; he *will do it*. The conditional side does not dispute a word of it. God's faithfulness was never the question; the believer's was. Paul, who wrote Philippians 1:6 about a church that had "always obeyed" (2:12), also wrote *I keep under my body … lest … I myself should be a castaway* (1 Corinthians 9:27), and Jude, who wrote that God is able to keep you from falling, wrote three verses earlier *keep yourselves in the love of God*. The Reformed reply is that "able" is Jude's modesty of doxology, not a hedge, and that Paul's confidence is stated as confidence about *God's* performance, which does not fail.

**8. Kept by the power of God (1 Peter 1:3–5, 23).**

> 1 Peter 1:3–5 — Blessed be the God and Father of our Lord Jesus Christ, which according to his abundant mercy hath begotten us again unto a lively hope by the resurrection of Jesus Christ from the dead, To an inheritance incorruptible, and undefiled, and that fadeth not away, reserved in heaven for you, Who are kept by the power of God through faith unto salvation ready to be revealed in the last time.

> 1 Peter 1:23 — Being born again, not of corruptible seed, but of incorruptible, by the word of God, which liveth and abideth for ever.

*Kept* is **φρουρέω**, garrisoned. The inheritance is reserved in heaven and the heirs are guarded on earth, and the new birth is of *incorruptible* seed — a birth, the Reformed say, cannot be undone. The conditional reading fastens on two words: *through faith*. The keeping is God's; the channel is faith; and faith is the one thing Scripture says a person can put away (1 Timothy 1:19). The Reformed answer that God keeps *by* sustaining the faith, so that "through faith" names the means of the keeping, not a condition that may fail.

**9. They were not of us (1 John 2:19).**

> 1 John 2:19 — They went out from us, but they were not of us; for if they had been of us, they would no doubt have continued with us: but they went out, that they might be made manifest that they were not all of us.

The Reformed key to every apostasy in Scripture. Those who leave were never truly of the body; their leaving does not change what they were but *reveals* it. The verb *continued* is **μένω**, and it is in the pluperfect: "they would have remained." The conditional side observes that John is speaking of a specific group — the "antichrists" of verse 18, false teachers who denied that Jesus is the Christ — and that he does not say every departure is of this kind; and that the same letter says *abide in him* (2:28) and *keep yourselves from idols* (5:21), which would be strange counsel if abiding were automatic. The Reformed reply that John's reasoning is general in form — *if they had been of us, they would have continued* — and applies to anyone who does not continue.

**10. Born of God (1 John 3:9; 5:4, 18).**

> 1 John 3:9 — Whosoever is born of God doth not commit sin; for his seed remaineth in him: and he cannot sin, because he is born of God.

> 1 John 5:18 — We know that whosoever is born of God sinneth not; but he that is begotten of God keepeth himself, and that wicked one toucheth him not.

The verbs are present: the one born of God does not *go on* sinning, cannot *keep on* sinning, because God's seed *remains* in him. On the Reformed reading this is the new birth described as a permanent change of nature. The conditional side largely agrees with the description and observes that John's own words include *keepeth himself* — the regenerate person is described as one who does not continue in sin, which is exactly what is in question about the man who does.

**11. The finished work (Hebrews 7:25; 9:12; 10:14; 13:5).**

> Hebrews 7:25 — Wherefore he is able also to save them to the uttermost that come unto God by him, seeing he ever liveth to make intercession for them.

> Hebrews 10:14 — For by one offering he hath perfected for ever them that are sanctified.

> Hebrews 13:5 — Let your conversation be without covetousness; and be content with such things as ye have: for he hath said, I will never leave thee, nor forsake thee.

Christ saves *to the uttermost* — completely and to the end — because he *ever liveth to make intercession*; his one offering has *perfected for ever* those it sanctifies; God will never leave. The conditional side accepts every word and notes only that these promises stand in the book with the New Testament's sternest warnings, addressed to the same readers: *them that come unto God by him* and *them that are sanctified* are the people Hebrews 10:26–29 warns.

**12. Christ's prayer (Luke 22:31–32; John 17:11–12, 15; Romans 8:34).**

> Luke 22:31–32 — And the Lord said, Simon, Simon, behold, Satan hath desired to have you, that he may sift you as wheat: But I have prayed for thee, that thy faith fail not: and when thou art converted, strengthen thy brethren.

> John 17:11–12 — And now I am no more in the world, but these are in the world, and I come to thee. Holy Father, keep through thine own name those whom thou hast given me, that they may be one, as we are. While I was with them in the world, I kept them in thy name: those that thou gavest me I have kept, and none of them is lost, but the son of perdition; that the scripture might be fulfilled.

Peter's faith failed in act and did not fail in fact, because Jesus prayed. The Reformed read the intercession of Christ (Romans 8:34; Hebrews 7:25) as the guarantee that the same is true of every believer: Christ prays for his own, and the Father hears him. The conditional side notes the clause in John 17:12: *none of them is lost, but the son of perdition*. Judas is discussed below.

**13. "If it were possible" (Matthew 24:24).**

> Matthew 24:24 — For there shall arise false Christs, and false prophets, and shall shew great signs and wonders; insomuch that, if it were possible, they shall deceive the very elect.

The Reformed read *if it were possible* as saying it is not. The conditional side reads it as saying the danger is real enough to warn against, and observes that the Greek is simply **εἰ δυνατόν**, "if possible," which in ordinary use (Romans 12:18, "if it be possible, as much as lieth in you") does not assert impossibility.

**14. "If we believe not, yet he abideth faithful" (2 Timothy 2:11–13).**

> 2 Timothy 2:11–13 — It is a faithful saying: For if we be dead with him, we shall also live with him: If we suffer, we shall also reign with him: if we deny him, he also will deny us: If we believe not, yet he abideth faithful: he cannot deny himself.

Position B's text: even when we are faithless, God remains faithful to us. Both A and C read the saying as a whole, and its third line is *if we deny him, he also will deny us*. God's faithfulness includes faithfulness to his own word, threats included; *he cannot deny himself* means he cannot be other than he has said he is, and he has said he will deny those who deny him.

**15. "Saved; yet so as by fire" (1 Corinthians 3:11–15).**

> 1 Corinthians 3:11–15 — For other foundation can no man lay than that is laid, which is Jesus Christ. Now if any man build upon this foundation gold, silver, precious stones, wood, hay, stubble; Every man's work shall be made manifest: for the day shall declare it, because it shall be revealed by fire; and the fire shall try every man's work of what sort it is. If any man's work abide which he hath built thereupon, he shall receive a reward. If any man's work shall be burned, he shall suffer loss: but he himself shall be saved; yet so as by fire.

Position B's other text: a man whose whole life's work burns is nonetheless saved. All three positions agree that this passage distinguishes a believer's salvation from the judgment of their works, and that a Christian can be saved with nothing to show. What A and C deny is that this describes the apostate. The passage is about builders — teachers whose work on the foundation is poor — not about people who leave the foundation, and Paul goes on in the same letter to say that the unrighteous *shall not inherit the kingdom* (6:9–10).

**16. "Much more" (Romans 5:8–10).**

> Romans 5:8–10 — But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us. Much more then, being now justified by his blood, we shall be saved from wrath through him. For if, when we were enemies, we were reconciled to God by the death of his Son, much more, being reconciled, we shall be saved by his life.

If God did the harder thing for his enemies, he will do the easier thing for his friends. The argument is from the greater to the lesser, and it is a strong one for the reliability of God. The conditional side accepts it as an argument about God and observes that "being reconciled" is the state in which Paul elsewhere tells people to *be ye reconciled* (2 Corinthians 5:20) and not to *receive the grace of God in vain* (6:1).

---

## Texts cited for the possibility of falling

The passages most often brought forward for Position C, each with the reading it is given and the answer it receives from A (and, where it differs, from B). Hebrews has its own section after this one.

**1. The seed on the rock (Luke 8:11–15; Matthew 13:18–23; Mark 4:16–17).**

> Luke 8:13 — They on the rock are they, which, when they hear, receive the word with joy; and these have no root, which for a while believe, and in time of temptation fall away.

> Matthew 13:20–21 — But he that received the seed into stony places, the same is he that heareth the word, and anon with joy receiveth it; Yet hath he not root in himself, but dureth for a while: for when tribulation or persecution ariseth because of the word, by and by he is offended.

Luke's account is the sharpest: *for a while believe, and in time of temptation fall away* — **πιστεύουσιν … ἀφίστανται**. Jesus says they *believe*, and does not say the belief was counterfeit; he says it did not last. The Reformed reading rests on *no root*: the plant that has no root was never truly alive at the root, whatever showed above ground, and Jesus contrasts it with the good ground that *keeps* the word and brings forth fruit *with patience* (8:15) — endurance being the mark of the good soil. Calvin conceded that the rocky-ground hearer has a real experience, which he called temporary faith, and held that it is not the faith of the elect. The conditional side asks why, if the belief was of a different kind, Jesus used the same word.

**2. The branch that is cut off and burned (John 15:1–6).**

> John 15:1–6 — I am the true vine, and my Father is the husbandman. Every branch in me that beareth not fruit he taketh away: and every branch that beareth fruit, he purgeth it, that it may bring forth more fruit. Now ye are clean through the word which I have spoken unto you. Abide in me, and I in you. As the branch cannot bear fruit of itself, except it abide in the vine; no more can ye, except ye abide in me. I am the vine, ye are the branches: He that abideth in me, and I in him, the same bringeth forth much fruit: for without me ye can do nothing. If a man abide not in me, he is cast forth as a branch, and is withered; and men gather them, and cast them into the fire, and they are burned.

The conditional side's text from John, and it is in the same Gospel as the sheep and the Father's gift. The branch is *in me*; it is taken away; the one who does not abide is *cast forth … and burned*. Jesus tells the eleven — Judas has already gone out (13:30) — *abide in me*, which presupposes that not abiding is possible for them.

The Reformed reading is that "in me" describes the branch's *attachment* as seen from outside — membership of the visible people of Christ, as Judas was one of the twelve — and that the fruitless branch never had the vine's life, fruit being the evidence of life. The command to abide is a command by which God keeps his own abiding. Position B reads the fire as loss of reward or usefulness rather than of salvation. The conditional side answers that a branch that was never in the vine cannot be *cast forth* from it, and that in John's Gospel fire is not a metaphor for lost reward.

**3. He that endureth to the end (Matthew 10:22; 24:10–13; Mark 13:13).**

> Matthew 24:10–13 — And then shall many be offended, and shall betray one another, and shall hate one another. And many false prophets shall rise, and shall deceive many. And because iniquity shall abound, the love of many shall wax cold. But he that shall endure unto the end, the same shall be saved.

Salvation is future and conditioned on endurance, and the context is a description of many whose love *waxes cold*. The Reformed accept the condition and say the elect will meet it: endurance to the end is the mark of the saved, so the sentence describes rather than threatens. The conditional side says a description that is stated as a condition ("he that shall endure … shall be saved") is a condition.

**4. The branches broken off (Romans 11:17–23).**

> Romans 11:17–23 — And if some of the branches be broken off, and thou, being a wild olive tree, wert graffed in among them, and with them partakest of the root and fatness of the olive tree; Boast not against the branches. But if thou boast, thou bearest not the root, but the root thee. Thou wilt say then, The branches were broken off, that I might be graffed in. Well; because of unbelief they were broken off, and thou standest by faith. Be not highminded, but fear: For if God spared not the natural branches, take heed lest he also spare not thee. Behold therefore the goodness and severity of God: on them which fell, severity; but toward thee, goodness, if thou continue in his goodness: otherwise thou also shalt be cut off. And they also, if they abide not still in unbelief, shall be graffed in: for God is able to graff them in again.

The Gentile believer is grafted in, *partakes of the root*, *stands by faith*, and is told: *if thou continue … otherwise thou also shalt be cut off*. The natural branches were *in* the tree and were broken off *because of unbelief*. The Reformed read the passage as corporate — the Gentiles as a body and Israel as a body, the olive tree being the covenant people in history rather than the roll of the elect — so that being cut off is a nation's loss of place, not an individual's loss of salvation. The conditional side points out that *thou* is singular throughout, that the cutting off is *because of unbelief*, and that the passage ends with the possibility of grafting back in: a cut-off branch is not described as one that was never alive.

**5. If ye live after the flesh (Romans 8:12–13; Galatians 5:19–21; 6:7–9; 1 Corinthians 6:9–10; Ephesians 5:5–6).**

> Romans 8:12–13 — Therefore, brethren, we are debtors, not to the flesh, to live after the flesh. For if ye live after the flesh, ye shall die: but if ye through the Spirit do mortify the deeds of the body, ye shall live.

> Galatians 6:7–9 — Be not deceived; God is not mocked: for whatsoever a man soweth, that shall he also reap. For he that soweth to his flesh shall of the flesh reap corruption; but he that soweth to the Spirit shall of the Spirit reap life everlasting. And let us not be weary in well doing: for in due season we shall reap, if we faint not.

> 1 Corinthians 6:9–10 — Know ye not that the unrighteous shall not inherit the kingdom of God? Be not deceived: neither fornicators, nor idolaters, nor adulterers, nor effeminate, nor abusers of themselves with mankind, Nor thieves, nor covetous, nor drunkards, nor revilers, nor extortioners, shall inherit the kingdom of God.

*Brethren … if ye live after the flesh, ye shall die.* These are addressed to Christians and say that a life of sin ends in death and exclusion from the kingdom. The Reformed agree entirely: those who are Christ's *have crucified the flesh* (Galatians 5:24), and the warning is the means by which they go on doing so; the person who lives after the flesh to the end shows he was never Christ's. Position B alone reads *die*, *corruption*, and *not inherit* as loss of reward and of the fulness of life rather than of salvation, and here A and C stand together against B: *be not deceived* is a strange way to introduce a warning about diminished reward.

**6. Lest I myself should be a castaway (1 Corinthians 9:24–27).**

> 1 Corinthians 9:24–27 — Know ye not that they which run in a race run all, but one receiveth the prize? So run, that ye may obtain. And every man that striveth for the mastery is temperate in all things. Now they do it to obtain a corruptible crown; but we an incorruptible. I therefore so run, not as uncertainly; so fight I, not as one that beateth the air: But I keep under my body, and bring it into subjection: lest that by any means, when I have preached to others, I myself should be a castaway.

*Castaway* is **ἀδόκιμος** — rejected, disqualified, the word rendered *reprobate* elsewhere. Paul thought it possible for himself. The Reformed read the race as the Christian's service and the disqualification as loss of the prize (reward) or of usefulness, not of salvation, and note that the next chapter ends with God's faithfulness (10:13). The conditional side notes that the word is Paul's ordinary word for the reprobate (Romans 1:28; 2 Corinthians 13:5; Titus 1:16) and that the chapter following is the wilderness generation, *overthrown*.

**7. If ye continue (1 Corinthians 15:1–2; Colossians 1:21–23).**

> 1 Corinthians 15:1–2 — Moreover, brethren, I declare unto you the gospel which I preached unto you, which also ye have received, and wherein ye stand; By which also ye are saved, if ye keep in memory what I preached unto you, unless ye have believed in vain.

> Colossians 1:21–23 — And you, that were sometime alienated and enemies in your mind by wicked works, yet now hath he reconciled In the body of his flesh through death, to present you holy and unblameable and unreproveable in his sight: If ye continue in the faith grounded and settled, and be not moved away from the hope of the gospel, which ye have heard, and which was preached to every creature which is under heaven; whereof I Paul am made a minister;

*Ye are saved, if ye keep in memory* [hold fast]; *reconciled … to present you holy … if ye continue in the faith*. The Greek of Colossians is **εἴ γε ἐπιμένετε**, "if indeed you continue." The conditional side takes the *if* as an *if*. The Reformed take it as evidential: continuing is the evidence that the reconciliation was real, in the way that Hebrews 3:14 says *we are made partakers of Christ, if we hold the beginning of our confidence stedfast unto the end* — where *are made* is a perfect tense (**γεγόναμεν**, "we have become"), so that a present holding fast demonstrates a past becoming. The conditional side replies that the same grammar reads just as naturally the other way: the having-become continues only while the holding continues.

**8. Fallen from grace (Galatians 1:6; 3:3–4; 5:1–4, 7).**

> Galatians 5:1–4 — Stand fast therefore in the liberty wherewith Christ hath made us free, and be not entangled again with the yoke of bondage. Behold, I Paul say unto you, that if ye be circumcised, Christ shall profit you nothing. For I testify again to every man that is circumcised, that he is a debtor to do the whole law. Christ is become of no effect unto you, whosoever of you are justified by the law; ye are fallen from grace.

> Galatians 5:7 — Ye did run well; who did hinder you that ye should not obey the truth?

> Galatians 3:3–4 — Are ye so foolish? having begun in the Spirit, are ye now made perfect by the flesh? Have ye suffered so many things in vain? if it be yet in vain.

People who *began in the Spirit* and *ran well* are told that Christ will *profit them nothing* and that they are *fallen from grace* (**ἐξεπέσατε**). The Reformed read "fallen from grace" as fallen from the doctrine of grace into law — a serious error, not a lost salvation — and observe that Paul still calls them brethren and expects their recovery (5:10). The conditional side answers that *Christ shall profit you nothing* is a statement about salvation, not about doctrine, and that Paul's fear that his labour was *in vain* (4:11) is a fear about people, not ideas.

**9. Shipwreck, departure, and erring from the faith (1 Timothy 1:18–20; 4:1; 5:8, 12, 15; 6:10, 21; 2 Timothy 2:17–18; 4:10).**

> 1 Timothy 1:18–20 — This charge I commit unto thee, son Timothy, according to the prophecies which went before on thee, that thou by them mightest war a good warfare; Holding faith, and a good conscience; which some having put away concerning faith have made shipwreck: Of whom is Hymenaeus and Alexander; whom I have delivered unto Satan, that they may learn not to blaspheme.

> 1 Timothy 4:1 — Now the Spirit speaketh expressly, that in the latter times some shall depart from the faith, giving heed to seducing spirits, and doctrines of devils;

> 1 Timothy 5:11–12 — But the younger widows refuse: for when they have begun to wax wanton against Christ, they will marry; Having damnation, because they have cast off their first faith.

> 1 Timothy 6:10 — For the love of money is the root of all evil: which while some coveted after, they have erred from the faith, and pierced themselves through with many sorrows.

> 2 Timothy 2:17–18 — And their word will eat as doth a canker: of whom is Hymenaeus and Philetus; Who concerning the truth have erred, saying that the resurrection is past already; and overthrow the faith of some.

The Pastoral Epistles have a whole vocabulary of leaving: *made shipwreck*, *depart from the faith*, *cast off their first faith*, *erred from the faith*, *turned aside after Satan* (5:15), *overthrow the faith of some*, and Demas, who *hath forsaken me, having loved this present world* (2 Timothy 4:10). The conditional side's point is simple: you cannot make shipwreck of a faith you never had, and Paul says these people *had* faith and a good conscience and *put away* the one and wrecked the other. The Reformed reply that "the faith" in these letters is often the body of Christian teaching, so that to depart from it is to abandon the doctrine rather than to lose regeneration; that "the faith of some" that was overthrown may have been the faith of the unregenerate; and that Hymenaeus was delivered to Satan *that he may learn* — a remedial discipline, not a verdict.

**10. Save a soul from death (James 5:19–20).**

> James 5:19–20 — Brethren, if any of you do err from the truth, and one convert him; Let him know, that he which converteth the sinner from the error of his way shall save a soul from death, and shall hide a multitude of sins.

*Any of you* — a brother — may err from the truth, and bringing him back *saves a soul from death*. The Reformed read the death as possibly physical (as in 1 Corinthians 11:30) or the erring one as revealed by his erring to be unconverted.

**11. Worse than the beginning (2 Peter 1:10; 2:1, 20–22; 3:17).**

> 2 Peter 1:10 — Wherefore the rather, brethren, give diligence to make your calling and election sure: for if ye do these things, ye shall never fall:

> 2 Peter 2:20–22 — For if after they have escaped the pollutions of the world through the knowledge of the Lord and Saviour Jesus Christ, they are again entangled therein, and overcome, the latter end is worse with them than the beginning. For it had been better for them not to have known the way of righteousness, than, after they have known it, to turn from the holy commandment delivered unto them. But it is happened unto them according to the true proverb, The dog is turned to his own vomit again; and the sow that was washed to her wallowing in the mire.

> 2 Peter 3:17 — Ye therefore, beloved, seeing ye know these things before, beware lest ye also, being led away with the error of the wicked, fall from your own stedfastness.

The people in 2:20 *escaped the pollutions of the world through the knowledge* (**ἐπίγνωσις**) *of the Lord and Saviour Jesus Christ* — the same word Peter uses for the believer's knowledge of Christ in 1:2, 3, and 8 — and their end is *worse than the beginning*. The false teachers of 2:1 are *denying the Lord that bought them*. The Reformed reading rests on the proverb: the dog was a dog before and after, and the sow was a sow; the washing was external and the nature never changed. The escape "through the knowledge" was the reformation of life that knowledge of the gospel produces even in the unregenerate. The conditional side answers that Peter's *if ye do these things, ye shall never fall* (1:10) is a promise with a condition, and that *beware lest ye … fall from your own stedfastness* is addressed to the *beloved*.

**12. Abide, and keep yourselves (1 John 2:24–25, 28; 5:16; Jude 1:21).**

> 1 John 2:24–25 — Let that therefore abide in you, which ye have heard from the beginning. If that which ye have heard from the beginning shall remain in you, ye also shall continue in the Son, and in the Father. And this is the promise that he hath promised us, even eternal life.

> 1 John 2:28 — And now, little children, abide in him; that, when he shall appear, we may have confidence, and not be ashamed before him at his coming.

> Jude 1:21 — Keep yourselves in the love of God, looking for the mercy of our Lord Jesus Christ unto eternal life.

*If* what you heard remains in you, you *shall continue* in the Son; abide, *that* we may have confidence at his coming; keep yourselves. The letters that supply the security side with 1 John 2:19 and Jude 1:24 also supply these.

**13. Be thou faithful unto death (Revelation 2–3; 22:19).**

> Revelation 2:10 — Fear none of those things which thou shalt suffer: behold, the devil shall cast some of you into prison, that ye may be tried; and ye shall have tribulation ten days: be thou faithful unto death, and I will give thee a crown of life.

> Revelation 3:5 — He that overcometh, the same shall be clothed in white raiment; and I will not blot out his name out of the book of life, but I will confess his name before my Father, and before his angels.

> Revelation 3:11 — Behold, I come quickly: hold that fast which thou hast, that no man take thy crown.

> Revelation 22:19 — And if any man shall take away from the words of the book of this prophecy, God shall take away his part out of the book of life, and out of the holy city, and from the things which are written in this book.

The seven letters are addressed to churches and promise everything to *him that overcometh* — the tree of life (2:7), escape from the second death (2:11), the white raiment and the name not blotted out (3:5). The conditional side asks why Christ would promise not to blot a name out if no name could be blotted out, and reads 22:19 as the answer. The Reformed reply that 3:5 is a figure of speech — an emphatic promise, **οὐ μὴ ἐξαλείψω**, "I will by no means blot out" — of the kind Scripture uses without implying the opposite was possible, and that Revelation elsewhere describes the book of life as written *from the foundation of the world* (13:8; 17:8). On 22:19 there is a textual note: the KJV's *book of life* follows the Textus Receptus (**βίβλου τῆς ζωῆς**); the great majority of Greek manuscripts and all modern critical editions read *tree of life* (**ξύλου τῆς ζωῆς**), so that the verse threatens loss of a share in the tree and the city rather than erasure from the book. It can be checked here:

```sh
grep '^Revelation 22:19 ' original-languages/greek/tr-scrivener.txt
grep '^Revelation 22:19 ' original-languages/greek/sblgnt.txt
```

**14. The unforgiving servant (Matthew 18:23–35).**

> Matthew 18:32–35 — Then his lord, after that he had called him, said unto him, O thou wicked servant, I forgave thee all that debt, because thou desiredst me: Shouldest not thou also have had compassion on thy fellowservant, even as I had pity on thee? And his lord was wroth, and delivered him to the tormentors, till he should pay all that was due unto him. So likewise shall my heavenly Father do also unto you, if ye from your hearts forgive not every one his brother their trespasses.

The servant's debt was forgiven, and then, because he would not forgive, the forgiveness was withdrawn and the whole debt reinstated: *so likewise shall my heavenly Father do also unto you*. The conditional side takes it as told. The Reformed take it as a parable about the necessity of forgiving, whose point is that the man who will not forgive shows he never received forgiveness in his heart — the forgiveness in the story being the king's declaration, which the servant's conduct proved he had not truly taken in.

**15. The servants and the virgins (Matthew 7:21–23; 24:45–51; 25:1–13; Luke 12:42–46).**

> Matthew 24:48–51 — But and if that evil servant shall say in his heart, My lord delayeth his coming; And shall begin to smite his fellowservants, and to eat and drink with the drunken; The lord of that servant shall come in a day when he looketh not for him, and in an hour that he is not aware of, And shall cut him asunder, and appoint him his portion with the hypocrites: there shall be weeping and gnashing of teeth.

> Luke 12:46 — The lord of that servant will come in a day when he looketh not for him, and at an hour when he is not aware, and will cut him in sunder, and will appoint him his portion with the unbelievers.

The servant was the lord's servant, set over the household, and *began* to beat the others — a change, the conditional side says, not a revelation. The Reformed notice where he ends up: *with the hypocrites* (Matthew), *with the unbelievers* (Luke). Jesus names what the man was. The foolish virgins, likewise, hear *I know you not* (25:12), and the workers of iniquity in Matthew 7 hear *I never knew you* — not "I knew you once." On the Reformed reading these are the parables of the mixed church, and every one of them ends by naming the excluded as people Christ never knew.

---

## The warning passages of Hebrews

Hebrews contains five warnings (2:1–4; 3:7–4:13; 5:11–6:12; 10:19–39; 12:14–29), and two of them are the hardest texts in the New Testament for Position A and Position B alike. They are quoted in full in [Appendix B](#b-the-two-great-warnings-of-hebrews-in-full). The core is here.

> Hebrews 6:4–8 — For it is impossible for those who were once enlightened, and have tasted of the heavenly gift, and were made partakers of the Holy Ghost, And have tasted the good word of God, and the powers of the world to come, If they shall fall away, to renew them again unto repentance; seeing they crucify to themselves the Son of God afresh, and put him to an open shame. For the earth which drinketh in the rain that cometh oft upon it, and bringeth forth herbs meet for them by whom it is dressed, receiveth blessing from God: But that which beareth thorns and briers is rejected, and is nigh unto cursing; whose end is to be burned.

> Hebrews 10:26–29 — For if we sin wilfully after that we have received the knowledge of the truth, there remaineth no more sacrifice for sins, But a certain fearful looking for of judgment and fiery indignation, which shall devour the adversaries. He that despised Moses' law died without mercy under two or three witnesses: Of how much sorer punishment, suppose ye, shall he be thought worthy, who hath trodden under foot the Son of God, and hath counted the blood of the covenant, wherewith he was sanctified, an unholy thing, and hath done despite unto the Spirit of grace?

> Hebrews 10:38–39 — Now the just shall live by faith: but if any man draw back, my soul shall have no pleasure in him. But we are not of them who draw back unto perdition; but of them that believe to the saving of the soul.

> Hebrews 3:12–14 — Take heed, brethren, lest there be in any of you an evil heart of unbelief, in departing from the living God. But exhort one another daily, while it is called To day; lest any of you be hardened through the deceitfulness of sin. For we are made partakers of Christ, if we hold the beginning of our confidence stedfast unto the end;

**Who is described.** Hebrews 6:4–5 lists five things: *once enlightened* (**ἅπαξ φωτισθέντας**), *tasted of the heavenly gift*, *made partakers* (**μέτοχοι**, "sharers") *of the Holy Ghost*, *tasted the good word of God*, and tasted *the powers of the world to come*. Hebrews 10:26 adds *received the knowledge* (**ἐπίγνωσις**) *of the truth*, and 10:29 says of the apostate that the blood of the covenant is that *wherewith he was sanctified* — **ἡγιάσθη**, an aorist passive, "was sanctified," the same verb Hebrews uses of what Christ's offering does for his people (10:10, 14). And 3:12 is addressed to *brethren*.

**What happens.** The KJV's *if they shall fall away* supplies an *if* that is not in the Greek. The word is a participle, **παραπεσόντας**, "having fallen away," in the same series as the participles before it: those who were enlightened, tasted, became partakers, tasted, *and fell away*. The author describes a thing that happens, not a hypothesis. For such people it is *impossible … to renew them again unto repentance*, because they are *crucifying afresh* the Son of God; there *remaineth no more sacrifice for sins*; they *draw back unto perdition* (**ἀπώλεια**, destruction).

**What the author thinks of his readers.** This is the thing most often missed on both sides.

> Hebrews 6:9 — But, beloved, we are persuaded better things of you, and things that accompany salvation, though we thus speak.

He warns them of apostasy and in the same breath says he is persuaded they are saved. Both sides claim this verse. For the conditional side it shows the warning is addressed to people the author believes are Christians — the warning is for believers, as a warning. For the Reformed it shows the author expects his readers *not* to fall, which is what perseverance means, and 10:39 says it outright: *we are not of them who draw back unto perdition*.

**The readings.** There are four.

*(a) The Reformed reading proper (Calvin, Owen).* The people described had every experience short of regeneration. *Enlightened* is not born again; *tasted* is not eaten; *partakers of the Holy Ghost* is sharing in his gifts and operations, as Saul and Balaam did, not his indwelling. Calvin: "the reprobate are sometimes affected by almost the same feeling as the elect, so that even in their own judgment they do not in any way differ from the elect" (*Institutes* 3.2.11). The warning describes what befalls the unregenerate professor, and its function for the elect is to keep them from becoming one. On 10:29, Owen argued that *he* who was sanctified is Christ himself, set apart by his own blood (John 17:19) — a reading few have followed — while most Reformed take the sanctification as covenantal and external, like Israel's.

*(b) The "means of salvation" reading (Schreiner and Caneday).* A more recent Reformed reading, which concedes to the conditional side that the warnings are real and are addressed to believers as believers, and holds that God uses exactly such warnings to keep his elect from apostasy. The warning is not describing what cannot happen; it is the instrument by which it does not. The elect heed the warning, and that is how they persevere. On this view the question "could a true believer fall away?" is answered: the warnings are how God ensures he does not, and asking what would happen without them is asking about a world God has not made.

*(c) The Free Grace reading.* The passage concerns believers who fall into unfruitfulness; what is *impossible* is renewal to the vigour of their first repentance; the *burning* of 6:8 is of the field's thorns, not the field; the judgment of 10:27 is temporal and the loss is of reward. Reformed and Arminian commentators alike regard this as the least natural reading of *perdition* and *fiery indignation, which shall devour the adversaries*.

*(d) The conditional reading (Wesley, Marshall, Picirilli).* The passage means what it says: people who were genuinely Christians — enlightened, partakers of the Spirit, sanctified by the blood — can fall away, and if they fall in *this* way, by a settled repudiation of Christ that crucifies him afresh, they cannot be brought back. Wesleyans generally take the impossibility as describing a real but rare and extreme apostasy, distinct from backsliding, from which one *could* not return only because one *would* not; the Reformed Arminian tradition takes it more strictly, as a final apostasy from which there is no return at all. Both note that the early church read the passage this way for its first four centuries (Part II).

**Hebrews 3:14 and the "if."** The Reformed side's best grammatical point in the whole debate is here. *We are made partakers of Christ* is a perfect, **γεγόναμεν**: "we have become." The condition follows: *if* (**ἐάνπερ**, "if indeed") *we hold the beginning of our confidence stedfast unto the end*. On the Reformed reading a completed becoming is proved by a continued holding: the *if* is the evidence, not the price. On the conditional reading the perfect tense describes a state that persists only as its condition is met, which is what the sentence says. The grammar allows both, and honest commentators on both sides say so.

**Esau.**

> Hebrews 12:15–17 — Looking diligently lest any man fail of the grace of God; lest any root of bitterness springing up trouble you, and thereby many be defiled; Lest there be any fornicator, or profane person, as Esau, who for one morsel of meat sold his birthright. For ye know how that afterward, when he would have inherited the blessing, he was rejected: for he found no place of repentance, though he sought it carefully with tears.

Esau is the fifth warning's picture of a man past recovery. The Reformed note that what Esau sought with tears was the *blessing*, not repentance — the "place of repentance" he could not find was a change of his father's mind — and that Esau was, on Paul's reading of the same story, never among the chosen (Romans 9:13). The conditional side sees in him the point of no return that Hebrews 6 describes.

**A fair summary.** The warnings of Hebrews are addressed to Christians, describe people with a real Christian experience, threaten them with real perdition, and are followed by the author's confidence that his readers will not fall. Every reading has to explain away one of those four things: the Reformed the second, the Free Grace the third, and the conditional the fourth (since on its view the author's confidence in 6:9 is a hope, not a knowledge). The "means of salvation" reading is the attempt to keep all four, at the cost of leaving the hypothetical question — what if a believer did not heed the warning? — deliberately unanswered.

---

## The New Testament's apostates

The New Testament names people who left. Each is claimed by one side, and in every case but one the text withholds the verdict the confessions supply.

**Judas.** Chosen among the twelve (John 6:70), given to Jesus by the Father (17:12), sent out to preach and heal with the others (Matthew 10:1–4), and lost. *By transgression fell* (Acts 1:25).

> John 6:70–71 — Jesus answered them, Have not I chosen you twelve, and one of you is a devil? He spake of Judas Iscariot the son of Simon: for he it was that should betray him, being one of the twelve.

> Acts 1:25 — That he may take part of this ministry and apostleship, from which Judas by transgression fell, that he might go to his own place.

For the Reformed, Judas is 1 John 2:19 in person. Jesus knew *from the beginning* who would betray him (6:64), called him *a devil* while he was still an apostle, said the disciples were clean *but not all* (13:10–11), and in 17:12 lists him as the one exception to *none of them is lost* — an exception that on the Reformed reading is not an exception to the *kept* but to the *given*: he was among them without being of them (the Greek *but*, **εἰ μή**, "except," can bear either sense, as in Galatians 1:19, where James is "excepted" from a group he does not strictly belong to). For the conditional side, Judas was chosen, sent, and *fell* — Luke's word — and John 17:12's *none … but the son of perdition* is a plain statement that one of those given was lost.

**Simon of Samaria.**

> Acts 8:13 — Then Simon himself believed also: and when he was baptized, he continued with Philip, and wondered, beholding the miracles and signs which were done.

> Acts 8:20–23 — But Peter said unto him, Thy money perish with thee, because thou hast thought that the gift of God may be purchased with money. Thou hast neither part nor lot in this matter: for thy heart is not right in the sight of God. Repent therefore of this thy wickedness, and pray God, if perhaps the thought of thine heart may be forgiven thee. For I perceive that thou art in the gall of bitterness, and in the bond of iniquity.

Luke says Simon *believed* and *was baptized*, with the same word (**ἐπίστευσεν**) and no qualification, in the same sentence as the Samaritans who believed and were baptised. Peter then says his heart is *not right* and he has *neither part nor lot in this matter*. The Reformed read Peter's diagnosis as the truth about Simon's "belief" — like the many in Jerusalem who "believed in his name" and to whom Jesus "did not commit himself" (John 2:23–24). The conditional side reads Peter's *repent* as a call to a fallen believer, not to an unconverted one, and notes that Luke, who could have qualified *believed*, did not.

**Hymenaeus, Alexander, and Philetus.** Made shipwreck of faith; delivered to Satan *that they may learn* (1 Timothy 1:20) — the same phrase Paul uses in 1 Corinthians 5:5 of a discipline whose aim is *that the spirit may be saved in the day of the Lord Jesus*. Whatever they were, Paul's treatment of them was remedial.

**Demas.** *Our fellowlabourer* (Philemon 1:24), *Demas … forsaken me, having loved this present world* (2 Timothy 4:10). We are told nothing else, and every tradition has written his ending for him.

**The disciples who went back.**

> John 6:66–69 — From that time many of his disciples went back, and walked no more with him. Then said Jesus unto the twelve, Will ye also go away? Then Simon Peter answered him, Lord, to whom shall we go? thou hast the words of eternal life. And we believe and are sure that thou art that Christ, the Son of the living God.

*Will ye also go away?* Jesus asks it of the twelve, and Peter's answer is not "we cannot" but "to whom shall we go?" On the Reformed reading Jesus has just explained why the others left — it was not given them (6:65) — and Peter's answer is the sound of a kept man. On the conditional reading the question is a real one, put to men who could have said yes.

**What the cases show.** That the New Testament records real departures, describes the departed in the language of faith, baptism, ministry and fellowship, and — except for Judas, whom Jesus called a devil in advance — does not tell us whether they were ever born again. The confessions of Part II fill that silence in opposite directions, and the reader should know that it is a silence being filled.

---

## How each side reads the other's texts

By this point the structure of the argument is visible. Each side has a class of texts it reads straight and a class it reads in the light of the first, and the whole disagreement is over which class controls. It helps to set the two strategies side by side.

**How the Reformed side reads the warnings.** Four moves, used singly or together.

1. *The warnings are addressed to the visible church, which is mixed.* Paul writes to "the church at Corinth," which includes people who will prove not to have been Christ's; Hebrews is written to a congregation, not to a list of the elect. A warning to a congregation warns its unregenerate members of what will befall them and its regenerate members of what they must avoid.
2. *The warnings describe the unregenerate professor.* The person who falls away had light, gifts, experience, and no life. The parable of the soils is the template: every soil but one produced a plant, and only one had a root.
3. *The warnings are the means of perseverance.* God has ordained not only that his people will persevere but that they will persevere *by* heeding warnings. Dort says it in so many words: God preserves his people "by the hearing and reading of his Word, by meditation thereon, and by the exhortations, threatenings, and promises thereof" (Fifth Head, Article 14). A warning is not made unreal by the certainty that it will be heeded.
4. *The conditional "if" is evidential.* "If ye continue" states what will be true of those who were truly reconciled; it does not name a price they might fail to pay. Hebrews 3:14 is the model.

**How the conditional side reads the promises.** Four moves also.

1. *The promises are made to believers as believers.* "He that believeth hath everlasting life" is true of the one believing and says nothing about the one who has stopped. The present participles are read continuously.
2. *No external power can take a believer from Christ; the believer can leave.* John 10:28–29 and Romans 8:38–39 list what cannot separate: wolves, thieves, death, angels, powers. Neither lists the believer's own unbelief, and Scripture names unbelief as the one thing that does separate (Romans 11:20; Hebrews 3:12).
3. *God's faithfulness is faithfulness to his promise, condition included.* "He is faithful that promised" — and what he promised is that the one who endures to the end will be saved. God's keeping is real and is offered to everyone who does not refuse it.
4. *"Elect" is primarily corporate and in Christ.* Christ is the Elect One; the church is elect in him; a person is elect as long as he is in Christ by faith. On this reading the golden chain of Romans 8:30 describes the destiny of the class, not the guaranteed itinerary of each member.

**How Position B reads the warnings.** Differently from both: as warnings of real consequences that are never eternal. Loss of *reward* (1 Corinthians 3:15; 2 John 1:8); loss of *fellowship* (1 John 1:6–7); loss of *usefulness* and *fruit* (John 15:2, 6); *temporal judgment* up to physical death (1 Corinthians 11:30; 1 John 5:16, "a sin unto death"; Acts 5:1–11). Its distinctive contribution to the debate is that it takes the security texts more literally than the Reformed do, and the warning texts less literally than anyone. Its critics on both sides say it must read "not inherit the kingdom" as "inherit less of it," and "perdition" as "a bad time," and that no one would arrive at those readings from the text.

**The symmetry.** There is no neutral ground from which to see which class of texts controls. Each side has to say that the other's texts are true *in a sense*; each accuses the other of muting a whole strand of Scripture; each has a text it cannot read straight without giving up its position — for the Reformed, Hebrews 10:29's *wherewith he was sanctified*; for the conditional, John 10:28's *they shall never perish*; for the Free Grace view, Matthew 24:13's *he that shall endure unto the end, the same shall be saved*. What decides the matter for most people is not one text but a judgment about the whole — about election, the new birth, the nature of faith, and what a warning is for — and that is the subject of the section after next.

---

## What both sides agree Scripture teaches

It helps to see how much is shared, because the disagreement is narrower than the heat around it suggests.

- **Salvation is by grace through faith, not by works, from first to last.** Ephesians 2:8–9; Titus 3:5–7; Romans 4:5. No tradition treated here holds that a Christian *earns* their continuance. The conditional traditions hold that a believer can *refuse* grace, not that he *merits* it.
- **God is able to keep his people, and wants to.** Jude 1:24; 2 Timothy 1:12; 1 Peter 1:5. No one doubts God's power or will to keep; the question is whether he keeps people against their own settled unbelief.
- **No outside power can take a believer from Christ.** John 10:28–29; Romans 8:38–39. Every tradition affirms this.
- **Those who endure to the end are saved, and those who end in unbelief and unrepentant sin are not.** Matthew 24:13; 1 Corinthians 6:9–10; Hebrews 12:14. Positions A and C both hold this. Position B is the one dissenter, and its dissent is what most separates it from historic Christianity in every branch.
- **People who professed faith do walk away, and the New Testament expects it.** 1 Timothy 4:1; 2 Timothy 4:10; 1 John 2:19. The question is never *whether* church members fall away, only what to say of them.
- **Christians are commanded to persevere, to watch, to examine themselves, and to take the warnings seriously.** 2 Corinthians 13:5; 2 Peter 1:10; Hebrews 3:12–13; 1 Corinthians 10:12. The Reformed are as emphatic about this as anyone; Westminster 17 and 18 are surrounded by Westminster 13–16 on sanctification, faith, repentance and good works.
- **A Christian who sins can be restored.** 1 John 1:9; 2:1; Luke 22:32; Galatians 6:1; James 5:19–20. Every tradition, including those that hold a *final* apostasy possible, holds that the ordinary backslider can return and is commanded to.
- **Assurance is possible and is meant to be normal.** 1 John 5:13; Romans 8:16; Hebrews 10:22. Rome qualifies this most (Part II); no one denies that a Christian may have a well-founded confidence.
- **A life of persistent, unrepentant sin is incompatible with a well-founded assurance.** 1 John 3:6–10; Galatians 5:19–21. On the Reformed view because it is evidence against regeneration; on the conditional view because it is the path out; on the Free Grace view because it is the path to severe loss — but no one tells such a person they are fine.

What remains is one question about one kind of person: **the person who truly believed and then finally turned away — was he ever alive, and is he now lost?** Everything else in the debate is an implication of the answer.

---

## What the question turns on

Whether a believer can be finally lost is not really a question that stands on its own. It is the last link in a chain, and people answer it the way they have already answered the questions upstream of it. There are five.

**1. Election.** If God's choice of who will be saved is unconditional and of individuals — if "whom he did predestinate, them he also called: and whom he called, them he also justified: and whom he justified, them he also glorified" is a chain with no leak — then the perseverance of the saints follows as a matter of logic, and the Reformed have always said so. Dort's Fifth Head is the conclusion of its First. If God's choice is conditioned on foreseen faith, or is corporate ("in Christ") so that individuals are elect by being in him, then perseverance is conditional on remaining in him. This is why the question of "once saved, always saved" is, underneath, the question of Calvinism and Arminianism, and why it is hard to hold the fifth point without the other four. Position B is the attempt to do exactly that — unconditional security without unconditional election — and Reformed critics have called it the least coherent combination on the board, while its defenders reply that they are simply reading John 5:24 as written.

**2. The new birth.** If regeneration is a new creation (2 Corinthians 5:17), a birth of incorruptible seed (1 Peter 1:23), a change of nature such that the reborn *cannot* go on sinning (1 John 3:9), then it is hard to see how it could be undone; nobody is unborn. If regeneration is the beginning of a new life *in relationship* with Christ — a branch in a vine — then it persists as the relationship persists, and John 15 says the relationship can end.

**3. Faith.** If faith is God's gift (Ephesians 2:8; Philippians 1:29) and Christ is "the author and finisher of our faith" (Hebrews 12:2) — the one who begins it and brings it to completion — then faith does not finally fail, because its author does not. If faith is the human response that grace makes possible without compelling it, then it can be withdrawn, and Paul's *some having put away … have made shipwreck* describes the withdrawal.

**4. What a warning is for.** Everyone agrees the warnings must be preached to believers. The Reformed say they are the means by which God keeps his people from the thing warned against, and that a warning does not need a possible outcome to function — a fence at a cliff's edge works by being obeyed, not by being fallen over. The conditional side says a warning of an impossible outcome is not a warning, and that Scripture's warnings read as though the outcome were possible because it is.

**5. Justification and the last judgment.** Scripture says the believer is *justified by faith* now (Romans 5:1) and will be *judged according to works* then (2 Corinthians 5:10; Romans 2:6–10; Revelation 20:12). Every tradition has to relate the two. The Reformed: the works are the evidence of the faith that justified. Rome: the works are the fruit of grace, and the justified life can be lost and regained before the judgment. The Wesleyan: the works are the evidence of a continuing faith, and their absence is the sign of its loss. Free Grace: the judgment of works determines reward only, and justification is untouched by it. Where a person places the relation between now and then largely fixes where they land on the question of this document.

| | **Reformed (A)** | **Free Grace (B)** | **Conditional (C)** |
| --- | --- | --- | --- |
| **Election** | Unconditional, individual | Usually unconditional, but not made to bear on security | Conditional on foreseen faith, or corporate in Christ |
| **The new birth** | A change of nature that cannot be undone | A change of status that cannot be undone | A new life in relationship that can be abandoned |
| **Faith** | God's gift, sustained by God | A single act; its continuance not required | God-enabled human response; can be withdrawn |
| **Warnings** | Means by which God keeps the elect | Threats of temporal loss and lost reward | Real alternatives set before real believers |
| **Justification and judgment** | Works evidence the faith that justified | Works determine reward only | Works evidence continuing faith (Wesleyan); justification can be lost and regained (Catholic) |
| **The apostate** | Was never regenerate | Is still saved | Was regenerate and is now lost |

Two observations.

**First, the practical counsel converges far more than the theology does.** Every tradition tells the wanderer to come back and the presumptuous to examine himself, and every tradition holds that the person who dies in settled unbelief is lost (Position B excepted). What differs is the *description* offered of the one who does not come back — and that description is, in the nature of the case, given about someone who is no longer there to hear it.

**Second, the Free Grace position stands apart from the argument between A and C in a way that the slogan hides.** "Once saved, always saved" sounds like the Reformed doctrine said plainly, and its adherents often think they hold the Reformed doctrine. They do not. The Reformed doctrine says the saved *will* persevere; Free Grace says they need not. On the practical question — what to say to the professing Christian living in settled sin — the Reformed pastor and the Wesleyan pastor say the same thing, and the Free Grace pastor says something else. Part II shows how that came about.
---
---

# Part II — What the Church Has Taught

## The first four centuries: falling assumed

For the first four hundred years of Christian writing, nobody argues about whether a baptised Christian can be lost. It is assumed on all sides that he can, and the argument is about something else: whether one who has fallen can be restored, and how often.

**The apostolic fathers** write as though apostasy is an ordinary hazard. Clement of Rome (about 96) urges the Corinthians to repentance with the examples of Lot's wife and the destroyed cities, and warns that those who have known God's mercy and then depart have no excuse. The **Didache** (perhaps 100) ends with the warning that "in the last days ... many shall be offended and perish; but they that endure in their faith shall be saved." The **Shepherd of Hermas** (Rome, about 140) is the whole question in one book: its occasion is that Christians after baptism have sinned grievously, and its answer — controversial then and later — is that God in mercy grants *one* further repentance, but only one, and not for long. Hermas would have had no reason to write if a baptised Christian could not fall, and no reason to limit the remedy if falling were reversible indefinitely.

**Justin Martyr** (about 155) states it flatly in the *Dialogue with Trypho*: those who lived righteously and then fell away at the end, he says, will not be saved by their former righteousness, and God judges each by what he is when he is called. The Old Testament source he is leaning on is Ezekiel 18 and 33. **Irenaeus** (about 180) warns that those who despise God's kindness lose life. **Tertullian** (about 200–212) wrote a whole treatise, *On Repentance*, on the lapsed, and in his later Montanist period denied that the gravest post-baptismal sins could be forgiven by the church at all — a rigorism that shows the era's assumption at its extreme, and that the church rejected.

**The persecutions forced the question.** After the Decian persecution (250) the church was full of *lapsi*, Christians who had sacrificed to the emperor to save their lives. Nobody said they had never been Christians. The dispute — between Cyprian and the rigorist Novatian, and a century later between the Catholics and the Donatists — was over the terms of readmission, and it presupposes on every side that a real Christian had really fallen.

**The Greek fathers** are, if anything, plainer. **Cyril of Jerusalem** warns his catechumens that the Spirit can be grieved away. **John Chrysostom** (about 390–400), preaching through Hebrews, takes 6:4–6 as describing baptised Christians who apostatise, and takes the impossibility as an impossibility of a second baptism, not of all repentance. **Jerome** and **Ambrose** say similar things. Whatever one concludes about the exegesis, the historical fact is not seriously disputed by either side today: the pre-Augustinian church, East and West, held that a Christian could fall away and be lost. Reformed historians grant it and argue that the fathers were reading Scripture through a moralism they had not yet unlearned; conditional writers treat it as the church's original and unbroken reading.

---

## Augustine: the gift of perseverance

Augustine changed the shape of the question, and what he actually taught is more surprising than either side's summary of him.

In his last works — *On Rebuke and Grace* (426) and *On the Gift of Perseverance* (429), written against monks in southern Gaul who thought his doctrine of grace made exhortation pointless — Augustine taught that perseverance to the end is itself a gift of God, given to the predestined and not to others. He then drew a conclusion the Reformed do not draw: that **some who are genuinely regenerate, justified, and in a state of grace are nevertheless not given the gift of perseverance, and do fall away and are lost.** They were truly children of God; they were not among the predestined; God did not give them the perseverance he gave the elect. The number of the saved is fixed by predestination, but the class "presently justified" is larger than the class "elect," and the difference between them is perseverance.

Two things follow. First, Augustine is the father of the doctrine that final salvation is guaranteed to the elect, and not the father of the doctrine that everyone truly saved is elect. Second, he faced the pastoral objection head on, and his answer is the one both later sides borrow: no one in this life can be certain he has the gift of perseverance, so the warnings remain urgent for everyone, and rebuke remains a means God uses. His position is, in the terms of Part I, a hybrid: unconditional security for the elect, conditional security for everyone else, and no infallible way to know in this life which you are.

The **Council of Orange** (529) settled the West on grace against the semi-Pelagians, affirming that grace precedes and enables every good act, without adopting Augustine's full doctrine of predestination and without ruling on perseverance.

---

## The medieval West and Trent

The medieval church built on Augustine's structure and made the pastoral conclusion into a system.

**Thomas Aquinas** (*Summa Theologiae* I-II q.109 a.10; III q.89) treats perseverance as a special gift, distinct from the grace of justification, given to the predestined. Sanctifying grace is lost by any mortal sin — not only by unbelief — and restored by the sacrament of penance. A man can be in grace, lose it, and regain it many times in a life. And no one, apart from a special revelation, can be certain that he is in grace at all, let alone that he will die in it.

**Trent, Session 6** (January 1547), the Decree on Justification, defined this against the Reformers. Three points matter here.

*On perseverance:* chapter 13 calls final perseverance "a great gift," to be hoped for from God but not presumed, and quotes 1 Corinthians 10:12, *let him that thinketh he standeth take heed lest he fall*.

*On assurance:* canon 16 anathematises anyone who "shall say, that he will for certain, with an absolute and infallible certainty, have that great gift of perseverance even unto the end, unless he have learned this by special revelation." Canon 15 condemns the claim that a man born again is bound to believe he is certainly among the predestined.

*On how grace is lost:* canon 23 and chapter 15 teach that grace is lost by every mortal sin, not by unbelief alone, so that a justified person who commits such a sin has lost justification and must be restored through the sacrament of penance. Canon 27 anathematises the claim that no sin but unbelief forfeits grace.

This is Position C in its strongest form, and it is the form the Reformers were arguing against. It should be read alongside its own qualification: Trent also taught that no one falls from grace except by his own fault, and that the fallen may always be restored.

The **Catechism of the Catholic Church** (1992) keeps the structure: mortal sin "results in the loss of charity and the privation of sanctifying grace" (1861), and the sacrament of penance restores it; final perseverance remains a gift to be prayed for.

---

## The East

The Orthodox churches never developed the question in Western terms, and their reluctance is itself a position.

Eastern theology frames salvation as *theosis* — a lifelong participation in the divine life — and as *synergy*, the cooperation of human freedom with divine grace. On that frame the question "can a saved person be lost?" is mis-posed, because salvation is not a transaction completed at a moment but a union that is being entered into and can be abandoned. The East has no doctrine of irresistible grace to make perseverance necessary and no doctrine of imputed righteousness to make it a matter of status. What it has instead is a liturgy full of petitions for "a Christian ending to our life, painless, blameless, peaceful," which assumes the ending is not settled.

The **Confession of Dositheus** (Jerusalem, 1672), written in reaction to the Calvinising confession circulated under the name of Patriarch Cyril Lucaris, rejects unconditional predestination and teaches that grace can be lost and regained. It is not a universally binding definition — the Orthodox do not have the Western machinery for those — but it is the nearest thing to an official Orthodox answer, and the answer is conditional.

---

## Luther and the Lutherans

Luther is claimed by both sides and belongs to neither.

He made assurance central in a way no one before him had: the Christian is to be *certain* of God's favour, because certainty rests on Christ's promise and not on the believer's condition, and Trent's canon 16 was written against him. His *Bondage of the Will* (1525) is as strong on unconditional election as anything in Calvin.

And he taught that faith can be lost. The **Smalcald Articles** (1537), which Luther himself wrote, say of those who fall into open sin: "it is necessary to know and teach that when holy people ... fall into open sin, as David did into adultery, murder, and blasphemy, then faith and the Holy Spirit have departed from them"; and David "did not receive the Holy Spirit again until he was renewed" (III.3). Luther's counsel to those who had fallen was not "you were never a Christian" but "return to your baptism."

The **Formula of Concord** (1577) fixed the Lutheran position. Article XI, on election, teaches that God's election is the cause of the salvation of the elect, and that the elect will certainly be saved — and Article II and the same article's treatment of the fallen teach that a person can lose faith and the Holy Spirit by wilful sin and can be restored by repentance. The Lutheran churches therefore reject "once saved, always saved" and reject equally the idea that a Christian must live in doubt. Their pastoral rule is to point the anxious to the objective promise given in baptism and the Supper, and the presumptuous to the law.

Lutheranism is the standing proof that the five positions of Dort are not the only way to combine unconditional election with a doctrine of apostasy, and that a church can hold both without thinking itself incoherent. Critics on both sides say it is incoherent; Lutherans reply that Scripture teaches both and that the resolution is hidden in God.

---

## Calvin

Calvin's doctrine is stated in the *Institutes* at 3.2.11–12, 3.21–24, and it has two halves that are usually quoted separately.

The first half is perseverance. Election is unconditional and of individuals; Christ loses none of those given him; the elect are preserved by the Spirit and cannot finally fall. "Christ ... will not allow any of them to perish, for they are safer than heaven and earth" (3.24.6, on John 10:28).

The second half is **temporary faith**, and it is Calvin's answer to every apostate in Scripture and in his congregation. He grants that the reprobate may have an experience that looks, to them and to everyone else, like faith:

> "Experience shows that the reprobate are sometimes affected in a way so similar to the elect, that even in their own judgment there is no difference between them. ... Therefore, it is not strange, that by his transient power he impresses on the reprobate a taste of his grace" (*Institutes* 3.2.11, in Henry Beveridge's translation).

He grounds it in the parable of the soils and in Hebrews 6, and it is the pivot on which the whole Reformed reading of the warning passages turns. It is also the doctrine that has caused the most pastoral trouble in Reformed churches: if a false faith can feel like a true one, how does anyone know? Calvin's answer, and the Puritans' after him, was the fruit of a changed life joined to the direct witness of the Spirit — which is why Reformed practical divinity is so heavily occupied with the marks of grace.

---

## Arminius, the Remonstrants, and Dort

**Jacobus Arminius** (1560–1609), a Dutch Reformed pastor and professor at Leiden, is the name the conditional position carries, and on this specific point he never actually committed himself. In his *Declaration of Sentiments* (1608) he said that he had never taught that a true believer can finally fall away, but that he would not assert the contrary either, since some passages "seem to me to wear this aspect," and that the matter deserved careful study. He died in 1609 with the question open.

**The Remonstrance** (1610), drawn up by his followers, kept his caution. Article 5 affirms that believers have sufficient grace to persevere and to conquer, and ends: "But whether they are capable, through negligence, of forsaking again the first beginnings of their life in Christ ... that must be more particularly determined out of the Holy Scripture, before we ourselves can teach it with the full persuasion of our minds." Within a decade the Remonstrants had made up their minds, and **Simon Episcopius** and the later Arminian confession taught that a believer can fall away finally.

**The Synod of Dort** (1618–19) answered the five Remonstrant articles with five heads of doctrine, and the fifth is *Of the Perseverance of the Saints*. It is worth knowing what it actually says, because it is far from the slogan.

- The regenerate are *not* free from indwelling sin, and daily sins of infirmity cleave to their best works (Articles 1–2).
- They can, by their own fault and the power of temptation, fall into "grievous sins," as *David* and *Peter* did; in such falls they grieve the Spirit, interrupt the exercise of faith, wound conscience, and lose for a time the sense of God's favour (Articles 4–5).
- But God "does not wholly withdraw the Holy Spirit from his own people even in their melancholy falls"; he does not suffer them to lose the seed of regeneration or forfeit adoption, and he renews them to repentance (Articles 6–7).
- This is not owing to their merits or strength, but to God's free mercy (Article 8).
- Believers may attain assurance of this perseverance, not by a special revelation but "from faith in God's promises, ... from the testimony of the Holy Spirit, ... and lastly, from a serious and holy desire to preserve a good conscience and to perform good works" (Article 10).
- And crucially, God preserves his people *through means*: "by the hearing and reading of his Word, by meditation thereon, and by the exhortations, threatenings, and promises thereof, as well as by the use of the sacraments" (Article 14).

The Rejection of Errors attached to the Fifth Head names, among the errors condemned, the teaching that perseverance is a condition of the new covenant to be fulfilled by the believer's free will, and the teaching that the doctrine of perseverance is "a pillow for the flesh" — Dort's own acknowledgement of the charge the doctrine has always attracted. What Dort does *not* say anywhere is that a believer may live as he pleases.

---

## England, Westminster, and the Baptists

**The Thirty-Nine Articles** (1571) are, on this point, not Reformed at all. Article 17 teaches predestination and election; Article 16, "Of Sin after Baptism," teaches the opposite of perseverance in the strict sense:

> "Not every deadly sin willingly committed after Baptism is sin against the Holy Ghost, and unpardonable. Wherefore the grant of repentance is not to be denied to such as fall into sin after Baptism. After we have received the Holy Ghost, we may depart from grace given, and fall into sin, and by the grace of God we may arise again and amend our lives. And therefore they are to be condemned which say they can no more sin as long as they live here, or deny the place of forgiveness to such as truly repent."

*We may depart from grace given.* The Article was aimed at Anabaptist perfectionism and at rigorism, not at Calvin, and Anglicans of a Reformed cast have read it as compatible with Article 17. But it is why Anglicanism has never been able to make perseverance a test, and why Wesley, an Anglican priest, could hold his position without leaving his church.

**The Westminster Confession** (1646) is the classic statement of Position A, and its two chapters belong together.

> Chapter 17.1: "They, whom God hath accepted in his Beloved, effectually called and sanctified by his Spirit, can neither totally nor finally fall away from the state of grace; but shall certainly persevere therein to the end, and be eternally saved."

> Chapter 17.3: "Nevertheless they may, through the temptations of Satan and of the world, the prevalency of corruption remaining in them, and the neglect of the means of their preservation, fall into grievous sins; and for a time continue therein: whereby they incur God's displeasure, and grieve his Holy Spirit; come to be deprived of some measure of their graces and comforts; have their hearts hardened, and their consciences wounded; hurt and scandalize others, and bring temporal judgments upon themselves."

And chapter 18, "Of the Assurance of Grace and Salvation," adds that assurance is not of the essence of faith, that a true believer may wait long for it and have it shaken, and that it is built on the promises, the inward evidence of the graces, and the witness of the Spirit. Westminster's perseverance is not a pillow: 17.3 is a paragraph about how far a saint can fall, and 18 is a chapter about how hard assurance can be to keep.

**The Baptists.** The Particular (Calvinistic) Baptists adopted Westminster's chapter almost word for word in the **Second London Confession** (1677/1689), and the General (Arminian) Baptists held the opposite in the **Standard Confession** (1660) and its successors; their descendants are the Free Will Baptists, who hold conditional security to this day. When American Baptists later adopted "once saved, always saved" as a watchword, they were inheriting the Particular Baptist doctrine — and the **Baptist Faith and Message**, the Southern Baptist confession, still states it in the Reformed and not the popular form: "All true believers endure to the end. Those whom God has accepted in Christ, and sanctified by His Spirit, will never fall away from the state of grace, but shall persevere to the end."

*All true believers endure to the end.* That sentence is the difference between Position A and Position B, and it is in the confession of the largest body that uses the slogan.

---

## Wesley

**John Wesley** is Position C's most influential modern advocate, and his controversy with the Calvinists is the reason the English-speaking world has the argument in the form it has.

His fullest treatment is *Serious Thoughts upon the Perseverance of the Saints* (1751), written against a doctrine he thought made holiness optional. Its method is to go through Scripture's cases and conditionals: Ezekiel 18, the seed on the rock, John 15, Romans 11, 1 Corinthians 9:27, 1 Timothy 1:19, Hebrews 6 and 10, 2 Peter 2. His argument is not that God is unreliable but that faith is a relationship a person can abandon, and that the New Testament's warnings are addressed to believers because believers need them.

Two things are often missed about Wesley. First, he was as strong on **assurance** as any Calvinist — the witness of the Spirit (Romans 8:16) was one of his signature doctrines, and Methodists were taught to expect a present, felt certainty of being God's children. He saw no tension: one can be certain of God's present favour without being certain of one's own future choices. Second, his counsel to the fallen was relentlessly hopeful. His sermon *A Call to Backsliders* argues at length that those who have fallen, even grievously, may be restored, and that the passages about irrecoverable apostasy describe an extremity most backsliders have not reached.

His opponents — **George Whitefield**, whose 1740 letter on election broke their public fellowship, and later **Augustus Toplady**, who wrote "Rock of Ages" and some of the most bitter pamphlets of the century — replied that the doctrine destroyed comfort and made salvation depend on man. The exchange set the tone for two centuries of the argument, and not much of it was edifying. That both men wrote hymns still sung in each other's churches is the fairest verdict on the controversy.

---

## The twentieth century: "once saved, always saved" and the Free Grace debate

The slogan itself is American and revivalist. It spread through the frontier churches, the Southern Baptist Convention, and mass evangelism, and by the mid-twentieth century had drifted well away from Westminster. A notorious tract by the Texas Baptist Sam Morris, *Do a Christian's Sins Damn His Soul?* (1930s), put the drifted version at its bluntest: the sins of a saved man do not affect his salvation at all, since they were paid for in advance. That is Position B in its rawest form, and it is what most critics of "once saved, always saved" have in mind.

**Dispensationalism** gave it a theological frame. In the Scofield tradition the believer's eternal position is settled at the moment of faith, the judgment seat of Christ concerns rewards only, and the warning passages are assigned to other dispensations or to loss of reward. **Charles Ryrie** and **Charles Stanley** put it in popular form; Stanley's *Eternal Security: Can You Be Sure?* (1990) contains the sentence that has been quoted against the view ever since: "even if a believer for all practical purposes becomes an unbeliever, his salvation is not in jeopardy."

**The Lordship salvation controversy** of the late 1980s was the collision. **John MacArthur**, in *The Gospel According to Jesus* (1988), argued from a Reformed position that a faith which does not submit to Christ as Lord is not saving faith, and that the "carnal Christian" of popular teaching is a category Scripture does not have. **Zane Hodges** answered in *Absolutely Free!* (1989) and **Charles Ryrie** in *So Great Salvation* (1989), arguing that MacArthur had added works to the gospel. The **Grace Evangelical Society**, founded in 1986, carried the Free Grace position; Reformed and Arminian writers found themselves on the same side of that particular argument, which is the clearest demonstration available that A and C are nearer to each other than either is to B.

**The scholarly literature** since has been unusually good, and both sides have produced work the other takes seriously.

- **I. Howard Marshall**, *Kept by the Power of God* (1969), is the standard exegetical case for conditional security, and is notable for its insistence that God's keeping is real and that the believer's perseverance is genuinely at stake.
- **Judith Gundry Volf**, *Paul and Perseverance* (1990), argues the Pauline case for perseverance.
- **Thomas Schreiner and Ardel Caneday**, *The Race Set Before Us* (2001), advance the "means of salvation" reading of the warnings described in Part I, which has since become the most common Reformed answer and which concedes more to the conditional side than Calvin did.
- **Robert Shank**, *Life in the Son* (1960), and **Robert Picirilli**, *Grace, Faith, Free Will* (2002), state the "Reformed Arminian" position: security is conditional, but only unbelief forfeits it, and such apostasy is final.
- **B. J. Oropeza**'s three-volume study of apostasy in the New Testament (2011–12) is the fullest recent survey of the texts.

Where the argument stands today is roughly where Part I leaves it. Nobody has produced a reading of all the texts that the other side finds compelling, the exegetical moves are well mapped, and most of the movement in the last fifty years has been the two main positions conceding to each other: the Reformed granting that the warnings are addressed to believers as believers, and the Arminian granting that God's keeping is not merely an offer.

---
---

# Part III — What It Means for You

## Start with what is certain

Whatever else is disputed, these are not, and they are enough to stand on.

- **Christ receives everyone who comes.** "Him that cometh to me I will in no wise cast out" (John 6:37). There is no category of person he turns away, and no number of returns after which the offer lapses.
- **Salvation is by grace through faith, not earned and not maintained by merit.** "By grace are ye saved through faith; and that not of yourselves: it is the gift of God" (Ephesians 2:8).
- **God is able to keep you.** "Now unto him that is able to keep you from falling, and to present you faultless before the presence of his glory" (Jude 1:24); "kept by the power of God through faith" (1 Peter 1:5).
- **No outside power can take you from him.** "Neither shall any man pluck them out of my hand" (John 10:28); "neither death, nor life ... shall be able to separate us" (Romans 8:38–39). Every tradition in Part II affirms this without qualification.
- **Confessed sin is forgiven, and the advocate is Christ.** "If we confess our sins, he is faithful and just to forgive us our sins" (1 John 1:9); "if any man sin, we have an advocate with the Father" (1 John 2:1).
- **The one who returns is received.** "Return, ye backsliding children, and I will heal your backslidings" (Jeremiah 3:22); the father ran (Luke 15:20).
- **God does not want you to perish.** "Not willing that any should perish, but that all should come to repentance" (2 Peter 3:9); "I have no pleasure in the death of him that dieth ... turn yourselves, and live ye" (Ezekiel 18:32).
- **A settled, unrepentant life of sin is not compatible with being Christ's.** "Follow peace with all men, and holiness, without which no man shall see the Lord" (Hebrews 12:14). Every tradition says this, for its own reasons.

Notice what is on this list: everything you actually need in order to come to God, stay with him, or come back to him. Notice what is not on it: the answer to the disputed question. That is not an accident of this document's arrangement. The practical counsel of Scripture does not depend on which of the three positions is right, which is why Christians who disagree about the doctrine give nearly identical advice to the person in front of them.

---

## Two ditches

The doctrine has a characteristic danger on each side, and both are described in Scripture.

**Presumption.** Taking security as permission. Paul anticipated it in the very next breath after his greatest statement of grace — "shall we continue in sin, that grace may abound? God forbid" (Romans 6:1–2) — and Jude describes people "turning the grace of our God into lasciviousness" (Jude 1:4). Dort named the charge and denied it; Wesley pressed it and would not let go. The test of whether a doctrine of security has become presumption is simple and practical: does it make you *less* concerned about sin in your life? If so, whatever else it is, it is not the doctrine Westminster 17.3 teaches.

**Terror.** Taking the warnings as a verdict already passed. This is the other ditch and, in most churches, the more common one among people who actually read their Bibles. It produces the Christian who cannot rest, who re-converts every few months, who reads Hebrews 6 with dread and 1 John's tests as an examination he is failing. Scripture calls that condition what it is: "there is no fear in love; but perfect love casteth out fear: because fear hath torment" (1 John 4:18); "God hath not given us the spirit of fear" (2 Timothy 1:7).

The two ditches are why the New Testament never gives assurance and warning to the same person in the same tone. It comforts the frightened and warns the comfortable. Most pastoral error on this subject consists of getting those two backwards, and most of the bitterness in the historical debate comes from each side aiming its best material at the wrong person.

---

## Assurance: how the New Testament says you can know

First John was written for exactly this: "These things have I written unto you that believe on the name of the Son of God; that ye may know that ye have eternal life" (5:13). It is the one book of the Bible whose stated purpose is assurance, and it gives three grounds, not one. All three matter, and taking any one alone produces a distortion.

**1. The promise of God in Christ — the objective ground.**

> John 5:24 — Verily, verily, I say unto you, He that heareth my word, and believeth on him that sent me, hath everlasting life, and shall not come into condemnation; but is passed from death unto life.

This is first because it is the only one that does not depend on you. Assurance that begins with self-examination will not survive a bad week. It begins with what Christ has done and promised, and it is renewed by hearing that promise again. Luther's counsel — go back to your baptism, where God said it to you — and Calvin's — look to Christ, not into yourself — are the same counsel.

**2. The witness of the Spirit — the inward ground.**

> Romans 8:16 — The Spirit itself beareth witness with our spirit, that we are the children of God:

> Romans 8:15 — For ye have not received the spirit of bondage again to fear; but ye have received the Spirit of adoption, whereby we cry, Abba, Father.

The impulse to call God *Father* and mean it is itself evidence. Wesley built on this and the Reformed affirm it; Dort's Article 10 lists "the testimony of the Holy Spirit" as the second ground of assurance.

**3. The fruit of a changed life — the confirming ground.** First John gives several tests, and they are all *in the present tense* and all about direction rather than perfection.

> 1 John 2:3 — And hereby we do know that we know him, if we keep his commandments.

> 1 John 3:14 — We know that we have passed from death unto life, because we love the brethren.

> 1 John 4:13 — Hereby know we that we dwell in him, and he in us, because he hath given us of his Spirit.

> 1 John 3:9 — Whosoever is born of God doth not commit sin; for his seed remaineth in him: and he cannot sin, because he is born of God.

Two cautions on the third ground, because it is the one that gets misused.

*It is not a demand for sinlessness.* The same letter says "if we say that we have no sin, we deceive ourselves" (1:8) and provides an advocate for when we do sin (2:1). The Greek of 3:9 is present and continuous — does not *go on* sinning — and 3:6–10 is about the settled character of a life, not its worst day. John is distinguishing the person who sins and hates it from the person who sins and is at peace with it.

*It is confirming, not foundational.* These tests are given to a church troubled by teachers who denied Christ, to reassure the ordinary believers who stayed. They function to confirm a faith that is already resting on Christ. A person who uses them as the *basis* of assurance will oscillate, because the evidence in any life varies from week to week, and that oscillation is the engine of most Christian anxiety about this subject.

And one thing that is not a ground of assurance in the New Testament: the memory of a past event. Not a date, not a prayer prayed, not an aisle walked. Those may have been the occasion of real faith, and there is nothing wrong with remembering them. But Scripture never tells anyone to rest on having once believed. It tells them to believe — now, today. This is the point at which every tradition, including the Reformed, parts company with the popular slogan, and it is the single most practical conclusion in this document.

---

## If you are afraid you have fallen away

This section is written for the person the warnings frighten. If that is you, four things.

**1. The fear itself is evidence against the thing you fear.** Hebrews 6 describes people who *crucify to themselves the Son of God afresh, and put him to an open shame* — people who have repudiated Christ with contempt and have no wish to return. Whatever that condition is, it is not the condition of someone reading a Bible in distress, wanting to be right with God. The desire to return *is* a turning; nobody seeks God whom God is not already drawing (John 6:44). The old pastors said that the person terrified of having committed the unpardonable sin has by that very terror shown he has not, and they were right about the psychology as well as the theology.

> Matthew 12:31–32 — Wherefore I say unto you, All manner of sin and blasphemy shall be forgiven unto men: but the blasphemy against the Holy Ghost shall not be forgiven unto men. ... whosoever speaketh against the Holy Ghost, it shall not be forgiven him, neither in this world, neither in the world to come.

Read what provoked it: "because they said, He hath an unclean spirit" (Mark 3:30). It was said of men watching the Spirit's work in front of them and calling it the devil's. It is a hardened, deliberate, settled attribution of God's work to Satan, made by people with no interest in repenting. An anxious believer who fears he has committed it is describing, by his fear, a heart in the opposite state.

**2. Come back today, and do not wait to feel worthy.** There is no waiting period, no probation, no sequence of steps. "If we confess our sins, he is faithful and just to forgive us" (1 John 1:9). "Let us therefore come boldly unto the throne of grace, that we may obtain mercy, and find grace to help in time of need" (Hebrews 4:15–16). The publican's whole prayer was seven words and he went home justified (Luke 18:13–14).

> Psalms 51:17 — The sacrifices of God are a broken spirit: a broken and a contrite heart, O God, thou wilt not despise.

**3. Note who else failed.** Peter denied Christ three times with oaths, hours after being warned, and wept (Luke 22:61–62). He was restored by name, over breakfast, with a threefold question that matched his threefold denial and a commission at the end of it (John 21:15–17). David wrote Psalm 51 after adultery and murder. Both are the standard examples in *every* tradition — Dort names them, and so does Wesley. Whatever the truth about final apostasy, Scripture's picture of a serious fall is a fall that ends in restoration.

**4. Stop settling the question and start doing the thing.** Notice that the question "am I still saved?" and the question "will I trust Christ now?" have different answers available to you. The first is about your past and is genuinely hard to settle from the inside. The second is in front of you and can be answered in the next minute, and answering it is what the first question was for. Every tradition in Part II agrees that the person presently trusting Christ is safe. Do that, and the doctrinal question loses its teeth.

> Isaiah 42:3 — A bruised reed shall he not break, and the smoking flax shall he not quench: he shall bring forth judgment unto truth.

> Micah 7:8 — Rejoice not against me, O mine enemy: when I fall, I shall arise; when I sit in darkness, the LORD shall be a light unto me.

If the anxiety is constant and not relieved by these, treat it as what it may well be: not only a theological problem but a burden to carry to a pastor, a mature friend, and, where it has the marks of an illness, to a doctor. Scrupulosity is a real affliction and argument does not cure it.

---

## If you are sure you are fine

This section is written for the opposite person: the one who made a decision years ago, has lived as they please since, and finds the doctrine of security a comfortable thing to hold.

The New Testament's counsel to you is not gentle, and it is the same from all three positions in Part I.

> 2 Corinthians 13:5 — Examine yourselves, whether ye be in the faith; prove your own selves. Know ye not your own selves, how that Jesus Christ is in you, except ye be reprobates?

> 2 Peter 1:10 — Wherefore the rather, brethren, give diligence to make your calling and election sure: for if ye do these things, ye shall never fall:

> Matthew 7:21–23 — Not every one that saith unto me, Lord, Lord, shall enter into the kingdom of heaven; but he that doeth the will of my Father which is in heaven. Many will say to me in that day, Lord, Lord, have we not prophesied in thy name? ... And then will I profess unto them, I never knew you: depart from me, ye that work iniquity.

Three observations, all of which hold whichever position is true.

**The people in Matthew 7 were confident.** They were not lapsed; they expected to be admitted and had a list of works to show. The one thing they lacked was any real relation to Christ — *I never knew you.* Confidence is not the same as assurance, and Scripture nowhere treats a person's certainty about themselves as evidence.

**"Make your calling and election sure" is an imperative.** Peter tells believers to do something, and the something is the list of qualities in the preceding verses (2 Peter 1:5–8). On the Reformed reading you are making sure *to yourself* what God has already made sure in himself. On the conditional reading you are securing what can be lost. Either way you are told to do it, and the man who says "no need, I am eternally secure" has disobeyed the verse he is quoting.

**No confession teaches what you may be assuming.** Westminster says the saints "can neither totally nor finally fall away" — and the same chapter describes the grievous sins they may fall into and the temporal judgments they bring on themselves, and the next chapter says assurance can be lost. The Baptist Faith and Message says "all true believers endure to the end." None of the great statements of security says that a person who believed once and then lived without reference to God is safe. That is the Free Grace position specifically, held by a minority, and it should be held knowingly if it is held at all.

The honest question is not "can I lose it?" but "do I have it?" The first is disputed. The second is testable, by the tests in the section above, and it is the question the New Testament actually puts to the comfortable.

---

## If someone you love has walked away

This is where the doctrine stops being abstract, and it is worth saying plainly what each position licenses you to do, because the answer is nearly the same.

**What no position licenses.** Pronouncing a verdict. You do not know whether they were ever regenerate, you do not know whether they are finally lost, and you do not know what the last hour of their life will hold. Even the Reformed doctrine, which says the truly regenerate will return, gives you no way to tell in advance which case you are looking at — Calvin's temporary faith is precisely the doctrine that these things are not visible from outside. "Who art thou that judgest another man's servant? to his own master he standeth or falleth" (Romans 14:4).

**What every position licenses.**

- **Pray.** No tradition limits prayer for a living person. This is the clearest practical difference between this question and the one in [`praying-for-the-dead.md`](praying-for-the-dead.md): while a person lives, nobody disputes that you may ask God for them, and no doctrine of security or of apostasy makes that prayer pointless.
- **Keep the door open.** The father in Luke 15 was watching the road. The single most useful thing a family or a church can do for someone who has left is to remain, visibly, somewhere they could return to.
- **Expect that return is possible.** James says it outright: "Brethren, if any of you do err from the truth, and one convert him; let him know, that he which converteth the sinner from the error of his way shall save a soul from death" (James 5:19–20). Even the Reformed Arminian tradition, which holds that a final apostasy is irrevocable, holds that almost nobody is in that condition, and Wesley's *Call to Backsliders* argues at length that the hopeless case is rare.
- **Do not use the doctrine as a sedative or a weapon.** Telling yourself "they prayed the prayer, so they are fine" and telling them "you were never really saved" are the two characteristic failures, one from each side. The first stops you praying. The second gives them a reason to stop listening.

> Luke 15:4–5 — What man of you, having an hundred sheep, if he lose one of them, doth not leave the ninety and nine in the wilderness, and go after that which is lost, until he find it? And when he hath found it, he layeth it on his shoulders, rejoicing.

---

## What the warnings are for

If the warnings of Scripture have made you anxious, it is worth asking what they were written to accomplish, because the answer is visible in the texts themselves and it is not anxiety.

Every major warning in the New Testament is followed immediately by an expression of confidence or an appeal to act.

- Hebrews 6:4–8 is followed by 6:9: *But, beloved, we are persuaded better things of you, and things that accompany salvation.*
- Hebrews 10:26–31 is followed by 10:39: *But we are not of them who draw back unto perdition; but of them that believe to the saving of the soul.*
- 1 Corinthians 10:12, *let him that thinketh he standeth take heed lest he fall*, is followed by 10:13: *God is faithful, who will not suffer you to be tempted above that ye are able.*
- 2 Peter 2's catalogue of apostates is preceded by 1:10's promise: *if ye do these things, ye shall never fall.*
- Jude's warnings end in the doxology: *now unto him that is able to keep you from falling.*

The pattern holds across the whole New Testament, and it tells you what the warnings are for. They are not verdicts and they are not predictions. They are the way Scripture keeps Christians awake, and they are always attached to a reason for hope and a thing to do. A warning that leaves you paralysed has been read out of its context; so has a promise that leaves you careless.

Notice also that the warnings are addressed to churches — congregations of people in various conditions — and that you are not obliged to apply every sentence in them to yourself. Paul writes to the Corinthians as *sanctified in Christ Jesus, called to be saints* (1 Corinthians 1:2) and then warns them about the wilderness generation. Both are in the same letter to the same people, and a healthy reading takes the warning as a reason to hold fast rather than as a diagnosis.

---

## The one thing everyone agrees on

Three positions, five centuries of argument, and one point of convergence: **whatever is true about the past, what God asks of you is faith in Christ today.**

> Hebrews 3:13 — But exhort one another daily, while it is called To day; lest any of you be hardened through the deceitfulness of sin.

> Psalms 95:7–8 — To day if ye will hear his voice, Harden not your heart.

The Reformed pastor says: continue, because that is how the kept are kept, and your continuing is the evidence that God has you. The Wesleyan says: continue, because faith is a relationship you are in and can leave. The Free Grace teacher says: continue, because the life you were given is meant to be lived. All three say *continue*, and all three say that today is when it is done.

> Revelation 22:17 — And the Spirit and the bride say, Come. And let him that heareth say, Come. And let him that is athirst come. And whosoever will, let him take the water of life freely.

That invitation is open to the person who has never come, to the person who came and stayed, and to the person who came and left. It does not ask which of the three you are. It is the last thing the Bible says on the subject, and it is an invitation rather than a verdict.

---
---

# Appendices

## A. Every passage that bears on the question

Every reference cited in Parts I–III, sorted canonically, with what it bears on and which side chiefly cites it. **S** marks a passage cited for security (Positions A and B), **C** a passage cited for conditional security, **B** a passage distinctive to the Free Grace position, and **—** a passage both sides use or that bears on the framework. Every reference was checked against [`kjv/kjv.txt`](kjv/kjv.txt).

### Old Testament

| Reference | | Bears on |
| --- | :---: | --- |
| Exodus 32:32–33 | C | Names blotted out of God's book |
| Numbers 23:19 | S | God does not change his mind |
| Deuteronomy 30:19–20 | C | Life and death set before the covenant people |
| 1 Samuel 10:6, 9 | C | Saul given the Spirit and another heart |
| 1 Samuel 16:14 | C | The Spirit departs from Saul |
| 1 Samuel 28:15–16 | C | "The LORD is departed from thee" |
| 1 Kings 11:4, 9 | C | Solomon's heart turned in old age |
| 2 Chronicles 15:2 | C | "If ye forsake him, he will forsake you" |
| Job 17:9 | S | The righteous holds on his way |
| Psalms 32:3–5 | — | Confession and forgiveness |
| Psalms 37:23–24, 28 | S | Though he fall, not utterly cast down |
| Psalms 51:11–12 | C | "Take not thy holy spirit from me" |
| Psalms 51:17 | — | A broken and contrite heart |
| Psalms 69:28 | C | Blotted out of the book of the living |
| Psalms 89:30–34 | S | Chastening without breaking the covenant |
| Psalms 94:14 | S | God will not cast off his people |
| Psalms 95:7–8 | — | "To day if ye will hear his voice" |
| Psalms 103:8–14 | — | God's mercy and knowledge of our frame |
| Psalms 125:1–2 | S | They that trust cannot be removed |
| Psalms 130:3–4 | — | Forgiveness with God |
| Psalms 138:8 | S | "The LORD will perfect that which concerneth me" |
| Psalms 139:23–24 | — | "Search me, O God" |
| Proverbs 24:16 | S | The just man falls seven times and rises |
| Isaiah 1:18 | — | Scarlet sins made white |
| Isaiah 42:3 | — | The bruised reed not broken |
| Isaiah 43:1–2 | S | "Thou art mine" |
| Isaiah 46:4 | S | God carries to old age |
| Isaiah 54:10 | S | The covenant of peace not removed |
| Isaiah 55:7 | — | The call to return |
| Jeremiah 3:12, 22 | — | "Return, ye backsliding children" |
| Jeremiah 24:7 | S | God gives a heart to know him |
| Jeremiah 29:13 | — | Found by those who seek wholly |
| Jeremiah 31:3 | S | An everlasting love |
| Jeremiah 32:40 | S | "They shall not depart from me" |
| Lamentations 3:22–23 | — | Mercies new every morning |
| Ezekiel 3:20 | C | The righteous who turns shall die |
| Ezekiel 18:21–22 | — | The wicked who turns shall live |
| Ezekiel 18:24, 26 | C | Righteousness abandoned is not remembered |
| Ezekiel 18:31–32 | — | "Turn yourselves, and live ye" |
| Ezekiel 33:12–13, 18 | C | The same, restated to the watchman |
| Ezekiel 36:26–27 | S | A new heart, and "cause you to walk" |
| Hosea 6:1 | — | "Let us return unto the LORD" |
| Hosea 11:8 | S | "How shall I give thee up, Ephraim?" |
| Hosea 14:4 | — | "I will heal their backsliding" |
| Joel 2:13 | — | Rend your heart and turn |
| Joel 2:25 | — | The years restored |
| Micah 7:8–9 | — | "When I fall, I shall arise" |
| Zechariah 1:3 | — | "Turn ye unto me ... and I will turn unto you" |
| Malachi 3:6–7 | S/— | God changes not; return unto me |

### New Testament

| Reference | | Bears on |
| --- | :---: | --- |
| Matthew 5:13 | C | Salt that loses its savour is cast out |
| Matthew 7:21–23 | — | "I never knew you" |
| Matthew 10:22 | C | He that endureth to the end shall be saved |
| Matthew 10:32–33 | C | Denying Christ before men |
| Matthew 11:28 | — | "Come unto me, all ye that labour" |
| Matthew 12:31–32 | — | The blasphemy against the Holy Ghost |
| Matthew 12:43–45 | C | The last state worse than the first |
| Matthew 13:3–8, 18–23 | C | The parable of the soils |
| Matthew 18:23–35 | C | Forgiveness withdrawn from the unforgiving servant |
| Matthew 24:10–13 | C | Love waxing cold; enduring to the end |
| Matthew 24:24 | S | "If it were possible ... the very elect" |
| Matthew 24:45–51 | C | The servant cut asunder, portioned with hypocrites |
| Matthew 25:1–13 | C | The foolish virgins: "I know you not" |
| Matthew 25:24–30 | C | The unprofitable servant cast out |
| Mark 3:28–30 | — | The unpardonable sin, and what provoked it |
| Mark 4:16–17 | C | Stony ground: no root, endures for a time |
| Mark 13:13 | C | Enduring to the end |
| Luke 8:11–15 | C | "For a while believe, and ... fall away" |
| Luke 9:62 | C | Looking back, unfit for the kingdom |
| Luke 12:42–46 | C | Portioned with the unbelievers |
| Luke 15:4–7, 20–24 | — | The lost sheep and the returning son |
| Luke 18:13–14 | — | The publican justified |
| Luke 21:34–36 | C | Watch, lest that day come unawares |
| Luke 22:31–32 | S | "I have prayed for thee, that thy faith fail not" |
| Luke 22:61–62 | — | Peter's denial |
| John 3:16, 36 | S | Believing and everlasting life |
| John 4:14; 6:35 | S | Never thirst again |
| John 5:24 | S | Passed from death unto life, no condemnation |
| John 6:37–40, 44 | S | The Father's gift; "I should lose nothing" |
| John 6:47 | S | "He that believeth on me hath everlasting life" |
| John 6:66–71 | — | Disciples who went back; "will ye also go away?" |
| John 8:31 | C | "If ye continue in my word" |
| John 10:27–30 | S | The sheep who shall never perish |
| John 11:25–26 | S | "Shall never die" |
| John 13:1 | S | "He loved them unto the end" |
| John 14:16 | S | The Comforter to abide for ever |
| John 15:1–6 | C | The branch in the vine, cast forth and burned |
| John 17:2, 11–12, 15, 24 | S | Christ keeps those given him |
| John 21:15–17 | — | Peter restored |
| Acts 1:25 | C | Judas "by transgression fell" |
| Acts 8:13, 18–24 | C | Simon believed, baptised, "thy heart is not right" |
| Acts 11:23; 13:43; 14:22 | C | Exhortations to continue in the grace and the faith |
| Acts 16:31 | — | "Believe on the Lord Jesus Christ, and thou shalt be saved" |
| Acts 20:28–30 | C | Wolves, and men from among yourselves |
| Romans 2:6–8 | — | Judgment according to deeds |
| Romans 3:28; 4:5 | — | Justified by faith without works |
| Romans 5:1–2, 8–10 | S | "Much more ... we shall be saved" |
| Romans 6:1–2, 15–16 | — | Grace is not a licence |
| Romans 8:1 | S | No condemnation |
| Romans 8:12–13 | C | "If ye live after the flesh, ye shall die" |
| Romans 8:15–17 | — | The Spirit of adoption; "if so be that we suffer with him" |
| Romans 8:16 | — | The Spirit's witness (assurance) |
| Romans 8:28–30 | S | The golden chain: predestinated to glorified |
| Romans 8:31–39 | S | Nothing shall separate |
| Romans 10:9–13 | — | Whosoever shall call shall be saved |
| Romans 11:17–23 | C | Branches broken off; "otherwise thou also shalt be cut off" |
| Romans 11:29 | S | The gifts and calling are irrevocable |
| Romans 14:4 | — | "To his own master he standeth or falleth" |
| Romans 14:15; 1 Corinthians 8:11 | C | Destroying one "for whom Christ died" |
| 1 Corinthians 1:8–9 | S | "Confirm you unto the end" |
| 1 Corinthians 1:18 | — | "Us which are saved" (present tense) |
| 1 Corinthians 3:11–15 | B | Saved, yet so as by fire |
| 1 Corinthians 6:9–11 | C | The unrighteous shall not inherit the kingdom |
| 1 Corinthians 9:24–27 | C | "Lest ... I myself should be a castaway" |
| 1 Corinthians 10:1–6, 11–12 | C | The wilderness generation as our example |
| 1 Corinthians 10:13 | S | God will not suffer you to be tempted above what you can bear |
| 1 Corinthians 11:30–32 | B | Chastened, that we be not condemned |
| 1 Corinthians 15:1–2 | C | "If ye keep in memory ... unless ye have believed in vain" |
| 2 Corinthians 1:21–22; 5:5 | S | Sealed, and the earnest of the Spirit |
| 2 Corinthians 5:10 | — | The judgment seat of Christ |
| 2 Corinthians 5:17 | S | A new creature |
| 2 Corinthians 6:1 | C | "Receive not the grace of God in vain" |
| 2 Corinthians 7:10 | — | Godly sorrow works repentance |
| 2 Corinthians 11:3 | C | Minds corrupted from the simplicity in Christ |
| 2 Corinthians 13:5 | — | "Examine yourselves" |
| Galatians 1:6; 3:3–4; 4:9–11 | C | Removed from him that called you; begun in the Spirit |
| Galatians 2:16 | — | Not justified by works of the law |
| Galatians 5:1–4, 7 | C | "Ye are fallen from grace" |
| Galatians 5:19–23 | C/— | Works of the flesh; fruit of the Spirit |
| Galatians 6:1 | — | Restoring one overtaken in a fault |
| Galatians 6:7–9 | C | Sowing and reaping; "if we faint not" |
| Ephesians 1:4–5 | S | Chosen before the foundation of the world |
| Ephesians 1:13–14 | S | Sealed with the Spirit, the earnest of the inheritance |
| Ephesians 2:4–10 | S/— | By grace through faith; created unto good works |
| Ephesians 4:30 | S/C | Sealed unto the day of redemption; grieve not the Spirit |
| Ephesians 5:5–6 | C | No inheritance for the covetous idolater |
| Philippians 1:6 | S | He who began the work will perform it |
| Philippians 2:12–13 | — | Work out your salvation; God works in you |
| Philippians 3:11–14 | C | "Not as though I had already attained" |
| Colossians 1:21–23 | C | "If ye continue in the faith" |
| Colossians 2:6–7 | — | Rooted and built up in him |
| Colossians 3:3–4 | S | Your life hid with Christ in God |
| 1 Thessalonians 1:4–5 | — | "Knowing ... your election of God" |
| 1 Thessalonians 3:5, 8 | C | Lest the tempter have tempted you |
| 1 Thessalonians 5:19 | C | "Quench not the Spirit" |
| 1 Thessalonians 5:23–24 | S | "Faithful is he that calleth you, who also will do it" |
| 2 Thessalonians 2:3 | C | The falling away (*apostasia*) |
| 2 Thessalonians 2:13–14 | S | Chosen to salvation through sanctification |
| 2 Thessalonians 3:3 | S | "The Lord is faithful, who shall stablish you" |
| 1 Timothy 1:5–6, 18–20 | C | Shipwreck concerning faith |
| 1 Timothy 4:1 | C | "Some shall depart from the faith" |
| 1 Timothy 4:16 | C | "Continue in them ... thou shalt both save thyself" |
| 1 Timothy 5:8, 11–12, 15 | C | Denied the faith; cast off their first faith; turned aside |
| 1 Timothy 6:9–12, 20–21 | C | Erred from the faith; lay hold on eternal life |
| 2 Timothy 1:7 | — | Not the spirit of fear |
| 2 Timothy 1:9, 12 | S | Saved according to his own purpose; able to keep |
| 2 Timothy 2:11–13 | S/C | "If we deny him, he also will deny us"; "he abideth faithful" |
| 2 Timothy 2:16–18 | C | Overthrowing the faith of some |
| 2 Timothy 2:19 | S | "The Lord knoweth them that are his" |
| 2 Timothy 2:25–26 | — | Recovery out of the snare of the devil |
| 2 Timothy 4:7–8, 18 | S | "I have kept the faith"; the Lord will preserve me |
| 2 Timothy 4:10 | C | Demas forsook me |
| Titus 2:11–12 | — | Grace teaches us to deny ungodliness |
| Titus 3:5–7 | S | Saved by the washing of regeneration |
| Hebrews 2:1–3 | C | Lest we let them slip; how shall we escape |
| Hebrews 3:6, 12–14 | C | "If we hold fast ... stedfast unto the end" |
| Hebrews 3:7–11; 4:1–2, 6, 11 | C | The wilderness generation and the rest |
| Hebrews 4:15–16 | — | Come boldly to the throne of grace |
| Hebrews 5:9 | C | Eternal salvation to them that obey him |
| Hebrews 6:4–8 | C | The great warning |
| Hebrews 6:9–12 | S/— | "We are persuaded better things of you" |
| Hebrews 6:17–19 | S | The hope as an anchor, sure and stedfast |
| Hebrews 7:25 | S | Saved to the uttermost; he ever liveth to intercede |
| Hebrews 9:12 | S | Eternal redemption obtained |
| Hebrews 10:14 | S | Perfected for ever them that are sanctified |
| Hebrews 10:22–31 | C | Sin wilfully; "wherewith he was sanctified" |
| Hebrews 10:35–39 | C/S | "If any man draw back"; "we are not of them who draw back" |
| Hebrews 11:6 | — | Without faith it is impossible to please him |
| Hebrews 12:1–2 | S/— | Run with patience; Jesus the author and finisher |
| Hebrews 12:5–11 | B/— | The chastening of sons |
| Hebrews 12:14–17 | C | Holiness, without which no man shall see the Lord; Esau |
| Hebrews 12:25 | C | See that ye refuse not him that speaketh |
| Hebrews 13:5 | S | "I will never leave thee, nor forsake thee" |
| Hebrews 13:9 | C | Be not carried about with strange doctrines |
| James 1:12–15 | C | Sin, when it is finished, bringeth forth death |
| James 2:17–18 | — | Faith without works is dead |
| James 5:19–20 | C | Converting one who errs "shall save a soul from death" |
| 1 Peter 1:3–5 | S | Kept by the power of God through faith |
| 1 Peter 1:23 | S | Born again of incorruptible seed |
| 1 Peter 5:8–9 | C | Resist the devil, stedfast in the faith |
| 1 Peter 5:10 | S | God will stablish, strengthen, settle you |
| 2 Peter 1:4–11 | C/S | "If ye do these things, ye shall never fall" |
| 2 Peter 2:1 | C | "Denying the Lord that bought them" |
| 2 Peter 2:20–22 | C | The latter end worse than the beginning |
| 2 Peter 3:9 | — | Not willing that any should perish |
| 2 Peter 3:17 | C | "Lest ye ... fall from your own stedfastness" |
| 1 John 1:9 | — | Confession and cleansing |
| 1 John 2:1–2 | — | An advocate with the Father |
| 1 John 2:3 | — | Assurance: keeping his commandments |
| 1 John 2:19 | S | "They went out from us, but they were not of us" |
| 1 John 2:24–25, 28 | C | "If that which ye have heard ... remain in you"; abide in him |
| 1 John 3:6–10 | S/— | The one born of God does not go on sinning |
| 1 John 3:14; 4:7, 13 | — | Assurance: love of the brethren, the Spirit given |
| 1 John 3:18–21 | — | Assurance when the heart condemns |
| 1 John 4:18 | — | Perfect love casts out fear |
| 1 John 5:4 | S | Born of God overcometh the world |
| 1 John 5:11–13 | S | "That ye may know that ye have eternal life" |
| 1 John 5:16 | B | A sin unto death |
| 1 John 5:18 | S | Born of God sinneth not; the wicked one toucheth him not |
| Jude 1:1 | S | Preserved in Jesus Christ |
| Jude 1:5 | C | Saved out of Egypt, afterward destroyed |
| Jude 1:21 | C | "Keep yourselves in the love of God" |
| Jude 1:24–25 | S | Able to keep you from falling |
| Revelation 2:4–5, 7 | C | "Remember from whence thou art fallen"; to him that overcometh |
| Revelation 2:10–11, 25–26 | C | Faithful unto death; hold fast till I come |
| Revelation 3:2–5 | C | "I will not blot out his name out of the book of life" |
| Revelation 3:10–12, 15–16, 21 | C | Hold fast that no man take thy crown |
| Revelation 13:8; 17:8 | S | Names written from the foundation of the world |
| Revelation 20:12 | — | Judged according to works |
| Revelation 21:7–8 | C | He that overcometh shall inherit |
| Revelation 22:17 | — | "Whosoever will, let him take the water of life freely" |
| Revelation 22:19 | C | "God shall take away his part out of the book of life" (see textual note) |

---

## B. The two great warnings of Hebrews in full

Quoted entire, because they are the passages that decide the question for most readers and both sides accuse the other of quoting them in fragments.

### Hebrews 5:11–6:12

> **5:11** Of whom we have many things to say, and hard to be uttered, seeing ye are dull of hearing.
>
> **12** For when for the time ye ought to be teachers, ye have need that one teach you again which be the first principles of the oracles of God; and are become such as have need of milk, and not of strong meat.
>
> **13** For every one that useth milk is unskilful in the word of righteousness: for he is a babe.
>
> **14** But strong meat belongeth to them that are of full age, even those who by reason of use have their senses exercised to discern both good and evil.
>
> **6:1** Therefore leaving the principles of the doctrine of Christ, let us go on unto perfection; not laying again the foundation of repentance from dead works, and of faith toward God,
>
> **2** Of the doctrine of baptisms, and of laying on of hands, and of resurrection of the dead, and of eternal judgment.
>
> **3** And this will we do, if God permit.
>
> **4** For it is impossible for those who were once enlightened, and have tasted of the heavenly gift, and were made partakers of the Holy Ghost,
>
> **5** And have tasted the good word of God, and the powers of the world to come,
>
> **6** If they shall fall away, to renew them again unto repentance; seeing they crucify to themselves the Son of God afresh, and put him to an open shame.
>
> **7** For the earth which drinketh in the rain that cometh oft upon it, and bringeth forth herbs meet for them by whom it is dressed, receiveth blessing from God:
>
> **8** But that which beareth thorns and briers is rejected, and is nigh unto cursing; whose end is to be burned.
>
> **9** But, beloved, we are persuaded better things of you, and things that accompany salvation, though we thus speak.
>
> **10** For God is not unrighteous to forget your work and labour of love, which ye have shewed toward his name, in that ye have ministered to the saints, and do minister.
>
> **11** And we desire that every one of you do shew the same diligence to the full assurance of hope unto the end:
>
> **12** That ye be not slothful, but followers of them who through faith and patience inherit the promises.

**Notes.** *If they shall fall away* (verse 6) renders a Greek participle, **παραπεσόντας**, in the same string as *enlightened*, *tasted*, and *made partakers*; the KJV's *if* is supplied. *Made partakers* is **μέτοχοι γενηθέντας**, "having become sharers." Verse 6's *seeing they crucify* is two present participles, which many modern versions render "because they are crucifying," describing the continuing state of the apostate rather than a single act. Verses 7–8 turn to a field, not a person: the same ground receives the same rain, and the *thorns and briers* are *rejected* (**ἀδόκιμος**, the *castaway* of 1 Corinthians 9:27). Verse 9 is the hinge both sides claim.

### Hebrews 10:19–39

> **19** Having therefore, brethren, boldness to enter into the holiest by the blood of Jesus,
>
> **20** By a new and living way, which he hath consecrated for us, through the veil, that is to say, his flesh;
>
> **21** And having an high priest over the house of God;
>
> **22** Let us draw near with a true heart in full assurance of faith, having our hearts sprinkled from an evil conscience, and our bodies washed with pure water.
>
> **23** Let us hold fast the profession of our faith without wavering; (for he is faithful that promised;)
>
> **24** And let us consider one another to provoke unto love and to good works:
>
> **25** Not forsaking the assembling of ourselves together, as the manner of some is; but exhorting one another: and so much the more, as ye see the day approaching.
>
> **26** For if we sin wilfully after that we have received the knowledge of the truth, there remaineth no more sacrifice for sins,
>
> **27** But a certain fearful looking for of judgment and fiery indignation, which shall devour the adversaries.
>
> **28** He that despised Moses' law died without mercy under two or three witnesses:
>
> **29** Of how much sorer punishment, suppose ye, shall he be thought worthy, who hath trodden under foot the Son of God, and hath counted the blood of the covenant, wherewith he was sanctified, an unholy thing, and hath done despite unto the Spirit of grace?
>
> **30** For we know him that hath said, Vengeance belongeth unto me, I will recompense, saith the Lord. And again, The Lord shall judge his people.
>
> **31** It is a fearful thing to fall into the hands of the living God.
>
> **32** But call to remembrance the former days, in which, after ye were illuminated, ye endured a great fight of afflictions;
>
> **33** Partly, whilst ye were made a gazingstock both by reproaches and afflictions; and partly, whilst ye became companions of them that were so used.
>
> **34** For ye had compassion of me in my bonds, and took joyfully the spoiling of your goods, knowing in yourselves that ye have in heaven a better and an enduring substance.
>
> **35** Cast not away therefore your confidence, which hath great recompence of reward.
>
> **36** For ye have need of patience, that, after ye have done the will of God, ye might receive the promise.
>
> **37** For yet a little while, and he that shall come will come, and will not tarry.
>
> **38** Now the just shall live by faith: but if any man draw back, my soul shall have no pleasure in him.
>
> **39** But we are not of them who draw back unto perdition; but of them that believe to the saving of the soul.

**Notes.** The warning is framed by *let us* (verses 22–25) and by an appeal to the readers' own past endurance (32–34) — it is addressed to the congregation as participants, not as spectators. *We sin wilfully* is first person plural. *Knowledge of the truth* is **ἐπίγνωσις**. *Wherewith he was sanctified* (verse 29) is **ἐν ᾧ ἡγιάσθη**, aorist passive of the verb Hebrews uses at 10:10 and 10:14 for what Christ's offering accomplishes; it is the single hardest phrase in the New Testament for Position A, and the readings offered for it are surveyed in Part I. *Draw back* (38–39) is **ὑποστέλλω**, to shrink back, and *perdition* is **ἀπώλεια**, destruction — the noun of the verb in John 3:16 and 10:28.

---

## C. A timeline

| Date | Event |
| --- | --- |
| c. 96 | Clement of Rome warns the Corinthians of falling from God's mercy |
| c. 140 | *Shepherd of Hermas*: one post-baptismal repentance, and no more |
| c. 155 | Justin Martyr: those who fall away at the end are not saved by past righteousness |
| c. 200–212 | Tertullian on the lapsed; his later rigorism denies restoration for grave sin |
| 250–251 | The Decian persecution and the *lapsi*; Cyprian against Novatian on readmission |
| c. 390 | Chrysostom reads Hebrews 6 of baptised Christians who apostatise |
| 426–429 | Augustine, *On Rebuke and Grace* and *On the Gift of Perseverance*: the regenerate may fall; the predestined are given perseverance |
| 529 | Council of Orange settles the West on grace, without defining perseverance |
| c. 1270 | Aquinas: perseverance a special gift; no certainty of grace without revelation |
| 1517–1525 | Luther on assurance; *The Bondage of the Will* on unconditional election |
| 1537 | Smalcald Articles: faith and the Holy Spirit depart from those who fall into open sin |
| 1547 | Trent, Session 6: grace lost by mortal sin; canon 16 against certainty of perseverance |
| 1559 | Calvin's *Institutes*, final edition: perseverance of the elect, and temporary faith |
| 1571 | Article 16: "after we have received the Holy Ghost, we may depart from grace given" |
| 1577 | Formula of Concord: the elect are saved; faith can be lost and regained |
| 1608–1610 | Arminius leaves the question open; the Remonstrance, Article 5, does the same |
| 1618–19 | Synod of Dort, Fifth Head: the perseverance of the saints, through means |
| 1646 | Westminster Confession 17 and 18: perseverance, and the varieties of assurance |
| 1660 / 1689 | General Baptists affirm conditional security; Particular Baptists follow Westminster |
| 1672 | Confession of Dositheus (Orthodox): grace can be lost and regained |
| 1740 | Whitefield's letter to Wesley on election breaks their public fellowship |
| 1751 | Wesley, *Serious Thoughts upon the Perseverance of the Saints* |
| c. 1770s | Toplady against Wesley; the controversy at its most bitter |
| 19th c. | American revivalism spreads "once saved, always saved" as a watchword |
| 1909 | Scofield Reference Bible; dispensationalism frames the warnings as loss of reward |
| c. 1930s | Sam Morris, *Do a Christian's Sins Damn His Soul?* — the slogan at its bluntest |
| 1960 | Robert Shank, *Life in the Son*: the case for conditional security |
| 1963 / 2000 | Baptist Faith and Message: "All true believers endure to the end" |
| 1969 | I. Howard Marshall, *Kept by the Power of God* |
| 1988–1990 | The Lordship salvation controversy: MacArthur, Hodges, Ryrie, Stanley |
| 2001 | Schreiner and Caneday, *The Race Set Before Us*: warnings as the means of perseverance |

---

## D. Where the traditions stand

| Tradition | Can a truly saved person be finally lost? | How it is described | Assurance | Governing text |
| --- | --- | --- | --- | --- |
| Reformed / Presbyterian | No | The elect are preserved and will persevere; apostates were never regenerate | Possible and to be sought, not of the essence of faith, and may be shaken | Westminster Confession 17, 18; Dort, Fifth Head |
| Reformed Baptist | No | As Reformed | As Reformed | Second London Confession (1689) 17 |
| Southern Baptist (confessional) | No | "All true believers endure to the end" | Assumed | Baptist Faith and Message, Article V |
| Free Grace / much popular Baptist teaching | No | The apostate remains saved; he loses reward, fellowship, and usefulness | Rests on the promise alone; self-examination is discouraged as undermining it | No confession; Hodges, Ryrie, Stanley |
| Lutheran | Yes | Faith and the Spirit are lost by wilful sin and restored by repentance; the elect are nonetheless saved | Central; grounded in the objective promise of baptism and the Supper | Smalcald Articles III.3; Formula of Concord XI |
| Anglican | Yes, in the Articles | "We may depart from grace given ... and by the grace of God we may arise again" | Varies with churchmanship | Thirty-Nine Articles 16, 17 |
| Roman Catholic | Yes | Sanctifying grace is lost by any mortal sin and restored through penance; final perseverance is a gift | Moral, not infallible; canon 16 forbids absolute certainty | Trent, Session 6, chs. 13, 15, canons 16, 23, 27; *Catechism* 1861 |
| Eastern Orthodox | Yes | Salvation is a lifelong synergy that can be abandoned; the question is not defined in Western terms | Not framed as a doctrine of certainty | Confession of Dositheus (1672); liturgical practice |
| Methodist / Wesleyan | Yes | By unbelief or persistent wilful sin; the fallen can usually be restored | Strong: the witness of the Spirit | Wesley, *Serious Thoughts* (1751); *A Call to Backsliders* |
| Pentecostal / Holiness | Yes | As Wesleyan | As Wesleyan | Assemblies of God and similar statements of faith |
| Free Will Baptist / Reformed Arminian | Yes | Only by a settled apostasy of unbelief, and that apostasy is final | Present, resting on present faith | Shank, *Life in the Son*; Picirilli, *Grace, Faith, Free Will* |
| Churches of Christ / Restorationist | Yes | Salvation is forfeited by falling away; restoration through repentance | Present-tense faithfulness | No binding confession |

---

## E. Honest caveats

**Both sides have a text they cannot read straight.** The Reformed have Hebrews 10:29's *wherewith he was sanctified*, and the various expedients offered for it are visibly expedients. The conditional side has John 10:28's *they shall never perish*, and the "no one can snatch, but you can walk" reading of it is also an expedient. Position B has Matthew 24:13 and 1 Corinthians 6:9–10, and reads both in a way almost nobody arrives at from the text. A reader who finds one side's difficulties fatal should check whether they have weighed their own side's with the same scales.

**The grammar does not settle it.** This document has resisted the temptation to make the Greek decide, because it does not. The present participles in John, the perfect in Hebrews 3:14, the aorist chain in Romans 8:30, the conditional particles in Colossians 1:23 — all of them are compatible with more than one reading, and commentators who claim otherwise are usually claiming more than the language supports. Where a grammatical point is genuinely one-sided (the missing *if* in Hebrews 6:6, the textual variant at Revelation 22:19) it is said so.

**The historical sketch is a sketch.** The fathers, the Reformers, and the confessions are quoted in standard English editions and translations, from a knowledge of those texts rather than from a fresh reading of each; a reader building an argument on a quotation should check it in a printed edition. Dates for the earliest material are approximate. The account of Orthodoxy flattens real diversity, the account of Lutheran teaching compresses a long internal discussion, and "Free Grace" covers a range of writers who differ among themselves.

**Terminology is a trap on this subject, and the trap is partly deliberate.** "Once saved, always saved," "eternal security," and "perseverance of the saints" are used interchangeably in popular speech and mean materially different things, and arguments frequently consist of one person attacking Position B while the other defends Position A. Part I's three-position frame is this document's attempt to keep them apart; it is a clarification, not a neutral fact, and other writers divide the ground differently.

**This document takes a position, and states it.** On the exegesis, the strongest case is the one that takes both strands as written: the promises of preservation are unconditional and mean what they say, and the warnings are addressed to real believers and describe a real danger. The reading that accounts for the most data with the fewest expedients is the "means of perseverance" reading (Position A in the form Schreiner and Caneday give it), because it is the only one that does not have to soften either strand — it grants the conditional side that the warnings are genuine and addressed to Christians, and grants the security side that those who are Christ's will in fact heed them. That reading has a real cost, which should be stated rather than hidden: it declines to answer the hypothetical question "what would happen to a true believer who ignored the warning?", and a reader may fairly judge that a position which cannot answer the central question is not an answer to it. Readers who weigh Hebrews 10:29, Ezekiel 18, or the plain force of the conditional clauses more heavily will land on Position C, and this document has tried to quote their texts at full strength rather than in the abbreviated form that makes them easy to answer. Position B is the one view treated here as clearly weaker than its rivals, for the reason given in Part I: it must read *shall not inherit the kingdom of God* and *draw back unto perdition* as describing consequences short of being lost, and no reader comes to those verses with that reading unless a system has supplied it.

**Nothing here is pastoral counsel for a particular person.** Someone in acute distress about their salvation needs a pastor, a friend, time, and sometimes a doctor, more than they need an argument. Part III is written to be usable by such a person, and it is not a substitute for those things.

---

## F. Further reading

**Primary — read these first, in this order:**

1. **John 10:22–30** — the sheep, the hand, and the Father
2. **Hebrews 6:1–12 and 10:19–39** — the two great warnings, entire and in context ([Appendix B](#b-the-two-great-warnings-of-hebrews-in-full))
3. **1 John**, the whole letter in one sitting — the New Testament's book on assurance, warnings and all
4. **Romans 8** and **Romans 11:17–24** — by the same author, twelve pages apart
5. **Luke 8:4–15** — the parable every reading of the warnings has to accommodate
6. **Ezekiel 18** and **33:10–20** — the Old Testament's case, symmetrical in both directions
7. **1 Corinthians 9:24–10:13** — Paul's fear for himself, the wilderness generation, and God's faithfulness, in one argument
8. **2 Peter 1:1–11 and 2:17–22** — "ye shall never fall" and "the latter end is worse"
9. **Luke 15 and John 21:15–17** — what restoration looks like

**Confessional texts, all short and freely available:** Dort's Fifth Head of Doctrine; Westminster Confession chapters 17 and 18; Trent, Session 6, chapters 13 and 15 with canons 16, 23 and 27; the Thirty-Nine Articles 16 and 17; the Smalcald Articles III.3. Reading the actual confessions is the fastest cure for the caricatures on every side, and each of these takes a few minutes.

**Modern treatments, one from each camp:** I. Howard Marshall, *Kept by the Power of God* (1969), for the conditional case; Thomas Schreiner and Ardel Caneday, *The Race Set Before Us* (2001), for the Reformed case in its most concessive form; Robert Picirilli, *Grace, Faith, Free Will* (2002), for the Reformed Arminian position; and, for the four-views format, *Four Views on Eternal Security* (ed. J. Matthew Pinson, 2002), which puts a Wesleyan, a Reformed Arminian, a moderate Calvinist and a classical Calvinist in one volume with each other's replies.

**Related material in this repository:**

- [`kjv/`](kjv) — the full King James text, greppable by reference
- [`original-languages/`](original-languages) — the Greek behind every word discussed here, with Strong's numbers and parsing
- [`faith-vs-works-living-christian-letter.txt`](faith-vs-works-living-christian-letter.txt) — notes on faith and works, and on Philippians 2:12, which is the question underneath this one
- [`jude-bible-study-outline.md`](jude-bible-study-outline.md) — Jude, whose twenty-five verses contain both *preserved in Jesus Christ* and *keep yourselves in the love of God*
- [`praying-for-the-dead.md`](praying-for-the-dead.md) — on the state of the dead, and on what can and cannot be done for a person once the question is closed

---

*Scripture quoted from the King James Version (1769), public domain in the United States, as carried in [`kjv/kjv.txt`](kjv/kjv.txt) in this repository; every quotation was taken directly from that file. Greek words, parsing and Strong's numbers are from [`original-languages/`](original-languages). Confessional and historical sources are quoted in standard English editions and are named where used.*
