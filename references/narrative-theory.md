# Narrative Theory: The Decision Vocabulary

> Purpose: name the narratological concepts Narraith uses so that a narrative choice can be argued instead of felt.
> Read when: you are fixing POV, temporal handling, scene shape, character logic, dialogue register, or an ending, and you need the concept that makes the choice inspectable.
> Related: `references/quality-levels.md` — the L1–L7 ladder these concepts attach to. `references/ai-narrative-signature.md` — the measured failure patterns these concepts are meant to counteract. `references/story-architecture.md` — the structural layer built on these terms. `references/temporal-complexity.md` — §2 and §3 extended to whole-plot time.

## Contents

1. [Purpose and how to use this file](#purpose-and-how-to-use-this-file)
2. [1. Story vs. discourse](#1-story-vs-discourse)
3. [2. Narrative order, duration, frequency](#2-narrative-order-duration-frequency-genette)
4. [3. Voice, mood, focalization](#3-voice-mood-focalization)
5. [4. Psychic distance and free indirect discourse](#4-psychic-distance-gardner-and-free-indirect-discourse)
6. [5. Scene and sequel, motivation-reaction units](#5-scene-and-sequel-motivation-reaction-units-swain)
7. [6. Value charge and turning points](#6-value-charge-and-turning-points-mckee)
8. [7. Character: round, flat, want, need, lie](#7-character-roundflat-forster-wantneedliewound-contradiction)
9. [8. Premise and dramatic question](#8-premise-and-dramatic-question-egri-others)
10. [9. Defamiliarisation](#9-defamiliarisation--ostranenie-shklovsky)
11. [10. Heteroglossia and dialogism](#10-heteroglossia-and-dialogism-bakhtin)
12. [11. Intertextuality and the canon](#11-intertextuality-and-the-canon)
13. [12. Plot grammar and its limits](#12-plot-grammar-functions-and-their-limits-propp-todorov)
14. [13. Readerly cooperation and gaps](#13-readerly-cooperation-and-gaps-iser-barthes)
15. [14. Endings](#14-endings)
16. [15. Theory into decisions: a mapping table](#15-theory-into-decisions-a-mapping-table)
17. [What theory cannot do](#what-theory-cannot-do)

*Everything in this file is `[theory]` — craft and narratology, not measurement. The single empirical claim, in §11, is tagged `[data: StoryScope]` and is a detection finding, not a writing rule.*

## Purpose and how to use this file

Theory in this file is a decision vocabulary, not a checklist to satisfy: every concept exists so a choice already made can be named, defended, and revised. Use it before writing to fix a decision — who focalizes, what speed a beat runs at, what value a scene moves — and after writing to diagnose why a passage feels wrong when no single sentence in it is wrong. If a concept does not change a decision you are about to make, close the file and write.

## 1. Story vs. discourse

The Russian formalists separated **fabula** (the events in chronological, causal order) from **sjuzhet** (the order and manner in which the text delivers them); structuralist narratology restated this as **story** vs. **discourse**. The distinction is not academic bookkeeping. It says that a narrative has two independent design surfaces, and that almost every problem a draft has lives on exactly one of them.

The common failure is inverted investment: the fabula is thin — four events, one line, each following the last by "and then" rather than by "therefore" or "but" — while the discourse is richly worked with image, rhythm, and interiority. No amount of discourse craft repairs a fabula that has nothing to deliver.

The second use of the split is permission: the discourse is allowed to withhold, reorder, and repeat, and these are not lies told to the reader but the medium itself. A story that delivers every event in order, at equal weight, has chosen to have no discourse — and the reader has nothing to do.

Operational:

- Write the fabula as 5–9 bare sentences in chronological order, no style, named agents, active verbs. If it will not compress, the plot is not yet understood.
- Read the connectives between those sentences aloud. "And then" means you have a sequence; "therefore" or "but" means you have a plot. Convert each "and then" into one or the other, or delete the event.
- Write the discourse as a second list: which fabula event the reader receives first, second, third, and what each arrival teaches. Two lists that are identical are legal but mean you have chosen chronological narration deliberately, not by default.
- Diagnose in the right layer. If the fabula summary is unconvincing, fix causality, agency, and stakes — not sentences. If the summary is strong and the draft is dull, the fault is discourse: order, speed, distance, withholding.

Worked example, same material, two layers:

- Fabula: *A woman inherits her father's shop. The debts are larger than the shop. She sells the stock to pay them. The buyer turns out to be the man who ruined her father.*
- Sjuzhet: open on the sale, in progress. Let the buyer's name arrive in the fourth scene, on a document she has already signed. Let the reader learn the debt figure only after she has agreed to it.

The fabula is four causally connected events; the sjuzhet is a decision about which of them the reader is allowed to see, and when. Both are the writer's work, and neither is prose.

## 2. Narrative order, duration, frequency (Genette)

Genette's three categories describe the relation between story time and text time, and they are the most directly usable instruments in narratology because each one is a physical property of the page.

**Order** — the text can move backward (**analepsis**) or forward (**prolepsis**) relative to the story's chronology. Two properties matter: *reach* (how far back it goes) and *extent* (how long it stays there). An analepsis is either *completing* (it fills a gap the main line opened) or *repeating* (it retells what the reader already knows, from a different position); a prolepsis is judged by the mirror question — what does knowing this early cost the scene? Rule: an anachrony must arrive because the present scene has just raised the question it answers. A flashback inserted because the information is due is an interruption, not a structure.

**Duration** — five speeds, from fastest to slowest:

| Technique | Effect on pace and knowledge | Use when | Failure mode |
|---|---|---|---|
| **Ellipsis** — story time passes, text skips it | Fastest. Creates a hole the reader must infer or accept | A period holds no decision, only transport between decisions; or the gap itself is the point and will be revisited | Unexplained skip reads as a continuity error; the reader cannot tell whether time passed or the author lost track |
| **Summary** — story time compressed, text brief | Fast. Delivers information and covers ground; knowledge rises, immersion falls | Spanning weeks of routine, establishing a situation, moving between scenes without losing the causal thread | Long summary where a scene was required; the draft reports the story instead of playing it |
| **Scene** — story time and text time roughly equal | Neutral pace, high immersion | Any moment where a decision is made, a relationship shifts, or force is applied and resisted | Scene inflation: whole scenes of talk that move nothing, because "scene" was mistaken for "good" |
| **Stretch** — text time exceeds story time | Slow. Attention narrows; subjective time dilates | A decision under pressure, violence, pain, shame, the half-second before an irreversible act | Used on ordinary action it reads as padding; the reader feels the author stalling |
| **Pause** — story time stops, text continues | Frozen. Knowledge may rise, tension usually falls | Description of the object the character is currently deciding about; commentary that reframes what just happened | The default AI pause: three sentences of weather before anything happens, because the model has nothing to decide |

**Frequency** — **singulative** (tell once what happened once), **repetitive** (tell many times what happened once), **iterative** (tell once what happened many times). Frequency is the cheapest structural signal available: run a stretch in the iterative, then break into the singulative at the moment routine fails. That switch alone tells the reader *this is the day it changed* without a word of explanation. Repetition is not redundancy when the second telling knows something the first did not — same event, different knowledge, is the whole mechanism of revelation.

Worked example of duration — one fabula event at five speeds:

- **Ellipsis:** *Winter passed.*
- **Summary:** *He worked the depot through the winter and learned the timetable by heart.*
- **Scene:** the exchange in which he is refused a transfer, in dialogue.
- **Stretch:** the four seconds in which he reads the refusal and decides not to appeal.
- **Pause:** the notice board described while he stands in front of it, deciding.

The same event can be any of the five. The choice is not a matter of taste — it is what the reader experiences as the story's rhythm, and a draft with only scenes and summaries has two gears where it needs five.

Worked example of frequency — the same mechanism at paragraph scale:

- **Iterative, then singulative:** *Most evenings he ate at the counter and said nothing to the girl behind it. On the last evening he asked her name.* The switch is the story.
- **Repetitive with escalation:** the same refusal told three times, each time with one more detail the narrator could not previously admit. The event does not change; the narrator's access to it does.

## 3. Voice, mood, focalization

Genette split two questions that everyday craft language muddles: **voice** is who speaks (and when, and from what narrative level); **mood** is who sees — regulated by distance and by **focalization**. The narrating "I" and the perceiving "I" need not be the same person, and separating them fixes most POV confusion.

- **Zero focalization** — the narrator knows more than any character. Omniscience. Expensive: it removes the reader's need to interpret, and it is the mode AI prose drifts into without deciding to.
- **Internal focalization** — knowledge is bounded by one character (*fixed*), by several in turn (*variable*), or by several on the same events (*multiple*). This is the default for close third and first person.
- **External focalization** — the text reports only exteriors, knowing less than the characters do. Behaviourist, cinematic, deliberately opaque. Rare, and it makes the reader do the inferring, which is the point.

Voice also fixes **when** the narrating happens relative to the story, which is a separate axis from tense:

- **Subsequent** — narrated after the fact, in past tense. The default, and the only mode in which a narrator can plausibly know the ending.
- **Simultaneous** — narrated as it happens, in present tense. Narrows what the narrator can know to the current moment, which is why present-tense narration feels immediate and slightly blind.
- **Prior** — narrated before it happens: prophecy, plan, threat. Rare in full, common as an inserted frame.
- **Interpolated** — narrated between episodes, as in a diary, log, or epistolary frame.

English tense is not the same thing as time of narrating. A present-tense novel can be a subsequent narration imitating immediacy, and the reader will feel the seam wherever the imitation is inconsistent. Decide which situation the narrating voice is physically in, and let that decision constrain what it can know.

Two interior modes are often confused with focalization itself. **Psychonarration** is the narrator's report of a character's inner state in the narrator's own language ("she was afraid of the answer"). **Free indirect discourse** carries the character's diction and evaluative stance inside the narrator's third person and past tense, with no reporting clause ("Of course he would be late. Of course."). The first summarizes a mind; the second inhabits one. See §4 for the mechanics.

**Limited vs. unreliable is not a matter of degree.** A limited narrator is honest within a bounded field of knowledge; nothing in the text contradicts the report, the reader simply knows the field is bounded. An unreliable narrator's report is itself bent — by interest, ideology, shame, incapacity — and unreliability only exists if the text supplies a *second track*: a detail, a contradiction, a pattern of avoidance that lets the reader locate the bend. No second track means you have written a confusing narrator, not an unreliable one. E15 owns the full protocol.

**Three-question test to locate the actual focalizer of a scene:**

1. Whose sensory access limits what can be described here? Name the body in the room whose ears and eyes the sentence depends on.
2. Whose vocabulary and judgment appear in the narration? Find one evaluative word ("absurd", "predictably", "obviously") and ask who would use it.
3. What does the narration refuse to state that this character could not know? The refusals are the strongest evidence; a sentence that knows too much breaks the answer to (1).

Where the three answers converge, that is your focalizer. Where they disagree, you have head-hopping even if the pronouns never change. Focalization may legitimately shift between chapters or sections; inside a scene it must hold, or the shift must be marked by a break.

One event, three focalizations — a letter arrives at a kitchen table:

- **Zero:** *The letter said the claim had been refused, and both of them knew before she opened it that the winter would be spent in the other house.*
- **Internal, fixed to the daughter:** *Her mother's thumb went white on the envelope. The letter had been opened and resealed — she could see the second fold.*
- **External:** *The woman put the envelope on the table. The girl picked it up, turned it over, and put it down again. Neither of them sat.*

Same event, three information budgets. The zero version tells the reader the outcome; the internal version gives one body's evidence and leaves the outcome to be inferred; the external version reports only what a camera would hold. None is better in itself — the choice decides what the scene can be about.

## 4. Psychic distance (Gardner) and free indirect discourse

Gardner's psychic distance is the perceived gap between narrator and character, and its value is that it is a *ladder*, not a switch: discrete rungs a scene can climb one at a time. Same moment, seven rungs:

| Rung | Mode | Example |
|---|---|---|
| 1 | Panoramic summary, no character in view | It rained in the depot town that night, as it had all week. |
| 2 | Character in frame, exterior only | Elias stood at the edge of the awning with a paper bag. |
| 3 | Exterior plus inference about feeling | He held the bag tight against his chest, as if it might be taken. |
| 4 | The character's perception, still narrated | The rain came sideways under the awning and found his collar. |
| 5 | Free indirect discourse — his diction, narrator's grammar | Nine minutes late, and of course the awning had to leak tonight. |
| 6 | Direct thought, quoted or italicized | *Nine minutes late. If the hill road floods, I sleep here.* |
| 7 | Interior monologue, unmediated | nine minutes late the hill road floods the bag is paper the bag is paper |

Rules that make the ladder usable:

- **One rung at a time.** A paragraph that starts at rung 2 and lands at rung 6 without intermediate steps reads as either head-hopping or authorial intrusion, and the reader's trust in the frame drops even if they cannot name why.
- **Distance is information, so it must move for a reason.** Come close for the moment of decision; pull back to cross time, to establish, or to end a section. A scene that opens at rung 5 has spent its whole budget before anything has happened.
- **Two legal jumps.** A hard cut at a section break, where the reader expects re-entry; and one deliberate shock where the jump *is* the effect — a character's composure snapping. The second is available once per story.
- **FID has a signature you can check.** Third person, past tense, no reporting clause, and at least one marker that belongs to the character rather than the narrator: a judgment, an idiom, an exclamation, a ragged fragment. Remove the marker and it is plain psychonarration — which is fine, but it is a different rung.
- **FID is the only mode that lets a narrator stay outside while the character's bias leaks in.** That is why it carries irony, and why it is the default vehicle for unreliable narration in third person.

A legal two-rung move, inside one beat: *He held the bag tight against his chest, as if it might be taken. The rain came sideways under the awning and found his collar.* Rung 3 to rung 4 — the second sentence stops inferring from outside and starts registering from his own skin.

An illegal jump, same material: *It rained in the depot town all evening. Of course the awning had to leak tonight.* Rung 1 to rung 5 with no step between. The second sentence enters a mind the first never admitted existed, and the reader experiences it as the author's convenience rather than the character's attention.

## 5. Scene and sequel, motivation-reaction units (Swain)

Swain's split: a **scene** is a unit of pursuit — **goal → conflict → disaster** (or setback); a **sequel** is the unit that processes the result — **reaction → dilemma → decision**. Scenes run hot and move the plot; sequels run cool and move the character. Alternating them produces the characteristic rhythm of commercial narrative: pressure, then processing, then pressure.

The failure modes are symmetrical and easy to spot. Scenes without sequels produce breathless plots where nothing lands, because the reader is never given time to feel the cost. Sequels without scenes produce stasis — pages of reflection in which the character almost decides something, again.

A **motivation-reaction unit** is the sentence-level version of the same principle, and its ordering rule is absolute: the stimulus (motivation) must be on the page before the response, and the response must run from involuntary to voluntary — **reflex or feeling → thought → action → speech**. Swain's point is physical: a body reacts before it thinks, and thinks before it speaks. Reversing the order is not a stylistic choice, it is a claim about how minds work, and it is usually wrong.

What breaking the order costs:

- **Speech before feeling** makes the line sound like the author talking, because the character has had no interior time to arrive at it.
- **Action before stimulus** makes the reader reread the previous sentence to find out what the character was reacting to.
- **Thought before reflex** flattens the moment into commentary; the reader learns what the character concluded without witnessing the jolt that produced it.
- **Two responses to one stimulus in the wrong sequence** (she said, then flinched) read as comic, whether or not you meant it.

The rule has one legitimate exemption: deliberate simultaneity, where the point is that the character is too fast, trained, or dissociated for the sequence to run in order. Mark it once, and the deviation becomes characterisation rather than error.

The same beat, both ways:

- **Reversed:** *"I'm not going," she said, and stepped back.* Speech first, body second. The line arrives before the body has reached it, so it reads as a stage direction with a quote attached.
- **Ordered:** *Her hand found the doorframe. She stepped back without deciding to. "I'm not going."* Reflex, action, speech — and now the speech sounds like a conclusion the body reached first.

Not every unit carries all four beats; a one-beat response is fine. The rule is only that the order never reverses and the stimulus is never withheld until after the reaction.

## 6. Value charge and turning points (McKee)

McKee's definition: a scene is a unit of change in a **value** — a pair like life/death, love/hate, truth/lie, freedom/servitude, justice/injustice, trust/betrayal, hope/despair. The scene opens with the value at one charge, closes at another, and a **turning point** is the action that flips it. A passage where the value enters positive and exits positive is not a scene; it is exposition, texture, or atmosphere, and it should be merged into something that turns.

Operational:

- Name the value in two words, in the positive/negative pair form. If you cannot name a pair, the passage has no stake and no amount of prose will supply one.
- Mark the charge at entry and at exit with `+` or `−`. This is the whole diagnosis: `+ → −`, `− → +`, `+ → +`, `− → −`.
- `+ → +` or `− → −` means cut, merge, or convert. The third option is legitimate and underused: press the value hard and let it *refuse* to move — a character tries to save the thing and fails to change anything. That is a value *tested*, not a value unchanged, and it must be marked as such in the scene card, or a later reader will mistake it for filler.
- Locate the turning point as a specific action by a specific agent, not a realisation. If the value flips because the character understood something, the understanding is the turning point and it needs an event to cause it.
- Track values across the sequence. Three consecutive scenes that all turn trust/betrayal in the same direction is one scene told three times.

**Conflict with §5.** This rule collides with the sequel, which is often a unit of *decision* rather than of value-change. Resolution: a sequel earns its place by producing a decision that changes what the character will do; if it produces neither a decision nor a value movement, cut it.

A scene card that passes: *Value — his standing with the crew. Entry `+`. He asks the foreman to sign off on a repair he did not make. The foreman reads it, signs it, and thanks him in front of the others. Exit `−`. Turning point — the thanks, which is the one response he has no answer for.* The value moved, an agent acted, and the exit charge is the opposite of the entry.

## 7. Character: round/flat (Forster), want/need/lie/wound, contradiction

Forster's pair remains the cleanest statement of the distinction. A **flat** character is built around a single idea or quality and does not surprise; a **round** character is capable of surprising the reader in a way that remains convincing. Forster's own correction matters more than the binary: flat characters are not a defect. They are economical, memorable, and often funny, and a story needs them. The defect is a *cast* of flat characters in the positions that require interior conflict.

The craft vocabulary that operationalizes roundness is want / need / lie / wound, and no single theorist owns it. It earns its place because each term is testable:

- **Want** — the external, articulable goal. The character can say it. It drives plot.
- **Need** — what would actually repair the character, usually invisible to them and frequently opposed to the want. It drives theme.
- **Lie** (self-deception) — the false belief that makes the want feel necessary. It is a proposition, statable in one sentence, and it must be *false in the world of the story*.
- **Wound** — the prior event that made the lie plausible. Optional, but if present it must be causally prior, not decorative backstory.

Operational: the three-axis card is want / need / self-deception, with the wound as an annotation on the third. Write each in one sentence with a verb. Then run the check that kills most character work: **name the scene where the want and the need pull in opposite directions and the character chooses.** If no such scene exists, the character has a description, not a conflict.

**Contradiction must be costly.** A contradiction that costs the character nothing is a quirk: the assassin who loves cats. A contradiction that costs something is character: the assassin who loves cats and therefore cannot take the job that would let him leave. The test is a scene, not a trait list — state what the contradiction makes the character *lose*, and to whom. If the answer is "nothing", it is decoration. This is E4's territory, and the reason AI prose produces so many characters with interesting surfaces and no interior pressure.

Two further checks, in this order:

- **Say the lie as a sentence the character would deny.** If you cannot produce the sentence, the character has an attitude, not a belief, and no amount of backstory will convert one into the other.
- **Place the contradiction on a cost ledger.** Write what it costs, to whom, and in which scene. A contradiction that appears in the character file but never in a scene has not been written, only planned.

Flatness is the correct choice for most of the cast: the clerk, the foreman, the brother who exists to be relied on. Save interior conflict for the two or three positions where the story actually turns, and let the rest be legible in one stroke. A cast where everyone is round is a cast where no one is.

## 8. Premise and dramatic question (Egri, others)

Three terms get used interchangeably and must not be:

- **Theme** — the subject. One word or phrase: loyalty, inheritance, cowardice.
- **Premise** — a proposition *about* that subject, which the story tests by dramatising its consequences. Egri's shape is character + conflict + conclusion; the usable form is **"X leads to Y because Z"**.
- **Moral** — an instruction derived from the premise ("be loyal"). A moral is a conclusion the reader is handed; a premise is a hypothesis the story runs.

Operational: write the premise as one sentence of the form **"X leads to Y because Z"**, with a causal connective you can defend. Example: *Loyalty to a liar makes you the lie's accomplice, because loyalty without judgment transfers your agency to someone else's account of the world.* This is testable in a way that "the theme is loyalty" is not.

Then test the ending against it. Three legitimate outcomes, one illegitimate:

- **Confirms** — the story demonstrates Z, and the ending shows the cost paid.
- **Refutes** — the story sets up Z and the ending shows a case where the causal chain breaks, with the mechanism visible.
- **Complicates** — the story shows Z holding under one condition and failing under another, and both are dramatised.
- **Indifferent** — the ending resolves the plot without touching the premise. This is the failure: the story has been *about* something for two hundred pages and then stops.

**Conflict with §3.** An unreliable narrator can make the premise untestable: if every account of events is bent, the reader has no ground on which to verify 'X leads to Y because Z'. Resolution: the implied author's track must still deliver a verdict. The narrator may be wrong about the premise; the *text* must be legible about what actually happened, even if only in retrospect and even if the reader must assemble it from details the narrator let slip. An unreliable narrator whose unreliability leaves the premise unresolvable has produced a puzzle, not a story — which is a legitimate form, but a different one, and it needs to be chosen.

The **dramatic question** is the reader-facing version: the single yes/no question the plot keeps open, phrased so that either answer is a real answer. If only one answer is possible, there is no question and no forward motion — that is E1's gate.

## 9. Defamiliarisation / ostranenie (Shklovsky)

Shklovsky's claim: art exists to make perception difficult, to restore the sensation of things rather than to report their recognition. Habit automates perception — we stop seeing the chair, the street, the hand — and the literary device makes the familiar strange so it can be seen again. Note the precise target: the device attacks *habit of perception*, not vocabulary. Reaching for an unusual adjective is not defamiliarisation; it is decoration with a thesaurus.

Operational:

- Choose **one object per scene**, and choose the object the scene turns on — the thing that will be handled, broken, paid with, or refused.
- Render it as if seen for the first time, by one of three routes: **function** (what it actually does, described from the mechanism rather than the name), **scale** (a part described at the wrong magnification), or **sensory mismatch** (the wrong sense applied, or a sense given a property it does not have).
- Keep the surrounding prose plain. Defamiliarisation works by contrast; if every noun is strange, the device has no figure to stand against and the page reads as mannered.

The mannerism warning is the real risk, and it is the specific risk for a model: the instruction "make it strange" applied continuously produces a uniform weirdness that is itself a formula, and the reader adapts within a page. The device is a spot instrument. One per scene, on the load-bearing object, and never twice in the same paragraph.

The three routes, worked on the same object — a rubber hot-water bottle:

- **Function:** *A flat sack with a brass screw at the top, which you fill and then cannot put down.*
- **Scale:** *Its surface had gone the dull grey of a thing that has been boiled too often.*
- **Sensory mismatch:** *It gave off a smell like clean coins.*

All three avoid naming the object's use directly; all three make it perceptible again. None of them requires an unusual adjective.

**Conflict with §4.** Defamiliarisation pulls the reader's attention to the object; close psychic distance pulls it into the character's idiom. A scene at rung 5–7 that also defamiliarizes every object develops two competing attentions and reads as the author performing. Resolution: at close distance, defamiliarize only through the character's own frame — the object is strange *because* this character sees it that way, and the strangeness must be consistent with their lexical field (§10). Forced strangeness at close rung is the single most recognizable mannerism in literary pastiche.

## 10. Heteroglossia and dialogism (Bakhtin)

Bakhtin's **heteroglossia** is the presence of multiple social languages inside a single text: the speech of a profession, a generation, a class, an institution, a region. **Dialogism** is the claim that every utterance answers prior utterances and anticipates future ones — meaning lives between voices, not inside one. Applied to craft, both say the same thing: a character's voice is a *social fact* before it is a stylistic one. Register comes from where the person has been, not from a list of quirks.

Operational: every named character gets two assigned properties, recorded in the character file.

- **A lexical field they return to** — the domain their metaphors come from. A nurse reaches for triage, dosage, charting. A foreman reaches for load, tolerance, shift. Four to eight words or images, used across the story, not announced.
- **A syntactic habit** — clause length, where they put the qualifier, whether they ask or assert, whether they finish sentences. One habit, held consistently, optional under stress.

Then run the two tests:

- **The tag-strip test.** Delete every dialogue tag and beat. If you cannot tell who is speaking, you have one voice wearing hats — the most common dialogue failure in generated prose, and the reason characters feel interchangeable despite differing content.
- **The empty-room test.** A line that could be spoken into an empty room, answering nothing, is not dialogue; it is a statement the author needed on the record. Real dialogue replies to what was just said, or evades it in a way that is itself a reply.

Register difference is not accent spelling and not catchphrases. Catchphrases are the cheap substitute and they read as tags. The lexical field does the work because it is invisible until it recurs.

Same information, two registers — a shift supervisor and a new hire, both reporting a stopped machine:

- **Supervisor:** *It's down again. Third time this week. Log it, tag it, don't touch it until I've looked at the load.*
- **New hire:** *It made a noise and then it just — stopped? I didn't do anything. Should I get someone?*

The content is identical. The difference is what each speaker treats as obvious: the supervisor assumes procedure and repeats it in imperatives; the new hire assumes blame and asks permission. Neither voice carries a catchphrase, and neither is described by the narration.

## 11. Intertextuality and the canon

Kristeva's term, built on Bakhtin: a text is a mosaic of other texts, and meaning is produced by the relation, not by the individual piece. Three usable forms:

- **Allusion** — a pointed reference, expecting recognition, that imports a frame for the current scene. It works only if the reader can be expected to know it, and it fails loudly when they cannot.
- **Retelling** — borrowing structure or situation rather than words. The reader feels the shape before naming the source. Cheap to do badly, because surface plot transfers without the original's causal pressure.
- **Pastiche** — borrowing surface: diction, rhythm, period furniture. The most imitable and the least interesting, because it delivers the manner without the argument.

**Named references behave differently from vague ones.** A named text, brand, street, or song is a checkable claim: it carries specific associations, it can be verified, and getting it wrong costs credibility in a way that a vague gesture never does. A vague reference ("some old novel", "a brand he recognised") is unfalsifiable, and readers register it as evasion. This is also where the measured difference sits: `[data: StoryScope]` humans reference real texts and brands at roughly twice the rate of model-written stories (47% vs 24%). Treat that as a detection finding about corpus behaviour, not as an instruction to name-drop — a named reference that the scene does not use is worse than a vague one. The test is whether the reference does work: if you can swap it for another title and nothing changes, delete it or make it specific enough that the swap would break something.

**Conflict with §12.** Canonical retelling is the strongest form of intertextuality and the most tempting shortcut around causality: the borrowed shape supplies the reader's sense of inevitability for free, and the draft then has consequence without causation. Resolution: import structure only where your own causal chain independently produces the same turns. If the reader would still believe the turn with the source unrecognized, the borrowing is doing work; if the turn only feels inevitable because the source is recognizable, you have borrowed the debt and not the payment.

## 12. Plot grammar: functions and their limits (Propp, Todorov)

Propp's morphology reduced a corpus of Russian wonder tales to a sequence of **functions** — recurring actions defined by their role in the whole — and a small set of **spheres of action** (the hero, the donor, the villain, the helper, and so on). Todorov read narrative as a syntax: an equilibrium, a disruption, a transformed equilibrium, with the tale's units behaving like clauses that can be substituted and combined. Both are genuine analyses of structure, and both are descriptive grammars, not generative ones.

What the grammar is good for:

- **Recognising the skeleton.** Naming which function a beat is performing tells you whether it is doing work or filling space. A donor who gives a gift that is never used is a missing function, not a character.
- **Diagnosing gaps.** If the sequence jumps from lack to resolution without the test, the reader feels the shortcut even if they cannot name it.
- **Comparing.** Two drafts of the same chapter can be compared by function sequence rather than by vibe.

What it is bad for: **literal application.** A grammar derived from a corpus tells you what that corpus has in common — it cannot tell you what a new story needs. Filling all thirty-one slots produces the formulaic artifact Narraith exists to prevent, and the formula is recognizable precisely because it is complete. Two further limits: Propp's corpus is a specific historical genre, so the grammar is domain-bound; and the functions describe *what is done*, never *why this character would do it*, which is where agency lives.

Resolution rule: use plot grammar as a **post-hoc diagnostic** on a draft, never as a template for a plot. If a structural analysis makes you add a beat, the addition must be justified by a character's causal reason, not by the slot.

Reading a draft by function produces a list like this, and nothing more:

- lack stated → donor approached → test failed once → test passed → object received → return → recognition.

Then ask three questions of that list. Which function is missing and does the reader feel the absence? Which function is doubled and which of the two is doing less work? Which function is performed by a character whose causal reason you cannot state? The first two are structure, the third is agency, and only the third requires rewriting a scene rather than reordering one.

## 13. Readerly cooperation and gaps (Iser, Barthes)

Iser's account of reading: the text supplies schematized aspects and *indeterminacies*, and the reader concretizes them. Meaning is not in the text or in the reader but in the interaction — which makes the gap a designed component, not a defect. Barthes' five codes in *S/Z* give two of those components their engines: the **hermeneutic code** (the enigma — posed, delayed, partially answered, resolved) and the **proairetic code** (the sequence of actions whose completion the reader anticipates). Forward motion comes from these two, not from sentence-level beauty. A reader turning pages is holding an open question or an unfinished action.

Operational, and this is the part that distinguishes craft from vagueness:

- **A gap must be marked.** There must be something concrete for the reader to hold: an object that recurs, an anomaly someone notices, a phrase the narrator repeats without explaining, a date that does not fit. The reader completes meaning only when given a shape to complete. An unmarked absence is not a gap, it is missing information, and the reader experiences it as confusion or as an error.
- **Plant the enigma before the delay.** The hermeneutic code requires the question to be explicit enough to be *a question*. Withholding the question itself is not mystery; it is withholding.
- **Distinguish gap from ellipsis.** *Conflict with §2.* An ellipsis is a *temporal* absence — time skipped, and the reader knows it was skipped. A gap is a *semantic* absence — meaning withheld, and the reader does not know it is missing until later. They are not interchangeable: using an ellipsis where a gap was needed leaves a hole the reader reads as a cut, and using a gap where an ellipsis was needed leaves a fog the reader reads as vagueness. Which one you want is decided by whether the reader should know that something is missing.
- **Answer late, answer partially, answer once.** The failure mode in generated prose is the opposite: the enigma is resolved in the same paragraph it is posed, because the model is unwilling to leave a question standing. Check the distance between posing and answering; if it is under a scene, you have written exposition in the shape of suspense.

Marked versus unmarked, same withheld fact — that the brother is dead:

- **Unmarked:** the family eats dinner. The brother is not mentioned. The scene ends. Nothing has been withheld that the reader could notice; the reader assumes he was not invited.
- **Marked:** the family eats dinner, and the mother sets four places. Nobody moves the fourth plate. The scene ends. The reader now holds an object, and the object asks the question.

The marking is not a hint about the answer. It is a concrete thing for the reader to hold while the answer stays absent, and the reader's work is what makes the absence legible as design.

Barthes' **writerly/readerly** distinction follows: a readerly text hands over a fixed meaning, a writerly text makes the reader produce it. Most genre work is deliberately readerly and is not improved by becoming writerly. Choose, do not drift.

## 14. Endings

Five types, each with a price and a precondition:

- **Resolved** — the dramatic question is answered and the value at stake is fixed. Requires that the answer was in play and that the cost of reaching it has been paid on the page. Cost: closure forecloses rereading; the story becomes a delivery.
- **Ambiguous** — the question is answered in more than one defensible way, and the text supports each. Requires that the ambiguity be *structural*: two readings with evidence for both. Cost: ambiguity without evidence reads as an unfinished draft; the reader cannot tell design from failure.
- **Ironic** — the outcome contradicts what the protagonist (or the reader) expected, and the contradiction is legible as a judgment. Requires a stable implied position from which the irony is visible; without one, irony collapses into mere misfortune.
- **Circular** — the ending returns to the opening situation, changed in meaning if not in fact. Requires that the return be *earned by difference*: the same room, the same gesture, a different charge. Cost: if nothing has changed, circularity is stasis with a rhyme.
- **Open** — the story stops without closing the question, and the incompletion is the point. Requires that the reader be given the terms of the unresolved question, so that the openness is a considered refusal rather than a truncation. Cost: the highest tolerance demand on the reader; the wrong reader reads it as a missing chapter.

Two operational rules. First, **the ending must touch the premise** (§8); all five types can confirm, refute, or complicate it, and any of them can fail by indifference. Second, **the last movement should change the value one final time**, or explicitly refuse to — the refusal being marked. An ending that only summarizes what the reader already knows is a stop, not an ending. Revision of endings belongs to E14; the structural placement of the final turn belongs to `references/story-architecture.md`.

## 15. Theory into decisions: a mapping table

| Concept | Decision it forces | Where it is implemented in Narraith |
|---|---|---|
| Story vs. discourse (§1) | Separate the event chain from the delivery order; fix causality before prose | E2, `methodologies/01-plot-and-causality.md` |
| Order, duration, frequency (§2) | Assign every beat a speed and a position; no uniform tempo | E7, `methodologies/03-time-and-scene.md` |
| Focalization (§3) | Fix whose senses and vocabulary bound each scene; audit for head-hopping | E10, E15, `methodologies/04-prose-voice-originality.md` |
| Psychic distance (§4) | Set the opening rung and the direction of travel; move one rung at a time | E10, `methodologies/04-prose-voice-originality.md` |
| Scene and sequel, MRU (§5) | Order stimulus before response; give every disaster a processing unit | E8, `methodologies/03-time-and-scene.md` |
| Value charge (§6) | Name the value and its entry/exit charge; cut or merge unchanged scenes | E8, E2, `methodologies/03-time-and-scene.md` |
| Character axes (§7) | Fill want/need/self-deception; stage the costly contradiction | E3, E4, `methodologies/02-character-and-dialogue.md` |
| Premise (§8) | Write "X leads to Y because Z"; test the ending against it | E1, `methodologies/01-plot-and-causality.md` |
| Defamiliarisation (§9) | Choose one load-bearing object per scene to re-perceive | E11, `methodologies/04-prose-voice-originality.md` |
| Heteroglossia (§10) | Assign each speaker a lexical field and a syntactic habit | E9, `methodologies/02-character-and-dialogue.md` |
| Intertextuality (§11) | Decide named vs. dissolved reference, and make the named one work | E11, E12, `methodologies/04-prose-voice-originality.md` |
| Plot grammar (§12) | Use as post-hoc diagnostic; never as a beat template | E2, `methodologies/01-plot-and-causality.md` |
| Gaps and codes (§13) | Mark the gap with a concrete object; keep the enigma open past its scene | E6, `methodologies/01-plot-and-causality.md` |
| Endings (§14) | Choose the ending type and pay its stated price | E1, E14, `methodologies/05-continuity-and-revision.md` |

## What theory cannot do

- **It describes successful texts; it does not generate them.** Every concept here was derived by looking backward at work that already succeeded. Backward description does not invert into forward production, which is why a draft that satisfies every definition can still be dead.
- **Applied as a checkbox, a concept produces the genericness it was meant to prevent.** A scene that has a goal, a conflict, a disaster, a value turn, and one defamiliarised object, all present and all inert, is the recognizable artifact of a writer optimizing for the checklist. The concepts describe properties that good scenes *have*; they do not cause them.
- **No concept here is mandatory in every story.** Focalization can be inconsistent on purpose; value can refuse to turn; a story can have no premise it tests; dialogue can be deliberately uniform. Each deviation is a decision with a cost, and the cost is the only thing that has to be argued.
- **Genre and culture change the rules.** The implied reader that Iser's gaps presuppose is a specific historical reader; the register that reads as authentic in one tradition reads as affectation in another; the canonical allusion that lands in one literature is invisible in the next. State the tradition you are writing in before you apply the rule.
- **Theory has no access to the page.** It cannot tell you whether a sentence is bad. It can tell you what work a sentence is failing to do — that is the whole of its authority.
- **Where two concepts conflict, the conflict is usually real and the resolution is local.** The five conflicts marked in this file (§5/§6, §9/§4, §11/§12, §13/§2, §3/§8) are not oversights; each is a genuine tension between two true descriptions, resolved by deciding which one the current scene is for.
- **Nothing here replaces a reader.** The measured signature patterns in `references/ai-narrative-signature.md` and the ladder in `references/quality-levels.md` give you a diagnosis; they do not give you the sentence. That remains the work.
