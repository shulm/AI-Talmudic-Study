"""Package L03 checkpoint evidence; all semantics/replay use the frozen runner.

Run only after producers have checkpointed. No source corpus is copied.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[6]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);args=p.parse_args()
    output=args.output.resolve()
    if output.exists():raise ValueError('Choose a fresh immutable package output')
    if output.is_relative_to(ROOT) or output.is_relative_to(Path('F:/Sefaria-Export-master').resolve()):raise ValueError('Package must be external and outside original sources')
    run=ROOT/'research/bavli_dataset_runs/run_20261125_01'
    contract=runner.read(run/'RUN_CONTRACT.json')
    contract_sha=runner.sha((run/'RUN_CONTRACT.json').read_bytes())
    if contract_sha!='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174':raise ValueError('Contract pin mismatch')
    for rel,expected in contract['production_files'].items():
        if runner.sha((ROOT/rel).read_bytes())!=expected:raise ValueError('Changed production file '+rel)
    assignment=next(l for l in runner.read(ROOT/'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json')['lanes'] if l['lane_id']=='L03')
    package_run=output/'run';runner.immutable(package_run/'RUN_CONTRACT.json',(run/'RUN_CONTRACT.json').read_bytes())
    release=dict(run_id='run_20261125_01',lane_id='L03',status='PARTIAL_REQUIRED_WORK_REMAINS',contract_sha256=contract_sha,production_git_commit=contract['production_git_commit'],jobs=[])
    for job in assignment['jobs']:
        directory=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03')/job['job_id']
        result=runner.replay(directory);state=runner.current(directory);owner=runner.read(directory/'OWNER.json')
        version=runner.sha(runner.encoded(state))
        if result['snapshot_sha256']!=version:raise ValueError('Producer changed during capture')
        props=state['proposals']
        for h in props:
            raw=(directory/'proposals'/f'{h}.json').read_bytes()
            if runner.sha(raw)!=h:raise ValueError('Corrupt proposal')
            runner.immutable(package_run/'proposals'/f'{h}.json',raw)
        exp=runner.export(directory,output/'exports'/job['job_id'])
        if exp['snapshot_sha256']!=version:raise ValueError('Producer changed during export')
        row=dict(job_id=job['job_id'],lane_id='L03',tractate=job['tractate'],owner=owner['owner'],epoch=owner['epoch'],source_sha256=job['expected_source_sha256'],source_path=job['source_path'],source_schema_sha256=job['source_schema_sha256'],source_segments=job['expected_source_segments'],snapshot_sha256=version,proposal_sha256=props,job_dir=str(directory),coverage=result,export_manifest_sha256=runner.sha((output/'exports'/job['job_id']/'manifest.json').read_bytes()),unresolved_records=[r['id'] for r in state['records'] if r['release_state']=='valid' and r['uncertainty']],open_tails=state['open_tails'],state='checkpointed_inactive' if props else 'queued_unstarted',remaining_by_layer={l:job['expected_source_segments']-result['completed_by_layer'][l] for l in runner.LAYERS})
        release['jobs'].append(row)
    # Include immutable initial independent readings and original attempts; never infer review acceptance.
    review=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/review_source_first_20261125')
    if review.exists():
        for f in sorted(review.rglob('*')):
            if f.is_file() and f.suffix in ['.json','.md','.py']:
                runner.immutable(output/'review_source_first'/f.relative_to(review),f.read_bytes())
    for f in sorted((run/'lanes/L03').rglob('*')):
        if f.is_file() and f.suffix in ['.json','.md','.py']:
            runner.immutable(output/'lane_provenance'/f.relative_to(run/'lanes/L03'),f.read_bytes())
    runner.immutable(package_run/'releases/L03_checkpoint.json',runner.encoded(release))
    manifest={str(f.relative_to(output)).replace('\\','/'):runner.sha(f.read_bytes()) for f in sorted(output.rglob('*')) if f.is_file()}
    runner.immutable(output/'PACKAGE_MANIFEST.json',runner.encoded(dict(files=manifest,source_corpora_included=False,review_comparison_complete=False,tractates_delivered=0)))
    archive=output.with_suffix('.zip')
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED) as z:
        for f in sorted(output.rglob('*')):
            if f.is_file():
                info=zipfile.ZipInfo(f.relative_to(output).as_posix(),date_time=(2026,11,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,f.read_bytes())
    receipt=dict(release=release,package_dir=str(output),package_manifest_sha256=runner.sha((output/'PACKAGE_MANIFEST.json').read_bytes()),archive_path=str(archive),archive_sha256=runner.sha(archive.read_bytes()),new_metered_api_calls=0,tokens=None,cost=None,review_state='source_first_readings_only_comparison_and_risk_review_outstanding',no_background_continuation=True)
    runner.immutable(args.receipt,runner.encoded(receipt))
    print(json.dumps(dict(receipt=str(args.receipt),archive=str(archive),sha256=receipt['archive_sha256'],jobs=[dict(tractate=r['tractate'],completed=r['coverage']['completed_by_layer'],next=r['coverage']['next_unprocessed_by_layer']) for r in release['jobs']]),ensure_ascii=False))

if __name__=='__main__':main()
