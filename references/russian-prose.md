# Russian Prose: Word Order, Aspect, and the Traditions That Shape the Sentence

> Purpose: supply the instruments Russian actually uses — word order, aspect, the period, the narrator's licence — so that Russian prose is written in Russian rather than assembled from translated English rules.
> Read when: you are writing in Russian, revising a Russian draft, or judging whether a Russian text has been flattened by translation.
> Related: `references/prose-engineering.md` — the language-neutral layer this file re-instruments; `references/multilingual-notes.md` — what transfers between languages and what does not; `references/narrative-theory.md` §9–10 — остранение and heteroglossia, the theory behind §7; `references/english-prose.md` — the defaults not to import.

*Everything here is `[theory]` — craft and literary history, not measurement. There is one `[hypothesis]` tag, in §10, and no `[data]` claims: none of the five studies behind this skill contains Russian material.*

## Contents

1. [Why a translated rulebook fails](#why-a-translated-rulebook-fails)
2. [Word order as information structure](#word-order-as-information-structure)
3. [Aspect as pacing](#aspect-as-pacing)
4. [Sentence and period](#sentence-and-period)
5. [Narrator and comment](#narrator-and-comment)
6. [Skaz and voice](#skaz-and-voice)
7. [Psychologism](#psychologism)
8. [Dialogue punctuation and typography](#dialogue-punctuation-and-typography)
9. [Diminutives, particles, and the untranslatable](#diminutives-particles-and-the-untranslatable)
10. [Genre expectations in Russian](#genre-expectations-in-russian)
11. [A revision checklist for Russian](#a-revision-checklist-for-russian)
12. [Links](#links)

## Why a translated rulebook fails

English craft advice is built on English's constraints: a fixed subject position, articles that mark definiteness, stress-timed rhythm, and a strong prohibition on comma splices. None of those constraints exist in Russian in the same form. Applied literally, the advice produces **translationese** — text that is grammatical Russian and audibly not Russian. The markers are consistent enough to audit:

- **Over-explicit pronouns.** English needs a subject in every clause; Russian does not. *Он вошёл в комнату. Он сел. Он закурил.* is three English sentences wearing Russian words. Russian chains the verbs and drops the subject: *Он вошёл в комнату, сел, закурил.* The repeated pronoun is the single loudest tell, because it is never a mistake — it is a structural habit imported wholesale.
- **Analytic word order.** English order (subject, verb, object, adverbial last) imposed where Russian would move a word to the front or the end for emphasis. The result is syntactically correct and informationally flat: every sentence has the same shape and the same focus position, so nothing is emphasised anywhere.
- **Flattened intonation.** English marks emphasis with stress and with constructions (*it was X that…*); Russian marks it with position. A translator who renders the English emphasis word-for-word imports the stress into a language that does not put it there, and the sentence reads as though nobody meant anything by it.
- **Loss of aspect.** *He was reading when she came in* becomes *Он читал, когда она вошла* — which happens to be right — but the next sentence, *he read the letter and put it down*, comes out as *он читал письмо и клал его*, two imperfectives, because the translator was tracking English tense rather than Russian aspect, and the scene loses the event. Aspect is a decision, not a correspondence.
- **`который` chains.** English relative clauses calque into stacked relatives: *дом, который стоял на углу, который был построен ещё при отце, который…* Russian prefers a participial phrase, an apposition, or a new sentence. Two `который` in one sentence is a warning; three is a translation.
- **Calqued constructions.** *имеет место* (takes place), *является* as a copula (*это является проблемой* — Russian says *это проблема*), *в рамках* (within the framework of), *на сегодняшний день* (today), *данный* (this/given), *осуществлять* (carry out), *не секрет, что*, *стоит отметить*. Each has a Russian verb or a bare noun that does the same job in half the words.
- **Overuse of the passive.** *Было принято решение* where Russian says *решили*. The passive is legal and sometimes right; the reflex is bureaucratic, and it removes the agent that Russian prose usually keeps.
- **`было` as a crutch.** *Было холодно. Было темно. Было слышно, как…* The impersonal construction is native and often the best choice. It becomes a crutch when scene-setting defaults to it, because every sentence then begins with the same two syllables and no sentence has an actor.

**A pair.** The material: a man comes home, the house is cold, his wife has left a note.

*Translationese: Он открыл дверь и вошёл в дом. В доме было холодно и темно. Он прошёл на кухню и увидел записку на столе. Он взял записку и прочитал её. Она писала, что ушла к матери. Он сел на стул и долго смотрел в окно.*

*Russian: Дверь он открыл сам — ключ повернулся тяжело, с той зимней заминкой, которую так и не исправили. В доме пахло остывшей золой. На кухне, на клеёнке, лежала записка, придавленная солонкой, чтобы не улетела: ушла к маме, не жди. Он сел, не снимая пальто, и сидел так, пока за окном не стало совсем темно.*

Six differences, each one an instrument:

| Translationese | Russian | What changed |
|---|---|---|
| *Он открыл дверь* | *Дверь он открыл сам* | Object fronted, *сам* added: the sentence now answers a question (who opened it, and did anyone help), so it has a focus. |
| *Он… Он… Он…* | one subject, then verb chains | Pronouns dropped where Russian does not need them; the paragraph gains speed. |
| *было холодно и темно* | *пахло остывшей золой* | A sense that implies absence — cold ash means the stove went out hours ago — replaces two adjectives that state it. |
| *Она писала, что ушла* | *ушла к маме, не жди* | Reported speech becomes the note's own words, without a reporting clause. Russian does this far more readily than English. |
| *долго смотрел в окно* | *сидел так, пока за окном не стало совсем темно* | Imperfective duration with a terminal clause: the time passes *inside* the sentence instead of being summarised after it. |
| *на столе* | *на клеёнке… придавленная солонкой* | Two material nouns carry the household. Not decoration: the salt cellar is why the note is still there. |

## Word order as information structure

Russian word order is free in the grammatical sense and strict in the informational sense. Because there are no articles and no fixed subject position, **position is the main focus mechanism**: the last position in the sentence is the rheme (what is new), the first is the theme (what is given). Default subject-verb-object is therefore not neutral — it is a choice that puts the object in focus, and a paragraph where every sentence does it has no emphasis at all.

**Three pairs, neutral and marked.** Each pair is the same content at two settings, and the second is not a prettier version of the first; it answers a different question.

1. *Он вернулся в город.* — neutral; the city is the news, so the sentence answers *where did he go?* / *В город вернулся он.* — marked; the person is the news, and the sentence answers *who came back?* A third possibility, *В город он вернулся*, marks the return instead: *did he come back?*
2. *Ночь была тёмной.* — neutral; the instrumental predicate is the unmarked form. / *Тёмная была ночь.* — marked; the adjective is fronted and the copula trails it, which is colloquial, evaluative, and at home in skaz (§6). *Была тёмная ночь* keeps the standard order but opens on the copula, which is why it drifts toward the *было*-crutch of §1: the sentence begins with existence and the description has nowhere to land.
3. *Дом стоял на краю деревни.* — neutral; the house is given, the edge of the village is the news. / *На краю деревни стоял дом.* — marked; the sentence introduces the house, so the village is the ground and the house is what arrives.

All of these are idiomatic. They are not stylistic variants of one sentence; they are sentences about different things. Write the one whose final word is the thing you want the reader holding.

**Inversion is emphasis, and it must be earned.** Moving a word out of its neutral place is a marked move, and marked moves lose their force when repeated. A paragraph with three inversions has no emphasis, exactly as a paragraph with three exclamation marks has no exclamation. Keep one marked order per paragraph, and let the rest run neutral.

**The test for whether a sentence sounds Russian.** Read it aloud and ask where the new information is. If it is not at the end, and there is no visible reason for it to be elsewhere, the sentence is probably English in Russian clothes. The second test: can you move any word without the sentence becoming wrong? If nothing can move, the order is fixed by grammar rather than chosen for information, and the sentence is probably a calque.

**The chain, not the sentence.** The unit that has to be planned is the theme–rheme chain across a paragraph, because a sentence's final word becomes the next sentence's given material. If each sentence's rheme becomes the next sentence's theme, the paragraph reads as a walk; if the rhemes are unrelated, the paragraph reads as a list; if the same theme is repeated with a new rheme each time, the paragraph reads as an inventory of one thing. Plan two or three sentences at a time and check the joins, not just the sentences:

> *В комнате стоял шкаф. Шкаф был старый. Старик открыл его и достал папку. В папке лежали фотографии.* — chained: cabinet, cabinet, folder, folder. Each sentence picks up the last word of the previous one.

That chain is clear and slightly plodding, and Russian usually breaks it by changing what the sentence is *about*: *Папка оказалась тяжёлой* keeps the folder as the theme but makes the weight the news, and the paragraph stops sounding like a relay of last words. The alternation of chained and re-themed sentences is what the paragraph-level rhythm of Russian prose actually is.

**A second paragraph-level instrument: the paragraph's last word.** Russian paragraphs often end on a nominal phrase that stands alone as a fragment, because the language tolerates verbless sentences far more readily than English. *И тишина.* / *И ничего.* A one- or two-word paragraph is a legitimate Russian closing beat, and it is used more often — and more quietly — than the English equivalent, which would need a beat of narration around it.

**The subject-initial run.** The commonest rhythmic failure in Russian prose written by a model, or by a translator, is not a wrong word but a repeated position: sentence after sentence, and especially paragraph after paragraph, beginning with the subject, usually a pronoun. *Он открыл дверь. Он приложил вывод. Он нашёл issue.* The verb ending already names the person; the pronoun adds nothing but a metronome. Count the paragraphs that begin with *он / она / они*: if more than one in five does, the prose has a pulse you did not choose.

Repair it without changing what the paragraph says: front the adverbial (*В четверг он поставил spark*), begin on the object (*Тикет он закрыл*), use a dash construction (*Бэкап — в час ночи*), or let a verbless sentence carry the beat. Two caveats. A pronoun in the first sentence of a paragraph is normal — it re-establishes the subject after a break. And deliberate anaphora (*Он ждал. Он знал. Он не спал.*) is a device, not a defect. The test is whether the repetition does work; if you cannot say what work in one line, it is a tic.

A page of short declaratives with no periodic sentence anywhere is the other half of the same problem: the prose reads as a report, and in Russian specifically as a translated one. The two checks belong together — vary the opening *and* build one long sentence where it carries a complex thought.

## Aspect as pacing

Aspect is usually taught as a grammar problem to be got right. It is better understood as the main instrument of **duration** in Russian, and it does at the verb what sentence length does in English: it tells the reader whether to dwell or to move.

- **Perfective** — the action is bounded, whole, an event: *он выпил* (he drank it, done), *она вошла* (she came in), *письмо пришло* (the letter arrived).
- **Imperfective** — the action is a process, a duration, a habit, or a repeated fact: *он пил* (he was drinking, or he used to drink), *она входила* (she was coming in, or she used to come in), *письма приходили* (letters kept arriving).

The same scene, two aspects, two experiences:

*Он вошёл, сел, достал бумаги, разложил их, прочитал первый лист.* Five perfectives. The reader receives five completed events of equal weight, briskly, with no duration anywhere. This is a legitimate effect — bureaucratic, forensic, a man performing a procedure — and it is a *choice*. Left uniform for a whole scene, it becomes mechanical, because nothing is dwelt on and nothing has weight.

*Он вошёл и сел. Бумаги он доставал долго, раскладывал их по краю стола, потом читал первый лист, и было слышно, как в коридоре кто-то ходит.* Two perfectives to get him in and seated, then imperfectives for the papers and the reading. The imperfectives open duration, and the duration is where the scene's pressure lives: he is stalling, and the footsteps in the corridor are why. The aspect change *is* the pacing.

**Sequences that feel mechanical when aspect is uniform.** Four or more perfectives in a row produce a list of completed actions; four or more imperfectives in a row produce a scene where nothing happens and time pools. Both are usable, both are traps when they are the default. The audit is simple: mark the main verb of every sentence in the scene П (perfective) or Н (imperfective), and read the string. `П П П П` is a procedure; `Н Н Н Н` is a mood; a scene usually needs both, and the switch between them is where the reader feels the story change gear.

**Three further uses worth knowing.**

- **Negation changes the meaning of the choice.** *Он не читал эту книгу* — he never read it. *Он не прочитал эту книгу* — he did not finish it. The perfective negation implies an attempt; the imperfective does not.
- **The imperative encodes duration.** *Сядь* — sit down, one act. *Сиди* — stay seated, a state to be maintained. The difference is not politeness; it is what the speaker wants the body to do.
- **Imperfective presents make a scene cinematic.** *Он идёт по улице, никого не трогает, и вдруг…* The imperfective present holds the camera on a continuous action, which is why it is the standard opening of an anecdote and the standard way to make a described action feel simultaneous with the telling.

## Sentence and period

Russian tolerates longer, more hypotactic sentences than modern English, and it does so because its participles and деепричастия (verbal adverbs) can carry subordinate action without a new clause. That tolerance is an instrument, not a licence.

**A period that works**, because every clause adds delay and the delay is the point:

*Он вышел на улицу, где ещё с ночи лежал снег, присыпанный сверху серой кашей из-под колёс, и долго стоял у ворот, глядя, как дворник, сгорбившись, скребёт тротуар, и думал, что теперь ему некуда идти.*

One main clause (*вышел… и стоял… и думал*), one relative clause, one participial phrase, two деепричастия. The syntax enacts the character's inability to move: the sentence will not end because he will not leave. If the same syntax carried a plot event — a chase, an arrest — it would be sludge, because the reader would be waiting for the event while the sentence admired the snow.

**Sludge**, same grammar, no reason:

*Будучи назначенным на должность, о которой он давно мечтал и которая, как ему казалось, была создана специально для него, он, прибыв на место и ознакомившись с делами, обнаружил, что…*

The sentence's real verb, *обнаружил*, arrives after two subordinate constructions and a parenthetical, and everything before it is a justification rather than an action. The rule that separates the two examples: **a participle or деепричастие is a device when it frames the main action; it is sludge when it replaces it.** If the most important thing that happens in the sentence appears as a деепричастие, rewrite the sentence and put that thing in the main clause.

**The Russian short sentence lands harder than the English one**, and the reason is distributional. Russian prose runs longer on average, so a three-word sentence has more contrast behind it. *Свет погас.* after a period is not a beat in a rhythm; it is a stop. Use the short sentence where the scene needs finality, and do not use it as punctuation — a page of short sentences in Russian reads as a telegram, which is a voice, and must be chosen as one.

**Two syntactic habits English forbids and Russian uses freely.** Sentences may begin with *И* and *А* (*И вот он пришёл*, *А она молчала*), which English style treats as a fault and Russian treats as a narrative connector. And the dash can replace a copula or introduce an explanation (*Дом — это было всё, что осталось*), which lets Russian make an assertion without the verb *to be* that Russian does not have in the present tense anyway.

## Narrator and comment

The Russian tradition grants the narrator a licence that Anglo-American workshop prose mostly withholds: the right to comment, digress, generalise, and address the reader. Pushkin's digressions in *Евгений Онегин* are the canonical instance; the essayistic chapters of *Война и мир* are the extreme; the skaz narrators of Leskov and Zoshchenko are the comic version. The licence is real, and importing the Anglo suspicion of it into Russian produces a narrator who is not allowed to think — which Russian readers experience as thinness, not restraint.

**The distinction that keeps it from becoming an essay: a narrator with an attitude versus an author with an opinion.**

- A narrator with an attitude has a **position in the story**: they were there, they knew someone, they have a stake, they may be wrong. Their comment is a move in the narrative, not a pause in it.
- An author with an opinion has a **thesis and no stake**. The comment cannot be wrong, cannot cost anything, and cannot be contradicted by the story, because it is the story's frame rather than its content.

**Two operational tests.**

1. **Can the narrator be wrong?** If the generalisation cannot be falsified by anything later in the text, it is an essay in the middle of a story. Give the narrator a blind spot and let the story exploit it.
2. **Why now?** A digression must be triggered by the scene — the funeral reminds the narrator of a joke, and the joke has to be told badly, at the wrong moment, which is what makes it a fact about the narrator rather than about jokes. A digression with no trigger is the author changing the subject.

**Avoiding the author's essay.** Write the comment in the narrator's lexicon (§6) and let it contain one thing the narrator would not want admitted. A generalisation that flatters the narrator is the author speaking; a generalisation that exposes the narrator is the narrator speaking.

## Skaz and voice

**Skaz** (сказ) is narration in a spoken idiom — the tale told in a character's or a subculture's oral register, with the narrator visible as a performer rather than transparent. Leskov's *Левша*, Babel's *Конармия*, Zoshchenko's feuilletons, and much of Soviet anecdotal prose belong to it. In skaz the telling is part of the subject: the narrator's idiom is a character, and the gap between what they say and what happened is where the story lives.

**The danger is pastiche.** A register adopted as costume produces a text where every sentence performs, the reader hears the performance rather than a person, and after a page the idiom has become a noise. The specific failure is a narrator who is *charmingly* unreliable — wrong about everything in a way that is always funny — because charm is not a position.

**How to hold an oral register over three thousand words:**

- **The narrator must be less informed than the story.** They misunderstand, embellish, get names and causes wrong, and defend themselves. The information gap is the engine; remove it and skaz becomes dialect comedy.
- **The register must break once.** At the point where the narrator cannot be funny any more, the idiom fails — a flat sentence, a term they would never use, a silence. That break is the payoff of the whole device, and it only works if the register was consistent enough for the break to be audible.
- **Do not spell the dialect.** Mark the register with syntax and lexicon — word order, particles (§9), a habitual construction, a wrong register word — never with phonetic spelling. Phonetic spelling is a costume; syntax is a person.
- **Imply a listener.** Skaz is told *to* someone, and the listener's presence shapes what the narrator admits. A skaz with no implied audience is a monologue, and monologue drifts toward the author.

**A short demonstration.** The material: a man has died of a heart attack after thirty years of working in the cold.

*А он, значит, взял и помер, а доктор говорит — сердце. Какое там сердце, когда человек тридцать лет на морозе. Ну и похоронили.*

The narrator rejects the medical cause in favour of a moral one, in three words (*какое там сердце*), and the rejection is the grief. Nothing is named. If the same content were narrated in standard prose — *он умер от сердечного приступа, что было неудивительно после тридцати лет на морозе* — the narrator would be explaining, and the loss would be information.

## Psychologism

Russian prose is famous for interiority, and the fame hides the fact that its three main modes are technically different and produce different sentences. Use them as distinct instruments.

**Tolstoy: the defamiliarising detail and the involuntary correction.** Shklovsky's *остранение* (defamiliarisation) was derived from Tolstoy, and the mechanism is visible at sentence level: the character gives a false account of their own state, and a detail they did not notice corrects it. The narration does not comment; the detail does.

*Ему казалось, что он спокоен. Он сам налил себе чаю и даже спросил у жены, где сахар, и только потом заметил, что мешает одной и той же ложкой второй раз и что чай давно остыл.*

The assertion is the character's; the spoon and the cold tea are the narrator's evidence against him. No adjective of distress appears, and none is needed. The technique's cost: it requires the narrator to know more than the character, which is why it belongs to third person and to a narrator willing to be silent about the conclusion.

**Dostoevsky: argumentative consciousness.** Bakhtin's dialogic or polyphonic novel has a sentence-level signature: the character's speech anticipates the other person's objection, answers it before it is made, and argues with an interlocutor who may not be in the room. The sentences are full of *разумеется*, *конечно*, *вы, вероятно, думаете*, self-correction, and provocation. This is not stream of consciousness; it is a mind that cannot stop defending itself.

*— Вы, разумеется, полагаете, что я теперь стану оправдываться. Что ж, оправдывайтесь вы, если вам это так нужно. А я вам лучше скажу вот что: я и не думал скрывать, я просто не считал нужным ставить вас в известность. И, пожалуйста, не делайте такое лицо — такое лицо вы делаете для прислуги.*

The character answers a question nobody asked, converts the accusation into a concession that is itself an attack, and ends by describing the other person's face. Every sentence is a move in a fight that started before the scene.

**Chekhov: withholding and the "irrelevant" detail.** Chekhov's restraint is not absence of feeling; it is the refusal to state the feeling and the substitution of a detail that is *slightly wrong for the moment*. The detail does not serve the plot, which is why it feels true: it serves the world, and the reader must convert it.

*Обещали дождь, но было сухо, и в палисаднике кто-то оставил грабли, прислонив их к забору, — так, как ставят, когда собираются вернуться через минуту. Она посмотрела на грабли и пошла в дом.*

The rake is not the story. It is the world continuing while something else happens, and the phrase *как ставят, когда собираются вернуться через минуту* is where the text's pressure sits — someone intended to come back. Nothing is named; the reader supplies it. The failure mode of this technique is the decorative detail that is merely odd: an irrelevant detail must be *just* relevant enough to be noticed, or it is trivia with a literary manner.

## Dialogue punctuation and typography

Russian dialogue is set with the **em dash** (тире, `—`), not quotation marks, and each new speaker takes a new paragraph. This is the largest typographic difference from English and the one most often got wrong by writers working from English models.

```
— Ты придёшь?
— Не знаю.
```

**Attribution after the line:** lowercase, with a dash before the verb.

```
— Ты придёшь? — спросила она.
— Не знаю, — сказал он и отвернулся.
```

**Attribution before the line:** the common modern form is to keep the remark on its own line and let the dash open it, with the attribution in the preceding narration paragraph. The older form puts a colon after the narration and the dash on the same line: *Он обернулся: — Ты уже собрался?* Both are in use; pick one and hold it.

**Direct speech inside narration** uses «ёлочки» (guillemets), not dashes:

```
«Я приду», — сказала она.
Она сказала: «Я приду».
```

Note the comma *inside* the closing guillemet and the dash *outside* it. When the quoted speech ends in a question mark or exclamation mark, the comma is not added: *«Ты придёшь?» — спросила она.*

**Interruption** is marked by a dash and an ellipsis of the cut word: *— Я не… — начал он.* A trailing dash without ellipsis is also used for a cut-off (*Я не —*), and house styles differ on which.

**Nested quotation** uses „лапки" inside «ёлочки».

**Other conventions, stated plainly, with the caveat that publishers vary:**

- **Ё.** Not compulsory in most modern print, but use it where it disambiguates (*всё* / *все*, *осёл* / *осел*, *мёл* / *мел*) and be consistent. Some houses require it everywhere; some forbid it in fiction. This is a house-style decision, not a grammatical one.
- **No Oxford comma.** Russian comma rules are syntactic: before *что*, *чтобы*, *который*, *если*, *когда*; around participial and деепричастные phrases; between homogeneous members without a conjunction.
- **The dash is spaced** in dialogue and in the copula-replacement use (*Дом — это всё*), and unspaced between numerals and in ranges (*1990—1995*). Do not use a hyphen where a dash belongs.
- **Paragraphing.** New speaker, new paragraph, always. Narration between two lines of dialogue gets its own paragraph if it is a beat, and stays in the same paragraph if it is a tag.

A sequence with a beat, correctly paragraphed:

```
— Ты уже собрался? — она стояла в дверях, не включая свет.

— Почти.

— Пальто бы надел.

Он не ответил. За окном уже шёл снег, и было слышно, как внизу
дворник скребёт лопатой асфальт.
```

Note what the layout does: the em dash at the start of each line marks a voice, the blank line between them marks a change of speaker, and the final paragraph has no dash because it is narration — the camera has left the speakers. A Russian reader parses all of this before reading a word of content, which is why a missing blank line reads as two people speaking at once.

**What varies.** Dash versus guillemets for dialogue in published fiction, ё policy, the spacing of the dash, and whether an interrupted line keeps its ellipsis. Check the target publication; do not treat one house's sheet as the language.

## Diminutives, particles, and the untranslatable

Russian marks **stance** — the speaker's relation to what they are saying and to the person they are saying it to — with small closed-class words that English renders as intonation, word order, or nothing. They are the hardest thing to translate and the easiest thing to overuse.

**Particles.**

- **`-то`** marks the topic as known or contrastive. *Я-то думал, что он уехал* — I, for my part, thought he had left. *Он-то знает* — he knows, whatever the rest of you think. It is a shrug, a concession, or a knife, depending on the stress.
- **`же`** insists or contrasts. *Скажи же!* — do say it. *Он же знал* — he knew, after all (and did nothing). It carries reproach more often than emphasis.
- **`ведь`** appeals to shared knowledge and recruits the listener as a witness. *Ведь ты обещал* — you did promise, and you know you did. It is the particle of pressure disguised as agreement.
- **`хоть`** sets a concession or a minimum. *Хоть что-нибудь* — at least something. *Хоть умри* — even if you die. It concedes the frame in order to insist on the point.
- **`уж`** carries resignation or intensification. *Уж я-то знаю* — I of all people know. *Уж лучше молчать* — better to say nothing.
- **`-ка`** softens an imperative into a nudge, often at oneself: *дай-ка* — let me just. It is the particle of a speaker who is being reasonable about something they intend to do anyway.

**Diminutives.** The suffixes (*-ик*, *-ок*, *-ец*, *-очк-*, *-еньк-*, *-ушк-*, *-ишк-*) do not mean "small". They position the speaker:

- affectionate: *мамочка*, *сынок*, *часик* (a bit of time, said fondly)
- pejorative and dismissive: *домишко* (a miserable little house), *статейка* (a pathetic little article), *народишко* (the wretched populace)
- idiomatic and stance-neutral: *минутку*, *ложечка*, *водички* (a bit of water, polite)

The same suffix can do all three. *Домик* is a small house, affectionately; *домишко* is a house the speaker despises; *домище* is a house that has got above itself. The suffix does not measure — it evaluates, and it evaluates *from the speaker's position*.

The stance is relational, not cute: the diminutive puts the speaker in a relation to the object and to the listener at the same time. That is why it can be tender in one mouth and contemptuous in another, and why a translator who renders every diminutive as "little" produces a text that is sentimental where the Russian was cruel.

**The risk: the flavour shortcut.** A Russian text that reaches for *водочка, закусочка, берёзонька* is writing a tourist's Russia. The test for each one: **whose stance is this, and why would this speaker take it now?** If the answer is "the author wanted the text to feel Russian", cut it. A particle or a diminutive that cannot be attributed to a speaker's position is decoration, and decoration in a language this heavily marked reads as pastiche.

**The translation loss.** English renders *ведь* as "after all" or as nothing, *же* as stress, *-то* as a pause. A translation therefore flattens stance, and a writer working from an English model will reproduce the flatness. When you write Russian, the particles are where the voice lives; when you translate into English, the loss has to be compensated elsewhere — a tag question, an adverb, a word order — or the character becomes politer than they are.

## Genre expectations in Russian

Conventions are not laws, but a writer who ignores them writes a text that reads as imported. Three differences matter for pacing and structure.

**The рассказ tolerates open moral material.** The Russian short-story tradition — Chekhov, Bunin, later Trifonov and Petrushevskaya — can end on an unresolved ethical question and treat the unresolution as the story's payload. The Anglo-American workshop story more often requires a turn: an epiphany, a reversal, a moment of recognition that closes the arc. A Russian рассказ may end on a state, a refusal, or a repetition with no change, and the change is in the reader. This is why an ending that "resolves nothing" can be a finished Russian story and an unfinished Anglo one — and why importing the epiphany requirement produces a last paragraph that explains what the story already knew.

**`Рассказ` is not the Anglo short story with a turn.** The Russian form's centre of gravity is the rendering of a condition — a life, a marriage, a provincial town — and its tolerance for stasis is higher, provided the stasis is *inhabited* rather than merely described. The corresponding risk is a story that is all condition and no pressure: the Russian tradition does not excuse a scene where nothing is at stake, only a scene where the stake is not resolved.

**The thriller convention is comparatively weak.** Russian literary culture has a strong psychological novel and a strong detective tradition, but the Anglo-American thriller's machinery — the ticking clock, the chapter-end cliffhanger, the scene-sequel rhythm at fixed intervals — is less codified, and pacing advice imported from it can make Russian prose feel dubbed. Apply it as a tool for a specific book, not as the default shape of a Russian narrative.

`[hypothesis]` The stasis tolerance interacts with the agency law: a story about a character who cannot act is still a story about a choice — the choice not to act must cost something and must be visible as a choice. A Russian рассказ that renders paralysis without cost is not a Russian form; it is an unfinished one.

## A revision checklist for Russian

Ten checks, in the order that catches the most text.

1. **Count sentences that begin with *Он* or *Она*.** Two in a row is a habit; three is English syntax. Drop the subject and chain the verbs.
2. **Mark the focus of every sentence.** If the new information is not at the end and there is no visible reason, the order is a calque. If every sentence ends on the rheme, there is no emphasis anywhere — front one word per paragraph.
3. **Aspect audit.** Write П or Н above the main verb of each sentence in a scene. `П П П П` is a procedure, `Н Н Н Н` is a mood. Find the switch, or make one.
4. **Count `который`.** Two in one sentence: rewrite as a participial phrase or split. Three: the sentence was translated.
5. **Count sentences that open with *Было*.** More than one per page of scene-setting means the impersonal has become the default and no sentence has an actor.
6. **Find the sentence's most important action.** If it appears as a деепричастие or inside a participial phrase, promote it to the main clause.
7. **Dialogue mechanics.** Em dash, not hyphen; new speaker, new paragraph; lowercase attribution after the dash; guillemets for quoted speech inside narration.
8. **Every diminutive and particle: whose stance?** If you cannot name the speaker's position and the reason for it here, cut it.
9. **Calque sweep.** *является*, *имеет место*, *в рамках*, *на данный момент*, *осуществлять*, *данный*. Replace each with the verb or noun a person would say.
10. **Read aloud.** If you run out of breath at the same point in three consecutive sentences, the rhythm is a metronome, and the paragraph has no emphasis regardless of its word order.

## Links

- `references/prose-engineering.md` — the language-neutral layer: paragraph shape, image, attention, and the emotion channels §7 re-instruments.
- `references/multilingual-notes.md` — what transfers when a Russian text is translated, and what is lost.
- `references/narrative-theory.md` §9–10 — остранение and heteroglossia, the concepts behind §7 and §6.
- `references/english-prose.md` — the defaults this file exists to keep out of Russian prose.
- `references/quality-levels.md` — the L1–L7 tags; §1 here is almost entirely [L1]–[L2], §5–§7 are [L3]–[L6].
