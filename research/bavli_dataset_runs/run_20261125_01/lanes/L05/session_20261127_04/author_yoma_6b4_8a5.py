"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='a8f543fdd362915e59d5a82024392b70066950e32225901b5c594d58d0f17ccb';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
assert I[108]['ref']=='Yoma 6b:4' and I[134]['ref']=='Yoma 8a:5'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2704.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('public','structure',range(108,134+1),dict(title='Corpse impurity in communal service: variants, exceptions and forehead plate derivations',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted'):c[k]=cl(k,ii,p,scope,cond,holder,mode);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('corpse',108,'Instead of separating him from household impurity, why not separate him from corpse impurity?', ['High priest preparation before Yom Kippur'])
C('rava',108,'Corpse impurity is permitted in communal service.','Inference answering why corpse separation is not required',holder='רבא')
add('report','attributions',108,dict(surface='רב תחליפא אבוה דרב הונא (בר תחליפא) משמיה דרבא',role='transmitter',candidates=['רב תחליפא אבוה דרב הונא'],scope='Report of Rava’s inference; parenthetical source wording retained',transmission_chain=['רב תחליפא אבוה דרב הונא (בר תחליפא)','רבא']),[c['rava']])
C('ravina',109,'Even if corpse impurity is only overridden in communal service, the separation rule is intelligible.','Alternative defense, does not adopt permitted theory',holder='רבינא',mode='conditional',cond=['Assume corpse impurity overridden'])
C('rare',109,'Corpse impurity is uncommon.','Frequency reason for Ravina’s alternative',holder='רבינא')
C('home',109,'Household impurity is common.','Frequency reason for separating from wife',holder='רבינא')
C('nahman',110,'Corpse impurity is permitted in communal service.','Named dispute; does not encompass every kind of impurity',holder='רב נחמן')
C('sheshet',110,'Corpse impurity is overridden in communal service.','Named dispute; overridden differs from unrestricted permission',holder='רב ששת')
C('samepure',111,'In the first version all agree that pure priests perform the service.','First version only',cond=['Pure and impure priests available in same paternal house'])
C('sameimpure',111,'In the first version all agree impure priests do not perform the service.','First version only, qualified by alternate report',cond=['Pure and impure priests available in same paternal house'])
C('fetchscope',111,'The first version locates the dispute in seeking pure priests from another paternal house.','First version of dispute scope')
C('nofetch',112,'One need not seek pure priests from another paternal house.','Permitted position in first version',holder='רב נחמן',cond=['Would need another paternal house'])
C('fetch',112,'One must seek pure priests from another paternal house.','Overridden position in first version',holder='רב ששת',cond=['Would need another paternal house'])
C('alternate',[113,114],'In the alternative version impure priests may serve even when pure priests are present in the same paternal house.','איכא דאמרי; independent version, not harmonized with first',holder='רב נחמן',cond=['Corpse impurity','Communal service','Pure and impure in same paternal house'])
C('alternatereason',[113,114],'The Torah permitted all corpse impurity in communal service.','Rav Nahman’s rationale in alternative version; full folio continuation',holder='רב נחמן')
Q('source',115,'From where does Rav Sheshet derive his view?', ['Corpse impurity overridden in public'])
C('omerreplace',115,'If the omer meal offering becomes impure in the officiant’s hand, he says so and they bring another in its place.','Baraita used by Rav Sheshet',cond=['Another offering available'],holder='Anonymous baraita')
C('omersilent',115,'If only that omer offering is available, they tell him הוי פקח ושתוק.','No replacement case; preserves exact instruction',cond=['Offering impure in his hand','No other available'],holder='Anonymous baraita')
C('omerproof',116,'The instruction to announce impurity and bring another supports seeking a pure substitute.','Rav Sheshet proof against unrestricted public permission')
C('eating',116,'Rav Nahman concedes replacement where there are remainders for eating.','Exception to his public-permission position',cond=['שיריים לאכילה'],holder='רב נחמן')
C('animalsreplace',117,'If the meal offering of bulls, rams or lambs becomes impure in his hand, he says so and another is brought.','Second baraita objection',cond=['Replacement available'],holder='Anonymous baraita')
C('animalssilent',117,'If only that offering is available they tell him הוי פקח ושתוק.','Second baraita exception',cond=['No other available'],holder='Anonymous baraita')
Q('festival',118,'Does this not refer to the bulls, rams and lambs of the festival?', ['Baraita requiring pure substitute','Proposed communal fixed-time interpretation'])
C('festivalreading',118,'The objection proposes festival offerings as the baraita’s subject.','Provisional reading rejected by Rav Nahman’s answer',mode='rejected')
C('idolbull',119,'The bull is the communal idolatry bull; a pure substitute is sought because it has no fixed time.','Answer on behalf of Rav Nahman',cond=['Communal offering','No fixed time'],holder='רב נחמן')
C('aaronram',119,'The ram is Aaron’s ram; a pure substitute is sought because it is individual despite having a fixed time.','Answer on behalf of Rav Nahman',cond=['Individual offering','Fixed time'],holder='רב נחמן')
C('omerlamb',119,'The lamb accompanies the omer; a pure substitute is sought because there are remainders for eating.','Answer on behalf of Rav Nahman',cond=['Omer lamb','Remainders for eating'],holder='רב נחמן')
C('bloodacc',120,'Impure blood sprinkled inadvertently is accepted.','Quoted baraita, restricted to individual next',cond=['שוגג'],holder='Anonymous baraita')
C('blooddelib',120,'Impure blood sprinkled deliberately is not accepted.','Quoted baraita, restricted to individual next',cond=['מזיד'],holder='Anonymous baraita')
C('individual',120,'That baraita concerns an individual offering.','Answer to objection from blood',cond=['Blood acceptance baraita'])
Q('platewhat',121,'For what does the forehead plate obtain acceptance?', ['Quoted baraita about impure sacrificial components'])
for k,word in [('blood','blood'),('flesh','flesh'),('fat','fat')]:
 C('plate'+k,121,'The plate obtains acceptance for impure '+word+'.','Quoted baraita before Rav Nahman’s restrictions',cond=['Inadvertent or deliberate','Compulsion or willingness','Individual or communal'],holder='Anonymous baraita')
Q('plateneed',121,'If corpse impurity is permitted in communal service, why is acceptance through the plate needed?', ['Baraita includes communal offerings'])
C('plateindividual',122,'The clause that the plate obtains acceptance is interpreted as concerning individual offerings.','First answer on behalf of Rav Nahman',holder='רב נחמן')
C('platenonfixed',122,'Alternatively, the communal case concerns offerings without a fixed time.','ואיבעית אימא alternative answer, not cumulative with first',cond=['Communal','No fixed time'],holder='רב נחמן')
Q('sin',123,'Which sin of the holy things does Aaron bear?', ['ונשא אהרן את עון הקדשים'])
C('notpiggul',123,'The sin borne is not עון פיגול, because the text says לא ירצה.','Baraita’s exclusion; exact source labels retained',cond=['Proposed פיגול'],holder='Anonymous baraita')
C('notnotar',123,'The sin borne is not עון נותר, because the text says לא יחשב.','Baraita’s exclusion; no silent substitution of quotation',cond=['Proposed נותר'],holder='Anonymous baraita')
C('impuritysin',[123,124],'Only the sin of impurity is borne, impurity having been permitted in its communal case.','Cross-folio conclusion of baraita',holder='Anonymous baraita')
C('sheshetchallenge',124,'The baraita’s description of communal impurity as permitted challenges Rav Sheshet.','Explicit וקשיא לרב ששת')
C('tannaim',124,'The matter is a tannaitic dispute.','Answer to challenge against Rav Sheshet; not refutation of his view')
C('shimonon',124,'The plate obtains acceptance when on the forehead.','Rabbi Shimon, subject to intact-plate restriction below',holder='רבי שמעון',cond=['On forehead'])
C('shimonoff',124,'The plate obtains acceptance when not on the forehead.','Rabbi Shimon, subject to intact-plate restriction below',holder='רבי שמעון',cond=['Off forehead','Intact'])
C('yehudaon',125,'The plate obtains acceptance while on his forehead.','Rabbi Yehuda',holder='רבי יהודה',cond=['On forehead'])
C('yehudaoff',125,'The plate does not obtain acceptance when not on his forehead.','Rabbi Yehuda',holder='רבי יהודה',cond=['Off forehead'])
C('ykproof',125,'The high priest on Yom Kippur proves acceptance while the plate is not on his forehead.','Rabbi Shimon’s argument answered next',holder='רבי שמעון',cond=['Yom Kippur service without plate'])
C('ykanswer',126,'Set aside the high priest on Yom Kippur, because impurity is permitted for him in communal service.','Rabbi Yehuda answers proof; does not concede absent plate effective',holder='רבי יהודה',cond=['Communal Yom Kippur service'])
C('shimonoverridden',126,'It follows that Rabbi Shimon holds impurity is overridden in communal service.','Anonymous inference from Rabbi Shimon’s proof',holder='רבי שמעון')
C('broken',127,'All agree a broken plate does not obtain acceptance.','Abaye limits disagreement',holder='אביי',cond=['Plate broken'])
C('peg',127,'The disagreement concerns an intact plate hanging on a peg.','Abaye limits disagreement to absence while intact',holder='אביי',cond=['Plate hanging on peg'])
C('yehudaverse',127,'Rabbi Yehuda derives the forehead requirement from על מצח ונשא.','Source proof of on-forehead condition',holder='רבי יהודה')
C('shimonverse',128,'Rabbi Shimon reads תמיד לרצון לפני ה׳ as always obtaining acceptance.','Accepted interpretation, subject to fitness restriction',holder='רבי שמעון')
Q('always',128,'What does תמיד mean?', ['Rabbi Shimon’s cited verse'])
Q('alwaysforehead',128,'Can תמיד mean always on his forehead; is that possible?', ['Proposed literal uninterrupted wearing'])
Q('toilet',128,'Does he not need to enter the privy?', ['Proposed uninterrupted plate wearing'])
Q('sleep',128,'Does he not need to sleep?', ['Proposed uninterrupted plate wearing'])
C('impossiblewear',128,'Literal uninterrupted wearing is rejected because he needs the privy and sleep.','Rejection of proposed uninterrupted-wearing interpretation; reason for always-effective reading',mode='asserted',cond=['Proposed always on forehead interpretation'])
Q('yehudatamid',129,'For Rabbi Yehuda too, is not תמיד written?', ['Rabbi Yehuda requires plate on forehead'])
C('attention',[129,130],'תמיד requires that he not divert his attention from the plate.','Rabbi Yehuda’s answer; source proof crosses folio',holder='רבי יהודה')
C('touch',[129,130],'A person must touch his tefillin every hour.','Rabbah bar Rav Huna’s statement, derived a fortiori from plate',holder='רבה בר רב הונא')
C('onename',130,'The plate has one divine-name mention yet the Torah requires undiverted attention.','Premise of a fortiori argument')
C('manynames',130,'Tefillin contain many divine-name mentions, so the requirement applies all the more.','A fortiori conclusion supporting touching tefillin')
Q('shimonforehead',131,'For Rabbi Shimon, who says always effective, what of על מצחו ונשא?', ['Plate effective while absent'])
C('locationinitial',131,'The phrase initially is explained as fixing the plate’s location.','Initial response for Rabbi Shimon, refined by next exchange',holder='רבי שמעון')
Q('yehudalocation',132,'From where does Rabbi Yehuda derive its location?', ['He uses forehead-and-bearing for acceptance condition'])
C('locationfromal',132,'The location is derived from מעל מצחו.','Rabbi Yehuda’s derivation',holder='רבי יהודה')
Q('shimonlocation',132,'Could Rabbi Shimon also derive location from מעל מצחו?', ['Alternative derivation leaves על מצחו ונשא available'])
C('yeslocation',132,'Yes, Rabbi Shimon can derive location from מעל מצחו.','Explicit concession אין הכי נמי',holder='רבי שמעון')
Q('remaining',133,'Then what does he do with על מצחו ונשא?', ['Rabbi Shimon derives location elsewhere'])
C('fit',133,'A plate fit for the forehead obtains acceptance.','Rabbi Shimon’s revised explanation of verse',holder='רבי שמעון',cond=['Fit for forehead'])
C('unfit',133,'A plate unfit for the forehead does not obtain acceptance, excluding a broken plate.','Rabbi Shimon’s revised explanation',holder='רבי שמעון',cond=['Unfit for forehead, including broken'])
Q('yehudabroken',134,'From where does Rabbi Yehuda derive the broken-plate exclusion?', ['Different allocation of forehead verse'])
C('yehudabroken',134,'He derives the broken-plate exclusion from מצח / מצחו.','Rabbi Yehuda’s morphological derivation',holder='רבי יהודה')
C('shimonmorph',134,'Rabbi Shimon does not derive a distinction from מצח / מצחו.','Limit on Rabbi Shimon’s method, not denial of broken-plate exclusion',holder='רבי שמעון')
rels=[(108,'rava','corpse','answer'),(109,'ravina','corpse','answer'),(109,'rare','ravina','support'),(109,'home','ravina','support'),(112,'nahman','nofetch','support'),(112,'sheshet','fetch','support'),(114,'alternatereason','alternate','support'),(115,'omerreplace','source','answer'),(116,'omerreplace','omerproof','support'),(116,'omerproof','nahman','objection'),(116,'eating','nahman','qualification'),(117,'animalsreplace','nahman','objection'),(118,'festival','animalsreplace','qualification'),(119,'idolbull','festival','answer'),(119,'aaronram','festival','answer'),(119,'omerlamb','festival','answer'),(119,'idolbull','nahman','qualification'),(119,'aaronram','nahman','qualification'),(119,'omerlamb','eating','support'),(120,'blooddelib','nahman','objection'),(120,'individual','blooddelib','qualification'),(120,'individual','bloodacc','qualification'),(121,'plateblood','platewhat','answer'),(121,'plateflesh','platewhat','answer'),(121,'platefat','platewhat','answer'),(121,'plateneed','nahman','objection'),(122,'plateindividual','plateneed','answer'),(122,'platenonfixed','plateneed','answer'),(123,'notpiggul','sin','answer'),(123,'notnotar','sin','answer'),(124,'impuritysin','sin','answer'),(124,'impuritysin','sheshetchallenge','support'),(124,'sheshetchallenge','sheshet','objection'),(124,'tannaim','sheshetchallenge','answer'),(125,'ykproof','yehudaoff','objection'),(126,'ykanswer','ykproof','objection'),(126,'ykproof','shimonoverridden','support'),(126,'shimonoverridden','tannaim','support'),(127,'broken','shimonoff','qualification'),(127,'peg','shimonoff','qualification'),(127,'yehudaverse','yehudaon','support'),(128,'shimonverse','always','answer'),(128,'shimonverse','shimonoff','support'),(128,'toilet','alwaysforehead','objection'),(128,'sleep','alwaysforehead','objection'),(128,'impossiblewear','alwaysforehead','answer'),(129,'attention','yehudatamid','answer'),(130,'onename','manynames','analogy'),(130,'manynames','touch','support'),(131,'locationinitial','shimonforehead','answer'),(132,'locationfromal','yehudalocation','answer'),(132,'yeslocation','shimonlocation','answer'),(133,'fit','remaining','answer'),(133,'unfit','remaining','answer'),(133,'unfit','locationinitial','correction'),(134,'yehudabroken','yehudabroken','answer')]
# Last pair has identical labels in separate namespaces: use explicit question id.
for n,(ii,a,b,r) in enumerate(rels[:-1]):E(str(n),ii,a,b,r)
e('brokenanswer',134,c['yehudabroken'],z['yehudabroken'],'answer')
notes={108:'Separation challenge and Rava report; transmitter Rav Tahlifa distinguished from authority.',109:'Ravina allows overridden hypothesis and explicitly contrasts rare corpse with frequent household impurity.',110:'Named corpse-impurity dispute only; permitted versus overridden preserved.',111:'FIRST VERSION agreement for same paternal house; dispute only fetching another house.',112:'Rav Nahman no fetching and Rav Sheshet fetching separately attributed.',113:'ALTERNATIVE VERSION permits impure service even with pure same-house priests; full rationale continues7a1.',114:'Cross-folio rationale belongs to preceding alternative, not universal permission for all impurity.',115:'Rav Sheshet source question and both replacement/no-other omer cases retained.',116:'Replacement inference and edible-remainder concession differentiated.',117:'Second baraita retains all bull/ram/lamb categories and no-substitute instruction.',118:'Festival interpretation is explicit question, subsequently rejected, not accepted scope.',119:'Three separate responses preserve communal nonfixed bull, fixed individual ram and edible-remainder lamb.',120:'Inadvertent acceptance versus deliberate nonacceptance restricted to individual offering.',121:'Question what plate covers and challenge why needed; blood/flesh/fat atoms with all listed circumstances.',122:'Two distinct alternative answers: individual interpretation or public without fixed time.',123:'Which sin question; exact printed פיגול/לא ירצה and נותר/לא יחשב retained without silent correction.',124:'Cross-folio impurity conclusion challenges Rav Sheshet; tannaitic response and Rabbi Shimon views retained.',125:'Rabbi Yehuda on/off opposition; Rabbi Shimon Yom Kippur objection retained.',126:'Yom Kippur permitted reply and inference Rabbi Shimon overridden distinguished.',127:'Abaye broken unanimous exclusion versus intact hanging dispute; Yehuda proof.',128:'Meaning question and uninterrupted wearing, privy, sleep objections separately represented; always effective conclusion.',129:'Yehuda תמיד question, attention reply, Rabbah bar Rav Huna tefillin rule read across folio.',130:'One divine-name plate versus multiple-name tefillin a fortiori full continuation.',131:'Rabbi Shimon forehead-verse question and initially location response retained.',132:'Both location-source questions and yes concession; allocation revised next.',133:'Remaining-verse question and fit/unfit distinction including broken exclusion.',134:'Rabbi Yehuda broken-source question, morphological answer and Rabbi Shimon rejection of that derivation. Read8a6–14: proposed identification of later sprinkling dispute with this dispute is rejected; do not assign Rabbi Meir/Jose permitted/overridden from initial analogy.'}
for i in range(108,135):
 add('u'+str(i),'utterances',i,dict(textual_voice='Named reports and anonymous argument separately attributed in linked claims',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara framing and/or quotation',role='anonymous',candidates=[],scope='Anonymous connective argument only; does not replace named holders and transmitter records',transmission_chain=[]))
COV=[]
for i in range(108,135):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found for this layer.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s1])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_6b4_8a5_final_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=27,sha256=hashlib.sha256(b).hexdigest())))
