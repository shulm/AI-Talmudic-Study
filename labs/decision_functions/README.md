# Individual decision-function laboratory

Import-safe CPU scripts for issue #2. Data, histories, embeddings, weights and cell probabilities live in `~/.cache/decision_functions/pilot_v1`, outside Git. Override with `DECISION_LAB_PRIVATE`. Public run artifacts live under `research/decision_functions_2026-11-24/runs/pilot_v1`.

Install the exact versions in `requirements.txt` in an isolated Python 3.12 environment if needed. The executed environment already had all dependencies; no installation occurred.

Run from repository root, in order:

```powershell
python labs/decision_functions/prepare.py acquire
python labs/decision_functions/prepare.py prepare
python labs/decision_functions/run_logged.py python labs/decision_functions/checks.py
python labs/decision_functions/run_logged.py python labs/decision_functions/encode.py
python labs/decision_functions/run_logged.py python labs/decision_functions/develop.py
python labs/decision_functions/run_logged.py python labs/decision_functions/evaluate.py development
python labs/decision_functions/freeze.py
# Commit and push PROTOCOL_FROZEN, then publish SHA to issue #2 before scoring.
python labs/decision_functions/run_logged.py python labs/decision_functions/evaluate.py test --freeze EXACT_PUSHED_SHA
python labs/decision_functions/report.py
```

Never rerun development or modify the model after test exposure and claim a fresh confirmation. The evaluator refuses to overwrite prediction files. A reproduction should use a fresh private directory and the frozen checkout; it is a reproduction of the exposed test. Freeze verification requires the exact declared remote branch HEAD, so an independent reproduction must explicitly document a new verification reference rather than bypass the historical freeze.

`grid.json` fixes all candidates, penalty conventions, optimizer settings and final comparisons before development. Human fitting performs 3 B2 + 27 M1 shared fits. Personal adaptations are vectorized separable convex solves, with counts recorded per person. At k=0 B3/B4/M1 equal B2; B1 equals B0. New-person IDs serve only to order/join histories and are never model features. All three raw CSV outcomes survive the adapter.

Commands actually run, statuses and sampled child CPU/RSS appear in `command_log.json`; initial acquisition/preparation are separately recorded as successful but unprofiled. Source files are never rewritten in place. `prepare.py` uses the author exclusion list and input-only grouping, and writes disjoint learner, support and evaluator views. Only `evaluate.py test` opens test query outcomes after freeze verification. `prepare.py` mechanically maps them without reporting their distributions. No historical source-index builder is imported or run.

Scope limitation: full-token coverage does not establish preservation of reasoning. Grouping identical contexts is conservative but does not certify all semantic families. The bootstrap is descriptive for the fixed models and one split, not uncertainty over all possible data collection or training designs.
