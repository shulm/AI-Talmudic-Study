"""Read-only replay of the lane's frozen bounded proposals, not fresh generation."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner as r

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--receipt',type=Path,default=HERE/'SESSION_CHECKPOINT.json')
    p.add_argument('--source-root',type=Path,default=Path('F:/Sefaria-Export-master'))
    args=p.parse_args()
    receipt=r.read(args.receipt)
    assert receipt['lane_id']=='L02'
    assert receipt['denominator']==13669
    for rel,expected in receipt['artifact_hashes'].items():
        assert r.sha((HERE/rel).read_bytes())==expected,rel
    review_manifest=r.read(HERE/'review/REVIEW_ARTIFACT_MANIFEST.json')
    for rel,expected in review_manifest['files'].items():
        assert r.sha((HERE/'review/frozen'/rel).read_bytes())==expected,rel
    for rel,expected in receipt['production_files'].items():
        assert r.sha((ROOT/rel).read_bytes())==expected,rel
    reports=[]
    for job in receipt['jobs']:
        spec=job['job_contract']
        _,rows=r.source(args.source_root,ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json',spec['tractate'])
        segments={s['id']:s for s in rows}
        state=r.empty()
        for h in job['accepted_proposal_sha256s']:
            raw=(HERE/'frozen'/job['job_id']/'proposals'/(h+'.json')).read_bytes()
            assert r.sha(raw)==h
            prior=state['proposals']
            state=r.validate_apply(state,json.loads(raw),segments,spec)
            state['proposals']=prior+[h]
        assert r.sha(r.encoded(state))==job['snapshot_sha256']
        assert r.encoded(state)==(HERE/'frozen'/job['job_id']/'snapshot.json').read_bytes()
        report=r.report(state,segments)
        assert report==job['coverage']
        reports.append({'job_id':job['job_id'],'snapshot_sha256':job['snapshot_sha256'],'source_segments':len(rows),'completed_by_layer':report['completed_by_layer'],'replay_pass':True})
    assert len(reports)==5
    print(json.dumps({'status':'PASS_FROZEN_PARTIAL_CHECKPOINT_NOT_TRACTATE_COMPLETION','jobs':reports},indent=2))

if __name__=='__main__': main()
