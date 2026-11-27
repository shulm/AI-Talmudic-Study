"""Manual source-first RH016; no independent labels consulted."""
import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');BASE='8f3bc0abcd7bcbe41afd058b7f0ab3f241ef96214b28bccbef0268ecc1884fcd'
job,segs=runner.load(J);state=runner.current(J);assert runner.sha(runner.encoded(state))==BASE;runner.authorize(J,'L03/rosh_hashanah',3)
S={s['ref'].removeprefix('Rosh Hashanah '):s for s in segs.values()};old={r['id']:r for r in state['records']};P='rh.e3.b016.';PRE='rh.e3.b015.'
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
refs=['11a:'+str(i) for i in range(16,19)]+['11b:'+str(i) for i in range(1,8)]+['12a:'+str(i) for i in range(1,11)]
def ev(ref):
 s=S[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(k,l,rr,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(rr,str):rr=[rr]
 r=dict(id=P+k,layer=l,evidence=[ev(x) for x in rr],content=c,links=list(links),uncertainty=list(unc),origin=origin);p['records'].append(r);return r['id']
C={};Q={}
def claim(k,rr,text,holder='anonymous Gemara',cond=(),mode='asserted',status='Local stated interpretation; no external factual or legal certification',unc=()):
 C[k]=add(k,'claims',rr,dict(proposition=text,conditions=list(cond),scope='Local chronology derivations and vegetable tithe discussion; source occurrences retained',assertion_mode=mode),unc=unc)
 add(k+'.p','positions',rr,dict(holder_candidates=[holder],claim_id=C[k],question_id=None,conditions=list(cond),local_status=status),links=[C[k]],unc=unc);return C[k]
def q(k,rr,text):Q[k]=add(k,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'));return Q[k]
def edge(k,rr,a,b,rel):return add(k,'edges',rr,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),links=[a,b])
def attr(k,rr,surface,role,scope,candidates=(),chain=(),unc=()):return add(k,'attributions',rr,dict(surface=surface,role=role,scope=scope,candidates=list(candidates),transmission_chain=list(chain)),unc=unc)
r=copy.deepcopy(old[PRE+'chronology']);r['id']=P+'chronology';r['supersedes']=PRE+'chronology'
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['evidence'] += [ev(x) for x in refs[:15]];r['content']['boundary']='closed';r['content']['title']='Creation, patriarch, redemption and flood chronology with completed derivations';p['records'].append(r)
for c in state['coverage']:
 if PRE+'chronology' in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[P+'chronology' if x==PRE+'chronology' else x for x in c['record_ids']];c['rationale']+=' Chronology continuation completed through12a5 with immutable successor.';p['coverage'].append(c)
add('vegetables','structure',refs[15:],dict(title='Vegetable tithe terminology, collection thresholds and year boundary; crossfolio harvest ruling continues',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference');p['open_tails']=[P+'vegetables']
roles=['Remembrance source question and Elazar word analogy','Visitation analogy connects Hannah and Sarah','Joseph release source starts','Joseph verse completes across folio','Labor cessation burden-word analogy','Nisan past and Tishrei future redemption derivation','Yehoshua Nisan redemption and guarded-night source','Other view guarded against harmful beings','Yehoshua flood date, seasonal course and changed cosmos','Eliezer flood date and seasonal course','Eliezer changed cosmos account continues','Second-month problem and second-to-judgment answer','What changed on Eliezer view question','Rav Hisda hot corruption and hot judgment analogy','Israel and nations chronology conventions','Vegetables/tithes/vows list and vegetable meaning','Apparent duplication distinguished rabbinic/Torah','Ordering preference and Mishnah a fortiori','Singular-versus-plural tithes/vegetables and two collection forms','Vegetable picking before sunset; case continues next folio']
voices=['Rabbi Elazar','Rabbi Elazar continued','anonymous Gemara','anonymous Gemara continued','anonymous Gemara','anonymous Gemara on Eliezer account','Rabbi Yehoshua and anonymous derivation','anonymous reply on Eliezer side','Rabbi Yehoshua quoted','Rabbi Eliezer quoted','Rabbi Eliezer continued','anonymous Gemara','anonymous Gemara','Rav Hisda quoted','anonymous baraita','anonymous tanna and Gemara','anonymous Gemara','anonymous Gemara','anonymous Gemara citing Mishnah','anonymous baraita']
for i,(ref,role,voice) in enumerate(zip(refs,roles,voices)):
 add('u'+str(i),'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
 if i not in [0,1,6,8,9,10,13]:attr('frame'+str(i),ref,'anonymous framing','anonymous',role)
q('remember_q','11a:16','What establishes that Sarah, Rachel and Hannah were remembered on Rosh Hashanah?')
claim('rachel_remember','11a:16','Rachel’s verse uses remembrance wording.',holder='Rabbi Elazar derivation')
claim('hannah_remember','11a:16','Hannah’s verse uses remembrance wording.',holder='Rabbi Elazar derivation')
claim('rh_remember','11a:16','The Rosh Hashanah verse uses remembrance wording with teruah.',holder='Rabbi Elazar derivation')
claim('remember_analogy','11a:16','Rabbi Elazar connects the remembrance passages to Rosh Hashanah by זכירה/זכירה.',holder='Rabbi Elazar')
attr('elazar',['11a:16','11a:17'],'א״ר אלעזר','speaker','Remembrance/visitation derivation',['Rabbi Elazar (explicit printed אלעזר)'])
for k in ['rachel_remember','hannah_remember','rh_remember']:edge(k+'_support','11a:16',C[k],C['remember_analogy'],'support')
edge('remember_answer','11a:16',C['remember_analogy'],Q['remember_q'],'answer')
claim('hannah_visit','11a:17','Hannah’s verse also uses visitation wording.',holder='Rabbi Elazar derivation continued')
claim('sarah_visit','11a:17','Sarah’s verse uses visitation wording.',holder='Rabbi Elazar derivation continued')
claim('visit_analogy',['11a:16','11a:17'],'The פקידה/פקידה analogy connects Sarah to Hannah in the Rosh Hashanah derivation.',holder='Rabbi Elazar')
for k in ['hannah_visit','sarah_visit']:edge(k+'_support','11a:17',C[k],C['visit_analogy'],'support')
edge('visit_answer',['11a:16','11a:17'],C['visit_analogy'],Q['remember_q'],'answer')
for prefix in ['el','ye']:
 for person in ['rachel','hannah']:edge(prefix+'_'+person+'_proof','11a:16',C['remember_analogy'],PRE+prefix+'_'+person,'support')
 edge(prefix+'_sarah_proof',['11a:16','11a:17'],C['visit_analogy'],PRE+prefix+'_sarah','support')
q('joseph_q','11a:18','What establishes Joseph’s release from prison on Rosh Hashanah?')
claim('joseph_verse',['11a:18','11b:1'],'The Psalm’s shofar/festival/statute passage is linked to its testimony of Joseph going out.')
edge('joseph_answer',['11a:18','11b:1'],C['joseph_verse'],Q['joseph_q'],'answer')
for prefix in ['el','ye']:edge(prefix+'_joseph_proof',['11a:18','11b:1'],C['joseph_verse'],PRE+prefix+'_joseph','support')
claim('egypt_burdens','11b:2','The Egypt verse speaks of bringing Israel out from burdens.')
claim('psalm_burden','11b:2','The Psalm speaks of removing burden from the shoulder.')
claim('labor_analogy','11b:2','Shared burden wording connects cessation of Egyptian labor with the Rosh Hashanah Psalm.')
for k in ['egypt_burdens','psalm_burden']:edge(k+'_support','11b:2',C[k],C['labor_analogy'],'support')
for prefix in ['el','ye']:edge(prefix+'_labor_proof','11b:2',C['labor_analogy'],PRE+prefix+'_labor','support')
claim('past_nisan_repeat','11b:3','Past redemption in Nisan is recalled as already established.',status='Repeated source occurrence, not an additional unique topic')
claim('future_tishrei_repeat','11b:3','Future redemption in Tishrei is the Eliezer-side assertion now being derived.',holder='Eliezer-side account')
claim('shofar_rh','11b:3','The Rosh Hashanah Psalm contains shofar wording.')
claim('shofar_future','11b:3','The future redemption verse speaks of a great shofar.')
claim('shofar_analogy','11b:3','The shofar/shofar comparison grounds future Tishrei redemption.',holder='Eliezer-side account')
for k in ['shofar_rh','shofar_future']:edge(k+'_support','11b:3',C[k],C['shofar_analogy'],'support')
edge('future_tishrei_proof','11b:3',C['shofar_analogy'],C['future_tishrei_repeat'],'support')
claim('ye_past_repeat','11b:4','Yehoshua states past redemption in Nisan.',holder='Rabbi Yehoshua',status='Repeated occurrence')
claim('ye_future_repeat','11b:4','Yehoshua states future redemption in Nisan.',holder='Rabbi Yehoshua',status='Repeated occurrence')
q('ye_redemption_q','11b:4','What is the source for Yehoshua’s future Nisan redemption?')
claim('guarded_creation','11b:4','The guarded night is interpreted as reserved from the six days of creation.',holder='Yehoshua-side account')
attr('ye_redemption','11b:4','ר׳ יהושע אומר','quoted_authority','Nisan redemption account',['Rabbi Yehoshua'])
edge('guarded_answer','11b:4',C['guarded_creation'],Q['ye_redemption_q'],'answer');edge('guarded_proof','11b:4',C['guarded_creation'],C['ye_future_repeat'],'support')
claim('guarded_harm','11b:5','The other view interprets the night as guarded from harmful beings.',holder='Eliezer-side reply',unc=['Identity follows the two explicit competing accounts, not an unnamed pair assigned by order alone.'])
edge('guarded_distinction',['11b:4','11b:5'],C['guarded_harm'],C['guarded_creation'],'distinction')
# Flood accounts preserve identical reported operations as separate source occurrences.
for prefix,holder,date,ref,continuation,course,water in [('ye','Rabbi Yehoshua','seventeenth of Iyyar','11b:6','11b:6','sets','diminish'),('el','Rabbi Eliezer','seventeenth of Marheshvan','11b:7','12a:1','rises','increase')]:
 claim(prefix+'_flood_date',ref,'The flood day was the '+date+'.',holder=holder)
 claim(prefix+'_kimah',ref,'At that season Kimah '+course+' during the day.',holder=holder)
 claim(prefix+'_springs',ref,'At that season the springs '+water+'.',holder=holder)
 claim(prefix+'_conduct',continuation,'Because people changed their conduct, God changed creation’s course for them.',holder=holder)
 claim(prefix+'_raise',continuation,'God raised Kimah during the day in this flood account.',holder=holder,unc=['For Eliezer, subsequent question asks what changed; preserve asserted action rather than silently correct the text.'] if prefix=='el' else [])
 claim(prefix+'_stars',continuation,'God removed two stars from Kimah in this account.',holder=holder)
 claim(prefix+'_flood',continuation,'God brought the flood upon the world.',holder=holder)
 attr(prefix+'_flood_authority',[ref,continuation] if ref!=continuation else ref,'רבי יהושע אומר' if prefix=='ye' else 'ר׳ אליעזר אומר','quoted_authority','Flood date and altered-creation account',[holder])
 edge(prefix+'_conduct_support',continuation,C[prefix+'_conduct'],C[prefix+'_flood'],'support')
edge('flood_dates',['11b:6','11b:7'],C['ye_flood_date'],C['el_flood_date'],'distinction')
q('second_month_q','12a:2','The second-month wording fits Yehoshua; what does second mean for Eliezer?')
claim('second_judgment','12a:2','For Eliezer, second means second to judgment.')
edge('second_answer','12a:2',C['second_judgment'],Q['second_month_q'],'answer')
q('changed_q','12a:3','Changing the course fits Yehoshua; what changed according to Eliezer?')
claim('hot_corruption','12a:4','Rav Hisda says they corrupted themselves with heat in transgression.',holder='Rav Hisda')
claim('hot_judgment','12a:4','Rav Hisda says they were judged with hot water.',holder='Rav Hisda')
claim('subsiding_analogy','12a:4','The subsiding-waters wording is compared with the king’s wrath subsiding.',holder='Rav Hisda account')
attr('hisda','12a:4','דאמר רב חסדא','quoted_authority','Hot corruption and hot judgment explanation',['Rav Hisda'])
edge('heat_proof','12a:4',C['subsiding_analogy'],C['hot_judgment'],'support');edge('heat_answer',['12a:3','12a:4'],C['hot_judgment'],Q['changed_q'],'answer')
claim('israel_flood','12a:5','Sages of Israel count the flood according to Eliezer.',holder='anonymous baraita')
claim('israel_seasons','12a:5','Sages of Israel count the seasonal cycle according to Yehoshua.',holder='anonymous baraita')
claim('nations_flood','12a:5','Sages of the nations count even the flood according to Yehoshua.',holder='anonymous baraita',unc=['Even retained; no additional independent seasonal-rule assertion fabricated.'])
# Vegetable terminology and distinct collection thresholds.
for k,item in [('vegetable','vegetables'),('tithes','tithes'),('vows','vows')]:claim('list_'+k,'12a:6','The tanna’s list includes '+item+'.',holder='anonymous tanna')
q('vegetable_meaning','12a:6','What does vegetables mean here?')
claim('vegetable_tithe','12a:6','Vegetables refers to vegetable tithe.')
edge('vegetable_answer','12a:6',C['vegetable_tithe'],Q['vegetable_meaning'],'answer')
q('tithe_duplicate','12a:7','Is that not already included in tithes?')
claim('rabbinic_vegetables','12a:7','The vegetable entry teaches rabbinic tithing.')
claim('torah_tithes','12a:7','The tithes entry teaches Torah tithing.')
for k in ['rabbinic_vegetables','torah_tithes']:edge(k+'_answer','12a:7',C[k],Q['tithe_duplicate'],'answer')
q('order_q','12a:8','Why not teach the Torah rule first?')
claim('beloved_first','12a:8','The rabbinic item is put first because it is especially cherished.')
claim('mishnah_rabbinic','12a:8','Our Mishnah states the rabbinic item.')
claim('torah_follows','12a:8','The Torah item follows all the more so.')
edge('order_answer','12a:8',C['beloved_first'],Q['order_q'],'answer');edge('afortiori','12a:8',C['mishnah_rabbinic'],C['torah_follows'],'support')
q('singular_tithe','12a:9','Why not use singular tithe for both animal and grain tithes?')
q('singular_vegetable','12a:9','Why not use singular vegetable?')
claim('two_vegetables','12a:9','There are two forms of vegetables for the stated completion rule.')
claim('bundled_threshold','12a:9','Vegetables ordinarily bundled reach the stated threshold when bundled.',holder='quoted Mishnah',cond=['Vegetable ordinarily bundled'])
claim('unbundled_threshold','12a:9','Vegetables not ordinarily bundled reach the stated threshold when the vessel is filled.',holder='quoted Mishnah',cond=['Vegetable not ordinarily bundled'])
edge('vegetable_plural_answer','12a:9',C['two_vegetables'],Q['singular_vegetable'],'answer')
for k in ['bundled_threshold','unbundled_threshold']:edge(k+'_support','12a:9',C[k],C['two_vegetables'],'support')
claim('picking_case',['12a:10','12b:1'],'The baraita considers vegetables picked before New Year sunset and again after sunset.',holder='anonymous baraita',mode='hypothetical',cond=['Two picking times straddling the year boundary'])
# Necessary crossfolio context is semantic evidence, not new core coverage.
for k,act,direction in [('teruma_new_old','terumah','new for old'),('teruma_old_new','terumah','old for new'),('tithe_new_old','tithing','new for old'),('tithe_old_new','tithing','old for new')]:
 claim('context.'+k,['12a:10','12b:1'],'One may not separate '+act+' from '+direction+' in this case.',holder='anonymous baraita',cond=['Vegetables picked on opposite sides of New Year sunset'],status='Read continuation context, not counted as core')
for k,year,tithe in [('second_first','second','first tithe'),('second_second','second','second tithe'),('third_first','third','first tithe'),('third_poor','third','poor tithe')]:claim('context.'+k,'12b:1','The '+year+' year requires '+tithe+'.',holder='anonymous baraita',cond=['Transition from second to third year'],status='Uncounted continuation context')
rationales=['Elazar remembrance analogy with Rachel/Hannah/RoshHashanah evidence; Sarah linked by following visitation analogy.','Hannah/Sarah visitation terms and analogy separate; original chronology claims reused.','Joseph source question begins; full Psalm connection spans next folio.','Joseph Psalm continuation completes without index shift.','Two burden passages and connecting inference; previous labor claims reused.','Past Nisan recalled; Tishrei future claim and two shofar premises distinct.','Yehoshua repeated past/future Nisan claims and guarded-night source retained.','Other guarded-night reading attributed by explicit preceding two-account context.','Yehoshua date, Kimah setting, diminished springs, conduct, rising, two stars and flood separate.','Eliezer date, Kimah rising and increased springs separate.','Eliezer creation-change account repeats operations; subsequent objection preserved rather than harmonized away.','Second-month objection and second-to-judgment explanation.','What-changed question scoped to Eliezer.','Hisda hot corruption, hot judgment and subsiding analogy separate.','Israel flood, Israel seasonal cycle and nations flood conventions distinct.','Three list categories and explicit vegetable meaning question.','Tithe duplication question; rabbinic/Torah entries distinct.','Ordering question, cherished-first response and Mishnah a fortiori.','Both singular wording questions retained; two vegetable collection thresholds separate.','Crossfolio case begins before sunset; nextfolio prohibition and year-specific tithe outcomes retained as uncounted context.']
combined={r['id']:r for r in state['records'] if r['release_state']=='valid' and r['id']!=PRE+'chronology'};combined.update({r['id']:r for r in p['records']})
for ref,why in zip(refs,rationales):
 sid=S[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in combined.values() if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  reason=why+' Actual '+layer+' source pass; no independent acceptance or task qualification.'
  if layer=='reconciliation':reason='Omission reread: '+why+' Context through12b5 read;12b6 vow discussion boundary inspected.'
  elif not ids:reason+=' No additional supported record after pass; inherited quoted voice retains scope in adjacent records.'
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
runner.validate_apply(state,p,segs,job)
runner.immutable(OUT/'INITIAL_PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'SOURCE_RECONCILIATION.json',runner.encoded({'base_snapshot':BASE,'core_refs':refs,'source_indices':[S[x]['source_index'] for x in refs],'omission_rationales':dict(zip(refs,rationales)),'context_read':'11a13–15 preceding;12b1–5 following;12b6 boundary','reused_records':'Prior Sarah/Rachel/Hannah/Joseph/labor chronology claims linked to proofs; primary chronology immutably closed.','context_semantics':'12b1 harvest prohibition and tithe-year outcomes produced but uncounted;12b2–5 proof read but unproduced.','uncertainties':['No astronomical harmonization imposed on Kimah account.','Eliezer changed-course objection and hot-water reply preserved.','Source conventions not adjudicated historical truth.','No forced explicit answer to singular-tithe question beyond source’s vegetable clarification.'],'next_source':'Rosh Hashanah12b:1','open_tail':P+'vegetables','independent_reading_seen':False}))
print(json.dumps({'records':len(p['records']),'cores':len(refs),'proposal':runner.sha(runner.encoded(p))}))
