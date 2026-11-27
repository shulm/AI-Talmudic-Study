import json,hashlib,copy
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');r=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pins=r(out.parent/'bounded_001_20261127/PINS.json');a=r(Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_dataset_runs/ACTIVE_RUN.json'));cp=root/a['contract_path'];assert h(cp)==a['contract_sha256']==pins['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
assert h(Path(pins['source_path']))==pins['source_sha256'];assert h(Path(pins['source_schema_path']))==pins['source_schema_sha256'];assert r(job/'OWNER.json')==pins['owner'];cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur=='5120405f3ba10a4a6863730b405cad2496965e0638120ed57a3b9eddc2f8976d';assert h(job/'snapshots'/(cur+'.json'))==cur;state=r(job/'snapshots'/(cur+'.json'));assert state['open_tails']==['kid003.exit_ages'];inv=r(job/'source_inventory.json');raw=r(Path(pins['source_path']))['text'];core=inv[50:70]
for s in inv[50:74]:i,j=s['source_index'];assert raw[i][j]==s['text']
meta=r(job/'JOB.json');p={k:meta[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root/yevamot',model_id=None),records=[],coverage=[],open_tails=['kid004.intercourse_derivation'])
def ev(i,q=None):
 s=inv[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase'):
 rid='kid004.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(*i) if isinstance(i,tuple) else ev(i) for i in inds],content=c,origin=origin,links=list(links or []),uncertainty=list(u or [])));return rid
def claim(k,inds,text,cond=None,holder='anonymous Gemara',mode='asserted',u=None):
 cid=rec(k,'claims',inds,dict(proposition=text,conditions=list(cond or []),scope='Local acquisition/exit derivation or expressly marked continuation; stages and conditions retained',assertion_mode=mode),u=u);rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond or []),local_status=mode+' at this source stage; alternatives preserved'),[cid],u);return cid
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,x,y,rel):return rec(k,'edges',inds,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
def attr(k,inds,surface,role,candidates,scope,chain=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=list(candidates),scope=scope,transmission_chain=list(chain or [])))
gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};old={x['id']:x for x in state['records'] if x['id'] not in gone};changes={}
def revise(oid,content=None,inds=None):
 if oid not in changes:
  n={k:copy.deepcopy(old[oid][k]) for k in ['id','layer','evidence','content','origin','uncertainty','links']};n['id']='kid004.revised.'+oid;n['supersedes']=oid;changes[oid]=n
 n=changes[oid]
 if content:n['content'].update(content)
 if inds is not None:n['evidence']=[ev(i) for i in inds]
 return n['id']
# Extend only the existing age-release Gemara boundary, preserving separate preceding Mishnah/derivation.
oldstart=old['kid003.exit_ages']['evidence'];start=min(next(i for i,s in enumerate(inv) if s['id']==e['segment_id']) for e in oldstart);revise('kid003.exit_ages',dict(title='Maturity/adolescence redundancy and final original-sale interpretation, through4b2',boundary='closed'),list(range(start,62)))
rec('money_derivation','structure',list(range(62,69)),dict(title='Money acquisition verse and challenged a-fortiori; two verses required for entitlement and direction',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('intercourse_derivation','structure',[69],dict(title='ובעלה intercourse acquisition and proposed a-fortiori; objection and resolution continue',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference',u=['Continuation70–72 read and extracted as context; next deed-acquisition topic73 inspected.'])
roles=['Rabbah one provision teaches other','Resident/permanent and hired/term illustration','Why not only resident: a-fortiori proposal','Without hired, resident could be misread; clarification','Abaye two-person case and expressly written a-fortiori','One girl already released at adolescence objection','Abaye aylonit maturity interpretation','Proposed no maturity release rejected','Mar bar Rav Ashi signs versus maturity objection','Original aylonit sale explanation and rejected no-sale hypothesis','Crossfolio verse confirms original sale','Prefer available alternative interpretation to redundant a-fortiori text','Tanna money derivation from taking and field-price verse','Maid-to-wife a-fortiori for money acquisition','Yevamah counterexample and deed distinction','Why verse if inference works; Rav Ashi initial-premise refutation','Maid exits by money but wife not; verse needed','Why both verses: husband money might belong to daughter','Why both verses: female-to-male direction excluded','Intercourse verse and proposed yevamah-to-wife a-fortiori']
for i,role in zip(range(50,70),roles):rec('u'+str(i),'utterances',[i],dict(textual_voice='Gemara with quoted baraita and scoped named speech',discourse_role=role,composition='composite'));attr('anon'+str(i),[i],'anonymous framing','anonymous',[],role)
# Prior context becomes core with atomic successor claims, retaining prior composite evidence.
parts=[]
for oid,t1,key,t2,inds in [
('kid003.context.resident_misread','Without שכיר one could misread תושב as acquisition for a term of years.','permanent_eats_hyp','On that misreading one could suppose permanent acquisition permits eating.',[53]),
('kid003.context.hired_clarifies','שכיר clarifies that תושב means permanent acquisition.','permanent_not_eat','Even the permanent acquisition does not permit eating in the cited illustration.',[53]),
('kid003.context.two_bodies','Abaye distinguishes the resident/hired case as concerning two persons.','write_af','Scripture may explicitly write a rule already derivable a fortiori in the stated two-person illustration.',[54]),
('kid003.context.signs','Signs do not remove paternal authority in this comparison.','signs_master','Signs release the girl from the master in this comparison.',[58]),
('kid003.context.no_sale_hyp','The proposed original-sale restriction validates sale of one who develops adolescent signs.','no_signs_no_sale','The proposed original-sale restriction invalidates sale of one who does not develop adolescent signs.',[59]),
('kid003.context.prefer_other','Where an alternative interpretation is available, the passage adopts it.','no_alternative_af','Where no alternative interpretation is available, Scripture may expressly write a rule derivable a fortiori.',[61])]:
 revise(oid,dict(proposition=t1));pos=old[oid+'.p'];nid=claim(key,inds,t2,old[oid]['content']['conditions'],pos['content']['holder_candidates'][0],old[oid]['content']['assertion_mode']);parts.append((oid,nid,inds))
revise('kid003.context.aylonit_no_exit_hyp',dict(proposition='One might think an aylonit without adolescence signs does not leave at maturity; the added maturity wording excludes that supposition.'))
qresident=q('resident_only_q',[52],'Why not state תושב alone and infer the term-of-years case a fortiori?');edge('resident_reply',[52,53],'kid003.context.resident_misread',qresident,'answer');edge('clarify_reply',[52,53],'kid003.context.hired_clarifies',qresident,'answer')
# New money-derivation unit.
money=claim('money_take',[62],'כי יקח איש אשה teaches acquisition by money.',['Tanna’s derivation'],'quoted baraita');taking=claim('taking_money',[62],'The taking here is interpreted as money, with נתתי כסף השדה קח ממני as the cited comparison.',['Local קיחה derivation'],'quoted baraita');edge('take_source',[62],taking,money,'support');qaf=q('money_af_q',[63],'Could money acquisition be derived a fortiori without the verse?');maidno=claim('maid_no_intercourse',[63],'A Hebrew maidservant is not acquired by intercourse.',['Premise of proposed comparison'],'baraita argument');maidmoney=claim('maid_money',[63],'A Hebrew maidservant is acquired by money.',['Premise of proposed comparison'],'baraita argument');wifeint=claim('wife_intercourse_premise',[63],'A wife is acquired by intercourse in the premise of this money comparison.',['Premise, derivation treated separately below'],'baraita argument');afmoney=claim('wife_money_af',[63],'The proposed a-fortiori derives wife acquisition by money from the Hebrew maidservant.',['Provisional inference; initial-premise objection follows'],'baraita argument','challenged');edge('maid_money_inference',[63],maidmoney,afmoney,'analogy');edge('maid_lesser',[63],maidno,afmoney,'support');edge('wife_intercourse_basis',[63],wifeint,afmoney,'support');edge('af_money_answer',[63],afmoney,qaf,'answer')
yivint=claim('yevamah_intercourse',[64],'A yevamah is acquired by intercourse.',['Counterexample in money derivation'],'baraita argument');yivno=claim('yevamah_no_money',[64],'A yevamah is not acquired by money.',['Counterexample in money derivation'],'baraita argument');edge('yevamah_counter',[63,64],yivno,afmoney,'objection');yivnodeed=claim('yevamah_no_deed',[64],'A yevamah is not acquired by deed.',['Distinguishing feature'],'baraita argument');wifedeed=claim('wife_deed',[64],'A wife is acquired by deed.',['Distinguishing feature'],'baraita argument');edge('deed_distinction',[64],wifedeed,yivno,'distinction');edge('yevamah_deed_distinction',[64],yivnodeed,yivno,'qualification')
qneed=q('money_verse_need',[65],'Why is כי יקח needed if the a-fortiori argument appears to establish money acquisition?');initial=claim('money_initial_objection',[65],'Rav Ashi answers that the initial premise of the a-fortiori can be refuted.',['Money derivation'],'Rav Ashi');attr('rav_ashi',[65],'אמר רב אשי','speaker',['Rav Ashi'],'Money a-fortiori initial-premise refutation, distinct from Mar bar Rav Ashi');edge('initial_answer',[65],initial,qneed,'answer');qfrom=q('money_from_where',[66],'From where is that inference being drawn—Hebrew maidservant?');maidexit=claim('maid_money_exit',[66],'The Hebrew maidservant leaves her status by money.',['Feature of comparison source'],'baraita argument as explained by Rav Ashi');wifenoexit=claim('wife_no_money_exit',[66],'A wife does not leave marriage by money.',['Distinguishing feature of target case'],'baraita argument as explained by Rav Ashi');edge('exit_refutes',[63,66],maidexit,afmoney,'objection');edge('wife_exit_distinction',[66],wifenoexit,maidexit,'distinction');edge('refutation_explains',[65,66],maidexit,initial,'support');edge('verse_needed',[62,66],money,qneed,'answer')
needboth=claim('both_verses',[67],'Both ויצאה חנם and כי יקח איש are needed.',['Complementary derivations, not competing textual witnesses']);daughter=claim('daughter_money_hyp',[67],'With כי יקח alone one might assign the husband’s betrothal money to the daughter.',['Counterfactual omission of ויצאה חנם'],'anonymous argument','rejected');fatherrule=claim('father_money_from_exit',[67],'ויצאה חנם supplies the father’s monetary entitlement in this contrast.',['Father/daughter setting of prior derivation']);edge('father_corrects',[67],fatherrule,daughter,'correction');edge('father_verse_needed',[67],fatherrule,needboth,'support')
female=claim('female_transfer_hyp',[68],'With ויצאה חנם alone one might validate her giving money to him and betrothing him.',['Counterfactual omission of כי יקח; preserve parenthesized ליה'],'anonymous argument','rejected');manrule=claim('man_takes',[68],'כי יקח requires the man’s taking in the stated betrothal transaction.',['This local acquisition direction argument']);notwoman=claim('not_woman_takes',[68],'The reading excludes כי תקח, the woman’s taking in that proposed reverse transaction.',['Local exclusion, not a general claim about all matrimonial actions']);edge('direction_correction',[68],notwoman,female,'correction');edge('direction_need',[67,68],manrule,needboth,'support')
intercourse=claim('intercourse_verse',[69],'ובעלה teaches acquisition by intercourse.',['Tanna’s derivation'],'quoted baraita');qint=q('intercourse_af_q',[69],'Could intercourse acquisition be derived a fortiori from yevamah without the verse?');afint=claim('wife_intercourse_af',[69],'The proposed a-fortiori derives intercourse acquisition for a wife who is acquired by money, from yevamah who is not acquired by money.',['Provisional inference; rebuttal follows'],'baraita argument','challenged');edge('intercourse_af_answer',[69],afint,qint,'answer');edge('yevamah_int_basis',[64,69],yivint,afint,'analogy');edge('yevamah_money_basis',[64,69],yivno,afint,'support');edge('wife_money_basis',[62,69],money,afint,'support')
# Context closes the actual proof before next deed-acquisition topic.
maidcounter=maidno
for row in p['records']:
 if row['id'] in [maidno,maidno+'.p',maidmoney,maidmoney+'.p']:row['evidence'].append(ev(70))
edge('context.counter',[69,70],maidcounter,afint,'objection');maidnotmarry=claim('context.maid_not_marriage',[70],'The Hebrew maidservant’s acquisition is not for marriage.',['Distinguishing feature'],'baraita argument');wifemarry=claim('context.wife_marriage',[70],'The wife’s acquisition is for marriage.',['Distinguishing feature'],'baraita argument');edge('context.marriage_distinction',[70],wifemarry,maidcounter,'distinction');edge('context.maid_scope',[70],maidnotmarry,maidcounter,'qualification');qintverse=q('context.intercourse_verse_need',[71],'Why is ובעלה needed if the inference appears sufficient?');intinitial=claim('context.initial_refutation',[71],'Rav Ashi answers that the inference can be refuted at its original premise.',['Intercourse derivation'],'Rav Ashi');attr('context.rav_ashi',[71],'אמר רב אשי','speaker',['Rav Ashi'],'Separate intercourse a-fortiori refutation');edge('context.refutation_answer',[71],intinitial,qintverse,'answer');bound=claim('context.yevamah_bound',[72],'A yevamah already stands bound by the levirate bond.',['Feature of source of the inference']);unbound=claim('context.wife_unbound',[72],'The woman in ordinary betrothal does not already stand under that bond.',['Target of inference']);edge('context.bond_refutation',[69,72],bound,afint,'objection');edge('context.bond_difference',[72],unbound,bound,'distinction');edge('context.verse_answer',[69,72],intercourse,qintverse,'answer')
# Extend existing split branch links to each independently queryable successor.
for oid,nid,inds in parts:
 if oid=='kid003.context.prefer_other':continue
 for x in old.values():
  if x['layer']=='edges' and x['content'].get('source_id')==oid:
   edge('split.'+nid+'.'+x['id'],sorted(set(inds+[next(i for i,s in enumerate(inv) if s['id']==e['segment_id']) for e in x['evidence']])),nid,x['content']['target_id'],x['content']['relation'])

def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 more=[k for k,x in old.items() if k not in changes and strings([x['content'],x['links']])&set(changes)]
 if not more:break
 for k in more:revise(k)
mp={k:x['id'] for k,x in changes.items()}
def repl(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [repl(y) for y in x]
 if isinstance(x,dict):return {k:repl(y) for k,y in x.items()}
 return x
for x in changes.values():x['content']=repl(x['content']);x['links']=repl(x['links']);p['records'].append(x)
for x in p['records']:x['content']=repl(x['content']);x['links']=repl(x['links'])
for c in state['coverage']:
 if set(c['record_ids'])&set(changes):p['coverage'].append(repl({k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'}))
active={k:x for k,x in old.items() if k not in changes};active.update({x['id']:x for x in p['records']})
for s,role in zip(core,roles):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  matches=[x['id'] for x in active.values() if x['layer']==layer and any(e['segment_id']==s['id'] for e in x['evidence'])]
  if layer=='reconciliation':matches=[x['id'] for x in active.values() if x['layer'] in ['claims','edges','structure'] and any(e['segment_id']==s['id'] for e in x['evidence'])]
  p['coverage'].append(dict(segment_id=s['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if matches else 'none_found_after_pass',record_ids=matches,rationale=role+'. Source-first reread through4b13, next deed topic5a1 inspected. Exact prior context reused/split, originalindices retained. '+('Evidence-bearing '+layer+' rows after omission check.' if matches else 'No explicit '+layer+' finding after pass; no invented position/question.')))
for x in p['records']:
 for e in x['evidence']:
  s=next(s for s in inv if s['id']==e['segment_id']);assert s['text'][e['start_char']:e['end_char']]==e['quote']
 for k in x['links']:assert k in active
 assert not strings([x['content'],x['links']])&set(changes)
for c in p['coverage']:
 for k in c['record_ids']:assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
(out/'INITIAL_PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'PINS.json').write_text(json.dumps(dict(pins=pins,parent_snapshot=cur,core_refs=[s['ref'] for s in core],core_indices=[s['source_index'] for s in core],revision_map=mp,independent_reading_seen=False,context_refs=[s['ref'] for s in inv[70:73]],uncertainties=['Prior context50–61 reused with atomic immutable successors; no duplicate coverage.','Rabbah,Abaye,Mar bar Rav Ashi stages remain distinct; Rav Ashi later objections are different speaker.','Both money and intercourse a-fortiori constructions retain rejected routes and final verse grounds.','No practical authority ruling inferred from these derivations.','Context70–72 uncounted; core ends4b10 and open intercourse derivation continues at4b11.']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(proposal=h(out/'INITIAL_PROPOSAL.json'),records=len(p['records']),revisions=len(changes))))
