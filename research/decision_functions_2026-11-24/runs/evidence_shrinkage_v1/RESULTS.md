# evidence_shrinkage_v1 results

**INCOMPLETE / NUMERICALLY_UNRESOLVED**. Overall qualification: false. All prescribed optimization finished, but the frozen numerical validity gate failed on H.

One fixed conditional-evidence mixture, four mixed populations, two16-observation histories. No parameter selection or scientific retry.

| Realization | Active gain | Recovery | Contrast NRMSE | Inactive degradation | ES passes all gates |
|---|---:|---:|---:|---:|---|
| E | 0.507506519859 | 0.761034056737 | 0.555275891653 | 9.2423361996e-06 | False |
| F | 0.502356548102 | 0.752794678083 | 0.564899178641 | -0 | False |
| G | 0.519710033767 | 0.778996613658 | 0.534684507943 | -0 | False |
| H | 0.514874691633 | 0.770563481246 | 0.556166870719 | -0 | False |

Complete per-history/aggregate comparator and seed metrics, per-person losses, evidence/weight distributions, bootstrap intervals and numerical checks are in the realization JSON files. Losses and squared contrast errors are averaged across histories; probabilities are not pooled. No control or pooled result rescues an ES failure.

Execution: {'attempted_optimizer_records': 76, 'completed_optimizer_records': 76, 'shared_fits': 12, 'adaptation_batches': 64, 'person_solves': 1664, 'scientific_retries': 0}. The frozen verifier terminated because scientific_summary.json was not published on the numerical-stop path. A post-run observer retained1158 of1160 reached checks, maximum discrepancy2.842170943040401e-14, and unchanged hashes of all112 private artifacts. This is not VERIFIED_COMPLETE. The final qualification/resource-contract comparisons were not reached; the separate delivery inventory above is not a replacement for them.

Forward replay independently implements prediction matrix multiplication and a dense two-count DP, checking full optimizer slices, priors and mixtures. Metric replay uses a different loss reduction and multiplicity-weighted bootstrap; report schema, gates and much contrast logic are shared and are not an entirely independent statistical implementation.

The .009 theorem bounds expected positive inactive excess loss over possible support responses under the correct known-base, fixed-label, independent-response model. It does not guarantee an observed cohort below .009 or .01 and does not guarantee active recovery. Both empirical point gates and theory checks are reported separately. Bootstrap intervals condition on the fitted heads and fixed histories; they exclude retraining and domain uncertainty.

Resource accounting: {'cpu_seconds_sampled': 42.140625, 'peak_rss_bytes_sampled': 101486592, 'wall_seconds_profiled': 56.889999999664724, 'commands': 5, 'failed_commands': 2, 'independent_review_cpu_seconds': 0.265625, 'limitations': 'CPU/RSS polled at .05 seconds; startup/exit sampling loss, supervisor, Git, reporting, and interactive orchestration overhead not comprehensively profiled. Reviewer toy CPU measured after imports. No paid calls or dataset/model downloads.', 'accounted_cpu_subtotal': 42.40625}.

Preserve DICES/SRO exposure, v1 null failure, v2 bounded96-support qualification, and short-history primary failure. PR18 remains a distinct planning package; its CLI and seed banks were not used. Corpus production/review PR14/16 remain separate. Stop for review; do not retune E/F/G/H or merge.

## Preserved stopping condition and interpretation

H schedule101 batch7 versus batch48 exceeded the fixed probability tolerance: M1 seed11 difference1.2232536670264693e-6, seed29 1.2232044063198444e-6, seed47 1.2232421133795413e-6; ensemble1.223233395575285e-6 and ES1.100854312485744e-6. The limit was1e-6. Maximum expected-NLL difference3.1479469031481244e-7 was below1e-5, but both conditions were required. E/F/G numerical checks passed. The H maximum exceeds tolerance by2.232536670264693e-7. No tolerance was changed and no solve was retried.

All76 optimizers reported success, while numerical batch invariance failed. These are different states. The failure occurred after the final realization artifacts were saved. No missing scientific summary was manufactured, no scientific source changed, and the completed fit budget is not a complete verification pass. The captured replay invokes the unchanged frozen verifier and preserves its exception; the observer command succeeds only at recording that failure.

ES retains large active loss gains and small observed inactive loss, but its contrast NRMSE fails .5 on every realization and every history. M1 retains stronger contrast but fails inactive loss on all four; the fixed90% mixture also fails inactive loss. These observations show the declared tradeoff in these saved arrays, not a unique mechanism or a qualified method.

| Realization | M1 contrast | M1 inactive loss | Fixed mixture contrast | Fixed mixture inactive loss |
|---|---:|---:|---:|---:|
| E | 0.408206012498 | 0.0452073652682 | 0.513978812665 | 0.0359906923371 |
| F | 0.39439629244 | 0.0361430446244 | 0.504310330688 | 0.028792826539 |
| G | 0.381240603293 | 0.0470105642687 | 0.494657196309 | 0.0374407885955 |
| H | 0.403815515927 | 0.035267856933 | 0.511815407925 | 0.028144268789 |

Inactive weights are exactly zero on both histories for F/G/H. E has one nonzero inactive weight per history (max .0333737221/.0307635047). Active mean weights range .7895â€“.8746 across the eight histories; many hit .9. These are prediction weights, not calibrated activity probabilities. Full all-person values, quantiles, counts, seed evidence and history disagreements are saved. The inactive donor expected pair contrast is structurally zero under identical-offset inactive pairs.

Sampled-label ES active accuracy is .783565/.798032/.785880/.797454 for E/F/G/H, versus B3 .355324/.405093/.368056/.361111. The detailed JSON includes sampled NLL, Brier, seed diagnostics, per-person excess and positive-part inactive excess. Bootstrap active gain intervals are [.460626,.545135], [.454321,.544531], [.483979,.554425], [.485441,.543290]. Inactive loss intervals are [0,.0000224992] for E and [0,0] for F/G/H; these conditional zero intervals reflect exact observed fallback and are not universal null guarantees. ES loses .0335565/.0519937/.0373541/.0348644 active expected NLL versus FIXED_MIX while improving inactive expected loss; all paired interval endpoints are in each bootstrap JSON.

## Exact provenance and resources

Assignment724be8c49808e1e1b8643d81c73267f7577439c8; pre-fit38dfff076b90d7c08387a06bd25f3cc75f15f6ae. NumPy2.1.3, SciPy1.15.1, Python3.12.4; single-thread BLAS. No external pretrained model revision exists. Shared model NPZ SHA-256 values:
- E: `a25b9f03a248160af4f889176f94327b63c1d1e125fa1d57014144f808e483c1`
- F: `7667eb564a04ace3f9aff78ef867d344c10e08daee56826a679a0060599323c8`
- G: `0682535b6f83d067c67558b036abc2edf121bb3a2292e3e71690cf1e7375d931`
- H: `9b2f96034d032deb508b0e769a2c80a05d586cfdac41aa29dcffa78fa47f0624`

965 historical blobs and18 frozen source/protocol files are unchanged. Exact12 ledgers,76 successful optimizer records,1664 personal solves,36 archive roles and176 query arrays are present. Maximum optimizer gradient2.9634130522008736e-07; maximum person-scaled residual2.8448765301128387e-05. Stationarity values are separate from optimizer success and failed batch validity.

Final measured accounting: 43.46875 CPU seconds; 101486592 bytes peak sampled RSS. See RESOURCE_USAGE_FINAL.json, including successful and failed command receipts and .265625 reviewer CPU seconds. Two failed post-fit commands are the mandated numerical stop and complete verifier rejection; no pre-fit command failed and no scientific attempt was repeated. Sampling and unprofiled overhead are disclosed.

Next review: retain this incomplete run and all empirical failures. A new numerical-stationarity/batch investigation and any conditional-evidence power study require separately frozen assignments; do not change this code or retune these exposed seeds. The proposal-only text specification remains blocked on numerical validity and the known-base/null-model transport question.
