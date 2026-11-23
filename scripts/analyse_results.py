#!/usr/bin/env python3
"""Decode blind judgments and summarise an evaluation round.

Reads:
    tests/results/judging/key.json
    tests/results/judging/judge-*.json

Prints:
    per-pair preference by condition (after decoding the key)
    mean axis score by condition
    agreement between judges
    a markdown table suitable for pasting into the results file

This is a descriptive summary of a case series. It computes no p-values and no
effect sizes; with six pairs they would not mean what they look like.

usage:
    python scripts/analyse_results.py
"""

from __future__ import annotations

import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JUDGING = ROOT / "tests" / "results" / "judging"
AXES = [
    "narrative_coherence",
    "character",
    "prose",
    "emotional_credibility",
    "originality",
    "structural_integrity",
]


def main() -> int:
    key = json.loads((JUDGING / "key.json").read_text(encoding="utf-8"))
    judges = sorted(JUDGING.glob("judge-*.json"))
    if not judges:
        print("no judge files found")
        return 1

    data = {j.stem: json.loads(j.read_text(encoding="utf-8")) for j in judges}
    pairs = sorted(key)

    print(f"judges: {', '.join(data)}\npairs: {len(pairs)}\n")

    tally = {"with": 0, "without": 0, "tie": 0}
    agree = 0
    total_decisions = 0

    rows = []
    for pair in pairs:
        labels = key[pair]  # {"A": "with"|"without", ...}
        prefs = {}
        for name, report in data.items():
            entry = next((p for p in report["pairs"] if p["pair"] == pair), None)
            if entry is None:
                continue
            pref = entry["preference"]
            prefs[name] = labels.get(pref, "tie") if pref in ("A", "B") else "tie"
            if len(prefs) == 2:
                total_decisions += 1
                if len(set(prefs.values())) == 1:
                    agree += 1
        for condition in prefs.values():
            tally[condition] += 1
        rows.append((pair, prefs))

    print("preference by pair (decoded)")
    for pair, prefs in rows:
        print(f"  {pair}: " + ", ".join(f"{j}={c}" for j, c in prefs.items()))

    print(f"\ntally across judge-decisions: {tally}")
    print(f"judge agreement: {agree}/{total_decisions} pairs unanimous")

    print("\nmean axis score by condition")
    sums = {("with", a): [] for a in AXES}
    sums.update({("without", a): [] for a in AXES})
    for pair in pairs:
        labels = key[pair]
        for report in data.values():
            entry = next((p for p in report["pairs"] if p["pair"] == pair), None)
            if not entry:
                continue
            for label, condition in labels.items():
                for axis in AXES:
                    sums[(condition, axis)].append(entry["scores"][label][axis])

    print("| axis | with skill | without | delta |")
    print("|---|---|---|---|")
    for axis in AXES:
        w = statistics.mean(sums[("with", axis)])
        wo = statistics.mean(sums[("without", axis)])
        print(f"| {axis} | {w:.2f} | {wo:.2f} | {w - wo:+.2f} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
