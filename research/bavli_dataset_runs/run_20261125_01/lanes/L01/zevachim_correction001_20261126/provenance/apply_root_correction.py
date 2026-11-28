"""Manually specified atomic splits and semantic dependency repairs; no source expansion."""
from pathlib import Path
import sys,copy
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent;JOB=HERE.parent
BASE='5ad828b4ad2031682bc81f8e065ec769f7b44a73dab0a1bc3651480bf2af3ec8'
j,ss=r.load(JOB);state=r.current(JOB);assert r.sha(r.encoded(state))==BASE
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
rows=[];splits={};revisions={};why={}
def clean(x):
 x=copy.deepcopy(x)
 for k in ['ml_eligible','release_state','review_state','supersedes']:x.pop(k,None)
 return x
def evidence(old,quote):
 for e in active[old]['evidence']:
  t=ss[e['segment_id']]['text']
  if quote in t:
   a=t.index(quote);return [dict(segment_id=e['segment_id'],start_char=a,end_char=a+len(quote),quote=quote)]
 raise ValueError((old,quote))
def split(old,specs):
 out=[]
 for suffix,quote,prop,conditions,mode in specs:
  x=clean(active[old]);x['id']=old+'.r20261126.'+suffix
  x['content'].update(proposition=prop,conditions=conditions,assertion_mode=mode)
  x['evidence']=evidence(old,quote)
  if not out:x['supersedes']=old
  rows.append(x);out.append(x['id'])
 splits[old]=out;revisions[old]=out[0]
def cond(old):return copy.deepcopy(active[old]['content']['conditions'])
split('zev_open_c_valid',[
 ('valid','הזבחים שנזבחו שלא לשמן כשרים','Sacrifices slaughtered under another designation remain valid, apart from the stated exceptions.',cond('zev_open_c_valid'),'asserted'),
 ('obligation','אלא שלא עלו לבעלים לשם חובה','Those sacrifices do not discharge their owners’ obligation.',cond('zev_open_c_valid'),'asserted')])
split('zev_open_c_high',[
 ('higher','שחטן לשם גבוה מהן כשרין','Shimon the brother of Azariah validates slaughter under the designation of an offering of higher sanctity.',['Slaughter under the designation of a higher-sanctity offering'],'asserted'),
 ('lower','לשם נמוך מהן פסולין','Shimon the brother of Azariah invalidates slaughter under the designation of an offering of lower sanctity.',['Slaughter under the designation of a lower-sanctity offering'],'asserted')])
split('zev_open_c_high_examples',[
 ('holy_lower','קדשי קדשים ששחטן לשם קדשים קלים פסולין','Most-holy offerings slaughtered under the designation of lesser-holy offerings are invalid.',['Example continuing Shimon the brother of Azariah','Most-holy offering designated as lesser-holy'],'asserted'),
 ('lesser_higher','קדשים קלים ששחטן לשם קדשי קדשים כשרין','Lesser-holy offerings slaughtered under the designation of most-holy offerings are valid.',['Example continuing Shimon the brother of Azariah','Lesser-holy offering designated as most-holy'],'asserted'),
 ('firstborn_tithe','הבכור והמעשר ששחטן לשם שלמים כשרין','Firstborn and tithe offerings slaughtered under the designation of peace offerings are valid.',['Example continuing Shimon the brother of Azariah','Firstborn or tithe offering designated as peace offering'],'asserted'),
 ('peace_lower','שלמים ששחטן לשם בכור ולשם מעשר פסולין','Peace offerings slaughtered under the designation of firstborn or tithe offerings are invalid.',['Example continuing Shimon the brother of Azariah','Peace offering designated as firstborn or tithe'],'asserted')])
split('zev_open_c_sanctity',[
 ('sanctity','אבל בקדושתייהו קיימי','Failure to discharge the owners’ obligation does not remove the offerings’ sanctity.',cond('zev_open_c_sanctity'),'asserted'),
 ('prohibition','ואסור לשנויי בהו','It is forbidden to continue changing the designation of these offerings.',cond('zev_open_c_sanctity'),'asserted')])
split('zev_baalim_todah',[
 ('todah_valid','תודה ששחטה לשם שלמים כשרה','Abba Chanin in Rabbi Eliezer’s name validates a thanksgiving offering slaughtered as a peace offering.',['Thanksgiving offering slaughtered as a peace offering'],'asserted'),
 ('peace_invalid','שלמים ששחטן לשם תודה פסולה','The same report invalidates a peace offering slaughtered as a thanksgiving offering.',['Peace offering slaughtered as a thanksgiving offering'],'asserted'),
 ('naming','תודה קרויה שלמים ואין שלמים קרויה תודה','The reported distinction is that thanksgiving is called peace offering, whereas peace offering is not called thanksgiving.',['Explanation of the two designation rulings in the same report'],'asserted')])
split('zv.20261126.b3.c10',[
 ('inquiry','לאחר שחיטה לא קא מיבעיא לן','Rava says the inquiry did not concern violations arising after slaughter.',['Local inquiry about positive-commandment violations after designation'],'asserted'),
 ('possible','דכל כמה דלא שחיט בעמוד וסמוך קאי','Until slaughter, laying on hands can still be performed.',['Before slaughter'],'asserted'),
 ('fixed','אימת קא הוי עשה לאחר שחיטה','The omitted laying-on-hands violation becomes fixed after slaughter.',['Laying on hands omitted before slaughter'],'asserted')])
split('zv.20261126.b3.c12a',[
 ('omitted','ואם לא נתן לא כיפר','Rabbi Akiva says atonement does not occur if the remaining oil is not applied.',['Remaining oil application to the head omitted'],'asserted'),
 ('applied','אם נתן כיפר','Rabbi Akiva says atonement occurs if the remaining oil is applied.',['Remaining oil application to the head performed'],'asserted')])
split('zv.20261126.b3.c12b',[
 ('omitted','בין ניתן בין שלא ניתן כיפר','Rabbi Yohanan [ben Nuri] says atonement occurs even if the remaining oil is not applied.',['Remaining oil application to the head omitted'],'asserted'),
 ('applied','בין ניתן בין שלא ניתן כיפר','Rabbi Yohanan [ben Nuri] says atonement occurs when the remaining oil is applied.',['Remaining oil application to the head performed'],'asserted'),
 ('remainder','שירי מצוה הן','Rabbi Yohanan [ben Nuri] characterizes the remaining oil application as a remainder of the commandment.',['Remaining oil application to the head'],'asserted'),
 ('reckoned','ומעלין עליו כאילו לא כיפר','Omission is reckoned as if he had not atoned, despite the stated atonement.',['Remaining oil application to the head omitted','Quoted Rabbi Yohanan [ben Nuri] position'],'asserted')])
for x in rows:
 if x['id'].startswith('zv.20261126.b3.c12b.'):
  x['uncertainty'].append('בן נורי is bracketed in the original source; no independent identity verification claimed.')
split('zv.20261126.b3.c13',[
 ('proposal','אלא כיפר גברא לא כיפר קמי שמיא','The proposed oil interpretation distinguishes personal atonement from atonement before Heaven; 6b:4 supplies a counter-interpretation.',['Interpretation of the quoted as-if-not-atoned formulation'],'challenged'),
 ('no_extra','אילימא דמבעי לאיתויי קרבן אחרינא האמרת בין ניתן בין לא ניתן כיפר','The discussion rejects reading as-if-not-atoned as a requirement to bring another offering, citing atonement whether oil is applied or not.',['Proposed interpretation of the oil Mishnah'],'asserted'),
 ('analogy',"הכא נמי כיפר כו'",'The person/before-Heaven interpretation is proposed as an explanation of the earlier laying-on-hands baraita as well.',['Analogy proposed from the oil Mishnah; counter-interpretation follows'],'challenged')])
# Replace the overlapping oil summary with the explicit discourse act, not another copy of its rulings.
split('zv.20261126.b3.c12',[
 ('citation','מי לא תנן','The oil Mishnah is introduced as cited evidence in the proposed person/before-Heaven interpretation.',['Local proof attempt; counter-reading at6b4'],'asserted')])
x=clean(active['zv.20261126.b3.c11']);x['id']+=' .unused' if False else '.r20261126';x['supersedes']='zv.20261126.b3.c11'
x['content']['assertion_mode']='challenged'
x['content']['scope']='Rav Huna bar Yehuda’s offered interpretation to Rava; the oil analogy used to support it receives a counter-interpretation at6b4. Not a settled conclusion.'
rows.append(x);revisions[x['supersedes']]=x['id'];splits[x['supersedes']]=[x['id']]
oilq='zv.review20261126.q.oil_omitted'
rows.append(dict(id=oilq,layer='questions',evidence=active['zv.20261126.b3.c12a']['evidence'],content=dict(formulation='If the remaining oil application to the head is omitted, does atonement occur?',question_origin='editorial_reconstruction',conditions=['Remaining oil application to the head omitted'],answer_set_status='unreviewed_alternatives'),origin='editorial_inference',uncertainty=['Common question reconstructed to expose the incompatible quoted outcomes; not a certified choice set.'],links=[]))
atom_by_id={x['id']:x for x in rows}
# Expand every position that formerly referred to a split claim; each successor gets the atom's own conditions.
for old,p in active.items():
 if p['layer']!='positions' or p['content']['claim_id'] not in splits:continue
 cs=splits[p['content']['claim_id']];newids=[]
 for n,cl in enumerate(cs):
  x=clean(p);x['id']=old+'.r20261126.'+str(n+1);x['content']['claim_id']=cl
  x['content']['conditions']=atom_by_id[cl]['content']['conditions'];x['evidence']=atom_by_id[cl]['evidence']
  x['links']=[cl]+([p['content']['question_id']] if p['content']['question_id'] else [])
  if n==0:x['supersedes']=old
  if old in ['zv.20261126.b3.p11','zv.20261126.b3.p13']:
   x['content']['local_status']='Proposed interpretation or its stated reasoning; the person/before-Heaven inference is challenged by the alternative oil reading at6b4, not established as a settled conclusion.'
  if cl in [splits['zv.20261126.b3.c12a'][0],splits['zv.20261126.b3.c12b'][0]]:
   x['content']['question_id']=oilq;x['links'].append(oilq)
   x['content']['local_status']='Quoted incompatible atonement outcome under omitted oil; common question editorial, not task-qualified.'
  if p['content']['claim_id']=='zv.20261126.b3.c12b':x['uncertainty']=list(set(x['uncertainty']+atom_by_id[cl]['uncertainty']))
  rows.append(x);newids.append(x['id'])
 revisions[old]=newids[0];splits[old]=newids
# Edge endpoints are deliberately chosen by meaning, rather than by first-successor substitution.
endpoint_overrides={
 'zev_open_e_rava':dict(target_id=splits['zev_open_c_sanctity'][1]),
 'zev_open_e_examples':dict(source_id=splits['zev_open_c_high_examples'][0],target_id=splits['zev_open_c_high'][1]),
 'zv.20261126.b3.e12_11':dict(source_id=splits['zv.20261126.b3.c12b'][3]),
 'zv.20261126.b3.e13_12':dict(target_id=splits['zv.20261126.b3.c12b'][3])}
def replace(value):
 if isinstance(value,str):return revisions.get(value,value)
 if isinstance(value,list):return [replace(v) for v in value]
 if isinstance(value,dict):return {k:replace(v) for k,v in value.items()}
 return value
pending=True
while pending:
 pending=False
 for old,p in active.items():
  if old in revisions:continue
  if replace(p['content'])==p['content'] and not any(k in revisions for k in p['links']):continue
  x=clean(p);x['id']=old+'.r20261126';x['content']=replace(x['content'])
  x['links']=[child for link in p['links'] for child in (splits.get(link,[revisions.get(link,link)]) if p['layer']=='attributions' else [revisions.get(link,link)])]
  if p['layer']=='edges':
   x['content'].update(endpoint_overrides.get(old,{}));x['links']=[x['content']['source_id'],x['content']['target_id']]
  x['supersedes']=old;rows.append(x);revisions[old]=x['id'];splits[old]=[x['id']];pending=True
# Add the remaining individually anchored example edges and the omitted-oil answer relations.
def edge(id,source,target,ev,relation='support',explicitness='source_explicit'):
 rows.append(dict(id=id,layer='edges',evidence=ev,content=dict(source_id=source,target_id=target,relation=relation,explicitness=explicitness),origin='editorial_inference' if explicitness=='editorial_reconstruction' else 'source_paraphrase',uncertainty=[],links=[source,target]))
for n,t in [(1,0),(2,0),(3,1)]:
 cl=splits['zev_open_c_high_examples'][n];edge('zv.review20261126.e.example'+str(n),cl,splits['zev_open_c_high'][t],atom_by_id[cl]['evidence'])
cl=splits['zev_open_c_sanctity'][1];edge('zv.review20261126.e.prohibition_answer',cl,'zev_open_q_word',atom_by_id[cl]['evidence'],'answer')
for label,old in [('akiva','zv.20261126.b3.c12a'),('yohanan','zv.20261126.b3.c12b')]:
 cl=splits[old][0];edge('zv.review20261126.e.oil_'+label,cl,oilq,atom_by_id[cl]['evidence'],'answer','editorial_reconstruction')
cov=[]
affected={(e['segment_id'],x['layer']) for x in rows for e in x['evidence']}
for cv in state['coverage']:
 if not any(i in splits for i in cv['record_ids']) and (cv['segment_id'],cv['layer']) not in affected:continue
 x=copy.deepcopy(cv);x.pop('proposal_execution',None)
 x['record_ids']=[child for i in cv['record_ids'] for child in splits.get(i,[i]) if child not in {z['id'] for z in rows} or any(e['segment_id']==cv['segment_id'] for e in next(z for z in rows if z['id']==child)['evidence'])]
 for z in rows:
  if z['layer']==cv['layer'] and any(e['segment_id']==cv['segment_id'] for e in z['evidence']) and z['id'] not in x['record_ids']:x['record_ids'].append(z['id'])
 x['extraction_result']='records_found' if x['record_ids'] else 'none_found_after_pass'
 x['rationale']+=' Targeted review correction: atomic successors, proposed/challenged local status, and reconstructed common omitted-oil question; original pass scope unchanged.'
 cov.append(x)
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_zevachim_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
new=r.validate_apply(state,p,ss,j)
assert r.report(new,ss)['completed_by_layer']==r.report(state,ss)['completed_by_layer']
r.immutable(HERE/'proposal.json',r.encoded(p))
result=r.submit(JOB,HERE/'proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'submit_receipt.json',r.encoded(result))
r.immutable(HERE/'split_lineage.json',r.encoded(dict(base_snapshot_sha256=BASE,one_to_many_successors=splits,edge_endpoint_overrides=endpoint_overrides,notes='Original composites superseded; oil composite becomes explicit citation discourse claim, not a duplicate normative summary. Primary successor carries supersedes; extra atoms are individually anchored. All dependent positions split with atom conditions; original judgments remain immutable.')))
r.immutable(HERE/'replay.json',r.encoded(r.replay(JOB)))
print(r.encoded(result).decode())
