# DetectGPT — Probability Curvature, and the Text the Model Would Write by Default
> Purpose: Extract the one transferable idea from a machine-text detector — that model output sits at a local maximum of the model's own distribution — and turn it into a craft protocol that requires no log-probabilities.
> Read when: Before building or auditing E11 (default-avoidance); when a draft is fluent and forgettable; when a turn feels either obvious or arbitrary; or when you are about to claim a passage is "low probability".
> Related: `methodologies/04-prose-voice-originality.md` — E11 owns the continuation test; `methodologies/01-plot-and-causality.md` — prepared surprise; `references/editorial-intelligence.md` — paraphrase survival in revision; `references/research/01-storyscope.md` — the measured AI narrative signature this idea helps explain.

## Bibliographic record

- Authors: Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn (Stanford University).
- Title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature."
- Venue: ICML 2023. arXiv:2301.11305v1 [cs.CL], 26 January 2023.
- PDF: https://arxiv.org/pdf/2301.11305 — project page: ericmitchell.ai/detectgpt
- Task: binary classification of a candidate passage `x` as a sample from a specific source model `pθ` or not.
- Setting: zero-shot. No detector training, no dataset of real/generated pairs, no watermark. White-box: the detector may evaluate `log pθ(x)`.
- Stated contributions: (a) empirical validation that the curvature of the log-probability function is more negative at model samples than at human text; (b) DetectGPT, an algorithm that approximates the trace of the Hessian of `log pθ` with respect to the sample `x`.
- What it is not: a quality metric, a theory of human writing, or a generation method. The paper measures *origin*, never merit.

## The claim

`[data: DetectGPT]` Text sampled from a language model tends to sit in regions of **negative curvature** of that model's log-probability function. Human-written text usually does not.

Define a **perturbation function** `q(·|x)`: a distribution over small rewrites of `x` that preserve its meaning. Then the **perturbation discrepancy** is

```
d(x, pθ, q) ≜ log pθ(x) − E_{x̃∼q(·|x)} log pθ(x̃)
```

the log-probability of the original passage minus the average log-probability of its meaning-preserving rewrites. The paper's formal hypothesis:

> Hypothesis 4.1. If `q` produces samples on the data manifold, `d(x, pθ, q)` is positive with high probability for samples `x ∼ pθ`. For human-written text, `d(x, pθ, q)` tends toward zero for all `x`.

Plain-language reading, which is the part a writer can actually use:

- Picture `log pθ` as a landscape over "all passages that mean roughly this thing". A model sample sits at a **local peak** of that landscape — by construction, because sampling from the model is how the text got there. Step to any neighbouring phrasing that means the same thing and you walk downhill. The average drop is large and positive.
- Human text normally sits on a **slope**. Some rewrites score a bit higher, some lower; the average lands near the original, so the discrepancy is near zero. Not because human prose is more "random", but because no single phrasing is the maximum of this particular model's distribution.
- Curvature is the shape of that peak. Negative curvature at a point means the point is a maximum: every direction leads down. The paper shows that `d` is proportional to the **negative trace of the Hessian of `log pθ` with respect to the sample** (not with respect to model parameters — the authors are explicit about the distinction). It reaches this via Hutchinson's trace estimator plus finite differences; with symmetric noise and step size `h = 1`, `−tr(H)f(x)/2 ≈ f(x) − E_z f(x+z)`, which is the discrepancy again.

The decision rule is a threshold on the **normalized** discrepancy: `(log pθ(x) − μ̃) / σ̃ > ε`, where `μ̃` and `σ̃` are the mean and standard deviation of `log pθ` over the `k` perturbed samples. Normalizing by that standard deviation "typically increas[es] AUROC by around 0.020", so every reported experiment uses the normalized form. There is nothing to implement here on our side: we are taking the *idea*, not the estimator.

One scope note that later sections depend on: the paper says it will "generally consider roughly paragraph-length texts `x`". Nothing in it licenses sentence-level claims.

## Methodology

`[data: DetectGPT]`

**Perturbation function.** Off-the-shelf mask-filling, not a fine-tuned paraphraser. Randomly sampled **2-word spans** are masked until **15%** of the words are masked, then filled by T5 at temperature 1. The 15% mask rate is borrowed from BERT masked-language-modeling practice. A small sweep over span lengths `{2, 5, 10}` on held-out XSum found 2 best; these settings were then fixed for all experiments, with no per-dataset tuning. Mask-fillers: **T5-3B** for almost everything, **T5-11B** for the GPT-NeoX and GPT-3 runs where compute allowed, **mT5-3B** for the multilingual WMT experiment.

**Why mask-filling and not random tokens.** The perturbation must stay on the data manifold — must produce sentences a human would accept as the same meaning. Figure 7 shows random mask-filling (uniform sampling from the filler's vocabulary) performs poorly across every source-model scale, while larger mask-filling models perform better. The authors read this as evidence that the method estimates curvature in a *latent semantic* space, not in raw token space: a bigger T5 represents that space better, so its random directions correspond to meaningful edits.

**What the 2-word span buys.** Masking short spans and refilling them produces *local* variation: a verb swapped for a synonym, a phrase replaced by an equivalent, a redundant connector dropped. That is the right resolution for the question "is this exact string the peak?", because a larger span would change what the passage says rather than how it says it, and the curvature estimate would then be measuring content difference, not phrasing preference. `[theory]` The craft analogue is exact: when you test a passage against alternatives, hold the *meaning* fixed and vary the *execution*. If your alternatives change what happens, you are testing the plot, not the prose, and you need a different pass.

**Number of perturbations.** The expectation in `d` is approximated with **100 T5 samples** in the main experiments. Number of perturbations is the accuracy/speed dial: Figure 8 shows detection accuracy rising and then **converging at 100**; evaluations there use 100 examples per dataset and fills from T5-large. Fewer perturbations cost less and lose accuracy; past 100 the reported curves flatten.

**Data.** Six datasets, chosen to span LLM use-cases:

| Dataset | Role in the paper |
|---|---|
| XSum (news articles) | fake-news detection |
| SQuAD contexts (Wikipedia paragraphs) | machine-written academic/expository text |
| WritingPrompts (Reddit, prompted stories) | machine-generated creative writing |
| WMT16 English and German | robustness to distribution shift / language |
| PubMedQA (long-form expert answers) | scientific writing, out-of-distribution |

Machine text is generated by prompting each model with the **first 30 tokens** of the real text (question tokens only, for PubMedQA), sampling from the raw conditional distribution at temperature 1 unless stated otherwise. Each experiment uses **150–500 examples**, with equal numbers of positive and negative examples. The hypothesis check in Figure 3 uses **500 XSum articles** and four models.

**Models.** GPT-2 (1.5B), OPT-2.7B, GPT-Neo-2.7B, GPT-J (6B), GPT-NeoX (20B) in the main table; GPT-3 (175B) via the paid API in a separate comparison, restricted to 150 examples because of API cost.

**Baselines.** Four zero-shot criteria built from the source model's token distributions: mean token log-probability (`log p(x)`), mean token rank, mean log-rank, and mean predictive entropy. Plus two supervised RoBERTa detectors (base and large) fine-tuned on millions of GPT-2 samples, as an out-of-family reference.

**Metrics.** AUROC — the probability that the detector ranks a randomly chosen machine sample above a randomly chosen human sample. Figure 8 also reports AUPR. Both are threshold-free ranking measures; a threshold `ε` is only needed to emit a decision.

**Compute.** No wall-clock or FLOP figures are reported. The cost is structural and the authors name it: for each candidate passage the method must **sample `k` perturbations and score `k+1` texts**, not one. They call DetectGPT "more compute-intensive than other methods for detection", and note that even where an API exposes probabilities (GPT-3), scoring them "costs money".

## Results

`[data: DetectGPT]` Headline, from the abstract: detecting fake-news articles generated by **20B GPT-NeoX** rises from **0.81 AUROC for the strongest zero-shot baseline to 0.95 AUROC** for DetectGPT. The 0.81 is log-rank thresholding.

Before any of the detection numbers, the paper validates the hypothesis itself (Figure 3). Five hundred XSum articles, machine text from four models, discrepancy estimated with 100 T5-3B samples: the distribution of `d` is shifted right for model samples at every model size, and the range of observed discrepancies widens as the model grows. The two distributions are not disjoint, though — they overlap, and the method only separates them in aggregate. That is why AUROC is the right metric and why no single passage can be classified by eye: the claim is about where a *population* of texts sits, not about a tell you can point at in one paragraph.

Table 1 averages across five source models, with the 20B column broken out because that is where the effect is largest and where it also breaks:

| Dataset (proxy) | Best baseline avg (LogRank) | DetectGPT avg | Δ avg | NeoX baseline | NeoX DetectGPT | Δ NeoX |
|---|---|---|---|---|---|---|
| XSum (fake news) | 0.87 | 0.97 | +0.10 | 0.81 | 0.95 | **+0.14** |
| SQuAD (Wikipedia / expository) | 0.87 | 0.92 | +0.05 | 0.76 | 0.79 | +0.03 |
| WritingPrompts (fiction) | 0.96 | 0.97 | +0.01 | 0.95 | 0.93 | **−0.02** |

Per model, on XSum, against the log-rank baseline:

| Source model | LogRank | DetectGPT | Δ |
|---|---|---|---|
| GPT-2 (1.5B) | 0.89 | 0.99 | +0.10 |
| OPT-2.7B | 0.88 | 0.97 | +0.09 |
| GPT-Neo-2.7B | 0.90 | 0.99 | +0.09 |
| GPT-J (6B) | 0.86 | 0.97 | +0.11 |
| GPT-NeoX (20B) | 0.81 | 0.95 | +0.14 |

Two things to read off that table. The baseline weakens at the top: 0.89 for GPT-2 against 0.81 for GPT-NeoX-20B, the weakest baseline in the row. And DetectGPT's margin is widest at that same top end (+0.14 against +0.09–0.11 for the smaller models). `[theory]` For a writer this is the useful direction of the result: the bigger and more fluent the generator, the more its default output is a recognisable *shape* rather than a collection of surface tics. The tell moves from the word to the choice.

Other results that matter:

- DetectGPT is best in **14 of 15** dataset–model combinations, with a **0.06 AUROC** average improvement. The single loss is WritingPrompts with GPT-NeoX, where log-rank wins 0.95 to 0.93.
- The improvement is largest where the text is most "typical": **+0.10** average on XSum news. On fiction the margin nearly vanishes (**+0.01**), and the paper's own explanation is a footnote worth memorising: "machine-generated creative writing tends to be noticeably generic, and therefore relatively easy to detect". Every method scores high there — the task got easy, not the method strong.
- Against GPT-3 (175B), DetectGPT averages **0.85** across PubMedQA / XSum / WritingPrompts, level with the RoBERTa-large supervised detector (**0.85**) and ahead of likelihood thresholding (**0.76**). On PubMedQA it is 0.84 versus 0.71 for RoBERTa-large and 0.64 for `log p(x)`.
- Against supervised detectors under distribution shift (Figure 4, 200 samples each): on in-distribution English news the supervised models are comparable or better; on German WMT16 the RoBERTa detectors collapse (0.394 and 0.537) while DetectGPT holds at **0.962**. Zero-shot generalises; the trained detector overfits its training distribution.
- Revised text (Figure 5): DetectGPT stays **above 0.8 AUROC even when nearly a quarter of the model text has been replaced** with T5-generated spans. All methods degrade with heavier revision; DetectGPT is highest at every revision level.
- Decoding (Table 3, averaged over five models, `k = 40`, `p = 0.96`): both truncation schemes make detection easier. DetectGPT: XSum 0.98 top-p / 0.98 top-k; SQuAD 0.94 / 0.93; WritingPrompts 0.98 / 0.97. The appendix explains the *why* in one clause — top-k narrows the gap "presumably because top-k generations are more generic". Truncated sampling moves text closer to the mode.
- Cross-model scoring (Figure 6, nine source/scorer combinations): performance is best on the diagonal, where the scorer is the generator. Off-diagonal it degrades. Some models are better scorers than others (GPT-2 and GPT-Neo-2.7 beat GPT-J), which the authors suggest points toward ensembling.
- Mask-filler scale (Figure 7): there is "a clear association between capacity of mask-filling model and detection performance", tested at 60M → 220M → 770M → 2.7B parameters, across source-model scales and at both 5 and 25 perturbations. Random mask-filling does not show this association — it performs poorly throughout.

**Where it fails, concretely.** SQuAD with GPT-NeoX is 0.79 — barely above its 0.76 baseline and the weakest cell with a positive delta. WritingPrompts with GPT-NeoX is the one outright loss. PubMedQA is the weakest domain overall and the authors attribute the drop to "lower quality perturbations" — the mask-filler does not represent biomedical rephrasings well. Outside the white-box setting the signal weakens. And none of this is a statement about prose quality in any direction.

## Why this matters conceptually

`[data: DetectGPT]` The detection result is a side effect. The finding is a fact about the **generator**: a text sitting at a local maximum of the model's distribution is, almost tautologically, the text that model would produce by default. Sampling put it there. Any meaning-preserving step away from it goes downhill.

`[data: DetectGPT]` The paper states the consequence better than any paraphrase: if rephrasings are systematically lower-probability, "the model is exposing its bias toward the specific (and roughly arbitrary, by human standards) phrasing used." And: "LLMs that do not perfectly imitate human writing essentially watermark themselves implicitly."

That is the whole craft argument in two sentences. The machine's preferred phrasing is not better phrasing — it is *arbitrary but specific*. Arbitrary because a human would accept several equivalents; specific because the model prefers exactly one. The preference is a fingerprint, not a judgement.

**Fluency and predictability are different properties.** Fluency is local: these words follow those words plausibly. Predictability is relational: this passage is the high-probability continuation *for this model*. A sentence can be maximally fluent and maximally predictable at once — that is the normal case, not the pathological one. So "this reads well" is not evidence against "this is the default". It is often evidence *for* it.

**The trap.** An instruction like "make it sound like good literary prose" is a similarity criterion, and the model's only operational model of "good literary prose" is the region of its own distribution where such prose lives. Optimising for resemblance pushes the text toward the modal continuation — the peak. The result is competent, frictionless, and forgettable: every sentence is the sentence the model would have written, which is exactly the property DetectGPT measures. The failure is not bad writing. It is writing with no decision in it.

`[data: DetectGPT]` Worth being precise about what "default" means here, because it is not greedy decoding. The main experiments sample "from the raw conditional distribution with temperature 1" — the ordinary, unforced way a model writes. And when sampling is truncated (top-k, top-p), detection gets *easier*, because truncation raises the average log-likelihood of generations by cutting low-probability tokens. So the tell is strongest under the settings that feel most "natural" to a user. `[theory]` The peak is not an artefact of a degenerate decoding mode you can configure away. It is where ordinary sampling lives.

`[theory]` The correction is not "be weird". It is to replace the similarity criterion with a *function* criterion: what must this passage do to this scene, and is the default phrasing the best available instrument for that job? Usually it is not, because the default was selected for typicality, not for this scene.

**High probability is not quality.** The paper never measures quality, and the correlation between "human-authored" and "good" in its data is an artefact of what humans chose to publish, not a law. A formulaic bestseller and a boilerplate legal notice are both human, both high-probability, both correctly classified as human. Conversely, an unconventional good sentence can sit in a low-probability region and be flagged. The signal is a difference between *distributions*, not a verdict on an *item*.

`[theory]` **What the peak is made of.** A distribution's mass concentrates where its sources agree. A model trained on heterogeneous prose therefore has its high-probability region at the *intersection* of many genres' habits: the sentence that could appear in a thriller, a romance, and a literary novel without anyone objecting. That intersection is exactly what readers recognise as the universal literary voice — competent, tonally neutral, belonging to no one. This is why the default is not stupid. It is an average, and averages are inoffensive by construction. The failure of default prose is not that it is wrong about anything; it is that it is the one thing every genre would accept and no character would say.

## Limitations

`[data: DetectGPT]` and `[theory]` where noted.

1. **White-box assumption.** The method needs `log pθ(x)`. Some APIs expose it; some do not. Where they do, "evaluating probabilities nonetheless costs money". Everything in the paper is a white-box result except the surrogate-scoring study, which shows degradation.
2. **Perturbation-model dependency.** The curvature estimate is only as good as the mask-filler's notion of "same meaning, different words". PubMedQA is the demonstration: best-in-class detection, still a visible drop, attributed to "lower quality perturbations". Where the filler does not represent a domain's rephrasings well, the estimate degrades — and it degrades silently, with no signal to the user that the number is less trustworthy.
3. **Cost.** `k` samples plus `k+1` scorings per passage, against one scoring for the log-likelihood baseline. The paper offers no efficiency numbers, only the structural comparison and a hope that "a better tuned perturbation function or more efficient curvature approximation may help".
4. **Language and domain coverage.** Most datasets are English. The one non-English test is German WMT16, with mT5 perturbations, and DetectGPT is largely unaffected there — a single positive data point, not a multilingual validation.
5. **Length.** The method is defined for roughly paragraph-length passages. There is no reported behaviour for single sentences, sentence fragments, or very long documents. Any sentence-level use is extrapolation.
6. **AUROC is a ranking score, not a usable threshold.** All experiments use an equal number of positive and negative examples, and AUROC is threshold-free. A 0.95 means that in 95% of randomly drawn (machine, human) pairs the machine text scores higher. It does not tell you the false-positive rate you would get at a chosen threshold on a real, unbalanced stream of documents; the paper reports no precision/recall operating point.
7. **The crucial one — the criterion is origin, not value, and it is statistical.** A human text can sit in a high-probability region: boilerplate, genre formula, a competently written report, a deliberately flat procedural passage. An unconventional good text can sit in a low-probability region and be flagged. The hypothesis is about distributions ("tends toward zero"), not about individual passages. Using it as a per-passage aesthetic verdict inverts its logic and produces the two failure modes in the last section.

`[theory]` Also worth stating plainly: the tested models are 2022-era (GPT-2 through GPT-3) under raw, top-k, and top-p sampling. The paper's own future-work section asks whether prompting can evade detection. A curvature result on those generators is evidence about the *shape* of default output, not a permanent property of every model.

## What transfers, and what does not

**Transfers.**

**(a) The alternative-continuation test.** The operational core of the paper is: *compare a passage against its own meaning-preserving alternatives*. We cannot score them, but we can generate them. Write the passage the model would write; then deliberately produce the next 3–5 most likely continuations; then choose on dramatic grounds. The default is now visible, which is the only precondition for rejecting it. This is E11.

`[theory]` **(b) Surprising versus arbitrary.** Curvature logic explains why surprise must be *prepared*. A good surprise is locally off-peak — not the continuation the reader was predicting — while remaining recoverable from what came before, so that in retrospect it becomes the reading the text was building toward. Unprepared surprise is off-peak with no licence, which is the definition of arbitrary. The distinction is not "bold vs safe"; it is "licensed vs unlicensed". Preparation is the mechanism that converts a low-probability event into a necessary one.

**(c) Perturbation-thinking as a revision tool.** Rephrase a passage while preserving meaning. See what survives. If the meaning is fragile — if every paraphrase either loses the point or turns the sentence into a platitude — the prose is doing too little work, or it is doing work that only one exact string can carry. Both are diagnosable; the first is a defect, the second is a decision to record.

**Does not transfer.** We must never claim to compute log-probabilities, curvature, Hessians, perturbation discrepancy, or a detection score. The model's introspection about "what is likely" is a heuristic shaped by the same distribution it is trying to escape; it is not a measurement, and it is systematically blind to its own defaults. Say "this is the obvious choice and here is why I am not taking it", never "this sentence has low probability". No number in this file may appear in a critique as a measured value.

`[theory]` There is a second, subtler break in the analogy, and it is the one that ruins naive implementations. The paper averages over *random* perturbations drawn by a separate mask-filler — a wide sample of the space of equivalent phrasings, produced by a model that is not the one being audited. When we generate "the other options", we generate them with the same head that produced the default. Our alternative set is therefore biased toward the peak: it will contain the second-most-likely continuation, the third, and so on, all of them the same *kind* of choice. This is why step 3 of the protocol insists on declared axes taken from outside the sentence — who acts, what it costs, what is withheld. Asking "what else could I write here?" returns variations. Asking "who else could act here?" returns decisions.

## Idea → capability map

| Idea | Narraith mechanism | File |
|---|---|---|
| A model sample is a local maximum of `pθ`; the default is the peak | E11 Default-Avoidance: name the modal continuation *before* choosing, so it becomes visible and rejectable | `methodologies/04-prose-voice-originality.md` |
| Perturbation discrepancy: rewrites score lower than the original | E11 continuation divergence: generate 3–5 meaning-compatible alternatives for a beat and compare them as decisions | `methodologies/04-prose-voice-originality.md` |
| Surprise must be recoverable — off-peak but licensed | "Prepared surprise" rule: every turn names the earlier material that makes it available; no licence, no turn | `methodologies/01-plot-and-causality.md` |
| Perturbation = meaning-preserving rewrite | Paraphrase-survival check: two paraphrases; if the meaning collapses, the prose is carrying nothing | `references/editorial-intelligence.md` |
| The model's preferred phrasing is "roughly arbitrary, by human standards" | Voice Contract: prohibitions must be specific to *this* narrator's bias, not general "avoid cliché" | `methodologies/04-prose-voice-originality.md` |
| Detection ≠ quality; high probability is not a defect | Suspension rule: default-avoidance switches off where flatness is the dramatic job | `methodologies/04-prose-voice-originality.md` |

## The protocol we actually implement

**The Continuation Divergence Pass.** One unit at a time; the output is written, never merely thought. Run it on a sentence, a scene turn, or a plot turn, and state which one you are running.

1. **Freeze the unit.** Write its boundary in one line: "Scene 4, from her entering the workshop to the first lie". If you cannot state the boundary, you are not testing a unit, you are improvising.
2. **Write the modal version.** Produce the continuation you would generate by default — fast, undeliberated, one or two sentences. This is the peak, by definition. Do not make it a strawman; a strawman makes the whole test worthless.
3. **Generate 3–5 alternatives, each on a declared axis.** One axis per alternative: *who acts*, *what it costs*, *what is withheld*, *what the reader expects next*, *what the scene is actually about*. These are different decisions, not different wording. If two alternatives differ only in phrasing, you have produced one alternative.
4. **Score each on three questions.** *(i) Licence* — which earlier line, fact, wound, or pressure makes this choice available? Name it, or write "none". *(ii) State change* — what changes: knowledge, power, relationship, possibility? Nothing changed means it is not a turn. *(iii) Predictability* — would a competent reader have written this before reading? Yes / probably / no.
5. **Choose at the intersection.** Take "no" on predictability **with a named licence** and a real state change. Reject the other two corners: predictable-and-licensed is the default; unpredictable-and-unlicensed is arbitrary. If every alternative lands in those two corners, the scene is under-prepared — fix the setup, not the sentence.
6. **Keep the receipt.** Fill the record block below. It belongs in the decision ledger, not in the prose.
7. **Test on the page.** Read the chosen passage as if the licence were removed. If it now reads as random, the preparation is too thin: strengthen the setup or pick a prepared alternative.
8. **Prose-only add-on: paraphrase survival.** For a sentence you suspect of decoration, write two meaning-preserving paraphrases. If both reduce to the same thin statement, cut or replace it. If one paraphrase loses the point, the original phrasing is load-bearing — keep it and note why in the Voice Contract.

**Record format.** One block per pass, in the decision ledger, not in the draft. Three alternatives is the minimum; add rows for four and five.

```
divergence — <sentence | scene turn | plot turn> — <boundary, one line>
modal: <the version you would have written>
alt 1 | axis: who acts         | licence: <...> | change: <...> | predictable: y
alt 2 | axis: what it costs    | licence: <...> | change: <...> | predictable: p
alt 3 | axis: what is withheld | licence: <...> | change: <...> | predictable: n
chosen: alt 3 — <reason, one line>
rejected default: <why the modal version was not taken, or "taken, because ...">
```

`y` / `p` / `n` = yes / probably / no, from step 4.

**Calibration by unit.**

| Unit | Modal version is | Alternatives | Judged against |
|---|---|---|---|
| Sentence | the next sentence you would write without stopping | 3 | the previous paragraph, as licence |
| Scene turn | the obvious thing that happens next | 3–5 | the scene card: goal, obstacle, turn, cost |
| Plot turn | the modal outcome of the causal setup | 4–5 | the causal spine: what has been planted to make it possible |

**Budget guard.** Spend 3–5 alternatives on load-bearing decisions and none on filler. Running this on every sentence produces texture without structure and reads as strain. The method's own evidence says the same thing: the signal is strongest on paragraph-length units and weakest where everything already scores high.

**Diagnostics.** Three ways the pass fails, and what each one actually means.

- *All the alternatives are the same choice in different clothes.* You generated paraphrases instead of decisions. Re-run step 3 with a different axis; do not proceed until at least two alternatives would produce a different next scene.
- *Nothing has a licence.* The scene is under-prepared. You are trying to buy originality with a turn instead of with setup. Go back to the material that should have planted it, or accept the default and mark the scene as needing work at the structural level.
- *Every alternative is obviously worse than the default.* Then the default is probably correct here. Write it down as a decision with its reason — "the flat version is the point, she is too tired to notice him" — and move on. The pass exists to make the choice visible, not to forbid the modal option.

**A sentence-level run, in full.** Modal version: *She looked at the door and felt afraid.* That is what the first attempt produces: licensed by the knocking, predictable because fear is named rather than enacted. Alternatives on declared axes — *who acts*: she blocks the door with the chair. *What it costs*: she opens it, because the knocking has stopped and the silence is worse. *What is withheld*: she counts to four before answering, because she has counted before every door since chapter two. The first two are the stock moves — licensed, and exactly what a reader expects. The third is licensed by established material and is not what a reader would have written. Take the third. Record: chosen, rejected modal, licence. The difference between this and "make it more interesting" is that every move has a named source in the text and a named cost.

## Engineering hypotheses

- `[hypothesis]` Drafts that explicitly record the modal version plus 3–5 alternatives at each major turn will be rated more original in blind paired comparison than drafts written straight, **without** a loss in coherence ratings. Falsifiable by blind raters on paired outputs; the coherence clause is the part most likely to fail.
- `[hypothesis]` Divergence budget matters more at turns than at sentences. The same total number of alternatives, concentrated on 3–5 structural decisions, will outperform the same budget spread across line-level variation. Falsifiable by holding the budget constant and varying only its allocation.
- `[hypothesis]` "Prepared surprise" — unpredictable choice plus a named textual licence — will be rated as satisfying more often than the same choice with the licence stripped, and this gap will be larger than the gap between bold and timid choices. Falsifiable by A/B with the preparation deleted and nothing else changed.
- `[hypothesis]` The paraphrase-survival check will agree with human raters on which sentences are doing no work, at a rate better than chance. Falsifiable by correlating check outcomes with rater judgements of "this sentence could be deleted".
- `[hypothesis]` Writing the modal version first reduces regression to it. Naming the default is itself the intervention, independent of which alternative is chosen. Falsifiable by comparing a modal-first condition against a modal-unnamed condition where the same alternatives are offered.
- `[hypothesis]` Uniform application at sentence level degrades readability while improving local novelty — the "surprise for its own sake" failure. Falsifiable by measuring reader friction as a function of divergence density.

## Verbatim anchors

1. "text sampled from an LLM tends to occupy negative curvature regions of the model's log probability function" — Abstract.
2. "minor rewrites of model-generated text tend to have lower log probability under the model than the original sample" — Section 1.
3. "`d(x, pθ, q)` is positive with high probability for samples `x ∼ pθ`" and "For human-written text, `d(x, pθ, q)` tends toward zero for all `x`" — Hypothesis 4.1.
4. "the model is exposing its bias toward the specific (and roughly arbitrary, by human standards) phrasing used" — Section 6, "DetectGPT and Watermarking".
5. "LLMs that do not perfectly imitate human writing essentially watermark themselves implicitly" — Section 6, "DetectGPT and Watermarking".
6. "Detection accuracy continues to improve until 100 perturbations, where it converges." — Section 5.3.
7. "machine-generated creative writing tends to be noticeably generic, and therefore relatively easy to detect" — footnote 4.
8. "presumably because top-k generations are more generic" — caption, Table 5.

## Misapplication risks

1. **Surprise for its own sake.** The fastest way to invert a curvature signal is to always pick the least likely option. That produces arbitrary text with a novelty smell, not original text. The paper's signal concerns origin; inverting it produces a different default, not a decision. Condition under which the rule does not apply: when the unlikely choice has no licence, it is not a candidate at all.
2. **Confusing low probability with quality.** "Unpredictable" is not "good", and "high-probability" is not "bad". A flat, procedural passage can be the right instrument for an exhausted POV, a bureaucratic voice, or a scene that needs to feel administered rather than felt. Default-avoidance is suspended there deliberately, and the decision to be flat should be recorded like any other.
3. **Claiming measurement.** Never write "this sentence has low probability", "DetectGPT would flag this", or any curvature or detection number in a critique. We have no log-probability access; the model's sense of "what is likely" is a heuristic generated by the distribution it is auditing, and it is blind exactly where it is most confident. State the choice and the reasoning, not a score.
4. **Treating curvature as a theory of human writing.** Human text is not "flat" by nature. It is flat *under a particular model at a particular time*, and the paper's own limitation is that a human text can sit at a high-probability point. Reading the result as "human writing is intrinsically surprising" gets the causality backwards and produces prose that performs difficulty instead of having it.
5. **Extrapolating to sentences and to newer models.** The paper defines the method for roughly paragraph-length passages under 2022-era generators. Sentence-level verdicts and claims about current models are extrapolations, and the paper's own future work asks whether prompting alone can move a text off the peak.
