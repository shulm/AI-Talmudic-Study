"""Reporting-only path: no fitting, generator, solver or prediction imports."""
from common import *
def resources(out):
    files=sorted((out/'commands').glob('*.complete.json'));rows=[read(p) for p in files]
    starts={p.name.split('.')[0] for p in (out/'commands').glob('*.start.json')};ends={p.name.split('.')[0] for p in files}
    return dict(cpu_seconds_sampled=sum(r['cpu_seconds_sampled'] for r in rows),wall_seconds=sum(r['wall_seconds'] for r in rows),peak_process_tree_rss_bytes_sampled=max([r['peak_process_tree_rss_bytes_sampled'] for r in rows]+[0]),completed_commands=len(rows),failed_commands=sum(r['reason'] is not None for r in rows),unmatched_commands=sorted(starts-ends),receipts={p.name:sha(p) for p in files},limits=dict(cpu_seconds=3600,rss_bytes=4*1024**3),limitations='20ms sampled process-tree accounting. Startup/exit CPU, short-lived children and transient RSS may be missed. Supervisor/editor/Git/network/final metadata overhead is not fully profiled; not an exact process-lifetime bound. Mock-child totals are included within outer preflight and not double counted.')
def report(out,receipt,recovery=False):
    require(receipt is not None and receipt.exists(),'Explicit existing verification receipt required')
    v=read(receipt);worlds=[]
    for w in WORLDS:
        path=out/'worlds'/w/'SCORES.json'
        if path.exists():worlds.append(dict(world=w,**read(path)))
    complete=v.get('integrity')=='PASS' and len(worlds)==82
    inference=v.get('inference');qualified=bool(complete and inference['statistical_and_resolution_pass'])
    status='INCOMPLETE' if not complete else ('NUMERICALLY_UNRESOLVED' if inference['unresolved'] else ('PRIMARY_SUCCESS' if qualified else 'PRIMARY_FAILURE'))
    def summary(x):
        a=np.array(x);return dict(values=x,mean=float(a.mean()),sample_std=float(a.std(ddof=1)) if len(a)>1 else None,**dict(zip(['min','median','q10','q90','max'],np.quantile(a,[0,.5,.1,.9,1],method='linear').tolist())))
    distributions={}
    for h in ('H1','H2','aggregate'):
        for m in ('gain','recovery','contrast','inactive'):
            vals=[w['gates'][h]['values'][m] for w in worlds]
            distributions[h+'/'+m]=summary(vals) if vals and all(x is not None for x in vals) else dict(values=vals,undefined_present=True)
    paired={}
    if worlds:
        for h in HIST:
            for stratum in ('active','inactive'):
                for m in METHODS:
                    rr=[next(r for r in w['rows'] if (r['history'],r['stratum'],r['method'])==(h,stratum,m)) for w in worlds]
                    for metric in rr[0]['metrics']:
                        paired[f'{h}/{stratum}/{m}/minus_U/{metric}']=summary([r['minus_uncapped'][metric] for r in rr]);paired[f'{h}/{stratum}/{m}/own_minus_donor/{metric}']=summary([r['own_minus_donor'][metric] for r in rr])
    result=dict(status=status,scientific_qualification_pending_final_resource_check=qualified,verification_receipt=str(receipt),verification_sha256=sha(receipt),inference=inference,primary_distributions=distributions,paired_descriptive=paired,history_disagreements=sum(w['history_disagreement'] for w in worlds),aggregate_hides_failure=sum(w['aggregate_hides_failure'] for w in worlds),both_histories_pass=sum(w['both_histories_pass'] for w in worlds),H2_statuses={w['world']:w['gates']['H2']['joint'] for w in worlds},primary_statuses={w['world']:w['gates']['H1']['joint'] for w in worlds},unreached_worlds=[w for w in WORLDS if w not in {x['world'] for x in worlds}],reporting_only_recovery=recovery)
    atomic(out/'RESULT_STATUS.json',result)
    text=f'# Uncapped single-history confirmation v1\n\nOutcome: **{status}**. Final qualification and cumulative resources are in DELIVERY_TERMINAL.json and RESOURCE_USAGE_FINAL.json, emitted after this reporting command completes.\n\nPrimary inference: {json.dumps(inference)}. H1 alone is primary. H2, aggregate histories and controls cannot rescue it. All four metric distributions and all-world values are in RESULT_STATUS.json; per-world SCORES.json contains all controls, donor, sampled metrics, inactive tails and evidence/weight diagnostics.\n\nAssignment {ASSIGNMENT}; pre-fit '+read(out/'PUBLICATION.json')['commit']+'. Models are identified by each world\'s sealed archive hashes. Final commit is posted/read back in issue #2 and the draft PR.\n\nNumerical enclosures condition on saved shared models, weights/evidence and computed oracle references. They are not directed-rounding certificates, sampling intervals or shared global-optimum certificates. The exact binomial calculation concerns operational world reliability under the declared balanced-history generator, not individual people or arbitrary text histories.\n\nHistorical PR20 remains INCOMPLETE / NUMERICALLY_UNRESOLVED. PR27 remains a post hoc diagnostic; E/101 remains a failure. No historical refit, human/text evaluation, downloads, paid calls, PR18 execution, corpus changes or merge.\n'
    with (out/'RESULTS.md').open('x',encoding='utf-8') as f:f.write(text)
    handoff='''# Next handoff

Read RESULTS.md, RESULT_STATUS.json, DELIVERY_TERMINAL.json, RESOURCE_USAGE_FINAL.json and the immutable verification receipt. Preserve all failures, starts, incomplete identities and private artifacts. Never retry this scientific run or generate replacement worlds; a separate reviewed assignment would be required for any unstarted identities. End the automatic same-family synthetic sequence.

One next proposed study, not executed: an outcome-blind admission and frozen-representation evaluation for text-to-decision prediction with an estimated population predictor. First audit candidate TID-8 CommitmentBank constituent terms, immutable revision, respondent identity/overlap, common response semantics and at least16 usable support responses per held-out person; if these fail, publish the admission obstruction without silently replacing the candidate. Freeze grouped-question/new-person splits, one16-case history, representation and population-model training confined to training data, and B1/B2/B3 controls with equal information budgets before accessing held-out responses. Compare fixed representation interaction to personal-offset B3 using paired loss, calibration/accuracy/Brier tradeoffs and predeclared uncertainty. Make no .009 guarantee for estimated g without a separately justified conditional-null argument. DICES/SRO are exposed; corpus production and scholarly certification remain separate. No launch or download is authorized by this handoff.

Reproduction: run the new cli.py verify stage under supervise.py, with explicit output/private roots and a fresh receipt. Verification consumes saved arrays only; it must not import an execution entry point or invoke world generation/optimization. Read the existing receipt first; repeat only to resolve a concrete risk. Reporting recovery is the predeclared recover-report stage, requires an existing verification receipt and refuses existing report destinations. Missing scientific work cannot be reconstructed.
'''
    with (out/'NEXT_HANDOFF.md').open('x',encoding='utf-8') as f:f.write(handoff)
def finalize(out):
    r=resources(out);atomic(out/'RESOURCE_USAGE_FINAL.json',r);s=read(out/'RESULT_STATUS.json');valid=not r['unmatched_commands'] and r['cpu_seconds_sampled']<=3600 and r['peak_process_tree_rss_bytes_sampled']<=4*1024**3
    verified=s['status']!='INCOMPLETE';qualified=s['scientific_qualification_pending_final_resource_check'] and valid
    atomic(out/'DELIVERY_TERMINAL.json',terminal(completed=len(s['primary_statuses']),expected=82,integrity='PASS' if verified else 'INCOMPLETE',numerical='UNRESOLVED' if s['status']=='NUMERICALLY_UNRESOLVED' else ('PASS' if verified else 'NOT_ESTABLISHED'),scientific='PASS' if qualified else ('FAIL' if s['status']=='PRIMARY_FAILURE' else 'NOT_ESTABLISHED'),reason=None if qualified else s['status'],qualified=qualified,resource_status='PASS' if valid else 'UNRESOLVED',primary_status=s['status']))
