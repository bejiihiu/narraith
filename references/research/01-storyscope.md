# StoryScope — discourse-level idiosyncrasies in AI fiction

> Purpose: Record what Russell et al. (COLM 2026) actually measured about narrative-level differences between human and LLM short stories, and state precisely which parts Narraith may treat as constraints.
> Read when: You are writing `references/ai-narrative-signature.md`, any engine that touches theme, subplot, resolution, interiority, intertextuality, or a workflow gate that calls a feature "AI-like".
> Related: `references/research-foundations.md` — how the five dossiers combine; `references/ai-narrative-signature.md` — primary consumer; `references/quality-levels.md` — L1–L7 vocabulary used in the mapping; `references/research/02-ghostbuster.md` … `05-fingerprinting.md` — the other four sources.

Tags used throughout: `[data: StoryScope]` = measured in the paper; `[theory]` = narratology or craft claim, not an experimental result; `[hypothesis]` = our engineering bet, unproven.

## Contents

1. Bibliographic record
2. Research question and hypothesis
3. Methodology
4. Results
5. The feature taxonomy as an instrument
6. Limitations
7. What transfers to generation, and what does not
8. Idea → capability map
9. Engineering hypotheses (not proven by this paper)
10. Verbatim anchors
11. How we would know this dossier was misapplied

## Bibliographic record

- **Authors:** Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, John Wieting.
- **Affiliations:** University of Maryland, College Park; Google DeepMind.
- **Venue:** COLM 2026 (published conference paper, arXiv:2604.03136v6, 10 Aug 2026).
- **PDF:** https://arxiv.org/pdf/2604.03136
- **Artifacts released:** code, 10,272 writing prompts, 51,336 AI-generated narratives, per-story feature vectors. Human stories withheld for copyright. Total cost reported at ~$4.4k (≈$2.8k generation, ≈$1.6k feature extraction).
- **Kind of paper:** empirical measurement plus a supervised-classification benchmark. It induces a feature space by LLM analysis, then trains classifiers to test whether that space separates sources. It is *not* a craft essay, not a reader-response study, and not an intervention study.
- **What it does not study:** literary quality or reader preference; novels or long-form; languages other than English; partial AI editing of human text; human–AI collaboration; whether *changing* a feature changes perceived quality; genre-conditioned craft norms (topic is used only as a robustness check, §G); causal mechanism inside the models that produces these choices.

The paper's own framing of the stakes is legal and economic, not aesthetic: it opens with a commercially published novel withdrawn after being flagged ~78% AI-generated, and with ~20% of a 14,000-novel self-published sample flagged as largely AI-generated. Originality is operationalised as *statistical rarity in a feature space of narrative decisions*, a proxy the authors explicitly borrow from creativity research and copyright doctrine rather than from criticism.

## Research question and hypothesis

`[data: StoryScope]` The question: can AI-generated fiction be separated from human fiction *without* using style — that is, using discourse-level narrative choices (who acts, what is revealed when, how time is ordered, whether subplots exist)?

The paper's surface-vs-discourse distinction is the load-bearing move. Surface signals are lexical and syntactic: em-dash overuse, "delve", "tapestry", sentence rhythm, figurative density. The authors grant these are "highly discriminatory" and then argue they are *fleeting*: GPT-5.4 reportedly reduced em-dash usage, and fine-tuning to mimic human style reportedly drops creative-writing detection from 97% to 3%. Discourse-level features — plot structure, character agency, information revelation — are claimed to be harder to "humanize" because changing them requires structural rewriting rather than post-hoc editing.

Stated hypothesis: humans and AI models make systematically distinct narrative choices, and those differences persist when stylistic cues are removed. `[theory]` The implicit second hypothesis, never tested directly, is that these choices are *more durable* as models evolve. The paper asserts durability; it measures durability only against one editing procedure on one model (§4.2).

## Methodology

### Corpus construction

`[data: StoryScope]` 10,272 human short stories extracted from Books3, identified by running Gemini 2.5 Flash over titles and blurbs to find short-story anthologies. For each human story, a writing prompt is reverse-engineered by prompting Gemini 2.5 Flash to infer the underlying premise (June 2025), constrained to a single paragraph ≤120 words beginning "Write a short story" and naming at least one character or setting; comparison phrases ("in the style of", "reminiscent of") are forbidden. The same prompt text goes to all six sources. Source identities are anonymised in every LLM-facing prompt; presentation order in pairwise comparisons is randomised.

Six sources:

| Source | Exact model | n | Mean words | Median words |
|---|---|---|---|---|
| Human | Books3 anthology stories | 10,272 | 6,403 | 5,035 |
| Claude | Claude Sonnet 4.6 | 10,259 | 6,817 | 6,187 |
| GPT | GPT-5.4 | 10,272 | 6,651 | 6,515 |
| Gemini | Gemini 3 Flash | 10,261 | 3,155 | 2,967 |
| Kimi | Kimi K2.5 | 10,272 | 3,274 | 3,005 |
| DeepSeek | DeepSeek V3.2 | 10,272 | 2,946 | 2,693 |

61,608 stories total (51,336 AI + 10,272 human), mean 4,753 words; 24 generations refused. Prompt word targets average 6,242 (median 5,000, IQR 3,000–7,000). Note the spread: the abstract's "each ~5,000 words" holds for the corpus mean, not for individual sources — Gemini, DeepSeek and Kimi produce roughly half the length of GPT and Claude.

### Three-stage pipeline

1. **Structured intermediate representation.** GPT-5.1 extracts, per story, a JSON template over ten NarraBench dimensions (agents and motivations, event sequence, causal links, plot fields, setting, revelation, temporal order, narration/POV, style inventory). The template deliberately strips wording so later stages reason over narrative content. Early ablation: running the pipeline on raw text instead of templates changes the discovered features almost entirely — only 6 of the top 20 overlap; raw-text features are style-heavy (humour, vocabulary register, allusion type), template features are structure-heavy (emotional arcs, relationship trajectories, event density, flashback use).
2. **Cross-source comparison.** A discovery pool of 600 stories over 100 randomly selected parallel prompts, held out from the main corpus. All six templates for a prompt go to GPT-5.1 in one call (32 batches, mean 3.1 prompts per batch); output is per-source dimension notes, cross-source divergence notes, and an executive summary. This compresses ~2.7M tokens of raw text to ~686K tokens of comparative analysis.
3. **Feature discovery.** Ten dimension-specific expert prompts (one per NarraBench aspect), each asking for closed-form questions with discrete answers. Three independent discovery runs, union taken: **408 candidates**, deduplicated by embedding clustering (F2LLM-4B, single linkage, cosine 0.85, keep the member nearest the centroid, 65 clusters merged) → **304 features**, a 25.5% reduction.

`[data: StoryScope]` NarraBench has twelve aspects; **ten are used**: Agent, Social Network, Event, Plot, Structure, Setting, Time, Revelation, Perspective, Style. **Excluded: Paratext and Motivation** — the latter because it depends on external context unavailable in this setting. One naming wrinkle: the ablation table (Table 8) runs nine dimensions and uses **Situatedness** where the enumerated ten have **Structure**; Style is absent because the narrative variant excludes it. Every core-feature tag in the appendix is one of SIT, PLT, EVT, AGENT, SET, TMP, REV, PER — no feature carries a STRUCT tag.

Feature types: categorical 124, ordinal 59, scale 45, binary 44, multi-select 32.

### Feature assignment and reliability

Assignment model: **Gemini 3 Flash with minimal thinking**, applied aspect-by-aspect rather than in one call. Coverage rose from 68.4% (single-call) to 95.4% (aspect-based); single-call dropout concentrated in revelation and temporal dimensions. Reliability: five independent runs give Krippendorff's α = 0.90 (nominal), mean pairwise Cohen's κ = 0.89. Human validation on 240 story-feature items across 12 stories: model vs annotator 1 κ = 0.91, vs annotator 2 κ = 0.77, mean 0.84; **human vs human κ = 0.74**. The model agrees with individual humans more than humans agree with each other.

Encoding: one-hot for categorical and binary, multi-hot for multi-select, numeric for ordinal and scale. Encoded dimensionality: Narrative+Style D = 1,108; Narrative D = 958; Style Only D = 129.

### Feature roles and selection

`[data: StoryScope]` XGBoost (chosen over linear models and random forests on the validation split, and kept because it decomposes exactly with SHAP tree values). Importance and stability estimated by bootstrap SHAP, **B = 50 with prompt-level resampling**. Three roles:

- **Core** — stable and important in the binary human-vs-AI task, with a consistent gap across all five AI models, signed human-leaning or AI-leaning. Thresholds (§D): stable-important quadrant membership, null significance (permutation p ≤ 0.10), stability ≥ 0.55, top-quartile frequency ≥ 0.60, absolute human–AI mean gap ≥ 0.20, cross-model AI spread ≤ 0.35.
- **Fingerprint** — from the six-way task; SHAP importance concentrated in a single source class whose observed values visibly differ. Counts: human 32, Claude 26, GPT 11, Gemini 11, DeepSeek 7, Kimi 3.
- **Excluded** — neither.

Result: **30 core features, 75 fingerprint features.**

Feature variants: Narrative (257 features = 304 minus 39 style features minus 8 features elsewhere flagged as style-related, 47 removed); Style Only (39); Narrative+Style (304); Core Only (30); Core+Fingerprint (101).

### Baselines, metrics, protocol

Baselines on raw text: ModernBERT-base fine-tuned (max length 512, 3 epochs); Stylometric+XGB on 144 hand-crafted features (n-grams, POS distributions, readability, punctuation, dialogue, function words); TF-IDF+XGB on 5,000 features; Binoculars zero-shot in accuracy mode.

Metrics: macro-F1 and AUPRC for binary; macro-F1 and accuracy for six-way. Confidence intervals are **prompt-bootstrap** (prompt-level resampling). All splits are prompt-grouped to prevent leakage. Hyperparameters via grid search: binary `nest=420, depth=8, λ=2.0, scale_pos_weight=5`; six-way `nest=500, depth=7, λ=1.0`.

Split sizes are reported two ways and do not reconcile: §3 states 52,434 training stories / 8,739 prompts and a test set of 1,377 prompts / 8,262 stories; §D states 7,383 train / 1,405 validation / 1,384 test prompts, final retrain on 8,788 prompts / 52,707 stories, test 1,384 prompts / 8,301 stories. Treat all headline numbers as stable to ±0.1 point, not as exactly reproducible from the text.

### Robustness checks

- **Length.** A length-only logistic regression reaches 55.9% macro-F1, so length is not trivial. On a decile-stratified length-matched subset (2,754 stories; human median 4,973 vs AI 4,951 words) Narrative stays at 93.2% before and after; across short/medium/long tertile bands it is 91.6 / 94.3 / 93.7.
- **Memorisation.** 13-gram and near-verbatim screens flag 0.70% of comparisons, removing 1.67% of prompts; the strongest cases are canonical anthology texts (Poe, Doyle, Wilde, Dickens, *The Yellow Wallpaper*). Removing them moves binary 93.18 → 93.23 and six-way 68.42 → 68.68.
- **Topic.** BISAC coding over the test set; narrative binary macro-F1 ranges 90.0% (mystery/detective) to 96.2% (historical), six-way 65.8% to 70.8%; Kruskal–Wallis over six topics H = 4.69, p = 0.46 — no significant topic effect.

## Results

### Binary detection (Table 2)

| Model | Features | macro-F1 | AUPRC |
|---|---|---|---|
| Narrative (ours) | 257 | 93.2 | .959 |
| Core Only | 30 | 84.8 | .828 |
| Core + Fingerprint | 101 | 91.1 | .934 |
| Narrative + Style | 304 | 96.0 | .982 |
| Style Only | 39 | 85.8 | .867 |
| ModernBERT | — | 99.9 | 1.00 |
| Stylometric + XGB | 144 | 99.8 | .999 |
| TF-IDF + XGB | 5,000 | 99.7 | .999 |
| Binoculars (zero-shot) | — | 55.9 | .404 |

> The LAMP row is not part of the full test set. It is a separate subset: 278 Gemini-generated stories,
> scored 95.5% before rewriting and 93.9% after. Do not read it as the corpus-wide post-edit score.

`[data: StoryScope]` Narrative alone is 2.8 points below Narrative+Style (95% prompt-bootstrap CI 2.09–3.54), i.e. it recovers ~97% of the combined model. Core Only (30 features) retains ~91% of the narrative model. Style Only is roughly at parity with Core Only (85.8 vs 84.8). Supervised raw-text baselines are near-ceiling: ModernBERT 99.9. The paper's phrasing "nearly matches the strongest baselines" (96.0 vs 99.9) is generous; the defensible claim is that narrative features are competitive with a *style-only* feature model and interpretable, not that they rival a fine-tuned encoder.

Binary has a 5:1 class imbalance; an all-AI classifier already scores 83.3% accuracy, which is why accuracy is omitted from the binary table.

### Six-way attribution (Table 3)

| Model | Features | macro-F1 | Accuracy |
|---|---|---|---|
| Narrative | 257 | 68.4 | 68.4% |
| Core Only | 30 | 46.5 | 46.8% |
| Core + Fingerprint | 101 | 63.4 | 63.6% |
| Narrative + Style | 304 | 77.3 | 77.3% |
| Style Only | 39 | 60.4 | 60.5% |
| ModernBERT | — | 99.8 | 99.8% |
| Stylometric + XGB | 144 | 99.6 | 99.6% |
| TF-IDF + XGB | 5,000 | 99.5 | 99.5% |

Chance is 16.7%. Narrative exceeds Style Only by 8.0 points (CI 6.7–9.2); Core+Fingerprint exceeds Core Only by 16.8 points (15.7–17.9). Per-class F1 (Narrative / with Style): Human .89/.93, Claude .77/.89, GPT .73/.82, Gemini .60/.67, DeepSeek .57/.66, Kimi .55/.67. Human is the most separable source; the five models overlap heavily with each other. The six most-confused pairs are exclusively AI↔AI; the worst single pair (Gemini↔DeepSeek, 222 and 207 stories) dwarfs the worst human confusion (Human→Kimi, 46 stories).

### Qualitative findings, with exact figures

Thematic over-determination (all `[data: StoryScope]`):

- Thematic explicitness and moralising is ~20% higher for AI on the 1–5 scale (3.94 vs 3.28).
- The narrator explicitly explains the story's theme in **77%** of AI stories vs **52%** of human ones.
- AI dialogue serves philosophical debate in **59%** vs **34%**.
- AI references to other works are vague allusions in **72%** vs **50%**; humans name specific texts and authors in **47%** vs **24%**, and balance explicit with implicit references in **37%** vs **16%**.
- Moral/philosophical weighting 3.68 vs 3.26; thematic unity 4.74 vs 4.41.

Structural streamlining:

- Resolution driven by the protagonist's own choice: **69%** AI vs **46%** human.
- "No subplots": **79%** AI vs **57%** human; subplots that echo the central theme: **42%** human vs **21%** AI.
- Resolution through internal understanding or acceptance: **47%** AI vs **27%** human.
- Causal chain continuity 4.20 vs 3.92; spatial granularity 2.53 vs 2.27; opening spatial grounding 2.33 vs 2.12; pre-threat character investment 2.99 vs 2.76.
- Central character introduced by external description: **52%** AI vs **30%** human.

Sensory and embodied performance:

- Emotion conveyed through physical sensation and bodily metaphor: **81%** AI vs **38%** human.
- Explicit emotion labels: **8%** AI vs **29%** human.
- Smell-based imagery: **82%** AI vs **57%** human.
- Setting as psychological mirror 4.07 vs 3.58; environmental/ecological emphasis 3.21 vs 2.83; sensory density 3.93 vs 3.66; depth of interior access 3.93 vs 3.67.

Reader engagement and intertextuality:

- Fourth-wall breaking: **67%** human vs **39%** AI; direct reader address **28%** vs **7%**.
- Human writing "acknowledges its audience as a co-participant"; AI "writes as though no one is watching".

Temporal complexity:

- Human vs AI: depth of recontextualisation after a surprise 3.28 vs 2.95; chronological discontinuity 2.40 vs 2.12; nonlinear framing for delayed disclosure 1.96 vs 1.68; anachrony intensity 2.58 vs 2.31.

Narrative diversity:

- Human vs AI: location variety 1.34 vs 1.08; dialogue-to-narration ratio 2.95 vs 2.70; morally ambivalent protagonists **59%** vs **38%**.

### Geometry of the space

`[data: StoryScope]` In z-scored encoded feature space with Euclidean distance: mean human–AI centroid distance **6.6** vs mean AI–AI **4.3** (1.6×). The closest human–AI centroid pair (6.2) is still farther apart than the most distant AI–AI pair (6.0) — humans are not merely a wider version of the AI cluster, they sit elsewhere. Human dispersion: mean distance to own centroid 33.2 vs average AI radius 27.4 (+22%); median 10-NN radius 33.1 vs 29.2 (1.13×).

Per-story rarity (mean distance to 25 nearest neighbours, percentile against train+val): human mean percentile **0.71** vs **0.49** for AI, AUC 0.73, Cohen's **d = 0.83**. Overrepresentation in the rare tail: **24.7%** of human stories in the corpus-wide top 10% rarest vs **7.1%** of AI; top 1%: 3.0% vs 0.6%. Counts in the 8,262-story test set: top 10% holds 340 human and 487 AI stories; top 1% holds 42 human and 41 AI. At prompt level the human version is the rarest of the six **57.8%** of the time (chance 16.7%), mean margin 0.96 distance units. All distributions overlap substantially.

### Per-model fingerprints

| Source | Fingerprints | Signature (top features from Table 17) |
|---|---|---|
| Claude | 26 | Strength of event escalation (SHAP .402, uniqueness 22.4), event-type diversity, epilogue/flash-forward endings, no dreams, uncanny setting mood. Most distinctive AI profile: "restraint", flattest escalation, most uniform voice, reverent/continuist stance to tradition in 62% of stories vs 39–56% elsewhere; favours epilogues, avoids dream sequences, quiet rather than "avalanche" endings. |
| GPT | 11 | Gossip and rumour as plot mechanism (.200, 22.1), distant retrospective narrator, subverts reader expectation (41% vs 27–36%), no iterative narration, partial/ambiguous reconciliation. Gossip salience 64% vs 44–55% for other sources; ensemble social networks at human levels. |
| Gemini | 11 | Protagonist's social trajectory expands, speech primarily direct, siege/ordeal schema, personal names, frequent flashbacks. Tidies endings with extended denouements; bleakest settings (88% tagged bleak and oppressive). |
| DeepSeek | 7 | Narrator presence/visibility (.153), emotion through behavioural cues, plot-vs-atmosphere orientation, evenly interleaved backstory, embedded storytelling scenes. Front-loads crucial context other sources defer. |
| Kimi | 3 | In-action character introduction, in medias res entry, no explicit trait labelling. Fewest fingerprints, lowest F1 — sits at the generic centre, no distinctive choices. |

### Robustness to stylistic editing (LAMP)

`[data: StoryScope]` LAMP (Chakrabarty et al., 2025) rewrites seven categories of AI writing artifacts (cliché, redundant exposition, purple prose, etc.) using 25 few-shot examples from professional writers. Applied to **278 Gemini-generated stories**, with Gemini as the rewriter. Narrative classifier on edited stories: **93.9%** macro-F1 (AUPRC .988) vs **95.5%** (.996) unedited — a drop of **1.6 points**.

What this implies: the classifier is largely orthogonal to the surface artifacts LAMP targets. What it does not imply: that narrative features are immutable. The test uses one model as both author and rewriter, 278 stories, and edits that by construction do not touch causal structure, subplot count, or resolution mode. It shows those particular edits do not move those particular features; it does not show that a determined rewriter could not.

## The feature taxonomy as an instrument

Ten dimensions, with the paper's prefix conventions: **SIT** situatedness, **PLT** plot, **EVT** events, **AGENT** agents, **SOC** social networks, **SET** setting, **TMP** temporal structure, **REV** revelation, **PER** perspective, **STYLE** style. Core features cluster in SIT (6), SET (7), PLT (4), PER (4), REV (3), EVT (2), TMP (2), AGENT (2); no core feature is tagged SOC, STRUCT or STYLE, and no dimension alone is sufficient (best single dimension: agents, 80.2% binary macro-F1) or necessary (largest leave-one-out drop: agents, −1.2 points).

All 30 core features are recoverable with means. Three variables appear twice because both poles are discriminative, so the table has 33 rows and 30 unique features. `Human`/`AI` columns are means (scale/ordinal) or prevalence % (categorical/binary), from Table 16.

| # | Feature | Dim | Type | Question (abridged from Tables 14–15) | Human | AI | Leans |
|---|---|---|---|---|---|---|---|
| 1 | Thematic Explicitness and Moralizing | SIT | scale 1–5 | How explicitly does the story articulate its themes or morals? | 3.28 | 3.94 | AI |
| 2 | Moral / Philosophical Weighting | SIT | scale 1–5 | How heavily does the story foreground moral or philosophical questions? | 3.26 | 3.68 | AI |
| 3 | Thematic Unity | PLT | scale 1–5 | To what extent do subplots and flourishes serve a central thematic concern? | 4.41 | 4.74 | AI |
| 4 | Narratorial Thematic Commentary | SIT | binary | Does the narrator explicitly comment on themes beyond characters' perspectives? | 52% | 77% | AI |
| 5 | Dialogue Function → philosophical debate | PER | multi | What main functions does dialogue serve? (advance plot, reveal character, worldbuilding, philosophical, comic) | 34% | 59% | AI |
| 6 | Reference Explicitness → implicit echoes | SIT | categorical | Are intertextual gestures explicit or diffuse? (none, explicit named, implicit echoes, balanced mix) | 50% | 72% | AI |
| 7 | Dominant Emotional Expression → embodied metaphors | AGENT | categorical | How are characters' emotions most commonly conveyed? (explicit labels, embodied metaphors, behavioural cues, ambiguous) | 38% | 81% | AI |
| 8 | Setting as Psychological Mirror | SET | scale 1–5 | To what degree does physical environment mirror characters' inner states? | 3.58 | 4.07 | AI |
| 9 | Environmental and Ecological Emphasis | SET | scale 1–5 | How prominent is the natural environment or ecology in the narrative? | 2.83 | 3.21 | AI |
| 10 | Dominant Sensory Modalities → olfactory | SET | multi | Which sensory modalities does the story most frequently engage? (visual, auditory, olfactory, tactile, gustatory, kinesthetic) | 57% | 82% | AI |
| 11 | Sensory Density | SET | scale minimal–lush | How dense is sensory description across the narrative? | 3.66 | 3.93 | AI |
| 12 | Depth of Interior Access | PER | scale 1–5 | How deep into characters' inner life does narration go? | 3.67 | 3.93 | AI |
| 13 | Continuity of Main Causal Chain | EVT | scale 1–5 | How continuous is the single causal chain from inciting incident to ending? | 3.92 | 4.20 | AI |
| 14 | Spatial Granularity Level | SET | ordinal very_low–high | How fine-grained is the story's depiction of physical space? | 2.27 | 2.53 | AI |
| 15 | Agency in Resolution → protagonist choice | PLT | categorical | Is resolution driven by protagonist's choices or external events? (protagonist_choice, mixed, external_fate) | 46% | 69% | AI |
| 16 | Character Introduction → external description | AGENT | categorical | What narrative device primarily introduces the central character? (external_desc, in-action, in-dialogue, inner_thought, others_reports) | 30% | 52% | AI |
| 17 | Subplot Integration → no subplots | PLT | categorical | How directly do subplots echo the central theme? (no_subplots, thematically_parallel, contrasting, independent) | 57% | 79% | AI |
| 18 | Mode of Resolution → internal understanding | EVT | categorical | Is the main event chain resolved through internal acceptance or external action? (resolved externally, resolved internally, unresolved) | 27% | 47% | AI |
| 19 | Opening Spatial Grounding | SET | ordinal | How clearly does the opening ground the reader in a specific physical setting? (none/vague, minimal, clear local, clear local+global) | 2.12 | 2.33 | AI |
| 20 | Pre-Threat Character Investment | REV | scale 1–5 | How much does the story build investment before major jeopardy? | 2.76 | 2.99 | AI |
| 21 | Intertextual Strategy Types → explicit named reference | SIT | multi | What kinds of intertextual engagement does the story employ? (explicit named, retelling, pastiche, myth/religion, self referential) | 47% | 24% | Human |
| 22 | Reference Explicitness → balanced mix | SIT | categorical | Second pole of #6. | 37% | 16% | Human |
| 23 | Fourth-Wall Permeability | SIT | ordinal 1–4 | To what extent does the story break the boundary between story-world and reader? (1 none – 4 radical) | 0.67 | 0.39 | Human |
| 24 | Frequency of Direct Reader Address | PER | ordinal | How often does the text directly address the reader? (never, occasional asides, frequent/structural) | 0.28 | 0.07 | Human |
| 25 | Depth of Recontextualization After Surprise | REV | scale 1 (none)–5 (complete re-reading) | How extensively does a revelation force reinterpretation of earlier scenes? | 3.28 | 2.95 | Human |
| 26 | Degree of Chronological Discontinuity | TMP | scale 1–5 | How often does the narrative jump across time? | 2.40 | 2.12 | Human |
| 27 | Nonlinear Framing for Delayed Disclosure | REV | scale 1 (linear)–5 (heavily fragmented) | To what extent does the story use time jumps to stage revelations? | 1.96 | 1.68 | Human |
| 28 | Anachrony Intensity | TMP | scale 1 (absent)–5 (dominant anachronic) | How heavily does the narrative rely on flashbacks or flash-forwards? | 2.58 | 2.31 | Human |
| 29 | Location Variety Scope | SET | ordinal single–multiworld | How many distinct physical locales does the story inhabit? | 1.34 | 1.08 | Human |
| 30 | Dialogue-to-Narration Proportion | PER | scale 1 (no dialogue)–5 (dialogue dominates) | What proportion of text is direct dialogue vs narration? | 2.95 | 2.70 | Human |
| 31 | Subplot Integration → thematically parallel | PLT | categorical | Second pole of #17. | 42% | 21% | Human |
| 32 | Moral Polarity Toward Protagonist → ambivalent | PLT | categorical | Does the narrative frame the protagonist's choices as morally clear or ambiguous? (clearly positive, ambivalent/mixed, clearly negative) | 59% | 38% | Human |
| 33 | Dominant Emotional Expression → explicit labels | AGENT | categorical | Third pole of #7. | 29% | 8% | Human |

Recovered: **30/30** unique core features, all with dimension, type, response options and human/AI means. Nothing here is partially reconstructed — the appendix prints the full set. What is *not* printed: per-feature SHAP values for all 30 (only the top-20 AI and top-13 human lists are ranked, with no scores), and the distribution of answers for the excluded options.

Reading notes on the table:

- **#23 and #24 are printed as ordinal but behave as prevalence.** Table 15 gives Fourth-Wall Permeability as ordinal 1–4 and Direct Reader Address as ordinal "never / occasional / frequent", yet Table 16 reports means of 0.67 and 0.28 for humans — below the stated floor — which coincide exactly with the §4.1 prevalence figures (67% vs 39%; 28% vs 7%). Treat both as binary rates, not scale points. Also note that #24's prevalence is under 30% in both populations: direct address is a minority device even among humans, so its absence is not diagnostic on its own.
- **#17/#21/#22 absolute rates are high for humans too.** "No subplots" is the modal human category (57%). Vague allusion is the modal human category (50%). These indicate relative propensity, never a required feature.
- **The largest gaps are emotional-channel and reader-stance items** (#7 81/38, #24 28/7, #33 29/8); the smallest are structural scales (#13 4.20/3.92, #19 2.33/2.12). Weight the diagnostic accordingly: a checklist that treats a 0.2-point scale difference as a verdict will fire on noise.

## Limitations

The paper's own:

- Human texts are Books3 anthology short stories — a specific canon, not a sample of all human writing.
- Human stories withheld; only the AI half and the features are released, so independent verification of the human side is limited.
- Feature extraction is LLM-based; validation is 240 items over 12 stories with two annotators.
- Fingerprints are model-version-specific (Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2) and will drift.
- LAMP robustness rests on 278 Gemini stories rewritten by Gemini.
- No claim about quality: originality is proxied by statistical rarity.

Methodological ones I would defend:

- **LLM-as-annotator circularity.** Templates are extracted by GPT-5.1, features discovered by GPT-5.1, values assigned by Gemini 3 Flash, and classifiers trained on those values. If the assigner's priors about "what AI text looks like" leak into the assignment, part of the 93.2% is the assigner recognising its own family. The κ = 0.84 human agreement blunts this but does not remove it: humans were asked to apply the same LLM-authored definitions.
- **Prompt reverse-engineering strips exactly the features being measured.** The prompt is a ≤120-word premise naming one character and one situation, with comparison and style framing forbidden. A human story's second storyline, frame narrative, or dense web of allusion is not recoverable from its premise, so it cannot appear in the prompt. The "no subplots 79% vs 57%" and "vague allusions 72% vs 50%" gaps are therefore measured *under a prompt that suppresses subplots and allusions for everyone*. The gap is real; its absolute size is prompt-shaped.
- **The human baseline is a premise-matched imitation target.** Models are asked to write the story the human already wrote. That is a task where fidelity to a known design is rewarded, which plausibly favours tidy single-track execution.
- **Length is audited only for binary.** Length-only classification reaches 55.9% macro-F1; six-way attribution is not length-audited, and Gemini/DeepSeek/Kimi produce roughly half the words of GPT/Claude. Many "narrative" features (location variety, secondary character density, event count, subplot presence) co-vary with length, so some of the 68.4% six-way signal may be a length proxy.
- **Single language, single form.** English; ~5k-word stories; no novels. Subplot economy, temporal architecture and intertextual density all scale with length.
- **Correlational.** Nothing here shows that changing a feature changes perceived quality, originality, or reader engagement. The classifier is a description of a difference, not a causal model of it.
- **"Human" is a publisher's canon.** Books3 short-story anthologies skew literary, mid-century-to-contemporary, Anglophone. A human-leaning feature may be a *literary-anthology* feature rather than a *human* feature. The paper never separates these.
- **Internal arithmetic gaps.** Fingerprint counts by source sum to 90 but the paper reports 75; Core+Fingerprint is 101, not 105, so ~4 features are counted in both roles. Split sizes differ between §3 and §D. The enumerated ten aspects include Structure, but Table 8 ablates Situatedness instead and no feature is tagged STRUCT. The abstract also credits Gemini with "external character description" as its signature, while §5 and Table 17 give Gemini expanding social trajectory, primarily direct speech, siege/ordeal schema, personal names and frequent flashbacks — external-description introduction is an AI-general core feature (#16), not a Gemini fingerprint. Reliability of the headline numbers is fine; exact feature-role bookkeeping is not fully reconciliable from the text.

## What transfers to generation, and what does not

| Finding | Transfers as | Does not transfer as |
|---|---|---|
| 93.2% narrative-only detection | Evidence that *discourse-level* choices are a real, large-variance axis between AI and human fiction — worth making the centre of the skill, ahead of word-level style. | Evidence that our skill can detect AI text better than a fine-tuned encoder (99.9%). We are not building a detector, and our features are not their features. |
| 30 core features at 84.8% | A short, high-yield diagnostic list. If 30 binary decisions carry most of the separation, those 30 are the right places to spend editorial attention. | A scoring rubric. Cohort means are not per-story thresholds; a story can hit every AI-leaning value and be excellent, or every human-leaning value and be unreadable. |
| "Human-leaning" signs | A prior: in the absence of a reason, the human-typical choice is the less default one. | A prescription. Human-leaning is a population statistic about Books3 anthologies. Copying it produces inverted snobbery: epigraphs, named references, fourth-wall asides and unresolved endings added to hit a distribution. |
| Emotional channel: AI 81% embodied / 8% labelled | The channel is a *choice*, and the modal AI choice is embodiment. Our rule must be "pick the channel by scene function", not "show, don't tell" — the paper shows AI already over-embodies. | "Never name an emotion." 29% of human stories do, and the human rate is the higher one. Naming is a legitimate instrument with a lower base rate, not a fault. |
| Subplot absence 79% vs 57% | Subplot presence is a structural decision that AI under-makes; a long-form workflow should force the question. | "Every story needs subplots." 57% of human stories have none. The correct gate is "if there is a second line, it must carry its own question and intersect the spine", not "add subplots". |
| Resolution by protagonist choice 69% vs 46% | Agency in the ending is the single largest structural difference; check who causes the final state change. | "External resolution is bad." 46% of human stories resolve otherwise, often deliberately (fate, system, refusal). The test is whether the ending's cause was *earned*, not who holds the lever. |
| Rarity: human percentile 0.71, d = 0.83 | Diversity is a portfolio property: vary the *combination* of decisions across a body of work, not within one story. | "Maximise unusualness per story." Rarity is measured against a corpus; chasing it inside one text produces incoherence, not originality. |
| LAMP: 1.6-point drop after style edits | Surface polish does not fix structural defaults — line editing cannot rescue a story whose decisions are modal. Justifies L5-before-L3 revision order. | "Structural features are immutable." One editing procedure on one model; nothing shows a structural rewrite is impossible, only that cliché removal does not do it. |
| Model fingerprints (Claude flat escalation, GPT gossip) | A caution: these are house styles of specific 2026 model versions, useful as a checklist of *defaults to avoid* when drafting with a given model. | Permanent laws of a model family, or a reason to write "anti-Claude" prose. They will be stale within a version cycle. |

The hard line: **the paper measures detectability, not merit.** A human story can be bad; an AI story can be good. Every number above is a difference between two sampling distributions. Our skill is allowed to use them as evidence about *defaults* — what gets produced when nobody decides — and must never use them as evidence about *value*.

## Idea → capability map

| Finding | Narrative mechanism it justifies | Narraith file that implements it |
|---|---|---|
| Narrator explains the theme 77% vs 52%; thematic explicitness 3.94 vs 3.28 | Meaning must be carried by a cost or an object, and the narrator must not close the inference the reader was supposed to perform. Gate: name the sentence where the story states its thesis; convert it into a consequence or delete it. Premise is written as a question, never as a verdict. | `references/ai-narrative-signature.md`, engine E1 in `methodologies/01-plot-and-causality.md`, L4 audit in `references/quality-levels.md` |
| Subplot absence 79% vs 57%; thematic-parallel integration 42% vs 21% | Every subplot carries its own dramatic question, costs the protagonist something the spine needs, and intersects the spine at two points (complication, resolution). If it cannot, it is a scene, not a line. | engine E1 `methodologies/01-plot-and-causality.md`, workflow 14 `workflows/05-voice-and-complex-structure.md`, workflow 3 `workflows/02-long-form.md` |
| Agency in resolution 69% vs 46%; internal-understanding endings 47% vs 27% | The final state change must be caused by a choice the protagonist makes under pressure, not by an event that arrives. Audit the last scene for who moves the lever and what it costs. | engine E3 `methodologies/02-character-and-dialogue.md`, E2 `methodologies/01-plot-and-causality.md`, L5/L6 in `references/quality-levels.md` |
| Causal chain continuity 4.20 vs 3.92; "tighter causal chains" | Tidy causality is the default. Force at least one causal link to be contingent (would not have happened without a specific earlier choice) and one to remain unexplained. | E2 `methodologies/01-plot-and-causality.md`, scene gate in `methodologies/03-time-and-scene.md` |
| Temporal complexity: discontinuity 2.40 vs 2.12, anachrony 2.58 vs 2.31, recontextualisation 3.28 vs 2.95 | Time order is a revelation instrument: choose the order that withholds the causal antecedent, and check that the surprise forces a re-reading of an earlier scene. | E7 `methodologies/03-time-and-scene.md`, `references/temporal-complexity.md`, workflow 13 |
| Embodied emotion 81% vs 38%; explicit labels 8% vs 29%; smell 82% vs 57%; sensory density 3.93 vs 3.66 | Channel selection by function: embodiment for what the character cannot say, naming for what they refuse to feel, sensory detail for scene pressure. Prohibit the reflex "tight chest + cold sweat" as a default. | E9 `methodologies/02-character-and-dialogue.md`, E10 `methodologies/04-prose-voice-originality.md`, `references/prose-engineering.md` |
| Fourth wall 67% vs 39%; direct address 28% vs 7% | Narrator stance is a decision with a cost: address implies a listener and a reason to speak now. If there is no listener, do not perform one. | `templates/decision-ledger.md` (voice contract fields), E10 in `methodologies/04-prose-voice-originality.md`, E15 `methodologies/02-character-and-dialogue.md` |
| Named references 47% vs 24%; balanced mix 37% vs 16% | Specificity is a reality-effect: real works, places and brands anchor the fictional world. Constraint: only where the world permits it, and only when the reference does work. | `references/genre-and-form.md`, E8 `methodologies/03-time-and-scene.md` |
| Moral ambivalence 59% vs 38% | The protagonist's choice must remain defensible from at least two positions at the end; if one side is clearly correct, the conflict was administered, not dramatised. | E4 `methodologies/02-character-and-dialogue.md`, `references/character-intelligence.md` |
| Character introduction by external description 52% vs 30% | Introduce through pressure, not portrait: the first appearance should show a want meeting an obstacle. | E3 `methodologies/02-character-and-dialogue.md`, workflow 7 `workflows/03-scene-and-ensemble.md` |
| Rarity percentile 0.71 vs 0.49; 24.7% vs 7.1% in the rarest decile | Diversity is managed at portfolio level: track the combination of decisions across pieces, forbid repeating the same spine configuration twice. | E12 `methodologies/04-prose-voice-originality.md`, `references/originality.md`, `templates/decision-ledger.md` |
| LAMP drop 1.6 points | Revision order: structure → scene → paragraph → line. Line polish cannot move a structural default. | E14 `methodologies/05-continuity-and-revision.md`, `references/editorial-intelligence.md`, workflow 11 |
| 30 core features at 84.8% | A short diagnostic checklist beats a long one; the review should ask ~30 questions, not 300. | `checklists/`, `references/literary-critique.md` |
| Per-model fingerprints | When drafting with a specific model, know its house defaults and check exactly those. | `references/ai-narrative-signature.md` (per-model table, marked as version-specific) |

## Engineering hypotheses (not proven by this paper)

`[hypothesis]` Each is a bet Narraith makes that StoryScope does not test. Each has a test that could kill it.

1. **Subplot intersection beats subplot addition.** Mandating one subplot that carries its own dramatic question and intersects the spine twice raises blind-rated quality; mandating "add a subplot" without intersection does not. *Test:* 20 drafts, three arms (no subplot instruction / generic subplot / intersecting subplot), blind pairwise preference by ≥5 raters. Killed if the intersecting arm is not preferred over generic.
2. **Theme transfer beats theme deletion.** Rewriting a narrator's thesis statement into a consequence the protagonist pays for preserves reader comprehension while reducing perceived didacticism. *Test:* same story in three versions (stated / deleted / transferred), measure theme-identification accuracy and rated didacticism. Killed if transfer loses comprehension or does not reduce didacticism.
3. **Channel-by-function beats channel-by-dogma.** A rule that picks naming / embodiment / behaviour by scene function outperforms both "always embody" and "always name". *Test:* three rewrites of one scene by ≥8 writers, blind rating of emotional accuracy and freshness. Killed if blanket embodiment wins.
4. **Rarity is a portfolio variable, not a per-story target.** Pushing a single story toward the rare tail increases surprise but decreases coherence non-monotonically. *Test:* generate 30 stories at low/mid/high target rarity, rate coherence and surprise; expect an inverted U. Killed if coherence is flat.
5. **The subplot gap is partly a prompt artifact.** Re-running the comparison with prompts that explicitly seed a second line shrinks the 79/57 gap substantially. *Test:* small replication, 100 prompts × 2 conditions × 3 models, same feature definition as #17. Killed if the gap is stable under seeded subplots.
6. **Fingerprints do not survive version drift or translation.** Per-model signatures measured on English 2026 versions disappear or re-sort on later versions and on Russian drafts. *Test:* re-assign the top fingerprint features to 50 new drafts per model in both languages; measure whether the uniqueness ratio holds. Killed if signatures are stable — in which case they can be promoted from caution to diagnostic.
7. **The 30-feature checklist predicts editorial judgement.** Human editors independently flagging "AI-ish" passages converge on the same 30 decisions. *Test:* 15 editors, 30 stories, compare their free-text complaints against checklist hits. Killed if overlap is near chance — which would mean our checklist is measuring the paper's taxonomy rather than craft.

## Verbatim anchors

1. "AI spells out meaning rather than trusting the reader to infer it." (§4.1)
2. "Its stories are defined by restraint: event intensity escalates less than in any other source, and narrative voice is the most uniform." (§5, Claude)
3. "AI writes as though no one is watching." (§4.1)
4. "the human-AI boundary lives in a compact subset of narrative decisions" (§4)
5. "Because these features reflect structural decisions rather than lexical ones, they may prove more durable" (§1)
6. "altering them requires significant structural rewrites" (§7)
7. "Narrative features alone recover 97% of the combined model's macro-F1." (§4)
8. "the five AI models occupy a tight cluster that is well-separated from human stories" (§1)
9. "editing out clichéd phrasing or purple prose does not alter the structural narrative choices" (§4.2)
10. "the question of what constitutes original work shifts from how a story is written to how it is conceived" (§1)

## How we would know this dossier was misapplied

1. **It becomes a rubric with thresholds.** Any sentence of the form "fewer than two time jumps = AI-like" is a misreading. The paper reports means over thousands of stories with heavy overlap; it never sets a per-story cut-off.
2. **Inverted snobbery.** Drafts acquire epigraphs, named references, fourth-wall asides, unresolved endings and multiple subplots *because* those are human-leaning. That optimises a statistic, not a story, and produces a new tell.
3. **The numbers are quoted as quality claims.** "93.2%" appears in a document as evidence that our method produces good prose. It is a detection result. Nothing in the paper measures whether anyone enjoyed the story.
4. **The checklist is applied to sentences.** These are discourse-level variables (who resolves, what is revealed when, whether a second line exists). Used at the line level — "vary sentence length, add olfactory detail" — they reproduce L3 decoration and make the prose worse.
5. **Short-story norms are pushed onto novels.** A 90k-word novel is not a 5k-word story with more scenes; subplot economy, temporal architecture and intertextual density scale differently, and the prompt-artifact critique applies even more strongly there.
6. **Model fingerprints are treated as permanent.** A document says "GPT gossips, Claude is flat" without a date and version stamp. Within one model generation this is folklore, not evidence.
