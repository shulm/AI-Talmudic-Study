"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='0dce64bf439c2436ea857615d451128d57ff8e4db069673d17bc4dc17b99c04f';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[72]['ref']=='Chullin 4a:19' and I[91]['ref']=='Chullin 4b:17'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2710.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('support','structure',range(72,82),dict(title='Reasons and proposed baraita support for Rava: appetite, inspection and alternative apostate categories',primary=True,boundary='closed',legacy_ids=[]))
s2=add('anan','structure',range(82,92),dict(title='Rav Anan reporting Shmuel and the Jehoshaphat/Ahab meal proof; objections continue',primary=True,boundary='open_right',legacy_ids=[]))
e('continue',72,'ch.s2709.mumar',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('reason',72,'What is the reason for Rava’s permission?', ['Appetite-driven carcass eater','Checked knife supplied'])
C('preferpermitted',72,'When permitted and prohibited options are available, he does not leave the permitted option and eat the prohibited one.','Reason for Rava’s appetite-motive rule, not every category of apostate',cond=['Appetite-driven carcass eater','Permitted option available'])
Q('unchecked',73,'If so, should permission apply even without checking the knife?', ['Reason that he prefers available permitted food'])
C('noeffort',73,'He does not trouble himself to make the effort.','Answer preserves need for supplied knife inspection; preference does not guarantee self-inspection',cond=['Effort needed to secure permitted slaughter'])
C('scholarssupport',[74,75],'The rabbis tell Rava that a baraita supports him.','Speakers are rabbis; Rava is addressee, not speaker of their proposed proof',holder='רבנן הפונים לרבא')
C('leavenallowed',[74,75],'The leaven of transgressors after Passover is permitted immediately.','Full cross-folio baraita quotation',holder='Anonymous leaven baraita',cond=['After Passover','Leaven of transgressors'])
C('exchange',[74,75],'The reason is that they exchange it.','Baraita’s stated behavior, distinguished below from merely presuming an exchange',holder='Anonymous leaven baraita')
C('yehudainitial',76,'The initial assumption identifies this baraita with Rabbi Yehuda.','סברוה; challenged as non-unique next',mode='challenged')
C('yehudatorah',76,'Post-Passover leaven is prohibited by Torah law.','Rabbi Yehuda’s quoted position',holder='רבי יהודה',cond=['Leaven after Passover'])
C('exchangeproof',76,'The exchange instruction indicates that they do not leave permitted food and eat prohibited food.','Initial inference supporting Rava from assumed Torah-prohibition case')
Q('whoyehuda',77,'How do we know it is Rabbi Yehuda—perhaps it is Rabbi Shimon?', ['Initial baraita identification'])
C('shimonrabbinic',77,'Post-Passover leaven is prohibited rabbinically.','Rabbi Shimon’s cited position',holder='רבי שמעון',cond=['Leaven after Passover'])
C('leniencyobjection',77,'Perhaps leniency applies for a rabbinic prohibition but not a Torah prohibition.','Suggested objection to transferring leaven evidence to slaughter; answered next',mode='challenged',cond=['Hypothesis: baraita follows Rabbi Shimon'])
Q('presumedexchange',78,'Even if it follows Rabbi Shimon, does it say “I presume they exchanged”?', ['Distinguishing presumption from definite behavior','Baraita says מפני שמחליפין'])
C('definiteexchange',78,'It says “because they exchange,” meaning they certainly exchange.','Answer establishes behavioral premise rather than merely lower evidentiary threshold')
Q('afortiori',78,'If they do not leave permitted food for prohibited food even in a rabbinic matter, is that not all the more true for a Torah prohibition?', ['Definite exchanging behavior','Rabbinic-to-Torah inference'])
C('afortioriproof',78,'Avoiding the rabbinic prohibition supports avoidance of a Torah prohibition all the more.','Defense of Rava’s support even on Rabbi Shimon identification')
Q('allslaughterproof',79,'Shall the baraita “all slaughter,” even a Kuti, uncircumcised person and Israelite apostate, support Rava?', ['Proposed further support'])
C('kutibaraita',79,'Even a Kuti is included in those who slaughter.','Quoted all-slaughter baraita; scope debated locally, not universal final Kuti ruling',holder='Anonymous all-slaughter baraita')
C('uncircbaraita',79,'Even an uncircumcised person is included.','Quoted all-slaughter baraita; identity clarified next',holder='Anonymous all-slaughter baraita')
C('apostatebaraita',79,'Even an Israelite apostate is included.','Quoted all-slaughter baraita; category disputed below',holder='Anonymous all-slaughter baraita')
Q('whichuncirc',79,'What kind of uncircumcised person is meant?', ['Baraita specifically includes ערל'])
C('brothersdead',79,'If his brothers died from circumcision, he is a fully proper Israelite.','Reason that this obvious case cannot explain emphasized inclusion',cond=['Brothers died because of circumcision'])
C('circumapostate',79,'The intended uncircumcised case is an apostate regarding circumcision.','Local conclusion about first category',cond=['מומר לערלות'])
C('onevsall',79,'Apostasy regarding one matter is not apostasy regarding the whole Torah.','Principle inferred from circumcision case',cond=['One specific matter'])
Q('whichapostate',80,'What kind of Israelite apostate is meant in the final clause?', ['All-slaughter baraita already includes circumcision apostate'])
C('otherredundant',80,'An apostate regarding a different matter would duplicate the circumcision case.','Redundancy argument about latter clause')
Q('sameoffense',80,'Must it not therefore mean an apostate regarding this very matter, in accordance with Rava?', ['Redundancy of different-matter interpretation','Proposed appetite-driven slaughter relevance'])
C('sameproposed',80,'The proposed inference reads the baraita as permitting the same-matter apostate, supporting Rava.','Proposed support disputed by alternative interpretation next',mode='challenged')
C('samenotnecessary',81,'One may instead deny permission for the same-matter apostate in interpreting this baraita.','Alternative blocking this proof, not a final refutation of Rava’s separate appetite rule',mode='hypothetical')
Q('samewhy',81,'Why might the same-matter apostate be excluded?', ['Alternative interpretation rejecting proposed proof'])
C('habit',81,'Because he is accustomed to it, it seems permitted to him.','Reason within alternative interpretation',cond=['Habitual violation of that same matter'])
C('idolatryalternative',81,'The baraita could instead concern an apostate to idolatry, following Rav Anan’s report.','Alternative to same-matter reading; later5a6–14 rejects Rav Anan’s idolatry rule',mode='rejected')
C('shmuelcited',81,'One may eat from the slaughter of an Israelite apostate to idolatry.','Shmuel’s rule as cited through Rav Anan; local report retained, explicit refutation of Rav Anan at5a14 governs final status',holder='שמואל',mode='rejected',cond=['Israelite apostate to idolatry'])
C('shmuelresumed',82,'One may eat from the slaughter of an Israelite apostate to idolatry.','Repeated גופא report preserved as separate occurrence; later refuted, not merged with Rava appetite case',holder='שמואל',mode='rejected',cond=['Israelite apostate to idolatry'])
for k,ii,target in [('ananreport',81,c['shmuelcited']),('ananresumed',82,c['shmuelresumed'])]:
 add(k,'attributions',ii,dict(surface='רב ענן אמר שמואל',role='transmitter',candidates=['רב ענן'],scope='Rav Anan reports Shmuel; report subsequently explicitly refuted at5a14',transmission_chain=['רב ענן','שמואל']),[target])
C('mealexample',82,'Jehoshaphat king of Judah benefited from Ahab’s meal.','Proposed historical proof for reported idolatry-slaughter permission; objections interrogate participation and slaughterers')
C('mealverse',82,'The cited verse says Ahab slaughtered sheep and cattle in abundance for him and his people and persuaded him to ascend to Ramoth-gilead.','Full proof text including abundance and persuasion, used in successive answers')
Q('slaughternoteat',83,'Perhaps he slaughtered, but Jehoshaphat did not eat?', ['Ahab’s slaughter does not alone establish participation'])
C('persuasionword',83,'ויסיתהו is written.','First answer relying on persuasion wording')
Q('justwords',83,'Perhaps the persuasion was through words?', ['Challenge to inferring eating from ויסיתהו'])
C('nowordspersuasion',83,'There is no persuasion through words.','Local answer tested by scriptural counterexamples, not a universal linguistic certification')
Q('brotherverse',84,'Is that so—what about כי יסיתך אחיך?', ['Challenge to no-persuasion-through-words answer'])
C('brotherfood',84,'That persuasion is through eating and drinking.','Answer interpreting the brother verse')
Q('jobverse',84,'What about ותסיתני בו לבלעו חנם?', ['Further challenge from Job verse'])
C('heavendifferent',84,'Above is different.','Answer distinguishes divine context from ordinary meal-persuasion usage')
Q('drinknoteat',85,'Perhaps Jehoshaphat drank but did not eat?', ['Meal evidence could show drink alone'])
Q('drinkdifferent',85,'Why should drinking differ from eating in applying the rule that apostasy to idolatry is not apostasy to the whole Torah?', ['Proposed rejection of drinking-only distinction'])
C('drinkcomparison',85,'The proposed reply treats drinking and eating alike under non-universal apostasy.','Provisional analogy rejected next',mode='rejected')
Q('comparable',86,'Are these cases comparable?', ['Drinking/eating analogy'])
C('wineunprohibited',86,'The drinking would concern ordinary gentile wine, which had not yet been prohibited.','Temporal legal distinction undermining analogy',cond=['Historical meal period before wine prohibition'])
C('foodmaybeall',86,'For eating, one could still say apostasy to idolatry is apostasy to the whole Torah.','Counter-possibility defeating drinking analogy; not yet final proof',mode='hypothetical',cond=['Eating/slaughter rather than then-unprohibited wine'])
C('royalcustom',87,'Alternatively, it is not a king’s custom to drink without eating.','First independent answer to drinking-only hypothesis')
Q('persuadedbywhat',87,'By what did he persuade him?', ['Second answer joins ויזבח and ויסיתהו'])
C('slaughterpersuasion',87,'Alternatively, the paired words ויזבח and ויסיתהו show persuasion through slaughter.','Second independent answer; not collapsed with royal-custom rationale')
Q('ovadyah',88,'Perhaps Obadiah slaughtered?', ['Would avoid proof from Ahab-associated slaughterers'])
C('toomany',88,'לרוב is written; Obadiah would not have sufficed.','Answer from large quantity')
Q('seventhousand',89,'Perhaps the seven thousand who had not bowed to Baal slaughtered?', ['Cited I Kings19:18 alternative righteous slaughterers'])
C('hiding',89,'They were hiding from Jezebel.','Answer rejecting their availability as slaughterers')
Q('ahabupright',90,'Perhaps Ahab’s men were upright?', ['Alternative that slaughterers were reliable despite Ahab'])
C('ahabwicked',90,'That is rejected through the verse that a ruler listening to falsehood has wicked servants.','Proverb applied to Ahab’s men in this proof, not a universal unsupported historical survey')
Q('yehoshapatnot',91,'Perhaps Jehoshaphat’s men too were not upright?', ['Alternative division of meal consumers and slaughterers','Answered explicitly at4b18'])
C('splitservants',91,'Perhaps Ahab’s men slaughtered and Jehoshaphat’s men ate their slaughter.','First part of proposed scenario; rejected by continuation4b18',mode='rejected')
C('splitking',91,'Perhaps Obadiah slaughtered for Jehoshaphat himself.','Second part of proposed scenario; rejected by continuation4b18',mode='rejected')
rels=[(72,'preferpermitted','reason','answer'),(72,'preferpermitted','ch.s2709.ravaeat','support'),(73,'noeffort','unchecked','answer'),(73,'noeffort','ch.s2709.ravaappetite','support'),(75,'leavenallowed','scholarssupport','support'),(75,'exchange','leavenallowed','support'),(76,'exchange','exchangeproof','support'),(76,'exchangeproof','preferpermitted','support'),(77,'whoyehuda','yehudainitial','objection'),(77,'leniencyobjection','exchangeproof','objection'),(78,'definiteexchange','presumedexchange','answer'),(78,'definiteexchange','leniencyobjection','objection'),(78,'afortioriproof','afortiori','answer'),(78,'afortioriproof','preferpermitted','support'),(79,'circumapostate','whichuncirc','answer'),(79,'circumapostate','onevsall','support'),(80,'otherredundant','whichapostate','qualification'),(80,'sameproposed','sameoffense','answer'),(80,'sameproposed','allslaughterproof','answer'),(81,'samenotnecessary','sameproposed','objection'),(81,'habit','samewhy','answer'),(81,'idolatryalternative','whichapostate','answer'),(81,'shmuelcited','idolatryalternative','support'),(82,'mealexample','shmuelresumed','support'),(82,'mealverse','mealexample','support'),(83,'persuasionword','slaughternoteat','answer'),(83,'justwords','persuasionword','objection'),(83,'nowordspersuasion','justwords','answer'),(84,'brotherverse','nowordspersuasion','objection'),(84,'brotherfood','brotherverse','answer'),(84,'jobverse','nowordspersuasion','objection'),(84,'heavendifferent','jobverse','answer'),(85,'drinknoteat','mealexample','objection'),(85,'drinkcomparison','drinknoteat','answer'),(86,'comparable','drinkcomparison','objection'),(86,'wineunprohibited','drinkcomparison','objection'),(86,'foodmaybeall','drinkcomparison','objection'),(87,'royalcustom','drinknoteat','answer'),(87,'slaughterpersuasion','drinknoteat','answer'),(87,'slaughterpersuasion','persuadedbywhat','answer'),(88,'ovadyah','mealexample','objection'),(88,'toomany','ovadyah','answer'),(89,'seventhousand','mealexample','objection'),(89,'hiding','seventhousand','answer'),(90,'ahabupright','mealexample','objection'),(90,'ahabwicked','ahabupright','answer'),(91,'yehoshapatnot','mealexample','objection')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={72:'Explicit reason question; appetite-motive preference principle scoped to available permitted option.',73:'Unchecked-knife challenge and lack-of-effort answer preserve required prior inspection.',74:'Rabbis speak to Rava; baraita leaven clause completed4b1, full cross-folio evidence.',75:'Immediate after-Passover permission because exchanging; not silently converted to mere presumption.',76:'סברוה provisional Yehuda identification, his Torah-level position, and behavioral support distinguished.',77:'How-known/perhaps-Shimon question and rabbinic-versus-Torah leniency objection remain provisional.',78:'Presumption-versus-definite-exchange question, definite behavior answer and a fortiori question/argument retain reasoning even if Shimon.',79:'Support question; all three inclusion categories; uncircumcised identity question; brothers-death case distinguished from circumcision apostasy and one-matter principle.',80:'Latter-clause apostate identity question; redundancy and same-matter inference explicitly proposed, not final exclusive reading.',81:'Alternative denying same-matter inference, habit reason question/answer, idolatry interpretation, Rav Anan transmitter and Shmuel authority. Later5a14 explicitly refutes Rav Anan report; source occurrence remains.',82:'Separate resumed Rav Anan/Shmuel report with historical meal proof and full abundance/persuasion verse; eventual refutation not concealed.',83:'Slaughter-but-not-eat question, persuasion answer, words-only question and tested no-verbal-persuasion claim.',84:'Both brother and Job counterexample questions and distinct food/drink versus divine-context replies.',85:'Drink-without-food hypothesis and why-different question; proposed category analogy marked subsequently rejected.',86:'Comparable question and wine-not-yet-prohibited temporal distinction, leaving food apostasy possibility open.',87:'Two independent optional answers: royal custom and slaughter/persuasion wording; embedded by-what question retained.',88:'Obadiah-slaughter hypothesis and insufficient-capacity answer from לרוב.',89:'Seven-thousand righteous-slaughterers hypothesis and hiding-from-Jezebel response.',90:'Ahab-servants-upright hypothesis rejected using cited ruler/servants verse.',91:'Jehoshaphat-servants-not-upright question and split meals scenario retained as hypothesis, rejected4b18. Full relevant context through5a14 read: further separated-groups alternatives, later support disputes and explicit Rav Anan refutation remain future source occurrences; no context coverage credit.'}
for i in range(72,92):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous argument and named reports separately attributed; proposed sources are quoted, not narrator endorsement',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara framing',role='anonymous',candidates=[],scope='Anonymous argument only; named reporting and holder roles separately recorded',transmission_chain=[]))
COV=[]
for i in range(72,92):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s2])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_4a19_4b17_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
