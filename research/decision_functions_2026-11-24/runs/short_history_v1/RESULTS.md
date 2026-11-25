# Short-history v1: fixed numerical method at 16 observations

Outcome: **COMPLETED_PRIMARY_FAILURE**. Verification: VERIFIED_COMPLETE. Numerical checks: True.

Shared rho=.01, offset penalty=.1, rank two. No tuning. Primary policy retains these adaptation penalties. The prespecified secondary policy uses .06/.6 at k=16 with its matching B3 comparator. Secondary success cannot rescue primary failure.

| Realization | Policy | Expected gain | Oracle-gap recovery | Contrast NRMSE | Null degradation | Gates |
|---|---|---:|---:|---:|---:|---|
| C | primary | 0.594196396265 | 0.86361127463 | 0.283460783779 | 0.0521856455164 | {'gain': True, 'recovery': True, 'contrast': True, 'null': False} |
| C | count_scaled_secondary | 0.598978285668 | 0.88542901342 | 0.335466537577 | 0.00958698674347 | {'gain': True, 'recovery': True, 'contrast': True, 'null': True} |
| D | primary | 0.602815011497 | 0.877918026354 | 0.248433285313 | 0.0574110414085 | {'gain': True, 'recovery': True, 'contrast': True, 'null': False} |
| D | count_scaled_secondary | 0.58874602741 | 0.882308089581 | 0.375023149822 | 0.0109214528293 | {'gain': True, 'recovery': True, 'contrast': True, 'null': False} |

These point metrics average per-history losses and squared contrasts, not probability mixtures across histories. Seed probabilities are ensembled only within one history. Every gate uses unrounded values. Full schedule-specific metrics, margins, worst-schedule margins, support curves, B1/B2/B3/M1 accuracy/NLL/Brier and donor contrasts are in C_scores.json and D_scores.json.

## Conditional uncertainty

| Realization | Primary metric | Point | 95% interval |
|---|---|---:|---|
| C | positive_gain | 0.594196396265 | [0.5683659615072316, 0.6182255272688848] |
| C | null_degradation | 0.0521856455164 | [0.04079924002042824, 0.06305625834914612] |
| C | positive_donor | 3.82920422768 | [3.565073067188733, 4.10123597906343] |
| D | positive_gain | 0.602815011497 | [0.5768916849459744, 0.6238939063898943] |
| D | null_degradation | 0.0574110414085 | [0.048981003607609166, 0.06586630719731808] |
| D | positive_donor | 3.42710885963 | [3.119453361511723, 3.7363974221873804] |

Each interval uses 2,000 paired resamples of whole person pairs and whole three-case question groups, with identical indices across contrasts. They are conditional on fitted models and fixed schedules, excluding retraining/domain uncertainty. C and D are separate; schedules and initialization seeds do not create more independent people. Gates remain point-metric rules.

## Controls and interpretation

Support schedules use SHA-256 of IDs only. Raw feature Gram spectra meet the frozen 1e-12 contract at all budgets. Histories are deliberately well-covered; this does not establish performance for arbitrary observed histories. The k=96 prediction is one canonical-order anchor reused by both schedules; k=0 uses analytic fallback.

Matched-other predictions are saved row permutations with map row xor 1 and recipient outcomes/oracles. Equal-offset opposite-phase pairs form an engineered hard negative. Under the null the pair-average expected donor contrast is zero algebraically; this is not evidence against spurious fitted interactions. Uninformative k=16 M1 predictions equal the fitted B3 prediction analytically; no redundant M1 solves were performed.

Data-only and ridge-augmented personal curvature is reported for every saved individual M1 adaptation, in mean-loss units after removing the shared offset direction. These are explanatory diagnostics, not calibrated posterior intervals, selection criteria or evidence of an information-theoretic limit.

## Audit, resources and provenance

Exact scientific audit: 196 optimizer records; 12 shared fits; 184 adaptation batches; 3776 personal solves. No retries. Saved-evidence replay: 17038 comparisons; maximum discrepancy 3.552713678800501e-14. Private artifacts are hashed before/after. Complete verification requires both realizations and exact protocol-derived archive/array/row/ledger sets. No scientific early stop is declared.

Cumulative resources: 78.984375 sampled CPU seconds; peak RSS 90120192 bytes. 9 profiled commands; 2 unsuccessful command receipts. The retained unsuccessful zero-fit tests found a Windows path serialization issue and a syntax typo while adding shape contracts, both before any scientific fit; no scientific retry occurred. See PREFIT_ENGINEERING.md and RESOURCE_USAGE.json. Sampling and unprofiled overhead limits are explicit.

Fresh generator/label seeds C=20261128/2721 and D=20261129/2722; shared initialization seeds 11/29/47. Generator/head adapted from frozen v2 delivery 40d201997ab8d79d138734b1ef116c161719c11b. No pretrained encoder or downloaded model is used. Exact fitted basis and adapted-vector hashes are in each realization manifest.

Historical pilot/v1/v2 outputs and their failures remain unchanged. PR5/PR8 SRO outcomes are exposed; PR10/PR11 are separate provisional corpus tracks, not validated training labels. This experiment did not acquire source text, evaluate humans, train on scholarly positions or merge branches.

## Next review

Read TEXT_REPRESENTATION_NEXT_SPEC.md as a proposal only. If the primary policy fails, report the observed penalty sensitivity, geometry, curvature and numerical behavior without assigning a unique cause or calling the problem impossible. A secondary success remains descriptive. No representation experiment follows automatically from this delivery.

## Observed outcome and concrete next decision

The primary method recovers question-dependent personal interaction with16 well-covered observations in both C and D. It nevertheless fails the complete qualification because it invents enough interaction in the null to increase expected loss by0.0521856455163503 and0.05741104140850006, respectively. Both schedules fail that primary null gate in each realization. The positive recovery evidence and the null failure must both be retained.

The count-scaled secondary policy reduces null degradation to0.009586986743470138 on C and0.010921452829349976 on D. C's aggregate passes, but C schedule211 still fails its descriptive null gate. D fails in both schedules and in aggregate; its excess above the aggregate threshold is0.0009214528293499755, not a numerical tie. This demonstrates sensitivity to adaptation shrinkage in these fixtures, without proving a unique mechanism or selecting a replacement primary method.

The96-support anchor has null degradation0.00853583657312007 on C and0.012138861735729867 on D. Thus D's96-case anchor also exceeds0.01. This does not erase v2's qualification on its two specified realizations; it reinforces that the earlier bounded qualification was not a universal null guarantee.

At primary k16, realized positive accuracy improves B3→M1 from0.405093 to0.821759 on C and0.377315 to0.793403 on D. Null accuracy changes from0.366898 to0.357639 on C and0.352431 to0.357060 on D. Expected loss degradation does not imply identical accuracy behavior. Expected positive donor-minus-own losses are3.829204 on C and3.427109 on D; these compare deliberately opposite-phase matched donors, not an ordinary real-world donor pool.

Raw support geometry met the exact spectra on all schedules and budgets. Batch maximum probability differences were4.873261173488075e-7 on C and2.635265077821636e-7 on D, below1e-6; first-person expected-NLL differences stayed below1e-5. The k16 projected data curvature was nonsingular for all reported individual seeds/persons under the stated1e-12 singularity diagnostic. Positive primary minimum data eigenvalues ranged0.01969–0.18721 on C and0.01603–0.20550 on D; these diagnostics do not make inverse curvature a calibrated posterior. The observed failure cannot be explained merely by violating the raw geometry contract or the declared numerical checks. It is not evidence that16 decisions are information-theoretically insufficient.

Review the primary null failure and secondary sensitivity before authorizing a new modeling experiment. Do not reselect on C/D, loosen gates, add a strength or regenerate another realization. The text specification remains proposal-only and must carry a matched numerical control; no claim that a reliable primary16-case method has been established is authorized.

## Final provenance and resource receipt

The separate post-run audit verifies513 historical laboratory/run files retain their Git identities, all frozen scientific source hashes are unchanged, and the summary uses the required qualification conjunction. It made no new fits or predictions. See delivery_audit.json and postrun_source_receipt.json. Largest recorded optimizer gradient2.867201237667736e-7 and person-scaled residual1.3762565940805133e-5 are disclosed separately from termination and predictive gates.

RESOURCE_USAGE_FINAL.json is the final cumulative ledger:78.984375 sampled CPU seconds across9 profiled commands, plus0.1875 measured Python CPU seconds for the post-run audit; accounted subtotal79.171875 seconds. Peak sampled RSS90,120,192 bytes. Two failed pre-fit test commands are included. All scientific execution and replay commands succeeded; zero scientific retries. Git/metadata/supervisor/final reporting overhead and polling limitations remain explicitly unprofiled. No total end-to-end CPU claim is made.
