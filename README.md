# Narraith

**A narrative decision system for language models that write fiction.**

Most writing advice tells a model what good prose looks like. Narraith makes it decide what the story
is doing — who wants what, what it costs, what the reader knows and when, why this order and not
another — and then write prose that serves those decisions.

It is a skill: a set of instructions and reference modules that a model loads when asked to write,
continue, critique or revise fiction. It is designed to work with any capable model and needs no tools, no API
access, and no fine-tuning.

---

## The problem it targets

A model asked for a story produces competent prose that fails in a consistent way: it explains what
should be inferred, resolves what should stay open, keeps one causal track, and withholds the concrete
detail that would have let the reader infer anything at all.

StoryScope (Russell et al., COLM 2026) measured this across 61,608 stories. AI narrators state the
theme in 77% of stories against 52% for humans; resolve through internal acceptance in 47% against
27%; render emotion through the body in 81% against 38%, while naming it directly in only 8% against
29%. The classifier built on these narrative features separates human from AI fiction at 93.2%
macro-F1 across the corpus. On a 278-story Gemini subset, span-level rewriting moved detection from
95.5% to 93.9% — a 1.6-point drop. Better sentences do not fix it. Different decisions might.

Narraith is built on that distinction. It is an engineering bet, not a proven result: the papers
measure detection, not improvement. The skill is designed so the bet can fail visibly, and the
limitations are documented rather than smoothed over.

## What it does

- **Plans**: premise pressure, dramatic question, causal spine, information plan, subplot
  intersections, ending mode — with a Decision Ledger that stays short enough to be used.
- **Writes**: scene construction, dialogue with subtext, prose rhythm, point of view, description,
  voice — calibrated by scene function rather than by bans.
- **Complicates**: moral ambiguity from competing goods, unreliable narration with recoverable
  evidence, non-linear order that does argumentative work, multiple timelines that stay orientable.
- **Diagnoses**: twelve critical axes, differential diagnosis of "this scene feels flat", severity by
  leverage rather than by ease.
- **Revises**: developmental → structural → line → copy, in that order, with a regression check.
- **Continues**: continuity ledgers, voice-contract inference, and a rule against resolving what the
  original left open.
- **Writes in Russian and English**: separate craft layers, because a translated rulebook produces
  translationese.

## How it is built

Progressive disclosure, five layers:

```
SKILL.md            doctrine, seven levels, scene gate, revision triage, routing   (always loaded)
references/         why and what: research, narratology, craft, language, genre    (read by need)
methodologies/      15 engines: how to make a specific decision well                (read by need)
workflows/          14 routes: what order, for this kind of request                (read by need)
templates/          copyable artifacts: ledgers, bibles, scene cards               (used in work)
checklists/         gates inside the writing process                               (used in work)
```

The always-loaded file is self-sufficient for a scene. Depth is retrieved by task, never preloaded.

## Install

With the skills CLI:

```bash
npx skills add <owner>/narraith -g -y
```

Manually — copy the repository into your skills directory:

```bash
git clone https://github.com/<owner>/narraith.git
cp -r narraith ~/.agents/skills/narraith        # or ~/.claude/skills/narraith
```

Then ask for fiction. The skill triggers on writing, continuing, critiquing and revising prose, in
English or Russian. You do not need to name it.

## Use

Ordinary requests work:

> Write a 900-word story about a locksmith called to open the flat of a woman who vanished three weeks
> ago. One location, no flashbacks, no explanation. End badly but quietly.

The skill will make the decisions, write, and run the scene gate — without showing you a planning
document. If you want the decisions visible:

> Before you write, give me the dramatic question, the causal spine, and what the protagonist loses
> either way.

For revision:

> Diagnose this chapter. Two structural problems maximum, with evidence. Don't rewrite it yet.

## What it is not

- Not a style guide. It contains no banned words. A long dash, an adverb, a simile, the word
  "suddenly" — each is a tool with conditions.
- Not a beat sheet. Structure is taught as a pressure curve and a set of decisions, not page counts.
- Not a detector. It offers a qualitative self-audit against documented defaults and refuses to
  score, classify, or claim measurement.
- Not a generator of twists. Originality is default-avoidance under a plausibility budget, not
  randomness.
- Not a replacement for the author's voice. Voice contracts exist to protect it, not to overwrite it.

## Research basis

Five studies, used for what they measured and nothing more:

| # | Study | What Narraith takes |
|---|---|---|
| 1 | [StoryScope](https://arxiv.org/pdf/2604.03136) — Russell et al., COLM 2026 | The catalogue of narrative defaults; the seven-level emphasis on decisions; the diversity argument |
| 2 | [Ghostbuster](https://aclanthology.org/2024.naacl-long.95.pdf) — Verma et al., NAACL 2024 | Multi-signal diagnosis, minimal explanatory sets, honest treatment of robustness |
| 3 | [DetectGPT](https://arxiv.org/pdf/2301.11305) — Mitchell et al., 2023 | Fluency ≠ predictability; the alternative-continuation test |
| 4 | [DNA-GPT](https://arxiv.org/abs/2305.17359) — Yang et al., 2023 | The regeneration test for predictable narrative choices |
| 5 | [Every Model Leaves a Trace](https://arxiv.org/pdf/2610.28434) — Modarres et al., 2026 | Signal durability hierarchy; why not to build a quality model on surface tells |

Full records, methodology, results, limitations and the Research → Capability map:
[`references/research-foundations.md`](references/research-foundations.md). Every claim in the skill
is tagged `[data: Paper]`, `[theory]` or `[hypothesis]`.

## Evaluation

Ten prompts are defined, covering short stories, multi-thread chapters, four-hand scenes, subtext-only
dialogue, non-linear structure, continuity-constrained continuation, purple-prose revision, genre dread,
Russian prose and unreliable narration. Iteration 1 ran six of them, with and without the skill, under
identical conditions, and had the pairs judged blind by two independent judges against a twelve-criterion
rubric.

Results and the honest reading of them: [`tests/results/iteration-1.md`](tests/results/iteration-1.md) —
nine of twelve judge decisions favoured the skill condition, the one clear loss was a continuity
contradiction, and the measurable movement was in voice/subtext/originality rather than in structure, which
is not what the doctrine predicts.
Protocol: [`tests/protocol.md`](tests/protocol.md). This is a small blinded study, not a benchmark.

Surface proxies (sentence distribution, lexical diversity, dialogue share, emotional-channel ratio,
repetition) can be computed with `python scripts/story_metrics.py draft.md`. They are proxies, and
the script says so.

## Repository map

```
SKILL.md
references/     research dossiers, narratology, craft, language layers
methodologies/  fifteen engines with procedures and failure lists
workflows/      fourteen task routes
examples/       ten worked examples: weak/strong pairs and channel calibration
templates/      decision ledger, bibles, timeline, scene card, revision plan
checklists/     pre-draft, scene, dialogue, continuity, final, RU, EN
tests/          evals, rubric, protocol, results
docs/           architecture, research map, design decisions, limitations
scripts/        validator, surface metrics
```

## Development

```bash
python scripts/validate_skill.py .
python -m py_compile scripts/*.py
```

CI runs both on every push. See [CONTRIBUTING.md](CONTRIBUTING.md). Epistemic markers are mandatory:
unmarked claims are treated as errors.

## License

MIT. The research is cited, not reproduced; the prose examples are original to this repository.
