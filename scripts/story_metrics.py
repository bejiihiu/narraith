#!/usr/bin/env python3
"""Surface proxies for fiction drafts.

These are *proxies*, not quality scores. They measure things a regex can see:
sentence variance, lexical diversity, dialogue share, emotion-word density,
repetition. A good text can score badly on every one of them, and a bad text
can score well. Use them to find where to look, never to decide whether a
story works.

usage:
    python scripts/story_metrics.py draft.md [more.md ...] [--json]
    python scripts/story_metrics.py --compare before.md after.md

The emotional-channel split (labelled vs somatic vs neutral) follows the
distinction studied in StoryScope: models tend to render emotion through the
body and withhold direct labels. Both directions are legitimate; the ratio is
only interesting as a tendency.

The opener metrics — pronoun-initial sentences, paragraphs opening on a pronoun,
one-sentence paragraphs, paragraph-length spread — were added after a detector
report on a sparse Russian story. They measure the kind of rhythmic uniformity
that makes well-made prose statistically typical of machine output. See
references/detector-feedback.md.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+(?=[«\"'(A-ZА-ЯЁ])")
WORD = re.compile(r"[A-Za-zА-Яа-яЁё]+(?:[-'][A-Za-zА-Яа-яЁё]+)*")
DIALOGUE = re.compile(r"[«\"—–-]\s*[^»\"\n]{2,}?[»\"]|^\s*[—–-]\s", re.M)

EMOTION_LABELS = {
    "en": """afraid anger angry anguish anxious ashamed bewilderment bitter bored calm
    contempt confused curiosity delight despair disgust dread eager ecstatic elated
    embarrassed envious euphoric fear furious glad grief guilty happy hate hope horror
    humiliated hurt jealous joy lonely longing love melancholy miserable nostalgia panic
    pity pride rage regret relief remorse resentful sad scared shame shock sorrow spite
    surprise terrified tired uneasy wonder worry yearning""".split(),
    "ru": """страх страшно тревога тревожно стыд стыдно вина виноват гнев злость ярость
    ярость обида обидно горе горько тоска тоскливо печаль печально грусть грустно
    радость радостно счастье счастлив восторг ужас отвращение презрение зависть
    нежность умиление растерянность недоумение удивление спокойствие отчаяние
    безнадёжность безнадежность смущение досада жалость сострадание""".split(),
}

SOMATIC = {
    "en": """chest throat stomach jaw fists knuckles spine shoulders breath pulse
    sweat shiver tremble flinch swallow blink ache sting burn tight loosen""".split(),
    "ru": """грудь горло живот желваки кулаки позвоночник плечи дыхание пульс пот
    дрожь озноб сглатывать вздрагивать бледнеть краснеть неметь сжиматься""".split(),
}

CONNECTIVES = {
    "en": "however therefore moreover furthermore nevertheless thus hence consequently additionally meanwhile".split(),
    "ru": "однако поэтому кроме того более того тем не менее следовательно таким образом при этом затем".split(),
}

ADVERBS = {
    "en": re.compile(r"\b\w+ly\b", re.I),
    "ru": re.compile(r"\b\w+(?:о|е)\b", re.I),
}


@dataclass
class Metrics:
    file: str
    words: int
    sentences: int
    paragraphs: int
    mean_sentence: float
    median_sentence: float
    stdev_sentence: float
    pct_long_sentences: float
    pct_short_sentences: float
    mattr: float
    dialogue_ratio: float
    emotion_label_per_1k: float
    somatic_per_1k: float
    connective_per_1k: float
    repeated_4grams: int
    top_repeated_4grams: list[tuple[str, int]]
    pronoun_initial_share: float
    paragraph_initial_pronoun_share: float
    one_sentence_paragraph_share: float
    paragraph_mean_words: float
    paragraph_stdev_words: float
    top_openers: list[tuple[str, int]]


PRONOUNS = {
    "en": {"he", "she", "they", "it", "i", "we", "you"},
    "ru": {"он", "она", "они", "оно", "я", "мы", "ты", "вы"},
}


def strip_lead(token: str) -> str:
    return token.strip("—–-«»\"'(),.:;!?…").lower()


def opener(sentence: str) -> str:
    words = sentence.split()
    return strip_lead(words[0]) if words else ""



def detect_lang(text: str) -> str:
    cyr = len(re.findall(r"[А-Яа-яЁё]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    return "ru" if cyr > lat else "en"


def mattr(tokens: list[str], window: int = 50) -> float:
    if len(tokens) < window:
        return len(set(tokens)) / max(len(tokens), 1)
    ratios = []
    for i in range(len(tokens) - window + 1):
        chunk = tokens[i : i + window]
        ratios.append(len(set(chunk)) / window)
    return round(sum(ratios) / len(ratios), 3)


def ngrams(tokens: list[str], n: int = 4) -> Counter:
    return Counter(tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1))


def analyse(path: Path) -> Metrics:
    text = path.read_text(encoding="utf-8")
    lang = detect_lang(text)
    body = re.sub(r"^#.*$", "", text, flags=re.M)

    sents = [s.strip() for s in SENT_SPLIT.split(body) if len(WORD.findall(s)) > 1]
    tokens = [w.lower() for w in WORD.findall(body)]
    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    lengths = [len(WORD.findall(s)) for s in sents] or [0]
    total = max(len(tokens), 1)

    labels = sum(tokens.count(w) for w in EMOTION_LABELS[lang])
    somatic = sum(tokens.count(w) for w in SOMATIC[lang])
    connectives = sum(tokens.count(w) for w in CONNECTIVES[lang])
    dialogue_chars = sum(len(m.group(0)) for m in DIALOGUE.finditer(body))
    grams = ngrams(tokens, 4)

    openers = [opener(s) for s in sents]
    pron = PRONOUNS[lang]
    pronoun_initial = sum(1 for o in openers if o in pron) / max(len(openers), 1)
    para_openers = [opener(p.splitlines()[0]) for p in paras]
    para_pron = sum(1 for o in para_openers if o in pron) / max(len(para_openers), 1)
    one_sent_paras = sum(
        1 for p in paras if len([s for s in SENT_SPLIT.split(p) if WORD.findall(s)]) <= 1
    )
    para_words = [len(WORD.findall(p)) for p in paras] or [0]
    top_openers = [(w, c) for w, c in Counter(openers).most_common(6) if w]

    return Metrics(
        file=str(path),
        words=len(tokens),
        sentences=len(sents),
        paragraphs=len(paras),
        mean_sentence=round(statistics.mean(lengths), 2),
        median_sentence=float(statistics.median(lengths)),
        stdev_sentence=round(statistics.pstdev(lengths), 2),
        pct_long_sentences=round(100 * sum(1 for x in lengths if x > 35) / len(lengths), 1),
        pct_short_sentences=round(100 * sum(1 for x in lengths if x <= 6) / len(lengths), 1),
        mattr=mattr(tokens),
        dialogue_ratio=round(dialogue_chars / max(len(body), 1), 3),
        emotion_label_per_1k=round(1000 * labels / total, 2),
        somatic_per_1k=round(1000 * somatic / total, 2),
        connective_per_1k=round(1000 * connectives / total, 2),
        repeated_4grams=sum(1 for _, c in grams.items() if c > 1),
        top_repeated_4grams=[(" ".join(g), c) for g, c in grams.most_common(5) if c > 1],
        pronoun_initial_share=round(pronoun_initial, 3),
        paragraph_initial_pronoun_share=round(para_pron, 3),
        one_sentence_paragraph_share=round(one_sent_paras / max(len(paras), 1), 3),
        paragraph_mean_words=round(statistics.mean(para_words), 1),
        paragraph_stdev_words=round(statistics.pstdev(para_words), 1),
        top_openers=top_openers,
    )


def render(m: Metrics) -> str:
    return (
        f"{m.file}\n"
        f"  words {m.words}  sentences {m.sentences}  paragraphs {m.paragraphs}\n"
        f"  sentence length: mean {m.mean_sentence}  median {m.median_sentence}  sd {m.stdev_sentence}\n"
        f"  long (>35w) {m.pct_long_sentences}%   short (<=6w) {m.pct_short_sentences}%\n"
        f"  MATTR-50 {m.mattr}   dialogue share {m.dialogue_ratio}\n"
        f"  emotion labels {m.emotion_label_per_1k}/1k   somatic {m.somatic_per_1k}/1k\n"
        f"  connectives {m.connective_per_1k}/1k   repeated 4-grams {m.repeated_4grams}\n"
        f"  pronoun-initial {m.pronoun_initial_share:.1%}   paragraphs opening on a pronoun {m.paragraph_initial_pronoun_share:.1%}\n"
        f"  one-sentence paragraphs {m.one_sentence_paragraph_share:.1%}   paragraph words {m.paragraph_mean_words} (sd {m.paragraph_stdev_words})\n"
        f"  top openers {m.top_openers}\n"
    )


def delta(before: Metrics, after: Metrics) -> str:
    fields = [
        "mean_sentence",
        "stdev_sentence",
        "pct_long_sentences",
        "mattr",
        "dialogue_ratio",
        "emotion_label_per_1k",
        "somatic_per_1k",
        "connective_per_1k",
        "repeated_4grams",
        "pronoun_initial_share",
        "paragraph_initial_pronoun_share",
        "one_sentence_paragraph_share",
    ]
    rows = []
    for f in fields:
        a, b = getattr(before, f), getattr(after, f)
        rows.append(f"  {f:24} {a:>8} -> {b:>8}   {b - a:+.2f}")
    return "\n".join(rows)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--compare", action="store_true")
    args = ap.parse_args()

    paths = [Path(f) for f in args.files]
    missing = [str(p) for p in paths if not p.exists()]
    if missing:
        print("missing: " + ", ".join(missing), file=sys.stderr)
        return 1

    results = [analyse(p) for p in paths]
    if args.json:
        print(json.dumps([asdict(r) for r in results], ensure_ascii=False, indent=2))
    elif args.compare and len(results) == 2:
        print(render(results[0]))
        print(render(results[1]))
        print("delta")
        print(delta(results[0], results[1]))
    else:
        for r in results:
            print(render(r))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
