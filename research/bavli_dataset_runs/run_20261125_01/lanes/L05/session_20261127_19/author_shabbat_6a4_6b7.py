"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shabbat')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='b77690862170d571563691364a79174be99fecf98cb41fad07490fa23bad5676';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shabbat','epoch':2}
assert I[99]['ref']=='Shabbat 6a:4' and I[118]['ref']=='Shabbat 6b:7'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='sha.s2719.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('stoaend','structure',range(99,104),dict(title='Stoa comparison refined to public-domain sides, protective barriers and Ben Azzai throwing exception',primary=True,boundary='closed',legacy_ids=[]))
s2=add('domainbaraita','structure',range(104,111),dict(title='Four Shabbat domains: definitions, transfer liabilities, eruv and threshold alternatives',primary=True,boundary='closed',legacy_ids=[]))
s3=add('domainanalysis','structure',range(111,119),dict(title='Exclusive domain formulas, desert conditions and deliberate-transfer liability; Issi wording corrected in continuation',primary=True,boundary='open_right',legacy_ids=[]))
priorstoa=next(r for r in S['records'] if r['id']=='sha.s2712.stoa');closedstoa={k:json.loads(json.dumps(v)) for k,v in priorstoa.items() if k not in ['review_state','release_state','ml_eligible','supersedes']};closedstoa['id']='sha.s2712.stoa.s19closed';closedstoa['supersedes']=priorstoa['id'];closedstoa['content']['boundary']='closed';closedstoa['content']['title']+='; analogy challenges and Ben Azzai exception completed in6a4–8';R.append(closedstoa)
e('stoacontinuation',99,closedstoa['id'],s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('same',99,'Are these comparable?', ['Prior four-cubit public-domain analogy for passing through stoa'])
C('relativeexemption',99,'There the place is exempt only relative to this person; for everyone generally it is a place of liability.','Objection to prior four-cubit-distance analogy')
C('universalexemption',99,'Here the stoa is a place of exemption for everyone.','Distinction showing prior analogy inadequate, not permission for all transfers')
C('sidesanalogy',100,'Rather compare one who transfers from private to public domain via the sides of the public domain.','Replacement analogy after rejected earlier comparisons')
C('sidesrest',100,'If he sets it down at the sides of the public domain, he is exempt.','Premise of replacement analogy, challenged under Eliezer view next',cond=['Object set down at public-domain sides'])
C('publicrest',100,'If he sets it down in the public domain, he is liable.','Analogy final endpoint',cond=['Transfer from private domain','Passes through sides','Sets down in public domain'])
C('stoalikewise',100,'The stoa-transfer case is likewise.','Analogy conclusion subject to side-domain qualification next')
Q('eliezerviewquestion',101,'This works for the sages who say the sides are not public domain; what can be said for Rabbi Eliezer (ben Yaakov), who treats them as public domain?', ['Replacement public-side analogy','Different tannaitic classifications'])
C('sagessides',101,'The sages regard the sides of the public domain as not equivalent to public domain.','Position invoked by Rav Pappa objection',holder='רבנן')
C('eliezersides',101,'Rabbi Eliezer (ben Yaakov) regards the sides as public domain.','View as introduced in objection; next reply limits understood evidence',holder='רבי אליעזר (בן יעקב)',unc=['Parenthetical בן יעקב preserved exactly as source identification variant.'])
add('pappaask','attributions',101,dict(surface='מתקיף לה רב פפא',role='speaker',candidates=['רב פפא'],scope='Objects under Eliezer view, not holder of that tannaitic view',transmission_chain=[]),[z['eliezerviewquestion']])
C('withoutbarriers',102,'The heard Eliezer ruling concerns a place without חיפופי.','Rav Aha son of Rav Ika limits report scope',cond=['No חיפופי'],holder='רב אחא בריה דרב איקא')
Q('withbarriers',102,'Have you heard him say this where there are חיפופי?', ['Eliezer view','Sides with protective barriers/posts'])
C('validanalogy',102,'Therefore the stoa case is analogous to this side-domain case.','Rav Aha resolution using barrier-qualified sides, no assertion all sides exempt',cond=['Sides with חיפופי'],holder='רב אחא בריה דרב איקא')
add('ahaask','attributions',102,dict(surface='א״ל רב אחא בריה דרב איקא ... מי שמעת ליה',role='speaker',candidates=['רב אחא בריה דרב איקא'],scope='Reply to Rav Pappa and scope question',transmission_chain=[]),[z['withbarriers']])
C('benazzaithrow',103,'Ben Azzai concedes in the throwing case.','Rabbi Yohanan report, supported by baraita',cond=['Throwing between shop and plaza through stoa'],holder='בן עזאי')
add('yohananreport','attributions',103,dict(surface='א״ר יוחנן ומודה בן עזאי בזורק',role='transmitter',candidates=['רבי יוחנן'],scope='Reports Ben Azzai concession, not a new attribution of all following baraita to Yohanan',transmission_chain=[]),[c['benazzaithrow']])
for k,act in [('taking','taking out'),('bringing','bringing in'),('throwing','throwing'),('handing','handing across')]:
 C('first_'+k,103,'The first baraita view imposes liability for '+act+'.','Shop/plaza through stoa, explicit four operations',cond=['Between shop and plaza through stoa',act],holder='First baraita view')
for k,act in [('taking','taking out'),('bringing','bringing in')]:C('ben_'+k,103,'Ben Azzai exempts '+act+'.','Exemption for walking transfer; not necessarily permission',cond=['Between shop and plaza through stoa',act],holder='בן עזאי')
for k,act in [('throwing','throwing'),('handing','handing across')]:C('ben_'+k,103,'Ben Azzai imposes liability for '+act+'.','Separate explicit liable operations',cond=['Between shop and plaza through stoa',act],holder='בן עזאי')
C('fourdomains',104,'There are four Shabbat domains: private, public, karmelit and exempt place.','Baraita classification; all four names retained')
Q('whichprivate',105,'What is private domain?', ['Four-domain baraita classification'])
C('trench',105,'A trench ten deep and four wide is complete private domain.','Dimensions stated by baraita',cond=['Depth ten','Width four'])
C('wall',105,'A wall ten high and four wide is complete private domain.','Separate raised case',cond=['Height ten','Width four'])
Q('whichpublic',106,'What is public domain?', ['Four-domain baraita classification'])
C('publicexamples',106,'A highway, large plaza and through-going alleys are complete public domain.','Three named examples retained')
C('noout',106,'One may not take out from this private domain to this public domain.','Prohibition, not merely liability after act',cond=['Private to public'])
C('noin',106,'One may not bring in from this public domain to this private domain.','Reverse direction prohibition',cond=['Public to private'])
C('inadvertentsin',106,'Inadvertent taking out or bringing in incurs a sin offering.','Stated sanction',cond=['Stated interdomain transfer','Inadvertent'])
C('deliberatekaret',106,'Deliberate transfer incurs karet.','Baraita stated punishment; not claim karet and execution are administered cumulatively in one adjudicated circumstance',cond=['Stated interdomain transfer','Deliberate'])
C('deliberatestone',106,'The baraita also states stoning for deliberate transfer.','Legal liability statement; detailed adjudication conditions are not supplied in this line',cond=['Stated interdomain transfer','Deliberate'])
C('middleplaces',107,'Sea, open valley, colonnade and karmelit are neither public nor private domain in this classification.','Later6b10–7a2 qualifies valley language; no denial of every sense of private-domain terminology')
C('nowithin',107,'One may not carry within them.','Baraita prohibition; source excerpt does not restate distance here',cond=['Within listed intermediate domains'])
C('withinexempt',107,'If one carries within them, one is exempt.','Exempt despite preceding prohibition; not permitted',cond=['Carrying performed within listed domains'])
for k,direction in [('outpublic','from them to public domain'),('inpublic','from public domain into them'),('inprivate','from private domain into them'),('outprivate','from them to private domain')]:
 C(k,107,'One may not transfer '+direction+'.','Explicit four-direction restrictions',cond=[direction])
C('transferexempt',107,'If one takes out or brings in in those cases, one is exempt.','Liability exemption does not override prohibition',cond=['Transfer involving listed intermediate domains'])
C('eruvpermitted',108,'Shared courtyards and non-through alleys are permitted when an eruv was made.','Conditional permission',cond=['Shared courtyards or non-through alleys','Eruv made'])
C('noeruvforbidden',108,'Without an eruv, they are forbidden.','Opposite condition',cond=['Same courtyards or alleys','No eruv'])
C('thresholdowner',109,'A person standing on the threshold may take from the householder and give back to him.','Threshold baraita first view; later discussion determines its type',cond=['Person stands on threshold','Exchange with householder'])
C('thresholdpoor',109,'He may take from the poor person and give back to him.','Separate side',cond=['Person stands on threshold','Exchange with poor person'])
C('nocrossowner',109,'He must not take from the householder and give to the poor person.','Cross-domain relay restriction',cond=['Threshold intermediary','Householder to poor person'])
C('nocrosspoor',109,'He must not take from the poor person and give to the householder.','Reverse relay restriction',cond=['Threshold intermediary','Poor person to householder'])
C('threeexempt',109,'If he did take and give, all three are exempt.','Explicit all-three liability outcome despite prohibition',cond=['Forbidden cross relay performed'])
C('thresholdtwo',110,'Others say a threshold serves two domains.','Alternative view, not anonymously merged with preceding view',holder='אחרים')
C('dooropen',110,'When the door is open, it is like the inside.','Others conditional classification',cond=['Door open'],holder='אחרים')
C('doorclosed',110,'When the door is shut, it is like the outside.','Others opposite condition',cond=['Door shut'],holder='אחרים')
C('thresholdindependent',110,'If the threshold is ten high and four wide, it is a domain of its own.','Independent threshold dimensions rule',cond=['Height ten','Width four'],holder='אחרים')
Q('privateexclude',111,'What does this is private domain exclude?', ['Restrictive formula in baraita'])
C('excludejudah',[111,112],'It excludes Rabbi Yehuda’s rule concerning two houses on opposite sides of public domain.','Quoted alternative spans folio; full evidence included')
C('judahposts',[111,112],'One with two houses on opposite sides of public domain may make a sidepost on each side and carry between them.','Rabbi Yehuda first remedy',cond=['Two houses on opposite sides','Sidepost on each side'],holder='רבי יהודה')
C('judahbeams',[111,112],'Alternatively he may put a crossbeam on each side and carry between them.','Rabbi Yehuda second remedy, not cumulative with sideposts',cond=['Two opposite houses','Crossbeam on each side'],holder='רבי יהודה')
C('sagesreject',112,'They said to him that public domain cannot be made permitted by an eruv in that manner.','Sages reject Yehuda enclosure procedure',cond=['Stated two-house sidepost/crossbeam arrangement'],holder='חכמים')
Q('completeprivate',113,'Why call it complete?', ['Private-domain description'])
C('throwconcession',113,'One might think the sages disagree only for carrying but concede to Yehuda for throwing.','Rejected possible distinction',cond=['Yehuda two-house arrangement'],mode='hypothetical')
C('nothrowconcession',113,'The complete designation teaches that they do not concede even for throwing.','Answer rejects hypothetical Torah-private-domain concession',cond=['Yehuda arrangement','Throwing'])
Q('publicexclude',114,'What does this is public domain exclude?', ['Public-domain restrictive formula'])
C('excludeotherjudah',114,'It excludes the other Rabbi Yehuda rule cited next.','Different rule from two-house arrangement')
C('roaddivert',114,'Rabbi Yehuda says that if a public road interrupts them, it must be diverted to the sides.','Quoted Mishnah; referent of מפסקתן not restated here, do not fabricate full enclosure description',cond=['Public road interrupts the referenced arrangement'],holder='רבי יהודה',unc=['Antecedent of מפסקתן not explicitly supplied in this excerpt.'])
C('noneeddivert',114,'The sages say this is unnecessary.','Opposition to road diversion',cond=['Same road-through arrangement'],holder='חכמים')
Q('completepublic',115,'Why call it complete?', ['Public-domain description'])
C('parallelword',115,'Because the first clause used complete, the later clause also uses complete.','Stylistic explanation, not additional new public-domain exclusion')
Q('desert',116,'Why not also count the wilderness?', ['Current list omits it','Another baraita includes it with highway/plaza/through alleys'])
C('desertbaraita',116,'The other baraita also lists the wilderness as public domain.','Apparent list discrepancy, resolved temporally next')
C('desertisrael',116,'The wilderness listing applies when Israel were dwelling in the wilderness.','Abaye first temporal branch',cond=['Israel dwelling in wilderness'],holder='אביי')
C('desertnow',116,'The other list concerns the present time.','Abaye second branch explains omission; not a universal domain claim regardless use',cond=['Present time, unlike Israel encampment'],holder='אביי')
Q('sinobvious',117,'Is inadvertent liability for a sin offering not obvious?', ['Quoted transfer sanction'])
C('deliberateneeded',117,'The deliberate karet and stoning clause was needed.','Initial answer points to next challenge')
Q('deliberateobvious',118,'Is that not also obvious?', ['Deliberate-transfer punishment clause'])
C('scrollfound',118,'Rav said he found a hidden scroll in Rabbi Hiyya’s house.','Report source, not assertion Rabbi Hiyya authored the written view',holder='רב')
C('issithirtynine',118,'Issi ben Yehuda says the principal labors are forty less one.','Scroll quotation as reported by Rav',holder='איסי בן יהודה')
C('issionlyone',118,'The initial wording says he is liable only for one.','Provisional scroll wording explicitly challenged and reformulated6b8–9; do not release as final single-offering rule',holder='איסי בן יהודה',mode='challenged')
C('issirevised',[118,119,120],'Rather read that he is not liable for one of them.','Explicit אלא אימא revision of initial wording; context concerns deliberate capital liability, not blanket denial of separate sin offerings',holder='איסי בן יהודה',mode='reconciled')
C('transfercertain',[118,120],'The teaching tells us this transfer is among those about which there is no doubt.','Final contextual answer for need to state deliberate liability, complete continuation preserved')
add('scrollreport','attributions',118,dict(surface='כדרב דא״ר מצאתי מגלת סתרים בי רבי חייא וכתוב בה איסי בן יהודה אומר',role='transmitter',candidates=['רב'],scope='Rav reports a written Issi teaching found at Hiyya house; not invented Hiyya-to-Rav oral chain',transmission_chain=[]),[c['issithirtynine'],c['issionlyone']])
rels=[(99,'relativeexemption','same','support'),(99,'universalexemption','same','support'),(100,'sidesanalogy','same','answer'),(100,'sidesrest','sidesanalogy','support'),(100,'publicrest','stoalikewise','support'),(101,'eliezerviewquestion','sidesanalogy','objection'),(101,'eliezersides','eliezerviewquestion','support'),(102,'withoutbarriers','eliezerviewquestion','answer'),(102,'withbarriers','eliezersides','qualification'),(102,'validanalogy','eliezerviewquestion','answer'),(103,'ben_throwing','benazzaithrow','support'),(105,'trench','whichprivate','answer'),(105,'wall','whichprivate','answer'),(106,'publicexamples','whichpublic','answer'),(107,'withinexempt','nowithin','qualification'),(107,'transferexempt','outpublic','qualification'),(107,'transferexempt','inpublic','qualification'),(107,'transferexempt','inprivate','qualification'),(107,'transferexempt','outprivate','qualification'),(109,'threeexempt','nocrossowner','qualification'),(109,'threeexempt','nocrosspoor','qualification'),(110,'dooropen','thresholdtwo','qualification'),(110,'doorclosed','thresholdtwo','qualification'),([111,112],'excludejudah','privateexclude','answer'),(112,'sagesreject','judahposts','objection'),(112,'sagesreject','judahbeams','objection'),(113,'nothrowconcession','throwconcession','correction'),(113,'nothrowconcession','completeprivate','answer'),(114,'excludeotherjudah','publicexclude','answer'),(114,'noneeddivert','roaddivert','objection'),(115,'parallelword','completepublic','answer'),(116,'desertbaraita','desert','support'),(116,'desertisrael','desert','answer'),(116,'desertnow','desert','answer'),(117,'deliberateneeded','sinobvious','answer'),(118,'deliberateobvious','deliberateneeded','objection'),([118,119,120],'issirevised','issionlyone','correction'),([118,120],'transfercertain','deliberateobvious','answer'),([118,120],'transfercertain','deliberatestone','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={99:'Is-it-comparable question rejects prior4cubit analogy: exemption person-relative versus stoa universal; no invented public-domain permission.',100:'Replacement via public-domain sides with exempt intermediate resting versus liable final public resting, analogous stoa result; next tanna objection retained.',101:'Rav Pappa distinguishes sages and Eliezer sides classification; source parenthetical benYaakov identification preserved, not silently resolved.',102:'Aha son of Rav Ika limits heard Eliezer view to no חיפופי and asks whether heard with barriers; valid analogy scoped accordingly.',103:'Yohanan Ben Azzai throwing concession; all four first-tanna liable acts and Ben Azzai two exempt/two liable acts separated. Stoa source discussion closes here; original structure explicitly superseded closed, evidence unchanged.',104:'All four domain names and count retained; no invented fifth category.',105:'Definition question, trench depth10width4 and wall height10width4 separate, complete designation retained.',106:'Public definition question and3examples; both transfer-direction prohibitions, inadvertent sin offering versus deliberate karet/stoning liability; no invented cumulative execution scenario.',107:'Sea/valley/colonnade/karmelit neither domain classification, internal prohibition yet exemption, four transfer directions prohibited yet exempt.6b10–7a2 context read for valley qualifications, not forced into simple universal identity.',108:'Shared courtyards/nonthroughalleys permitted only with eruv, forbidden otherwise.',109:'Threshold person same-side exchanges with householder/poor versus both prohibited cross relays; allthree exempt does not mean permitted.',110:'Others alternative threshold view, dooropen inside/closed outside, height10width4 independent domain; no merged first-tanna attribution.',111:'Private-domain exclusion question and Yehuda twohouses opposite public domain quotation continues6b1; full split evidence.',112:'Yehuda sideposts OR crossbeams and carry-between permission, sages no public-domain-eruv-by-this answer retained.',113:'Why complete question; provisional sages-carrying-only disagreement/throwing concession rejected by baraita, not final stance.',114:'Public-domain exclusion question and different Yehuda road-diversion rule versus sages unnecessary; unstated מפסקתן antecedent flagged rather than invented.',115:'Why complete public question answered stylistic parallel, not an additional legal exclusion.',116:'Desert-omission question; other baraita listsdesert, Abaye Israel-encampment versus present temporal conditions preserved.',117:'Why state obvious inadvertent sin offering query; deliberate clause initial answer challenged next.',118:'Deliberate obvious question; Rav found written scroll in Hiyya house, Issi39labors and initial only-one wording. Full6b8–9 continuation included in explicit correction to not-liable-for-one and transfer-not-doubtful conclusion. No final false single-sin-offering rule; context evidence not new core coverage.'}
for i in range(99,119):
 add('u'+str(i),'utterances',i,dict(textual_voice='Quoted baraita, named reports and anonymous analysis separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only; named holders/reporters preserved separately',transmission_chain=[]))
COV=[]
for i in range(99,119):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
for priorcov in S['coverage']:
 if priorstoa['id'] in priorcov['record_ids']:
  cv={k:json.loads(json.dumps(v)) for k,v in priorcov.items() if k!='proposal_execution'};cv['record_ids']=[closedstoa['id'] if v==priorstoa['id'] else v for v in cv['record_ids']];cv['rationale']+=' Session19 completes stoa argument6a4–8; explicit closed successor preserves original source partition.';COV.append(cv)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shabbat',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=[v for v in S['open_tails'] if v!=priorstoa['id']]+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shabbat_6a4_6b7_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
