"""Read-only integrity/replay check for this partial L01 artifact, not scholarly certification."""
import argparse, hashlib, json, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path('F:/Sefaria-Export-master'))
    args=parser.parse_args()
    manifest=read(HERE/'PACKAGE_HASHES.json')['files']
    for name,h in manifest.items():
        p=(HERE/name).resolve()
        assert p.is_relative_to(HERE.resolve()),name
        assert digest(p)==h,('artifact hash',name)
    readiness=read(HERE/'receipts/readiness_session_20261125.json')
    for name,h in readiness['production_files'].items(): assert digest(ROOT/name)==h,('production hash',name)
    status=read(HERE/'LANE_STATUS_AND_RESUME.json')
    assert status['original_denominator']==13657 and status['completed_tractates']==0
    assert len(status['jobs'])==6
    results=[]
    for item in status['jobs']:
        d=HERE/item['job_id']; j=read(d/'JOB.json')
        _,rows=runner.source(args.source_root,ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json',item['tractate'])
        segments={x['id']:x for x in rows}
        state=runner.empty()
        for h in item['accepted_proposal_sha256']:
            p=d/'proposals'/f'{h}.json'; assert digest(p)==h
            chain=state['proposals']; state=runner.validate_apply(state,read(p),segments,j); state['proposals']=chain+[h]
        assert runner.sha(runner.encoded(state))==item['snapshot_sha256']
        assert runner.encoded(state)==(d/'snapshot.json').read_bytes()
        report=runner.report(state,segments)
        assert report['completed_by_layer']==item['completed_by_layer']
        assert report['next_unprocessed_by_layer']==item['next_unprocessed_by_layer']
        assert len(rows)==item['source_denominator']
        assert sum(x['release_state']=='valid' for x in state['records'])==item['active_records']
        assert not item['tractate_delivered'] and not item['independent_review_complete']
        results.append(dict(tractate=item['tractate'],source_segments=len(rows),completed_by_layer=report['completed_by_layer'],snapshot_sha256=item['snapshot_sha256']))
    assert sum(x['source_denominator'] for x in status['jobs'])==13657
    for layer in runner.LAYERS:
        assert sum(x['completed_by_layer'][layer] for x in status['jobs'])==status['completed_by_layer'][layer]
        assert status['remaining_by_layer'][layer]+status['completed_by_layer'][layer]==13657
    print(json.dumps(dict(integrity_and_replay='PASS',artifact_files=len(manifest),jobs=results,scholarly_completeness_certified=False,tractates_delivered=0),ensure_ascii=False,indent=2))

if __name__=='__main__': main()
