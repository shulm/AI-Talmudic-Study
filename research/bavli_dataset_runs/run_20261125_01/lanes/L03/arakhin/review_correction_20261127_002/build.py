import json,pathlib,copy,hashlib
D=pathlib.Path(__file__).parent;J=pathlib.Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');base='12a61d3b490ae865f3e631714c93578718741065a7767dece107bf23d5743b6e';assert json.loads((J/'CURRENT.json').read_text())['snapshot_sha256']==base;s=json.loads((J/'snapshots'/f'{base}.json').read_text(encoding='utf8'));old={r['id']:r for r in s['records']};job=json.loads((J/'JOB.json').read_text());inv={r['ref']:r for r in json.loads((J/'source_inventory.json').read_text(encoding='utf8'))};rows=[];pre='ar.e1.r002.'
def ev(ref,quote=None):
 r=inv['Arakhin '+ref];q=quote or r['text'];a=r['text'].index(q);return dict(segment_id=r['id'],start_char=a,end_char=a+len(q),quote=q)
def rev(oid,nid):
 r={k:copy.deepcopy(v) for k,v in old[oid].items() if k not in ['release_state','review_state','ml_eligible']};r['id']=pre+nid;r['supersedes']=oid;rows.append(r);return r
father=rev('ar.e1.b002.c16','father');father['content']['proposition']='Under the second alternative, one of the two remaining קרבנו occurrences excludes the father’s offering.';father['evidence']=[ev('2a:17'),ev('2b:1','חד קרבנו ולא קרבן אביו')]
fp=rev('ar.e1.b002.c16.pos','father.pos');fp['content']['claim_id']=father['id'];fp['evidence']=father['evidence'];fp['links']=[father['id']]
co=copy.deepcopy(father);co['id']=pre+'coowners';co.pop('supersedes');co['content']['proposition']='Under the second alternative, the other remaining קרבנו occurrence includes all joint owners for semikhah.';co['evidence']=[ev('2a:17'),ev('2b:1','ואידך לרבות כל בעלי חוברין לסמיכה')];rows.append(co)
cp=copy.deepcopy(fp);cp['id']=pre+'coowners.pos';cp.pop('supersedes');cp['content']['claim_id']=co['id'];cp['evidence']=co['evidence'];cp['links']=[co['id']];rows.append(cp)
e=rev('ar.e1.b002.e13','father.support');e['content']['target_id']=father['id'];e['links']=[e['content']['source_id'],father['id']]
e2=copy.deepcopy(e);e2['id']=pre+'coowners.support';e2.pop('supersedes');e2['content']['target_id']=co['id'];e2['links']=[e2['content']['source_id'],co['id']];rows.append(e2)
chron=rev('ar.e1.b002.c35','chronology');chron['evidence']=[ev('2b:13'),ev('2b:14'),ev('2b:16')];chron['uncertainty']=['Earlier/later distinction retained without assigning Ravina and inclusion to precise stages beyond explicit text. Context2b14–16 not new completed core coverage.']
pos=rev('ar.e1.b002.c35.pos','chronology.pos');pos['content']['claim_id']=chron['id'];pos['content']['local_status']='Context-anchored distinction: initial alternating service and explicit Beit Hillel retraction to freeing solution; no forced Ravina-stage allocation';pos['links']=[chron['id']];pos['evidence']=chron['evidence'];pos['uncertainty']=chron['uncertainty']
for oid,nid in [('ar.e1.b002.e30','ravina.qualification'),('ar.e1.b002.e31','restored.support')]:
 r=rev(oid,nid);r['content']['source_id']=chron['id'];r['links']=[chron['id'],r['content']['target_id']]
def claim(id,ref,text,holder,status):
 cid=pre+id;es=[ev(ref)];r=dict(id=cid,layer='claims',evidence=es,content=dict(proposition=text,conditions=['Person half slave and half free'],scope='Following Mishnah context only for2b13 earlier/later reconciliation',assertion_mode='asserted'),origin='source_paraphrase',uncertainty=[],links=[]);rows.append(r);rows.append(dict(id=cid+'.pos',layer='positions',evidence=es,content=dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=r['content']['conditions'],local_status=status),origin='source_paraphrase',uncertainty=[],links=[] if False else [cid]));return cid
i=claim('initial','2b:14','The initial Beit Hillel view has the half-slave half-free person work for his master one day and for himself one day.','בית הלל as cited','Initial Mishnah view; explicitly retracted in2b16')
ob=claim('objection','2b:15','Beit Shammai objects that the initial arrangement leaves him unable to marry either a slave woman or a free woman, despite the creation purpose of procreation.','בית שמאי as cited','Objection to initial alternating-service arrangement')
f=claim('freeing','2b:16','For תיקון העולם the master is compelled to free him, and the person writes a debt instrument for half his value.','בית שמאי in the cited continuation','Freeing solution subsequently accepted by Beit Hillel; paired procedural requirement retained')
r=claim('retraction','2b:16','Beit Hillel retracted and ruled in accordance with Beit Shammai.','cited Mishnah reporting בית הלל','Explicit retraction, not permanent opposed outcomes')
def edge(id,refs,a,b,rel):rows.append(dict(id=pre+id,layer='edges',evidence=[ev(x) for x in refs],content=dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),origin='source_paraphrase',uncertainty=[],links=[a,b]))
edge('initial.objection',['2b:15'],ob,i,'objection');edge('initial.retracted',['2b:16'],r,i,'retraction');edge('chronology.context',['2b:13','2b:14','2b:16'],r,chron['id'],'support');edge('freeing.context',['2b:16'],f,chron['id'],'qualification')
# Replace each existing coverage reference to superseded rows, never add context coverage.
replacements={r['supersedes']:[r['id']] for r in rows if r.get('supersedes')};replacements['ar.e1.b002.c16'].append(co['id']);replacements['ar.e1.b002.c16.pos'].append(cp['id']);replacements['ar.e1.b002.e13'].append(e2['id']);coverage=[]
for cv in s['coverage']:
 if any(x in replacements for x in cv['record_ids']):
  x={k:copy.deepcopy(v) for k,v in cv.items() if k!='proposal_execution'};x['record_ids']=[z for rid in cv['record_ids'] for z in replacements.get(rid,[rid])];x['rationale']='AR01/AR02 immutable semantic correction and dependency replacement; no new source coverage.';coverage.append(x)
p=dict(schema_version='2.0.0-production',tractate='Arakhin',owner='/root/lead_l01_l03',epoch=1,source_sha256=job['source_sha256'],protocol_sha256=job['protocol_sha256'],schema_sha256=job['schema_sha256'],execution=dict(route='interactive_agent',agent_id='/root/blind_review',model_id=None),records=rows,coverage=coverage,open_tails=s['open_tails'])
with (D/'PROPOSAL.json').open('x',encoding='utf8') as out:json.dump(p,out,ensure_ascii=False,indent=2)
print(len(rows),hashlib.sha256((D/'PROPOSAL.json').read_bytes()).hexdigest())
