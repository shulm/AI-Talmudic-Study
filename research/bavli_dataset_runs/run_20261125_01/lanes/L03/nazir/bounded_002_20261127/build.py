import json,hashlib,copy
from pathlib import Path
root=Path.cwd();out=Path(__file__).parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir');read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
a=read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/a['contract_path'];assert sha(cp)==a['contract_sha256'];contract=read(cp)
for f,h in contract['production_files'].items():assert sha(root/f)==h
pins=read(out.parent/'bounded_001_20261127/PINS.json');assert sha(Path(pins['source_path']))==pins['source_sha256'];assert sha(Path(pins['source_schema_path']))==pins['source_schema_sha256'];assert read(job/'OWNER.json')==pins['owner']
cur=read(job/'CURRENT.json')['snapshot_sha256'];assert cur=='e2896b8c1d248f54ff5e233460c4fd5183f6c31e18302f425f262828d0e4a486';state=read(job/'snapshots'/(cur+'.json'));assert sha(job/'snapshots'/(cur+'.json'))==cur
review=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/nazir_review_20261127/correction_recheck/VERDICT.json';assert sha(review)=='4c0d874fb4355c12bd95571b34ec69ef53b4db0298ba6b5b5f89f204c787250e'
inv=read(job/'source_inventory.json');raw=read(Path(pins['source_path']))['text'];seg={s['ref']:s for s in inv};core=inv[10:30];assert core[0]['ref']=='Nazir 2a:11' and core[-1]['ref']=='Nazir 3a:6'
for s in inv[:34]:i,j=s['source_index'];assert raw[i][j]==s['text']
oldgone={x['supersedes'] for x in state['records'] if 'supersedes'in x};active={x['id']:x for x in state['records'] if x['id'] not in oldgone}
p={k:copy.deepcopy(read(out.parent/'bounded_001_20261127/INITIAL_PROPOSAL.json')[k]) for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256','owner','epoch','execution']};p.update(records=[],coverage=[],open_tails=[])
def ev(ref,quote=None):
 if isinstance(ref,int):ref=inv[ref]['ref']
 s=seg[ref];t=s['text'];a=0 if quote is None else t.index(quote);b=len(t) if quote is None else a+len(quote);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def evid(refs):return [ev(*r) if isinstance(r,tuple) else ev(r) for r in refs]
def rec(k,l,refs,c,links=None,u=None,origin='source_paraphrase'):
 rid='naz002.'+k;p['records'].append(dict(id=rid,layer=l,evidence=evid(refs),content=c,origin=origin,links=list(links or []),uncertainty=list(u or [])));return rid
def claim(k,refs,text,cond=None,holder='anonymous Gemara',mode='asserted',u=None):
 cid=rec(k,'claims',refs,dict(proposition=text,conditions=list(cond or []),scope='Local opening exposition or formula explanation; quoted examples remain scoped',assertion_mode=mode),u=u)
 rec(k+'.p','positions',refs,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond or []),local_status=mode+' locally; no task eligibility inferred'),[cid],u);return cid
def q(k,refs,text):return rec(k,'questions',refs,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,refs,x,y,rel):return rec(k,'edges',refs,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
def attr(k,refs,surface,role,candidates,scope):return rec(k,'attributions',refs,dict(surface=surface,role=role,candidates=list(candidates),scope=scope,transmission_chain=[]))
# Reconcile the previously open primary unit and split the two composite context conclusions without duplicating their semantic content.
changes={}
def revise(oid,content=None,refs=None):
 x=active[oid];n={k:copy.deepcopy(x[k]) for k in ['id','layer','evidence','content','origin','uncertainty','links']};n['id']='naz002.revised.'+oid;n['supersedes']=oid
 if content:n['content'].update(content)
 if refs is not None:n['evidence']=evid(refs)
 changes[oid]=n;return n['id']
order=revise('naz001.order',dict(boundary='closed',title='Kinuyim/yadot exposition order: counterexamples and local explanation resolved at 2b:3'),list(range(5,17)))
local=revise('nazfix001.context.localreason',dict(proposition='Yadot are explained first because they are derived by exposition and therefore valued.'),[15]);revise('nazfix001.context.localreason.p',dict(local_status='Local rationale for explaining yadot first, distinct from why kinuyim opens the text'),[15])
intent=revise('naz001.context.intent',dict(proposition='The אהא case is specified as intending naziriteship in the speaker’s heart, excluding merely paying another nazirite’s offerings.',conditions=['אהא with nazirite passing before him','Speaker intends naziriteship in his heart']),[19]);revise('naz001.context.intent.p',dict(conditions=['אהא with nazirite passing before him','Speaker intends naziriteship in his heart']),[19])
# Existing exact Shmuel claims remain active and will acquire coverage rather than duplicate rows.
for k,refs,title in [('aha',list(range(17,21)),'אהא: passing nazirite, disambiguation and intention'),('beautiful',list(range(21,25)),'אהא נאה: mitzvah alternative, hair gesture and pure/impure nazirite'),('like',[25],'הריני כזה: demonstrative and passing nazirite'),('mesalsel',[26,27],'מסלסל: maidservant usage versus Torah alternative'),('mekalkel',[28,29],'מכלכל: temple hair usage versus supporting the poor')]:rec('structure.'+k,'structure',refs,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
roles=['Animal example objects to last-mentioned-first order','Inheritance example objects to ordering principle','Both exposition orders occur','Personal versus animal prohibition explains examples','Inheritance starts with principal inheritance case','Renewed question and derivation-based preference','Opening with primary formulation versus explaining yadot first','Fasting ambiguity and Shmuel condition','Inference about ambiguous yadot and contextual clarification','Paying another’s offerings alternative and inner intention','Novelty question and speech/intention hypothesis','Mitzvah-beautification alternative with baraita examples','Shmuel requires grasping hair','Objection: sinful naziriteship termed beautiful','Pure/impure qualification to Rabbi Elazar HaKappar’s sinner statement','Demonstrative objection and Shmuel’s passing-nazirite condition','Hair meaning established by the household maid’s usage','Torah alternative and Shmuel’s hair gesture','Hair meaning from lime measure and Rav’s gloss','Sustenance alternative and Shmuel’s hair gesture']
for i,role in zip(range(10,30),roles):
 rec('utterance.'+str(i),'utterances',[i],dict(textual_voice='anonymous Gemara with explicitly scoped quotations and speakers',discourse_role=role,composition='composite' if i not in [12,14,22,23] else 'atomic'))
 # Do not duplicate the five existing exact named-attribution rows.
 attr('anonymous.'+str(i),[i],'anonymous Gemara','anonymous',[],role+'; named speech separately scoped')
# Counterexamples and the local ordering rationale.
a1=claim('animal_example',[10],'The animal-carrying Mishnah lists permitted then prohibited going out and begins explanation with the camel’s permitted going out.',holder='quoted anonymous Mishnah')
a2=claim('inheritance_example',[11],'The inheritance Mishnah lists inheriting/bequeathing, inheriting only, bequeathing only, neither, and first explains those who both inherit and bequeath.',holder='quoted anonymous Mishnah')
edge('animal_objection',[10],a1,'naz001.last_first','objection');edge('inheritance_objection',[11],a2,'naz001.last_first','objection')
# Existing nazfix001.context.variable preserves the actual conclusion in 2a:13.
personal=claim('personal_order',[13],'Where the prohibition concerns the person directly, the tanna explains that personal prohibition first.',['Personal prohibition examples'])
animal=claim('animal_order',[13],'Where the prohibition comes via the animal, the tanna explains the permitted case first.',['Animal-mediated prohibition example'])
inherit=claim('inheritance_order',[14],'The inheritance exposition begins with the principal inheritance case.',['Inheritance example'])
edge('animal_order_reason',[10,13],animal,a1,'support');edge('inheritance_order_reason',[11,14],inherit,a2,'support')
qagain=q('kinuyim_again',[15],'Given that either order occurs, why not explain kinuyim first here?');edge('derived_answer',[15],local,qagain,'answer')
qopen=q('open_yadot',[16],'If yadot are favored, why not begin with them?');primary=claim('primary_open',[16],'The tanna opens with the primary offering formulation, while in explanation he treats yadot first.',['Distinction between opening and exposition order']);edge('primary_answer',[16],primary,qopen,'answer')
# אהא: retain existing Shmuel answer and separate alternatives/questions.
qfast=q('fasting',[17],'Could אהא mean I shall undertake a fast?');edge('fasting_answer',[17],'nazfix001.context.aha',qfast,'answer')
qinfer=q('yadot_inference',[18],'Should one infer that Shmuel holds non-demonstrative yadot are ineffective?')
clear=claim('passing_clear',[18],'When a nazirite passes before him, the declaration is not ambiguous with another undertaking.',['Nazirite passing before speaker'])
unclear=claim('no_passing',[18],'Without a passing nazirite, אהא can mean undertaking a fast.',['No nazirite passing before speaker'])
edge('inference_clarify',[18],clear,qinfer,'answer');edge('inference_limit',[18],unclear,qinfer,'qualification')
qpay=q('pay_other',[19],'Could the speaker intend only to discharge the passing nazirite’s offerings?');edge('intent_answer',[19],intent,qpay,'answer')
qnovel=q('intent_novelty',[20],'If he intends naziriteship in his heart, what is the novelty?')
hyp=claim('speech_hypothesis',[20],'One might require the spoken declaration and inner intention to match explicitly.',['Proposed objection concerning abbreviated אהא'],'anonymous Gemara','rejected')
suff=claim('abbreviation_suffices',[20],'In this specified case the abbreviated speech suffices despite the proposed requirement that speech and heart match explicitly.',['אהא with passing nazirite and nazirite intent'],'anonymous Gemara','asserted',['Local resolution only; no general suspension of speech/intention requirements.']);edge('speech_rejection',[20],suff,hyp,'correction');edge('novelty_answer',[20],suff,qnovel,'answer')
# אהא נאה and the baraita: preserve each concrete act without converting it to nazirite intent.
qbeauty=q('mitzvah_alternative',[21],'Could אהא נאה mean beautifying oneself before God through commandments?')
beautify=claim('beautify_rule',[21],'The baraita interprets זה אלי ואנוהו as beautifying oneself before God through commandments.',holder='quoted anonymous baraita')
for k,phrase,act in [('sukkah','סוכה נאה','make a beautiful sukkah'),('lulav','לולב נאה','prepare a beautiful lulav'),('tzitzit','ציצית נאה','prepare beautiful tzitzit'),('torah','ספר תורה נאה','write a beautiful Torah scroll'),('silk','ואכרכנו בשיראין נאים','wrap the Torah scroll in beautiful silks')]:
 c=claim('beautify.'+k,[(21,phrase)],'The baraita gives the example: '+act+'.',holder='quoted anonymous baraita');edge('beautify_example.'+k,[21],c,beautify,'support')
attr('baraita',[21],'כדתניא','quoted_authority',[],'Beautification exposition and its five examples; anonymous baraita')
edge('beautify_alternative_support',[21],beautify,qbeauty,'support');edge('hair_beauty_answer',[21,22],'nazfix001.context.beautiful',qbeauty,'answer')
qsin=q('sin_beauty',[23],'How can a sinful nazirite undertaking be called beautiful?')
sinner=claim('kappar_sinner',[(24,'לרבי אלעזר הקפר דאמר נזיר חוטא')],'Rabbi Elazar HaKappar is quoted as calling a nazirite a sinner.',holder='Rabbi Elazar HaKappar',u=['Quoted premise is qualified by the anonymous reply here; not an unrestricted final ruling.'])
impure=claim('impure_limitation',[24],'The reply confines that sinner description to an impure nazirite who must undo the prior count.',['Impure nazirite whose earlier days fall'],'anonymous Gemara')
risk=claim('impure_risk',[24],'Restarting after impurity may lead him to transgress his nazirite obligations.',['Impurity requires restarting the count'],'anonymous Gemara',u=['Possibility expressed as דלמא, not certainty of transgression.'])
pure=claim('pure_not_sinner',[24],'A pure nazirite is not called a sinner in this reply.',['Pure nazirite'],'anonymous Gemara',u=['Local answer even on Rabbi Elazar HaKappar’s premise; no global reconciliation with other sugyot asserted.'])
fall=claim('days_fall',[(24,'והימים הראשונים יפלו כי טמא נזרו')],'The verse states that the earlier days fall because his naziriteship became impure.',['Nazirite impurity'],'quoted Numbers 6:12')
attr('kappar',[24],'לרבי אלעזר הקפר דאמר','quoted_authority',['Rabbi Elazar HaKappar'],'Sinner description quoted as premise; local restriction is anonymous')
edge('impure_qualification',[24],impure,sinner,'qualification');edge('risk_support',[24],risk,impure,'support');edge('verse_restart',[24],fall,risk,'support');edge('pure_answer',[23,24],pure,qsin,'answer')
# Three successive formulas: reuse exact existing Shmuel qualifications.
qlike=q('like_demonstrative',[25],'Even if he grasps his hair, has he indicated the referent of כזה?');edge('like_answer',[25],'nazfix001.context.like_this',qlike,'answer')
qcurl=q('mesalsel_meaning',[26],'How is מסלסל known to refer to hair?');maid=claim('maid_usage',[26],'The maidservant of Rabbi’s household used מסלסל בשערך when addressing a man about his hair.',holder='reported maidservant of Rabbi’s household');attr('maid',[26],'ההיא אמתא דבי רבי','speaker',['unnamed maidservant of Rabbi’s household'],'Reported usage to an unnamed man; Rabbi is not the speaker');edge('usage_answer',[26],maid,qcurl,'answer')
qtorah=q('torah_alternative',[27],'Could מסלסל refer to Torah, as סלסלה ותרוממך?');torah=claim('torah_usage',[(27,'סלסלה ותרוממך')],'The Torah alternative invokes the wording סלסלה ותרוממך in Proverbs.',['Proposed Torah reading'],'quoted Proverbs 4:8','hypothetical');edge('torah_support',[27],torah,qtorah,'support');edge('torah_answer',[27],'nazfix001.context.mesalsel',qtorah,'answer')
qkalkel=q('mekalkel_meaning',[28],'How is כילכול known to refer to hair?');lime=claim('lime_measure',[(28,'סיד ר\' יהודה אומר כדי לסוד כילכול')],'Rabbi Yehuda gives the lime measure as enough to apply to כילכול.',holder='Rabbi Yehuda');rav=claim('rav_gloss',[(28,'ואמר רב בת צידעא')],'Rav explains כילכול as the temple/sideburn region.',holder='Rav');attr('yehuda',[28],"ר' יהודה אומר",'quoted_authority',['Rabbi Yehuda'],'Lime quantity in quoted Mishnah');attr('rav',[28],'ואמר רב','speaker',['Rav'],'Gloss בת צידעא on כילכול, not Rabbi Yehuda’s identity or a dispute');edge('lime_quotation',[28],lime,qkalkel,'support');edge('rav_answer',[28],rav,qkalkel,'answer')
qfeed=q('feeding_alternative',[29],'Could מכלכל mean feeding the poor, as Joseph sustained his father and brothers?');feed=claim('feeding_usage',[(29,'ויכלכל יוסף את אביו ואת אחיו')],'The alternative draws on Joseph sustaining his father and brothers in Genesis.',['Proposed sustenance reading'],'quoted Genesis 47:12','hypothetical');edge('feeding_support',[29],feed,qfeed,'support');edge('feeding_answer',[29],'nazfix001.context.mekalkel',qfeed,'answer')
# Immutable dependency closure and all old coverage substitutions.
def strings(x):
 if isinstance(x,str):return {x}
 if isinstance(x,list):return set().union(*(strings(y) for y in x)) if x else set()
 if isinstance(x,dict):return strings(list(x.values()))
 return set()
while True:
 keys=set(changes);more=[k for k,x in active.items() if k not in keys and strings([x['content'],x['links']])&keys]
 if not more:break
 for k in more:revise(k)
mp={k:x['id'] for k,x in changes.items()}
def repl(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [repl(y) for y in x]
 if isinstance(x,dict):return {k:repl(y) for k,y in x.items()}
 return x
for x in changes.values():
 x['content']=repl(x['content']);x['links']=repl(x['links']);p['records'].append(x)
for x in p['records']:
 x['content']=repl(x['content']);x['links']=repl(x['links'])
for c in state['coverage']:
 if set(c['record_ids'])&set(mp):p['coverage'].append(repl({k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'}))
combined={k:x for k,x in active.items() if k not in changes};combined.update({x['id']:x for x in p['records']})
# Coverage reflects a manual semantic pass; evidence lookup only attaches the already adjudicated rows.
for s in core:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  matches=[x['id'] for x in combined.values() if x['layer']==layer and any(e['segment_id']==s['id'] for e in x['evidence'])]
  if layer=='reconciliation':matches=[x['id'] for x in combined.values() if x['layer'] in ['claims','edges','structure'] and any(e['segment_id']==s['id'] for e in x['evidence'])]
  p['coverage'].append(dict(segment_id=s['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if matches else 'none_found_after_pass',record_ids=matches,rationale=roles[inv.index(s)-10]+'. Read source-first with context through 3a:10; reused prior exact context records, closed ordering tail, checked alternatives, scoped attribution and omissions. '+('No independent proposition in this question-only segment.' if not matches and layer in ['claims','positions'] else 'No additional '+layer+' finding after this pass.' if not matches else 'Evidence-linked records reflect this layer.')))
for x in p['records']:
 for e in x['evidence']:
  s=next(s for s in inv if s['id']==e['segment_id']);assert s['text'][e['start_char']:e['end_char']]==e['quote']
 assert not strings([x['content'],x['links']])&set(changes),x['id']
for c in p['coverage']:
 for rid in c['record_ids']:assert rid in combined and any(e['segment_id']==c['segment_id'] for e in combined[rid]['evidence']),(c,rid)
(out/'PROPOSAL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'PINS_AND_RECONCILIATION.json').write_text(json.dumps(dict(pins=pins,parent_snapshot=cur,review_sha256=sha(review),source_indices=[s['source_index'] for s in core],core_refs=[s['ref'] for s in core],context_only=[s['ref'] for s in inv[:34] if s not in core],revision_map=mp,reused_existing_context=True,independent_reading_seen=False,open_tails=[],uncertainties=['N03 bird choice-task admission remains deferred','2b:5 encodes contextual inference question without forcing a universal doctrine for Shmuel','Local sinner distinction not projected to other passages']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(proposal_sha256=sha(out/'PROPOSAL.json'),new_and_revised_records=len(p['records']),revisions=len(changes),core20=True)))
