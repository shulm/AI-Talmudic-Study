# PR20 saved-evidence supplement to PR25

PR20 remains **INCOMPLETE / NUMERICALLY_UNRESOLVED**, qualification=false, at `f18255c5fad37f704881ff1f9ad50cd113497236`. Its original 1158/1160 replay remains partial. This supplement validates additional saved evidence; it does not repair or qualify the scientific run.

## Coordination and scope

Issue #2 was rechecked before analysis. PR25 had already published the public review and one next assignment at `2f1cae3e894bec16c9c5cd280356a4e051029031`, but lacked private artifacts. This supplement contributes that missing evidence. It uses only original B3, M1, FIXED_MIX(.9), and ES predictions. PR25's uncapped ablation and engineering solves were **not executed**. PR18 stays closed and scientifically unexecuted.

The audit checked all 112 private files against original manifests, replayed all saved forward/evidence outputs using the frozen independent replay helper, reconciled all 76 optimizer records, and independently recalculated individual gradients for 64 personal vectors / 1664 row instances. It joined saved fixture, support, query and evaluator arrays without calling the generator. All 1317 files at the pinned commit match their Git blobs and their before/after byte hashes. No source/run file changed.

## H: a real discrepancy between approximate solutions

The largest discrepancy is `H/numerical.npz:7_M1_11` versus `H/predictions.npz:101_M1_11`, at zero-based `[person=0, query=32, class=1]`. The person is the first row of the saved evaluator mapping (global person 144); the exact query ID is `learner.npz:query_ids[32]`. Both use history 101, the same first person's responses, and seed 11's shared basis. This is metadata identifying an existing comparison, not a published response/prediction row.

The responsible vectors are `H/parameters/H_numerical_101_M1_11_7.npy` and `H/parameters/H_support_101_M1_11_48.npy`. Their completion records live under the original `records/H_numerical/` and `records/H_support/` directories. The measured probability difference is **1.2232536670264693e-6**, above 1e-6. Expected-NLL difference for this seed is 2.8436359589267823e-7, below its separate 1e-5 threshold. Passing one test does not override the other.

| Batch | Iterations | Stop reason | Batch gradient infinity norm | First-person unscaled residual L2 |
|---|---:|---|---:|---:|
| 1 | 11 | Gradient tolerance | 5.8798872e-9 | 8.6088213e-9 |
| 7 | 16 | Relative function reduction | 9.4588924e-8 | 6.8554934e-7 |
| 48 | 17 | Relative function reduction | 2.3249903e-8 | 3.2100979e-7 |

The batch objective is the average of independent personal objectives; its gradients divide the individual residuals by batch size. Its unique per-person optimum is invariant to other batch members, but the joint L-BFGS trajectory and function-reduction stopping are not. Both batch 7 and 48 stopped above the nominal 1e-8 gradient tolerance. Batch 48 is not an exact reference solution. The first-person parameter distance is 4.8235300e-6, within the residual-derived upper bound 1.6775985e-5.

**Established:** saved parameter differences reproduce the saved prediction difference; nonzero residuals and function-reduction stopping explain why successful termination does not establish equal precision. **Unresolved:** without iteration trajectories or additional optimization, the audit cannot isolate the relative contributions of batch gradient scaling, joint line-search trajectory, and the function-reduction criterion. It does not claim that changing only one setting would fix the discrepancy.

## Recovery loss is much larger than personal numerical uncertainty

For fixed shared V, each personal objective is strongly convex: its Hessian is at least the positive diagonal penalty matrix. Using the conservative scalar curvature `mu=.06` for M1 and `.6` for B3,

`||theta_hat - theta_star||_2 <= ||gradient J_person(theta_hat)||_2 / mu = radius`.

At each query, let A map personal parameters to the three logits. Each log-probability gradient is a convex combination of class-row differences, so its norm is at most `max_cd ||A_c-A_d||_2`. Multiplying by the radius bounds each log-probability error. Fixed positive seed ensembles and fixed probability mixtures preserve the largest component log-error bound. The score-floor transformation is nonexpansive in log space. An anchored pair contrast contains eight signed log probabilities; summing their bounds and applying the RMS triangle inequality yields the NRMSE enclosures. Histories are combined as mean squared errors, never pooled probabilities.

These are analytic bounds evaluated in float64, **not directed-rounding certificates** or confidence intervals. They hold shared parameters, evidence and weights fixed, and address personal optimization error only. They do not bound shared-model optimization error, finite-history statistical error, misspecification, or retraining uncertainty. The conservative mixture bound ignores cancellation, including B3's structurally zero interaction contrast.

| World | M1 NRMSE | Fixed .9 NRMSE | ES NRMSE | ES numerical radius | ES lower bound |
|---|---:|---:|---:|---:|---:|
| E | .408206 | .513979 | .555276 | .000005787 | .555270 |
| F | .394396 | .504310 | .564899 | .000006809 | .564892 |
| G | .381241 | .494657 | .534685 | .000006928 | .534678 |
| H | .403816 | .511815 | .556167 | .000010982 | .556156 |

All eight per-history ES lower bounds also exceed .50. Under the stated fixed-model assumptions, personal numerical error cannot bridge the observed recovery gap. E/F/G passed their original numerical checks and still fail recovery; fixing H alone cannot qualify the method.

## Paired recovery and inactive-loss tradeoff

For contrast error `e = C_source - C_truth` and change `d = C_target - C_source`, the exact identity is `MSE_target - MSE_source = mean(d^2) + 2 mean(e*d)`. Every existing world/history/stratum comparison was checked. The aggregate active changes are:

| World | Transition | MSE increase | Change squared | Error cross-term | Expected-NLL increase |
|---|---|---:|---:|---:|---:|
| E | M1 → fixed .9 | 7.315655 | 1.015078 | 6.300577 | .033659 |
| E | Fixed .9 → ES | 3.311782 | .454129 | 2.857653 | .033556 |
| F | M1 → fixed .9 | 7.408536 | 1.053867 | 6.354669 | .034473 |
| F | Fixed .9 → ES | 4.858663 | .695783 | 4.162880 | .051994 |
| G | M1 → fixed .9 | 7.450601 | 1.163460 | 6.287141 | .033090 |
| G | Fixed .9 → ES | 3.090134 | .435616 | 2.654517 | .037354 |
| H | M1 → fixed .9 | 7.416603 | .983186 | 6.433417 | .034574 |
| H | Fixed .9 → ES | 3.552493 | .368690 | 3.183803 | .034864 |

Positive cross-terms show that these recorded changes reinforce existing contrast error on average. Probability mixing changes log-odds nonlinearly; these are exact within-artifact decompositions, not estimates of a new method's causal or out-of-sample effect.

| World | Inactive excess M1 | Inactive excess fixed .9 | Inactive excess ES |
|---|---:|---:|---:|
| E | .045207 | .035991 | .000009242 |
| F | .036143 | .028793 | 0 |
| G | .047011 | .037441 | 0 |
| H | .035268 | .028144 | 0 |

153/192 active person-history weights reach the cap; no inactive weight does. All inactive weights are zero in F/G/H. In E, one inactive weight per history is nonzero. Detailed aggregate weight distributions and paired tables are in `private_audit_02/analysis.json`; no individual response, prediction, weight, or parameter arrays are published. Two histories are repeated observations of the same people, not independent subjects.

The remaining M1 error is compatible with statistical/adaptation/shared-model limitations; this audit does not identify their separate causal shares. The .009 expectation guarantee remains conditional on the declared null model and cannot replace finite-cohort gates.

## One next investigation: preserve PR25's coordinated proposal

Recommend the already published **post_es_diagnostics_v1 H0–H4**, at PR25 commit `2f1cae3e894bec16c9c5cd280356a4e051029031`, rather than invent a second experiment. Hypothesis: the imposed .9 cap is a material source of recovery attenuation, and batch-independent personal optimization can remove the implementation-level precision dependence.

The private findings here supply additional H1 evidence, but do not declare that assignment complete. Its one uncapped ES ablation, exactly eight derived arrays, and fixed 384 engineering attempts / 114 wrapper calls remain prospective. Compare its uncapped rule with the four existing methods; keep E–H explicitly exposed and post hoc. No new scientific fits, historical refits, or fresh worlds belong to that diagnostic. Its ceiling remains 600 accounted CPU seconds and 1 GiB sampled RSS, with its required pre-analysis checkpoint before ablation or engineering solves. Consult its exact frozen toy suite and solver specification rather than substituting a new one.

Numerical/engineering gates and descriptive recovery criteria remain separate. A solver failure or uninformative recovery result blocks a scientific launch. A successful engineering result and favorable uncapped descriptive comparison would justify proposing one later confirmation with untouched seeds and frozen endpoints; it would not qualify PR20. This audit does not perform that ablation or select a new penalty, weight, prior, or support policy.

[Existing complete assignment](https://github.com/shulm/AI-Talmudic-Study/blob/2f1cae3e894bec16c9c5cd280356a4e051029031/research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/NEXT_AGENT_PROMPT.md).

## Reproduction, receipts, and limitations

From this checkout's root, with the existing Python environment:

```powershell
python research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/PRIVATE_AUDIT.py --private-root C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1 --output research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/private_audit_NEW
python research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/PRIVATE_AUDIT_CHECKS.py
```

The output directory must be new; collisions are rejected. The checks script validates the delivered `private_audit_02` receipts and independent fixed arithmetic derivative tests. The audit never calls the historical complete verifier, because that function regenerates fixtures and would still encounter the intentionally missing summary. Pure frozen forward and objective helpers are reused, so this is not an independently authored end-to-end replay. Personal residuals, paired metrics and error propagation are independently expressed; derivative checks validate the new residual implementation.

The successful audit reports 911 checks, 7.703125 measured Python CPU seconds, 77.453 wall seconds and 82,788,352 bytes sampled peak RSS. The failed first invocation encountered Git-quoted Hebrew paths before private analysis; its 6.534625 reported command wall seconds are retained, while CPU/RSS were not captured. Git subprocess CPU, process startup/exit, authoring and orchestration are not included in the Python CPU figure. Do not treat unknown overhead as zero. Additional deterministic-check CPU is recorded in `private_checks.json`.

Inputs and outputs are SHA-256 bound in the new receipts. The failed attempt is preserved. Zero optimization, zero research-world generation, zero new policy evaluation, zero paid calls/data-model downloads, zero historical repair, and no merge.
