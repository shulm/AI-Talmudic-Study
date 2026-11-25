"""Coordinator-only exact-version rolling inventory; never infer semantic review.

Produces metadata, not a full source-text copy. Pin this script's hash in every
release receipt. Record versions and complete source-gap intervals are retained.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner as r

def missing_ranges(rows, covered):
    result=[]; start=None; end=None; count=0
    for row in rows:
        if row['id'] not in covered:
            if start is None:start=row['ref']
            end=row['ref'];count+=1
        elif start is not None:
            result.append(dict(start_ref=start,end_ref=end,source_segments=count));start=None;count=0
    if start is not None:result.append(dict(start_ref=start,end_ref=end,source_segments=count))
    return result

def assess_review(run_dir,job,snapshot,active,source):
    """Admit only a separately frozen exact-version full review receipt.

    Reading artifacts must contain their own source refs, substantive findings,
    execution identity and source-first declaration. Metadata alone cannot pass.
    An honest unsupported interpretation remains a documented exclusion.
    """
    receipt_path=run_dir/'review'/job['job_id']/(snapshot+'.json')
    if not receipt_path.exists():return False,'No full source-coordinate probability/endpoint/risk review receipt admitted for this exact tractate version'
    receipt=r.read(receipt_path);plan_path=run_dir/'review_plans'/(job['job_id']+'.json');plan=r.read(plan_path)
    assert receipt['snapshot_sha256']==snapshot and receipt['source_sha256']==job['source_sha256']
    assert receipt['plan_file_sha256']==r.sha(plan_path.read_bytes())
    assert receipt['review_kind']=='independent_ai_source_first'
    core=set();reviewed_risk=set();byref={x['ref']:x for x in source.values()}
    for binding in receipt['initial_readings']:
        path=(run_dir/binding['path']).resolve();assert path.is_relative_to(run_dir.resolve())
        raw=path.read_bytes();assert r.sha(raw)==binding['sha256'];reading=json.loads(raw)
        assert reading['source_sha256']==job['source_sha256']
        assert reading['frozen_before_comparison'] is True and reading['producer_labels_exposed'] is False
        assert reading['execution']['agent_id'] and reading['execution']['route']=='interactive_agent'
        assert reading['findings'] and reading['core_refs']
        assert set(reading['core_refs'])<=set(byref)
        for finding in reading['findings']:
            assert finding['interpretation'] and finding['evidence']
            for e in finding['evidence']:
                text=byref[e['ref']]['text'];a=e['start_char'];b=e['end_char']
                assert 0<=a<b<=len(text) and text[a:b]==e['quote'],'Invalid independent source evidence'
        core.update(reading['core_refs'])
    required={span['ref'] for block in plan['review_blocks'] for span in block['spans']}
    if not required<=core:return False,'Independent source reading missing '+str(len(required-core))+' required probability/endpoint core segments'
    compare_path=(run_dir/receipt['comparison']['path']).resolve();assert compare_path.is_relative_to(run_dir.resolve())
    raw=compare_path.read_bytes();assert r.sha(raw)==receipt['comparison']['sha256'];compare=json.loads(raw)
    assert compare['snapshot_sha256']==snapshot
    assert compare['initial_reading_hashes']==[x['sha256'] for x in receipt['initial_readings']]
    assert compare['omission_pass_performed'] is True
    reviewed_risk.update(compare['reviewed_risk_record_ids'])
    risks={x['id'] for x in active if x['uncertainty'] or (x['layer']=='structure' and x['content']['boundary']!='closed')}
    if not risks<=reviewed_risk:return False,'Risk review incomplete'
    if compare['unresolved_integrity_critical_count']!=0:return False,'Unresolved integrity-critical review findings'
    if receipt['verdict']!='ACCEPT_PROVISIONAL_TRACTATE':return False,'Review verdict is partial or requires rework'
    return True,'Exact-version source-first review, required source cores and risk records admitted; no human certification'

def inspect(job,run_dir):
    directory=Path(job['job_dir'])
    with r.lock(directory):
        meta,source=r.load(directory); state=r.current(directory)
        r.authorize(directory,job['owner'],job['epoch'])
        # Independently reconstruct this exact accepted version while holding
        # the same lock as the promoter. Rejected/orphan proposals do not count.
        rebuilt=r.empty()
        for h in state['proposals']:
            raw=(directory/'proposals'/(h+'.json')).read_bytes()
            assert r.sha(raw)==h
            previous=rebuilt['proposals'];rebuilt=r.validate_apply(rebuilt,json.loads(raw),source,meta);rebuilt['proposals']=previous+[h]
        assert r.encoded(rebuilt)==r.encoded(state),'checkpoint replay mismatch'
        active=[x for x in state['records'] if x['release_state']=='valid']
        quarantine_path=run_dir/'QUARANTINE.json'
        entries=r.read(quarantine_path)['entries'] if quarantine_path.exists() else []
        quarantined={x['id'] for x in active for q in entries if q['job_id']==job['job_id'] and q['record_id']==x['id'] and q['record_sha256']==r.sha(r.encoded(x))}
        # Dependent records cannot become release-valid through an export.
        changed=True
        while changed:
            before=len(quarantined)
            for x in active:
                deps=set(x['links'])|{x['content'][k] for k in ['claim_id','question_id','source_id','target_id'] if x['content'].get(k)}
                if deps & quarantined:quarantined.add(x['id'])
            changed=len(quarantined)!=before
        released=[x for x in active if x['id'] not in quarantined]
        layers={}
        for layer in r.LAYERS:
            done={x['segment_id'] for x in state['coverage'] if x['layer']==layer and x['extraction_state']=='completed'}
            layers[layer]=dict(completed_source_segments=len(done),required_source_segments=len(source),missing_ranges=missing_ranges(list(source.values()),done),active_records=sum(x['layer']==layer for x in active),abstained_source_segments=sum(x['layer']==layer and x['extraction_result']=='abstained_ambiguous' for x in state['coverage']))
        all_passes=all(x['completed_source_segments']==len(source) for x in layers.values())
        snapshot=r.sha(r.encoded(state));review,review_note=assess_review(run_dir,job,snapshot,active,source)
        delivered=all_passes and review and not state['open_tails'] and not quarantined
        return dict(job_id=job['job_id'],tractate=job['tractate'],lane_id=job['lane_id'],owner=job['owner'],epoch=job['epoch'],source_sha256=meta['source_sha256'],source_segments=len(source),snapshot_sha256=snapshot,has_promoted_checkpoint=bool(state['proposals']),proposal_sha256=state['proposals'],source_integrity='PASS',schema_and_replay='PASS',layers=layers,active_semantic_records=len(active),release_valid_records=len(released),quarantined_record_ids=sorted(quarantined),preserved_superseded_records=len(state['records'])-len(active),open_tails=state['open_tails'],required_extraction_passes_complete=all_passes,independent_review_complete=review,review_note=review_note,verdict='ACCEPT_PROVISIONAL_TRACTATE' if delivered else 'ACCEPT_PARTIAL_WITH_EXCEPTIONS' if active else 'NOT_STARTED',tractate_delivered=delivered,ml_eligible_records=0)

def main():
    p=argparse.ArgumentParser();p.add_argument('--run-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    ledger=r.read(args.run_dir/'ASSIGNMENT_LEDGER.json');contract=r.read(args.run_dir/'RUN_CONTRACT.json')
    expected=json.loads((ROOT/'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json').read_bytes())
    expected_ids={j['job_id'] for l in expected['lanes'] for j in l['jobs']}
    assert len(ledger['jobs'])==37 and {j['job_id'] for j in ledger['jobs']}==expected_ids
    jobs=[inspect(j,args.run_dir) for j in ledger['jobs']]
    assert sum(j['source_segments'] for j in jobs)==81793
    output=dict(run_id=contract['run_id'],contract_sha256=r.sha((args.run_dir/'RUN_CONTRACT.json').read_bytes()),assignment_revision=ledger['revision'],integrator_sha256=r.sha(Path(__file__).read_bytes()),status='COMPLETE_PROVISIONAL_CORE' if all(j['tractate_delivered'] for j in jobs) else 'PARTIAL_REQUIRED_WORK_REMAINS',tractates_required=37,tractates_delivered=sum(j['tractate_delivered'] for j in jobs),source_segments_verified=81793,completed_source_segments_by_layer={l:sum(j['layers'][l]['completed_source_segments'] for j in jobs) for l in r.LAYERS},active_semantic_records=sum(j['active_semantic_records'] for j in jobs),preserved_superseded_records=sum(j['preserved_superseded_records'] for j in jobs),historical_coverage_separate=dict(berakhot_provisional_structure=386,bava_metzia_interior_pilot=64,not_added_to_new_semantic_counts=True),jobs=jobs,limitations=['Targeted bootstrap review is separate from required probability/endpoint and risk review.','A completed extraction pass is agent execution evidence, not proof of scholarly completeness.','All new task eligibility remains false.'])
    r.immutable(args.output,(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode())
    print(json.dumps({k:v for k,v in output.items() if k not in ['jobs','limitations']}))

if __name__=='__main__':main()
