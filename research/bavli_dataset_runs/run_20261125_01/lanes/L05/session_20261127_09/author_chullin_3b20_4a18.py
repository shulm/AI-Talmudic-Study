"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='e3820a8f1a9958659f65f5fd706c5ba00b7c2962a74e4157aee272ec18ccd165';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[52]['ref']=='Chullin 3b:20' and I[71]['ref']=='Chullin 4a:18'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.s2709.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('kuti','structure',range(52,71),dict(title='Kuti slaughter: supervision and consumption test, hidden sample, established practice and matzah dispute',primary=True,boundary='closed',legacy_ids=[]))
s2=add('mumar','structure',71,dict(title='Rava on appetite-driven eater of carcasses: knife inspection and permitted slaughter; continuation follows',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
C('supervised',52,'A Kuti’s slaughter is permitted when an Israelite stands over him.','Baraita’s local rule; later5b8–6a1 restrictions are separate source occurrences, not silently merged',holder='Anonymous slaughter baraita',cond=['Israelite stands over Kuti during slaughter'])
C('olivetest',52,'If one comes and finds that he has already slaughtered, cut off an olive-sized portion and give it to him.','Post-slaughter consumption test',holder='Anonymous slaughter baraita',cond=['No observation; arrives after slaughter'])
C('atepermitted',52,'If the Kuti eats that portion, one may eat from his slaughter.','Positive outcome of consumption test',holder='Anonymous slaughter baraita',cond=['Arrived after slaughter','Kuti eats offered olive-sized portion'])
C('notateforbidden',52,'If he does not eat it, one may not eat from his slaughter.','Negative outcome retained',holder='Anonymous slaughter baraita',cond=['Arrived after slaughter','Kuti does not eat offered portion'])
C('birdsample',[53,54],'Similarly, if one finds a דקוריא of birds in his possession, cut off the head of one and give it to him.','Full split-folio test; source grouping term retained without fixed numerical count',holder='Anonymous slaughter baraita',cond=['Bird group in Kuti possession'])
C('birdyes',[53,54],'If he eats the sampled head, one may eat from his slaughter.','Bird-test positive outcome, procedure qualified below',holder='Anonymous slaughter baraita',cond=['Bird group found','Kuti eats head offered'])
C('birdno',[53,54],'If he does not eat it, one may not eat from his slaughter.','Bird-test negative outcome',holder='Anonymous slaughter baraita',cond=['Bird group found','Kuti does not eat sampled head'])
C('abayehead',55,'Abaye draws his inference from the opening clause.','Named textual inference, not name-order attribution',holder='אביי')
C('abayeinout',55,'Only standing over him permits; going in and out does not suffice.','Abaye’s inference from opening supervision condition',holder='אביי',cond=['Israelite intermittently enters and leaves rather than continuously standing over'])
C('ravatail',56,'Rava draws his inference from the latter clause.','Named textual inference',holder='רבא')
C('ravainout',56,'The test is required when one arrives after slaughter, but going in and out suffices.','Rava’s inference from latter post-slaughter case',holder='רבא',cond=['Israelite intermittently enters and leaves'])
Q('abayeproblem',57,'Does the latter clause not pose a difficulty for Abaye?', ['Abaye disallows intermittent supervision','Latter clause singles out arriving after slaughter'])
C('abayeanswer',57,'Going in and out is also called coming and finding that he slaughtered.','Answer on behalf of Abaye broadens latter clause scope',holder='אביי',cond=['Intermittent supervision'])
Q('ravaproblem',57,'Does the opening clause not pose a difficulty for Rava?', ['Rava permits intermittent supervision','Opening says Israelite stands over him'])
C('ravaanswer',57,'Going in and out is also considered like standing over him.','Answer on behalf of Rava interprets opening clause',holder='רבא',cond=['Intermittent supervision'])
Q('oneproper',58,'Why does one head establish permission—should we not fear that only this bird was slaughtered properly?', ['Bird-group consumption test','One head sampled'])
C('hidden',59,'The birds are placed under his כנפיו.','Rav Menashe’s concealment procedure answering selective identification concern; retain source wording',holder='רב מנשה',cond=['Bird-group test'],unc=['The terse source does not explicitly identify every actor or describe the garment; do not turn the mnemonic into a legal condition.'])
add('mnemonic','utterances',59,dict(textual_voice='Parenthetical mnemonic',discourse_role='סימן מכני"ס איזמ"ל בזכרי"ם is a mnemonic, not an independently asserted rule',composition='atomic'),origin='literal')
Q('internalmark',60,'Perhaps he had placed a distinguishing mark inside it?', ['Concealed bird-sample procedure','Kuti might still identify properly slaughtered specimen'])
C('mash',60,'It is mashed—דממסמס ליה מסמוסי.','Rav Mesharshiya’s response preventing recognition by identifying mark; source pronoun retained',holder='רב משרשיא',cond=['Sample used in bird test'],unc=['Exact object of the pronoun is not independently expanded beyond the sampled material in this terse answer.'])
Q('birdtorah',61,'Perhaps the Kutim hold that bird slaughter is not required by Torah law?', ['Consumption of a bird would then not establish our slaughter standard'])
Q('fivewritten',62,'On your reasoning, are שהייה, דרסה, חלדה, הגרמה and עיקור written explicitly?', ['Challenge based on requirement not explicit in written text','Five slaughter defects listed in full'])
C('establishedfive',63,'Once they have established observance of those rules, their observance is established.','Response concerning the listed slaughter defects',cond=['They have established the relevant practice'])
C('establishedbird',63,'Likewise, once they have established this practice, it is established.','Analogous response for bird slaughter; not proof merely from text being written',cond=['Established bird-slaughter practice'])
C('tannaitic',64,'Acceptance of established practice where a rule is not written is a tannaitic dispute.','Introduction to matzah baraita; actual disputed axis clarified at4a17')
C('matzahallowed',64,'Kuti matzah may be eaten.','First tanna’s matzah rule',holder='תנא קמא — ברייתת מצת כותי',cond=['Kuti matzah'])
C('matzahobligation',64,'A person fulfills the Passover obligation with it.','First tanna’s additional ritual-use claim',holder='תנא קמא — ברייתת מצת כותי',cond=['Kuti matzah','Passover obligation'])
C('raforbids',65,'ר"א forbids it.','Opposed matzah position; source abbreviation preserved',holder='ר"א',cond=['Kuti matzah'])
C('radetails',65,'The Kutim are not expert in the fine points of mitzvot like Israel.','ר"א reason for matzah prohibition',holder='ר"א')
C('rsbgcareful',66,'In every mitzvah they have established, Kutim are much more exacting than Israel.','Rabban Shimon ben Gamliel’s conditional statement',holder='רשב"ג',cond=['Mitzvah they have established in practice'])
Q('obvious',67,'Is the permission and fulfillment statement not obvious?', ['Quoted first tanna’s matzah rule'])
C('possibleunguarded',67,'One might have thought they are not expert in guarding the matzah.','Suggested concern rejected by first tanna’s teaching',mode='rejected',cond=['שימור for matzah'])
C('guardingaffirmed',67,'The teaching rules out that concern about guarding.','Explanation of first tanna’s matzah ruling; not unrestricted endorsement of all Kuti practices')
C('raguarding',67,'ר"א holds they are not expert in guarding.','Specific explanation of prohibition, separate from first tanna’s rejected concern',holder='ר"א',cond=['שימור for matzah'])
Q('sameastk',68,'Is Rabban Shimon ben Gamliel’s position not the same as the first tanna’s?', ['Both apparently accept Kuti practice'])
C('firstaxis',68,'The initial answer distinguishes a rule written explicitly that they have not established in practice.','First proposed axis, rejected by wording objection next',mode='rejected',cond=['Written rule','Not established in practice'])
C('tkwritten',68,'The first tanna is initially explained as trusting the written rule even without established practice.','Provisional interpretation only; rejected as the dispute’s axis',holder='תנא קמא — ברייתת מצת כותי',mode='rejected',cond=['Written','No established practice'])
C('rsbgwritten',68,'Rabban Shimon ben Gamliel is initially explained as requiring established practice even for a written rule.','Provisional interpretation only; not final classification of written/unpracticed case',holder='רשב"ג',mode='rejected',cond=['Written rule','Only if established in practice'])
Q('ifwording',69,'If so, should the wording not be “if they established” rather than “every mitzvah they established”?', ['Initial written-but-unpracticed interpretation','כל versus אם wording'])
C('finalaxis',70,'Instead the dispute concerns a rule not written explicitly that they have established in practice.','Revised and accepted dispute axis',cond=['Not explicitly written','Established in practice'])
C('tknonwritten',70,'The first tanna does not accept the practice when the rule is not written, even though they have established it.','Final explanation of first tanna’s scope',holder='תנא קמא — ברייתת מצת כותי',cond=['Not explicitly written','Established practice'])
C('rsbgnonwritten',70,'Rabban Shimon ben Gamliel accepts it because they have established the practice.','Final explanation; practical establishment sufficient in unwritten case',holder='רשב"ג',cond=['Not explicitly written','Established practice'])
C('ravaappetite',71,'For an Israelite apostate who eats carcasses for appetite, one checks a knife and gives it to him.','Rava’s resumed statement; checking is performed before handing over, not presumed self-inspection by offender',holder='רבא',cond=['ישראל מומר','Eats נבילות לתיאבון','Knife checked before given'])
C('ravaeat',71,'One may eat from that person’s slaughter.','Rava’s permission conditioned on prior knife checking and appetite motive; continuation distinguishes lack of inspection effort, not spiteful violation',holder='רבא',cond=['Israelite who eats carcasses for appetite','Knife checked and given to him'])
rels=[(55,'supervised','abayeinout','support'),(56,'olivetest','ravainout','support'),(57,'abayeanswer','abayeproblem','answer'),(57,'ravaanswer','ravaproblem','answer'),(58,'oneproper','birdyes','objection'),(59,'hidden','oneproper','answer'),(60,'internalmark','hidden','objection'),(60,'mash','internalmark','answer'),(61,'birdtorah','birdyes','objection'),(62,'fivewritten','birdtorah','objection'),(63,'establishedfive','establishedbird','analogy'),(63,'establishedbird','birdtorah','answer'),(64,'tannaitic','establishedbird','qualification'),(65,'radetails','raforbids','support'),(67,'guardingaffirmed','obvious','answer'),(67,'guardingaffirmed','possibleunguarded','objection'),(67,'raguarding','raforbids','support'),(68,'firstaxis','sameastk','answer'),(69,'ifwording','firstaxis','objection'),(70,'finalaxis','firstaxis','correction'),(70,'finalaxis','sameastk','answer'),(70,'tknonwritten','tkwritten','correction'),(70,'rsbgnonwritten','rsbgwritten','correction'),(70,'rsbgnonwritten','tannaitic','support'),(70,'tknonwritten','tannaitic','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
Q('whenpermitted',52,'Under what circumstances is a Kuti’s slaughter permitted?', ['Baraita opening permission','במה דברים אמורים introduces supervision condition'])
E('scopeanswer',52,'supervised','whenpermitted','answer')
notes={52:'Scope question, continuous-supervision permission, olive-sized test and both eating/refusal outcomes. Baraita local rule kept distinct from later5b8–6a1 restriction.',53:'Similarly-found-bird-group fragment joined to4a1; no numeric group count invented.',54:'Complete bird sample/head, eat-permit/refuse-forbid outcomes with preceding fragment evidence.',55:'Abaye expressly infers from opening; intermittent supervision insufficient on his view.',56:'Rava expressly infers from latter clause; intermittent supervision sufficient on his view.',57:'Both named objections and both interpretive responses retained, without forcing agreement.',58:'Sampling objection: only selected bird might be properly slaughtered; no assumed uniform flock status.',59:'Rav Menashe concealment answer, exact כנפיו wording and actor ambiguity retained; parenthetical mnemonic separately identified as mnemonic.',60:'Internal-mark question and Rav Mesharshiya mashing answer with restrained pronoun interpretation.',61:'Perhaps Kuti rejection of Torah bird-slaughter obligation posed as question, not accepted belief.',62:'Counter-question lists all five slaughter defects in exact evidence; no one defect omitted.',63:'Established observance answers both five-defect and bird-slaughter concern; not a rule that unwritten practices always trusted.',64:'Tannaitic dispute introduction; matzah edible and fulfills Passover obligation separately recorded.',65:'ר"א prohibition and lack-of-expertise reason; abbreviation preserved rather than silently expanded.',66:'RSBG greater exactness explicitly conditioned on established practice.',67:'Obviousness question; possible guarding ignorance rejected by first tanna, affirmed separately as ר"א rationale.',68:'Same-as-first-tanna question; written-but-unestablished first distinction retained as rejected, both proposed views scoped locally.',69:'כל versus אם wording question defeats first distinction.',70:'Accepted dispute instead unwritten-but-established; first tanna distrust versus RSBG trust, distinct from prior rejected interpretation.',71:'Rava resumed statement restricted to appetite-driven carcass eater and checked knife. Context4a19–5a14: no-effort concern preserves need to check; competing support interpretations concern distinct apostate categories; final Rav Anan idolatry refutation is not a refutation of this appetite-driven Rava claim. Further5b8–6a1 Kuti restriction read as separate future occurrence; all context uncredited.'}
for i in range(52,72):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous baraita/argument framing with named views and replies separately attributed',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous framing or quoted baraita',role='anonymous',candidates=[],scope='Anonymous connective material only; does not replace named holder and speaker records',transmission_chain=[]))
COV=[]
for i in range(52,72):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s2])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_3b20_4a18_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
