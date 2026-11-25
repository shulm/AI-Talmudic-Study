import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window006.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['yev004.override','yev005.override','yev006.karet'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev006.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Karet-override source search and adjacent Temple-reverence discussion',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' in local discussion'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('karet','structure',list(range(24)),dict(title='Search for karet override from circumcision, offerings, parental honor and Temple construction; Temple reverence excursus',primary=True,boundary='open_both',legacy_ids=[]))
rec('temple_reverence','structure',list(range(20,24)),dict(title='Temple reverence: its object, conduct and persistence after destruction',primary=False,boundary='closed',legacy_ids=[]))
rec('continuation','edges',[0],dict(source_id='yev005.override',target_id='yev006.karet',relation='continuation',explicitness='source_explicit'),['yev005.override','yev006.karet'])
roles=['Ordinary override established; karet-source question renewed','Circumcision proposal rejected by thirteen covenants','Passover proposal rejected by karet feature','Daily offering proposal rejected by frequency','Paired-source search: circumcision/Passover and Passover/daily offering objections','Circumcision/daily pair and all-three rejected by pre-revelation feature with explicit opinion condition','Parental-honor source suggested','Baraita: parental honor does not override Sabbath because all owe divine honor','Slaughter/cooking interpretation proposed and denied','Driving a laden animal substituted; still no override','Challenge: infer no ordinary override from parental honor','Proposed Sabbath-specific severity exception challenged','Baraita: father ordering defilement or nonreturn is not obeyed','Transition to distinguishing these cases','Mitzvah-preparation distinction','Temple-construction source suggested; baraita denies Sabbath override','Building/demolition interpretation and counterfactual override proposed','Driving animal interpretation; renewed ordinary-override challenge','Repeated Sabbath-severity suggestion and parental baraita counterexample','Preparatory-act distinction repeated; question of redundant Temple verse','Redundancy conceded; new Temple-reverence baraita begins','Fear directed to commander, not Sabbath or sanctuary objects','Definition of Temple reverence: entry prohibitions, shortcut and spitting','Post-destruction continuation of Temple reverence derived by Sabbath analogy']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous Gemara with embedded anonymous baraitot',discourse_role=role,composition='composite' if i not in [6,9,13,14] else 'atomic'))
 rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion' if i not in [7,12,21,22,23] else 'anonymous baraita',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
rec('conditional_authority','attributions',[5],dict(surface='ואליבא דמ"ד',role='quoted_authority',candidates=[],scope='Opinion identifying wilderness burnt offering as daily offering',transmission_chain=[]),u=['No named holder supplied in source.'])
a=claim('ordinary_established',[0],'A positive command overrides an ordinary negative command; this has now been established.')
b=q('karet_source',[0],'Where do we find override of a negative command carrying karet, so that עליה must explicitly exclude wife’s sister?')
c=claim('milah',[1],'Circumcision might supply the karet-override precedent.','hypothetical')
d=claim('thirteen',[1],'Circumcision is exceptional because thirteen covenants were made concerning it.');edge('milah_proposal',[1],c,b,'answer');edge('milah_obj',[1],d,c,'objection')
e=claim('pesach',[2],'Passover offering might supply the precedent.','hypothetical');f=claim('pesach_karet',[2],'Passover offering is exceptional because it itself carries karet.');edge('pesach_proposal',[2],e,b,'answer');edge('pesach_obj',[2],f,e,'objection')
g=claim('tamid',[3],'The daily offering might supply the precedent.','hypothetical');h=claim('tamid_frequency',[3],'The daily offering is exceptional because it is frequent.');edge('tamid_proposal',[3],g,b,'answer');edge('tamid_obj',[3],h,g,'objection')
j=q('two',[4],'If no single case establishes the rule, which pair could establish it?')
k=claim('milah_pesach',[4],'Circumcision and Passover together remain exceptional because both carry karet.');l=claim('pesach_tamid',[4],'Passover and the daily offering together remain exceptional because both serve the divine service.');edge('pair1',[4],k,j,'answer');edge('pair2',[4],l,j,'answer')
m=claim('milah_tamid',[5],'Circumcision and the daily offering remain exceptional because they predate revelation, according to the opinion that the wilderness burnt offering was the daily offering.','conditional',cond=['Opinion that Israel’s wilderness burnt offering was the daily offering'])
n=claim('all_three',[5],'The combined set is also distinguished as predating revelation.','conditional',cond=['Same stated premise concerning wilderness daily offering'])
edge('pair3',[5],m,j,'answer');edge('all_obj',[5],n,b,'objection')
o=claim('honor_source',[6],'Parental honor might supply the reason a specific exclusion is needed.','hypothetical');edge('honor_proposal',[6],o,b,'answer')
pp=q('honor_sabbath',[7],'Could parental honor override Sabbath?')
r=claim('honor_no_override',[7],'Parental honor does not override Sabbath; Leviticus 19:3 commands both parental reverence and Sabbath observance, for all owe honor to God.',holder='anonymous parental-honor baraita');edge('honor_answer',[7],r,pp,'answer')
s=q('slaughter_reading',[8],'Does the case not concern a father commanding slaughtering or cooking, with the verse alone preventing override?')
t=claim('slaughter_hyp',[8],'If the baraita concerned slaughter or cooking, absent the Sabbath verse parental honor would override.','hypothetical',cond=['Proposed slaughter/cooking interpretation; rejected by לא'])
v=claim('animal_reading',[9],'The case is the prohibition on driving a laden animal, and even this is not overridden.');edge('animal_correct',[8,9],v,t,'correction');edge('animal_ans',[9],v,s,'answer')
wq=q('no_ordinary',[10],'Why not derive here that a positive command does not override an ordinary prohibition?')
x=claim('sabbath_severity',[11],'Perhaps Sabbath prohibitions differ because of their severity.','hypothetical')
y=claim('not_sabbath_only',[11,12],'The baraita also applies the same verse outside Sabbath, so Sabbath severity alone does not account for it.');edge('severity_proposal',[11],x,wq,'answer');edge('severity_obj',[11,12],y,x,'objection')
z=q('father_commands',[12],'Should a child obey a father who orders defilement or orders not returning an item?')
aa=claim('defilement',[12],'A father’s command to become impure is not obeyed when it conflicts with the divine command, because both owe divine honor.',holder='anonymous parental-honor baraita')
bb=claim('nonreturn',[12],'A father’s command not to return an item is not obeyed when it conflicts with the divine command.',holder='anonymous parental-honor baraita')
edge('father_ans1',[12],aa,z,'answer');edge('father_ans2',[12],bb,z,'answer');edge('outside_support1',[12],aa,y,'support');edge('outside_support2',[12],bb,y,'support')
cc=claim('preparation',[13,14],'These cases can be distinguished because they involve preparation for a mitzvah.',u=['The terse הכשר מצוה distinction is preserved without imposing a disputed expanded antecedent mapping.']);edge('preparation_ans',[13,14],cc,wq,'answer');edge('honor_failure',[13,14],cc,o,'objection')
dd=claim('temple_source',[15],'Temple construction might instead supply the proposed precedent.','hypothetical');edge('temple_proposal',[15],dd,b,'answer')
ee=q('temple_sabbath',[15],'Could building the Temple override Sabbath?')
ff=claim('temple_no_override',[15],'Temple building does not override Sabbath; Leviticus 19:30 pairs Sabbath observance and sanctuary reverence, for all owe divine honor.',holder='anonymous Temple-construction baraita');edge('temple_answer',[15],ff,ee,'answer')
gg=q('building_reading',[16],'Does this not concern building and demolition, which would override absent the verse?')
hh=claim('building_hyp',[16],'On the building/demolition interpretation, absent the explicit Sabbath verse the positive command would override.','hypothetical',cond=['Interpretation rejected next'])
ii=claim('temple_animal',[17],'The case is driving a laden animal, and it still does not override.');edge('temple_animal_correct',[17],ii,hh,'correction');edge('temple_animal_answer',[17],ii,gg,'answer')
jj=q('temple_no_ordinary',[17],'Then why not derive a general rule that positive commands do not override negative commands?')
kk=claim('temple_severity',[18],'Perhaps Sabbath prohibitions are exceptionally severe.','hypothetical')
ll=claim('repeat_father',[18],'The parental-command baraita also forbids obeying orders to become impure or refrain from return, using the same all-owe-divine-honor explanation.',holder='anonymous repeated baraita')
edge('temple_severity_answer',[18],kk,jj,'answer');edge('temple_severity_obj',[18],ll,kk,'objection')
mm=claim('temple_preparation',[19],'These cases involve preparation for a mitzvah, blocking the generalization.');edge('temple_preparation_ans',[19],mm,jj,'answer')
nn=q('already_known',[19],'If the Temple case is only mitzvah preparation, is that not already learned from the earlier case?')
oo=claim('redundancy_conceded',[20],'Indeed, the non-override point can be learned from the earlier case.')
edge('concede',[20],oo,nn,'answer')
qq=q('temple_verse_purpose',[20],'What then is the purpose of pairing Sabbath observance and sanctuary reverence?')
rr=q('fear_object',[20],'Might one fear the sanctuary itself?')
ss=claim('fear_commander',[20,21],'As Sabbath reverence concerns the one who commanded Sabbath, sanctuary reverence concerns the one who commanded about the sanctuary, not the sanctuary itself.',holder='anonymous sanctuary-reverence baraita')
edge('fear_answer',[20,21],ss,rr,'answer');edge('temple_verse_answer',[20,21],ss,qq,'answer')
tt=q('reverence_definition',[22],'What conduct constitutes sanctuary reverence?')
# Each separately named prohibition retains its own atomic claim, with shared source evidence.
for key,prop in [('staff','Do not enter the Temple Mount with one’s staff.'),('shoe','Do not enter the Temple Mount with one’s shoe.'),('pundato','Do not enter the Temple Mount with one’s pundah/pundato.'),('dust','Do not enter the Temple Mount with dust on one’s feet.'),('shortcut','Do not use the Temple Mount as a shortcut.'),('spitting','Spitting is forbidden by an a-fortiori inference.')]:
 cid=claim('reverence_'+key,[22],prop,holder='anonymous sanctuary-reverence baraita',u=['פונדתו lexical identification is left untranslated pending review.'] if key=='pundato' else (['The a-fortiori premises are not stated here and are not invented.'] if key=='spitting' else []));edge('reverence_answer_'+key,[22],cid,tt,'answer')
uu=q('after_destruction',[23],'How is sanctuary reverence known to continue when the Temple no longer stands?')
vv=claim('forever',[23],'Just as Sabbath observance is perpetual, sanctuary reverence is perpetual, by the pairing in Leviticus 19:30.',holder='anonymous sanctuary-reverence baraita');edge('forever_answer',[23],vv,uu,'answer')
for i in range(24):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read with prior ordinary-override proof and continuation through 6b:12. '
  rationale+=('Omission reread keeps all rejected single/pair sources, conditional wilderness premise, repeated parental occurrences, incomplete transition and sanctuary-conduct atoms; karet question remains open.' if layer=='reconciliation' else ('Actual '+layer+' pass with no separate item.' if not ids else 'Completed '+layer+' pass.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal006.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
