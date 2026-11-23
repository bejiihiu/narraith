# Blind Comparison Protocol

> Purpose: define a run that can answer, honestly and at small scale, whether using the skill changes the text a model writes, and in which direction.
> Read when: you are about to run an evaluation of the skill, or reading a results file and need to know what the numbers can and cannot support.
> Related: `evals.json` — the ten frozen prompts, used verbatim. `rubric.md` — the judging instrument. `../docs/architecture.md` — where this fits among the three verification checks. `../references/literary-critique.md` — the diagnosis behind the twelve axes.

## The question

The question is not "is Narraith good". That question has no design behind it, and any answer would be an advertisement.

The question is: **does the presence of the skill change the text, in which direction, on which axes?** It decomposes into three, and each is answered separately.

1. **Does it change the judged outcome at all?** Per prompt, two texts, one blinded preference. Ten pairs, ten directions.
2. **If it changes, is the change on the axes the skill claims?** A win produced by longer paragraphs or a more literary register is not evidence for the skill's thesis; a win concentrated in narrative coherence, character agency, causal consistency and dialogue quality is.
3. **What does it cost?** A package that improves structure while flattening voice has a real result, and it is a mixed one. The protocol exists to surface the cost, not to net it out.

**What a positive result supports.** On this prompt set, with this model version, under these parameters, blind judges preferred the skill condition more often than not, and the profile moved on the predicted axes. That is a claim about a package, in a setting, at n=10.

**What it does not support.** That the skill improves writing in general, that it transfers across models, that it beats any other skill, or that its output is harder to identify as machine-written. None of these is measured here.

## Design

**Paired runs.** Every prompt is generated twice: once with the skill available, once without. The pair is the unit of analysis, and everything downstream is a comparison inside a pair.

| | Skill condition | Baseline condition |
|---|---|---|
| Prompt | Verbatim from `evals.json` | Identical, byte for byte |
| Added text | One instruction, below | Nothing |
| Context | Fresh session, no history, no memory | Fresh session, no history, no memory |
| Model | Same ID and version | Same ID and version |
| Parameters | Same temperature, top-p, max tokens, stop; same seed if the API supports it | Same |

**The skill instruction, exactly.**

```
The skill at <absolute path to the skill root> applies to this request. Read it and follow it.
```

Nothing else is added. No hint about which files matter, no mention of quality, no mention of this protocol, no per-prompt variation. The instruction is identical across all ten runs, because a per-prompt hint would test the hint.

**Baseline gets the prompt and nothing else.** Do not add "do not use any skill" — that is extra instruction, and it makes the baseline a third condition. Do not add "write normally".

**Fresh context per run.** New session, new container if possible, no shared conversation, no scratch files carried over, no memory of previous runs. A model that has already written the locksmith story will write a different one the second time, and the difference will be attributed to the wrong cause.

**Run order.** Generate pairs in a random or alternating order rather than all baseline runs first. Model behaviour drifts with load and time; blocking by condition converts that drift into a treatment effect.

**The confound, named.** The skill condition carries more instructions, more input tokens, an extra file-reading step, and a much longer effective context. **Any gain measured here is a gain from the package, not from any component of it.** This design cannot tell you whether the eight decisions, the scene gate, the reference files or the sheer volume of instruction did the work. Say that in the results file before anyone else has to.

Record the token counts per run (input and output) and the number of tool calls if the harness reports them. If the skill condition uses an order of magnitude more input tokens, the result is a statement about an expensive package and should be read that way.

**No ablation.** There is no condition that removes one part of the skill. Ablation is the right next study if this one produces a signal, and pretending this design has it would be the standard way to overclaim.

**One sample per condition, per prompt.** Ten pairs, twenty texts. Multiple samples would give within-condition variance and a better estimate; it also multiplies the judging cost by the same factor. If K > 1 is used, say so and pair the samples explicitly rather than pooling them.

## Prompts

The ten prompts are in `evals.json` and are used verbatim. They are deliberately ordinary requests: none names the skill, none asks for a methodology, and none contains the vocabulary the skill would use to answer. Their coverage is stated below so that a null result can be read as "the skill did not help on these" rather than "the skill does not help".

| # | Prompt (gist) | Stresses | Hazard worth noting |
|---|---|---|---|
| 1 | Locksmith opens a vanished woman's flat; one location, no flashbacks, quiet bad ending | Coherence, causal consistency, structural integrity, emotional credibility, agency | The premise is itself a withheld-explanation machine, which flatters any method that withholds |
| 2 | First chapter of a novel, three strands, Russian, 1400–1800 words | Coherence, structural integrity, style consistency, agency | Length and three-strand load make it the hardest single judgement; RU confounds language with craft |
| 3 | Four people in a car at night; nobody says what they want; the fiancée decides | Dialogue quality, character depth, agency, style consistency | Four voices is a natural test of idiolect and a natural way to fail loudly |
| 4 | Divorced couple in a car park; dialogue only; four words banned | Dialogue quality, emotional credibility, originality, character depth | The word ban forces lexical invention; a method can win here by refusing synonyms |
| 5 | Funeral of a man still alive in section two; three time layers, no dates, no headings | Temporal complexity, structural integrity, coherence, continuity | The only strong test of temporal complexity in the set |
| 6 | Chapter 3 from a supplied bible; keep every fact; no new named characters | Continuity, character depth, agency | The only strong test of continuity; the bible caps invention, which may penalise the skill |
| 7 | Revise a purple paragraph; same events, same narrator; explain ≤120 words | Prose quality, style consistency, originality, emotional credibility | The obvious revision is deletion; the test is whether the sensibility survives |
| 8 | Horror in a municipal pool after closing; no gore, no monster, no jump scares | Emotional credibility, causal consistency, prose quality, originality | "Something wrong with the rules" makes internal consistency load-bearing |
| 9 | Russian story: return home for the funeral of a teacher who humiliated him; no catharsis, no klyukva | Prose quality (RU idiom), character depth, emotional credibility, originality | Anti-klyukva is an explicit instruction, so a win may be compliance rather than craft |
| 10 | Narrator lying about the last weekend of his marriage; contradictions recoverable from the text | Character depth, narrative coherence, temporal complexity, continuity, emotional credibility | Deliberate contradiction tests whether judges can distinguish licence from error |

**What the set covers.** All twelve criteria are stressed by at least one prompt. The coverage is uneven, and the unevenness belongs to the prompts, not to the rubric: emotional credibility appears in seven prompts, character depth in five, narrative coherence and character agency and originality in four, prose quality and structural integrity and style consistency and continuity in three, dialogue quality and causal consistency in two, and temporal complexity strongly only in prompt 5, with 10 and 2 as secondary cases. Two consequences follow. A null result on dialogue quality or causal consistency rests on two prompts each, and a positive result on temporal complexity rests on one; both must be reported as thin axes rather than as findings about the skill.

**Prompt-set bias.** The set was written by the people who wrote the skill. It never names the skill, but it selects for the skill's interests: withheld explanations, subtext, single locations, moral complication without resolution. A set drawn from a magazine's slush pile would test different things. This is the largest single threat to external validity here and is restated in § Threats to validity.

## Judging

**Blind, in the strict sense.** Judges see texts and the rubric. They do not see the hypothesis, this file, the skill, the failure criteria, the prompt set's provenance, or which text came from which condition.

**Preparation.**

1. Strip condition labels from filenames and from any preamble the model added. Record what was stripped, and save the raw text alongside.
2. Assign each pair's two texts to `A` and `B` by coin flip, per pair. Record the flips in `key.json`, stored outside the judging folder.
3. Randomise the order in which pairs are judged, and the order of A and B on the page, per judge.
4. Check for vocabulary leakage before judging: search the skill-condition texts for the skill's own terms (ledger, L5, state change, value charge, scene gate) and for planning artifacts. If present, record it as a leakage finding; do not tell the judge, and do not "fix" it by editing the story.

**Procedure per pair.** Read A. Score A on all twelve criteria (`rubric.md`). Read B. Score B. Then, and only then, answer: which would you rather have written, as a piece of fiction in this mode? Record `A`, `B` or `none`, with one sentence.

The preference is overall and separate from the profile. Do not derive it by counting criteria at 4 or above; that is a total in disguise and it defeats the point of scoring a profile.

**Judges.** At least two where possible, scoring independently. A single-judge run is legal and must be labelled as such everywhere the result appears — it has no agreement figure and its profile is one reading.

**Judge briefing.** Ten minutes: read the anchors, score one practice text not from the set, compare with the other judge, discuss only the anchors. Do not discuss any real text before scoring it.

**What judges must not do.** Discuss a text mid-scoring; re-score after seeing the other text of the pair; infer the condition; consult the skill "for context"; or adjust a score to make a pair consistent.

## Analysis

**Unit of analysis: the pair.** Three outputs, reported separately.

1. **Direction.** Per pair: skill better, baseline better, or none. Aggregate as counts — for example, "seven of ten pairs preferred the skill condition, two the baseline, one none". Never as a mean score.
2. **Per-axis delta.** For each criterion, the skill score minus the baseline score, per pair, then a tally of how many pairs moved up, down, or stayed. This is where the *shape* of the change appears: a package can win overall while losing prose quality, and the tally shows it.
3. **Agreement.** Per § Inter-rater reliability in `rubric.md`: simple agreement and within-one-point rate, computed on scored cells only.

**No inference.** n = 10 is a case series. Report counts, directions and the qualitative read. Do not compute p-values, do not call anything significant, do not present an effect size as established, and do not write "the results suggest a trend toward" as a way of smuggling a claim past the design. The honest sentence is: "seven of ten pairs went one way; with ten pairs, a 7–3 split would not be surprising under no effect, and this run cannot distinguish the two." If that sentence feels too weak to publish, the study needs more pairs, not stronger wording.

**The qualitative read.** Pick three pairs — a win, a loss and a tie — and read both texts closely. Write what the skill condition did differently, with quotations: did it withhold, did it add a cost, did it flatten the voice, did it produce a scene that changes state where the baseline produced a summary? This is where the mechanism lives. The numbers only decide whether looking is worthwhile; they never explain anything.

**Handling missing cells.** `NA` scores and unscored criteria are excluded from deltas and agreement, and the exclusion is reported. A pair where both texts failed the word limit is still a pair for preference, but its structural criteria may be `NA` for both.

## What would count as failure

Fixed before the first run. Changing these after seeing results converts a test into a rationalisation.

1. **Fewer than half the pairs won.** Four or fewer of ten preferring the skill condition, with ties counted as not-won. Revision: the package does not improve judged output on this set. Audit the cheapest part first — the eight decisions at Tier B — by removing it and re-running; if that changes nothing, the skill's value is in critique and planning artifacts, and `SKILL.md` should say so instead of implying it improves prose.
2. **Wins on structure, losses on prose.** The skill wins six or more pairs but loses the prose-quality axis in six or more. Revision: the process is over-producing. The likely mechanism is the scene gate and revision pass applied to every draft, which yields cautious, thesis-driven prose. Revision action: tighten adaptive depth so that Tier B does not run the full gate, and add an anti-flattening check to the revision triage.
3. **Judges cannot distinguish the conditions.** Preference splits five/five or the judges report guessing, while agreement on the profile is high — the two conditions produced texts of comparable quality, whatever their differences in kind. Revision: either raise sensitivity (longer texts, sharper anchors, more judges) before drawing any conclusion, or record "no detectable difference on this design". That is a valid and reportable result, and it is different from failure 1.
4. **The win is length.** The skill condition is systematically longer, and the preference tracks length within pairs rather than condition. Revision: the apparent effect is plausibly an artefact. Before any claim, add a length-matched control — an instruction to both conditions to hit the same word count, which changes the design and must be reported as a second study, not as a fix.

Each of these is a result, not a scandal. A run where 1 or 2 fires has told you something specific about which part of the skill to change.

One case sits between them: five wins, four losses and a tie is neither failure 1 nor failure 3. Report it as undetermined, with the per-axis tally, and do not round it toward a verdict by describing it as "a modest advantage". Ten pairs cannot carry a modest advantage.

## Threats to validity

- **Length confound.** Skill outputs are likely longer, and judges reward length. The prompts specify word counts, which caps the confound but does not remove it: a 900-word target lands at 880 in one run and at 1,050 in another, and a judge registers the difference in scope even when both obey the brief. Mitigation: record word counts, report the correlation between winning and being longer, and treat failure condition 4 as live.
- **Judge bias toward the literary register.** The skill trains density, subtext and withheld explanation; judges trained on criticism reward exactly that. Mitigation: judges who have not read the skill, anchors that price plainness explicitly, and at least one judge with editorial rather than academic experience if available.
- **Vocabulary and artefact leakage.** Skill-condition texts may use the skill's terminology or display planning scaffolding, cueing the judge. Mitigation: the pre-judging search, stripping preambles only, and recording every stripping decision.
- **Model specificity.** One model, one version, one decoding regime. A different model may follow the skill more literally, ignore it, or improve without it. No claim survives a version change; record the version.
- **Prompt-set specificity.** Ten prompts written by the skill's authors, selecting for its interests. This is the largest external-validity threat and cannot be mitigated inside this design, only stated.
- **Language pair.** English and Russian only. The Russian prompts confound craft quality with the model's Russian proficiency, which is not measured here. No third language; no claim about transfer.
- **No reader study.** Judges read for defects by instruction. Judged quality is not pleasure, memorability or rereading, and a text that wins here can be a text nobody wants to finish.
- **Single sample per condition.** Within-condition variance is unmeasured, so one unrepresentative generation decides a pair. With K = 1, a 7–3 split is compatible with a coin.
- **Expectancy.** Whoever runs the study knows the hypothesis. Mitigations are procedural: blinded key, randomised order, no contact between the analyst and the judges until scores are filed.

## Reproduction

**Shape.** 10 prompts × 2 conditions × K samples = generation calls (20 at K = 1). Judging: 20 texts × 2 judges at K = 1.

**Directory layout.** One folder per run, nothing edited after the fact.

```
tests/results/<YYYY-MM-DD>-<model-slug>/
  meta.json            model id and version, params, date, skill commit, K, token counts per run
  prompts.json         frozen copy of evals.json used for this run (hash it in meta.json)
  runs/
    p01-skill.md       raw output, exactly as generated
    p01-base.md
    ...
  key.json             condition mapping and per-pair coin flips (never given to judges)
  judging/
    <judge>/p01-A.md   scores in the rubric.md reporting format
    <judge>/p01-B.md
    ...
  analysis.md          the results file, per § Reporting
```

**Rules.** Never edit a generated text; if a preamble was stripped for judging, keep both `p01-skill.md` (raw) and the stripped copy. Record the skill commit hash in `meta.json`, because "the skill" changes. Record the harness and whether tool use was enabled; a run where the model could not read files is a different experiment.

## Reporting

A results file is incomplete without its failures. The block below is the shape of the *results* file, not of this one.

```
# <model> — <date>

## Setup
Model and version, parameters, K, skill commit, judge count and background, prompt-set hash.

## Headline
Counts, not adjectives. Pairs won / lost / tied. Which pre-registered failure conditions fired.

## Per-prompt table
| Pair | Preference | Axes that moved up | Axes that moved down | Word counts |

## Axes
Per-criterion tally across pairs. Which axes moved, in which direction, and on how many pairs.
Note the thin axes (style consistency, temporal complexity) and which prompts carried them.

## Agreement
Simple agreement, within-one-point rate, and the criteria that disagreed, with reasons.
Single-judge runs say so here and omit the figures.

## Qualitative findings
Three pairs (win, loss, tie), quoted. What the skill condition did differently, and the mechanism.

## Failures and what was done
Every pre-registered condition that fired, and the revision it implies. If none fired, say which
were checked. A run that reports no failures anywhere is a run that has not looked.

## What this does not show
Restate the limits in the run's own terms: n, one model, this prompt set, two languages, no readers.
```

Two prohibitions, both about honesty rather than format. Do not report a mean score across criteria, in the results file or in any summary of it; the rubric forbids totals and a mean reintroduces one. Do not report a result from a run whose judging was not blind, or whose key was accessible to a judge — such a run may be described as a pilot, in a sentence, and nothing more.
