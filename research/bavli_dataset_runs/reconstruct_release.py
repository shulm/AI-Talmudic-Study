"""Rebuild an exact partial release from frozen proposals and approved sources.

No model calls. Original source files are never copied or edited. Legacy archive
restoration is separate; its snapshot manifest and external location are pinned
in RUN_CONTRACT.json.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner as r

def reconstruct(release_path,source_root,output):
    release_path=Path(release_path);source_root=Path(source_root).resolve();output=Path(output).resolve()
    assert not output.is_relative_to(ROOT) and not output.is_relative_to(source_root)
    release=r.read(release_path);run=release_path.parent.parent
    assert r.sha((run/'RUN_CONTRACT.json').read_bytes())==release['contract_sha256']
    files={r.sha(p.read_bytes()):p for p in run.rglob('*.json')}
    receipts=[]
    for job in release['jobs']:
        hashes=job['proposal_sha256'];first=r.read(files[hashes[0]]) if hashes else job
        owner,epoch=first['owner'],first['epoch'];dest=output/job['lane_id']/job['job_id']
        r.init(dest,source_root,ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json',job['tractate'],owner,epoch)
        for h in hashes:
            proposal=r.read(files[h])
            if proposal['owner']!=owner or proposal['epoch']!=epoch:
                assert proposal['epoch']==epoch+1,'Missing ownership transition in accepted proposal sequence'
                with r.lock(dest):
                    r.authorize(dest,owner,epoch);r.immutable(dest/'ownership_history'/(str(epoch)+'.json'),r.encoded(dict(owner=owner,epoch=epoch)))
                    owner,epoch=proposal['owner'],proposal['epoch'];r.atomic(dest/'OWNER.json',dict(owner=owner,epoch=epoch))
            r.submit(dest,files[h],owner,epoch)
        result=r.replay(dest);assert result['snapshot_sha256']==job['snapshot_sha256'],'Reconstructed snapshot mismatch'
        # A handoff can occur after the last accepted proposal.
        if owner!=job['owner'] or epoch!=job['epoch']:
            assert job['epoch']==epoch+1
            with r.lock(dest):
                r.immutable(dest/'ownership_history'/(str(epoch)+'.json'),r.encoded(dict(owner=owner,epoch=epoch)))
                r.atomic(dest/'OWNER.json',dict(owner=job['owner'],epoch=job['epoch']))
        receipts.append(dict(job_id=job['job_id'],proposal_count=len(hashes),snapshot_sha256=result['snapshot_sha256'],replay_pass=True))
    report=dict(release_sha256=r.sha(release_path.read_bytes()),source_manifest_sha256=r.PIN,reconstruction_script_sha256=r.sha(Path(__file__).read_bytes()),jobs=receipts,all_37_reconstructed=len(receipts)==37,new_model_calls=0,legacy_archive_note='Restore separately from pinned preserved snapshot; these receipts reconstruct new production core only.')
    r.immutable(output/'RECONSTRUCTION.json',r.encoded(report));print(json.dumps(dict(all_37_reconstructed=report['all_37_reconstructed'],accepted_proposals=sum(x['proposal_count'] for x in receipts),receipt=str(output/'RECONSTRUCTION.json'))))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--release',type=Path,required=True);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();reconstruct(a.release,a.source_root,a.output)
