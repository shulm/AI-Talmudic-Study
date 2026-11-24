# Executed agent report — pilot_v1

Status: **VALID_PILOT_POSITIVE_PRIMARY**. P0–P3 executed. **Scientific interpretation: no numerically resolvable interaction gain.** The formal sign-only status is preserved, but its positive interval is many orders below optimizer tolerance and must not be reported as substantive success. Freeze: `4de12a1fb300a7c9e9d927591bc4b101f0e263a2`; execution PR https://github.com/shulm/AI-Talmudic-Study/pull/4; coordination https://github.com/shulm/AI-Talmudic-Study/issues/2. The final reporting commit is linked in the issue/PR because it cannot self-embed.

## Measured result

Primary selected baseline B3, k=16: baseline minus M1 macro-person NLL **1.91459137553e-12**, paired two-way 95% interval **[1.655029168969052e-13, 3.804900589608094e-12]**. There are 22 independent held-out people, 55 held-out input groups and 76 query items per person. Three support draws are averaged at the cell-loss level; three training seeds form the M1 probability ensemble. Neither adds independent human observations. Bootstrap: 2,000 valid resamples, 0 rejected.

| Model | NLL | Accuracy | Multiclass Brier |
|---|---:|---:|---:|
| B0 | 0.782941436 | 0.675837 | 0.483413 |
| B1 | 0.726286859 | 0.648525 | 0.453094 |
| B2 | 0.772511973 | 0.675837 | 0.474703 |
| B3 | 0.720448538 | 0.658692 | 0.444266 |
| B4 | 0.728098487 | 0.661882 | 0.447894 |
| M1 | 0.720448538 | 0.658692 | 0.444266 |

M1's basis norms across seeds are [6.598532669670373e-05, 1.4454418664283208e-05, 3.255720181727323e-05]. Its interaction effectively collapses under the declared regularization and its predictions match the personal-intercept B3 baseline to numerical precision. Tiny signed differences are optimizer-scale artifacts, not evidence of a distinct reasoning mechanism. The original grid and all results are preserved; no test-directed refitting occurred.

History controls (shuffled NLL minus true NLL; positive favors correct history):

```json
[
  {
    "model": "B3",
    "true_nll": 0.7204485381213804,
    "shuffled_nll": 0.8145900346846182,
    "true_history_advantage": 0.09414149656323786
  },
  {
    "model": "B4",
    "true_nll": 0.7280984870479158,
    "shuffled_nll": 0.7889511547774672,
    "true_history_advantage": 0.060852667729551495
  },
  {
    "model": "M1",
    "true_nll": 0.7204485381194657,
    "shuffled_nll": 0.8145900346844069,
    "true_history_advantage": 0.09414149656494109
  }
]
```

M1/B3 improve NLL over B2 by 0.0520634 (paired interval 0.0140724 to 0.0986192), and improve Brier, but accuracy declines from 0.675837 to 0.658692. The largest absolute M1–B3 probability difference is 6.00721694610229e-11. The B2/B3/M1 contrasts, seed diagnostics, support curves, evaluator-only disagreement subset, and anonymous per-person distributions are retained in test_results.json. A personalization improvement over B2 and an interaction improvement over B3 are separate claims.

## Provenance and execution

DICES revision `b5596d9edd585361967991a591abc7b11fb1f7a3`, MiniLM revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Source hashes, weight hashes, actual schema and exclusion policy are in the manifests. Measured source: 123 people/350 items/43,050 rows; after author-listed quality exclusions: 104/350/36,400. Input-only duplicate/context grouping: 271 groups. Train/development/test people 62/20/22; groups 162/54/55; items 207/67/76. Source class mapping: No=0, Unsure=1, Yes=2 (unsafe). All 33,998 input tokens covered by 369 windows.

30 human shared fits, four synthetic shared fits across two validation executions; human adaptation counts in RESOURCE_USAGE.json. Selected settings: {"B0": null, "B2": 0.01, "B1": 4, "B3": 0.1, "B4": [8, 4], "M1": {"rank": 2, "l2": 0.1}}. Checks include independent partitions, nested supports, strict input allowlist, missing-vs-uncertain mapping, all-model probability checks and person-renaming invariance, synthetic shared/exception rules and ambiguous supports, numerical gradient checks, and grouped bootstrap checks.

Commands actually executed and exit statuses are in command_log.json; initial acquire and prepare succeeded without process profiling. No dependency installation, paid calls, encoder fine-tuning, or source-index rebuild. Download payload: 122724436 bytes. Sampled measured CPU: 105.750 seconds; summed profiled wall time 156.651 seconds; sampled peak RSS 582651904 bytes. Small setup/documentation commands and network transport overhead are unprofiled, so these are explicitly not exact end-to-end resource totals.

## Failures and limits

The first encoder attempt failed on an unavailable tokenizer API; fixed before fitting. An inspection command failed on a NumPy norm argument. A development-control filename collision overwrote detailed grid optimizer logs; the complete selection table was recovered from independently persisted DEV_RESULTS.md, with model hashes unchanged. A console check before the collision observed all 30 shared fits and 1,800 person adaptations converged; individual iteration records are unavailable. The initial freeze command failed on this collision; corrected before test exposure. No extra shared fits were used to conceal the lost records. Final evaluation optimization records are preserved.

This is one fixed split, one safety-rating domain, one small frozen representation, and a narrow predeclared penalty range. Identical contexts are grouped, but semantic near-duplicate families remain unverified. Author quality exclusions were adopted rather than independently reconstructed. Full token coverage does not prove preservation of decisive conditions. Bootstrap intervals are descriptive conditional on this dataset, split, and selected fitted models. Per-cell probabilities and histories remain local; public hashes support local verification and regeneration rather than a hosted public prediction download.

## Concrete next task

Review this exact freeze and result, including gradient/penalty conventions and the near-zero interaction. If pursuing interaction learning, freeze a separately versioned experiment testing weaker basis regularization or a differently normalized basis on a new split or independent dataset. This test is now exposed and must not be called fresh confirmation. Do not expand the current run. TID-8 and MultiPref audits are documentation-only; their terms/coverage and separate ordinal or candidate-aware protocols remain prerequisites. P4/P5 were not started.
