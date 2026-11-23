---
name: narraith
description: "Literary craft system for writing, planning, continuing and revising fiction: short stories, novels, chapters, scenes, dialogue, characters, worlds, nonlinear structures and multi-thread plots. Use this skill whenever the user asks for creative prose of any length, even a single scene or exchange of dialogue, and whenever they ask to critique, edit, rewrite, continue, diagnose or outline fiction. It supplies narrative decision procedures (agency, causality, information flow, temporal structure, subtext), prose craft across seven levels, and a revision engine that fixes structural defects before cosmetic ones. Also trigger on Russian requests such as «напиши рассказ», «напиши роман», «напиши сцену», «диалог», «отредактируй текст», «продолжи историю», and on genre work (literary, horror, crime, SFF, romance, historical). Do not use for non-fiction, marketing copy, poetry or song lyrics."
---

# Narraith

A system for making narrative decisions, then writing prose that serves them, then repairing what failed.

The failure this skill exists to correct is not bad grammar. It is **over-determination**: prose that
explains what it should leave inferable, resolves what it should leave open, and withholds the concrete
detail that would have made inference possible. Everything below is aimed at that.

## How to use this file

Read it fully once. It is self-sufficient for short work. For anything longer than a scene, or for
revision, follow the routing table at the end into the deeper modules. Do not read all modules
"for completeness" — read the two or three the task actually needs.

## The six laws

1. **Decide first, decorate second.** Prose is the execution of a decision. If you cannot state the
   decision a paragraph is executing, the paragraph is decoration.
2. **A scene changes a state.** Knowledge, trust, power, possibility, or the reader's understanding.
   If nothing changed, it is summary; either make it change something or cut it.
3. **Agency is causal, not admirable.** Characters cause events through costly choices. Events that
   happen *to* a character for the author's convenience are the most common structural failure.
4. **Meaning is inferred, but inference needs handles.** Do not announce the theme. Do not remove the
   evidence either. The reader must be able to reconstruct the meaning from concrete material.
5. **The obvious choice is the draft choice.** Your first solution is the modal continuation of the
   setup. Draft it, then test two or three alternatives before committing.
6. **Do not perform the method.** Never show the user a filled-in ledger unless they asked for planning
   artifacts. The work happens; the artifact stays behind.

## The seven levels

Every defect belongs to a level. Naming the level prevents the classic error of line-editing a
structural problem. Use these tags in diagnosis (`[L5]`) and route repairs accordingly.

| Level | Name | What it governs | Typical failure |
|---|---|---|---|
| L1 | Lexical | word choice, precision, register, repetition | vague evaluative nouns instead of objects |
| L2 | Syntactic | length, rhythm, order, period, emphasis | uniform sentence length, stacked participles |
| L3 | Stylistic | voice, tone, image density, figuration | a generic "literary" voice; ornament without function |
| L4 | Semantic | meaning, subtext, ambivalence, echo | the meaning is stated rather than built |
| L5 | Narrative | plot, causality, agency, structure | events arranged for convenience; single-track tidiness |
| L6 | Psychological | motivation, contradiction, defence, cost | motivation explained instead of dramatised |
| L7 | Literary | composition, wholeness, originality, impact | competent parts, no whole; predictable |

Deep treatment, including the misattribution table (symptom at one level, cause at another):
`references/quality-levels.md`.

## Adaptive depth

Judge the task before choosing a process. The cost of over-processing is as real as the cost of
under-processing: it produces cautious, thesis-driven prose.

**Tier A — a line, an image, a short exchange (under ~300 words).**
No plan. Write. Check only: does it contain one concrete thing, and does it avoid explaining itself?
Stop.

**Tier B — a scene, a short story, a chapter (300–7,500 words).**
Run the eight decisions below (five minutes of thought, not a document). Write. Then run the scene
gate and one revision pass. Do not read the methodology modules unless a specific failure appears.

**Tier C — a novella, a novel, anything over roughly 7,500 words, a multi-thread or non-linear
structure, a continuation of existing work.**
Full Decision Ledger, continuity ledger if material exists, structural plan before prose, per-scene
cards, and staged revision. Read the relevant workflow file and the engines it names. Artifacts stay
internal unless the user asks to see them.

If the user's request is ambiguous between tiers, choose the lower tier and let the draft reveal
whether more structure is needed. Key the tier to the **unit requested**, not to the size of the
imagined work: a single chapter of an unwritten novel is Tier B plus a continuity read, because the
deliverable is a chapter, not a plan. If a Tier C route requires material that does not exist — a
spine, a previous chapter, a word budget — invent the minimum, state it in one line, and proceed.

Never open with a questionnaire. Infer what you can, name your assumptions in one line, and proceed.

## The eight decisions

For Tier B and C. Answer in your head or in a scratch note, not in the reply.

1. **Kind.** Is this attitudinal (a stance toward something), situational (a condition rendered),
   narrative (a change through events), or expository (an argument embodied)? Most requests that
   "feel like a story" are situational. Choosing narrative by default is itself a default.
2. **Dramatic question.** One question the reader wants answered, which cannot be answered until the
   end. If you cannot phrase it as a question, you have a topic, not a story.
3. **Pressure.** What force resists the protagonist, and why is that force *right from inside itself*?
   An obstacle with no internal justification produces a villain, and a villain produces melodrama.
4. **Want / need / lie.** What the character pursues, what they actually require, and the false belief
   that makes the pursuit costly. All three must be concrete enough to be shown in behaviour.
5. **Cost.** What is lost by acting, and what would be lost by succeeding. A story without cost has
   stakes only in the synopsis.
6. **Information plan.** What does the reader know at each point, what does the protagonist know, and
   what keeps the gap open? Write the three or four revelations in order.
7. **Time.** Which order serves the question? Chronological is a choice, not a neutral baseline.
8. **Refusals.** Name the two or three obvious solutions you are rejecting and what replaces each.
   This is the originality mechanism, not a decoration ([details](references/originality.md)).

For the full ledger with all fields: `templates/decision-ledger.md`.

## The scene gate

Run this on every scene you write, in this order. Stop at the first failure.

1. **State change.** Name what is different at the end. If the answer is "nothing, but it's
   atmospheric", the scene is a fragment — fold it into a scene that changes something. The one
   exception is a scene that deliberately refuses to move a value; then the refusal itself must be
   marked and paid, and named as a refusal rather than defended as atmosphere.
2. **Agency.** Who acts, and what does the action cost them? If the scene's turn is produced by an
   accident, a message, or a new character arriving, the turn is not yet earned. If the subject is the
   impossibility of choice, the passivity must be chosen against visible alternatives and priced on the
   page; the turn then stays where it is, and you say so.
3. **Entry and exit.** Enter as late as possible, leave as early as possible. The last line should
   land on the change, not after it.
4. **Information.** Does the scene give the reader something to hold — a detail, a discrepancy, a
   question — or does it only transmit plot?
5. **Voice.** Is the narration doing something only this narrator could do? If any competent narrator
   could have written it, [L3] is flat.
6. **Modal test.** Would a competent re-writer, given the same setup, produce this scene? If yes,
   you have written the default. Revise the decision, not the adjectives
   ([the continuation test](methodologies/04-prose-voice-originality.md)).

For a scene that carries weight, write the card before the prose: `templates/scene-card.md`. Its fields
force the gate's answers before the sentences exist.

## Revision triage

Never revise top-down through the text. Revise by leverage, in this order, and stop when the budget
runs out. If the unit is smaller than a scene — a paragraph, a passage, a page — run only the pass the
sample can support; do not diagnose architecture from an excerpt.

1. **L7/L5 — architecture.** Wrong protagonist, missing cost, unearned turn, an ending that answers the
   wrong question. Fixing these invalidates prose work, so do them first.
2. **L6 — motivation.** Replace explained motive with a decision the reader can see and resist.
3. **L4 — information and subtext.** Move meaning out of statements and into arrangement: what is
   withheld, what is juxtaposed, what is repeated with a changed sense. Do not apply this to a passage
   whose function *is* the statement — a confession, a self-diagnosis, a deliberate naming. The labelled
   channel is a decision, not a defect.
4. **L5 (scene level) — scene shape.** Merge, cut, or re-enter scenes.
5. **L3 — voice.** Establish the narrator's attitude and lexical field; remove prose that any narrator
   could have written.
6. **L2 — rhythm.** Vary sentence length by function, not by rule. A long sentence earns its length by
   carrying a complex thought or a sustained image; a short one lands a change.
7. **L1 — words.** Last, and only where the reader would stumble or where a word is doing no work.

Full procedure and repair patterns: `references/editorial-intelligence.md`.

## Dialogue, in one page

- **Two agendas, not two positions.** Each speaker wants something from the other in this scene, and
  usually will not ask for it directly. If both speakers say what they mean and nothing is at stake in
  the saying, the scene is an exchange of information. But transparency is a legitimate effect:
  a confession, a declaration, a briefing, a formal warning. There the directness *is* the choice, and
  blurring it is the defect.
- **Reply to the act, not the line.** The strongest reply answers what the other person is *doing*
  (testing, retreating, claiming innocence), not the literal content.
- **Idiolect is syntax and vocabulary, not accent.** Give each character a habitual sentence shape and
  a small set of words they return to. Never mark class or origin with phonetic spelling.
- **Silence and logistics are content.** Who changes the subject, who answers a question with a
  question, who gives a precise time and date — these carry more than stated feeling.
- **Cut the greeting.** Enter after the opening ritual and leave before the farewell.
- **Subtext needs a surface.** If nothing is said, there is no subtext, only absence. The surface talk
  must be genuinely about something (the parking fee, the sister's operation).

Deep treatment: `references/character-intelligence.md`, engine E9 in
`methodologies/02-character-and-dialogue.md`. Worked pairs: `examples/02-dialogue-weak-vs-strong.md`.

## Continuity, in one page

For any work with established material, keep four lists and update them as you write: **facts**
(dates, ages, injuries, objects), **knowledge** (who knows what, and since when), **debts** (promises,
threats, unanswered questions), **names** (spellings, forms of address, who is allowed to use which).
Before writing a new chapter, read them. After writing, add to them. Contradiction is not a detail
problem; it destroys the reader's trust in the whole narrative.

Full system and templates: `references/continuity-memory.md`, `templates/continuity-ledger.md`.

## Russian and English

The prose modules are language-specific on purpose. English craft advice translated literally into
Russian produces translationese: over-explicit pronouns, flattened intonation, lost aspect, and
sentences that distribute information the way English does. Russian prose distributes information by
word order and aspect; English by syntax and stress. When writing in Russian, read
`references/russian-prose.md` before the first paragraph, not after. For English, the relevant
defaults are in `references/english-prose.md`.

Do not apply English genre conventions as a universal standard. A Russian short story's tolerance for
unresolved moral material, its narrator's licence to comment, and its paragraph norms differ.

## What not to do with this skill

- **Do not ban a word or a mark as such.** A long dash, an adverb, a simile, the word "suddenly" — each is
  a tool with conditions. Ban it only where you can name the sentence in which it replaces a decision,
  and name the decision that should have been made instead.
- **Do not invert the defaults.** "AI writes tidy plots, so I will write a messy one" produces
  arbitrary mess. The correction is a *justified* choice, not the opposite of a statistic.
- **Do not apply every engine.** Fifteen engines exist; a story needs three or four. A text that
  satisfies every checklist is a text with no centre.
- **Do not claim measurement.** This skill reasons about texts. It does not compute probabilities,
  detect authorship, or reduce a text to a single quality score. The scripts in `scripts/` compute
  surface proxies
  and say so.

## Research basis

This skill is built on five studies plus narratology. Their findings are cited as `[data: <paper>]`
where they are used; our own rules are marked `[hypothesis]`. Read the dossiers before quoting numbers.

1. **StoryScope** — Russell et al., *StoryScope: Investigating idiosyncrasies in AI fiction*, COLM 2026.
   https://arxiv.org/pdf/2604.03136 — 10 narrative dimensions, 304 features, 61,608 stories; narrative
   features alone separate human from AI fiction at 93.2% macro-F1 and survive stylistic rewriting.
2. **Ghostbuster** — Verma et al., NAACL 2024. https://aclanthology.org/2024.naacl-long.95.pdf —
   structured search over interpretable feature combinations; multi-signal evidence instead of a verdict.
3. **DetectGPT** — Mitchell et al., 2023. https://arxiv.org/pdf/2301.11305 — probability curvature;
   the reason to treat fluency and predictability as different properties.
4. **DNA-GPT** — Yang et al., 2023. https://arxiv.org/abs/2305.17359 — divergent n-gram analysis;
   the basis of the continuation test for predictable narrative choices.
5. **Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting** — Modarres et al., 2026.
   https://arxiv.org/pdf/2610.28434 —
   multi-resolution fingerprinting; behavioural and formatting cues collapse when surface form is
   scrubbed, stylometry is weakest across languages, lexical n-grams are durable in-language but
   language-bound, and semantic representation travels best. A warning against building a quality model
   on surface tells.

Full bibliographic records, methodology, results, limitations and the Research → Capability map:
`references/research-foundations.md`. Individual dossiers: `references/research/`.

## Routing table

| The request is… | Read first | Then |
|---|---|---|
| a short story | `workflows/01-short-form.md` | `references/story-architecture.md` |
| a novel, novella, or long serial | `workflows/02-long-form.md` | `references/continuity-memory.md`, `references/story-architecture.md` |
| chapter 1 of an unplanned novel | `workflows/02-long-form.md`, W4 | infer a one-line spine, state it, write the chapter |
| a scene, dialogue, character, or world | `workflows/03-scene-and-ensemble.md` | the matching engine |
| a continuation, rewrite, or edit | `workflows/04-continuation-and-revision.md` | `references/editorial-intelligence.md` |
| critique only ("why doesn't this work?") | `workflows/04-continuation-and-revision.md`, W10 stages 1–2 | `references/literary-critique.md` |
| a voice match, or non-linear / multi-thread structure | `workflows/05-voice-and-complex-structure.md` | `references/temporal-complexity.md` |
| "why doesn't this work?" | `references/literary-critique.md` | `references/quality-levels.md` |
| "does this read as AI?" | `references/ai-narrative-signature.md` | the audit procedure there |
| a genre question ("is this a thriller?") | `references/genre-and-form.md` | the workflow for its length |
| Russian prose | `references/russian-prose.md` | `references/multilingual-notes.md` |

## File map

```
SKILL.md                          this file: doctrine, levels, gates, routing
references/
  research-foundations.md         the five papers: what they show, what they do not
  research/01..05                 per-paper dossiers with methodology and limits
  narrative-theory.md             narratology as decision vocabulary
  ai-narrative-signature.md       evidence-based catalogue of model defaults
  quality-levels.md               L1-L7 in depth; misattribution table
  story-architecture.md           premise, spine, subplots, acts, endings
  genre-and-form.md               length forms and genre contracts
  character-intelligence.md       want/need/lie, contradiction, relationships, voice
  prose-engineering.md            sentence, paragraph, image, description, POV
  russian-prose.md                Russian-specific craft and translationese
  english-prose.md                English-specific craft and register
  temporal-complexity.md          order, duration, focalization, unreliability
  originality.md                  default-avoidance without arbitrary novelty
  literary-critique.md            diagnosis: 12 axes, severity, evidence
  editorial-intelligence.md       developmental → line → copy, repair patterns
  continuity-memory.md            bibles, ledgers, contradiction sweeps
  multilingual-notes.md           cross-language transfer and its limits
methodologies/                    fifteen engines, each with a procedure and a failure list
workflows/                        fourteen task routes with gates and repair loops
examples/                         ten worked examples: pairs and calibrations
templates/                        copyable artifacts
checklists/                       pre-draft, scene, dialogue, continuity, final, RU, EN
tests/                            eval prompts, rubric, protocol, results
docs/                             architecture, research map, limitations
scripts/                          structure validator, surface-proxy metrics
```

When a link above points to a file you have not read and the task depends on it, read it. Otherwise
write.
