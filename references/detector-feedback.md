# Detector Feedback: Using a Report Without Obeying It

> Purpose: turn a machine-text detector's report into a craft diagnosis, and refuse the two failure modes it invites — panic rewriting and score-chasing.
> Read when: a user brings a detector verdict, a publisher or school asks whether a text is "AI", or a draft is well made and still reads statistically typical.
> Related: `references/ai-narrative-signature.md` — the catalogue of model defaults; `references/russian-prose.md` — the checks that diagnosed this case; `scripts/story_metrics.py` — the proxies named here; `docs/limitations.md` — what a detector cannot establish.

Tags in this file: `[report: vendor, date]` means a third-party measurement of one specific text, not a research finding. `[theory]` and `[hypothesis]` mean what they mean everywhere else.

## 1. What a report actually says

A detector returns a verdict and a set of fragments marked as likely machine-written. It does not return the feature that triggered the mark, a confidence interval, or a reason you can audit. Textovod's report of 2026-11-23, run on a Russian short story written for this skill, states 57% "explicit AI signs" and 43% "suspicious fragments", verdict: generation detected `[report: textovod, 2026-11-23]`. The same page claims 99.3% recall and 98.9% specificity on the vendor's own test set. Treat that as a vendor claim about a benchmark you cannot inspect, not as a property of your text.

The useful part is not the percentage. It is the fact that a classifier trained on distributions found the text statistically close to generated prose. That is a *description of the surface*, and it can be true of a well-made story.

## 2. Case file

The text: 884 words, 5,627 characters, Russian, a single evening in the life of a server administrator. Written under this skill, deliberately sparse.

What the report said: **57% explicit + 43% suspicious = 100% flagged**.

What the text measured:

| Metric | Value | Skill check it touches |
|---|---|---|
| sentences over 35 words | 0% | Russian checklist: "at least one periodic sentence per page or two" — failed |
| sentences at 6 words or fewer | 34.9% | fine alone; a problem as a run |
| paragraph-initial pronoun (*он / она*) | 21.9% (7 of 32) | "pronouns dropped" — failed at paragraph level |
| one-sentence paragraphs | 18.8% (6 of 32) | no rule; a rhythm tic |
| mean paragraph length | 27.6 words (sd 12.8, median 26) | uniformity, not a rule |
| repeated 4-grams | 1 | clean |

The diagnosis is uncomfortable and precise: **the story violated two of the skill's own Russian checks**, and the detector noticed the same statistics those checks exist to catch. The prose was not purple, not abstract, not sentimental — it was *uniform*: a run of short declaratives, a third of the paragraphs opening on the same grammatical subject, no period anywhere.

## 3. What the case shows, and what it does not

It shows that avoiding the catalogue in `references/ai-narrative-signature.md` does not make a text pass a detector. The catalogue covers *narrative and semantic* defaults — stated themes, tidy causality, somatic emotion. A detector can also key on *rhythmic* defaults that the catalogue does not list: uniform sentence length, repeated openings, even paragraph size.

It does not show that the story is bad, or that the detector is right about authorship. Both can be true at once: the statistics are typical of generated prose, and the text was written by a person making deliberate choices. A detector measures typicality; a reader measures effect.

The third thing it shows is a limit of the artifact: the PDF marked fragments in colour, and colour is lost in text extraction. Without the HTML report, fragment-level attribution is guesswork. If fragment detail matters, ask for the HTML result, not the PDF.

## 4. The four statistical suspects

When a report gives no usable fragments, check these four. Each has a repair that is also a craft improvement — that is the filter. A repair that exists only to move a number is forbidden.

| Suspect | Measure | Craft repair | When the pattern is legitimate |
|---|---|---|---|
| Sentence-length uniformity | share over 35 words, standard deviation | build one periodic sentence per page or two, where it carries a complex thought; keep short sentences for landings | a hard-boiled or *сказ* narrator, a child's view, a scene about exhaustion |
| Subject-initial monotony | share of sentences and paragraphs opening on a pronoun | front the adverbial, start on the object, use a dash construction, let the verb carry the subject | deliberate anaphora, a list, a ritual |
| Paragraph uniformity | mean, median and spread of paragraph length; one-sentence share | let the paragraph follow attention: merge where the beat continues, break where it turns | a scene built on clipped beats (a fight, a panic) |
| Lexical and syntactic repetition | repeated 4-grams, repeated sentence openers | vary the opening, not the noun; Russian repeats key words on purpose | motif, refrain, deliberate return |

## 5. Procedure

1. **Freeze the version.** Save the exact text that was checked. A report about an unknown revision is useless.
2. **Harvest the fragments.** If the report marks spans, list them. If it gives only a percentage, say so and go to step 3.
3. **Run the metrics.** `python scripts/story_metrics.py draft.md` gives sentence distribution, paragraph counts, pronoun-initial share, repeated n-grams.
4. **Classify each suspect.** *Double defect* (detector and craft agree), *deliberate* (the pattern does work), or *unknown* (needs a reader). Write the classification down.
5. **Repair only double defects, one at a time.** Keep a copy before each change. Do not touch the deliberate ones.
6. **Re-measure and report.** State what changed, what was kept and why. Never present the new score as a result; the score is the detector's opinion, not your work.
7. **If the user's requirement is "must pass detector X", say what that means.** This skill can make prose less statistically typical. It cannot guarantee a pass, and chasing one produces a text optimised for a classifier rather than a reader.

## 6. When the flag is not a defect

- **A flat narrator.** Platonov's syntax, a *сказ*, a hard-boiled register, a child reporting what he saw. The uniformity is the voice.
- **A scene of exhaustion or shock.** Short declaratives, no subordination, repeated openings — the rhythm is the experience.
- **A deliberate refrain.** The same sentence returning with a changed sense.
- **A translated or non-native text.** The detector may be reacting to interference, not to generation. Flagging it as AI is a false positive with a real cost.

The test is not "does the pattern exist" but "does the pattern carry meaning". If explaining why it carries meaning takes longer than the passage, it probably does not.

## 7. What never to do

- **Synonym churn.** Replacing concrete nouns to look less typical removes precision and changes nothing structurally.
- **Injected errors.** Random typos, comma splices and fragments are not a human signature; they are damage.
- **"Humaniser" paraphrase.** Rewriting until the score drops usually flattens voice and can invert meaning. If a tool did the rewriting, the result is a machine paraphrase of a machine text.
- **Score-chasing as a goal.** A text optimised against one classifier is a text with a new tell, for the next one.
- **Presenting a pass as a certificate.** Passing means one detector, on one day, did not object.

## 8. Boundaries

One vendor, one language, one text, one date. Detectors are trained on distributions that shift as models change; their published accuracy figures are benchmark claims, not guarantees. False positives fall hardest on non-native writers, translated prose, and minimalist styles. A human text can be flagged; a generated text can pass. Neither outcome settles whether the prose is worth reading.

The reverse error is just as bad: treating a detector's silence as permission to write the generic version. The catalogue in `references/ai-narrative-signature.md` remains the better guide, because it describes decisions rather than statistics.
