"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_temurah')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='c707095cba580154adb46bb43f6a50b63affe0eea83f3c5a7455db7adf2e5ad7';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/temurah','epoch':2}
assert I[64]['ref']=='Temurah 4a:3' and I[83]['ref']=='Temurah 4b:13'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='tem.s2713.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('priority','structure',range(64,74),dict(title='Priority of terumah and first fruits: unnamed alternatives, reversed attribution, exemption and positive-command explanation',primary=True,boundary='closed',legacy_ids=[]))
s2=add('positive','structure',range(74,84),dict(title='Positive command after prohibition: substitution, priest exception, leftover dispute and second morning',primary=True,boundary='closed',legacy_ids=[]))
c={'initial':'tem_status001_initial_liability_inference','finalpair':'tem_status001_final_pairing','yosiold':'tem_open_c_c40c_review001_v2'};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
C('quotedaddition',64,'In the name of Rabbi Yosi son of Rabbi Hanina they add “also one who places terumah before first fruits.”','Quoted addition initially read in liability context; final exemption reading at4b1 is already preserved in earlier correction',mode='challenged',cond=['Terumah before first fruits'])
add('additionauthority','attributions',64,dict(surface='משום רבי יוסי ברבי חנינא אמרו',role='quoted_authority',candidates=['רבי יוסי ברבי חנינא'],scope='Quoted addition, not final assignment to liability; anonymous reporters not invented as named transmitters',transmission_chain=[]),[c['quotedaddition']])
Q('yosireason',64,'What is Rabbi Yosi son of Rabbi Hanina’s reason?', ['Ordering terumah and first fruits'])
C('firstfruits',64,'מלאתך refers to first fruits.','Verse interpretation in ordering discussion')
C('terumahword',64,'ודמעך refers to terumah.','Verse interpretation in ordering discussion')
C('notdelay',64,'The verse says לא תאחר.','Ordering prohibition supporting the discussion, distinct from final question whether lashes follow')
C('unnamedliable',65,'One side says that giving terumah before first fruits incurs lashes.','Initially unnamed view; later explicit proof identifies Rabbi Elazar',cond=['Terumah before first fruits'])
C('unnamedexempt',65,'The other side says that it does not incur lashes.','Initially unnamed view; later explicit resolution identifies Rabbi Yosi son of Rabbi Hanina',cond=['Terumah before first fruits'])
for k in ['unnamedliable','unnamedexempt']:
 add(k+'.a','attributions',65,dict(surface='ר"א ורבי יוסי ברבי חנינא חד אמר ... וחד אמר',role='position_holder',candidates=['רבי אלעזר','רבי יוסי ברבי חנינא'],scope='Unassigned at this point; initial תסתיים is reversed, final explicit proof establishes mapping',transmission_chain=[]),[c[k]],unc=['Do not assign from order; source continuation required.'])
 add(k+'.p','positions',65,dict(holder_candidates=['רבי אלעזר','רבי יוסי ברבי חנינא'],claim_id=c[k],question_id=None,conditions=['Terumah before first fruits'],local_status='Initially unnamed alternative; final identification follows source proof, not order'),[c[k]],unc=['Candidates remain unordered in initial-stage record.'])
C('reverseproposal',66,'On the contrary, the proposed identification should assign liability to Rabbi Elazar.','Second attribution inference, proved by basket teaching and confirmed4a7')
C('basketone',[66,67],'With two baskets of untithed produce, saying מעשר של זו בזו makes the first basket tithed.','First case in cited Mishnah; exact formula preserves reference without invented allocation arithmetic',holder='Anonymous two-basket Mishnah',cond=['Two baskets of טבל','Says מעשר של זו בזו'])
C('basketfirst',67,'Saying של זו בזו ושל זו בזו makes the first basket tithed.','First result of reciprocal-formula case',holder='Anonymous two-basket Mishnah',cond=['Two baskets','Sequential reciprocal formula'])
C('basketsecond',67,'In that reciprocal-formula case, the second basket is not tithed.','Negative second result retained',holder='Anonymous two-basket Mishnah',cond=['Two baskets','Sequential reciprocal formula'])
C('basketdesignation',67,'Saying מעשרותיהם מעשר כלכלה בחבירתה effects designation.','Third case קרא את השם; do not replace formula with unsupported calculations',holder='Anonymous two-basket Mishnah',cond=['Joint basket designation formula'])
C('elazarbasket',68,'Rabbi Elazar imposes lashes in that case.','Explicit named basket ruling used to establish liability side',holder='רבי אלעזר',cond=['Joint basket tithe designation'])
C('secondbeforefirst',68,'The reason is that he advanced the second tithe in one basket before the first tithe in the other.','Rabbi Elazar’s stated reason; ordinal tithes and different baskets distinguished',holder='רבי אלעזר')
C('elazarfinal',68,'The identification of Rabbi Elazar with the liability view is confirmed: תסתיים.','Final confirmation reverses first proposed assignment, preserving earlier correction as history',holder='רבי אלעזר',cond=['Terumah before first fruits liability dispute'],mode='reconciled')
Q('yosicontradiction',69,'If Rabbi Yosi son of Rabbi Hanina says no lashes, is this not a contradiction within his statements?', ['Final pairing implies exemption','Earlier addition had been read as liability'])
C('exemptattachment',[70,71],'Rabbi Yosi son of Rabbi Hanina’s statement attaches to the exemption clause.','Full split sentence לא רבי יוסי ... אפטורא קאי; confirms existing correction',holder='רבי יוסי ברבי חנינא',mode='reconciled')
C('noactionrule',71,'A prohibition without an action does not receive lashes.','Exemption clause to which the quoted addition attaches',cond=['Prohibition without action'])
C('yosiexempt',71,'Also one who places terumah before first fruits is exempt from lashes.','Final reading of quoted Rabbi Yosi addition, not an additional liability exception',holder='רבי יוסי ברבי חנינא',cond=['Terumah before first fruits'],mode='reconciled')
Q('subdifferent',72,'Why is substitution different, receiving lashes because speech performs an action?', ['Comparison with advancing terumah before first fruits'])
Q('priorityaction',72,'Should advancing terumah before first fruits not also receive lashes because speech performs an action?', ['Spoken designation effects a result','Exemption just established'])
C('subspeechaction',72,'In substitution, his speech effects an action.','Ground of substitution liability invoked by question')
C('priorityspeechaction',72,'Advancing terumah before first fruits likewise effects an action through speech.','Objection premise; not accepted conclusion that lashes follow')
C('positiveconnection',73,'That case is different because the prohibition is connected to a positive command.','Rabbi Avin’s answer to designation-action objection',holder='רבי אבין',cond=['Terumah/tithe ordering case'])
C('titheverse',73,'מכל מעשרותיכם תרימו supplies the positive command.','Verse cited for Rabbi Avin’s explanation')
C('dimireports',74,'Rav Dimi was seated and relating this teaching.','Reporting scene, not a new original-author attribution to Rav Dimi')
add('dimirole','attributions',74,dict(surface='יתיב רב דימי וקאמר לה להא שמעתא',role='transmitter',candidates=['רב דימי'],scope='Relates the preceding teaching; Abaye addresses him',transmission_chain=[]),[c['dimireports']])
Q('everypositive',74,'Does every prohibition connected to a positive command avoid lashes?', ['Abaye questions Rav Dimi about preceding rule'])
add('abayespeaker','attributions',74,dict(surface='א"ל אביי',role='speaker',candidates=['אביי'],scope='Challenges Rav Dimi’s reported rule; not original speaker of answer automatically',transmission_chain=[]),[z['everypositive']])
Q('subcounter',75,'What of substitution, which is connected to a positive command yet receives lashes?', ['Counterexample to general positive-command exemption'])
C('subnotallowed',75,'A person is not permitted to substitute.','Quoted Mishnah prohibition; do not confuse efficacy with permission',holder='Anonymous substitution Mishnah')
C('subeffective',75,'If he substitutes, the substitution takes effect.','Quoted Mishnah efficacy despite prohibition',holder='Anonymous substitution Mishnah',cond=['Substitution performed'])
C('sublashes',75,'He receives forty lashes.','Quoted Mishnah sanction',holder='Anonymous substitution Mishnah',cond=['Substitution performed'])
C('twonegatives',76,'Substitution has two prohibitions and one positive command.','Answer distinguishing substitution from ordinary connected-prohibition case')
C('onenotuproot',76,'One positive command does not uproot two prohibitions.','Explanation of continuing substitution lashes',cond=['Two negative commands','One positive command'])
Q('rapecounter',77,'What of the rapist’s divorce, with one prohibition and one positive command, where the positive command does not remove lashes?', ['Challenge using priest’s outcome in baraita','Not generalized to non-priest'])
C('israelreturn',77,'If the rapist who divorced her is an Israelite, he returns her.','First outcome in quoted baraita',holder='Anonymous divorce baraita',cond=['Rapist divorced the woman','Israelite, not priest'])
C('israelnolashes',77,'That Israelite does not receive lashes.','Second result in non-priest case',holder='Anonymous divorce baraita',cond=['Rapist divorced the woman','Israelite, not priest'])
C('priestlashes',77,'If he is a priest, he receives lashes.','Priestly case, exception explained next',holder='Anonymous divorce baraita',cond=['Rapist divorced the woman','Priest'])
C('priestnoreturn',77,'The priest does not return her.','Negative return rule must not be omitted',holder='Anonymous divorce baraita',cond=['Rapist divorced the woman','Priest'])
Q('priests',78,'Are you speaking of priests?', ['Counterexample relies on priestly divorce case'])
C('priestextra',78,'Priests have a different reason: the Torah gives them additional sanctity.','Answer distinguishes priest exception; no unqualified generalization from it',cond=['Priestly case'])
C('yehudareason',79,'The verse gives a positive command after a prohibition to establish no lashes.','Rabbi Yehuda’s leftover-offering rationale',holder='רבי יהודה',cond=['Remaining offering after morning','Subsequent burning command'])
C('yaakovreject',80,'Rabbi Yaakov rejects that reason: לא מן השם הוא זה.','Explicit opposition to positive-command explanation',holder='רבי יעקב')
C('yaakovreason',80,'Rather, it is a prohibition without an action.','Rabbi Yaakov’s reason for no lashes',holder='רבי יעקב',cond=['Leaving over offering'])
C('yaakovgeneral',80,'A prohibition without an action does not receive lashes.','Rabbi Yaakov’s general principle',holder='רבי יעקב',cond=['No-action prohibition'])
C('yehudainference',80,'It follows that Rabbi Yehuda holds a prohibition without an action does receive lashes.','Anonymous inference from his different explanation; named substantive inferred stance',holder='רבי יהודה',cond=['No-action prohibition, absent other exemption'])
Q('yaakovverse',81,'What does Rabbi Yaakov need והנותר ממנו עד בקר באש תשרופו for?', ['He does not use it for positive-command exemption rationale'])
C('burnsixteen',82,'Bones, sinews and leftovers are burned on the sixteenth.','Quoted Mishnah supplying alternative use of verse',holder='Anonymous burning Mishnah',cond=['Bones, sinews and leftover offering'])
C('burnseventeen',82,'If the sixteenth falls on Shabbat, they are burned on the seventeenth.','Calendar exception to sixteenth-day rule',holder='Anonymous burning Mishnah',cond=['Sixteenth falls on Shabbat'])
C('noshabbatoverride',82,'Their burning does not override Shabbat.','Reason for postponed burning',holder='Anonymous burning Mishnah',cond=['Burning falls on Shabbat'])
C('nofestivaloverride',82,'Their burning does not override a festival.','Separate festival restriction retained',holder='Anonymous burning Mishnah',cond=['Festival'])
Q('morningreason',83,'What is the reason?', ['Hezekiah and school of Hezekiah explain delayed burning rule'])
C('secondmorning',83,'The verse supplies a second morning for its burning.','Hezekiah’s interpretation of והנותר ממנו עד בקר באש תשרופו',holder='חזקיה')
add('schoolhezekiah','attributions',83,dict(surface='וכן תנא דבי חזקיה',role='quoted_authority',candidates=['תנא דבי חזקיה'],scope='School of Hezekiah teaches the same second-morning interpretation; not an invented sequential oral chain',transmission_chain=[]),[c['secondmorning']])
rels=[(64,'firstfruits','yosireason','answer'),(64,'terumahword','yosireason','answer'),(64,'notdelay','yosireason','answer'),(65,'quotedaddition','initial','support'),(66,'reverseproposal','initial','objection'),(68,'elazarbasket','reverseproposal','support'),(68,'secondbeforefirst','elazarbasket','support'),(68,'elazarfinal','initial','correction'),(68,'elazarfinal','finalpair','support'),(71,'exemptattachment','yosicontradiction','answer'),(71,'yosiexempt','quotedaddition','correction'),(71,'yosiexempt','yosiold','local_resolution'),(72,'subspeechaction','subdifferent','support'),(72,'priorityspeechaction','priorityaction','support'),(73,'positiveconnection','priorityaction','answer'),(73,'titheverse','positiveconnection','support'),(75,'subcounter','everypositive','objection'),(75,'sublashes','subcounter','support'),(76,'twonegatives','subcounter','answer'),(76,'onenotuproot','sublashes','support'),(77,'rapecounter','onenotuproot','objection'),(77,'priestlashes','rapecounter','support'),(78,'priestextra','rapecounter','answer'),(79,'yehudareason','positiveconnection','support'),(80,'yaakovreject','yehudareason','objection'),(80,'yaakovgeneral','yaakovreason','support'),(80,'yehudareason','yehudainference','support'),(82,'burnsixteen','yaakovverse','answer'),(82,'noshabbatoverride','burnseventeen','support'),(83,'secondmorning','morningreason','answer'),(83,'secondmorning','burnsixteen','support'),(83,'secondmorning','yaakovverse','answer')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={64:'Quoted Rabbi Yosi addition retained without reintroducing final liability attribution; reason question and three verse components distinguished.',65:'Two views initially unnamed; candidates not assigned by order. Reuse preserved initial-liability-inference correction artifact rather than erase it or call initial תסתיים final.',66:'אדרבה begins competing assignment to Rabbi Elazar, followed by basket evidence; full basket context read.',67:'All three basket designation formulas/results preserved including second basket NOT tithed and effective joint designation; no invented arithmetic.',68:'Elazar explicit lashes ruling, second-tithe-before-first-tithe in other basket reason, final תסתיים assignment distinguished from initial reversed inference.',69:'Explicit internal-contradiction question for Rabbi Yosi; not a new accepted contradictory position.',70:'Fragment לא רבי יוסי... must join4b1 אפטורא קאי; full evidence used.',71:'Final exemption attachment and no-action rule retained, linked to inherited corrected context record; overlapping contextual records are not independent unique-claim counts.',72:'Both substitution-difference and priority-designation-lashes questions; speech effects an action premise not silently dropped.',73:'Rabbi Avin positive-command-linked answer and exact מכל מעשרותיכם תרימו verse preserved.',74:'Rav Dimi reports teaching; Abaye asks general connected-prohibition question; roles explicitly distinct.',75:'Substitution counterexample and Mishnah prohibition/efficacy/forty-lashes claims distinct.',76:'Two prohibitions versus one positive command explains substitution exception, no universal positive-command override.',77:'Rapist divorce challenge includes Israelite return/no-lashes versus priest lashes/no-return; priesthood and negative outcomes explicit.',78:'Priests question and extra-sanctity answer prevent generalizing exceptional case.',79:'Rabbi Yehuda positive-command-after-prohibition explanation, in tannaitic comparison.',80:'Rabbi Yaakov rejects rationale and gives no-action rule; anonymous inference about Yehuda no-action liability separately scoped.',81:'Question about Rabbi Yaakov alternate use of burning verse.',82:'Bones/sinews/leftovers sixteenth-day burning, Shabbat-to-seventeenth exception, neither Shabbat nor festival overridden.',83:'Hezekiah and school of Hezekiah same teaching, reason question and second morning derivation. Context4b14–5a6 read: next efficacy dispute and alternative divorce-baraita arguments are a new unit; do not import its provisional objections as final refutations of this completed core.'}
for i in range(64,84):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous argument with named reports and quoted authorities separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective Gemara discussion',role='anonymous',candidates=[],scope='Framing/inference only; named positions and reporters separately preserved',transmission_chain=[]))
# Earlier correction records used the later continuation as evidence while correcting3a18.
# Include those valid records in new source coverage without changing them or adding new record counts.
ALL=[r for r in S['records'] if r.get('release_state')=='valid']+R
COV=[]
for i in range(64,84):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in ALL if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/temurah',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails'])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'temurah_4a3_4b13_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
