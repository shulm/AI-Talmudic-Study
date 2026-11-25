import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window005.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['yev004.override','yev005.override'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev005.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Sources for positive command overriding ordinary negative command',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' at this argument stage; no karet override inferred'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('override','structure',list(range(22)),dict(title='Ordinary-prohibition override: tzitzit derivation, proposed leper/nazirite sources and redundancy revisions',primary=True,boundary='open_both',legacy_ids=[]))
rec('continuation','edges',[0],dict(source_id='yev004.override',target_id='yev005.override',relation='continuation',explicitness='source_explicit'),['yev004.override','yev005.override'])
roles=['Challenge to needing wool-and-linen verse under school of Rabbi Yishmael','Garment rule, blue wool command, and question/evidence for wool identification','Proposed need on Rava’s model; apparent contradiction between corner-kind and wool/linen','Rava’s resolution: wool/linen cross-kind; other materials same-kind only','Challenge: school rejects Rava’s position','Revised same-kind-only hypothesis and explicit cross-kind correction','Question for sages’ source','Proposed ראשו source; baraita question and head-rounding restriction hypothesis','ראשו exemption and whole-head rounding premise','Objection: head-rounding prohibition not universal','Alternative beard source with priestly-leper hypothesis and exception','Transfer from non-universal to universal prohibition proposed','Objection: priests’ additional commandments require specific exception','Alternative ראשו source regarding leprous nazirite','Objection: nazirite vow can be released; general positive-plus-negative rule','Counterexample argument continued: release feature prevents generalization','Transition back to first verse, incomplete until following page','Return to tzitzit; proposed redundancy of גדילים','Objection: גדילים encodes thread number and construction','New redundant-term proposal: יחדו','Two-stitch qualification needs יחדו; next candidate שעטנז','שעטנז needed for combined/ spun/ twisted; all laws from that term permits redundancy conclusion']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous analysis with embedded baraitot and Rava quotation',discourse_role=role,composition='composite' if i!=16 else 'atomic'))
 rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
for k,inds,surface,candidates,scope,role in [('school',[0,1,4,5],'תנא דבי רבי ישמעאל',['school of Rabbi Yishmael'],'Garments as wool/linen and distinction from Rava','collective'),('rava',[2,3],'רבא',['Rava'],'Contradiction and resolution on materials of fringes','quoted_authority'),('sages',[6],'רבנן',['sages'],'Source question; no named identification supplied','collective'),('tanna_head',[7,8],'דתניא / האי תנא',[],'Leper head-shaving baraita and inferred whole-head-rounding premise','anonymous'),('tanna_beard',[10],'דתניא',[],'Priestly leper beard baraita','anonymous'),('tanna_nazir',[13],'דהך תנא דתניא',[],'Different ראשו baraita concerning nazirite','anonymous')]:rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=[]))
a=q('school_need',[0,1],'Under the school of Rabbi Yishmael, why need the explicit wool-and-linen phrase to permit mixed-material tzitzit when the command already requires blue wool on garments including linen?')
b=claim('school_garments',[1],'For the school of Rabbi Yishmael all unspecified garments are wool or linen.',holder='school of Rabbi Yishmael')
c=claim('blue_wool',[1],'Tekhelet is wool; the discussion identifies it by contrast with shesh, which is linen.')
d=q('blue_material',[1],'How do we know tekhelet is wool?');edge('blue_ans',[1],c,d,'answer');edge('school_premise',[0,1],b,a,'support');edge('blue_premise',[1],c,a,'support')
e=claim('rava_need',[2],'One might need the verse for Rava’s interpretation.','hypothetical')
f=q('rava_contradiction',[2],'How can the corner clause require the corner’s own material while the other verse specifies wool and linen?')
g=claim('rava_wool',[3],'Wool and linen fringes discharge the obligation on both matching and nonmatching garment materials.',holder='Rava')
h=claim('rava_other_same',[3],'Other fringe materials discharge the obligation on garments of their own material.',holder='Rava')
j=claim('rava_other_diff',[3],'Other fringe materials do not discharge the obligation on garments of different material.',holder='Rava')
for num,cid in enumerate([g,h,j]):edge('rava_answer'+str(num),[3],cid,f,'answer')
edge('proposed_need',[2],e,a,'answer')
k=claim('school_not_rava',[4],'The school of Rabbi Yishmael does not accept Rava’s interpretation.');edge('notrava_obj',[4],k,e,'objection')
l=claim('same_only_hyp',[5],'Following Rava’s inference from corner material alone, one might require wool fringes for wool and linen for linen, with blue dye only on the wool, excluding cross-material fringes.','hypothetical')
m=claim('cross_material',[5],'The explicit wool-and-linen phrase allows wool on linen and linen on wool.');edge('revised_need',[5],l,a,'answer');edge('cross_correct',[5],m,l,'correction')
n=q('sages_source',[6],'What supplies the override derivation for the sages rather than the school of Rabbi Yishmael?')
o=q('head_term',[7],'What does ראשו in the leper-shaving passage teach?')
pp=claim('leper_round_hyp',[7],'The head-rounding prohibition might have been thought to apply even to a leper.','hypothetical')
r=claim('leper_head',[8],'ראשו requires the leper’s head shaving despite the head-rounding prohibition.',holder='anonymous head-shaving baraita')
s=claim('whole_head',[8],'This tanna considers rounding the entire head to count as prohibited rounding.')
edge('head_ans',[8],r,o,'answer');edge('head_source',[7,8],r,n,'answer');edge('head_correction',[8],r,pp,'correction')
t=claim('nonuniversal',[9],'The head-rounding source cannot establish the general rule because its prohibition is not equally applicable to all.');edge('head_obj',[9],t,r,'objection')
v=q('beard_term',[10],'What does זקנו in the leper passage teach?')
wq=claim('priest_hyp',[10],'The priestly prohibition on shaving the beard might have been thought to apply even to a priest who is a leper.','hypothetical')
x=claim('priest_leper',[10],'זקנו permits the priestly leper’s prescribed beard shaving despite the beard prohibition.',holder='anonymous beard-shaving baraita');edge('beard_ans',[10],x,v,'answer');edge('beard_correct',[10],x,wq,'correction')
y=claim('transfer',[11],'Since a non-universal prohibition override was already established, transfer the beard verse’s lesson to a universal prohibition.','hypothetical');edge('transfer_source',[11],y,n,'answer')
z=claim('priests_distinct',[12],'The beard verse may still be needed specifically for priests, whose additional commandments could suggest that even a non-universal prohibition is not overridden.','hypothetical')
aa=claim('priest_override',[12],'The beard verse teaches override even for priests despite their additional commandments.');edge('priest_obj',[12],z,y,'objection');edge('priest_answer',[12],aa,z,'correction')
bb=q('nazir_head',[13],'What does ראשו teach in the other baraita?')
cc=claim('nazir_hyp',[13],'The nazirite’s razor prohibition might have been thought to apply even when he is a leper.','hypothetical')
dd=claim('nazir_leper',[13],'ראשו permits the prescribed head shaving of a nazirite who is a leper.',holder='anonymous nazirite baraita');edge('nazir_ans',[13],dd,bb,'answer');edge('nazir_source',[13],dd,n,'answer');edge('nazir_correct',[13],dd,cc,'correction')
ee=claim('release_distinction',[14,15],'The nazirite source cannot be generalized because nazirite status is subject to release by inquiry.')
ff=claim('positive_negative',[14],'The accepted general rule is that a positive command does not override a combined negative and positive command.')
gg=q('nazir_counterexample',[14,15],'If nazirite shaving could establish a general rule, why not infer override even of a combined negative and positive command from it?')
edge('nazir_obj',[14,15],ee,dd,'objection');edge('counterexample',[14,15],gg,dd,'objection');edge('general_rule',[14],ff,gg,'support');edge('release_answer',[15],ee,gg,'answer')
hh=claim('gedilim_free',[16,17],'Return to the original tzitzit verse: גדילים is proposed as available for adjacency interpretation because ציצית תעשה לך could have been written.','hypothetical');edge('return_source',[16,17],hh,n,'answer')
ii=claim('thread_count',[18],'גדיל means two and גדילים means four, teaching the thread count.')
jj=claim('thread_construction',[18],'Make a braided section and extend the threads from it.',u=['The phrase ופותלהו מתוכו is rendered conservatively; technical construction details need specialist review.'])
edge('count_obj',[18],ii,hh,'objection');edge('construction_obj',[18],jj,hh,'objection')
kk=claim('yachdav_free',[19],'יחדו is proposed as available for interpretation since the prohibition could omit it.','hypothetical');edge('yachdav_revise',[19],kk,hh,'correction')
ll=claim('two_stitches',[20],'Two stitches create a joining, while one stitch does not; יחדו is needed for this distinction.');edge('stitches_obj',[20],ll,kk,'objection')
mm=claim('shaatnez_free',[20],'שעטנז is next proposed as available, since wool and linen together could express the prohibition.','hypothetical');edge('shaatnez_revise',[20],mm,kk,'correction')
nn=claim('processing',[21],'שעטנז is needed to require שוע טווי ונוז.');edge('processing_obj',[21],nn,mm,'objection')
oo=claim('all_from_shaatnez',[21],'The concluding answer derives all the requirements from שעטנז.',u=['The terse conclusion does not explicitly restate which remaining word is free; adjacent-verses argument resumes as established at 5b:6.']);edge('all_answer',[21],oo,nn,'answer');edge('override_established',[21],oo,n,'answer')
for i in range(22):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read with prior 3b:16–4b:8 and continuation to 5b:10. '
  rationale+=('Reread preserves changing derivations, counterfactuals, separate anonymous baraitot, Rava/school distinction, and cross-page אלא לעולם continuation; no karet override assigned.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal005.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
