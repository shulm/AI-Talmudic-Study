"""Verify and package the bounded Yoma wave and review evidence."""
import hashlib,json,shutil,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parent
W=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
previous=json.loads((S.parent/'session_20261127_19/CHECKPOINTS.json').read_bytes())
rows=[]
for row in previous:
    job=J/row['job_id']
    rep=json.loads(subprocess.check_output([sys.executable,'-X','utf8','research/bavli_production_v1/runner.py','replay','--job-dir',str(job)]))
    assert rep['replay_pass']
    assert rep['completed_by_layer']==({k:180 for k in row['replay']['completed_by_layer']} if row['job_id']=='bavli_yoma' else row['replay']['completed_by_layer'])
    assert json.loads((job/'OWNER.json').read_bytes())==row['owner']
    if row['job_id']=='bavli_yoma':
        assert rep['snapshot_sha256']!=row['replay']['snapshot_sha256']
        ex=W/'exports/session20261127_20_delivery'/('bavli_yoma_'+rep['snapshot_sha256'][:12])
        if not ex.exists(): subprocess.check_output([sys.executable,'-X','utf8','research/bavli_production_v1/runner.py','export','--job-dir',str(job),'--output',str(ex)])
        m=json.loads((ex/'manifest.json').read_bytes())
        assert m['snapshot_sha256']==rep['snapshot_sha256']
        for rel,h in m['files'].items(): assert sha(ex/rel)==h
        row['previous_snapshot_sha256']=row['replay']['snapshot_sha256']
        row['export_dir']=str(ex);row['export_manifest_sha256']=sha(ex/'manifest.json')
        snap=json.loads((job/'snapshots'/(rep['snapshot_sha256']+'.json')).read_bytes())
        assert sha(job/'snapshots'/(rep['snapshot_sha256']+'.json'))==rep['snapshot_sha256']
        row['open_tails']=snap['open_tails']
        row['active_records']=sum(r['release_state']=='valid' for r in snap['records'])
        row['superseded_records']=sum(r['release_state']=='superseded' for r in snap['records'])
        for p in (job/'proposals').glob('*.json'):
            if not any(q.name==p.name for q in S.parent.glob('session_*/**/*.json') if S not in q.parents):
                d=S/'new_canonical_proposals'/p.name;d.parent.mkdir(exist_ok=True)
                if d.exists():assert d.read_bytes()==p.read_bytes()
                else:shutil.copyfile(p,d)
    else: assert rep['snapshot_sha256']==row['replay']['snapshot_sha256']
    row['replay']=rep;rows.append(row)
for p in (W/'review_session20261127_20').rglob('*'):
    if p.is_file() and p.suffix in {'.json','.sha256','.md'}:
        d=S/'review'/p.relative_to(W/'review_session20261127_20');d.parent.mkdir(parents=True,exist_ok=True)
        if d.exists():assert d.read_bytes()==p.read_bytes()
        else:shutil.copyfile(p,d)
(S/'CHECKPOINTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Six replays PASS; bounded coverage verified; Yoma export verified.')
