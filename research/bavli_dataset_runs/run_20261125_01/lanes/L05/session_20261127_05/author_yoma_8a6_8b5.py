"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='81508d3e6d6c18572df97ef759c1e45868080c86b9868a06f4bedf8ea15ba24b';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
assert I[135]['ref']=='Yoma 8a:6' and I[149]['ref']=='Yoma 8b:5'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2705.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('sprinkling','structure',range(135,150),dict(title='Sprinkling schedules: successive explanations, separation standards and calendar exceptions',primary=True,boundary='closed',legacy_ids=[]))
e('continue',135,'yom.s2704.public',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted'):c[k]=cl(k,ii,p,scope,cond,holder,mode);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('parallel',135,'Shall we identify these tannaim with the tannaim of the following sprinkling dispute?', ['Prior permitted/overridden communal-impurity dispute','Proposed identification tested and rejected'])
C('meirdays',135,'Both priests receive sprinkling on all seven days, from all the purification ashes that were there.','Rabbi Meir’s baraita; all seven qualified below by Sabbath and fourth-day exclusions',holder='רבי מאיר',cond=['High priest before Yom Kippur or priest burning red heifer'])
C('yosidays',135,'Both priests receive sprinkling only on the third and seventh days.','Rabbi Yosi’s baraita position',holder='רבי יוסי',cond=['High priest before Yom Kippur or priest burning red heifer'])
C('seganheifer',135,'The priest burning the red heifer receives sprinkling all seven days.','Rabbi Hanina Segan HaKohanim; later day exceptions apply',holder='רבי חנינא סגן הכהנים',cond=['Priest burning red heifer'])
C('seganyk',135,'The high priest before Yom Kippur receives sprinkling only on the third and seventh days.','Rabbi Hanina Segan HaKohanim',holder='רבי חנינא סגן הכהנים',cond=['High priest before Yom Kippur'])
Q('impurityexplain',136,'Do they not disagree whether communal impurity is overridden or permitted?', ['Proposed explanation of Meir versus Yosi sprinkling schedules'])
C('initialmeir',136,'The first explanation assigns overridden communal impurity to Rabbi Meir.','Provisional explanation subsequently rejected as basis of this dispute',holder='רבי מאיר',mode='rejected')
C('initialyosi',136,'The first explanation assigns permitted communal impurity to Rabbi Yosi.','Provisional assignment explicitly rejected next',holder='רבי יוסי',mode='rejected')
Q('anysprinkling',137,'If Rabbi Yosi holds communal impurity permitted, why require any sprinkling at all?', ['First proposed alignment','Rabbi Yosi still requires third and seventh days'])
C('alloverridden',137,'All these tannaim hold that communal impurity is overridden.','Corrected common ground, not earlier proposed alignment')
C('secondmeir',138,'The second explanation assigns to Rabbi Meir the principle that immersion at its proper time is a mitzvah.','Interim explanation of the schedule dispute; Meir’s principle remains but proposed contrast rejected',holder='רבי מאיר',mode='hypothetical')
C('secondyosi',138,'The second explanation assigns to Rabbi Yosi denial that immersion at its proper time is a mitzvah.','Interim assignment rejected by contrary baraita',holder='רבי יוסי',mode='rejected')
Q('yosidenial',139,'Does Rabbi Yosi really deny that immersion at its proper time is a mitzvah?', ['Second explanation','Contrary baraita about a divine name on the flesh'])
for key,act in [('wash','wash'),('anoint','anoint'),('filth','stand in a filthy place')]:
 C('name'+key,139,'A person may not '+act+'.','Opening rule of quoted baraita',holder='Anonymous baraita',cond=['Divine name written on his flesh'])
C('reed',139,'When a mitzvah immersion is occasioned, he wraps a reed around it and immerses.','First tanna’s prescribed protection',holder='תנא קמא — ברייתת שם על בשרו',cond=['Divine name written on flesh','Mitzvah immersion'])
C('yosidip',139,'He goes down and immerses in his usual way, provided he does not rub.','Rabbi Yosi’s alternative; no removal of no-rubbing condition',holder='רבי יוסי',cond=['Divine name written on flesh','Mitzvah immersion','Does not rub'])
C('tkprinciple',140,'The established explanation of that baraita assigns to its first tanna denial that immersion at its proper time is a mitzvah.','Quoted-baraita first tanna, not Rabbi Meir by name',holder='תנא קמא — ברייתת שם על בשרו')
C('yosiprinciple',140,'The established explanation assigns to Rabbi Yosi the principle that immersion at its proper time is a mitzvah.','Contradicts earlier proposed denial',holder='רבי יוסי')
C('alltimed',140,'All the tannaim of the sprinkling discussion accept immersion at its proper time as a mitzvah.','Revised common ground; does not erase first tanna of name-on-flesh baraita')
C('meiranalogy',141,'Sprinkling is compared to immersion.','Final explanation of Rabbi Meir’s scheduling position',holder='רבי מאיר')
C('yosinoanalogy',141,'Sprinkling is not compared to immersion.','Final explanation of Rabbi Yosi’s scheduling position',holder='רבי יוסי')
Q('seganif',142,'If Rabbi Hanina Segan HaKohanim compares sprinkling to immersion, why not require the same for the high priest on Yom Kippur?', ['His differing red-heifer and high-priest schedules','Hypothesis: comparison accepted'])
Q('seganifnot',142,'If he does not compare sprinkling to immersion, why require it for the priest burning the red heifer?', ['His differing schedules','Hypothesis: comparison rejected'])
C('segannoanalogy',143,'Rabbi Hanina Segan HaKohanim does not compare sprinkling to immersion.','Answer to dilemma',holder='רבי חנינא סגן הכהנים')
C('seganextra',143,'The additional requirement for the priest burning the red heifer is a mere extra standard.','מעלה בעלמא rather than comparison to immersion',holder='רבי חנינא סגן הכהנים',cond=['Priest burning red heifer'])
Q('baraitaholder',[144,145],'Whose view does the baraita limiting the difference between the two priests follow?', ['Baraita states only a separation-purpose and touching difference','Question and full content cross folio'])
C('ykholy',[144,145],'The high priest’s separation is for sanctity.','Only-difference baraita, not Rabbi Hanina’s additional schedule distinction',holder='Anonymous only-difference baraita',cond=['High priest before Yom Kippur'])
C('yktouch',[144,145],'His fellow priests may touch the high priest during separation.','Only-difference baraita',holder='Anonymous only-difference baraita',cond=['High priest before Yom Kippur'])
C('heiferpure',[144,145],'The red-heifer priest’s separation is for purity.','Only-difference baraita',holder='Anonymous only-difference baraita',cond=['Priest burning red heifer'])
C('heifernotouch',[144,145],'His fellow priests do not touch the priest burning the red heifer during separation.','Only-difference baraita',holder='Anonymous only-difference baraita',cond=['Priest burning red heifer'])
C('baraitameiryosi',145,'The baraita can follow either Rabbi Meir or Rabbi Yosi.','Alternative compatible holders, not unique named assignment',cond=['Their schedules do not distinguish between the two priests'])
C('notsegan',145,'It cannot follow Rabbi Hanina Segan HaKohanim, because on his view the sprinkling schedules also differ.','Rejection based on baraita’s only-difference assertion')
for day in [1,2,3]:
 C('day'+str(day),146,'Separation day '+str(day)+' may be the third day of impurity.','Rabbi Yosi son of Rabbi Hanina acknowledges these sprinklings',holder='רבי יוסי ברבי חנינא',cond=['Uncertainty about prior impurity timing'])
for day in [5,6,7]:
 C('day'+str(day),146,'Separation day '+str(day)+' may be the seventh day of impurity.','Rabbi Yosi son of Rabbi Hanina acknowledges these sprinklings',holder='רבי יוסי ברבי חנינא',cond=['Uncertainty about prior impurity timing'])
Q('fourth',[146,147],'Why is sprinkling required on the fourth day at all?', ['All-seven-days formulation','Fourth separation day cannot be a suspected third or seventh impurity day'])
C('fourthneither',147,'The fourth separation day is not a possible third or seventh impurity day.','Rabbi Yosi son of Rabbi Hanina’s objection; distinct from Rabbi Yosi the tanna',holder='רבי יוסי ברבי חנינא')
Q('sevenliteral',148,'On your reasoning, is sprinkling really performed on all seven days?', ['Literal all-seven-days wording','Known Sabbath exception'])
C('shevut',148,'Sprinkling is a shevut.','Established rule invoked against literal seven days')
C('noshabbat',148,'Sprinkling does not override Shabbat.','Established restriction',cond=['Shabbat'])
C('sevenexceptshabbat',148,'The all-seven-days wording must mean seven apart from Shabbat.','Necessary qualification of literal wording',cond=['Shabbat within separation days'])
C('sevenexceptfourth',148,'Likewise the wording means seven apart from the fourth day.','Answer to fourth-day objection',cond=['Fourth separation day'])
C('ykcalendar',149,'The high priest’s timing depends on the fixed calendar date, not our choice.','Rava’s distinction in scheduling',holder='רבא',cond=['Preparation for Yom Kippur'])
C('ykthird',149,'The high priest must be separated on the third of Tishrei.','Rava’s calendar consequence',holder='רבא',cond=['Preparation for Yom Kippur'])
C('ykweekday',149,'He is separated whenever the third of Tishrei falls.','Rava: day of week does not move this date',holder='רבא',cond=['Whatever weekday third of Tishrei falls'])
C('heiferchoice',149,'The timing for the priest burning the red heifer is in our control.','Rava’s contrast with fixed calendar service',holder='רבא',cond=['Red-heifer preparation'])
C('heiferwednesday',149,'The red-heifer priest is separated on Wednesday.','Rava’s chosen schedule',holder='רבא',cond=['Red-heifer preparation'])
C('fourthshabbat',149,'That schedule makes his fourth separation day fall on Shabbat.','Rava’s purpose in Wednesday start; combines two non-sprinkling exclusions',holder='רבא',cond=['Wednesday start'])
Q('sevenmeaning',148,'What must you then say the seven-day expression means?', ['Sprinkling cannot override Shabbat','Reply invokes a necessary exception before parallel fourth-day exception'])
rels=[(136,'impurityexplain','parallel','qualification'),(137,'anysprinkling','initialyosi','objection'),(137,'alloverridden','initialyosi','correction'),(137,'alloverridden','parallel','answer'),(139,'yosidenial','secondyosi','objection'),(140,'yosiprinciple','yosidenial','answer'),(140,'yosiprinciple','secondyosi','objection'),(140,'alltimed','secondyosi','correction'),(141,'meiranalogy','meirdays','support'),(141,'yosinoanalogy','yosidays','support'),(143,'segannoanalogy','seganif','answer'),(143,'seganextra','seganifnot','answer'),(143,'seganextra','seganheifer','support'),(145,'baraitameiryosi','baraitaholder','answer'),(145,'notsegan','baraitaholder','answer'),(147,'fourthneither','fourth','support'),(148,'noshabbat','sevenliteral','support'),(148,'sevenexceptshabbat','sevenmeaning','answer'),(148,'sevenexceptfourth','fourth','answer'),(148,'sevenexceptshabbat','meirdays','qualification'),(148,'sevenexceptshabbat','seganheifer','qualification'),(148,'sevenexceptfourth','meirdays','qualification'),(148,'sevenexceptfourth','seganheifer','qualification'),(149,'ykcalendar','ykthird','support'),(149,'ykcalendar','ykweekday','support'),(149,'heiferchoice','heiferwednesday','support'),(149,'fourthshabbat','heiferwednesday','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={135:'All three named schedule views retained; all-seven wording subject to8b3–5 exceptions. Earlier impurity-dispute analogy posed as question.',136:'First proposed Meir-overridden/Yosi-permitted explanation rejected; never exported as final holder view.',137:'Why any sprinkling question defeats permitted assignment; all tannaim overridden common ground.',138:'Second proposal timed-immersion mitzvah contrast retained as intermediate; Yosi denial rejected next.',139:'Explicit Yosi objection; three divine-name prohibitions, reed protection and usual immersion with no rubbing separately represented.',140:'Name-on-flesh first tanna remains distinct from Meir; Yosi timed-immersion view refutes prior denial; all sprinkling tannaim agree on timed immersion.',141:'Final dispute is comparison of sprinkling to immersion, not immersion mitzvah itself.',142:'Both horns of Hanina Segan dilemma separately recorded with opposite hypothetical conditions.',143:'No comparison plus red-heifer extra standard resolves both horns.',144:'Full baraita and holder question carried across folio; no truncated evidence.',145:'Purpose and touching differences kept separately; compatible either Meir or Yosi, Hanina excluded for additional schedule difference.',146:'Rabbi Yosi son of Rabbi Hanina is distinct from Rabbi Yosi the tanna; all six acknowledged day possibilities separately preserved, fourth-day objection continues.',147:'Fourth day neither possible third nor seventh; separately anchored explicit question includes prior speaker context.',148:'Literal seven-day and meaning questions, shevut, nonoverride Shabbat, fourth-day exception retained.',149:'Rava third-of-Tishrei fixed date independent of weekday versus chosen Wednesday for red heifer to align fourth day with Shabbat.8b6–7 read as next separate chamber-name topic, no new coverage.'}
for i in range(135,150):
 add('u'+str(i),'utterances',i,dict(textual_voice='Named views and anonymous argument separated below',discourse_role=notes[i],composition='composite'))
 if i not in [146,147,149]:add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara or quoted baraita framing',role='anonymous',candidates=[],scope='Connective argument and quotation framing; named views separately attributed',transmission_chain=[]))
COV=[]
for i in range(135,150):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails'])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_8a6_8b5_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=15,sha256=hashlib.sha256(b).hexdigest())))
