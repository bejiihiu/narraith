# Changelog

All notable changes to this skill. Format loosely follows Keep a Changelog; versions follow semver
where the "API" is the instruction surface a model reads.

## [1.1.0] — 2026-11-24

### Added

- `references/detector-feedback.md` — how to use a machine-text detector's report without obeying it:
  the case file, the four statistical suspects, the repair filter, and the boundary between a flagged
  text and a bad one.
- `scripts/story_metrics.py` — pronoun-initial share, paragraphs opening on a pronoun, one-sentence
  paragraph share, paragraph-length spread, and the most common sentence openers.
- `references/russian-prose.md` — "the subject-initial run": repeated paragraph openings as the
  commonest rhythmic tell in Russian model prose, with repairs that do not change the content.
- `[report: <vendor>, <date>]` as a fourth claim marker, for third-party measurements of one text.

### Changed

- `SKILL.md` — routing row for a detector verdict, and a prohibition on optimising for a classifier.

### Evidence

A Russian story written under 1.0.0 was flagged by Textovod as machine-generated: 57% explicit signs,
43% suspicious. Its metrics showed the cause the skill's own Russian checks already name — no sentence
over 35 words, 22% of paragraphs opening on a pronoun. Recorded in
`tests/results/detector-2026-11-23.md`.

## [1.0.0] — 2026-11-23

Initial release.

### Added

- `SKILL.md` — doctrine, seven-level vocabulary, eight decisions, scene gate, revision triage,
  adaptive depth tiers, routing table.
- `references/` — five research dossiers with methodology, results and limits; a synthesis with the
  Research → Capability map; narratology as decision vocabulary; an evidence-based catalogue of model
  defaults; seven-level depth with a misattribution table; architecture, genre, character, prose,
  Russian, English, temporal, originality, critique, editorial, continuity and multilingual modules.
- `methodologies/` — fifteen engines in a fixed eight-part format, with an index and combination notes.
- `workflows/` — fourteen task routes across short form, long form, scene and ensemble, continuation
  and revision, voice and complex structure.
- `examples/` — ten worked examples: weak/strong pairs and three-channel calibrations, in English with
  a Russian variant.
- `templates/` — decision ledger, character and world bibles, timeline, scene card, revision plan,
  voice contract, continuity ledger.
- `checklists/` — pre-draft, scene, dialogue, continuity, final, Russian, English.
- `tests/` — ten eval prompts, a twelve-criterion rubric, a blind comparison protocol, recorded results.
- `scripts/` — structure validator and surface-proxy metrics.
- CI workflow validating structure and links on every push.

### Known limitations

See `docs/limitations.md`. The central one: the transfer from detection research to generation craft
is an engineering hypothesis, not a measured result, and the evaluation is a small blinded study, not
a benchmark.
