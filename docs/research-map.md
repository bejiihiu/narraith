# Research Map: Claim and Figure Audit

> Purpose: a maintainer's audit of every load-bearing claim and every number in the skill — what it rests on, whether the file says so, and where the files currently disagree.
> Read when: editing a file that quotes a figure, reviewing a research claim, or deciding whether a rule is evidence or craft.
> Links: `references/research-foundations.md` — the synthesis this audits; `references/research/01-storyscope.md` … `05-fingerprinting.md` — the primary records; `docs/limitations.md` — the hypotheses the design depends on.

Method: every `.md` file outside `notes/` was searched for percentage pairs, decimal figures, `[data: …]` markers, and prescriptive sentences with no marker. Rows below are a representative audit, not an exhaustive concordance; the numbers register is complete for the figures the skill actually uses.

Severity is not recorded per row because most defects are cheap to fix and expensive to leave: a wrong denominator produces a wrong rule downstream, and a missing tag produces a confident sentence with nothing behind it.

## Contents

1. [Purpose](#purpose)
2. [Claim audit table](#claim-audit-table)
3. [Numbers register](#numbers-register)
4. [Known inconsistencies](#known-inconsistencies)
5. [How to add a claim](#how-to-add-a-claim)

## Purpose

This file exists because the skill quotes research in twenty-odd files and no single one of them can see the others. Three failure modes recur:

- **Denominator drift.** A figure measured on a 278-story subset is compared with a figure measured on the full corpus, and the comparison reads as a trend.
- **Tag drift.** A measured result appears in a file that usually marks theory, or a craft rule appears in a file that usually marks data, and neither carries a marker.
- **Promise drift.** A dossier's capability map says a mechanism lives in a file; the file does not contain it, or contains a different version of it.

None of these is a factual error in the paper. All of them are errors in the skill's use of the paper, which is the thing this repository is responsible for.

This is not a second synthesis. `references/research-foundations.md` explains what the papers found and what the skill does with it; this file records whether the skill's files actually say that. Where the two disagree, the synthesis is the intended state and this file is the evidence that the repository has not reached it yet.

## Claim audit table

Status: **measured** (a result in a paper), **inferred** (our transfer of a result), **theory** (craft or narratology), **hypothesis** (our untested bet). "Unmarked" means the file states the claim without a marker.

| Claim | File | Source | Status | Confidence note |
|---|---|---|---|---|
| "A scene changes a state" | `SKILL.md` law 2 | craft (McKee-derived) | theory | Load-bearing and unmarked. "State" is never defined at that altitude; the four kinds appear only in the scene gate. |
| "Enter as late as possible, leave as early as possible" | `SKILL.md` scene gate | workshop convention | theory | Unmarked. The correction — do not cut before the consequence — appears only in `references/story-architecture.md` §6. |
| "Fifteen engines exist; a story needs three or four" | `SKILL.md` | design judgement | hypothesis | Unmarked. No test; the number is a budget heuristic. |
| Narrative features separate human from AI at 93.2% | `SKILL.md`, `README.md` | StoryScope §4.1 | measured | Binary macro-F1, narrative-only (257 features), prompt-matched test set. |
| "still at 93.9% after span-level stylistic rewriting" | `README.md` | StoryScope §4.2 | measured | 278 Gemini stories whose pre-edit score was 95.5. See inconsistency 1. |
| "79% of model-written stories carry no subplot" | `methodologies/01-plot-and-causality.md` | StoryScope §4.1 | measured | Human baseline (57%) omitted here; see inconsistency 4. |
| Protagonist-driven resolution 69% vs 46% | `methodologies/02-character-and-dialogue.md`, `references/character-intelligence.md` | StoryScope §4.1 | measured | Categorical, one dimension; AI-first order, labelled in prose. |
| Internal-acceptance endings 47% vs 27% | `references/story-architecture.md`, `examples/10` | StoryScope §4.1 | measured | Prevalence contrast, not a verdict on the mode; 27% of human stories do it. |
| Embodied emotion 81% vs 38% | `references/prose-engineering.md`, `methodologies/03-time-and-scene.md`, `examples/07` | StoryScope §4.1 | measured | AI-first. Human rate is 38%, so the body is legitimate at a lower base rate. |
| Explicit labels 8% vs 29% | same files | StoryScope §4.1 | measured | AI-first. Used correctly as a prior, not a quota, in `examples/07`. |
| Named reference 24% vs 47% | `references/ai-narrative-signature.md`, `references/narrative-theory.md` | StoryScope §4.1 | measured | AI-first; the prescription ("name it and make it work") is `[theory]`. |
| Rarity percentile 0.71 vs 0.49; 24.7% vs 7.1% | `references/originality.md` | StoryScope §4 | measured | Human-first there, AI-first in the signature file; both label the direction. |
| Behavioural attribution 52.42 → 25.59 | `docs/architecture.md` | Fingerprinting §4 | measured | 8-way, chance 12.5; T0 → T3. Architecture calls it "formatting accuracy". See inconsistency 3. |
| Stylometric attribution 19.74 cross-lingual | `docs/architecture.md`, `references/multilingual-notes.md` | Fingerprinting §5.3 | measured | Averaged over six directions at T0; prompts were machine translations. |
| "≈22–27% at fifty words" | `references/literary-critique.md` | Fingerprinting §4 | measured | P2* condition (paraphrased and scrubbed) only. See inconsistency 5. |
| Ghostbuster 99.0 in-domain, 97.0 out-of-domain | `references/research/02-ghostbuster.md` | Ghostbuster §6 | measured | 2023-era data; in-domain baseline comparison is unfair by the authors' own account. |
| DetectGPT 0.81 → 0.95 AUROC | `references/research/03-detectgpt.md` | DetectGPT §5 | measured | GPT-NeoX on XSum, 150–500 examples, equal positive/negative. |
| DNA-GPT 99.09 → 98.48 AUROC | `references/research/04-dna-gpt.md` | DNA-GPT §5 | measured | 100 Reddit instances, 50% of tail replaced by T5. |
| "Emotion should be channelled by scene function" | `SKILL.md`, `references/prose-engineering.md` | inference from 81/8 | hypothesis | Marked in the prose file, unmarked in `SKILL.md`. Our rule, not a finding. |
| "A 200-word sample cannot support a voice claim" | `references/literary-critique.md` | inference from length curve | hypothesis | Marked there. The 600–800-word budget is engineering judgement. |
| "A subplot must cross the spine twice" | `references/story-architecture.md` §7, W14 | craft + 79/57 | hypothesis | Unmarked as hypothesis: the statistic supports the gap, not the two-intersection rule. |
| "The obvious choice is the draft choice" | `SKILL.md` law 5 | DetectGPT/DNA-GPT analogy | hypothesis | Unmarked. The papers measure distributions, not individual decisions. |
| "Human-leaning is the less default choice" | `references/ai-narrative-signature.md` | inference from StoryScope | hypothesis | Stated as a prior in the same file; elsewhere in the repo it can read as a target. |
| "The durability order maps onto L1–L7" | `docs/architecture.md` §4 | Fingerprinting + design | inferred | No file states the mapping explicitly; the dossier promises it in `quality-levels.md`. See inconsistency 6. |
| "A fixed-form sample cannot support a voice claim" | `references/literary-critique.md` | Fingerprinting constrained-task result | inferred | 35.94% attribution on rewrite tasks; the craft transfer is ours. |
| "Continuity ledgers reduce contradiction" | `docs/limitations.md` H4 | craft | hypothesis | Explicitly untested; the only honest status in the file. |
| "Russian prose distributes information by word order and aspect" | `SKILL.md`, `references/russian-prose.md` | Slavistics | theory | No paper in the corpus covers Russian. |
| "Twelve critical axes" | `README.md`, `references/literary-critique.md` | design | theory | The count is a design choice; the axes are not a validated instrument. |
| "Two agendas, not two positions" | `SKILL.md` dialogue section | craft | theory | Unmarked. Useful and unfalsifiable as phrased; the operational test (reply to the act) is better than the slogan. |
| "Defamiliarise one load-bearing object per scene" | `references/narrative-theory.md` §9 | Shklovsky, applied | theory | No measurement. The mannerism warning is the part with craft authority. |
| "The last line should land on the change" | `SKILL.md` scene gate | craft | theory | Unmarked, and stated without its exception: endings that refuse closure land after the change deliberately. |

Two rows deserve a second look. "A scene changes a state" is the most quoted rule in the repository and has no marker anywhere except the scene gate's operational definition. "The obvious choice is the draft choice" is the skill's originality law and rests on an analogy between a sampling distribution and a decision — a good analogy, but not a measurement.

What was not audited: the Russian and English craft files' linguistic claims (no source in the corpus covers them), the rubric's criteria (a judgement instrument, not a measurement), the scripts (surface proxies, labelled as such), and the prose in `examples/` (original to the repository, not evidence for any claim). What was audited: every percentage, every `[data: …]` marker, every prescriptive sentence in the always-loaded and knowledge layers.

Read the status column as a ladder, not a binary. A theory row that is load-bearing is more important than a measured row that is decorative — the question is not "is this evidenced?" but "what breaks if this is wrong?". The rows marked hypothesis are the ones where the answer is "the skill's central claim", which is why `docs/limitations.md` exists and why the evaluation protocol measures output rather than compliance.

## Numbers register

Every figure the skill uses, with the denominator that makes it meaningful. "Used in" lists the files where the figure appears; a figure used without its condition in any of those files is an inconsistency.

| Figure | Paper | Exact meaning | Denominator / condition | Used in |
|---|---|---|---|---|
| 93.2 | StoryScope | Binary macro-F1, narrative features only (257) | Human vs AI, prompt-matched test set (~8.3k stories, ~1.38k prompts) | `SKILL.md`, `README.md`, `ai-narrative-signature.md`, `docs/architecture.md`, `docs/design-decisions.md` |
| 84.8 | StoryScope | Binary macro-F1, 30 core features | Same test set | `ai-narrative-signature.md`, `01-storyscope.md` |
| 91.1 | StoryScope | Binary macro-F1, core + fingerprints (101) | Same test set | `01-storyscope.md` only — the string also appears in `05-fingerprinting.md` as Qwen MATH accuracy, an unrelated measure |
| 96.0 | StoryScope | Binary macro-F1, narrative + style (304) | Same test set | `01-storyscope.md` only — collides with 96.05 AUROC in `04-dna-gpt.md` |
| 85.8 | StoryScope | Binary macro-F1, style only (39) | Same test set | `01-storyscope.md` only |
| 93.9 / 95.5 | StoryScope | Binary macro-F1 after vs before LAMP editing | 278 Gemini stories, Gemini as rewriter | `README.md`, `docs/architecture.md`, `docs/design-decisions.md`, `ai-narrative-signature.md`, `01-storyscope.md` |
| 68.4 | StoryScope | Six-way macro-F1, narrative features | Six sources, chance 16.7% | `01-storyscope.md` only — collides with 68.44 (Qwen vs base) in `05-fingerprinting.md` |
| 79 / 57 | StoryScope | % of stories with no subplots | AI / human, categorical | `story-architecture.md`, `ai-narrative-signature.md`, `methodologies/01`, W1, W14, `01-storyscope.md` |
| 77 / 52 | StoryScope | % of narrators explicitly explaining the theme | AI / human | `README.md`, `docs/design-decisions.md`, `ai-narrative-signature.md`, `01-storyscope.md` |
| 69 / 46 | StoryScope | % resolution driven by protagonist choice | AI / human, categorical | `methodologies/02`, `character-intelligence.md`, `ai-narrative-signature.md`, `01-storyscope.md` |
| 47 / 27 | StoryScope | % resolution by internal understanding or acceptance | AI / human, categorical | `README.md`, `docs/design-decisions.md`, `story-architecture.md`, `examples/10`, `01-storyscope.md` |
| 81 / 38 | StoryScope | % emotion conveyed through physical sensation / bodily metaphor | AI / human | `prose-engineering.md`, `methodologies/03`, `examples/07`, `01-storyscope.md` |
| 8 / 29 | StoryScope | % explicit emotion labels | AI / human | Same four files |
| 24 / 47 | StoryScope | % explicit named intertextual reference | AI / human | `ai-narrative-signature.md`, `01-storyscope.md` |
| 21 / 42 | StoryScope | % thematically parallel subplots | AI / human | `ai-narrative-signature.md`, `01-storyscope.md` |
| 38 / 59 | StoryScope | % morally ambivalent protagonist | AI / human | `ai-narrative-signature.md`, `01-storyscope.md` |
| 0.71 / 0.49 | StoryScope | Mean rarity percentile (distance to 25 nearest neighbours) | Human / AI, percentile against train+val; Cohen's d = 0.83 | `originality.md`, `ai-narrative-signature.md`, `01-storyscope.md` |
| 24.7 / 7.1 | StoryScope | % in the corpus-wide rarest decile | Human / AI | Same three files |
| 99.0 | Ghostbuster | In-domain F1 averaged over three domains | 3 × 7,000 documents, gpt-3.5-turbo training data | `02-ghostbuster.md` — collides with 99.00 TPR in DNA-GPT's white-box cells |
| 97.0 | Ghostbuster | Mean out-of-domain F1 | Train on two domains, test on the third | `02-ghostbuster.md` |
| +7.5 | Ghostbuster | F1 margin over the best prior system under domain shift | Same out-of-domain protocol | `02-ghostbuster.md` |
| 52.42 → 25.59 | Fingerprinting | Behavioural-feature accuracy, T0 → T3 | 8-way, 19 models, chance 12.5% | `docs/architecture.md` (as 52.4/25.6), `05-fingerprinting.md` |
| 60.72 → 19.74 | Fingerprinting | Stylometric accuracy, within-English T0 → cross-lingual average T0 | 8-way, six translation directions, translated prompts | `docs/architecture.md` (as 19.7), `multilingual-notes.md`, `05-fingerprinting.md` |
| 80.07 | Fingerprinting | Lexical accuracy at T0 | 8-way, cross-family, chance 12.5% | `05-fingerprinting.md` |
| 30.58 | Fingerprinting | Semantic accuracy, cross-lingual average at T0 | Six directions, chance 12.5% | `multilingual-notes.md`, `05-fingerprinting.md` |

Deliberately absent from the register: 55.9 (length-only baseline), 97.8 (random features), 5.9 and 41.6 (Ghostbuster margins), 0.06 (DetectGPT average gain). They are real and appear in the dossiers, but no skill rule turns on them; adding them to the register would imply they carry weight they do not.

**Numeric collisions are a hazard, not an oddity.** Five figures in this register are also used, with a different meaning, in another dossier: 91.1 (Qwen MATH accuracy), 96.0 (96.05 AUROC), 68.4 (68.44 averaged accuracy), 99.0 (99.00 TPR), 93.9 (93.98 AUROC for the OpenAI classifier on German). A repo-wide grep for a bare number therefore returns false positives, which is why any change must grep the full expression and the file that owns the denominator, not the digits alone.

## Known inconsistencies

Ordered by likely damage, not by file.

1. **`README.md`: two denominators presented as one trend.** Fragment: "separates human from AI fiction at 93.2% macro-F1 — and still at 93.9% after span-level stylistic rewriting". 93.2 is the full-corpus narrative-only score; 93.9 is LAMP on 278 Gemini stories whose own pre-edit score was 95.5. The same-subset change is −1.6, not +0.7. Repair: state both baselines.

2. **`docs/architecture.md`: same mismatch, plus a mislabelled cause.** Fragments: "the corpus-wide narrative baseline of 93.2% barely moved", and "after professional span-level stylistic rewriting". The first compares 93.2 with 93.9 across denominators. The second implies professional editors; the rewriter was Gemini, prompted with 25 professional examples.

3. **`docs/architecture.md`: "formatting accuracy falling from 52.4 to 25.6".** The measure is behavioural-feature *classification* accuracy, and the fall spans crop, format strip, and case/punctuation scrub. Calling it formatting accuracy attributes the whole drop to formatting, when T2→T3 alone accounts for 16.29 of the 26.83 points.

4. **Three files quote 79% without the 57% human baseline.** `methodologies/01-plot-and-causality.md`: "79% of model-written stories carry no subplot"; `workflows/01-short-form.md` and `workflows/05-voice-and-complex-structure.md` have the same figure. Bare, it implies subplots are the norm; the dossier's own base-rate note says 57% of human stories also have none. `references/story-architecture.md` and `references/ai-narrative-signature.md` quote both.

5. **`references/literary-critique.md`: length figure without its transformation.** Fragment: "at fifty words, identification accuracy sits near 22–27% … and only approaches 50% at full-response length". Those values are the P2* condition — fully paraphrased and surface-scrubbed. Under T0 the same 50-word window scores higher. The claim is directionally right and numerically understated.

6. **A promised mechanism is missing from its file.** `05-fingerprinting.md`'s capability map says the L1–L7 grid is "annotated with a durability rating per level" in `references/quality-levels.md`. That file contains no durability rating and no instance of the word. Either add the ratings or correct the map.

7. **Ending vocabulary collides with a canonical artifact.** `templates/decision-ledger.md`: "ENDING MODE [resolved | unresolved | refused | ironic]". `references/story-architecture.md` §10 and `references/narrative-theory.md` §14 define six types: resolved, ambiguous, ironic, circular, open, tragic. "Unresolved" is not "open" as defined, "refused" is a stance rather than a type, and three types are unavailable in the artifact that is supposed to record the decision.

8. **Two different "eight"s.** `SKILL.md`'s eight decisions include Time and Refusals but not Ending mode. `templates/decision-ledger.md`'s "Minimum viable ledger — eight fields" includes Ending mode and two refusals but not Time. Both are called eight; a reader comparing them will assume one is wrong.

9. **`docs/design-decisions.md` D4: "Fifteen engines, five workflows, one doctrine".** The repository has 14 routes across five workflow *files*. The title conflates files with routes and undercounts by nine.

10. **Tag names are not stable, and one paper has no tag definition.** `[data: Fingerprinting]` (capital F) appears in `literary-critique.md` and twice in `multilingual-notes.md`, but `05-fingerprinting.md` never defines a tag at all — the other four dossiers do. `[data: :]` in `originality.md` line 18 is malformed. `[data: Paper]` and `[data: <Paper>]` are legitimate placeholders in the marker legends, but a naive count reads them as citations and they should be excluded when auditing. Repair: settle on `[data: Fingerprinting]` for all three uses, add the definition line to the dossier header, fix the empty tag, and document the placeholder convention.

11. **`ai-narrative-signature.md` repeats an error its own dossier flags.** The Gemini row says "external character description elevated"; `01-storyscope.md` §Limitations says this is an abstract-level error and that external-description introduction is an AI-general core feature (52% vs 30%), not a Gemini fingerprint. One of the two must change.

12. **`ai-narrative-signature.md` cites "21.4% uniqueness" for in-dialogue character introduction.** The value 21.4 does appear in the paper's appendix table, verified against `research/sources/storyscope.txt`, but it is not in the dossier's recovered feature set, so the skill cannot check it — or its unit — from its own sources. Add it to the dossier with its column definition, or drop it.

13. **`prose-engineering.md` points at section numbers that do not exist.** Header: "except the StoryScope figures in §8 and §9". The file's sections are unnumbered; the figures sit in "Sensory channels without the checklist" and "Emotion on the page". Every stale § reference in the repo has the same cause: headings were renamed and the pointer was not.

14. **`tests/results/iteration-1.md` is linked but absent, and the raw evidence covers six of ten prompts.** `README.md`, `README.ru.md`, `docs/limitations.md` and `tests/protocol.md` all point at the aggregate report; `limitations.md` calls it "a case series of ten prompts". `tests/evals.json` defines ten evals, but `tests/results/raw/` contains runs for eval 1, 2, 4, 6, 7 and 9 only, with no evals 3, 5, 8 or 10 and no aggregate file. `scripts/validate_skill.py` reports the two broken README links. Either publish what exists and state the missing four, or drop the claim to six.

15. **`01-storyscope.md`'s capability map mixes pair orders inside one cell.** Fragment: "Embodied emotion 81% vs 38%; explicit labels 29% vs 8%". The first pair is AI-first, the second human-first, in a table whose other rows are also mixed. The appendix table it summarises has explicit Human/AI column headers; the map lost them.

16. **`SKILL.md` conflates two transformations.** Research basis: "formatting and stylometry are the first signals to die under paraphrase and across languages". Behavioral dies under formatting removal; stylometry is weakest across languages; paraphrase hurts lexical most in absolute points (11.9 vs 4.3). Three transformations, three different rankings.

17. **"Roughly 5,000 words" is a corpus mean, not a per-source fact.** `ai-narrative-signature.md`: "61,608 stories of roughly 5,000 words" and "each about 5,000 words". Per-source means run 2,946 to 6,817; three of the five models average near 3,000. Harmless in a summary, misleading if used to argue that length was controlled.

18. **`references/story-architecture.md` quotes 79/57 without the prompt-artifact caveat.** This file's own audit, since it is the file most likely to be cited on subplots. The gap is measured under a ≤120-word premise that cannot ask for a second line; the direction is informative, the size is prompt-shaped.

19. **Ghostbuster is effectively untagged outside its dossier.** Across the files that predate this audit, `[data: Ghostbuster]` appears once — in the dossier's own style note. Every other use of its findings (99.0, 97.0, +7.5, the search shape) is untagged or sits beside a StoryScope tag by proximity. Not wrong, but the marker system is carrying less than it appears to.

20. **`references/originality.md` line 18: `[data: :]`.** A malformed tag in a file that otherwise uses markers correctly. Trivial to fix; worth fixing because it is the string a validator will report first.

21. **`01-storyscope.md` puts LAMP-edited stories inside the binary detection table.** The row "LAMP-edited stories | — | 93.9 | .988" sits under "Binary detection (Table 2)" beside rows measured on the full test set, but it is a robustness check on 278 Gemini stories whose baseline was 95.5. This is the origin of inconsistencies 1 and 2: the figure left its condition behind when it was copied out. Repair: move the row below the table, or annotate the denominator in the row itself.

Fixing these: items 1, 2, 3, 4, 5, 15, 16, 18 and 21 are denominator, ordering, table-structure, or labelling repairs and can be done in one pass without a design decision. Items 6, 7, 8, 9, 13 and 14 need an owner to choose between adding the missing thing and correcting the promise. Items 10, 11, 12, 17, 19 and 20 are hygiene and should be done with the next edit of the file they live in, not as a separate sweep.

## How to add a claim

1. **Decide the status before writing the sentence.** If the sentence would survive a reviewer asking "measured where?", it is data. If it would not, it is theory or hypothesis, and the marker goes on the sentence, not in a footnote.
2. **Find the dossier section.** A data claim needs `references/research/NN-*.md` §section. If the figure is not there, add it to the dossier first — with its denominator — then use it.
3. **Register the number.** If the claim contains a figure, add a row to the numbers register above: paper, exact meaning, denominator, files. Update every file that already quotes it in the same commit.
4. **Add a capability row.** If the claim changes what the skill does, add a row to the Research → Capability map in `references/research-foundations.md`, naming the file, engine, or workflow where the capability lives.
5. **Add a hypothesis row if needed.** If the claim is ours and load-bearing, add it to `docs/limitations.md` with a falsification condition. A hypothesis without a test is a slogan.
6. **Run the validator and grep the figure.** `python scripts/validate_skill.py` catches structure, not denominators; searching the raw number across the repo catches the denominators.
7. **Report a disagreement rather than resolving it silently.** If two sources conflict — DNA-GPT's lexical metric against Fingerprinting's durability ladder is the standing example — write both and say how the skill resolves the conflict. A maintainer who picks one without recording the other has created the next inconsistency.
