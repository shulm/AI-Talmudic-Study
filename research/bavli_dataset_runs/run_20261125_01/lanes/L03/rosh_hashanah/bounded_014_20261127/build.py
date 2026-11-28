"""Manual bounded source reading serialization; immutable context reuse."""
import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');BASE='bf41c8a7b65c5785322012cb486037a4714c38bc0898d8a0dbe9d583239f16a1'
job,segs=runner.load(J);state=runner.current(J);assert runner.sha(runner.encoded(state))==BASE;runner.authorize(J,'L03/rosh_hashanah',3)
S={s['ref'].removeprefix('Rosh Hashanah '):s for s in segs.values()};old={r['id']:r for r in state['records']};P='rh.e3.b014.';PRE='rh.e3.b013.'
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
refs=['9b:'+str(i) for i in range(6,14)]+['10a:'+str(i) for i in range(1,8)]+['10b:'+str(i) for i in range(1,6)]
def ev(ref):
 s=S[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(k,l,rr,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(rr,str):rr=[rr]
 r=dict(id=P+k,layer=l,evidence=[ev(x) for x in rr],content=c,links=list(links),uncertainty=list(unc),origin=origin);p['records'].append(r);return r['id']
C={};Q={}
def claim(k,rr,text,holder='anonymous Gemara',cond=(),mode='asserted',status='Local source assertion, no external legal qualification',unc=()):
 C[k]=add(k,'claims',rr,dict(proposition=text,conditions=list(cond),scope='Jubilee derivation, planting year count and absorption; precise local argument stage',assertion_mode=mode),unc=unc)
 add(k+'.p','positions',rr,dict(holder_candidates=[holder],claim_id=C[k],question_id=None,conditions=list(cond),local_status=status),links=[C[k]],unc=unc);return C[k]
def q(k,rr,text):Q[k]=add(k,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'));return Q[k]
def edge(k,rr,a,b,rel):return add(k,'edges',rr,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),links=[a,b])
def attr(k,rr,surface,role,scope,candidates=(),chain=(),unc=()):return add(k,'attributions',rr,dict(surface=surface,role=role,scope=scope,candidates=list(candidates),transmission_chain=list(chain)),unc=unc)
# Extend existing primary tail, keeping every previous evidence segment and updating its coverage.
r=copy.deepcopy(old[PRE+'s4']);r['id']=P+'jubilee';r['supersedes']=PRE+'s4'
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['evidence'] += [ev(x) for x in refs[:5]];r['content']['boundary']='closed';r['content']['title']='Jubilee indispensable acts, interpretation scope, freedom and territorial dependence';p['records'].append(r)
for c in state['coverage']:
 if PRE+'s4' in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[P+'jubilee' if x==PRE+'s4' else x for x in c['record_ids']];c['rationale']+=' Primary continuation completed through9b10, immutable successor.';p['coverage'].append(c)
for key,rr,title,bound in [('plant_year_s',refs[5:7],'Planting Tishrei year analogy and rejected Nisan alternative','closed'),('plant_days',refs[7:],'Planting thirty-day rule, fruit boundary and Meir/printed Elazar day-count analysis; proof continuation follows','open_right')]:
 add(key,'structure',rr,dict(title=title,primary=True,boundary=bound,legacy_ids=[]),origin='editorial_inference')
p['open_tails']=[P+'plant_days']
roles=['Second reason needed because slave-absence feasibility can be challenged','Rabbi Yehudah source and interpretation scope','Freedom meaning and Rabbi Yehudah lexical explanation','Hiyya bar Abba reports Yohanan: sages require all three','Territorial inclusion and dependence on land observance','Planting year source and Tishrei analogy','Nisan alternative and matching rule','Three planting acts: thirty days versus shorter interval','Fruit prohibition through Shevat15 by orlah/revai year','Source question with Yohanan and alternative Yannai report','Fourth-year orlah and fifth-year revai extensions','Proposed exclusion of Meir; bull age24months+one day','Printed Elazar24months+30days; Meir calf/cattle/bull ages','Attempted Meir end-year/start-year distinction','Rava a fortiori begins with niddah premises','Rava conclusion across folio: day counts initially too','Alternative printed RA problem; planting prohibition and absorption views','Nahman→Rabbah barAvuha combined intervals and33day objection','Return to Meir:30days refer to absorption','31day objection answered by shared30thday']
voices=['anonymous Gemara','anonymous Gemara explaining Rabbi Yehudah','anonymous baraita and Rabbi Yehudah','Rabbi Hiyya bar Abba reporting Rabbi Yohanan','anonymous Gemara','anonymous Gemara','anonymous Gemara','anonymous baraita','same baraita','Rabbi Hiyya bar Abba reporting Rabbi Yohanan; alternative report in Rabbi Yannai name','derivation continued','anonymous Gemara quoting Rabbi Meir','printed Rabbi Elazar; Rabbi Meir quoted','anonymous proposed reconciliation','Rava','Rava continued','anonymous Gemara citing printed Rabbi Eliezer, abbreviated RY and Rabbi Yose/RSh','Rav Nahman reporting Rabbah bar Avuha; anonymous conclusion','anonymous final reconciliation','anonymous objection and answer']
for i,(ref,role,voice) in enumerate(zip(refs,roles,voices)):
 add('u'+str(i),'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
 # Named reports receive narrower explicit attribution below. Other frames are not assigned to an individual.
 if i not in [3,9,14,15]:attr('frame'+str(i),ref,'anonymous framing','anonymous','Narrative/question frame only: '+role)
# Reuse prior context proposals exactly; only previously absent source questions/relations added.
q('yehuda_reason','9b:7','What is Rabbi Yehudah’s reason, given Rabbi Yose’s stated reason?')
edge('yehuda_answer','9b:7',PRE+'yehuda_derivation',Q['yehuda_reason'],'answer')
edge('court_reply','9b:6',PRE+'court_responsibility',PRE+'slave_exists_hyp','answer')
claim('dror_freedom','9b:8','All agree that דרור denotes freedom.',holder='anonymous Gemara citing baraita')
q('dror_meaning','9b:8','How does דרור convey freedom?')
claim('dwelling','9b:8','Rabbi Yehudah explains the expression through a person dwelling where he wishes.',holder='Rabbi Yehudah',unc=['Lexical paraphrase of כמדייר בי דיירא; not independent property right.'])
claim('trading','9b:8','Rabbi Yehudah explains freedom through transporting merchandise in every province.',holder='Rabbi Yehudah')
attr('yehuda_lexical','9b:8','א״ר יהודה','quoted_authority','Lexical explanation of דרור',['Rabbi Yehudah'])
edge('dwelling_answer','9b:8',C['dwelling'],Q['dror_meaning'],'answer');edge('trading_answer','9b:8',C['trading'],Q['dror_meaning'],'answer')
q('yovel_inclusion','9b:10','What does the inclusion יובל supply for the sages?');q('land_restriction','9b:10','How is בארץ reconciled with outside-land application?')
claim('outside_inclusion','9b:10','The inclusive יובל extends Jubilee to outside the land.',cond=['Subsequent בארץ restriction requires operative freedom in the land'])
edge('outside_answer','9b:10',C['outside_inclusion'],Q['yovel_inclusion'],'answer')
edge('land_yes','9b:10',PRE+'outside_when_inside',Q['land_restriction'],'answer');edge('land_no','9b:10',PRE+'outside_not_without',Q['land_restriction'],'answer')
edge('outside_yes_scope','9b:10',PRE+'outside_when_inside',C['outside_inclusion'],'qualification');edge('outside_no_scope','9b:10',PRE+'outside_not_without',C['outside_inclusion'],'qualification')
q('plant_year','9b:11','What establishes Tishrei as the planting year boundary?')
claim('orlah_three','9b:11','The quoted planting verse assigns three years of orlah.',holder='Leviticus quoted')
claim('fourth_year','9b:11','The continuation speaks of the fourth year.',holder='Leviticus quoted')
claim('tishrei_analogy','9b:11','The year/year wording is derived from the Tishrei verse מראשית השנה.')
edge('plant_answer','9b:11',C['tishrei_analogy'],Q['plant_year'],'answer')
q('nisan','9b:12','Why not derive the planting year from the Nisan verse first of the months of the year?')
claim('match_year','9b:12','A year without months is compared to a year without months.')
claim('not_months','9b:12','A year without months is not compared to a year accompanied by months.')
edge('year_match','9b:12',C['match_year'],Q['nisan'],'answer');edge('months_excluded','9b:12',C['not_months'],Q['nisan'],'answer')
for op,label in [('plant','planting'),('layer','layering'),('graft','grafting')]:
 for k,text,cond in [('year_yes','counts as a year',['At least thirty days before New Year preceding the seventh year']),('retain','may be retained during the seventh year',['At least thirty days before New Year preceding the seventh year']),('year_no','does not count as a year',['Less than thirty days before that New Year']),('not_retain','may not be retained during the seventh year',['Less than thirty days before that New Year'])]:
  claim(op+'_'+k,'9b:13',label.capitalize()+' '+text+'.',holder='anonymous baraita',cond=cond,status='Baraita rule; final Meir reconciliation treats thirty as absorption with final day also year-count')
claim('orlah_until','10a:1','Fruit of this planting remains prohibited as orlah until Shevat15 where orlah applies.',holder='baraita',cond=['This planting whose short initial interval counted as a year','Orlah boundary'])
claim('revai_until','10a:1','Fruit of this planting remains under revai restriction until Shevat15 where revai applies.',holder='baraita',cond=['Same planting','Revai boundary'])
q('fruit_source','10a:2','What is the scriptural source for these extended fruit restrictions?')
claim('verse_years','10a:2','The cited fourth-year and fifth-year wording grounds the boundary extensions.',holder='Rabbi Yohanan through Rabbi Hiyya bar Abba; alternatively reported in Rabbi Yannai name')
attr('hiyya','10a:2','ר׳ חייא בר אבא א״ר יוחנן','transmitter','Fruit boundary derivation',['Rabbi Hiyya bar Abba'],['Rabbi Hiyya bar Abba','Rabbi Yohanan'])
attr('yohanan','10a:2','א״ר יוחנן','quoted_authority','Main report of fruit boundary source',['Rabbi Yohanan'],['Rabbi Hiyya bar Abba','Rabbi Yohanan'])
attr('yannai','10a:2','ומטו בה משמיה דר׳ ינאי','quoted_authority','Alternative report; not appended as certain link to main chain',['Rabbi Yannai'],unc=['Alternative transmission explicitly marked ומטו בה; immediate reporter unspecified.'])
claim('fourth_orlah','10a:3','Sometimes fruit in the fourth year is still prohibited as orlah.',holder='reported interpretation',cond=['Boundary case of this planting'])
claim('fifth_revai','10a:3','Sometimes fruit in the fifth year is still prohibited as revai.',holder='reported interpretation',cond=['Boundary case of this planting'])
edge('verse_answer','10a:2',C['verse_years'],Q['fruit_source'],'answer');edge('orlah_derive',['10a:2','10a:3'],C['verse_years'],C['fourth_orlah'],'support');edge('revai_derive',['10a:2','10a:3'],C['verse_years'],C['fifth_revai'],'support')
edge('orlah_scope',['10a:1','10a:3'],C['fourth_orlah'],C['orlah_until'],'qualification');edge('revai_scope',['10a:1','10a:3'],C['fifth_revai'],C['revai_until'],'qualification')
q('not_meir','10a:4','Does the thirty-day planting baraita disagree with Rabbi Meir, who counts one day as a year?')
claim('meir_day','10a:4','Rabbi Meir treats one day in a year as a year.',holder='Rabbi Meir quoted')
claim('meir_bull','10a:4','An unspecified Torah פר is twenty-four months and one day according to Rabbi Meir.',holder='Rabbi Meir')
claim('elazar_bull','10a:5','Printed Rabbi Elazar gives twenty-four months and thirty days for that פר.',holder='ר׳ אלעזר (printed)',unc=['Source10a5 prints אלעזר;10b2 parenthesis prints אליעזר. Preserve discrepancy, do not silently conflate.'])
attr('meir','10a:4','דברי ר״מ','quoted_authority','Bull age and one-day year principle',['Rabbi Meir'])
attr('elazar','10a:5','ר׳ אלעזר אומר','quoted_authority','Bull age24months+30days',['ר׳ אלעזר (printed)'],unc=['Later printed אליעזר/abbreviated ר״א left unresolved.'])
for k,term,age in [('calf','עגל',1),('cattle','בן בקר',2),('bull','פר',3)]:claim('meir_'+k+'_year','10a:5','Rabbi Meir assigns an unspecified '+term+' to year '+str(age)+'.',holder='Rabbi Meir',cond=['Unspecified Torah usage'])
claim('end_day','10a:6','The attempted reconciliation limits Meir’s one-day counting to the end of a year.',mode='hypothetical',status='Attempted explanation challenged by Rava; final answer distinguishes absorption instead')
claim('start_not_day','10a:6','The attempted reconciliation denies one-day counting at the beginning of a year.',mode='rejected',status='Rava’s following a fortiori defeats this distinction')
edge('attempt_answer','10a:6',C['end_day'],Q['not_meir'],'answer')
claim('niddah_last','10a:7','For niddah, the beginning of the last day does not suffice at the end of her count.',holder='Rava',cond=['Premise of local a fortiori'])
claim('niddah_first','10a:7','The end of a day suffices at the beginning of her count.',holder='Rava',cond=['Niddah comparison premise'])
claim('year_end_premise','10a:7','One day counts at the end of a year in the comparison.',holder='Rava',cond=['Meir’s accepted end-year premise'])
q('rava_kv',['10a:7','10b:1'],'Does it not follow a fortiori that one day also counts at the beginning of the year?')
claim('year_start',['10a:7','10b:1'],'Rava infers that one day counts at the beginning of a year.',holder='Rava',cond=['A fortiori from niddah and accepted end-year premise'])
attr('rava',['10a:7','10b:1'],'אמר רבא','speaker','Crossfolio a fortiori objection',['Rava'])
for k in ['niddah_last','niddah_first','year_end_premise']:edge('kv_'+k,['10a:7','10b:1'],C[k],C['year_start'],'support')
edge('rava_refutes',['10a:6','10a:7','10b:1'],C['year_start'],C['start_not_day'],'correction')
q('ra_sixty','10b:2','If the planting baraita is assigned to abbreviated ר״א, would it not require thirty plus thirty days?')
claim('ra_sixty_hyp','10b:2','The alternative assignment to ר״א would require thirty days for absorption and thirty for year-count.',mode='hypothetical',cond=['Attempted alternative to Meir'],unc=['Abbreviation not forcibly resolved across אלעזר/אליעזר spellings.'])
for op,label in [('plant','plant'),('layer','layer'),('graft','graft')]:
 claim('mishnah_no_'+op,'10b:2','One may not '+label+' less than thirty days before New Year preceding the seventh year.',holder='ר׳ אליעזר (parenthetical printed attribution)',cond=['Less than thirty days before New Year preceding seventh year'])
 claim('mishnah_uproot_'+op,'10b:2','If one did '+label+' in that prohibited interval, it must be uprooted.',holder='ר׳ אליעזר (parenthetical printed attribution)',cond=['Act performed within the prohibited interval'])
claim('three_absorb','10b:2','A graft which has not taken root within three days will not subsequently take root.',holder='ר״י, identified by following רבי יהודה',cond=['Grafting absorption'])
claim('two_weeks','10b:2','Rabbi Yose and abbreviated RSh give two weeks for absorption.',holder='Rabbi Yose and ר״ש (printed)',cond=['Alternative absorption interval'],unc=['Printed ר״ש retained without expanded identity witness.'])
attr('eliezer','10b:2','(דברי ר׳ אליעזר)','quoted_authority','Parenthetical attribution of thirty-day planting rule',['ר׳ אליעזר (printed)'],unc=['Distinct printed surface from אלעזר10a5; no automatic entity resolution.'])
attr('yehuda','10b:2','ר״י אומר','quoted_authority','Three-day absorption view; following10b3 explicitly רבי יהודה',['Rabbi Yehudah'])
attr('yose_rsh','10b:2','רבי יוסי ור״ש אומרים','collective','Two-week absorption view',['Rabbi Yose','ר״ש (printed)'])
for k,days,label in [('thirty',30,'thirty days'),('three',3,'three days'),('weeks',14,'two weeks')]:claim('total_'+k,'10b:3','For the view requiring '+label+' absorption, one needs that interval plus thirty days.',holder='Rabbah bar Avuha reported by Rav Nahman',cond=['Absorption view: '+label,'Separate thirty-day year-count requirement'])
attr('nahman','10b:3','רב נחמן אמר רבה בר אבוה','transmitter','Combined absorption and year-count intervals',['Rav Nahman'],['Rav Nahman','Rabbah bar Avuha'])
attr('rabbah','10b:3','רבה בר אבוה','quoted_authority','Combined intervals, not Rabbah without patronymic',['Rabbah bar Avuha'],['Rav Nahman','Rabbah bar Avuha'])
claim('thirtythree_problem','10b:3','Even adopting Rabbi Yehudah’s absorption interval would require three plus thirty days in this alternative assignment.',cond=['Attempted non-Meir year-count view'])
edge('sixty_support',['10b:2','10b:3'],C['total_thirty'],C['ra_sixty_hyp'],'support')
edge('thirtythree_objection',['9b:13','10b:3'],C['thirtythree_problem'],C['plant_year_yes'],'objection')
claim('meir_final','10b:4','The baraita is ultimately reconciled with Rabbi Meir.',status='Final assignment after rejected start/end distinction and alternative assignment')
claim('thirty_absorption','10b:4','Its thirty days refer to taking root.',cond=['Final Rabbi Meir reconciliation'])
edge('final_answer',['10a:4','10b:4'],C['meir_final'],Q['not_meir'],'answer')
edge('absorption_scope',['9b:13','10b:4'],C['thirty_absorption'],C['plant_year_yes'],'qualification')
q('thirtyone','10b:5','On that account, should thirty-one days not be required?')
claim('shared_day','10b:5','The thirtieth day counts both toward absorption and toward the year.',cond=['Final Meir reconciliation of the thirty-day planting baraita'])
edge('shared_answer','10b:5',C['shared_day'],Q['thirtyone'],'answer')
edge('shared_scope',['10b:4','10b:5'],C['shared_day'],C['thirty_absorption'],'qualification')
# The interpretation applies equally to all three explicit operations in the original baraita.
for op in ['layer','graft']:edge('absorption_'+op,['9b:13','10b:4'],C['thirty_absorption'],C[op+'_year_yes'],'qualification')
# Source omission checking and coverage include existing context records without duplicating them.
rationales=['Reuse q13, slave-existence hypothesis and court responsibility; add reply linkage.','Reuse Yehudah derivation/scope; explicit source question added.','Freedom lexical question, dwelling and commerce explanations distinct.','Reuse Yohanan transmission, all-three statement plus three atomic requirements and scope.','Two source questions, inclusive outside-land rule and both territorial conditions linked.','Planting verses and Tishrei year analogy separated.','Nisan alternative retained; two matching criteria separated.','All three operations each have count/no-count and retain/no-retain outcomes; later absorption reconciliation attached.','Orlah and revai restrictions separate; applies to this planting only.','Main Hiyya→Yohanan and alternative Yannai transmissions distinct.','Fourth-year orlah and fifth-year revai outcomes separated.','Meir one-day principle and24month+one-day bull age distinct; proposed incompatibility questioned.','Printed אלעזר retained; three Meir animal categories split.','Provisional end/start distinction retained with rejected start exclusion.','Niddah beginning/end premises distinct; Rava crossfolio argument preserved.','Crossfolio inference completes without shifting original index.','Printed אלעזר/אליעזר/ר״א discrepancy flagged; three prohibited operations and uprooting consequences split; absorption views separate.','Nahman→Rabbah barAvuha chain preserved; three combined intervals and33day objection separated.','Final Meir assignment distinct from30day absorption explanation.','31day question and shared30thday answer; following10b6–9 derivation read, not yet produced.']
combined={r['id']:r for r in state['records'] if r['release_state']=='valid' and r['id']!=PRE+'s4'};combined.update({r['id']:r for r in p['records']})
for ref,why in zip(refs,rationales):
 sid=S[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in combined.values() if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  reason=why+' Actual '+layer+' pass; no new independent acceptance or task qualification.'
  if layer=='reconciliation':reason='Omission reread: '+why+' Context through10b9 read;10b10 starts next creation-date discussion.'
  elif not ids:reason+=' No further record supported in this segment after pass; inherited named voice retained in adjacent scoped evidence.'
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
runner.validate_apply(state,p,segs,job)
runner.immutable(OUT/'INITIAL_PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'SOURCE_RECONCILIATION.json',runner.encoded({'base_snapshot':BASE,'core_refs':refs,'source_indices':[S[x]['source_index'] for x in refs],'omission_rationales':dict(zip(refs,rationales)),'context_read':'9b1–5 and10b6–10;10b6–9 continues exact day-count derivation','reused_context_ids':[r['id'] for r in state['records'] if r['release_state']=='valid' and any(e['segment_id'] in {S[x]['id'] for x in refs[:5]} for e in r['evidence'])],'uncertainties':['Printed אלעזר10a5 versus אליעזר10b2 and abbreviation ר״א not silently resolved.','ר״ש left surface-only.','Alternative Yannai report not merged into certain chain.'],'next_source':'Rosh Hashanah10b:6','open_tail':P+'plant_days','independent_reading_seen':False}))
print(json.dumps({'records':len(p['records']),'cores':len(refs),'proposal':runner.sha(runner.encoded(p))}))
