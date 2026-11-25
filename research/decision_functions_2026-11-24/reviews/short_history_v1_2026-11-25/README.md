# Short-history v1 review and evidence-dependent personalization

Reviewed [PR #15](https://github.com/shulm/AI-Talmudic-Study/pull/15) at `ee2b0a5a2f0916fed3dd59f720b902eb332eecc3`; pre-fit `89d9e0ca1b3fe3e23c3829294d3a806949943d3a`.

**Disposition: retain `VERIFIED_COMPLETE / COMPLETED_PRIMARY_FAILURE`.** The experiment recovers substantial personal interaction at 16 observations, but primary null degradation fails in both C and D. The stronger joint adaptation policy does not qualify on D; D's 96-observation anchor also fails. The earlier A/B qualification remains bounded evidence for those realizations.

The previous empty-run verifier weakness is repaired. Independent review checked public arithmetic, exact records, manifests, resources, and the empty-run failure path. The original private cache was unavailable, so its 17,038 saved-evidence comparisons were not independently replayed here.

The next assignment is **`evidence_shrinkage_v1`**: one fixed evidence-dependent probability mixture, tested on four fresh mixed populations where the same learned basis serves people with and without personal interaction. A conditional-count likelihood ratio removes unknown personal offsets from the evidence calculation. The proposed mixture has an expected null excess-log-loss bound of 0.009 under the stated known-base model; its positive recovery remains an empirical question.

- [Review and evidence boundaries](REVIEW.md)
- [Mathematical construction, proof, and primary sources](METHOD_NOTE.md)
- [Executable next-agent prompt](NEXT_AGENT_PROMPT.md)
- [Machine-readable assignment](next_evidence_shrinkage_design.json)
- [Public review receipt](public_review_receipt.json)

Complete next-study budget: 12 shared fits, 64 adaptation batches, 1,664 person-solves, 76 optimizer records. No experiment is executed by this review. Coordinate through [issue #2](https://github.com/shulm/AI-Talmudic-Study/issues/2). Parallel source preparation, including PRs #14/#16, remains separate.
