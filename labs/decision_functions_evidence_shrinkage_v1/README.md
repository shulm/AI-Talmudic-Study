# Bounded evidence shrinkage laboratory

Assignment: PR19 at724be8c49808e1e1b8643d81c73267f7577439c8. All scientific code is frozen before optimization. No selection, human data, encoder or PR18 sweep.

`preflight.py` checks deterministic small cases. `integration_preflight.py` substitutes mock optimizer outcomes and nonresearch seeds8001/8002/8003; its arrays are disposable tests, not scientific results. `freeze.py` publishes exact contracts/source hashes. `execute.py` requires explicit fresh private root, output root and verified publication receipt. It runs E/F/G/H once, stopping on engineering invalidity. `verify.py` performs no optimization; receipts require a new destination. `report.py` renders delivered evidence.

Use `run_logged.py python <stage.py> ...` for every execution/test/verification command. It enforces single-thread BLAS and cumulative sampled CPU/RSS guards. Default private documentation path: `C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1`; never commit it. Detailed commands are retained in command receipts. Nine archives per realization plus separate full optimizer vectors are immutable.

Example verification (read only; choose a fresh receipt path):

```
python labs/decision_functions_evidence_shrinkage_v1/run_logged.py python labs/decision_functions_evidence_shrinkage_v1/verify.py --private-root C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1 --output-root research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1 --receipt NEW_RECEIPT.json
```

Never rerun execution to repair scientific failures. The protocol and exact expected contracts are in the public run directory.
