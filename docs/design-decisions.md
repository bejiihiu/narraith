# Design decisions

> Purpose: a record of the choices that could have gone another way, and why they did not.
> Read when: reviewing the skill, proposing a structural change, or wondering why an obvious
> alternative is missing.
> Related: `docs/architecture.md`, `docs/limitations.md`.

Format: context → decision → consequence → rejected alternative. Numbers in brackets refer to the
research dossiers in `references/research/`.

---

## D1. Narrative decisions as the primary intervention

**Context.** The corpus offers three plausible levers: prose surface, narrative structure, and
detection-style feedback. StoryScope shows narrative features separating human and AI fiction at
93.2% macro-F1, and the narrative classifier held at 93.9% on a 278-story Gemini subset after
span-level rewriting (from 95.5% before) [1].

**Decision.** The skill's load-bearing layer is narrative decision-making. Prose modules exist to
execute decisions, not to lead them.

**Consequence.** A draft can pass every prose check and still be rejected by the scene gate. This is
intended: a beautifully written scene with no state change is the characteristic failure.

**Rejected.** A prose-first skill. It would be easier to write, immediately visible to users, and
wrong: surface advice converges, and the evidence says the surface is what editing removes first.

**Honest caveat.** None of the five papers tests whether *teaching* narrative decisions improves
generation. That transfer is `[hypothesis]`. See `docs/limitations.md`.

---

## D2. No word or punctuation blacklists

**Context.** The most popular AI-prose advice is a list of banned tokens: "delve", "tapestry", em
dashes, adverbs. These lists circulate because they are easy to apply and easy to measure.

**Decision.** No token bans anywhere in the skill. Every stylistic prohibition is restated as a
function test ("is this word doing work?"), and every rule carries the condition under which it does
not apply.

**Consequence.** The skill is harder to audit mechanically. The validator cannot check compliance,
only structure. That is accepted.

**Rejected.** A lexicon of forbidden words with a linter. It produces convergent prose, punishes
legitimate uses, and is trivially gamed by paraphrase — the same fragility the fingerprinting study
documents for surface signals [5].

---

## D3. Over-determination as the named enemy

**Context.** "AI writing" is usually described as bland, purple, or repetitive. StoryScope's actual
findings are more specific: AI fiction explains theme more (77% vs 52% of narrators state the theme),
resolves morally more (47% vs 27% internal-acceptance endings), and renders emotion somatically far
more (81% vs 38%) while labelling it far less (8% vs 29%) [1].

**Decision.** The skill names one failure — over-determination: resolving what should stay open,
withholding the concrete that would let the reader infer. Both halves matter. Most craft advice only
attacks the first and accidentally worsens the second.

**Consequence.** The emotion guidance is calibrated rather than prohibitive: three channels, chosen
by scene function. "Show, don't tell" appears only as a historical note with its failure modes.

**Rejected.** Adopting "show, don't tell" as doctrine. The data show models already over-apply it.

---

## D4. Fifteen engines, fourteen routes in five files, one doctrine

**Context.** Modules could be organised by genre, by length, by craft topic, or by task.

**Decision.** Knowledge is organised by craft topic (`references/`), decisions by reusable engine
(`methodologies/`), and tasks by route (`workflows/`). Doctrine stays in one file.

**Consequence.** Some duplication of *pointers* but not of content. A reader can enter from a task
("write a chapter") or from a problem ("the middle sags") and reach the same engine.

**Rejected.** A single monolithic guide. It would exceed the always-loaded budget and encourage
skimming instead of retrieval.

---

## D5. Adaptive depth with an explicit tier system

**Context.** Skill instructions tend to be applied uniformly: a 200-word scene gets the same
ceremony as a novel. Over-processing produces cautious, symmetrical, thesis-driven prose — the very
failure the skill targets.

**Decision.** Three tiers (A: under 300 words, B: scene to chapter, C: long or structurally complex).
Tier is inferred, never asked. Two triggers move work between tiers: repeated local failure escalates,
an oversized plan de-escalates.

**Consequence.** The model must exercise judgement about scope, which is itself a narrative skill.
Miscalibration is visible in the output and correctable in one instruction.

**Rejected.** A mandatory intake questionnaire. It shifts work to the user and produces the same
plan for every story.

---

## D6. The Decision Ledger as the central artifact, kept short

**Context.** Planning artifacts can either externalise decisions or substitute for writing.

**Decision.** One ledger, fourteen fields, with an eight-field minimum variant. Every field maps to
a failure that prose cannot repair.

**Consequence.** Long-form work has a persistent object to test scenes against. Short work uses the
minimum variant or the eight decisions in `SKILL.md`.

**Rejected.** A full story bible as the entry artifact. It is a filing system, not a decision
procedure, and it grows faster than the manuscript.

---

## D7. Research claims carry markers; hypotheses are labelled

**Context.** The project sits on five detection studies. It would be easy — and dishonest — to present
their F1 scores as evidence that the skill writes better fiction.

**Decision.** Three markers: `[data: Paper]`, `[theory]`, `[hypothesis]`. The synthesis file states
what each paper cannot support. The limitations file lists every load-bearing hypothesis with a
falsification condition.

**Consequence.** Some sentences are longer. Reviewers can audit the epistemic status of any claim.

**Rejected.** A single "based on research" banner. It would launder inference as evidence.

---

## D8. Two language layers, no universal baseline

**Context.** English craft advice translated into Russian produces translationese; Russian advice
applied to English produces periodic, comment-heavy prose that reads as dated.

**Decision.** Separate Russian and English craft modules, a transfer-notes module, and per-level
language-variance notes. No language is the default.

**Consequence.** The skill is larger, and a third language requires a new file rather than a
translation. That is the correct cost.

**Rejected.** One language-neutral prose module. It would be neutral in the way that mediocre
translations are neutral.

---

## D9. Originality as default-avoidance, not novelty

**Context.** DetectGPT and DNA-GPT both formalise a version of "the model's own output is the output
it would produce again" [3][4]. Applied naively to craft, this becomes "be unpredictable", which
produces contrivance.

**Decision.** Originality is operationalised as: name the modal choice, generate alternatives at the
level of *decision*, score them on plausibility and cost, choose a non-modal option with a
preparation trail, then stop after two rounds.

**Consequence.** Surprises must be seeded and priced. The skill can reject a twist as arbitrary even
when it is unexpected.

**Rejected.** A "twist generator" or a randomness step. Both produce the thing the skill exists to
prevent.

---

## D10. Critique reports few defects, ordered by leverage

**Context.** LLM critique tends to list everything it notices. A writer — or a model — cannot act on
twelve items, and the list flattens fatal and cosmetic defects into equals.

**Decision.** At most two structural and three local defects per pass, ordered by leverage, each with
a quoted span, a level tag, and a mechanism. Repairs are executed one at a time with a regression
check.

**Consequence.** A critique may omit real problems. That is preferable to a critique that changes
nothing.

**Rejected.** A full issue list with severity labels. It looks thorough and functions as noise.

---

## D11. Surface metrics as proxies, labelled everywhere

**Context.** There is pressure to produce a number that says whether a draft improved. Sentence
variance and lexical diversity are computable and look objective.

**Decision.** `scripts/story_metrics.py` computes them, and every mention calls them proxies. They are
used for before/after comparison and regression detection, never as a quality score.

**Consequence.** The evaluation relies on blind human-style judgement for the actual claim, which is
slower and less impressive-looking. That is the honest design.

**Rejected.** A composite "quality score". It would create false precision and reward balance over
character.

---

## D12. No automated AI detection

**Context.** The five papers are detection papers; the temptation is to add a "does this read as AI?"
score.

**Decision.** The skill offers a *signature audit* — a qualitative self-check against documented
defaults — and explicitly refuses detection claims.

**Consequence.** Users who want a detector are pointed elsewhere. The skill cannot be gamed into
adversarial prose, because it is not optimising against a classifier.

**Rejected.** A heuristic detector. It would be inaccurate, and worse, it would make the skill's
success metric "fool the detector", which is not the same as "write well".

---

## D13. English instruction surface, multilingual subject matter

**Context.** The skill is used by models that read English best, and by users who may write in any
language.

**Decision.** All instructions in English. Russian, and other languages, appear as subject matter:
examples, terminology, craft notes. `README.ru.md` serves Russian-speaking readers.

**Consequence.** One consistent instruction surface; language-specific depth where it matters.

**Rejected.** A Russian-language skill. It would fragment the instruction surface and make the repo
useless to most of its potential audience, without improving the Russian prose module, which is
already written in English about Russian.
