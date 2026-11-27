"""Capture an exact, partial checkpoint without touching authoritative data.

Copies only accepted annotations/proposals and metadata, never source corpora.
Usage: python package_checkpoint.py TRACTATE_SLUG
"""
from author_remaining_openings_001 import r
from pathlib import Path
import sys

slug=sys.argv[1]
assert slug in ['taanit','bava_batra','pesachim','avodah_zarah','nedarim','moed_katan','makkot']
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04')/('bavli_'+slug)
pointer=r.read(job/'CURRENT.json');h=pointer['snapshot_sha256']
raw=(job/'snapshots'/(h+'.json')).read_bytes();assert r.sha(raw)==h
state=r.read(job/'snapshots'/(h+'.json'))
out=Path(__file__).parent/'packages'/slug/h
for name in ['JOB.json','OWNER.json','source_manifest.json']:
    r.immutable(out/'job'/name,(job/name).read_bytes())
r.immutable(out/'job'/'CURRENT.json',r.encoded(pointer))
r.immutable(out/'job'/'snapshots'/(h+'.json'),raw)
for ph in state['proposals']:
    raw=(job/'proposals'/(ph+'.json')).read_bytes();assert r.sha(raw)==ph
    r.immutable(out/'job'/'proposals'/(ph+'.json'),raw)
replay=r.replay(out/'job');assert replay['snapshot_sha256']==h
export=r.export(out/'job',out/'export');assert export['snapshot_sha256']==h
by={x['id']:x for x in state['records']}
stale_scopes=[x['id'] for x in state['records'] if x['release_state']=='valid' and x['layer']=='attributions' and x['content']['scope'] in by and by[x['content']['scope']]['release_state']!='valid']
assert not stale_scopes,stale_scopes
receipt=dict(slug=slug,snapshot_sha256=h,source_sha256=r.read(job/'JOB.json')['source_sha256'],owner=r.read(job/'OWNER.json'),replay=replay,export_manifest_sha256=r.sha((out/'export'/'manifest.json').read_bytes()),active_records=sum(x['release_state']=='valid' for x in state['records']),superseded_records=sum(x['release_state']=='superseded' for x in state['records']),open_tails=state['open_tails'],stale_exact_id_attribution_scopes=stale_scopes,tractate_delivered=False,ml_eligible=False,human_certified=False,qualification='Partial source extraction; review artifacts apply only to their explicitly named versions and cohorts. No full-tractate review acceptance.',files={p.relative_to(out).as_posix():r.sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file() and p.name not in ['.lock','PACKAGE.json']})
r.immutable(out/'PACKAGE.json',r.encoded(receipt))
print(slug,h,replay['completed_by_layer'],out)
