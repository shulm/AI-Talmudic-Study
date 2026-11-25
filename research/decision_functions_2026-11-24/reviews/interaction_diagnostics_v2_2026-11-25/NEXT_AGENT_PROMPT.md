# Next agent: test short-history adaptation at sixteen observations

## Assignment and starting point

Continue `shulm/AI-Talmudic-Study` through [issue #2](https://github.com/shulm/AI-Talmudic-Study/issues/2). The target remains $P(a\mid q,C(q),H_s)$, including question-dependent personal decisions. Execute one new synthetic-only study: does the frozen canonical head retain useful interaction at 16 well-covered observations?

Read `AGENTS.md`, `AGENT_HANDOFF.md`, the adjacent `REVIEW.md` and `next_short_history_design.json`, and PR #12's `RESULTS.md`, `NEXT_HANDOFF.md`, `PROTOCOL.json`, `SELECTION.json`, and `NEXT_STUDY_PROPOSAL.md` at `40d201997ab8d79d138734b1ef116c161719c11b`. Check current coordination threads and branch heads before editing. V2 selected rho=.01 with lambda_b=.1 and qualified its 96-support numerical setting on both declared realizations. Preserve that result and all prior failures.

Create a new continuation branch from the latest reviewed assignment head after recording its SHA. Use `labs/decision_functions_short_history_v1/` for versioned code and `research/decision_functions_2026-11-24/runs/short_history_v1/` for public output. Use a new private directory for generated arrays/parameters. Do not change historical laboratory/run files, merge branches, or change visibility. The old Windows caches are not needed for this fresh synthetic task.

No human fitting/evaluation, corpus acquisition, encoder/model download, paid API call, source-text expansion, or person-directed communication is included. Read parallel PR #5/#8 and #10/#11 handoffs for coordination before proposing overlapping later work; their source and exposure tracks remain separate.

## F0. Repair complete-run verification and freeze the full design

The v2 generic verifier can label an empty run PASS by checking only existing stages and upper count bounds. Its actual result is complete, but do not carry this behavior forward.

Implement protocol-derived exact stage, archive, array-key, metric-row, and ledger requirements. Use distinct verification states: `VERIFIED_COMPLETE`, `VERIFIED_DECLARED_EARLY_STOP`, and `INCOMPLETE`. A verified early stop can never qualify as a completed predictive success. This assignment declares no scientific early-stop path: a failed C predictive gate still requires D, and engineering/resource interruptions remain INCOMPLETE. The early-stop state is reserved for a future explicitly frozen permitted path, not an improvised exception. Overall qualification must be an explicit conjunction of complete valid audit evidence, passed numerical checks, successful saved-array verification, and all four primary gates on both realizations.

Before fitting, use isolated, zero-fit checks to reject: an empty run; a missing whole ledger; a missing held-out stage/archive; a missing array key; inconsistent expected IDs/counts; unsuccessful optimizer evidence; and a success flag inconsistent with prerequisites. Check the objective/gradient equivalence to v2, split/group/pair preservation, the support construction below, donor-map semantics, and permutation invariance of the mean-loss objective. Failures must not silently reduce expected counts.

Keep v2 float64 L-BFGS-B settings: `maxiter=1000`, `ftol=1e-12`, `gtol=1e-8`, `maxls=50`. Keep three classes, rank two, generator dimensions/scales, known shared logits, loss clipping at 1e-12, and initialization seeds 11/29/47. Scientific code must be immutable during the run; post-run verifier additions must have separate source hashes and cannot change outputs under test.

Commit/push the full protocol, scientific code, exact stage manifests, seeds, numerical tolerances, resources and zero-fit checks. Post the checkpoint SHA in issue #2 before the first optimizer call. Then execute the declared study without another routine confirmation. If execution is blocked, report the precise access/resource/engineering limitation and preserve reached evidence.

## Fixed fresh realizations and shared training

Use the unchanged rotational generator with parameterized seeds:

- C: generator seed `20261128`, categorical-label seed `2721`.
- D: generator seed `20261129`, categorical-label seed `2722`.

Each has 96 people, 192 cases/64 rotational groups, feature dimension 2, person partitions 48/24/24, and group partitions 40/12/12. Preserve adjacent matched pairs within partitions. Training uses 48 people and 120 cases; held-out scoring uses 24 people and 36 cases. Reserve the middle person/group partition unused; there is no new selection or tuning.

Use both positive and null regimes. Fit shared parameters at rho=.01, lambda_b=.1, rank 2, with seeds 11/29/47. This is exactly two realizations×two regimes×three seeds = **12 shared fits**. Reuse each fitted basis for all support budgets, schedules, controls and adaptation policies. Do not refit shared models for a different history length. No training-intercept certificate solves are assigned; v2 already qualified that machinery.

Materialize separate learner/support/evaluator views. The generator may mechanically write complete fixtures, but training/adaptation routines must not receive query labels or oracle query probabilities. Save each prediction before its aggregate scoring. Execute both realizations even if the first fails a scientific gate, unless an engineering or resource failure prevents valid execution. No second realization or secondary control can rescue a primary failure.

## Exact nested support schedules

For each realization, retain the generator's existing 32 complete training support groups (96 cases); do not replace this pool using outcomes or fitted parameters.

Use exactly two support seeds: `101` and `211`. For each seed:

1. Order the 32 group IDs by SHA-256 of UTF-8 `short_history_v1|<realization>|<seed>|group|<group_id>`, breaking an exact hash tie by canonical group ID.
2. Set the starting phase of each group to the integer value of SHA-256 of `short_history_v1|<realization>|<seed>|phase|<group_id>` modulo 3. Use cyclic phase order start, start+1, start+2 modulo 3.
3. Concatenate the group triplets and reveal prefixes of exactly 4, 16, 32, 96 cases. Serialize the realization as uppercase C or D and seed/group IDs as base-10 integers without leading zeros. Hash exactly the displayed UTF-8 string, with no whitespace or trailing newline; interpret the complete phase digest as a big-endian integer. Document this byte serialization in the frozen protocol.

These choices use IDs only, not angles, responses, oracle probabilities, gradients or model predictions. Save the group order, case-selection order, revealed IDs and hashes. Every person, method and donor control gets the same selected case IDs at a given schedule/budget.

Verify the raw Gram eigenvalues: k=4: (.375, .625); k=16: (.46875, .53125); k=32: (.484375, .515625); k=96: (.5, .5), within a predeclared 1e-12 absolute tolerance. A short history may reveal only part of a training group; the whole group remains in the training partition and no sibling moves to a query partition. A geometry-contract failure is an engineering failure, not permission to choose another subset.

At k=96 both schedules contain the same full pool. Use the fixture's canonical full-pool case order and fit once per head/regime/realization; reuse that saved prediction as both schedules' 96-case anchor. Nestedness concerns the revealed observation sets. Record this reuse rather than counting identical histories as independent data. Do not refit merely to reproduce a different ordering.

Include k=0 as an analytic fallback: B3/M1 equal the known shared predictor, and B1 equals its training-frequency prior. Do not call a mean-CE optimizer with an empty history. K=0 is a zero-fit sanity check outside the four-budget adaptation count.

## F1. Primary policy and one secondary scaling control

Primary policy at k=4/16/32/96:

$$
\operatorname{meanCE}_{H_s}+0.01\|u_s\|^2/2+0.1\|b_s\|^2/2.
$$

B3 uses offset penalty .1. B1 uses four pseudo-observations toward this realization/regime's training-label frequencies; B2 uses known shared logits. Supports and permitted shared information are identical across methods. Ensemble the three M1 initialization probabilities **within one history**.

At k=16 only, add the prespecified secondary count-scaled policy: personal interaction penalty .06 and offset penalty .6. Its M1 reuses the same shared bases. Its B3 comparator must also use .6. This preserves the 96-support policy's summed-loss ridge precision, because 96*.01=16*.06 and 96*.1=16*.6. It is a diagnostic control, not a new grid or replacement primary. Do not select between policies after seeing outcomes.

K=4/32/96 and count-scaled k=16 cannot rescue failure of the primary fixed-policy k=16 result. Report policy-specific qualification separately. Interpret the primary as the frozen algorithm's learning curve, not a fixed-prior information-only experiment.

## F2. Identity and uninformative-history controls without redundant fits

For every informative own-history condition, construct one matched-other prediction using donor map `pi(s)=s xor 1` on the 24 held-out rows. This preserves each adjacent pair, which has equal planted offsets and opposite positive-regime interaction phases. The mapping uses metadata, not query outcomes. It is an intentionally constructed hard negative, not a real-world matching claim.

All people share query and support identities. Therefore the donor prediction is an exact row permutation of the already-saved same-budget/same-policy own-history prediction. Use the same mapping for B1/B3/M1, and B2 as a zero-change check. No donor adaptation fits are needed. Under the null, paired oracle distributions are identical, so the pair-averaged expected donor-minus-own loss must be zero within 1e-12. This is a mapping/aggregation sanity identity, not evidence of absent spurious interaction; realized-label contrasts can vary. The positive-regime donor contrast remains informative. Score against the **recipient's** oracle/outcomes. Save the actual recipient→donor mapping, support-label provenance, input hashes and resulting array identities; independently verify the constructed mapping. Do not average probabilities from different donors before scoring.

At primary k=16, both schedules and both regimes, also execute the existing uninformative-history condition: interaction support features zero, support labels drawn from the generator's no-interaction oracle, query distribution unchanged. Fit B3 once for each condition. With zero support interaction features, the M1 optimum has u=0 and the same offset objective; construct its prediction analytically from that B3 solution. Check this identity algebraically before execution and disclose the avoided redundant solves. This control is excluded from positive/null qualification.

For numerical checks, use the positive regime at k=16 and the first support schedule, for both primary and count-scaled policies. Compare each of B3 and the three individual M1 seeds with the same first person adapted in batches of 1, 7, and the existing 24. Require maximum probability difference<=1e-6 and first-person expected-NLL difference<=1e-5. Each realization contributes 16 small batch solves/64 personal solves. No tolerance expansion is allowed after scoring.

## F3. Metrics, primary gates, and uncertainty

Primary k=16 point metrics average the two fixed support schedules. **Average losses, not prediction probabilities across different histories.** Averaging two distinct 16-observation predictions before scoring would change the information budget. Initialization seeds remain a within-history probability ensemble and do not increase the independent sample size.

Define expected NLL per person/query/history using the oracle distribution. Compute B3-minus-M1 improvement from schedule-averaged cell losses. Oracle-gap recovery is the ratio of the averaged improvement to averaged B3 excess expected NLL over the oracle. For contrast recovery, compute the unchanged v2 personal contrast separately for each history. For each of the three pairwise class log-odds, first subtract adjacent matched people, then subtract that pair difference at the first canonical query. Let $D_h$ and $D^*$ be those predicted and oracle contrasts and $j$ index matched pairs. Use $\mathrm{NRMSE}=\sqrt{\operatorname{mean}_{h,j,q,c}(D_h-D^*)^2/\operatorname{mean}_{j,q,c}(D^*)^2}$. Do not average per-history ratios or mix history predictions. Require finite metrics and positive oracle-gap/contrast denominators in the positive regime; a missing or undefined value cannot pass a gate.

Retain all four primary gates, separately for C and D:

- Positive expected-NLL gain>=.05.
- Oracle-gap recovery>=.50.
- Contrast NRMSE<=.50.
- Null expected-NLL degradation<=.01.

Report each schedule's results, the aggregate, worst schedule and distance to every threshold. No point result is rounded into a pass. The secondary policy has its own identically calculated descriptive gate table, explicitly separate from overall primary qualification. Report realized NLL, accuracy, Brier, expected NLL, initialization variation, null contrast RMS, and the single-donor-minus-own loss contrast. Do not infer accuracy improvement from an NLL improvement.

For primary gain, null degradation and positive-regime matched-other M1 contrast, use 2,000 paired bootstrap resamples per realization and report 95% percentile intervals (2.5th and 97.5th percentiles, linear quantile interpolation). Reset a fresh NumPy Generator(PCG64(1701)) separately for C and D; draw a 2000-by-12 person-pair index array, then a separate 2000-by-12 query-group index array, each uniformly with replacement from integers 0 through 11. Save these arrays and their hashes. Average support-schedule losses at each person/query cell first. Independently resample the 12 matched-person pairs and 12 query groups, retaining both people in a pair and all three cases in a query group; normalize within person and then average persons. Reject incomplete bootstrap output rather than silently using fewer replicates. Use identical resample indices for paired model contrasts. Do not pool C and D or count schedules/initializations as additional independent people. Intervals are conditional on fitted models and fixed schedules and exclude retraining uncertainty. Gates remain the predeclared point-metric rules, not newly chosen interval rules.

Record raw support Gram spectra for all nonzero budgets. As an explanatory zero-fit calculation, evaluate personal-likelihood curvature for each saved individual M1 seed head in the informative primary and secondary conditions, excluding k=0. Project the three offset coordinates onto the orthonormal columns $(1,-1,0)/\sqrt2$ and $(1,1,-2)/\sqrt6$. In the resulting two offset plus two interaction coordinates, use mean-loss units: $I=k^{-1}\sum_i J_i^\top[\operatorname{diag}(p_i)-p_ip_i^\top]J_i$, then add $\operatorname{diag}(\lambda_b I_2,\rho_{\mathrm{adapt}}I_2)$ for penalized curvature. Report data-only and data-plus-ridge minimum eigenvalues/condition numbers separately, labeling k, policy, seed and units. Record singular cases explicitly. Do not treat the probability ensemble as one parameter fit or inverse curvature as a calibrated posterior interval. Use only the saved-parameter fitted support probabilities and model features. These diagnostics cannot exclude people, select histories, alter penalties or change gates. No extra optimization is assigned.

## Exact execution ledger and limits

Per realization, require three exact stage ledgers: shared (6 records), support (76 records), and batch (16 records). Support contains 56 primary informative batches, 16 count-scaled batches, and 4 uninformative B3 batches. All support batches contain 24 people. Small numerical batches are the declared 1/7-person checks. Across both realizations:

| Component | Shared fits | Adaptation batches | Personal solves |
| --- | ---: | ---: | ---: |
| C/D shared heads | 12 | 0 | 0 |
| Primary informative: 4/16/32 across 2 schedules plus one 96-case anchor | 0 | 112 | 2,688 |
| Count-scaled 16: 2 schedules | 0 | 32 | 768 |
| Uninformative 16: B3 only, analytic M1 identity | 0 | 8 | 192 |
| Both-policy positive 16-case batch checks | 0 | 32 | 128 |
| Total | 12 | 184 | 3,776 |

Total optimizer records: 196. No training-offset, donor, zero-support, redundant 96-case, or extra uninformative M1 solves. Maximum personal-solve sanity cap 4,096; unused capacity does not authorize extra work. No retries or new configurations: a failed attempt consumes its slot and stays recorded. Stop on an execution/resource failure with explicit incomplete state. Maximum one CPU core-hour, 4 GiB memory, zero paid calls or dataset/model downloads. Report sampled totals, failures and unprofiled overhead.

## F4. Verification, reporting, and GitHub handoff

Save private arrays, support schedules, donor maps, adapted parameters and source hashes before aggregation. Independently replay the declared scalar metrics, bootstrap quantities, gate decisions, donor permutations, analytic identities and complete-run state from saved evidence without fitting. Derive exact comparison and array-key counts from the frozen protocol; upper limits alone cannot establish completion. Hash private artifacts before and after verification.

Publish a draft continuation PR, `PROTOCOL.json`, support and model manifests, exact ledgers, `RESULTS.md`, `results_summary.json`, complete verification receipts, cumulative resource ledger, and `NEXT_HANDOFF.md`. Link exact pre-fit and final SHAs in issue #2. Overall qualification requires exact complete audit/verification, passed numerical checks and all four primary gates on both realizations. Preserve a completed failure as a result; no secondary success changes its primary status.

Also write `TEXT_REPRESENTATION_NEXT_SPEC.md` as a proposal only. Define what a later text question must express, how person IDs/answers/oracle values are excluded, how semantic cases/paraphrases/templates are grouped, what numerical-feature control is matched to text features, and how encoder admission/revision/preprocessing/training-only transforms would be frozen. Do not select/download an encoder or execute that study here. If the primary 16-case result fails, identify what is observed about history coverage, numerical behavior and penalty sensitivity without asserting an information-theoretic impossibility or a uniquely established cause.

Stop after the bounded report and next specification. Do not expand the corpus, reopen DICES/SRO as fresh confirmation, train on provisional scholarly positions, or change the parallel corpus tracks. Their separate source-review work may continue under its own assignment.
