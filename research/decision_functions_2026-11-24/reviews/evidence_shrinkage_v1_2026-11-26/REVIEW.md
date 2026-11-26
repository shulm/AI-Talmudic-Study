# Independent review of PR #20

## Disposition

Retain **INCOMPLETE / NUMERICALLY_UNRESOLVED**, qualification false, at [f18255c5fad37f704881ff1f9ad50cd113497236](https://github.com/shulm/AI-Talmudic-Study/commit/f18255c5fad37f704881ff1f9ad50cd113497236).

The inspected scientific implementation and public arithmetic are consistent with the [PR #19 assignment](https://github.com/shulm/AI-Talmudic-Study/tree/724be8c49808e1e1b8643d81c73267f7577439c8/research/decision_functions_2026-11-24/reviews/short_history_v1_2026-11-25). The implementation stopped at its frozen numerical validity gate. Its available ES predictions additionally fail contrast recovery in all four realizations and all eight histories. There is no basis to raise a tolerance, repair the historical summary, retry a solve, or declare predictive success.

The next assignment addresses the two issues with saved-artifact diagnosis and numerical engineering. It does not launch another scientific parameter sweep.

## What the review independently established

| Evidence | Independent check |
|---|---|
| Exported laboratory/run files plus root instructions | 252 exact Git blob identities |
| Public delivery manifest | 233 SHA-256 identities match |
| Scientific pre-fit freeze | All 18 source/protocol SHA-256 identities match |
| Historical preservation | All 965 declared historical blobs match both the assignment and final trees |
| Protocol | Exactly equal to the PR #19 machine-readable design |
| Optimization inventory | 12 exact ledgers; 76 starts and completions; 12 shared fits; 64 personal batches; 1,664 personal solves |
| Archive inventory | 36 archive roles; 588 declared array shapes; 176 query prediction arrays |
| Private artifact references | 112 hash bindings agree across public manifests and the partial receipt |
| Public score/evidence arithmetic | 6,796 comparisons; 144 rows; 72 aggregates; 384 person-history evidence rows |
| Independent equation checks | 1,814 comparisons over 760 ordered toy assignments and 42 count groups |
| Recorded private replay coverage | Exactly 1,158 successful IDs; exactly two declared IDs unreached |

Public score arithmetic differs by at most 3.21e-16, excluding raw evidence calculations. Evidence magnitudes differ by at most 2.04e-10 under an explicitly declared 1e-14 relative tolerance; log evidence and weights use 1e-12 absolute tolerance. The independent deterministic enumeration agrees with the implemented conditional-count DP within 8.88e-16.

The original private cache was unavailable. Hash bindings are not private-byte verification, and recorded comparison coverage is not independent private replay. This review did not regenerate E/F/G/H or fit any model.

The source inspection covered the mixed-pair generator, information boundaries, matched histories, seed-specific U/V priors, exact count normalization, arithmetic evidence averaging, fixed weight map, query predictions, donor row permutation, history aggregation, bootstrap pairing, numerical gate and terminal control flow. No substantive scientific deviation was identified.

## Numerical stop

The [published numerical results](https://github.com/shulm/AI-Talmudic-Study/blob/f18255c5fad37f704881ff1f9ad50cd113497236/research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/H_numerical.json) show:

| Realization | Maximum probability difference | Maximum expected-NLL difference |
|---|---:|---:|
| E | 1.6396200e-7 | 9.6183889e-8 |
| F | 3.0976498e-7 | 1.8677740e-7 |
| G | 2.5995425e-7 | 5.2907670e-8 |
| H | 1.2232537e-6 | 3.1479469e-7 |

Both frozen conditions were required: probability difference at most 1e-6 and expected-NLL difference at most 1e-5. H therefore fails.

All 76 optimizers reported success. That flag is different from a verified precision requirement. The personal objective is the mean of separable per-person objectives. Its exact minimizer is independent of batch size, but the implementation uses one joint L-BFGS-B process, batch-scaled gradients, and both function-reduction and gradient stopping.

For H, history 101, seed 11:

| Batch size | Stop reason | Global maximum gradient | Person-scaled maximum |
|---|---|---:|---:|
| 1 | Gradient | 5.8798872e-9 | 5.8798872e-9 |
| 7 | Function reduction | 9.4588924e-8 | 6.6212247e-7 |
| 48 | Function reduction | 2.3249903e-8 | 1.1159953e-6 |

The version-matched [SciPy documentation](https://docs.scipy.org/doc/scipy-1.15.1/reference/optimize.minimize-lbfgsb.html) specifies these stopping conditions separately. Tightening only the gradient tolerance does not prevent earlier function-reduction termination.

These observations explain why the chosen implementation does not ensure equal per-person precision. They do not establish a unique cause of H's discrepancy or identify which compared solution is closer to its optimum. The public maxima cover all people in each batch; batch 48 is a comparison reference, not ground truth.

Across the run, all 12 shared solves stopped on function reduction; 25 of 64 personal solves did so, and 39 personal solves stopped on gradient. The maximum personal-only scaled residual is 1.5631002109328662e-6. The report's larger 2.8448765301128387e-5 maximum includes shared optimization and should not be read as the personal-head maximum.

The method note derives a residual bound for each fixed-V personal optimum. It does not certify global optimality of the nonconvex shared training problem.

## Partial verification means two unreached checks

The [frozen verifier](https://github.com/shulm/AI-Talmudic-Study/blob/f18255c5fad37f704881ff1f9ad50cd113497236/labs/decision_functions_evidence_shrinkage_v1/verify.py) reads scientific_summary.json before its final qualification comparison. The executor intentionally never writes that file after the numerical stop. The missing-summary exception therefore prevents both final IDs, qualification and resource_contract, from being recorded.

The correct statement is: **1,158 successful recorded checks of 1,160 declared, two unreached, no complete verification verdict.** It is not two failed numerical comparisons.

The post-run observer retains the unchanged verifier's exception and recorded checks. Its maximum reached discrepancy is 2.842170943040401e-14. The observer's successful capture and separate delivery inventory do not turn the original study into VERIFIED_COMPLETE. Future laboratories should write a terminal status record on success and failure paths, so that a failed study can still have complete evidence. That future engineering improvement must not repair PR #20.

## Scientific observations

All numbers below are descriptive observations from a numerically unqualified run.

| Realization | ES active NLL gain | Oracle-gap recovery | ES contrast NRMSE | Inactive degradation |
|---|---:|---:|---:|---:|
| E | 0.507506520 | 0.761034057 | 0.555275892 | 0.00000924234 |
| F | 0.502356548 | 0.752794678 | 0.564899179 | 0 |
| G | 0.519710034 | 0.778996614 | 0.534684508 | 0 |
| H | 0.514874692 | 0.770563481 | 0.556166871 | 0 |

The 0.50 contrast limit fails in every realization and every individual history; history NRMSE ranges from 0.521022 to 0.581864. Averaging did not create the failure.

The predeclared controls identify two contributions to the observed attenuation:

| Realization | Raw M1 contrast | Fixed 90% M1 mixture | ES contrast |
|---|---:|---:|---:|
| E | 0.408206 | 0.513979 | 0.555276 |
| F | 0.394396 | 0.504310 | 0.564899 |
| G | 0.381241 | 0.494657 | 0.534685 |
| H | 0.403816 | 0.511815 | 0.556167 |

Raw M1 passes contrast in all four but fails inactive degradation, approximately 0.0353–0.0470. The fixed mixture already fails contrast in E/F/H and inactive degradation in all four. ES adds further active loss and contrast error while reducing inactive loss in these arrays.

A probability mixture with B3 adds a floor to each class probability. This can attenuate extreme class log-odds. Expected NLL weights answers by their oracle probabilities; contrast measures class-pair log-odds differences across people and questions. Strong expected-NLL gains do not imply accurate log-odds contrast recovery.

All 192 active person-history weights are positive; 153 hit the 0.9 cap. Of 192 inactive rows, 190 weights are zero, and the remaining two are about 0.03337 and 0.03076. No inactive row hits the cap. These counts describe repeated histories of the same people, not 192 independent people per stratum.

This supports a single deterministic cap-removal diagnosis. It does not prove that the cap is the only cause, that every weight bounded by 0.9 must fail, or that an uncapped method will generalize.

## Provenance and resource accounting

The scientific pre-fit commit was posted in issue #2 at 2026-11-25 21:18:59 UTC and PR #20 at 21:19:00 UTC. The retained readback receipt is 21:19:08.928803 UTC; the first optimizer start is 21:19:10.988078 UTC. The sequence is consistent with publication before fitting.

Only root AGENT_HANDOFF.md and the outcome note in the proposal-only text specification changed among existing pre-fit files. Scientific source/protocol hashes are unchanged. Relative to the PR #19 assignment, the other existing-file change is .gitattributes; all declared historical scientific blobs remain identical.

Seven supervised commands account for 43.203125 sampled CPU seconds, plus 0.265625 separately measured review CPU seconds, totaling **43.46875 seconds**. The delivery audit's internal timing is already included and was not added twice. Profiled wall time is 59.374 seconds; peak sampled RSS is 101,486,592 bytes. The two failed commands are the mandated execution stop and complete-verifier rejection. Sampling can miss short transients and does not include all orchestration overhead.

## Next decision

Execute the adjacent H0–H4 assignment:

1. Diagnose saved personal parameters and quantify their numerical uncertainty without refitting.
2. Evaluate exactly one uncapped ES rule on the same saved components as a post hoc ablation.
3. Implement a personwise solver with an explicit residual stopping condition on fixed engineering fixtures.
4. Make future failure paths publish complete terminal evidence.
5. Return a decision and the next independent-study proposal.

Do not turn this into another tuning grid or require repeated synthetic success before every empirical text baseline. Text-based prediction can be studied without claiming the conditional-null theorem; transporting that theorem to an estimated population predictor requires an additional argument.

PR #18 advanced during this review to cdcafb41726820265bd4e1dea5272702f2663aae after a focused execution-accounting and repeat-verification repair. Its current handoff and supervisory review still identify it as frozen and scientifically unexecuted. This review inspected its updated metadata, handoff, review comments and changed-path list for coordination; it did not independently repeat that repair audit. PR #18 retains its separate scientific-execution authorization boundary. No corpus production, source review, human evaluation, encoder acquisition, fresh scientific seed execution, or merge is part of this assignment.
