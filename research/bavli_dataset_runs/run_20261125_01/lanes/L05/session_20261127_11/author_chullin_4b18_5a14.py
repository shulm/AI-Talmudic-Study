"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='b0ce5a2b110699b460d566e48510d031a970103fcf76984e7359ab1f8be6566f';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[92]['ref']=='Chullin 4b:18' and I[107]['ref']=='Chullin 5a:14'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2711.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('refutation','structure',range(92,108),dict(title='Meal and raven proofs tested; apostate-offering baraita resolves in explicit refutation of Rav Anan report',primary=True,boundary='open_right',legacy_ids=[]))
e('continue',92,'ch.s2710.anan',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
C('righteousservants',92,'A ruler listening to truth has righteous servants, by contrast with the cited ruler listening to falsehood.','Reply rejecting preceding hypothesis about Jehoshaphat’s servants; source inference, not independent historical survey')
Q('separatefood',93,'Perhaps Ahab’s men slaughtered for Ahab and his men, and Jehoshaphat’s men slaughtered for Jehoshaphat and his men?', ['Separate preparation and consumption would undermine shared-slaughter proof'])
C('separatehypothesis',93,'Each royal group may have consumed only its own group’s slaughter.','Proposed separation hypothesis answered next',mode='rejected')
C('notseparate',94,'Jehoshaphat did not separate himself from Ahab.','Reply to separated-meals hypothesis; proposed evidence tested')
Q('notsource',94,'From where do we know that he did not separate himself?', ['Reply rejecting separate meals'])
C('firstverse',94,'כמוני כמוך כעמי כעמך is proposed as evidence of nonseparation.','Initial proof, rejected as noncompelling',mode='rejected')
Q('horses',94,'If so, does כסוסי כסוסיך also mean that sort of identity or sharing?', ['Proposed literal nonseparation reading of parallel declarations'])
C('horsefate',94,'The horse declaration means that what happens to your horses will happen to mine.','Alternative meaning of parallel verse clause; not evidence of shared food')
C('peoplefate',94,'Likewise, what happens to you and your people will happen to me and mine.','Corresponding interpretation defeats first nonseparation proof')
C('secondverse',95,'Instead the verse describes the two kings seated on their thrones in royal clothing in a גורן at the entrance of Samaria’s gate.','Replacement proof of their shared company; complete cited setting retained')
Q('goren',95,'What does גורן mean here?', ['Verse about two kings at city gate'])
Q('literalfloor',95,'Could it mean a literal threshing floor—was Samaria’s gate a threshing floor?', ['Proposed literal meaning'])
C('likegoren',95,'It means like a threshing floor.','Nonliteral spatial comparison in reply')
C('sanhedrinshape',95,'The Sanhedrin sat in a semicircle like half a threshing floor.','Quoted Mishnah used for comparison',holder='Anonymous Sanhedrin Mishnah')
C('seeeachother',95,'The arrangement lets them see one another.','Purpose in quoted Mishnah',holder='Anonymous Sanhedrin Mishnah')
Q('ravenssupport',96,'Shall the raven passage support the reported permission?', ['Ravens brought Elijah bread and meat morning and evening','Proposed source of meat from Ahab'])
C('ravenmeals',96,'The ravens brought him bread and meat in the morning and bread and meat in the evening.','Quoted verse used in proposed support; both times and foods retained')
C('ahabbutchers',96,'The food came from Ahab’s slaughterers.','Rav’s statement transmitted by Rav Yehuda',holder='רב')
add('yehudareport','attributions',96,dict(surface='אמר רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope='Rav Yehuda reports Rav’s identification of food source; not Rav Yehuda as original authority',transmission_chain=['רב יהודה','רב']),[c['ahabbutchers']])
C('divineexception',96,'A case by divine command is different.','Rejects this incident as ordinary-law support, not denial that food came from Ahab’s slaughterers',cond=['על פי הדבור'])
Q('whatravens',97,'What are the עורבים?', ['Elijah food-bringers'])
C('literalravens',97,'They were actual ravens.','Ravina’s identification',holder='רבינא')
Q('menoravim',97,'Perhaps there were two men whose names were Orev, as the verse mentions killing Orev at the rock of Orev and Zeeb?', ['Rav Adda bar Minyomi challenges literal-bird reading','Human name Orev attested'])
add('addaspeaker','attributions',97,dict(surface='רב אדא בר מניומי',role='speaker',candidates=['רב אדא בר מניומי'],scope='Questions Ravina with human-name alternative; addressee not assigned as its holder',transmission_chain=[]),[z['menoravim']])
Q('bothnamed',97,'Would it just so happen that both men were named Oravim?', ['Reply to two-men alternative; improbable coincidence objection'])
Q('place',98,'Perhaps they were called that after their place—is there not the verse about a נערה קטנה?' , ['Alternative geographical reading of עורבים'])
C('maidenverse',98,'The quoted verse describes Aramean bands capturing a נערה קטנה from Israel.','Analogy offered for a place-derived reading')
Q('maidenlittle',98,'Why is she called both נערה and קטנה?', ['Quoted earlier interpretive difficulty used in geographical analogy'])
C('pedat',98,'She was a young girl from Naaran.','Rabbi Pedat’s interpretation: קטנה דמן נעורן; source place reading retained without new geography',holder='רבי פדת')
C('orviyim',98,'If the ravens were named for their place, the wording should be עורביים.','Answer rejecting geographic explanation on source wording')
Q('baraitasupport',99,'Shall the all-slaughter baraita support Rav Anan’s report?', ['Even Kuti, uncircumcised person and Israelite apostate included','Repeated source occurrence distinguished from earlier Rava-support use'])
C('allbaraita',99,'All slaughter, including a Kuti, an uncircumcised person and an Israelite apostate.','Repeated baraita quotation; category of apostate under dispute',holder='Anonymous all-slaughter baraita')
Q('whichuncirc',99,'What kind of uncircumcised person is meant?', ['Specific inclusion of ערל'])
C('brothers',99,'If his brothers died from circumcision, he is a fully proper Israelite.','Reason this would be an obvious inclusion rather than the intended novelty',cond=['Brothers died because of circumcision'])
C('circumcision',99,'It instead means an apostate regarding circumcision.','Clarification of first category',cond=['מומר לערלות'])
Q('whichapostate',100,'What apostate is meant in the last clause?', ['Circumcision apostate already included'])
C('singleredundant',100,'If it meant apostasy regarding one matter, that would repeat the circumcision case.','Redundancy objection')
Q('idolatryinference',100,'Must it not mean an apostate to idolatry, as in Rav Anan’s report?', ['Proposed inference from distinct final category'])
C('idolatryproposed',100,'The proposed support reads the final category as apostasy to idolatry.','Inference expressly rejected next',mode='rejected')
C('idolatryexcluded',101,'One may instead exclude the apostate to idolatry from this permission.','Answer defeating proposed support for Rav Anan')
C('idolatrysevere',101,'Idolatry is severe: anyone who denies it is like one who acknowledges the whole Torah.','Quoted reason for treating idolatry differently; exact positive formulation retained')
C('sameasrava',102,'The apostate clause instead concerns that same matter, in accordance with Rava.','Alternative baraita interpretation counters Rav Anan proof; relates to Rava appetite case, not all motives')
C('excludeapostate',103,'מכם, not all of you, excludes the apostate.','Opening of sacrificial-acceptance baraita; kind of apostate clarified below',holder='Anonymous offering baraita')
C('notnations',103,'The distinction is made among you, not among the nations.','מכם בכם חלקתי ולא באומות; preserve negative scope',holder='Anonymous offering baraita')
C('animalpeople',103,'מן הבהמה includes people resembling animals.','Derivation introducing acceptance of offerings from sinners',holder='Anonymous offering baraita')
C('acceptsinners',103,'Offerings from Israel’s sinners are accepted so that they may return in repentance.','Baraita allowance with stated purpose; exceptions follow',holder='Anonymous offering baraita',cond=['פושעי ישראל','Purpose of return in repentance'])
C('exceptionlist',103,'The stated exceptions are the apostate, one who pours wine libations, and one who publicly desecrates Shabbat.','Initial baraita list, grammatical relationship reinterpreted at5a14; preserve public qualification',holder='Anonymous offering baraita',cond=['Listed exception categories, not cumulative prerequisites'])
Q('internalcontradiction',104,'How can the baraita first exclude the apostate and then accept offerings from Israel’s sinners?', ['Apparent internal contradiction'])
C('headalltorah',105,'The first clause concerns an apostate to the whole Torah.','Answer distinguishing scope of initial exclusion',cond=['Whole-Torah apostasy'])
C('middleone',105,'The middle clause concerns an apostate in one matter.','Answer distinguishing scope of accepted sinners',cond=['One-matter apostasy'])
Q('lastapostate',106,'What kind of apostate does the final exception mean?', ['Earlier whole-Torah exclusion and one-matter acceptance distinguished'])
Q('wholeduplicate',106,'If the final exception means the whole Torah, does that not repeat the opening clause?', ['Whole-Torah reading of final apostate exception'])
Q('onecontradiction',106,'If it means one matter, does that not contradict the middle clause?', ['One-matter reading of final exception'])
C('finalexception',107,'The final clause means: except an apostate to wine libation or to public Shabbat desecration.','Revised parsing of exception list; preserves publicly qualification, does not silently delete either listed practice',cond=['Wine libation or public Shabbat desecration; alternative exception categories'])
C('idolatryall',107,'It follows that an apostate to idolatry is an apostate to the whole Torah.','Conclusion drawn from the offering baraita against Rav Anan’s report',cond=['Apostasy to idolatry'])
C('refuted',107,'Rav Anan’s report is explicitly refuted: תיובתא דרב ענן תיובתא.','Final target is Rav Anan’s report of permission for idolatry apostate slaughter; not a retraction by Rav Anan, and not refutation of Rava’s appetite-based rule')
Q('reinterpretation',107,'Must the final clause not instead mean an apostate to the specified wine-libation or public-Shabbat violations?', ['Neither whole-Torah repetition nor isolated one-matter reading fits the baraita'])
rels=[(92,'righteousservants','ch.s2710.q.yehoshapatnot','answer'),(92,'righteousservants','ch.s2710.splitservants','objection'),(92,'righteousservants','ch.s2710.splitking','objection'),(93,'separatefood','ch.s2710.mealexample','objection'),(94,'notseparate','separatefood','answer'),(94,'firstverse','notsource','answer'),(94,'horses','firstverse','objection'),(94,'horsefate','horses','answer'),(94,'peoplefate','firstverse','objection'),(95,'secondverse','notsource','answer'),(95,'secondverse','firstverse','correction'),(95,'likegoren','goren','answer'),(95,'likegoren','literalfloor','answer'),(95,'sanhedrinshape','likegoren','support'),(95,'seeeachother','sanhedrinshape','support'),(96,'ahabbutchers','ravenssupport','support'),(96,'divineexception','ravenssupport','answer'),(97,'literalravens','whatravens','answer'),(97,'menoravim','literalravens','objection'),(97,'bothnamed','menoravim','objection'),(98,'place','literalravens','objection'),(98,'pedat','maidenlittle','answer'),(98,'pedat','place','support'),(98,'orviyim','place','answer'),(99,'circumcision','whichuncirc','answer'),(100,'singleredundant','whichapostate','qualification'),(100,'idolatryproposed','idolatryinference','answer'),(100,'idolatryproposed','baraitasupport','answer'),(101,'idolatryexcluded','idolatryproposed','objection'),(101,'idolatrysevere','idolatryexcluded','support'),(102,'sameasrava','whichapostate','answer'),(102,'sameasrava','idolatryproposed','correction'),(103,'animalpeople','acceptsinners','support'),(105,'headalltorah','internalcontradiction','answer'),(105,'middleone','internalcontradiction','answer'),(105,'headalltorah','excludeapostate','qualification'),(105,'middleone','acceptsinners','qualification'),(107,'finalexception','reinterpretation','answer'),(107,'finalexception','lastapostate','answer'),(107,'finalexception','exceptionlist','correction'),(107,'finalexception','idolatryall','support'),(107,'idolatryall','refuted','support'),(107,'refuted','ch.s2710.shmuelcited','local_resolution'),(107,'refuted','ch.s2710.shmuelresumed','local_resolution')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={92:'Explicit answer to prior endpoint: truth-listening ruler has righteous servants; rejects proposed unreliable Jehoshaphat servants.',93:'Separate royal groups’ slaughter and meals posed as alternative, not historical assertion.',94:'Nonseparation reply, source question, initial personal/people identity verse, horse counter-question and shared-fate interpretations distinguish failed proof from claim.',95:'Replacement enthroned-kings verse, what-goren and literal-floor questions, semicircle comparison and see-each-other purpose all retained.',96:'Raven proof question; morning/evening bread/meat; Rav Yehuda reports Rav distinctly; divine-command exception blocks ordinary-law inference.',97:'What-ravens question, Ravina actual birds, Rav Adda bar Minyomi human-name question and coincidence counter-question.',98:'Geographical hypothesis with נערה קטנה analogy, quoted contradiction, Rabbi Pedat’s Naaran interpretation and required עורביים wording reply.',99:'Repeated all-slaughter support occurrence preserved; uncircumcised question, brothers-death obvious case and circumcision apostasy distinguished.',100:'Final apostate identity question, one-matter redundancy and idolatry inference posed as proposed support for Rav Anan.',101:'Counter-reading excludes idolatry; quoted severity uses denial-of-idolatry like accepting-all-Torah formulation, no polarity reversal.',102:'Same-matter Rava reading answers proof; does not infer a universal permission for every motive.',103:'Full offering baraita: exclude apostate, distinction only among you not nations, beast-like people inclusion, repentance purpose and all listed exceptions including public Shabbat.',104:'Internal contradiction between excluded apostate and accepted sinners explicitly questioned.',105:'Whole-Torah opening exclusion versus one-matter middle acceptance resolves first contradiction only.',106:'Final exception identity, whole-Torah redundancy and one-matter contradiction separately questioned.',107:'Reparsing question answered with wine-libation/public-Shabbat apostate categories; idolatry-all-Torah inference; explicit Rav Anan report refutation linked to both prior occurrences. Context5a15–5b6 read: later source distinction sin-offering/burnt-offering and beast-versus-human-and-beast limitations are not covered here; prior claims preserved.'}
for i in range(92,108):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous proof testing with named speech and reports separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara framing',role='anonymous',candidates=[],scope='Connective argument only; named source authorities and transmitters separately retained',transmission_chain=[]))
COV=[]
for i in range(92,108):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s1])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_4b18_5a14_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=16,sha256=hashlib.sha256(b).hexdigest())))
