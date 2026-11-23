# DNA-GPT: continuation divergence as a test of authorship

> Purpose: what DNA-GPT actually measured, and the one procedure from it that a writer can run on their own draft.
> When to read: before E11, before the scene gate, or when a scene reads competent and you cannot say why it feels unowned.
> Connects: `references/research/05-fingerprinting.md` — why the lexical half of this method does not transfer; `references/ai-narrative-signature.md` — what AI text does instead of choosing; `methodologies/04-prose-voice-originality.md` — E11, the engine this dossier feeds.

## Contents

Bibliographic record · The claim · Methodology · Results · The mechanism, restated for a writer · Limitations · What transfers, and what does not · Idea → capability map · The regeneration protocol · Engineering hypotheses · Verbatim anchors · Misapplication risks.

Tagging follows the project convention: `[data: DNA-GPT]` is measured in the paper, `[theory]` is craft reasoning, `[hypothesis]` is our untested engineering claim.

---

## Bibliographic record

Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, Haifeng Chen. "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text." arXiv:2305.17359v2 [cs.CL], 4 October 2023. Preprint (the ethics statement references the ICLR code of ethics; no venue is printed on the PDF).

Affiliations: UC Santa Barbara (Yang, Petzold, Wang), NEC Laboratories America (Cheng, Chen), UCLA (Wu). Code: `https://github.com/Xianjun-Yang/DNA-GPT`.

The paper sits in the detection literature and inherits DetectGPT's task framing: given a text, decide whether it came from a specific known model or from a human. Its own contribution is the *method of comparison* — cut the text, let the model re-write the rest, measure how far the re-write lands from the original — plus a claim that this comparison is explainable and survives editing. Everything in this dossier that reaches the writing craft comes from that comparison, not from the classifier built on top of it.

---

## The claim

`[data: DNA-GPT]` The empirical observation under the whole method, stated in the introduction: "Given appropriate preceding text, LLMs tend to output highly similar text across multiple runs of generations." Given the same preceding text, the human remainder "tends to follow a more diverse distribution." Detection is the exploitation of that asymmetry.

The task is binary: a sequence `S = [s1 … sL]` came either from model distribution `M` or human distribution `H`. The detector knows which model it is testing against. Two settings: black-box (only text in, text out) and white-box (token probabilities `p(sl+1 | s1:l)` are also visible).

### The shared first move: truncate

`[data: DNA-GPT]` A truncation ratio `γ` splits the sequence:

- `X = [s1 … s⌈γL⌉]` — the prefix, fed to the model as-is;
- `Y0 = [s⌈γL⌉+1 … sL]` — the original remainder, held back as the thing to compare against.

The model is then asked to continue from `X` alone, `K` independent times: `Ω = {Y1 … YK}`, each `Yk ~ M(·|X)`. The point of the design is that the prefix is copied verbatim, so the model's continuation is conditioned on the same words the human author faced. Nothing about the prefix is scored. Only the divergence of the tail is.

### Black-box: n-gram divergence

`[data: DNA-GPT]` The BScore averages, over the `K` regenerations, a weighted overlap between each regeneration and the original remainder:

```
BScore(S, Ω) = (1/K) Σ_k Σ_{n=n0..N} f(n) · |grams(Yk,n) ∩ grams(Y0,n)| / (|Yk| · |grams(Y0,n)|)
```

Parameters as printed: `f(n) = n log(n)`, `n0 = 4`, `N = 25`. So the metric counts shared word n-grams from length 4 to length 25, weights longer matches more heavily (a 20-gram counts far more than a 4-gram), and normalizes by the length of the regeneration and by the number of n-grams in the original tail. Longer shared spans are what move the score; short function-word coincidences are suppressed by the `n0 = 4` floor.

`[data: DNA-GPT]` The same overlap doubles as the explanation. The *evidence* is the union of matched n-grams:

```
En = ⋃_k ( grams(Yk,n) ∩ grams(Y0,n) )
```

"Compared with the classifier-only detector, our method also provides evidence for detection results and thus is explainable." A human reader can look at the matched spans and judge for themselves.

### White-box: probability divergence

`[data: DNA-GPT]` Where token probabilities are available, the score is a likelihood ratio between the original tail and the regenerations, averaged over `K`:

```
WScore(S, Ω) = (1/K) Σ_k log [ p(Y0|X) / p(Yk|X) ]
```

A machine tail sits at high probability under the model that produced it; a human tail sits lower. The ratio makes that gap a single number. `p(Y|X)` here is the probability of the continuation tokens only — the prefix is not re-scored.

### How many completions

`[data: DNA-GPT]` `K` is not fixed by theory in the experiments. The appendix derives `K = Ω(σ log(1/δ)/Δ²)` from a sub-Gaussian assumption on the distance and a likelihood gap `Δ`, which only says *more is better, logarithmically*. Empirically: AUROC saturates at `K = 10` in the black-box setting and `K = 5` in white-box; TPR at 1% FPR keeps climbing to about five regenerations. The recommendation is 5–10 on cost grounds. The headline tables use `K = 20, γ = 0.7` and `K = 10, γ = 0.5`.

### How the threshold is set

`[data: DNA-GPT]` Figure 1's caption: "The threshold ϵ balances TPR and FPR." That is the whole description. In practice every result is reported as TPR at a fixed 1% FPR, which implies the threshold was placed at the score cutting off the lowest 1% of human texts in the evaluation set. The paper does not describe a held-out calibration split, a cross-validated threshold, or an error bar on the threshold itself. Treat "the threshold" as an operating-point choice on the test data, not as a calibrated decision rule.

### Why they think it must work

`[data: DNA-GPT]` The Likelihood-Gap Hypothesis: `E_{Y~M}[log p(Y|X)] − E_{Y~H}[log p(Y|X)] > Δ` for some `Δ > 0`. Via Pinsker's inequality this bounds the gap from below by `‖log p(·|X)‖∞ · sqrt(½ d_KL(M,H))`, and LeCam's lemma then gives a non-trivial upper bound on achievable detection error. The argument is that machine and human conditional distributions are separated enough that *some* test must work. It is an existence argument, not a guarantee for this particular statistic.

---

## Methodology

### Datasets

`[data: DNA-GPT]` Five sets, four English and one German:

| Dataset | Domain | Provenance in the paper |
|---|---|---|
| Reddit-ELI5 | long-form question answering | ELI5 community, physics and biology flairs, January 2022 – March 2023 |
| Scientific Abstracts | research abstracts | titles from Nature, collected 23 April 2023, experiments run the same day |
| PubMedQA | biomedical QA | Jin et al. 2019, used as in DetectGPT |
| Xsum | news summarisation / continuation | Narayan et al. 2018 |
| WMT16 (en, de) | translation corpus, used as prose | Bojar et al. 2016; German sentences of ~200 words, first 20 words as prompt |

Instance counts in Appendix B.1: 200 Reddit, 200 Scientific Abstracts, 150 PubMedQA, 200 Xsum, 300 WikiText-103. Appendix B.3 restates the range as "150 to 200 instances from each dataset". WikiText-103 is not a detection benchmark here — it is the memorisation control (see Limitations).

The two newest sets exist because of a specific worry: if the model has memorised the source, detection is meaningless. Reddit was filtered to dates after the claimed training cutoff and abstracts were scraped and tested the same day.

### Models

`[data: DNA-GPT]` Five: `text-davinci-003`, `gpt-3.5-turbo`, `gpt-4-0314`, `GPT-NeoX-20B`, `LLaMa-13B`. Temperature 0.7 for all five, maximum output 300 tokens. Only `text-davinci-003` exposes token probabilities; `gpt-3.5-turbo` was being silently updated during the study, `gpt-4-0314` was frozen. That distribution of capabilities is what forces the two-track design: black-box is the default, white-box is a bonus available on older or open models.

### Procedure and parameters

`[data: DNA-GPT]` Detection is run twice per dataset, once with the golden prompt known, once unknown, because both situations occur in the wild (Reddit questions are visible; fake news prompts are not). Truncation ratio was swept over `{0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.98}` on three model/dataset pairs with 150–200 instances each. Performance rises then falls, and 0.5 wins across models and datasets: too short a prefix gives the model too much freedom, too long a prefix leaves nothing to compare.

### Revised-text attack

`[data: DNA-GPT]` Following DetectGPT, human revision is simulated with T5-3B mask-filling: randomly replace `r%` of 5-word spans and let T5 fill them. 100 Reddit instances answered by GPT-4. Ratios `r ∈ {0.0, 0.1, 0.2, 0.35, 0.5}`. Both training-based baselines degrade sharply past `r > 0.3`; DNA-GPT drops from 99.09 to 98.48 AUROC at `r = 0.5`.

### Model sourcing

`[data: DNA-GPT]` A secondary task the authors name: given text and a set of candidate models, say which one produced it. The pipeline is unchanged — truncate, regenerate with each candidate, rank by the resulting score. Tested on Xsum and Reddit with pairs drawn from `{GPT-3.5-turbo, GPT-4, GPT-NeoX-20B, LLaMa-13B}`.

### Baselines

`[data: DNA-GPT]` GPTZero (perplexity and burstiness), OpenAI's AI text classifier (fine-tuned from 34 models across five organisations), and DetectGPT for `text-davinci-003` only, since it needs token probabilities. Entropy- and rank-based detectors are excluded because they need full-vocabulary probabilities, unavailable through the ChatGPT API.

### Additional probes

`[data: DNA-GPT]` Proxy-model detection with OPT-125M and GPT2-124M when the source model is unknown; a sliding window of size 2 for text that is half machine, half human; a re-test after several weeks to see whether model updates break the score; a "smart system prompt" substitution on the abstracts set (simplified system prompt costs 1.02 AUROC and 4.50 TPR); inverse prompt inference, hand-checked on 20 instances where 14 reconstructed questions were "very similar" to the originals.

---

## Results

### Headline AUROC / TPR at 1% FPR

`[data: DNA-GPT]` Table 1, selected cells (`AUROC / TPR`):

| Generator | Dataset | DNA-GPT | OpenAI classifier | GPTZero |
|---|---|---|---|---|
| GPT-4-0314 | Reddit-ELI5 | 99.63 / 87.34 | 71.64 / 5.00 | 94.50 / 36.00 |
| GPT-4-0314 | Scientific Abstracts | 96.72 / 67.00 | 96.05 / 73.00 | 76.08 / 11.10 |
| GPT-4-0314 | PubMedQA | 95.72 / 44.50 | 94.91 / 52.00 | 87.72 / 44.00 |
| GPT-4-0314 | Xsum | 91.72 / 32.67 | 77.78 / 30.67 | 79.59 / 36.00 |
| GPT-3.5-turbo | Reddit-ELI5 | 99.61 / 87.50 | 94.36 / 48.50 | 96.85 / 63.00 |
| GPT-3.5-turbo | Scientific Abstracts | 98.02 / 82.00 | 99.25 / 94.00 | 88.76 / 5.50 |
| GPT-3.5-turbo | Xsum | 97.12 / 33.33 | 94.74 / 74.00 | 90.79 / 54.67 |
| text-davinci-003 | Xsum (K=10, γ=0.5) | 97.97 / 51.00 | 85.73 / 58.67 | 83.80 / 35.33 |

What this table actually says, plainly: AUROC is high almost everywhere for DNA-GPT (91.7–99.6 on those cells), and TPR at 1% FPR is wildly uneven (32.7–87.5). The OpenAI classifier beats it on TPR in several cells while collapsing on Reddit against GPT-4 (5.00). The paper's own framing — that AUROC near 1.0 hides deployment differences — is the honest reading of its numbers, and their Xsum TPR of 32.67 for GPT-4 is not a strong result.

Where the margin is largest is exactly where training-based detectors fail: a new corpus (Reddit, 71.64 AUROC for OpenAI against GPT-4) and a new model (below).

### White-box

`[data: DNA-GPT]` Table 1, `text-davinci-003`, WScore:

| Dataset | DetectGPT (K=100) | DNA-GPT (K=10, γ=0.5) |
|---|---|---|
| Reddit-ELI5 | 58.36 / 0.00 | 100.00 / 100.00 |
| Scientific Abstracts | 55.45 / 0.89 | 99.94 / 99.00 |
| PubMedQA | 70.92 / 2.38 | 99.87 / 96.67 |
| Xsum | 82.11 / 0.00 | 100.00 / 100.00 |

This is the cleanest result in the paper: at 1% FPR, DetectGPT's TPR is essentially zero on three of four sets while DNA-GPT's is near saturation. The comparison is one-sided because the two methods use different statistics on the same signal, but the operating-point advantage is enormous and costs far fewer forward passes (10 vs 100).

### German

`[data: DNA-GPT]` WMT16 German, AUROC only, Figure 6: DNA-GPT 92.79 (`text-davinci-003`) and 90.44 (`gpt-3.5-turbo`); OpenAI classifier 90.09 and 93.98; GPTZero 12.18 and 11.43. So: GPTZero is at chance, OpenAI is slightly better than DNA-GPT on the newer model and slightly worse on the older one, and the paper's claim of "comparable or even superior" is accurate but modest. No TPR is reported for German.

### Under revision

`[data: DNA-GPT]` AUROC 99.09 → 98.48 as the revised fraction goes 0 to 0.5. The baselines fall off a cliff past `r = 0.3`. Note what this measures: the ranking of scores stays intact, not that the lexical evidence survives. Half the tail rewritten by T5 necessarily destroys most 5-gram matches in the rewritten spans, so the score's *absolute* level must move; the paper reports only that the separation between classes holds. It does not show the evidence spans, and does not say what happens to `En` under revision.

### Model sourcing

`[data: DNA-GPT]` Two-model discrimination on Xsum and Reddit, reported AUROC 86.99–99.91 and TPR at 1% FPR 45.60–99.00 across the five pairs (Table 2). The strongest cell is 99.91 / 99.00, the weakest 86.99 / 45.60.

### Open-source models

`[data: DNA-GPT]` Table 3, Xsum: GPT-NeoX-20B black-box 90.20 / 52.67, white-box 95.57 / 66.22; LLaMa-13B black-box 88.87 / 46.67, white-box 84.62 / 20.00. Both baselines degrade badly on these models (OpenAI 78.70 / 56.67 and 73.84 / 46.67 respectively), which is the paper's point about bespoke detectors not transferring to models they were not trained on. The LLaMa white-box TPR of 20.00 is a counterexample to any claim of uniform superiority.

### Appendix figures worth knowing

`[data: DNA-GPT]` Additional metrics (Appendix C) exist only for selected cells — Reddit across three generators, PubMedQA for `text-davinci-003`, Reddit for LLaMa. Best F1 in those cells is 99.75 (white-box Reddit, `text-davinci-003`, prompt known). Proxy-model detection with OPT-125M yields AUROC 69.2–82.3 across five source models (Table 6), i.e. usable but far below same-model detection. After a six-week gap on an updated `gpt-3.5-turbo`, AUROC 99.61 → 98.70 and TPR 87.50 → 92.00 (Table 7): the score survives a model update.

### What was not reported

No confidence intervals, no significance tests, no per-instance variance across the `K` regenerations. No F1 or accuracy for most cells. No TPR for German; no per-language breakdown beyond the single German split. No human evaluation of the *evidence* spans — the explainability claim is illustrated with examples (Appendix D, Tables 14–16) rather than validated with readers. No 4-way model sourcing despite the task being motivated with four candidates. No literary or fiction corpus of any kind: the domains are QA, abstracts, news, and encyclopedic text.

---

## The mechanism, restated for a writer

`[theory]` Strip the classifier and what remains is a fact about conditional distributions that any writer can verify by hand. Take a competent writer, hand them the first two-thirds of a paragraph, and ask for the rest. Two things can happen. Either they produce something close to what is already there, because the setup left only one thing to do — or they produce something else, because the original author had made choices the setup does not force.

DNA-GPT's finding is that a machine continuation tends to land close, and a human continuation tends to land elsewhere. The paper's explanation is the likelihood-gap hypothesis: `[data: DNA-GPT]` "the thought process of human writing does not simply follow the likelihood maximisation criterion." A model samples near its own conditional mode. A person writing does something else: they remember a detail that does not belong to the argument, they reach for a word because of its sound, they leave a thread hanging because the scene did not need it tied.

So a machine text is close to its own mode *because it was drawn from that mode*. Regenerating it is close to sampling the same distribution twice from nearly the same point. This is not a stylistic fact — it is a sampling fact. And it is why the method works without training: nothing about the text's surface is being classified. The text is being asked, in effect, *how much room did the author leave?*

### The literary reading

`[theory]` Predictability is measurable as the tendency of a competent re-writer to reproduce your choices.

That sentence is the whole transfer. It reframes a vague complaint ("this feels generic") as an operational question with a procedure attached: *if someone with the same setup wrote the next 200 words, would they land where I landed?* If yes, then whatever is on the page is a property of the setup, not of an author. The setup wrote it. You typed it.

Three things make a continuation diverge, and all three are ordinary craft objects rather than stylistic flourishes:

1. **Idiosyncratic word choice.** Not rare words — *chosen* words. A word selected for a reason the sentence does not explain cannot be predicted from the sentence. In DNA-GPT terms this shows up as low n-gram overlap; in craft terms it is voice.
2. **Unexplained detail.** A specific object, number, or gesture that the text does not account for. Models are trained to account for what they include; a detail that pays no immediate rent is a signature. This is the strongest divergence source available to a writer, because it survives paraphrase far better than word choice does — the detail itself is the content.
3. **An unresolved thread.** A question raised and not closed, a want stated and not satisfied, a person mentioned once and never again. Modal continuation closes threads; that is what "well-made" means to a model. A thread left open changes what the next scene can be, and no re-writer guessing from the setup will guess *which* thread you left open.

`[theory]` A scene that another writer would inevitably write the same way is a scene without authorship. It may still be a good scene — inevitable scenes are how genre delivers its pleasures — but if every scene in a manuscript is inevitable, the manuscript has a setup and no author.

This is also the correct way to read the paper's *evidence* output. `[data: DNA-GPT]` The long identical spans printed in Appendix D are not stylistic similarity; they are near-verbatim reproduction. In the memorisation control the longest overlaps reach 27 and 26 grams (Table 13) — a model reciting *Die Another Day* plot summary from Wikipedia. The longest identical spans are recitation, not authorship. A writer's analogue is blunt: if a re-writer reproduces your sentence nearly verbatim, you did not choose the sentence, you recalled it.

---

## Limitations

**It needs the model.** Every number in the paper is computed by regenerating with the *same* model that supposedly wrote the text. `[data: DNA-GPT]` Proxy-model detection with OPT-125M drops to 69.2–82.3 AUROC. As a self-audit this is not a problem — you have your own model — but it means the test measures "how much room did this text leave *for this model*", not "how would a human have written it". Cross-model transfer is weak evidence at best.

**The black-box metric is surface-level, and that is a real conflict.** `[data: DNA-GPT]` BScore counts shared 4-to-25-grams. It is a lexical statistic wearing an explanatory story. `[data: fingerprinting]` The fingerprinting study finds the opposite ordering of durability: surface and behavioural signals are "relatively fragile", lexical information stays strong after surface normalisation but weakens under paraphrasing, and semantic representations are the most robust across languages. Read together, the two papers do not contradict each other's measurements — they disagree about *what survives contact with editing*. A paraphrase that preserves every dramatic decision destroys every 4-gram. DNA-GPT's own revision experiment supports the fragile reading: at `r = 0.5` half the tail is T5-generated, so the n-gram evidence for those spans is gone, yet AUROC holds at 98.48. The ranking survives because both classes lose overlap at once; the *evidence* does not. **Resolution for Narraith:** use the procedure (truncate, regenerate, compare) and the dramatic criterion (is the continuation equivalent in event, agency, and state change), never the lexical metric. The lexical layer is the one layer we are told to distrust; the continuation divergence at the level of *decisions* is what we keep. See `references/research/05-fingerprinting.md`.

**Length.** `[data: DNA-GPT]` The ethics statement is explicit: tested only "within a moderate length range (1000-2000 characters)", and the appendix adds that the classifier needs more than 1000 characters while short answers are hard to separate. That is roughly 150–350 English words. Our protocol works at 150–250 words of continuation, which is inside the tested band, but a whole chapter is far outside it.

**Truncation point.** `[data: DNA-GPT]` Performance is a hump in `γ`, best near 0.5, and the authors warn that a fixed ratio is "unsuitable for a longer text that starts with AI-generated prefix text and is followed by human-written text" — hence the sliding window. In craft terms: cutting at the wrong hinge makes the test meaningless. Cut before a turn and you measure the turn; cut mid-sentence in a passage of pure description and both continuations will agree for boring reasons.

**Language.** English and German only, and the German result is AUROC without TPR. Nothing here licenses claims about Russian, and `[theory]` the mechanism is likely language-sensitive in a specific way: languages with richer inflection give a re-writer more surface freedom, which would inflate apparent divergence without any gain in authorship.

**High temperature produces false negatives.** `[data: DNA-GPT]` At `T = 1.8` the generated text becomes nonsense ("nonsensical text" is the authors' word; Appendix C.1 prints pages of it), and all detectors collapse. More relevant to us: at `T = 1.0–1.4` detection degrades, because a high-temperature machine text is no longer near the mode. A machine draft written at high temperature will pass a divergence test while still being nobody's. Do not read "diverged" as "human" — read it as "the sampler was not at its mode", which has many causes.

**Formulaic human prose produces false positives.** `[data: DNA-GPT]` The revised-text result is the mechanism in miniature: the more a text is rewritten by a model toward fluency, the more detectable it becomes. The same logic applies to a human writing a genre scene by the book — a police procedural beat, a romance reunion — where the next move really is forced. Low divergence there is a fact about the *form*, not the author.

**Memorisation destroys the test.** `[data: DNA-GPT]` On WikiText-103, where models have seen the text, `text-davinci-003` reproduces three consecutive sentences verbatim in 13 of 100 sampled cases, and TPR collapses (94.40 AUROC but 7.00 TPR for the black-box detector; 0.33 and 0.67 for GPT-4 and white-box cells). A model reciting its training data is indistinguishable from the human who wrote it, because it *is* the human's text. Any craft test built on regeneration inherits this: if the model has seen your sentence, its re-write is recall, and agreement means nothing.

---

## What transfers, and what does not

### Transfers

**The regeneration test as a self-audit, at scene level and at plot level.** Delete the last 150–250 words of a scene, keep the setup, regenerate, compare. At plot level the same move works on a beat sheet: delete the outcome of a turn, keep the setup, ask what happens next. If the regenerated outcome is the one you wrote, the turn was supplied by the situation rather than chosen.

**"Authorship density" as a diagnostic.** `[theory]` A scene's density is the number of decisions in it that a competent re-writer would not reproduce: a word chosen against the grain, a detail with no function, a thread left open, an exit that refuses the expected emotion. Density is not the same as difficulty, and it is not per-sentence — one unpaid detail can carry a page. This is a *counter* you can run by hand, not a metric we compute.

**Unresolved details and unpaid attention are features, not bugs.** `[theory]` The mechanism predicts that a text where everything is accounted for is a text a model could have written, because accounting-for-everything is what the conditional mode does. The craft consequence is uncomfortable and correct: a detail that never pays off is not automatically a flaw. It is often the only thing on the page that a machine would not have put there. The test is not "does every detail pay off" but "does this detail belong to a world" — and the second question has no mechanical answer.

**The revision warning.** `[theory]` Polishing toward fluency pushes text toward the mode. `[data: DNA-GPT]` The revised-text experiment shows the direction: as more of a text is replaced by T5-generated spans, detection gets easier, not harder, and the baselines collapse past `r = 0.3`. Editing for smoothness is editing toward the modal. That is a reason to keep the strange detail when the line "reads worse" — the worse-reading line may be the only unowned thing left.

### Does not transfer

**We do not compute divergence.** No BScore, no WScore, no `n0 = 4`, no `N = 25`, no threshold. We have no token probabilities and, per the project's honesty rule, we do not claim any.

**We cannot claim detection.** Everything here is a craft diagnostic run by an author on their own draft. Applying it to someone else's text as evidence of machine authorship would be exactly the misuse the paper itself warns about, and it would be worse in our hands because we have no calibrated statistic at all.

**Lexical divergence is not quality.** The metric rewards not being predictable. A deliberately plain style — a fairy tale, a legal memo, Hemingway's dialogue, a scene whose whole point is that nothing surprising happens — scores as low-divergence and may be excellent. Predictability is one axis of authorship, not a virtue in itself, and the modal answer is sometimes the right answer. Law 5 of the doctrine says the obvious option is the *draft*, not that it is always wrong.

---

## Idea → capability map

| Idea | Narraith mechanism | File |
|---|---|---|
| Continuation divergence as a test of default-ness | E11: take the obvious continuation, then force and justify an alternative; the regeneration test is the inspection tool at the end of the engine | `methodologies/04-prose-voice-originality.md` |
| Truncate at the hinge, regenerate the tail | Scene gate: before passing a scene, delete its last beat and ask what a re-writer would do; if the answer is the written beat, the beat is modal | `workflows/03-scene-and-ensemble.md` |
| Dramatic equivalence as the criterion | Modal-scene audit: a scene whose state change can be regenerated from its setup is a scene without an author; log it and rewrite the *setup*, not the sentences | `methodologies/03-time-and-scene.md` |
| Authorship density | E11's evaluation criterion: count decisions a competent re-writer would not reproduce (word, detail, open thread, refused emotion) | `methodologies/04-prose-voice-originality.md` |
| Unpaid detail as signature | E11 / L4: protect details that belong to the world but pay no thesis; the failure is not "unexplained", it is "unowned" | `methodologies/04-prose-voice-originality.md` |
| Editing toward fluency raises predictability | Revision workflow: a pass that only smooths is a pass toward the mode; require one non-smoothing change per page | `workflows/04-continuation-and-revision.md` |
| Evidence spans / recitation | Continuity check in reverse: verbatim agreement between draft and model output means recall, not authorship; flag any sentence the model reproduces exactly | `workflows/04-continuation-and-revision.md` |

---

## The regeneration protocol

Seven steps, run by the model on its own draft. Budget: one scene, two rounds, five minutes.

**1. Pick the hinge.** Choose a scene of 600–1500 words that you believe works. Identify the beat where the scene turns — the decision, the reveal, the refusal. The cut goes *immediately before* that beat, not at the end of the scene. `[data: DNA-GPT]` The paper's 0.5 ratio is a default; our cut is chosen for dramatic reasons, which is a deliberate departure and is marked as such.

**2. Cut 150–250 words.** Everything from the hinge onward is the tail. Set it aside; do not paraphrase it in your head, and do not leave it visible in context while generating. The measured object is what the setup alone forces.

**3. Regenerate twice, cold.** From the prefix only, write two independent continuations of 150–250 words. Same POV, same tense, same voice contract. Do not aim for a good continuation; aim for *the* continuation — the one the setup makes easiest. `[data: DNA-GPT]` The paper uses 5–20 samples; two is a budget downgrade and is only enough to catch agreement, not to estimate a distribution. Say so when you report the result.

**4. Compare on four axes, in this order.**
   - *Event*: what happens next. Same action, or a different one?
   - *Agency*: who makes it happen. Does the same character cause it, or does the continuation hand the turn to circumstance, to a new arrival, to an accident?
   - *State change*: what is different at the end. The axis that usually decides.
   - *Left open*: what the continuation refuses to resolve. If it resolves your thread, note which one.

**5. Apply the equivalence rule.** The continuations are **dramatically equivalent** to your original if three things hold: the same state change at the end, produced by the same agent, with the same threads left open. Wording, imagery, and the specific event are diagnostic — they tell you *why* the verdict came out that way — but they do not decide it. They are **not equivalent** if any continuation produces a different state change, hands the turn to a different agent, or closes a thread the original leaves hanging. Lexical overlap is irrelevant at this step; `[data: DNA-GPT]` it is exactly the layer the fingerprinting study says to distrust.

**6. Read the verdict.**
   - Both equivalent, same state change → the beat was modal. Rewrite the *setup* so the modal continuation stops being available. Do not rewrite the sentences.
   - Equivalent but the two continuations differ in detail → the setup is under-determined. Your original is one valid choice among several, which is acceptable only if you can name why this one. If you cannot, it is a coin flip and should be logged as such.
   - Not equivalent, and the continuations disagree with each other → the scene carries authorship at the hinge. Stop.
   - Not equivalent because one continuation went somewhere impossible → the setup is unclear, not original. Fix the setup.

**7. Stop.** Two rounds maximum. Second round means: rewrite the setup, re-cut, regenerate once. If round two is again equivalent, do not rewrite again — the problem is upstream, in what the scene is for (E1/E8), and further sentence-level passes will only produce a more elaborate modal scene. Log the finding and move up a level.

### Avoiding infinite regress

The regress is real: every rewrite has a new hinge, and every hinge can be tested. Three brakes. First, a scene is tested once per draft; a scene that fails twice is escalated, not re-tested. Second, the test is only valid where the setup constrains — a passage of pure atmosphere has no hinge and no verdict. Third, the goal is not maximal divergence. `[theory]` Divergence is a proxy for authorship, and a scene can be fully authored while remaining predictable, if the predictability is *chosen and paid for* — the genre promise kept deliberately, the inevitable ending made costly on the way. When you can name the reason the modal move is right, the test has done its job even though the continuation matched.

### Worked micro-example

Original (79 words):

> The flat smelled of the tenant before her, a smell like coins. Mira worked through the kitchen with a bin bag and found a jam jar of screws in the third drawer. Each one had a strip of masking tape beside it, and on the tape, in pencil, a word: *hinge*. *the door that sticks*. *shelf, left*. She screwed the lid back on, put the jar in her coat pocket, and stood at the window until the light went.

Regenerated from the same prefix, continuation A (75 words):

> She read the labels twice. Somebody had kept every screw in this flat and named it, as if the flat could be repaired from a drawer. Mira thought about her mother's handwriting and how it had got smaller every year. She put the jar back where she found it, because it was not hers to take, and went out to the car, and sat in it for a while before she could start the engine.

Verdict: **not equivalent, but not for the reason it looks.** The event differs (keeps vs takes the jar) and the state change is the same — Mira ends immobilized by grief — and the agent is the same. The deciding difference is on the "left open" axis: the regeneration *closes* what the original leaves open. It explains the grief (handwriting getting smaller, "not hers to take"); the original lets the pencil labels stand unexplained and lets the pocketing happen without comment. One unpaid detail, and the original's last clause refuses the expected emotion by giving the light instead of the crying.

What this means for the draft: the hinge is authored; the final clause is doing the work, and a smoothing pass would delete it as flat. What it does *not* mean: that the regeneration is bad. It is competent, and it is the modal scene — the one the setup hands you if you account for everything. Keep the jar in the pocket; keep the tape.

---

## Engineering hypotheses

`[hypothesis]` H1. Scenes that readers rate as "generic" will show higher dramatic equivalence under the regeneration protocol than scenes rated "distinctive", at matched quality ratings. Test: 30 scenes, 6 raters per scene, blind to condition; correlate mean distinctiveness with equivalence verdict from two cold regenerations.

`[hypothesis]` H2. Among the three divergence sources, *unexplained detail* survives paraphrase and rewriting better than word choice, and is therefore the most reliable authorship signal for a writer. Test: take 20 passages, paraphrase them with a strong model, and count how many authored details survive vs how many chosen words survive.

`[hypothesis]` H3. A revision pass that only smooths will increase dramatic equivalence on a matched pair of drafts (pre/post), while a pass that adds or protects one unpaid detail will not. Test: paired drafts, protocol run before and after each pass, verdicts compared.

`[hypothesis]` H4. Plot-level regeneration (delete the outcome of a turn, regenerate the outcome) discriminates authored turns from situational turns at least as well as scene-level regeneration, because outcomes are more constrained than prose. Test: 20 turn descriptions with and without a distinctive causal choice, regenerated 5 times each, agreement rate compared.

`[hypothesis]` H5. Two regenerations are enough to detect *agreement* (both continuations equivalent) but not to detect *disagreement* (one equivalent, one not); the protocol's false-negative rate on authored scenes falls sharply from 2 to 5 samples. Test: reuse the same 30 scenes at K = 2 and K = 5, measure verdict stability.

`[hypothesis]` H6. High-temperature drafting (T ≥ 1.0) produces drafts that pass the divergence test while failing reader ratings of coherence, so divergence and quality are separable in exactly the way the paper's temperature results predict. Test: same prompts at T = 0.7 and T = 1.2, protocol verdict plus reader coherence rating.

---

## Verbatim anchors

1. "Given appropriate preceding text, LLMs tend to output highly similar text across multiple runs of generations." (§1)
2. "the thought process of human writing does not simply follow the likelihood maximisation criterion" (§3)
3. "the human-generated Y0 will have a much lower overlap with Ω, compared with GPT-generated text" (§3.1)
4. "When n is large, En serves as strong evidence for AI-generated text" (§3.3)
5. "the most favorable truncation ratio is expected to fall within the middle range" (§5)
6. "our DNA-GPT shows only a slight drop in AUROC from 99.09 to 98.48" (§5, revised text)
7. "our method is only tested for detecting text within a moderate length range (1000-2000 characters)" (Ethics Statement)
8. "careful consideration must be given to the choice of the dataset when testing detectors" (Appendix B.2.1)

---

## Misapplication risks

**Novelty for novelty's sake.** The protocol tells you a beat was modal; it does not tell you the modal beat was wrong. `[theory]` A genre scene that delivers exactly what the form promises is doing its job, and a writer who rejects every predictable move produces a text that is surprising and unreadable. The test is a detector of *unowned* choices, not of conventional ones. Before rewriting, name what the scene loses by becoming less predictable; if the answer is "the reader's trust", keep the beat and pay for it elsewhere.

**Confusing obscurity with originality.** A detail that is unexplained because the text is confused is not the same as a detail that is unexplained because the world contains it. `[theory]` The regeneration test can be gamed by deleting every causal link: the continuations will diverge wildly and the scene will be worthless. The guard is the equivalence rule read in both directions — divergence with no recoverable state change is noise, not authorship. Ask what the reader can reconstruct from the detail; if nothing, it is decoration with a cost.

**Using it as detection.** Running the protocol on someone else's text and reporting "this scene is equivalent, therefore AI" is unsupported. `[data: DNA-GPT]` Even the paper's calibrated detector, with a threshold and 20 samples, reports TPR at 1% FPR ranging from 20.00 to 100.00 depending on model and corpus, and its own ethics statement says the method "might still make mistakes". We have no threshold, no probability, and no samples. The protocol is for your own draft, and its output is a craft verdict, not an accusation.

**Treating divergence as quality.** `[data: DNA-GPT]` AUROC measures separability, not merit, and the paper is careful to say so. A text can be highly divergent and bad, and a text can be low-divergence and excellent. `[theory]` The failure mode in our hands is a draft that gets stranger under revision because the test keeps saying "modal" — a drift toward difficulty that readers experience as evasion. Cap it: the protocol may change at most one decision per scene per round.

**Testing a text too short to have a setup.** `[data: DNA-GPT]` The method needs 1000–2000 characters and a prefix that constrains. A single sentence, a line of dialogue, or a passage of pure description has no hinge and no measurable room. Running the test there produces agreement for trivial reasons — the setup determined everything because there was almost no setup — and the writer will "fix" a line that was never the problem. Test scenes, not sentences.
