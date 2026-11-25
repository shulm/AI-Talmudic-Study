# Next agent: evidence-dependent personalization with mixed populations

## Assignment

Continue `shulm/AI-Talmudic-Study` through issue #2. Read root `AGENTS.md` and `AGENT_HANDOFF.md`, then this directory's `REVIEW.md`, `METHOD_NOTE.md`, and `next_evidence_shrinkage_design.json`. Read PR #15's completed results/protocol/handoff at `ee2b0a5a2f0916fed3dd59f720b902eb332eecc3`.

Retain `VERIFIED_COMPLETE / COMPLETED_PRIMARY_FAILURE`: k=16 interaction recovery is strong, primary null loss fails C/D, secondary D also fails, and D's k=96 anchor fails. These outcomes are exposed. The .06/.6 policy is an exposed starting configuration fixed for this new experiment, not a retrospectively qualified replacement.

Execute one new synthetic-only experiment, **`evidence_shrinkage_v1`**. Question: can a fixed evidence-dependent probability mixture preserve useful personal interaction while limiting inactive-person harm when the same shared basis serves both types of people?

Create a continuation branch from the reviewed assignment head after recording its SHA. Put new code under `labs/decision_functions_evidence_shrinkage_v1/` and public artifacts under `research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/`. Use a fresh private artifact directory. Preserve every historical laboratory/run file. Consult current SRO and corpus coordination, including PRs #5/#8/#14/#16, without duplicating their work. No merge, human evaluation, encoder acquisition, corpus expansion, paid call or external person-directed communication is assigned.

## Coordination with parallel PR #18

A separate null-control planning package appeared during this review: PR #18 at `49d7157e3998a20f646e9200c3e223bbbb58541f`. Read its current handoff for coordination. It studies a globally selected penalty/blend policy over development and confirmation worlds; its mixed condition is descriptive. This assignment tests one history-dependent method with mixed populations as primary. The reserved seeds are disjoint, and PR #18 reports no fresh scientific execution. Preserve its separate authorization boundary: do not run its CLI, consume its seed banks, alter its branch or add its sweep to this assignment. This prompt neither cancels nor supersedes that proposal. Check issue #2/current heads before the new pre-fit checkpoint; keep the numerical design and seeds below unchanged.

## G0. Prove, implement and freeze before fitting

Implement the single continuous rule in `METHOD_NOTE.md`; do not add a hard-gate arm, penalty grid, learned selector or alternate prior. Write the conditional-count derivation and null-loss proof into the run's method record. Have an independent review check that the code implements that argument before the first optimizer call.

Keep float64 and the existing L-BFGS-B settings: maxiter=1000, ftol=1e-12, gtol=1e-8, maxls=50. Shared training uses rho=.01, lambda_b=.1, rank two, three classes and seeds 11/29/47. All personal M1 adaptation uses rho=.06 and lambda_b=.6; B3 uses lambda_b=.6. There is no policy selection.

Retain exact protocol-derived completeness states and conjunctions. Add a zero-optimization forward-consistency check: bind shared V/U/b archives to their full optimizer-vector slices; reconstruct existing-condition B3/M1 query probabilities from saved parameters and query inputs; reconstruct ensembles, evidence, weights, mixtures and donor permutations. Replaying an existing condition is not refitting. Do not assert a private-cache replay unless its bytes were actually available.

Before fitting, run deterministic small-case checks requiring no optimizer or scientific fixture materialization:

- Objective/gradient equivalence to the frozen head and full-vector extraction.
- Scalar and vectorized conditional DP versus exhaustive enumeration, for every count vector in at least k=0,1,3,6 toy cases.
- Conditional normalization, arbitrary-offset cancellation, and conditional null mean evidence=1.
- All-one-class, zero-feature and all-zero-prior evidence identities.
- Simultaneous latent-coordinate transformation of each seed's U/V; class/question permutation invariance.
- Arithmetic seed averaging and prior-weight normalization; no maximum-seed selection.
- Mixture normalization, 0<=w<=.9, B3 fallback for E<=1, and per-answer clipped-log-loss inequality.
- Empty/missing/duplicate/corrupt evidence, wrong parameter slice, wrong prediction, wrong evidence/weight, and inconsistent qualification must fail verification.

Freeze a short deterministic test-fixture specification and its hashes. Require absolute log-partition/normalization/evidence-identity differences <=1e-10; probability/weight and pointwise loss-bound checks <=1e-12. Report every check. Engineering fixes before scientific execution are allowed, with failed test receipts and resources preserved; publish a new final pre-fit SHA after fixes. Once scientific fitting starts, do not change the scientific code or replace failed scientific attempts.

Commit/push the full scientific code, protocol, seeds, source/environment hashes, exact expected stages/arrays/rows/records and test receipts. Post/read back the pre-fit SHA in issue #2 before any shared or personal fit. Then execute the bounded study without another routine confirmation.

## G1. Four fresh mixed-population realizations

Use these fixed seeds:

| ID | Generator | Labels | Activity mask |
| --- | ---: | ---: | ---: |
| E | 20261201 | 2801 | 2901 |
| F | 20261202 | 2802 | 2902 |
| G | 20261203 | 2803 | 2903 |
| H | 20261204 | 2804 | 2904 |

Extend only the person count and activity mask of the rotational family. Keep 192 questions/64 three-case groups, group partitions 40/12/12, z dimension two, shared-logit scale .25, interaction matrices of scale 2.5, and centered offset standard deviation .12. Use 192 people with partitions 96 training, 48 reserved, 48 held out. Preserve adjacent pairs with identical offsets and opposite unit-vector phases.

Generator draw order: use NumPy Generator(PCG64(generator_seed)) to draw 64 question angles, the 64-group permutation, 96 pair phases, then 96 three-class offset vectors. Construct the existing z/base/V formulas, adjacent opposite phases, repeated centered offsets, and original first-32-training-group support pool. The changed number of person draws is intentional and must be documented.

For activity, initialize a separate Generator(PCG64(mask_seed)). In order, permute global pair IDs for train [0,48), reserved [48,72), held out [72,96); mark the first half of each permutation active. Both members of a pair have the same status. Thus training contains 48 active/48 inactive people, and held out contains 24/24. Set effective interaction u_s to zero for inactive people and preserve it for active people. Draw one mixed response array using Generator(PCG64(label_seed)) and the same categorical sampling rule as v2. Do not generate separate globally positive/null training regimes.

The middle people and question partitions remain unused. Fit three shared heads per realization on its own 96 training people and 120 training cases, using all mixed labels without activity flags. Retain full fitted V/U/b. Activity flags and planted parameters belong only to the generator/evaluator view. The prediction/evidence code must not branch on them. Save predictions/evidence before evaluator labels/oracles/status are loaded for scoring.

### Two fixed 16-observation histories

Use support seeds 101 and 211. Reuse the previous group-block construction with namespace `evidence_shrinkage_v1`: SHA-256 sort the original 32 support group IDs using `evidence_shrinkage_v1|<ID>|<seed>|group|<group_id>`, and choose cyclic starting phase from the full integer digest of `evidence_shrinkage_v1|<ID>|<seed>|phase|<group_id>` modulo 3. Serialize uppercase ID and decimal integers without leading zeros, spaces or trailing newline. Break digest ties by integer group ID.

Take exactly the first 16 cases: five complete triplets plus one case. Require Gram eigenvalues (.46875,.53125) within 1e-12. Save exact orders, IDs, labels and hashes. All people/methods use the same cases at a given schedule. No angle/outcome/evidence-based history selection. No additional k curve is assigned.

## G2. Conditional evidence and the sole new primary predictor

For each shared seed j, use all 96 fitted training-person vectors to form exactly 192 equal-weight atoms: +u_jt and -u_jt, weight 1/192. No filtering by norm or true activity, no additional atom, no fitted scale, and no target/reserved-person data. Keep each prior paired with its own V_j; never average latent coordinates across seeds.

For each history's question set, compute exact conditional normalizers in log space for these 192 atoms plus the null u=0. The DP sums ordered label assignments with a specified count vector; do not add an extra multinomial coefficient. Compute all 153 final three-class count compositions simultaneously and share the table across people. Do not apply the 1e-12 scoring floor inside evidence calculations.

Using each person's observed counts and sufficient sum, compute the prior-averaged likelihood ratio E_j=integral Q_u/Q_0. Q_0 uses known shared logits and conditioned counts, not fitted B3 probabilities. Compute E=(E_11+E_29+E_47)/3 with log-sum-exp. Never take the maximum or pool evidence across the two histories.

Fit B3 and three M1 personal heads on the same history. M1 is their probability ensemble. B1 uses four pseudo-observations toward the mixed training-label prior; B2 uses the known shared logits.

Compare six named aggregate predictors:

- B1, B2 and B3.
- M1, the three-seed probability ensemble.
- FIXED_MIX=.1*B3+.9*M1.
- ES, the sole primary method: h=min(.009*max(E-1,0),log(10)), w=1-exp(-h), ES=(1-w)*B3+w*M1.

Use the stable log-E/expm1 construction in METHOD_NOTE. The epsilon=.009 budget and .9 weight cap are fixed; no threshold/scale selection is allowed. The same w applies to all queries for one person/history. It is a prediction weight, not a posterior probability of activity. Save the three seed evidences, averaged evidence, h/w, counts, prior atoms/weights, DP count ordering/normalizers, adapted parameters, raw probabilities and provenance.

Do not clip/renormalize probability arrays. Apply max(p,1e-12) only inside log-loss scoring. Independently verify ES>=exp(-h)*B3 and the corresponding clipped-loss inequality for every saved person/query/class, within 1e-12.

Construct single matched-other controls by the local held-out row mapping pi(s)=s xor 1, permuting existing same-history predictions for all six aggregate methods. Score donor predictions against recipient targets. No donor fits or donor mixtures. Null expected pair-averaged donor contrast remains a structural zero.

## G3. Gates, diagnostics and numerical checks

Use evaluator status only to form active and inactive scoring subsets, retaining whole pairs. Apply the original four empirical point gates to ES separately in E/F/G/H:

- Active expected-NLL gain over B3 >=.05.
- Active oracle-gap recovery >=.50.
- Active contrast NRMSE <=.50.
- Inactive expected-NLL degradation relative to B3 <=.01.

Average losses/squared contrast errors across the two histories, not probabilities. Recovery is averaged gain divided by averaged B3 excess over oracle. Contrast uses adjacent matched-person differences in the three class log-odds, then subtracts the first canonical query value, on the active subset only. Require finite metrics and positive denominators. Use unrounded values. Report each history, aggregate, worst-history margins and each comparator's descriptive gates. No comparator, pooled realization or theoretical expectation bound rescues primary failure.

Report expected/realized NLL, accuracy, Brier, donor contrasts, inactive contrast RMS, per-seed results, and per-person excess loss. For active/inactive evidence and weights report all saved values and fixed summaries (min, median, mean, max, quantiles .1/.9, fraction w=0, fraction at cap), plus disagreement across histories. Also report inactive mean positive-part excess loss; it is descriptive, not an extra pass rule. Do not diagnose a unique mechanism from these summaries.

The theorem bounds expected inactive excess over possible support responses under the stated known-base model. It does not force an observed cohort mean below .009 or .01. State that distinction in the report; exact theory and numerical implementation checks are separate.

Use 2,000 conditional paired bootstrap resamples for ES active gain, ES inactive degradation, ES positive donor contrast, and ES-versus-FIXED_MIX expected loss (L_ES minus L_FIXED_MIX, negative favors ES) separately within each activity stratum. Preserve 12 whole person pairs and 12 whole query groups in each stratum. Index each active/inactive pair list in ascending original global pair-ID order; index query groups by their first appearance in the canonical fixture test split, preserving its three-case order. Average history cell losses first. Per realization, reset PCG64(1702); draw (2000,12) active-pair indices, then (2000,12) inactive-pair indices, then (2000,12) query-group indices, all uniform integers 0..11. Use the same resample indices for paired model contrasts, and 95% percentile intervals with linear interpolation. Save indices/replicates. Do not pool realizations or treat seeds/histories as new independent people. Intervals exclude retraining uncertainty and do not change gates.

Numerical checks use schedule 101: each B3/M1 seed is adapted on the first 1 and first 7 held-out people and compared with the existing 48-person batch for the same first person. Require maximum probability difference<=1e-6 and first-person expected-NLL difference<=1e-5. Also reconstruct the ensemble/FIXED_MIX/ES at these batch sizes with the same evidence weights, without extra optimization. Preserve tolerances after fitting.

## Exact execution and output contract

Per realization: shared stage 3 records; support stage 8 batches of 48 people; numerical stage 8 batches (four heads at sizes 1 and 7). The derived ensemble/mixture numerical predictions require no additional optimizer.

| Work across E/F/G/H | Shared fits | Adaptation batches | Person-solves |
| --- | ---: | ---: | ---: |
| Shared mixed heads | 12 | 0 | 0 |
| Two histories, B3 plus three M1 seeds | 0 | 32 | 1,536 |
| Numerical 1/7-person checks | 0 | 32 | 128 |
| Total | 12 | 64 | 1,664 |

Total 76 optimizer records, 12 exact stage ledgers. For each realization save 30 primary prediction arrays: 2 histories times (9 own arrays + 6 donor arrays). The nine own arrays are six aggregate methods plus three M1 seed heads. Save 14 numerical arrays: at each of sizes 1/7, four fitted heads plus the three derived M1/FIXED_MIX/ES predictors. Thus 176 query-prediction arrays across four realizations; evaluator oracles are separately identified inputs.

Freeze nine private archive roles per realization: fixture, learner, support, evaluator, models, predictions, numerical, evidence, bootstrap. Full optimizer vectors are separate immutable files. Derive and publish every archive key/shape, score/evidence row identity, and verification comparison count before fitting. Upper bounds alone cannot establish completion. No extra uninformative, zero-support, certificate or alternative-policy fits are assigned.

Limits: one CPU core-hour, 4 GiB sampled memory, exactly the declared complete-design fits/solves, zero paid calls/downloads/human evaluations. No scientific retries or replacement seeds. Retain failures and stop on engineering/resource invalidity with INCOMPLETE state. A scientific gate failure does not stop the remaining prescribed realizations; complete them unless execution becomes invalid. Unused budget does not authorize more work.

## G4. Verification, report and GitHub handoff

Carry forward complete-run verification and add independently implemented forward/evidence/mixture replay. Bind V/U/b to optimizer vectors, reconstruct existing probabilities, check actual priors/count lookups/DP recurrences/seed averaging/weights/donor permutations, replay metrics and bootstrap using a different aggregation expression, and enforce exact required evidence sets. Hash private artifacts before/after. New scientific results must not depend on post-run verifier changes.

Publish RESULTS.md, results_summary.json, PROTOCOL.json, exact stage/array contracts, model/support/evidence manifests, proof/preflight records, complete verification receipts, cumulative resources including failed pre-fit tests, and NEXT_HANDOFF.md in a draft PR. Link exact pre-fit/final SHAs and findings in issue #2. Qualification requires complete valid evidence, numerical pass, forward/saved-evidence verification and all four ES gates separately on all four realizations. Use separate complete-failure and incomplete statuses.

Update the proposal-only text specification with the known-g, fixed-label and response-independence assumptions. Arbitrary fixed text features do not themselves break the e-value identity, but an incorrect shared null predictor can. Explain which later representation/base-model experiment would be interpretable given the result. Do not choose/download an encoder or run a text/human study here.

Stop after the bounded report. Preserve every primary/control failure. Do not retune E/F/G/H, increase epsilon, replace the prior, add a hard gate, or use corpus work to relabel the result. Separate source-production agents may continue their already authorized tasks.
