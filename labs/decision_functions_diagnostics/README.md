# Interaction diagnostics v1

This continuation preserves the frozen pilot. All commands run from repository root with existing Python 3.12, NumPy 2.1.3, SciPy 1.15.1 and psutil 7.2.2. No installation or model/data download is needed.

The original cache is read-only. New synthetic arrays use a different private directory. Public outputs are under `research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/`. `synthetic_protocol.json` at commit `5fc8cf48394b4e620a75be8e8f92054a6c02a451` fixes the generator, optimization, counts and gates before fitting.

Executed commands:

```powershell
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/checks.py
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/replay.py --private-root C:/Users/David/.cache/decision_functions/pilot_v1
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/synthetic.py --output-private-root C:/Users/David/.cache/decision_functions/interaction_diagnostics_v1
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/human_certificate.py --private-root C:/Users/David/.cache/decision_functions/pilot_v1
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/audit_checks.py
python labs/decision_functions_diagnostics/run_logged.py python labs/decision_functions_diagnostics/verify_diagnostics.py --private-root C:/Users/David/.cache/decision_functions/pilot_v1 --output-private-root C:/Users/David/.cache/decision_functions/interaction_diagnostics_v1
python labs/decision_functions_diagnostics/report.py
```

These stages publish immutable receipts and refuse to overwrite them. To independently replay, use a fresh checkout whose diagnostics output directory does not contain prior receipts, and a new synthetic-output directory. Never delete original evidence to rerun in place. The old private root is never a destination. Offline replay does not require changing HEAD or a remote branch to the old freeze.

`core.py` uses same-filesystem hard-link publication for complete immutable records; it requires a filesystem supporting hard links (the executed NTFS workspace does). Missing capability fails rather than falling back to unsafe replacement. Starts, completions and expected identities are separate. Receipts include both Git HEAD and hashes of actual working source; the two post-run verification additions were tested before their final commit, so their content hashes are the authoritative source identity.

The synthetic objective adapter preserves the historical algebra and gradients, but uses the declared tighter solver settings. B3 is the personal-offset head on known shared logits; there is no synthetic or human B2 refit. A single numerical case is one observation. Two wording variants were materialized afterward as a grouping/engineering artifact, not encoder inputs or extra observations. The 24-person development split was reserved and not scored.

All fit records include termination and stationarity information separately. Shared gradients have differently scaled parameter blocks, so the reported `person_scaled_gradient_max` is a conservative common rescaling, not a declaration that every block should share one scientific tolerance. The human certificate uses the actual per-person intercept residual and a strong-convexity bound.

The initial engineering checks used no optimizer: frozen objective closures were captured through a substituted `solve` callback. Supplemental audit tests require the complete numerical record fields. No repeated fits were performed. The statistical experiment remains complete even though the null recovery gate failed.
