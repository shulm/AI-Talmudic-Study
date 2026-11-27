"""Pinned whole-tractate ingest and deterministic interactive-proposal production."""
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import tempfile
import jsonschema

HERE = Path(__file__).resolve().parent
PIN = '11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c'
VERSION = '2.0.0-production'
LAYERS = ['structure', 'utterances', 'claims', 'attributions', 'questions', 'positions', 'edges', 'reconciliation']
def sha(b): return hashlib.sha256(b).hexdigest()
def encoded(x): return (json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode('utf-8')
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def need(ok, message):
    if not ok: raise ValueError(message)
def hashes(): return {k+'_sha256':sha((HERE/f).read_bytes()) for k,f in [('schema','schema.json'),('protocol','PROTOCOL.md')]}
def immutable(p,b):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=p.parent,prefix='.immutable-')
    try:
        with os.fdopen(fd,'wb') as f: f.write(b); f.flush(); os.fsync(f.fileno())
        try: os.link(tmp,p)
        except FileExistsError: need(p.read_bytes()==b, f'immutable conflict: {p}')
    finally: os.unlink(tmp)
def atomic(p,x):
    p=Path(p); fd,tmp=tempfile.mkstemp(dir=p.parent,prefix='.stage-')
    try:
        with os.fdopen(fd,'wb') as f: f.write(encoded(x)); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,p)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
@contextmanager
def lock(job):
    job=Path(job); job.mkdir(parents=True,exist_ok=True)
    with (job/'.lock').open('a+b') as f:
        f.seek(0); f.write(b'0'); f.flush(); f.seek(0)
        if os.name=='nt':
            import msvcrt
            msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
        else:
            import fcntl
            fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        try: yield
        finally:
            f.seek(0)
            if os.name=='nt': msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1)
            else: fcntl.flock(f,fcntl.LOCK_UN)
def source(root,manifest,tractate):
    need(sha(Path(manifest).read_bytes())==PIN,'unapproved source manifest bytes')
    m=next(x for x in read(manifest)['tractates'] if x['title']==tractate)
    root=Path(root)
    for path,h in [(m['source_path'],m['source_sha256']),(m['schema_path'],m['schema_sha256'])]:
        need(sha((root/path).read_bytes())==h,'source/schema hash mismatch: '+path)
    d=read(root/m['source_path'])
    need(d['title']==tractate and d['versionTitle']=='Wikisource Talmud Bavli' and d['language']=='he','wrong edition')
    rows=[]
    for i,page in enumerate(d['text']):
        need(isinstance(page,list),'invalid page shape')
        for j,t in enumerate(page):
            need(isinstance(t,str),'invalid source string')
            sid='seg_'+sha('|'.join([tractate,d['versionTitle'],str(i),str(j)]).encode())[:20]
            rows.append(dict(id=sid,ref=f'{tractate} {i//2+1}{"a" if i%2==0 else "b"}:{j+1}',source_index=[i,j],text=t,text_sha256=sha(t.encode())))
    need(len(rows)==m['source_segments'],'inventory count mismatch')
    return m,rows
def load(job):
    j=read(job/'JOB.json'); need(all(j[k]==v for k,v in hashes().items()),'tool contract changed')
    m,rows=source(j['source_root'],job/'source_manifest.json',j['tractate'])
    need(j['source_sha256']==m['source_sha256'] and j['source_segments']==len(rows),'JOB source metadata mismatch')
    return j,{r['id']:r for r in rows}
def init(job,root,manifest,tractate,owner,epoch):
    job=Path(job)
    m,rows=source(root,manifest,tractate)
    with lock(job):
        if (job/'JOB.json').exists():
            existing,ss=load(job)
            need(existing['tractate']==tractate and existing['source_root']==str(Path(root).resolve()),'job identity conflict')
            authorize(job,owner,epoch)
            return dict(tractate=tractate,source_segments=len(ss),resumed=True,**hashes())
        immutable(job/'source_manifest.json',Path(manifest).read_bytes())
        immutable(job/'source_inventory.json',encoded(rows))
        atomic(job/'OWNER.json',dict(owner=owner,epoch=epoch))
        immutable(job/'JOB.json',encoded(dict(schema_version=VERSION,tractate=tractate,source_root=str(Path(root).resolve()),source_sha256=m['source_sha256'],source_segments=len(rows),metadata=m['metadata'],**hashes())))
    return dict(tractate=tractate,source_segments=len(rows),**hashes())
def empty(): return dict(records=[],coverage=[],open_tails=[],proposals=[],review_state='unreviewed',ml_eligible=False)
def current(job):
    if not (job/'CURRENT.json').exists(): return empty()
    h=read(job/'CURRENT.json')['snapshot_sha256']; b=(job/'snapshots'/f'{h}.json').read_bytes()
    need(sha(b)==h,'corrupt checkpoint'); return json.loads(b)
def validate_apply(state,p,segments,j):
    jsonschema.Draft202012Validator(read(HERE/'schema.json')).validate(p)
    for k in ['tractate','source_sha256','schema_sha256','protocol_sha256']: need(p[k]==j[k],'proposal contract mismatch '+k)
    records={r['id']:r for r in state['records']}
    newids=[r['id'] for r in p['records']]
    need(len(set(newids))==len(newids),'duplicate proposal ID')
    for r in p['records']:
        need(r['id'] not in records,'record IDs immutable; use supersedes')
        for e in r['evidence']:
            need(e['segment_id'] in segments,'unknown evidence segment')
            t=segments[e['segment_id']]['text']; a=e['start_char']; b=e['end_char']
            need(0<=a<b<=len(t) and t[a:b]==e['quote'],'invalid original quote/offset')
        records[r['id']]=dict(r,review_state='unreviewed',release_state='valid',ml_eligible=False)
    revised=set()
    for r in p['records']:
        for link in r['links']: need(link in records,'dangling link')
        old=r.get('supersedes')
        if old:
            need(old in records and old!=r['id'] and old not in newids,'invalid revision lineage')
            need(old not in revised and records[old]['release_state']=='valid','ambiguous or stale revision successor')
            revised.add(old)
            need(records[old]['layer']==r['layer'],'revision layer mismatch')
            records[old]=dict(records[old],release_state='superseded')
        c=r['content']
        if r['layer']=='positions':
            need(c['claim_id'] in records and records[c['claim_id']]['layer']=='claims','position claim foreign key')
            if c['question_id']: need(c['question_id'] in records and records[c['question_id']]['layer']=='questions','position question foreign key')
        if r['layer']=='edges':
            for key in ['source_id','target_id']: need(c[key] in records,'edge endpoint absent')
            a,b=[records[c[k]]['layer'] for k in ['source_id','target_id']]
            if c['relation']=='continuation': need(a==b=='structure','continuation endpoints must be structure')
            else: need(a in ['claims','utterances','questions','positions'] and b in ['claims','utterances','questions','positions'],'argument endpoint type')
    for r in records.values():
        if r['release_state']!='valid': continue
        dependencies=list(r['links']); c=r['content']
        if r['layer']=='positions': dependencies += [c['claim_id']] + ([c['question_id']] if c['question_id'] else [])
        if r['layer']=='edges': dependencies += [c['source_id'],c['target_id']]
        need(all(records[d]['release_state']=='valid' for d in dependencies),'active graph references superseded record; revise dependent records')
    expected_tails={r['id'] for r in records.values() if r['release_state']=='valid' and r['layer']=='structure' and r['content']['boundary']!='closed'}
    need(len(p['open_tails'])==len(set(p['open_tails'])) and set(p['open_tails'])==expected_tails,'open tails must exactly match active open structure')
    coverage={(c['segment_id'],c['layer']):c for c in state['coverage']}
    seen=set()
    for c in p['coverage']:
        key=(c['segment_id'],c['layer']); need(key not in seen,'duplicate coverage'); seen.add(key)
        need(c['segment_id'] in segments,'unknown coverage segment')
        done=c['extraction_state']=='completed'
        need(done==(c['extraction_result'] is not None),'extraction state/result mismatch')
        need(bool(c['rationale'].strip()),'coverage requires pass rationale')
        for rid in c['record_ids']:
            need(rid in records and records[rid]['release_state']=='valid','invalid coverage record')
            need(c['layer']=='reconciliation' or records[rid]['layer']==c['layer'],'coverage layer mismatch')
            need(any(e['segment_id']==c['segment_id'] for e in records[rid]['evidence']),'coverage record has no evidence in scope')
        if c['extraction_result']=='records_found': need(bool(c['record_ids']),'records_found without records')
        if c['extraction_result'] in ['none_found_after_pass','not_applicable']: need(not c['record_ids'],'zero-record pass has records')
        coverage[key]=dict(c,proposal_execution=p['execution'])
    # Recheck all completed structure partitions, including effects of revisions.
    for (sid,layer),c in coverage.items():
        need(all(records[rid]['release_state']=='valid' for rid in c['record_ids']),'revision requires replacement of dependent coverage')
        if layer!='structure' or c['extraction_state']!='completed': continue
        intervals=[]
        for r in records.values():
            if r['layer']=='structure' and r['release_state']=='valid' and r['content']['primary']:
                intervals.extend((e['start_char'],e['end_char']) for e in r['evidence'] if e['segment_id']==sid)
        cursor=0
        for a,b in sorted(intervals): need(a==cursor,'structure overlap or gap'); cursor=b
        need(cursor==len(segments[sid]['text']),'structure partition incomplete')
    return dict(records=sorted(records.values(),key=lambda r:r['id']),coverage=[coverage[k] for k in sorted(coverage)],open_tails=p['open_tails'],proposals=state['proposals'],review_state='unreviewed',ml_eligible=False)
def authorize(job,owner,epoch): need(read(job/'OWNER.json')==dict(owner=owner,epoch=epoch),'stale owner/epoch')
def submit(job,proposal,owner,epoch,fail_before_pointer=False):
    job=Path(job); raw=Path(proposal).read_bytes(); h=sha(raw)
    with lock(job):
        authorize(job,owner,epoch); j,segments=load(job)
        immutable(job/'proposals'/f'{h}.json',raw)
        p=json.loads(raw); need(p['owner']==owner and p['epoch']==epoch,'proposal ownership mismatch')
        old=current(job)
        if h in old['proposals']: return dict(snapshot_sha256=sha(encoded(old)),idempotent=True)
        new=validate_apply(old,p,segments,j); new['proposals']=old['proposals']+[h]
        b=encoded(new); sh=sha(b); immutable(job/'snapshots'/f'{sh}.json',b)
        if fail_before_pointer: raise RuntimeError('injected interruption before checkpoint promotion')
        atomic(job/'CURRENT.json',dict(snapshot_sha256=sh))
        return dict(snapshot_sha256=sh,proposal_sha256=h,coverage=report(new,segments))
def report(s,segments):
    completed={(c['segment_id'],c['layer']) for c in s['coverage'] if c['extraction_state']=='completed'}
    return dict(source_segments=len(segments),semantic_records=len(s['records']),completed_by_layer={l:sum(c['layer']==l and c['extraction_state']=='completed' for c in s['coverage']) for l in LAYERS},outcomes_by_layer={l:{outcome:sum(c['layer']==l and c['extraction_result']==outcome for c in s['coverage']) for outcome in ['records_found','none_found_after_pass','abstained_ambiguous','not_applicable']} for l in LAYERS},independent_review_completed=False,tractate_delivered=False,next_unprocessed_by_layer={l:next((r['ref'] for sid,r in segments.items() if (sid,l) not in completed),None) for l in LAYERS})
def replay(job):
    job=Path(job)
    with lock(job):
        j,segments=load(job); accepted=current(job); s=empty()
        for h in accepted['proposals']:
            b=(job/'proposals'/f'{h}.json').read_bytes(); need(sha(b)==h,'proposal hash corruption')
            previous=s['proposals']; s=validate_apply(s,json.loads(b),segments,j); s['proposals']=previous+[h]
        need(encoded(s)==encoded(accepted),'replay differs from accepted checkpoint')
        return dict(replay_pass=True,snapshot_sha256=sha(encoded(s)),**report(s,segments))
def migrate(job,legacy,owner,epoch):
    job=Path(job); legacy=Path(legacy)
    with lock(job):
        authorize(job,owner,epoch)
        j,segments=load(job); mappings=[]; files=[]
        for p in sorted((legacy/'data').glob('*.jsonl')):
            raw=p.read_bytes(); h=sha(raw); immutable(job/'legacy'/f'{h}.jsonl',raw); files.append(dict(path=p.name,sha256=h))
            for line in raw.decode('utf-8-sig').splitlines():
                r=json.loads(line)
                if r.get('tractate') not in [None,j['tractate']]: continue
                if p.stem=='segments':
                    need(r['id'] in segments and r['text']==segments[r['id']]['text'] and r['source_sha256']==j['source_sha256'],'legacy source mismatch')
                mappings.append(dict(table=p.stem,legacy_id=r.get('id'),record_sha256=sha(encoded(r)),production_id=r.get('id') if p.stem=='segments' else None,relationship='equivalent' if p.stem=='segments' else 'unmapped',reason='exact preserved source ID' if p.stem=='segments' else 'preserved legacy selected record; explicit semantic reannotation required'))
        out=dict(schema_version=VERSION,files=files,mappings=mappings,loss_report=['New interval structure, utterances, claims, and expanded attribution cannot be represented by v1; compatibility export preserves originals only.','Legacy semantic coverage does not count as completed production layers.'])
        h=sha(encoded(out)); immutable(job/'migrations'/f'{h}.json',encoded(out)); return dict(migration_sha256=h,files=len(files),records=len(mappings))
def export(job,output):
    job=Path(job); output=Path(output)
    with lock(job):
        j,segments=load(job); s=current(job); version=sha(encoded(s))
        # Bind generated views to one immutable authoritative version.
        for layer in LAYERS[:-1]:
            immutable(output/f'{layer}.jsonl',b''.join(encoded(r) for r in s['records'] if r['layer']==layer))
        immutable(output/'coverage.json',encoded(s['coverage']))
        immutable(output/'qualification.json',encoded(dict(snapshot_sha256=version,ml_eligible=False,review_state='unreviewed',policy='no qualification implemented; independent review required')))
        immutable(output/'unresolved.json',encoded([dict(id=r['id'],uncertainty=r['uncertainty']) for r in s['records'] if r['uncertainty']]))
        active=[r for r in s['records'] if r['release_state']=='valid']
        for sug in [r for r in active if r['layer']=='structure']:
            scopes={e['segment_id'] for e in sug['evidence']}
            rows=[r for r in active if any(e['segment_id'] in scopes for e in r['evidence'])]
            immutable(output/'per_sugya'/f'{sha(sug["id"].encode())}.json',encoded(dict(structure=sug,records=rows,selection='segment-overlap context, not semantic containment')))
        receipt=dict(snapshot_sha256=version,**report(s,segments),files={p.relative_to(output).as_posix():sha(p.read_bytes()) for p in sorted(output.rglob('*')) if p.is_file() and p.name!='manifest.json'})
        immutable(output/'manifest.json',encoded(receipt)); return receipt
def main():
    a=argparse.ArgumentParser(); sub=a.add_subparsers(dest='cmd',required=True)
    for name in ['init','submit','replay','migrate','handoff','packet','export','compatibility-export']:
        p=sub.add_parser(name); p.add_argument('--job-dir',type=Path,required=True)
        if name in ['init','submit','handoff','migrate']: p.add_argument('--owner',required=True); p.add_argument('--epoch',type=int,required=True)
        if name=='init':
            p.add_argument('--source-root',type=Path,required=True); p.add_argument('--manifest',type=Path,required=True); p.add_argument('--tractate',required=True)
        if name=='submit': p.add_argument('--proposal',type=Path,required=True)
        if name=='migrate': p.add_argument('--legacy-dir',type=Path,required=True)
        if name=='handoff': p.add_argument('--new-owner',required=True)
        if name=='packet': p.add_argument('--start-ref',required=True); p.add_argument('--end-ref',required=True); p.add_argument('--output',type=Path,required=True)
        if name in ['export','compatibility-export']: p.add_argument('--output',type=Path,required=True)
        if name=='compatibility-export': p.add_argument('--migration-sha256',required=True)
    x=a.parse_args(); j=x.job_dir
    if x.cmd=='init': result=init(j,x.source_root,x.manifest,x.tractate,x.owner,x.epoch)
    elif x.cmd=='submit': result=submit(j,x.proposal,x.owner,x.epoch)
    elif x.cmd=='replay': result=replay(j)
    elif x.cmd=='migrate': result=migrate(j,x.legacy_dir,x.owner,x.epoch)
    elif x.cmd=='export': result=export(j,x.output)
    elif x.cmd=='compatibility-export':
        with lock(j):
            need(len(x.migration_sha256)==64 and all(c in '0123456789abcdef' for c in x.migration_sha256),'invalid migration hash')
            b=(j/'migrations'/f'{x.migration_sha256}.json').read_bytes(); need(sha(b)==x.migration_sha256,'corrupt migration')
            migration=json.loads(b)
            for f in migration['files']:
                raw=(j/'legacy'/f'{f["sha256"]}.jsonl').read_bytes(); need(sha(raw)==f['sha256'],'corrupt legacy bytes'); need(Path(f['path']).name==f['path'],'invalid compatibility path'); immutable(x.output/f['path'],raw)
            immutable(x.output/'loss_report.json',encoded(migration['loss_report'])); result=dict(files=len(migration['files']),migration_sha256=x.migration_sha256)
    elif x.cmd=='handoff':
        with lock(j):
            authorize(j,x.owner,x.epoch); result=dict(owner=x.new_owner,epoch=x.epoch+1); immutable(j/'ownership_history'/f'{x.epoch}.json',encoded(read(j/'OWNER.json'))); atomic(j/'OWNER.json',result)
    else:
        meta,ss=load(j); rows=list(ss.values()); refs=[r['ref'] for r in rows]; lo=refs.index(x.start_ref); hi=refs.index(x.end_ref); need(lo<=hi,'reversed packet'); result=dict(job=meta,segments=rows[lo:hi+1]); immutable(x.output,encoded(result))
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
