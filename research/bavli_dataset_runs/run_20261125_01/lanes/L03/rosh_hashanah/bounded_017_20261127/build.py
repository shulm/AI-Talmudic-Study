"""Manual source-first RH017; no independent labels consulted."""
import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');BASE='a6eb2f7edae5b8d70a6ff7ba73bbe83bcd8f5173d370d3c5712df5c867c500b4'
job,segs=runner.load(J);state=runner.current(J);assert runner.sha(runner.encoded(state))==BASE;runner.authorize(J,'L03/rosh_hashanah',3)
S={s['ref'].removeprefix('Rosh Hashanah '):s for s in segs.values()};old={r['id']:r for r in state['records']};P='rh.e3.b017.';PRE='rh.e3.b016.'
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
refs=['12b:'+str(i) for i in range(1,14)]+['13a:'+str(i) for i in range(1,8)]
def ev(ref):
 s=S[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(k,l,rr,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(rr,str):rr=[rr]
 r=dict(id=P+k,layer=l,evidence=[ev(x) for x in rr],content=c,links=list(links),uncertainty=list(unc),origin=origin);p['records'].append(r);return r['id']
C={};Q={}
def claim(k,rr,text,holder='anonymous Gemara',cond=(),mode='asserted',status='Local stated interpretation; no external factual or legal certification',unc=()):
 C[k]=add(k,'claims',rr,dict(proposition=text,conditions=list(cond),scope='Local tithe-year, vow-year and one-third crop threshold discussion; original occurrences retained',assertion_mode=mode),unc=unc)
 add(k+'.p','positions',rr,dict(holder_candidates=[holder],claim_id=C[k],question_id=None,conditions=list(cond),local_status=status),links=[C[k]],unc=unc);return C[k]
def q(k,rr,text):Q[k]=add(k,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'));return Q[k]
def edge(k,rr,a,b,rel):return add(k,'edges',rr,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),links=[a,b])
def attr(k,rr,surface,role,scope,candidates=(),chain=(),unc=()):return add(k,'attributions',rr,dict(surface=surface,role=role,scope=scope,candidates=list(candidates),transmission_chain=list(chain)),unc=unc)
r=copy.deepcopy(old[PRE+'vegetables']);r['id']=P+'vegetables';r['supersedes']=PRE+'vegetables'
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['evidence'] += [ev(x) for x in refs[:5]];r['content']['boundary']='closed';r['content']['title']='Vegetable harvest years and first/second/poor tithe derivations';p['records'].append(r)
for c in state['coverage']:
 if PRE+'vegetables' in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[P+'vegetables' if x==PRE+'vegetables' else x for x in c['record_ids']];c['rationale']+=' Closed through12b5 by immutable successor.';p['coverage'].append(c)
add('vows','structure',refs[5:8],dict(title='Twelve months versus this-year vow wording',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('third','structure',refs[8:],dict(title='Crop maturity threshold and proofs, objections and retraction',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference');p['open_tails']=[P+'third']
roles=['Picking-year outcomes continued','Third-year tithe source question and Yehoshua ben Levi exposition','First tithe cancellation challenge and inheritance analogy','Repeated baraita and Yehudah alternative proof','Eliezer ben Yaakov inheritance proof','Vow wording alternatives','Even view denying one day as year accepts distress rationale','Nisan alternative and ordinary language reply','Fenugreek/grain/olive Mishnah','Fenugreek seed clarification','Threshold source and Rav Asi report with alternate Yosi attribution','Seventh-to-eighth-year grain conclusion','Zeira addresses Asi across folio','Alternative extension of seventh year until festival','Asif verse and redundant collection interpretation','Harvest interpretation and one-third knowledge','Yirmeyah challenges precision; Zeira defends measures','Water and food threshold paired examples','Fabric threshold paired example','Yirmeyah retracts and introduces colleagues question to Kahana']
voices=['anonymous baraita','Rabbi Yehoshua ben Levi','anonymous continuation','Rabbi Yehudah in baraita','Rabbi Eliezer ben Yaakov','anonymous baraita','anonymous Gemara','anonymous Gemara','quoted Mishnah','anonymous Gemara','Rav Asi reporting Rabbi Yohanan; variant Yosi the Galilean','reported exposition continued','Rabbi Zeira addressing Rav Asi','Rabbi Zeira continued','anonymous reply','anonymous reply continued','Rabbi Yirmeyah and Rabbi Zeira dialogue','Rabbi Zeira reply continued','Rabbi Zeira reply continued','Rabbi Yirmeyah retracting and reporting colleagues']
for i,(ref,role,voice) in enumerate(zip(refs,roles,voices)):
 add('u'+str(i),'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
 attr('frame'+str(i),ref,voice,'anonymous' if voice.startswith('anonymous') else 'speaker',role,[] if voice.startswith('anonymous') else [voice])
q('third_source','12b:2','What is the source of the third-year tithe allocation?')
claim('one_tithe','12b:2','The third-year verse is read as a year with only one tithe of the relevant competing allocations.',holder='Rabbi Yehoshua ben Levi',unc=['Not a denial of first and poor tithes together; immediately specified by the source.'])
for k,t in [('first','first tithe remains'),('poor','poor tithe applies'),('second','second tithe ceases')]:claim('third_'+k,'12b:2','In the third year '+t+'.',holder='Rabbi Yehoshua ben Levi',cond=['Third-year allocation'])
attr('ybl','12b:2','ריב״ל','speaker','Third-year exposition',['Rabbi Yehoshua ben Levi'])
for k in ['first','poor','second']:edge('third_'+k+'_answer','12b:2',C['third_'+k],Q['third_source'],'answer');edge('one_'+k,'12b:2',C['one_tithe'],C['third_'+k],'support')
q('first_cancel','12b:3','Could first tithe also cease in the third year?')
claim('inheritance_word','12b:3','The Levite tithe verse calls the gift an inheritance.')
claim('inheritance_continuity','12b:3','Inheritance has no interruption in this analogy.')
claim('first_continuity','12b:3','First tithe has no interruption by comparison to inheritance.')
edge('inheritance_basis','12b:3',C['inheritance_word'],C['first_continuity'],'support');edge('inheritance_analogy','12b:3',C['inheritance_continuity'],C['first_continuity'],'analogy');edge('first_answer','12b:3',C['first_continuity'],Q['first_cancel'],'answer')
for k,t in [('one','Third year is described as having one tithe in the relevant allocation.'),('first','First tithe remains in the third year.'),('poor','Poor tithe applies in the third year.'),('second','Second tithe ceases in the third year.')]:claim('baraita_'+k,'12b:4',t,holder='Rabbi Yehudah in repeated baraita',status='Repeated distinct source occurrence')
q('baraita_first_cancel','12b:4','Could first tithe also cease, in the repeated baraita?')
claim('levite_comes','12b:4','Whenever the Levite comes, give him his portion, as derived from ובא הלוי.',holder='Rabbi Yehudah')
attr('yehudah','12b:4','דברי ר׳ יהודה','quoted_authority','Whenever the Levite comes proof',['Rabbi Yehudah']);edge('levite_answer','12b:4',C['levite_comes'],Q['baraita_first_cancel'],'answer')
claim('eby_no_need','12b:5','Eliezer ben Yaakov says Yehudah’s proof is not needed.',holder='Rabbi Eliezer ben Yaakov')
claim('eby_inheritance','12b:5','The Levite tithe is compared by the verse to inheritance.',holder='Rabbi Eliezer ben Yaakov')
claim('eby_unbroken','12b:5','Inheritance has no interruption.',holder='Rabbi Eliezer ben Yaakov')
claim('eby_first','12b:5','First tithe has no interruption.',holder='Rabbi Eliezer ben Yaakov')
attr('eby','12b:5','רבי אליעזר בן יעקב אומר','quoted_authority','Alternative inheritance proof',['Rabbi Eliezer ben Yaakov'])
edge('eby_alternative',['12b:4','12b:5'],C['eby_no_need'],C['levite_comes'],'distinction');edge('eby_analogy','12b:5',C['eby_unbroken'],C['eby_first'],'analogy');edge('eby_basis','12b:5',C['eby_inheritance'],C['eby_first'],'support');edge('eby_answer',['12b:4','12b:5'],C['eby_first'],Q['baraita_first_cancel'],'answer')
claim('vow_twelve','12b:6','A benefit prohibition from another person stated for a year lasts twelve months from day to day.',holder='anonymous baraita',cond=['Wording לשנה'])
claim('vow_this','12b:6','A benefit prohibition stated for this year is fulfilled when the first of Tishrei arrives, even if made on29Elul.',holder='anonymous baraita',cond=['Wording לשנה זו','Even made29Elul'])
claim('vow_even','12b:7','This result holds even for the view that one day in a year does not count as a year.',cond=['This-year benefit prohibition'])
claim('vow_distress','12b:7','He accepted distress upon himself and has already suffered it.',cond=['This-year benefit prohibition'])
edge('vow_reason','12b:7',C['vow_distress'],C['vow_even'],'support');edge('vow_qualify',['12b:6','12b:7'],C['vow_even'],C['vow_this'],'qualification')
q('nisan','12b:8','Why not end the stated year at Nisan?');claim('ordinary','12b:8','Vows follow ordinary human language.');edge('ordinary_answer','12b:8',C['ordinary'],Q['nisan'],'answer')
for k,text in [('fenugreek','Fenugreek reaches the tithe threshold when it grows.'),('grain','Grain reaches the stated threshold at one-third growth.'),('olives','Olives reach the stated threshold at one-third growth.')]:claim(k,'12b:9',text,holder='quoted Mishnah')
q('growth','12b:10','What does when it grows mean?');claim('seed_growth','12b:10','The fenugreek phrase means growth to seeds.');edge('seed_answer','12b:10',C['seed_growth'],Q['growth'],'answer');edge('seed_qualify',['12b:9','12b:10'],C['seed_growth'],C['fenugreek'],'qualification')
q('third_threshold','12b:11','What establishes one-third for grain and olives?');q('eighth_festival','12b:11','Why call Sukkot the release year when it is already the eighth year?')
attr('asi_yohanan','12b:11','אמר רב אסי א״ר יוחנן','transmitter','One-third threshold verse exposition',['Rav Asi','Rabbi Yohanan'],['Rav Asi','Rabbi Yohanan'])
attr('yosi_variant','12b:11','ומטו בה משמיה דרבי יוסי הגלילי','reported_authority','Alternate report of the exposition',['Rabbi Yosi the Galilean'],unc=['Alternate attribution; unspecified reporters, not an invented single sequential chain.'])
claim('seventh_eighth','12b:12','Grain that reached one-third in seventh year before New Year is treated by seventh-year rules in the eighth.',holder='reported exposition',cond=['One-third before New Year in seventh year'])
edge('eighth_answer',['12b:11','12b:12'],C['seventh_eighth'],Q['eighth_festival'],'answer');edge('threshold_answer',['12b:11','12b:12'],C['seventh_eighth'],Q['third_threshold'],'answer')
q('no_growth',['12b:13','13a:1'],'Could the verse instead cover grain with no previous growth, extending release until Sukkot?')
claim('no_growth_proposal',['12b:13','13a:1'],'Perhaps release continues until Sukkot even where growth had not begun.',holder='Rabbi Zeira challenge to Rav Asi',mode='hypothetical',status='Challenged proposal, not accepted conclusion')
attr('zeira_asi',['12b:13','13a:1'],'אמר ליה ר׳ זירא לרב אסי','speaker','Challenge directed to Rav Asi',['Rabbi Zeira'],unc=['Rav Asi is addressee, not a transmission-chain member.'])
q('asif_meaning','13a:2','What is אסיף: merely a festival in gathering time, despite the separate באספך wording?')
claim('asif_redundant','13a:2','The collection-time reading is challenged because באספך already says it.')
claim('asif_harvest','13a:3','The initial reply interprets אסיף as harvest.',status='Initial interpretation later challenged by Hanina and withdrawn by Zeira in13a14–15')
claim('known_third','13a:3','Sages know grain harvested at Sukkot had reached one-third before New Year.',status='Initial proof assertion; exact proof challenged in continuation')
claim('outgoing_year','13a:3','The verse calls that crop outgoing-year produce.',status='Initial proof based on harvest interpretation; later challenged')
edge('redundancy_answer','13a:2',C['asif_redundant'],Q['asif_meaning'],'answer');edge('harvest_answer',['13a:2','13a:3'],C['asif_harvest'],Q['asif_meaning'],'answer');edge('known_support','13a:3',C['known_third'],C['outgoing_year'],'support');edge('outgoing_answer',['13a:1','13a:3'],C['outgoing_year'],Q['no_growth'],'answer')
q('precision','13a:4','Do the sages know the difference between exactly one-third and less?')
attr('yirmeyah','13a:4','א״ל ר׳ ירמיה לר׳ זירא','speaker','Precision challenge',['Rabbi Yirmeyah'],unc=['Zeira is addressee.'])
claim('measure_rebuke','13a:4','Zeira tells Yirmeyah not to take himself outside halakhic practice.',holder='Rabbi Zeira reply')
claim('all_measures','13a:4','All sages’ measures operate with such exact boundaries.',holder='Rabbi Zeira reply');edge('measure_answer','13a:4',C['all_measures'],Q['precision'],'answer')
for k,ref,text,cond in [('water_full','13a:5','Immersion is possible in forty seah.','Forty seah'),('water_less','13a:5','Immersion is not possible in forty seah less a kortov.','Forty seah minus kortov'),('food_full','13a:5','An egg-size conveys food impurity.','Egg-size'),('food_less','13a:5','An egg-size less a sesame seed does not convey food impurity.','Egg-size minus sesame seed'),('fabric_full','13a:6','A three-by-three piece is susceptible to midras impurity.','Three by three; unit not expanded beyond source'),('fabric_less','13a:6','Three by three less one thread is not susceptible to midras impurity.','Three by three minus one thread')]:
 claim(k,ref,text,holder='Rabbi Zeira reply continued',cond=[cond]);edge(k+'_example',ref,C[k],C['all_measures'],'support')
claim('yirmeyah_retract','13a:7','Yirmeyah retracts his precision challenge as not a valid statement.',holder='Rabbi Yirmeyah');edge('retract_precision',['13a:4','13a:7'],C['yirmeyah_retract'],Q['precision'],'retraction')
q('entry_omer','13a:7','From where did Israel obtain the omer offered on entering the land?')
attr('colleagues','13a:7','דבעו מיניה חברייא מרב כהנא','speaker','Colleagues ask Rav Kahana about entry omer',['colleagues (unnamed)'],unc=['Rav Kahana is recipient; Yirmeyah reports the exchange.'])
claim('foreign_harvest','13a:7','Your harvest excludes a gentile’s harvest in the omer question.',holder='reported colleagues question',cond=['Proposed crop grown under gentile possession'])
# Full necessary continuation retained as uncounted context; later retraction constrains current proof.
for ref,role in [('13a:8','Whether omer was offered challenged and answered from eating date'),('13a:9','Kahana replies before-third crop'),('13a:10','Knowledge challenge and analogy'),('13a:11','No-growth alternative versus quarter growth'),('13a:12','Jordan tenth day and five-day challenge'),('13a:13','Quarter/sixth challenge and land-of-deer response'),('13a:14','Hanina attacks harvest interpretation'),('13a:15','Zeira concedes argument demolished'),('13a:16','Replacement derivation introduced'),('13b:1','Read three as third'),('13b:2','Literal verse need objection and other verse answer')]:add('context.u'+ref,'utterances',ref,dict(textual_voice='Gemara continuation with explicit speakers separately recorded',discourse_role=role,composition='composite'))
q('context.offered','13a:8','How know they offered the omer rather than not offering it?')
claim('context.eating','13a:8','They ate produce only on the morrow of Passover, not before.')
claim('context.offering','13a:8','The eating sequence establishes offering the omer before eating.');edge('context.eating_proof','13a:8',C['context.eating'],C['context.offering'],'support');edge('context.offered_answer','13a:8',C['context.offering'],Q['context.offered'],'answer')
claim('context.before_third','13a:9','The omer came from crop that had not reached one-third in gentile possession.',holder='Rav Kahana reply',cond=['Entry omer']);attr('context.kahana','13a:9','אמר להן','speaker','Answer to colleagues in13a7',['Rav Kahana']);edge('context.entry_answer',['13a:7','13a:9'],C['context.before_third'],Q['entry_omer'],'answer')
q('context.growth_unknown','13a:10','Perhaps it reached one-third and they did not know?');claim('context.knowledge','13a:10','They must have known the omer crop’s stage; likewise sages know here.');edge('context.knowledge_answer','13a:10',C['context.knowledge'],Q['context.growth_unknown'],'answer');edge('context.precision_support',['13a:4','13a:10'],C['context.knowledge'],C['yirmeyah_retract'],'support')
q('context.no_growth','13a:11','Perhaps it had not grown at all; that would not prove distinguishing a quarter from one-third?')
claim('context.jordan','13a:12','The people crossed the Jordan on the tenth of the month.')
q('context.five_days','13a:12','Could entirely ungrown grain fill in five days?');edge('context.date_basis','13a:12',C['context.jordan'],Q['context.five_days'],'support')
q('context.partial_days','13a:13','Could even a quarter or sixth-grown crop fill in five days?')
claim('context.swift_land','13a:13','The land called ארץ צבי supplies the exceptional growth answer in either case.',unc=['No forced resolution that this proves precise one-third knowledge; same response available for no prior growth.']);edge('context.swift_answer','13a:13',C['context.swift_land'],Q['context.partial_days'],'answer');edge('context.swift_other',['13a:12','13a:13'],C['context.swift_land'],Q['context.five_days'],'answer')
q('context.hanina','13a:14','Can אסיף mean harvest given the verse about gathering from threshing floor and winepress?')
claim('context.waste','13a:14','The threshing-floor and winepress passage speaks of their waste.',holder='previous authority cited by Hanina')
attr('context.hanina','13a:14','מתקיף לה רבי חנינא','speaker','Challenge to harvest interpretation',['Rabbi Hanina']);edge('context.hanina_objection',['13a:3','13a:14'],Q['context.hanina'],C['asif_harvest'],'objection');edge('context.waste_basis','13a:14',C['context.waste'],Q['context.hanina'],'support')
claim('context.zeira_concedes','13a:15','Zeira says Hanina has struck down the argument they had.',holder='Rabbi Zeira');attr('context.zeira','13a:15','א״ר זירא','speaker','Concession',['Rabbi Zeira']);edge('context.proof_retract',['13a:3','13a:15'],C['context.zeira_concedes'],C['asif_harvest'],'retraction')
q('context.replacement','13a:16','Then from where is the one-third threshold derived?')
claim('context.third_reading',['13a:16','13b:1'],'Yonatan ben Yosef reads לשלש as לשליש in the produce-for-three-years verse.',holder='Rabbi Yonatan ben Yosef');attr('context.yonatan','13a:16','רבי יונתן בן יוסף אומר','quoted_authority','Replacement one-third derivation',['Rabbi Yonatan ben Yosef']);edge('context.third_answer',['13a:16','13b:1'],C['context.third_reading'],Q['context.replacement'],'answer')
q('context.literal','13b:2','Is that verse not needed for its literal meaning?');claim('context.other_verse','13b:2','Another verse describes sowing in eighth year and eating old produce until ninth year.');edge('context.literal_answer','13b:2',C['context.other_verse'],Q['context.literal'],'answer')
rationales=roles
combined={r['id']:r for r in state['records'] if r['release_state']=='valid' and r['id']!=PRE+'vegetables'};combined.update({r['id']:r for r in p['records']})
for ref,why in zip(refs,rationales):
 sid=S[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in combined.values() if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  reason=why+'. Actual '+layer+' source pass; full continuation through13b2 constrains initial derivation. Prior12b1 outcomes reused without duplicate claims; original indices preserved.'
  if layer=='reconciliation':reason='Omission reread: '+reason+' Subsequent Hanina objection/Zeira concession and replacement proof retained; future context not counted.'
  elif not ids:reason+=' No additional supported record after pass; quoted authority scope inherited from adjacent explicit records.'
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
runner.immutable(OUT/'UNVALIDATED_INITIAL.json',runner.encoded(p))
for row in p['records']:
 if row['layer']=='attributions' and row['content']['role']=='reported_authority':row['content']['role']='quoted_authority'
runner.immutable(OUT/'VALIDATION_RECOVERY.json',runner.encoded({'initial_error':'reported_authority is not an allowed attribution role','change':'Use quoted_authority for alternate Yosi report, retaining alternate attribution uncertainty and no invented chain','initial_promoted':False}))
runner.immutable(OUT/'ROLE_FIXED_CANDIDATE.json',runner.encoded(p))
for row in p['records']:
 if row['id']==P+'context.hanina' and row['layer']=='attributions':row['id']+='.a'
runner.immutable(OUT/'VALIDATION_RECOVERY_2.json',runner.encoded({'error':'Duplicate context.hanina question/attribution ID','change':'Attribution receives .a suffix; no semantics changed','promoted':False}))
runner.validate_apply(state,p,segs,job);runner.immutable(OUT/'INITIAL_PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'SOURCE_RECONCILIATION.json',runner.encoded({'base_snapshot':BASE,'core_refs':refs,'source_indices':[S[x]['source_index'] for x in refs],'omission_rationales':dict(zip(refs,rationales)),'context_read':'Prior12a6–10; following13a8–13b2 and13b3 boundary','reused_records':'Eight prior12b1 tithe-direction/year outcomes and crossfolio picking_case reused, not duplicated.','context_semantics':'Omer proof challenge, Hanina objection, Zeira concession and replacement Yonatan derivation produced uncounted.','uncertainties':['Rav Asi is not Rav; alternate Yosi attribution not forced into single chain.','Thirteen-a growth argument retains swift-land reply for both alternatives; no forced proof of precision.','Measurement units not expanded beyond printed source.','Initial asif-harvest proof explicitly constrained by subsequent withdrawal.'],'next_source':'Rosh Hashanah13a:8','open_tail':P+'third','independent_reading_seen':False}))
print(json.dumps({'records':len(p['records']),'cores':len(refs),'proposal':runner.sha(runner.encoded(p))}))
