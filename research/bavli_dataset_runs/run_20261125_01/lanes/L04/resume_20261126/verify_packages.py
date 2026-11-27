"""Verify delivered checkpoint bytes and replay against exact local originals.

Run with --source-root PATH when the originals live elsewhere. Does not mutate
the original corpus, production jobs or packaged JOB metadata.
"""
from author_remaining_openings_001 import r
from pathlib import Path
import argparse,json

p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path);p.add_argument('--snapshot',action='append',default=[],help='Verify only this exact packaged snapshot; repeat for multiple new packages. Omit to verify all.');args=p.parse_args()
requested=set(args.snapshot)
assert all(len(h)==64 and all(c in '0123456789abcdef' for c in h) for h in requested),'Expected exact lowercase SHA256 values'
base=Path(__file__).parent
results=[]
for receipt_path in sorted((base/'packages').glob('*/*/PACKAGE.json')):
    out=receipt_path.parent;receipt=r.read(receipt_path)
    if requested and receipt['snapshot_sha256'] not in requested:continue
    for relative,h in receipt['files'].items():
        path=out/relative
        assert path.resolve().is_relative_to(out.resolve()),relative
        assert r.sha(path.read_bytes())==h,relative
    j=r.read(out/'job'/'JOB.json')
    assert all(j[k]==v for k,v in r.hashes().items())
    meta,rows=r.source(args.source_root or j['source_root'],out/'job'/'source_manifest.json',j['tractate'])
    assert meta['source_sha256']==j['source_sha256']
    segments={x['id']:x for x in rows}
    h=receipt['snapshot_sha256'];raw=(out/'job'/'snapshots'/(h+'.json')).read_bytes()
    assert r.sha(raw)==h
    accepted=json.loads(raw);state=r.empty()
    for ph in accepted['proposals']:
        proposal=(out/'job'/'proposals'/(ph+'.json')).read_bytes();assert r.sha(proposal)==ph
        previous=state['proposals'];state=r.validate_apply(state,json.loads(proposal),segments,j);state['proposals']=previous+[ph]
    assert r.encoded(state)==raw
    by={x['id']:x for x in state['records']}
    for x in state['records']:
        if x['release_state']=='valid' and x['layer']=='attributions' and x['content']['scope'] in by:
            assert by[x['content']['scope']]['release_state']=='valid',x['id']
    export=out/'export';expected={}
    for layer in r.LAYERS[:-1]:expected[layer+'.jsonl']=b''.join(r.encoded(x) for x in state['records'] if x['layer']==layer)
    expected['coverage.json']=r.encoded(state['coverage'])
    expected['qualification.json']=r.encoded(dict(snapshot_sha256=h,ml_eligible=False,review_state='unreviewed',policy='no qualification implemented; independent review required'))
    expected['unresolved.json']=r.encoded([dict(id=x['id'],uncertainty=x['uncertainty']) for x in state['records'] if x['uncertainty']])
    active=[x for x in state['records'] if x['release_state']=='valid']
    for structure in [x for x in active if x['layer']=='structure']:
        scope={e['segment_id'] for e in structure['evidence']}
        expected['per_sugya/'+r.sha(structure['id'].encode())+'.json']=r.encoded(dict(structure=structure,records=[x for x in active if any(e['segment_id'] in scope for e in x['evidence'])],selection='segment-overlap context, not semantic containment'))
    manifest=dict(snapshot_sha256=h,**r.report(state,segments),files={k:r.sha(v) for k,v in sorted(expected.items())})
    expected['manifest.json']=r.encoded(manifest)
    assert {x.relative_to(export).as_posix() for x in export.rglob('*') if x.is_file()}==set(expected)
    for relative,raw in expected.items():assert (export/relative).read_bytes()==raw,relative
    results.append(dict(slug=receipt['slug'],snapshot_sha256=h,replay_pass=True,exact_export_pass=True,source_sha256=meta['source_sha256'],completed_by_layer=r.report(state,segments)['completed_by_layer']))
assert results,'No packages selected'
assert not requested or {x['snapshot_sha256'] for x in results}==requested,'Requested snapshot not packaged'
print(json.dumps(dict(engineering_pass=True,scholarly_accuracy_certified=False,requested_snapshots=sorted(requested),packages=results),ensure_ascii=False,indent=2))
