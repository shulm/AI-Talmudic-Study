# Independent AI methods review

Status: approved for the single declared exploratory old-test pass, conditional on exact reviewed hashes and all runtime guards. Reviewer is the independently delegated `model_engine` AI agent, not a human methods expert. This reviewer helped implement the original pilot models, so independence here means a separate review of the follow-up implementation and boundaries, not independence from the original research team.

The reviewer read the user's follow-up assignment, `DIAGNOSTIC_PROTOCOL.md`, `contrast_definitions.json`, and original `run_lab.py` loading/fitting/freezing logic. No human labels, fitted outputs, or diagnostic outcomes were loaded; no fit or numerical diagnostic was run. Original PR5 artifacts were not modified.

## Protocol assessment

The declared analysis addresses the requested distinctions without replacing the original inconclusive result. Identity uses seed-averaged probabilities for each donor, then averages donor losses. Mixture averages those donor probabilities before loss. This preserves the Jensen comparison and avoids treating seeds or donors as people. The same-profile curve uses the integrated latent prior at zero, while historical fallback-zero donor comparisons remain separate.

Validation recipients have disjoint opposite-fold reference banks. The exposed test uses a fixed validation-only bank. Neither membership nor weights depend on recipient responses or donor target labels. The entire source history is moved in the validation-only pairing diagnostic, with recipient target identity fixed. This is an inference pairing test, not a retraining test or a simple renaming of identities.

The four source-blind candidates and alpha=.5 item smoothing are fixed. Selection uses pooled cross-fold validation loss at budget eight, with a declared tie rule. Because the original model was already selected on these people, development intervals are explicitly descriptive. The selected identity and probabilities must be frozen before exploratory old-test scoring. No positive post hoc finding can become independent confirmation.

Analytic rank claims are correct: four active source coordinates bound source-likelihood rank by four, and the target's affine final coordinate limits target design rank to three. Latent rotations are observationally interchangeable under the isotropic prior. The original penalty is `lambda * ||B||_F^2 / (2*F*d)`; fixed lambda therefore changes its Frobenius coefficient when d changes. A future normalization change must be a separately declared model, never an alteration of the reproduced pilot.

## Requirements to verify in executable review

1. Original fitted weights, split artifacts, and assignment-level probability arrays must be checked against pinned provenance. Verify donor axes and whether seed averaging already occurred; do not average losses over optimization seeds on only one side. Match original recipient ordering and target IDs explicitly.
2. Source-blind probability constructors must not accept or consult recipient source answers. Reference-bank construction must assert bank/recipient disjointness and common scenario/probe ordering. Each positive-budget donor state must be inferred from precisely that budget's source labels.
3. Prior-zero prediction must bypass the original `ProfileModel.predict` fallback and integrate `z~N(0,I)` using the same frozen basis and quadrature. Historical zero and coherent zero need separate arrays/labels.
4. Save all declared predictions and hashes before the old-test evaluator-label join. Freeze baseline identity, code/protocol/config hashes, bank memberships and prediction hashes. The scorer must reject stale review/protocol or repeated completed execution and disclose any failed/corrected run.
5. Score complete binary alternatives, average ten schedule rows within each participant, and bootstrap paired participant differences with the fixed bank held fixed. Donor-loss and mixture-loss arrays must remain separate. Validate finite normalized probabilities and exact clipping/averaging order.
6. The five cyclic history permutations must be nonself permutations of all validation recipients within each fold and move complete histories with their design metadata. They must not leak target outcomes into assignment. No old-test pairing diagnostic is authorized by this protocol.
7. Report the validation reference-bank size (51) and old-test reference-bank size (102). They are deliberately different specified empirical predictors; their bank size change must not be described as an identical numerical baseline evaluated twice.

No blocking protocol-level issue was found. Final approval depends on checking these requirements against the implementation and frozen artifacts. All statements here concern the prespecified exploratory follow-up; archival confirmation admission remains a separate gate.

## Executable review, first pass

Read `diagnostics.py` and `test_diagnostics.py`. The donor and mixture calculations use the intended averaging order; original `run_lab.py` confirms saved assignment arrays already average the three optimization seeds, while the donor axis is first. The validation reference is built from other-fold source-adapted predictions, and the test reference from all validation members. Swapping entire predictions in the validation pairing diagnostic is equivalent to swapping histories here because `load` asserts common source and target designs. The old-test scorer contains the only explicit allowed test-label join. Development selection, same-model zero, fixed item smoothing, rank calculation, full-vector Brier, and participant bootstrap match the protocol.

Two implementation hardening requests were sent before signoff: persist an exploratory attempt marker before the label join so failures cannot disappear from the run history; explicitly assert original donor membership/order/uniqueness and saved seed aggregation/array axes before reuse. Neither changes an estimand or selects based on outcomes.

Observed root-executed checks: `boundary_checks.json` reports all focused checks passed, with 4.34375 process CPU seconds and no old-test outcome access. `smoke.json` reports 0.859375 process CPU seconds, zero profile fits, and a 65.7421875-second conservative inference forecast. The reviewer has not rerun these checks or loaded human outcomes.

## Final artifact review and approval

Both implementation requests were addressed before scoring. `predict_exposed` now validates ordered original recipient membership, five distinct validation-only donors, no self donor, `(5,102,10)` donor arrays, `(3,102,10)` optimization-seed arrays, and equality of saved own predictions to the seed mean. `score_exposed` writes an attempt marker before the label join, records completed/failed status, and refuses any existing attempt rather than allowing an unnoticed retry.

The selected source-blind comparator is the fixed-alpha training-item frequency predictor, selected from the four declared candidates using validation only. The reviewer inspected its selection metadata, not human label files. Its validation NLL is 0.4083901480; the other declared scores are 0.6138966726 (prior), 0.4493640048 (reference mixture), and 0.5667439702 (legacy). The source/target design and fitted-basis ranks are 4/3 for every optimization seed, as expected. These are development descriptions.

Independent non-label artifact checks verified specification and probability hashes, unique validation membership, exact disjoint fold/bank memberships, donor-array indexing, reference means, prior-zero consistency, valid probabilities, all five history permutations, and baseline choice against the declared development scores. No exploratory predictions or scoring attempt existed during these checks. `reviewer_validation.json` records 0.046875 process CPU seconds for these checks; zero model fits and no human-label file access. This is additional reviewer computation, not a rerun of development or the root's tests.

`diagnostic_review_signoff.json` binds this approval to the exact reviewed code, protocol, selected comparator, audit artifacts, and provenance manifests. Runtime checks must still save the new predictions before label access, enforce the original model/split/probability hashes, and preserve a single exploratory score attempt. Approval does not establish independent confirmation or remove fixed-position confounding, original validation-selection dependence, one-family scope, or the conditional nature of intervals. The completed PR5 verdict remains inconclusive regardless of these post hoc results.
