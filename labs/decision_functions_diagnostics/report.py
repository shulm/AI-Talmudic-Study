"""Derive final aggregate report from immutable diagnostic receipts, no fitting."""
from core import *

def markdown(name,text):
    path=OUT/name
    with path.open('x',encoding='utf-8',newline='\n') as stream: stream.write(text)

def main():
    replay=read(OUT/'replay_receipt.json'); syn=read(OUT/'synthetic_results.json'); human=read(OUT/'human_certificate.json'); checks=read(OUT/'engineering_checks.json'); audit=read(OUT/'audit_validation.json'); verify=read(OUT/'diagnostic_verification.json')
    commands=[read(p) for p in sorted((OUT/'commands').glob('*.json'))]
    records=[read(p) for p in (OUT/'records').glob('*/*.complete.json')]
    resources=dict(profiled_cpu_seconds=sum(c['cpu_seconds_sampled'] for c in commands),profiled_wall_seconds=sum(c['wall_seconds'] for c in commands),sampled_peak_rss_bytes=max(c['peak_rss_bytes_sampled'] for c in commands),optimizer_cpu_seconds=sum(r['cpu_seconds'] for r in records),optimizer_wall_seconds=sum(r['wall_seconds'] for r in records),synthetic_shared_fits=24,synthetic_person_solves=1952,human_training_intercept_batches=3,human_training_intercept_person_solves=186,human_B2_M1_fits=0,new_human_heldout_predictions=0,retries=0,dataset_weight_download_bytes=0,paid_calls=0,dependency_installs=0,command_count=len(commands),command_failures=[c for c in commands if c['exit_status']!=0],sampling_interval_seconds=.05,limits=dict(cpu_seconds=3600,memory_bytes=4294967296,synthetic_shared_fits=24,synthetic_person_solves=4096,human_training_intercept_person_solves=186),measurement_limits='Child-process CPU/RSS sampled every 0.05 seconds; last sampling interval may be missed. Git, report generation, small inspection commands and documentation HTTP transfer were not process-profiled. Dataset/weight downloads are zero; documentation/metadata transfer is excluded, not asserted zero.',hardware=environment())
    assert resources['profiled_cpu_seconds']<3600 and resources['sampled_peak_rss_bytes']<4294967296
    atomic(OUT/'RESOURCE_USAGE.json',resources)
    source=dict(status='DOCUMENTATION_ONLY',sources=[dict(name='TID-8 CommitmentBank',revision='e12b715be7582af64efc596f8402d916fb64f1e3',url='https://huggingface.co/datasets/MichiganNLP/TID-8/blob/e12b715be7582af64efc596f8402d916fb64f1e3/README.md',readme_sha256='0275ef5ec8cd2918f6a37f5d170409375d9f5e6693d309bee835d44cad74347b',readme_bytes=22576,license='unknown in card',outcome_index_to_value=[0,1,2,3,-3,-1,-2]),dict(name='Original CommitmentBank',revision='14ea91f56e3575b011d28fca5c37a1f5e92769b7',url='https://github.com/mcdm/CommitmentBank/tree/14ea91f56e3575b011d28fca5c37a1f5e92769b7',readme_sha256='9d523fae31e072aaf5bcff4f893894819a32ce6e16094e5aa86a1ac41df52c18',license_status='GitHub license endpoint HTTP404; README does not resolve terms; no inference of prohibition')],access='Primary documentation fetched successfully with requests after web-renderer access errors; no corpus acquisition',remaining=['constituent/distribution terms','identity scope and availability','cross-track overlap audit','k=16 support feasibility','seven-class likelihood/encoder specification before any human fitting'])
    atomic(OUT/'candidate_source_audit.json',source)
    exposure=dict(DICES=dict(final=FINAL,source='b5596d9edd585361967991a591abc7b11fb1f7a3',status='EXPOSED',test_people=22,test_groups=55,test_items=76),SRO=dict(delivery='6ca2dedc547144d7279696bd5322c1e39c7f03d3',source='4e6e837fb5aaca87ed5914fd9be251156f43eec9',release='Complete_02-16-2019',task='Kirby to Holt-Laury',status='EXPOSED; metadata/handoff only reviewed here',test_people=102,test_events=1020),Cross_Psych_101=dict(source='532794c51e046a0ddaf560e7972789688d46bf63',status='REJECTED on parallel track; not an available confirmation fallback'),scholarly=dict(status='Separate PROVISIONAL_PENDING_REVIEW track',families=30,attempted_occurrences=32,usable_focal_cases=24,human_expert_validation=False,new_work_here=False),TID8=dict(status='DOCUMENTATION_ONLY; freshness and terms not yet established'))
    atomic(OUT/'exposure_ledger.json',exposure)
    pos=next(r for r in syn['results'] if r['regime']=='positive' and r['lambda_']==.001 and r['condition']=='informative')
    null=next(r for r in syn['results'] if r['regime']=='null' and r['lambda_']==.001 and r['condition']=='informative')
    summary=dict(assignment='D0-D4 complete; stop at proposal',synthetic_protocol_commit='5fc8cf48394b4e620a75be8e8f92054a6c02a451',cache=replay['cache'],replay=replay['status'],max_replay_error=replay['max_arithmetic_error'],audit=audit['actual_ledgers'],engineering=checks['status'],positive_recovery={k:pos[k] for k in ['expected_gain','oracle_gap_recovery','contrast_normalized_rmse']},synthetic_status=syn['status'],synthetic_gates=syn['gates'],null_degradation=-null['expected_gain'],batch_max_probability_difference=max(r['max_first_person_difference'] for r in syn['batch_checks']),human_certificates=human['results'],diagnostic_arithmetic=verify['status'],human_confirmation='BLOCKED_BY_NULL_GATE_AND_DATA_ADMISSION',next_step='One separately frozen synthetic penalty-separation study; no human experiment launched')
    atomic(OUT/'results_summary.json',summary)
    rows='\n'.join(f"| {r['lambda']} | {r['spectral_norm']:.10g} | {r['threshold']:.10g} | {r['signed_margin']:.10g} | {r['error_bound']:.4g} | {r['status']} |" for r in human['results'])
    text=f'''# Interaction diagnostics v1 — executed report

**D0–D4 complete.** Original cache available; saved evidence replayed; audit failure paths fixed in separate tooling; informative synthetic interaction recovery demonstrated; full synthetic gate **failed on the null**; original DICES penalties favor zero interaction. No second human evaluation was run. Human confirmation remains blocked.

Branch `codex/interaction-diagnostics-v1`; draft PR https://github.com/shulm/AI-Talmudic-Study/pull/7; issue https://github.com/shulm/AI-Talmudic-Study/issues/2. Base review `ef580ec8c8b92c65179c5b0a5840c60a5cbfd612`. Synthetic protocol/code checkpoint **5fc8cf48394b4e620a75be8e8f92054a6c02a451** was pushed and posted before fitting. Final delivery SHA is recorded in the PR/issue, avoiding a self-referential commit hash.

## D0 — independently replayed existing arrays

The read-only verifier validated {replay['public_integrity_files']} frozen public integrity files, exact 171 prediction keys/shapes and 24 paired-loss keys/shapes, pinned private/source/archive hashes, normalization and finite probabilities. It replayed support-curve scores, disagreement-subset scores, per-person losses, training-seed diagnostics, shuffled-history point contrasts, and original 2,000-resample paired bootstrap intervals. Maximum arithmetic discrepancy: **{replay['max_arithmetic_error']}** at absolute tolerance 1e-12. Consumed private bytes had identical before/after hashes. Original M1–B3 maximum probability difference remains {replay['max_M1_B3_probability_difference']:.12g}.

This independently reproduces saved-array arithmetic. It does not regenerate predictions from weights, prove the historical execution used the reconstructed derangement schedule, restore lost optimizer logs, or establish scientific model correctness. It adds no new inferential claim about shuffled histories. The old sign-only positive status remains untouched; the scientific interpretation stays NO_RESOLVABLE_INTERACTION_GAIN. NLL/Brier improvement is **improved probabilistic prediction**, not specifically established calibration improvement.

## D1 — audit evidence fails closed

Expected stage/configuration/seed/batch identities are declared first. Separate start/completion records are atomically published and cannot overwrite one another. The ledger requires exact IDs, counts, mandatory optimizer fields, finite values and successful termination. Empty logs, missing configurations, interrupted runs, identity changes, incomplete numerical fields, nonconvergence and output collisions are rejected. Successful termination and stationarity residuals remain separate observations.

Measured ledgers: **104 synthetic records** (24 shared fits plus 80 adaptation batches, 1,952 person-solves) and **three human training-intercept records** (186 person-solves), all successful and complete. Original development remains RECOVERED_SELECTION_ONLY. New diagnostic solves never substitute for the missing original records. The versioned objective adapter matches frozen objective values and gradients on fixed toy inputs; finite-difference checks pass. No optimizer was invoked by those engineering checks.

## D2 — planted recovery and preserved null failure

Fixed generator: 96 people, 192 circular-feature cases/64 rotational groups; people 48/24/24 and groups 40/12/12. Training uses 48 people and 120 cases; test uses 24 new people and 36 new cases; support contains 96 training cases, with Gram eigenvalues {syn['support_gram_eigenvalues']}. Development was reserved and not scored. Matched pairs share nonzero offsets and have opposite interaction phases. Known shared logits scale 0.25, planted rank two scale 2.5, offset standard deviation 0.12; categorical seed 2718, generator seed 20261125, optimization seeds 11/29/47. No text encoder was used.

At the predeclared weak penalty 0.001, informative supports give:

- Oracle-expected NLL: B3 **{pos['expected_nll_B3']:.9f}**, M1 **{pos['expected_nll_M1']:.9f}**, oracle **{pos['expected_nll_oracle']:.9f}**.
- Gain **{pos['expected_gain']:.9f}**, oracle-gap recovery **{100*pos['oracle_gap_recovery']:.3f}%**, contrast normalized RMSE **{pos['contrast_normalized_rmse']:.6f}**: all positive-control gates pass.
- Realized NLL B3 {pos['B3']['nll']:.6f}, M1 {pos['M1']['nll']:.6f}; accuracy {pos['B3']['accuracy']:.6f} → {pos['M1']['accuracy']:.6f}; Brier {pos['B3']['brier']:.6f} → {pos['M1']['brier']:.6f}.
- Null expected-NLL degradation **{-null['expected_gain']:.9f}**, exceeding the predeclared maximum 0.01. **Do not round this into a pass.** Null contrast RMS is {null['predicted_contrast_rms']:.6f} although oracle contrast is zero.
- Uninformative supports produce zero interaction gain and contrast NRMSE 1, the expected identifiability failure.
- Maximum batch-size probability difference **{summary['batch_max_probability_difference']:.9g}**, below 1e-6. This tests a fixed person's adaptation alone, with seven people, and against the original 24-person batch.

Overall outcome: **BOUNDED_DIAGNOSTIC_FAILURE**, with informative-feature capability demonstrated. The known null and positive regimes must both pass before a human extension. All four penalties and all seeds are retained; no fixture replacement, penalty tuning, retries or extra fits occurred. The 0.001 setting has training spectral norm 0.0487941 versus threshold 0.000144338, supporting its predeclared signal-permitting rationale. This does not remove its measured null failure.

Expected matched-pair class-frequency discrepancy reaches {syn['frequency_balance']['positive']['expected_pair_max']:.6f} (sampled maximum {syn['frequency_balance']['positive']['sampled_pair_max']:.6f}); matching offsets does not imply exactly matched marginal class frequencies. The large B3 contrast and recovered question-dependent log-odds establish that frequency offsets alone cannot explain this positive control. The wording variants were materialized after fitting solely to inspect grouping; they neither supplied encoder features nor added label observations.

## D3 — original training objective favors zero interaction

Saved B2 and training center were fixed. Only the training block was used: S=62, N=207, d=384. Three new intercept batches, one per original penalty, produced:

| lambda | ||G||op | lambda/sqrt(S) | threshold minus norm | numerical bound | Conclusion |
|---:|---:|---:|---:|---:|---|
{rows}

The bound uses strong convexity of each regularized intercept problem and the softmax Jacobian bound: `||delta G||op <= ||Z||op ||r||F / (2 S sqrt(N) lambda)`, plus a conservative floating-point SVD allowance. These are numerical certificates, not interval-arithmetic proofs. The observed margins exceed these bounds comfortably. Largest human per-person intercept residual is about 1.94e-6; it is reported rather than described as exact convergence.

The training objective therefore explains zero interaction at all three original penalties. Increasing rank cannot defeat that penalty-induced optimum. This says nothing about generalization under weaker or separately normalized penalties. A subsequent independent source join reconstructed the 62×207 training-label matrix from the pinned raw CSV exactly. Its original standalone matrix hash was not historically pinned; the source-based equality check supplies the missing provenance link without refitting.

## Resources, failures and preservation

{resources['profiled_cpu_seconds']:.6f} sampled child CPU seconds; {resources['profiled_wall_seconds']:.6f} summed profiled wall seconds; peak sampled RSS {resources['sampled_peak_rss_bytes']} bytes. Exact optimizer process CPU sum {resources['optimizer_cpu_seconds']:.6f} seconds. All six profiled scientific/check commands exited zero. No installation, dataset/weight downloads, paid calls, human B2/M1 fits or new human held-out predictions. Git, reporting, small inspections and metadata HTTP requests are not included in process-profiled totals; sampling may omit the last 0.05-second interval.

Scientific failure: null gate exceeded by about 0.0019493 NLL. It is preserved as the main constraint on continuation. Documentation browser access failed for several primary URLs; direct read-only HTTP retrieval succeeded, and source identities/hashes are recorded. No run artifacts were overwritten. Additional post-run validation strengthened mandatory ledger-field checks and materialized wording/grouping artifacts; it did not change fitting or scoring code/results. Source hashes in receipts identify the exact working code, including those additions before their final commit.

The original frozen laboratory and pilot_v1 directory remain unchanged. Original source corpora, scholarly reports, repository visibility and PR #5's parallel branch are preserved. Exposure reconciliation in exposure_ledger.json treats DICES and SRO as exposed, Cross-Psych-101 as rejected on the parallel track, and its scholarly preparation as provisional. No independent re-audit of PR #5's calculations is claimed.

## D4 — next decision

The attached NEXT_PROTOCOL_PROPOSAL.md proposes one small synthetic study separating offset and interaction penalties, retaining both positive and null gates. It does not start that study. TID-8 CommitmentBank is the first conditional confirmation candidate, but its card lists an unknown license, constituent terms remain unresolved, and identity/overlap/support coverage have not been audited. No human acquisition or confirmation may follow automatically. Preserve the numerical-head result separately from any future representation or domain-transfer claim.

Evidence: replay_receipt.json, engineering_checks.json, audit_validation.json, synthetic_results.json, human_certificate.json, diagnostic_verification.json, records/, commands/, RESOURCE_USAGE.json, candidate_source_audit.json and exposure_ledger.json. Exact commands are in the laboratory README and command receipts.
'''
    markdown('DIAGNOSTIC_REPORT.md',text)
    markdown('NEXT_HANDOFF.md',f'''# Diagnostic handoff

D0–D4 are complete on `codex/interaction-diagnostics-v1`, PR #7. Read DIAGNOSTIC_REPORT.md and results_summary.json. Protocol checkpoint: 5fc8cf48394b4e620a75be8e8f92054a6c02a451. Final delivery SHA is in issue #2/PR #7.

Saved-array replay matches exactly. The numerical head recovers planted interaction, but weak-penalty null degradation 0.0119493 fails the 0.01 gate. All three original DICES penalties make zero interaction optimal under the training certificate. No new human held-out predictions or human shared fits occurred. Original missing development logs remain missing.

Stop here for review. The sole next proposal is separately frozen synthetic penalty separation with an explicit null gate; it is not executed. Human confirmation is blocked by that failure and TID-8 admission/terms. DICES and PR #5's SRO evaluation are exposed. Do not create a fresh-confirmation claim by resplitting either, overwrite historical arrays, or repeat scholarly corpus preparation.

Original private cache: C:/Users/David/.cache/decision_functions/pilot_v1 (read only). New private arrays and engineering fixture: C:/Users/David/.cache/decision_functions/interaction_diagnostics_v1. Public receipts contain hashes and exact commands. Replaying requires a new output checkout/directory because receipts and ledgers deliberately reject overwrites. No additional fit budget remains in diagnostics v1: all 24 synthetic shared fits and three human intercept batches have been used.
''')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
