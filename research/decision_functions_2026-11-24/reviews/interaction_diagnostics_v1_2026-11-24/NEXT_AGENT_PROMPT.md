# Next agent: execute the canonical-penalty synthetic diagnostic

## Goal and evidence to preserve

Continue `shulm/AI-Talmudic-Study` through [issue #2](https://github.com/shulm/AI-Talmudic-Study/issues/2). The target remains $P(a\mid q,C(q),H_s)$, including person-specific responses to question features. This task is a bounded synthetic diagnostic, not a new human experiment.

Read `AGENTS.md`, `AGENT_HANDOFF.md`, the adjacent `REVIEW.md` and `next_synthetic_design.json`, and PR #7's `DIAGNOSTIC_REPORT.md`, `synthetic_protocol.json`, `NEXT_PROTOCOL_PROPOSAL.md`, and `NEXT_HANDOFF.md` at delivery `6da06a4b01bb825bcf4ad4b13c61648d6ee82220`. Also inspect current issue/PR comments for intervening work. The present prompt revises D4's proposal; it does not revise the completed v1 result.

Settled evidence: saved-array replay is reproducible by the committed verifier; audit records now reject missing evidence; the head learns a planted interaction; the complete v1 synthetic gate fails on the null; all original DICES penalties favor zero interaction under that objective. Neither original Windows cache is needed for this assignment.

Keep `runs/pilot_v1/`, `runs/interaction_diagnostics_v1/`, and their laboratory implementations unchanged. Work on a new branch from the reviewed continuation head after recording its exact SHA. Put versioned code in `labs/decision_functions_diagnostics_v2/` and public outputs in `research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/`. Store generated arrays and fitted parameters in a new private run directory. Publish aggregate evidence, hashes, manifests, and code. Do not merge branches or change visibility.

## Fixed scientific design

Use the same generator family, dimensions, likelihood, rank-two architecture, support design, metrics, and informative/uninformative conditions as v1. Parameterize the generator seeds; do not change its signal scales or replace a failed realization. Keep three classes, 96 people, 192 cases in 64 rotational groups, person partitions 48/24/24, group partitions 40/12/12, and 96 support cases from 32 training groups. Preserve matched-person pairs and whole case groups within partitions.

Declare two independent generated realizations before any fitting:

- **A, selection and first held-out check:** generator seed `20261126`, categorical-label seed `2719`.
- **B, independent realization:** generator seed `20261127`, categorical-label seed `2720`.

Initialization seeds are `11,29,47`; ensemble their probabilities. They are optimization repetitions within each realization, not independent data replications. Realization B must not be materialized, inspected, or scored before the selected configuration is frozen. On B, train new shared parameters on its own training block using the already-selected rule; do not transfer A's latent person vectors or reselect hyperparameters.

Keep known shared logits fixed. No encoder, embedding download, feature transformation, rank change, or human data is included.

## Corrected parameterization

Use

$$
J=\operatorname{mean\ CE}
+\frac\rho2\left(\|V\|_F^2+\frac{\|U\|_F^2}{S}\right)
+\frac{0.1}{2S}\|b\|_F^2.
$$

For new-person adaptation, use mean support CE plus $\rho\|u_s\|^2/2+0.1\|b_s\|^2/2$; average the per-person objectives when batching. This is the canonical choice $\lambda_V=\lambda_U=\rho$, with independently fixed $\lambda_b=0.1$.

Exactly three candidates are allowed, identified by their products to avoid ambiguous rounded values:

1. `rho=sqrt(0.00001)`.
2. `rho=sqrt(0.0001)`.
3. `rho=sqrt(0.001)`.

The original pairs `(0.001,0.1)` and `(0.01,0.01)` both map to the second candidate. Do not count them as separate models. Use float64 and the v1 diagnostic L-BFGS-B settings: maxiter 1000, ftol 1e-12, gtol 1e-8, maxls 50. Keep initialization distributions unchanged.

Controls: B3 with personal-offset penalty 0.1; B1 with four pseudo-observations toward training-label frequencies; B2 with known shared logits. Every method receives the same support cases/outcomes and permitted shared information. Compute training-frequency priors from the appropriate realization's training block only. B1/B2 require no optimizer fit.

## E0. Implement, verify, and publish the pre-fit checkpoint

Implement a new version rather than modifying v1. Carry forward immutable stage ledgers, exact configuration identities, finite-field validation, original scientific/audit status separation, and private-array manifests. Record both rho and lambda_b explicitly.

Before invoking an optimizer:

1. Verify the new objective/gradient algebra and finite differences on fixed, small numerical inputs.
2. Verify logit/objective rescaling invariance under $(\lambda_V,\lambda_U,V,U)\mapsto(t\lambda_V,\lambda_U/t,V/\sqrt t,\sqrt t U)$, including the new-person adaptation objective. This is a zero-fit calculation, not another candidate fit.
3. Verify the old single-penalty objective is recovered when `rho=lambda_b=old_lambda`, without fitting.
4. Check grouped partitions, pair preservation, support/query boundaries, generated shape contracts, and exact selection-code access boundaries. Oracle/query arrays must remain evaluation inputs, not fitting inputs.
5. Prepare exact stage-A ledger IDs and deterministic selected-configuration ledger templates for later stages. Each stage gets its own immutable expected-ID manifest; completed manifests must never be rewritten.

Commit all scientific code, the machine-readable protocol, seeds, gates, planned counts, and environment identity. Push and post the exact checkpoint SHA in issue #2 before the first fit. Then execute the declared stages without requesting another routine confirmation. If required access or resources are unavailable, complete what is possible and report the precise blocker.

## E1. Development selection on realization A

Materialize A with separate training, support, development-query, and held-out-query views. Training consumes 48 training people and 120 training cases. Development adaptation consumes only the 24 development people's informative support observations; selection evaluates their 36 development cases. Development selection uses informative histories only. Uninformative-history evaluations are reserved for the held-out stages and are not additional development adaptation batches.

Fit exactly three rho candidates × two regimes (positive/null) × three initializations: **18 shared fits**. Adapt each candidate/seed to development histories. Compare the probability ensemble to B3 using oracle-expected NLL and the unchanged contrast metric. Retain every candidate and seed result.

A candidate is eligible only if all four predictive criteria pass on development:

- Positive expected-NLL gain over B3 is at least `0.05`.
- Positive oracle-gap recovery is at least `0.5`.
- Positive personal-contrast normalized RMSE is at most `0.5`.
- Null expected-NLL degradation versus B3 is at most `0.01`.

Among eligible candidates choose the greatest positive expected-NLL gain. Gains within `1e-5` are numerical ties; prefer the larger rho. If no candidate is eligible, publish `NO_QUALIFIED_INTERACTION` and stop without scoring either held-out block or materializing B. Do not fall back to a candidate that passes only the null, change the thresholds, or add a candidate.

For the selected positive-regime models and B3, compare the same first development person adapted in batches of 1, 7, and the existing 24. Require maximum probability discrepancy at most `1e-6` and absolute expected-NLL discrepancy for that person at most `1e-5`. Record deterministic objective repeats as a separate zero-fit numerical check. A tolerance failure is `NUMERICALLY_UNRESOLVED`; do not enlarge the tolerance after inspecting results.

Fit one training-intercept-only batch per regime with lambda_b=0.1 to compute the training gradient G. Reuse each G across the three candidate thresholds; no repeated intercept fit per rho is needed. The separated certificate uses:

- `residual = mean_i(p-y) + lambda_b*b`.
- `threshold = rho/sqrt(S)`.
- Intercept-error denominator `lambda_b`, not rho.

Report spectral margins and numerical uncertainty as explanatory diagnostics, never as a substitute for held-out predictive gates.

## E2. Freeze selection and evaluate A's held-out block once

Publish a second immutable checkpoint with the selected rho, complete stage-A ledgers, fitted-model hashes, numerical checks, and exact later-stage manifests. Selection must be locked before any held-out metrics are computed.

Evaluate the selected models on A's 24 held-out people and 36 held-out cases. Use both informative and uninformative support conditions. Save probabilities before aggregate reporting. Compute the same positive/null predictive gates, oracle-expected metrics, realized NLL/accuracy/Brier, seed diagnostics, contrast metrics, and simple baselines.

Uninformative support is an engineered identifiability control: zero interaction features and support outcomes from the zero-interaction oracle, while positive query interaction remains. Expect inability to recover that interaction. Keep the check distinct from the informative positive/null qualification.

Record a held-out failure without reopening development selection. Continue to the predeclared independent realization for diagnostic completeness unless an engineering or resource failure prevents valid execution; its result cannot rescue a failure on A.

## E3. Independent realization B at the frozen configuration

Only after selection is frozen, materialize B using its declared seeds and the unchanged generator. Fit the selected rho × two regimes × three initializations: **six shared fits**. The B development partition is unused for selection or redesign.

Use B's training block for shared fits and its 24 held-out people's training-group histories for adaptation. Evaluate its held-out queries once, in both support conditions, with the same controls and metrics. Compute one training-intercept certificate per regime (two total on B), at the selected rho.

Require all four predictive gates separately on each held-out realization. Do not pool results to conceal a failed null or contrast gate. Two generated realizations support a bounded engineering claim, not universal null control, natural-language adequacy, or human-domain generalization.

## Exact budget and ledger accounting

No retries or extra configurations are included. A failed attempt consumes its planned slot and remains in the ledger. Stop if the fixed design cannot be completed within the caps.

| Stage | Shared fits | Adaptation batches | Personal solves |
| --- | ---: | ---: | ---: |
| A training-offset certificates | 0 | 2 | 96 |
| A development: all M1 candidates/seeds | 18 | 18 | 432 |
| A development: B3 by regime | 0 | 2 | 48 |
| A selected positive batch-size checks | 0 | 8 | 32 |
| A held-out: selected M1, two regimes/conditions | 0 | 12 | 288 |
| A held-out: B3, two regimes/conditions | 0 | 4 | 96 |
| B training-offset certificates | 0 | 2 | 96 |
| B held-out: selected M1, two regimes/conditions | 6 | 12 | 288 |
| B held-out: B3, two regimes/conditions | 0 | 4 | 96 |
| **Maximum completed design** | **24** | **64** | **1,472** |

The complete maximum is 88 optimizer records: 24 shared plus 64 adaptation batches. Conditional early stops use fewer. Keep the outer personal-solve cap at 4,096 for detecting mistakes, but the declared experiment contains exactly the table above; unused capacity does not authorize additional scientific solves. Zero human fits/solves/evaluations, zero new corpus/model downloads, zero paid model calls. Maximum one CPU core-hour and 4 GiB sampled memory. Report sampling limits and unprofiled overhead explicitly.

## E4. Deliver through GitHub and stop

Create a draft continuation PR targeting the new review branch. Publish `PROTOCOL.json`, `SELECTION.json` when reached, `RESULTS.md`, `results_summary.json`, exact ledgers, prediction manifests, resource receipts, independent arithmetic verification, and `NEXT_HANDOFF.md`. Update the active handoff with links while preserving historical results. Post exact pre-fit, selection-freeze, and final SHAs in issue #2.

Separate these outcomes in the report: audit completeness; numerical resolution; development eligibility; held-out A qualification; held-out B qualification; and overall qualification. Overall success requires complete valid audit records, passed numerical checks and saved-array verification, development eligibility, and all four predictive gates on both held-out realizations. A completed failure is a valid result. No new candidate, threshold, data seed, fixture family, or run is added after failure.

If qualification succeeds, propose the next limited-history/text-representation study without executing it. If qualification fails, explain which gate failed and whether the result suggests signal attenuation, spurious interaction, numerical issues, or insufficient evidence; do not assign a cause the data do not establish.

Read the parallel PR #5 and PR #8 handoffs before proposing future human confirmation. DICES and the SRO pilot/follow-up are exposed; a new split is not new confirmation. Prior TID-8 admission questions and scholarly expert-review requirements remain unresolved tasks on their own tracks. This assignment does not acquire those corpora, repeat scholarly preparation, contact anyone, run human models, or merge PRs.
