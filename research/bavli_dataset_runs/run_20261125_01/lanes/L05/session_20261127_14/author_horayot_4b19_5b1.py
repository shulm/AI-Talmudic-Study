"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_horayot')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='b161e3f79e71f5d463d653d3c53b883c2aff0bb7fd715d0a893448a8d57d961d';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/horayot','epoch':2}
assert I[121]['ref']=='Horayot 4b:19' and I[140]['ref']=='Horayot 5b:1'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='hor.s2714.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('mishnah','structure',range(121,125),dict(title='Court-error offerings: public or tribal action, counts by tanna, and tribal versus Great Court',primary=True,boundary='closed',legacy_ids=[]))
s2=add('proofs','structure',range(125,141),dict(title='Identifying the sin, kahal derivations and population/tribal majorities; court-action proof continues',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
base=['Court gives ruling','Whole congregation or majority acts on that ruling']
C('meirbull',121,'One bull is brought.','Rabbi Meir; court responsibility clarified by baraita5a7',base,'רבי מאיר')
C('meiridol',121,'For idolatry, one bull and one goat are brought.','Rabbi Meir offering types/counts',base+['Idolatry'],'רבי מאיר')
C('yehuda12',121,'The twelve tribes bring twelve bulls.','Rabbi Yehuda',base,'רבי יהודה')
C('yehudaidol',121,'For idolatry they bring twelve bulls and twelve goats.','Rabbi Yehuda',base+['Idolatry'],'רבי יהודה')
C('shimon13',[121,122],'Thirteen bulls are brought.','Rabbi Shimon; initial court/action condition continues from prior segment',base,'רבי שמעון')
C('shimonidol',[121,122],'For idolatry, thirteen bulls and thirteen goats are brought.','Rabbi Shimon',base+['Idolatry'],'רבי שמעון')
C('shimontribe',122,'For idolatry each tribe brings a bull and a goat.','Rabbi Shimon distribution of stated total',base+['Idolatry'],'רבי שמעון')
C('shimoncourtallocation',122,'The court brings a bull and a goat.','Rabbi Shimon additional court share in idolatry total',base+['Idolatry'],'רבי שמעון')
seven=['Court gives ruling','Source condition: seven tribes or רובן act on the ruling']
C('sevenmeir',123,'One bull is brought.','Rabbi Meir seven-tribe scenario; source רובן retained, not silently interpreted as population majority',seven,'רבי מאיר')
C('sevenmeiridol',123,'For idolatry, a bull and a goat are brought.','Rabbi Meir seven-tribe scenario',seven+['Idolatry'],'רבי מאיר')
C('sevenyehuda',123,'The seven tribes that sinned bring seven bulls.','Rabbi Yehuda',seven,'רבי יהודה')
C('othersyehuda',123,'The remaining tribes that did not sin also bring bulls because of the sinners.','Rabbi Yehuda extension to nonsinning tribes; one per tribe clarified baraita5a5',seven+['Other tribes did not sin'],'רבי יהודה')
C('sevenshimon',123,'Eight bulls are brought.','Rabbi Shimon seven-tribe scenario',seven,'רבי שמעון')
C('sevenshimonidol',123,'For idolatry, eight bulls and eight goats are brought.','Rabbi Shimon',seven+['Idolatry'],'רבי שמעון')
C('sevenallocation',123,'Each sinning tribe brings a bull and goat, and the court brings a bull and goat.','Distribution of eight idolatry pairs',seven+['Idolatry'],'רבי שמעון')
C('tribalcourtliable',124,'That tribe alone is liable when it acts on the ruling of its own tribal court.','Rabbi Yehuda tribal-court scope',cond=['One tribe’s court rules','That tribe acts on it'],holder='רבי יהודה')
C('othertribesexempt',124,'The other tribes are exempt in the tribal-court case.','Rabbi Yehuda negative scope; later5b8–9 distinguishes Great Court',cond=['Ruling by that tribe’s own court'],holder='רבי יהודה')
C('greatcourtonly',124,'Liability arises only from rulings of the Great Court.','Sages oppose tribal-court liability',cond=['Court-error offering liability'],holder='חכמים')
C('wholeassembly',124,'The verse says the whole assembly of Israel errs, not the assembly of that tribe.','Sages’ textual basis for Great Court limitation')
Q('forgotruling',125,'If they know they issued a ruling but no longer know what they ruled, might they be liable?', ['Knowledge of having ruled','Specific ruling/sin not identified'])
C('knownsin',125,'ונודעה החטאת requires the sin to become known, not merely the sinners.','Baraita rejects sufficiency of knowing who sinned without the specific sin',cond=['Specific sin unknown','Sinners known'])
C('twotribes',126,'If two tribes sinned, they bring two bulls.','Rabbi Yehuda’s tribal reading of אשר חטאו',cond=['Two sinning tribes'],holder='רבי יהודה')
C('threetribes',126,'If three tribes sinned, they bring three bulls.','Rabbi Yehuda’s tribal reading',cond=['Three sinning tribes'],holder='רבי יהודה')
Q('twoindividuals',126,'Could it instead mean two individuals bring two bulls, and three individuals bring three?', ['Possible individual rather than tribal interpretation of plural sinners'])
C('eachkahal',126,'הקהל means the congregation is liable, and each congregation is liable.','Text excludes proposed individual unit and counts tribal congregations',holder='רבי יהודה')
C('sevenbaraita',126,'Seven sinning tribes bring seven bulls.','Rabbi Yehuda repeated baraita instance',cond=['Seven tribes sinned'],holder='רבי יהודה')
C('othersbaraita',126,'Each remaining nonsinning tribe brings a bull on account of the sinners.','פר פר explicit; separate from court’s bull in other views',cond=['Other tribes sinned','This tribe did not sin'],holder='רבי יהודה')
C('shimonseven',127,'Seven sinning tribes bring seven bulls.','Rabbi Shimon baraita',cond=['Seven tribes sinned'],holder='רבי שמעון')
C('shimoncourt',127,'The court brings an additional bull on their account.','Rabbi Shimon court plus public',cond=['Seven tribes sinned'],holder='רבי שמעון')
C('shimonanalogy',127,'The later קהל is compared to the earlier קהל: as there the court is with the congregation, so here too.','Rabbi Shimon derivation includes both court and congregation',holder='רבי שמעון')
C('meircourt',128,'When seven tribes sin, the court brings a bull on their account.','Rabbi Meir court obligation',cond=['Seven sinning tribes'],holder='רבי מאיר')
C('meirpublicfree',128,'The people themselves are exempt.','Rabbi Meir contrasting allocation',cond=['Seven tribes sinned'],holder='רבי מאיר')
C('meiranalogy',128,'The later קהל is compared to the earlier קהל as court without the public.','Rabbi Meir same comparison with different referent',holder='רבי מאיר')
C('sixmajority',129,'Six sinning tribes that form a majority of the congregation bring a bull.','Rabbi Shimon ben Elazar reporting Rabbi Meir; tribal count and population count distinct',cond=['Six tribes sinned','They constitute majority of population'],holder='רבי מאיר — במסירת רבי שמעון בן אלעזר')
C('sevenminority',129,'Seven sinning tribes bring a bull even if they are not a majority of the congregation.','Alternative tribal-majority condition',cond=['Seven tribes sinned','Even without population majority'],holder='רבי מאיר — במסירת רבי שמעון בן אלעזר')
add('shimonelazarreport','attributions',129,dict(surface='רבי שמעון בן אלעזר אומר משמו',role='transmitter',candidates=['רבי שמעון בן אלעזר'],scope='משמו continues preceding Rabbi Meir attribution; two threshold alternatives reported',transmission_chain=['רבי שמעון בן אלעזר','רבי מאיר']),[c['sixmajority'],c['sevenminority']])
Q('whoknownsin',130,'Who is the tanna requiring knowledge of the sin rather than merely of the sinners?', ['Baraita at5a4','Specific sin uncertain'])
C('noteliezer',[130,131],'The baraita is not Rabbi Eliezer.','First answer, challenged by Rav Ashi’s distinction; transmitted with alternative Rav/Rava attribution',mode='challenged')
add('ravroute','attributions',130,dict(surface='אמר רב יהודה אמר רב ואיתימא רבא',role='transmitter',candidates=['רב יהודה'],scope='First report route: Rav Yehuda in Rav’s name; alternative attribution is Rava, retained separately rather than forced into same chain',transmission_chain=['רב יהודה','רב']),[c['noteliezer']],unc=['Source offers alternative attribution to Rava.'])
add('ravaroute','attributions',130,dict(surface='ואיתימא רבא',role='speaker',candidates=['רבא'],scope='Alternative reporting attribution of not-Rabbi-Eliezer answer, not a second independent argument',transmission_chain=[]),[c['noteliezer']],unc=['Alternative to Rav Yehuda reporting Rav.'])
C('eliezerfat',131,'If he ate forbidden fat, he is liable.','Rabbi Eliezer’s either-way argument',cond=['Uncertain whether consumed חלב or נותר','If consumed חלב'],holder='רבי אליעזר')
C('eliezerleftover',131,'If he ate leftover sacrificial food, he is liable.','Second limb of Rabbi Eliezer’s either-way argument',cond=['Uncertain whether consumed חלב or נותר','If consumed נותר'],holder='רבי אליעזר')
C('ashicompatible',132,'The baraita can even follow Rabbi Eliezer.','Rav Ashi alternative resolves apparent contradiction by special verse',holder='רב אשי')
C('thisverse',132,'Here the verse says אשר חטאו עליה.','Rav Ashi’s specific requirement in communal-error case',holder='רב אשי')
Q('thereverse',132,'But there too is אשר חטא בה written?', ['Proposed textual distinction between communal case and Eliezer individual case'])
C('excludeunintended',132,'That expression is needed to exclude מתעסק.','Answer giving individual-case verse another function; not blanket exemption for all inadvertence',cond=['מתעסק category'])
Q('yehudareason',133,'What is Rabbi Yehuda’s reason?', ['Multiple tribe/court offering allocations'])
C('fourkahal',133,'He counts four קהל expressions: קהל הקהל קהל הקהל.','Rabbi Yehuda counts base words and articles as separate derivational units',holder='רבי יהודה')
C('yehudafunction1',134,'One requires liability for each congregation.','First of four derivations',holder='רבי יהודה')
C('yehudafunction2',134,'One makes instruction depend on the court and action on the congregation.','Distinct institutional roles',holder='רבי יהודה')
C('yehudafunction3',134,'One establishes גרירה, drawing other tribes into the offering obligation.','Third derivation, scope of this principle further tested5b4–9',holder='רבי יהודה')
C('yehudafunction4',134,'One covers a tribe acting on its court’s instruction.','Fourth derivation; tribal-court case',holder='רבי יהודה')
C('threekahal',135,'Rabbi Shimon counts three קהל expressions.','Contrasting derivational count',holder='רבי שמעון')
C('eyesidiom',135,'מעיני הקהל is ordinary phrasing, like people say מעיני דפלניא.','Reason not to count its article as separate extra expression',holder='רבי שמעון')
C('shimonone',136,'One expression imposes liability on each congregation.','Rabbi Shimon first use',holder='רבי שמעון')
C('shimontwo',136,'The other two compare later and earlier קהל to include the court with the congregation.','Rabbi Shimon paired derivation',holder='רבי שמעון')
C('meirnoarticle',137,'Rabbi Meir does not derive separately from קהל versus הקהל.','No extra article-based count',holder='רבי מאיר')
C('meirtwo',137,'He therefore counts two קהל expressions.','Rabbi Meir resulting count',holder='רבי מאיר')
C('meirpair',137,'Both are needed for the earlier/later comparison: court, not public.','Rabbi Meir allocation derivation',holder='רבי מאיר')
Q('shimonelazarreason',138,'What is Rabbi Shimon ben Elazar’s reason?', ['Six population-majority tribes or seven without population majority'])
C('eyesminority',138,'והיה אם מעיני העדה implies a minority.','First textual pressure in threshold derivation')
C('allmajority',138,'כי לכל העם בשגגה implies majority, not minority.','Opposing textual pressure; both requirements reconciled next')
Q('reconcilethreshold',139,'How are these reconciled?', ['Minority expression and majority expression','Population versus tribe counts'])
C('sixresolution',139,'Six tribes that are a population majority are liable.','First reconciliation branch',cond=['Six sinning tribes','Population majority'])
C('sevenresolution',139,'Seven tribes are liable even without population majority.','Second reconciliation branch',cond=['Seven sinning tribes','Population majority not required'])
Q('institutionalsource',140,'From where do Rabbi Shimon and Rabbi Meir derive that instruction belongs to the court and action to the congregation?', ['They use their קהל expressions for other derivations'])
C('abayeproof',140,'והיה אם מעיני העדה נעשתה לשגגה is the source.','Abaye proof; next5b2 states both verses needed, so not exclusive rival final rules',holder='אביי')
C('ravaproof',140,'מכל העם בשגגה is the source.','Rava proof; combined necessity clarified next',holder='רבא')
Q('howeach',126,'How is liability for each congregation applied?', ['Plural tribal congregations rather than individual sinners'])
Q('eitherway',131,'Whichever of the two foods was eaten, is he not liable?', ['Uncertain whether forbidden fat or leftover sacrificial food was consumed'])
rels=[(124,'wholeassembly','greatcourtonly','support'),(125,'knownsin','forgotruling','answer'),(126,'eachkahal','twoindividuals','answer'),(126,'twotribes','howeach','answer'),(126,'sevenbaraita','howeach','answer'),(126,'eachkahal','twotribes','support'),(126,'eachkahal','othersbaraita','support'),(127,'shimonanalogy','shimoncourt','support'),(127,'shimonanalogy','shimonseven','support'),(128,'meiranalogy','meircourt','support'),(128,'meiranalogy','meirpublicfree','support'),(130,'noteliezer','whoknownsin','answer'),(131,'eliezerfat','noteliezer','support'),(131,'eliezerleftover','noteliezer','support'),(131,'eliezerfat','eitherway','answer'),(131,'eliezerleftover','eitherway','answer'),(132,'ashicompatible','noteliezer','correction'),(132,'thisverse','ashicompatible','support'),(132,'thereverse','thisverse','objection'),(132,'excludeunintended','thereverse','answer'),(133,'fourkahal','yehudareason','answer'),(134,'yehudafunction1','eachkahal','support'),(134,'yehudafunction3','othersyehuda','support'),(134,'yehudafunction4','tribalcourtliable','support'),(135,'eyesidiom','threekahal','support'),(136,'shimontwo','shimoncourt','support'),(136,'shimonone','shimonseven','support'),(137,'meirnoarticle','meirtwo','support'),(137,'meirpair','meircourt','support'),(137,'meirpair','meirpublicfree','support'),(138,'eyesminority','shimonelazarreason','answer'),(138,'allmajority','eyesminority','objection'),(139,'sixresolution','reconcilethreshold','answer'),(139,'sevenresolution','reconcilethreshold','answer'),(139,'sixresolution','sixmajority','support'),(139,'sevenresolution','sevenminority','support'),(140,'abayeproof','institutionalsource','answer'),(140,'ravaproof','institutionalsource','answer')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={121:'Mishnah initial court instruction and whole/majority action govern offering counts; Meir and Yehuda idolatry types separated.',122:'Continuation of initial condition; Shimon thirteen totals and tribe/court distribution preserved.',123:'Seven tribes or source רובן retained without conflating population and tribal count; all three views, nonsinning tribes and court share distinguished.',124:'Own tribal court versus Great Court, other tribes exemption and scriptural exclusion explicitly represented; later5b8 distinguishes national-court case.',125:'Explicit hypothetical liability question and knowledge-of-sin not merely sinner answer; specific unknown ruling condition retained.',126:'Rejected individual reading and כיצד illustration separately questioned; two/three/seven tribal counts, each nonsinning tribe obligation, and Yehuda attribution.',127:'Shimon court with congregation comparison supports separate court and tribal obligations.',128:'Meir court without public comparison supports court obligation and public exemption.',129:'Six with population majority versus seven without it; Shimon ben Elazar reports preceding Meir rather than an invented independent speaker position.',130:'Who-tanna question; initial not-Eliezer answer is challenged later, alternative Rav Yehuda reporting Rav OR Rava preserved separately.',131:'Eliezer either-way argument and fat/leftover conditional branches; full preceding reported argument evidence retained.',132:'Rav Ashi permits Eliezer via communal verse; individual verse counterquestion and מתעסק exclusion prevent universalizing distinction.',133:'Why-Yehuda question and four-expression count; lexical article counts preserved.',134:'Four separate derivational functions: each congregation, institutional roles, drawing other tribes, tribal own-court case.',135:'Shimon three-expression count and ordinary-language explanation for מעיני הקהל.',136:'One expression per congregation, other two comparison for court with congregation.',137:'Meir does not derive extra article; two expressions, court not public; scope is this derivation.',138:'Why Shimon ben Elazar question; apparently minority and majority textual pressures remain separately asserted before reconciliation.',139:'Explicit reconciliation question, six population-majority versus seven without population-majority alternatives.',140:'Question about institutional roles for Shimon and Meir; Abaye and Rava verses separately attributed.5b2 requires both,5b3 extends idolatry verses by מעיני analogy; context through5b16 read for tribal court distinctions, rejected proofs and later tribe-as-kahal argument. Context not new core coverage.'}
for i in range(121,141):
 add('u'+str(i),'utterances',i,dict(textual_voice='Mishnah/baraita and anonymous argument with named views and reports separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous source framing',role='anonymous',candidates=[],scope='Framing only; not replacing named tannaitic positions or report routes',transmission_chain=[]))
ALL=[r for r in S['records'] if r.get('release_state')=='valid']+R
COV=[]
for i in range(121,141):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in ALL if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s2])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'horayot_4b19_5b1_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
