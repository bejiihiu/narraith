# The AI Narrative Signature: statistical defaults, not sins

> Purpose: catalogue what LLM fiction does by default, with the measured numbers, and turn each default into a diagnostic probe and a calibrated repair — never a blacklist.
> Read when: after a draft exists and you suspect it is competent but anonymous; before writing any rule that begins "avoid" or "never"; when a critique is about to name a defect the evidence does not support.
> Related: `references/research/01-storyscope.md` — the full study and its method; `references/quality-levels.md` — the L1–L7 level each default belongs to; `references/literary-critique.md` — quoting evidence instead of asserting a verdict; `methodologies/05-continuity-and-revision.md` — E14, which receives this audit's output.

## Contents

1. [What this file is and is not](#what-this-file-is-and-is-not)
2. [The one-sentence diagnosis](#the-one-sentence-diagnosis)
3. [The evidence base in six numbers](#the-evidence-base-in-six-numbers)
4. [The defaults table](#the-defaults-table)
5. [The four clusters behind the table](#the-four-clusters-behind-the-table)
6. [The four overcorrections](#the-four-overcorrections)
7. [Calibration, not inversion](#calibration-not-inversion)
8. [Model-specific fingerprints are about models, not about you](#model-specific-fingerprints-are-about-models-not-about-you)
9. [How to run the signature audit](#how-to-run-the-signature-audit)
10. [Boundaries](#boundaries)
11. [Links](#links)

Numbers tagged `[data: StoryScope]` come from Russell et al., COLM 2026. The mechanism column and every repair rule are `[hypothesis]` or `[theory]`: they are inferences from the data, not findings of the study.

## What this file is and is not

This is a catalogue of **statistical defaults observed in one detection study**. Ten narrative dimensions, 304 features, 61,608 stories whose corpus mean is roughly 5,000 words (per-source means run from 2,946 to 6,817), six sources per prompt: one human and five 2026 models `[data: StoryScope]`. Narrative features alone separated human from machine fiction at 93.2% macro-F1, without any stylistic feature `[data: StoryScope]`. That number means the choices are *separable*. It does not mean they are *bad*.

It is not a list of sins. A default becomes a defect only when the scene did not need it. The stated theme that ruins one ending is the entire method of a nineteenth-century omniscient narrator. The bodily emotion that reads as evasion in a drawing-room scene is the only honest channel in a scene of shock. Nothing in the table is forbidden; everything in it is **suspicious when unearned**.

It is not a detector. Narraith does not compute log-probabilities, does not train classifiers, and cannot tell a user whether a text was machine-written. The table is for recognising a pattern in the draft in front of you — not for accusing a text, and never for accusing a person.

What counts as evidence here is narrow: a feature value, a quoted phrase, a location. A feeling that the prose is "AI-ish" is not evidence; it is a symptom looking for a feature. If you cannot point to the decision, you do not yet have a diagnosis, and the correct move is to re-read the scene, not to reach for a repair.

Three rules of use:

- **A feature is not a fault.** Before scoring a feature, write the scene's function in one line: what the
  reader must know, feel, or fear by the end. The feature scores 0 only if that line requires it; otherwise
  it scores 1 and you look for the decision underneath.
- **A single instance is a choice; a cluster is a signature.** One epilogue proves nothing. An epilogue, a stated theme, and an internal acceptance in the same final page is a pattern.
- **The repair is one level up.** If the channel is wrong because the scene has no decision in it, fix the scene (L5/L6), not the sentence (L1).

## The one-sentence diagnosis

**The model over-determines significance and under-determines the world: it resolves the ambiguity a scene should preserve and withholds the concrete particulars a scene should supply.**

That is one failure seen from two sides. On the significance side the evidence is dense: the narrator states the theme in 77% of AI stories against 52% of human ones; resolution is driven by protagonist choice in 69% against 46%; resolution arrives through internal understanding in 47% against 27%; moral ambivalence appears in 38% against 59% `[data: StoryScope]`.

On the world side the same stories name a real text in 24% of cases against 47%, use a balanced mix of explicit and implicit reference in 16% against 37%, address the reader in 7% against 28%, and carry no subplot in 79% against 57% `[data: StoryScope]`. The world is thinner at exactly the points where it would have to be specific, checkable, shared with a reader.

The prose looks literary because it has literature's markers — sensory density, symbolic weather, an epiphany — without the risk that ordinarily produces them. Meaning is asserted where it should be paid for; the world is left vague where it should be concrete. The coupling is our reading, not the paper's `[hypothesis]`, but both halves are measured separately.

Three consequences follow. A story can be *about* something without ever *risking* anything: the theme is the safest thing to add, because it cannot be contradicted by an event that never happens. Ambiguity is expensive — it requires two fully built possibilities — while vagueness is cheap and gets called ambiguity. And concreteness is expensive in a different way: a named book, a real street, a brand, a date can be wrong, so the model avoids the falsifiable.

## The evidence base in six numbers

| Number | What it is |
|---|---|
| 61,608 | stories in the corpus; corpus mean about 5,000 words, per-source means 2,946–6,817 |
| 10,272 | writing prompts, each written by one human and five models |
| 304 | narrative features extracted per story, across ten dimensions |
| 93.2% | macro-F1, human vs. AI, narrative features only `[data: StoryScope]` |
| 84.8% | macro-F1 from just 30 core features `[data: StoryScope]` |
| 93.9% | macro-F1 on Gemini stories after LAMP surface edits (95.5% before) `[data: StoryScope]` |

The 30-feature result is the one that matters for craft: the human/AI boundary lives in a compact set of *decisions* — who acts, what is explained, what is left loose — not in a long tail of stylistic tics. That is why a skill can act on it at all. The 93.9% result is the second: removing clichés and purple prose did not remove the narrative signature, because the signature is structural `[data: StoryScope]`.

### What the study measured

The features come from ten dimensions of the NarraBench taxonomy: agents, social network, event, plot, structure, setting, time, revelation, perspective, and style. The narrative-only model excludes the style dimension and the features flagged as style-dependent, leaving 257 features; the headline 304 includes style `[data: StoryScope]`.

Each feature is a closed-form question with discrete answers, assigned to every story by Gemini 3 Flash. Examples of what that yields:

| Dimension | A question it asks |
|---|---|
| Situatedness | Does the narrator comment on themes beyond the characters? Does the text address the reader? |
| Plot | Is the resolution driven by protagonist choice, mixed, or external fate? Are there subplots, and do they echo the theme? |
| Agents | How are emotions conveyed — labels, embodied metaphors, behaviour, ambiguity? How is the protagonist introduced? |
| Setting | Does the physical environment mirror inner states? Which senses dominate? How fine-grained is the space? |
| Events | How continuous is the single causal chain? Is the resolution external, internal, or unresolved? |
| Temporal structure | How often does the narrative jump across time? How heavy is the anachrony? |
| Revelation | How much does a surprise force a rereading of earlier scenes? When is information withheld? |
| Perspective | How deep is interior access? How often does the narrator address the reader? |
| Social network | Are key scenes dyads or groups? How large is the cast? |
| Structure | Linear, nonlinear, or mixed? What global schema organises the events? |

This matters because the features describe **decisions, not sentences**. A story can be rewritten in different diction and keep the same signature — which is what the LAMP result demonstrated `[data: StoryScope]`. It also means a critique built on these features is arguing about construction, not taste.

## The defaults table

Read a row as: *if this appears, ask the probe before touching the text*. The probe is answerable from the draft alone. The lever is one operation, not a rewrite. The last column is the failure the repair itself produces if applied as a ban. Every comparison is **AI vs. human**, with the AI figure first.

| Default | Evidence `[data: StoryScope]` | Mechanism (why the model does it) `[hypothesis]` | Diagnostic probe | Repair lever | Overcorrection risk |
|---|---|---|---|---|---|
| **Thematic explicitness** — the narrator states the lesson | Thematic explicitness 3.94 vs 3.28 (1–5); narrator comments on theme 77% vs 52%; dialogue as philosophical debate 59% vs 34% | Legibility is rewarded: a stated theme is a completed answer, and completion is the path of least resistance | Underline every sentence that tells the reader what the events mean. Which could be deleted with no loss of information? | Delete the statement; move its content into a cost, an object, or a choice the character makes and regrets | Removing all commentary leaves the reader without a frame; some narrators are supposed to editorialise |
| **Tidy causal chains** | Causal-chain continuity 4.20 vs 3.92 (1–5) | Each next event is chosen for probability given the last; loose ends lower likelihood | Mark the connective between every pair of scenes: *therefore*, *but*, or *and then*. Is there an accident that is never recruited into the chain? | Introduce one cause the protagonist cannot control and do not resolve it; or let a decision produce a consequence that arrives late and off-target | Randomness for its own sake reads as an authorial shrug; a loose end still needs a shape |
| **Single-track plotting** — no subplot | No subplots 79% vs 57%; thematically parallel subplots 21% vs 42% | One goal thread is cheaper to keep coherent across thousands of words | Name every thread that is not the main line. Does any apply pressure to the main line, or are they decoration? | Add one subplot with its own agent and its own cost, whose outcome comments on the main line without repeating it | A subplot added to satisfy a metric is ballast; it must change the main line's odds |
| **Protagonist-driven resolution, internal acceptance** | Protagonist choice drives resolution 69% vs 46%; resolution by internal understanding 47% vs 27% | Therapy-shaped arc vocabulary and conflict-resolution templates dominate instruction data | Who performs the decisive act in the final movement? If the answer is "the protagonist understands something", what did it cost, and who paid? | Make the climax an irreversible external act with a price; or keep the inward resolution but subject it to an external consequence | Forcing external action onto an inward story produces a genre ending glued to a literary body |
| **Embodied emotion (somatic), few direct labels** | Embodied emotion 81% vs 38%; explicit labels 8% vs 29% | "Show, don't tell" is over-represented in writing advice; the body is the most available proxy for interiority | Count body responses and named feelings in one scene. If every feeling arrives as chest, jaw, or breath, what is the character avoiding — and does the text know? | Choose the channel by function (§Calibration); name the feeling when the exact word is the information, or when naming is itself an act | Banning the body yields talking heads; banning labels yields coyness and reader fatigue |
| **Setting as psychological mirror** | Setting mirrors inner state 4.07 vs 3.58 (1–5); ecological emphasis 3.21 vs 2.83 | Pathetic fallacy is a high-frequency literary pattern and a cheap way to make mood legible | Does the weather agree with the character? If you reversed the setting's mood, would the scene still work? | Make the setting resist the character, or stay indifferent; keep one detail that contradicts the mood | Contradicting every mood becomes a mannerism; harmony is sometimes the point |
| **Sensory over-density, especially smell** | Olfactory dominant modality 82% vs 57%; sensory density 3.93 vs 3.66 (1–5) | Sensory detail is taught as proof of vividness; smell reads as unusually specific | Which senses appear? Is each detail there because this POV character would notice it, or because the paragraph needed texture? | Cut sense detail that carries neither information nor point of view; keep one detail only this character in this state would select | Stripping sensory detail produces a sterile report; density is right when the scene is about overload |
| **Vague allusion instead of named reference** | Explicit named reference 24% vs 47%; implicit echoes 72% vs 50%; balanced mix 16% vs 37% | Naming a real work risks factual error; a vague allusion is unfalsifiable and safe | What exactly is being alluded to? Can you name the text, painting, or song? If not, is the vagueness characterising someone or hiding ignorance? | Name the thing, and make the choice of thing characterise the character; or cut the allusion and use the object itself | Name-dropping to look human is costume; a wrong or gratuitous reference is worse than none |
| **Narrator invisibility, rare direct address** | Direct reader address 7% vs 28%; fourth-wall breaking 39% vs 67% (both prevalence rates) | Assistant register suppresses "you"; direct address risks being read as instruction | Is there any moment where the narration acknowledges a listener? Would the story gain from the narrator having an attitude to being told? | Give the narrator a reason to tell: an audience, a withheld fact, a grudge. One address can be enough | Forced metafiction is the loudest artificial tell of all; most stories do not need a visible narrator |
| **Low narrative dispersion / rarity** | Rarity percentile 0.49 vs 0.71 (Cohen's d = 0.83); top-10% rarest 7.1% vs 24.7%; the human story is the rarest of the six 57.8% of the time, against 16.7% chance | Mode-seeking decoding converges on the centroid of the training distribution | Describe the story's central combination of choices in one sentence. Have you read that sentence before? | Change one structural variable at a time — who narrates, what order, what the ending costs — and test whether the change is load-bearing | Novelty for its own sake produces a gimmick; rarity measures distance, not merit |
| **Moral ambivalence deficit** | Morally ambivalent protagonist 38% vs 59% | Preference training rewards resolved, non-upsetting outcomes; safety training avoids endorsing harm | State the protagonist's worst act. Does the text defend it, condemn it, or both? Is there a reading in which they are simply wrong? | Give the antagonist the strongest argument; make the right choice harm someone specific; refuse the verdict in the final line | Ambiguity by omission is mush; both readings need evidence |
| **Front-loaded context** *(DeepSeek)* | Fingerprint: front-loads crucial context other sources defer; narrator visibility is its top attributable feature | A planning prior that establishes stakes before dramatising them | What does page one tell the reader that the character does not yet know? Would discovering it later be stronger? | Withhold one fact the opening explains; let a later scene raise the question that fact answers | Withholding everything produces confusion; a reader needs a question, not a vacuum |
| **Flat escalation** *(Claude)* | Lowest event escalation of the five sources; most uniform narrative voice; continuist stance 62% vs 39–56%; favours epilogues, avoids dream sequences | A restraint prior: avoid melodrama, resolve quietly, extend the ending | Plot event intensity across the story. Does any scene raise the stakes above the previous one, or does the curve flatten after the midpoint? | Build an escalation ladder where each rung costs a different kind of thing; cut the epilogue if it only confirms what the climax proved | Forced escalation produces inflation; quiet endings are legitimate when the pressure was internal and the cost is real |
| **Gossip as plot engine** *(GPT)* | Gossip/rumour as plot mechanism 64% vs 44–55% for other sources; retrospective framing; subverts expectations 41% vs 27–36%; ambiguous reconciliation | Social information is high-probability narrative fuel; talk creates stakes without staging events | How much of the plot arrives as reported speech about absent people? Would it survive if every rumour had to be dramatised? | Convert one rumour into a scene with the person present; let another rumour be false and cost someone | Banning gossip kills social novels; it is a legitimate engine when shown to damage or bind |
| **Bleak settings, tidy denouements** *(Gemini)* | 88% of Gemini stories tagged bleak/oppressive; tidiest endings and extended denouements | Atmosphere as a shortcut to seriousness; denouement as reassurance | Is the setting bleak because the story is, or because bleakness signals literary? Does the ending continue after the question is answered? | Make one location neutral or pleasant and let the harm come from people; end on the last necessary sentence | Brightness imposed as a corrective is tonal dishonesty; the defect is default bleakness, not bleakness |
| **The generic centre** *(Kimi)* | Fewest fingerprint features (3 vs 7–32); lowest six-way F1 (0.55); sits at the centre of the AI distribution | Least distinctive post-training profile among the five | Which three choices in this draft could only belong to this story? If none, the draft is at the centre | Choose one commitment — voice, structure, moral stance — and let it constrain everything else; genericity is a refusal to commit | Forced quirk is not character; distinctiveness must be load-bearing |
| **Character introduced by external description** | Introduced by external description 52% vs 30% | Description is a safe way to establish a character before the risk of action | How is the protagonist introduced? If by a block of description, what does it tell us that a first action could not? | Introduce in action or in another character's reaction; keep one physical detail that will matter later | Withholding all description produces floating voices; some genres require the portrait |

## The four clusters behind the table

Seventeen rows are too many to hold in mind. They collapse into four clusters, and the clusters are what a revision plan should target.

**1. Over-determination of meaning.** Thematic explicitness, thematic unity, moral weighting, philosophical dialogue, protagonist-driven resolution, internal acceptance, the surplus of epilogues. The text keeps answering a question the reader has not been allowed to ask. *If this cluster dominates:* the draft is a thesis with illustrations.

**2. Streamlining of structure.** Tidy causal chains, no subplots, low pre-threat investment, few locations, single track, tidy denouement. The text removes the friction that would make its events feel found rather than assigned. *If this cluster dominates:* the draft is a corridor; every door opens onto the same room.

**3. Performativity of interiority.** Embodied emotion, setting as mirror, sensory density, olfactory dominance, deep interior access. Interiority is rendered as *texture* rather than as *consequence*: the character feels intensely, and the feeling changes nothing. *If this cluster dominates:* the draft is a mood with people in it.

**4. Withdrawal from the shared world.** Vague allusion, no named works, no brands, rare direct address, no fourth wall, few locations, thin dialogue proportion, low moral ambivalence. The text avoids anything that could be checked, contradicted, or argued with. *If this cluster dominates:* the draft is sealed; nothing enters from outside.

The diagnosis follows from the cluster pattern. Clusters 1 and 2 over-determine significance; cluster 4 under-determines the world; cluster 3 is the bridge — interiority performed in place of a world that could resist it. A draft with 1+2+3 high and 4 low is the characteristic AI shape. A draft with 4 high and 1 low is doing something else, and the table should be put down.

Two cautions about clusters:

- **Clusters are not scores.** You are looking for which cluster is *load-bearing*, not for the highest count.
- **A cluster can be a legitimate poetics.** A locked-room monologue may deliberately withdraw from the shared world. The question is whether the withdrawal is chosen and paid for.

### The base rate problem

The human comparison is published literary fiction, and published fiction already has high rates of some features the table treats as suspicious. 57% of the human stories have no subplots; 27% resolve through internal understanding; 52% state the theme somewhere `[data: StoryScope]`. A draft is not defective for sharing a feature with that baseline.

What the model does differently is narrower and more useful: it removes the *option*. The defect is not "no subplot" but "no subplot was ever considered, because the plot arrived already streamlined". The repair is not "add a subplot"; it is "restore the possibility that this story could have had one, and decide".

So compare a draft to its own genre's norms before comparing it to the corpus:

- A literary novella with one thread is not fixed by bolting on a subplot; it is fixed by making the single thread carry more pressure.
- A quiet ending is not fixed by an escalation; it is fixed by making the quiet cost something on the page.
- A first-person narrator who never addresses the reader is not fixed by an aside; most first-person narrators don't.

Use the human percentages as a **prior**, not a target. A prior tells you where to look; a target tells you what to fabricate.

### Default or decision?

The same feature can be either. This is the distinction the whole file exists to protect.

| Signal | Looks like a default when | Looks like a decision when |
|---|---|---|
| Narrator states the theme | It restates what the scene already showed, and nothing contradicts it | An unreliable or tendentious narrator is characterised by the statement |
| Emotion rendered in the body | The same chest/jaw/breath cluster recurs with no new information | The body says something the character cannot, and the scene knows it |
| No subplot | Nothing in the story could have been a second thread | The single thread is pressured from several directions and the exclusion is felt |
| Epilogue | It confirms what the climax proved | It changes the meaning of the climax by showing its cost over time |
| Named reference | It is there to signal erudition, and the character would not know it | The choice of reference reveals the character's formation or evasion |
| Time jump | It skips research or arrives because the information is due | It withholds an answer the present scene has just made urgent |
| Bleak setting | The weather agrees with the mood and nothing else | The bleakness is indifferent to the character, or actively hostile in a way that costs |
| Ambiguous ending | Neither reading has evidence | Two readings each have evidence and the text refuses to choose |
| No direct address | The narrator has no reason to know they are being read | The narration is shaped by an implied listener, even without the word "you" |

The last five rows of the defaults table are fingerprints, not core defaults: they describe particular 2026 models rather than the shared AI profile. Read them as variants of the same failure, not as five extra sins. A draft can carry none of them and still be over-determined; a draft can carry one and be fine because the scene required it.

## The four overcorrections

Every repair in the table can be applied as a ban. Applied as a ban, each produces a new and more embarrassing failure. The rule is never "stop doing X"; it is "stop doing X **by default**". A ban is a default with the sign flipped: it replaces one unexamined choice with another, and it usually removes the technique that was carrying the scene's information.

**(a) Banning somatic emotion → disembodied talking heads.**

- *The ban:* never render feeling through the body; it is a cliché.
- *What it produces:* characters who discuss their states like case studies, and scenes where grief is a topic rather than an event.
- *Calibrated rule:* the body is for affect the character cannot process, will not name, or is actively defending against. It is not a general substitute for interiority. Keep one labelled or behavioural anchor per scene so the reader can calibrate the body's signals `[theory]`.
- *Test:* if the chest tightens in three consecutive scenes, the body has stopped being evidence and become a tic.

**(b) Banning explicit emotion words → coyness and reader fatigue.**

- *The ban:* never name a feeling; naming is telling.
- *What it produces:* a character who never says "ashamed" when shame is exactly the point, and a reader doing work the scene has already done.
- *Calibrated rule:* name the feeling when the precise word is the information (shame is not grief; envy is not admiration), when the character is self-diagnosing, or when naming is itself a social act — a confession, a diagnosis, a cruelty `[theory]`.
- *Test:* substitute the label for the metaphor. If both carry the same information, the label is shorter and the metaphor is decoration.

**(c) Forcing nonlinearity → arbitrary chronology.**

- *The ban:* linear chronology is an AI tell; jump time.
- *What it produces:* a flashback inserted because the information is due, a frame that exists to look literary, a timeline the reader has to reconstruct for no return.
- *Calibrated rule:* reorder only when the order of telling changes what the reader can infer at each point. Every anachrony must be raised by a question the present scene has just created; if chronology can be restored with no loss, restore it `[theory]`.
- *Test:* restore chronological order on a copy. Name what is lost. If the answer is "smoothness", the nonlinearity was decoration.

**(d) Forcing ambiguity → unresolved mush.**

- *The ban:* resolve nothing; ambiguity is literary.
- *What it produces:* an ending that refuses a verdict it never earned, and two readings with no evidence for either.
- *Calibrated rule:* ambiguity is the presence of two answers, each with evidence, not the absence of an answer. Write both readings in one sentence each and list the textual evidence for each `[theory]`.
- *Test:* if you cannot state the two readings, you have vagueness; the repair is specification, not more fog.

## Calibration, not inversion

Use the table in this order:

1. **Name the scene's function.** What must the reader know, feel, or fear by the end of it? (E8, scene card.)
2. **Choose the channel that performs that function.** There are three: **labelled**, **enacted** (body, action, or speech-as-behaviour), and **oblique** (juxtaposition, displacement, omission). Each is good at different work; the named variants below are routes within them.
3. **Check whether the default has crept in as a substitute.** The question is not "is this a body response?" but "is this body response doing the job the scene needed?"
4. **Repair one level up.** If the channel is wrong because the scene has no decision in it, fix the scene, not the sentence.

| Scene function | Default channel | Why it fits |
|---|---|---|
| Shock or dissociation without a witness | Enacted (the body) | The body reports before the mind edits, and there is no one to perform for |
| Social shame, status injury, self-diagnosis | Labelled | The exact word distinguishes neighbouring states |
| Concealment, family or class reticence | Oblique | The gap between feeling and speech *is* the subject |
| Physical danger | Enacted + short syntax | Attention narrows; the sentence should too |
| Self-deception | Oblique + a wrong label | The character names the feeling incorrectly, and the text lets us see the error |

The same beat, three ways. In each, Ines has just been rejected.

**Enacted (the body)** — *fits dissociation or shock without a witness; the character is defended and the reader sees the cost before she admits it.*
> The letter was one page. Ines read it twice, then found she was standing, though she did not remember standing, and the kitchen tap was running, and her jaw ached from a clamp she had put on it somewhere between the first line and the second.

**Labelled** — *fits social shame or self-diagnosis; the exact word is the revelation, and the scene's job is precision.*
> Ines read the rejection twice. She was not sad, exactly; she was embarrassed, which was worse, because embarrassment had no dignified way of being shown, and she had been rehearsing grief for a week.

**Oblique** — *fits concealment; the scene is about what the family will not say, so the feeling must stay under the words.*
> Ines folded the letter along its existing creases, put it back in the envelope, and asked her mother whether there was any of the good tea left. Her mother looked at the envelope and said there was.

None of the three is more literary. The first fails in a scene about a family that talks; the third fails in a scene about a woman alone; the second fails in a scene where the character does not yet have the word.

### Four misreadings the numbers invite

- **"AI uses smell more, so cut smell."** Olfactory dominance is 82% vs 57% `[data: StoryScope]`, but the feature measures which modality *dominates*, not whether smell appears. A scene in a fish market without smell is a scene written by someone who has not been to one. The question is selection by point of view, not the sense itself.
- **"Humans break the fourth wall, so break it."** 67% vs 39% is a prevalence difference in published fiction `[data: StoryScope]`, and most stories in both groups still do not. A forced aside is worse than an invisible narrator; the feature is a permission, not an assignment.
- **"Humans are rarer, so be strange."** Rarity is distance to near neighbours in feature space, not merit; 7.1% of AI stories also sit in the rarest decile, and a rare story can be unreadable `[data: StoryScope]`. Use rarity to check whether a choice was made or inherited, not to justify a gimmick.
- **"AI resolves internally, so force external action."** 27% of human stories also resolve through internal understanding `[data: StoryScope]`. The defect is not the mode; it is the mode arriving without cost. A protagonist can understand something and lose the workshop anyway.

Calibration is not:

- **Neutrality.** Choosing a channel is not refusing to judge; it is judging the scene's job instead of the technique's reputation.
- **A quota.** "One label per scene, two body responses per chapter" is a new default with extra steps.
- **A defence of the status quo.** If every channel is equally available, the draft still has to choose one and pay for it.

## Model-specific fingerprints are about models, not about you

The per-model findings describe five generators as they existed in 2026: Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2, Claude Sonnet 4.6, GPT-5.4 `[data: StoryScope]`. They are relative to each other, measured on one prompt set, and will drift with the next version. Kimi's "generic centre" is a fact about Kimi's position among those five, not a property of any text you are writing.

A skill must not teach a model to "sound like Claude" or to "avoid sounding like GPT". That is fingerprint cosplay: it encodes a dated statistical profile as a target and calls the result voice. It also violates the doctrine — build a text that has a reason to be as it is; do not build a text that dodges a classifier.

Use the fingerprints only as **self-recognition probes**, phrased as questions about your own draft:

- **Claude probe:** has the escalation flattened because the story is quiet, or because I avoided the scene where someone raises the price? Does the epilogue confirm anything the climax did not already prove?
- **GPT probe:** is this rumour load-bearing social machinery, or the cheapest way to create stakes without staging them? Does the story keep looking backward because the present is thin?
- **Gemini probe:** is this setting bleak because the story is, or because bleakness is my shortcut to seriousness? Does the ending continue past its own answer?
- **DeepSeek probe:** did I explain this on page one because the reader needs it, or because I did not trust the scene to raise the question later?
- **Kimi probe:** if I deleted the names, would anything in this draft tell you it was mine?

The warning has a second edge. Just as there is no merit in sounding like a model, there is no merit in sounding unlike one. Inserting a brand name, a fake fourth-wall aside, or a random flashback to satisfy a human-leaning feature is inverted snobbery, and it produces a text that is artificial in a different direction. The study measured *published human fiction*, not "human behaviour"; copying its surface markers is still copying.

## How to run the signature audit

Run this on a finished draft, not on an outline. It takes twenty minutes and produces two decisions, not a report card.

1. **Sample three passages.**
   - The opening 200 words.
   - The middle of the scene that carries the most weight.
   - The final 200 words.
   - If the draft is under 1,500 words, use the whole thing. Do not sample only the passages you like.

2. **Score the twelve shared defaults 0–2 per passage.** The five model-fingerprint rows are self-recognition probes, not scored items: a draft is not graded on whether it resembles a particular generator.
   - 0 = absent.
   - 1 = present and doing a job the scene requires.
   - 2 = present as a default, with no scene function that requires it.
   - Score the passage, not your intention. A beautiful sentence that states the theme still scores 2 if the scene did not need the theme stated.

3. **Write one line of evidence for every 2.**
   - Quote at most eight words and give the location.
   - If you cannot quote it, it is not there; lower the score.
   - "The mood was heavy with unspoken grief" is evidence of a stated mood, not of subtext.

4. **Read the three passages against each other.**
   - A default that appears in all three is a signature; one that appears once may be a choice.
   - Look for the cluster (§The four clusters), not the count.
   - Ask which cluster is load-bearing: which one, if removed, would change the story most.

5. **Pick the two highest-leverage defects.**
   - Prefer the one at the highest structural level: an L5 or L6 defect outranks an L1 defect even when the L1 defect is more visible (see the interaction map in `references/quality-levels.md`).
   - The second is the defect whose repair changes the most downstream text.
   - If both candidates are at L1, you have probably misdiagnosed; look for the scene or character decision underneath.

6. **Hand the two to E14.**
   - Supply: passage, defect, level, evidence quote, proposed lever, and one invariant — what must not change in the repair.
   - E14 turns them into the revision plan. Do not line-edit from this table directly.

Two structural, three local — not five all at once. A revision plan with five structural defects is a wish list, and a writer with five open fronts fixes none of them. The first defect is the one at the highest structural level; the second is the one whose repair changes the most downstream text. If the two interact — a stated theme that exists because the scene has no decision — write them as one defect with two symptoms, and give E14 the scene-level repair.

**Compute nothing.** Do not sum the scores, average them, or convert them to a percentage. The numbers are attention allocators, not measurements. A draft with six 2s in one scene and none elsewhere is a different problem from a draft with one 2 in every scene, and an average erases exactly that difference.

### Worked scoring

Four snippets from different drafts. Score only the default named; ignore the others.

> "She finally understood that the sea had never been the point."

Thematic explicitness: **2**. The sentence states the lesson, and there is no unreliable narrator to make the statement a characterisation. The scene has already shown whatever the sea was; this repeats it as a verdict.

> "Mr. Okonkwo ran the only garage in town and had once charged a widow nothing for a clutch."

Character introduction: **0**. The character arrives in an action and a reputation, not a description block. The detail is concrete and will plausibly matter later.

> "The town was dying, and the rain had not stopped for eleven days, and Mara felt the damp in her bones like a verdict."

Setting as mirror: **2**. Weather, town, and body all agree; the simile ("like a verdict") is the narrator explaining the mood the scene has not earned. Somatic emotion: **1**, because the damp is a real physical condition of the place, not only a metaphor.

> "It reminded her of a painting she had seen once, somewhere."

Vague allusion: **2**. The reference cannot be named, so it cannot characterise anyone's formation; it exists to signal that the character has an inner life.

The point of the exercise is not the score. It is that each 2 has a quote, and each quote points to a different lever: delete a verdict, cut a mirror, name a thing.

The audit is not a grade, a detector, or a substitute for reading the draft aloud. It is a way of allocating attention: three passages, twelve scored defaults, two defects. If the audit produces a clean sheet on a draft that still feels dead, the problem is outside its scope — premise, structure, or a scene that has no reason to exist — and belongs to E1, E2, or E8.

## Boundaries

- **Detection is not quality.** 93.2% macro-F1 means the narrative choices are separable from published human fiction. It does not mean AI stories are worse, and it does not mean a human story with these features is bad. The classifier has no access to merit.
- **The human baseline is published literary fiction.** Human stories come from Books3, mean 6,403 words, selected and edited for publication `[data: StoryScope]`. "Human" here means professional canon-adjacent short prose, not a random sample of people. That is convenient for us — it is the target — but it is not a universal human norm.
- **The prompts were reverse-engineered from the human stories.** Gemini 2.5 Flash inferred a premise from each human story, and all six sources wrote to that prompt `[data: StoryScope]`. The design controls content, but it also narrows what counts as an AI default: the models were asked to mirror a human plot, not to invent freely.
- **Five models, one year.** The fingerprints belong to specific 2026 versions. A model update can move a feature; the core human/AI separation is the more durable claim, and even that is a claim about this corpus.
- **Features are model-extracted.** Gemini 3 Flash assigned the 304 features; human agreement on a 240-item validation set was mean Cohen's κ = 0.84 `[data: StoryScope]`. Feature-level error exists, especially on scales and on setting.
- **Correlational, not causal.** Nothing here shows that stating a theme *causes* a story to be worse, or that adding a subplot *causes* it to be better. The causal direction is our craft hypothesis.
- **The edit-robustness test is narrow.** LAMP removed surface artifacts from 278 Gemini stories, and the narrative classifier still scored 93.9% against 95.5% on the unedited versions `[data: StoryScope]`. That shows narrative signal survives *that* kind of editing; it does not show that structural revision cannot change it.
- **Scope.** English, short fiction, roughly 5,000-word targets, no poetry, no drama, no novels, no non-English prose. Topic effects were not significant overall (H = 4.69, p = 0.46), but mystery/detective had the lowest binary score at 90.0% `[data: StoryScope]` — treat genre-specific numbers with more caution, not less.
- **Length is a real boundary.** The features were extracted from stories averaging about 4,753 words `[data: StoryScope]`. Flash fiction may not contain enough events for subplot or temporal features to be meaningful; a novel has too many to be scored as one unit. Apply the audit per scene or per chapter, not to a whole book.
- **The classifier was trained on a 5:1 class balance.** Base rates in the corpus are not base rates in your draft, and the model's macro-F1 is not a probability that any given text is machine-written. Do not quote 93.2% as a likelihood.
- **No measure of reader response.** Nothing in the study measures immersion, pleasure, memorability, or sales. The features are structural descriptions; the effect on a reader is inferred, and the inference is ours.
- **The human sample is curated, not random.** Stories were extracted from short-story anthologies identified by running Gemini 2.5 Flash over titles and blurbs in Books3 `[data: StoryScope]`. That is prize-adjacent, canon-shaped fiction, not a cross-section of everything people write.
- **The features are correlated, not independent.** No single dimension is necessary or sufficient: the best single dimension (agents) reaches 80.2% macro-F1, and the worst leave-one-out costs 1.2 points `[data: StoryScope]`. A draft can score high on one cluster and low on another, and the profile matters more than any row.
- **"AI" in the table is an average of five models.** The AI column means across Claude, DeepSeek, Gemini, GPT, and Kimi `[data: StoryScope]`. No single model may match the average, which is why the model rows exist. When a number matters, check whether it is a shared default or one model's fingerprint.

## Links

- Paper: Russell, Rajendhran, Pham, Iyyer, Wieting. "StoryScope: Investigating idiosyncrasies in AI fiction." COLM 2026. https://arxiv.org/abs/2604.03136
- Code and feature set: https://github.com/jenna-russell/storyscope
- Full extraction, tables, and limitations: `references/research/01-storyscope.md`
- Where each default lands in the quality grid: `references/quality-levels.md`
- How to quote evidence in a critique: `references/literary-critique.md`
