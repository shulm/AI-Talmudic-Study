# Evidence review of short-history v1

The canonical head recovers strong planted interaction at sixteen well-covered observations but fails null control on both C and D. This remains COMPLETED_PRIMARY_FAILURE. Numerical correctness does not establish predictive usefulness or human generalization.

Exact base and PR15 final: ee2b0a5a2f0916fed3dd59f720b902eb332eecc3. PR13 assignment: 47b19560350aa8c5d877d99f381d5b27f5b3490a. PR12: 40d201997ab8d79d138734b1ef116c161719c11b. PR8: 165bd826f02c91894dc9806d5e49af119eb230a5. The current remote branch heads and issue2 were inspected before creating this isolated branch; no overlapping null-control branch was present. Corpus production remains separate.

| Primary k16 measure | C | D | Original requirement |
|---|---:|---:|---|
| B3 minus M1 expected NLL | .594196396265 | .602815011497 | >=.05 |
| Oracle-gap recovery | .863611274630 | .877918026354 | >=.50 |
| Contrast NRMSE | .283460783779 | .248433285313 | <=.50 |
| M1 minus B3 null NLL | .052185645516 | .057411041409 | <=.01 |

All four gates were required separately on each realization, together with exact complete audit and numerical checks. Both null gates fail. Secondary rho=.06/lambda=.6 gives .009586986743 and .010921452829: not qualification across both. Both penalties changed, so the historical contrast cannot attribute improvement to one penalty. C secondary schedule211 fails its descriptive null gate. D96 null harm .012138861736 exceeds .01. PR12's own A/B qualification remains valid for its declared setting; it was never a universal guarantee.

## Checks personally executed in this assignment

The original private arrays were available. The unchanged PR15 verifier was executed against them with a fresh copied public evidence directory, excluding the old verification receipt. It returned VERIFIED_COMPLETE, qualification=false, numerical_pass=true, 17,038 comparisons, maximum discrepancy 3.552713678800501e-14. Hashes before and after were identical. No generator or optimizer was called by this replay. See HISTORICAL_REPLAY.json for exact receipt identity and compact outcome. This is a new execution of the historical verifier, not a newly authored independent scientific validator.

The public audit script in this package checks report/summary values, exact gate conjunctions, source hashes, ledger counts, structured-score identity and PR15 source/commit identity. It distinguishes these checks from the executor's historical claims. See PUBLIC_EVIDENCE_AUDIT.json.

Historical resource reports give 12 shared fits,184 adaptation batches,3,776 personal solves,196 records; accounted CPU79.171875 seconds and peak sampled RSS90,120,192 bytes. Two failed prefit engineering checks are disclosed in that report; they are not scientific retries. We do not reinterpret sampling as complete machine accounting.

## Earlier evidence and exposure

DICES M1 differed from B3 by approximately1.9e-12, so history calibration did not establish interaction benefit. PR5's joint criteria were not met. PR8's exposed follow-up found item-frequency minus own loss -.071577, single-donor minus own .003012 with interval spanning zero, and donor-mixture minus own -.007573. A probability mixture and mean donor loss differ because log loss is nonlinear. Its prospective eight-support human protocol remains unexecuted and separate.

All A-D, DICES and SRO results are exposed. They motivate this design but cannot provide its fresh confirmation. The supplied Individual_Decision_Research_Plan_2026-11-25.docx was read as a proposed direction. Its later text, human, adaptive-question and scholarly studies are not part of the present execution scope.

