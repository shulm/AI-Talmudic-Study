# Diagnostic protocol v1 — declared before new analyses

This is a post hoc explanatory follow-up to completed PR5, not independent confirmation. Preserve the original inconclusive verdict, signed files, predictions and exact contrasts. Original delivery `6ca2dedc547144d7279696bd5322c1e39c7f03d3`, freeze `430c0ec4e74db8c265e77e1eb028b21abe6bff43`. No old shared model is refitted or changed. All new outputs go in this follow-up directory; participant artifacts remain ignored locally. Diagnostic specification is hashed before execution. No people-directed messages, recruitment, paid APIs or new compute.

## Questions and fixed computations

1. Does shared prediction improve without recipient history? Compare training-only per-item frequencies (Beta(.5,.5), fixed), same frozen profile's integrated Normal(0,I) prior, same profile's empirical development-history mixture, and legacy population. A separate target-context fit is omitted because the ten known common items are completely covered by item frequencies; no varying-item extrapolation claim. No smoothing search or fitted calibration.
2. Distinguish identity replacement from probability averaging: average losses of five individual donor predictions versus loss of their probability mixture. Each donor prediction first averages the same three optimization seeds as own predictions. Retain both contrasts and their Jensen gap.
3. Compute coherent 0/2/4/8 same-profile curves: integrated prior at zero; frozen posterior predictions at positive budgets. Preserve historical logistic-fallback zero separately. Empirical reference curves at positive budgets use exactly that budget's source choices; at zero every reference is the same prior.
4. Break whole-history pairing **only at inference**, on original validation people at k=8. No retraining. Five deterministic within-fold cyclic permutations, shifts1,5,11,17,23 on fixed hash ordering, move complete eight-answer histories together, while target recipient stays fixed. Score each permutation then average participant losses. Do not score a probability mixture for this pairing diagnostic. No old-test pairing analysis.
5. Audit numerical source/target feature rank and each frozen basis's source/target rank; analytically document latent rotation nonidentifiability and mean-square penalty scaling. No new dimension search. Report calibration with fixed ten probability bins and full-vector Brier/accuracy/NLL.

## People, banks and access

Retain 304 original training,102 validation,102 exposed old-test people, one target schedule family of ten choices and fixed eight source probes with nested0/2/4 prefixes. No extra exclusions. Training labels are used only for fixed item frequency estimates. New source-blind functions never take recipient source responses.

Partition validation people into two51-person folds by sorted SHA256(`20261124|diagnostic_fold|person`) alternating assignment. For each fold, the opposite fold is a **fixed disjoint51-person reference/donor bank**. Shared models remain their original training-only fit; there is no fold-level refitting. Validation participated in original model selection, so these diagnostics are development descriptions, not unbiased generalization estimates. Banks are uniform; never use target responses or recipient source answers to choose bank members or weights.

Use all102 validation people as the fixed source-only bank for the old test. It is disjoint from test recipients. Infer each bank member's MAP/Laplace state from the permitted source budget afresh for this analysis, never from a saved target-fitted vector. Cache those source-only posterior predictions within this run to avoid redundant solves. With common target scenarios, the reference mixture is exactly identical across recipients in that fold/test; this invariant is tested.

Development five-donor assignments use SHA256(`20261124|diagnostic_donor|assignment|person`) modulo the sorted opposite-fold bank, advancing duplicates to the next index. For the exposed test, use the original saved five assignment arrays and membership without regeneration. Seeds/donors/permutations are not people.

## Development choice and exposed-test reuse

Select the source-blind comparator by lowest pooled participant-average cross-fold validation NLL at k=8 from item frequency, prior, empirical mixture and legacy population. Ties within1e-12 follow that listed order. This selects a diagnostic comparator, not a newly confirmed algorithm. Freeze its identity and exact development probabilities before old-test label access. No selection using old-test scores.

Perform one declared exploratory old-test pass covering all four budgets and models above, own coherent curve, saved donor replacement, saved donor mixture, historical source summary, and Jensen gap. At zero saved donors use the historical fallback; report their historical identity/mixture comparisons versus historical own, separately from coherent-prior curves. At positive budgets both own and saved donor predictions use the frozen profile.

Save new old-test probabilities and their hashes before joining the already exposed test outcomes. Original prediction arrays are reused for own positive-budget, legacy, summary and donors. No re-running original scorer, overwriting outputs, retraining, test-based calibration, or changing diagnostic endpoints after scores. Any correction is recorded and the old test stays exposed.

## Contrasts and intervals

Δvalue=L(validation-selected source-blind)−L(coherent own); Δidentity=mean_d L(single donor_d)−L(own); Δmixture=L(mean_d probabilities)−L(own). Jensen gap=mean_d L(donor_d)−L(mean_d probabilities)≥0. All are full-alternative NLL in nats. Average ten trials within each person/family, then people equally. Bootstrap two-sided95% percentile intervals,2,000 paired participant draws, seed20261124; donor banks and prediction arrays fixed. For validation cross-fold inference, intervals are descriptive conditional summaries: donor-recipient dependencies across folds are not modeled and no confirmatory coverage claim is made. The old-test bank is fully disjoint and fixed, so usual conditional paired-person intervals apply, still post hoc and exploratory.

No multiplicity-adjusted scientific claim; all declared effects are reported. Neither positive post hoc intervals nor null effects alter PR5's original verdict. A positive identity contrast without positive value against the stronger source-blind comparator is at most fitted-history sensitivity, not demonstrated useful personalization. Intervals crossing zero do not establish equivalence.

## Checks, smoke and resources

Before analysis verify original files against freeze, split and probability manifests and Git identities, including saved weights. Read-only original access; no data downloads needed for diagnostics. Synthetic tests check Jensen averaging order, recipient-independent source-blind predictions, donor disjointness, option permutations, budgets, probability validity and participant-level weighting. Do not present synthetic outputs as humans.

Small smoke: frozen-model prior and source adaptation on first eight validation people, timed process CPU, forecast bounded full inference. No parameter fitting is planned; fixed item counts are closed-form estimates. Stop further compute if conservative aggregate forecast exceeds14,400 process CPU seconds. Additional archival research stays below2GiB; no MRI. Exact environment, measurements, hashes, failures and stage events retained. Independent AI methods review precedes exposed-test diagnostic execution. This is not human expert review or new confirmation.
