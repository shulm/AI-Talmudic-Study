# Independent review of PR #12 and the next short-history experiment

Date: 2026-11-25. Reviewed final: `40d201997ab8d79d138734b1ef116c161719c11b`. Pre-fit: `1ac9eaec22230d3db2b46ebdda3ada1f84f25366`. Selection: `f830fbd989d196ebf5b44c2c862a2725da330c81`.

## 1. Disposition

**The bounded synthetic qualification is supported by the inspected implementation and public evidence. Proceed to a separately frozen short-history numerical study.**

The review found no score-invalidating error in the separated objective, A-development selection, logical training/support/query boundaries, oracle metrics, or declared predictive gates. Both held-out realizations pass the four gates. This qualifies a rank-two head with known shared logits, two informative numerical features, and 96 support observations. It does not establish performance at 16 observations, with natural-language embeddings, or on human decisions.

One concrete validation weakness remains: the generic verifier can label an empty run `PASS`, and the report's success flag does not explicitly require every audit/numerical prerequisite. The actual completed run has all required evidence and an exact supplemental audit, so this does not invalidate v2. The next version must make complete-run verification and overall qualification explicit conjunctions of their required evidence.

The completed historical pilot and v1 failures remain preserved. This review ran no model fits and generated no new prediction conditions.

## 2. Scientific result and selection

The pinned [results](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/RESULTS.md) report:

| Measure | Held-out A | Held-out B | Gate |
| --- | ---: | ---: | --- |
| Positive expected-NLL improvement | 0.647037383834 | 0.648745897342 | at least 0.05 |
| Oracle-gap recovery | 0.978751661292 | 0.979931153328 | at least 0.50 |
| Personal-contrast NRMSE | 0.133680284438 | 0.123272421144 | at most 0.50 |
| Null expected-NLL degradation | 0.005625588593 | 0.006591984071 | at most 0.01 |

The remaining null allowances are approximately 0.00437441 and 0.00340802. Null performance is worse than B3, within the declared tolerance; it is not zero degradation or a universal no-harm result. Realized accuracy can also decline under the null, as the report discloses.

All three candidates were eligible on A development. Their positive expected-NLL gains were 0.651015161532, 0.652849062994, and 0.638412395634. The selected $\rho=0.01$ leads the runner-up by approximately 0.00183390, comfortably above the $10^{-5}$ tie tolerance. The recorded choice follows the predeclared rule. See [A_dev.json](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/A_dev.json) and [SELECTION.json](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/SELECTION.json).

Independent public-JSON arithmetic checked 70 scalar comparisons across all 14 stage rows and reconstructed all gates and selection. Maximum discrepancy was zero. This does not replay the underlying private prediction arrays.

## 3. The implemented method matches the intended mathematics

The [head implementation](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/labs/decision_functions_diagnostics_v2/head.py) fits

$$
\ell_{sic}=g_{ic}+b_{sc}+u_s^\top V_cz_i,
$$

with

$$
J=\operatorname{meanCE}
+\frac\rho2\left(\|V\|_F^2+\frac{\|U\|_F^2}{S}\right)
+\frac{\lambda_b}{2S}\|b\|_F^2.
$$

The gradients use $\rho V$, $\rho U/S$, and $\lambda_b b/S$ in their respective blocks. New-person adaptation preserves the separate penalties. The certificate correctly uses $\lambda_b$ in the intercept residual and strong-convexity error denominator, and $\rho/\sqrt S$ as the spectral threshold.

The [staged execution code](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/labs/decision_functions_diagnostics_v2/study.py) consumes training labels for shared fits and support labels for personal adaptation. A development uses its designated people and question groups. B is generated after the selection publication check and the A evaluation, then trains new shared parameters under the frozen configuration. Its outcomes do not select another rho.

The generated fixture contains oracle/query arrays, but the inspected learning paths do not pass them to fitting. This is a logical code boundary, not a claim of OS-enforced secrecy on the executing machine.

Expected NLL integrates over the oracle's query-response distribution. It removes sampled query-response noise from that metric while retaining training/support-response variation. The contrast metric removes question-independent personal offsets and shared logits; its recovery supports nonconstant personal responses to question features. The uninformative-support result is a deliberately constructed identifiability control, not a separate discovery about broad generalization.

## 4. Audit evidence supports the completed run

Independent checks reconciled all six stage ledgers:

| Stage | Optimizer records | Personal solves |
| --- | ---: | ---: |
| A offsets | 2 | 96 |
| A development | 38 | 480 |
| A batch checks | 8 | 32 |
| A held-out | 16 | 384 |
| B offsets | 2 | 96 |
| B held-out | 22 | 384 |
| Total | 88 | 1,472 |

These are 24 shared fits, 60 support-adaptation batches, and four training-offset batches. Exact IDs, configurations, required fields, finite values, and successful terminations agree with the declared stage definitions. The A-development hash matches its selection binding.

All 225 normalized-text hashes in the delivery manifest and all eight pre-fit scientific-source hashes match the exported files. Git-tree comparison confirms that previously present scientific files stayed unchanged through pre-fit, selection, and final delivery; only the active handoff changed. All 287 prior pilot/v1 laboratory and run files retain their identities.

The committed verification loops account for 329 primary arithmetic comparisons and 280 supplemental comparisons. Their reported private-array discrepancies are $2.22\times10^{-16}$ and zero. These are executor-run saved-array results, not a private-cache replay performed in this review.

All seven command receipts report successful exit. Their sums match [RESOURCE_USAGE_FINAL.json](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/RESOURCE_USAGE_FINAL.json): 27.171875 sampled CPU seconds, approximately 72.829 profiled wall seconds, and 80,646,144 bytes peak sampled child RSS. The earlier resource file is a preserved subtotal, not a contradictory total. Sampling limitations and unprofiled operations remain disclosed.

Publication receipts and ledger times are consistent with the intended pre-fit and selection ordering. They support the code/record chronology without constituting independent observation of every action on the original machine.

## 5. Required repair: complete-run verification must require complete evidence

The pinned [verify.py](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/labs/decision_functions_diagnostics_v2/verify.py) skips missing stage files, validates only existing ledger directories, and checks upper limits rather than the exact complete-run stage set. An isolated non-fitting check during this review reproduced:

```json
{
  "status": "PASS",
  "comparisons": 0,
  "optimizer_records": 0,
  "person_solves": 0,
  "stages": []
}
```

The related [report.py](https://github.com/shulm/AI-Talmudic-Study/blob/40d201997ab8d79d138734b1ef116c161719c11b/labs/decision_functions_diagnostics_v2/report.py) derives qualification from selection and predictive gates while assigning audit completeness without an explicit conjunction over verification, numerical state, and exact completion.

The actual run is complete, its batch checks pass, and its supplemental audit requires the exact 88/24/1,472 counts. Those facts were independently checked in public records. The defect therefore affects what the tooling could falsely approve in another run; it does not show that this run is false.

In the next version, derive mandatory stages, archives, array keys, expected rows, and ledger IDs from the frozen protocol. Distinguish `VERIFIED_COMPLETE`, `VERIFIED_DECLARED_EARLY_STOP`, and `INCOMPLETE`. An empty or missing mandatory component cannot become a successful complete run. Overall qualification must require complete audit evidence, passed numerical checks, completed saved-array verification, and all primary predictive gates. Do not change or rerun v2 to hide this limitation.

## 6. The next scientific question: sixteen well-covered observations

Keep shared training fixed at $\rho=0.01$, $\lambda_b=0.1$, rank two. Changing history length changes personal adaptation; it does not require refitting shared models for every budget. Two fresh realizations, two regimes, and three initialization seeds therefore require only

$$2\times2\times3=12$$

shared fits.

Use primary $k=16$, secondary $k=4,32,96$, and a zero-fit $k=0$ fallback. Use two outcome-blind nested support schedules within the existing 32-group/96-case training support pool. Whole question groups remain in their original train/query partitions even when only part of a training group is observed in a short history.

For each rotational group,

$$
\sum_{j=0}^{2}z_jz_j^\top=\frac32 I.
$$

Hash-order groups and cyclically order their three cases, then take case prefixes. This gives exact raw Gram spectra:

| k | Revealed cases | Eigenvalues of $Z_H^\top Z_H/k$ |
| ---: | --- | --- |
| 4 | One full group plus one case | 0.375, 0.625 |
| 16 | Five full groups plus one case | 0.46875, 0.53125 |
| 32 | Ten full groups plus two cases | 0.484375, 0.515625 |
| 96 | Thirty-two full groups | 0.5, 0.5 |

No angle search, labels, oracle scores, or fitted personal parameters are used to choose histories. This deliberately provides good feature coverage. Passing it would not establish performance for arbitrary, naturally collected histories.

Near-isotropic raw features do not guarantee sufficient categorical information. Class-probability saturation and confounding between personal offsets and interaction coordinates still matter. Explanatory curvature calculations should remove the common-logit-shift direction and distinguish data curvature from ridge curvature. They cannot select histories or change the gate.

## 7. One prespecified adaptation-scaling control

The primary adaptation policy remains

$$
\frac1k\sum_i\operatorname{CE}_i+
\frac{0.01}{2}\|u_s\|^2+
\frac{0.1}{2}\|b_s\|^2.
$$

It tests the frozen algorithm's learning curve. In summed-loss units, its ridge coefficients are $0.01k$ and $0.1k$. Thus this is not a study holding summed-likelihood prior precision fixed as observations disappear.

At $k=16$, add one separately reported secondary policy:

$$
\rho_{\mathrm{adapt}}=0.01\frac{96}{16}=0.06,
\qquad
\lambda_{b,\mathrm{adapt}}=0.1\frac{96}{16}=0.6.
$$

This preserves the summed-loss ridge precision of the qualified 96-support setting. Shared fits stay unchanged. Compare that M1 to B3 with the matching offset penalty 0.6, not to primary B3 with 0.1. There is no parameter search or selection between policies. A secondary success cannot turn a primary failure into qualification, but it can show whether the result is sensitive to the adaptation convention.

## 8. Controls, uncertainty, and next boundaries

Use the adjacent matched person as a single donor, $\pi(s)=s\mathbin{\mathrm{xor}}1$. The generator makes these pairs share offsets and have opposite planted interaction phases. The mapping is fixed from metadata, not selected using queries. Because question identities and history budgets are common, wrong-history predictions are row permutations of existing same-budget predictions. Score them against the recipient's oracle/outcomes. This requires no new fits and avoids averaging donor probabilities before scoring. Under the null, paired oracle distributions are identical, so the pair-averaged expected donor contrast is zero algebraically; it is a structural sanity check, not evidence that the fitted head lacks spurious interaction. The positive-regime donor contrast is the substantive identity control.

Average losses across support schedules, not predictions from different histories. Otherwise a nominal 16-observation prediction could benefit from multiple histories. The three initialization seeds still form a probability ensemble within each one-history condition.

The 24 query people form 12 matched pairs, and the 36 query cases form 12 rotational groups. Paired uncertainty must resample whole person pairs and whole question groups. Report realizations separately; intervals are conditional on fitted models and declared histories and do not cover retraining or new domains. Primary qualification retains the four point-metric gates; confidence intervals are reported without retroactively changing the rule.

The executable assignment defines two fresh realizations, two support schedules, exact counts, the complete-run validator repair, and the fixed secondary policy. Maximum execution: 12 shared fits, 184 adaptation batches, 3,776 personal solves, 196 optimizer records. No human data, encoder acquisition, or corpus construction is included.

After this experiment, the text-representation question remains separate: can text-derived features retain the distinctions needed by a qualified numerical head? The next agent should prepare a representation contract as a proposal only. Parallel PRs #10/#11 already prepare provisional Bavli material; this numerical assignment does not duplicate or suspend that independent source work. Human and scholarly claims require their own source, attribution, and evaluation evidence.

## 9. Verification boundary

This review used source inspection, public scalar arithmetic, complete exported ledgers/manifests, and isolated non-fitting failure checks. Neither original private cache was available. No prediction arrays were independently replayed from that cache; no new models or prediction conditions were generated. The [public receipt](public_review_receipt.json) distinguishes independent checks from executor-reported replay and preserves the scoped qualification.
