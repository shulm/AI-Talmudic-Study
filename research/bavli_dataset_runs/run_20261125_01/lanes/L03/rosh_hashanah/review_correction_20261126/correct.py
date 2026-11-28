import json,hashlib,copy,sys,importlib.util
from pathlib import Path
HERE=Path(__file__).parent
REPO=HERE.parents[5]
while not (REPO/'research/bavli_production_v1/runner.py').exists(): REPO=REPO.parent
spec=importlib.util.spec_from_file_location('runner',REPO/'research/bavli_production_v1/runner.py'); runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah')
BASE='73e6ef36b8a8df4f14fc006202501b4bfbeee0589919f8ad4c8330c7f3103592'
sha=lambda b:hashlib.sha256(b).hexdigest()
cp=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/comparisons/rosh_hashanah_batch001_exact_version.json')
raw=cp.read_bytes(); assert sha(raw)=='068d0b0e2321796a6ae4106025dc7c36b70b258a7343453bb6324ce360a38e8d'
cmp=json.loads(raw); rb=Path(cmp['reader_path']).read_bytes(); assert sha(rb)==cmp['reader_sha256']
for name,b in [('comparison_frozen.json',raw),('reader_frozen.json',rb)]:
 target=HERE/name
 if target.exists():assert target.read_bytes()==b
 else:target.write_bytes(b)
assert json.loads((J/'OWNER.json').read_text())=={'owner':'L03/rosh_hashanah','epoch':3}
assert json.loads((J/'CURRENT.json').read_text())['snapshot_sha256']==BASE
job,segs=runner.load(J);state=runner.current(J);old={r['id']:r for r in state['records'] if r['release_state']=='valid'}
byref={s['ref'].replace('Rosh Hashanah ',''):s for s in segs.values()}
reader={r['id']:r for r in json.loads(rb)['records']}
# Read/validate all frozen evidence and exact comparison record identities, not excerpts.
for r in reader.values():
 for e in r['evidence']:
  s=byref[e['ref'].replace('Rosh Hashanah ','')];assert s['text'][e['start_char']:e['end_char']]==e['quote']
for item in cmp['claim_comparisons']:
 assert sha(json.dumps(reader[item['reader_id']],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())==item['reader_record_sha256']
 for rid,h in item['producer_record_sha256'].items():assert sha(json.dumps(old[rid],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())==h
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah/review_correction_20261126','model_id':None},records=[],coverage=[],open_tails=state['open_tails'])
new={};mapping={};lineage={}
def evidence(ref,quote=None):
 s=byref[ref];q=s['text'] if quote is None else quote;a=s['text'].index(q)
 return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(key,layer,content,ev,origin='source_paraphrase',links=(),supersedes=None):
 rid='rh.e3.review20261126.'+key
 r=dict(id=rid,layer=layer,content=content,evidence=ev,origin=origin,uncertainty=[],links=list(links))
 if supersedes:r['supersedes']=supersedes;mapping[supersedes]=rid
 new[rid]=r;return rid
def revise(rid,**changes):
 if rid in mapping:r=new[mapping[rid]]
 else:
  r={k:copy.deepcopy(v) for k,v in old[rid].items() if k not in ['review_state','release_state','ml_eligible','supersedes']}
  r['id']='rh.e3.review20261126.rev.'+rid;r['supersedes']=rid;mapping[rid]=r['id'];new[r['id']]=r
 for k,v in changes.items():r[k]=v
 return r
def claim(key,text,ref,quote=None,holder='anonymous discussion',conditions=(),supersedes=None):
 rid=add(key,'claims',dict(proposition=text,conditions=list(conditions),scope='Bounded reviewed source occurrence; no final practical ruling or task eligibility inferred',assertion_mode='asserted'),[evidence(ref,quote)],supersedes=supersedes)
 if supersedes:
  pos=next(r for r in old.values() if r['layer']=='positions' and r['content']['claim_id']==supersedes)
  pr=revise(pos['id']);pr['content'].update(claim_id=rid,holder_candidates=[holder],conditions=list(conditions),local_status='Asserted in this occurrence; continuation qualifications preserved');pr['evidence']=[evidence(ref,quote)];pr['links']=[rid]
 else:add(key+'.pos','positions',dict(claim_id=rid,question_id=None,holder_candidates=[holder],conditions=list(conditions),local_status='Asserted in this occurrence; no final ruling inferred'),[evidence(ref,quote)],links=[rid])
 return rid
def edge(key,src,tgt,ref,relation='support',quote=None,editorial=False):
 return add(key,'edges',dict(source_id=src,target_id=tgt,relation=relation,explicitness='editorial_reconstruction' if editorial else 'source_explicit'),[evidence(ref,quote)],origin='editorial_inference' if editorial else 'source_paraphrase',links=[src,tgt])
# Distinct occurrences: primary replacement retains original occurrence; added claim retains repeated lemma.
for name,first,repeat,quote in [('adar','2a:7','2a:8','מלך שעמד בעשרים ותשעה באדר כיון שהגיע אחד בניסן עלתה לו שנה'),('nisan','2a:7','2b:1','ואם לא עמד אלא באחד בניסן אין מונין לו שנה עד שיגיע ניסן אחר')]:
 oid='rh.kings.pass1.c.'+name;r=revise(oid);r['evidence']=[evidence(first,quote)]
 pos=revise('rh.kings.pass1.p.'+name);pos['evidence']=[evidence(first,quote)]
 cr=claim(name+'.repeat',old[oid]['content']['proposition'],repeat,quote,holder='anonymous baraita quoted by discussion',conditions=old[oid]['content']['conditions'])
 lineage[oid]=[r['id'],cr]
 if name=='adar':
  for eid in ['rh.kings.pass1.teaching1','rh.kings.pass1.teaching2']:
   er=revise(eid);er['content']['source_id']=cr;er['links']=[cr,er['content']['target_id']]
 else:
  er=revise('rh.kings.pass1.rejecttwo');er['content'].update(source_id=cr);er['links']=[cr,er['content']['target_id']]
pr=revise('rh.kings.pass1.p.hyp_two');pr['content']['local_status']='Rejected hypothesis: prior Adar selection does not count two years when accession occurs in Nisan.'
resolution=claim('selection.resolution','Prior Adar selection does not produce the proposed two-year count for accession in Nisan.','2b:2',holder='anonymous discussion',conditions=['Appointment in Adar','Accession in Nisan'])
er=revise('rh.kings.pass1.rejecttwo');er['content'].update(source_id=resolution,relation='correction');er['links']=[resolution,er['content']['target_id']]
# Decompose reviewer-identified bundles while retaining a one-to-one primary revision and separately recorded split lineage.
rab=claim('jonah.use','The sages use the festivals verse for Rabbi Yonah’s teaching.','4b:9','ורבנן ההוא לכדרבי יונה',holder='רבנן as reported by discussion',supersedes='rh.e3.b007.c20')
jon1=claim('jonah.comparison','All the festivals are compared with one another.','4b:9','הוקשו כל המועדים כולם זה לזה',holder='רבי יונה')
jon2=claim('jonah.atonement','All the festivals atone for impurity of the sanctuary and its sacred things.','4b:9','שכולן מכפרים על טומאת מקדש וקדשיו',holder='רבי יונה')
lineage['rh.e3.b007.c20']=[rab,jon1,jon2];edge('jonah.inference',jon1,jon2,'4b:9','support')
cr=revise('rh.e3.b007.c21');cr['content']['conditions']=['Sukkot has passed']
pr=revise('rh.e3.b007.c21.pos');pr['content']['conditions']=['Sukkot has passed']
use=claim('festival.list.use','Rabbi Meir and Rabbi Eliezer ben Jacob use the festival list for the Shavuot make-up-period teaching.','4b:11','מיבעי להו לכדרבי אלעזר אמר ר\' אושעיא',holder='רבי מאיר and רבי אליעזר בן יעקב as explained by discussion')
prem=claim('passover.premise','Passover has a seven-day period for make-up offerings.','4b:11','מה חג המצות יש לו תשלומין כל שבעה',holder='רבי אושעיא, reported by רבי אלעזר')
add('passover.chain','attributions',dict(surface='רבי אלעזר אמר רבי אושעיא',role='transmitter',candidates=['רבי אלעזר'],scope='Passover premise and Shavuot conclusion',transmission_chain=['רבי אלעזר','רבי אושעיא']),[evidence('4b:11',"דאמר ר' אלעזר אמר ר' אושעיא")],links=[prem,'rh.e3.b007.c22'])
edge('passover.analogy',prem,'rh.e3.b007.c22','4b:11','analogy');edge('list.answer',use,'rh.e3.b007.q8','4b:11','answer')
cons=claim('eighth.compensation','For make-up offerings all agree the eighth day compensates for the first.','4b:13','אבל לעניין תשלומין דברי הכל תשלומין דראשון הוא',supersedes='rh.e3.b007.c24')
mn=claim('eighth.mnemonic','The eighth day is independent for the matters denoted by פז״ר קש״ב.','4b:13','אימור דאמרינן שמיני רגל בפני עצמו לענין פז"ר קש"ב')
lineage['rh.e3.b007.c24']=[cons,mn];edge('mnemonic.qualifies',mn,'rh.e3.b007.c23','4b:13','qualification')
last=claim('makeup.last','One who did not offer on the first festival day may offer on the last festival day too.','4b:14','מי שלא חג יום טוב הראשון של חג חוגג את כל הרגל ויום טוב האחרון של חג',holder='quoted anonymous Mishnah',conditions=['Did not offer on first festival day'],supersedes='rh.e3.b007.c25')
through=claim('makeup.throughout','One who did not offer on the first festival day may offer throughout the festival.','4b:14','מי שלא חג יום טוב הראשון של חג חוגג את כל הרגל',holder='quoted anonymous Mishnah',conditions=['Did not offer on first festival day'])
lineage['rh.e3.b007.c25']=[last,through];edge('throughout.support',through,cons,'4b:14')
small=claim('inference.smaller','Taking the smaller amount secures the inference.','4b:15','תפשת מועט תפשת',supersedes='rh.e3.b007.c26')
large=claim('inference.larger','Taking the larger amount does not secure the inference.','4b:15','תפשת מרובה לא תפשת')
lineage['rh.e3.b007.c26']=[small,large]
edge('larger.objection',large,'rh.e3.b007.q10','4b:15','answer')
# Reconstructed common questions do not assert complete or qualified answer sets.
def common(key,text,refs,cids,cumulative=False):
 qid=add(key,'questions',dict(formulation=text,question_origin='editorial_reconstruction',conditions=[],answer_set_status='topic_inventory'),[evidence(r) for r in refs],origin='editorial_inference')
 new[qid]['uncertainty']=['Editorial grouping only; no independently certified exhaustive/comparable choice set.']+(['Cumulative teachings, not competing alternatives.'] if cumulative else [])
 for cid in cids:
  for pos in old.values():
   if pos['layer']=='positions' and pos['content']['claim_id']==cid:
    pr=revise(pos['id']);pr['content']['question_id']=qid;pr['links']=list(dict.fromkeys(pr['links']+[qid]))
 return qid
common('q.animal','When does the animal-tithe year begin?',['2a:2'],['rh.opening1.c.animal','rh.opening1.c.animal_alt'])
common('q.tree','When does the tree year begin?',['2a:4'],['rh.opening1.c.tree_bs','rh.opening1.c.tree_bh'])
common('q.teachings','What does the Adar-accession case teach?',['2a:8','2b:1'],['rh.kings.pass1.c.newyear','rh.kings.pass1.c.day'],True)
common('q.deadline','What festival threshold triggers delay liability in this baraita?',['4b:1','4b:2'],['rh.e3.b007.c'+str(i) for i in range(9,14)])
edge('kings.qualify','rh.e3.b006.c1','rh.opening1.c.kings','3a:14','qualification')
edge('festivals.qualify','rh.e3.b007.c1','rh.opening1.c.festivals','4a:12','qualification')
# Transitively revise graph dependencies; no valid row may retain a superseded endpoint.
changed=True
while changed:
 changed=False
 for rid,r in old.items():
  if rid in mapping:continue
  dependencies=r['links']+[r['content'][k] for k in ['claim_id','question_id','source_id','target_id'] if r['content'].get(k)]
  if any(d in mapping for d in dependencies):revise(rid);changed=True
for r in new.values():
 r['links']=[mapping.get(x,x) for x in r['links']]
 for k in ['claim_id','question_id','source_id','target_id']:
  if r['content'].get(k):r['content'][k]=mapping.get(r['content'][k],r['content'][k])
p['records']=list(new.values())
active={k:v for k,v in old.items() if k not in mapping};active.update(new)
# Rebuild coverage references only on already-completed segment/layer cells.
for cv in state['coverage']:
 if cv['extraction_state']!='completed':continue
 sid,layer=cv['segment_id'],cv['layer'];ids=[r['id'] for r in active.values() if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
 if set(ids)!=set(cv['record_ids']):
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Bounded source-rechecked review correction: refresh atomic/repeated occurrences, editorial question links and dependent edges; no new source-pass scope.'))
runner.validate_apply(state,p,segs,job)
(HERE/'proposal.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
response=dict(status='PRODUCER_CORRECTIONS_PROVISIONAL_NOT_INDEPENDENT_ACCEPTANCE',comparison_sha256=sha(raw),reader_sha256=sha(rb),base_snapshot=BASE,proposal_sha256=sha((HERE/'proposal.json').read_bytes()),split_lineage=lineage,revision_map=mapping,no_new_coverage=True,reviewer_caveats=cmp['reader_corrections'],deferred=['Schema lacks typed split-lineage and repeated-occurrence relation: explicit split_lineage in response preserves one-to-many history; supersedes supplies one primary successor.','Common questions use topic_inventory, not a certified comparable answer-set policy; qualification remains false.'],findings=[])
for group in ['claim_comparisons','question_comparisons','edge_comparisons','context_edge_comparisons']:
 for item in cmp[group]:
  rid=item['reader_id'];desc=item.get('note','');disposition='Retained existing source-faithful representation; no automatic import of reader wording.'
  if rid in ['c18','c21','c24','c27','c28','c29','c30','c31','c33','c36','c37','c38','c39','c40','c41','q01','q02','q04','q06','e04','e05','e06','e09','e13','e14']:disposition='Supported representation correction included; see revision_map, split_lineage and proposal evidence.'
  if rid in ['c01','c20','q07','e07']:disposition='Reader caveat preserved: retain producer scope/typing; do not adopt overstrong count, unscoped year rule, generalized explicit question, or source-explicit objection.'
  if rid=='c33':disposition='Added separate Passover premise and analogy, preserving Elazar-to-Oshaya transmission rather than reader empty chain.'
  response['findings'].append(dict(group=group,reader_id=rid,comparison_note=desc,disposition=disposition))
(HERE/'response_pre_submit.json').write_text(json.dumps(response,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'new_records':len(new),'superseded':len(mapping),'coverage_cells_refreshed':len(p['coverage']),'proposal_sha256':response['proposal_sha256'],'all_comparison_findings_disposed':len(response['findings'])}))
