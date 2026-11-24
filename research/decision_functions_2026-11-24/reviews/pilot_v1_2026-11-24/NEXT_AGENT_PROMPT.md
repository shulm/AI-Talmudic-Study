# Next agent: diagnose interaction collapse and prepare the next protocol

## Objective and starting point

Work in `shulm/AI-Talmudic-Study`. Continue the general decision-function study coordinated in [issue #2](https://github.com/shulm/AI-Talmudic-Study/issues/2). The target remains $P(a\mid q,C(q),H_s)$: predict a specified person's decision from problem content and their observed history. Speaker identification is a different task.

Completed pilot: draft PR [#4](https://github.com/shulm/AI-Talmudic-Study/pull/4), final commit `0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0`, effective freeze `4de12a1fb300a7c9e9d927591bc4b101f0e263a2`. Read `AGENTS.md`, `AGENT_HANDOFF.md`, the pilot's `AGENT_REPORT.md`, `NEXT_HANDOFF.md`, `experiment_protocol.json`, `results_summary.json`, and the adjacent `REVIEW.md` before implementation. Check the current issue/PR threads for intervening work and branch changes.

The outcome is settled for that experiment: history improves NLL/Brier; M1 is numerically equivalent to B3; accuracy is lower than B2; detailed development convergence logs were lost. The next task is to distinguish a validation/optimization problem from regularization-induced collapse and representation limitations. Do not seek a favorable reinterpretation of the exposed test.

## Scope, location, and limits

Create a separate continuation branch from the latest review branch containing this prompt, after inspecting its exact head. Preserve the `pilot_v1` run directory and frozen implementation. Put new tooling under `labs/decision_functions_diagnostics/` and new outputs under `research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/`. Reuse the old objective only through an explicitly versioned adapter or copied, source-attributed implementation whose equivalence is checked.

The original private cache is at `C:\Users\David\.cache\decision_functions\pilot_v1` on the executing machine. Use an explicit `--private-root` argument. Read it without modifying files. If it is unavailable, complete all public/synthetic work, report `CACHE_UNAVAILABLE` for dependent tasks, and provide the exact read-only command for the original machine. Do not download the human corpus again or refit models to imitate the missing cache.

This assignment permits:

- Public-artifact inspection and a read-only verification of already saved, already reported arrays, where available.
- At most **24 synthetic shared-head fits** and **4,096 synthetic personal adaptation solves**, on small generated fixtures. Keep a ledger; an optimizer retry counts again.
- At most **three human training-intercept batch solves**, one for each original $\lambda\in\{0.1,1,10\}$, using frozen B2 logits and training-only features/labels. With 62 people this is at most 186 personal solves. These are new diagnostics, not recovered original fits.
- At most one CPU core-hour, 4 GiB peak memory, zero paid model calls, and no new dataset/model downloads. Inspect existing dependencies first. If limits block completion, report the specific unfinished work rather than expanding the search.

No new B2 or M1 fits on human data, human hyperparameter search, new held-out human predictions, changed human split, or new held-out human experiment is assigned. The explicitly permitted D3 training-intercept solves may compute their training probabilities and gradients. Offline verification may recompute only the originally declared quantities from saved arrays; this does not reopen the test for model selection. Do not merge a PR or change repository visibility. Keep participant records, text, histories, weights, and probabilities outside Git; publish code, aggregates, manifests, and hashes.

## D0. Preserve and reproduce the completed evidence

Implement a standalone offline verifier. It must not call the fitting functions or `evaluate.batch`, and must not require moving the execution branch back to the freeze. Validate the immutable code/protocol snapshot separately from the working branch state.

From the existing cache and pinned manifests, verify:

1. Source/private artifacts and saved archive SHA-256 values; exact named array keys and expected counts, not merely a minimum count.
2. The 171 array shapes, finite/nonnegative probabilities, normalization, and documented numerical tolerance; the 24 paired-loss arrays and original loss clipping convention.
3. The reported model/budget means, accuracy, Brier, seed diagnostics, fixed derangements, and originally reported contrasts, using the original aggregation and bootstrap seeds.
4. Maximum M1–B3 probability difference at the reported comparison scope.
5. Original artifact bytes remain unchanged before and after verification.

Write a new verification receipt with code SHA, commands, environment versions, exact input hashes, comparison tolerances, mismatches, and resource use. Distinguish `REPLAYED_FROM_SAVED_ARRAYS` from `PUBLIC_MANIFEST_ONLY`. Hash agreement establishes identity, not that the generating model was scientifically correct. Do not regenerate missing arrays or silently rewrite the old final-verification JSON.

Use isolated toy arrays to test that the verifier rejects changed bytes, missing keys, bad normalization, and inconsistent loss aggregation. These are necessary failure-path checks, not a new scientific evaluation.

## D1. Make future audit validation fail closed

The old condition `all(o['success'] for o in dev['optimizations'])` accepts the recovered empty log. In the new diagnostics tooling:

- Give each stage, configuration, initialization, and adaptation batch a unique ID and separate append-only record path. Persist records before replaceable summaries and use atomic writes.
- Declare expected shared-fit records, adaptation batch records, and person-solve counts before execution. Check exact configuration identity, not just a nonzero count.
- Record optimizer status, stopping message, iterations, objective, gradient scale/residual, seeds, parameter/feature dimensions and norms, and finite-value checks. A successful library flag and a small stationarity residual are different observations.
- Treat missing records, unexpected configurations, unsuccessful termination, and interrupted runs explicitly. `RECOVERED_SELECTION_ONLY` must not become `VERIFIED_OPTIMIZATION`.
- Add meaningful failure-path checks for empty logs, a missing configuration, nonconvergence, and a simulated output-name collision. Preserve the pilot's historical log-loss disclosure.

The continuation's status must report mathematical checks, audit completeness, predictive recovery, and cache access separately. A single broad `PASS` must not hide an unperformed component.

## D2. Demonstrate that the head can learn a known interaction

Before any synthetic fit, commit a compact synthetic protocol containing the generator, fixed seeds, dimensions, candidate settings, fit accounting, acceptance thresholds, and expected null/positive behavior. Publish that checkpoint in issue #2. This is a diagnostic protocol, not a new human preregistration.

Use the same three-class likelihood and low-rank interaction family as M1. Start with informative numerical features whose relationship to generated labels is known. The primary positive control must be generated by a nonzero interaction inside that family. Keep a pure personal-offset null condition. Split synthetic people and question cases separately; all variants of a case stay in one group.

Required design properties:

- Include known shared logits, personal offsets, a known low-rank interaction, and an oracle probability predictor. Report the generator's rank, signal scale, and stochastic-label policy.
- Use sufficient history coverage and verify the support feature design is informative for adaptation. Include an intentionally uninformative-history condition as an identifiability control; failure there is expected, not a solver defect.
- Make interaction recovery necessary: prevent a large imbalance in personal label frequencies from satisfying the positive criterion alone. Quantify any residual imbalance. A designed contrast between people with matched class frequencies is useful.
- Compare B3 and M1 under identical supports. Include the original penalty settings as a diagnostic condition and a predeclared signal-permitting setting justified from synthetic training data, with all attempts recorded.
- Measure prediction quality on new synthetic people and questions, recovery relative to the oracle, interaction contribution magnitude, and a question-dependent personal contrast. Raw $U,V$ coordinate similarity is not a valid recovery criterion because their factorization is nonidentifiable.
- Specify substantial predictive recovery criteria and the acceptable null behavior before results are exposed. A $10^{-12}$ improvement, finite probabilities, or nonzero weights alone cannot pass.
- Test whether batching a fixed person's adaptation with additional independent people materially changes their result beyond the declared solver tolerance. This checks the globally averaged objective's numerical stopping behavior.

Report all configurations and seeds, including failures. If the informative-feature positive control fails, investigate within the fixed budget and record deviations; do not proceed to a new human experiment. Do not keep generating favorable fixtures until one passes. Any revised diagnostic must have a new version and preserve the failed one.

A text-to-embedding fixture is a separate follow-up. It may be specified here, but downloading or comparing encoders is outside this assignment. Numerical-feature recovery establishes the head's capability, not that a pretrained text embedding contains the needed distinctions.

## D3. Test whether the original objective favors zero interaction

Use the derivation in `REVIEW.md`. For each of the three original penalties, keep the cached B2 parameters and original training center fixed. Load only training outcomes/features for this diagnostic. Optimize training-person offsets with zero interaction; do not use development/test histories or query outcomes.

For $S$ training people and $N$ training questions, construct

$$
G_{s,(c,j)}=\frac1{SN}\sum_i
\left[\operatorname{softmax}_c(g_i+b_s^{(0)})-\mathbf1(y_{si}=c)\right]\tilde z_{ij}.
$$

The implemented factor penalty induces $(\lambda/\sqrt S)\|W\|_*$. Compare $\|G\|_{\mathrm{op}}$ to $\lambda/\sqrt S$.

Record $S,N,d$, input/model hashes, feature scales, intercept optimality residuals, largest singular value, threshold, signed margin, and a numerical error/tolerance assessment. Validate the formula first on a small synthetic case with a deliberately satisfied and violated inequality. For a violated inequality, check the predicted rank-one descent direction on that synthetic objective.

Use three conclusions:

- `ZERO_INTERACTION_OPTIMAL`: the inequality holds with a defensible numerical margin and adequate intercept convergence. The declared objective can explain collapse.
- `NONZERO_DESCENT_AVAILABLE`: the inequality is violated beyond numerical uncertainty. A nonzero interaction can improve the training objective; investigate optimizer behavior rather than concluding there is no signal.
- `NUMERICALLY_UNRESOLVED` or `CACHE_UNAVAILABLE`: do not force a scientific conclusion.

The certificate concerns the training objective. It does not show that a nonzero interaction generalizes, and violation is not authorization to tune on the exposed human test. These new training-intercept logs must not be presented as the missing original development logs.

## D4. Write the next experimental proposal and stop at its checkpoint

Based on diagnostics, propose one bounded continuation rather than a broad architecture sweep. Candidates include separating interaction and offset penalties, correcting feature scaling using training data, resolving an optimizer failure, or testing a representation with independently supported relevance. Explain which diagnostic justifies the choice.

Prespecify:

1. A strong B3 baseline and B1/B2 controls; identical information and support budgets.
2. The loss normalization and independent penalty definitions, feature transforms, candidate count, seeds, tie rule, and compute budget.
3. Numerical equivalence tolerances validated on controlled computations, separately from the smallest scientifically worthwhile held-out effect. Prefer the simpler model when development differences are numerically equivalent.
4. Disjoint people and question families, support/query boundaries, grouping limitations, missingness policy, metrics, paired uncertainty, and history controls. Retain accuracy as a reported tradeoff alongside proper scores.
5. A concrete independent dataset or demonstrably untouched future units, with exact source/license/revision and overlap audit before acquisition or scoring. Existing general-corpus literature and the pilot's `NEXT_DATASET_AUDIT.md` are starting points; verify any newly relied-upon source claims against primary sources.
6. A clear label for exploratory reuse. A new random split of already exposed DICES data is not fresh confirmation. A second corpus still requires an explicit domain-transfer question rather than assuming transfer to Talmudic texts.

Write `DIAGNOSTIC_REPORT.md`, `NEXT_PROTOCOL_PROPOSAL.md`, and `NEXT_HANDOFF.md`, plus machine-readable audit/resource/verification results. Include exact commands, source SHAs, failures, and which components could not run. Open a draft continuation PR and post an issue #2 summary linking the immutable report and proposal. Preserve original results and clearly distinguish observed, independently replayed, mathematically derived, proposed, and unavailable evidence.

Stop after the diagnostic report and reviewable next-protocol proposal. No second human held-out scoring batch, large corpus preparation, or representation search is included in this assignment.

## Completion criteria

The assignment is complete when the available-cache verification is reproduced or precisely blocked; future audit gaps fail explicitly; informative synthetic recovery is demonstrated or a bounded failure is documented; the regularization diagnostic is computed or precisely blocked; and GitHub contains an evidence-linked next protocol proposal. A favorable interaction result is not required. An honest diagnostic failure is a useful completed outcome.
