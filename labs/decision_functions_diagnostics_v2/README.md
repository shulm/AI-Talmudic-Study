# Synthetic diagnostic v2

Scientific assignment: PR9, review commit 3c93bd5c9ef9c14825e45c089fba0b59106d8a36. Existing NumPy/SciPy/psutil only. No downloaded model revision: this is a rank-two numerical head, with source/checkpoint hashes and saved private fitted vectors.

The public PROTOCOL.json is the review's unchanged machine-readable design. Stage IDs/templates are fixed by stage_templates_final.json. Earlier preflight.json is retained from the initial implementation check; preflight_final.json includes generator-equivalence checks and the final parameter-saving implementation. Both runs made zero scientific fits.

Commands from repository root (PowerShell), after publishing required checkpoints:

```powershell
$privateRun = 'C:/Users/David/.cache/decision_functions/interaction_diagnostics_v2'
$publicRun = 'research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2'
python labs/decision_functions_diagnostics_v2/run_logged.py python labs/decision_functions_diagnostics_v2/study.py development --private-root $privateRun --output-root $publicRun
python labs/decision_functions_diagnostics_v2/study.py freeze --private-root $privateRun --output-root $publicRun
# Publish and verify selection checkpoint before either next command.
python labs/decision_functions_diagnostics_v2/run_logged.py python labs/decision_functions_diagnostics_v2/study.py heldout-a --private-root $privateRun --output-root $publicRun
python labs/decision_functions_diagnostics_v2/run_logged.py python labs/decision_functions_diagnostics_v2/study.py heldout-b --private-root $privateRun --output-root $publicRun
python labs/decision_functions_diagnostics_v2/run_logged.py python labs/decision_functions_diagnostics_v2/verify.py --private-root $privateRun --output-root $publicRun
python labs/decision_functions_diagnostics_v2/report.py
```

Do not run freeze or holdouts if development has no eligible candidate or fails numerical checks. No retries. No original-cache dependency. A is generated once; B is generated only after the selection publication. The private fixture contains sealed-by-workflow evaluation arrays, not an OS security boundary. Fitting consumes explicit training arrays; adaptations consume explicit supports; selection only A development. The B development block remains unused.

Publication receipt JSON records commit and verified issue/PR comment links; stage launch requires matching HEAD. GitHub publication is checked by the executor. Oracle arrays and query labels are evaluation inputs, never fit inputs. Every stage refuses reused record destinations. Full optimizer vectors are saved privately for all attempts; public records give finite checks and norms.

Resource wrapper enforces a conservative 3,500 sampled CPU-second guard below the one-hour cap and 4 GiB sampled RSS. BLAS/OMP/MKL threads are one. The public resource report states sampling limits and overhead excluded from process measurements.
