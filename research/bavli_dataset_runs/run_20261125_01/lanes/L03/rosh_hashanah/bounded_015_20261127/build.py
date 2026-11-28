"""Manual source-first RH015; no independent labels consulted."""
import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');BASE='5f5ecc0243bdef7ea4eeb29f9d58f4fbf7578e0658b35d4ef5312884749ece15'
job,segs=runner.load(J);state=runner.current(J);assert runner.sha(runner.encoded(state))==BASE;runner.authorize(J,'L03/rosh_hashanah',3)
S={s['ref'].removeprefix('Rosh Hashanah '):s for s in segs.values()};old={r['id']:r for r in state['records']};P='rh.e3.b015.';PRE='rh.e3.b014.'
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=[])
refs=['10b:'+str(i) for i in range(6,11)]+['11a:'+str(i) for i in range(1,16)]
def ev(ref):
 s=S[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def add(k,l,rr,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(rr,str):rr=[rr]
 r=dict(id=P+k,layer=l,evidence=[ev(x) for x in rr],content=c,links=list(links),uncertainty=list(unc),origin=origin);p['records'].append(r);return r['id']
C={};Q={}
def claim(k,rr,text,holder='anonymous Gemara',cond=(),mode='asserted',status='Local stated interpretation; no external factual or legal certification',unc=()):
 C[k]=add(k,'claims',rr,dict(proposition=text,conditions=list(cond),scope='Local day-count derivation and chronology discussion; source occurrences retained',assertion_mode=mode),unc=unc)
 add(k+'.p','positions',rr,dict(holder_candidates=[holder],claim_id=C[k],question_id=None,conditions=list(cond),local_status=status),links=[C[k]],unc=unc);return C[k]
def q(k,rr,text):Q[k]=add(k,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'));return Q[k]
def edge(k,rr,a,b,rel):return add(k,'edges',rr,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),links=[a,b])
def attr(k,rr,surface,role,scope,candidates=(),chain=(),unc=()):return add(k,'attributions',rr,dict(surface=surface,role=role,scope=scope,candidates=list(candidates),transmission_chain=list(chain)),unc=unc)
r=copy.deepcopy(old[PRE+'plant_days']);r['id']=P+'plant_days';r['supersedes']=PRE+'plant_days'
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['evidence'] += [ev(x) for x in refs[:4]];r['content']['boundary']='closed';r['content']['title']='Planting day count and completed shared-verse derivation';p['records'].append(r)
for c in state['coverage']:
 if PRE+'plant_days' in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[P+'plant_days' if x==PRE+'plant_days' else x for x in c['record_ids']];c['rationale']+=' Day-count continuation closed through10b9 by immutable successor.';p['coverage'].append(c)
add('chronology','structure',refs[4:],dict(title='Creation, patriarch and redemption chronology: paired baraita and subsequent proofs',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference');p['open_tails']=[P+'chronology']
roles=['Yohanan attributes common verse and Meir inference','Other view distinguishes syntax of numbered years','Abbreviated RA month-to-year counting derivation','Parenthetical inference that both assume Nisan creation','Eliezer chronology begins','Eliezer chronology continues across folio','Yehoshua parallel chronology occurrence','Eliezer creation proof and rain account','Yehoshua creation proof and mating season','Challenge to Eliezer from fruit-producing tree and reply','Challenge to Yehoshua from fruit tree; Yehoshua ben Levi account','Eliezer patriarch birth proof','Eitan lexical question with supporting verses and merit interpretations','Yehoshua patriarch birth proof','Challenge from eitan answered as strength in commandments','Challenge from ziv answered by tree radiance; Rav Yehudah blessing','Death months linked to birth months through completed righteous lives','Isaac Passover birth question and rejected seasonal calculations','Six-month objection, intercalation answer and impurity-days objection','Mar Zutra resolves with partial seven-month pregnancy']
voices=['Rabbi Yohanan reporting Meir and unnamed other','anonymous account of other interpreter','anonymous account of abbreviated RA','parenthetical editorial inference','Rabbi Eliezer quoted','Rabbi Eliezer continued','Rabbi Yehoshua quoted','Rabbi Eliezer quoted','Rabbi Yehoshua quoted','anonymous objection and reply for Eliezer','anonymous reply invoking Rabbi Yehoshua ben Levi','Rabbi Eliezer quoted','anonymous Gemara','Rabbi Yehoshua quoted','anonymous reply for Yehoshua','anonymous reply for Eliezer citing Rav Yehudah','anonymous Gemara','anonymous Gemara','anonymous objection; tanna reply; renewed objection','Mar Zutra']
for i,(ref,role,voice) in enumerate(zip(refs,roles,voices)):
 add('u'+str(i),'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
 if i in [1,2,3,9,10,12,14,15,16,17,18]:attr('frame'+str(i),ref,'anonymous framing','anonymous','Local editorial discourse: '+role)
claim('same_verse','10b:6','Rabbi Yohanan says both interpreters derive their positions from the same Genesis8:13 verse.',holder='Rabbi Yohanan')
attr('yohanan','10b:6','א״ר יוחנן','speaker','Shared verse for competing day-count derivations',['Rabbi Yohanan'])
claim('meir_wording','10b:6','Meir reads the verse as calling the newly begun year a year after only one day.',holder='Rabbi Meir as explained by Yohanan')
edge('meir_proof','10b:6',C['meir_wording'],PRE+'meir_day','support')
claim('other_counterfactual','10b:7','The other interpreter concedes that six hundred and one year wording would support Meir.',mode='hypothetical',cond=['Counterfactual word order: בשש מאות ואחת שנה'])
claim('year_sixhundred','10b:7','In the actual wording, שנה applies to six hundred.',holder='Other interpreter in Yohanan account')
claim('one_beginning','10b:7','The numeral one denotes the beginning of the next year.',holder='Other interpreter in Yohanan account')
edge('syntax_reply','10b:7',C['year_sixhundred'],C['meir_wording'],'objection');edge('one_reply','10b:7',C['one_beginning'],C['meir_wording'],'qualification')
q('ra_source','10b:8','What is the reason of abbreviated ר״א?')
claim('month_one','10b:8','A single day in a month counts as a month because the verse calls the first day a month.',holder='ר״א (printed abbreviation)')
claim('year_thirty','10b:8','Thirty days in a year count as a year, by extending the month-unit principle.',holder='ר״א (printed abbreviation)')
claim('count_units','10b:8','A month is reckoned by its units and a year by its units.',holder='Anonymous explanation of ר״א')
attr('ra','10b:8','ור״א','quoted_authority','Thirty-day year-count proof',['ר״א (printed)'],unc=['Earlier אלעזר/אליעזר printed discrepancy remains unresolved; later explicit creation-date Eliezer is not automatic resolution.'])
edge('month_year','10b:8',C['month_one'],C['year_thirty'],'support');edge('unit_year','10b:8',C['count_units'],C['year_thirty'],'support');edge('ra_answer','10b:8',C['year_thirty'],Q['ra_source'],'answer')
claim('both_nisan','10b:9','The parenthetical editorial inference is that both interpreters assume creation in Nisan.',cond=['Inference attached to the preceding day-count derivation'],unc=['Parenthetical source text retained; do not silently harmonize with subsequent explicit Rabbi Eliezer Tishrei creation statement.'])
# Separate all events and repeated occurrences in the paired baraita.
events=[('creation','the world was created'),('birth','the patriarchs were born'),('death','the patriarchs died'),('isaac','Isaac was born'),('sarah','Sarah was remembered'),('rachel','Rachel was remembered'),('hannah','Hannah was remembered'),('joseph','Joseph left prison'),('labor','the ancestors’ forced labor in Egypt ceased'),('past','Israel was redeemed'),('future','Israel will be redeemed')]
for prefix,holder,month in [('el','Rabbi Eliezer','Tishrei'),('ye','Rabbi Yehoshua','Nisan')]:
 for i,(key,event) in enumerate(events):
  ref=('10b:10' if i<8 else '11a:1') if prefix=='el' else '11a:2'
  when=month if i<3 or i==10 else ('Passover' if i==3 else ('Nisan' if i==9 else 'Rosh Hashanah'))
  claim(prefix+'_'+key,ref,'According to '+holder+', '+event+' in/on '+when+'.',holder=holder,status='Quoted baraita position; repeated common events are separate occurrences, not unique-topic counts')
 attr(prefix+'_authority',['10b:10','11a:1'] if prefix=='el' else '11a:2','רבי אליעזר אומר' if prefix=='el' else 'ר׳ יהושע אומר','quoted_authority','Chronology list attributed across entire quotation',[holder])
attr('el_proofs',['11a:3','11a:7'],'ר״א אומר','quoted_authority','Creation and patriarch-birth derivations within explicit Eliezer/Yehoshua sequence',['Rabbi Eliezer'])
attr('ye_proofs',['11a:4','11a:9'],'ר׳ יהושע אומר','quoted_authority','Creation and patriarch-birth derivations',['Rabbi Yehoshua'])
attr('tanna_leap','11a:14','תנא','anonymous','Unnamed tanna supplying intercalated-year answer')
# The explicit competing creations and birth months, not mere proximity, warrant alternatives.
for key in ['creation','birth','death','future']:edge('alternative_'+key,['10b:10','11a:1','11a:2'],C['el_'+key],C['ye_'+key],'distinction')
q('el_creation_q','11a:3','What establishes creation in Tishrei?')
claim('el_grass','11a:3','Eliezer identifies Tishrei as the month when earth brings forth grass.',holder='Rabbi Eliezer')
claim('el_fruit','11a:3','Eliezer identifies Tishrei as the month when trees are full of fruit.',holder='Rabbi Eliezer')
claim('el_verse','11a:3','Eliezer reads Genesis1:11 grass and fruit-tree wording as evidence for Tishrei creation.',holder='Rabbi Eliezer')
claim('rain_season','11a:3','That time was the rain season.',holder='Rabbi Eliezer quoted')
claim('rain_growth','11a:3','Rain descended and made growth sprout, linked to the mist-rising verse.',holder='Rabbi Eliezer quoted')
for k in ['el_grass','el_fruit']:edge(k+'_support','11a:3',C[k],C['el_verse'],'support')
edge('el_creation_answer','11a:3',C['el_verse'],Q['el_creation_q'],'answer');edge('el_creation_support',['10b:10','11a:3'],C['el_verse'],C['el_creation'],'support')
q('ye_creation_q','11a:4','What establishes creation in Nisan?')
claim('ye_grass','11a:4','Yehoshua identifies Nisan as the month when earth is full of grass.',holder='Rabbi Yehoshua')
claim('ye_fruit','11a:4','Yehoshua identifies Nisan as the month when trees begin producing fruit.',holder='Rabbi Yehoshua')
claim('ye_verse','11a:4','Yehoshua reads Genesis1:12 grass and fruit-producing tree wording as evidence for Nisan creation.',holder='Rabbi Yehoshua')
for key,animal in [('beast','domestic animals'),('wild','wild animals'),('bird','birds')]:claim('mating_'+key,'11a:4','That season is when '+animal+' mate.',holder='Rabbi Yehoshua quoted')
claim('flocks_verse','11a:4','The flocks-clothed verse is invoked for the mating-season account.',holder='Rabbi Yehoshua quoted')
for k in ['ye_grass','ye_fruit']:edge(k+'_support','11a:4',C[k],C['ye_verse'],'support')
edge('ye_creation_answer','11a:4',C['ye_verse'],Q['ye_creation_q'],'answer');edge('ye_creation_support',['11a:2','11a:4'],C['ye_verse'],C['ye_creation'],'support')
for k in ['beast','wild','bird']:edge('mating_proof_'+k,'11a:4',C['flocks_verse'],C['mating_'+k],'support')
q('fruit_producing_q','11a:5','How does the other view account for fruit-producing tree wording?')
claim('future_blessing','11a:5','That wording is a blessing for subsequent generations.',holder='Anonymous answer on Eliezer side')
edge('blessing_answer','11a:5',C['future_blessing'],Q['fruit_producing_q'],'answer')
q('full_fruit_q','11a:6','How does the other view account for fruit-tree wording?')
for k,term in [('stature','their full stature'),('consent','their own consent/awareness'),('form','their chosen form')]:claim('creation_'+k,'11a:6','All works of creation were created with '+term+'.',holder='Rabbi Yehoshua ben Levi',unc=['Paraphrase of '+{'stature':'(לקומתן)','consent':'לדעתן','form':'לצביונן'}[k]+'; precise conceptual interpretation not externally resolved.'])
claim('tzivyon_reading','11a:6','Yehoshua ben Levi reads צבאם as צביונם in the completion verse.',holder='Rabbi Yehoshua ben Levi')
attr('ybl','11a:6','דא״ר יהושע בן לוי','quoted_authority','Creation qualities invoked in answer for Yehoshua; not same person as Rabbi Yehoshua',['Rabbi Yehoshua ben Levi'])
for k in ['stature','consent','form']:edge('qualities_'+k,'11a:6',C['tzivyon_reading'],C['creation_'+k],'support');edge('quality_answer_'+k,'11a:6',C['creation_'+k],Q['full_fruit_q'],'answer')
q('el_birth_q','11a:7','What establishes patriarchs’ birth in Tishrei?')
claim('eitan_birth','11a:7','Eliezer interprets the month of eitanim as the birth-month of the mighty ones of the world.',holder='Rabbi Eliezer')
edge('eitan_birth_answer','11a:7',C['eitan_birth'],Q['el_birth_q'],'answer');edge('eitan_birth_support',['10b:10','11a:7'],C['eitan_birth'],C['el_birth'],'support')
q('eitan_meaning','11a:8','How does eitan signify strength?')
for k,text in [('dwelling','Eitan is linked with a strong dwelling in Numbers24:21.'),('foundations','The enduring foundations in Micah6:2 support the strength reading.'),('fathers_merit','Leaping over mountains is interpreted as acting through the merit of the patriarchs.'),('mothers_merit','Skipping over hills is interpreted as acting through the merit of the matriarchs.')]:claim(k,'11a:8',text)
for k in ['dwelling','foundations']:edge(k+'_lexical','11a:8',C[k],Q['eitan_meaning'],'answer')
q('ye_birth_q','11a:9','What establishes patriarchs’ birth in Nisan?')
claim('ziv_birth','11a:9','Yehoshua interprets the month of ziv as the birth-month of the radiant ones of the world.',holder='Rabbi Yehoshua',unc=['Retain source month-word derivation as stated; no external calendar harmonization added.'])
edge('ziv_answer','11a:9',C['ziv_birth'],Q['ye_birth_q'],'answer');edge('ziv_support',['11a:2','11a:9'],C['ziv_birth'],C['ye_birth'],'support')
q('eitan_counter','11a:10','How does the other view account for month of eitanim?')
claim('commandments','11a:10','That month is strong in commandments.',holder='Anonymous answer on Yehoshua side')
edge('commandments_answer','11a:10',C['commandments'],Q['eitan_counter'],'answer')
q('ziv_counter','11a:11','How does the other view account for month of ziv?')
claim('tree_radiance','11a:11','That expression refers to radiance of the trees.',holder='Anonymous answer on Eliezer side')
claim('blessing','11a:11','Rav Yehudah instructs the person who goes out in Nisan and sees blossoming trees to recite the quoted blessing praising creation of good creatures and trees for human benefit.',holder='Rav Yehudah',cond=['Goes out during Nisan','Sees blossoming trees'])
attr('rav_yehudah','11a:11','דאמר רב יהודה','quoted_authority','Blossoming-tree blessing, not Rav himself',['Rav Yehudah'])
edge('radiance_answer','11a:11',C['tree_radiance'],Q['ziv_counter'],'answer');edge('blessing_support','11a:11',C['blessing'],C['tree_radiance'],'support')
for k,month in [('nisan','Nisan'),('tishrei','Tishrei')]:claim('death_'+k,'11a:12','The view assigning patriarch birth to '+month+' also assigns death to '+month+'.',cond=['Birth assigned to '+month])
claim('moses_today','11a:12','Moses’ superfluous today wording is read as completion of his days and years on that day.')
claim('righteous_days','11a:12','God completes the years of the righteous from day to day.')
claim('righteous_months','11a:12','God completes the years of the righteous from month to month.')
claim('days_verse','11a:12','The promise to fill the number of days is cited for this completion principle.')
for k in ['righteous_days','righteous_months']:
 edge('moses_'+k,'11a:12',C['moses_today'],C[k],'support');edge('verse_'+k,'11a:12',C['days_verse'],C[k],'support')
 for m in ['nisan','tishrei']:edge(k+'_'+m,'11a:12',C[k],C['death_'+m],'support')
q('isaac_date','11a:13','What establishes Isaac’s birth at Passover?')
claim('appointed','11a:13','The promise to return at the appointed time is the textual basis of the calculation.')
claim('passover_shavuot','11a:13','A proposal places the announcement at Passover and the promised return at Shavuot.',mode='rejected',status='Rejected by fifty-day birth objection')
q('fifty_days','11a:13','Could she give birth in fifty days?')
claim('shavuot_tishrei','11a:13','A second proposal places the announcement at Shavuot and the return in Tishrei.',mode='rejected',status='Rejected by five-month birth objection')
q('five_months','11a:13','Could she give birth in five months?')
claim('festival_nisan','11a:13','The retained calculation places the announcement at the festival and the return in Nisan.',cond=['Subsequent intercalation and partial seven-month birth resolution'])
edge('fifty_objection','11a:13',Q['fifty_days'],C['passover_shavuot'],'objection');edge('five_objection','11a:13',Q['five_months'],C['shavuot_tishrei'],'objection');edge('date_answer','11a:13',C['festival_nisan'],Q['isaac_date'],'answer')
q('six_months','11a:14','Even so, could she give birth in six months?')
claim('leap_year','11a:14','The tanna answers that the year was intercalated.',holder='Unnamed tanna')
q('impurity_days','11a:14','After deducting her impurity days, is the period not still too short?')
edge('six_objection','11a:14',Q['six_months'],C['festival_nisan'],'objection');edge('leap_answer','11a:14',C['leap_year'],Q['six_months'],'answer');edge('days_objection','11a:14',Q['impurity_days'],C['leap_year'],'objection')
claim('nine_month_premise','11a:15','Mar Zutra takes even the view that a nine-month birth cannot occur in a partial ninth month as the comparison premise.',holder='Mar Zutra',mode='hypothetical',cond=['Even according to that nine-month view'])
claim('seven_partial','11a:15','A seven-month birth can occur in a partial seventh month even on that premise.',holder='Mar Zutra',cond=['Seven-month pregnancy','Even according to view requiring complete nine months for nine-month birth'])
claim('seasons_two','11a:15','The minimum plural of seasons in the cited verse is two.',holder='Mar Zutra')
claim('days_two','11a:15','The minimum plural of days in the cited verse is two.',holder='Mar Zutra')
attr('mar_zutra','11a:15','אמר מר זוטרא','speaker','Partial seven-month birth resolution',['Mar Zutra'])
for k in ['seasons_two','days_two']:edge(k+'_proof','11a:15',C[k],C['seven_partial'],'support')
edge('partial_answer',['11a:14','11a:15'],C['seven_partial'],Q['impurity_days'],'answer');edge('leap_scope',['11a:13','11a:14'],C['leap_year'],C['festival_nisan'],'qualification');edge('partial_scope',['11a:13','11a:15'],C['seven_partial'],C['festival_nisan'],'qualification')
# All eight source passes, with segment-specific omission rationale and no context coverage expansion.
rationales=['Shared verse attribution, Meir inference and old day-count claim link.','Counterfactual wording distinct from actual six-hundred syntax and beginning-of-one explanation.','RA source question, single-day month, thirty-day year and counting units; printed identity remains unresolved.','Parenthetical both-Nisan inference preserved without harmonizing later explicit Tishrei attribution.','Eight atomic Eliezer events begin chronology; three remembered women separated.','Three Eliezer events complete cross-folio list.','Eleven separate Yehoshua events retain repeated common events and four explicit alternative date positions.','Two seasonal premises, verse derivation, rain season and growth account distinct.','Two seasonal premises, verse proof and three animal classes distinct; flocks evidence retained.','Other means Eliezer here; blessing for generations answers fruit-producing tree challenge.','Other means Yehoshua here; full stature, awareness and form separate; Yehoshua ben Levi distinct authority.','Eitan birth derivation linked to earlier Eliezer birth claim.','Lexical evidence and patriarch/matriarch merit readings separated.','Ziv derivation retained exactly; no unsupported calendar harmonization.','Strong in commandments answers challenge to Yehoshua.','Tree radiance and condition-bound Rav Yehudah blessing distinct; full blessing retained in exact evidence.','Both death-month conditionals, Moses today interpretation and day/month completion principles split.','Isaac source question, two rejected announcement hypotheses, two duration objections and retained festival/Nisan calculation.','Six-month objection, intercalated-year answer and renewed impurity deduction objection distinct.','Nine-month premise not generalized; seven-month partial-birth resolution, two plural minima and qualification links retained.']
combined={r['id']:r for r in state['records'] if r['release_state']=='valid' and r['id']!=PRE+'plant_days'};combined.update({r['id']:r for r in p['records']})
for ref,why in zip(refs,rationales):
 sid=S[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in combined.values() if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  reason=why+' Actual '+layer+' source pass; no independent acceptance or task qualification.'
  if layer=='reconciliation':reason='Omission reread: '+why+' Continuation read through12a5; subsequent chronology proofs remain unproduced.'
  elif not ids:reason+=' No further record supported after this pass; inherited quoted voice preserved in adjacent scoped records.'
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=reason))
runner.validate_apply(state,p,segs,job)
runner.immutable(OUT/'INITIAL_PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'SOURCE_RECONCILIATION.json',runner.encoded({'base_snapshot':BASE,'core_refs':refs,'source_indices':[S[x]['source_index'] for x in refs],'omission_rationales':dict(zip(refs,rationales)),'context_read':'10b3–5 and11a16–12a5;12a6 next topic boundary','reused_context':'No preexisting semantic context records for10b6–9; prior plant_days structure extended immutably; prior Meir day-count claim reused.','uncertainties':['Printed RA day-count identity unresolved across prior אלעזר/אליעזר discrepancy.','Parenthetical both-Nisan statement not silently harmonized with following explicit Eliezer.','Interpretations of creation qualities kept with original terms.','No external historical or biological truth claim implied by quoted argument.'],'next_source':'Rosh Hashanah11a:16','open_tail':P+'chronology','independent_reading_seen':False}))
print(json.dumps({'records':len(p['records']),'cores':len(refs),'proposal':runner.sha(runner.encoded(p))}))
