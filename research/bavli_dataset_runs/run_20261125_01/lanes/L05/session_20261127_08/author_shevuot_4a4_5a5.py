"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shevuot')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='b3049a3e12c0a4bca5eaa7b700541f844b78da51d6500aab9e6398b7b836b112';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shevuot','epoch':2}
assert I[49]['ref']=='Shevuot 4a:4' and I[76]['ref']=='Shevuot 5a:5'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='she.s2708.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('revision','structure',range(49,77),dict(title='Anonymous-Mishnah revision, rejection of lashes-only reading, and Rabbi’s personal versus reported positions',primary=True,boundary='open_right',legacy_ids=[]))
e('continuation',49,'she.s2707.identity',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('rabbiinconsistent',49,'On your reasoning, how did Rabbi himself teach one anonymous Mishnah this way and the other differently?', ['Prior question why Rabbi Yohanan prefers one anonymous source','Conflicting no-action lashes implications'])
C('initiallashes',50,'Rabbi initially held that a prohibition without action receives lashes and taught anonymously accordingly.','Earlier editorial position retained as history, subsequently revised',holder='רבי',mode='retracted',cond=['Earlier stage','Prohibition without action'])
C('laternolashes',50,'Rabbi later held that such a prohibition does not receive lashes and taught anonymously accordingly.','Later revised position explains Rabbi Yohanan’s choice',holder='רבי',mode='asserted',cond=['Later stage','Prohibition without action'])
C('mishnahretained',50,'The earlier Mishnah did not move from its place.','Preservation of earlier text despite change of view; no erasure of historical source')
Q('establishedas',51,'How was the Mishnah interpreted?', ['Return to attempted Rabbi Yishmael/lashes reading'])
C('recap',51,'It was interpreted as Rabbi Yishmael and concerning lashes.','Recap of interim reading, not final endorsement',mode='rejected')
Q('lesionlashes',51,'What lashes are there for appearances of lesions?', ['All categories tentatively interpreted as lashes'])
C('cutslesion',51,'The case is one who cuts off his baheret.','Local answer defending lashes reading',cond=['Cuts off בהרת'])
C('negativeformula',51,'Every occurrence of השמר, פן, or אל is a negative prohibition.','Rabbi Avin reports Rabbi Ilaa; do not conflate reporter with originator',holder='רבי אילעא')
add('avin','attributions',51,dict(surface='רבי אבין א"ר אילעא',role='transmitter',candidates=['רבי אבין'],scope='Reported rule of negative-prohibition formulations',transmission_chain=['רבי אבין','רבי אילעא']),[c['negativeformula']])
Q('shabbatlashes',52,'What lashes apply to Shabbat transfers?', ['Attempted all-lashes reading','Prohibition warns of a court-imposed death penalty'])
C('capitalwarning',52,'The Shabbat transfer prohibition is given as a warning for a court-imposed death penalty.','Ground of objection to lashes interpretation')
C('capitalnolashes',52,'A prohibition given as warning for a court-imposed death penalty does not incur lashes.','Principle invoked by objection; opposed view follows',cond=['לאו שניתן לאזהרת מיתת בית דין'])
C('yishmaelcapital',52,'Such a prohibition does incur lashes.','Rabbi Yishmael’s view invoked to defend identifying Mishnah with him',holder='רבי ישמעאל',cond=['לאו שניתן לאזהרת מיתת בית דין'])
C('whyidentify',52,'That is why the Mishnah was being assigned to Rabbi Yishmael.','Local defense of provisional attribution, not final author determination',mode='challenged')
Q('akivaotherwise',53,'Otherwise could it be Rabbi Akiva? Awareness of impurity would remain difficult.', ['Implied alternative to Yishmael attribution','Akiva excludes unawareness of Temple for sacrifice'])
C('akivalashes',53,'Just as the Yishmael reading used lashes, an Akiva reading could also concern lashes.','Alternative defense of classification scope, rejected by further difficulties',mode='rejected')
Q('warnings',54,'If so, should the heading not say warnings instead of awareness?', ['Lashes interpretation requires warnings'])
C('warningawareness',54,'Read it as awareness of warnings.','Local answer to terminology objection, not final accepted Mishnah interpretation',mode='rejected')
Q('onlytwo',55,'If so, are there not only two rather than two that are four?', ['Awareness interpreted as warnings for lashes'])
Q('forgetting',55,'What role could intervening unawareness have for lashes?', ['Mishnah requires awareness initially and finally with unawareness between'])
Q('variableoffering',55,'Moreover, does the Mishnah not specify a variable-value offering?', ['Attempted lashes-only interpretation'])
C('onlytwoproblem',55,'The warning interpretation yields only two categories.','First objection to lashes-only reading')
C('awarenesspattern',55,'The Mishnah includes awareness at the beginning and end with unawareness between.','Quoted condition contradicting proposed lashes-only scope',cond=['Initial awareness','Final awareness','Intervening unawareness'])
C('offeringproblem',55,'The Mishnah specifies a variable-value offering.','Third objection to lashes-only interpretation')
C('yosefauthor',56,'The Mishnah is Rabbi’s, formulated according to different tannaim.','Rav Yosef’s replacement of whole-list Yishmael/Akiva alternatives',holder='רב יוסף')
C('yosefimpurity',56,'For awareness Rabbi adopts Rabbi Yishmael’s position.','Rav Yosef’s attribution, subsequently refined to Rabbi’s own reasoning',holder='רב יוסף')
C('yosefoaths',56,'For oaths Rabbi adopts Rabbi Akiva’s position.','Rav Yosef’s attribution, final personal-disagreement qualification at5a5',holder='רב יוסף')
C('kahanaadmonition',57,'Do not say Rabbi merely adopts the tannaim’s views without personally agreeing.','Rav Kahana’s response reported by Rav Ashi; subsequent inquiry ultimately limits this explanation for oaths',holder='רב כהנא',mode='challenged')
add('ashireport','attributions',57,dict(surface='אמר רב אשי אמריתא לשמעתא קמיה דרב כהנא ואמר לי',role='transmitter',candidates=['רב אשי'],scope='Rav Ashi reports presenting the teaching to Rav Kahana and receiving his response',transmission_chain=['רב אשי','רב כהנא']),[c['kahanaadmonition']])
C('ownreason',58,'Rather, Rabbi explains his own reasoning.','Response continuing Rav Kahana report; demonstrated for awareness, not unqualified final oath agreement',holder='רב כהנא',cond=['Awareness derivation established below'])
Q('awarenesssource',58,'From where do we derive liability only with initial and final awareness and intervening unawareness?', ['Baraita’s awareness conditions'])
C('akivadouble',58,'The twice-written ונעלם establishes liability only with awareness initially and finally and unawareness between.','Rabbi Akiva’s baraita derivation',holder='רבי עקיבא',cond=['Initial awareness','Final awareness','Unawareness between'])
C('rabbineednot',[59,60],'Rabbi says that derivation is unnecessary.','Full cross-folio response to Akiva’s use of repeated ונעלם',holder='רבי')
C('priorawareness',[59,60],'ונעלם implies prior knowledge.','Rabbi’s stated derivation; later5a8–13 examines what knowledge means, so no invented experiential requirement',holder='רבי')
C('finalawareness',60,'והוא ידע supplies the other awareness, yielding two awareness states.','Rabbi’s alternative derivation',holder='רבי')
Q('doubleleft',60,'What then does the repeated ונעלם teach?', ['Two awareness states already derived from ונעלם and והוא ידע'])
C('rabbiimpurity',60,'The repetition imposes liability for unawareness of impurity.','Rabbi’s own derivation, not merely borrowed Yishmael report',holder='רבי',cond=['העלם טומאה'])
C('rabbitemple',60,'The repetition imposes liability for unawareness of the Temple.','Second liability grounded in Rabbi’s own derivation',holder='רבי',cond=['העלם מקדש'])
Q('oathsource',61,'We have found Rabbi’s own reasoning for awareness; from where is his position on oaths established?', ['First wording of question','Awareness reasoning shown','Oath reasoning not yet shown'])
C('reasonanswer',61,'It is a matter of reasoning.','First wording’s initial answer, argument developed and revised below')
Q('oathsourcealt',62,'We have found that Rabbi agrees with Rabbi Yishmael on awareness; from where do we know he agrees with Rabbi Akiva on oaths?', ['לישנא אחרינא','Alternative wording preserved separately'])
C('reasonansweralt',62,'It is a matter of reasoning.','Alternative wording’s initial answer; not an independently resolved agreement claim')
Q('akivapast',63,'Why does Rabbi Akiva impose liability for the past?', ['Past-directed oath liability'])
C('akivaribuy',63,'Rabbi Akiva interprets by inclusions and exclusions.','Explanation for his past-oath liability',holder='רבי עקיבא')
C('rabbiribuyinitial',63,'Rabbi too interprets by inclusions and exclusions.','Initial unrestricted explanation of oath agreement, subsequently restricted to special textual case and rejected as proof of personal oath agreement',holder='רבי',mode='rejected')
C('rabbiredemption',64,'A human firstborn may be redeemed with everything except documents.','Rabbi’s baraita rule',holder='רבי',cond=['Redemption of human firstborn'])
C('sagesredemption',64,'A human firstborn may be redeemed with everything except slaves, documents and land.','Sages’ contrasting baraita rule',holder='רבנן',cond=['Redemption of human firstborn'])
Q('rabbireason',65,'What is Rabbi’s reason?', ['Redemption admits all except documents'])
C('redeemribuy',65,'Rabbi reads ופדויו מבן חדש as inclusion, בערכך כסף חמשת שקלים as exclusion, and תפדה as renewed inclusion.','Redemption-specific method; later limited by adjacent-general-text pattern',holder='רבי')
C('includeall',66,'An inclusion, exclusion and renewed inclusion includes everything.','Interpretive rule applied here')
Q('included',66,'What is included?', ['Inclusion-exclusion-inclusion for redemption'])
C('allitems',66,'All items are included.','Answer in the stated interpretive scheme, subject to explicit document exclusion')
Q('excluded',66,'What is excluded?', ['Inclusion-exclusion-inclusion for redemption'])
C('documents',66,'Documents are excluded.','Specific exclusion in Rabbi’s redemption reading',holder='רבי')
C('sagesgeneral',67,'The sages use general and particular interpretation.','Redemption method',holder='רבנן')
C('sagessequence',67,'ופדויו מבן חדש is general, בערכך כסף חמשת שקלים particular, and תפדה general again.','Sages’ verse mapping',holder='רבנן')
C('likeparticular',68,'With general-particular-general one includes only things similar to the particular.','Rule underlying sages’ redemption exclusions',holder='רבנן')
C('movablevalue',68,'The particular specifies a movable thing with intrinsic monetary value; included items must share those features.','Joint conditions, not merely movability',holder='רבנן',cond=['Movable','גופו ממון'])
C('excludeland',68,'Land is excluded because it is not movable.','Sages’ redemption exclusion and reason',holder='רבנן')
C('excludeslaves',68,'Slaves are excluded because they are compared to land.','Sages’ redemption exclusion and reason',holder='רבנן')
C('excludedocs',68,'Documents are excluded although movable, because they lack intrinsic monetary value.','Sages’ redemption exclusion preserves concession and negation',holder='רבנן',cond=['Movable yet אין גופן ממון'])
Q('ravina',69,'Does Rabbi interpret by inclusions and exclusions? Does he not interpret by general and particular?', ['Ravina addresses Ameimar','Challenge to unrestricted inference from redemption'])
add('ravinaspeaker','attributions',69,dict(surface='א"ל רבינא לאמימר',role='speaker',candidates=['רבינא'],scope='Ravina asks Ameimar the interpretive-method challenge; Ameimar is addressee, not automatically author of ensuing anonymous text',transmission_chain=[]),[z['ravina']])
Q('tools',70,'With only מרצע stated, from where are הסול, הסירה, המחט, המקדח and המכתב included?', ['Ear-piercing instrument baraita'])
C('yosibarinclude',70,'ולקחת includes anything taken in the hand, including the listed הסול, הסירה, המחט, המקדח and המכתב.','Rabbi Yosi son of Rabbi Yehuda’s expansion; all listed implements retained in original terms',holder='רבי יוסי ברבי יהודה')
C('rabbimetal',70,'Just as the awl is metal, every included implement must be metal.','Rabbi’s restrictive instrument rule',holder='רבי',cond=['Metal implement'])
Q('methods',71,'In what do they disagree?', ['Instrument baraita; quoted analysis'])
C('rabbigeneral',71,'Rabbi interprets by general and particular.','Analysis of instrument baraita; confirmed as general practice at5a2',holder='רבי')
C('yosiribuy',[71,72],'Rabbi Yosi son of Rabbi Yehuda interprets by inclusions and exclusions.','Full split-folio methodological attribution, not assigned from name order',holder='רבי יוסי ברבי יהודה')
C('normallygeneral',73,'Yes, Rabbi generally interprets by general and particular.','Reply concedes challenge; no definitive named speaker assigned to anonymous answer',holder='רבי')
C('specialcase',73,'Here the reason is the rule taught in the school of Rabbi Yishmael.','Redemption exception, not universal Rabbi inclusion-exclusion method')
C('waterdouble',74,'The twice-written במים is not general-particular but inclusion-exclusion.','Teaching from Rabbi Yishmael’s school used for the special textual pattern',holder='תנא דבי רבי ישמעאל')
Q('sageshow',75,'How do the sages interpret this arrangement?', ['Special double-general-text explanation for Rabbi','Elliptical ורבנן question'])
C('westgeneral',75,'When two general expressions are adjacent, place the particular between them and interpret as general-particular.','Western teaching reported by Ravina; preserve its exact stated formula',holder='אמרי במערבא',cond=['Two adjacent general expressions'])
add('ravinareport','attributions',75,dict(surface='אמר רבינא כדאמרי במערבא',role='transmitter',candidates=['רבינא'],scope='Reports western interpretive rule in answer for sages',transmission_chain=['רבינא','אמרי במערבא']),[c['westgeneral']])
Q('oathdifficulty',76,'Given that Rabbi generally interprets by general and particular, how can the oath position be explained?', ['The proposed personal agreement on past-oath liability rested on a method now limited to redemption'])
C('finalreport',76,'For oaths Rabbi adopts Rabbi Akiva’s view.','Final revision distinguishing reported ruling from personal endorsement',holder='רבי',cond=['Oaths'])
C('finaldisagree',76,'Rabbi himself does not agree with that oath position.','Explicit וליה לא סבירא ליה; limited to oaths, not reversal of his own awareness derivation',holder='רבי',cond=['Oaths position adopted from Rabbi Akiva'])
rels=[(50,'laternolashes','initiallashes','retraction'),(50,'laternolashes','rabbiinconsistent','answer'),(50,'mishnahretained','rabbiinconsistent','answer'),(50,'laternolashes','she.s2707.q.prefer','answer'),(51,'recap','establishedas','answer'),(51,'cutslesion','lesionlashes','answer'),(51,'negativeformula','cutslesion','support'),(52,'capitalwarning','shabbatlashes','support'),(52,'capitalnolashes','shabbatlashes','support'),(52,'yishmaelcapital','shabbatlashes','answer'),(52,'yishmaelcapital','whyidentify','support'),(53,'akivalashes','akivaotherwise','answer'),(54,'warningawareness','warnings','answer'),(55,'onlytwo','warningawareness','objection'),(55,'forgetting','recap','objection'),(55,'variableoffering','recap','objection'),(55,'awarenesspattern','forgetting','support'),(55,'offeringproblem','variableoffering','support'),(56,'yosefauthor','she.s2707.yishmaellashes','correction'),(57,'kahanaadmonition','yosefauthor','qualification'),(58,'ownreason','kahanaadmonition','support'),(58,'akivadouble','awarenesssource','answer'),(60,'rabbineednot','akivadouble','objection'),(60,'priorawareness','rabbineednot','support'),(60,'finalawareness','rabbineednot','support'),(60,'rabbiimpurity','doubleleft','answer'),(60,'rabbitemple','doubleleft','answer'),(60,'rabbiimpurity','ownreason','support'),(60,'rabbitemple','ownreason','support'),(61,'reasonanswer','oathsource','answer'),(62,'reasonansweralt','oathsourcealt','answer'),(63,'akivaribuy','akivapast','answer'),(63,'rabbiribuyinitial','reasonanswer','support'),(63,'rabbiribuyinitial','reasonansweralt','support'),(64,'rabbiredemption','rabbiribuyinitial','support'),(65,'redeemribuy','rabbireason','answer'),(66,'allitems','included','answer'),(66,'documents','excluded','answer'),(66,'redeemribuy','rabbiredemption','support'),(68,'likeparticular','movablevalue','support'),(68,'movablevalue','excludeland','support'),(68,'movablevalue','excludeslaves','support'),(68,'movablevalue','excludedocs','support'),(68,'excludeland','sagesredemption','support'),(68,'excludeslaves','sagesredemption','support'),(68,'excludedocs','sagesredemption','support'),(69,'ravina','rabbiribuyinitial','objection'),(70,'yosibarinclude','tools','answer'),(71,'rabbigeneral','methods','answer'),(72,'yosiribuy','methods','answer'),(73,'normallygeneral','ravina','answer'),(73,'normallygeneral','rabbiribuyinitial','correction'),(73,'specialcase','redeemribuy','qualification'),(74,'waterdouble','specialcase','support'),(75,'westgeneral','sageshow','answer'),(75,'westgeneral','sagesgeneral','support'),(76,'oathdifficulty','rabbiribuyinitial','objection'),(76,'finalreport','oathdifficulty','answer'),(76,'finaldisagree','oathdifficulty','answer'),(76,'finaldisagree','kahanaadmonition','qualification'),(76,'finaldisagree','yosefoaths','qualification')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={49:'Counter-question targets Rabbi’s own conflicting anonymous formulations rather than only Rabbi Yohanan’s preference.',50:'Earlier lashes view, subsequent no-lashes revision and retained earlier Mishnah separately structured; preserve history.',51:'Both recap question and lesion-lashes question; cuts-baheret answer and Avin reporting Ilaa prohibition-formula rule with exact chain.',52:'Transfer-lashes question; court-death warning and general no-lashes principle versus Yishmael contrary view and interim identity defense.',53:'Akiva counterfactual and awareness difficulty; alternative lashes response retained as later-rejected.',54:'Warnings-versus-awareness question and provisional awareness-of-warnings answer.',55:'All three objections separately questioned: only two categories, intervening unawareness, explicit variable offering.',56:'Rav Yosef mixed tannaitic reading: Rabbi author, awareness per Yishmael, oaths per Akiva; not yet personal-agreement decision.',57:'Rav Ashi reports to/from Rav Kahana; initial admonition not to assume lack of agreement remains qualified by final oath conclusion.',58:'Kahana response and baraita source question; Akiva twofold ונעלם source with full three awareness conditions.',59:'Rabbi response fragment read with4b1; no invented truncation.',60:'Prior and final awareness derivations; repeated-word question; impurity and Temple liability separately grounded in Rabbi own reasoning.',61:'First question version concerning Rabbi own reasoning and initial reasoning answer.',62:'Explicit לישנא אחרינא separately recorded: agreement-with-Yishmael versus agreement-with-Akiva wording, not conflated.',63:'Akiva past-oath question and method; initially broad Rabbi-method assertion marked revised by5a2–5.',64:'Redemption Rabbi only documents excluded versus sages slaves/documents/land excluded, two named positions.',65:'Rabbi reason question and full three-part inclusion/exclusion verse mapping; scoped to redemption.',66:'Inclusion-exclusion-inclusion rule, what-included and what-excluded questions and answers separately captured.',67:'Sages method and complete verse mapping general-particular-general.',68:'Similarity rule, movable plus intrinsic-value conditions, land/slaves/documents exclusions with individual reasons and documents movability concession.',69:'Ravina speaker and Ameimar addressee distinct; challenge to generalizing Rabbi’s method.',70:'Instrument expansion question with all five Hebrew terms; Yosi son of Yehuda any-handheld expansion versus Rabbi metal restriction.',71:'Quoted methodological question and Rabbi general/particular; Yosi-method completion crosses folio.',72:'Full71–72 evidence preserves Yosi son of Yehuda inclusion/exclusion; no name-order inference.',73:'Anonymous reply concedes Rabbi generally general/particular; redemption is a special school-of-Yishmael explanation.',74:'Twice במים teaching is inclusion/exclusion not general/particular; attributed to school, not direct isolated personal statement.',75:'Elliptical sages question and Ravina report of western adjacent-generals rule; preserve exact final כלל ופרט formula.',76:'Final difficulty and explicit oath-only reported adoption without Rabbi personal agreement. Context5a6–13 rereads awareness derivation, rejects naive prior-experiential-knowledge inference, allows בית רבו knowledge and captive-child exception; no new coverage or details forced into core derivation.'}
for i in range(49,77):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous argument with named reports, citations and positions separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara framing',role='anonymous',candidates=[],scope='Framing/inferences only; named speakers and transmission roles remain separately recorded',transmission_chain=[]))
COV=[]
for i in range(49,77):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shevuot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s1])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shevuot_4a4_5a5_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=28,sha256=hashlib.sha256(b).hexdigest())))
