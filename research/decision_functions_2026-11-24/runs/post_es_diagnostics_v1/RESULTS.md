# post_es_diagnostics_v1

**POST_HOC_EXPOSED_DIAGNOSTIC. Scientific qualification remains false.**

Decision: PROPOSE_FRESH_UNCAPPED_CONFIRMATION. Historical PR20 status remains INCOMPLETE / NUMERICALLY_UNRESOLVED. Diagnostic evidence: COMPLETE; solver engineering: PASS; cap ablation: DESCRIPTIVE_COMPLETE.

No historical refit, shared-model fitting, new scientific personal fitting, fresh scientific world, donor arm or bootstrap was run. Original missing scientific_summary.json and verifier exception are preserved.

Pre-analysis checkpoint: dfc649e4557d4689c5d33556bb52faa88ec3cf03; assignment: 2f1cae3e894bec16c9c5cd280356a4e051029031. Historical delivery: f18255c5fad37f704881ff1f9ad50cd113497236.

## POST_HOC_EXPOSED_DIAGNOSTIC: active contrast and loss

| Realization | M1 NRMSE | FIXED_MIX NRMSE | ES NRMSE | Uncapped NRMSE [optimization enclosure] | Uncapped gain | Recovery | Inactive excess |
|---|---:|---:|---:|---|---:|---:|---:|
| E | 0.408206012 | 0.513978813 | 0.555275892 | 0.482192103 [0.482189842, 0.482194365] | 0.531136882 | 0.796469090 | 9.2423361996e-06 |
| F | 0.394396292 | 0.504310331 | 0.564899179 | 0.482826602 [0.482824351, 0.482828853] | 0.528201872 | 0.791524584 | -0 |
| G | 0.381240603 | 0.494657196 | 0.534684508 | 0.438866544 [0.438863223, 0.438869865] | 0.547532244 | 0.820699498 | -0 |
| H | 0.403815516 | 0.511815408 | 0.556166871 | 0.475928782 [0.475925526, 0.475932037] | 0.539463307 | 0.807362899 | -0 |

All1664 saved personal row instances diagnosed;128 individual batch1/7 versus48 comparisons. Maximum D-weighted residual: 2.79456146588e-06. The batch48 solution is not ground truth. Each comparison is bounded through the common exact personal optimum. Shared global optimality is not claimed.

Exactly8 new primary arrays,16 stratum/history rows and8 stratum aggregates. All192 inactive rows are bitwise unchanged;153 active weights changed. Baseline coefficient underflows in12 rows; finite log coefficients are retained, without replacing the cap or renormalizing predictions. Log-zero M1 coefficients use legitimate negative infinity in the private coefficient archive.

The detailed five-arm tables include expected/sample NLL, accuracy, Brier, per-person changes, positive-part excess, ordered contrast MSE/NRMSE changes and loss/contrast enclosures. History losses and squared contrasts are averaged, not probabilities. Former thresholds are descriptive reference lines only. No old or new bootstrap is claimed for the uncapped rule.

Bounds condition on saved V, priors, scalar evidence and histories. Gradients are independently recomputed without batch averaging. A fixed1e-12-scaled gradient comparison allowance is added to the residual bound. These are analytic bounds evaluated numerically, not directed-rounding certificates or sampling confidence intervals. A contrast lower bound above.5 excludes personal optimization error as an explanation of that gap under these conditions.

## Engineering and verification

The fixed suite contains48 people,8 motifs,2 heads and4 layouts:384 actual zero-initialized Newton attempts in114 wrappers. The sole support residual target is1e-10; queries are evaluated only afterward. The fixed roundoff full-step acceptance is logged without relaxing convergence. Derivative tests contain96 gradient and96 Hessian blocks and no optimizer calls. Complete attempt receipts retain every guarded acceptance and failure.

New verification: 395 exact grouped comparison IDs passed. The maximum returned grouped replay discrepancy is 0.0; internal scalar-gradient and forward comparisons have their own tolerance checks and are not all summarized by that number. Terminal examples cover success, numerical/scientific failure, incomplete evidence and resource stop. A terminal record itself is not integrity proof.

Resources: {'cpu_seconds_sampled': 40.59375, 'wall_seconds_profiled': 103.34299999987707, 'peak_rss_bytes_sampled': 107982848, 'commands': 5, 'failed_commands': 1, 'limits': {'cpu': 600, 'rss': 1073741824}, 'limitations': 'CPU/RSS polled every .02 seconds. Startup/exit CPU and transient RSS may be missed; Git/shell/network and final rendering overhead not comprehensively profiled. No unseen expenditure or scientific retry inferred as zero.'}. Final accounting may be extended by a separately identified final delivery receipt.

The original112 private artifacts and all pinned historical scientific blobs are hash-checked before/after. Derived data live outside the old cache. PR18 remains a separately authorized, scientifically unexecuted planning package; corpus production and DICES/SRO exposure remain separate. Nothing is merged.

## Preserved failures and final interpretation

**POST_HOC_EXPOSED_DIAGNOSTIC:** E history 101 still has contrast NRMSE **0.5165570102926313**, above the former 0.5 reference. The aggregate E result averages squared contrast errors across both histories. It must not be described as recovery on every history. The original ES aggregate optimization-enclosure lower bounds are E 0.5552739114101162, F 0.5648972346557398, G 0.5346817867502928 and H 0.5561640887160271. Under the fixed saved basis, priors and evidence, personal optimization error cannot explain those failures.

All 384 engineering attempts succeeded without retries. Maximum independently evaluated residual R was 9.840073629366365e-11; maximum K*R was 4.730843750530189e-10. At most nine accepted steps were needed. There were 36 declared guarded full-step acceptances. Parameters and probabilities were bitwise invariant across all four layouts. These are toy engineering results, not new scientific fits.

The executor failed **after** completing diagnosis, ablation and all engineering attempts, while composing its terminal report: `TypeError: dict() got multiple values for keyword argument 'qualification'`. The failed command and its resources remain recorded. `FINALIZE_REPORTING_ONLY.py` validates completed inventories and writes the terminal without calling fitting or prediction code. `REPORTING_RECOVERY.json` records its source hash and success/failure/collision tests. The subsequent frozen verifier independently accepted the underlying evidence. All 13 frozen scientific source files remain unchanged; this delivery does not claim an uninterrupted execution or repair the historical missing summary. Future executors must integrate and test the corrected terminal composition before launch.

Final command accounting is in `RESOURCE_USAGE_FINAL.json`; the earlier resource snapshot above predates rendering this report. The delivery manifest binds public report bytes separately from the frozen scientific checkpoint. Environment: Python 3.12.4, NumPy 2.1.3, SciPy 1.15.1, psutil 7.2.2, one numerical thread. No new trained model revision exists: all scientific parameters come from historical delivery f18255c5fad37f704881ff1f9ad50cd113497236, with private archive identities in INPUT_BINDINGS.json and INPUT_HASH_RECEIPT.json. All 1,215 historical blobs were preserved.
