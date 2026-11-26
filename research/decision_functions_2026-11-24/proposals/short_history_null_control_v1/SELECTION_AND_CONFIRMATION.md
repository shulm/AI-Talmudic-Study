# Selection and independent confirmation

## Finite development

Before fitting, bind code/specification hashes, exact twelve development seed pairs and the reserved96 confirmation pairs. No development/confirmation seed replacement or extra candidate is allowed. The candidate list has20 rows but18 unique predictor settings: at w=0 each pair of rho values with the same offset penalty duplicates B3.

Select common B3 first by lowest mean oracle expected query NLL over12 worlds and population/offset/strong equally. Average cases within people,people equally,then two schedules equally. Ties within1e-12 favor lambda=.1. This is one global comparator, frozen separately from the matching B3 used inside each blend. Weak/stress outputs do not select it.

A candidate is eligible only if w>0; both development null upper bounds<=.01; strong mean common-B3 gain>=.05, gain lower bound>0, recovery>=.50 and contrast NRMSE<=.50. Recovery is ratio of average gain to average common-B3 excess over oracle. NRMSE is square root of average squared contrast error divided by average squared oracle contrast. Recompute from blended probabilities using all paired class log-odds differences relative to the first canonical query.

Select greatest strong gain. Within1e-12 of maximum, choose lower w,then larger rho,then larger lambda,then lexical ID. There is no per-person or regime-dependent choice. Twenty development comparisons are selection heuristics, not familywise confirmatory evidence. Independent confirmation removes the need to pretend these selected development intervals have their nominal coverage.

If no candidate is eligible, DEV_NO_CANDIDATE is a complete declared stop, qualification=false. Required evidence: all12 worlds×6 regimes, exact dev ledgers, manifests/arrays and resource receipts, complete score and20-row selection table, source freeze and replay. Empty or partial development cannot produce that stop.

## Confirmation count and bounds

For the selected candidate compute development SD across worlds for each of two candidate-minus-common-B3 null harms and strong common-B3-minus-candidate gain. Let s_max be their maximum. Choose the smallest integer n from24 through96 satisfying t_(1-.05/3,n-1)*s_max/sqrt(n)<=.005. No solution gives DEV_INSUFFICIENT_PRECISION, complete declared stop, never success. Zero variance, nonfinite inputs or undefined primary ratios cannot qualify; retain explicit unresolved/error state. No favorable replacement seed is allowed.

Freeze the exact selected policy, common B3, n, prefix of confirmation bank, expected IDs and source hashes before any confirmation generation. The orchestrator binds these to selection_freeze.json. Confirmation never tunes or refits a policy on query outcomes; each world regenerates shared training and new support under the same algorithm.

For each endpoint, mean +/- t_(1-.05/3,n-1)*sampleSD/sqrt(n), ddof=1, supplies the needed one-sided bound. Three one-sided endpoints share family alpha=.05 by Bonferroni: two null upper bounds and one strong-gain lower bound. Independence between these endpoints is unnecessary; independence of worlds is essential. Optimization seeds, people and schedules are not independent world replicates.

Student-t is exact for independent normal world contrasts; our nonlinear generated-world contrasts are not proven normal. Here it is an explicitly approximate Monte Carlo procedure, relying on averages over many people/cases and24+ independent worlds. Bounded clipped losses give finite moments but do not establish finite-sample normality. We do not claim distribution-free95% coverage. Report all world values and tail summaries; no normality-test-based method switch is allowed. The planning SD is selected and uncertain; it is a planning estimate, not a power guarantee. Actual confirmation half-widths must also be<=.005; otherwise COMPLETE_INSUFFICIENT_PRECISION without adding worlds.

The t interval mechanics and Bonferroni rationale follow [NIST confidence limits](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) and [NIST Bonferroni method](https://itl.nist.gov/div898/handbook/prc/section4/prc473.htm). Their assumptions do not prove normality of this simulation's endpoints.

## Prospective success and continuity

New-study success requires exact complete evidence and saved-component replay, successful finite optimizers with personal scaled residual<=1e-4, both null upper bounds<=.01, strong gain lower bound>0, all three half-widths<=.005, w>0, strong point gain>=.05,recovery>=.50,NRMSE<=.50. No secondary rescue or null averaging is permitted. A failed gate with complete evidence is a completed failure, not incomplete engineering.

The historical four point thresholds are also tabulated per world using the blend's matching-offset B3, separately from new common-B3 gates. Changing comparator changes the estimand; only threshold values carry directly into the new primary test. Exposed C/D remain separately unchanged.

Probability log floor1e-12. Primary denominator floor1e-8; at/below it the ratio is undefined and cannot pass. Nonfinite probabilities, wrong identities, missing/duplicate records, changed files or unsuccessful optimizers cause INCOMPLETE, never qualification. Zero observed endpoint variance is unresolved rather than a claim of zero uncertainty.

Always report candidate/common-B3 losses relative to the known shared-base control, realized NLL,accuracy,Brier,oracle expected NLL,paired-antiphase donor contrasts, each schedule,person harms and world distribution. Harm fractions are descriptive with clustered dependence. Expected-risk success across worlds is not a maximum-harm guarantee. No source-blind noninferiority claim is made.
