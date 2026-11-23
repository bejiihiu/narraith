# Limitations

> Purpose: state what this skill is not entitled to claim, and under what conditions its central bet fails.
> Read when: citing the skill, evaluating it, extending it, or deciding whether to trust a rule.
> Related: `docs/research-map.md`, `references/research-foundations.md`, `tests/protocol.md`.

## 1. The central epistemic problem

Narraith is built on five studies of **detection and attribution**. None of them tests whether teaching a
model narrative decisions improves the fiction it writes. The step from "AI stories differ from human
stories in these measured ways" to "a skill that pushes away from those ways produces better stories"
is ours, and it is unproven.

There are three independent gaps in that step:

1. **Description ≠ prescription.** A population difference is not a quality difference. 57% of the human
   stories in StoryScope have no subplot; a subplot is therefore not a requirement. "Human-leaning" means
   "rarer in this corpus", not "better".
2. **Detection ≠ evaluation.** A classifier's macro-F1 says how separable two distributions are. It says
   nothing about which text a reader would prefer, remember, or reread.
3. **Avoidance ≠ achievement.** A text that avoids the measured defaults is not automatically good. It can
   be contrived, obscure, or merely different — the same failure with a new signature.

Everything below follows from taking those gaps seriously.

## 2. Load-bearing hypotheses

Each is stated so it can fail. If a hypothesis fails, the modules that depend on it need revision, not
defence.

| # | Hypothesis | Fails if | Modules at risk |
|---|---|---|---|
| H1 | Forcing explicit narrative decisions before drafting changes the text measurably, and mostly for the better | Paired blind evaluation shows no preference for the skill condition, or preference only on structure with consistent loss on prose | `SKILL.md`, all of `methodologies/` |
| H2 | The seven-level grid improves diagnostic accuracy over free-form critique | Two judges using the grid agree no better than two judges writing prose critiques, and repairs miss the actual defect | `references/quality-levels.md`, `references/literary-critique.md` |
| H3 | The continuation/regeneration test surfaces predictable choices that the model would not otherwise notice | Models run the test and choose the same modal option anyway, or the test produces contrivance | E11, `references/originality.md` |
| H4 | Continuity ledgers reduce contradiction in long-form work | Contradiction rates are unchanged, or ledger upkeep consumes attention disproportionate to the gain | `references/continuity-memory.md`, `templates/` |
| H5 | Calibrating the emotional channel by scene function beats both "show don't tell" and "name the feeling" | Calibrated passages are judged no better, or judges prefer the uncalibrated baseline | `references/prose-engineering.md`, `examples/07` |
| H6 | Adaptive depth prevents over-processing without causing under-structuring | Tier B outputs show either planning theatre or missing structure at similar rates | `SKILL.md` §adaptive depth, `workflows/` |
| H7 | An English instruction surface with a Russian craft layer produces Russian prose without translationese | Russian judges identify the Russian outputs as translated, or the Russian module's rules prove inapplicable | `references/russian-prose.md`, `references/multilingual-notes.md` |

The evaluation in `tests/results/` is a case series of six prompts drawn from the ten defined in `tests/evals.json`. It can support H1 weakly and the
others not at all. No hypothesis here has been tested at a scale that would justify a general claim.

## 3. Coverage limits

**Language.** English and Russian. The five papers cover English; the fingerprinting paper adds Chinese
and Persian, with translated rather than natively authored prompts. Nothing in the corpus supports claims
about Russian, and the Russian module is craft knowledge, not measurement. A third language requires its
own craft file; translating the English one is exactly the failure the skill warns about.

**Form.** Short stories are the measured form. Novels, series, screenplays, interactive fiction and
serialised web fiction are covered by inference from craft literature. The continuity and long-form
modules are the least evidenced part of the skill.

**Tradition.** The narratology is European and Anglo-American: Russian formalism, French structuralism,
the Anglo-American workshop. It is not a universal account of storytelling. Story structures from other
traditions — episodic, frame-nested, oral-formulaic, non-teleological — are not well served by a model
built on dramatic question and causal spine. The skill says so where it can, but the centre of gravity is
visible.

**Genre.** Genre contracts are principles, not market knowledge. The skill cannot tell you what a
particular imprint is buying this year.

## 4. Measurement limits

The skill has no access to log probabilities, model internals, or training data. It cannot compute
probability curvature, divergence scores, perplexity, or authorship. Whenever the skill uses those ideas
(it does, in E11), it uses them as **procedures of attention**, not measurements.

`scripts/story_metrics.py` computes surface proxies: sentence length distribution, MATTR, dialogue share,
emotion-word density, repeated n-grams. These are fragile in both directions. A great paragraph can score
badly; a bad one can score well. The script is for before/after comparison and regression detection, and
it says so in its own docstring.

The rubric in `tests/rubric.md` is a judgement instrument, not a measurement. It measures the properties
the skill claims to improve, which makes it useful for the skill's own evaluation and unsuitable as a
general theory of literary quality.

## 5. Failure modes of the skill itself

These are observed risks of instruction-heavy craft systems, and the mitigations are in the text:

- **Checklist theatre.** A scene that satisfies goal, conflict, turn, cost, value charge and one
  defamiliarised object, all inert. Mitigation: the engines are diagnostic-first, and `SKILL.md` says a
  story needs three or four engines, not fifteen.
- **Inverted snobbery.** "AI is tidy, so I will be messy." Produces arbitrary structures. Mitigation: the
  plausibility budget and the refusal to treat any human-leaning statistic as a prescription.
- **Pastiche of the method.** Outputs that read like a writing workshop rather than a story: symmetrical
  scenes, visible turns, a thesis-shaped ending. Mitigation: Tier A exists, and the "do not perform the
  method" rule.
- **Over-correction on emotion.** Removing somatic rendering produces talking heads. Mitigation: three
  channels, chosen by function.
- **Ledger abandonment.** A bible that is filled once and never read. Mitigation: the admission rule —
  track only what the plot has made load-bearing.
- **Voice laundering.** A revision that removes the author's oddness along with their errors. Mitigation:
  the preserve list in W10, and the rule that a bad habit can be a voice.

## 6. Ethical and legal limits

- **Imitation of living authors.** W12 permits style matching only on request and only as an exercise. The
  skill instructs that imitation must not be presented as original work. It cannot enforce this.
- **Cultural specificity.** Writing a setting you do not know produces a setting assembled from other
  texts. The skill's concreteness rules make this *more* visible, not less; they do not substitute for
  knowledge.
- **Sensitive material.** The skill offers craft procedure for violence, grief, and moral horror. It does
  not offer content policy. Harness-level policy applies and overrides anything here.
- **Copyright.** The examples are original to this repository. The research is cited, not reproduced. The
  Books3 corpus used by StoryScope is not redistributed; only aggregate findings appear here.

## 7. What would change our mind

- A paired evaluation at scale (100+ prompts, multiple models, multiple judges) showing no consistent
  preference for the skill condition.
- Evidence that narrative-level interventions are *less* durable than the StoryScope authors argue — for
  example, a model generation that closes the measured gap without being taught to.
- Evidence that explicit decision artifacts *reduce* quality by displacing attention from the page.
- A replication showing that the emotional-channel calibration produces worse reader response than either
  of the extremes it replaces.
- A demonstration that the continuity system's cost exceeds its benefit in realistic long-form work.

None of these has been tested. They are the experiments this skill is waiting for.
