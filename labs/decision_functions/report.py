"""Publish compact interpretation and handoff from already frozen evaluation."""
import subprocess
import numpy as np
from common import *
from freeze import resources

def main():
    r=read(OUT/'test_results.json'); usage=resources(); enc=read(OUT/'encoder_manifest.json')
    selected=read(OUT/'development_results.json')['selected']
    curve={x['model']:x for x in r['support_curve'] if x['k']==16}
    norms=np.sqrt((np.load(PRIVATE/'selected_models.npz')['vs']**2).sum(axis=(1,2,3))).tolist()
    summary={k:r[k] for k in ['status','freeze_commit','people','items','groups','primary_baseline','primary','contrasts','history_controls','seed_diagnostics']}
    summary.update(source_revision=REV,encoder_revision=enc['revision'],primary_support=16,selected=selected,k16_results=curve,basis_norms=norms,probability_artifacts=r['artifacts'],claim='Fixed-split pilot on new people and held-out input groups, not new verified semantic topics or recovered reasoning mechanisms')
    write(OUT/'results_summary.json',summary)
    delta=r['primary']['delta']; interval=r['primary']['interval95']
    rows='\n'.join(f"| {name} | {x['nll']:.9f} | {x['accuracy']:.6f} | {x['brier']:.6f} |" for name,x in curve.items())
    text=f'''# Executed agent report — pilot_v1

Status: **{r['status']}**. P0–P3 executed. Freeze: `{r['freeze_commit']}`; execution PR https://github.com/shulm/AI-Talmudic-Study/pull/4; coordination https://github.com/shulm/AI-Talmudic-Study/issues/2. The final reporting commit is linked in the issue/PR because it cannot self-embed.

## Measured result

Primary selected baseline {r['primary_baseline']}, k=16: baseline minus M1 macro-person NLL **{delta:.12g}**, paired two-way 95% interval **{interval}**. There are {r['people']} independent held-out people, {r['groups']} held-out input groups and {r['items']} query items per person. Three support draws are averaged at the cell-loss level; three training seeds form the M1 probability ensemble. Neither adds independent human observations. Bootstrap: 2,000 valid resamples, {r['primary']['rejected']} rejected.

| Model | NLL | Accuracy | Multiclass Brier |
|---|---:|---:|---:|
{rows}

M1's basis norms across seeds are {norms}. Its interaction effectively collapses under the declared regularization and its predictions match the personal-intercept B3 baseline to numerical precision. Tiny signed differences are optimizer-scale artifacts, not evidence of a distinct reasoning mechanism. The original grid and all results are preserved; no test-directed refitting occurred.

History controls (shuffled NLL minus true NLL; positive favors correct history):

```json
{json.dumps(r['history_controls'],indent=2)}
```

The B2/B3/M1 contrasts, seed diagnostics, support curves, evaluator-only disagreement subset, and anonymous per-person distributions are retained in test_results.json. A personalization improvement over B2 and an interaction improvement over B3 are separate claims.

## Provenance and execution

DICES revision `{REV}`, MiniLM revision `{enc['revision']}`. Source hashes, weight hashes, actual schema and exclusion policy are in the manifests. Measured source: 123 people/350 items/43,050 rows; after author-listed quality exclusions: 104/350/36,400. Input-only duplicate/context grouping: 271 groups. Train/development/test people 62/20/22; groups 162/54/55; items 207/67/76. Source class mapping: No=0, Unsure=1, Yes=2 (unsafe). All 33,998 input tokens covered by 369 windows.

30 human shared fits, four synthetic shared fits across two validation executions; human adaptation counts in RESOURCE_USAGE.json. Selected settings: {json.dumps(selected)}. Checks include independent partitions, nested supports, strict input allowlist, missing-vs-uncertain mapping, all-model probability checks and person-renaming invariance, synthetic shared/exception rules and ambiguous supports, numerical gradient checks, and grouped bootstrap checks.

Commands actually executed and exit statuses are in command_log.json; initial acquire and prepare succeeded without process profiling. No dependency installation, paid calls, encoder fine-tuning, or source-index rebuild. Download payload: {usage['downloaded_dataset_and_weight_payload_bytes']} bytes. Sampled measured CPU: {usage['measured_cpu_seconds']:.3f} seconds; summed profiled wall time {usage['measured_wall_seconds']:.3f} seconds; sampled peak RSS {usage['sampled_peak_rss_bytes']} bytes. Small setup/documentation commands and network transport overhead are unprofiled, so these are explicitly not exact end-to-end resource totals.

## Failures and limits

The first encoder attempt failed on an unavailable tokenizer API; fixed before fitting. An inspection command failed on a NumPy norm argument. A development-control filename collision overwrote detailed grid optimizer logs; the complete selection table was recovered from independently persisted DEV_RESULTS.md, with model hashes unchanged. A console check before the collision observed all 30 shared fits and 1,800 person adaptations converged; individual iteration records are unavailable. The initial freeze command failed on this collision; corrected before test exposure. No extra shared fits were used to conceal the lost records. Final evaluation optimization records are preserved.

This is one fixed split, one safety-rating domain, one small frozen representation, and a narrow predeclared penalty range. Identical contexts are grouped, but semantic near-duplicate families remain unverified. Author quality exclusions were adopted rather than independently reconstructed. Full token coverage does not prove preservation of decisive conditions. Bootstrap intervals are descriptive conditional on this dataset, split, and selected fitted models. Per-cell probabilities and histories remain local; public hashes support local verification and regeneration rather than a hosted public prediction download.

## Concrete next task

Review this exact freeze and result, including gradient/penalty conventions and the near-zero interaction. If pursuing interaction learning, freeze a separately versioned experiment testing weaker basis regularization or a differently normalized basis on a new split or independent dataset. This test is now exposed and must not be called fresh confirmation. Do not expand the current run. TID-8 and MultiPref audits are documentation-only; their terms/coverage and separate ordinal or candidate-aware protocols remain prerequisites. P4/P5 were not started.
'''
    (OUT/'AGENT_REPORT.md').write_text(text,encoding='utf-8')
    (OUT/'NEXT_HANDOFF.md').write_text('# Concrete handoff\n\nRead AGENT_REPORT.md, results_summary.json and the exact external freeze SHA before changes. Review PR #4 and issue #2. The experiment is complete; no model tuning remains authorized within pilot_v1. All test outcomes are exposed. Preserve the local cache at '+str(PRIVATE)+'; it contains immutable source files, split/support memberships, frozen vectors/weights, raw probability arrays and paired losses. Public manifests record hashes.\n\nReview priority: verify source grouping and new-person support boundaries, loss normalization and collapsed interaction, paired two-way bootstrap, and the disclosed development optimizer-log loss. No rerun is needed to obtain a favorable result. Future interaction/representation experiments need a new frozen protocol and explicit test-reuse disclosure. Source indexes and repository visibility are unchanged.\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
