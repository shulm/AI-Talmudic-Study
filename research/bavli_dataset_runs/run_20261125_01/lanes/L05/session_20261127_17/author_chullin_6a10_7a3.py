"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='dfadd95de7eb330fbb8af1fc0814ed10f4af0fbda367c524e602ffe2f6a2db41';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[128]['ref']=='Chullin 6a:10' and I[147]['ref']=='Chullin 7a:3'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2717.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('domains','structure',range(128,130),dict(title='Domain-right procedures and rental distinction',primary=True,boundary='closed',legacy_ids=[]))
s2=add('mixtures','structure',range(130,142),dict(title='Demai mixtures, deliberate preparation, flavorings and substitution objections',primary=True,boundary='closed',legacy_ids=[]))
s3=add('beitshean','structure',range(142,148),dict(title='Beit Shean testimony and Rabbi ruling, ancestral precedent and three scholarly-response variants',primary=True,boundary='open_right',legacy_ids=[]))
e('domaincontinuation',128,'ch.s2716.decrees',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
C('israelgive',128,'An Israelite may give domain rights.','Baraita explanation of preceding public-Shabbat observance distinction',cond=['Israelite domain-right procedure'])
C('israelrenounce',128,'An Israelite may relinquish domain rights.','Separate procedural alternative',cond=['Israelite domain-right procedure'])
C('gentilerental',128,'For a gentile, rental is required.','עד שישכור: earlier giving/relinquishing procedures do not replace rental',cond=['Gentile domain rights'])
Q('howdomain',129,'How is this accomplished?', ['Giving/relinquishing an Israelite’s domain rights'])
C('givenformula',129,'Saying רשותי קנויה לך effects acquisition of the domain right.','First verbal formula',cond=['Israelite giving rights','Says רשותי קנויה לך'])
C('nullformula',129,'Saying רשותי מבוטלת לך effects the stated domain-right result.','Second formula retained as relinquishment, not physical title transfer to land',cond=['Israelite relinquishing rights','Says רשותי מבוטלת לך'])
C('noformal',129,'There is no need for an additional act of conferring acquisition: ואינו צריך לזכות.','Negative procedural requirement following formulas; avoid importing mechanism not stated',cond=['Said either stated formula'])
C('innvisit',130,'Rabbi Zeira and Rav Asi came to the inn of Yai and were served eggs reduced in wine.','Narrative setting; source reads רב אסי, not Rav himself')
C('zeiranoeat',130,'Rabbi Zeira did not eat.','Conduct in wine-egg episode')
C('asieat',130,'Rav Asi ate.','Contrasting conduct; reason discussed, not inferred blanket legal stance')
Q('demaimix',130,'Do you not worry about a mixture containing demai?', ['Rabbi Zeira addresses Rav Asi','Eggs reduced in wine'])
C('notconsidered',130,'It was not on my mind.','Rav Asi answer לאו אדעתאי; not a deliberate denial of concern',holder='רב אסי')
add('zeiraask','attributions',130,dict(surface='א״ל רבי זירא לרב אסי',role='speaker',candidates=['רבי זירא'],scope='Questions Rav Asi after contrasting conduct',transmission_chain=[]),[z['demaimix']])
Q('possibledecree',131,'Could there have been a decree on demai mixtures, yet Rav Asi have come to eat forbidden food?', ['Hypothesized mixture prohibition','Observed eating by Rav Asi'])
Q('righteousmore',131,'If even animals of the righteous are protected, how much more the righteous themselves?', ['Premise of divine prevention of mishaps','Potential forbidden consumption'])
C('animalprotection',131,'The Holy One does not bring a mishap through animals of the righteous.','Rabbi Zeira argument premise, not independently verified universal immunity',holder='רבי זירא')
C('humaninference',131,'All the more so for the righteous themselves.','A fortiori argument challenges hypothesized mixture decree',holder='רבי זירא')
C('investigated',132,'Rabbi Zeira investigated and found the following Mishnah.','Actual textual search, distinct from preceding inference')
C('winebrine',132,'One buying wine to put into fish brine must account for demai.','Purchased ingredient destined for mixing, not purchased finished mixture',cond=['Buys wine to add to מורייס'])
C('winedrink',132,'One buying wine to put into aluntit must account for demai.','Second wine-mixture destination',cond=['Buys wine to add to אלונתית'])
C('vetch',132,'One buying vetch to make ground material must account for demai.','Third ingredient-preparation case',cond=['Buys כרשינין to make טחינין'])
C('lentils',132,'One buying lentils to make crushed material must account for demai.','Fourth ingredient-preparation case',cond=['Buys lentils to make רסיסין'])
C('certain',132,'Certainly this applies when the produce is definitely untithed.','אין צריך לומר משום ודאי explicitly stronger obligation',cond=['Any listed bought ingredient','Definitely untithed'])
C('finishedmixtures',[132,133],'The finished mixtures themselves are permitted because they are mixtures.','Contrast with buying ingredients to prepare them; applies to demai, not definite untithed produce blanket exemption',cond=['Finished mixtures themselves','Demai context'])
Q('nomixdecree',134,'Was there no decree on demai mixtures?', ['Finished-mixture permission','Neighbor food-preparation baraita follows'])
C('neighborseventh',134,'One giving a neighbor dough to bake or a pot to cook need not worry about seventh-year produce in her leaven and spices.','Initial baraita case, before explicit request to use her ingredients',cond=['Gives own dough/pot for preparation','No instruction עשי לי משליכי'])
C('neighbortithe',134,'In that case one need not worry about tithing of the leaven and spices.','Separate negative concern',cond=['Gives own dough/pot for preparation','No instruction to use her ingredients'])
C('requestseventh',135,'If he asks her to make it from her own, he must worry about seventh-year status of the leaven and spices.','Baraita conditional exception',cond=['Says עשי לי משליכי'])
C('requesttithe',135,'If he asks her to use her own, he must worry about tithing of the leaven and spices.','Conditional exception creates demai-mixture challenge',cond=['Says עשי לי משליכי'])
C('deliberatemix',136,'There it is different: requesting her ingredients is like mixing them by hand.','Anonymous distinction; purchase of finished mixture not equated with intentional mixing',cond=['Explicit request to use her ingredients'])
C('flavorpurpose',136,'Leaven and spices differ because they are added for flavor.','Rafram alternative distinction',cond=['Leaven or spices added for flavor'],holder='רפרם')
C('flavornotnull',136,'Flavor is not nullified.','Rafram stated reason, local flavoring context',cond=['Ingredient added for flavor'],holder='רפרם')
Q('motherreplace',137,'Are we not concerned about substitution?', ['Neighbor preparation case','Mother-in-law Mishnah requires tithing both directions'])
C('mothergive',137,'One giving food to his mother-in-law tithes what he gives her.','Quoted Mishnah',cond=['Food given to mother-in-law'])
C('motherreceive',137,'He also tithes what he receives from her.','Return obligation distinct from initial outgoing tithing',cond=['Food returned by mother-in-law'])
C('mothersuspect',137,'She is suspected of replacing what has spoiled.','Specified substitution suspicion, not all women generalized')
C('motherdaughter',137,'She wants her daughter’s well-being.','Rabbi Yehuda reason distinguishing mother-in-law',holder='רבי יהודה')
C('motherashamed',137,'She is ashamed before her son-in-law.','Second stated motivation in Rabbi Yehuda explanation',holder='רבי יהודה')
Q('generalreplace',138,'Are we not concerned about substitution with people generally?', ['Mother-in-law distinction','Innkeeper Mishnah'])
C('inngive',138,'One giving food to his innkeeper tithes what he gives her.','Quoted Mishnah first obligation',cond=['Food given to innkeeper'])
C('innreceive',138,'He also tithes what he receives from her.','Return obligation',cond=['Food returned by innkeeper'])
C('innsuspect',138,'She is suspected of substitution.','Reason stated by Mishnah')
C('innrationale',138,'She rationalizes: let the scholar eat warm food while I eat cold.','Answer distinguishes innkeeper by attributed rationalization; not annotator speculation about motives')
Q('grindingreplace',139,'Are we not concerned about substitution?', ['Another challenge after special mother-in-law and innkeeper explanations','Grinding-companions baraita'])
C('impuregrind',139,'The wife of a haver may grind with the wife of an am haaretz when she is impure.','Quoted baraita first view; source pronoun retained without assigning an uncertain antecedent',cond=['Grinding companionship','בזמן שהיא טמאה'],unc=['The excerpt does not explicitly repeat whose impurity status the pronoun specifies.'])
C('purenogrind',139,'But she may not do so when she is pure.','Negative complementary branch',cond=['Grinding companionship','בזמן שהיא טהורה'],unc=['Pronoun antecedent retained as source wording, not forced.'])
C('shimonno',140,'Even when she is impure she must not grind.','Rabbi Shimon ben Elazar stricter alternative',cond=['Grinding companionship','Even in stated impure condition'],holder='רבי שמעון בן אלעזר')
C('givesandeats',140,'Her companion gives her food and she eats.','Rabbi Shimon ben Elazar reason; role pronouns preserved',holder='רבי שמעון בן אלעזר')
Q('stealthenswap',141,'If she even steals, is substitution not all the more a concern?', ['Giving companion food treated as unauthorized taking','Prior absence of general substitution suspicion'])
C('oxrationale',141,'There too she rationalizes: an ox eats from its threshing.','Rav Yosef answer treats this as a special rationalization for giving food during labor, not a general license to steal',holder='רב יוסף')
C('testimony',142,'Rabbi Yehoshua ben Zeruz testified before Rabbi that Rabbi Meir ate a vegetable leaf in Beit Shean.','Named eyewitness report; later7a7–9 tests leaf/bundle, oversight and tithing alternatives')
C('kinship',142,'Yehoshua ben Zeruz was the son of Rabbi Meir’s father-in-law.','Explicit בן חמיו kinship; not confused with son-in-law of Rabbi Meir')
C('permittedbeit',142,'Rabbi permitted all Beit Shean on the strength of that testimony.','Tithing context; scope/legal basis challenged and clarified7a4–9, not universal exemption from all commandments',holder='רבי')
add('yehoshuawitness','attributions',142,dict(surface='העיד רבי יהושע בן זרוז ... לפני רבי על ר״מ',role='transmitter',candidates=['רבי יהושע בן זרוז'],scope='Reports Rabbi Meir conduct to Rabbi; Rabbi issues resulting ruling, Meir not attributed an explicit spoken ruling here',transmission_chain=[]),[c['testimony']])
Q('ancestors',143,'Will you permit a place where your fathers and forefathers practiced prohibition?', ['Rabbi’s Beit Shean ruling','Brothers and paternal household challenge'])
add('familyquestion','attributions',143,dict(surface='אחיו ובית אביו אמרו לו',role='collective',candidates=['אחיו ובית אביו של רבי'],scope='Family challenge addresses Rabbi',transmission_chain=[]),[z['ancestors']])
C('bronzeverse',144,'The verse recounts crushing the bronze serpent made by Moses, because Israel had burned incense to it until then, and calling it Nehushtan.','Rabbi cites2Kings18:4 in reply; full quotation retained')
Q('asaleft',144,'Could Asa have come and not removed it?', ['Bronze serpent remained for later destruction','Earlier removal of idolatry'])
Q('jehoshaphatleft',144,'Could Jehoshaphat have come and not removed it?', ['Same ancestral-precedent argument'])
Q('removedidols',144,'Did Asa and Jehoshaphat not remove all idolatry?', ['Apparently retained bronze serpent','Earlier reformers'])
C('ancestorsleft',145,'His ancestors left him room to distinguish himself.','Rabbi explanation for later bronze-serpent reform despite earlier reformers',holder='רבי')
C('myleft',145,'Likewise my ancestors left me room to distinguish myself.','Rabbi applies precedent to his own Beit Shean ruling; no accusation of deliberate forbidden action by ancestors',holder='רבי')
C('nozichin',146,'From here: a scholar who states a halakhic teaching is not מזיחין אותו.','First wording; displacement/removal sense linked to breastplate verse next; not proof any novel ruling is automatically correct',cond=['Scholar states a halakhic teaching'])
C('nozanichin',146,'An alternative wording says אין מזניחין אותו.','Second version, retained separately; rejection/abandonment root supported next',cond=['Scholar states a halakhic teaching'])
C('nozachichin',146,'Another alternative wording says אין מזחיחין אותו.','Third version tied to haughtiness-language Mishnah next; no silently merged wording',cond=['Scholar states a halakhic teaching'])
C('breastplate',147,'The מזיחין wording is supported by ולא יזח החשן.','Lexical proof for first variant, not legal derivation about Beit Shean')
C('notforsake',147,'The מזניחין wording is supported by כי לא יזנח לעולם ה׳.','Lexical proof for second variant')
C('haughty',147,'The מזחיחין wording is supported by the Mishnah: when the haughty-hearted increased, disputes increased in Israel.','Lexical proof for third version, with increased-disputes consequence retained')
add('zeiraargument','attributions',131,dict(surface='א״ר זירא',role='speaker',candidates=['רבי זירא'],scope='Conditional decree question and righteous-animal a fortiori',transmission_chain=[]),[z['possibledecree'],z['righteousmore']])
add('rabbibronze','attributions',[144,145],dict(surface='דרש להן מקרא זה ... אף אני',role='speaker',candidates=['רבי'],scope='Reply to family with bronze-serpent precedent and rhetorical questions',transmission_chain=[]),[c['bronzeverse'],z['asaleft'],z['jehoshaphatleft'],z['removedidols'],c['myleft']])
add('variants','attributions',[146,147],dict(surface='ואמרי לה ... ואמרי לה ... מאן דאמר',role='anonymous',candidates=[],scope='Three alternative wordings and corresponding lexical supports; no named holder assignment by order',transmission_chain=[]),[c['nozichin'],c['nozanichin'],c['nozachichin']])
rels=[(129,'givenformula','howdomain','answer'),(129,'nullformula','howdomain','answer'),(129,'noformal','givenformula','qualification'),(129,'noformal','nullformula','qualification'),(130,'notconsidered','demaimix','answer'),(131,'animalprotection','humaninference','support'),(131,'humaninference','righteousmore','answer'),(131,'humaninference','possibledecree','support'),([132,133],'finishedmixtures','possibledecree','answer'),(133,'finishedmixtures','demaimix','answer'),(135,'requesttithe','nomixdecree','support'),(136,'deliberatemix','nomixdecree','answer'),(136,'flavorpurpose','nomixdecree','answer'),(136,'flavornotnull','flavorpurpose','support'),(137,'mothergive','motherreplace','support'),(137,'motherreceive','motherreplace','support'),(137,'mothersuspect','mothergive','support'),(137,'mothersuspect','motherreceive','support'),(137,'motherdaughter','motherreplace','answer'),(137,'motherashamed','motherreplace','answer'),(138,'inngive','generalreplace','support'),(138,'innreceive','generalreplace','support'),(138,'innsuspect','innreceive','support'),(138,'innrationale','generalreplace','answer'),(140,'shimonno','impuregrind','objection'),(140,'givesandeats','shimonno','support'),(141,'stealthenswap','grindingreplace','support'),(141,'oxrationale','stealthenswap','answer'),(142,'testimony','permittedbeit','support'),(143,'ancestors','permittedbeit','objection'),(145,'ancestorsleft','asaleft','answer'),(145,'ancestorsleft','jehoshaphatleft','answer'),(145,'ancestorsleft','removedidols','answer'),(145,'ancestorsleft','myleft','analogy'),(145,'myleft','ancestors','answer'),(146,'myleft','nozichin','support'),(146,'myleft','nozanichin','support'),(146,'myleft','nozachichin','support'),(147,'breastplate','nozichin','support'),(147,'notforsake','nozanichin','support'),(147,'haughty','nozachichin','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={128:'Israelite giving/relinquishing versus gentile rental requirement; continuation of prior decree novelty, no inferred permission for gentile to use Israelite procedures.',129:'כיצד question, both domain formulas and no need לזכות preserved; no conflation with sale of physical land.',130:'Yai inn, wine eggs, Zeira abstention versus Rav Asi eating, explicit mixture concern and not-considered answer; Rav Asi not Rav.',131:'Zeira conditional decree query and righteous-animal a fortiori explicit rhetorical question; supported argument not factual guarantee of universal infallibility.',132:'Investigation and four purchased-ingredient preparation cases: wine/brine, wine/aluntit, vetch/ground, lentils/crushed; demai and definite untithed stronger obligation.',133:'Finished mixtures themselves permitted for demai, unlike deliberate ingredient purchase; does not nullify definite untithed obligations.',134:'Explicit no-decree-on-mixtures challenge with neighbor dough/pot initial no-concern rules separately for seventh-year and tithe.',135:'Explicit use-her-ingredients condition changes both seventh-year and tithe concern; source exception not generalized.',136:'Anonymous deliberate-mixing rationale versus Rafram flavoring/not-nullified rationale retained separately without forcing same reasoning.',137:'Substitution question; mother-in-law outgoing/return tithing, spoiled-food replacement suspicion; Yehuda daughter-welfare and son-in-law-shame reasons.',138:'General substitution challenge; innkeeper outgoing/return tithing and suspicion; warm-scholar/cold-self rationalization explicitly source-attributed.',139:'New substitution question, grinding companions impure/pure alternative; pronoun antecedent retained with uncertainty rather than forced identity.',140:'Shimon ben Elazar forbids even impure case because companion gives/eats; no unsupported attribution of earlier first-tanna view.',141:'Stealing-to-substitution a fortiori question, Rav Yosef ox-eating-threshing rationalization distinguishes case, not broad theft permission.',142:'Yehoshua ben Zeruz kinship as son of Meir father-in-law, testimony before Rabbi of Meir leaf-eating, Rabbi Beit Shean permission;7a4–9 context read for jurisdiction and proof objections.',143:'Brothers and paternal household directly challenge Rabbi ancestral prohibition precedent; actual question structured.',144:'Rabbi full bronze-serpent verse and separate Asa/Jehoshaphat questions plus prior-idolatry-removal premise; continuation gives explanation.',145:'Ancestors left room for later reform, analogue applied by Rabbi to own ruling; no unqualified dismissal of ancestral practice.',146:'Three distinct versions מזיחין/מזניחין/מזחיחין preserved with condition scholar speaks halakha; no assigned names by order, no universal correctness certification.',147:'Each version matched its own lexical proof; haughty-hearted increase of disputes retained.7a4–9 read: Beit Shean challenge answered by first versus second conquest/sanctity and poor seventh-year support; leaf-in-bundle, oversight, remote-tithing, mental-designation alternatives tested, great witness reply. These context claims not new core coverage.'}
for i in range(128,148):
 add('u'+str(i),'utterances',i,dict(textual_voice='Narrative, named teachings and anonymous argument separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only; not replacement for named speaker/holder records',transmission_chain=[]))
COV=[]
for i in range(128,148):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_6a10_7a3_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
