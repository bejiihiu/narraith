# Multilingual Notes: What Transfers, What Does Not, and How to Work Across Languages

> Purpose: separate the layer of narrative craft that survives a change of language from the layer that is made of the language, and give a procedure for each.
> Read when: you are writing in a language that is not the one you planned in, translating or adapting a draft, or editing a user's non-native text.
> Links: `references/russian-prose.md` — the worked case, and the language where translationese is most visible; `references/english-prose.md` — the defaults that travel worst; `references/prose-engineering.md` — the language-neutral layer; `references/research/05-fingerprinting.md` — the evidence behind §1.

*Everything here is `[theory]` or `[hypothesis]` except the one `[data: Fingerprinting]` citation in §1. That paper measures model attribution, not craft, and contains no Russian data at all; the transfer to our purposes is explicitly labelled.*

## What transfers between languages

A story is made of two kinds of material: **propositions** (who did what, who knew what, what it cost) and **surfaces** (the words, the rhythm, the punctuation, the register). Propositions survive translation because a translator can always restate them; surfaces do not, because they are made of the sound and grammar of one language. Craft that lives in propositions therefore transfers; craft that lives in surfaces does not.

`[hypothesis]` The durable layer is: structure, causality, information planning, and character logic. This is our engineering bet, and it is consistent with the finding in the fingerprinting paper that content-bearing representations survive a change of language better than grammar-derived statistics do. `[data: Fingerprinting]` Averaged over six translation directions, the semantic representation transfers at 30.58 against 19.74 for the stylometric one, while lexical features are excluded from the cross-lingual experiment altogether because they are "strongly tied to language and script" (§5.3).

**What that evidence does and does not license.** It measures how well a classifier recovers *which model wrote a text* when the text crosses languages. It does not measure craft, it does not test Russian, and its non-English prompts were machine translations of English ones. So the finding supports an analogy, not a rule: the layer that carries content survives; the layer that carries grammar does not. Whether narrative decisions are "the semantic layer" of craft is our hypothesis, and it would be falsified if native readers of two languages judged the same translated scene to have different causal logic — which they should not, since the logic is in the propositions.

**The operational version**, and the reason this matters:

| Layer | Survives translation | Why |
|---|---|---|
| Fabula — the events in causal order | Yes | It is a sequence of propositions; any language can state them |
| Scene card — goal, obstacle, turn, cost | Yes | It is a set of relations between agents, not a wording |
| Information ledger — who knows what, when | Yes | Knowledge is a propositional state |
| Want / need / lie | Yes | Three sentences about a person, translatable without loss |
| Value charge and turning point | Yes | A relation between states, not a phrase |
| Motif and structural repetition | Partly | The *pattern* transfers; the specific word that carries it usually does not |
| Sentence rhythm and stress | No | It is phonology |
| Register and social deixis | No | Social meaning is encoded differently in every language |
| Punctuation and dialogue layout | No | Pure typographic convention |
| Forms of address | No | Grammaticalised in some languages, absent in others |
| Tolerance for narratorial comment | No | A genre norm, not a language universal |

**The test.** Write the scene's causal chain as bare propositions: *A wants X. B blocks it by Y. A pays Z. A learns W.* If that summary still makes sense after translation — and it will, because it contains no language — then the structure is portable and the prose is the only thing to rebuild. If the summary stops making sense, what you had was not structure; it was a wording that happened to imply a structure, and the structure needs to be built explicitly before you write a line in the new language.

**The test on a scene.** A woman sells her father's shop to pay his debts; the buyer turns out to be the man who ruined him. In propositions: *She wants to keep the shop. The debt blocks her. She sells to a stranger to pay it. The stranger is the man who caused the debt. She learns this after signing.* Nothing in that summary depends on English, and every one of those propositions can be restated in another language without loss. What does not survive is the decision to reveal the buyer's name on a document she has already signed, in a sentence whose last word is the name — that is a decision about English syntax, and in another language it must be re-decided, not copied.

That is the working definition of the portable layer: **a scene's causal skeleton is portable; the sentence that delivers it is not.**

**What to do at the start of a task in another language.** Four moves, before any prose: write the premise and the dramatic question in propositions; write the scene cards in propositions; write the information plan (who knows what, when the reader learns it) in propositions; and only then decide the sentences. The propositions are language-free by construction, so this is the one planning stage that cannot be contaminated by the source language. If you plan in English sentences and translate, every later decision inherits an English shape and the target language spends the whole draft accommodating it.

## What does not transfer

Each of these is a place where a good sentence in one language becomes a correct but wrong sentence in another.

**Rhythm.** English counts stresses; Russian counts syllables and weight; Japanese counts morae; Chinese counts syllables and tones. A sentence transplanted with its word order intact carries the source language's rhythm into a language that does not have it. The reader hears the foreign cadence before they can name it, and that is what "sounds translated" means.

**Politeness.** Languages grammaticalise social relations to different degrees. Russian's ты/вы is a decision English cannot represent: *you* is one word, and the translator must choose, and the choice changes the relationship. The reverse is also true: a Russian scene in which a character shifts from *вы* to *ты* is an event — a permission granted, a boundary crossed — and English has to dramatise the shift with behaviour because it has no word for it.

**Forms of address.** *Иван Петрович*, *Ваня*, *Ванька*, *гражданин Иванов* are four relationships, and the choice among them is a social act. Languages without the patronymic cannot reproduce it; a text that renders all four as "Ivan" has flattened the social field and must compensate elsewhere or lose it.

**Humour.** What is funny is a social contract, not a property of content. Zoshchenko's narrators are funny because of the register they narrate in; translated into neutral prose, the same events are sad or merely odd. A joke that survives translation is a joke about a situation; a joke that does not is a joke about a way of speaking.

**Punctuation.** Russian dialogue uses an em dash and a new paragraph per speaker; English uses quotation marks and can run exchanges inside a paragraph. Carrying one convention into the other language produces text that looks wrong on the page before it reads wrong in the ear.

**Paragraph norms.** Russian prose tolerates longer paragraphs, more subordination, and more digression inside a single block; modern English prose, especially online, runs shorter. The same content paragraphed by the other language's norm reads as either breathless or bloated.

**Narratorial comment.** The Russian tradition licenses the narrator to generalise and digress; the Anglo-American workshop treats it with suspicion. A translator who preserves the content of a digression but not its licence produces a text that reads as an author's intrusion — the comment is there, the permission is not.

**Time.** How a language marks time is grammatical, and grammars differ in kind rather than in degree. English has tense and aspect fused into the verb; Russian has aspect and only one past tense; Chinese marks aspect with particles and does not inflect for tense at all. This means the *same* narrative decision — how long does this beat last, and is it an event or a condition — is expressed by different machinery in each. `references/russian-prose.md` §3 is the worked case: imperfective for duration, perfective for event, and a scene that uses one aspect throughout goes flat in a way English readers cannot diagnose because English has no equivalent lever.

**A consequence for adaptation.** When a scene is moved between languages, the pacing decisions have to be re-made even if the event sequence is preserved: the same events, at the same order, can run fast in one language and slow in another because the target language's default duration is different. The rule is that the *effect* must be preserved, not the means.

**What to do instead.** Each non-transferable layer has a portable substitute, and naming it is the whole adaptation procedure:

- For **rhythm**, rebuild rather than copy: decide the stress plan (what lands, what is hurried) and achieve it with the target language's instruments.
- For **politeness**, dramatise the switch: if a ты/вы shift is an event in Russian, give the English version a behaviour that carries the same permission or boundary.
- For **address**, establish hierarchy and intimacy by what characters are allowed to say and to whom, not by the form of the name.
- For **humour**, keep the situation and rebuild the idiom; if the joke was in the register, the joke is not portable, and the scene needs a different joke or none.
- For **punctuation and paragraphing**, follow the target convention without exception; a compromise produces a text that looks like neither.
- For **comment**, decide the licence explicitly in the voice contract (three obligations, three prohibitions). If the narrator is allowed to generalise, say so and hold it; if not, the digression has to become a scene or go.

The substitution is not a loss to be mourned. It is a re-encoding: the target reader judges the effect, never the fidelity, and a text that preserves the English means at the cost of the Russian effect has failed both. The only thing that must survive intact is the causal skeleton of §1.

## Writing in a third language

**The rule: do not translate an English draft.** Decide the information structure first — what is given, what is new, where the focus falls, what the paragraph's last word should be — and then write the sentence in the target language with that plan in hand. Translating a finished English draft forces the target language to accommodate English decisions, and the accommodation is exactly what translationese is. This is the same instruction `references/russian-prose.md` §2 gives for Russian, generalised: the language's own instruments decide the sentence; the plan decides the information.

**Three failure patterns**, in the order they appear in a draft.

**(1) The pronoun-subject default.** Every sentence starts with a subject because the source language requires one, and the target language does not.

*Failure (Russian):* *Он вошёл в кухню. Он открыл холодильник. Он достал бутылку. Он налил себе.*

*Repair:* *Он вошёл в кухню, открыл холодильник, достал бутылку и налил себе.* — one subject, chained verbs. The repair is not "use fewer pronouns" as a rule; it is that the repeated subject was doing no work in a language where the subject can be carried by the verb ending.

**(2) The focus-order transplant.** The writer keeps the source language's habit of putting new information in a fixed position, and in the target language every sentence then carries the same marking — which means none is marked.

*Failure:* three consecutive sentences of the form *Дверь открыла она. Письмо написала мать. Решение принял совет.* Each is a legitimate Russian construction that answers *who?*, and three in a row turn the paragraph into a series of accusations: every sentence is emphatic, so nothing is.

*Repair:* keep one marked order and let the others run neutral. *Она открыла дверь. Письмо написала мать. Совет уже решил.* — the middle sentence keeps the focus on the agent because that is the surprising fact; the others do not need it.

**(3) Over-marked connection.** Source-language connectives and articles get imported as words. *Однако*, *более того*, *следовательно*, *таким образом* appear at the head of every paragraph where the target language would use word order, a particle, or nothing at all; and languages without articles acquire a rash of *один*, *этот*, *какой-то* as compensation for a definiteness the grammar does not require.

*Failure:* *Таким образом, он остался один. Однако это было не так уж плохо. Более того, он даже обрадовался.* Three connectives in three sentences: the paragraph narrates a man's solitude like a report, and each connective claims a logical relation the scenes have not earned.

*Repair:* *Он остался один. Это было не так уж плохо. Он даже обрадовался.* The relations are still there — consequence, concession, escalation — but they are carried by the sequence, which is where Russian puts them. The explicit connective is a written register; using it in narration is like narrating in a suit.

**A fourth, common to all three:** the writer keeps the source language's sentence *length distribution*. English's short-medium-short pattern transplanted into Russian reads as clipped; Russian's long period transplanted into English reads as unparagraphed. The distribution is part of the rhythm, and the rhythm does not transfer.

**How to find these in a draft.** Do not read for words; read for patterns. Take three consecutive paragraphs and mark, for each sentence, whether the subject comes first, where the new information falls, and what the first word is. If the answers are the same in every sentence, one of the three patterns is present, and the fix is structural rather than lexical. Run the same audit on a paragraph you know is native: the pattern usually shifts within three sentences, and that shift is what variety looks like from the inside.

**The order of operations, worked.** Target: Russian. The scene decision: she has been waiting an hour; when he finally comes in, she does not get up.

1. **Information plan.** Theme: her waiting (given by the scene). Rheme: the not-getting-up (the news). The paragraph's last word should be the refusal.
2. **Duration.** The wait is imperfective and dilated; the arrival is perfective, one event; the refusal is imperfective again, a state that continues past the sentence.
3. **Focus.** The refusal goes last, because it is what the next paragraph will have to deal with.
4. **Then write**, in Russian, with those three decisions in hand: *Она ждала его час. Когда он наконец вошёл, она не встала.*

The English source might have read *She had been waiting an hour. When he finally came in, she didn't get up.* The Russian is not a translation of that sentence; it is the same plan executed with a different machine — one past tense instead of a pluperfect, aspect carrying the duration, and the final position reserved for the refusal. There is no Russian equivalent of *had been waiting*, and none is needed: the imperfective does the work that English does with an auxiliary.

## Working with a user's non-native draft

The job is to remove errors without removing the writer. Those are different operations and they use different criteria.

**Step 1 — read the whole draft before marking anything.** Non-native texts have consistent patterns, and a pattern is not an error; it is a dialect of the writer's relation to the language. Marking sentence by sentence produces a text that is correct in every line and inconsistent across the page.

**Step 2 — classify every non-standard item into exactly one of three.**

| Class | Test | Action |
|---|---|---|
| **Error** | It impedes meaning, or it contradicts something else in the text, or it is inconsistent with the same construction elsewhere | Fix it |
| **Dialect** | It is consistent, it is shared with a real variety of the language, and it does not impede meaning | Leave it, or ask |
| **Register** | It is deliberate: a child narrating, a formal letter, a character's idiom, a period voice | Leave it, always |

The classification is the whole skill. A correction applied to a dialect item is an act of erasure; a correction withheld from an error is an act of negligence. The test that separates them is **consistency**: an error is usually local, a dialect is systematic.

**Step 3 — fix errors by the smallest move.** Replace the word, not the sentence; reorder the clause, not the paragraph. A non-native draft often has one wrong word carrying a right idea, and rewriting the sentence around it loses the idea. If a construction is odd but meaningful, the repair is to make it grammatical and keep it odd.

**Step 4 — re-read for voice.** After the corrections, read a page aloud. If the text no longer sounds like the person who wrote the draft — if it has become fluent, generic, and slightly official — the corrections went too far. Fluency is not the goal; comprehensibility plus the writer's own pressure is.

**Two rules that are absolute.**

- **Never "correct" a deliberate register.** A narrator who uses a formal construction because they are formal, a child who uses the wrong tense because they are a child, a letter that is stiff because the writer is stiff — these are characterisation. Correcting them is rewriting the character.
- **Never replace an odd word that is doing work with a standard word that is not.** *Он вошёл в комнату, как входит человек, который не хочет, чтобы его услышали* is slightly unusual and completely clear. The "improvement" — *он вошёл тихо* — is standard and has lost the comparison, the intention, and the shame. If the odd word is the only place the meaning lives, the odd word stays.

**The over-correction failure, named.** A text corrected into fluency reads as translated *from* something, because the corrections have removed the only evidence of a person. The characteristic result is grammatically perfect, rhythmically uniform, and voiceless — which is the same signature §1 of `references/english-prose.md` describes, arrived at by editing rather than by generation. Preserving a writer's non-native pressure is not sentiment; it is the difference between a text with an author and a text with a proofreader.

**The pass, in order.**

1. Read the whole draft without marking anything. Note what repeats.
2. Classify each non-standard item as error, dialect, or register, using the table above.
3. Fix errors with the smallest move; leave dialect and register.
4. Check the motifs: a construction that recurs three times is a pattern, and patterns are not corrected — they are recognised. If the pattern is a tic, say so and let the writer decide.
5. Read a page aloud and ask whether a person is still audible. If not, undo the last pass.

| Do | Do not |
|---|---|
| Fix agreement, case, or aspect where it changes the meaning | Standardise a consistent regional or personal form |
| Reorder a clause whose focus has been lost | Reorder because the target language "prefers" it |
| Replace a word that means the wrong thing | Replace a word that means the right thing unusually |
| Mark a repeated construction and name it | Remove the repetition when it is a motif |

## Links

- `references/russian-prose.md` — the worked case for §3: word order, aspect, and the specific markers of translationese.
- `references/english-prose.md` — the defaults that travel worst, and the register and FID machinery that has no direct equivalent elsewhere.
- `references/prose-engineering.md` — the language-neutral layer: paragraph, image, attention, and the emotion channels.
- `references/research/05-fingerprinting.md` — the durability hierarchy and its limits; read before quoting §1.
- `references/narrative-theory.md` §1 — fabula and sjuzhet, the distinction that makes the transferable layer statable.
