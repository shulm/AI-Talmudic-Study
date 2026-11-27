"""Read-only exact-prefix verification; creates no production files."""
import sys,hashlib,collections,json
sys.dont_write_bytecode=True
import meilah_supplement003b_inspect as z
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def binding(p):return {'path':str(p),'sha256':sha(p)}
def verify():
 assert sha(z.B/'readings/meilah_supplement003b.json')=='2496b2453df2468775c3833af887cbbbe1bda76e0137e610f8529b451fbafa51'
 assert sha(z.J/'snapshots'/f'{z.H}.json')==z.H
 for b in [z.a['neutral_job_binding'],z.a['source_binding']]+z.a['common_document_bindings']:
  assert sha(z.pathlib.Path(b['path']))==b['sha256'],b
 counts={}
 for label,records in [('reader',z.r),('snapshot',z.p['records'])]:
  n=0
  for x in records:
   for e,ref in zip(x['evidence'],z.refs(x)):
    assert z.texts[ref][e['start_char']:e['end_char']]==e['quote'],(label,x['id'],ref)
    n+=1
  counts[label+'_exact_evidence']=n
 s=z.m.empty()
 for h in z.p['proposals']:
  path=z.J/'proposals'/f'{h}.json';assert sha(path)==h
  prior=s['proposals'];s=z.m.validate_apply(s,z.read(path),z.segs,z.j);s['proposals']=prior+[h]
 assert z.m.encoded(s)==z.m.encoded(z.p)
 assert z.m.sha(z.m.encoded(s))==z.H
 cores=set(z.a['core_refs']);layers=sorted({x['layer'] for x in z.r})
 completed={l:{z.segs[c['segment_id']]['ref'] for c in z.p['coverage'] if c['layer']==l and c['extraction_state']=='completed'} for l in layers}
 assert all(cores<=v for v in completed.values())
 active=[x for x in z.p['records'] if x.get('release_state')=='valid' and cores.intersection(z.refs(x))]
 return dict(counts,proposal_count=len(s['proposals']),replay='PASS_exact_canonical_bytes',completed_by_layer={l:len(v) for l,v in completed.items()},compared_by_layer={l:len(cores&v) for l,v in completed.items()},reader_records_by_layer=dict(collections.Counter(x['layer'] for x in z.r)),producer_intersecting_records_by_layer=dict(collections.Counter(x['layer'] for x in active)))
if __name__=='__main__':print(json.dumps(verify(),ensure_ascii=False))
