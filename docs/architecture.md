# Narraith architecture

> Purpose: explain why the skill is shaped this way, so that future maintainers change it deliberately.
> Read when: extending the skill, reviewing a proposed module, or wondering why a rule exists.
> Related: `SKILL.md`, `docs/design-decisions.md`, `docs/research-map.md`, `docs/limitations.md`.

## 1. The problem, stated precisely

A capable language model asked to write fiction produces competent prose that fails in a predictable
pattern. StoryScope measured the pattern across 61,608 stories: the model states its theme, closes its
causal chains, keeps one track, resolves morally, renders emotion somatically, and avoids naming real
texts. The stories cluster tightly in narrative space; human stories are more dispersed and rarer.

Three readings of that result are possible.

- *Surface reading*: the model needs better sentences. This is the reading most writing advice assumes,
  and it is the weakest: on a 278-story Gemini subset, span-level rewriting moved detection only from
  95.5% to 93.9%. The rewriting was done by Gemini prompted with professional examples, not by editors,
  and the narrative classifier's corpus-wide baseline of 93.2% is a different denominator.
- *Deficit reading*: the model lacks knowledge of craft. This is implausible for current models, which
  can recite every rule in this repository.
- *Decision reading*: the model is not making choices. It is sampling the modal continuation of a
  premise and then justifying it. Quality is a by-product of decisions made under constraint, and the
  model has no mechanism that forces those decisions.

Narraith is built on the third reading. That is an engineering hypothesis, not a finding of the papers
(see `docs/limitations.md`). The architecture is designed so the hypothesis can fail visibly: every
mechanism has a stated failure condition, and the evaluation protocol measures output, not compliance.

## 2. Design constraints

1. **The model must be able to act on it without a second model.** No mechanism may require log
   probabilities, classifiers, embeddings, or an external service.
2. **Simple requests must stay simple.** A user asking for a 200-word scene should not receive a
   planning document. Over-processing is a failure mode with its own signature: cautious, thesis-driven,
   symmetrical prose.
3. **No blacklists.** Word and punctuation bans are context-free rules applied to context-dependent
   decisions. They also converge: every model avoiding the same tokens produces the same voice.
4. **Claims must be traceable.** Research findings, craft theory, and our own hypotheses are marked
   differently. No invented statistics.
5. **Progressive disclosure.** The always-loaded layer must fit in a few hundred lines. Depth is
   retrieved by task, not preloaded.
6. **Bilingual by design, not by translation.** Russian and English prose have different default
   distributions of information. A single set of rules applied to both produces translationese in one.

## 3. The five layers

```
                 ┌──────────────────────────────────────────┐
                 │ SKILL.md                                 │
                 │ doctrine · 7 levels · gates · routing    │  always loaded
                 └───────────────┬──────────────────────────┘
                                 │ task requires depth
        ┌────────────────────────┼─────────────────────────┐
        ▼                        ▼                         ▼
┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ references/   │       │ methodologies/  │       │ workflows/      │
│ knowledge     │◄─────►│ 15 engines      │◄─────►│ 14 routes       │
│ why + what    │       │ how to decide   │       │ what order      │
└───────┬───────┘       └────────┬────────┘       └────────┬────────┘
        │                        │                         │
        ▼                        ▼                         ▼
┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ templates/    │       │ checklists/     │       │ examples/       │
│ artifacts     │       │ verification    │       │ calibration     │
└───────────────┘       └─────────────────┘       └─────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ tests/ scripts/ │
                        │ measurement     │
                        └─────────────────┘
```

**Doctrine (SKILL.md).** Five laws, the seven-level vocabulary, the eight decisions, the scene gate,
revision triage, the routing table. This is the only layer guaranteed to be in context. It must be
sufficient for Tier A and Tier B work on its own.

**Knowledge (references/).** Why a technique works and what it costs. Narratology, the evidence
catalogue, per-level depth, language-specific craft, genre contracts. Written to be *read*, not
recited: each concept ends in a decision it forces.

**Procedure (methodologies/, workflows/).** Engines answer "how do I make this decision well".
Workflows answer "in what order, for this kind of request, with what artifacts and gates". The split
matters: engines are reusable across lengths and genres; workflows are route-specific and may combine
engines differently. A novel and a 900-word story both use E2 (causal spine); they do not use it at the
same resolution.

**Artifacts (templates/).** The Decision Ledger, character and world bibles, continuity ledger, scene
card, revision plan, voice contract. These exist because working memory is the binding constraint in
long-form work, not knowledge. Every template is copyable and short enough to actually fill in.

**Verification (checklists/, tests/, scripts/).** Checklists are gates inside the writing process.
Tests are the external evaluation of the skill. Scripts compute surface proxies only, and are labelled
as proxies everywhere they appear.

## 4. Why narrative decisions carry the primary weight

Three reasons, in order of strength.

1. **Durability.** Narrative choices survive rewriting; surface choices largely do not. StoryScope's
   narrative classifier lost only 1.6 points on a rewritten subset, while the fingerprinting study found
   behavioural-feature classification accuracy falling from 52.4 to 25.6 across crop, format strip and
   case/punctuation scrub — the last step alone accounts for 16.3 of the 26.8 points — and stylometric
   attribution falling to 19.7% across languages against a 12.5% chance baseline. A skill that trains the
   durable layer is not obsoleted by the next model's improved sentence rhythm.
2. **Non-convergence.** Surface advice converges: if every model avoids the same constructions, the
   result is a new uniform style. Decision procedures diverge by construction, because they are
   parameterised by this story's premise, this character's cost, this reader's information state.
3. **Leverage.** A structural fix changes every sentence downstream. A lexical fix changes one word.
   Revision triage in `SKILL.md` follows the same ordering for the same reason.

This does not demote prose. Prose is where the decisions become perceptible, and a decision executed
in flat prose is invisible. The claim is about *order of operations*, not importance.

## 5. The decision artifact

The Decision Ledger is the architectural hinge. It converts implicit sampling into explicit
commitment, and it gives revision something to test against: a scene can be judged against the
decision it was supposed to execute.

Its fields were chosen to cover the failure modes that prose cannot repair:

| Field | Failure it prevents |
|---|---|
| dramatic question | a topic presented as a story |
| pressure with internal justification | villain-shaped obstacles, melodrama |
| want / need / lie | coherent but unmotivated behaviour |
| cost of acting and of succeeding | stakes that exist only in summary |
| information plan | twists that are either obvious or unearned |
| temporal plan | chronology by default |
| refusals | the modal continuation |

The ledger is deliberately short. A long planning document becomes its own substitute for writing:
the model satisfies the document and the story goes flat.

## 6. Adaptive depth as a first-class mechanism

The same request can need three lines or three weeks. The skill estimates tier from scope, existing
material, and structural complexity, and states its estimate implicitly by behaviour rather than by
asking.

Two guards keep the estimate honest:

- **Escalation trigger.** If a draft fails the scene gate twice at the same point, escalate one tier
  rather than revising harder at the current one. Repeated local failure usually means a structural
  decision is missing.
- **De-escalation trigger.** If the plan exceeds roughly one page for a story under 2,000 words, the
  plan is longer than the work. Cut the plan to the eight decisions and write.

## 7. Language architecture

There is one doctrine, two craft layers, and a set of transfer notes.

- `references/russian-prose.md` — information structure via word order, aspect as pacing, the Russian
  tolerance for narratorial comment, skaz, paragraph norms, translationese markers, dialogue punctuation
  conventions.
- `references/english-prose.md` — stress-timed rhythm, Germanic/Latinate register, free indirect
  discourse, the comma splice as voice, the "show don't tell" inheritance and its limits.
- `references/multilingual-notes.md` — what transfers and what does not; how to write in a third
  language without importing either default.

No language is treated as the baseline. The seven levels are language-neutral axes; their observable
signals are not, which is why each level's section in `references/quality-levels.md` ends with a
variance note.

## 8. Verification design

Three independent checks, none of which trusts the skill's own prose about itself.

1. **Structural** (`scripts/validate_skill.py`): frontmatter, links, placeholders, size, fence balance.
   Runs in CI on every push. Catches rot, not quality.
2. **Surface proxies** (`scripts/story_metrics.py`): sentence distribution, lexical diversity, dialogue
   share, emotional-channel ratio, repetition. Explicitly not a quality score. Used to compare a draft
   with its revision and to catch regressions such as flattening during editing.
3. **Blind evaluation** (`tests/protocol.md`): paired with-skill / without-skill generations on the same
   prompts, judged blind against a 12-criterion rubric, with position randomised and agreement reported.
   The rubric measures the twelve properties the skill claims to improve; the protocol states what the
   result can and cannot support.

## 9. What was deliberately left out

- **A single quality score.** Averaging seven levels into one number creates false precision and
  rewards balance over character. The level profile is reported unaggregated.
- **Per-genre rulebooks for every genre.** Genre contracts are principles plus a small number of
  load-bearing conventions (`references/genre-and-form.md`). Exhaustive trope lists date quickly and
  encourage formula.
- **Automated detection.** Out of scope, and a conflict of interest: a writing skill that optimises
  against a detector produces adversarial prose, not good prose.
- **A prose generator prompt.** The skill teaches decisions. A house style would contradict the goal of
  preserving the author's voice.
- **Word lists of any kind.** See constraint 3.

## 10. Extension points

- New engine: add to `methodologies/` in the fixed eight-part format, register it in `SKILL.md`'s file
  map, and add a failure condition to `docs/limitations.md` if it rests on a hypothesis.
- New language: add a craft file, a variance note per level in `quality-levels.md`, and a transfer note
  in `multilingual-notes.md`. Do not clone the English file.
- New workflow: it must name the engines it uses, its artifacts, its gate, and its repair loop. A
  workflow that only lists steps is a table of contents, not a procedure.
- New research: add a dossier in the fixed eleven-section format and a row to `docs/research-map.md`.
  Mark clearly what is measured and what is inferred.
