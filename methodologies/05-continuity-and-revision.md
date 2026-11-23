# Continuity and Revision — E13, E14

> Purpose: keep the story's world stable enough to be trusted, and repair a draft by leverage rather than by taste.
> Read when: writing chapter two of anything, continuing someone else's material, changing established facts, or when a finished draft does not work and the reason is not visible in any single sentence.
> Links: `SKILL.md` — the continuity page and the revision triage this engine implements. `references/continuity-memory.md` — bibles, ledgers, sweep procedures in depth. `references/editorial-intelligence.md` — developmental and line editing, repair patterns. `templates/continuity-ledger.md` — the copyable artifact. `methodologies/01-plot-and-causality.md` — E6's ledger is the same instrument seen from the reader's side; E2 for a spine that needs rebuilding. `methodologies/03-time-and-scene.md` — E8's gates are the regression test at scene scale. `methodologies/02-character-and-dialogue.md` — E15 owns contradictions that are deliberate.

## Engine index

| ID | Engine | The question it answers | Section |
|---|---|---|---|
| E13 | Continuity & Memory | What does the story assert, who knows it, and which inconsistencies are errors rather than choices? | [E13](#e13--continuity--memory) |
| E14 | Critique & Revision Planning | What are the two or three defects that matter, in what order, and what will each repair break? | [E14](#e14--critique--revision-planning) |

## Contents

1. [E13 — Continuity & Memory](#e13--continuity--memory)
2. [E14 — Critique & Revision Planning](#e14--critique--revision-planning)
3. [How these engines combine](#how-these-engines-combine)

## E13 — Continuity & Memory

### 1. Purpose

Keep the story's world stable enough for the reader to build a model of it, and turn every inconsistency into a decision. Continuity is not a list of trivia; it is the reader's ability to trust that the text knows its own facts. One contradiction costs more than ten missing details, because a contradiction retroactively makes every earlier detail suspect — including the ones the reader had already used to feel something.

### 2. When to use and when not

Use it from the second chapter of anything, and always when continuing material you did not write: a series, a shared world, a draft someone else started. Use it when a revision changes facts, when multiple POV characters know different things, when the plot turns on money, injury, time or documents, and when a narrator is deliberately unreliable — there you need the ledger in order to know what is bent and what is merely wrong.

Do not use it on a first draft you are still discovering. Track facts after the scene exists, not before, or the ledger becomes a second manuscript and you write toward it. Do not use it on a fragment with no prior material. And do not use it to smooth a deliberate contradiction: some stories are built on one, and the ledger's job there is to record which contradictions are owned, not to remove them.

### 3. Inputs

- The draft, or all drafts and prior chapters.
- Any existing ledgers, bibles, or notes. If none exist, the draft is the only source of truth, and step 1 is the whole job.
- The timeline as the text states it, not as you remember it.
- A list of facts you already know are load-bearing: the ones a character acts on, or the reader could catch.

### 4. Procedure

1. **Extract assertions, one per line, with location.** Dates and durations, ages, injuries and bodies, money, objects, names and forms of address, places and layouts, knowledge, promises and threats. Record only what the text asserts. Do not infer a fact the prose does not state, however obvious it is to you.
2. **Sort into the four ledgers.** Facts, knowledge, debts, names. Anything that fits none of the four — weather, clothing, the colour of a door — goes to a loose column, and the loose column is usually not tracked.
3. **Build the knowledge matrix.** Rows are facts, columns are characters, cells hold the beat where the character learned it and the source: witnessed, told, inferred, assumed. A character who acts on a fact with an empty cell is a knowledge leak. This is the most damaging class, because it reads as the plot cheating rather than as a slip.
4. **Do the arithmetic explicitly.** Birth years from stated ages at stated dates; money as a running balance; injuries with dates and healing windows; travel with distance and time. Write the numbers down. If a constraint window is impossible, at least one input is wrong — find which one before choosing a fix.
5. **Sweep in both directions.** Draft to ledger: every assertion is recorded, and anything missing means you have not extracted it. Ledger to draft: every fact that should appear does appear, and a fact established early and never used is either a plant or a cut.
6. **Classify every hit** as error, retcon, or deliberate unreliability, using the table below. The classification decides the fix, and getting it wrong is how a good contradiction gets smoothed into a dull one.
7. **Fix or mark.** Fix errors at the level of the fact, not the sentence: changing "four weeks later" to "six weeks later" is a fix only if six weeks is what the rest of the story needs. Propagate retcons to every dependent fact. Mark deliberate contradictions as owned, and confirm the second track exists (E15).
8. **Apply the not-track rule.** Delete from the ledger anything the reader cannot check and no character acts on. A ledger longer than the chapter it describes is a clerk's job, and it makes you write toward the ledger instead of the scene.
9. **Set the cadence.** Before writing, read the debt column and the knowledge matrix. After writing, add new assertions and new knowledge states. The debt column first, because promises to the reader are the failures readers remember.

#### What a reader actually tracks

A reader does not hold the whole ledger. They hold what recurs, what is load-bearing, and what surprised them. Three consequences. A fact mentioned once and never used will be forgotten, so a later reliance on it reads as a cheat even though it was established. A fact repeated with variation is remembered precisely, which is where contradictions hurt most. A surprising detail is remembered even when it was never used, so a surprise that later contradicts is worse than a dull detail that does. Track in that order: load-bearing, repeated, surprising.

#### The four ledgers, compact

```
FACTS      id | fact | established (location) | load-bearing? | depends on
KNOWLEDGE  fact id | who knows | since beat | source: witnessed / told / inferred / assumed
DEBTS      debt | opened (location) | owed by → to | must close by | closed?
NAMES      name | spelling | form used by X | never used by Y
```

Three of these earn their place for different reasons. Facts fail as arithmetic. Knowledge fails as cheating. Debts fail as disappointment — the promise the reader was holding when the book ended. Names fail as embarrassment, and only in published text; in a draft they fail as confusion between characters the reader is still learning to tell apart.

#### The knowledge matrix, worked

| Fact | Mira | Ilias (uncle) | Solicitor |
|---|---|---|---|
| F1 the deed is forged | — | — | beat 2, witnessed |
| F2 the uncle signed it | beat 9, told by Ilias | beat 3, did it | beat 2, prepared it |
| F3 the uncle paid the debt | — | beat 3, did it | beat 2 |

Leak check: at beat 7 Mira says the date on the deed is wrong. Her cell for F1 is empty, so the line is a leak. Two repairs. Add a beat where someone tells her, usually around beat 5. Or give the line to the solicitor, who can know. The second is usually better, because the leak exists because the plot needed the line said, not because Mira needed to know — and moving the line keeps her honest.

#### Arithmetic, worked

Mira is 34 in the spring of 1998, so she was born between spring 1963 and spring 1964. Her mother left "when she was six, in the spring of 1970" — the same window, so the two agree. The draft also says she was twelve when her sister was born, and the sister is thirty in 1998: the sister's birth is 1968, which puts Mira's at 1956. That is seven or eight years outside the window, and one of the three statements has to go. Write every constraint as a window, intersect them, and the impossible line names itself.

Money works the same way: *she pays 4,000 for the stock, sells it for 5,200, and still owes 9,000* is a running balance, and the balance must survive every later payment. Injury: a broken ankle in chapter two and a footrace in chapter four are compatible only if the text covers six weeks, and the cast is the clock the reader is holding.

#### Classification

| Class | Test | Action |
|---|---|---|
| Error | No later fact depends on it, and nothing in the text marks it as intended | Fix at the fact level; check that nothing downstream assumed the old version |
| Retcon | The change is deliberate and the story is better for it | Propagate to every dependent fact; in serial publication, leave a trace so returning readers are not silently corrected |
| Deliberate unreliability | A narrator with an interest produced the contradiction, and a second, contradictory track exists in the text | Mark as owned; confirm E15's second track; never "fix" it |

The middle class is where most damage happens, because a retcon that is not propagated reads exactly like an error, and the reader cannot tell which of the two versions to believe.

#### Facts that arrive late

A fact introduced in the last third works harder than one introduced early, because the reader has no model to fit it into. Two rules. If it changes the meaning of earlier scenes, it needs a plant — a detail the reader saw and did not need (E6). If it is merely new, it needs a consequence inside a scene, or it reads as a convenient invention. The test is E6's re-reading sentence: name what an earlier scene now means. A late fact that passes both is a revelation; one that passes neither is a coincidence with a date attached.

#### Cadence

Before each session, read two things: the debt column, because promises to the reader are the failures readers remember, and the knowledge row for the POV character of the scene you are about to write. After each session, extract the new assertions from what you wrote — dates, injuries, money, names, knowledge — and add them. Ten minutes, twice, and it prevents the class of error that costs the most trust. Keep the ledgers as one-liners you can scan; the moment they become prose, they compete with the draft.

#### Serial publication

A serial changes the arithmetic of retcons. Readers hold facts across weeks, so a silent correction is a bet that nobody noticed, and the readers who notice are the ones who care most. Two rules. If the old version is published, prefer a small in-text acknowledgement — a character misremembers, a document is corrected — over a silent fix; it costs one line and preserves trust. If the old version is unpublished, the retcon is free and needs only propagation. Where the change is too large to reconcile, mark it as a new continuity and say so, rather than maintaining two incompatible canons.

### 5. Criteria — what counts as failure

- A character acts on knowledge with no source in the matrix.
- Two load-bearing facts are incompatible, and both are used later.
- The arithmetic does not close: age against date, money against balance, injury against elapsed time.
- A debt is opened and abandoned without being marked as deliberate.
- A retcon has not been propagated: one scene says the shop was sold, another says she still owns it.
- Deliberate unreliability with no second track — which is E15's failure arriving dressed as continuity.
- A fact that exists only in the ledger and never on the page.
- A ledger longer than the chapter, with no ranking of what is load-bearing.
- A retcon propagated to the prose but not to the knowledge matrix.
- A knowledge cell marked "assumed" with no basis in the text for the assumption.

### 6. Typical errors

- **Tracking trivia and missing the load-bearing.** Forty entries about weather and nothing about the date of the hearing, which is the one fact a character's whole plan depends on.
- **Fixing the sentence instead of the fact.** The prose is adjusted to fit the mistake, and three scenes later the mistake is load-bearing and the prose has to be adjusted again.
- **Eyeballing arithmetic.** "About six weeks" passes the eye and fails the calendar. Write the subtraction.
- **The silent retcon.** In a serial, the author quietly changes a fact between instalments. Readers who noticed trust nothing afterwards, and the ones who did not notice are now reading a different story than the one they remember.
- **The ledger as bible.** Writing paragraphs of backstory into the ledger and then writing the chapter toward them, so the chapter becomes a citation of the ledger rather than a scene.
- **Correcting an unreliable narrator.** Smoothing the contradiction is how a narrator with an interest becomes a narrator with a typo.
- **The knowledge leak disguised as intuition.** *She just knew he was lying.* If she cannot know, the intuition is the author's, and the reader feels the hand on the scale.
- **The matrix without sources.** Cells marked "knows" with no record of how. Without the source column the matrix cannot tell a leak from a legitimate inference, and every hit becomes an argument.

### 7. Output format

```
Facts:      <n> entries, <n> load-bearing
Knowledge:  <n> facts × <n> characters, <n> leaks
Debts:      <n> open, <n> closed, <n> abandoned
Names:      <n> variants found
Arithmetic: <window> | <balance> | <injury clock> — pass / fail
Hits:       <id> | <class> | <fix> | <propagated to>
Not tracked: <list>
Verdict:    clean | <n> errors, <n> retcons to propagate, <n> owned contradictions
```

### 8. Micro-example

**Failed:** in chapter two a man's ankle is broken; in chapter nine he runs for a train, and the text says six weeks passed. The injury contradicted the arithmetic, not the reader's patience.

**Repaired:** the timeline sheet gives the break a date, a six-week cast window, and one scene where he tests the ankle on a stair and cannot. Now the run costs something, and the reader who remembers the cast gets a payoff instead of a mistake. Classify before fixing: this was an error, not a retcon, because no later scene depended on him being whole — which is exactly why the fix was cheap and the alternative, changing the elapsed time, would have broken the court date.

## E14 — Critique & Revision Planning

### 1. Purpose

Diagnose a draft with as few defects as possible, order them by leverage, and spend the revision budget on the repair that changes the most downstream text. A critique that lists everything is a critique that changes nothing: the writer fixes the cheap items first, which is exactly backwards, and the structural defect survives into the next draft wearing better sentences.

### 2. When to use and when not

Use it on any draft above a scene; when a draft "does not work" and no single sentence is wrong; before a submission; after a structural change, to check for regression; when a user asks what is wrong and expects a verdict rather than encouragement.

Do not use it on a first draft you are still discovering — write first, diagnose when the draft has an effect to measure. Do not use it when the user asked for a specific local fix and the structure is sound: do the local fix, note the structural observation in one line, and do not hijack the request. Do not use it on your own fresh text without a gap; the effect read is contaminated by memory of intent, and you will diagnose the draft you meant.

### 3. Inputs

- The draft, complete or as complete as it will get.
- The intended length, genre, and audience.
- The decisions the draft was supposed to execute, if they exist: E1's question, E2's load-bearing node, E6's revelation order, the voice contract.
- The budget: how much can change, in time and in words.

### 4. Procedure

1. **Read once for effect, with no pen.** At the end write one sentence: what the text did to you, and the exact line where attention dropped or belief broke. That line is the most valuable piece of evidence in the whole process, and it is destroyed by taking notes during the read.
2. **Read once for structure, answering six questions.** Who wants what? What resists, and why is it right from inside itself? What does it cost? What does the reader know, and when? In what order? Where does the ending land relative to the question? Any question you cannot answer from the text is a structural defect — not a reader failure, and not something the reader should have inferred.
3. **Read once for evidence.** For every structural claim, find the line that proves it. No line means the text asserts what it has not built. Collect the quote and its location; a defect without a quote is an opinion.
4. **Diagnose with a cap: at most two structural defects and three local ones `[hypothesis]`.** More than five means you have not ranked. For each, write the level tag, the evidence line, the decision it violates, and the repair in one sentence.
5. **Order by leverage.** Structure, then motivation, then information, then scene shape, then voice, then rhythm, then words (SKILL.md's triage). Within structure, the defect whose repair changes the most downstream sentences goes first — usually the protagonist's want, the ending's question, or the load-bearing node.
6. **Write the plan.** Defect, repair, scenes touched, predicted risk, test. Cap it at the budget; a plan that requires rewriting everything is a rebuild (see the escape hatch).
7. **Predict the risk of each repair.** Every repair has a second-order effect, and the one you did not predict is the one that shows up in the regression check.
8. **Execute the highest-leverage repair only.** Re-read the changed scenes plus one scene either side. Do not batch repairs: two repairs at once make a regression unattributable.
9. **Run the regression check.**
10. **Stop, or rebuild** if the escape-hatch conditions hold.

#### The three reads

| Read | Attention on | Question | Output |
|---|---|---|---|
| Effect | immersion | where did I stop believing, and where did I stop wanting to? | one sentence plus the exact line |
| Structure | decisions | can I answer the six questions from the text alone? | the questions the text cannot answer |
| Evidence | proof | which line proves each claim? | quotes with locations |

#### What counts as evidence

A quote with a location that shows the defect operating. Three things are not evidence: the writer's stated intention, the reader's summary impression, and a general sense of quality. *It feels rushed* becomes evidence only when you can point to the two paragraphs where a decision happens without a scene. When the defect is an absence — a missing cost, a missing plant — the evidence is the place where the reader would need it, quoted for what is not there. Absence is harder to quote, which is why it is so often skipped and so often the real defect.

#### Severity, not just level

Level says where a defect lives; severity says whether it matters. Four bands. **Fatal:** the story's question is unanswered, or answered by the wrong decision. **Structural:** a scene or an act does not do its job, but the whole survives. **Local:** a passage fails at its own scale without damaging the structure. **Cosmetic:** visible to a careful reader, invisible to the story. Diagnose in that order, and never mix bands in one list — a fatal defect and three cosmetic ones listed together read as four equal problems, which is how writers end up fixing the cosmetic ones.

#### The diagnosis, worked

| # | Level | Defect | Evidence | Decision violated | Repair | Risk |
|---|---|---|---|---|---|---|
| 1 | L5 | The ending answers whether he keeps the shop | final scene: *he signed* | E1's question was whether he becomes his father | make the deed scene turn on the father's approval, not the property | the brother becomes a plot device |
| 2 | L6 | His want is stated once and never dramatised | ch. 1: *he wanted the shop more than anything* | E3: want must be shown in behaviour | give him a scene where keeping the shop costs him the sister | makes him colder |
| 3 | L4 | The letter's meaning is explained twice | end of ch. 6 | E6: one channel per reveal | cut the summary sentence, keep the gesture | none |
| 4 | L2 | Three same-length sentences at the turn | ch. 6, ¶4 | rhythm by function | break one at the decision | none |
| 5 | L1 | *Beautiful* twice in one paragraph | ch. 2, ¶2 | precision | replace with the thing seen | none |

The cap is five rows, and rows 3–5 are held until row 1 is done, because row 1 may delete the scene row 3 is in.

#### Predicting the risk of a repair

| Repair | Common second-order effect | Check |
|---|---|---|
| Cut a scene | Removes a plant or a source of knowledge | E6 ledger: does a later reveal lose its setup? |
| Add a cost | The character becomes unsympathetic | Does an earlier generous act still read? |
| Reorder scenes | A plant now arrives after its payoff | List plants and payoffs by position |
| Change POV | Information the reader needs is no longer available | Re-run E6 for that scene |
| Raise the stakes | The quiet scenes now feel pointless | Does the middle still have a reason to exist? |
| Add a subplot | Dilutes the spine | E2: does it attach at a node and change a cost? |
| Rewrite the ending | The middle no longer points at it | Does the load-bearing node still feed the final decision? |

The table is not exhaustive; it is a prompt. The rule behind it: name the repair's *loss*, not only its gain, before you make it.

#### The regression check

Run all six on the changed material, and on one scene either side.

1. **Scene gate** (E8): does each changed scene still change a state, with a turn someone makes?
2. **Plants and payoffs**: every setup still has its payoff, and every payoff still has its setup.
3. **Continuity diff**: new facts added by the repair are in the ledger, and no old fact was silently orphaned (E13).
4. **Premise**: the ending still touches E1's proposition, in the declared relation.
5. **Effect sentence**: reread the passage where attention dropped. Is it fixed, and has a new drop appeared elsewhere?
6. **Budget**: did the repair add length without adding pressure? A repair that grows the draft by a third and fixes one scene is usually a rebuild in disguise.

#### The escape hatch

Rebuild rather than repair when two or more of these hold.

- Two or more of the six structural questions cannot be answered from the text.
- The protagonist is the wrong person for the question — the draft keeps getting more alive when someone else is on the page.
- The ending answers a different question than the opening asked.
- The premise fails E1, and the draft is long enough that every scene would need to change.
- The repairs keep breaking each other: fixing A breaks B, fixing B breaks A. That pattern means the structure, not the text, is wrong.

A rebuild replaces the spine and keeps the material: re-run E1 and E2, then redraft. It is not permission to avoid a hard structural decision. The difference is that a rebuild states a new spine before writing, and a repair keeps the old one and adjusts the surface.

#### What a rebuild keeps

A rebuild is not amnesia. Keep the scenes that worked as scenes — they can be re-placed; the images and objects that carry charge; the lines whose voice is unmistakably this narrator's; and any research that is still true. Replace the premise, the spine, the ending's question, and the POV if it is the wrong one. Write the new spine before reusing anything, or the old structure will reassert itself through the good material, which is how a rebuild becomes a third draft of the same book.

#### The local pass

After the structural repair has held through the regression check, run one pass for the three local defects, grouped by scene rather than by defect type: read the scene, fix its L4, L2 and L1 items, move on. Do not reopen structure in this pass, even when you notice something — write it into the next diagnosis. A local pass that keeps escalating into structure never finishes, and the draft ends up half-repaired in two incompatible directions.

#### When the critique is for someone else

Give the effect sentence, the two structural defects with their evidence, and one repair to try. Do not present the ledger, the three reads, or the leverage table unless asked. Name the level only if it changes what the writer does next. And do not offer five local notes as a kindness when the structure is broken: the kind version names the expensive problem first and says what it costs to fix.

#### Reading your own work

The effect read is contaminated by memory of intent: you know what the scene was for, so you supply the missing pressure without noticing. Three mitigations. Leave a gap of at least a day, or work on something else in between. Read aloud, which slows you to the page's actual speed. Read the scene away from its neighbours, because a scene often works only because of what precedes it, and alone reveals that it does not stand. If none of these produces a drop point, ask a reader and use their line rather than their opinion — the line is evidence, the opinion is a summary of several lines you cannot see.

#### Re-diagnosing after a repair

A repair changes the diagnosis. After executing the highest-leverage fix, re-run the effect read on the whole draft before touching defect two: the new scene may have answered the second defect, or created a third. Do not carry the old list forward as a to-do queue. That is how a draft accumulates repairs that were each correct against a version that no longer exists.

#### The diagnosis in a long work

A novel cannot be diagnosed in one pass, and should not be. Diagnose at three scales: the whole (premise, spine, the ending's question), the act (two or three parts, each with its own spine), and the chapter, sampled rather than exhaustive. Run the whole-book pass first, because an act-level repair made before the spine is settled is wasted work. Then diagnose the act containing the load-bearing node, repair it, and only then sample chapters. A chapter-level diagnosis of a novel whose spine is wrong produces beautiful chapters in the wrong book.

### 5. Criteria — what counts as failure

- More than five defects listed: an inventory, not a diagnosis.
- A defect with no line evidence.
- A repair aimed at a lower level than the cause — line-editing a structural fault.
- Revision begun at L1 while a structural defect is open.
- No predicted risk for a repair that touches more than one scene.
- No regression check after the repair.
- Repairing when the premise is the defect and the escape-hatch conditions hold.
- A diagnosis that only flatters: every defect local, every note minor.
- A diagnosis that describes the draft's intention rather than its effect. *The scene is meant to show his loneliness* is not a finding; *nothing in the scene requires her to be there* is.
- A whole-book diagnosis performed chapter by chapter while the spine is unsettled.
- A repair executed without naming what it costs the draft.

### 6. Typical errors

- **Line-editing a structural problem.** The most common failure in the whole skill. The prose gets better and the story stays broken, and the second draft is harder to diagnose because the sentences now argue for the wrong structure.
- **"Make it more vivid" as a repair.** Not a repair, a wish. Name the decision: whose agenda is missing, what cost is unstated, which reveal has no plant.
- **Fixing everything at once.** Then a regression appears and cannot be attributed, and the draft is now worse in a way nobody can locate.
- **Treating a deliberate choice as a defect.** Before calling something wrong, state what it costs and whether the story needs that cost. A flat narrator can be a decision; a flat narrator with no reason is a defect.
- **Diagnosing by taste.** *I don't like him* is a reaction, not a finding. Convert it: which decision of his is unearned, and which line shows it?
- **The polite critique.** Naming no defect and praising the atmosphere. It feels kind and costs the writer a draft.
- **Rewriting the ending first.** The ending is the most visible symptom and the last thing that should be touched, because every structural repair changes what the ending has to answer.
- **Diagnosing a novel chapter by chapter.** Beautiful chapters in the wrong book. The spine is settled first, or the chapter work is spent twice.

### 7. Output format

```
Effect:   <one sentence> — drop at <location>
Diagnosis (ordered by leverage):
  1. [L5] <defect> | evidence: <quote, location> | violates: <decision> | repair: <one sentence> | risk: <...>
  2. [L6] ...
Local (held): 3. [L4] ... 4. [L2] ... 5. [L1] ...
Executed: <repair 1 only>
Regression: scene gate <pass/fail> | plants <pass/fail> | continuity <pass/fail> | premise <pass/fail> | effect <pass/fail> | budget <pass/fail>
Next: <repair 2, or rebuild, or stop>
```

### 8. Micro-example

**Failed:** the diagnosis lists eleven problems — three adverbs, a weak simile, an unclear pronoun — and the story still does not land, because the protagonist's want is never dramatised and the ending answers the wrong question.

**Repaired:** two structural defects only: the want has no scene where it costs him, and the ending answers whether he keeps the shop instead of whether he becomes his father. Three local notes are held. The want is repaired first — a scene where keeping the shop requires selling the thing his father built — and the adverb list stays untouched. Predicted risk: the new scene makes him colder; test it against the sister's one generous act, which now has to survive it.

## How these engines combine

E13 first when material exists, because it is mechanical, cheap, and produces evidence E14 cannot get any other way. A contradiction is often the scar of an earlier structural repair: the plot needed someone to know something, so they were given knowledge they never acquired, and the scene reads as cheating. The ledger turns that vague unease into a named defect with a location.

E14 feeds back into E13 through the regression check. Every repair that invents a fact — a new date, a new injury, a new document — must be entered in the ledgers in the same pass, or the repair quietly creates the next draft's continuity error. A common way for a good revision to make a manuscript worse is a repair that fixes a scene and forgets the fact it invented to do it.

The knowledge matrix is shared property. E6 uses it to plan the reader's information; E13 uses it to catch leaks. Run them against each other and the disagreements are informative: E6 says the reader should not know yet, E13 says the character behaves as if they do — one of the two is wrong, and it is usually the scene.

E13's third class, deliberate unreliability, belongs to E15. Do not let E14's repair instinct touch it: the corrective move on an unreliable narrator is to confirm the second track, never to smooth the contradiction. E14 should be able to say "this is owned" and move on, and a diagnosis that cannot make that distinction will sand the most interesting thing in the book into consistency.

E8 is the regression instrument at scene scale: after any structural repair, the changed scenes have to pass the scene gate again, because a repair that fixes the spine can leave a scene whose turn no longer belongs to anyone.

Do not run the full four-ledger sweep on a short story with no prior material. The arithmetic sheet and the knowledge matrix are the two that pay at that length; debts and names matter from the point where a reader has to remember them, which is usually a chapter or two in.
