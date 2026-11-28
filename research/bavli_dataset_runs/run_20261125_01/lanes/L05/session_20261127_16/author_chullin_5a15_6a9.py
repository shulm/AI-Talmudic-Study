"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='09f9b6009d69765ce6add70718c9a863ce1093908b4d786cdeda88890bb83b0f';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[108]['ref']=='Chullin 5a:15' and I[127]['ref']=='Chullin 6a:9'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2716.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('offerings','structure',range(108,115),dict(title='Apostate offering exclusion: sin/burnt offering distinction and human/animal verse language',primary=True,boundary='closed',legacy_ids=[]))
s2=add('mnemonic','structure',115,dict(title='Mnemonic נקלף',primary=True,boundary='closed',legacy_ids=[]))
s3=add('decrees','structure',range(116,128),dict(title='Samaritan slaughter and wine decrees, reception history and domain-right consequence',primary=True,boundary='open_right',legacy_ids=[]))
e('priorcontinuation',[108], 'ch.s2711.refutation',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('source',[108,109],'Does this exclusion come from here? Does it not come from the other verse?', ['Prior מכם exclusion of apostate offerings','Alternate מעם הארץ exclusion cited next'])
C('exclude',109,'מעם הארץ excludes the apostate.','Quoted baraita alternative source for sin-offering exclusion',cond=['Apostate in sin-offering context'])
C('return',110,'One who would desist upon knowing brings an offering for his inadvertent act.','Rabbi Shimon criterion reported by Shimon ben Yosi',cond=['Would desist if aware','Inadvertent transgression'],holder='רבי שמעון')
C('notreturn',110,'One who would not desist upon knowing does not bring an offering for his inadvertent act.','Negative complementary criterion',cond=['Would not desist if aware','Inadvertent transgression'],holder='רבי שמעון')
C('verse',110,'אשר לא תעשינה בשגגה ואשם grounds the knowledge-responsive criterion.','Quoted verse supporting Rabbi Shimon alternative formulation',holder='רבי שמעון')
add('shimonreport','attributions',110,dict(surface='ר״ש בן יוסי אומר משום ר״ש',role='transmitter',candidates=['רבי שמעון בן יוסי'],scope='Reports Rabbi Shimon criterion, not independent identical position inferred from proximity',transmission_chain=['רבי שמעון בן יוסי','רבי שמעון']),[c['return'],c['notreturn']])
Q('difference',111,'What is the practical difference between them?', ['Apostate exclusion versus desisting-if-aware criterion'])
C('fatblood',111,'Their difference concerns an apostate regarding eating forbidden fat who brings an offering for blood.','Rav Hamnuna practical case; this sentence itself does not distribute outcomes to named sides',cond=['Apostate regarding fat','Offering concerns blood'],holder='רב המנונא')
C('twoofferings',112,'One source concerns a sin offering and one a burnt offering.','Answer to duplicated exclusion-source objection; source categories kept distinct')
C('sinrationale',112,'If only sin offering were taught, exclusion could be attributed to its atoning function.','Counterfactual explaining need for burnt-offering teaching',cond=['Only sin-offering exclusion taught'],mode='hypothetical')
C('burntgift',112,'One might then accept the burnt offering because it is a gift.','Rejected inference prevented by second teaching',cond=['Only sin-offering exclusion taught','Burnt offering is gift'],mode='hypothetical')
C('burntnonobligation',112,'If only burnt offering were taught, exclusion could be attributed to its nonobligatory character.','Reverse counterfactual',cond=['Only burnt-offering exclusion taught'],mode='hypothetical')
C('sinobligatory',112,'One might then accept the sin offering because it is obligatory.','Rejected inference prevented by sin-offering teaching',cond=['Only burnt-offering exclusion taught','Sin offering obligatory'],mode='hypothetical')
C('bothneeded',112,'Both exclusions are necessary.','צריכא resolves both counterfactuals')
Q('animalnegative',113,'Is every use of animal language derogatory?', ['Earlier מן הבהמה applied to sinners','Psalm36:7 says humans and animals are saved'])
C('cleverhumble',113,'Those are people who are discerning in knowledge but make themselves like an animal.','Rav reading of אדם ובהמה תושיע ה׳; favorable humility contrast with prior sinners',holder='רב')
add('ravreport','attributions',113,dict(surface='אמר רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope='Reports Rav explanation, not Rav Yehuda as independent author',transmission_chain=['רב יהודה','רב']),[c['cleverhumble']])
C('jointvsalone',113,'There it says human and animal together; here animal alone.','First answer distinguishing favorable Psalm language from prior offering verse')
Q('jointpositive',114,'Is every occurrence of human and animal together favorable?', ['Prior distinction','Jeremiah31:27 seed of human and seed of animal'])
C('separateseed',114,'There Scripture separates them: seed of human on its own and seed of animal on its own.','Reply preserves distinction despite apparent co-occurrence')
C('decree',116,'Rabban Gamliel and his court voted on Samaritan slaughter and prohibited it.','Reported decree; supervision-scope and reception distinguished in following discussion',holder='רבן גמליאל ובית דינו')
add('decreechain','attributions',116,dict(surface='א״ר חנן א״ר יעקב בר אידי א״ר יהושע בן לוי משום בר קפרא',role='transmitter',candidates=['רבי חנן'],scope='Chain reporting Rabban Gamliel and court decree',transmission_chain=['רבי חנן','רבי יעקב בר אידי','רבי יהושע בן לוי','בר קפרא']),[c['decree']])
Q('unsupervised',116,'Perhaps you heard the prohibition only when an Israelite is not standing over the slaughterer?', ['Rabbi Zeira addresses Rabbi Yaakov bar Idi','Scope of Samaritan slaughter decree'])
add('zeiraask','attributions',116,dict(surface='א״ל רבי זירא לרבי יעקב בר אידי',role='speaker',candidates=['רבי זירא'],scope='Question addressed to Rabbi Yaakov bar Idi',transmission_chain=[]),[z['unsupervised']])
C('notlearned',116,'The reply likens this scholar to people who have not learned the teaching.','Rabbi Yaakov bar Idi rebuke in reply to Zeira, not narrator endorsement of personal ignorance',holder='רבי יעקב בר אידי')
Q('needunsupervised',116,'Would an unsupervised case even need to be stated?', ['Reply to limiting decree to no Israelite supervision'])
C('supervisedscope',116,'The decree is not limited to slaughter without an Israelite standing over it.','Rhetorical reply establishes disputed extension even with supervision',cond=['Israelite standing over slaughterer'],holder='רבי יעקב בר אידי')
Q('accepted',117,'Did Rabbi Zeira accept that explanation from him or not?', ['Scope explanation from Rabbi Yaakov bar Idi','Not yet asking whether all authorities accepted the decree'])
C('yohananate',117,'Rabbi Asi says he saw Rabbi Yohanan eat from Samaritan slaughter.','Reported witnessed conduct, later reception issue not silently resolved here',holder='רבי אסי')
C('asiate',117,'Rabbi Asi also ate from Samaritan slaughter.','Narrative conduct; Rabbi Asi not Rav himself')
add('asireport','attributions',117,dict(surface='ר״נ בר יצחק א״ר אסי',role='transmitter',candidates=['רב נחמן בר יצחק'],scope='Reports Rabbi Asi first-person observation of Rabbi Yohanan',transmission_chain=['רב נחמן בר יצחק','רבי אסי']),[c['yohananate']])
Q('notheard',117,'Had they not heard, but would have accepted it if they had heard?', ['Rabbi Zeira puzzles over Yohanan and Asi eating','Decree applicability assumed in his dilemma'])
Q('heardrejected',117,'Or had they heard and not accepted it?', ['Alternative explanation of same eating conduct'])
C('heardrejectedanswer',118,'It is reasonable that they heard and did not accept it.','Rabbi Zeira resolves his own dilemma; separate from Zeira accepting scope explanation',holder='רבי זירא',mode='reconciled')
Q('howforbidden',118,'If they had not heard and would have accepted, how could they have come to eat forbidden food?', ['Hypothesis they lacked knowledge but would accept decree','Observed eating'])
C('animalsprotected',118,'The Holy One does not bring a mishap through the animals of the righteous.','Premise of Zeira argument about forbidden consumption, not independently universalized modern empirical guarantee',holder='רבי זירא')
C('righteousmore',118,'All the more so for the righteous themselves.','A fortiori inference supporting rejection of ignorance hypothesis',holder='רבי זירא')
Q('kalvachomer',118,'If their animals are protected, is it not all the more so the righteous themselves?', ['Righteous animals premise','Hypothetical forbidden consumption'])
Q('scopeacceptance',119,'If Zeira had not accepted the scope explanation, why not distinguish supervised from unsupervised slaughter?', ['Possibility he rejected Yaakov bar Idi explanation','Could explain Yohanan/Asi conduct by supervision'])
C('coulddistinguish',119,'He could have answered that one case has Israelite supervision and the other does not.','Counterfactual alternative unavailable once scope accepted',cond=['If scope explanation not accepted'],mode='hypothetical')
C('zeiraaccepted',119,'Thus Zeira accepted the explanation from him.','שמע מינה: accepts decree scope even with supervision; does not mean Yohanan/Asi accepted prohibition',holder=None,mode='reconciled')
Q('whydecree',120,'Why did the sages decree concerning them?', ['Samaritan slaughter prohibition'])
C('meirsent',120,'Rabbi Meir sent Rabbi Shimon ben Elazar to bring wine from the Samaritans.','Named sender/task/agent in wine episode')
C('elderwarning',120,'An elder told him: ושמת סכין בלועך אם בעל נפש אתה.','Warning to Shimon ben Elazar through Proverbs23:2; elder unnamed')
C('reportedmeir',120,'Shimon ben Elazar returned and reported these words to Rabbi Meir.','Report route of incident')
C('meirdecreed',120,'Rabbi Meir issued a decree concerning them.','Wine incident decree; later6a7 separates earlier enactment from acceptance',holder='רבי מאיר')
Q('whywine',121,'What was the reason?', ['Rabbi Meir decree following warning'])
C('dove',121,'They found an image of a dove at the top of Mount Gerizim which they worshiped.','Rav Nahman bar Yitzhak explanation; minority premise follows, do not infer every Samaritan worshiped it',holder='רב נחמן בר יצחק')
C('meirminority',121,'Rabbi Meir follows his view of taking account of a minority.','Explicit minority policy explanation',holder='רבי מאיר')
C('majoritydecree',121,'He decreed concerning the majority because of the minority.','Scope of decree not claim of universal actual worship',holder='רבי מאיר')
C('gamlielagreement',121,'Rabban Gamliel and his court also follow Rabbi Meir in this.','Connects slaughter decree with minority rationale',holder='רבן גמליאל ובית דינו')
Q('plainverse',122,'What is the plain context of the verse?', ['Elder applied Proverbs warning to wine','Distinguish original teaching context from narrative application'])
C('student',122,'It concerns a student sitting before his teacher.','Answer introducing Rabbi Hiyya teaching')
C('ifknows',[122,123],'If the student knows his teacher can return an explanation to him, he should seek understanding: בין.','Rabbi Hiyya exposition',cond=['Student knows teacher can explain'],holder='רבי חייא')
C('ifnot',[122,123],'If not, consider what is before you, put a knife at your throat if you have self-command, and separate from him.','Conditional alternative; exact verse retained, not literal instruction invented by annotator',cond=['Teacher not known able to explain'],holder='רבי חייא')
C('abahuagent',124,'Rabbi Abbahu sent Rabbi Yitzhak ben Yosef to bring wine from the Samaritans.','Separate later episode, not same envoy as Meir episode')
C('eldersays',124,'An elder told him there are no Torah observers here.','Unnamed elder assessment quoted, not unsupported identification with earlier elder')
C('yitzhakreport',124,'Rabbi Yitzhak reported the words to Rabbi Abbahu.','First stage of later reporting route')
C('abahureport',124,'Rabbi Abbahu reported them to Rabbi Ami and Rabbi Asi.','Second stage, both recipients retained')
C('completegentiles',124,'They did not leave until they made the Samaritans fully like gentiles.','Rabbi Ami and Rabbi Asi enactment; legal scope clarified6a7–10',holder='רבי אמי ורבי אסי')
Q('forwhat',125,'For what purpose was this enactment?', ['Prior statement treating them as complete gentiles'])
Q('alreadydecreed',125,'If for slaughter and libation wine, had the sages not already decreed those?', ['Proposed scope slaughter and wine','Earlier decrees'])
C('earliernotaccepted',125,'The earlier authorities decreed, but it was not accepted from them.','Explanation of enactment/reception chronology; not denial that prior decrees existed')
C('lateraccepted',125,'Rabbi Ami and Rabbi Asi then decreed and it was accepted from them.','Later reception distinguished from initial prohibition',holder='רבי אמי ורבי אסי')
Q('fullymeans',126,'What does fully like gentiles mean?', ['Novel legal force beyond the preceding decree/reception discussion'])
C('domainrights',126,'It concerns relinquishing domain rights and giving domain rights.','Rav Nahman bar Yitzhak identifies domain law; next baraita and6a10 clarify restriction/rental, not grant these powers to Samaritans',holder='רב נחמן בר יצחק')
C('shabbatrenounce',127,'An Israelite apostate who observes Shabbat publicly may relinquish domain rights.','Quoted baraita positive branch',cond=['Israelite apostate','Observes Shabbat in public'])
C('shabbatgive',127,'Such a publicly Shabbat-observant Israelite apostate may give domain rights.','Separate positive branch',cond=['Israelite apostate','Observes Shabbat in public'])
C('notshabbat',[127,128],'One who does not observe Shabbat publicly cannot relinquish or give domain rights by those procedures.','Negative branch read with6a10 requiring rental for gentile; raw אינו מבטל רשות ונותן רשות retained, no mistaken positive giving permission',cond=['Does not observe Shabbat in public'])
add('zeiradilemma','attributions',[117,118],dict(surface='ותהי בה רבי זירא ... הדר פשיט לנפשיה',role='speaker',candidates=['רבי זירא'],scope='Dilemma over Yohanan/Asi conduct and self-resolution; not speaker of anonymous acceptance-of-scope inquiry',transmission_chain=[]),[z['notheard'],z['heardrejected'],z['howforbidden'],z['kalvachomer'],c['heardrejectedanswer']])
add('yaakovreply','attributions',116,dict(surface='א״ל דמי האי מרבנן',role='speaker',candidates=['רבי יעקב בר אידי'],scope='Reply to Rabbi Zeira; rhetorical unsupervised-case question',transmission_chain=[]),[z['needunsupervised']])
add('hiyyateaching','attributions',[122,123],dict(surface='דתני רבי חייא',role='quoted_authority',candidates=['רבי חייא'],scope='Verse exposition continues over segment boundary',transmission_chain=[]),[c['student'],c['ifknows'],c['ifnot']])
# Keep envoy/report chains separate from original authorship of rulings.
add('meirepisode','attributions',120,dict(surface='הלך ר״ש בן אלעזר וספר דברים לפני ר״מ',role='transmitter',candidates=['רבי שמעון בן אלעזר'],scope='Relays unnamed elder warning to Rabbi Meir; not a chain making Meir author of warning',transmission_chain=[]),[c['elderwarning'],c['reportedmeir']])
add('laterreport','attributions',124,dict(surface='הלך רבי יצחק ... רבי אבהו ... רבי אמי ורבי אסי',role='transmitter',candidates=['רבי יצחק בן יוסף','רבי אבהו'],scope='Narrative report relay: Yitzhak tells Abbahu, who tells both Ami and Asi; no serial Ami-to-Asi oral chain',transmission_chain=[]),[c['yitzhakreport'],c['abahureport']])
rels=[([108,109],'exclude','source','support'),(110,'verse','return','support'),(110,'verse','notreturn','support'),(111,'fatblood','difference','answer'),(112,'twoofferings','source','answer'),(112,'sinrationale','burntgift','support'),(112,'burntnonobligation','sinobligatory','support'),(112,'burntgift','bothneeded','support'),(112,'sinobligatory','bothneeded','support'),(113,'cleverhumble','animalnegative','support'),(113,'jointvsalone','animalnegative','answer'),(114,'jointpositive','jointvsalone','objection'),(114,'separateseed','jointpositive','answer'),(116,'needunsupervised','unsupervised','objection'),(116,'supervisedscope','unsupervised','answer'),(116,'supervisedscope','decree','qualification'),(117,'yohananate','notheard','support'),(117,'asiate','heardrejected','support'),(118,'heardrejectedanswer','notheard','answer'),(118,'heardrejectedanswer','heardrejected','answer'),(118,'animalsprotected','righteousmore','support'),(118,'righteousmore','kalvachomer','answer'),(118,'righteousmore','howforbidden','support'),(118,'howforbidden','heardrejectedanswer','support'),(119,'coulddistinguish','scopeacceptance','support'),(119,'scopeacceptance','zeiraaccepted','support'),(119,'zeiraaccepted','accepted','answer'),(120,'elderwarning','meirdecreed','support'),(120,'meirdecreed','whydecree','answer'),(121,'dove','whywine','answer'),(121,'meirminority','majoritydecree','support'),(121,'majoritydecree','meirdecreed','support'),(121,'gamlielagreement','decree','support'),(122,'student','plainverse','answer'),(123,'ifknows','student','qualification'),(123,'ifnot','student','qualification'),(124,'eldersays','completegentiles','support'),(125,'alreadydecreed','forwhat','objection'),(125,'earliernotaccepted','alreadydecreed','answer'),(125,'lateraccepted','alreadydecreed','answer'),(125,'earliernotaccepted','decree','qualification'),(125,'lateraccepted','completegentiles','qualification'),(126,'domainrights','fullymeans','answer'),(126,'domainrights','completegentiles','qualification'),(127,'shabbatrenounce','domainrights','support'),(127,'shabbatgive','domainrights','support'),([127,128],'notshabbat','domainrights','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={108:'Exclusion-source challenge split from alternate verse5b1; prior מכם context read and structure linked without erasing inherited open tail.',109:'מעם הארץ exclusion completes prior source challenge; sin-offering setting clarified5b4.',110:'Shimon ben Yosi reports Shimon; aware-would-desist positive and negative conditions separate, verse support retained.',111:'Practical-difference question and Rav Hamnuna fat-apostate/blood-offering case; no unsupported named side allocation.',112:'Both sin/burnt offering sources needed; both counterfactual directions, atonement/gift and obligation/nonobligation reasons preserved as hypothetical, not final permissions.',113:'Animal-language generalization question; Rav via Rav Yehuda, discerning humility, human-plus-animal versus animal-alone reply.',114:'Human-plus-animal favorable-language challenge; separately stated seed categories answer, not simple word proximity.',115:'Parenthetical נקלף mnemonic retained as textual structure/utterance; no invented halakhic claim/question/holder.',116:'Four-link report of Gamliel/court decree, Zeira supervised-scope question, Yaakov reply and rhetorical need-to-state question; even-supervised scope distinguished from acceptance.',117:'Anonymous question whether Zeira accepted explanation differs from Zeira dilemma whether Yohanan/Asi heard/accepted decree. Rav Nahman bar Yitzhak reports Asi observation; Asi also ate.',118:'Zeira resolves own dilemma toward heard/not-accepted, conditioned contradiction and righteous-animal a fortiori argument; no general certification of immunity from all errors.',119:'Counterfactual supervised/unsupervised solution proves Zeira accepted scope explanation, not that Yohanan/Asi accepted decree. Explicit question and שמע מינה recorded.',120:'Why decree question; Meir sends Shimon ben Elazar for wine; unnamed elder verse warning, report back and decree separate.',121:'Reason question; dove idol atop Gerizim, minority policy, decree on majority because minority, Gamliel/court agreement; no universal actual worship allegation.',122:'Plain-context question distinguishes verse application from Rabbi Hiyya student/teacher exposition.',123:'Teacher able-to-explain condition and alternative withdrawal retained with full prior quotation evidence.',124:'Later Abbahu/Yitzhak episode separate; elder unnamed, relay through Abbahu to Ami and Asi; no invented linear Ami-Asi transmission.',125:'For-what and already-decreed questions; earlier decree not accepted versus later Ami/Asi decree accepted; enactment not erased by reception history.',126:'What complete-gentile-status means explicitly questioned; domain relinquishing/giving answer interpreted with next baraita, not permission to exercise those rights.',127:'Public Shabbat-observing apostate positive relinquish/give branches versus nonobservant negative branch.6a10 rental requirement and6a11 formula read fully, preventing false positive reading of ונותן.6a12–6b5 later demai argument also inspected as context only; next core is6a10.'}
for i in range(108,128):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous argument, quoted teachings and named reports distinguished',discourse_role=notes[i],composition='composite'))
 if i!=115:add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only; named reports and quoted authorities separately attributed',transmission_chain=[]))
COV=[]
for i in range(108,128):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_5a15_6a9_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
