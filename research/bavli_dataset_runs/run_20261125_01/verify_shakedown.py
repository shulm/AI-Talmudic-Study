"""Verify real saved interactive readings, restart, source fidelity and replay."""
import json
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner as r

def main():
    checks=[]
    for tractate,lane,jobid,proposal in [('Berakhot','L01','bavli_berakhot','berakhot_b24_initial.json'),('Rosh Hashanah','L03','bavli_rosh_hashanah','rosh_hashanah_opening_initial.json')]:
        frozen=HERE/'proposals'/proposal
        with tempfile.TemporaryDirectory(prefix='bavli-real-restart-') as td:
            job=Path(td)/jobid
            r.init(job,Path('F:/Sefaria-Export-master'),ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json',tractate,'GLOBAL_COORDINATOR_BOOTSTRAP',1)
            try: r.submit(job,frozen,'GLOBAL_COORDINATOR_BOOTSTRAP',1,fail_before_pointer=True)
            except RuntimeError as e: assert 'injected interruption' in str(e)
            else: raise AssertionError('interruption not raised')
            assert not (job/'CURRENT.json').exists()
            assert not r.current(job)['proposals']
            promoted=r.submit(job,frozen,'GLOBAL_COORDINATOR_BOOTSTRAP',1)
            assert r.submit(job,frozen,'GLOBAL_COORDINATOR_BOOTSTRAP',1)['idempotent']
            replay=r.replay(job)
            assert replay['snapshot_sha256']==promoted['snapshot_sha256']
            canonical=Path('F:/Sefaria_QA/bavli_production_run_20261125_01')/lane/jobid
            # Later reviewed corrections may advance CURRENT; initial accepted
            # snapshot remains immutable and is the shakedown replay target.
            assert r.sha((canonical/'snapshots'/(replay['snapshot_sha256']+'.json')).read_bytes())==replay['snapshot_sha256']
            assert r.replay(canonical)['replay_pass']
            bad=json.loads(frozen.read_bytes()); bad['records'][0]['evidence'][0]['quote']+='X'
            badpath=Path(td)/'badquote.json';badpath.write_bytes(r.encoded(bad))
            meta,segments=r.load(job)
            try: r.validate_apply(r.empty(),bad,segments,meta)
            except ValueError as e: assert 'quote/offset' in str(e)
            else: raise AssertionError('corrupt evidence accepted')
            try: r.submit(job,frozen,'STALE_OWNER',1)
            except ValueError: pass
            else: raise AssertionError('stale owner accepted')
            assert r.replay(job)['snapshot_sha256']==replay['snapshot_sha256']
            checks.append(dict(tractate=tractate,proposal_sha256=r.sha(frozen.read_bytes()),snapshot_sha256=replay['snapshot_sha256'],source_segments=replay['source_segments'],completed_by_layer=replay['completed_by_layer'],records=replay['semantic_records'],passed=['original_source_hash','source_schema_hash','proposal_schema','exact_evidence_spans','primary_interval_partition','per_layer_validation','interruption_before_pointer','recovery','idempotency','deterministic_replay','bad_quote_rejected','stale_owner_rejected'],whole_tractate_complete=False))
    report=dict(status='PASSED_REAL_SEMANTIC_SHAKEDOWN',checks=checks,**r.hashes(),new_metered_external_api_calls=0,agent_route='interactive_agent',agent_id='/root',model_id=None,model_id_note='Not exposed as a reliable runtime identifier',review_note='Independent readings are separate artifacts; no human review implied.')
    path=HERE/'SHAKEDOWN.json'; r.immutable(path,(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode())
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
