# Review of short_history_v1 and the next research question

Date: 2026-11-25. Reviewed final `ee2b0a5a2f0916fed3dd59f720b902eb332eecc3`, pre-fit `89d9e0ca1b3fe3e23c3829294d3a806949943d3a`, assignment `47b19560350aa8c5d877d99f381d5b27f5b3490a`.

## 1. Disposition

**Retain `VERIFIED_COMPLETE / COMPLETED_PRIMARY_FAILURE`.** No score-invalidating error was found in the objective, support construction, information boundaries, primary/secondary comparisons, history aggregation, contrast metric, donor construction, or bootstrap implementation. The full declared experiment finished and preserved its failure.

The result establishes useful question-dependent personal recovery under the controlled numerical setting. It rejects the full primary qualification because null degradation exceeds the fixed allowance. These statements are compatible: learning genuine interactions where they exist does not establish reliable behavior where they are absent.

This review used public sources, summaries, exact ledgers and manifests. It did not have the private executor cache, fit models, generate new scientific fixtures/prediction conditions, or rerun the private saved-array calculations.

## 2. Results and arithmetic

The [pinned report](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/research/decision_functions_2026-11-24/runs/short_history_v1/RESULTS.md) gives:

| Primary k=16 measure | C | D | Gate |
| --- | ---: | ---: | --- |
| Expected NLL gain | 0.594196396265 | 0.602815011497 | at least 0.05 |
| Oracle-gap recovery | 0.863611274630 | 0.877918026354 | at least 0.50 |
| Contrast NRMSE | 0.283460783779 | 0.248433285313 | at most 0.50 |
| Null degradation | 0.052185645516 | 0.057411041409 | at most 0.01 |

Independent arithmetic reproduced 1,216 scalar comparisons over all 48 condition rows and 28 aggregates, including subtraction, ratios, contrast normalization, loss-level history aggregation, gates/margins, and agreement with `results_summary.json`. Maximum discrepancy was zero.

Both primary null schedules fail: C has 0.0447660 and 0.0596052; D has 0.0592982 and 0.0555239. The reported conditional bootstrap intervals for aggregate null degradation, [0.0407992, 0.0630563] and [0.0489810, 0.0658663], are also well above 0.01. The gates remain point-metric rules. These conditional intervals do not include shared-model retraining or new-population uncertainty.

### The secondary result does not isolate one penalty

The secondary policy changes both interaction penalty 0.01→0.06 and offset penalty 0.1→0.6. Its B3 comparator receives the same offset change. Under the null:

| Expected NLL | C primary | C secondary | D primary | D secondary |
| --- | ---: | ---: | ---: | ---: |
| B3 | 1.112866011514 | 1.088134837334 | 1.124853282881 | 1.090407556384 |
| M1 | 1.165051657030 | 1.097721824078 | 1.182264324290 | 1.101329009213 |

Both methods improve. The result is sensitivity to a joint adaptation policy, not isolated causal evidence that interaction shrinkage alone fixes the problem. Secondary null degradation is 0.009586986743 on C and 0.010921452829 on D. C's schedule 211 also fails descriptively at 0.011412972449. No secondary result rescues the primary.

Secondary positive expected NLL improves on both realizations, while contrast NRMSE worsens to 0.335467/0.375023. Predictive loss and recovery of contrast magnitude need not improve together.

### The issue extends beyond sixteen observations

| Primary history size | C null degradation | D null degradation |
| ---: | ---: | ---: |
| 4 | 0.201145975377 | 0.192744077196 |
| 16 | 0.052185645516 | 0.057411041409 |
| 32 | 0.023877401092 | 0.031551716285 |
| 96 | 0.008535836573 | 0.012138861736 |

The decline with history size is consistent with an estimation-variance contribution, but it does not uniquely establish a mechanism. D's 96-case failure shows that the earlier A/B qualification does not extend uniformly even within this generator family. Preserve that earlier bounded result and the new counterexample. Do not phrase the next problem as solely a defect unique to k=16.

The source values are in [C_scores.json](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/research/decision_functions_2026-11-24/runs/short_history_v1/C_scores.json) and [D_scores.json](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/research/decision_functions_2026-11-24/runs/short_history_v1/D_scores.json).

## 3. Implementation and information boundaries

[execute.py](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/labs/decision_functions_short_history_v1/execute.py) separates learner, support and evaluator views. Shared fitting uses training people/questions; adaptation uses the new people's support labels. Query labels/oracles are loaded for scoring after predictions are saved. This is source-level separation, not independent observation of all actions on the private executor.

Support schedules use fixed hashes of IDs, not outcomes or angle-based search. The raw Gram contracts pass. The 96-case anchor is fitted once per condition and reused, k=0 is analytic, and the uninformative condition correctly obtains M1 from B3 with u=0.

[scoring.py](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/labs/decision_functions_short_history_v1/scoring.py) ensembles seed probabilities within a history and averages losses/squared contrasts across histories. The bootstrap preserves both people in each pair and all three questions in each group; the verifier uses an independently expressed multiplicity-weight calculation. Positive donor results use engineered equal-offset/opposite-phase pairs. Null expected donor loss is a structural zero under the pair swap, not a test against spurious interaction.

Projected k=16 data curvature is nonsingular under the stated diagnostic threshold. Together with the geometry and batch checks, this rules out failures of those declared numerical contracts as a sufficient explanation. It does not prove statistical sufficiency, calibrated posterior uncertainty, or impossibility at sixteen observations.

## 4. Complete-run verification is repaired

The original empty-run PASS path is fixed. An isolated zero-fit invocation now exits with status 1 and returns `INCOMPLETE`, qualification false, `Missing all ledgers`, and zero reached comparisons. The qualification function also rejects incomplete, early-stop and numerical-failure states even when supplied with all predictive gates true.

All six ledgers reconcile:

| Stage | Optimizer records | Person-solves |
| --- | ---: | ---: |
| C shared | 6 | 0 |
| C support | 76 | 1,824 |
| C batch | 16 | 64 |
| D shared | 6 | 0 |
| D support | 76 | 1,824 |
| D batch | 16 | 64 |
| Total | 196 | 3,776 |

This is 12 shared fits and 184 adaptation batches. Exact identities, metadata, finite evidence and successful optimizer terminations match the frozen contract. All 452 normalized-text delivery hashes and 12 pre-fit scientific-source hashes match. The 690 public archive-array shapes match their declared contracts. The 214 private hash bindings agree across manifests and verifier receipts after normalizing path separators; their underlying private bytes were unavailable here.

The reported 17,038 unique comparison IDs agree with the source-derived count. Their executor-reported maximum discrepancy is 3.552713678800501e-14. This is a count of checks, largely including curvature calculations; it is not 17,038 independent experiments. The review did not replay those private calculations.

Git-tree inspection confirms all 513 historical pilot/v1/v2 laboratory/run blobs retain their identities. Previously present files changed after pre-fit are only the root handoff and the proposal-only text specification's outcome note; frozen scientific code and protocol are unchanged. Public pre-fit issue/PR comments precede the publication receipt and the first optimizer record.

Nine profiled command receipts total 78.984375 sampled CPU seconds, 143.17000000039116 profiled wall seconds, and 90,120,192 peak sampled RSS bytes. Adding 0.1875 measured Python audit CPU gives the reported 79.171875 accounted subtotal. The two failed commands are disclosed pre-fit engineering tests, not scientific retries. Unprofiled overhead and sampling limitations remain explicit in [RESOURCE_USAGE_FINAL.json](https://github.com/shulm/AI-Talmudic-Study/blob/ee2b0a5a2f0916fed3dd59f720b902eb332eecc3/research/decision_functions_2026-11-24/runs/short_history_v1/RESOURCE_USAGE_FINAL.json).

### A bounded forward-replay improvement

The verifier replays statistics from saved probabilities, donor/analytic identities, parameter norms and support curvature. It does not independently bind each saved shared basis to its full optimizer-vector slice or regenerate every existing B3/M1 query probability from saved parameters. The execution source is consistent and no mismatch is observed; this does not invalidate the result. Add these zero-optimization forward checks in the next laboratory. Another audit-only research cycle is unnecessary.

## 5. Next question: evidence-dependent personalization in a mixed population

All previous synthetic positive/null regimes trained separate shared bases. Therefore they do not test whether the same useful shared representation can serve a person with strong interaction and another person with no interaction. That is the next substantive question.

Use one mixed population per realization, with active and inactive people in both training and held-out partitions. Learn one shared basis per initialization. Keep the existing .06/.6 personal adaptation policy fixed for B3/M1, then compare:

1. B3 personal offsets.
2. M1 interaction prediction.
3. A fixed 90% M1 / 10% B3 mixture.
4. One evidence-dependent mixture, the sole new primary method.

The new method conditions the support-label likelihood on class counts, removing arbitrary constant personal offsets. A training-only mixture of conditional likelihood ratios has null expectation one. Its value E determines

$$h(E)=\min\{0.009(E-1)_+,\log 10\},\qquad w(E)=1-e^{-h(E)},$$

$$p_{\rm ES}=(1-w)p_{\rm B3}+wp_{\rm M1}.$$

This supplies an expected null excess-log-loss bound of 0.009 under the explicit model assumptions, while permitting partial personalization below a hard rejection threshold. It does not guarantee an observed realization's mean loss, positive recovery, correctness of a learned population predictor, or human-domain performance. The complete derivation and sources are in [METHOD_NOTE.md](METHOD_NOTE.md).

Four fresh 192-person mixed realizations retain 24 active and 24 inactive held-out people each. Two fixed 16-case histories, three shared seeds, and a single fixed policy require 12 shared fits, 64 adaptation batches, 1,664 person-solves, and 76 optimizer records. The original four point gates apply to the new primary method separately on every realization. No control or pooled result rescues a failure; the theoretical expectation bound does not replace those empirical gates.

This is a new method and new mixed-population question. It does not relabel C/D as fresh confirmation, rerun them with another strength, or claim the secondary policy was retrospectively qualified. Text remains a separate representation problem; the known-base assumption and fixed answer-label meanings must be addressed before transferring the bound to natural-language tasks. Parallel corpus preparation, including PRs #14/#16, may continue under its separate instructions.
