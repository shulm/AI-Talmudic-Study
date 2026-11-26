"""Freeze bounded accepted versions; does not promote or generate semantics."""
from pathlib import Path
import sys, json, subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner as r
QA=Path('F:/Sefaria_QA/bavli_production_run_20261125_01')
OUT=HERE/'resume_20261126'
expected={
'bavli_bava_metzia':'6ae7d3ff84f60aa050dc89331a3732f5f46a68198f19a09b7e9b93ca9ceb4312',
'bavli_gittin':'f3fe34947e41266a2f969dc4a0e9af8ec5928fe86e736abed2b4beae81fc1765',
'bavli_keritot':'160f470b13ecb9fc104d6484ae4ee7b1b30c3e7ca3378b2902c48ea65889304f',
'bavli_sanhedrin':'b4575728a42e6d57296e8b079cdd84fea74831dfacbaa9d7f15aff767daf79c7',
'bavli_sotah':'caf1a0e2d7565c91718f41cdf910c84261f7942f22758e6135d52666f3280de1'}
jobs=[]
for slug,h in expected.items():
    job=QA/'L02'/slug
    report=r.replay(job);assert report['snapshot_sha256']==h
    state=r.read(job/'snapshots'/f'{h}.json')
    r.immutable(OUT/slug/'snapshot.json',(job/'snapshots'/f'{h}.json').read_bytes())
    for ph in state['proposals']:
        raw=(job/'proposals'/f'{ph}.json').read_bytes();assert r.sha(raw)==ph
        r.immutable(OUT/slug/'proposals'/f'{ph}.json',raw)
    ex=job/'exports'/('integration_resume_'+h[:12]);r.export(job,ex)
    r.immutable(OUT/slug/'export_manifest.json',(ex/'manifest.json').read_bytes())
    jobs.append(dict(job_id=slug,owner=r.read(job/'OWNER.json'),job_path=str(job),snapshot_sha256=h,
        snapshot_path=str(job/'snapshots'/f'{h}.json'),accepted_proposal_sha256=state['proposals'],
        export_manifest_path=str(ex/'manifest.json'),export_manifest_sha256=r.sha((ex/'manifest.json').read_bytes()),
        source_sha256=r.read(job/'JOB.json')['source_sha256'],report=report,open_tails=state['open_tails']))
reviews=[]
for p in sorted((QA/'review/L02_resume_20261126').glob('*_source_reading.json')):
    raw=p.read_bytes();reading=json.loads(raw)
    assert r.sha(Path(reading['source_file']).read_bytes())==reading['source_sha256']
    slug=next(x for x in expected if x.replace('bavli_','').replace('_',' ').lower()==reading['core_start'].rsplit(' ',1)[0].lower())
    segments={x['ref']:x for x in r.load(QA/'L02'/slug)[1].values()}
    for rec in reading['records']:
        lo,hi=rec['raw_unicode_span'];assert segments[rec['ref']]['text'][lo:hi]==rec['source_text']
    r.immutable(OUT/'review'/p.name,raw)
    reviews.append(dict(path=str(p),repo_relative_path=str((OUT/'review'/p.name).relative_to(ROOT)),sha256=r.sha(raw),
        core_start=reading['core_start'],core_end=reading['core_end'],core_segments=reading['core_segment_count'],
        source_slice_verification='PASS',comparison_completed=False))
receipt=dict(run_id='run_20261125_01',contract_sha256='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174',
    producing_parent_commit_before_freeze=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
    coordination_commit_observed='9e0a56ebb53f52ddc145bb58c351a855a2ff0f5f',assignment_revision=4,
    jobs=jobs,source_segments=13669,completed_each_layer=sum(x['report']['completed_by_layer']['structure'] for x in jobs),
    review_readings=reviews,review_launch=dict(agent='/root/review_resume',fork_turns='none',route='interactive_agent',model_id=None,
      instruction_scope='Source-only original readings; no producer labels; continuation/risk cores, not probability sample.'),
    review_backlog='Compare new frozen readings against exact versions; Sanhedrin core not produced. Remaining frozen probability blocks and risk/task policies still incomplete.',
    exposure='Sotah producer disclosed seeing portions of prior source-review annotations for 3b:15–4a:1 before overlapping production; do not score independent agreement there.',
    blockage='All three child agents terminated with platform usage-limit errors; no parallel production or fresh reader remains running.',
    independent_review_completed=False,tractates_delivered=0,ml_eligible=False,
    bm001_resolution='Only corrected snapshot1de0ef2ed8f9cd4fc22791162f92e7d59d276dc09dd9c50336dd8fe0a3940a92; later new content not admitted by that receipt.',
    artifact_files={p.relative_to(OUT).as_posix():r.sha(p.read_bytes()) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='RECEIPT.json'})
r.immutable(OUT/'RECEIPT.json',r.encoded(receipt))
print(json.dumps(dict(receipt_path=str(OUT/'RECEIPT.json'),sha256=r.sha((OUT/'RECEIPT.json').read_bytes()),completed_each_layer=receipt['completed_each_layer'],reviews=reviews)))
