# Independent post-evaluation audit

Independent AI reviewer: methods_review, 2026-11-24. **PASS.** Recomputed saved-result arithmetic without fitting, tuning, generating predictions, rerunning the final scorer, or changing signed files. Test target labels were first opened by this reviewer for this authorized post-evaluation audit.

All frozen-file, signed-review, split-artifact and prediction-artifact SHA256 hashes match. Freeze-manifest content equals the committed manifest in `430c0ec4e74db8c265e77e1eb028b21abe6bff43`. Its working file uses CRLF and Git blob uses LF; parsed content is identical. An initial exact-byte comparison stopped on this newline difference before labels were opened; the content-aware comparison resolved it without changing artifacts.

Verified 102 distinct people, each with ten decisions in one target family (1,020 choices). All 20,400 full probability rows cover five models and four budgets without duplicate prediction keys. Vectors are finite, valid, sum to one, and match saved arrays. Profile predictions equal the three-seed probability mean; donor predictions equal the five-assignment probability mixture.

Independently recomputed complete-alternative NLL, two-class Brier, accuracy and all calibration bins at every model/budget. Recomputed all sixteen paired contrasts and 2,000-draw percentile intervals using seed 20261124, independently of model scoring functions. Agreement is within 1e-12. Trial losses average within each participant; participants receive equal weight. Paired resampling preserves participant clusters and fixed donor predictions.

Donor IDs exactly match the declared hash procedure: five distinct validation-pool people per test participant, none from the test cohort. Outcome labels, target IDs and prediction axes align. No extra hypotheses, alternative intervals or performance-driven corrections were introduced.

| Primary-budget contrast: comparator NLL minus own profile | Estimate | 95% interval |
|---|---:|---:|
| Population | 0.11127584 | [0.08583043, 0.13595034] |
| Matched-donor mixture | -0.00757304 | [-0.02979985, 0.01356818] |
| Source summary | 0.06491699 | [0.04330426, 0.08627301] |

**Inconclusive** follows the declared rule: improvement over population does not establish own-history specificity over matched donors. Improvement over summary cannot substitute for the second co-primary criterion. Do not claim positive individual signal or demonstrated practical benefit.

The result records one final evaluation and the scorer has an overwrite guard. This is arithmetic verification of that saved evaluation, not a new model evaluation. Hashes establish consistency, not proof that unrecorded external runs are impossible; no evidence of another final run was found in the reviewed workflow/artifacts. Fixed-position confounding, retrospective task access, approximate posteriors and conditional uncertainty for one target family remain limitations.
