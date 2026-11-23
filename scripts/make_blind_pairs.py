#!/usr/bin/env python3
"""Build blind A/B pairs from evaluation runs.

Run layout expected:

    tests/results/raw/eval-<id>/with/output.md
    tests/results/raw/eval-<id>/without/output.md

Output:

    tests/results/judging/pair-<id>/A.md
    tests/results/judging/pair-<id>/B.md
    tests/results/judging/key.json     <- do not show this to judges

The assignment is randomised with a fixed seed so a judging round can be
reproduced, and the key is written separately so a judge can be handed the
pair directories without the answer.

usage:
    python scripts/make_blind_pairs.py [--seed 7]
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "tests" / "results" / "raw"
OUT = ROOT / "tests" / "results" / "judging"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    evals = sorted(p for p in RAW.iterdir() if p.is_dir()) if RAW.exists() else []
    if not evals:
        print(f"no runs under {RAW}")
        return 1

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    rng = random.Random(args.seed)
    key: dict[str, dict[str, str]] = {}
    made = 0

    for run in evals:
        outputs = {}
        for condition in ("with", "without"):
            candidate = run / condition / "output.md"
            if candidate.exists():
                outputs[condition] = candidate
        if len(outputs) != 2:
            print(f"skip {run.name}: need with/ and without/ output.md")
            continue

        pair_dir = OUT / f"pair-{run.name.replace('eval-', '')}"
        pair_dir.mkdir()
        task = RAW / f"task-{run.name.replace('eval-', '')}.md"
        if task.exists():
            shutil.copyfile(task, pair_dir / "prompt.md")
        labels = ["A", "B"]
        rng.shuffle(labels)
        assignment = dict(zip(("with", "without"), labels))
        for condition, label in assignment.items():
            shutil.copyfile(outputs[condition], pair_dir / f"{label}.md")
        key[pair_dir.name] = {label: cond for cond, label in assignment.items()}
        made += 1

    (OUT / "key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    print(f"{made} pairs written to {OUT}")
    print("hand judges the pair directories only; key.json stays with the lead")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
