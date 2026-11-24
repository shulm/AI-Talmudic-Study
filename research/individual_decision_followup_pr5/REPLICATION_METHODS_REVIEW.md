# Independent replication methods review

Reviewer: independent_AI (methods_review), 2026-11-24. This review reads specifications only; no confirmation responses or new fitted outputs were inspected.

## Review status

Replication protocol review pending: REPLICATION_PROTOCOL.md had not yet been created when this initial note was written. No prospective experiment is approved to execute on this basis. Exactly three archival candidates were screened; none was admitted. See REPLICATION_ADMISSION.md.

## Diagnostic specification review

DIAGNOSTIC_PROTOCOL.md distinguishes exploratory exposed-test reuse from confirmation, preserves the original verdict, defines donor replacement before probability mixing, and uses disjoint development banks with source-only inference. Coherent integrated-prior zero-support predictions are separated from the historical fallback. The specification appropriately conditions intervals on the fixed models/banks, notes cross-fold dependence, uses participant weighting, and avoids treating seeds/donors/trials as people. No methods blocker identified in this document. Exact implementation review/signoff is separately assigned to model_engine; this note does not approve code or certify execution history.

## Prospective review requirements

The forthcoming protocol must identify exact task/probe/feature definitions, actual independent source and target display assignments, eligibility and independence checks, consent and exact-release permission, endpoint thresholds, all candidate models and selection rules, fixed donor/reference bank construction, budget accounting, and prediction-before-outcome-join controls. An incomplete appendix or unspecified collection size must be clearly gated rather than portrayed as execution-ready.

Requiring both co-primary lower endpoints to exceed thresholds is an intersection-union success rule. Marginal two-sided95% intervals are not jointly95% simultaneous intervals. Prospective precision must consider both paired participant contrasts and their dependence; it must not promise joint success from an arbitrary sample size. Zero thresholds support only provisional predictive signal. No recruiting, author contact, participant publication, or new confirmation is authorized by preparing a collection specification.

## Review of prospective v1 and planning helper

REPLICATION_PROTOCOL.md and precision_plan.py were read after their creation. No candidate outcomes or diagnostic result files were opened for this review. The specification correctly keeps collection authorization, ethics/consent, independent-person certification, executable adaptation, numeric confirmation size and exact-artifact signoff as unpassed future gates. It is a collection specification, not a present permission to run confirmation.

The source/target complementary layouts are independently assigned; each source2/4/8 prefix and target10-trial schedule is balanced. The four layout-pair blocks identify the intended actual presentation intervention. Requiring actual rendering logs and retaining unresolved assignment deviations is appropriate. Semantic encodings alone are explicitly insufficient. Raw task definitions, hypothetical incentives, role separation, eight charged probes, source-only inference, fixed-bank comparators, single-donor scoring, seed aggregation, supporting position control, participant weighting and restricted inferential scope are specified.

Findings sent to the author before final review:

1. Future planning must use the newly selected source-blind comparator, not the current helper's hardcoded item_frequency_8. The present helper is valid only as clearly labeled exploratory original-development planning. The future adaptation must implement the new matching/fold specification and selected-comparator contrast before its size decision.
2. The normal Monte Carlo bound p-1.96*sqrt(p*(1-p)/200) degenerates at p=1. Freeze a Wilson or exact binomial lower confidence bound instead of allowing a zero estimated error to imply certainty. This concerns Monte Carlo error only; it does not resolve transport or development-variance uncertainty.
3. Candidate250 must be rounded to252 before simulation, or explicitly resimulated after rounding, so the numeric confirmation size equals the tested candidate.
4. Use control-minus-own consistently for the position control; the initial own-minus-control wording otherwise reverses the stated positive-is-better convention.
5. Explicitly distinguish the intersection-union success rule from simultaneous interval coverage. The two marginal95% intervals are not jointly95% simultaneous intervals.
6. Freeze a deterministic development-fold assignment rule/seed in the future executable contract. The specification gives correct fold/bank sizes, but an implementation needs the exact membership algorithm.

No recruitment or new confirmation occurred in this review. These findings do not authorize changes to the completed pilot, diagnostic endpoints, or candidate admission. Future precision remains conditional on fixed fitted models/reference banks and a finite development-residual approximation; matched cross-fold residuals may be dependent. This must remain a limitation, not a claim of guaranteed power under new counterbalanced data.

## Final specification review after revisions

The six findings above were addressed in the prospective specification: the future planner uses the selected comparator and matched-layout donors; the size rule uses the explicit Wilson lower bound;252 is simulated directly; the control sign is consistent; marginal versus simultaneous coverage is distinguished; and development folds use a declared stratified SHA256 ordering. The existing precision_plan.py remains an original-development illustration (including its250-person candidate), not the future executable specification. That distinction is explicit and acceptable.

**Disposition: suitable as a gated prospective collection/replication specification; no remaining methods blocker to delivering this document. NOT an execution signoff, admission, recruitment approval, human review, or confirmation result.** Final instruction/translation/comprehension text, consent/custodian certifications, numeric n, future executable ingestion/model/planner and exact fitted-artifact review remain required before execution, as the protocol states. Conditional residual simulations cannot guarantee new-cohort power; finite development uncertainty and cross-fold bank dependence remain planning limitations even when Monte Carlo error is bounded.

Reviewed SHA256 bytes:

- REPLICATION_PROTOCOL.md: `5a1972dda64078494368db1f568336cf81355cb833b1dd7eabe69099ae5ff4d2`
- precision_plan.py: `6ef0740695412731f6449bfab4c2a7c3d750fb07b3f4d25cec0b4e3d0f0011ba`
- DIAGNOSTIC_PROTOCOL.md: `a4ad9e85cbd863fbf489aa36c1052ca514138393537b93f2cf0496981b9bc316`

This final disposition supersedes the initial pending status above while preserving review history. No outcome inspection or fitting was needed for this review.
