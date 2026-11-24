# Independent AI protocol review

Reviewer: methods_review agent, 2026-11-24. This is an independent AI review, not expert-human validation. Status: **CONDITIONAL — DO NOT UNLOCK FINAL TARGETS YET**. The model/evaluator implementation, selected configurations, smoke resource evidence and frozen hashes remain to be reviewed. This record preserves initial findings rather than overwriting disagreements.

## Inspected boundaries

Read PROTOCOL.md, DATA_ADMISSION.md, data_pipeline.py, pinned Kirby JavaScript and Holt–Laury TSV. Inspected only scenario/family aggregates from the learner artifacts; no evaluator labels or raw participant target answers were opened. Cross-Psych exclusion is justified by the independently established 601-versus-591 opt-out mismatch, absent release license, and unresolved canonical decision identity. SRO choice semantics and nonadaptive scenario construction agree with the inspected definitions. Source selection by fixed item hash is appropriate for this retrospective static regime; it is not chronological forecasting or live querying.

The person split, common target cohort, fixed donor pool, own-versus-other estimands, complete-choice NLL, participant bootstrap, zero provisional threshold and separate source-summary comparison are well specified. Holding the validation donor pool fixed produces conditional uncertainty as explicitly stated. The rule called simpler model sufficient is correctly qualified as lack of demonstrated profile advantage, not equivalence.

## Findings requiring closure before freeze

1. **Monetary feature arithmetic.** Holt–Laury code uses `(195*p-75)/100`. The pinned options imply risky expected value `190*p+5*(1-p)` and safe value `100*p+80*(1-p)`, so the difference is `165*p-75`. Correct this if the feature is intended as expected-value difference. Though both formulas lie in the span of an intercept and p, the scaling affects penalized fits and must not be changed after test evaluation.
2. **Fail-fast correspondence checks.** Current parser checks chosen-response text and only the first target probability. It should verify every lottery's complete monetary outcomes/probabilities against pinned TSV and each Kirby amount/delay tuple against pinned JavaScript. Count-only eligibility should additionally assert one observation per expected source family and target question. Independent scenario-only aggregate inspection found all 508 admitted people have 27 distinct source families and ten distinct target probabilities, with exactly one shared source set and one shared target set. This supports current data but needs executable enforcement.
3. **Data contract missing at review time.** DATA_CONTRACT.json must be present before freeze. Clarify that `predecessor_dependencies=[]` means no task-program transition dependency in the static representation, not proven psychological independence. Holt–Laury click order is unavailable, and its ten simultaneous items remain one family.
4. **Training/access details pending.** Actual training budgets, latent inference/uncertainty approximation, stopping rules, tuning values, synthetic checks and evaluator label gate must be checked against final code/configuration. A prose promise cannot certify the learner/evaluator boundary. Do not approve final scoring on this partial review alone.

## Required qualifications, not automatic blockers

The pinned task-definition revisions postdate collection, so exact historical deployment remains unverified. All current raw alternatives must correspond, and reports must retain that limitation. The source first practice trial is excluded, while unmeasured carryover from earlier items cannot be ruled out. Target response consistency must not become a post hoc exclusion.

Kirby's later option is always right/second and Holt–Laury's riskier option is always second. Canonical semantic recoding prevents an implementation position bug but cannot experimentally separate a stable second-option response tendency from monetary preference. Retain the simple source-response baseline and qualify any positive result as predictive individual information, potentially including response-style effects. Do not describe the profile as an isolated psychological trait.

The eight features occupy task-specific blocks; shared latent covariance can express transfer, but learned dimensions need not be unique or interpretable. With four active feature coordinates per task and an affine-redundant target coordinate, latent dimension eight does not establish eight distinguishable psychological factors.

Raw input and canonical files necessarily contain labels for extraction; the operational boundary is which files/fields fitting and prediction read. Hashing labels is allowed for artifact integrity and does not constitute outcome inspection, but test labels must not influence feature selection, fitting or calibration. Final model/evaluator review is outstanding.

## Second review: implementation before development grid

Reviewed models.py, run_lab.py, test_models.py, DATA_CONTRACT.json and updated parser. The expected-value arithmetic is corrected and complete target option numerical values are checked. Per-person common source-set and target-probability checks were added; the schema now exists. Kirby's global source set should additionally be checked against the pinned JavaScript arrays rather than only against itself.

Model equations match the intended shared basis/Gaussian prior. Source MAP inference does not accept target labels; covariance is inverse source posterior Hessian, with 20-node Gauss–Hermite predictive integration. Shared training uses target episode loss from training people and the same approximation; its five damped Newton steps versus converged prediction optimization are a disclosed approximation. Probability ensembles precede scoring. Donors receive matching probes and fresh inference; averaging their distributions before scoring matches the frozen estimand. Complete-choice NLL, two-class Brier, fixed calibration bins, participant-mean losses and paired percentile bootstrap are implemented consistently. Synthetic tests distinguish engineering evidence from human data and exercise option reversal and own-versus-donor intervention.

**Open implementation blockers sent to root:** development `load(..., labels=True)` currently iterates the shared evaluator-label JSONL and parses test rows before filtering. Although the filtered labels do not enter fitting, this violates the stronger stated test-file access boundary. Physically partition label files, read only development files in fitting, and reserve the test file for scoring. `validate_data` performs mechanical label-validity checks on canonical evidence; document this as extraction validation, not model access or outcome inspection. `freeze` must compare signed review hashes rather than accept any stale `approved:true`. Cumulative resource accounting must include previous smoke/synthetic fits and enforce the pre-fit forecast, not merely check elapsed CPU after each fit.

No test target responses were opened by this reviewer. Final approval remains pending fixes, selected configuration, validation/synthetic evidence, resource forecast and final signed hashes.

## Third review: blockers closed before final prediction

Verified physical train/validation/test evaluator files, signed-file hash validation in freeze(), prior resource bound plus refined forecast gate, and explicit Kirby tuple comparison with the pinned JavaScript arrays. Independent guarded-loader execution prohibited canonical evidence, shared evaluator labels and test evaluator labels: train loaded 304 people, validation 102, and test prediction inputs 102 with no target labels. Explicit `load('test', True)` raised as required. This test performed no fitting and opened no test target-label file.

Reviewed passing data_validation.json and synthetic_controls.json (18 process CPU seconds for the root synthetic run). No-transfer intervals encompass zero; transfer control recovers signal. These tests do not establish human transfer. The initial resource forecast exceeded the cap, and its record remains; a full-cohort, dimension-eight, ten-epoch smoke replaced its poor small-sample extrapolation without using model scores to change the study. The refined 1,861.875-second grid forecast plus conservative 180-second prior bound is below the 14,400-second cap.

Extraction/schema validation mechanically reads canonical observed labels to verify validity and matching; this is separate from learner fitting and final scoring, and it is not an outcome-driven design audit. Same-page dependencies and fixed-position confounding remain interpretation qualifications, not resolved causal claims.

All implementation blockers in prior sections are closed. Final hash-bound approval will be emitted separately after checking selected configurations against the completed development grid; the initial findings above are intentionally retained.

## Final pre-test approval

The complete development grid contains eleven configurations (including six profile dimension/regularization combinations, each an ensemble of three declared seeds). Independently recomputed each selected configuration using the declared validation-NLL and tie-breaking rule; selections match. Selected profile: dimension 8, regularization 0.1, population regularization 0.1. All four comparator configurations and fitted-artifact hashes are fixed. Development process CPU was 115.046875 seconds; the conservative prior bound plus development is 295.046875 seconds, well below the cap. Final prediction and result files were absent when approval was written.

**APPROVED for the declared one-time final prediction and scoring after freeze/commit.** `review_signoff.json` binds this approval to exact reviewed file hashes. This approval certifies the reviewed protocol/implementation boundaries to the extent of an independent AI code review, not absence of every possible defect, human-subject generalizability, or a positive outcome. Earlier findings and their resolutions remain in this file. No test target responses were inspected by this reviewer.

## Pre-freeze boundary tightening, same review cycle

After initial signoff, the extractor limited the learner source file to the fixed eight revealed probes per person (`sr[:8]`), retaining all 27 only in evaluator/raw evidence. Reviewed this one-line change and verified 508 people each have exactly eight source-file rows, whose ID union exactly equals the budget-eight episode supports. Every lower-budget support is included. The loader already selected those same eight IDs, so this changes physical exposure without changing the model input selection or requiring refitting. Only data_pipeline.py and split_manifest.json differed among previously signed files. Refreshed the approval hashes before any final predictions/results existed. No target labels were opened.
