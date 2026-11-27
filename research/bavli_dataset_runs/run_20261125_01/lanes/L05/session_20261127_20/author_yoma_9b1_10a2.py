"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='2583050f7c4119f1e88b4aff81fb9dba363c3967edf0d99b9b04644f14c02b23';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
assert I[160]['ref']=='Yoma 9b:1' and I[179]['ref']=='Yoma 10a:2'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2720.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
prior=next(r for r in S['records'] if r['id']=='yom.s2715.shiloh');closed={k:json.loads(json.dumps(v)) for k,v in prior.items() if k not in ['review_state','release_state','ml_eligible','supersedes']};closed['id']='yom.s2715.shiloh.s20closed';closed['supersedes']=prior['id'];closed['content']['boundary']='closed';closed['content']['title']+='; split qualification and contempt evidence completed9b1–2';R.append(closed)
s2=add('temples','structure',range(162,179),dict(title='Temple destruction, generations and return: explanations, objections, reporting alternatives and corrections',primary=True,boundary='closed',legacy_ids=[]))
s3=add('nations','structure',179,dict(title='Japheth descendants, Tiras alternative identifications and Rav Yosef teaching; geography continues',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
# Exact split-sentence claims already exist with full evidence from prior wave; reuse rather than duplicate.
c['delay']='yom.s2715.delayed';c['asif']='yom.s2715.asif';c['contempt']='yom.s2715.shilohcontempt'
C('rawmeat',161,'Before the fat was burned, the priest’s servant demanded raw meat for roasting and refused cooked meat.','Quoted Samuel evidence for contempt of holy offerings; servant role not confused with sacrificer')
C('burnfirst',161,'The sacrificer replied to burn the fat first and then take what he desired.','Quoted response preserves order requirement')
C('force',161,'The servant demanded it immediately and threatened to take it by force.','Quoted coercive reply, conditional threat',cond=['If meat not given immediately'])
C('greatsin',161,'The young men’s sin was very great before the Lord because they despised the offering.','Scriptural evaluation cited as contempt evidence')
Q('firstwhy',162,'Why was the First Temple destroyed?', ['Contrast after Shiloh discussion'])
for k,v in [('idolatry','idolatry'),('sexual','sexual misconduct'),('blood','bloodshed')]:C('first_'+k,162,'One of the three stated causes was '+v+'.','First Temple destruction explanation')
C('shortbedverse',162,'כי קצר המצע מהשתרע is cited for idolatry.','Isaiah28:20 prooftext, interpreted next')
Q('shortbed',163,'What does כי קצר המצע מהשתרע mean?', ['Isaiah prooftext for idolatry'])
C('twocompanions',163,'This bed is too short for two companions to exercise rule together.','Rabbi Yonatan homiletic interpretation, not literal furniture measurement',holder='רבי יונתן')
C('yonatanwept',164,'When Rabbi Yonatan reached this verse, he wept.','Rabbi Shmuel bar Nahmani report of response')
Q('narrowcover',164,'For the One described as gathering sea waters as a heap, is a covering made narrow?', ['Rabbi Yonatan response to והמסכה צרה כהתכנס','Contrasting Psalm33:7 citation'])
# Source reference is Psalms33:7; preserve quote itself exactly through evidence.
add('yonatanreport','attributions',164,dict(surface='א״ר שמואל בר נחמני כי מטי רבי יונתן ... בכי אמר',role='transmitter',candidates=['רבי שמואל בר נחמני'],scope='Reports Yonatan weeping and rhetorical interpretation',transmission_chain=['רבי שמואל בר נחמני','רבי יונתן']),[c['yonatanwept'],z['narrowcover']])
C('tallshort',165,'They walked a tall woman beside a short one.','Interpretation of גבהו בנות ציון')
C('upright',165,'They walked with an erect posture.','Interpretation of נטויות גרון')
C('eyepaint',165,'They filled their eyes with kohl.','Interpretation of משקרות עינים')
C('heeltotoe',165,'They walked heel beside toe.','Interpretation of הלוך וטפוף')
C('perfumeshoes',165,'They placed myrrh and balsam in their shoes.','Rabbi Yitzhak interpretation of תעכסנה',holder='רבי יצחק')
C('kickperfume',165,'When they reached the young men of Israel they kicked and sprayed it toward them.','Conditional action in Rabbi Yitzhak account',cond=['Encounter young men of Israel'],holder='רבי יצחק')
C('arousedesire',165,'They induced desire in them like the venom of a viper.','Source simile in Rabbi Yitzhak account, not physiological assertion by producer',holder='רבי יצחק')
C('manassehblood',166,'Manasseh shed innocent blood until he filled Jerusalem from end to end.','Quoted Kings evidence for bloodshed, including source bracket הרבה מאד')
C('secondvirtues',167,'In the Second Temple period they engaged in Torah, commandments and acts of kindness.','Concession framing why-destruction question, not denied by following cause')
Q('secondwhy',167,'Why was the Second Temple destroyed despite Torah, commandments and kindness?', ['Those virtues present'])
C('baselesshatred',167,'It was because there was baseless hatred.','Stated cause')
C('equivalentthree',167,'This teaches that baseless hatred is equivalent to idolatry, sexual misconduct and bloodshed together.','Comparative moral lesson, not asserted identical statutory punishments')
C('wickedtrusted',168,'They were wicked but placed their trust in the Holy One.','Explicit אתאן למקדש ראשון returns statement to First Temple, not Second Temple virtue cohort')
C('leadersbribe',168,'Its leaders judged for bribes.','Micah3:11 quoted charge')
C('priestsprice',168,'Its priests taught for a price.','Separate quoted charge')
C('prophetsmoney',168,'Its prophets divined for money.','Separate quoted charge')
Q('godamong',168,'Is the Lord not among us?', ['Quoted words of those relying on God despite wrongdoing','Rhetorical reassurance, not narrator question about actual divine presence'])
C('noevilclaim',168,'They claimed that evil would not come upon them.','Quoted reassurance rejected by stated ensuing decrees, not accepted guarantee')
C('threedecrees',168,'Three decrees came upon them corresponding to their three transgressions.','Narrative theological explanation')
C('zionfield',168,'Zion would be plowed as a field.','First Micah3:12 decree')
C('jerusalemheaps',168,'Jerusalem would become heaps.','Second decree')
C('templeforest',168,'The mountain of the Temple would become forested heights.','Third decree')
Q('firstnohatred',169,'Was there no baseless hatred in the First Temple?', ['Earlier cause contrast','Ezekiel verse and interpretation of companions wounding by speech'])
C('tongueswords',169,'These are people who eat and drink with one another but stab one another with the swords of their tongues.','Interpretation attributed to source רבי (אליעזר); name variant preserved',holder='רבי (אליעזר)',unc=['Parenthesized name in source retained; no external normalization.'])
C('princesonly',170,'That case concerned the princes of Israel.','Answer restricts prior counterexample, not denial of its existence')
Q('everyone',170,'Could the cry and lament refer to everyone?', ['Quoted baraita interpreting Ezekiel21:17'])
C('princesverse',170,'The text specifies all the princes of Israel.','Baraita answer supports restricted scope')
C('firstsinknown',171,'The earlier generation’s sin was revealed.','Joint Yohanan and ר״א statement')
C('firstendknown',171,'Their end was revealed.','First generation correlated outcome')
C('latersinhidden',171,'The later generation’s sin was not revealed.','Negative contrast')
C('laterendhidden',171,'Their end was not revealed.','Unrevealed endpoint, not an invented date')
add('jointreport','attributions',171,dict(surface='ר׳ יוחנן ור״א דאמרי תרווייהו',role='position_holder',candidates=['רבי יוחנן','ר״א'],scope='Both state earlier/later sin-and-end contrast; abbreviated second name retained without forced expansion',transmission_chain=[]),[c['firstsinknown'],c['firstendknown'],c['latersinhidden'],c['laterendhidden']],unc=['ר״א left as abbreviated source identity.'])
C('yohananbetter',172,'The fingernail of the earlier generation is better than the belly of the later generation.','Rabbi Yohanan comparative metaphor',holder='רבי יוחנן')
C('lakishbetter',172,'On the contrary, the later generation is better.','Reish Lakish opposition',holder='ריש לקיש')
C('torahoppressed',172,'Even under the subjugation of kingdoms they engage in Torah.','Reish Lakish reason',cond=['Political subjugation'],holder='ריש לקיש')
C('templereturn',172,'The Temple proves it: it returned to the earlier generation but not to the later.','Rabbi Yohanan reply, not a new unreported date',holder='רבי יוחנן')
Q('whichgreater',173,'Were the earlier or later generations greater?', ['Question addressed to Rabbi Elazar'])
C('looktemple',173,'Set your eyes on the Temple.','Rabbi Elazar first reported answer',holder='רבי אלעזר')
C('templewitness',173,'An alternative report has: the Temple is your witness.','איכא דאמרי wording alternative, same respondent not invented second opinion',holder='רבי אלעזר')
C('jordanmeeting',174,'Reish Lakish was bathing in the Jordan; Rabbah bar bar Hanah came and offered him a hand.','Initial narrative participant pairing corrected9b17–18; retained as provisional report',mode='challenged')
C('hateyou',174,'He said: by God, I hate you.','Initial narrative rebuke addressed to returnee cohort; personal speaker pairing is corrected later, not producer endorsement')
C('wallreturn',174,'Had you made yourselves like a wall and all ascended in Ezra’s days, you would have been like silver that rot does not rule over.','Counterfactual all-at-once return in rebuke',cond=['All ascend together in Ezra days'],mode='hypothetical')
C('doorreturn',174,'Now that you ascended like doors, you are compared to cedar over which rot rules.','Actual-return contrast within quoted rebuke; reported rationale challenged by Yohanan later')
Q('cedar',175,'What is cedar here?', ['Cedar/rot comparison'])
C('sasmagor',175,'Ulla answers: ססמגור.','Term retained without speculative modern botanical identification',holder='עולא')
Q('sasmagorwhat',175,'What is ססמגור?', ['Ulla interpretation'])
C('batkol',175,'Rabbi Abba answers: a bat kol.','Interpretive link to diminished revelation, not replacement of exact word',holder='רבי אבא')
C('spiritdeparted',175,'After the last prophets Haggai, Zechariah and Malachi died, the holy spirit departed from Israel.','Quoted baraita',cond=['Death of named last prophets'])
C('stillbatkol',175,'They still used a bat kol.','Continuing lower form of communication despite departure, not complete absence of any revelation')
Q('lakishtalk',176,'Did Reish Lakish speak with Rabbah bar bar Hanah?', ['Initial narrative pairing','Contrary standard of his social speech'])
C('nottalkel',176,'He would not speak even with Rabbi (Eliezer), described as master of the Land of Israel.','Objection premise; parenthesized source name preserved',unc=['Source parenthetical רבי (אליעזר) retained.'])
C('trustbusiness',176,'Someone with whom Reish Lakish spoke in the market would be entrusted with business without witnesses.','Reported consequence of selective social speech',cond=['Reish Lakish spoke with person in marketplace'])
C('pairone',177,'Rav Pappa says one alternative was Reish Lakish with Zeiri.','Corrected participant pairing, not names assigned by narrative order',holder='רב פפא')
C('pairtwo',177,'The other alternative was Rabbah bar bar Hanah with ר״א.','Alternative corrected pairing; abbreviation retained',holder='רב פפא',unc=['Second name abbreviated ר״א in source; not forcibly normalized.'])
C('notreason',177,'Rabbi Yohanan said that this was not the reason.','Rejects explanation tying Second Temple absence of Shekhina to incomplete collective return; visitor not identified beyond source pronoun',holder='רבי יוחנן')
C('evenall',[177,178],'Even had they all ascended in Ezra’s days, the Shekhina would not have dwelled in the Second Temple.','Rabbi Yohanan counterfactual rebuttal, full Genesis continuation',cond=['All ascended in Ezra days'],holder='רבי יוחנן')
C('shemalone',[177,178],'Although God enlarges Japheth, the Shekhina dwells only in the tents of Shem.','Genesis9:27 interpretation underlying rebuttal; negation and exclusive scope retained',holder='רבי יוחנן')
Q('persiajapheth',179,'From where do we know Persians descend from Japheth?', ['Interpretation of Japheth versus Shem applied to Second Temple'])
for k,v in [('gomer','גומר — גרממיא'),('magog','מגוג — קנדיא'),('madai','מדי — מקדוניא'),('yavan','יון — כמשמעו'),('tuval','תובל — בית אונייקי'),('meshekh','משך — מוסיא')]:C(k,179,v,'Source geographical identification, Hebrew labels preserved without imposing modern geography')
C('tirasthrace',179,'One view identifies Tiras with בית תרייקי.','Unnamed side of dispute; no view assigned from name order')
C('tiraspersia',179,'The other view identifies Tiras with Persia.','Other unnamed side, not automatically assigned to sages')
add('tiraspair','attributions',179,dict(surface='פליגי בה ר׳ סימאי ורבנן ואמרי לה רבי סימון ורבנן חד אמר ... וחד אמר',role='position_holder',candidates=['רבי סימאי','רבנן','רבי סימון — alternative name report'],scope='Disputing parties with alternative named sage; each position-to-party pairing unresolved',transmission_chain=[]),[c['tirasthrace'],c['tiraspersia']],unc=['Do not assign חד אמר positions by named order.','Alternative Simai/Simon reports retained.'])
C('yosefpersia',179,'Rav Yosef teaches: Tiras is Persia.','Explicit separate teaching supports Persian lineage but does not identify which disputed side belonged to Simai/Simon',holder='רב יוסף')
for k in ['firstsinknown','firstendknown','latersinhidden','laterendhidden']:
 add(k+'.p','positions',171,dict(holder_candidates=['רבי יוחנן','ר״א'],claim_id=c[k],question_id=None,conditions=[],local_status='Joint assertion; second source name abbreviation retained'),[c[k]],unc=['ר״א not expanded beyond source.'])
# Attach positions to both unnamed Tiras alternatives without forced named alignment.
for k in ['tirasthrace','tiraspersia']:
 add(k+'.p','positions',179,dict(holder_candidates=[],claim_id=c[k],question_id=z['persiajapheth'],conditions=[],local_status='Unnamed alternative among reported disputants; assignment unresolved'),[c[k],z['persiajapheth']],unc=['No name-order inference.'])
rels=[(161,'rawmeat','contempt','support'),(161,'force','contempt','support'),(161,'greatsin','contempt','support'),(161,'burnfirst','rawmeat','objection'),(162,'first_idolatry','firstwhy','answer'),(162,'first_sexual','firstwhy','answer'),(162,'first_blood','firstwhy','answer'),(162,'shortbedverse','first_idolatry','support'),(163,'twocompanions','shortbed','answer'),(164,'narrowcover','first_idolatry','support'),(165,'tallshort','first_sexual','support'),(165,'upright','first_sexual','support'),(165,'eyepaint','first_sexual','support'),(165,'heeltotoe','first_sexual','support'),(165,'perfumeshoes','kickperfume','support'),(165,'arousedesire','first_sexual','support'),(166,'manassehblood','first_blood','support'),(167,'baselesshatred','secondwhy','answer'),(167,'baselesshatred','equivalentthree','support'),(168,'leadersbribe','wickedtrusted','support'),(168,'priestsprice','wickedtrusted','support'),(168,'prophetsmoney','wickedtrusted','support'),(168,'noevilclaim','wickedtrusted','support'),(168,'zionfield','threedecrees','support'),(168,'jerusalemheaps','threedecrees','support'),(168,'templeforest','threedecrees','support'),(169,'tongueswords','firstnohatred','support'),(170,'princesonly','firstnohatred','answer'),(170,'princesverse','everyone','answer'),(170,'princesverse','princesonly','support'),(172,'lakishbetter','yohananbetter','objection'),(172,'torahoppressed','lakishbetter','support'),(172,'templereturn','lakishbetter','objection'),(172,'templereturn','yohananbetter','support'),(173,'looktemple','whichgreater','answer'),(173,'templewitness','whichgreater','answer'),(175,'sasmagor','cedar','answer'),(175,'batkol','sasmagorwhat','answer'),(175,'stillbatkol','batkol','support'),(176,'lakishtalk','jordanmeeting','objection'),(176,'nottalkel','lakishtalk','support'),(176,'trustbusiness','lakishtalk','support'),(177,'pairone','jordanmeeting','correction'),(177,'pairtwo','jordanmeeting','correction'),(177,'notreason','doorreturn','objection'),([177,178],'evenall','wallreturn','objection'),([177,178],'shemalone','evenall','support'),(179,'yosefpersia','persiajapheth','answer'),(179,'yosefpersia','tiraspersia','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={160:'Fragment completes9a6 מתוך: delay of women bird offerings and Scripture-as-if intercourse; reuse prior full-evidence delayed/asif claims, not duplicate claim count. Shiloh primary structure already includes this segment and is explicitly closed successor.',161:'Contempt proof fullSamuel exchange: servant demands rawmeat before fat, sacrificer asks fatfirst, servant threatens force; evaluation greatsin and despisedoffering. Prior structure evidence already covers, no overlapping new primary.',162:'First Temple why-question and allthree causes separate; idolatry Isaiah proof retained.',163:'What-short-bed question; Yonatan two-companions ruling metaphor.',164:'Shmuel bar Nahmani reports Yonatan tears and rhetorical narrow-cover question, Psalm33:7 versus Isaiah text; no mistaken original attribution to reporter.',165:'All five Isaiah phrase interpretations and Yitzhak myrrh/balsam-in-shoes, encounter/kick/spray/desire details preserved; source simile not producer physiological claim.',166:'Manasseh innocent-blood verse supports third cause; bracketed text remains original.',167:'Second Temple virtues acknowledged; why destroyed question, baseless hatred answer and equivalence to three offenses retained, not legal-penalty identity.',168:'אתאן למקדש ראשון explicitly relocates wicked-yet-trusting statement; three paid-corrupt roles, quoted God-among-us reassurance question and noevilclaim, three specific decrees retained.',169:'NoFirstTemplehatred question, companions eating/drinking and tongue-sword harm; parenthesized Eliezer source name unnormalized.',170:'Princes-only answer, could-all question within baraita and princes verse support; does not erase existence of elite hostility.',171:'Joint Yohanan/ר״א contrast with four propositions: firstsin/end revealed, latersin/end unrevealed; second name abbreviation not forced.',172:'Yohanan firstbetter, ReishLakish laterbetter under oppression/Torah, Temple-return reply; views and argument direction distinct.',173:'Question to Elazar and two reported answerwordings eyes-on-Temple versus Temple-witness; alternative not lost.',174:'Initial ReishLakish/Rabbah meeting kept provisional; oath-rebuke, allwall/silver counterfactual versus doors/cedar actual comparison; actor correction and explanatory refutation later retained.',175:'Two definition questions and Ulla/Abba answers; Haggai/Zechariah/Malachi death, holyspirit departure yet batkol continued; no collapse to total revelation absence.',176:'Speech-with-Rabbah question, evenEliezer premise and market speech business-without-witnesses implication; identifies objection to original actor pairing.',177:'RavPappa alternative pairs ReishLakish/Zeiri OR Rabbah/ר״א explicitly correct initial; no assigned choice. Visitor to Yohanan unnamed; Yohanan rejects reason, evenall-return wouldnot suffice; Genesis continuation included.',178:'Full despiteJapheth-onlyShem qualification joins priorverse, negation/exclusive domain intact.',179:'PersianJapheth-lineage question; six geographic mappings in Hebrew no modern renaming. Tiras alternatives ביתתרייקי/Persia remain unnamed; Simai/Simon reported identityvariant distinct; RavYosef explicitly Persia supports one view without resolving disputed attribution.10a3–12 context read through later imperial-prediction arguments, no import into20core coverage.'}
for i in range(160,180):
 add('u'+str(i),'utterances',i,dict(textual_voice='Quoted verses, reports, discourse revisions and anonymous framing distinguished',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only; named reports and quoted claims separately attributed',transmission_chain=[]))
ALL=[r for r in S['records'] if r.get('release_state')=='valid' and r['id']!=prior['id']]+R
COV=[]
for i in range(160,180):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in ALL if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
for pc in S['coverage']:
 if prior['id'] in pc['record_ids']:
  cv={k:json.loads(json.dumps(v)) for k,v in pc.items() if k!='proposal_execution'};cv['record_ids']=[closed['id'] if v==prior['id'] else v for v in cv['record_ids']];cv['rationale']+=' Session20 completes Shiloh split sentence and contempt proof9b1–2; closed successor keeps exact original evidence.';COV.append(cv)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=[v for v in S['open_tails'] if v!=prior['id']]+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_9b1_10a2_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
