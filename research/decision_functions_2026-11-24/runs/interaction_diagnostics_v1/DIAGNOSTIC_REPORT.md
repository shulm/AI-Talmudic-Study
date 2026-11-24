# Interaction diagnostics v1 — executed report

**D0–D4 complete.** Original cache available; saved evidence replayed; audit failure paths fixed in separate tooling; informative synthetic interaction recovery demonstrated; full synthetic gate **failed on the null**; original DICES penalties favor zero interaction. No second human evaluation was run. Human confirmation remains blocked.

Branch `codex/interaction-diagnostics-v1`; draft PR https://github.com/shulm/AI-Talmudic-Study/pull/7; issue https://github.com/shulm/AI-Talmudic-Study/issues/2. Base review `ef580ec8c8b92c65179c5b0a5840c60a5cbfd612`. Synthetic protocol/code checkpoint **5fc8cf48394b4e620a75be8e8f92054a6c02a451** was pushed and posted before fitting. Final delivery SHA is recorded in the PR/issue, avoiding a self-referential commit hash.

## D0 — independently replayed existing arrays

The read-only verifier validated 19 frozen public integrity files, exact 171 prediction keys/shapes and 24 paired-loss keys/shapes, pinned private/source/archive hashes, normalization and finite probabilities. It replayed support-curve scores, disagreement-subset scores, per-person losses, training-seed diagnostics, shuffled-history point contrasts, and original 2,000-resample paired bootstrap intervals. Maximum arithmetic discrepancy: **0.0** at absolute tolerance 1e-12. Consumed private bytes had identical before/after hashes. Original M1–B3 maximum probability difference remains 6.0072169461e-11.

This independently reproduces saved-array arithmetic. It does not regenerate predictions from weights, prove the historical execution used the reconstructed derangement schedule, restore lost optimizer logs, or establish scientific model correctness. It adds no new inferential claim about shuffled histories. The old sign-only positive status remains untouched; the scientific interpretation stays NO_RESOLVABLE_INTERACTION_GAIN. NLL/Brier improvement is **improved probabilistic prediction**, not specifically established calibration improvement.

## D1 — audit evidence fails closed

Expected stage/configuration/seed/batch identities are declared first. Separate start/completion records are atomically published and cannot overwrite one another. The ledger requires exact IDs, counts, mandatory optimizer fields, finite values and successful termination. Empty logs, missing configurations, interrupted runs, identity changes, incomplete numerical fields, nonconvergence and output collisions are rejected. Successful termination and stationarity residuals remain separate observations.

Measured ledgers: **104 synthetic records** (24 shared fits plus 80 adaptation batches, 1,952 person-solves) and **three human training-intercept records** (186 person-solves), all successful and complete. Original development remains RECOVERED_SELECTION_ONLY. New diagnostic solves never substitute for the missing original records. The versioned objective adapter matches frozen objective values and gradients on fixed toy inputs; finite-difference checks pass. No optimizer was invoked by those engineering checks.

## D2 — planted recovery and preserved null failure

Fixed generator: 96 people, 192 circular-feature cases/64 rotational groups; people 48/24/24 and groups 40/12/12. Training uses 48 people and 120 cases; test uses 24 new people and 36 new cases; support contains 96 training cases, with Gram eigenvalues [0.49999999999999994, 0.5000000000000001]. Development was reserved and not scored. Matched pairs share nonzero offsets and have opposite interaction phases. Known shared logits scale 0.25, planted rank two scale 2.5, offset standard deviation 0.12; categorical seed 2718, generator seed 20261125, optimization seeds 11/29/47. No text encoder was used.

At the predeclared weak penalty 0.001, informative supports give:

- Oracle-expected NLL: B3 **1.103753636**, M1 **0.463527496**, oracle **0.437046045**.
- Gain **0.640226141**, oracle-gap recovery **96.028%**, contrast normalized RMSE **0.203964**: all positive-control gates pass.
- Realized NLL B3 1.096394, M1 0.466101; accuracy 0.437500 → 0.798611; Brier 0.661041 → 0.273051.
- Null expected-NLL degradation **0.011949302**, exceeding the predeclared maximum 0.01. **Do not round this into a pass.** Null contrast RMS is 0.393161 although oracle contrast is zero.
- Uninformative supports produce zero interaction gain and contrast NRMSE 1, the expected identifiability failure.
- Maximum batch-size probability difference **1.67186372e-07**, below 1e-6. This tests a fixed person's adaptation alone, with seven people, and against the original 24-person batch.

Overall outcome: **BOUNDED_DIAGNOSTIC_FAILURE**, with informative-feature capability demonstrated. The known null and positive regimes must both pass before a human extension. All four penalties and all seeds are retained; no fixture replacement, penalty tuning, retries or extra fits occurred. The 0.001 setting has training spectral norm 0.0487941 versus threshold 0.000144338, supporting its predeclared signal-permitting rationale. This does not remove its measured null failure.

Expected matched-pair class-frequency discrepancy reaches 0.051256 (sampled maximum 0.114583); matching offsets does not imply exactly matched marginal class frequencies. The large B3 contrast and recovered question-dependent log-odds establish that frequency offsets alone cannot explain this positive control. The wording variants were materialized after fitting solely to inspect grouping; they neither supplied encoder features nor added label observations.

## D3 — original training objective favors zero interaction

Saved B2 and training center were fixed. Only the training block was used: S=62, N=207, d=384. Three new intercept batches, one per original penalty, produced:

| lambda | ||G||op | lambda/sqrt(S) | threshold minus norm | numerical bound | Conclusion |
|---:|---:|---:|---:|---:|---|
| 0.1 | 0.002618463452 | 0.0127000127 | 0.01008154925 | 1.079e-07 | ZERO_INTERACTION_OPTIMAL |
| 1.0 | 0.00254529534 | 0.127000127 | 0.1244548317 | 1.78e-09 | ZERO_INTERACTION_OPTIMAL |
| 10.0 | 0.002531989071 | 1.27000127 | 1.267469281 | 7.22e-11 | ZERO_INTERACTION_OPTIMAL |

The bound uses strong convexity of each regularized intercept problem and the softmax Jacobian bound: `||delta G||op <= ||Z||op ||r||F / (2 S sqrt(N) lambda)`, plus a conservative floating-point SVD allowance. These are numerical certificates, not interval-arithmetic proofs. The observed margins exceed these bounds comfortably. Largest human per-person intercept residual is about 1.94e-6; it is reported rather than described as exact convergence.

The training objective therefore explains zero interaction at all three original penalties. Increasing rank cannot defeat that penalty-induced optimum. This says nothing about generalization under weaker or separately normalized penalties. A subsequent independent source join reconstructed the 62×207 training-label matrix from the pinned raw CSV exactly. Its original standalone matrix hash was not historically pinned; the source-based equality check supplies the missing provenance link without refitting.

## Resources, failures and preservation

22.109375 sampled child CPU seconds; 36.421000 summed profiled wall seconds; peak sampled RSS 105226240 bytes. Exact optimizer process CPU sum 8.203125 seconds. All six profiled scientific/check commands exited zero. No installation, dataset/weight downloads, paid calls, human B2/M1 fits or new human held-out predictions. Git, reporting, small inspections and metadata HTTP requests are not included in process-profiled totals; sampling may omit the last 0.05-second interval.

Scientific failure: null gate exceeded by about 0.0019493 NLL. It is preserved as the main constraint on continuation. Documentation browser access failed for several primary URLs; direct read-only HTTP retrieval succeeded, and source identities/hashes are recorded. No run artifacts were overwritten. Additional post-run validation strengthened mandatory ledger-field checks and materialized wording/grouping artifacts; it did not change fitting or scoring code/results. Source hashes in receipts identify the exact working code, including those additions before their final commit.

The original frozen laboratory and pilot_v1 directory remain unchanged. Original source corpora, scholarly reports, repository visibility and PR #5's parallel branch are preserved. Exposure reconciliation in exposure_ledger.json treats DICES and SRO as exposed, Cross-Psych-101 as rejected on the parallel track, and its scholarly preparation as provisional. No independent re-audit of PR #5's calculations is claimed.

## D4 — next decision

The attached NEXT_PROTOCOL_PROPOSAL.md proposes one small synthetic study separating offset and interaction penalties, retaining both positive and null gates. It does not start that study. TID-8 CommitmentBank is the first conditional confirmation candidate, but its card lists an unknown license, constituent terms remain unresolved, and identity/overlap/support coverage have not been audited. No human acquisition or confirmation may follow automatically. Preserve the numerical-head result separately from any future representation or domain-transfer claim.

Evidence: replay_receipt.json, engineering_checks.json, audit_validation.json, synthetic_results.json, human_certificate.json, diagnostic_verification.json, records/, commands/, RESOURCE_USAGE.json, candidate_source_audit.json and exposure_ledger.json. Exact commands are in the laboratory README and command receipts.
