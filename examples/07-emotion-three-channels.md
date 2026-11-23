# One death, three channels: the same beat labelled, enacted, oblique

> Purpose: show the emotion-channel decision on one beat, so the choice can be made by scene function instead of by the "show, don't tell" reflex.
> Read when: a death, a diagnosis, a betrayal, or any shock is on the page and you are about to reach for the body; also when a draft names feelings and you are about to cut every label.
> Related: `references/prose-engineering.md` — the three-channel table and the stacking failure; `references/ai-narrative-signature.md` — the 81/38 and 8/29 numbers and the overcorrection; `checklists/scene-gate.md` — the state-change test each version is judged by.

## What this example tests

Whether you can tell the three channels apart *as decisions* rather than as quality levels, on a beat where the obvious literary move (body, weather, the shopkeeper's radio) is also the statistical default. All three versions are competent prose. The difference is what each one asks the reader to do, and what each one leaves changed.

## Setup

Ray, forty-six, is in Bishop's hardware on a Saturday morning, buying fittings for a gate: forty 40mm screws, clear sealant, a spare blade — crosscut, for a ten-inch saw. His sister Deborah calls. Their father died an hour ago. The list in his hand is correct and complete.

## Version A

*Labelled: the feeling named exactly, and the naming is the event.*

He took the call by the paint mixer, because the shop was loud and he did not want to be the man on the phone in the middle of the floor. Deborah said it in the order she had rehearsed. Ray said, "Right." Then he said, "When?" His voice came out in the voice he used for the rep from the timber yard, and he heard it do that, and he was ashamed of it, which surprised him more than the news did. He was not sad yet. He knew what sad was like and this was not it; this was the feeling of a room after someone has moved the furniture out. He said, "I'll ring you back." Deborah said, "Don't." He said, "I'll ring you back," and she hung up. He looked at the list. Forty 40mm screws, a tube of clear sealant, a crosscut blade for the saw. He read it twice. The list was still correct. That was the part he could not get past — that it was still correct.

## Version B

*Enacted: the body and the room report the feeling, and nobody names it.*

The fluorescent tube over the screws ticked. Ray stood with the phone at his ear and felt the cold come up through the concrete into his heels, and then his jaw set, and his tongue found the ridge behind his front teeth where he always held it when he was lifting something heavy. The shopkeeper was watching him. Ray could see him watching, in the convex mirror in the corner, a small reversed man floating in the glass. Rain went down the window in ropes. His hand closed on the box of screws and the cardboard gave along one corner and the screws shifted inside with a sound like gravel. He heard his own breathing and tried to make it quieter. "Ray," Deborah said. "Ray." The tube ticked. Behind him the shopkeeper's radio gave the football results, half-time, a score he did not take in. Ray stood in the aisle with his jaw locked and the box going soft in his hand, and the rain came on the glass, and he did not move, and he did not put the phone down, and the light kept ticking overhead.

## Version C

*Oblique: the feeling is never named and never performed; the text attends to the purchase.*

He put the phone in his pocket and read the list again. "Forty of the forty-mill," he said. The shopkeeper came down the aisle with a box and set it on the counter. "And a blade for a ten-inch saw." "Ripping or crosscut?" "Ripping." The shopkeeper found one and laid it beside the screws. "That's the lot?" the shopkeeper said. "Grand," Ray said, though it was not an answer to anything, and the shopkeeper waited a moment longer than the question needed. "Do you do keys?" Ray said. The shopkeeper said they did keys. "How long do they take?" "Ten minutes, if the machine's not busy." "Right," Ray said. "I'll come back for the keys." He paid for the screws and the sealant and the blade, and carried the bag out to the van, and sat in it with the engine off. The gate was a two-hour job. He put the bag on the passenger seat and drove home the long way, past the hospital, and did not stop.

## Which channel for which scene

| Version | Channel (labelled / enacted / oblique) | Scene function it fits | Where it fails |
|---|---|---|---|
| A | Labelled | Self-recognition: the character's relation to his own feeling is the drama, and the precise word does the work — *ashamed* is not *sad*, and a man who audits his own voice is characterised by the audit | When the label is the conclusion the scene was supposed to earn; here it survives only because the label is the unexpected one and the list contradicts it |
| B | Enacted | Solitary shock, dissociation, or a body that is the site of the conflict — pain, exhaustion, panic, the moment before passing out | Here there is a witness: the scene's real material is a man managing being seen, and the body inventory turns the reader into a spectator of suffering instead of a reader of management |
| C | Oblique | Concealment, male reticence, a POV defended so hard the narration will not look at the thing | If the reader has no way to know the purchase is wrong; without the setup, this is a man buying a saw blade and asking about keys |

1. **Name the function before the channel.** By the end of this scene the reader must know what Ray is like when he is hit. That is a fact about character, not about grief, and it decides the channel.
2. **Run the witness test.** Someone is watching. A witness pushes the scene toward labelled or oblique, because the character's management of his face is now the action; the body is what he is trying not to show, so putting the camera on the body is putting it in the wrong place.
3. **Run the state-change test on each version.** A changes what Ray knows about himself; B changes only the reader's sympathy; C changes what he owns, what he has admitted to a stranger, and the fact that he drove past the hospital without stopping. If the chosen channel leaves the state unchanged, it is decoration.
4. **Do not stack.** Label, body, and gloss in one paragraph — *he felt a wave of grief, his chest tightening, as if the world had stopped* — is the characteristic failure, and it is three channels each telling the reader what the previous one said.
5. **The channel may move inside a scene.** A man can hold it together while watched (labelled, or oblique) and lose it in the van (enacted, one sentence). What is forbidden is all three at once on the same beat.

`[data: StoryScope]` The numbers explain why this file exists. AI stories render emotion through the body in 81% of cases against 38% for human stories, and label it explicitly in 8% against 29%. The gap is not evidence that the body is bad or that labels are good; it is evidence of a substitution, produced by "show, don't tell" applied as a rule. The correction is calibration — channel chosen by function — not inversion, where every label is deleted because a statistic leaned the other way.

## What not to conclude

- **Not "labels are the human choice, so label more."** The human rate is still under a third (29%), so most human stories in that corpus do not label the emotion either. The number is a prior about where defaults cluster, not a quota.
- **Not "Version B is bad prose."** B is publishable, and in a scene of solitary shock it is the right channel; the signature module's own calibration table sends shock to the body. It fails *here*, because of the witness and because it ends in stasis.
- **Not "oblique is the literary option."** C is legible only because the setup says crosscut and he asks for ripping. Remove that, and the wrongness becomes random, which is not reticence but noise.
- **Not "one channel per scene, forever."** See point 5. The rule is one channel per beat, and a beat can be six lines.
- **Not "this tells you whether a text was machine-written."** Nothing here is a detector; a human can write B and a model can write C.

## Transfer rule

Choose the channel by what the emotion has to *do* in the scene, and verify it against the state change; if the reader's only gain is sympathy, the channel is carrying the writer's feeling instead of the character's.
