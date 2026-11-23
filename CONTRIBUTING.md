# Contributing to Narraith

Narraith is a skill, not a framework: its substance is the quality of its instructions. A change is
worth making if it changes what a model *does*, not if it adds words.

## Before you write

Read `SKILL.md` and `docs/architecture.md`. The architecture explains why modules are split the way
they are; a patch that violates the split will be asked to move, not merged as-is.

## What belongs here

- A mechanism that is executable by a model in one pass, with a stated failure condition.
- Research findings with a traceable source and an explicit boundary between what was measured and
  what is inferred.
- Worked examples that are original and short enough to be read in one sitting.
- Corrections: an instruction that produced worse output, with the evidence.

## What does not

- Word or punctuation blacklists. Judgement is contextual; bans are not.
- Unattributed statistics, invented citations, or "studies show".
- Beat sheets and trope lists presented as rules.
- Restatements of material already in another file. Link instead.
- Planning documents longer than the work they plan.

## Epistemic markers

Every non-obvious claim carries one of three markers:

- `[data: <Paper>]` — measured in the cited study. The number must appear in the dossier in
  `references/research/`.
- `[theory]` — narratology or craft consensus, not an experimental result.
- `[hypothesis]` — our own rule, not established. Must come with a way it could fail.

A file may declare a default marker in its preamble ("everything here is `[theory]` except…"), in which
case individual claims carry a marker only where they deviate from the default. A claim that has neither
a marker nor a declared default is treated as an error. Do not use a detector's F1 as evidence that prose
is good; do not describe a heuristic as a measurement.

## File format

Every reference and methodology file starts with:

```markdown
# Title
> Purpose: one line.
> Read when: one line.
> Related: `path` — why.
```

Then a table of contents if the file exceeds 300 lines. Engines follow a fixed eight-part format —
purpose; when to use and when not; inputs; procedure; criteria for failure; typical errors; output
format; micro-example. `docs/architecture.md` §10 explains how to register a new one. Do not invent a
different format; the consistency is what makes the engines composable.

## Validation

```bash
python scripts/validate_skill.py .
python -m py_compile scripts/*.py
```

The validator checks frontmatter, relative links, placeholders, empty files, fence balance, and file
size. CI runs it on every push. A broken link is a failed build, not a warning.

If your change affects the claims in `docs/research-map.md`, update the map in the same commit.

## Pull requests

- One concern per PR. A new engine and a typo sweep do not belong together.
- Say what changed in model behaviour, and how you know. If you ran the eval prompts, include the
  outputs or the comparison.
- Do not reformat unrelated files. Diffs are read.
- Commit messages: conventional commits, imperative, under 72 characters in the subject.

## Language

The skill is written in English so that it reads consistently regardless of the user's language.
Russian and other languages appear as *subject matter* — examples, terminology, and craft notes — not
as a second instruction language. `README.ru.md` is the exception.

Spelling is British (`-ise`, `-our`, `behaviour`, `labelled`), except in verbatim quotations and in the
US/UK comparison table in `references/english-prose.md`. Prose examples use double quotation marks; the
English craft file describes both conventions and does not prescribe one for this repository.

## Reporting problems

Open an issue with: the prompt, the output, what the skill instructed, and what went wrong. "It felt
generic" is not actionable; "the scene gate passed a scene with no state change because the model
counted an emotional shift as a change" is.
