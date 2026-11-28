import json,hashlib,sys,copy
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=runner.current(job);assert runner.sha(runner.encoded(base))=='2c734e3e48f6686ab6cece6bd52141c56d7b5c3e5dbe71a485262c5642a83c3b'
j,segs=runner.load(job);src={s['ref']:s for s in segs.values()}; records={r['id']:r for r in base['records'] if r['release_state']=='valid'}
initial=json.loads((out.parent/'bounded_001_20261127/VALIDATED_PROPOSAL.json').read_text(encoding='utf-8'))
p={k:copy.deepcopy(v) for k,v in initial.items() if k not in ['records','coverage']};p.update(records=[],coverage=[])
def ev(ref,q=None):
 s=src[ref];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def new(k,l,e,c,links=None,u=None,origin='source_paraphrase',sup=None):
 r=dict(id='tam001.r1.'+k,layer=l,evidence=e,content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup
 p['records'].append(r);return r['id']
mapping={}
def cl(k,e,prop,holder,old=None,u=None,origin='source_paraphrase'):
 c=new(k,'claims',e,dict(proposition=prop,conditions=[],scope='Targeted clarification of opening-core continuation; no new coverage',assertion_mode='asserted'),u=u,origin=origin,sup=old)
 pos=new(k+'.p','positions',e,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=[],local_status='Local explanation; alternatives remain separate; no final task qualification'),[c],u,origin,sup=old+'.p' if old else None)
 if old:mapping.update({old:c,old+'.p':pos})
 return c
non=cl('nonmixed',[ev('Tamid 27b:4','ואי בעית אימא באותן שאין בהן כלאים')],'The anonymous alternative explains the under-head placement using garments that contain no mixed fibres.','anonymous Gemara','tam001.garment_alternatives',u=['Alternative explanation; does not belong to Rav Ashi.'])
stiff=cl('stiff',[ev('Tamid 27b:4','רב אשי אמר בגדי כהונה קשין הן')],'Rav Ashi explains that priestly garments are stiff.','Rav Ashi',u=['A distinct alternative to the anonymous no-mixed-fibres explanation.'])
felt=cl('felt',[ev('Tamid 27b:4','דאמר רב הונא בריה דרב יהושע הא נמטא גמדא דנרש שריא')],'Rav Huna son of Rav Yehoshua permits the stiff felt of Narsh in the cited precedent.','Rav Huna son of Rav Yehoshua')
verse=cl('verse_separation',[ev('Tamid 26a:7','משה והדר אהרן ובניו שומרי משמרת המקדש')],'The anonymous reading separates Moses from the following Aaron-and-sons clause.','anonymous Gemara','tam001.separate',u=['Further justification and Rav Ashi alternative occur26a8–10; open tail remains.'])
aaron=cl('aaron_one',[ev('Tamid 26a:7','אהרן בחד מקום')],'Aaron is assigned one watch location in this reading.','anonymous Gemara')
sons=cl('sons_two',[ev('Tamid 26a:7','ובניו בשני מקומות')],'His sons are assigned two watch locations in this reading.','anonymous Gemara')
total=cl('count_inference',[ev('Tamid 26a:7','אהרן בחד מקום ובניו בשני מקומות')],'Aaron’s one location plus his sons’ two locations yields three priestly locations.','editorial reconstruction of anonymous argument',origin='editorial_inference')
def edge(k,e,a,b,rel,ex='source_explicit',sup=None):return new(k,'edges',e,dict(source_id=a,target_id=b,relation=rel,explicitness=ex),[a,b],sup=sup)
edge('stiff_qualification',[ev('Tamid 27b:4')],stiff,'tam001.placement','qualification')
edge('felt_support',[ev('Tamid 27b:4')],felt,stiff,'support')
edge('aaron_count',[ev('Tamid 26a:7')],aaron,total,'support','editorial_reconstruction')
edge('sons_count',[ev('Tamid 26a:7')],sons,total,'support','editorial_reconstruction')
new('rav_ashi_attribution','attributions',[ev('Tamid 27b:4','רב אשי אמר')],dict(surface='רב אשי אמר',role='speaker',candidates=['Rav Ashi'],scope='Stiffness explanation only, distinct from preceding anonymous alternative',transmission_chain=[]))
new('nonmixed_attribution','attributions',[ev('Tamid 27b:4','ואי בעית אימא')],dict(surface='ואי בעית אימא',role='anonymous',candidates=[],scope='No-mixed-fibres alternative only',transmission_chain=[]))
# Revise every active dependency transitively and preserve superseded originals.
changed=True
while changed:
 changed=False
 for rid,r in records.items():
  if rid in mapping:continue
  deps=set(r['links'])|{r['content'].get(k) for k in ['claim_id','question_id','source_id','target_id']}
  if deps.intersection(mapping):mapping[rid]='tam001.r1.dep.'+rid.removeprefix('tam001.');changed=True
for old,nid in mapping.items():
 if any(r.get('supersedes')==old for r in p['records']):continue
 r={k:copy.deepcopy(v) for k,v in records[old].items() if k in ['id','layer','evidence','content','origin','uncertainty','links']};r.update(id=nid,supersedes=old)
 r['links']=[mapping.get(v,v) for v in r['links']]
 for k in ['claim_id','question_id','source_id','target_id']:
  if k in r['content']:r['content'][k]=mapping.get(r['content'][k],r['content'][k])
 if old=='tam001.three_basis':r['content']['source_id']=total;r['content']['explicitness']='editorial_reconstruction';r['links']=[total,'tam001.three']
 p['records'].append(r)
for c in base['coverage']:
 n=copy.deepcopy(c); n['record_ids']=[mapping.get(v,v) for v in n['record_ids']]
 for r in p['records']:
  if (n['layer']=='reconciliation' or r['layer']==n['layer']) and any(e['segment_id']==n['segment_id'] for e in r['evidence']) and r['id'] not in n['record_ids']:n['record_ids'].append(r['id'])
 n['extraction_result']='records_found' if n['record_ids'] else 'none_found_after_pass';n['rationale']+=' T01/T02 repair: distinct garment voices and priestly count components source-scoped; no source coverage added.';p['coverage'].append(n)
f=out/'PROPOSAL.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'LINEAGE.json').write_text(json.dumps({'base_snapshot_sha256':runner.sha(runner.encoded(base)),'initial_verdict_sha256':sha(root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/tamid_review_20261127/VERDICT.json'),'mapping':mapping,'required_findings':['T01','T02'],'unchanged_limits':['T03: final benefit ruling not fully encoded; no benefit-QA admission','T04: no shared lottery question/answer-set qualification'],'scope':'Ten cores only;59context not counted'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'proposal_sha256':sha(f),'new_records':len(p['records']),'superseded':len(mapping)}))
