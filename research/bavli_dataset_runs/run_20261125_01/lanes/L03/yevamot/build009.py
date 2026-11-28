import json,copy
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'))
w=read(job/'window009_resume.json');seg=w['segments'];state=read(job/'snapshots'/(read(job/'CURRENT.json')['snapshot_sha256']+'.json'));p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=[])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev009.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Rava’s explanation and revised transmission on co-wife prohibition and permission',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' at stated argument stage; later corrections remain separate'),[c],u);return c
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
# Source reading through 8b:9 establishes closure before explicit גופא at 8b:10.
# Preserve the five original proposals, demoting their partitions into nested context spans.
olds={r['id']:r for r in state['records']}; mapping={}; all_ev=[]
for idx,oid in enumerate(state['open_tails']):
 old=olds[oid]; all_ev.extend(old['evidence']);nr={k:copy.deepcopy(v) for k,v in old.items() if k in ['id','layer','evidence','content','origin','uncertainty','links']};nr['id']='yev009.context'+str(idx);nr['supersedes']=oid;nr['content']['primary']=False;nr['content']['boundary']='closed';nr['content']['title']='Nested topic context within reconciled 3b:16–8b:9 discussion: '+nr['content']['title'];nr['uncertainty']+=['Earlier primary packet span is retained only as nested context; it does not establish a separate sugya boundary.'];mapping[oid]=nr['id'];p['records'].append(nr)
all_ev += [ev(i) for i in range(3,23)]
merged=rec('sugya','structure',[],dict(title='Why עליה is required: override hypotheses, hermeneutic alternatives and Rava’s co-wife scope explanation (3b:16–8b:9)',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');p['records'][-1]['evidence']=all_ev
for old in state['records']:
 if old['release_state']!='valid' or not any(x in mapping for x in old['links']):continue
 assert old['layer']=='edges' and old['content']['relation']=='continuation',old['id']
 nr={k:copy.deepcopy(v) for k,v in old.items() if k in ['id','layer','evidence','content','origin','uncertainty','links']};nr['id']='yev009.reconciled.'+old['id'];nr['supersedes']=old['id'];nr['links']=[mapping.get(x,x) for x in nr['links']]
 for k in ['source_id','target_id']:nr['content'][k]=mapping.get(nr['content'][k],nr['content'][k])
 mapping[old['id']]=nr['id'];p['records'].append(nr)
for cov in state['coverage']:
 if not any(x in mapping for x in cov['record_ids']):continue
 nc={k:copy.deepcopy(v) for k,v in cov.items() if k!='proposal_execution'};nc['record_ids']=[mapping.get(x,x) for x in nc['record_ids']]
 if nc['layer'] in ['structure','reconciliation']:nc['record_ids'].append(merged)
 nc['rationale']+=' Continuation reconciled at 8b:9 before גופא: original packet partitions retained as nested context; merged primary ownership preserves every original character.';p['coverage'].append(nc)
roles={3:'Rava: relative needs no verse; co-wife prohibition initially assigned verse',4:'Baraita singular-language objection',5:'Answer: language for co-wife',6:'Plural-language objection and co-wives answer',7:'Rabbi’s two expressions cited against Rava',8:'Corrective reading co-wives of relatives; two-verse objection',9:'Both expressions assigned co-wife prohibition/permission by mitzvah context',10:'Reason from ויבמה for contextual scope',11:'Rav Ashi supports from Mishnah wording',12:'Challenge: same karet principle applies to co-wife',13:'Rav Aha bar Bibi Mar corrects report to Ravina in Rava’s name; sentence continues',14:'Corrected purpose: permission outside mitzvah context; עליה reason',15:'Rami bar Hama asks Rava to permit relative outside mitzvah; a-fortiori response',16:'Co-wife counterexample; בחייה response',17:'Death-exclusion need and alternative source proposed',18:'Divorce distinction defeats spare בחייה proposal',19:'Rav Huna bar Tahlifa in Rava’s name: plural/singular verses divided by context',20:'Proposed inverse allocation rejected by עליה',21:'Rav Ashi asks Rav Kahana whether עליה permits both in mitzvah context',22:'Singular ערותה requirement defeats that proposal; discussion closes'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous framing and named reports/dialogue as separately attributed',discourse_role=role,composition='composite'))
 rec('a'+str(i),'attributions',[i],dict(surface='anonymous framing / unassigned response' if i not in [3,11,13,19,21] else 'named discourse; see scoped attribution',role='anonymous',candidates=[],scope=role+'; unassigned turns remain unassigned',transmission_chain=[]))
for k,inds,surf,role,can,scope,chain in [('rava',[3],'רבא','speaker',['Rava'],'Initial explanation',[]),('rabbi',[7],'רבי','quoted_authority',['Rabbi'],'Two expressions prohibit co-wives and relatives',[]),('ashi_support',[11],'רב אשי','speaker',['Rav Ashi'],'Mishnah wording support',[]),('aha',[13,14],'רב אחא בר ביבי מר','transmitter',['Rav Aha bar Bibi Mar'],'Correction addressed to Ravina in Rava’s name',['Rav Aha bar Bibi Mar','Rava']),('rava_correct',[13,14],'משמיה דרבא','quoted_authority',['Rava'],'Verse needed to permit co-wife outside mitzvah context',[]),('rami',[15],'רמי בר חמא','speaker',['Rami bar Hama'],'Question addressed to Rava',[]),('huna',[19],'רב הונא בר תחליפא','transmitter',['Rav Huna bar Tahlifa'],'Plural/singular explanation in Rava’s name',['Rav Huna bar Tahlifa','Rava']),('rava_plural',[19],'משמיה דרבא','quoted_authority',['Rava'],'Two clauses divided by context',[]),('ashi_q',[21],'רב אשי','speaker',['Rav Ashi'],'Question addressed to Rav Kahana',[])]:rec(k,'attributions',inds,dict(surface=surf,role=role,candidates=can,scope=scope,transmission_chain=chain))
a=claim('no_karet_override',[3],'A positive command does not override a negative command carrying karet.',holder='Rava')
b=claim('relative_no_verse',[3],'The forbidden relative herself needs no special verse because of the karet rule.',holder='Rava')
c=claim('cowife_initial',[3],'The verse is needed to prohibit the co-wife.',holder='Rava',u=['Initial report is corrected explicitly at 8a:19–8b:1; not final formulation.'])
edge('rule_reason',[3],a,b,'support')
d=q('singular_obj',[4],'If the relative needs no verse, why does the baraita say only she is known?');edge('singular_challenge',[4],d,b,'objection')
e=claim('singular_reply',[5],'The baraita mentions her on account of the co-wife.');edge('singular_answer',[5],e,d,'answer')
f=q('plural_obj',[(6,'והא קתני אין לי אלא הן')],'Why does the baraita also say only they are known?')
g=claim('plural_reply',[(6,'משום צרותיהן')],'That formulation is on account of their co-wives.');edge('plural_answer',[6],g,f,'answer')
h=claim('rabbi_quote',[7],'Rabbi interprets ולקחה and ויבמה as prohibiting co-wives and forbidden relatives.',holder='Rabbi',u=['Quoted formulation is immediately reread as co-wives of relatives.']);edge('rabbi_obj',[7],h,b,'objection')
j=claim('reread',[8],'Read the teaching as prohibiting co-wives of forbidden relatives.');edge('reread_correction',[8],j,h,'correction')
k=q('two_verses',[8],'Since two verses are cited, is one not for the relative and one for the co-wife?')
l=claim('both_cowife',[9],'Both verses concern the co-wife: one prohibits her in a mitzvah situation, the other permits her outside it.');edge('two_answer',[9],l,k,'answer')
m=q('why_context',[10],'What grounds that contextual distinction?')
n=claim('yibmah_scope',[10],'ויבמה locates the co-wife prohibition within yibbum; outside yibbum the co-wife is permitted.');edge('context_answer',[10],n,m,'answer');edge('context_support',[10],n,l,'support')
o=claim('mishnah_support',[11],'The Mishnah says the fifteen women exempt their co-wives, not that they are exempt and exempt others; its wording supports the focus on co-wives.',holder='Rav Ashi');edge('mishnah_reason',[11],o,b,'support')
pp=q('cowife_same_rule',[12],'If the relative needs no verse because positive commands do not override karet, why would the co-wife need one?');edge('cowife_obj',[12],pp,c,'objection')
r=claim('cowife_corrected',[13,14],'The co-wife also needs no verse to prohibit her; the verse is needed to permit the co-wife outside a mitzvah situation.',holder='Rava via Rav Aha bar Bibi Mar')
s=claim('aleha_scope',[14],'עליה restricts co-wife prohibition to the עליה situation and permits her outside it.');edge('correct_report',[13,14],r,c,'correction');edge('corrected_answer',[13,14],r,pp,'answer');edge('aleha_reason',[14],s,r,'support')
t=q('relative_outside',[(15,'א"ל רמי בר חמא לרבא אימא ערוה גופיה שלא במקום מצוה תישתרי')],'Why not permit the forbidden relative herself outside a mitzvah situation?')
v=claim('fortiori',[15],'If the relative is prohibited even in the mitzvah situation, she should not be permitted outside it.')
wq=claim('cowife_counter',[16],'The co-wife is a counterexample: prohibited in the mitzvah situation but permitted outside it.');edge('fortiori_answer',[15],v,t,'answer');edge('counterexample',[16],wq,v,'objection')
x=claim('lifetime_reply',[16],'בחייה states the prohibition throughout the wife’s lifetime.');edge('lifetime_answer',[16],x,t,'answer')
y=q('death_need',[17],'Is בחייה not needed to exclude after her death?')
z=claim('death_other',[17],'The death distinction is proposed to follow from ואשה אל אחותה.');edge('death_answer',[17],z,y,'answer')
aa=claim('divorce_hyp',[18],'From ואשה אל אחותה alone one could have inferred permission after divorce.','hypothetical')
bb=claim('divorce_excluded',[18],'בחייה forbids the wife’s sister throughout her lifetime even after divorce.');edge('divorce_obj',[18],aa,z,'objection');edge('divorce_correction',[18],bb,aa,'correction')
cc=claim('two_clauses',[19],'לצרור implies both, while לגלות ערותה implies one; in the mitzvah situation both relative and co-wife are prohibited, outside it only the relative is prohibited.',holder='Rava via Rav Huna bar Tahlifa')
edge('new_explanation',[19],cc,x,'correction')
dd=q('inverse',[20],'Why not reverse the allocation: only the relative prohibited in mitzvah context, both outside it?')
ee=claim('inverse_refuted',[20],'If that were the allocation, עליה would not be needed.');edge('inverse_answer',[20],ee,dd,'answer');edge('inverse_support',[20],ee,cc,'support')
ff=q('permit_aleha',[21],'Why read עליה as prohibitive rather than permitting both relative and co-wife in the mitzvah situation, with both forbidden outside?')
gg=claim('singular_refutes',[22],'That reading leaves no case for the singular ערותה: both would be permitted in the mitzvah situation and both forbidden outside it.');edge('last_answer',[22],gg,ff,'answer');edge('scope_resolution',[22],gg,cc,'support')
for i in range(3,23):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read overlap from 8a:6 through גופא at 8b:10 and further 9a:1. '
  rationale+=('Omission reread retains initial and corrected Rava reports, sentence crossing page, plural/singular conditions, rejected inverse allocation; anonymous reply speakers not forced. Larger primary discussion closes at 8b:9.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal009.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(p['records']),len(p['coverage']))
