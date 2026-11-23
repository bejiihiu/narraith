# Every Model Leaves a Trace — what survives a rewrite

> Purpose: extract the durability hierarchy from multi-resolution LLM fingerprinting and turn it into rules for how much evidence a prose judgment needs.
> When to read: before writing or auditing any rule that infers voice, style, or authorship from surface features, and before grading voice from a short sample.
> Related: `references/quality-levels.md` — the L1–L7 grid gets its durability ordering here; `references/editorial-intelligence.md` — the paraphrase-survival test; `references/literary-critique.md` — the evidence-sufficiency gate; `references/russian-prose.md` — why English-calibrated style thresholds do not carry over.

Tags: `[data: Fingerprinting]` = measured in Modarres et al.; `[theory]` = craft or narratology; `[hypothesis]` = our engineering inference, including every sufficiency threshold.

## Contents

1. Bibliographic record
2. Research question
3. Methodology
4. Results
5. The central lesson for us
6. Limitations
7. What transfers, and what does not
8. Idea → capability map
9. Evidence sufficiency table
10. Engineering hypotheses
11. Verbatim anchors
12. Misapplication risks

## Bibliographic record

- **Authors:** Mohammad Reza Modarres\*, Armin Tourajmehr\*, Artin Tavasoli, Yadollah Yaghoobzadeh†, Mohammad Taher Pilehvar† (\* equal contribution, † corresponding).
- **Affiliations:** School of Electrical and Computer Engineering, University of Tehran; Tehran Institute for Advanced Studies, Khatam University; Cardiff University.
- **Title:** "Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting."
- **Identifier:** arXiv:2610.28434v1 [cs.CL], 20 October 2026. Preprint.
- **Artifacts:** prompt sets, more than 15,000 generations from over 19 models, and the generation/feature/classifier code, announced at `anonymous.4open.science/r/Fingerprint-Resolution`.
- **Field:** passive source attribution of machine-generated text, framed as a closed-set classification problem with `K` candidate generators.
- **What it is not:** not a study of prose quality, not a fiction-specific study, not a natively-authored multilingual study. Every number below is about *recovering model identity*, not about whether text is good.

## Research question

The paper replaces the usual single accuracy score with a two-axis account of *fingerprint resolution*. Verbatim, from §1:

> "Model resolution describes how attribution changes as candidate generators become more similar, from different families to within-family models, distilled descendants, and controlled LoRA adaptations."

> "Signal resolution describes which behavioural, stylometric, lexical, and semantic signals carry model identity and whether they survive as observable cues are reduced."

And the reason the two axes are separated at all:

> "Together, these complementary axes distinguish the existence of a fingerprint from the conditions under which it remains detectable."

**Axis 1 — model resolution (how similar the candidates are).** Four rungs: cross-family (8 distinct families), within-family (same family, different size or generation), distillation (teacher vs. its distilled student), controlled LoRA adaptation (same base weights, varying strength of one learned update). The design intent is explicit: performance differences should reflect candidate similarity, since the protocol is held fixed.

**Axis 2 — signal resolution (where the evidence lives).** Four families ordered from surface to meaning: behavioural/structural (length, layout, Markdown, punctuation, repetition), stylometric (vocabulary diversity, word-form statistics, function words, POS), lexical (word and character n-grams), semantic (frozen sentence embeddings).

The framing that matters for us, from §2:

> "passive attribution from ordinary model outputs and ask how much identifying information remains when text is shortened, reformatted, partly rewritten, or paraphrased."

Attribution here is a *measuring instrument*, not a product. §1: "We use model attribution as a diagnostic tool rather than treat accuracy as the endpoint." That is the only reason this paper belongs in a writing skill at all — it measures the durability of text properties, and durability is a property we care about.

## Methodology

### Candidate models

19 models across 8 families, plus extra models for the distillation and LoRA settings (§3.1, Appendix A.1). Cross-family representatives: Llama-4 Maverick, Qwen-3 32B, Mistral-Small-3.2 24B, Gemma-4 31B, DeepSeek-V4 Flash-0731, Claude Haiku 4.5, Gemini-2.5 Flash, GPT-4.1. Selection rule is fixed: newest release per family, or largest general-purpose instruct model within a release.

Within-family comparisons: six Llama pairs, three Qwen pairs, one pair each for DeepSeek, Gemma, Mistral, Anthropic, Gemini, OpenAI.

Three teacher–student pairs: Llama-3.1 8B → Llama-3.1-Minitron 4B; Mistral-NeMo 12B → Mistral-NeMo-Minitron 8B; Gemma-2 27B → Gemma-2 2B.

Controlled adaptation: Llama-3.1-8B-Instruct and Qwen3-8B, each LoRA-tuned on GSM8K and on MATH (1,200 examples per setting; rank `r = 16`, scaling 32, dropout 0.05, one epoch). The adapter contribution is then scaled at inference: `W_α = W_0 + α·ΔW_LoRA` with `α ∈ {0, .05, .10, .20, .40, .60, .80, 1.0}`. This yields two questions per model: *vs base* (does adaptation change the fingerprint at all?) and *vs previous* (can neighbouring strengths be told apart?).

### Prompts and generation

Four English prompt sets, 200 prompts each before filtering, 799 after removing one near-duplicate (§3.4). D1 and D2 are independent samples from INFINITY-CHAT; D3 is a researcher-designed control set with 40 prompts in each of five task categories (explanation, argument/advice, creative writing, rewriting, source synthesis); D4 is a separate general-prompt source. Generation at temperature 1.0, top-p 0.9, max 2,048 tokens; roughly 95% of responses exceed 50 words.

Multilingual extension: the English prompts are machine-translated into Persian and Mandarin Chinese with GPT-4o-mini, then used with the same decoding configuration. 798 prompts, five prompt-disjoint folds.

### The four signal families, concretely

**Behavioural/structural — 25 features.** Word count, character count, sentence count, paragraph count, mean sentence-span length, SD of sentence-span length; Markdown heading count, bullet/list count, code-fence count, newline count, newline-to-character ratio, counts of `#`, `*`, hyphens, underscores, backticks; counts of commas, periods, exclamation marks, question marks, colons, semicolons, quotation marks; repeated-bigram and repeated-trigram ratios.

**Stylometric — 17 dense features plus POS.** Token count, unique-token count, type–token ratio, MATTR-10, MATTR-50; mean and SD of word length; hapax ratio, most-common-word frequency ratio; function-word ratio, pronoun ratio, modal ratio, connective ratio; unigram/bigram/trigram repetition ratios; numeric-token ratio. Concatenated with POS unigram, bigram, and trigram TF–IDF (spaCy `en_core_web_sm`, min df 2, at most 2,500 features). MATTR is the mean type–token ratio over sliding windows of 10 or 50 tokens; the 50-token window is why short texts get an unreliable diversity estimate.

**Lexical — TF–IDF, up to 10,000 dimensions.** Lowercase word unigrams and bigrams (≤5,000 features) plus lowercase character 3–5-grams (≤5,000 features), min df 2, sublinear term frequency.

**Semantic — one frozen vector per response.** `openai/text-embedding-3-small`, 1,536 dimensions, recomputed after every transformation (embeddings of the raw text are never reused).

**Combined** concatenates the four groups. **PN Embedding** (prompt-neutralized) subtracts, per prompt and per view, the mean embedding across all candidate-model responses, then classifies the residual. It is deliberately excluded from Combined and is never described as deployable.

### Transformations

| View | Operation |
|---|---|
| T0 | raw response |
| T1 | crop: ≤10 words unchanged; 11–20 lose one word per side; 21–50 lose five per side; >50 lose fifteen per side |
| T2 | T1 + strip Markdown markers, link/image syntax, HTML tags, indentation, layout whitespace |
| T3 | T2 + NFKC, lowercase, remove punctuation, symbols, emoji, collapse whitespace |
| P1 | paraphrase roughly one third of eligible sentences, branching from T0 |
| P2 | paraphrase the full response, branching from T0 |
| P1\*, P2\* | T3 applied to P1 / P2 |

T2 keeps words and word order; T3 keeps lexical words, function words, numbers, and order, and destroys casing and punctuation. The paraphraser is `gpt-4o-mini-2024-07-18` at temperature 0, never sees the source-model identity, and is instructed to preserve facts, entities, numbers, qualifications, language, tone, and approximate length (85–115% of original words). Headings, structural fragments, and code are not paraphrase targets. Paraphrase selection is keyed to prompt identity, not to source label, so it cannot leak the answer.

### Classifiers and protocol

Logistic regression (L2, SAGA, `C ∈ {0.01, 0.1, 1, 10}` tuned on macro-F1) is the primary instrument; a one-hidden-layer MLP (256 units, ReLU, Adam, lr 1e-3, weight decay 1e-4, batch 128, ≤80 epochs, early stop 8) is the nonlinear check. Evaluation is five-fold, prompt-grouped, dataset-stratified: every response to the same prompt, across models and views, stays in one fold. Chance is 12.5% for the eight-way task, 50% for binary pairs. Neither classifier consistently wins, so the main text reports LR. Largest reported standard deviation: 3.2%.

### Text budgets

Exact windows of 50, 100, 200, 400 words, drawn from the beginning, centre, or end of a response, restricted to responses of at least 400 words so that the same items are compared across budgets (Appendix G). Full-response values in that analysis therefore do not match Table 2.

### Generalisation protocols

Cross-prompt: train on three of D1–D4, test on the held-out fourth. Cross-language: within-language attribution in EN/FA/ZH, then all six directed language transfers at T0, plus the full transformation ladder averaged over directions. Lexical features are excluded from cross-lingual experiments outright, because "word- and character-level lexical features are strongly tied to language and script" (§5.3), and TF–IDF vocabulary is "intrinsically tied to language and script" (Appendix J).

## Results

### Accuracy by signal family (cross-family, 8-way, LR, chance 12.5%)

| View | Behavioural | Stylometric | Lexical | Semantic | Combined | PN Emb. |
|---|---|---|---|---|---|---|
| T0 raw | 52.42 | 60.72 | **80.07** | 66.04 | 81.41 | 83.75 |
| T1 crop | 48.78 | 58.93 | 76.27 | 60.81 | 76.14 | 76.13 |
| T2 −format | 41.88 | 56.34 | 72.48 | 56.23 | 71.86 | 74.42 |
| T3 −case/punct | 25.59 | 49.62 | 67.76 | 50.94 | 67.04 | 69.35 |
| P1 partial para | 50.86 | 58.20 | 74.42 | 63.69 | 77.85 | 80.90 |
| P2 full para | 48.12 | 53.32 | 68.18 | 57.81 | 71.86 | 75.23 |
| P1\* | 24.48 | 46.51 | 61.01 | 47.51 | 61.47 | 64.99 |
| P2\* | 23.08 | 41.79 | **53.94** | 41.90 | 55.87 | 59.39 |

(Table 2. All values are percentages. MLP results in Appendix B sit within roughly 1–9 points of these, preserve the ordering, and leave lexical nearly unchanged.)

Four readings, each load-bearing:

1. **Formatting removal is the single steepest cliff for behavioural features.** 48.78 → 41.88 at T2 (Markdown stripped) → 25.59 at T3 (casing and punctuation gone). Nearly half of the T0 behavioural accuracy is gone by T3, and the biggest single step is the last one: what survives T2 is mostly casing, punctuation counts, and whitespace habits, not language.
2. **Lexical is the strongest single family on raw and surface-normalized text**, at 80.07 / 76.27 / 72.48 / 67.76 — and it overtakes Combined under T1–T3. Word choice survives what formatting does not.
3. **Paraphrase hurts most where the signal was most lexical.** T0 → P2 costs lexical 11.9 points, combined 9.6, semantic 8.2, stylometric 7.4, behavioural 4.3. In relative terms the losses are much more alike — 8% to 15% — which is why the ranking is set by the starting ceiling, not by the slope.
4. **Nothing goes to chance.** Even P2\* (full rewrite *and* full surface scrub) leaves every representation above 12.5%, with Combined at 55.87%. The residual is real, but it is a residual.

### Within-family, distillation, LoRA

Within-family Llama pairs are binary tasks (chance 50%), and accuracy falls into a narrow band (Table 3): Combined 61.39–72.09, Lexical 59.01–69.02, Behavioural 55.38–60.45, Semantic 55.38–60.51, PN 63.33–76.35. The authors' reading is that within-family identity "relies on several weak but complementary signals rather than a single dominant fingerprint" (§4). Pairwise difficulty is not a function of parameter count: generation gaps are often easier to detect than size gaps.

Teacher–student pairs are *more* separable, not less (Table 4, chance 50%):

| Pair | Behavioural | Stylometric | Lexical | Semantic | Combined | PN Emb. |
|---|---|---|---|---|---|---|
| Llama 8B → Minitron 4B | 66.67 | 69.49 | 71.24 | 70.68 | 74.56 | 80.58 |
| Mistral 12B → Minitron 8B | 99.31 | 99.44 | 99.12 | 99.62 | 99.62 | 99.87 |
| Gemma 27B → Gemma 2B | 69.92 | 67.98 | 69.80 | 72.74 | 77.94 | 88.47 |

Shared lineage does not imply a shared fingerprint: distillation leaves a strong trace, and the Mistral pair is nearly perfectly separable at every signal family.

LoRA (Figure 2, Combined LR, chance 50%) gives the sharpest result in the paper. Separation from the base rises monotonically with adapter strength for all four settings, while neighbouring variants stay at chance for Llama and only partially separate for Qwen:

| Setting | α=.05 | .10 | .20 | .40 | .60 | .80 | 1.0 |
|---|---|---|---|---|---|---|---|
| Llama GSM8K, vs base | 51.6 | 54.1 | 59.6 | 63.6 | 72.0 | 77.7 | 83.4 |
| Llama GSM8K, vs previous | 51.6 | 53.3 | 53.3 | 52.9 | 55.3 | 55.8 | 55.9 |
| Llama MATH, vs base | 52.2 | 52.3 | 54.3 | 57.3 | 61.0 | 62.6 | 66.8 |
| Qwen GSM8K, vs base | 51.1 | 53.3 | 57.4 | 74.1 | 83.9 | 90.1 | 93.5 |
| Qwen GSM8K, vs previous | 51.1 | 51.4 | 52.8 | 66.1 | 66.2 | 62.7 | 58.1 |
| Qwen MATH, vs base | 51.0 | 51.1 | 58.9 | 80.6 | 88.3 | 91.1 | 91.7 |

Averaged over datasets and strengths (Table 20): Llama vs base 58.37–60.20, vs previous 51.07–52.52; Qwen vs base 68.44–70.46, vs previous 55.35–56.56. So a real weight change can be unmistakable against the base and still invisible between two adjacent strengths. Detectability is not linear in the size of the underlying change.

### How much text is needed

Figure 3, the P2\* condition (paraphrased *and* surface-scrubbed), against 12.5% chance:

- 50 words: ≈22% for beginning and centre, ≈27% for the ending.
- Accuracy rises steadily with budget and reaches ≈50% at the full response.
- The ending is the most informative region at every limited budget.

Numbers for the 100/200/400-word points are **not reported** — the figure is the only source, and the authors give no values for them. The T0 and T3 versions of the same analysis (Appendix G, Figure 4) are reported as figures only, with no numbers at all.

### Cross-prompt transfer

Leave-one-dataset-out (Table 5a): 84.19 (→D1), 81.41 (→D2), 68.63 (→D3), 67.88 (→D4); mean 75.52. Holding out the target dataset costs only 4.8–5.9 points relative to mixed-source evaluation (Table 22: Combined 81.41 → 75.52 at T0; 67.04 → 62.25 at T3; 55.87 → 51.10 at P2\*), whereas the transformations themselves cost far more. Distribution shift is a smaller perturbation than rewriting.

The task effect is much larger than the dataset effect (Table 5b, D3, chance 12.5%): explanation 84.69, argument/advice 95.31, creative 87.81, **rewrite 35.94, source synthesis 39.38**; overall 68.63. Per-model recall in Table 21 ranges from 12.50 to 100.00 within the same task, so this is not a uniform effect either.

The explanation the authors give is the one worth stealing: constrained tasks

> "constrain more of the response content and structure, leaving less room for model-specific variation."

### Cross-language

Within-language (Tables 24, 25; 8-way, chance 12.5%): Persian T0 — Lexical 86.98, Combined 86.40, Semantic 69.60, Stylometric 57.69, Behavioural 51.60. Chinese T0 — Lexical 83.79, Combined 83.62, Semantic 68.48, Stylometric 59.01, Behavioural 54.57. Both exceed English at T0 for lexical and combined. At P2\* both still hold: Persian 66.53 combined, Chinese 67.27.

Cross-lingual transfer (Table 6, T0, lexical excluded by design):

| Direction | Behavioural | Stylometric | Semantic | Combined | PN Emb. |
|---|---|---|---|---|---|
| EN → FA | 34.54 | 15.38 | 32.63 | 34.82 | 44.75 |
| EN → ZH | 35.01 | 16.76 | 40.23 | 39.00 | 59.10 |
| FA → EN | 21.77 | 21.04 | 16.81 | 19.67 | 47.99 |
| FA → ZH | 26.39 | 21.98 | 24.40 | 34.76 | 55.78 |
| ZH → EN | 27.30 | 20.68 | 30.03 | 36.39 | 59.46 |
| ZH → FA | 32.86 | 22.62 | 39.36 | 35.53 | 51.07 |

Averaged over all six directions (Table 26, chance 12.5%): T0 — Behavioural 29.65, Stylometric 19.74, Semantic 30.58, Combined 33.36, best deployable 34.56, PN 53.03. At P2\*: Behavioural 17.54, Stylometric 18.09, Semantic 23.26, Combined 23.08, best deployable 24.48, PN 36.64.

That table is the core of the paper's multilingual claim, and it is more specific than the abstract's summary. **Stylometric transfer sits at 15–23%, i.e. barely above chance in most directions** — English-trained POS and function-word statistics simply do not describe Persian or Chinese. The authors themselves warn that "some Stylometric components, including the English-trained POS representation, are not linguistically calibrated for Persian or Chinese" and treat those numbers as a fixed-feature diagnostic rather than as evidence about language-general structure (Appendix J). Semantic (30.58) and behavioural (29.65) transfer comparably; the semantic advantage is clearest against stylometric, not against behavioural. PN embedding lands well above every deployable representation (53.03 vs 34.56), which mostly tells us how much of the raw embedding was prompt rather than model.

### The PN-embedding diagnostic

Centring by prompt mean raises embedding attribution on D3 from 50.50% to 74.88% (Table 23; Appendix H.1). On the two most constrained tasks it beats the strongest standard representation by 12.81 points (rewrite) and 13.75 (source synthesis). It is the highest column in Table 2 at every view, 83.75 at T0 and 59.39 at P2\*.

Its cost is structural, not computational: it requires responses from *all* candidate models to the *same* prompt. §3.2 states the requirement plainly — it "requires peer responses from all candidate models for the same test prompt" — and the limitations repeat that it "is therefore not applicable to standard single-response attribution." It is a way of measuring how much of the signal was shared context, not a classifier anyone can ship.

## The central lesson for us

The paper measures **durability under transformation**, not importance. Ranked by what survives, on the numbers above:

1. **Surface formatting dies first.** Behavioural features lose 26.83 points from T0 to T3, and the T2→T3 step alone costs 16.29. Strip Markdown, casing, and punctuation, and half of what looked like a signature is gone.
2. **Stylometry is the weakest cross-linguistically and the second-weakest under paraphrase.** It falls to 41.79 under P2\* and to 19.74 averaged cross-lingual — a 41-point collapse from its within-English ceiling of 60.72. Function-word ratios and POS distributions are a description of a language as much as of a writer.
3. **Lexical n-grams are the most accurate single family and the most language-bound.** 80.07 at T0, still 67.76 after total surface scrubbing, 53.94 after full paraphrase — but the authors will not even test them across scripts, because "word- and character-level lexical features are strongly tied to language and script."
4. **Semantic representation is the most portable.** 30.58 averaged cross-lingual versus 19.74 for stylometry, and the only family whose cross-lingual accuracy stays in the same neighbourhood as its behavioural competitor while carrying content rather than layout.

Note the honest caveat the paper supplies about its own semantic column: the embedding "can also retain lexical, stylistic, and structural signals," which is exactly why Semantic drops from 66.04 to 41.90 across the transformations. "Semantic" is a label for the representation's purpose, not a guarantee of content purity.

**The instruction this yields for a writing skill: do not build your quality model on surface tells.** A judgment that dissolves when the passage is rewritten with the same meaning was never a judgment about the passage's meaning. Build the model on what survives a meaning-preserving rewrite — causal structure, informational order, whose want drives the scene, what the ending costs — because those are the properties the text cannot lose without becoming a different text.

**But keep the asymmetry explicit.** Durability for attribution is not the same as importance for quality. The Mistral Small-24B / Small-3.2-24B pair is 94.37% separable on Combined and 98.75% on PN embedding — and nothing follows about which model writes better prose. In the other direction, a LoRA adapter at α = 0.05 is statistically indistinguishable from its base (51.6 vs base, 51.6 vs previous, chance 50) while being a genuinely different model. Detectability tracks *difference*, not *significance*. A skill that ranks features by how reliably they identify a source will rank them by the wrong criterion.

The correct use of the hierarchy is negative and cheap: it tells you which observations are *fragile evidence* and must therefore carry a confidence penalty, not which observations are *important*. A fragile signal can still be the whole voice — punctuation rhythm is exactly the kind of thing that vanishes under T3 and can still be the most deliberate decision in a paragraph.

## Limitations

- **Closed set.** Attribution assumes `K` known candidates. Real provenance involves unknown generators, and the authors say so: "real-world provenance may involve unknown or unseen generators." Every accuracy figure is therefore an upper bound on open-world usefulness.
- **Translated prompts, not natively authored ones.** Persian and Chinese prompts are GPT-4o-mini translations of the English set. The paper concedes this: non-English prompts were "translated from the English set rather than independently authored in each language." Translated prompts carry English task structure into the target language, so the multilingual results test *transfer of an English task*, not native composition.
- **Two base models, two adaptation datasets for LoRA.** GSM8K and MATH, Llama-3.1-8B and Qwen3-8B. Reasoning adaptations only; other adapter types and domains are untested by the authors' own admission.
- **The transformation suite is not human editing.** "Our transformation suite cannot capture the full range of human editing, rewriting, translation, and post-processing." A copy-editor's pass and a gpt-4o-mini paraphrase at temperature 0 are different operations, and the paper only tests the second.
- **Prompts are general-purpose, not fiction.** Creative writing is 40 of 200 prompts in one control set and is not analysed separately beyond Table 21's per-model recall. There is no study of narrative prose, dialogue, or literary form.
- **Semantic features need model access.** The semantic and PN columns require `text-embedding-3-small` and, for PN, peer responses. Neither is available inside a text-only skill.
- **English, Chinese, Persian only. No Russian.** Not a footnote gap but a total absence: no Cyrillic, no Slavic language, no case system, no aspect. Every stylometric threshold in the paper is calibrated on English POS tags via `en_core_web_sm`.

## What transfers, and what does not

### Transfers

**(a) Multi-layer diagnostic design with explicit resolution levels.** The paper's structural move — separate *how similar the candidates are* from *how much evidence survives* — is reusable as a design pattern for grading. Our L1–L7 grid already has levels; what it lacks is the second axis. Add it: every level gets a durability rating and an evidence requirement.

**(b) Paraphrasing as a stress test of meaning.** This is the most directly usable instrument in the paper. Rewrite a passage preserving meaning; whatever diagnosis changes was attached to wording, not to the thing. The paper's own numbers justify the test: at P2\*, lexical identification sheds a third of its raw accuracy while the residual structure still carries signal. The stable part is the load-bearing part.

**(c) Length-dependent confidence.** 50 words under P2\* yields ≈22–27% against 12.5% chance; the full response yields ≈50%. Evidence scales with text, and does so from a very low floor. `[hypothesis]` A 200-word sample therefore cannot support a confident verdict about voice — not as a stylistic preference, but as an arithmetic consequence of how little identifying structure a short span carries.

**(d) Cross-language caution.** The stylometric collapse from ~58–61% within English to 19.74% averaged cross-lingual is the cleanest available warning: a stylistic measurement built on one language's grammar does not describe another's. Do not port an English-derived function-word or POS threshold to Russian and call it analysis.

**(e) Constraint suppresses individuation.** Rewrite and source-synthesis tasks drop attribution to 35.94 and 39.38 while argument/advice sits at 95.31. When the form dictates the wording, the writer's (or model's) signature has nowhere to live. Corollary for us: fixed-form artifacts — a sonnet, a genre-template chapter, a mandated beat sheet — are the worst possible samples for a voice judgment, and that is a measurable effect, not an opinion.

### Does not transfer

- **We cannot compute any of these representations.** No TF–IDF over 10,000 dimensions, no POS tagging pipeline, no 1,536-dimension frozen embeddings, and no 19-model comparison panel. The feature lists are diagnostic vocabulary, not an implementation plan.
- **We are not attributing authorship.** Every number describes a closed-set classifier distinguishing models that were generated under one fixed decoding protocol. That task has nothing to do with deciding whether a human paragraph is good.
- **Fingerprint strength is not prose quality.** Restated because it is the easiest thing to get wrong: 99.62% separability between two Mistral models says the models differ, not that either writes well.
- **The PN-embedding result is not a technique for us.** It needs peer responses to the same prompt and is explicitly non-deployable. Cite it as evidence that prompt-shared variance is large, never as a method.

## Idea → capability map

| Idea | Narraith mechanism | File |
|---|---|---|
| Signals form a durability ladder from surface form to semantic structure; judgments must state which rung they rest on | L1–L7 grid annotated with a durability rating per level: L1/L2 lean on lexical-syntactic evidence (moderately durable, language-bound), L3 on stylometric evidence (fragile), L4–L7 on structural/semantic evidence (most portable). Each level carries the confidence penalty implied by its rung. | `references/quality-levels.md` |
| Meaning-preserving rewrite as a discriminator between load-bearing and decorative properties | Paraphrase-survival test: diagnose, rewrite preserving meaning, re-diagnose; any verdict that changes is demoted from structural to surface. Report the delta, not just the second verdict. | `references/editorial-intelligence.md` |
| Evidence scales with text; short samples carry a low ceiling | Evidence-sufficiency gate: refuse voice-level verdicts below a stated word budget; downgrade to "observation" with an explicit reason ("sample too short for L3"). A 200-word excerpt never receives a confident voice grade. | `references/literary-critique.md` |
| Stylometric measurements calibrated on one language do not describe another | Russian caveat: no function-word ratios, POS-distribution claims, or English-derived diversity thresholds applied to Russian text without a native calibration. Where a Russian-specific claim is unsupported, say so instead of translating the metric. | `references/russian-prose.md` |
| Constrained tasks suppress individuation | Gate on form: before a voice judgment, check whether the sample is a fixed-form artifact. If the form dictates the wording, the sample cannot support an L3 claim. | `references/literary-critique.md`, `references/quality-levels.md` |
| Detectability ≠ significance | In the critique output, separate "this is characteristic" from "this is a defect". A distinctive habit is not a flaw, and a statistically typical construction is not a virtue. | `references/editorial-intelligence.md` |

## Evidence sufficiency table

> `[hypothesis]` — the ordering is derived from the paper's length findings (50 words ≈ 22–27% under P2\*, full response ≈ 50%, chance 12.5%); the specific word budgets are our engineering judgement, not measured. Treat them as defaults to be revised against real grading sessions, not as findings.

| Level | Minimum text for a claim | What you may claim | What you may not claim |
|---|---|---|---|
| L1 Lexical | 1 sentence for "this word is vague"; ≥300 words for "this writer's diction" | Local word-choice defects, register slips, filler | A diction profile, a vocabulary signature |
| L2 Syntactic | ≥120 words (needs several sentences to establish a pattern) | Rhythm monotony, clause-stacking, sentence-length regularity | A syntax profile from one paragraph |
| L3 Stylistic / voice | ≥600–800 words, unparaphrased | Voice consistency, tonal drift, image density as a pattern | Voice from a fragment, voice from a paraphrase, voice from a fixed-form artifact |
| L4 Semantic | ≥400 words for a local claim; the whole work for a thematic claim | Subtext present/absent in a scene, whether meaning is stated or embedded | A whole-work theme from a chapter |
| L5 Narrative | The whole story, not a chapter | Causality, agency, scene-level state change | Plot-shape conclusions from an excerpt |
| L6–L7 Psychological / literary | The whole work plus context | Contradiction, cost, composition, originality | Anything from a sample |

Two derived rules, both `[hypothesis]`:

1. **A judgment that does not survive a paraphrase was a judgment about wording.** Demote it and say so in the output.
2. **Confidence is capped by sample size before it is capped by analysis quality.** A brilliant reading of 150 words is still a reading of 150 words.

## Engineering hypotheses

All marked `[hypothesis]`; each is falsifiable with a small, cheap experiment.

1. **Paraphrase-survival predicts diagnosis stability.** If a set of graded passages is rewritten by a meaning-preserving paraphraser, L4–L5 verdicts will agree with their pre-rewrite versions more often than L3 verdicts will. Measure: agreement rate by level over 30 passages. Falsified if L3 agreement ≥ L4 agreement.
2. **Short samples inflate voice confidence.** Judges given <200 words will produce L3 verdicts at the same rate as judges given 800+ words, but with lower inter-rater agreement. Measure: verdict rate and agreement across two length conditions on the same underlying texts. Falsified if short-sample agreement matches long-sample agreement.
3. **Fixed-form samples suppress detectable voice.** Two samples by the same author, one free-form and one heavily constrained (fixed metre, mandated beat structure), will yield lower stylometric distinctiveness in the constrained sample. Measure: within-author vs between-author distance in a simple surface-statistic space. Falsified if the constrained sample is *more* distinctive.
4. **English-derived stylistic thresholds misfire on Russian.** Function-word ratios and sentence-length distributions calibrated on English prose will classify Russian prose samples less reliably than Russian-calibrated equivalents. Measure: same classifier, two calibrations, held-out Russian texts. Falsified if the English calibration transfers without loss.
5. **Explicit durability labels reduce overclaiming.** Asking for a verdict plus its level and durability rung will reduce unsupported L3 claims on short samples compared with an unlabelled prompt. Measure: rate of unsupported voice claims across two prompt conditions. Falsified if labelling changes nothing.
6. **Structural questions survive translation better than stylistic ones.** The same scene, natively written in Russian and in English, will receive more consistent L4–L5 structural judgments than L1–L3 stylistic ones. Measure: cross-language agreement by level. Falsified if stylistic agreement is equal or higher.

## Verbatim anchors

1. "We use model attribution as a diagnostic tool rather than treat accuracy as the endpoint." — §1.
2. "Together, these complementary axes distinguish the existence of a fingerprint from the conditions under which it remains detectable." — §1.
3. "Even 50 words retain useful identifying information, with accuracy of approximately 22% for the beginning and centre and 27% for the ending." — §4, "How Much Evidence Is Needed?"
4. "Surface and behavioural signals are relatively fragile, lexical information remains strong after surface normalization, and combining signal types becomes more useful after paraphrasing." — §6, Conclusion.
5. "constrain more of the response content and structure, leaving less room for model-specific variation." — §5.1.
6. "Because word- and character-level lexical features are strongly tied to language and script, we exclude the Lexical representation from the cross-lingual transfer experiments." — §5.3.
7. "Our transformation suite cannot capture the full range of human editing, rewriting, translation, and post-processing." — Limitations.
8. "not as a definitive detector of AI-generated text or as a standalone basis for decisions about individuals." — Ethics Statement.

## Misapplication risks

1. **Reading the durability ranking as a quality ranking.** The most durable signal is not the most important one. Punctuation rhythm dies at T3 and can still be the most deliberate choice in a paragraph; a robust structural pattern can be a bad habit repeated. Durability tells you how much to *trust* an observation, never how much it *matters* — and by the same logic, a paraphrase that preserves meaning preserves the structural signal while destroying the stylistic one, so the two are never interchangeable inputs to a critique.
2. **Turning the feature lists into a checklist.** Twenty-five behavioural plus seventeen stylometric features look like an audit form. Applied as a checklist they become exactly the surface-tell scoring the paper's own results discredit — and they were built to identify a generator, not to evaluate prose.
3. **Citing accuracy numbers as if they were about writing.** 83.75% is an eight-way closed-set classification score over general-purpose prompts generated at temperature 1.0. It says nothing about fiction, nothing about quality, and nothing about a single unidentified text.
4. **Assuming cross-lingual semantic transfer licenses Russian grading.** The semantic advantage is 30.58 vs 19.74 against stylometry, in a setting where the "semantic" vector also retains lexical and structural information and where the prompts were translated from English. There is no Russian data at all. Using the paper to justify English-calibrated judgments on Russian prose inverts its own warning.
5. **Quoting PN embedding as a method.** It is the best column in every table and it is unusable: it needs peer responses from all candidate models to the same prompt. Citing it as an achievable technique is a straightforward misreading of §3.2 and the Limitations.
