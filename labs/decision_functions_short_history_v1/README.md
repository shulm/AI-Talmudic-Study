# Short-history v1 laboratory

Bounded assignment: review47b19560350aa8c5d877d99f381d5b27f5b3490a, draft PR13. Historical v2 source is copied/versioned here; historical files are unchanged. Existing NumPy/SciPy/psutil only. No encoder or human dataset is involved.

## Execution (after public pre-fit checkpoint)

```powershell
$privateRun = 'C:/Users/David/.cache/decision_functions/short_history_v1'
$publicRun = 'research/decision_functions_2026-11-24/runs/short_history_v1'
python labs/decision_functions_short_history_v1/run_logged.py python labs/decision_functions_short_history_v1/execute.py --realization C --private-root $privateRun --output-root $publicRun
python labs/decision_functions_short_history_v1/run_logged.py python labs/decision_functions_short_history_v1/execute.py --realization D --private-root $privateRun --output-root $publicRun
python labs/decision_functions_short_history_v1/run_logged.py python labs/decision_functions_short_history_v1/verify.py --private-root $privateRun --output-root $publicRun
python labs/decision_functions_short_history_v1/report.py
```

No tuning or scientific early stop: execute D even if C predictive gates fail. Stop for an optimizer/engineering/resource failure; preserve records and report INCOMPLETE. Never retry a consumed scientific slot. All outputs reject collisions. Source and publication hashes must match the pushed checkpoint. The wrapper uses single-thread BLAS/OMP/MKL,3500 sampled CPU seconds as a conservative guard below one hour, and4 GiB sampled RSS. Timing limitations are disclosed.

## Data flow and exact contracts

prepare writes separate learner (training labels and label-free query features), support (only support-pool labels/features), and evaluator (query outcomes/oracles) archives. Shared and personal fitting receive only learner/support inputs. Predictions are saved before execute loads evaluator arrays for aggregate scoring. This is a logical boundary, not OS-enforced secrecy. Complete fixture archives exist privately for provenance verification.

PROTOCOL.json copies the assignment design unchanged. EXPECTED.json materializes six exact ledgers,18 archives,230 prediction arrays per realization,24 metric rows per realization and17,038 independent arithmetic comparisons. There are54 curvature arrays /1296 person records per realization. Ledger totals196/12 shared/184 adaptation/3776 person-solves are exact requirements, not upper bounds. Verification rejects missing/duplicate components and cannot qualify declared early stops (none permitted here).

Each nonzero support solve records full private parameters. Donor predictions are exact saved-array permutations; k=0 and uninformative M1 are analytic; k=96 uses one canonical support order. No redundant scientific solves. Curvature is zero-fit calculation from saved individual parameters. Compare losses across schedules, probabilities only across initialization seeds within a history.

Preflight unit and complete zero-fit integration receipts are public. Integration uses legacy data and zero-parameter stubs in temporary directories, never a scientific optimizer. Retained engineering failures and cumulative resources are documented in PREFIT_ENGINEERING.md. Reproduction must use fresh destinations and remains a reproduction of exposed results, not new confirmation.
