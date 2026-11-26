# PR #27 review and next agent entry point

**Decision:** accept completed diagnostics and declared engineering recovery; retain scientific qualification=false and PR #20's historical incomplete status. Prepare, freeze, and execute one separately identified fresh confirmation through I0–I4.

| File | Purpose |
|---|---|
| [REVIEW.md](REVIEW.md) | Evidence, interpretation, limitations, and review decision |
| [NEXT_AGENT_PROMPT.md](NEXT_AGENT_PROMPT.md) | Complete executable assignment for the next agent |
| [CONFIRMATION_PROTOCOL.md](CONFIRMATION_PROTOCOL.md) | Fixed mathematical, statistical, numerical, and execution contract |
| [DESIGN.json](DESIGN.json) | Machine-readable design and exact main counts |
| [PLAN_CALCULATION.py](PLAN_CALCULATION.py), [receipt](PLAN_CALCULATION.json) | Exact sample-size and power calculation; zero fits |
| [SEEDS.json](SEEDS.json) | Untouched U000–U081 five-stream seed reservation |
| [SEED_RESERVATION.py](SEED_RESERVATION.py), [receipt](SEED_RESERVATION.json) | Deterministic derivation and historical disjointness |
| [PUBLIC_SCIENCE_REVIEW.json](PUBLIC_SCIENCE_REVIEW.json) | 161,386 public arithmetic assertions and explicit private-data boundary |
| [PUBLIC_ENGINEERING_REVIEW.json](PUBLIC_ENGINEERING_REVIEW.json) | Independent saved-trace replay and inventory/hash review |
| [CHRONOLOGY_PRESERVATION.json](CHRONOLOGY_PRESERVATION.json) | Git blob preservation and publication-before-recorded-execution evidence |
| [TERMINAL_REVIEW.json](TERMINAL_REVIEW.json) | Reproduced terminal failure and static reporting-adapter checks |
| [REVIEW_EVIDENCE.json](REVIEW_EVIDENCE.json) | Provenance and reproduction of packaged independent review evidence |

The primary prospective study uses one random balanced 16-case history per world, 82 worlds, and requires at least 72 numerically qualified joint successes. It entails 246 shared fits and 31,488 personal solves under one fixed uncapped rule. H2 and the old two-history aggregate are secondary. This package contains a design and reserved integers, **no newly generated confirmation worlds or fitted models**.

## Reproducing this review

The independent science and engineering scripts take a repository-root argument and an output-path argument. Run them against a checkout/export pinned to **PR #27 final `16ef28b105ff6c28ee3f822b1409f076fa895318`**, using the scripts from this review. Later root handoff changes intentionally differ from the reviewed delivery manifest. Inspect each output JSON's `status`; the portable engineering script preserves the original checker's exit behavior.

```bash
python PUBLIC_SCIENCE_REVIEW.py /absolute/pinned/pr27/checkout /absolute/new/science_receipt.json
python PUBLIC_ENGINEERING_REVIEW.py /absolute/pinned/pr27/checkout /absolute/new/engineering_receipt.json
python PLAN_CALCULATION.py --output /absolute/new/planning_receipt.json
python SEED_RESERVATION.py --output /absolute/new/SEEDS.json --receipt /absolute/new/seed_receipt.json
```

The last command derives the same seed bank but reports historical collision checking as NOT_CHECKED unless supplied `--seed-sources`. To reproduce that check, retrieve each exact revision/path recorded in SEED_RESERVATION.json, verify its content hash, and construct a JSON list of objects `{path, ref, content}` from those five sources. Pass that list's filename as `--seed-sources`. The PR #18 canonical path is `research/decision_functions_2026-11-24/proposals/short_history_null_control_v1/SEEDS.json`; the receipt discloses and corrects a reviewer input-label error. No source contents need be duplicated in this package.

These review scripts perform no scientific optimization or new research-world generation. Original private arrays remain unavailable in this review environment. Follow the receipt scope: public arithmetic and private-file hash bindings are not an independent private-array replay.

## Coordination

Read current issue #2 before claiming I0–I4. PR #18 and its bank remain separately unexecuted. Corpus lanes continue independently. The new execution must publish/read back its own implementation freeze before materializing U000, and return a draft PR without merging.
