# Research Foundations: What the Five Studies Support

> Purpose: state what each source measured, what it cannot tell us, and which capability in the skill rests on which finding — so that a number is never quoted without its boundary.
> Read when: before quoting any figure in another module, before claiming the skill is evidence-based, or when a rule's justification feels stronger than it should.
> Links: `references/research/01-storyscope.md` … `05-fingerprinting.md` — the dossiers this file summarises; `docs/research-map.md` — the maintainer audit of every claim and figure; `docs/limitations.md` — the hypotheses that would falsify the design.

Tags: `[data: <paper>]` is measured in that paper; `[theory]` is craft or narratology; `[hypothesis]` is our engineering inference. A number in this file without a dossier section reference is a bug.

## Contents

1. [The five sources](#the-five-sources)
2. [What the five studies have in common](#what-the-five-studies-have-in-common)
3. [The four findings that actually shape the skill](#the-four-findings-that-actually-shape-the-skill)
4. [Research → Capability map](#research--capability-map)
5. [Confirmed versus inferred](#confirmed-versus-inferred)
6. [What we deliberately do not claim](#what-we-deliberately-do-not-claim)
7. [How to cite inside the skill](#how-to-cite-inside-the-skill)
8. [Reading order for a new contributor](#reading-order-for-a-new-contributor)

## The five sources

Five papers, chosen because between them they cover the three things the skill needs to know: where model fiction differs (StoryScope), which of those differences survive editing (Fingerprinting), and what "the model's default" means mechanically (DetectGPT, DNA-GPT, Ghostbuster).

| # | Short name | Citation | URL | Venue, year | Kind of study | One-line finding |
|---|---|---|---|---|---|---|
| 1 | StoryScope | Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, John Wieting. "StoryScope: Investigating idiosyncrasies in AI fiction." | https://arxiv.org/pdf/2604.03136 | COLM 2026 (arXiv v6, Aug 2026) | Empirical measurement over 61,608 stories plus a supervised classifier | Discourse-level narrative choices separate human from model fiction at 93.2% macro-F1 without style features |
| 2 | Ghostbuster | Vivek Verma, Eve Fleisig, Nicholas Tomlin, Dan Klein. "Ghostbuster: Detecting Text Ghostwritten by Large Language Models." | https://aclanthology.org/2024.naacl-long.95.pdf | NAACL 2024, pp. 1702–1717 | Supervised detection over features built from weaker models' token probabilities | A structured search over combinations reaches 99.0 F1 in-domain and 97.0 averaged out-of-domain |
| 3 | DetectGPT | Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn. "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." | https://arxiv.org/pdf/2301.11305 | ICML 2023 (arXiv Jan 2023) | Zero-shot, white-box detection using log-probability curvature | Model samples sit at a local maximum of the model's own distribution; meaning-preserving rewrites score lower |
| 4 | DNA-GPT | Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, Haifeng Chen. "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text." | https://arxiv.org/abs/2305.17359 | arXiv 2305.17359v2, Oct 2023; preprint, no printed venue | Truncate-and-regenerate detection, black-box and white-box | Given the same prefix, a model's continuations are more similar to each other than a human's are |
| 5 | Fingerprinting | Mohammad Reza Modarres, Armin Tourajmehr, Artin Tavasoli, Yadollah Yaghoobzadeh, Mohammad Taher Pilehvar. "Every Model Leaves a Trace: Multi-Resolution LLM Fingerprinting." | https://arxiv.org/pdf/2610.28434 | arXiv 2610.28434v1, Oct 2026; preprint | Closed-set source attribution across 19 models, four signal families, eight transformations | Signal families form a durability ladder: surface form dies first, semantic representation travels furthest |

The two 2026 papers are recent enough that their model panels (GPT-5.4, Claude Sonnet 4.6, Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2; Llama-4, Qwen-3, Gemma-4) are already historical. Treat every per-model statement as a timestamp, not a property.

### 1. StoryScope

`[data: StoryScope]` It measured 61,608 short stories — 10,272 human anthology pieces plus five model versions answering a reverse-engineered prompt — on 304 narrative features across ten dimensions. Separation reaches 93.2% macro-F1 on narrative features alone; 30 core features retain 84.8%. What it cannot tell us: whether any of this matters to a reader. It measures detectability, not merit, on an Anglophone literary anthology, under prompts that suppress exactly the structures whose absence it reports.

### 2. Ghostbuster

`[data: Ghostbuster]` It measured document-level authorship classification on three new benchmarks of 7,000 documents each, using a structured search over 2,534 candidate features from four weaker models' token probabilities. It reaches 99.0 F1 in-domain, 97.0 averaged across held-out domains, 7.5 above the best prior system, and loses narrowly to RoBERTa on out-of-domain creative writing. What it cannot tell us: anything about prose. The label is provenance, the creativity set is one subreddit in 2022, and the method needs labels we do not have.

### 3. DetectGPT

`[data: DetectGPT]` It measured whether machine text sits in a region of negative curvature of its own model's log-probability function, using T5 mask-filling for meaning-preserving perturbations and 100 samples per passage. On 20B GPT-NeoX fake news, AUROC rises from 0.81 to 0.95; it wins 14 of 15 combinations by 0.06 on average. What it cannot tell us: whether a passage is good, or whether it is machine-written when the scorer is not the generator. White-box access, 2022-era models, paragraph-length text, no operating threshold.

### 4. DNA-GPT

`[data: DNA-GPT]` It measured how far regenerations of a truncated text diverge from the original continuation, on five corpora and five generators, black-box (n-gram overlap) and white-box (likelihood ratio). Machine continuations cluster; human ones do not. AUROC runs 91.7–99.6 on headline cells while TPR at 1% FPR ranges 32.7–87.5. What it cannot tell us: anything at sentence level, anything about fiction, anything about craft. Its corpora are QA, abstracts, news, and encyclopedic text.

### 5. Fingerprinting

`[data: Fingerprinting]` It measured source attribution across 19 models and eight transformations, separating candidate similarity from signal survival. Behavioural features fall from 52.42 to 25.59 across surface normalization, lexical n-grams are strongest in-language (80.07) but shed a third under full paraphrase (53.94), and stylometry collapses across languages (60.72 within English, 19.74 over six directions, against 12.5% chance). What it cannot tell us: anything about quality, fiction, or Russian. The task is closed-set identity on translated prompts.

## What the five studies have in common

**All five are detection or attribution studies.** Each asks some version of "which process produced this text?" StoryScope labels human vs model; Ghostbuster labels human vs model; DetectGPT labels sample-from-this-model vs not; DNA-GPT labels model vs human from a known generator; Fingerprinting labels which of nineteen models. Not one manipulates a text and measures a reader's response.

**None is an intervention study.** No paper teaches anyone to write differently, then measures the result. Every claim of the form "if you change this feature, the story improves" is a transfer we perform. `docs/limitations.md` lists the seven hypotheses this creates; none has been tested.

**Only StoryScope studies fiction as its primary material.** Ghostbuster's creative-writing set is prompted genre fiction from one subreddit, collected before November 2022. DetectGPT's writing set is Reddit prompts too. DNA-GPT has no fiction at all. Fingerprinting samples general-purpose prompts, of which 40 of 200 are creative writing, not analysed separately. A finding about "creative writing" in four of these papers is a finding about short prompted web fiction.

**Language coverage is narrow and mostly English.** StoryScope: English only. Ghostbuster: predominantly British and American English, plus non-native English test sets. DetectGPT: English, with one German split using mT5 perturbations. DNA-GPT: English and German, AUROC only for German. Fingerprinting: English, plus Persian and Chinese generated from machine-translated prompts. No study contains Russian; no study contains natively authored non-English fiction. `references/russian-prose.md` is craft knowledge, not evidence from this corpus.

**The measured unit is short.** StoryScope's stories average 4,753 words. Ghostbuster documents run from a few hundred words to a few thousand. DNA-GPT tests 1,000–2,000 characters. Fingerprinting caps responses at 2,048 tokens. No paper measures a novel, a chapter sequence, or a series. Long-form coverage in this skill is inference from craft literature, and `docs/limitations.md` says so.

**Consequence: every generation claim is an engineering hypothesis.** The chain is always the same — a population difference is measured, we infer that the difference reflects a default rather than a necessity, and we infer that forcing a decision away from the default improves the text. The first step is evidence. The second is plausible. The third is untested, and no number in any dossier shortens that gap.

### What the overlap does buy

Convergence across independent studies is the only substitute for an intervention study, and there is some. Two papers with different methods and corpora find that surface-level signals are the fragile layer (StoryScope's LAMP result, Fingerprinting's transformation ladder). Two find that model output clusters around a mode (DetectGPT's curvature, DNA-GPT's regeneration agreement). Two find that single signals fail where combinations hold (Ghostbuster's ablations, Fingerprinting's within-family result). None of these convergences was designed as a replication, and none of them measures prose quality — but a claim supported by two methods is stronger than a claim supported by one paper's section heading, and the capability map is built on those overlaps.

### What none of them measures

- **Reader response.** No paper asks whether anyone preferred, finished, remembered, or reread a text. Quality is absent by design.
- **The effect of instruction.** No paper tests a craft method, a checklist, or a revision pass.
- **Long form.** Nothing over a few thousand words; no chapter, no novel, no series.
- **Native non-English prose.** German, Chinese, and Persian appear, but on translated prompts or translated texts. Russian is absent entirely.
- **Mixed authorship.** Ghostbuster and DNA-GPT test paraphrase and revision, but as attacks on a detector, not as descriptions of how people and models actually collaborate.
- **Sentence-level behaviour.** The smallest tested unit is about fifty words under heavy transformation; Ghostbuster calls anything under roughly a hundred tokens unreliable. None tests a line, so no finding here licenses a line-level verdict.
- **Anything causal inside the model.** StoryScope reports what the outputs do, not why the weights produce it. Every mechanism column in `references/ai-narrative-signature.md` is `[hypothesis]` for this reason.

## The four findings that actually shape the skill

### (a) Narrative-level choices are discriminative, and they survive stylistic rewriting

`[data: StoryScope]` The numbers, in order of what they license:

- **93.2** macro-F1 from narrative features alone (257 features, binary human vs AI).
- **96.0** with style features added (304) — so style adds 2.8 points, not the other way round.
- **84.8** from the 30 core features, and **91.1** from core plus fingerprints (101).
- **68.4** for six-way attribution — the task of telling *which* model, not just whether.
- **93.9** after LAMP editing against **95.5** before, on 278 Gemini stories: a drop of 1.6 points.

The LAMP result is the load-bearing one, because it is the only test of durability. Span-level rewriting that removes cliché, redundant exposition, and purple prose does not move the narrative classifier much — the paper's claim is that the choices are structural, and a rewrite that does not restructure them leaves them intact.

**The boundary.** 93.2 is a detection score on a prompt-matched corpus, not a quality score. LAMP used one model as author and rewriter on 278 stories; the edits could not touch subplot count or resolution mode by construction, so the result shows those particular edits do not move those particular features — not that a determined structural rewrite could not. And the reverse inference is forbidden: a draft is not good because it is hard to classify.

**If the transfer fails:** a generation that closes the measured gaps without instruction, or a paired blind evaluation in which narrative-decision coaching loses to prose coaching. Either would move the skill's centre of gravity back to L3.

### (b) Surface signals are fragile under rewriting and language change, and the fragility has an order

`[data: Fingerprinting]` The order, from the eight-way closed-set task with 12.5% chance:

- **Behavioural** (length, layout, punctuation, Markdown): 52.42 raw → 48.78 cropped → 41.88 after formatting removal → **25.59** after case and punctuation scrub. Most of the loss is in the last step.
- **Stylometric** (function words, POS, vocabulary diversity): 60.72 within English → 49.62 after scrub → **19.74** averaged across six translation directions.
- **Lexical** (word and character n-grams): **80.07** raw, the strongest single family, still 67.76 after scrub, **53.94** after full paraphrase — and excluded from cross-lingual tests because it is tied to script.
- **Semantic** (frozen embeddings): 66.04 raw, **30.58** averaged cross-lingual, the most portable family.

`[data: Ghostbuster]` and `[data: DNA-GPT]` agree in direction: heavy paraphrase is the real attack surface for a detector (recall 99% → 62% against a commercial paraphraser; DNA-GPT's ranking survives revision only because both classes lose overlap at once). DetectGPT stays above 0.8 AUROC with a quarter of the text replaced, which bounds the fragility rather than denying it.

**The boundary.** Durability is not importance. Punctuation rhythm dies first under scrubbing and can still be the most deliberate decision in a paragraph. The ordering tells you how much confidence an observation deserves, not how much it matters. It also describes attribution under machine transformations, not human editing.

**Where the sources disagree.** DNA-GPT's black-box score is an n-gram overlap metric, which makes lexical evidence look like the thing that survives; Fingerprinting shows lexical evidence shedding a third of its accuracy under full paraphrase and being unusable across scripts. The measurements are not in conflict — DNA-GPT's ranking survives revision while its evidence spans do not — but the readings are. Narraith resolves it by taking the procedure from DNA-GPT (truncate, regenerate, compare the tail) and the durability ordering from Fingerprinting, and by never treating n-gram overlap as the criterion. The dossier records this in `references/research/04-dna-gpt.md` under Limitations; a maintainer who cites one paper against the other has missed it.

**If the transfer fails:** evidence that human readers weight surface signals more heavily than structural ones when judging quality — which would make durability a poor guide to where to spend revision effort, even though it remains a good guide to where to distrust a claim.

### (c) Interpretable multi-signal diagnosis beats single-signal verdicts, and needs robustness testing

`[data: Ghostbuster]` One signal collapses: document perplexity alone reaches 81.5 F1 in-domain, 49.0 on out-of-domain creative writing, and 13.2 accuracy on one non-native essay set — worse than chance on a balanced set. Handcrafted multi-feature intuition without search reaches 80.5. The structured search over comparisons between four weak models reaches **99.0** in-domain, **97.0** averaged out-of-domain, and **+7.5** over the best prior system under domain shift.

Two qualifications matter more than the headline. Random features still reach 97.8, so most of the gain is "some probability feature, well chosen", not the specific set — selected features are discriminators, not causes. And the method loses one cell it should not: RoBERTa beats it on out-of-domain creative writing, 95.7 to 95.3.

**The boundary.** This is evidence about detector design, not about critique. It supports a *shape*: enumerate candidate explanations, keep the smallest set that survives testing, report where the method fails. It does not support transplanting any feature or quoting 99.0 as validation of a revision method.

**If the transfer fails:** judges agree no better on which defect is present when using the differential procedure than when writing a flat list — the falsification condition H2 in `docs/limitations.md` states for the grid, and the same test applies to the search shape.

### (d) A text close to the generator's mode is the text it would write again

`[data: DetectGPT]` Machine samples sit at a local maximum: step to a meaning-preserving rewrite and the log-probability falls. Detection on 20B GPT-NeoX fake news rises from 0.81 to 0.95 AUROC; across five models the average gain is 0.06, with 14 of 15 combinations won. The effect is weakest exactly where the text is most formulaic: on prompted fiction the margin is +0.01, and with NeoX it is negative (0.93 against 0.95 for the baseline). The paper's own footnote explains why: machine creative writing "tends to be noticeably generic, and therefore relatively easy to detect".

`[data: DNA-GPT]` The same fact from the other side: given the same prefix, model continuations agree with each other far more than human continuations do. Truncate at the midpoint, regenerate, compare — the machine tail lands close to itself. The finding survives heavy revision as a *ranking* (99.09 → 98.48 AUROC when half the tail is rewritten) but the lexical evidence for the rewritten spans is gone.

**The boundary.** White-box or same-model access; paragraph-length units; 2022-era generators. Most importantly, the signal is about origin, not value: a human can write boilerplate, and an unconventional good sentence can sit in a low-probability region. "Close to the mode" is a description of how the text was produced, never a verdict on whether it should have been.

**If the transfer fails:** divergence turns out to be uncorrelated with what readers call authorship, or the continuation test produces contrivance at the rate `docs/limitations.md` H3 predicts. The second is the likelier failure, which is why the protocol caps itself at two rounds and insists on a named licence for every non-modal choice.

### How the four interlock

They are not four independent findings; they are one argument with four joints. (a) says the narrative layer carries most of the measurable difference, so that is where the skill should work. (b) says how much confidence any observation at that layer deserves, and ranks the evidence. (c) says how to reason when several candidate defects are present — enumerate, test, keep the minimal set, report the exception. (d) explains why the defaults exist at all: the model is not failing to try, it is landing on the mode, and the mode is what a probability distribution does when nobody decides.

Remove any joint and the design changes. Without (a), the skill would be prose advice. Without (b), it would treat every observation as equally strong. Without (c), it would list defects instead of diagnosing them. Without (d), it would prescribe novelty instead of decisions — which is the overcorrection the whole skill is built to avoid.

## Research → Capability map

Status says what the *link* is: **measured** when the finding is a result, **inferred** when the capability is our transfer of it.

| Source | Finding (with number) | Capability it grounds | Where it lives | Status |
|---|---|---|---|---|
| StoryScope | Narrative features separate sources at 93.2% macro-F1; 30 features retain 84.8% | Put narrative decisions, not surface style, at the centre of the skill | `SKILL.md` (laws, routing); `docs/architecture.md` §4 | measured separability / inferred priority |
| StoryScope | 10 dimensions, 304 features, all closed-form decisions | The decision vocabulary: agency, revelation, time, subplot, interiority as answerable questions | `templates/decision-ledger.md`; E1–E2 in `methodologies/01-plot-and-causality.md` | measured salience / inferred procedure |
| StoryScope | No subplots in 79% of AI stories vs 57% of human ones; thematic-parallel subplots 21% vs 42% | Subplot gate: a second line must carry its own question, cost, and two intersections | `references/story-architecture.md` §7; W14 in `workflows/05-voice-and-complex-structure.md` | measured gap / inferred rule |
| StoryScope | Protagonist-driven resolution 69% vs 46%; internal-acceptance endings 47% vs 27% | Agency audit of the final movement; ending-mode choice against a baseline | E1, E3 in `methodologies/02-character-and-dialogue.md`; L5/L6 in `references/quality-levels.md` | measured / inferred |
| StoryScope | Narrator states the theme in 77% vs 52%; thematic explicitness 3.94 vs 3.28 | Meaning carried by cost and object; premise written as a question | E1; L4 in `references/quality-levels.md`; `references/story-architecture.md` §2 | measured / inferred |
| StoryScope | Revelation features: recontextualisation 3.28 vs 2.95; nonlinear framing 1.96 vs 1.68 | Information plan: what the reader knows, when, and what the order buys | E6 in `methodologies/01-plot-and-causality.md`; `templates/decision-ledger.md` | measured salience / inferred rule |
| StoryScope | Embodied emotion 81% vs 38%; explicit labels 8% vs 29% | Channel chosen by scene function, not by "show, don't tell" | `references/prose-engineering.md` §9; E9; `examples/07-emotion-three-channels.md` | measured / hypothesis |
| StoryScope | Named intertextual reference 24% vs 47%; balanced mix 16% vs 37% | Specific, checkable reference where the world permits it; no name-dropping | `references/narrative-theory.md` §11; E11 | measured / inferred |
| StoryScope | Character introduction by external description 52% vs 30% | Introduce through pressure, not portrait | E3 in `methodologies/02-character-and-dialogue.md`; W7 | measured / inferred |
| StoryScope | Rarity percentile 0.71 vs 0.49; 24.7% vs 7.1% in the rarest decile | Diversity as a portfolio property, not a per-story target | E12 in `methodologies/04-prose-voice-originality.md`; `references/originality.md` | measured dispersion / inferred practice |
| StoryScope | 93.9 vs 95.5 after LAMP editing (−1.6 on 278 stories) | Revision order: structure before line; line polish cannot move a structural default | `SKILL.md` revision triage; E14 in `methodologies/05-continuity-and-revision.md` | measured edit robustness / inferred order |
| Fingerprinting | Behavioural 52.42 → 25.59; stylometric 60.72 → 19.74 cross-lingual; lexical 80.07 → 53.94 | Durability weighting: confidence falls as evidence moves toward surface form | `references/literary-critique.md` (evidence sufficiency); `references/quality-levels.md` | measured / inferred |
| Fingerprinting | ≈22–27% at 50 words under full paraphrase, ≈50% at full length, chance 12.5% | Evidence-sufficiency gate: no voice or structure verdict from a short sample | `references/literary-critique.md`; E14 | measured (attribution) / hypothesis (craft budgets) |
| Fingerprinting | Semantic transfer 30.58 vs stylometric 19.74 averaged over six directions | Multilingual caution: no English-derived stylistic threshold on Russian | `references/russian-prose.md`; `references/multilingual-notes.md` | measured / inferred |
| Fingerprinting | Constrained tasks collapse attribution: rewrite 35.94, source synthesis 39.38, argument 95.31 | Do not judge voice from a fixed form; name the form before the verdict | `references/literary-critique.md`; W12 in `workflows/05-voice-and-complex-structure.md` | measured / inferred |
| Fingerprinting | Within-family pairs sit at 61.39–72.09 combined; no single dominant signal | Prefer several weak, complementary signals over one strong tell in a critique | E14; `references/literary-critique.md` | measured / inferred |
| Ghostbuster | 99.0 in-domain; 97.0 out-of-domain; +7.5 over best baseline; random features 97.8 | Differential diagnosis: enumerate candidate defects, keep the minimal explanatory set, report the exception | E14; `references/literary-critique.md` | measured (detector) / inferred (critique) |
| DetectGPT | 0.81 → 0.95 AUROC on NeoX fake news; fiction margin +0.01, one loss | Continuation test: name the modal choice, then choose against it on declared axes | E11 in `methodologies/04-prose-voice-originality.md`; `references/originality.md` | measured curvature / hypothesis craft |
| DNA-GPT | 99.09 → 98.48 AUROC under 50% revision; tested at 1,000–2,000 characters; proxy models 69.2–82.3 | Regeneration test as self-audit only, at scene scale, with an explicit length floor | E11 (protocol); W9–W10 in `workflows/04-continuation-and-revision.md` | measured / hypothesis |
| DetectGPT + DNA-GPT | Default output is the output a model would produce again | Originality as default-avoidance, capped at two rounds | `references/originality.md`; `SKILL.md` law 5 | inferred |
| none (craft) | No study measures continuity, memory, or contradiction over long text | Continuity ledgers, knowledge state, debt tracking | E13; `references/continuity-memory.md`; `templates/continuity-ledger.md` | theory |
| none (craft) | No study measures the seven levels as a diagnostic instrument | The L1–L7 grid and the misattribution table | `references/quality-levels.md` | theory |

The two "none" rows are deliberate. A capability map that shows only evidenced rows implies the skill is more evidenced than it is.

When you add a rule that cites a paper, add a row here in the same commit. A row that cannot name a file, an engine, or a workflow is a rule with no home; a row whose status is "measured" but whose capability is a prescription is a category error. The map is the cheapest place to catch both.

### Which engines rest on no measured evidence

Read this before defending an engine by citation. E1, E2, E3, E6, E7, E8, E11, E12, and E14 have a measured finding behind at least one of their rules. E4 rests on one weak contrast (moral ambivalence 38% vs 59%). E5 (relationship dynamics), E9's dialogue technique beyond the philosophical-debate contrast, E10's voice prescriptions, E13 (continuity), and E15 (unreliable narration) rest on craft and narratology only. That is not a defect — most of any writing skill is craft — but it is a fact a maintainer needs when deciding what to test first.

## Confirmed versus inferred

| Confirmed by at least one study | Inferred by us, not confirmed |
|---|---|
| Narrative-level features separate human from model fiction, and are not reducible to style (93.2 vs 96.0; 84.8 on 30 features) | That a draft can be improved by deliberately choosing against those defaults |
| Those choices survive a span-level stylistic rewrite that leaves structure intact (95.5 → 93.9) | That the same choices survive a structural rewrite, or that they are the *cause* of perceived quality |
| Signal families differ in durability, in a stable order across transformations | That the ordering maps onto L1–L7, or that durability implies importance |
| Attribution degrades with shorter text, from ≈22–27% at 50 words | That a human reader's structural judgement has the same length floor, or that 600–800 words is the right budget for voice |
| Multi-signal structured search outperforms single-signal detection (99.0 vs 81.5) | That the same search shape improves a craft critique, or that a minimal defect set is more actionable |
| Model continuations cluster; human continuations diverge | That dramatic equivalence is the right craft analogue, or that unexplained detail is the strongest divergence source |
| Model fingerprints exist and drift with version | That naming a model's defaults helps a writer avoid them |
| Subplot absence differs (79 vs 57), as does resolution agency (69 vs 46) | That adding an intersecting subplot or an external climax improves the story |
| Non-English stylistic transfer is weak (19.74 against 60.72 in-language) | That Russian craft norms are therefore closer to the semantic layer, or that any Russian threshold is calibrated |
| Constrained tasks suppress attribution (rewrite 35.94) | That a sonnet or a mandated beat sheet therefore cannot carry a voice a reader recognises |
| Paraphrase hurts lexical most, in absolute points (11.9 vs 4.3) | That a paraphrase-surviving sentence is a better sentence, rather than a sentence whose meaning is more portable |

Read the right-hand column as the skill's actual bet, and the left as what would have to be true for the bet to be worth making. A rule whose justification sits only in the right column is not dishonest — most craft knowledge lives there — but it must not borrow the left column's authority. When a critique or a README compresses both columns into one confident sentence, that is the failure this table exists to make visible.

## What we deliberately do not claim

- **That any figure describes a single text.** Every percentage is a difference between sampling distributions with heavy overlap. A story can hit every AI-leaning value and be excellent.
- **That human-leaning is better.** 57% of the human stories have no subplot; 27% resolve through internal acceptance; 52% state the theme somewhere. The human baseline is a prior about where defaults cluster, not a target.
- **That the skill has been validated.** There is no intervention study, ours or anyone's. The evaluation in `tests/` is a case series, and `docs/limitations.md` says what it can support.
- **That we detect authorship.** No log-probabilities, no classifier, no surrogate ladder. The signature audit is qualitative and run on the user's own draft.
- **That a detector's F1 measures prose quality.** 99.0 and 93.2 are provenance scores. They are evidence that a difference exists, never that one side writes better.
- **That the findings generalise to novels, series, screenplays, or Russian.** The measured form is the short story; the measured languages are English, with German, Chinese, and Persian in narrow roles.
- **That the durability order is a quality order.** The most fragile signal can be the most deliberate decision on the page.
- **That model fingerprints are permanent.** They are properties of 2026 model versions and will be stale within a release cycle.

## How to cite inside the skill

Three markers, no exceptions:

1. `[data: <Paper>]` — a measured result. Follow it with the figure and the condition that produced it: corpus, task, denominator. `[data: StoryScope]` 93.2% is binary human-vs-AI macro-F1 on narrative features only.
2. `[theory]` — craft or narratology. Most of the skill is this, including its most load-bearing rules. A claim is not weaker for being theory; it is weaker for pretending otherwise.
3. `[hypothesis]` — our inference, with a test that could kill it. `docs/limitations.md` holds the ones the design depends on.

Rules of use:

- **A number needs a dossier.** If a figure cannot be traced to a section of `references/research/`, delete it or find the section. Numbers that arrive without a denominator are the most common failure in research-flavoured writing.
- **A number needs its transformation.** 93.9 is not "after rewriting" in general; it is after LAMP editing of 278 Gemini stories, against 95.5 on the same subset. 25.59 is after case and punctuation scrubbing, not after paraphrase.
- **Detector F1 is never evidence about prose.** It may appear as evidence that a difference exists. It may not appear as evidence that a method improves writing, that a draft is good, or that a reader will prefer something.
- **Cite direction when the prompt suppresses the feature.** StoryScope's 79/57 subplot gap is measured under a ≤120-word premise that cannot ask for a second line. The direction is informative; the size is prompt-shaped.
- **Stamp the version.** Any per-model claim carries the model version and the paper date, or it is folklore.

Three bad citations, and the repair:

- *"Narrative features are 93.2% accurate at detecting AI."* Wrong task. It is a classifier's macro-F1 on a balanced, prompt-matched test set, not an accuracy figure for a single document. Repair: name the task and the denominator.
- *"AI writes 81% of emotion through the body, so avoid the body."* Wrong inference. The figure is a prevalence contrast; the human rate is 38%, so the body is a legitimate instrument at a lower base rate. Repair: state the contrast and the condition.
- *"Ghostbuster proves multi-signal critique works."* Category error. It proves a detector design works on document classification. Repair: cite the shape (candidate sets, minimal explanation, reported exceptions) and mark the transfer as inferred.

**User-facing files are not exempt.** `README.md` and `SKILL.md` do not carry a tag on every figure because tags would make them unreadable, but they must carry the denominator in words: "on a 278-story subset", "narrative features only", "in-domain". A README sentence that compresses two denominators into one comparison is a citation error even if every number is correct.

**Dossier sections are the unit of traceability.** Cite `references/research/01-storyscope.md` §4.1, not the paper's page number. The dossiers were written against the PDFs and their section numbering is stable; page numbers are not, and the paper may be revised. If a figure is not in the dossier, the dossier is incomplete — add it there first, then use it.

## Reading order for a new contributor

1. `SKILL.md` — the doctrine and the vocabulary. Everything else is elaboration.
2. This file — what the evidence covers and where it stops. Read `docs/limitations.md` immediately after; it is the honest half of the same argument.
3. `references/research/01-storyscope.md` — the corpus the skill's centre of gravity comes from. Read the limitations section before the results.
4. `references/research/05-fingerprinting.md` — durability. It governs how much confidence any later claim deserves.
5. `references/research/02-ghostbuster.md` — the method the critique engine borrows: candidate sets, minimal explanations, reported exceptions.
6. `references/research/03-detectgpt.md` and `04-dna-gpt.md` — the originality mechanism. Read them together; they describe the same fact from two sides and disagree about what survives editing.
7. `docs/research-map.md` — the audit: every claim, every figure, every known inconsistency. Read it before editing any file that quotes a number.

A contributor who reads only steps 1–3 will write confident prose with wrong citations. Step 7 exists because that has already happened.

Short route for a writer rather than a maintainer: steps 1 and 2, then the dossier for whichever paper a rule in front of you cites. Do not read all five dossiers to write a scene; read the two that govern the decision you are about to make.

Before changing a number anywhere in the skill, do three things in this order: open the dossier section that owns it; open `docs/research-map.md` and check whether the figure already has a registered denominator; then change every file that quotes it, including the READMEs, in one commit. A number changed in one file and not another is how a repository starts disagreeing with itself, and the disagreement is always found by a reader who then distrusts the rest of the page.

One habit worth copying from the dossiers: write the boundary first and the finding second. A paragraph that begins with what a result cannot support is harder to overstate than one that begins with the result.
