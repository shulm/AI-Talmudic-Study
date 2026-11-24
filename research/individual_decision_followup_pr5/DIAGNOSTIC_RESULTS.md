# Diagnostic results — exploratory, not confirmation

PR5 remains inconclusive. The stronger training-only item-frequency baseline outperformed own-history predictions in the declared reuse of102 exposed people. Single-donor replacement does not demonstrate a person-specific advantage. No independent confirmation ran.

All original35 manifested artifacts were available and hash-verified; no weights or old outputs were reconstructed or refitted. The independent AI methods signoff and diagnostic lock preceded new test probabilities. Freeze commit: dbb208f2129f356f414e9e47915f56ef40653ed9. The scorer recorded its attempt before label access and completed exactly once. This study has304 training,102 development and102 exposed-test people, eight nested source choices, ten target choices per person, one target schedule family. No exclusions changed.

## Development selection and pairing diagnostic

Fixed Beta(.5,.5) training-only item frequencies were selected by development NLL at8; there was no smoothing/calibration search. A target-context fit was unnecessary for these common ten items. Development banks were disjoint51-person opposite folds; test reference bank was all102 development people. The larger test bank is a declared design difference, not a new recipient-dependent computation. Bank posterior states use source answers only.

| Source-blind candidate | Development NLL at8 |
|---|---:|
| item_frequency | 0.408390 |
| integrated_prior | 0.613897 |
| empirical_reference | 0.449364 |
| legacy_population | 0.566744 |

Development-only inference permutation-minus-own: 0.018613 [0.000611, 0.035674] nats. This moves intact histories, without retraining. The descriptive interval ignores cross-fold bank dependencies and original model selection; it cannot establish generalization. Development value-minus-own was -0.039792 [-0.064053, -0.016039]. Pairing sensitivity alone is insufficient when the strong source-blind comparator is better.

## Declared exposed-test contrasts

Positive values favor own prediction, except the Jensen gap which measures averaging benefit. Each interval is a2,000-draw paired participant percentile interval conditional on fitted models and fixed bank, not independent confirmation or simultaneous coverage. Zero-budget identity/mixture compare the historical fallback; coherent zero below uses the integrated prior. Tiny zero-budget values around1e-17 are floating-point noise.

| k | Strong-baseline minus own | Mean single-donor loss minus own | Donor-mixture loss minus own | Jensen gap |
|---:|---|---|---|---|
| 0 | -0.230920 [-0.261630, -0.197974] | 0.000000 [0.000000, 0.000000] | -0.000000 [-0.000000, 0.000000] | 0.000000 [-0.000000, 0.000000] |
| 2 | -0.124369 [-0.154832, -0.093788] | -0.007173 [-0.029011, 0.013797] | -0.013886 [-0.035558, 0.006794] | 0.006713 [0.005650, 0.007914] |
| 4 | -0.117973 [-0.147618, -0.088530] | -0.006879 [-0.030854, 0.014978] | -0.015910 [-0.039507, 0.005780] | 0.009030 [0.007676, 0.010531] |
| 8 | -0.071577 [-0.097832, -0.045677] | 0.003012 [-0.019581, 0.024749] | -0.007573 [-0.029800, 0.013568] | 0.010585 [0.008861, 0.012491] |

At8, the donor replacement estimate is slightly positive while the probability-mixture estimate is negative. Their0.010585-nat difference is the Jensen averaging benefit, not evidence of identity. Both specificity intervals cross zero. The item-frequency comparator beats own by0.071577 nats; this diagnoses a weak historical baseline comparison, not the absence of all personal information. The empirical-history reference also predicts well without recipient history; its at8 difference from own is -0.017076 [-0.037720, 0.001499].

## Coherent learning curve and all saved metrics

Own zero is the same frozen model's integrated Normal prior. The historical own-zero fallback is retained separately. Own NLL improves from0.611063 at0 to0.451720 at8, yet item frequencies achieve0.380143. A learning-curve improvement against the prior is not sufficient evidence of useful personalization.

| Saved predictor | NLL | Full-vector Brier | Accuracy |
|---|---:|---:|---:|
| own_0 | 0.611063 | 0.418632 | 0.798039 |
| integrated_prior_0 | 0.611063 | 0.418632 | 0.798039 |
| item_frequency_0 | 0.380143 | 0.244724 | 0.823529 |
| empirical_reference_0 | 0.611063 | 0.418632 | 0.798039 |
| legacy_population_0 | 0.562996 | 0.373514 | 0.798039 |
| historical_summary_0 | 0.562996 | 0.373514 | 0.798039 |
| donor_mixture_0 | 0.562996 | 0.373514 | 0.798039 |
| own_2 | 0.504512 | 0.326165 | 0.798039 |
| integrated_prior_2 | 0.611063 | 0.418632 | 0.798039 |
| item_frequency_2 | 0.380143 | 0.244724 | 0.823529 |
| empirical_reference_2 | 0.486554 | 0.305575 | 0.823529 |
| legacy_population_2 | 0.562996 | 0.373514 | 0.798039 |
| historical_summary_2 | 0.514120 | 0.330904 | 0.817647 |
| donor_mixture_2 | 0.490626 | 0.310199 | 0.822549 |
| own_4 | 0.498116 | 0.322224 | 0.779412 |
| integrated_prior_4 | 0.611063 | 0.418632 | 0.798039 |
| item_frequency_4 | 0.380143 | 0.244724 | 0.823529 |
| empirical_reference_4 | 0.477467 | 0.298344 | 0.823529 |
| legacy_population_4 | 0.562996 | 0.373514 | 0.798039 |
| historical_summary_4 | 0.512305 | 0.329205 | 0.813725 |
| donor_mixture_4 | 0.482206 | 0.303907 | 0.824510 |
| own_8 | 0.451720 | 0.289322 | 0.808824 |
| integrated_prior_8 | 0.611063 | 0.418632 | 0.798039 |
| item_frequency_8 | 0.380143 | 0.244724 | 0.823529 |
| empirical_reference_8 | 0.434644 | 0.268124 | 0.823529 |
| legacy_population_8 | 0.562996 | 0.373514 | 0.798039 |
| historical_summary_8 | 0.516637 | 0.333004 | 0.807843 |
| donor_mixture_8 | 0.444147 | 0.276881 | 0.823529 |
| historical_own_0 | 0.562996 | 0.373514 | 0.798039 |

All other declared baseline-minus-own contrasts, all four development budgets and ten-bin calibration counts/probabilities/outcome rates for every predictor are retained in `exploratory_results.json` and `development_results.json`; no unreported endpoint was dropped. Accuracy uses positive option at p>=.5. Brier sums both alternatives, so it is twice the single-positive-option squared error. These metrics do not count ten schedule rows as independent task families.

## Feature rank and penalty audit

Source design rank4; target rank3. For each seed17/29/43, source×B rank4 and target×B rank3, with selected latent dimension8. Isotropic prior rotations B→BQ and z→Qᵀz preserve predictions, so latent axes are not named psychological traits. The source likelihood has at most four informed directions; the prior supplies remaining curvature. Frobenius norms are4.725634,4.722325,4.724885. Original penalty λ||B||²/(2FK) has coefficients0.003125,0.0015625,0.00078125 for K=2/4/8 at λ=.1,F=8. Thus dimension search also changes effective Frobenius shrinkage. The prospective rank2 and dimension-independent penalty are a separately declared future definition, never retroactively fitted here.

Fixed source-later and target-risky second positions remain confounded with semantic preference. Representation permutation checks passed but cannot establish actual counterbalancing. No trait, causal mechanism, unseen-task or temporal claim follows.

## Joint precision illustration

Development paired SDs: 0.130301, 0.098073; correlation 0.607750.
Residuals are centered to imposed equal true advantages; observed development means are not treated as expected positive effects. Simulation preserves the two paired contrast axes, resampling people with200 outer samples and2,000 inner bootstrap draws, fixed seed20261125. Both lower endpoints must exceed0.

| Independent people | Joint success at0 | At.01 each | At.02 each | MC SE at.02 | Mean half-widths (value, identity) |
|---:|---:|---:|---:|---:|---|
| 100 | 0.010 | 0.105 | 0.345 | 0.034 | 0.02533, 0.01899 |
| 250 | 0.005 | 0.170 | 0.665 | 0.033 | 0.01593, 0.01206 |
| 500 | 0.010 | 0.315 | 0.915 | 0.020 | 0.01131, 0.00851 |
| 1000 | 0.010 | 0.630 | 1.000 | 0.000 | 0.00800, 0.00600 |
| 2000 | 0.000 | 0.930 | 1.000 | 0.000 | 0.00569, 0.00427 |

Under this conditional approximation500 people give91.5% simulated joint success at.02 each (Monte Carlo SE1.97 percentage points). This is not an enrollment recommendation. Reported binomial SE=0 at simulated0%/100% does not mean certainty; future size selection uses a Wilson lower bound, avoiding that degeneracy. Cross-fold bank dependence, fitted-model uncertainty, counterbalancing and new-cohort variance are not captured. The future rule requires new-development residuals, the newly selected comparator and matching-layout donors, with actual candidate n100/252/500/1000/2000 and a frozen numeric n before confirmation enrollment. See `REPLICATION_PROTOCOL.md`; no human observations are created by this simulation.
