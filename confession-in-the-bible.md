# Confession in the Bible
## What Scripture Says About Confessing Sin and Confessing Christ, Why Protestant Churches Have No Confessional, and Whether Salvation Depends on It

---

## How to Use This Document

This document was written to answer one question that is really three:

1. **What does the Bible actually say about confession?** — every passage that uses the word, and the passages that describe the thing without the word, quoted and read in context; who confesses, to whom, and what follows (Part I)
2. **How did confession become a sacrament heard by a priest, and what did the Protestant churches do with it?** — from the assemblies of the first century to Lateran IV, Trent, Luther, Calvin, the Prayer Book, and the Methodist band meeting, with the actual words of each (Part II)
3. **Is confession required for salvation, and what should a Protestant actually do with their sins?** — the answer the texts give, sorted by what kind of confession is meant, and a practical shape for confession in a church that has no confessional (Part III)

Part I is the reference material. Part II explains why the line runs where it does — Catholics and Orthodox confess to a priest; Protestants, on the whole, do not — and corrects a common assumption on both sides of it: that the Protestant churches abolished confession. They abolished the *sacrament* and the *obligation*; every one of the Reformation churches kept confession itself, in forms described below, and some of them kept private confession to a minister. Part III is the practical payoff.

**The short answer,** for a reader who wants it before the evidence: the Bible speaks of confession in two senses, and the answer differs for each. *Confessing Christ* — owning him openly as Lord — is bound to salvation as tightly as anything in the New Testament (Romans 10:9–10; Matthew 10:32). *Confessing sin* — agreeing with God about what you have done and saying so — is the voice of the repentance without which no one is saved (Luke 18:13–14; 1 John 1:8–10), and is commanded to God always, to the person you have wronged where there is one, and to fellow believers in certain settings. What Scripture nowhere requires is the third thing that the word "confession" usually brings to mind: the private recital of sins to a priest as the condition of their forgiveness. That practice has a history, and Part II tells it; but it is not in the Bible, and the texts appealed to for it (John 20:23; James 5:16) say something else when read whole.

### The source of the quotations

Scripture is quoted from the **King James Version (1769)**, the text carried in [`kjv/`](kjv) in this repository. Every quotation was taken directly from that file, so any verse can be checked at its source:

```sh
grep '^1 John 1:9 ' kjv/kjv.txt
grep -i 'confess' kjv/kjv.txt
```

Hebrew and Greek words, their parsing, and their Strong's numbers are from [`original-languages/`](original-languages), and where a count or a form is stated the command that produced it is given. Where the KJV's English has drifted far enough to mislead, the modern sense is supplied: *faults* in James 5:16 translates a word meaning *trespasses*; *profession* in Hebrews is the same Greek word as *confession* elsewhere; *remit* means forgive; *conversation* means conduct; *comfortably* in 2 Chronicles 30:22 means encouragingly.

**The Apocrypha.** Two passages from the books the 1611 King James Bible printed between the Testaments are mentioned in passing — Sirach's "Be not ashamed to confess thy sins" and the Prayer of Manasseh. Neither is in the 66-book text in [`kjv/`](kjv), neither can be checked against this repository, and both are marked *(Apocrypha)* where they appear. Nothing in the argument rests on them.

### A note on what this document is not

This is a study of the biblical and historical material, not a ruling from a church. On confession the churches have ruled, and the rulings are quoted, including the one that pronounces anathema on the position this document reaches. Where the difference between the traditions is a real difference about what a text means, both readings are set out and the reasons for preferring one are given. Where this document takes a position, it says so and shows its work.

---

## Contents

**[Part I — What the Bible Says](#part-i--what-the-bible-says)**

- [Two confessions, one word](#two-confessions-one-word)
- [The words themselves](#the-words-themselves)
- [Confession under the Law](#confession-under-the-law)
- [Confession in Israel's history](#confession-in-israels-history)
- [The Psalms: the anatomy of a confession](#the-psalms-the-anatomy-of-a-confession)
- [The Prophets and the Proverbs](#the-prophets-and-the-proverbs)
- ["I have sinned": nineteen confessions and what came of them](#i-have-sinned-nineteen-confessions-and-what-came-of-them)
- [John the Baptist and the Jordan](#john-the-baptist-and-the-jordan)
- [Confession in the presence of Jesus](#confession-in-the-presence-of-jesus)
- [Who can forgive sins?](#who-can-forgive-sins)
- [Confession between people: the brother, the church, and restitution](#confession-between-people-the-brother-the-church-and-restitution)
- [The apostles' preaching](#the-apostles-preaching)
- [The keys, binding and loosing, and John 20:23](#the-keys-binding-and-loosing-and-john-2023)
- [James 5:16: confess your faults one to another](#james-516-confess-your-faults-one-to-another)
- [1 John 1:9: the Christian's ongoing confession](#1-john-19-the-christians-ongoing-confession)
- [Confessing Christ](#confessing-christ)
- [One mediator, one high priest, a priesthood of all](#one-mediator-one-high-priest-a-priesthood-of-all)
- [Confession and salvation: putting the texts together](#confession-and-salvation-putting-the-texts-together)
- [What every tradition agrees Scripture teaches](#what-every-tradition-agrees-scripture-teaches)

**[Part II — What the Church Has Done](#part-ii--what-the-church-has-done)**

- [The first century after the apostles](#the-first-century-after-the-apostles)
- [Public penance: the one repentance](#public-penance-the-one-repentance)
- [From the Irish monasteries to the confessional](#from-the-irish-monasteries-to-the-confessional)
- [Lateran IV and Trent: confession becomes law](#lateran-iv-and-trent-confession-becomes-law)
- [The East](#the-east)
- [The Reformation: what was rejected and what was kept](#the-reformation-what-was-rejected-and-what-was-kept)
- [Since the Reformation](#since-the-reformation)
- [So is there really no mechanism?](#so-is-there-really-no-mechanism)

**[Part III — Is Confession Required for Salvation?](#part-iii--is-confession-required-for-salvation)**

- [The answer, in three parts](#the-answer-in-three-parts)
- [Confession to people: the three cases Scripture commands](#confession-to-people-the-three-cases-scripture-commands)
- [What confession is not](#what-confession-is-not)
- [A shape for confession in a church without a confessional](#a-shape-for-confession-in-a-church-without-a-confessional)
- [When you cannot stop confessing the same sin](#when-you-cannot-stop-confessing-the-same-sin)
- [For the Catholic or Orthodox reader](#for-the-catholic-or-orthodox-reader)

**[Appendices](#appendices)**

- [A. Every verse in the KJV that contains "confess"](#a-every-verse-in-the-kjv-that-contains-confess)
- [B. Every "I have sinned" in the KJV](#b-every-i-have-sinned-in-the-kjv)
- [C. A timeline](#c-a-timeline)
- [D. Where the traditions stand](#d-where-the-traditions-stand)
- [E. Honest caveats](#e-honest-caveats)
- [F. Further reading](#f-further-reading)

---
---

# Part I — What the Bible Says

## Two confessions, one word

The word *confess* in the Bible covers two acts that English keeps apart. One is confessing sin: saying to God, or to someone else, that you have done wrong. The other is confessing faith: saying who God is, or who Jesus is, in front of people who may not want to hear it. The Bible uses one word for both, in Hebrew and again in Greek, and it is not an accident. To confess is to *say the same thing* — to agree out loud with what is true, whether the truth is about God or about yourself. David does both in one Psalm. The creed and the confession of sin in a Sunday service are, in the Bible's vocabulary, the same verb.

That matters for the question this document answers, because "is confession required for salvation?" gets a different answer depending on which confession is meant, and the New Testament's clearest "yes" attaches to the one that is not about sin at all. Keep the two in view throughout.

There is also a third thing the word means in ordinary Christian speech, which the Bible does not use it for: the sacrament in which a Catholic or Orthodox Christian tells their sins to a priest and receives absolution. Part I asks whether the Bible describes that; Part II tells where it came from.

---

## The words themselves

**Hebrew: יָדָה (*yādāh*, H3034).** The root means to throw or to extend the hand, and in worship, to praise with hands lifted. In the form called the *hiphil* it is the ordinary Old Testament word for *give thanks* or *praise* — it is the verb behind "O give thanks unto the LORD" — and it occurs 114 times in the Hebrew Bible. In the reflexive form called the *hithpael* it means *confess*, and that form occurs exactly eleven times, all but one of them plainly confessions of sin (the exception, 2 Chronicles 30:22 at Hezekiah's Passover, sits where confession and thanksgiving meet):

```sh
grep -P '\tH3034\t' original-languages/hebrew/wlc-words.tsv | grep -c 'Vt'
```

Leviticus 5:5; 16:21; 26:40; Numbers 5:7; 2 Chronicles 30:22; Ezra 10:1; Nehemiah 1:6; 9:2; 9:3; Daniel 9:4; 9:20. Every one is quoted below. In a handful of other places the KJV translates the *praise* form as *confess* — Psalm 32:5, Proverbs 28:13, and "confess thy name" in Solomon's prayer (1 Kings 8:33, 35) — where the two senses run together: to confess God's name is to praise it. The noun **תּוֹדָה** (*tôdāh*, H8426) is the same: usually *thanksgiving* or *the sacrifice of praise*, twice *confession* (Joshua 7:19; Ezra 10:11).

Two other Hebrew verbs do the work in famous verses without the word. In Psalm 51:3, *I acknowledge my transgressions* is simply **יָדַע** (*yādaʻ*, H3045), *I know*: confession begins as knowing, and refusing to look away. And the opposite of confessing, in both Psalm 32:5 and Proverbs 28:13, is **כָּסָה** (*kāsāh*, H3680), *to cover*: "mine iniquity have I not hid"; "he that covereth his sins shall not prosper." The one who will not uncover his sin finds that God does not cover it either (Psalm 32:1).

**Greek: ὁμολογέω (*homologeō*, G3670).** From *homou* (together) and *logos* (word): to say the same thing, to agree, to acknowledge, to declare openly. It occurs in 21 verses of the Textus Receptus:

```sh
cut -f1,4 original-languages/greek/tr-scrivener-words.tsv | grep -P '\tG3670$' | cut -f1 | sort -u | wc -l
```

The KJV renders it *confess*, *profess*, *promise*, and — once, in Hebrews 13:15, *the fruit of our lips giving thanks to his name* — *give thanks*. Of its 21 verses, only one (1 John 1:9) is about confessing sin. The other twenty are about confessing Christ, confessing a belief, or confessing a status (Hebrews 11:13, *confessed that they were strangers and pilgrims*). This is the word of Matthew 10:32, Romans 10:9–10, and the whole of 1 John.

**ἐξομολογέω (*exomologeō*, G1843)** is the same verb with *ek* (out) in front, which makes it *confess fully, openly, out loud*, and in the middle voice — the form the New Testament uses for confessing sin — it carried the sense, in Greek business documents of the period, of *acknowledging a debt*. It occurs in eleven verses: Matthew 3:6 and Mark 1:5 (the crowds at the Jordan), Acts 19:18 (the Ephesian converts), James 5:16 (*confess your faults one to another*), Luke 22:6 (Judas *promised*), and six times as *praise* or *give thanks* — Matthew 11:25 and Luke 10:21 (*I thank thee, O Father*), Romans 14:11 and Philippians 2:11 (*every tongue shall confess*), Romans 15:9, and Revelation 3:5 (*I will confess his name*). Once again a single word does the work of confessing sin and praising God.

The noun **ὁμολογία (*homologia*, G3671)**, *confession*, occurs six times, and the KJV renders it *profession* in five of them: *the High Priest of our profession* (Hebrews 3:1), *let us hold fast our profession* (Hebrews 4:14), *the profession of our faith* (Hebrews 10:23), *a good profession before many witnesses* (1 Timothy 6:12), *your professed subjection unto the gospel* (2 Corinthians 9:13); and *confession* once, of Christ before Pilate (1 Timothy 6:13). Every one is a confession of faith, not of sin. When a Protestant church calls its doctrinal standard a *Confession* — the Augsburg Confession, the Westminster Confession — it is using the New Testament's word in the New Testament's commonest sense.

**Forgive** in the Old Testament is chiefly **סָלַח** (*sālach*, H5545), a verb used in the Hebrew Bible only of God forgiving, never of one person forgiving another; and **נָשָׂא** (*nāsāʼ*, H5375), *to lift, carry away*, the word of Psalm 32:1 (*whose transgression is forgiven*, literally *lifted*) and 32:5 (*thou forgavest*). In the New Testament it is **ἀφίημι** (*aphiēmi*, G0863), *to send away, let go, remit* — the KJV's *remit* in John 20:23 and *forgive* nearly everywhere else — with its noun **ἄφεσις** (*aphesis*, G0859), *remission*. **Repent** is **μετανοέω** (*metanoeō*, G3340), *to think differently afterwards*, to change one's mind: repentance and confession are distinct words for two sides of one turning, the inward change and its spoken acknowledgement.

Finally, the English. *Confess* or its forms occur in **44 verses** of the KJV; *I have sinned*, the Bible's simplest confession, in **19**; *forgive* in its forms in **98**:

```sh
grep -c -i 'confess' kjv/kjv.txt
grep -c 'I have sinned' kjv/kjv.txt
grep -c -i 'forgiv' kjv/kjv.txt
```

All 44 *confess* verses are tabulated in [Appendix A](#a-every-verse-in-the-kjv-that-contains-confess), with the Hebrew or Greek word behind each, and all 19 *I have sinned* verses in [Appendix B](#b-every-i-have-sinned-in-the-kjv).

---

## Confession under the Law

The Law of Moses is where confession of sin first appears as a required act, and it is worth reading closely, because it is the nearest thing in Scripture to a ritual of confession and it already has the shape that the rest of the Bible keeps.

> Leviticus 5:5 — And it shall be, when he shall be guilty in one of these things, that he shall confess that he hath sinned in that thing:

> Leviticus 5:6 — And he shall bring his trespass offering unto the LORD for his sin which he hath sinned, a female from the flock, a lamb or a kid of the goats, for a sin offering; and the priest shall make an atonement for him concerning his sin.

Three parties and three acts. The sinner *confesses* — the first *hithpael* of *yādāh* in the Bible — and what he confesses is *that he hath sinned in that thing*: specific, not general. The sinner *brings* the sacrifice. And the priest *makes atonement* — not by hearing the confession, which the text does not say he hears, but by offering the blood. The priest's part is the altar; the confession is directed, as verse 6 says of the offering, *unto the LORD*. Nowhere in Leviticus is a priest told to receive a confession, weigh it, or pronounce a verdict on it.

Where the sin was against a neighbour, a fourth act is added:

> Leviticus 6:4 — Then it shall be, because he hath sinned, and is guilty, that he shall restore that which he took violently away, or the thing which he hath deceitfully gotten, or that which was delivered him to keep, or the lost thing which he found,

> Leviticus 6:5 — Or all that about which he hath sworn falsely; he shall even restore it in the principal, and shall add the fifth part more thereto, and give it unto him to whom it appertaineth, in the day of his trespass offering.

> Numbers 5:7 — Then they shall confess their sin which they have done: and he shall recompense his trespass with the principal thereof, and add unto it the fifth part thereof, and give it unto him against whom he hath trespassed.

Confession and restitution go together, and the restitution goes to *him against whom he hath trespassed*, not to the sanctuary. The person you wronged is the person you settle with. This is the root of Jesus' *first be reconciled to thy brother* (Matthew 5:24) and of Zacchaeus' *I restore him fourfold* (Luke 19:8), and it is the first of the three cases in which Scripture requires confession to a human being, taken up in Part III.

On the Day of Atonement, confession is made for the whole nation, and by the high priest:

> Leviticus 16:21 — And Aaron shall lay both his hands upon the head of the live goat, and confess over him all the iniquities of the children of Israel, and all their transgressions in all their sins, putting them upon the head of the goat, and shall send him away by the hand of a fit man into the wilderness:

> Leviticus 16:22 — And the goat shall bear upon him all their iniquities unto a land not inhabited: and he shall let go the goat in the wilderness.

This is the one place in the Law where a priest is the one confessing, and he confesses on behalf of the people, not after hearing from them. The sins go on to a substitute and are carried away. Hebrews reads the whole chapter as a picture of Christ, and the picture is of a confession *by* the priest over the victim, not *to* the priest by the sinner.

The Law's last word on confession is a promise for the exile it foresaw:

> Leviticus 26:40 — If they shall confess their iniquity, and the iniquity of their fathers, with their trespass which they trespassed against me, and that also they have walked contrary unto me;

> Leviticus 26:41 — And that I also have walked contrary unto them, and have brought them into the land of their enemies; if then their uncircumcised hearts be humbled, and they then accept of the punishment of their iniquity:

> Leviticus 26:42 — Then will I remember my covenant with Jacob, and also my covenant with Isaac, and also my covenant with Abraham will I remember; and I will remember the land.

Confession here is national, it includes the fathers' sins as well as one's own, it is joined to a humbled heart and to accepting the justice of what has happened, and God's answer to it is to remember his covenant — not to be talked into mercy, but to act on a promise already made. Solomon's prayer at the dedication of the temple (1 Kings 8:46–50), Daniel's prayer in Babylon (Daniel 9), and Nehemiah's (Nehemiah 1:6; 9:2–3) are all this verse being obeyed.

One more thing the Law says by silence. The sacrificial system covered sins of ignorance and weakness; for presumptuous sin — sin *with a high hand*, in the Hebrew idiom — it offered nothing:

> Numbers 15:30 — But the soul that doeth ought presumptuously, whether he be born in the land, or a stranger, the same reproacheth the LORD; and that soul shall be cut off from among his people.

That is why David, an adulterer and a murderer, could not bring an offering, and said so — "thou desirest not sacrifice; else would I give it" (Psalm 51:16) — and why his confession is not a ritual in Leviticus but a Psalm.

---

## Confession in Israel's history

**Achan** (Joshua 7). After the defeat at Ai, the lot falls on Achan, and Joshua says:

> Joshua 7:19 — And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.

> Joshua 7:20 — And Achan answered Joshua, and said, Indeed I have sinned against the LORD God of Israel, and thus and thus have I done:

Notice the two directions in one sentence: *make confession unto him* — God — and *tell me* — Joshua. The confession is to God; the telling is to the man who has to deal with the consequences. Achan's is a full and specific confession (verse 21 lists the garment, the silver, and the gold, and where they are hidden), and it is, as Joshua put it, giving glory to God: to confess is to declare that God was right. And Achan is executed anyway. Confession made under exposure, after the lot has fallen, does not undo temporal consequences; the Bible does not pretend that it does. What it may have done for Achan before God, the text does not say.

**Saul and David** are the Old Testament's controlled experiment. Both are kings; both are confronted by a prophet; both say the same three words.

> 1 Samuel 15:24 — And Saul said unto Samuel, I have sinned: for I have transgressed the commandment of the LORD, and thy words: because I feared the people, and obeyed their voice.

> 1 Samuel 15:30 — Then he said, I have sinned: yet honour me now, I pray thee, before the elders of my people, and before Israel, and turn again with me, that I may worship the LORD thy God.

> 2 Samuel 12:13 — And David said unto Nathan, I have sinned against the LORD. And Nathan said unto David, The LORD also hath put away thy sin; thou shalt not die.

Saul's confession comes with an excuse (*because I feared the people*) and a request (*honour me now, I pray thee, before the elders*): what he wants back is his standing. David's comes with nothing — four words in Hebrew, no excuse, no request — and what follows is the one sentence of absolution a prophet pronounces in the Old Testament: *The LORD also hath put away thy sin.* Nathan does not forgive David; he tells David what the LORD has done. Psalm 51 is David's own account of the same moment, and it shows what was underneath the four words. The difference between the two confessions was not in the words; it was in the men. Every later discussion of "true" and "false" confession is a footnote to this pair.

**Solomon's prayer** foresees the exile and lays down the pattern for national confession: sin, defeat, captivity, and then —

> 1 Kings 8:47 — Yet if they shall bethink themselves in the land whither they were carried captives, and repent, and make supplication unto thee in the land of them that carried them captives, saying, We have sinned, and have done perversely, we have committed wickedness;

> 1 Kings 8:48 — And so return unto thee with all their heart, and with all their soul, in the land of their enemies, which led them away captive, and pray unto thee toward their land, which thou gavest unto their fathers, the city which thou hast chosen, and the house which I have built for thy name:

> 1 Kings 8:50 — And forgive thy people that have sinned against thee, and all their transgressions wherein they have transgressed against thee, and give them compassion before them who carried them captive, that they may have compassion on them:

*We have sinned, and have done perversely, we have committed wickedness* — three verbs, mounting — became the liturgical confession of Israel; Daniel prays it word for word (Daniel 9:5), and the Prayer of Manasseh *(Apocrypha)* and the synagogue's confession on the Day of Atonement are built on it. It is made from exile, with no temple and no priest, and God's promise is to hear it *in heaven thy dwelling place* (verse 49).

**Manasseh** is the extreme case: the worst king Judah had, who *humbled himself greatly before the God of his fathers, and prayed unto him: and he was intreated of him* (2 Chronicles 33:12–13). No priest, no sacrifice, no temple — he was in a Babylonian prison — and he was heard.

**Ezra, Nehemiah, and Daniel** each give a full national confession, and three things about them bear on the later argument.

> Ezra 10:1 — Now when Ezra had prayed, and when he had confessed, weeping and casting himself down before the house of God, there assembled unto him out of Israel a very great congregation of men and women and children: for the people wept very sore.

> Ezra 10:11 — Now therefore make confession unto the LORD God of your fathers, and do his pleasure: and separate yourselves from the people of the land, and from the strange wives.

> Nehemiah 1:6 — Let thine ear now be attentive, and thine eyes open, that thou mayest hear the prayer of thy servant, which I pray before thee now, day and night, for the children of Israel thy servants, and confess the sins of the children of Israel, which we have sinned against thee: both I and my father's house have sinned.

> Nehemiah 9:2 — And the seed of Israel separated themselves from all strangers, and stood and confessed their sins, and the iniquities of their fathers.

> Nehemiah 9:3 — And they stood up in their place, and read in the book of the law of the LORD their God one fourth part of the day; and another fourth part they confessed, and worshipped the LORD their God.

> Daniel 9:4 — And I prayed unto the LORD my God, and made my confession, and said, O Lord, the great and dreadful God, keeping the covenant and mercy to them that love him, and to them that keep his commandments;

> Daniel 9:5 — We have sinned, and have committed iniquity, and have done wickedly, and have rebelled, even by departing from thy precepts and from thy judgments:

> Daniel 9:20 — And whiles I was speaking, and praying, and confessing my sin and the sin of my people Israel, and presenting my supplication before the LORD my God for the holy mountain of my God;

First, confession is *public* and *corporate*: the whole assembly stands and confesses (Nehemiah 9:2–3), and a fourth of the day is given to it, paired with a fourth given to reading the Law. Confession in the Old Testament is not a private transaction; it is what the people of God do together, out loud, in the light of the Word. Second, the leaders confess sins they did not personally commit — Daniel, of whom Scripture records no fault, says *we have sinned* and *my sin and the sin of my people*. Confession is not only owning your own acts but owning your people. Third, it is joined in every case to doing something — *do his pleasure: and separate yourselves* (Ezra 10:11); confession that leaves the wrong in place is not what these chapters mean by the word.

---

## The Psalms: the anatomy of a confession

Psalm 32 is the Bible's most careful description of what confession is and what it does, and Paul chose it, of all the Old Testament, to explain justification by faith (Romans 4:6–8).

> Psalms 32:1 — Blessed is he whose transgression is forgiven, whose sin is covered.

> Psalms 32:2 — Blessed is the man unto whom the LORD imputeth not iniquity, and in whose spirit there is no guile.

> Psalms 32:3 — When I kept silence, my bones waxed old through my roaring all the day long.

> Psalms 32:4 — For day and night thy hand was heavy upon me: my moisture is turned into the drought of summer. Selah.

> Psalms 32:5 — I acknowledged my sin unto thee, and mine iniquity have I not hid. I said, I will confess my transgressions unto the LORD; and thou forgavest the iniquity of my sin. Selah.

The sequence is exact. Unconfessed sin is *silence*, and the silence is physical: bones, moisture, drought, a hand heavy day and night. Then three verbs of confession, piled up — *acknowledged*, *not hid*, *will confess* — against the one verb of the previous state, *kept silence*. Then, on the far side of a semicolon, forgiveness, and the Hebrew is more abrupt than the English: *I said, I will confess my transgressions to the LORD — and you lifted the guilt of my sin.* The forgiveness comes at the resolve, before the words are even out. God is not persuaded by the confession; he is waiting for it.

To whom? *Unto thee* ... *unto the LORD*. There is no one else in the Psalm. And what the Psalm calls the result — transgression forgiven, sin covered, iniquity not imputed — is what Paul calls *the blessedness of the man, unto whom God imputeth righteousness without works* (Romans 4:6). Confession, in the Psalm Paul chose, is the opposite of a work: it is the end of pretending, and the man in verse 2 *in whose spirit there is no guile* is the man who has stopped covering.

Psalm 51, David's confession after Nathan, adds what Psalm 32 leaves out.

> Psalms 51:3 — For I acknowledge my transgressions: and my sin is ever before me.

> Psalms 51:4 — Against thee, thee only, have I sinned, and done this evil in thy sight: that thou mightest be justified when thou speakest, and be clear when thou judgest.

> Psalms 51:6 — Behold, thou desirest truth in the inward parts: and in the hidden part thou shalt make me to know wisdom.

> Psalms 51:16 — For thou desirest not sacrifice; else would I give it: thou delightest not in burnt offering.

> Psalms 51:17 — The sacrifices of God are a broken spirit: a broken and a contrite heart, O God, thou wilt not despise.

*Against thee, thee only* — David had wronged Bathsheba, Uriah, his army, and his nation, and he knew it; but sin *as sin* is against God, and confession *as confession* is to God. This is the verse that makes confession to God non-negotiable in every tradition. *Thou desirest truth in the inward parts* — the confession God wants is not the recital but the honesty under it. And *thou desirest not sacrifice* — David, under the Law, with the tabernacle standing and priests on duty, says there is no ritual for what he has done, and offers a broken heart instead. It is accepted. Nathan had already said so.

Three shorter Psalms fill in the edges. *For I will declare mine iniquity; I will be sorry for my sin* (Psalm 38:18): confession and sorrow together. *I said, LORD, be merciful unto me: heal my soul; for I have sinned against thee* (Psalm 41:4): confession as a plea for healing, which James will pick up. *If I regard iniquity in my heart, the Lord will not hear me* (Psalm 66:18): the one thing that blocks prayer is not sin but cherished sin, sin looked at and kept.

And two Psalms settle a question the later church would torment consciences with — what about the sins you cannot remember?

> Psalms 19:12 — Who can understand his errors? cleanse thou me from secret faults.

> Psalms 139:23 — Search me, O God, and know my heart: try me, and know my thoughts:

> Psalms 139:24 — And see if there be any wicked way in me, and lead me in the way everlasting.

No one can enumerate their sins; David says so and asks to be cleansed from the ones he does not know. The Augsburg Confession would quote Psalm 19:12 in 1530 against the requirement to list every sin, and it is the right verse.

Finally, Psalm 130 states the ground of the whole thing in two lines: *If thou, LORD, shouldest mark iniquities, O Lord, who shall stand? But there is forgiveness with thee, that thou mayest be feared* (130:3–4). Forgiveness is *with God* — it is his character before it is anyone's transaction — and Psalm 103 spells the character out: *he hath not dealt with us after our sins ... as far as the east is from the west, so far hath he removed our transgressions from us ... for he knoweth our frame; he remembereth that we are dust* (103:10, 12, 14).

---

## The Prophets and the Proverbs

The wisdom literature has one proverb on confession, and it is the one to memorise:

> Proverbs 28:13 — He that covereth his sins shall not prosper: but whoso confesseth and forsaketh them shall have mercy.

Two verbs on the right side of the colon, and both are participles in the Hebrew — *the one confessing and forsaking*. Confession without forsaking is not the thing promised mercy; nor is forsaking without confession — the quiet resolution to do better that never admits what was done. The pair is the Old Testament's definition of repentance, and Isaiah gives the same pair in the same order: *Let the wicked forsake his way, and the unrighteous man his thoughts: and let him return unto the LORD, and he will have mercy upon him; and to our God, for he will abundantly pardon* (Isaiah 55:7).

The prophets add three things.

**God asks for the acknowledgement, and asks for little else.**

> Jeremiah 3:12 — Go and proclaim these words toward the north, and say, Return, thou backsliding Israel, saith the LORD; and I will not cause mine anger to fall upon you: for I am merciful, saith the LORD, and I will not keep anger for ever.

> Jeremiah 3:13 — Only acknowledge thine iniquity, that thou hast transgressed against the LORD thy God, and hast scattered thy ways to the strangers under every green tree, and ye have not obeyed my voice, saith the LORD.

*Only acknowledge.* The word is the smallest possible condition, and it is set beside the largest possible mercy. Hosea says the same from the other side — *I will go and return to my place, till they acknowledge their offence, and seek my face* (Hosea 5:15) — and then tells Israel exactly what to say, since they seem not to know how: *Take with you words, and turn to the LORD: say unto him, Take away all iniquity, and receive us graciously* (Hosea 14:2). The people are given the confession to pray. So is every Christian who prays the Lord's Prayer.

**The sorrow that matters is inward.** *Rend your heart, and not your garments, and turn unto the LORD your God: for he is gracious and merciful* (Joel 2:13). Nineveh, in Jonah 3, does the outward things — sackcloth, fasting, ashes, even on the animals — and God's response is to *their works, that they turned from their evil way* (3:10). The outward acts are not despised; but it is the turning God sees.

**Forgiveness is God's act, for God's own sake.** *I, even I, am he that blotteth out thy transgressions for mine own sake, and will not remember thy sins* (Isaiah 43:25). *Who is a God like unto thee, that pardoneth iniquity ... he will subdue our iniquities; and thou wilt cast all their sins into the depths of the sea* (Micah 7:18–19). Ezekiel 18 closes the circle: the wicked man who turns *shall surely live* and *all his transgressions that he hath committed, they shall not be mentioned unto him* (18:21–22), because God has *no pleasure in the death of him that dieth* (18:32). Confession is never, in the prophets, a way of overcoming God's reluctance. It is walking through a door he has already opened and is standing in.

Job, in the speech of Elihu, gives the nearest thing to a formula, and it is a formula for confessing to God alone:

> Job 33:27 — He looketh upon men, and if any say, I have sinned, and perverted that which was right, and it profited me not;

> Job 33:28 — He will deliver his soul from going into the pit, and his life shall see the light.

Sirach *(Apocrypha)* has the counsel that the later church would repeat most: *Be not ashamed to confess thy sins* (Sirach 4:26). It sits comfortably beside everything above.

---

## "I have sinned": nineteen confessions and what came of them

The plainest confession in the Bible is three words, and the KJV records it nineteen times:

```sh
grep 'I have sinned' kjv/kjv.txt
```

The full list is in [Appendix B](#b-every-i-have-sinned-in-the-kjv). What it shows, read as a set, is that the words prove nothing. Pharaoh says them twice (Exodus 9:27; 10:16) and hardens his heart again both times. Balaam says them with a hedge in the same breath — *if it displease thee, I will get me back again* (Numbers 22:34) — and goes on. Saul says them three times, once with an excuse (1 Samuel 15:24), once asking to be honoured before the elders (15:30), and and once to David, in words David did not trust enough to stay within his reach (26:21; 27:1). Judas says them to the chief priests — *I have sinned in that I have betrayed the innocent blood* — and receives the only answer a human confessor without a gospel can give: *What is that to us? see thou to that* (Matthew 27:4). It is the most desolate confession in Scripture, and it is desolate because it was made to the wrong people. Judas confessed to men who could not forgive him and did not try.

Set against these are David's — *I have sinned against the LORD* (2 Samuel 12:13), *I have sinned greatly in that I have done* (24:10), *I have sinned, and I have done wickedly: but these sheep, what have they done?* (24:17) — each followed by mercy; the Psalmist's *I have sinned against thee* (Psalm 41:4), which is a prayer for healing; Micah's *I will bear the indignation of the LORD, because I have sinned against him, until he plead my cause* (Micah 7:9), which is confession joined to patient hope; and the prodigal's, rehearsed and then delivered, *Father, I have sinned against heaven, and before thee* (Luke 15:18; 15:21), which is interrupted by an embrace before it is finished.

Two conclusions. First, the New Testament's warning that confession can be dead — *they profess that they know God; but in works they deny him* (Titus 1:16) — has a long Old Testament pedigree, and a church that wants to know whether a confession is real has always looked at what followed it, as Samuel did with Saul. Second, the confessions God accepted were made *to God* — David to the LORD, the prodigal to the father — and the confession that ended worst of all was made to priests. That is not an argument by itself; it is a pattern to keep in mind when the arguments come.

---

## John the Baptist and the Jordan

The New Testament opens with a mass confession of sin, and it is the first thing the Gospels record anyone doing in response to preaching.

> Matthew 3:6 — And were baptized of him in Jordan, confessing their sins.

> Mark 1:4 — John did baptize in the wilderness, and preach the baptism of repentance for the remission of sins.

> Mark 1:5 — And there went out unto him all the land of Judaea, and they of Jerusalem, and were all baptized of him in the river of Jordan, confessing their sins.

The verb is *exomologeō*, confessing out loud, and the participle is present: they were being baptised *while confessing*. Four things are plain. The confession was public — in a river, in a crowd. It was spoken, not merely felt. It was joined to repentance and to a baptism *for the remission of sins*: the forgiveness was God's, the baptism was its sign, the confession was the people's part. And there was no priest. John was a priest's son (Luke 1:5), but nothing in the account has him receiving confessions or absolving; the crowds confess *their sins* in the hearing of one another, and go under the water. When the church of the second century described confession, it looked like this — see Part II — and not like a booth.

---

## Confession in the presence of Jesus

The Gospels record no occasion on which Jesus asked anyone to list their sins, and several on which people confessed in his presence without being asked. Taken together they are a portrait of what confession looks like when it is made to the one person who can forgive.

**The publican** (Luke 18:9–14). The Pharisee's prayer is a confession too — of his fasting and tithing. The publican's is seven words in the Greek:

> Luke 18:13 — And the publican, standing afar off, would not lift up so much as his eyes unto heaven, but smote upon his breast, saying, God be merciful to me a sinner.

> Luke 18:14 — I tell you, this man went down to his house justified rather than the other: for every one that exalteth himself shall be abased; and he that humbleth himself shall be exalted.

*God be merciful to me a sinner* — literally *God, be propitiated toward me, the sinner*, the verb of the mercy seat and the sacrifices. He names no sin. He does not need to; he names himself. And Jesus says he went home *justified* — Paul's word, the word of Romans 3 to 5 — on the strength of a confession that consisted of a posture, a gesture, and a sentence, addressed to God. If the question is what the minimum saving confession looks like, this is the Lord's own answer.

**The prodigal** (Luke 15:17–24) rehearses his confession in the far country — *Father, I have sinned against heaven, and before thee, and am no more worthy to be called thy son: make me as one of thy hired servants* — and delivers it on the road, and the father, who *ran* while the son *was yet a great way off*, cuts it short before the last clause. The son gets *I have sinned* and *no more worthy* out; he never gets to *make me as one of thy hired servants*, because the robe and the ring are already being called for. Confession is met, in the parable, not by a verdict but by a welcome that was already on its way.

**The woman in Simon's house** (Luke 7:36–50) says nothing at all. Her confession is tears, hair, and ointment, and Jesus reads it as such, and says *Her sins, which are many, are forgiven ... Thy sins are forgiven ... Thy faith hath saved thee; go in peace* (7:47, 48, 50). The guests ask the right question — *Who is this that forgiveth sins also?* — and it is the question the next section takes up.

**Zacchaeus** (Luke 19:8–10) confesses by restitution: *if I have taken any thing from any man by false accusation, I restore him fourfold* — double what the Law required — and Jesus announces *This day is salvation come to this house*. The confession was made to Jesus, and its content was what he would do for the people he had wronged.

**Peter** confesses three times and in three ways. At the first miraculous catch: *Depart from me; for I am a sinful man, O Lord* (Luke 5:8) — confession as the reflex of a holy presence, the same reflex as Isaiah's *Woe is me! for I am undone; because I am a man of unclean lips* (Isaiah 6:5), which was answered by a coal from the altar and *thine iniquity is taken away, and thy sin purged* (6:7). At the denial: *Peter went out, and wept bitterly* (Luke 22:62) — no recorded words. And at the lakeside, in John 21:15–17, where Jesus does not ask him to confess the denial at all, but asks three times *lovest thou me?*, once for each denial, and restores him with a commission. Peter's restoration is the New Testament's fullest picture of a fallen believer being received back, and it contains no enumeration of sin, no penance, and no absolution formula. It contains a question about love and a job.

**The thief** (Luke 23:39–43) is the case every discussion of what is *required* comes back to, because he had no time for anything else.

> Luke 23:40 — But the other answering rebuked him, saying, Dost not thou fear God, seeing thou art in the same condemnation?

> Luke 23:41 — And we indeed justly; for we receive the due reward of our deeds: but this man hath done nothing amiss.

> Luke 23:42 — And he said unto Jesus, Lord, remember me when thou comest into thy kingdom.

> Luke 23:43 — And Jesus said unto him, Verily I say unto thee, To day shalt thou be with me in paradise.

He does both confessions. He confesses his sin — *we indeed justly* — and he confesses Christ — *Lord ... thy kingdom* — out loud, before men, to a crowd that was mocking. He is not baptised, he receives no sacrament, he makes no satisfaction, he is absolved by no one but Jesus, and Jesus promises him paradise that day. Every tradition has to accommodate him, and every tradition does, by admitting that what is ordinarily required is not what is absolutely required. Part III returns to him.

---

## Who can forgive sins?

The scribes asked the question, and their theology was correct:

> Mark 2:7 — Why doth this man thus speak blasphemies? who can forgive sins but God only?

Jesus does not dispute the premise. He answers by claiming to be the exception — *that ye may know that the Son of man hath power on earth to forgive sins* (Mark 2:10) — and proving it with a healing. Matthew's account ends with a line that both sides of the later argument cite: *when the multitudes saw it, they marvelled, and glorified God, which had given such power unto men* (Matthew 9:8). The Catholic reading takes *men* as the church's ministers, in anticipation; the plain reading takes it as the crowd's description of what they had just seen one man do. Either way, the premise stands throughout the New Testament: sin is against God (Psalm 51:4), and forgiveness is his to give (Isaiah 43:25; Micah 7:18). Whatever is later said about the church remitting sins has to be said inside that premise, and both Rome and the Reformers have always agreed that a priest or minister can at most *declare* or *convey* what God alone *does*.

That is also why the New Testament grounds forgiveness, without exception, in the cross and not in the confession. *Without shedding of blood is no remission* (Hebrews 9:22). *In whom we have redemption through his blood, the forgiveness of sins* (Ephesians 1:7). *He is the propitiation for our sins* (1 John 2:2). *Who his own self bare our sins in his own body on the tree* (1 Peter 2:24). Confession does not earn forgiveness, purchase it, or complete it. It receives it.

---

## Confession between people: the brother, the church, and restitution

Jesus does require confession to human beings, in one situation: when the sin was against them.

> Matthew 5:23 — Therefore if thou bring thy gift to the altar, and there rememberest that thy brother hath ought against thee;

> Matthew 5:24 — Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift.

The order is striking: reconciliation with the brother comes *before* the offering to God, and a worshipper who remembers an unresolved wrong is told to walk out of the temple. This is Leviticus 6 and Numbers 5 — confess, and go and settle with the person — carried into the kingdom. Its mirror image is the duty of the one wronged:

> Luke 17:3 — Take heed to yourselves: If thy brother trespass against thee, rebuke him; and if he repent, forgive him.

> Luke 17:4 — And if he trespass against thee seven times in a day, and seven times in a day turn again to thee, saying, I repent; thou shalt forgive him.

*Saying, I repent* — a spoken confession — and the answer to it is not a judgment but an obligation: *thou shalt forgive him*. Seven times a day. Peter's *till seven times?* gets *until seventy times seven* (Matthew 18:21–22). The New Testament's command to forgive one another is unconditional in a way that no human absolution ever has been, and it is tied to God's forgiveness of the forgiver: *if ye forgive not men their trespasses, neither will your Father forgive your trespasses* (Matthew 6:15).

Where a private word does not settle it, Jesus provides for escalation:

> Matthew 18:15 — Moreover if thy brother shall trespass against thee, go and tell him his fault between thee and him alone: if he shall hear thee, thou hast gained thy brother.

> Matthew 18:16 — But if he will not hear thee, then take with thee one or two more, that in the mouth of two or three witnesses every word may be established.

> Matthew 18:17 — And if he shall neglect to hear them, tell it unto the church: but if he neglect to hear the church, let him be unto thee as an heathen man and a publican.

This is the context of *whatsoever ye shall bind on earth shall be bound in heaven* in the very next verse (18:18), and it is worth noticing before that verse is discussed: the binding and loosing of Matthew 18 is the church's discipline of an unrepentant member, moving from private to semi-private to public. The whole passage is about confession *between people*, and the church enters it as the last court, not the first.

---

## The apostles' preaching

What did the apostles tell people to do about their sins? The book of Acts records the answer several times, and it is the same each time.

> Acts 2:38 — Then Peter said unto them, Repent, and be baptized every one of you in the name of Jesus Christ for the remission of sins, and ye shall receive the gift of the Holy Ghost.

> Acts 3:19 — Repent ye therefore, and be converted, that your sins may be blotted out, when the times of refreshing shall come from the presence of the Lord;

> Acts 10:43 — To him give all the prophets witness, that through his name whosoever believeth in him shall receive remission of sins.

> Acts 13:38 — Be it known unto you therefore, men and brethren, that through this man is preached unto you the forgiveness of sins:

> Acts 13:39 — And by him all that believe are justified from all things, from which ye could not be justified by the law of Moses.

> Acts 16:31 — And they said, Believe on the Lord Jesus Christ, and thou shalt be saved, and thy house.

> Acts 17:30 — And the times of this ignorance God winked at; but now commandeth all men every where to repent:

> Acts 26:20 — But shewed first unto them of Damascus, and at Jerusalem, and throughout all the coasts of Judaea, and then to the Gentiles, that they should repent and turn to God, and do works meet for repentance.

Repent, believe, be baptised; forgiveness is *through his name* and comes to *whosoever believeth*. The Philippian jailer asks the question of this document in its plainest form — *what must I do to be saved?* — and gets a one-clause answer. The word *confess* does not appear in any of these summaries of the apostolic message. That is not because confession was absent; it is because confession of sin is contained in *repent* and confession of Christ is contained in *believe on the Lord Jesus* and *be baptized in the name of Jesus Christ*. What is absent is any instruction to tell one's sins to an apostle.

The one place an apostle deals with a specific post-baptismal sin in Acts is instructive. Simon the sorcerer, already baptised (8:13), tries to buy the Spirit, and Peter tells him:

> Acts 8:22 — Repent therefore of this thy wickedness, and pray God, if perhaps the thought of thine heart may be forgiven thee.

Not *confess to me*, but *pray God*. Simon's answer — *Pray ye to the LORD for me* (8:24) — asks for intercession, which is what one believer can do for another, and is exactly what James 5:16 will command. The apostle with the keys, confronted with a baptised sinner, sends him to God and offers to pray.

The other Acts passage is Ephesus:

> Acts 19:18 — And many that believed came, and confessed, and shewed their deeds.

> Acts 19:19 — Many of them also which used curious arts brought their books together, and burned them before all men: and they counted the price of them, and found it fifty thousand pieces of silver.

This is *exomologeō* again, and it is public — *before all men* — specific — *shewed their deeds* — and costly, fifty thousand pieces of silver in the fire. It is the Jordan pattern, in a Gentile city, among people who had already believed. It shows that open confession of sin was a normal part of early Christian life, and it shows what the pattern was: not private recital to a minister but open renunciation before the church.

---

## The keys, binding and loosing, and John 20:23

Three sayings of Jesus are the foundation of the claim that the church, through its priests, forgives sins, and they must be read in full and in the Greek.

> Matthew 16:19 — And I will give unto thee the keys of the kingdom of heaven: and whatsoever thou shalt bind on earth shall be bound in heaven: and whatsoever thou shalt loose on earth shall be loosed in heaven.

> Matthew 18:18 — Verily I say unto you, Whatsoever ye shall bind on earth shall be bound in heaven: and whatsoever ye shall loose on earth shall be loosed in heaven.

> John 20:21 — Then said Jesus to them again, Peace be unto you: as my Father hath sent me, even so send I you.

> John 20:22 — And when he had said this, he breathed on them, and saith unto them, Receive ye the Holy Ghost:

> John 20:23 — Whose soever sins ye remit, they are remitted unto them; and whose soever sins ye retain, they are retained.

**What the words say.** *Bind* and *loose* were rabbinic terms for forbidding and permitting — declaring what the Law did and did not allow — and by extension for excluding from and admitting to the community. In Matthew 16 the keys are given to Peter after his confession of Christ (16:16), and the first thing Peter does with them in Acts is open the door of the kingdom by preaching, to Jews at Pentecost and to Gentiles at Caesarea. In Matthew 18 the same words are given to the disciples as a body, and the context, as shown above, is church discipline: the brother who will not hear the church is to be treated *as an heathen man and a publican*, and heaven stands behind that verdict. Neither passage mentions confession, a priest, or the forgiveness of sins.

John 20:23 does mention forgiveness, and it is the one text on which the whole edifice of sacramental confession rests. Its setting is the evening of the resurrection; the words are spoken to the gathered disciples (not to the Twelve as such — Thomas is absent, and Luke 24:33 has *them that were with them* in the room); and they follow a commission, *as my Father hath sent me, even so send I you*, and the gift of the Spirit for it. The forgiving and retaining of sins is what the sent church does in the world with the Spirit it has been given — which, as Luke's version of the same commission puts it, is *that repentance and remission of sins should be preached in his name among all nations* (Luke 24:47). Nothing in the context is about hearing confessions; the context is about going.

**The tenses.** In both Matthew sayings the Greek is a future of *to be* with a perfect passive participle — ἔσται δεδεμένον, ἔσται λελυμένον — a construction that reads most naturally as *shall have been bound*, *shall have been loosed*:

```sh
grep -P '^Matthew 16:19\t' original-languages/greek/tr-scrivener-words.tsv | grep -P 'G1210|G3089|G1510'
```

```
Matthew 16:19	13	δησης	G1210	V-AAS-2S
Matthew 16:19	17	εσται	G1510	V-FDI-3S
Matthew 16:19	18	δεδεμενον	G1210	V-RPP-NSN
```

On that reading the church's act on earth *ratifies* a verdict already reached in heaven rather than *initiating* one — the church declares bound what heaven has bound. Not every grammarian agrees that the construction carries that much weight, and the reading should be held as probable rather than proven; but it is the natural sense, and it fits the way Peter and the apostles actually used the authority in Acts.

In John 20:23 the manuscripts divide. The Textus Receptus and the Byzantine text have ἀφίενται, a present, *are remitted*; the older manuscripts have ἀφέωνται, a perfect, *have been remitted*, and the modern critical editions print it:

```sh
for e in tr-scrivener byzantine nestle1904 sblgnt sr; do grep '^John 20:23 ' original-languages/greek/$e.txt; done
```

The second half is a perfect in every edition — κεκράτηνται, *have been retained*. On the perfect reading the verse says what Matthew says: the disciples remit, and the remission turns out to have been God's already. On either reading the verb is passive. The disciples *remit*; the sins *are remitted* — by whom, the verse does not say, and the scribes of Mark 2:7 had already answered.

**The two readings.** The Catholic reading, defined at Trent (Part II), is that in John 20:23 Christ instituted the sacrament of penance, giving the apostles and their successors in the priesthood a judicial power to forgive or retain the sins of the baptised, which cannot be exercised without knowing the sins, which requires the sinner to confess them. The Protestant reading — Lutheran, Reformed, and Anglican alike — is that the verse gives the church the *ministry of the Word*: authority to proclaim forgiveness to the penitent and to declare that the impenitent remain in their sins, exercised in preaching, in baptism, in the Lord's Supper, in church discipline, and, where it is wanted, in the private assurance of forgiveness to a troubled conscience. On that reading the "power of the keys" is real — a minister who says *thy sins are forgiven* to a repentant believer speaks with heaven behind him — but it is *declarative*, and its ground is the promise of the gospel, not the completeness of the confession.

The Protestant reading is the one this document takes, for three reasons that a reader can check. First, the context of all three sayings is commission and discipline, not confession. Second, the apostles are never once shown in Acts or the Epistles hearing a private confession or pronouncing an individual absolution; they are shown preaching remission, baptising, and disciplining. Third, the one case of an apostle "forgiving" in the Epistles is Paul in 2 Corinthians 2, and it is a discipline case: the man excluded in 1 Corinthians 5 has repented, and Paul tells the church *ye ought rather to forgive him, and comfort him ... To whom ye forgive any thing, I forgive also: for if I forgave any thing, to whom I forgave it, for your sakes forgave I it in the person of Christ* (2 Corinthians 2:7, 10). The forgiveness is the *church's* — Paul joins it, he does not confer it — it is public, and its content is readmission to fellowship. That is what binding and loosing looked like when an apostle did it.

---

## James 5:16: confess your faults one to another

This is the only verse in the New Testament that commands Christians to confess sins to other Christians, and it repays reading in its paragraph.

> James 5:14 — Is any sick among you? let him call for the elders of the church; and let them pray over him, anointing him with oil in the name of the Lord:

> James 5:15 — And the prayer of faith shall save the sick, and the Lord shall raise him up; and if he have committed sins, they shall be forgiven him.

> James 5:16 — Confess your faults one to another, and pray one for another, that ye may be healed. The effectual fervent prayer of a righteous man availeth much.

**The Greek.** The verb is *exomologeisthe*, present imperative, middle: *keep on confessing openly*. The object in the Textus Receptus is τὰ παραπτώματα, *trespasses* — the KJV's *faults* is too mild — and in the critical text τὰς ἁμαρτίας, *sins*, with an *oun*, *therefore*, that ties the verse to the forgiveness of verse 15:

```sh
grep -P '^James 5:16\t' original-languages/greek/tr-scrivener-words.tsv | head -4
grep -P '^James 5:16\t' original-languages/greek/sblgnt-words.tsv | head -5
```

The decisive word is ἀλλήλοις, *to one another*, and its twin in the next clause, ὑπὲρ ἀλλήλων, *for one another*. The pronoun is reciprocal. It describes an exchange between equals — you confess to me and I confess to you, you pray for me and I for you — and it cannot describe a transaction that runs one way from layman to priest. The elders were named in verse 14, and they are told to *pray* and *anoint*; the confessing in verse 16 is not to them but *to one another*. If the verse were the charter of auricular confession it would be a strange one: it would require the priest to confess his sins to the penitent.

**What it teaches.** That confession of sin to fellow Christians is a normal, commanded part of church life; that it belongs with mutual prayer; that its purpose is *healing* — the word is *iaomai*, physical and spiritual healing both, in a paragraph about sickness — and that sin, prayer, and health are connected in a way the modern church is embarrassed to say and Paul was not (*for this cause many are weak and sickly among you*, 1 Corinthians 11:30). James is telling a congregation to be the kind of place where people can say what they have done and be prayed for. The Reformers took the verse as a warrant for exactly that, and for voluntary confession to a pastor as one form of it (Part II). It is a verse the Protestant churches have honoured more in the confessions than in practice, and Part III says so.

**What it does not teach.** It does not say *to a priest*; it does not say *all* your sins; it does not attach forgiveness to the confession — forgiveness in verse 15 comes through *the prayer of faith* and *the Lord* — and it does not describe a rite.

---

## 1 John 1:9: the Christian's ongoing confession

The verse every Protestant knows, in its paragraph:

> 1 John 1:5 — This then is the message which we have heard of him, and declare unto you, that God is light, and in him is no darkness at all.

> 1 John 1:6 — If we say that we have fellowship with him, and walk in darkness, we lie, and do not the truth:

> 1 John 1:7 — But if we walk in the light, as he is in the light, we have fellowship one with another, and the blood of Jesus Christ his Son cleanseth us from all sin.

> 1 John 1:8 — If we say that we have no sin, we deceive ourselves, and the truth is not in us.

> 1 John 1:9 — If we confess our sins, he is faithful and just to forgive us our sins, and to cleanse us from all unrighteousness.

> 1 John 1:10 — If we say that we have not sinned, we make him a liar, and his word is not in us.

> 1 John 2:1 — My little children, these things write I unto you, that ye sin not. And if any man sin, we have an advocate with the Father, Jesus Christ the righteous:

> 1 John 2:2 — And he is the propitiation for our sins: and not for ours only, but also for the sins of the whole world.

**Who is speaking to whom.** John writes to believers — *my little children* — and includes himself: *if we confess*. This is not the sinner's first confession at conversion but the Christian's continuing one, and the tense says so: ὁμολογῶμεν is a present subjunctive, *if we keep confessing*, set against the aorists of God's response, *forgive* and *cleanse*, which are single, complete acts. The Christian life, in this paragraph, is walking in the light, which means continually acknowledging what the light shows.

**What confession is set against.** Not against silence, as in Psalm 32, but against *saying* — three times: *if we say* we have fellowship while walking in darkness; *if we say* we have no sin; *if we say* we have not sinned. The alternative to confessing sin is claiming not to have any, and John calls that self-deception and, in the end, calling God a liar. Confession is simply refusing to make that claim.

**To whom.** To God: *he* is faithful and just, *he* forgives, *he* cleanses, and the *advocate with the Father* is Jesus Christ. There is no one else in the paragraph. The words *one another* in verse 7 describe the fellowship that results from walking in the light, not the direction of the confession.

**Why it works.** *Faithful and just* is the strangest pair of words in the verse. One would expect *merciful and gracious*. John says instead that God's forgiveness of the confessing Christian is a matter of his *faithfulness* — he promised — and his *justice* — the price has been paid, by *the propitiation for our sins* in 2:2, by *the blood of Jesus Christ his Son* which *cleanseth* — present tense, keeps on cleansing — in 1:7. Confession does not make God willing to forgive. It is the believer's side of a settlement already made at the cross, and God is *just* to honour it.

**What it does and does not settle.** This is the verse on which the Protestant practice of confession chiefly rests: continual, to God, in the confidence of a completed atonement. It is also the verse the Catholic tradition reads as compatible with sacramental confession, on the ground that it does not say *to God only*. That is true; it does not. But it names no one but God, and a reader who did not already know of a confessional would never guess one from it.

---

## Confessing Christ

The New Testament's other confession, and the one it ties most directly to salvation.

> Matthew 10:32 — Whosoever therefore shall confess me before men, him will I confess also before my Father which is in heaven.

> Matthew 10:33 — But whosoever shall deny me before men, him will I also deny before my Father which is in heaven.

> Luke 12:8 — Also I say unto you, Whosoever shall confess me before men, him shall the Son of man also confess before the angels of God:

> Romans 10:9 — That if thou shalt confess with thy mouth the Lord Jesus, and shalt believe in thine heart that God hath raised him from the dead, thou shalt be saved.

> Romans 10:10 — For with the heart man believeth unto righteousness; and with the mouth confession is made unto salvation.

> Romans 10:11 — For the scripture saith, Whosoever believeth on him shall not be ashamed.

> Romans 10:13 — For whosoever shall call upon the name of the Lord shall be saved.

> Philippians 2:11 — And that every tongue should confess that Jesus Christ is Lord, to the glory of God the Father.

> 1 John 4:2 — Hereby know ye the Spirit of God: Every spirit that confesseth that Jesus Christ is come in the flesh is of God:

> 1 John 4:15 — Whosoever shall confess that Jesus is the Son of God, God dwelleth in him, and he in God.

> Revelation 3:5 — He that overcometh, the same shall be clothed in white raiment; and I will not blot out his name out of the book of life, but I will confess his name before my Father, and before his angels.

Romans 10:9–10 is the only place in the Bible where the words *confess* and *saved* stand in the same sentence, and the thing confessed is not a sin but a Lord: *the Lord Jesus* — in the Greek, *Jesus as Lord*, κύριον Ἰησοῦν — and his resurrection. Paul's two clauses are not two conditions but one faith seen from inside and outside: the heart believes, the mouth says so. *With the mouth* means aloud, to people; *before men*, Jesus says, in the hearing of those who may punish it. The Gospels show what the alternative looks like — *among the chief rulers also many believed on him; but because of the Pharisees they did not confess him ... for they loved the praise of men more than the praise of God* (John 12:42–43) — and Jesus attaches to that silence the most solemn warning in the passage: *whosoever shall deny me before men, him will I also deny*. Confessing Christ is the one confession Jesus says he will answer with a confession of his own, *before my Father*.

The Epistle to the Hebrews makes this confession the thing to be *held fast*: *the Apostle and High Priest of our profession* (3:1), *let us hold fast our profession* (4:14), *let us hold fast the profession of our faith without wavering* (10:23). Timothy *professed a good profession before many witnesses* (1 Timothy 6:12) — at his baptism, most likely, which is where the church has always placed the confession of faith — and Christ himself *before Pontius Pilate witnessed a good confession* (6:13). And it is the test of a true spirit: whoever *confesseth that Jesus Christ is come in the flesh is of God* (1 John 4:2), *whosoever shall confess that Jesus is the Son of God, God dwelleth in him* (4:15).

So when someone asks whether confession is required for salvation and means *this* confession, the New Testament's answer is yes, without hedging — not as a work added to faith, but because a faith that will not say its Lord's name in public is, on Jesus' own account, a faith he will not own. The thief said it from a cross. The Christian says it at baptism, in the creed, and whenever it costs something.

---

## One mediator, one high priest, a priesthood of all

If confession of sin is to God, the question is how the sinner gets there. The New Testament's answer is the most direct thing in it.

> 1 Timothy 2:5 — For there is one God, and one mediator between God and men, the man Christ Jesus;

> Hebrews 4:14 — Seeing then that we have a great high priest, that is passed into the heavens, Jesus the Son of God, let us hold fast our profession.

> Hebrews 4:15 — For we have not an high priest which cannot be touched with the feeling of our infirmities; but was in all points tempted like as we are, yet without sin.

> Hebrews 4:16 — Let us therefore come boldly unto the throne of grace, that we may obtain mercy, and find grace to help in time of need.

> Hebrews 7:25 — Wherefore he is able also to save them to the uttermost that come unto God by him, seeing he ever liveth to make intercession for them.

> Hebrews 10:19 — Having therefore, brethren, boldness to enter into the holiest by the blood of Jesus,

> Hebrews 10:22 — Let us draw near with a true heart in full assurance of faith, having our hearts sprinkled from an evil conscience, and our bodies washed with pure water.

> 1 John 2:1 — My little children, these things write I unto you, that ye sin not. And if any man sin, we have an advocate with the Father, Jesus Christ the righteous:

*Come boldly.* *Draw near.* *Boldness to enter into the holiest.* The Old Testament sinner could not go past the priest; Hebrews says the Christian walks into the Holy of Holies, because the veil is torn and the high priest is Christ. Under the Law the priest's job was to stand between; under the gospel that job has been done, once, by the one person qualified to do it, and *he ever liveth* to keep doing it. The Christian who confesses sin to God is not bypassing the priest. He is going to him.

The New Testament never calls a Christian minister a priest. The word *priest* occurs in 157 verses of the KJV New Testament, and every one refers to the Jewish priesthood, to pagan priests, to Christ, or to the whole body of believers:

> 1 Peter 2:5 — Ye also, as lively stones, are built up a spiritual house, an holy priesthood, to offer up spiritual sacrifices, acceptable to God by Jesus Christ.

> 1 Peter 2:9 — But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light:

> Revelation 1:6 — And hath made us kings and priests unto God and his Father; to him be glory and dominion for ever and ever. Amen.

This is the Reformation's *priesthood of all believers*, and it is Peter's phrase before it is Luther's. Every Christian has the access the priest once had. That does not mean no Christian can help another — the Bible is full of one person praying for another's sin: Abraham for Abimelech (Genesis 20:7), Moses for Israel (Exodus 32:30–32), Samuel for the people who asked for a king (1 Samuel 12:19, 23), Job for his friends (Job 42:8–10), Peter for Simon (Acts 8:22–24), and *one for another* in James 5:16. But in every case the helper *prays*; none of them absolves. The prophet or apostle who stands beside the sinner faces the same direction the sinner does.

---

## Confession and salvation: putting the texts together

Set out in order, the New Testament's account of how a person is saved runs like this.

**The ground** is Christ's death: *a propitiation through faith in his blood* (Romans 3:25), *the just for the unjust, that he might bring us to God* (1 Peter 3:18). Nothing the sinner does, including confessing, adds to it.

**The means** is faith: *a man is justified by faith without the deeds of the law* (Romans 3:28); *to him that worketh not, but believeth on him that justifieth the ungodly, his faith is counted for righteousness* (4:5); *by grace are ye saved through faith; and that not of yourselves: it is the gift of God: not of works* (Ephesians 2:8–9); *not by works of righteousness which we have done, but according to his mercy he saved us* (Titus 3:5).

**Faith turns.** Jesus' first sermon is *repent ye, and believe the gospel* (Mark 1:15); Peter's is *repent, and be baptized* (Acts 2:38); God *now commandeth all men every where to repent* (Acts 17:30); *godly sorrow worketh repentance to salvation* (2 Corinthians 7:10). Repentance is not a second condition alongside faith; it is the shape faith takes in a sinner. And repentance cannot happen in a person who denies being a sinner: *if we say that we have no sin, we deceive ourselves* (1 John 1:8). The publican's *God be merciful to me a sinner* is what repentance sounds like, and it is a confession.

**Faith speaks.** *With the mouth confession is made unto salvation* (Romans 10:10). Faith that will not confess Christ is faith Christ will not confess (Matthew 10:33).

**Faith keeps confessing.** The believer walks in the light and keeps confessing (1 John 1:7, 9), not to be justified again but because fellowship with a God who is light means continual honesty, and because sin unconfessed does to a Christian what it did to David — bones, drought, a heavy hand. The blood keeps cleansing.

**Faith settles with people.** *First be reconciled to thy brother* (Matthew 5:24); restitution to the one wronged (Luke 19:8); *confess your faults one to another* (James 5:16); the offender who will not hear the church is put out, and the one who repents is forgiven and comforted by the church (2 Corinthians 2:7).

Now hold that account against the question. Is confession required for salvation? Confession of Christ: yes, as the voice of faith. Confession of sin to God: yes, as the voice of repentance, without which there is no faith. Confession of sin to the person wronged: yes, as the fruit of repentance, so that Jesus sends the unreconciled worshipper away from the altar. Confession of sin to other believers: commanded, for healing and prayer, and neglected at a cost — but not, in any text, made the condition of forgiveness. Confession of sin to a priest as the condition of forgiveness: not commanded, not described, not implied by any text read in context, and contradicted by the pattern of every confession Scripture records God accepting.

That last clause is the one Trent anathematised, and Part II shows how the church got from the texts above to that anathema.

---

## What every tradition agrees Scripture teaches

Before the history, it is worth listing what is not in dispute between Rome, the East, and the Reformation, because it is most of the subject.

1. **Sin is against God, and only God forgives it.** No tradition holds that a priest forgives sin by his own power; every absolution formula in every rite says, in one form or another, that God does it.
2. **Confession of sin to God is required of every Christian, always.** The Catholic Church teaches that a perfect act of contrition, made to God, obtains forgiveness even of mortal sin before the sacrament is received, provided the penitent intends to confess (Catechism 1452); the Orthodox teach that the confession is made to Christ, with the priest as witness.
3. **Confession must be joined to repentance and to forsaking the sin.** Proverbs 28:13 is everyone's verse.
4. **Where a sin has wronged a person, it must be confessed to that person and put right.** Restitution is a Catholic obligation of the sacrament and a Protestant obligation of repentance.
5. **Confession of Christ before men is bound to salvation.** Romans 10:9–10 and Matthew 10:32 are read the same way everywhere.
6. **The church has real authority to declare forgiveness and to exclude the impenitent.** Every tradition has a form of absolution and a form of discipline.
7. **God accepts the confession of a person who has no access to any minister.** The thief on the cross is everyone's exception, and every tradition provides for him — Rome in *baptism of desire* and *perfect contrition*, the Reformation in the sufficiency of faith.

What is disputed is narrower than the argument usually sounds: whether confession *to a priest* is, for sins after baptism, the ordinary and divinely instituted condition of forgiveness. That is the question Part II follows through history.

---
---

# Part II — What the Church Has Done

## The first century after the apostles

The earliest Christian writings outside the New Testament speak of confession often, and always in the same two settings: to God, and in the assembly.

The **Didache** (late first or early second century), a church manual, instructs: *In the assembly you shall confess your transgressions, and you shall not come to your prayer with an evil conscience* (4:14), and, of the Lord's Day: *gather together, break bread and give thanks, having first confessed your transgressions, that your sacrifice may be pure* (14:1). The **Epistle of Barnabas** (early second century) has the same rule in almost the same words: *You shall confess your sins. You shall not go to prayer with an evil conscience* (19:12). **1 Clement** (c. 96), writing from Rome to Corinth, says it is *better for a man to confess his transgressions than to harden his heart* (51:3), and its examples of confession are Moses and David confessing to God. **Ignatius of Antioch** (c. 110) writes that *the Lord forgives all who repent, if their repentance brings them back to the unity of God and the council of the bishop* (Philadelphians 8).

What these show is confession as a corporate, public act before the Sunday eucharist — the Jordan and Ephesus pattern — with the bishop's council as the place where a repentant sinner is received back. What they do not show is any private recital of sins to a presbyter. That practice is not mentioned by anyone in the first two centuries, and the silence is not from lack of interest in the subject.

**The Shepherd of Hermas** (mid-second century) introduces the idea that would govern the next four hundred years: that after baptism there is *one* repentance for grave sin, and only one (Mandate 4.3). The church's problem was not how to hear confessions but whether to readmit serious sinners at all, and how often.

---

## Public penance: the one repentance

By the third century the church had an institution, called in Greek *exomologesis* — the word of James 5:16 — and it was public, severe, and, in principle, once in a lifetime.

**Tertullian** describes it around 203 in *On Repentance*: the penitent in sackcloth and ashes, fasting, groaning, *prostrating before the presbyters and kneeling before the beloved of God*, asking the whole congregation to pray for him (ch. 9). He knows it is dreaded — *most men either shun this work, as being a public exposure of themselves, or else put it off from day to day* — and argues that shame before the brethren is a small price for pardon (ch. 10). The confession is made to the church, and the church prays; forgiveness is God's.

**Origen**, around 240, lists seven ways sins are forgiven under the gospel — baptism, martyrdom, almsgiving, forgiving others, converting a sinner, abundance of love, and last, *the hard and laborious remission of sins through penance, when the sinner washes his couch with tears ... and does not blush to make known his sin to the priest of the Lord and to seek the remedy* (Homilies on Leviticus 2.4). This is the earliest clear reference to disclosing sin to a priest, and it is a disclosure made in order to be admitted to public penance — Origen elsewhere advises choosing carefully the physician to whom one shows one's wound, since he may judge it needs to be brought before the assembly (Homilies on Psalm 37, 2.6).

**Cyprian** of Carthage, after the Decian persecution of 250 had produced thousands of Christians who had sacrificed to idols, insisted in *On the Lapsed* (251) that they confess before the church and receive the laying-on of hands from bishop and clergy before returning to communion, and urged even those with merely inward faults to confess *while confession can still be received, while the satisfaction and remission made through the priests is pleasing to the Lord* (chs. 28–29). Cyprian is the first to speak of remission *through the priests*, and it is in the context of the church's public readmission of the lapsed.

**Augustine**, writing around 421, distinguishes the grave sins that require public penance from the daily ones that do not, and names the remedy for the latter: *for the daily, brief, and light sins without which this life is not lived, the daily prayer of the faithful makes satisfaction* — the Lord's Prayer, *forgive us our debts* (Enchiridion 71). Confession of ordinary sin, for Augustine, is the fourth petition, prayed every day. **Chrysostom** (d. 407) goes further in the direction of God alone, and is quoted by every Protestant apologist since: *I do not bring you into a theatre of your fellow-servants ... show your wounds to the Lord, the best of physicians ... confess to God, who does not reproach* (Homilies on Hebrews 31, on 12:14, and often elsewhere). Chrysostom knew of public penance and administered it; what he taught the ordinary Christian to do with ordinary sin was to tell God.

Three things had settled by 450. Public penance was real, humiliating, and rare — many — the Emperor Constantine among them — delayed baptism itself, in part to avoid ever needing it. Ordinary sins were dealt with by prayer, almsgiving, and the Lord's Prayer. And no one had yet required private confession to a priest of anyone. In 459 **Leo the Great** actually forbade the reading aloud of penitents' sins in church, as a custom *contrary to apostolic rule*, and said it *suffices that the guilt of consciences be made known to the priests alone in secret confession* (Letter 168). His concern was to protect the penitent from exposure; the effect was to move the disclosure from the assembly into the priest's ear.

---

## From the Irish monasteries to the confessional

Private, repeatable, tariffed confession — the thing the word *confession* now usually means — is an Irish invention of the sixth and seventh centuries, and it is one of the clearest cases in church history of a practice that everyone now assumes to be ancient having a datable and local origin.

The Irish church was monastic, and in the monasteries a monk confessed his faults regularly to a senior monk, his *anmchara* or soul-friend, and received a penance. The practice spread from monks to laity. Manuals called **penitentials** — of Finnian (c. 550), of Columbanus (c. 600), of Cummean (c. 650), and, once the practice reached England, of Theodore of Canterbury (c. 700) — list sins with a fixed tariff of fasting or other penance for each: so many days for this, so many years for that. Confession under this system was private, to a priest or monk, could be repeated as often as one sinned, and was followed by a penance proportioned to the sin, after which reconciliation was given. Columbanus and the Irish missionaries carried it to Gaul and the Continent, where it spread through the seventh and eighth centuries against some resistance: the Council of Chalon-sur-Saône (813) notes that *some say sins should be confessed to God alone, others think they should be confessed to priests*, and says both are done *with great fruit in the holy church*. By the ninth century the Irish system had largely replaced the old public penance in the West.

Two things followed. The tariffs made confession look like a court — an offence, a sentence — and the vocabulary of the later doctrine (the priest as *judge*, absolution as a *judicial act*) grew out of that. And the penance, originally performed *before* reconciliation, came to be performed *after* it, so that the priest's absolution rather than the completed penance became the moment of forgiveness. By the twelfth century the theologians were working out what exactly the absolution did; **Thomas Aquinas** (d. 1274) defended the indicative formula, *I absolve you*, over the older deprecative *May God absolve you*, and it became the Latin form.

---

## Lateran IV and Trent: confession becomes law

**The Fourth Lateran Council** (1215), canon 21, made annual confession a legal obligation for the first time:

> All the faithful of both sexes, after they have reached the age of discretion, shall faithfully confess all their sins at least once a year to their own priest, and perform to the best of their ability the penance imposed, receiving reverently at least at Easter the sacrament of the Eucharist ... otherwise they shall be barred from entering a church during their lifetime and deprived of Christian burial at death.

*All their sins*; *to their own priest*; *at least once a year*; on pain of excommunication. This is the point at which private confession went from a widespread practice to a condition of membership, and it is the law the Reformers three centuries later called a tyranny over conscience. The same canon binds the priest to absolute secrecy, the origin of the seal of confession.

**The Council of Trent**, Session 14 (25 November 1551), replied to the Reformers by defining the doctrine, and its definitions are still the Catholic position:

- Penance is a sacrament, instituted by Christ in John 20:23 (chapter 1).
- Its parts are contrition, confession, and satisfaction on the penitent's side, and absolution on the priest's, and absolution is *a judicial act* in which the priest pronounces sentence *as a judge* (chapters 3, 6).
- *Entire confession of sins* to a priest is *necessary by divine law* for all who have sinned mortally after baptism, because a judge cannot pass sentence on what he does not know; every mortal sin must be confessed *by species and number*, with its circumstances (chapter 5).
- Canon 6: *If anyone denies that sacramental confession was instituted or is necessary to salvation by divine law; or says that the manner of confessing secretly to a priest alone ... is foreign to the institution and command of Christ, and is a human invention, let him be anathema.*
- Canon 7: *If anyone says that in the sacrament of penance it is not necessary by divine law for the remission of sins to confess each and all mortal sins which are remembered after due and diligent examination ... let him be anathema.*

The Catechism of the Catholic Church (1992) restates it: confession to a priest is *an essential part of the sacrament* (1456); a Catholic who has reached the age of discretion is *bound to confess serious sins at least once a year* (1457); confession of venial sins is *strongly recommended* but not required (1458); and perfect contrition, out of love for God, *obtains forgiveness of mortal sins if it includes the firm resolution to have recourse to sacramental confession as soon as possible* (1452). The last provision is the thief on the cross, made into a rule.

It is worth being exact about what Rome claims and does not claim. It does not claim the priest forgives by his own power; the absolution invokes God. It does not claim confession to a priest is the only way God ever forgives; it claims it is the way Christ instituted for the baptised who sin gravely, so that refusing it when it is available is refusing Christ's provision. And it claims that this was instituted in John 20:23 and practised from the beginning — which is the historical claim Part II has been testing, and which the evidence of the first five centuries does not support.

---

## The East

The Orthodox churches confess to a priest, and have since the same early-medieval period, but their theology of it is different enough to notice. The priest is described as a *witness*, not a judge; the penitent confesses before an icon of Christ, to Christ, with the priest standing beside; and the Greek form of absolution is deprecative — *May God, who pardoned David through Nathan the prophet ... pardon you ... through me a sinner* — the priest praying for the penitent's forgiveness rather than pronouncing it. The Russian church adopted an indicative formula, *I, an unworthy priest, by the power given me, forgive and absolve you*, from Peter Mohyla's service book of 1646, under Latin influence, and Orthodox writers have argued about it since. Orthodoxy has no tariffs, no *species and number*, and no defined doctrine that confession is necessary for the forgiveness of a given category of sin; it has a strong practice of confession before communion and of the *spiritual father* to whom one opens one's life. The East, in short, kept the third-century shape — the church as the place of confession and the priest as the one who prays — better than the West did, and its practice is closer to Origen than to Trent.

---

## The Reformation: what was rejected and what was kept

The Reformers did not abolish confession. It is the most persistent misunderstanding of what they did, and the confessions and catechisms they wrote say the opposite in plain words.

**Luther** attacked three things: the obligation (Lateran IV's *once a year to your own priest*), the enumeration (Trent's *species and number*, already the practice), and the doctrine that the absolution's validity depended on the completeness of the confession and the sufficiency of the penance, rather than on the promise of Christ. He kept private confession and absolution, and wanted it used. The **Small Catechism** (1529) has a section titled *How the unlearned should be taught to confess*:

> Confession embraces two parts: one is that we confess our sins; the other, that we receive absolution, or forgiveness, from the confessor, as from God himself, and in no wise doubt, but firmly believe, that our sins are thereby forgiven before God in heaven. What sins should we confess? Before God we should plead guilty of all sins, even of those which we do not know, as we do in the Lord's Prayer. But before the confessor we should confess those sins only which we know and feel in our hearts.

The **Large Catechism**'s *Brief Exhortation to Confession* (1529) is blunter: *If you are a Christian, you need neither my compulsion nor the pope's command at any point, but you will compel yourself and beg me for the privilege of sharing in it ... When I urge you to go to confession, I am simply urging you to be a Christian.* Luther's objection was to confession as a *law*; his practice was confession as a *gift*, and he went to confession himself throughout his life.

The **Augsburg Confession** (1530), the founding document of the Lutheran churches, Article XI:

> Of Confession they teach that private absolution ought to be retained in the churches, although in confession an enumeration of all sins is not necessary. For it is impossible according to the Psalm: "Who can understand his errors?"

And Article XXV: *Confession in the churches is not abolished among us; for it is not usual to give the body of the Lord, except to them that have been previously examined and absolved.* The Psalm is 19:12, quoted in Part I. Lutheran hymnals to this day contain an order for *Individual Confession and Absolution*.

**Calvin** attacked the same three things and more sharply. The third book of the *Institutes* (chapter 4) argues that the Lateran requirement, imposed by Innocent III, is a tyranny over consciences, that enumeration is impossible and its demand a torture of consciences, that the "power of the keys" is the preaching of the gospel, and that Scripture commands confession to God, to the person wronged, and to the church, but nowhere to a priest as such. Then he says this (3.4.12):

> Let every believer remember that if he is privately troubled and afflicted with a sense of his sins, so that without outside help he is unable to free himself from them, it is his duty not to neglect what the Lord has provided in the way of remedy: namely, that, for his relief, he should use private confession to his own pastor, and for his solace, he should beg the private help of him whose duty it is, both publicly and privately, to comfort the people of God by the gospel teaching.

Calvin also instituted a *general confession* — the whole congregation confessing sin together at the start of worship, in set words, followed by a declaration of pardon — first at Strasbourg and then at Geneva, on the model of Nehemiah 9. That is the form of confession most Reformed and Presbyterian congregations still practise every Sunday, and most of their members do not know they are doing what Calvin ordered.

**The Church of England** kept the most. The *Book of Common Prayer* opens Morning and Evening Prayer with a *General Confession* — *We have erred, and strayed from thy ways like lost sheep. We have followed too much the devices and desires of our own hearts. We have offended against thy holy laws* — followed by an *Absolution* in which the priest declares that God *hath given power, and commandment, to his Ministers, to declare and pronounce to his people, being penitent, the Absolution and Remission of their sins*. Before communion, the exhortation tells anyone who *cannot quiet his own conscience* to *come to me, or to some other discreet and learned Minister of God's Word, and open his grief; that by the ministry of God's holy Word he may receive the benefit of absolution*. And in the Visitation of the Sick: *Here shall the sick person be moved to make a special confession of his sins, if he feel his conscience troubled with any weighty matter*, after which the priest, *if he humbly and heartily desire it*, absolves him with the Latin form: *by his authority committed to me, I absolve thee from all thy sins*. The Thirty-Nine Articles (XXV) deny that penance is a sacrament of the gospel, and the Homily of Repentance (1563) denies that anyone is bound to the numbering of his sins to a priest; but the private confession remains, on the principle Anglicans put in a sentence: *all may, none must, some should*.

**The Westminster Confession** (1646), the standard of the Presbyterian churches, chapter 15, *Of Repentance unto Life*, section 6:

> As every man is bound to make private confession of his sins to God, praying for the pardon thereof; upon which, and the forsaking of them, he shall find mercy: so, he that scandalizeth his brother, or the church of Christ, ought to be willing, by a private or public confession, and sorrow for his sin, to declare his repentance to those that are offended, who are thereupon to be reconciled to him, and in love to receive him.

Three confessions: to God (always), to the brother (when wronged), to the church (when the sin is public) — the three cases Part I found in Scripture, and no fourth. Chapter 30 adds that the keys are given to *church officers*, who *have power ... to retain, and remit sins* by discipline and absolution, in the declarative sense.

What every one of these documents rejects is the same short list: that confession to a priest is a sacrament instituted by Christ; that it is necessary for the forgiveness of sins; that all sins must be enumerated; that the priest's absolution is a judicial sentence; and that penance satisfies for sin. What every one of them keeps is also the same list: confession to God, daily; confession to the wronged; confession to the church for public sin; general confession in worship, with a declaration of pardon; and — in the Lutheran and Anglican churches explicitly, in Calvin's Geneva by pastoral provision — private confession to a minister, voluntary, for the troubled conscience, with an absolution grounded in the gospel.

---

## Since the Reformation

The Protestant churches that came later kept less, but not nothing.

**The Methodist band meeting** was John Wesley's mechanism for James 5:16. The *Rules of the Band Societies* (25 December 1738) required members to meet weekly and answer, each in turn: *What known sins have you committed since our last meeting? What temptations have you met with? How were you delivered? What have you thought, said, or done, of which you doubt whether it be sin or not?* It was mutual, lay, and confidential, and it was the closest thing Protestantism has produced to a discipline of regular confession among equals.

**The Puritan and Reformed pastoral tradition** produced a literature of *cases of conscience* — how a minister should counsel a troubled sinner — that assumed people would come to their pastor with specific sins, and that the pastor's job was to apply the promises of the gospel to them: Calvin's 3.4.12 as a working practice.

**The free churches** — Baptist, Congregational, and later the Pentecostal and independent churches — dropped set forms of confession, general or private, and relied on the public testimony, the altar call, the prayer meeting, and church discipline. Confession in these churches is real and often very public, but it is unstructured, and it depends on a culture that many congregations have lost.

**Dietrich Bonhoeffer**, a Lutheran, wrote the modern Protestant case for confession to a brother in *Life Together* (1939), in a chapter called *Confession and Communion*: *He who is alone with his sin is utterly alone.* Sin wants to remain unknown, he argued, and in the fellowship of pious Christians it can; confessing it to one brother breaks the isolation, makes the forgiveness concrete, and is the only way most people will ever know they have been forgiven *by God* rather than by themselves. His rule was that the brother who hears the confession should be one who himself confesses, so that no one becomes a priest over another.

**The Twelve Steps** (1939) are a Protestant-derived confession discipline that most Protestants do not recognise as one. The Oxford Group, from which Alcoholics Anonymous took its method, was an evangelical movement built on the practice of *sharing* — confessing sin to another person — and Step Five preserves it: *Admitted to God, to ourselves, and to another human being the exact nature of our wrongs.* The three addressees are, in order, 1 John 1:9, 1 John 1:8, and James 5:16.

---

## So is there really no mechanism?

The premise of the question — that the Protestant churches have no mechanism for confession — is true of one thing and false of several.

It is true that no Protestant church has a *sacrament* of confession: a rite instituted by Christ, necessary for forgiveness, administered by a priest as judge. And it is true that in most Protestant congregations there is no confessional, no scheduled hour, and no expectation that anyone will ever tell their sins to the pastor. A Protestant who feels the lack is feeling something real.

But it is false that the Protestant churches have no *provision* for confession. Every one of them has, on paper and in its founding documents:

| Form | Where it is found | Scriptural basis |
| --- | --- | --- |
| Daily confession to God, in the Lord's Prayer and in private | Every tradition; Augustine's *daily satisfaction*; Luther's *before God ... all sins, even those we do not know* | 1 John 1:9; Psalm 32:5; Matthew 6:12 |
| General confession in public worship, with a declaration of pardon | Lutheran, Anglican, Reformed, Presbyterian, Methodist liturgies; Calvin's Strasbourg and Geneva orders; the Prayer Book | Nehemiah 9:2–3; Daniel 9; 1 Kings 8:47 |
| Confession to the person wronged, with restitution | Westminster 15.6; every catechism on the Fifth to Tenth Commandments | Numbers 5:7; Matthew 5:23–24; Luke 19:8 |
| Confession to one another, for prayer and healing | Wesley's bands; Bonhoeffer; accountability groups; Step Five | James 5:16; Galatians 6:1–2 |
| Private confession to a minister, voluntary, with absolution | Lutheran *Individual Confession and Absolution*; Anglican *open his grief*; Calvin's *private confession to his own pastor* | James 5:16; John 20:23 read declaratively |
| Public confession to the church, and readmission after discipline | Westminster 15.6 and 30; Matthew 18 process in every polity | Matthew 18:15–17; 2 Corinthians 2:5–11; 1 Timothy 5:20 |

The honest Protestant complaint is not that these do not exist but that most of them have been allowed to lapse. Many congregations have dropped the general confession as too formal; few members know that their pastor would hear a private confession, and fewer pastors have said so; the band meeting is a historical curiosity; and church discipline is rare enough to be news. Bonhoeffer's chapter was written because his own church had the doctrine and not the practice. A Protestant who says "we have no confession" is usually describing their congregation accurately and their tradition inaccurately, and the remedy is closer than a change of church.

---
---

# Part III — Is Confession Required for Salvation?

## The answer, in three parts

The question has to be split, because the word covers three things and Scripture answers each differently.

### 1. Confessing Christ: yes

> Romans 10:9 — That if thou shalt confess with thy mouth the Lord Jesus, and shalt believe in thine heart that God hath raised him from the dead, thou shalt be saved.

Saving faith speaks. It is not that a silent believer is saved by faith and then does an extra thing called confessing to finish the job; it is that a faith which will not say *Jesus is Lord* where it can be heard is not the faith the New Testament describes, and Jesus says he will not confess it (Matthew 10:33). The believers of John 12:42–43 who *did not confess him* because they *loved the praise of men more than the praise of God* are not commended for their private faith.

This is the confession made at baptism, said in the creed, and tested whenever the name of Christ costs something. It is required in the way that breathing is required of a living body — not as a condition imposed from outside but as the sign of what is inside. And it is the only confession that Scripture puts in the same sentence as the word *saved*.

### 2. Confessing sin to God: yes

> Luke 18:13 — And the publican, standing afar off, would not lift up so much as his eyes unto heaven, but smote upon his breast, saying, God be merciful to me a sinner.

> 1 John 1:8 — If we say that we have no sin, we deceive ourselves, and the truth is not in us.

No one is saved without repentance (Luke 13:3; Acts 17:30), and no one repents without agreeing with God that they have sinned. That agreement, spoken, is confession. It is the publican's sentence, the prodigal's *I have sinned*, the thief's *we indeed justly*, David's four words to Nathan. It is required not as a work — Psalm 32 is Paul's proof-text for righteousness *without works* — but as the end of pretending, and God has made it the smallest possible thing: *only acknowledge thine iniquity* (Jeremiah 3:13).

Three things follow that a troubled conscience needs to hear. It does not need to be complete: *who can understand his errors? cleanse thou me from secret faults* (Psalm 19:12), and Luther's *before God we should plead guilty of all sins, even of those which we do not know*. It does not need to be eloquent or long: seven words justified the publican. And it does not persuade God of anything: *thou forgavest* comes in Psalm 32 at the resolve, before the words, because forgiveness *is with him* (Psalm 130:4) and the price was paid before the sinner was born. Confession to God is required the way opening a hand is required to receive a gift.

For the Christian, this confession continues. *If we confess our sins* is present tense and addressed to *my little children*. It does not re-justify — the believer is not un-saved between one sin and the next confession, or the thief would have been lost between his cross and his death — but it keeps the fellowship honest, and Psalm 32:3–4 describes what happens to a believer who stops.

### 3. Confessing sin to a priest: no

Nothing in Scripture requires it, describes it, or implies it. The texts appealed to say something else in their contexts: John 20:23 is the commission of the sent church to proclaim remission, exercised in Acts by preaching, baptising, and discipline, never by hearing a private confession; James 5:16 commands confession *to one another*, reciprocally, for prayer and healing, and names the elders in the previous verse as those who *pray* and *anoint*, not those who absolve; Matthew 16 and 18 concern the kingdom's door and the church's discipline. Every confession Scripture records God accepting was made to God, or to Christ, or to the wronged party; the one confession made to priests was Judas's. The New Testament has *one mediator* (1 Timothy 2:5), one *high priest* (Hebrews 4:14), and a *royal priesthood* of all believers (1 Peter 2:9), and tells the Christian to *come boldly unto the throne of grace* (Hebrews 4:16). The early church confessed publicly, before the assembly; private confession to a priest is a sixth-century monastic practice that became a law in 1215 and a dogma in 1551.

This is the answer of every Reformation confession, and it is the one this document reaches from the texts. It is also the position Trent anathematises, and a reader should know that a serious and ancient church says the opposite. But the question asked was what *the Bible* says, and on that question the Reformers were right: confession to a priest is not a requirement of salvation, because it is not a requirement of Scripture.

**The whole answer in one sentence:** salvation requires the confession that faith makes — of Christ before men, and of sin before God — and the repentance that confession voices; it does not require the recital of sins to a priest, and it is not withheld from anyone who has no priest to go to.

---

## Confession to people: the three cases Scripture commands

Saying that confession to a priest is not required is not the same as saying that confession to human beings is optional. Scripture commands it in three cases, and a Protestant who has escaped the confessional has not escaped these.

**To the person you wronged, with restitution.** Numbers 5:7: *they shall confess their sin ... and give it unto him against whom he hath trespassed.* Matthew 5:24: *first be reconciled to thy brother.* Luke 19:8: *I restore him fourfold.* If your sin took something from someone — money, reputation, trust, time — confession to God does not close the account; you go to them, say what you did, and make it right where it can be made right. Jesus rates this above worship. It is the confession Protestants most often skip, because it is the one that costs the most.

**To one another, for prayer and healing.** James 5:16 is a command, its verb is present tense, and its logic is that sin hidden makes you sick and sin spoken lets a brother pray for you. This is not a command to broadcast; *one another* means a Christian you trust, who will pray and keep the confidence and confess to you in turn. Galatians 6:1–2 is the same duty from the other side: *ye which are spiritual, restore such an one in the spirit of meekness ... bear ye one another's burdens.* Bonhoeffer's argument stands: most Christians who have never told a single person a single sin have never quite believed they are forgiven, because they have never heard it from outside their own head. Proverbs 28:13 does not say *to whom*; but a man who has told no one is usually still *covering*.

**To the church, when the sin is public or persistent.** Matthew 18:15–17 moves a sin from private to public only when the sinner refuses to hear; 1 Timothy 5:20 says *them that sin rebuke before all*, of sins that are already known; 2 Corinthians 2:5–11 shows the church forgiving and receiving a man whose sin had been dealt with publicly. Public confession is for public sin, or for private sin that has become a scandal, and its purpose is the restoration of the sinner and the peace of the church. Westminster 15.6 is the rule: *he that scandalizeth his brother, or the church of Christ, ought to be willing, by a private or public confession ... to declare his repentance to those that are offended, who are thereupon to be reconciled to him, and in love to receive him.*

None of these three is a condition of forgiveness. All three are fruits of repentance, and a repentance that refuses them is suspect on Scripture's own terms — *whoso confesseth and forsaketh*.

---

## What confession is not

**Not penance.** Nothing the sinner does after confessing pays for the sin. *Without shedding of blood is no remission* (Hebrews 9:22), and the blood was shed. Restitution repairs a wrong to a neighbour; it does not satisfy God, whose satisfaction is Christ. The Reformers' quarrel with *satisfaction* was not with making amends but with the idea that amends are owed to God after Calvary.

**Not a way of earning or unlocking forgiveness.** Psalm 32 puts the forgiveness at the resolve to confess, and Paul chooses that Psalm to illustrate righteousness *without works*. If confession were a work it would be the wrong illustration.

**Not a feeling.** *Godly sorrow worketh repentance to salvation ... but the sorrow of the world worketh death* (2 Corinthians 7:10). Judas felt terrible. Saul wept. Pharaoh said *I have sinned* twice. The test of a confession is what follows it, not how it felt.

**Not an enumeration.** *Who can understand his errors?* The demand to remember and list every sin is a demand Scripture never makes, and Augsburg XI names the Psalm that forbids it. Confess what you know; ask cleansing for what you do not.

**Not public self-exposure.** The Bible's public confessions — the Jordan, Ephesus, Nehemiah 9 — were corporate and general, or were confessions of sins already public. Nothing in Scripture requires a Christian to announce private sin to a congregation, and Leo the Great forbade the practice as *contrary to apostolic rule*. James's *one another* is one other.

**Not to be repeated for the same forgiven sin.** *If our heart condemn us, God is greater than our heart* (1 John 3:20). A sin confessed and forsaken is removed *as far as the east is from the west* (Psalm 103:12) and cast *into the depths of the sea* (Micah 7:19); confessing it again is not humility but unbelief in the verse that promised the first time. The next section is about this.

---

## A shape for confession in a church without a confessional

What follows is not a rite. It is the practice that the texts of Part I and the Reformers of Part II describe, put in order, for a Christian who wants to do what Scripture says and has no one to tell them how.

**Daily, and in the Lord's Prayer.** *Forgive us our debts* (Matthew 6:12) is a confession, prayed every day, and Augustine and Luther both took it as the ordinary Christian's ordinary confession. Pray it meaning it. Add, when there is something particular, the particular thing.

**Specific.** *I acknowledged my sin unto thee* — *my* sin, the thing itself. *That he hath sinned in that thing* (Leviticus 5:5). Achan named the garment and the silver. A general sense of unworthiness is not a confession; it is often a way of avoiding one. Name what you did.

**Promptly.** Psalm 32:3–4 is a clinical description of a delayed confession: bones, roaring, drought, a heavy hand. The gap between the sin and the confession is where the damage is done. David waited a year and it took a prophet.

**With forsaking.** *Whoso confesseth and forsaketh.* Confession without the intention to stop is the thing Proverbs 28:13 says will not prosper. If you are not yet willing to forsake it, confess that too; God can be told the truth about the unwillingness.

**With restitution, where there is anyone to make it to.** The Law's rule was the principal plus a fifth, to the person, on the day. Do the equivalent. If it is impossible — the person is dead or unreachable — say so to God and let it go; the Law provided for that case too, and sent the restitution to the LORD (Numbers 5:8).

**In faith.** *He is faithful and just to forgive.* End the confession by believing the verse, not by inspecting your feelings. The publican *went down to his house justified*; he did not stay in the temple to see whether it had worked.

**With a brother, when you are alone with it.** Find one Christian — the same sex, older in the faith if possible, discreet, and someone who confesses too — and tell them the thing you have told no one. Ask them to pray for you, out loud, then and there. This is James 5:16. Wesley's four questions are as good a form as any: what known sins, what temptations, how delivered, what doubtful things. If the church has a small group or a band or an accountability pair, use it; if it does not, two people are enough.

**With the pastor, if the conscience will not settle.** Calvin's rule: if you are *privately troubled and afflicted with a sense of your sins, so that without outside help you are unable to free yourself*, go to your own pastor and ask them to hear you and to tell you, from the gospel, that you are forgiven. A Lutheran pastor has a form for this in the hymnal; an Anglican priest has the Visitation office; a Presbyterian or Baptist pastor has no form but has the same authority to declare the promise, and most would be glad to be asked. Say plainly that you want to confess something and to hear the gospel spoken to it. *All may, none must, some should.*

**In the assembly, together.** If your church has a general confession, pray it, and hear the declaration of pardon as addressed to you. If it does not, Nehemiah 9 and Daniel 9 and 1 Kings 8:47 are the pattern, and a pastor who reads this document could restore it in a Sunday.

**Once.** Then stop. See the next section.

---

## When you cannot stop confessing the same sin

Some Christians confess the same forgiven sin for years, and the confessional in the churches that have it is as full of them as the prayer closet in the churches that do not. Scripture speaks to it.

The sin is forgiven. *As far as the east is from the west, so far hath he removed our transgressions from us* (Psalm 103:12). *I will forgive their iniquity, and I will remember their sin no more* (Jeremiah 31:34). *All his transgressions that he hath committed, they shall not be mentioned unto him* (Ezekiel 18:22). These are not descriptions of a forgiveness that has to be refreshed. The blood *cleanseth* — present, continuous — and the advocate *ever liveth*.

The thing you are feeling is not conviction. Conviction names a sin and points to the cross; what you are feeling names a sin and points back at itself. *If our heart condemn us, God is greater than our heart, and knoweth all things* (1 John 3:20) — John wrote that sentence for exactly this, and it means that your heart is not the final court.

Confess the unbelief instead. The one sin actually in play is not believing 1 John 1:9 the first time. Say so, once, and then take the promise on the terms it is offered, which do not include feeling forgiven.

And tell someone. This is the case above all others for James 5:16 and for Calvin's *private confession to his own pastor*: a conscience that cannot hear the gospel from inside needs to hear it from outside, from a brother or a minister who says, on Christ's authority, *thy sins are forgiven*. That is the power of the keys in its Protestant sense, and it exists for you.

---

## For the Catholic or Orthodox reader

This document reaches a Protestant conclusion and says so. Three things should be said to a reader from a church that confesses to a priest.

First, nothing here suggests that confession to a priest is wrong, useless, or unbiblical in the sense of being forbidden. Scripture commands confession to God, to the wronged, to one another, and to the church, and a priest is a Christian, a brother, and a minister of the church; confessing to him is one way of doing several things Scripture commands, and Calvin and the Prayer Book say as much. What the document denies is that Scripture *requires* it, or makes forgiveness *depend* on it.

Second, the practice your church has, and most Protestant churches have let lapse, is something Scripture wants Christians to have in some form. A Protestant who reads Part II honestly should be less inclined to congratulate his tradition and more inclined to find a brother.

Third, the question of whether the absolution is *judicial* or *declarative* — whether the priest passes sentence or announces a verdict — is real, but it is a question about the minister, not about the penitent. The penitent's part is the same in both: to say what he did, to God, and to believe he is forgiven for Christ's sake. On that, Trent and Westminster and the Prayer Book and the publican all agree.

---
---

# Appendices

## A. Every verse in the KJV that contains "confess"

Forty-four verses. The Hebrew and Greek forms are from [`original-languages/`](original-languages); *hithpael* is the reflexive form of יָדָה that means *confess sin*, *hiphil* the causative form that ordinarily means *praise* or *give thanks*.

```sh
grep -i 'confess' kjv/kjv.txt
```

| Reference | Word | Who confesses | To whom | What |
| --- | --- | --- | --- | --- |
| Leviticus 5:5 | יָדָה hithpael | the guilty Israelite | the LORD | *that he hath sinned in that thing*; then the offering |
| Leviticus 16:21 | יָדָה hithpael | Aaron, the high priest | over the scapegoat | *all the iniquities of the children of Israel* |
| Leviticus 26:40 | יָדָה hithpael | Israel in exile | God | *their iniquity, and the iniquity of their fathers* |
| Numbers 5:7 | יָדָה hithpael | the one who wronged a neighbour | — | *their sin*; then restitution to the neighbour |
| Joshua 7:19 | תּוֹדָה | Achan | *unto him* (God); told to Joshua | what he had done |
| 1 Kings 8:33 | יָדָה hiphil | Israel, defeated | God | *thy name* — praise, acknowledgement |
| 1 Kings 8:35 | יָדָה hiphil | Israel, in drought | God | *thy name*; *turn from their sin* |
| 2 Chronicles 6:24 | יָדָה hiphil | Israel | God | *thy name* |
| 2 Chronicles 6:26 | יָדָה hiphil | Israel | God | *thy name* |
| 2 Chronicles 30:22 | יָדָה hithpael | the people at Hezekiah's Passover | *the LORD God of their fathers* | with peace offerings; confession or thanksgiving |
| Ezra 10:1 | יָדָה hithpael | Ezra, weeping | God, *before the house of God* | the people's sin |
| Ezra 10:11 | תּוֹדָה | the returned exiles | *the LORD God of your fathers* | with separation from the foreign wives |
| Nehemiah 1:6 | יָדָה hithpael | Nehemiah | God | *the sins of the children of Israel ... both I and my father's house* |
| Nehemiah 9:2 | יָדָה hithpael | the assembly, standing | God | *their sins, and the iniquities of their fathers* |
| Nehemiah 9:3 | יָדָה hithpael | the assembly | God | a fourth of the day, with the Law read |
| Job 40:14 | יָדָה hiphil | God (to Job) | Job | *that thine own right hand can save thee* — acknowledgement |
| Psalms 32:5 | יָדָה hiphil | David | *unto the LORD* | *my transgressions*; *thou forgavest* |
| Proverbs 28:13 | יָדָה hiphil | *whoso* | — | *his sins*, with forsaking; *shall have mercy* |
| Daniel 9:4 | יָדָה hithpael | Daniel | *the LORD my God* | the nation's sin |
| Daniel 9:20 | יָדָה hithpael | Daniel | God | *my sin and the sin of my people Israel* |
| Matthew 3:6 | ἐξομολογέω | the crowds at the Jordan | in public, at baptism | *their sins* |
| Matthew 10:32 | ὁμολογέω | *whosoever*; Christ | *before men*; *before my Father* | Christ; the confessor |
| Mark 1:5 | ἐξομολογέω | *all the land of Judaea* | in public, at baptism | *their sins* |
| Luke 12:8 | ὁμολογέω | *whosoever*; the Son of man | *before men*; *before the angels of God* | Christ; the confessor |
| John 1:20 | ὁμολογέω | John the Baptist | the priests and Levites | *I am not the Christ* |
| John 9:22 | ὁμολογέω | (anyone) | the synagogue | *that he was Christ* |
| John 12:42 | ὁμολογέω | the chief rulers (did *not*) | — | Christ |
| Acts 19:18 | ἐξομολογέω | Ephesian believers | publicly, *before all men* | *their deeds* |
| Acts 23:8 | ὁμολογέω | the Pharisees | — | resurrection, angel, spirit |
| Acts 24:14 | ὁμολογέω | Paul | Felix | his worship of God *after the way which they call heresy* |
| Romans 10:9 | ὁμολογέω | *thou* | *with thy mouth* | *the Lord Jesus*; *thou shalt be saved* |
| Romans 10:10 | ὁμολογέω | *man* | *with the mouth* | *confession is made unto salvation* |
| Romans 14:11 | ἐξομολογέω | *every tongue* | *to God* | acknowledgement at the judgment |
| Romans 15:9 | ἐξομολογέω | Christ (quoting Psalm 18:49) | *among the Gentiles* | praise |
| Philippians 2:11 | ἐξομολογέω | *every tongue* | — | *that Jesus Christ is Lord* |
| 1 Timothy 6:13 | ὁμολογία | Christ | *before Pontius Pilate* | *a good confession* |
| Hebrews 11:13 | ὁμολογέω | the patriarchs | — | *that they were strangers and pilgrims* |
| James 5:16 | ἐξομολογέω | believers | *one to another* | *your faults* (trespasses); with prayer, for healing |
| 1 John 1:9 | ὁμολογέω | *we* (believers) | God (*he is faithful and just*) | *our sins* |
| 1 John 4:2 | ὁμολογέω | *every spirit* of God | — | *that Jesus Christ is come in the flesh* |
| 1 John 4:3 | ὁμολογέω | the spirit of antichrist (does *not*) | — | the same |
| 1 John 4:15 | ὁμολογέω | *whosoever* | — | *that Jesus is the Son of God* |
| 2 John 1:7 | ὁμολογέω | deceivers (do *not*) | — | *that Jesus Christ is come in the flesh* |
| Revelation 3:5 | ἐξομολογέω | Christ | *before my Father, and before his angels* | *his name* — the overcomer's |

Of the 44, twenty are confessions of sin (fifteen Old Testament, five New), sixteen are confessions of Christ or of a belief, and eight are acknowledgement or praise of God. Of the twenty confessions of sin, every one that names an addressee names God, the public assembly, or *one another*; none names a priest as the hearer.

---

## B. Every "I have sinned" in the KJV

```sh
grep 'I have sinned' kjv/kjv.txt
```

| Reference | Who | To whom | What followed |
| --- | --- | --- | --- |
| Exodus 9:27 | Pharaoh | Moses and Aaron | hardened his heart again (9:34–35) |
| Exodus 10:16 | Pharaoh | Moses and Aaron | *forgive ... my sin only this once*; hardened again (10:20) |
| Numbers 22:34 | Balaam | the angel of the LORD | *if it displease thee, I will get me back*; went on |
| Joshua 7:20 | Achan | Joshua, and *unto* God | full confession; executed |
| 1 Samuel 15:24 | Saul | Samuel | *because I feared the people*; the kingdom taken |
| 1 Samuel 15:30 | Saul | Samuel | *yet honour me now, I pray thee, before the elders* |
| 1 Samuel 26:21 | Saul | David | *I have played the fool*; David fled to Gath |
| 2 Samuel 12:13 | David | Nathan, of *the LORD* | *The LORD also hath put away thy sin* |
| 2 Samuel 19:20 | Shimei | David | pardoned by David, for the day |
| 2 Samuel 24:10 | David | the LORD | *take away the iniquity of thy servant*; the plague, then the altar |
| 2 Samuel 24:17 | David | the LORD | *these sheep, what have they done?*; the plague stayed |
| 1 Chronicles 21:8 | David | God | the parallel of 2 Samuel 24:10 |
| Job 7:20 | Job | God | *what shall I do unto thee?* — a protest as much as a confession |
| Job 33:27 | *any* who will say it (Elihu) | God | *He will deliver his soul from going into the pit* |
| Psalms 41:4 | David | the LORD | *heal my soul* |
| Micah 7:9 | the prophet for Zion | the LORD | *I will bear the indignation ... until he plead my cause* |
| Matthew 27:4 | Judas | the chief priests | *What is that to us?*; hanged himself |
| Luke 15:18 | the prodigal (rehearsed) | *my father* | — |
| Luke 15:21 | the prodigal (delivered) | his father | the robe, the ring, the calf |

---

## C. A timeline

| Date | Event |
| --- | --- |
| c. 1400s BC | Leviticus 5, 6, 16, 26 and Numbers 5: confession with offering and restitution; the high priest's confession over the scapegoat |
| c. 1000 BC | David's confession to Nathan; Psalms 32 and 51 |
| c. 960 BC | Solomon's prayer: *We have sinned, and have done perversely, we have committed wickedness* |
| 539 BC | Daniel 9 |
| 458–445 BC | Ezra 9–10; Nehemiah 1 and 9 |
| c. AD 27 | John's baptism in the Jordan: *confessing their sins* |
| AD 30 | Resurrection evening: *whose soever sins ye remit* (John 20:23) |
| c. AD 55 | 2 Corinthians 2: the Corinthian church forgives the disciplined man |
| c. AD 57 | Romans 10:9–10 |
| c. AD 90 | 1 John 1:9 |
| c. 100 | Didache 4:14; 14:1: confess in the assembly before the eucharist |
| c. 140 | Shepherd of Hermas: one repentance after baptism |
| c. 203 | Tertullian, *On Repentance*: public *exomologesis* |
| c. 240 | Origen: seven ways of forgiveness, the last *making known his sin to the priest* |
| 251 | Cyprian, *On the Lapsed* |
| c. 400 | Chrysostom: *show your wounds to the Lord* |
| c. 421 | Augustine, Enchiridion 71: the Lord's Prayer as daily satisfaction for daily sins |
| 459 | Leo the Great forbids public reading of sins; secret confession to the priest suffices |
| c. 550–700 | Irish penitentials: Finnian, Columbanus, Cummean, Theodore |
| 813 | Council of Chalon: confession to God alone and confession to priests both practised *with great fruit* |
| 1215 | Lateran IV, canon 21: annual confession of all sins to one's own priest, on pain of excommunication |
| c. 1270 | Aquinas defends *I absolve you* |
| 1519–20 | Luther's *Sermon on the Sacrament of Penance* and *Babylonian Captivity* |
| 1529 | Luther's Small and Large Catechisms, with the *Exhortation to Confession* |
| 1530 | Augsburg Confession XI and XXV: private absolution retained; enumeration not required |
| 1536–59 | Calvin's *Institutes* 3.4 |
| 1549–1662 | Book of Common Prayer: General Confession and Absolution; *open his grief*; the Visitation of the Sick |
| 1551 | Trent, Session 14: confession to a priest necessary by divine law; anathemas |
| 1563 | Homily of Repentance |
| 1646 | Westminster Confession 15.6 and 30; Mohyla's Trebnik gives the Russian church an indicative absolution |
| 1738 | Wesley's *Rules of the Band Societies* |
| 1939 | Bonhoeffer, *Life Together*; the Twelve Steps published |
| 1992 | Catechism of the Catholic Church 1422–1498 |

---

## D. Where the traditions stand

| | **Confession to God** | **General confession in worship** | **Private confession to a minister** | **Required for forgiveness?** | **Form of absolution** |
| --- | --- | --- | --- | --- | --- |
| **Roman Catholic** | Required; perfect contrition forgives, with intent to confess | Penitential rite at Mass (not sacramental) | Sacrament of Penance; priest as judge | Yes, for mortal sin after baptism, by divine law (Trent) | *I absolve you* (indicative) |
| **Orthodox** | Required; the confession is to Christ | Pre-communion prayers | Before a priest as witness; spiritual father | Ordinary practice; not defined as Trent defines it | *May God forgive you* (deprecative; Russian use also indicative) |
| **Lutheran** | Required; daily, *even of those we do not know* | Yes; corporate confession and absolution | Individual Confession and Absolution retained and commended; voluntary | No; absolution is the gospel applied | *I forgive you all your sins* (indicative, declarative) |
| **Anglican** | Required | General Confession and Absolution at every office | *All may, none must, some should*; Visitation form | No (Article XXV) | Declarative at the office; indicative in the Visitation |
| **Reformed / Presbyterian** | Required; *upon which, and the forsaking of them, he shall find mercy* | Calvin's general confession and declaration of pardon | To one's own pastor, for the troubled conscience (Institutes 3.4.12); to the church for scandal | No; keys are declarative (Westminster 30) | Declaration of pardon |
| **Baptist / free church** | Required | Usually none set | Pastoral counsel; no form | No | None; the gospel preached |
| **Methodist / Wesleyan** | Required | Prayer of confession in the liturgy | Historically the band meeting; class leaders | No | Declaration of pardon |
| **Pentecostal** | Required | Altar call; public testimony | Informal | No | None; the gospel preached |

---

## E. Honest caveats

**The historical quotations are from standard editions and from a knowledge of those texts,** not from a fresh reading of each; a reader building an argument on one should check it in a printed edition. This applies especially to the fathers (Tertullian, Origen, Cyprian, Chrysostom, Leo), whose words are given in the standard English translations and whose chapter references follow those editions, and to the councils and confessions, which are quoted from the usual English texts. Dates before 300 are approximate.

**The grammatical argument from the future perfect** in Matthew 16:19 and 18:18 (*shall have been bound*) is widely made and, this document thinks, sound, but it is disputed by competent grammarians, and the case against sacramental confession does not depend on it. The manuscript variant in John 20:23 is reported from the editions in this repository; the reading is not in serious doubt, but the older reading, ἀφέωνται, is not the one behind the KJV.

**The Catholic position is stated from its own documents,** but a Catholic reader would add two things this document does not develop: that the church's authority to develop doctrine means a practice need not be found fully formed in the New Testament to be Christ's institution, and that Scripture is read within Tradition rather than alone. Those are real differences of method, and they, more than any single text, are why the argument does not end. This document answers the question as it was asked — what *the Bible* says — and states the Protestant conclusion as its own.

**The Orthodox account is flattened.** Practice varies between the Greek, Russian, and other churches, and between monasteries and parishes.

**The Protestant account is generous to the confessions and hard on the congregations,** and that is deliberate: the founding documents say what they say, and most congregations do not do it. But there are Lutheran and Anglican parishes where private confession is normal, Reformed churches that practise discipline faithfully, and free churches where confession among members is a living thing, and none of that is captured by a table.

**This document takes a position, and states it.** On the biblical evidence, confession to a priest is not a requirement of salvation or of forgiveness; confession to God, to the wronged, to one another, and to the church are all commanded; and confessing Christ is bound to salvation as tightly as believing in him. Where the evidence is thinner than the conclusion, the text says so.

**Nothing here is pastoral counsel for a particular person.** Someone in acute distress over a sin needs a pastor, a friend, and sometimes a doctor, more than they need an argument. Part III is written to be usable by such a person and is not a substitute for those things.

---

## F. Further reading

**Primary — read these first, in this order:**

1. **Psalm 32 and Psalm 51** — the two confessions, the one Paul chose and the one David wrote
2. **Luke 15:11–32 and 18:9–14** — the prodigal and the publican
3. **1 John 1:5–2:2** — the Christian's confession, in its paragraph
4. **James 5:13–20** — the only command to confess to one another, in its paragraph
5. **Romans 10:1–13** — the confession that is *unto salvation*
6. **Matthew 18:15–35** — the brother, the church, the keys, and the unforgiving servant, in one chapter
7. **John 20:19–23** with **Luke 24:44–49** — the commission, in both accounts
8. **Nehemiah 9 and Daniel 9** — corporate confession, entire
9. **Leviticus 5–6 and 16** — the Law's confessions, with the offering and the restitution

**Confessional texts, all short and freely available:** Augsburg Confession XI and XXV, with Apology XI–XII; Luther's Small Catechism, *Confession*, and the Large Catechism's *Brief Exhortation to Confession*; Calvin, *Institutes* 3.4 (the whole chapter, an afternoon); the Book of Common Prayer's Morning Prayer, the exhortation before Communion, and the Visitation of the Sick; Westminster Confession 15 and 30; Trent, Session 14 (chapters 1–9, canons 1–15); Catechism of the Catholic Church 1422–1498. Reading the actual texts is the fastest cure for the caricatures on every side.

**Histories:** Henry Charles Lea, *A History of Auricular Confession and Indulgences in the Latin Church* (1896), the classic Protestant account, exhaustive and hostile; Bernhard Poschmann, *Penance and the Anointing of the Sick* (1964), the standard Catholic history, candid about the development; John T. McNeill and Helena Gamer, *Medieval Handbooks of Penance* (1938), the Irish penitentials in translation, which is where private confession can be watched being invented.

**On confession among Protestants:** Dietrich Bonhoeffer, *Life Together* (1939), chapter 5, *Confession and Communion* — twenty pages, and the best modern Protestant treatment; John Wesley, *Rules of the Band Societies* (1738), one page.

**Related material in this repository:**

- [`kjv/`](kjv) — the full King James text, greppable by reference
- [`original-languages/`](original-languages) — the Hebrew and Greek behind every word discussed here, with Strong's numbers and parsing
- [`once-saved-always-saved.md`](once-saved-always-saved.md) — on assurance, and on what the New Testament says about a believer who sins; Part III of that document and Part III of this one are written for the same reader
- [`romans-7-study.md`](romans-7-study.md) — the Christian and indwelling sin, which is what makes 1 John 1:9 a daily verse
- [`progressive-sainthood.md`](progressive-sainthood.md) — sanctification, of which confession is the ordinary maintenance
- [`faith-vs-works-living-christian-letter.txt`](faith-vs-works-living-christian-letter.txt) — faith and works, the question underneath *is confession a work?*
- [`praying-for-the-dead.md`](praying-for-the-dead.md) — on purgatory and satisfaction, which grew from the same medieval root as the doctrine of penance
- [`fasting-in-the-bible.md`](fasting-in-the-bible.md) — Daniel 9, Jonah 3, and Joel 2, where confession and fasting are one act

---

*Scripture quoted from the King James Version (1769), public domain in the United States, as carried in [`kjv/kjv.txt`](kjv/kjv.txt) in this repository; every quotation was taken directly from that file. Hebrew and Greek words, parsing, and Strong's numbers are from [`original-languages/`](original-languages), and every count and form stated was produced from those files by the commands shown. Patristic, conciliar, and confessional sources are quoted in standard English editions and are named where used; see [Appendix E](#e-honest-caveats).*
