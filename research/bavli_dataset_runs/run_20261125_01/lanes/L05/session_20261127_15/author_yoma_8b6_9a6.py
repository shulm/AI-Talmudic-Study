"""Direct source annotations for the explicitly bounded range: 10 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='0076dc58395deeada80a786ed07b970e05f66fb3fb8312042034318d84455a82';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
assert I[150]['ref']=='Yoma 8b:6' and I[159]['ref']=='Yoma 9a:6'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2715.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('chamber','structure',range(150,152),dict(title='Chamber name changed from councilors to annually replaced officials',primary=True,boundary='closed',legacy_ids=[]))
s2=add('bakers','structure',range(152,157),dict(title='Bakers dues and annual officials pressure',primary=True,boundary='closed',legacy_ids=[]))
s3=add('tenures','structure',range(157,159),dict(title='Proverbs interpretation through High Priest tenures and alternative report',primary=True,boundary='closed',legacy_ids=[]))
s4=add('shiloh','structure',[159,160,161],dict(title='Shiloh destruction, Eli sons qualified accusation and contempt for holy things',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('chamber',150,'Was it the Parhedrin chamber? Was it not the Balvatei chamber?', ['Chamber named in Mishnah','Earlier chamber name'])
add('yehudaquestion','attributions',150,dict(surface='תניא רבי יהודה',role='speaker',candidates=['רבי יהודה'],scope='Quoted baraita questions chamber designation and explains the change',transmission_chain=[]),[z['chamber']])
C('oldname',[150,151],'At first it was called the Balvatei chamber.','Rabbi Yehuda baraita initial name',holder='רבי יהודה')
C('payment',151,'Money is paid for the priesthood.','Baraita explanation of changed office/chamber designation; no named purchaser inferred',holder='רבי יהודה')
C('annualpriesthood',151,'The priesthood changes every twelve months.','Baraita comparison underlying chamber name; not an exhaustive biographical rule overriding later exceptions',holder='רבי יהודה')
C('annualofficials',151,'These parhedrin officials are replaced every twelve months.','Analogy to priesthood turnover',holder='רבי יהודה')
C('newname',151,'Therefore it came to be called the Parhedrin chamber.','Name change explained by paid, annually changing priesthood',holder='רבי יהודה')
dues=['Bakers in the quoted dues ruling','Uncertain prior tithing context, inferred from survey and exemptions rather than explicit word דמאי in this excerpt']
C('bakerterumah',152,'The sages required bakers to separate terumat maaser.','Quoted Mishnah; restriction אלא includes this and challah',dues,'Quoted Mishnah sages')
C('bakerchallah',152,'The sages required bakers to separate challah.','Second required due in quoted Mishnah',dues,'Quoted Mishnah sages')
C('onlydues',152,'They did not require those bakers to separate dues beyond terumat maaser and challah.','Limited obligation in this quoted case, not a universal exemption for untithed produce',dues,'Quoted Mishnah sages')
C('greatnot',[153,154],'The absence of a requirement for terumah gedolah is understandable from the cited survey.','בשלמא accepted premise; full reason crosses folio',dues)
C('survey',154,'He sent throughout Israel and found that they separated only terumah gedolah.','Cited baraita gives empirical rationale; the sender is unnamed in this excerpt, not assigned an invented speaker identity')
C('firstnot',155,'First tithe is not compulsorily handed over in this case.','Monetary recovery rationale; not denial of terumat maaser separation already required',dues+['Claim for first-tithe payment'])
C('poornot',155,'Poor tithe is not compulsorily handed over in this case.','Same monetary proof rule',dues+['Claim for poor-tithe payment'])
C('proofburden',155,'The one seeking to extract property from another bears the burden of proof.','Reason for noncompulsory first/poor tithe payment; retains claimant condition',cond=['Claimant seeks property held by another'])
Q('secondtithe',155,'But should they not separate second tithe, bring it up and eat it in Jerusalem?',dues+['Second tithe not covered by preceding monetary-payment rationale'])
C('officialpressure',156,'These officials pressure the bakers every twelve months, repeatedly telling them to sell cheaply.','Ulla explanation; annual interval and repeated מכרו בזול retained',holder='עולא')
C('noburden',156,'The sages did not impose that burden on the bakers.','Ulla answers second-tithe question in this pressured baker context; not universal abolition of second tithe',dues+['Officials pressure them to sell cheaply'],'עולא')
Q('meaning',156,'What does parhedrin mean?', ['Word used of the annual officials'])
C('definition',156,'Parhedrin means פורסי.','Source gloss kept verbatim; no unsupported expansion into a modern office')
Q('proverbs',157,'What is meant by fear of the Lord adding days and the years of the wicked being shortened?', ['Proverbs10:27 interpretation'])
C('firsttemple',157,'Fear of the Lord adding days refers to the First Temple.','Rabbi Yohanan interpretation transmitted by Rabbah bar bar Hanah',holder='רבי יוחנן')
C('firstduration',157,'The First Temple stood four hundred and ten years.','Number as asserted in this source, not independent chronological certification',holder='רבי יוחנן')
C('firstpriests',157,'Only eighteen High Priests served in it.','Source count connected to lengthy righteous tenures',holder='רבי יוחנן')
C('secondtemple',[157,158],'The years of the wicked being shortened refers to the Second Temple.','Continuation of Rabbi Yohanan interpretation',holder='רבי יוחנן')
C('secondduration',158,'The Second Temple stood four hundred and twenty years.','Source chronology',holder='רבי יוחנן')
C('secondpriests',158,'More than three hundred priests served in it.','Source count, not exactly three hundred; High Priest tenure context',holder='רבי יוחנן')
C('shimonforty',158,'Shimon the Righteous served forty years.','Named long tenure excluded before calculating remainder',holder='רבי יוחנן')
C('yohanan80',158,'Yohanan the High Priest served eighty years.','Historical person in reported claim, not automatically Rabbi Yohanan the reporting authority',holder='רבי יוחנן')
C('ishmael10',158,'Ishmael ben Pabi served ten years.','Initial tenure report, followed by ואמרי לה alternative',holder='רבי יוחנן')
C('elazar11',158,'An alternative report gives eleven years served by Rabbi Elazar ben Harsum.','ואמרי לה variant preserved without silently adding or substituting its number in an invented combined arithmetic',unc=['Alternative report; relation to initial exclusion list left at source wording.'])
C('remaining',158,'After excluding the stated long tenures, calculate that each of the remaining priests did not complete his year.','Source rhetorical tenure conclusion; not applied to named exceptions or offered as independent verified arithmetic',cond=['Remaining Second Temple priests after stated exclusions'],holder='רבי יוחנן')
add('yohananreport','attributions',[157,158],dict(surface='אמר רבה בר בר חנה א"ר יוחנן',role='transmitter',candidates=['רבה בר בר חנה'],scope='Proverbs interpretation and temple-tenure discussion; alternative anonymous report separately retained',transmission_chain=['רבה בר בר חנה','רבי יוחנן']),[z['proverbs'],c['firsttemple'],c['secondtemple']])
add('tenurevariant','attributions',158,dict(surface='ואמרי לה',role='anonymous',candidates=[],scope='Alternative eleven-year Elazar ben Harsum tenure report, not a newly identified transmitter',transmission_chain=[]),[c['elazar11']])
Q('shilohwhy',159,'Why was Shiloh destroyed?', ['Rabbi Yohanan ben Torta asks about Shiloh, distinct from the preceding Rabbi Yohanan report'])
C('shilohsexual',159,'One of the two stated causes for Shiloh destruction is sexual misconduct.','Rabbi Yohanan ben Torta statement, qualified below by as-if scriptural reckoning for delaying offerings; not a final literal claim about Eli sons',holder='רבי יוחנן בן תורתא')
C('shilohcontempt',159,'The other stated cause is contempt for sacred offerings.','Rabbi Yohanan ben Torta; scriptural proof continues9b2',holder='רבי יוחנן בן תורתא')
C('eliverse',159,'The cited verse describes Eli hearing what his sons did and their lying with the women who assembled at the entrance of the Tent of Meeting.','Quoted1Samuel2:22 initially adduced for sexual-misconduct charge, subsequently qualified; do not turn quotation into unqualified historical endorsement')
C('notliteralguilt',159,'Anyone saying Eli’s sons sinned in this way is mistaken.','Rabbi Yohanan reported by Rabbi Shmuel bar Nahmani; local sexual-act allegation, not a denial of every wrongdoing',holder='רבי יוחנן')
add('shmuelreport','attributions',159,dict(surface='דאמר ר׳ שמואל בר נחמני א״ר יוחנן',role='transmitter',candidates=['רבי שמואל בר נחמני'],scope='Qualification of literal sexual accusation; this Rabbi Yohanan is not Rabbi Yohanan ben Torta',transmission_chain=['רבי שמואל בר נחמני','רבי יוחנן']),[c['notliteralguilt']])
C('delayed',[159,160],'They delayed the women’s bird offerings.','Full continuation of מתוך across9a6–9b1 supplies actual conduct underlying figurative scriptural reckoning')
C('asif',[159,160],'Because they delayed those offerings, Scripture nevertheless reckons it as though they lay with the women.','כאילו retains comparison and does not assert literal intercourse',cond=['Delay of women’s bird offerings'])
add('tortaquestion','attributions',159,dict(surface='א״ר יוחנן בן תורתא',role='speaker',candidates=['רבי יוחנן בן תורתא'],scope='Shiloh why-question and two causes; distinct from the authority cited inside subsequent qualification',transmission_chain=[]),[z['shilohwhy']])
rels=[(151,'oldname','chamber','answer'),(151,'newname','chamber','answer'),(151,'payment','newname','support'),(151,'annualpriesthood','newname','support'),(151,'annualofficials','annualpriesthood','analogy'),([153,154],'survey','greatnot','support'),(155,'proofburden','firstnot','support'),(155,'proofburden','poornot','support'),(155,'secondtithe','onlydues','objection'),(156,'noburden','secondtithe','answer'),(156,'officialpressure','noburden','support'),(156,'definition','meaning','answer'),(157,'firsttemple','proverbs','answer'),(157,'firstduration','firsttemple','support'),(157,'firstpriests','firsttemple','support'),(158,'secondtemple','proverbs','answer'),(158,'secondduration','secondtemple','support'),(158,'secondpriests','secondtemple','support'),(158,'shimonforty','remaining','qualification'),(158,'yohanan80','remaining','qualification'),(158,'ishmael10','remaining','qualification'),(158,'elazar11','ishmael10','qualification'),(158,'remaining','secondtemple','support'),(159,'shilohsexual','shilohwhy','answer'),(159,'shilohcontempt','shilohwhy','answer'),(159,'eliverse','shilohsexual','support'),(159,'notliteralguilt','eliverse','qualification'),([159,160],'delayed','asif','support'),([159,160],'asif','shilohsexual','qualification'),([159,160],'asif','notliteralguilt','local_resolution')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={150:'Rabbi Yehuda chamber-name question and earlier Balvatei name; speaker explicit.',151:'Payment, twelve-month priesthood turnover, annual-official comparison and resulting name separate; later long tenures prevent universalizing turnover.',152:'Quoted bakers obligation limited to terumat maaser and challah; uncertain-tithing context marked interpretive, not invented verbatim wording.',153:'בשלמא accepted terumah-gedolah exemption premise joins next folio survey, evidence fullcontinuation.',154:'Survey throughout Israel finds only terumah gedolah separated; unnamed sender not given unsupported proper name.',155:'First/poor tithe monetary burden of proof not confused with earlier terumat maaser; second tithe separation/ascent/Jerusalem-eating objection separately questioned with conditions.',156:'Ulla annual pressure and repeated sell-cheap command explains limited burden; separate definition question and exact פורסי answer.',157:'Rabbah bar bar Hanah reports Rabbi Yohanan; explicit verse question and First Temple410years/18priests claims kept source assertions.',158:'Second Temple420years/more-than300; named40/80/10years and alternate11years retained with reporting roles, not forcibly pooled; remaining priests conclusion excludes long tenures.',159:'Yohanan ben Torta question/two causes distinct from Shmuel bar Nahmani reporting Yohanan. Full מתוך...9b1 split qualification preserves actual delayed bird offerings and כאילו, not literal intercourse.9b2 contempt proof and9b3 following Temple destruction topic read as context; context not counted core coverage.'}
for i in range(150,160):
 add('u'+str(i),'utterances',i,dict(textual_voice='Quoted authorities and anonymous discussion with reports explicitly distinguished',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only, not an assertion that all named quoted material is anonymous',transmission_chain=[]))
COV=[]
for i in range(150,160):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s4])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_8b6_9a6_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=10,sha256=hashlib.sha256(b).hexdigest())))
