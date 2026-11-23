# Iteration 1 — paired blind evaluation

> Purpose: record what happened when six prompts were run with and without the skill, and state what the result does and does not support.
> Read when: evaluating the skill's claims, reproducing the run, or deciding whether a module needs revision.
> Related: `../protocol.md` — the design; `../rubric.md` — the axes; `judging/key.json` — condition assignment.

**Date:** 2026-11-24 · **Model:** `lunaroute/deepseek-4.1-flash` · **Runs:** 12 (six prompts × two
conditions) · **Judges:** 2 independent, blind to condition · **Language:** four English prompts, two Russian.

This is a case series. Six pairs cannot establish an effect size, and no p-value is reported. What it can
do is show whether the skill changes the text at all, in which direction, and where it fails.

## What was run

Six of the ten prompts in `../evals.json`, chosen to cover the skill's main claims:

| # | Stress | Target length | Words with | Words without |
|---|---|---|---|---|
| 1 | single-location short story, withheld explanation | ~900 | 871 | 1,101 |
| 2 | three-strand chapter in Russian, convergence unstated | 1,400–1,800 | 908 | 1,378 |
| 4 | four-hand scene, subtext, decision readable only to the reader | under 600 | 435 | 475 |
| 6 | continuation under a fixed bible, no new named characters | 1,200–1,600 | 1,206 | 1,534 |
| 7 | revision of purple prose, same events and POV | passage + 120-word note | 246 | 233 |
| 9 | Russian return-to-hometown story, no catharsis | 1,000–1,300 | 1,075 | 1,015 |

Fresh context per run, identical prompt, no shared conversation. The skill condition was told to read
`SKILL.md` and follow the modules it routes to; the baseline was told nothing beyond the task. Any gain is
therefore a gain from the skill **as a package**, including the extra instruction tokens.

## Result

Judge decisions after decoding the key: **9 for the skill condition, 3 for the baseline**. The two judges
agreed on five of six pairs. At pair level: four pairs to the skill, one to the baseline, one split.

| Pair | Skill | Baseline | Verdict | Why, in the judges' words |
|---|---|---|---|---|
| 1 | 2 | 0 | skill | "A keeps the whole ending inside the room it opened — the washed cup and 'Mind how you go' carry the badness without naming it." |
| 2 | 1 | 1 | split | One judge preferred the skill's convergence through a repeated act; the other preferred the baseline's fuller development of all three strands. |
| 4 | 2 | 0 | skill | "A never leaves the car park and lets a hedge and an unclaimed fence do all the saying." |
| 6 | 0 | 2 | baseline | "B's eleven-year backdating strains the bible and its own rule that the book holds only refusals." |
| 7 | 2 | 0 | skill | "B fixes the passage's actual failure — the abstract closing certainty — by replacing it with a concrete fact." |
| 9 | 2 | 0 | skill | "A dramatises the humiliation and then refuses both the compliment and the catharsis." |

### Axis scores

Mean of both judges, six pairs, 1–5 anchored rubric. Not a total, not a grade.

| Axis | With skill | Without | Delta |
|---|---|---|---|
| narrative coherence | 4.33 | 4.25 | +0.08 |
| character (depth + agency) | 4.08 | 4.00 | +0.08 |
| prose | 4.75 | 4.33 | +0.42 |
| emotional credibility | 4.50 | 3.83 | +0.67 |
| originality | 4.42 | 3.67 | +0.75 |
| structural integrity | 4.00 | 3.92 | +0.08 |

The shape of that table is the most useful result here, and it is not the one the skill predicts. The
skill's doctrine puts narrative structure first. In this round the measurable movement is at **L3/L4** —
voice, subtext, emotional channel, the choice of what to leave unstated — while **structural integrity,
coherence and character barely move**. Two readings are possible and this run cannot separate them: either
the skill's structural advice does not transfer into a 900-word draft, or the six prompts are mostly
tone-and-subtext problems where structure had little room to differ. The structural pair (6) was the one
loss, which is weak evidence for the second reading.

### Surface proxies

From `scripts/story_metrics.py`, averaged across the six runs per condition. Proxies, not quality.

| Metric | With | Without |
|---|---|---|
| words | 890 | 992 |
| mean sentence (words) | 13.96 | 14.30 |
| share of sentences over 35 words | 3.6% | 7.0% |
| MATTR-50 | 0.79 | 0.81 |
| dialogue share | 0.19 | 0.25 |
| somatic terms per 1,000 | 0.31 | 0.83 |
| repeated 4-grams | 4.7 | 3.5 |

The skill condition is shorter, avoids long sentences, and uses far less somatic rendering — consistent
with the channel-calibration and over-determination material. It also repeats more four-grams and has a
slightly lower lexical variety, which can be motif work or can be thinness; the proxy cannot tell, and the
judges did not penalise it.

## Failures found in this round

1. **The skill under-wrote a stated length.** Prompt 2 asked for 1,400–1,800 words; the skill condition
   produced 908. One judge still preferred it, which makes this worse rather than better: a text can win a
   craft comparison and still fail the brief. `workflows/01-short-form.md` now treats an under-run over
   15% as a missing movement, not tight writing.
2. **A continuity contradiction in the strongest-looking output.** In pair 6 the skill condition gave the
   ninth of October a full ledger entry, although the bible says the ledger records only refused ships.
   Both judges caught it. The module was not at fault — the model invented — but it shows that a voice as
   confident as the one the skill produces can carry an unchecked fact past a reader.
3. **A possible plainness bias.** One judge flagged that five of six preferences went to the sparser text
   and re-tested the pairs for it. The two judges still disagreed only once, so the effect was not strong
   enough to reverse a verdict, but it is a live confound for any future round.
4. **Brief compliance is not scored by the rubric.** Prompt 1's baseline was 1,101 words against "around
   900" and still scored well on craft. Compliance needs its own reported line, outside the twelve axes.

## What this supports

- The skill changes the text in a direction the rubric can see, on prose, emotional credibility and
  originality, in both English and Russian.
- The scene gate and dialogue material are usable within a single generation; they do not require a
  planning phase to show up in the output.
- Two independent judges converged on five of six pairs, so the preferences are not noise.

## What this does not support

- Any claim that the skill improves **structure**. It did not, measurably, in this round.
- Any general claim about models. One model, one version, one decoding regime, six prompts.
- Any claim about readers. The judges are language models, from the same family as the writers; a reader
  study is the missing instrument.
- Hypothesis H2–H7 in `docs/limitations.md`. Only H1 is touched, weakly.

## Reproduction

```bash
# runs: tests/results/raw/eval-<id>/{with,without}/output.md
python scripts/make_blind_pairs.py --seed 11
# judging: tests/results/judging/pair-*/{prompt,A,B}.md  (key.json withheld from judges)
python scripts/analyse_results.py
```

The seed is fixed, so the A/B assignment can be regenerated. Judge prompts and the verbatim judgments are
in `judging/judge-1.json` and `judge-2.json`.

## Next round

- Run all ten prompts, with a third judge and a reader panel.
- Pre-register the plainness-bias test: swap in a deliberately dense text and check whether judges still
  prefer the sparser one.
- Score brief compliance as a separate reported line.
- Add a structural prompt where the failure is unambiguous (a missing cost, an unearned turn) to test
  whether the L5 machinery can move the axis it was built for.
