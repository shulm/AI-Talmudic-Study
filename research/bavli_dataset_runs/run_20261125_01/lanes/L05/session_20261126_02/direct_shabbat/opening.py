"""Manually authored Shabbat opening annotations; mechanical schema serialization only."""
import json, hashlib
from pathlib import Path
W=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126/direct_shabbat')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shabbat')
inv=json.loads((J/'source_inventory.json').read_text(encoding='utf-8'))
meta=json.loads((J/'JOB.json').read_text(encoding='utf-8'))
assert json.loads((J/'OWNER.json').read_text())=={'owner':'L05/shabbat','epoch':2}
records=[]
def rid(x): return 'sha_open_'+x
def ev(indices):
 return [{'segment_id':inv[i]['id'],'start_char':0,'end_char':len(inv[i]['text']),'quote':inv[i]['text']} for i in indices]
def add(k,layer,indices,content,links=(),unc=(),origin='source_paraphrase'):
 records.append(dict(id=rid(k),layer=layer,evidence=ev(indices),content=content,origin=origin,uncertainty=list(unc),links=[rid(x) for x in links])); return k
def claim(k,i,prop,cond=(),mode='asserted',scope='Local discussion of the opening Mishnah',holder=None):
 add(k,'claims',[i],dict(proposition=prop,conditions=list(cond),scope=scope,assertion_mode=mode))
 if holder:
  add('p_'+k,'positions',[i],dict(holder_candidates=[holder],claim_id=rid(k),question_id=None,conditions=list(cond),local_status=mode),[k])
def q(k,i,form,cond=(),status='partial'):
 add(k,'questions',[i],dict(formulation=form,question_origin='explicit',conditions=list(cond),answer_set_status=status))
def edge(k,indices,a,b,rel):
 add(k,'edges',indices,dict(source_id=rid(a),target_id=rid(b),relation=rel,explicitness='source_explicit'),[a,b])
def attr(k,i,name,role='speaker',scope='',chain=(),unc=()):
 add(k,'attributions',[i],dict(surface=name,role=role,candidates=[name],scope=scope or 'Speech identified in this segment',transmission_chain=list(chain)),unc=unc)
for k,a,b,title in [('s0',0,5,'Opening Mishnah: carrying between domains'),('s1',6,20,'Two that are four: comparison with Shevuot and terminology'),('s2',21,27,'Counting exempt cases in the Mishnah'),('s3',28,28,'Two people jointly performing a labor'),('s4',29,31,'Removal of the body versus movement of the hand')]:
 add(k,'structure',range(a,b+1),dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
roles={0:'Mishnah heading',1:'Mishnah explanatory question',2:'Mishnah case rulings',3:'Mishnah case rulings',4:'Mishnah case rulings',5:'Mishnah case rulings',6:'Quotation of parallel Mishnah',7:'Continuation of quotation',8:'Continuation of quotation',9:'Continuation of quotation',10:'Question comparing formulations',11:'Initial answer, subsequently rejected',12:'Objection to initial answer',13:'Hypothetical repair and objection',14:'Rav Pappa replacement answer',15:'Question and answer',16:'Objection and Rav Ashi answer',17:'Request for evidence and proof',18:'Question and explanation of terminology',19:'Ravina supporting inference',20:'Rava alternative reading',21:'Rav Mattana question to Abaye',22:'Counterquestion in dialogue',23:'Reply introducing distinction; continues next segment',24:'Continuation of distinction',25:'Objection citing Shmuel',26:'Qualification of Shmuel',27:'Renewed objection and answer',28:'Question, Rabbi baraita and independently reported corroboration',29:'Rav question to Rabbi, reply and explanation',30:'Rabbi Hiyya admonishes Rav',31:'Rabbi Hiyya continuation and supporting baraita'}
for i in range(32):
 voice='Anonymous Mishnah' if i<6 else ('Anonymous Gemara and quoted sources' if i not in [14,19,20,21,30,31] else {14:'Rav Pappa',19:'Ravina',20:'Rava',21:'Rav Mattana',30:'Rabbi Hiyya',31:'Rabbi Hiyya'}[i])
 add('u'+str(i),'utterances',[i],dict(textual_voice=voice,discourse_role=roles[i],composition='composite' if i in [2,3,4,5,13,15,16,17,18,24,25,27,28,29,30,31] else 'atomic'))
 if i<6 or i in [6,7,8,9,10,11,12,13,15,17,18,22,23,24,25,26,27,28]:
  add('anon'+str(i),'attributions',[i],dict(surface='Anonymous Mishnah' if i<6 else 'Anonymous discussion / anonymous quoted source',role='anonymous',candidates=[],scope=roles[i],transmission_chain=[]),unc=['Dialogue participants of 2b:16–17 are not newly named in the source; do not assign by alternation alone.'] if i in [22,23,24] else [])
claim('c0',0,'The Mishnah enumerates two Sabbath transfers that are four inside, and two that are four outside.',scope='Opening numerical heading',holder='Anonymous Mishnah')
q('q1',1,'How are these enumerated transfers instantiated?')
claim('c2a',2,'The poor person is liable; the householder is exempt when the poor person reaches inward and gives into the householder’s hand.', ['Poor person outside; householder inside','Poor person performs the transfer'],holder='Anonymous Mishnah')
claim('c2b',2,'The poor person is liable; the householder is exempt when the poor person reaches inward, takes from the householder’s hand and carries outward.', ['Poor person outside; householder inside','Poor person performs the transfer'],holder='Anonymous Mishnah')
claim('c3a',3,'The householder is liable and the poor person exempt when the householder reaches outward and gives into the poor person’s hand.', ['Poor person outside; householder inside'],holder='Anonymous Mishnah')
claim('c3b',3,'The householder is liable and the poor person exempt when the householder reaches outward, takes from the poor person’s hand and carries inward.', ['Poor person outside; householder inside'],holder='Anonymous Mishnah')
claim('c4a',4,'Both are exempt when the poor person extends his hand inward and the householder takes from it.', ['Removal and placement are divided between the two participants'],holder='Anonymous Mishnah')
claim('c4b',4,'Both are exempt when the householder places into the poor person’s extended hand and the poor person withdraws it outward.', ['Poor person outside; householder inside'],holder='Anonymous Mishnah')
claim('c5a',5,'Both are exempt when the householder extends his hand outward and the poor person takes from it.', ['Poor person outside; householder inside'],holder='Anonymous Mishnah')
claim('c5b',5,'Both are exempt when the poor person places into the householder’s extended hand and the householder withdraws it inward.', ['Poor person outside; householder inside'],holder='Anonymous Mishnah')
for i,p in [(6,'The parallel Mishnah enumerates two oaths that are four.'),(7,'The parallel Mishnah enumerates two awarenesses of impurity that are four.'),(8,'The parallel Mishnah enumerates two appearances of lesions that are four.'),(9,'The parallel Mishnah enumerates two Sabbath transfers that are four.')]: claim('c'+str(i),i,p,scope='Quoted parallel Mishnah',holder='Anonymous quoted Mishnah')
q('q10',10,'Why does this Mishnah count inside and outside separately, while the parallel Mishnah says only two that are four?')
claim('c11',11,'Initial answer: this tractate’s main subject is Sabbath, so it teaches primary and derivative labors; the parallel tractate teaches only primary labors.',mode='rejected',scope='Rejected by 2b:6–7, replaced at 2b:8')
q('q12',12,'If the primary labors are outward transfers, are there not only two?')
claim('c12',12,'There are only two outward transfers for the proposed count of primary labors.',mode='challenged',scope='Objection to c11')
claim('c13a',13,'A possible defense would count some liable and some exempt cases.',mode='hypothetical',scope='Attempted defense of initial answer; rejected in same segment')
claim('c13b',13,'The parallel Mishnah likens these cases to lesion appearances, all of which entail liability, so all the transfer cases counted there must entail liability.',scope='Analogy defeating the hypothetical exemption count')
q('q13',13,'Does the comparison with lesion appearances not require all the counted cases to entail liability?')
claim('c14',14,'Here, where Sabbath is the primary topic, liable and exempt cases are taught; there only liable cases are taught.',holder='Rav Pappa')
attr('a14',14,'רב פפא',scope='Replacement answer about liable and exempt cases')
q('q15',15,'Which liable transfers are counted, given that outward transfers number only two?')
claim('c15',15,'The four liable transfers comprise two outward and two inward transfers.',scope='Answer supporting Rav Pappa’s count')
q('q16',16,'But does the Mishnah not say outward transfers?')
claim('c16',16,'The tanna also calls inward transfer outward transfer.',holder='Rav Ashi')
attr('a16',16,'רב אשי',scope='Terminological explanation; not Rav himself')
q('q17',17,'From where is this terminology established?')
claim('c17a',17,'The cited Mishnah states that one who transfers from domain to domain is liable.',scope='Quoted Mishnah',holder='Anonymous quoted Mishnah')
claim('c17b',17,'That wording includes bringing from public to private domain yet calls it outward transfer.',scope='Inference from cited Mishnah')
q('q18',18,'What explains this terminology?')
claim('c18',18,'The tanna calls every removal of an object from its place outward transfer.',scope='Terminological rationale, not an unrestricted liability rule')
claim('c19',19,'The opening Mishnah itself supports this terminology: it says outward transfers and immediately explains an inward transfer.',holder='Ravina')
attr('a19',19,'רבינא',scope='Supporting inference from opening Mishnah')
claim('c20',20,'Rava reads the Mishnah as enumerating domains: Sabbath domains are two.',scope='Alternative reading to preceding explanations; not merged with them',holder='Rava')
attr('a20',20,'רבא',scope='Alternative interpretation of heading')
q('q21',21,'The Mishnah counts eight; are there not twelve?')
attr('a21',21,'רב מתנה',scope='Question explicitly addressed to Abaye; Abaye is addressee, not co-author of question')
q('q22',22,'On your reasoning, should the count not be sixteen?')
claim('c23',23,'The respondent says that the sixteen-case problem is not difficult and begins a distinction.',scope='Incomplete sentence completed at 3a:1')
claim('c24a',24,'The first clause’s exempt-and-permitted cases are not counted.',scope='Counting distinction in the dialogue')
claim('c24b',24,'The latter clause’s exempt-but-forbidden cases remain a difficulty for the count.',mode='challenged',scope='Remaining counting problem')
q('q25',25,'Are any Sabbath cases exempt and permitted, given Shmuel’s rule?')
claim('c25',25,'Shmuel states that Sabbath exemptions mean exempt but forbidden except trapping a deer, trapping a snake, and opening an abscess, which are exempt and permitted.',scope='Quoted rule, scoped to acts by following answer; named exceptions retain their source-specific cases',holder='Shmuel')
attr('a25',25,'שמואל','quoted_authority',scope='Quoted rule used in objection; restriction follows in 3a:3')
claim('c26a',26,'Shmuel’s statement is needed for exemptions involving performance of an act.',scope='Qualification of quoted Shmuel rule')
claim('c26b',26,'There are many exempt-and-permitted cases where no act is performed.',scope='Reply to objection of 3a:2')
q('q27',27,'Nevertheless, are there not twelve cases?')
claim('c27a',27,'The Mishnah counts exempt cases that can develop into liability for a sin offering.',scope='Answer about count of exempt cases')
claim('c27b',27,'It does not count exempt cases that cannot develop into liability for a sin offering.',scope='Negative part of counting criterion')
q('q28',28,'Why are both exempt when the labor was performed between them?')
claim('c28a',28,'Rabbi derives from בעשותה that liability requires doing the whole act, not part of it.',scope='Baraita interpreting Leviticus 4:27',holder='Rabbi')
claim('c28b',28,'One individual who performs the act is liable; two who jointly perform it are exempt.',scope='Rabbi’s baraita, corroborated by reported group statement',holder='Rabbi')
claim('c28c',28,'The group reported through Rabbi Hiyya bar Gamda likewise expounds that one who performs it is liable and two who perform it are exempt.',scope='Separate corroborating transmission; retain occurrence',holder='Unnamed group')
attr('a28a',28,"ר'",'quoted_authority',scope='Baraita interpretation of בעשותה')
attr('a28b',28,'רב חייא בר גמדא','transmitter',scope='Reports a statement issued by an unnamed group',chain=['רב חייא בר גמדא','חבורה'])
attr('a28c',28,'חבורה','collective',scope='Original reported collective voice, not identified individuals')
q('q29a',29,'If another person loads food and drink onto a person who then carries them out, is removal of the body like removal of an object, making him liable?', ['Another loads him; he carries outside'])
claim('c29a',29,'One possibility is that moving the body counts as removal of the object and entails liability; the alternative denies this.',mode='queried',scope='Rav’s alternatives; not two asserted views',holder='Rav')
claim('c29b',29,'He is liable and his body is not analogous to his hand.', ['Another loads him with food/drink; he carries outside'],holder='Rabbi')
q('q29b',29,'Why does the body differ from the hand?')
claim('c29c',29,'The body rests, while the hand does not rest.',scope='Explanation of body/hand distinction in the local case')
attr('a29a',29,'רב',scope='Questioner, not author of Rabbi’s ruling')
attr('a29b',29,'רבי',scope='Respondent; answers חייב ואינו דומה לידו')
claim('c30a',30,'Rabbi Hiyya admonishes Rav not to ask Rabbi about another tractate while Rabbi is occupied with this tractate, lest it not be on his mind.', ['Rabbi occupied with another tractate'],scope='Pedagogic admonition',holder='Rabbi Hiyya')
claim('c30b',30,'Had Rabbi not been a great man, Rav might have embarrassed him through an inadequate answer.',mode='hypothetical',scope='Counterfactual warning, not assertion that Rabbi gave a wrong answer',holder='Rabbi Hiyya')
attr('a30',30,"ר' חייא",scope='Admonishes Rav; Rav and Rabbi are not speakers of the admonition')
claim('c31a',31,'In the present case Rabbi answered correctly.',scope='Continuation of Rabbi Hiyya’s speech',holder='Rabbi Hiyya')
claim('c31b',31,'A baraita rules that one loaded with food and drink before nightfall who takes them outside after dark is liable, because this is not like his hand.', ['Loaded before nightfall','Takes outside after nightfall'],scope='Cited baraita supporting Rabbi’s answer',holder='Anonymous baraita')
attr('a31',31,'תניא','anonymous',scope='Anonymous baraita quoted in support')
edge('e1',[2,3,4,5],'u2','q1','answer')
edge('e2',[11],'c11','q10','answer')
edge('e3',[12],'q12','c11','objection')
edge('e4',[13],'c13b','c13a','objection')
edge('e5',[14],'c14','c11','correction')
edge('e6',[14],'c14','q10','answer')
edge('e7',[15],'c15','q15','answer')
edge('e8',[16],'c16','q16','answer')
edge('e9',[17],'c17b','c16','support')
edge('e10',[18],'c18','q18','answer')
edge('e11',[19],'c19','c16','support')
edge('e12',[20],'c20','q10','answer')
edge('e13',[22],'q22','q21','objection')
edge('e14',[23,24],'c24a','q22','answer')
edge('e15',[25],'c25','c24a','objection')
edge('e16',[26],'c26a','c25','qualification')
edge('e17',[26],'c26b','q25','answer')
edge('e18',[27],'c27a','q27','answer')
edge('e19',[28],'c28a','q28','answer')
edge('e20',[28],'c28c','c28b','support')
edge('e21',[29],'c29b','q29a','answer')
edge('e22',[29],'c29c','q29b','answer')
edge('e23',[31],'c31b','c29b','support')
edge('e24',[31],'c31a','c30b','qualification')
# Source-based second pass notes: omissions, negation, alternative explanations and reporting.
notes={0:'Heading retained without forcing a unique interpretation; alternatives appear at 2b:8–14.',1:'Explicit explanatory question retained.',2:'Separated giving and taking cases and both liability statuses.',3:'Separated giving and taking cases and both liability statuses.',4:'Separated two shared-act cases; exemption not equated with permission.',5:'Separated two shared-act cases; exemption not equated with permission.',6:'Parallel oath heading retained, not discarded as context.',7:'Impurity heading retained.',8:'Lesion heading retained; later inference uses its liability scope.',9:'Parallel Sabbath heading retained as separate occurrence.',10:'Both formulations and comparison question retained.',11:'Initial explanation marked rejected after reading 2b:6–8.',12:'Numerical objection preserved.',13:'Hypothetical defense separated from refutation and analogy.',14:'Replacement answer attributed to Rav Pappa, not Rav.',15:'Question and answer distinguished; inbound and outbound counts retained.',16:'Rav Ashi distinguished from Rav; objection and terminological answer retained.',17:'Quoted rule distinguished from inclusive inference and request for evidence.',18:'Terminology not expanded into claim that any movement incurs liability.',19:'Ravina inference and source basis retained.',20:'Rava alternative retained separately; no forced harmonization.',21:'Rav Mattana question retained; Abaye is addressee only.',22:'Counterquestion retained without forcing unnamed speaker attribution.',23:'Read through 3a:1 to complete sentence.',24:'Exempt/permitted distinction and surviving difficulty both retained.',25:'Shmuel exceptions retained; next sentence restricts statement to acts.',26:'Positive act restriction and no-act exemption class both retained.',27:'Renewed question, positive criterion and negated criterion retained.',28:'Rabbi baraita and Hiyya bar Gamda/group transmission separated; joint act exception retained.',29:'Rav/Rabbi roles separated; queried alternatives not asserted dispute; body/hand distinction retained.',30:'Counterfactual warning not mistaken for rejected answer.',31:'Baraita timing conditions retained; reread continuation 3b:3–10 which starts Abaye hand inquiry.'}
coverage=[]
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
for i in range(32):
 for layer in layers:
  rs=[r['id'] for r in records if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==inv[i]['id'] for e in r['evidence'])]
  coverage.append(dict(segment_id=inv[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if rs else 'none_found_after_pass',record_ids=rs,rationale=('Source reread: '+notes[i]) if layer=='reconciliation' else ('Direct source pass for '+layer+': '+notes[i]+(' No separate record of this layer found in this segment.' if not rs else ''))))
proposal={k:meta[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
proposal.update(owner='L05/shabbat',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=records,coverage=coverage,open_tails=[])
out=W/'opening_2a1_3b2_v1.json'
blob=(json.dumps(proposal,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
if out.exists(): assert out.read_bytes()==blob
else: out.write_bytes(blob)
print(json.dumps({'path':str(out),'records':len(records),'sha256':hashlib.sha256(blob).hexdigest()}))
