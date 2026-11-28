import json,hashlib,copy
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;base=out.parent/'bounded_001_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir')
r=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
review=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/nazir_review_20261127/VERDICT.json';assert h(review)=='b3f2608959583881d0936a09cbcb56e8aeb358ad836c3057b70765c989c2f63a';v=r(review)
assert r(job/'OWNER.json')=={'owner':'/root/lead_l01_l03','epoch':1};cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur==v['snapshot_sha256'];assert h(job/'snapshots'/(cur+'.json'))==cur
pins=r(base/'PINS.json');assert h(Path(pins['source_path']))==pins['source_sha256'];assert h(Path(pins['source_schema_path']))==pins['source_schema_sha256']
a=r(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert h(cp)==a['contract_sha256']==pins['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
initial=r(base/'INITIAL_PROPOSAL.json');assert h(base/'INITIAL_PROPOSAL.json')==v['proposal_sha256'];state=r(job/'snapshots'/(cur+'.json'));rows={x['id']:x for x in state['records']};inv={s['ref']:s for s in r(job/'source_inventory.json')};raw=r(Path(pins['source_path']))['text']
for s in inv.values():i,j=s['source_index'];assert raw[i][j]==s['text']
p={k:copy.deepcopy(initial[k]) for k in initial if k not in ['records','coverage']};p['records']=[];p['coverage']=[]
selected=set(v['findings'][0]['producer_ids'])|{'naz001.birds_meir','naz001.birds_meir.p','naz001.birds_sages','naz001.birds_sages.p'}
assert len(v['findings'][0]['producer_ids'])==34
# Take transitive dependency closure before replacing IDs.
def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 more={k for k,x in rows.items() if strings([x['content'],x['links']])&selected};new=selected|more
 if new==selected:break
 selected=new
mapping={k:'nazfix001.'+k.removeprefix('naz001.') for k in selected}
def replace(x):
 if isinstance(x,str):return mapping.get(x,x)
 if isinstance(x,list):return [replace(y) for y in x]
 if isinstance(x,dict):return {k:replace(y) for k,y in x.items()}
 return x
for k in sorted(selected):
 x=rows[k];n=replace({f:copy.deepcopy(x[f]) for f in ['id','layer','content','evidence','origin','uncertainty','links']});n['supersedes']=k
 n['uncertainty']=list(dict.fromkeys(u for u in n['uncertainty'] if not u.startswith('Context 3a:11–3b:8 read:')))
 if k in {'naz001.birds_meir','naz001.birds_meir.p'}:
  n['content']['conditions']=['Bird declaration interpreted in the alternative source explanations; no unconditional rule inferred from the bare Mishnah.', 'Rabbi Yohanan: a pure nazirite passes before the speaker (3b:4); even explicit birds-adjacent-to-hair wording still requires a passing nazirite (3b:6).', 'Resh Lakish: birds adjacent to hair in the verse can be intended (3a:11–12); explicit birds-adjacent-to-hair wording works even without a passing nazirite (3b:6).']
  n['uncertainty']=['These are distinct explanations of Rabbi Meir; Rabbi Yohanan’s passing-nazirite condition is not imposed on Resh Lakish.']
 if k in {'naz001.birds_sages','naz001.birds_sages.p'}:n['uncertainty']=['Resh Lakish explains the sages by rejection of adjacency-based designation (3b:1); Rabbi Yohanan says all reject such designation and offers another basis for Rabbi Meir (3b:2).']
 p['records'].append(n)
def ev(ref):
 s=inv[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(k,layer,refs,content,links=None,uncertainty=None):
 rid='nazfix001.context.'+k;p['records'].append(dict(id=rid,layer=layer,evidence=[ev(s) for s in refs],content=content,origin='source_paraphrase',links=list(links or []),uncertainty=list(uncertainty or [])));return rid
def claim(k,refs,text,conditions,holder):
 cid=rec(k,'claims',refs,dict(proposition=text,conditions=list(conditions),scope='Continuation interpretation of opening bird declaration; context only, no added source coverage',assertion_mode='conditional'))
 rec(k+'.p','positions',refs,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(conditions),local_status='Alternative explanation preserved; no choice-task qualification'),[cid]);return cid
def edge(k,refs,x,y,relation):return rec(k,'edges',refs,dict(source_id=x,target_id=y,relation=relation,explicitness='source_explicit'),[x,y])
m=mapping['naz001.birds_meir'];s=mapping['naz001.birds_sages']
l=claim('lakish_meir',['Nazir 3a:11','Nazir 3a:12'],'Resh Lakish explains Rabbi Meir by the speaker accepting the birds adjacent to hair in Daniel; Rabbi Meir allows designation by an adjacent subject.',['Bird declaration construed through scriptural birds/hair adjacency'],'Rabbi Meir as explained by Resh Lakish')
ls=claim('lakish_sages',['Nazir 3b:1'],'In Resh Lakish’s account the sages do not allow designation by a subject merely adjacent in the verse.',['Resh Lakish explanation of the bird declaration'],'sages as explained by Resh Lakish')
y=claim('yohanan',['Nazir 3b:2','Nazir 3b:4'],'Rabbi Yohanan says all reject adjacency-based designation; Rabbi Meir fears that the speaker accepted birds of an impure nazirite, in the case where a pure nazirite passes before him.',['A pure nazirite passes before the speaker; excludes intent merely to pay an already impure nazirite’s offerings','Concern about accepting nazirite obligations, not a statement that the passing nazirite is impure'],'Rabbi Meir as explained by Rabbi Yohanan')
ydiff=claim('yohanan_difference',['Nazir 3b:6'],'For Rabbi Yohanan even explicit birds-adjacent-to-hair wording establishes the nazirite reading only if a nazirite passes before him.',['Speaker explicitly says birds adjacent to hair are upon me','A nazirite passes before him; if none passes the reading does not follow'],'Rabbi Yohanan')
ldiff=claim('lakish_difference',['Nazir 3b:6'],'For Resh Lakish explicit birds-adjacent-to-hair wording establishes the reading even when no nazirite passes before him.',['Speaker explicitly says birds adjacent to hair are upon me','Passing nazirite not required in this explicit-wording case'],'Resh Lakish')
for k,cid,target,refs in [('lakish_qualifier',l,m,['Nazir 2a:3','Nazir 3a:11','Nazir 3a:12']),('sages_qualifier',ls,s,['Nazir 2a:3','Nazir 3b:1']),('yohanan_qualifier',y,m,['Nazir 2a:3','Nazir 3b:2','Nazir 3b:4']),('yohanan_scope',ydiff,m,['Nazir 2a:3','Nazir 3b:6']),('lakish_scope',ldiff,m,['Nazir 2a:3','Nazir 3b:6'])]:edge(k,refs,cid,target,'qualification')
for k,surface,holder,refs,scope in [('lakish','אמר ריש לקיש','Resh Lakish',['Nazir 3a:11','Nazir 3a:12','Nazir 3b:1'],'Explanation of Rabbi Meir and sages through adjacency'),('yohanan','ר\' יוחנן אמר','Rabbi Yohanan',['Nazir 3b:2','Nazir 3b:4'],'Alternative rejecting adjacency and requiring the passing pure nazirite'),('difference','לר\' יוחנן ... לרשב״ל','Rabbi Yohanan and Resh Lakish',['Nazir 3b:6'],'Explicitly attributed differing conditions; not a transmission chain')]:rec('attribution.'+k,'attributions',refs,dict(surface=surface,role='speaker',candidates=[holder] if k!='difference' else ['Rabbi Yohanan','Resh Lakish'],scope=scope,transmission_chain=[]))
# Only existing ten-core coverage, retargeted to revised records; new context edges can attach at core 2a:3.
for c in initial['coverage']:
 n=replace(copy.deepcopy(c))
 if n['segment_id']==inv['Nazir 2a:3']['id'] and n['layer']=='edges':n['record_ids'] += [x['id'] for x in p['records'] if x['layer']=='edges' and x['id'].startswith('nazfix001.context.')];n['extraction_result']='records_found'
 p['coverage'].append(n)
active={k:x for k,x in rows.items() if k not in selected};active.update({x['id']:x for x in p['records']})
for x in active.values():assert not(strings([x['content'],x['links']])&selected),x['id']
for x in p['records']:
 for e in x['evidence']:
  source=next(s for s in inv.values() if s['id']==e['segment_id']);assert source['text'][e['start_char']:e['end_char']]==e['quote']
for k in v['findings'][0]['producer_ids']:assert all('Context 3a:11' not in u for u in active[mapping[k]]['uncertainty'])
assert len(p['coverage'])==80
(out/'PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'CORRECTION_MAP.json').write_text(json.dumps(dict(review_sha256=h(review),initial_snapshot=cur,initial_proposal_sha256=h(base/'INITIAL_PROPOSAL.json'),revisions=mapping,new_context_records=18,unresolved=['N03 editorial shared question/answer-set remains deferred; no scholar-choice admission'],source_sha256=pins['source_sha256'],coverage_increase=0),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(proposal_sha256=h(out/'PROPOSAL.json'),revisions=len(selected),new_records=len(p['records'])-len(selected))))
