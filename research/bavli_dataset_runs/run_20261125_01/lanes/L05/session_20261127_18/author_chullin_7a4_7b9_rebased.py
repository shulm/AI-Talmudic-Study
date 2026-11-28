"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='39a4882c2af119f876ae8173604a8ffe491f1453dd33a4fdb38748748a17e734';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[148]['ref']=='Chullin 7a:4' and I[167]['ref']=='Chullin 7b:9'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2718.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('beitproof','structure',range(148,154),dict(title='Beit Shean territorial sanctity and detailed testimony objections',primary=True,boundary='closed',legacy_ids=[]))
s2=add('pinhas','structure',range(154,162),dict(title='Pinhas ben Yair river narrative and donkey demai distinction',primary=True,boundary='closed',legacy_ids=[]))
s3=add('hospitality','structure',range(162,168),dict(title='Rabbi hospitality and white-mule objections; narrative conclusion follows',primary=True,boundary='open_right',legacy_ids=[]))
priorbeit=next(r for r in S['records'] if r['id']=='ch.s2717.beitshean')
closedbeit={k:json.loads(json.dumps(v)) for k,v in priorbeit.items() if k not in ['review_state','release_state','ml_eligible','supersedes']}
closedbeit['id']='ch.s2717.beitshean.s18closed';closedbeit['supersedes']=priorbeit['id'];closedbeit['content']['boundary']='closed';closedbeit['content']['title']+='; source argument completed by Chullin7a4–9 continuation'
R.append(closedbeit)
e('beitcontinuation',148,closedbeit['id'],s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('beitoutside',148,'Can anyone say Beit Shean is not part of the Land of Israel?', ['Rabbi permitted Beit Shean in prior passage','Judges1:27 lists Manasseh and Beit Shean'])
C('manassehverse',148,'The verse says Manasseh did not dispossess Beit Shean and its surrounding towns, and Taanach and its towns.','Yehuda son of Shimon ben Pazi verse objection, not final disproof of Rabbi ruling')
add('yehudaask','attributions',148,dict(surface='מתקיף לה יהודה בריה דר׳ שמעון בן פזי',role='speaker',candidates=['יהודה בריה דרבי שמעון בן פזי'],scope='Challenges Beit Shean territorial premise',transmission_chain=[]),[z['beitoutside'],c['manassehverse']])
C('twoconquests',149,'Many cities were conquered by those coming from Egypt but not by those coming from Babylon.','Teaching overlooked by objector; distinguishes conquests, not denial of initial Israelite territory',holder='רבי אלעזר בן שמוע')
add('conquestreport','attributions',149,dict(surface='ר׳ שמעון בן אליקים משום ר׳ אלעזר בן פדת ... משום ר׳ אלעזר בן שמוע',role='transmitter',candidates=['רבי שמעון בן אליקים'],scope='Three-link report of two-conquest distinction',transmission_chain=['רבי שמעון בן אליקים','רבי אלעזר בן פדת','רבי אלעזר בן שמוע']),[c['twoconquests']])
C('initialsanctity',150,'The first sanctification sanctified for its time.','Anonymous explanation of position underlying ruling; not an unrelated blanket future sanctity conclusion')
C('notfuture',150,'It did not sanctify for the future.','Negative temporal limit on first sanctification, in this explanation')
C('poorbenefit',150,'They left those cities so the poor could rely on them in the seventh year.','Purpose of not reconquering/sanctifying all earlier cities, not neglect charged as wrongdoing')
Q('singleleaf',151,'But did Rabbi Meir not eat only a leaf?', ['Rabbi Yirmeya addresses Rabbi Zeira','Whether observed eating establishes tithing exemption'])
C('bundle',151,'He ate it from a bundle.','Rabbi Zeira answer, not unsupported assumption about an isolated leaf',holder='רבי זירא')
C('bundlingrule',151,'A vegetable normally bundled reaches the stated tithing stage when it is bundled.','Quoted Mishnah supports answer',cond=['Vegetable normally bundled','It has been bundled'])
add('yirmeyaask','attributions',151,dict(surface='אמר ליה ר׳ ירמיה לרבי זירא',role='speaker',candidates=['רבי ירמיה'],scope='Explicit leaf objection to Rabbi Zeira',transmission_chain=[]),[z['singleleaf']])
Q('oversight',152,'Perhaps he was not aware of it?', ['Rabbi Meir eating from bundle','Proposed oversight rather than legal permission'])
C('protectedanimals',152,'The Holy One does not bring mishap through the animals of the righteous.','Reply premise about forbidden consumption, not producer-certified universal infallibility')
Q('protectedpeople',152,'If so for their animals, is it not all the more so for the righteous themselves?', ['Protection premise','Proposed Rabbi Meir oversight'])
C('protectedconclusion',152,'All the more so for the righteous themselves.','Reply rejects proposed forbidden-food oversight within argument')
Q('elsewheretithe',153,'Perhaps he tithed for them from produce elsewhere?', ['Observed leaf eating','Alternative to territorial exemption'])
C('noremotetithe',153,'Haverim are not suspected of separating terumah from produce not adjacent to the rest.','Reply rejects remote-separation hypothesis, local reliability assertion')
Q('mentaldesignation',153,'Perhaps he designated one side mentally and ate from the other?', ['Same observed eating','Alternative internal designation'])
C('greatwitness',153,'Consider what a great man is testifying about him.','Reply relies on witness quality; does not fabricate unreported explicit detail or recant original testimony')
Q('whichanimals',154,'What is the example of the animals of the righteous?', ['Repeated protection premise'])
C('redemptionjourney',154,'Rabbi Pinhas ben Yair was traveling to redeem captives.','Narrative purpose')
C('riverencounter',154,'He encountered the Ginai river.','Narrative setting')
C('splitrequest',155,'He asked Ginai to divide its waters so he could cross.','Pinhas ben Yair speech in narrated encounter')
C('riverpurpose',155,'The river replied that both it and he were doing their Creator’s will.','Personified river speech in source narrative, not an assertion of observed natural dialogue')
C('rivercertainty',155,'The river contrasted his uncertain accomplishment with its own certain accomplishment.','River’s stated reason for refusing; certainty of outcome not inferred by producer')
C('threat',155,'He said that if it did not divide, he would decree that water never pass through it again.','Pinhas conditional threat within narrative',cond=['River does not divide'])
C('firstsplit',155,'The river divided for him.','Narrated result; later repetition count explicitly questioned')
C('wheatman',156,'A man was carrying wheat for Passover.','Second traveler in narrative')
C('wheatrequest',156,'He asked the river to divide for that man too because he was engaged in a mitzvah.','Pinhas request and explicit reason')
C('wheatsplit',156,'It divided for him.','Narrated second beneficiary, not certainty of separate splitting event after later correction')
C('arabcompanion',156,'An Arab traveler was accompanying them.','Third traveler, distinct from wheat carrier')
C('companionrequest',156,'He asked it to divide for this companion too, so he would not say this is how companions are treated.','Pinhas stated social reason; not the wheat-carrier mitzvah rationale')
C('companionsplit',156,'It divided for him.','Narrated third beneficiary; count remains subject to next objection')
C('greaterinitial',157,'How much greater this man is than Moses and six hundred thousand: there once, here three times.','Rav Yosef initial comparison, revised after challenge',holder='רב יוסף',mode='challenged')
Q('onesplit',157,'Perhaps here too it was only once?', ['Initial three-times versus one-time comparison'])
C('equalfinal',157,'Rather, like Moses and six hundred thousand.','Revised comparison replaces claim of greater through three separate splits',mode='reconciled')
C('barleyrefusal',158,'At the lodging they gave his donkey barley, but it did not eat.','Narrative begins animal example; not yet solved by cleaning')
C('beatenrefusal',159,'They beat the barley, but it still did not eat.','First attempted remedy unsuccessful')
C('cleanedrefusal',159,'They cleaned it, but it still did not eat.','Second unsuccessful remedy')
Q('untithed',159,'Perhaps it is not tithed?', ['Repeated refusal despite preparation','Pinhas addresses hosts'])
C('titheate',159,'They tithed it and the donkey ate.','Narrated resolution')
C('rebuke',159,'He said this poor creature is going to do its Creator’s will, yet they are feeding it untithed produce.','Pinhas rebuke; legal scope of tithe obligation tested next')
Q('animalobligation',160,'Is there a tithing obligation in this case?', ['Feed bought for animal use','Quoted demai exemptions'])
C('seedexempt',160,'One buying for seed is exempt from demai.','Quoted Mishnah nonfood-use case',cond=['Purchased for seed'])
C('animalexempt',160,'One buying for an animal is exempt from demai.','Quoted Mishnah, qualified next by original purchase purpose',cond=['Purchased for animal'])
C('flourexempt',160,'Flour bought for hides is exempt from demai.','Nonfood purpose',cond=['Flour for hides'])
C('lampexempt',160,'Oil bought for a lamp is exempt from demai.','Nonfood purpose',cond=['Oil for lamp'])
C('vesselsexempt',160,'Oil bought to anoint utensils is exempt from demai.','Separate oil-use case',cond=['Oil to anoint utensils'])
C('originalanimal',161,'The exemption was taught only where he initially bought it for an animal.','Rabbi Yohanan qualification',cond=['Initial purchase for animal'],holder='רבי יוחנן')
C('originalhuman',161,'If initially bought for a person, then redirected to an animal, it must be tithed.','Rabbi Yohanan opposite branch',cond=['Initial human-food purchase','Subsequent decision for animal'],holder='רבי יוחנן')
C('ownanimalbaraita',161,'Produce bought in the market to eat and later redirected to animals may not be placed before one’s own animal unless tithed.','Supporting baraita',cond=['Purchased for eating','Changed purpose to animal','Not yet tithed'])
C('friendsanimal',161,'Nor may it be placed before another person’s animal unless tithed.','Separate recipient, same condition',cond=['Purchased for eating','Changed purpose to animal','Not yet tithed'])
Q('dine',162,'Would you like to dine with me?', ['Rabbi goes out to meet Pinhas ben Yair'])
C('yesdine',162,'He answered yes.','Pinhas accepts invitation at this stage; later delay and mule objection not erased')
C('rabbijoy',162,'Rabbi’s face brightened.','Narrated response')
Q('vowassumption',163,'Do you think I am forbidden by vow to benefit from Israel?', ['Pinhas addresses Rabbi after invitation','Explains selective acceptance, not an actual vow'])
C('israelholy',163,'Israel are holy.','Pinhas statement preceding host distinctions',holder='רבי פנחס בן יאיר')
C('willingpoor',163,'Some are willing but do not have the means.','First host category',holder='רבי פנחס בן יאיר')
C('richunwilling',163,'Some have means but are unwilling.','Second host category',holder='רבי פנחס בן יאיר')
C('begrudgingverse',163,'The cited Proverbs text says not to eat the grudging person’s bread or desire his delicacies; he says eat and drink but his heart is not with you.','Pinhas quotation grounds distinction between words and willingness',holder='רבי פנחס בן יאיר')
C('rabbiwilling',163,'You are willing and have the means.','Pinhas assessment of Rabbi, not rejection of all hospitality',holder='רבי פנחס בן יאיר')
C('urgentmitzvah',164,'For now he is in a hurry because he is engaged in a mitzvah.','Pinhas explanation for delaying meal',holder='רבי פנחס בן יאיר')
C('returnpromise',164,'When he returns he will enter Rabbi’s house.','Conditional future intention, not already completed meal',cond=['Return from present task'],holder='רבי פנחס בן יאיר')
C('whitemules',165,'On returning, he happened to enter by a doorway where white mules stood.','Narrative trigger of refusal')
Q('deathmeal',165,'The angel of death is in this man’s house, and should I dine with him?', ['White mules at doorway','Pinhas reacts to danger'])
C('sellproposal',166,'Rabbi offered to sell them.','Proposed disposal, not completed sale',holder='רבי',mode='hypothetical')
C('stumblingblock',166,'Pinhas replied with לפני עור לא תתן מכשול.','Objection to transferring dangerous mules to others, not acceptance of proposed sale',holder='רבי פנחס בן יאיר')
C('abandonproposal',167,'Rabbi offered to declare them ownerless.','Second proposed remedy, not actual abandonment',holder='רבי',mode='hypothetical')
C('moreharm',167,'That would increase harm.','Pinhas objection to abandonment',cond=['Mules declared ownerless'],holder='רבי פנחס בן יאיר')
C('crippleproposal',167,'Rabbi offered to disable them: עקרנא להו.','Third proposed remedy, not action performed',holder='רבי',mode='hypothetical')
C('animalpain',167,'That involves suffering of living creatures.','Pinhas objection',cond=['Proposed disabling of mules'],holder='רבי פנחס בן יאיר')
C('killproposal',167,'Rabbi offered to kill them.','Fourth proposed remedy, not completed killing',holder='רבי',mode='hypothetical')
C('waste',167,'That involves בל תשחית.','Pinhas objection to killing',cond=['Proposed killing of mules'],holder='רבי פנחס בן יאיר')
add('pinhasriver','attributions',[155,156],dict(surface='אמר ליה ... גוזרני עליך ... חלוק ליה נמי',role='speaker',candidates=['רבי פנחס בן יאיר'],scope='Narrated requests/threat to river for himself, wheat carrier and companion',transmission_chain=[]),[c['splitrequest'],c['threat'],c['wheatrequest'],c['companionrequest']])
add('riverspeech','attributions',155,dict(surface='אמר ליה אתה הולך ... ואני הולך',role='speaker',candidates=['גינאי נהרא — personified in narrative'],scope='River response in source narrative; do not replace with Pinhas position',transmission_chain=[]),[c['riverpurpose'],c['rivercertainty']])
add('pinhasdonkey','attributions',159,dict(surface='אמר להו דלמא לא מעשרן ... אמר ענייה זו',role='speaker',candidates=['רבי פנחס בן יאיר'],scope='Tithe question and donkey-food rebuke',transmission_chain=[]),[z['untithed'],c['rebuke']])
add('rabbiinvite','attributions',162,dict(surface='אמר ליה רצונך סעוד אצלי',role='speaker',candidates=['רבי'],scope='Invites Pinhas to dine',transmission_chain=[]),[z['dine']])
add('pinhasreply','attributions',[162,163,165],dict(surface='אמר לו הן ... כמדומה אתה ... ואני אסעוד אצלו',role='speaker',candidates=['רבי פנחס בן יאיר'],scope='Initial yes, explanation of hospitality, later danger objection are distinct stages',transmission_chain=[]),[c['yesdine'],z['vowassumption'],z['deathmeal']])
rels=[(148,'manassehverse','beitoutside','support'),(149,'twoconquests','beitoutside','answer'),(150,'initialsanctity','twoconquests','qualification'),(150,'notfuture','twoconquests','qualification'),(150,'poorbenefit','twoconquests','support'),(151,'bundle','singleleaf','answer'),(151,'bundlingrule','bundle','support'),(152,'protectedanimals','protectedconclusion','support'),(152,'protectedconclusion','protectedpeople','answer'),(152,'protectedconclusion','oversight','answer'),(153,'noremotetithe','elsewheretithe','answer'),(153,'greatwitness','mentaldesignation','answer'),(155,'rivercertainty','splitrequest','objection'),(155,'threat','firstsplit','support'),(156,'wheatman','wheatrequest','support'),(156,'companionrequest','companionsplit','support'),(157,'onesplit','greaterinitial','objection'),(157,'equalfinal','greaterinitial','correction'),(157,'equalfinal','onesplit','answer'),(159,'titheate','untithed','answer'),(159,'titheate','whichanimals','answer'),(160,'animalexempt','animalobligation','support'),(161,'originalanimal','animalexempt','qualification'),(161,'originalhuman','animalobligation','answer'),(161,'ownanimalbaraita','originalhuman','support'),(161,'friendsanimal','originalhuman','support'),(162,'yesdine','dine','answer'),(163,'rabbiwilling','yesdine','support'),(163,'begrudgingverse','richunwilling','support'),(163,'willingpoor','vowassumption','answer'),(163,'richunwilling','vowassumption','answer'),(164,'urgentmitzvah','returnpromise','support'),(164,'returnpromise','yesdine','qualification'),(165,'whitemules','deathmeal','support'),(166,'sellproposal','deathmeal','answer'),(166,'stumblingblock','sellproposal','objection'),(167,'abandonproposal','stumblingblock','answer'),(167,'moreharm','abandonproposal','objection'),(167,'crippleproposal','moreharm','answer'),(167,'animalpain','crippleproposal','objection'),(167,'killproposal','animalpain','answer'),(167,'waste','killproposal','objection')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={148:'Yehuda son of Shimon ben Pazi territorial question and Judges proof; not final disproof of Beit Shean ruling.',149:'Shimon ben Elikim→Elazar ben Pedat→Elazar ben Shamua chain, first conquest not repeated by second; overlooked teaching answers objection.',150:'First sanctity valid then but not future, omission of cities supports poor in seventh year; temporal limits and purpose separate.',151:'Yirmeya leaf question to Zeira, bundle answer, Mishnah bundling threshold; not infer obligation from any isolated leaf.',152:'Oversight question and righteous-animal a fortiori separately recorded; local theological argument not general factual verification.',153:'Remote-tithing question/rejection by proximity rule, mental-side-designation question and great-witness answer; no invented detailed eyewitness content.',154:'Explicit example question opens Pinhas captives-redemption and Ginai river narrative; answer reaches donkey episode.',155:'River personified response distinct from Pinhas speech: both purpose, certain/uncertain comparison, conditional threat and narrated split.',156:'Wheat carrier for Passover and mitzvah rationale versus Arab companion/social-treatment rationale; three beneficiaries not asserted three independent splits after next revision.',157:'Rav Yosef initially greater-than-Moses-and600000 based on3vs1; possible single splitting objection and revised equal comparison explicitly linked.',158:'Barley donkey refusal begins example; later cleaning not silently successful.',159:'Beating/cleaning failures, explicit untithed question, tithing/eating resolution and Pinhas rebuke.',160:'Obligation objection; all five nonfood purchase cases seed/animal/flour-for-hides/oil-lamp/oil-utensils preserved.',161:'Yohanan original animal purchase exemption versus human purchase then changed animal purpose obligation; baraita forbids feeding own or friend animal unless tithed.',162:'Rabbi invitation question, Pinhas initial yes, Rabbi joy; later refusal does not erase this stage.',163:'Vow-assumption question, Israel holiness, willing-without-means and means-without-willingness, full Proverbs warning and Rabbi both-willing-and-able response.',164:'Mitzvah urgency delays meal; return promise conditional, not completed visit or eating.',165:'Return and white mules trigger angel-of-death rhetorical meal question; danger metaphor distinguished from narrative animal presence.',166:'Rabbi sale proposal versus Pinhas stumbling-block objection; no sale performed.',167:'Three proposed remedies ownerless/disable/kill separately opposed by increased harm/animal suffering/bal tashchit.7b10 narrative closure read: continued pressure, hill separates, Rabbi weeps;7b11–13 derivation objections and mule injury clarification read, through7b16 final Pinhas meal-history note. No proposal accepted or meal asserted at boundary.'}
for i in range(148,168):
 add('u'+str(i),'utterances',i,dict(textual_voice='Source narrative, quoted dialogue and anonymous reasoning kept distinct',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Narrative/framing only, not substitution for named reports and dialogue speakers',transmission_chain=[]))
COV=[]
for i in range(148,168):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
for priorcov in S['coverage']:
 if priorbeit['id'] in priorcov['record_ids']:
  cv={k:json.loads(json.dumps(v)) for k,v in priorcov.items() if k!='proposal_execution'}
  cv['record_ids']=[closedbeit['id'] if v==priorbeit['id'] else v for v in cv['record_ids']]
  cv['rationale']+=' Session18 completes Beit Shean source argument7a4–9; explicit boundary successor, unchanged source partition and historical records.'
  COV.append(cv)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=[v for v in S['open_tails'] if v!=priorbeit['id']]+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_7a4_7b9_rebased_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
