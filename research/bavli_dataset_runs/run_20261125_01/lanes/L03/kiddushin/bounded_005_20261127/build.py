import json,hashlib,copy
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');r=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pins=r(out.parent/'bounded_001_20261127/PINS.json');a=r(Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_dataset_runs/ACTIVE_RUN.json'));cp=root/a['contract_path'];assert h(cp)==a['contract_sha256']==pins['contract_sha256'];contract=r(cp)
for f,sha in contract['production_files'].items():assert h(root/f)==sha
assert h(Path(pins['source_path']))==pins['source_sha256'];assert h(Path(pins['source_schema_path']))==pins['source_schema_sha256'];assert r(job/'OWNER.json')==pins['owner'];cur=r(job/'CURRENT.json')['snapshot_sha256'];assert cur=='22fcc9db9d44621f894e577bd245b76213e59027322fe50868f6635e2eee39a7';assert h(job/'snapshots'/(cur+'.json'))==cur;state=r(job/'snapshots'/(cur+'.json'));assert state['open_tails']==['kid004.intercourse_derivation'];inv=r(job/'source_inventory.json');raw=r(Path(pins['source_path']))['text'];core=inv[70:90]
for s in inv[67:102]:i,j=s['source_index'];assert raw[i][j]==s['text']
meta=r(job/'JOB.json');p={k:meta[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root/yevamot',model_id=None),records=[],coverage=[],open_tails=['kid005.canopy'])
def ev(i,q=None):
 s=inv[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase'):
 rid='kid005.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(*i) if isinstance(i,tuple) else ev(i) for i in inds],content=c,origin=origin,links=list(links or []),uncertainty=list(u or [])));return rid
def claim(k,inds,text,cond=None,holder='anonymous Gemara',mode='asserted',u=None):
 cid=rec(k,'claims',inds,dict(proposition=text,conditions=list(cond or []),scope='Local acquisition/exit derivation or expressly marked continuation; stages and conditions retained',assertion_mode=mode),u=u);rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond or []),local_status=mode+' at this source stage; alternatives preserved'),[cid],u);return cid
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,x,y,rel):return rec(k,'edges',inds,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
def attr(k,inds,surface,role,candidates,scope,chain=None):return rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=list(candidates),scope=scope,transmission_chain=list(chain or [])))
gone={x['supersedes'] for x in state['records'] if 'supersedes'in x};old={x['id']:x for x in state['records'] if x['id'] not in gone};changes={}
def revise(oid,content=None,inds=None):
 if oid not in changes:
  n={k:copy.deepcopy(old[oid][k]) for k in ['id','layer','evidence','content','origin','uncertainty','links']};n['id']='kid005.revised.'+oid;n['supersedes']=oid;changes[oid]=n
 n=changes[oid]
 if content:n['content'].update(content)
 if inds is not None:n['evidence']=[ev(i) for i in inds]
 return n['id']
revise('kid004.intercourse_derivation',dict(title='Intercourse acquisition: proposed a-fortiori and initial-premise refutation',boundary='closed'),list(range(69,73)))
rec('deed','structure',list(range(73,84)),dict(title='Deed acquisition; money divorce exclusion; competing verse allocations and severance conditions',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('three_methods','structure',list(range(84,88)),dict(title='Each acquisition method resists derivation from the other two',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('canopy','structure',[88,89],dict(title='Rav Huna canopy acquisition inference and objections; continuation through Abaye replies',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference',u=['Core endpoint is within Ulla quotation; context90–100 read and separately extracted, not counted.'])
roles=['Maidservant counterexample and marriage-purpose distinction','Verse necessity question and Rav Ashi original-premise refutation','Levirate prior bond distinguishes ordinary marriage; verse remains needed','Deed acquisition question and money-to-deed a-fortiori','Money redemption powers defeat initial deed inference','Exit-entry analogy establishes deed; reverse money-divorce inference proposed','Abaye advocate/prosecutor objection; reciprocal deed challenge','Distinct deed texts versus identical currency kind','Rava written-divorce restriction; alternate deed-betrothal exclusion rejected','Why divorce exclusion preferred: verse context','Rabbi Yosi Hagelili alternative money-divorce exclusion','Sages use severance wording for complete separation','Permanent versus thirty-day wine/home conditions','Rabbi Yosi Hagelili dual lexical use versus sages','Why not infer deed from money and intercourse','Why not infer intercourse from money and deed','Why not infer money from intercourse and deed','Maidservant involuntary money example distinguished from marital acquisition','Rav Huna canopy acquisition inference using terumah','Ulla Torah-law terumah eligibility challenges initial premise']
for i,role in zip(range(70,90),roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='Gemara with scoped named explanations and cited teachings',discourse_role=role,composition='composite'))
 attr('anon'+str(i),[i],'anonymous framing','anonymous',[],role)
# Core70–72 semantic claims and replies were extracted as prior context; retain exact IDs and evidence.
qdeed=q('deed_q',[73],'From where is acquisition by deed derived?')
money_noexit=claim('money_noexit',[73],'Money does not effect divorce.',['Premise of deed a-fortiori'],'anonymous argument')
money_entry=claim('money_entry',[73],'Money effects entry into marriage.',['Premise of deed a-fortiori'],'anonymous argument')
deed_exit=claim('deed_exit',[73],'A deed effects divorce.',['Premise of deed a-fortiori'],'anonymous argument')
deed_af=claim('deed_af',[73],'The proposed a-fortiori derives deed acquisition from money, since deed also effects divorce.',['Provisional route; challenged by redemption distinction'],'anonymous argument','challenged')
edge('deed_af_answer',[73],deed_af,qdeed,'answer');edge('deed_money_analogy',[73],money_entry,deed_af,'analogy');edge('deed_exit_basis',[73],deed_exit,deed_af,'support');edge('money_exit_basis',[73],money_noexit,deed_af,'support')
redeemholy=claim('money_redeems_holy',[74],'Money redeems consecrated property.',['Distinctive power used against a-fortiori'])
redeemmaaser=claim('money_redeems_maaser',[74],'Money redeems second tithe.',['Distinctive power used against a-fortiori'])
nodeedholy=claim('deed_no_redeem_holy',[74],'A deed does not redeem consecrated property.',['Contrast with money'])
nodeedmaaser=claim('deed_no_redeem_maaser',[74],'A deed does not redeem second tithe.',['Contrast with money'])
redverse=claim('redemption_verse',[74],'ונתן הכסף וקם לו is cited for the monetary-redemption distinction.',['Local citation; not a standalone proof of every redemption detail'])
edge('redemption_objection',[73,74],redeemholy,deed_af,'objection');edge('maaser_objection',[73,74],redeemmaaser,deed_af,'objection');edge('deed_holy_distinction',[74],nodeedholy,redeemholy,'distinction');edge('deed_maaser_distinction',[74],nodeedmaaser,redeemmaaser,'distinction')
heqesh=claim('entry_exit_link',[75],'ויצאה והיתה links entry into marriage to exit.',['Verse-based analogy'])
deed_rule=claim('deed_rule',[75],'Just as exit is by deed, entry is by deed.',['Conclusion of entry-exit linkage'])
edge('deed_verse_support',[75],heqesh,deed_rule,'support');edge('deed_final_answer',[73,75],deed_rule,qdeed,'answer')
qreverse=q('reverse_link_q',[75],'Why not reverse the analogy and allow divorce by money as entry is by money?')
revhyp=claim('money_divorce_hyp',[75],'Reverse analogy would permit divorce by money.',['Proposed inference, subsequently excluded'],'anonymous argument','rejected')
abaye=claim('abaye_advocate',[76],'Abaye rejects letting money both bring in and take out: the advocate would become prosecutor.',['Explanation of money-divorce exclusion'],'Abaye')
attr('abaye',[76],'אמר אביי','speaker',['Abaye'],'Advocate/prosecutor explanation of money exclusion')
edge('abaye_reply',[75,76],abaye,qreverse,'answer');edge('abaye_rejects',[75,76],abaye,revhyp,'objection')
qdeedrev=q('deed_prosecutor_q',[76],'Would the same reasoning not bar deed acquisition, since the prosecutor becomes advocate?')
texts=claim('different_deed_texts',[77],'The content of the divorce deed differs from the content of the betrothal deed.',['Answer to deed reciprocity challenge'])
edge('texts_answer',[76,77],texts,qdeedrev,'answer')
qcoins=q('different_coins_q',[77],'Could the particular acquisition money likewise differ from the divorce money?')
currency=claim('same_currency',[77],'The currency kind remains the same despite different pieces of money.',['Reply within Abaye explanation'])
edge('currency_answer',[77],currency,qcoins,'answer');edge('currency_preserves',[76,77],currency,abaye,'support')
rava_write=claim('rava_writing',[78],'וכתב לה limits divorce to writing in this contrast.',['Rava alternative explanation'],'Rava')
rava_nomoney=claim('rava_no_money',[78],'The writing limitation excludes money divorce.',['Rava alternative explanation'],'Rava')
attr('rava',[78],'רבא אמר','speaker',['Rava'],'Alternative scriptural basis for money-divorce exclusion')
edge('rava_nomoney_support',[78],rava_write,rava_nomoney,'support');edge('rava_reply',[75,78],rava_nomoney,qreverse,'answer');edge('rava_alternative',[76,78],rava_nomoney,abaye,'qualification')
qexclude=q('exclude_deed_entry_q',[78],'Could the limitation instead exclude betrothal by writing?')
noentry=claim('no_deed_entry_hyp',[78],'Alternative reading would allow written divorce but exclude written betrothal.',['Proposed alternative exclusion'],'anonymous argument','rejected')
edge('link_rejects_no_entry',[75,78],deed_rule,noentry,'objection');edge('link_answers',[75,78],heqesh,qexclude,'answer')
qchoose=q('choose_exclusion_q',[79],'Why prefer excluding money divorce over excluding deed betrothal?')
context=claim('divorce_context',[79],'The verse stands in a divorce context, so its limitation naturally concerns divorce rather than betrothal.',['Contextual explanation, not separate historical statement'])
edge('context_answer',[79],context,qchoose,'answer');edge('context_support',[78,79],context,rava_nomoney,'support')
qyosi=q('yosi_no_money_q',[80],'Rabbi Yosi Hagelili uses the writing verse for another derivation; whence does he exclude money divorce?')
yosi=claim('yosi_book_only',[80],'ספר כריתות teaches that a document severs, and no other means does in this contrast.',['Alternative verse allocation'],'Rabbi Yosi Hagelili explanation')
attr('yosi',[80,83],'רבי יוסי הגלילי','position_holder',['Rabbi Yosi Hagelili'],'Distinct verse allocation; other use of writing verse not specified locally')
edge('yosi_answer',[80],yosi,qyosi,'answer');edge('yosi_excludes',[75,80],yosi,revhyp,'objection')
qsages=q('sages_severance_q',[81],'How do the sages use כריתות?')
sever=claim('complete_separation',[81],'כריתות requires a condition that severs between husband and wife.',['Sages explanation'],'sages')
edge('sages_answer',[81],sever,qsages,'answer')
wineforever=claim('wine_forever',[82],'A divorce conditioned on never drinking wine lacks severance.',['Condition persists forever'],'cited baraita')
homeforever=claim('home_forever',[82],'A divorce conditioned on never going to her father’s house lacks severance.',['Condition persists forever; no extra family-lifespan qualification supplied here'],'cited baraita')
wine30=claim('wine_thirty',[82],'The wine abstention condition for thirty days constitutes severance.',['Finite thirty-day duration'],'cited baraita')
home30=claim('home_thirty',[82],'The father-house condition for thirty days constitutes severance.',['Finite thirty-day duration'],'cited baraita')
for key,cid in [('wineforever',wineforever),('homeforever',homeforever),('wine30',wine30),('home30',home30)]:edge('severance_'+key,[81,82],cid,sever,'support')
yosilex=claim('yosi_lexical',[83],'Rabbi Yosi Hagelili derives the severance requirement from כרת/כריתות.',['Additional lexical derivation'],'Rabbi Yosi Hagelili')
sageslex=claim('sages_no_lexical',[83],'The sages do not accept a distinct כרת/כריתות inference.',['Disputed lexical allocation'],'sages')
edge('yosi_second_use',[81,83],yosilex,sever,'qualification');edge('lexical_difference',[83],sageslex,yosilex,'distinction')
qpair=q('pair_derivation_q',[84],'If one method cannot derive from one other, why not derive one from the remaining two?')
qdeedpair=q('deed_pair_q',[84],'Could deed be omitted and derived from money and intercourse?')
benefit=claim('money_intercourse_benefit',[84],'Money and intercourse have substantial benefit, unlike the proposed deed comparison.',['Shared feature blocks this paired inference'])
edge('deed_pair_block',[84],benefit,qdeedpair,'answer')
qintpair=q('intercourse_pair_q',[85],'Could intercourse be omitted and derived from money and deed?')
rangeclaim=claim('money_deed_range',[85],'Money and deed have a wider range of acquisitions.',['Shared feature blocks the intercourse paired inference; no unquoted catalog invented'])
edge('intercourse_pair_block',[85],rangeclaim,qintpair,'answer')
qmoneypair=q('money_pair_q',[86],'Could money be omitted and derived from intercourse and deed?')
forced=claim('intercourse_deed_forced',[86],'Intercourse and deed operate against a person’s will in their relevant acquisition/divorce settings.',['Shared feature of proposed sources; do not assert forced ordinary betrothal is valid'])
edge('money_pair_block',[86],forced,qmoneypair,'answer')
qmaid=q('maid_forced_q',[87],'Does involuntary money acquisition of a Hebrew maidservant defeat the distinction?')
maidforce=claim('maid_money_forced',[87],'Money can operate involuntarily in the Hebrew maidservant case.',['Counterexample considered'])
maritalforce=claim('money_not_forced_marriage',[87],'In marital acquisition an involuntary money case is not found in this argument.',['Scope-specific reply; maidservant is not equivalent'])
edge('marital_answer',[87],maritalforce,qmaid,'answer');edge('forced_scope',[86,87],maritalforce,forced,'qualification');edge('maid_distinction',[87],maritalforce,maidforce,'distinction')
for key,cid,inds in [('benefit',benefit,[84]),('range',rangeclaim,[84,85]),('force',forced,[84,86])]:edge('pair_answer_'+key,inds,cid,qpair,'answer')
huna=claim('huna_canopy',[88],'Rav Huna holds that canopy effects acquisition by a-fortiori inference.',['Position defended through continuation; not a final unanimous ruling'],'Rav Huna')
attr('huna',[88],'אמר רב הונא','speaker',['Rav Huna'],'Canopy as acquisition method and developing inference')
nofood=claim('money_no_terumah_hyp',[88],'Initial premise says money acquisition does not permit terumah consumption.',['Initial unqualified premise challenged by Torah-law distinction'],'Rav Huna argument','challenged')
canopyfood=claim('canopy_terumah',[88],'Canopy permits terumah consumption in the proposed comparison.',['Initial inference premise'],'Rav Huna argument')
initialaf=claim('canopy_food_af',[88],'Since money acquires without permitting terumah, canopy that permits it should acquire.',['Initial form corrected after Ulla objection'],'Rav Huna argument','challenged')
edge('initial_huna_basis',[88],initialaf,huna,'support');edge('food_basis',[88],canopyfood,initialaf,'support');edge('money_food_basis',[88],nofood,initialaf,'support')
qfood=q('money_food_q',[89],'Is it true that money acquisition does not permit terumah?')
ulla=claim('ulla_torah',[89],'By Torah law an Israelite woman betrothed to a priest may eat terumah.',['Betrothal by money in this comparison; subsequent rabbinic restriction separate'],'Ulla')
ullaverse=claim('ulla_acquired',[89],'The betrothed woman is his monetary acquisition under וכהן כי יקנה נפש קנין כספו.',['Scriptural basis quoted with Ulla teaching'],'Ulla')
attr('ulla',[89],'והאמר עולא','speaker',['Ulla'],'Quoted Torah-law eligibility; no transmission chain invented')
edge('ulla_basis',[89],ullaverse,ulla,'support');edge('ulla_objection',[88,89],ulla,nofood,'objection');edge('ulla_answers',[89],ulla,qfood,'answer')
# Necessary continuation: rabbinic decree and corrected form, then objections and Abaye replies.
qdecree=q('context.decree_q',[90],'Why did the sages prohibit eating despite Torah-law eligibility?')
decree=claim('context.decree',[90],'The restriction guards against a cup mixed for her in her father’s house which she might give to siblings.',['Rabbinic risk; brothers and sisters distinct potential recipients'],'quoted explanation accompanying Ulla')
edge('context.decree_answer',[90],decree,qdecree,'answer');edge('context.torah_qualified',[89,90],decree,ulla,'qualification')
notfinish=claim('context.money_not_finish',[91],'Money acquisition does not complete marriage.',['Corrected inference premise'],'Rav Huna argument')
canfinish=claim('context.canopy_finishes',[92],'Canopy completes marriage.',['Corrected premise; prior betrothal restriction follows'],'Rav Huna argument')
correctaf=claim('context.corrected_af',[91,92],'Money acquires despite not completing; canopy that completes should acquire.',['Corrected form of Rav Huna inference'],'Rav Huna argument')
edge('context.corrects_food_af',[88,91,92],correctaf,initialaf,'correction');edge('context.money_completion_basis',[91,92],notfinish,correctaf,'support');edge('context.canopy_completion_basis',[92],canfinish,correctaf,'support');edge('context.huna_new_basis',[88,91,92],correctaf,huna,'support')
redob=claim('context.redemption_objection',[92],'Money has the distinctive powers of redeeming consecrated property and second tithe.',['Objection to corrected money-only comparison'])
intcounter=claim('context.intercourse_counter',[92],'Intercourse supplies the counterexample to the redemption-power objection.',['Argument stage, not a new redemption rule'])
edge('context.redemption_blocks',[92],redob,correctaf,'objection');edge('context.intercourse_answers',[92],intcounter,redob,'objection')
yivfeature=claim('context.intercourse_yevamah',[93],'Intercourse has the distinctive acquisition of a yevamah.',['Objection to using intercourse alone'])
moneycounter=claim('context.money_counter',[93],'Money supplies the counterexample to the yevamah-specific objection.',['Mutual comparison stage'])
edge('context.yiv_objection',[92,93],yivfeature,intcounter,'objection');edge('context.money_reply',[93],moneycounter,yivfeature,'objection')
paircommon=claim('context.pair_common',[93],'Money and intercourse each acquire elsewhere and here; canopy, which acquires elsewhere, is proposed to acquire here.',['First common-feature argument, before benefit objection'],'Rav Huna argument','challenged')
edge('context.pair_support',[88,93],paircommon,huna,'support')
benefitob=claim('context.benefit_objection',[94],'Money and intercourse share substantial benefit, blocking that two-method common-feature inference.',['Objection'])
deedcounter=claim('context.deed_counter',[94],'Deed counters the shared-benefit objection.',['Third method added'])
edge('context.benefit_blocks',[93,94],benefitob,paircommon,'objection');edge('context.deed_reply',[94],deedcounter,benefitob,'objection')
deedfeature=claim('context.deed_exit_feature',[94],'Deed has the distinctive power to effect divorce of an Israelite woman.',['Objection to deed alone'])
paircounter=claim('context.pair_counter',[94],'Money and intercourse counter the deed-specific divorce feature.',['Mutual comparison stage'])
edge('context.deed_objection',[94],deedfeature,deedcounter,'objection');edge('context.pair_reply',[94],paircounter,deedfeature,'objection')
threecommon=claim('context.three_common',[95],'The renewed common-feature construction supports canopy acquiring here because it acquires elsewhere.',['Three-method stage after deed counterexample'],'Rav Huna argument')
edge('context.three_support',[88,95],threecommon,huna,'support');edge('context.three_extends',[93,95],threecommon,paircommon,'qualification')
forceob=claim('context.forced_objection',[96],'The common sources operate involuntarily, challenging canopy derivation.',['General objection before marital-money distinction'])
hunaforce=claim('context.huna_force_reply',[96],'Rav Huna replies that involuntary money acquisition is not found in marriage.',['Marital scope, rather than maidservant acquisition'],'Rav Huna')
edge('context.force_blocks',[95,96],forceob,threecommon,'objection');edge('context.force_answer',[96],hunaforce,forceob,'objection')
rava_three=claim('context.rava_three',[97],'Rava objects that the Mishnah enumerates three methods, not four.',['First objection to canopy acquisition'],'Rava')
rava_prior=claim('context.rava_prior',[98],'Rava objects that canopy completes only after betrothal, so canopy without betrothal cannot simply be inferred from it.',['Second objection; preserve prerequisite'],'Rava')
attr('context.rava',[97,98],'אמר רבא שתי תשובות','speaker',['Rava'],'Two distinct objections to canopy acquisition')
edge('context.rava_count',[88,97],rava_three,huna,'objection');edge('context.rava_dependency',[92,98],rava_prior,canfinish,'qualification');edge('context.rava_inference',[91,92,98],rava_prior,correctaf,'objection')
abaye_count=claim('context.abaye_count',[99],'Abaye answers that the Mishnah lists methods explicit in Scripture, omitting one not explicit.',['Answer to enumeration objection, not proof that every omission is valid'],'Abaye')
attr('context.abaye',[99,100],'א״ל אביי','speaker',['Abaye'],'Replies to Rava, interpreting Rav Huna')
edge('context.count_reply',[97,99],abaye_count,rava_three,'objection')
postmoney=claim('context.money_after_money',[100],'Money does not complete marriage after money.',['Abaye formulation of Rav Huna comparison'],'Abaye interpreting Rav Huna')
postcanopy=claim('context.canopy_after_money',[100],'Canopy completes marriage after money.',['Abaye formulation of Rav Huna comparison'],'Abaye interpreting Rav Huna')
abaye_af=claim('context.abaye_af',[100],'Rav Huna compares money that fails to complete after money yet acquires, with canopy that completes after money and therefore should acquire.',['Abaye defense; no unanimous final endorsement stated'],'Abaye interpreting Rav Huna')
edge('context.abaye_dependency_reply',[98,100],abaye_af,rava_prior,'objection');edge('context.abaye_preserves',[91,92,100],abaye_af,correctaf,'qualification');edge('context.money_after_basis',[100],postmoney,abaye_af,'support');edge('context.canopy_after_basis',[100],postcanopy,abaye_af,'support')

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
  p['coverage'].append(dict(segment_id=s['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if matches else 'none_found_after_pass',record_ids=matches,rationale=role+'. Source-first reread through5b9; next money-formula topic5b10 inspected. Prior70–72 context reused, original indices retained. '+('Evidence-bearing '+layer+' rows after omission check.' if matches else 'No explicit '+layer+' finding after pass; no invented position/question.')))
for x in p['records']:
 for e in x['evidence']:
  s=next(s for s in inv if s['id']==e['segment_id']);assert s['text'][e['start_char']:e['end_char']]==e['quote']
 for k in x['links']:assert k in active
 assert not strings([x['content'],x['links']])&set(changes)
for c in p['coverage']:
 for k in c['record_ids']:assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
(out/'INITIAL_PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'PINS.json').write_text(json.dumps(dict(pins=pins,parent_snapshot=cur,core_refs=[s['ref'] for s in core],core_indices=[s['source_index'] for s in core],revision_map=mp,independent_reading_seen=False,context_refs=[s['ref'] for s in inv[90:101]],uncertainties=['Prior70–72 claims reused without duplicate proposals.','Abaye and Rava money-divorce explanations remain alternatives; no unsupported shared derivation.','Sages versus Rabbi Yosi Hagelili verse allocations retained, unnamed other derivation not invented.','Fixed-duration wine and father-house conditions separated from indefinite conditions.','Initial terumah-based canopy inference corrected in context; Ulla Torah law distinct from rabbinic restriction.','Rava objections and Abaye responses preserved; no final unanimous canopy ruling asserted.','Context90–100 uncounted; open structure continues until those segments receive all passes.']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(proposal=h(out/'INITIAL_PROPOSAL.json'),records=len(p['records']),revisions=len(changes))))
