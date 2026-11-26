# Post-ES diagnostics

PR25 H0–H4; source and exact contracts freeze before analysis. No historical refits or new scientific fitting. The only optimizer is `solver.py`, called exactly384 times by `suite.py` on the frozen toy fixture, in114 wrappers. Derivative preflight performs no optimization.

All commands use `run_profiled.py python SCRIPT ...` for single-thread numerical libraries and cumulative600-second/1GiB resource accounting. Explicit original cache: `C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1`. Explicit derived cache: `C:/Users/David/.cache/decision_functions/post_es_diagnostics_v1`. Both remain uncommitted. Never reuse the execution destination or repeat the suite.

`prepare.py` binds historical public Git bytes/private hashes and freezes fixtures, source, schemas and tests. `execute_new.py` requires a published/read-back checkpoint. It diagnoses saved parameters, creates one eight-array uncapped arm and runs the fixed engineering suite. `verify_new.py` does not invoke an optimizer; use a new receipt destination for each verification. `report_new.py` returns separate historical, diagnostic, engineering, ablation and scientific-status axes.

The historical replay API is a comparison only. The new individual gradient and forward calculations are independently expressed. Float64 analytic error enclosures are not directed-rounding certificates. All ablation outputs are POST_HOC_EXPOSED_DIAGNOSTIC; no qualification or historical-summary repair is allowed.
