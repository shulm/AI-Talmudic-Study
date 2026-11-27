# Uncapped single-history confirmation v1

**Final disposition: VERIFIED_COMPLETE / PRIMARY_FAILURE. Scientific qualification is false.**

All 82 worlds completed once. H1 returned **40 PASS / 42 FAIL / 0 UNRESOLVED**, versus the predeclared requirement of 72 passes. The observed operational success fraction is 40/82; the one-sided exact binomial p-value against reliability .80 is **0.99999999992784**, and the one-sided 95% Clopper–Pearson lower bound is **0.39242887100891427**. This does not establish reliability above .80. No subset, secondary endpoint or pooled mean replaces the failed primary test.

## H1 distributions across 82 independent worlds

These are descriptive distributions of the four primary point metrics, not additional significance tests. All 82 values and the numerical gate margins are retained in RESULT_STATUS.json and each world's SCORES.json.

| Metric | Mean | Sample SD | Minimum | q10 | Median | q90 | Maximum |
|---|---:|---:|---:|---:|---:|---:|---:|
| Active expected-NLL gain over B3 | .514928104 | .037582230 | .403937802 | .466517307 | .514752778 | .555961113 | .592939545 |
| Active oracle-gap recovery | .771076282 | .056577039 | .606335204 | .698649862 | .770068391 | .831698124 | .889285504 |
| Active contrast NRMSE | .502822336 | .048837969 | .395846788 | .442354026 | .505653701 | .564182110 | .655792522 |
| Inactive signed expected excess | .000361043 | .002277519 | -.000005588 | -.000000469 | 0 | .000062425 | .018628829 |

All 82 H1 worlds passed gain and recovery. **42 failed contrast; one also failed inactive excess.** U056 had inactive excess .018628829239286437 against .01, and contrast .5356250229558727 against .50. This fresh inactive-cohort failure is retained; a small across-world mean does not erase it or imply uniform null protection.

## Prespecified secondary findings and controls

H2 passed in 42/82 worlds, with 40 contrast failures and one inactive-excess failure. Its maximum inactive excess was .01208724553125129. Both histories passed in 25 worlds; H1/H2 disagreed in 32. The historical two-history aggregate passed in 39 worlds, **14 of which hid a failed individual history**. These summaries are descriptive and cannot rescue H1. Repeated histories are not independent worlds.

The following table reports the across-world mean paired expected-NLL difference, **control minus ES_UNCAPPED**, for H1. Positive values favor ES_UNCAPPED. All control rows, sampled-label metrics, donor comparisons, per-person signed/positive-part excess, linear-quantile tails, weight distributions and underflow diagnostics are retained in the public per-world scores; paired distributions and all-world values are in RESULT_STATUS.json.

| Control | Active expected-NLL difference | Inactive expected-NLL difference |
|---|---:|---:|
| B1 | .524388742 | .049247438 |
| B2 | .512963212 | -.005518404 |
| B3 | .514928104 | -.000361043 |
| M1 | -.066510960 | .047100425 |
| FIXED_MIX | -.032547078 | .037326956 |
| Original capped ES | .023846480 | -.000049341 |

Against B3, H1 ES_UNCAPPED's mean sampled-NLL improvement was .518031993 on active people; inactive sampled-NLL excess was .000288587. Its mean accuracy change was +.401352191 active and -.000141147 inactive; its Brier change was -.333448021 active and +.000176860 inactive. The uncapped rule improves active recovery relative to capped ES, but still sacrifices active predictive performance relative to raw M1 while substantially reducing M1's inactive loss. None of these descriptive tradeoffs changes qualification.

## Audit, numerical resolution and resource accounting

- Exactly **246 shared fits**, **656 wrappers**, **7,872 B3 + 23,616 M1 = 31,488 personal solves**; no retries, replacement worlds or unreached scientific identities.
- Exactly **2,788 probability arrays** and **328 stable uncapped log-probability arrays**, with complete parameter/evidence/view/bound inventories.
- All **32,229 frozen verifier groups** passed. All **2,271 historical blobs** were preserved. Probability replay uses absolute tolerance 1e-12; scalar replay uses 1e-10. A group count is not a count of independent scientific observations.
- The separately labeled post-execution DELIVERY_AUDIT.json passed **31,817 receipt/inference checks**. It explicitly reconciles source/input/model/penalty/initialization fields and independently reproduces the declared binomial tail with rational arithmetic and the lower confidence bound by tail inversion. This read-only supplement changes no scientific result, criterion or frozen source.
- Maximum independently evaluated personal residual R: **9.993369594871414e-11**. Maximum R_used: **1.0612508782238304e-10**. The stopping target applies to R; the prescribed allowance-adjusted R_used is correctly larger and is used only in downstream bounds. There were **2,327** declared guarded full-step acceptances.
- Final accounted command usage: **1,856.0625 sampled CPU seconds**, **2,350.768 profiled wall seconds**, **158,326,784 bytes sampled peak process-tree RSS**, nine completed required commands, no failed required commands or unmatched command starts. Deliberately failing preflight mocks are preserved separately and are included within preflight accounting, not counted as scientific retries.

The resource ceiling was 3,600 accounted CPU seconds and 4 GiB sampled process-tree RSS. Sampling was every 20 ms with one numerical thread. Startup/exit CPU, short-lived children, transient peaks, supervisor/editor/Git/network and final metadata overhead are not comprehensively measured; this is not an exact process-lifetime bound. Internal fit CPU is not added again to process totals. See RESOURCE_USAGE_FINAL.json and the command receipts.

Frozen implementation: **46b33884885f59a830c8a511091c39e9dcf51f0d**. Assignment: **ae74b9e5604b4905804d25b296097467f6794f14**. Shared objective/evidence/generator source: **f18255c5fad37f704881ff1f9ad50cd113497236**; personal solver source: **16ef28b105ff6c28ee3f822b1409f076fa895318**. Each new trained model is identified by its world's sealed models.npz SHA-256, collected in DELIVERY_AUDIT.json. Python 3.12.4, NumPy 2.1.3, SciPy 1.15.1 and psutil 7.2.2 were used. The final delivery commit is posted in issue #2 and draft PR #32.

Outcome: **PRIMARY_FAILURE**. Final qualification and cumulative resources are in DELIVERY_TERMINAL.json and RESOURCE_USAGE_FINAL.json, emitted after this reporting command completes.

Primary inference: {"n": 82, "successes": 40, "failures": 42, "unresolved": 0, "p_exact": 0.99999999992784, "one_sided_95_lower": 0.39242887100891427, "count_pass": false, "all_H1_resolved": true, "statistical_and_resolution_pass": false}. H1 alone is primary. H2, aggregate histories and controls cannot rescue it. All four metric distributions and all-world values are in RESULT_STATUS.json; per-world SCORES.json contains all controls, donor, sampled metrics, inactive tails and evidence/weight diagnostics.

Assignment ae74b9e5604b4905804d25b296097467f6794f14; pre-fit 46b33884885f59a830c8a511091c39e9dcf51f0d. Models are identified by each world's sealed archive hashes. Final commit is posted/read back in issue #2 and the draft PR.

Numerical enclosures condition on saved shared models, weights/evidence and computed oracle references. They are not directed-rounding certificates, sampling intervals or shared global-optimum certificates. The exact binomial calculation concerns operational world reliability under the declared balanced-history generator, not individual people or arbitrary text histories.

Historical PR20 remains INCOMPLETE / NUMERICALLY_UNRESOLVED. PR27 remains a post hoc diagnostic; E/101 remains a failure. No historical refit, human/text evaluation, downloads, paid calls, PR18 execution, corpus changes or merge.
