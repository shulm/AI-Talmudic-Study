import json,hashlib,copy
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'readings/meilah_supplement002.json'
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert H(P)=='3b264d8bd1e4f1e0d4f7c26f4e47d6f2031cc1c5c395693eb10407bc2c2f5994'
base=json.loads(P.read_text(encoding='utf-8'))
jobpath=ROOT/'jobs/bavli_meilah_supplement002.json';job=json.loads(jobpath.read_text(encoding='utf-8-sig'))
assert H(job['source']['path'])==job['source']['sha256']
for x in job['common_documents']:assert H(x['path'])==x['sha256']
src=json.loads(Path(job['source']['path']).read_text(encoding='utf-8-sig'))
texts={f'Meilah {i//2+1}{"a" if i%2==0 else "b"}:{j+1}':t for i,ls in enumerate(src['text']) for j,t in enumerate(ls)}
old=base['records'];new=[];remap={};retire={};notes=[]
def ref(loc):return loc if loc.startswith('Meilah ') else 'Meilah '+loc
def ev(loc,needle=None):
    rr=ref(loc);s=texts[rr];start=s.index(needle) if needle else 0;end=start+len(needle) if needle else len(s)
    return dict(segment_id=rr,start_char=start,end_char=end,quote=s[start:end])
def add(layer,loc,content,links=None,origin='source_paraphrase',uncertainty=None,supersedes=None,needle=None,evidence=None):
    r=dict(id=f'meilah_supplement002_completion001.{layer}.{len(new)+1:04d}',layer=layer,evidence=evidence or [ev(loc,needle)],content=content,origin=origin,uncertainty=uncertainty or [],links=links or [],supersedes=supersedes)
    new.append(r)
    if supersedes:remap[supersedes]=r['id']
    return r['id']
def prev(layer,loc):return [r for r in old if r['layer']==layer and r['evidence'][0]['segment_id']==ref(loc)]
def cid(loc,n=0):return prev('claims',loc)[n]['id']
def replacement(r,content=None,**kwargs):
    return add(r['layer'],r['evidence'][0]['segment_id'],content or copy.deepcopy(r['content']),links=r['links'][:],origin=r['origin'],uncertainty=kwargs.pop('uncertainty',r['uncertainty'][:]),supersedes=r['id'],evidence=kwargs.pop('evidence',r['evidence']),**kwargs)
def fixclaim(loc,n,prop=None,mode=None,conditions=None,uncertainty=None):
    r=prev('claims',loc)[n];c=copy.deepcopy(r['content'])
    if prop:c['proposition']=prop
    if mode:c['assertion_mode']=mode
    if conditions:c['conditions']=conditions
    return replacement(r,c,uncertainty=uncertainty or r['uncertainty'])

# Actual second-pass corrections: assertion force, reported roles, and local scope.
fixclaim('3b:11',1,mode='asserted')
fixclaim('5a:1',0,mode='queried');fixclaim('5a:1',1,mode='queried')
fixclaim('5a:2',0,prop='Rabbi Zeira says לא דייקא מתני\' דלא כחזקיה ודלא כרבי יוחנן, introducing the ensuing precision/inference argument.',uncertainty=['The compressed negative phrasing is preserved rather than resolved into a definitive final verdict for or against both named views.'])
fixclaim('5b:7',0,mode='hypothetical');fixclaim('5b:7',1,mode='reconciled')
fixclaim('6a:12',1,mode='hypothetical')
fixclaim('6b:13',1,mode='asserted')
fixclaim('7a:11',0,prop='An unnamed elder in Kefar Pani reports to Rabbi Shimon that Rabbi Akiva used to say sprinkling benefits exited material.',uncertainty=['The source uses אמר לי אומר היה, not an explicit interrogative; Rabbi Shimon responds הן.'])
fixclaim('7a:11',2,prop='Rabbi Shimon reports that his Galilean colleagues objected: the material is invalid, so how can sprinkling secure acceptance for it?',mode='challenged')
fixclaim('7b:7',2,mode='challenged',conditions=['Rabbi Yohanan’s two-guilt-offering hypothetical; proposed treatment as one body'])
fixclaim('7b:14',1,prop='The meat is priestly property, supplied as the premise of the objection.',mode='asserted')
fixclaim('7b:17',1,prop='The meat belongs to the owners, supplied as the premise of the objection.',mode='asserted')

# Replace descriptive English mixed-voice labels with actual named candidates and roles.
# Default is an unnamed textual voice, never a fabricated person called "anonymous".
PRIMARY={
'3b:8':('רב גידל','transmitter',['רב גידל','רב']),
'3b:9':('רב פפא','speaker',[]),
'3b:12':('רבי אבא','speaker',[]),
'3b:13':('רב אשי','speaker',[]),
'3b:15':('רבא','speaker',[]),
'4a:3':('רבינא','speaker',[]),
'4a:4':('אילפא','quoted_authority',['רבינא','אילפא']),
'4a:5':('רב אשי','speaker',[]),
'4b:11':('רבי יהושע','position_holder',[]),
'4b:12':('רבי יהושע','quoted_authority',[]),
'4b:13':('רבי יהושע','quoted_authority',[]),
'4b:14':('בר קפרא','speaker',[]),
'5a:1':('בר קפרא','speaker',[]),
'5a:2':('רבי זירא','speaker',[]),
'5a:10':('רב יוסף','speaker',[]),
'5b:1':('רב אסי','speaker',[]),
'5b:5':('ריש לקיש','speaker',[]),
'5b:6':('רבי יוחנן','speaker',[]),
'6a:1':('רבי שמעון','quoted_authority',[]),
'6a:2':('רבי שמעון','quoted_authority',[]),
'6a:9':('רבי שמעון','quoted_authority',[]),
'6a:10':('רבי שמעון','quoted_authority',[]),
'6b:2':('רבי אליעזר','position_holder',[]),
'6b:3':('רבי עקיבא','position_holder',[]),
'6b:4':('רבי עקיבא','speaker',[]),
'6b:5':('רבי עקיבא','speaker',[]),
'6b:6':('רבי עקיבא','speaker',[]),
'6b:8':('רבי אליעזר','position_holder',[]),
'6b:14':('רבי יוחנן','speaker',[]),
'6b:15':('רב אסי','transmitter',['רב אסי','חבירי שבגולה']),
'7a:1':('חבירי שבגולה','collective',['רב אסי','חבירי שבגולה']),
'7a:4':('רבי זירא','speaker',[]),
'7a:6':('רבא','speaker',[]),
'7a:7':('רב פפא','speaker',[]),
'7a:9':('רבי עקיבא','quoted_authority',[]),
'7a:10':('רבי אלעזר','speaker',[]),
'7a:11':('רבי שמעון','transmitter',[]),
'7a:12':('רבי שמעון','transmitter',['רבי שמעון','רבי עקיבא']),
'7b:1':('רבי עקיבא','quoted_authority',['רבי שמעון','רבי עקיבא']),
'7b:2':('רבי עקיבא','quoted_authority',['רבי שמעון','רבי עקיבא']),
'7b:3':('ריש לקיש','transmitter',['ריש לקיש','רב אושעיא']),
'7b:5':('רבי יוחנן','speaker',[]),
'7b:6':('רבי יוחנן','speaker',[]),
'7b:7':('רבי יוחנן','speaker',[]),
'7b:8':('רבי יוחנן','speaker',[]),
'7b:18':('רבי חנינא','speaker',[])}
scope_extra={'3b:9':'Rav Pappa raises the objection to Abaye; the embedded teaching is anonymous. Abaye is also a transmitter, recorded separately.','3b:15':'אמר ליה respondent inferred as Rava from 3b:13; retain possible pronoun attribution uncertainty.','4a:5':'Response to Ravina, inferred as Rav Ashi from 4a:3.','5a:1':'Only opening continuation of Bar Kappara’s question; Hezekiah and Rabbi Yohanan recorded separately.','5b:1':'Only latter challenge introduced אמר רב אסי; opening ה״נ לאו דוקא is unnamed.','6b:8':'Only first group of rulings; Akiva separately attributed.','7a:11':'Narrator of conversation, not holder of every embedded utterance.','7b:8':'Only victory statement; silence is narrator’s report.'}
attrs={}
for r in [x for x in old if x['layer']=='attributions']:
    loc=r['evidence'][0]['segment_id'].split(' ')[1]
    who,role,chain=PRIMARY.get(loc,('', 'anonymous', []))
    attrs[loc]=add('attributions',loc,dict(surface=who if who else 'unnamed textual voice',role=role,candidates=[who] if who else [],scope=scope_extra.get(loc,'Local utterance or quoted teaching; inherited speaker only where explicitly noted.'),transmission_chain=chain),supersedes=r['id'],origin='editorial_inference',uncertainty=([scope_extra[loc]] if loc in ['3b:15','4a:5'] else []))
EXTRA=[
('3b:8','רב','position_holder',['רב גידל','רב'],'Both pigul-sprinkling rulings'),
('3b:9','אביי','transmitter',['אביי','רב גידל','רב'],'Abaye repeats the immediately preceding report; chain inherited from 3b:8'),
('3b:13','עולא','quoted_authority',['רב אשי','עולא'],'Handful-on-altar statement, not Rav Ashi’s objection'),
('4a:3','אילפא','quoted_authority',['רבינא','אילפא'],'Dispute in two services'),
('5a:1','חזקיה','position_holder',[],'היתר שחיטה שנינו'),
('5a:1','רבי יוחנן','position_holder',[],'היתר אכילה שנינו'),
('5b:5','רבי יוחנן','quoted_authority',['ריש לקיש','רבי יוחנן'],'Addressee of question; answer follows at 5b:6, no own position in question alone'),
('5b:14','רב גידל','transmitter',['רב גידל','רב'],'Embedded report'),
('5b:14','רב','position_holder',['רב גידל','רב'],'Two embedded pigul-sprinkling rulings only, not the framing interpretation of לעולם'),
('6b:8','רבי עקיבא','position_holder',[],'Second group of lesser-holy fats rulings'),
('6b:14','רבי עקיבא','quoted_authority',['רבי יוחנן','רבי עקיבא'],'Interpretandum of Rabbi Yohanan’s qualification, not a separate recorded utterance by Akiva here'),
('7a:3','רב אסי','speaker',[],'Embedded earlier question to Rabbi Yohanan; anonymous narrator raises present inconsistency'),
('7a:7','רבי עקיבא','quoted_authority',['רב פפא','רבי עקיבא'],'Interpretandum of Rav Pappa’s distinction'),
('7a:10','רבי עקיבא','quoted_authority',['רבי אלעזר','רבי עקיבא'],'Interpretandum of Rabbi Eleazar’s restriction'),
('7a:11','זקן אחד','speaker',['רבי שמעון','זקן אחד'],'Elder reports Akiva’s teaching'),
('7a:11','רבי עקיבא','quoted_authority',['רבי שמעון','זקן אחד','רבי עקיבא'],'Sprinkling benefits exited material'),
('7a:11','חבירי שבגליל','collective',['רבי שמעון','חבירי שבגליל'],'Objection from invalidity'),
('7a:12','רבי עקיבא','quoted_authority',['רבי שמעון','רבי עקיבא'],'Two sin offerings and their meilah status'),
('7b:3','רב אושעיא','position_holder',['ריש לקיש','רב אושעיא'],'Criticism transmitted by Reish Lakish'),
('7b:7','עולא','quoted_authority',['רבי יוחנן','עולא'],'Raised lesser-holy fats do not descend and are altar bread'),
]
for loc,who,role,chain,scope in EXTRA:
    add('attributions',loc,dict(surface=who,role=role,candidates=[who],scope=scope,transmission_chain=chain),origin='editorial_inference')

ADDCLAIMS=[
('3b:9','Abaye repeats the immediately preceding Rav Giddel in Rav report.','asserted',['Immediately preceding report at 3b:8'],['אביי'],'יתיב אביי וקאמר לה להא שמעתא'),
('4a:8','The quoted teaching states that pigul always remains subject to meilah.','asserted',['Quoted premise; whether blood was sprinkled is disputed in continuation'],[], 'הפיגול לעולם מועלין בו'),
('4b:7','The quoted teaching states that most-holy pigul is subject to meilah.','asserted',['Quoted premise; sprinkling condition disputed'],[],'הפיגול בקדשי קדשים מועלין בו'),
('4b:9','The proposed alternative formulation would impose meilah before sprinkling.','hypothetical',['Suggested formulation under rejected proof attempt'],[],'לפני זריקה מועלין בו'),
('4b:9','The proposed alternative formulation would deny meilah after sprinkling.','hypothetical',['Suggested formulation under rejected proof attempt'],[],'לאחר זריקה אין מועלין בו'),
('5a:3','The quoted mishnah lists overnight, impurity and exit while denying meilah.','asserted',['Whether overnight refers to blood or flesh is contested'],[],'תנן שלנה ושנטמאת ושיצאת לאו דלן דם וקתני אין מועלין בו'),
('5b:14','The meaning of לעולם is explicitly questioned before the Rav Giddel explanation.','queried',['Quoted pigul teaching'],[],'ומאי לעולם'),
('6a:15','The response restricts the most-holy pigul teaching to blood not sprinkled.','reconciled',['Alternative to the proposed proof of permission-to-eat'],[],'לא דלא זרק'),
('6a:16','The cited ending denies meilah for lesser-holy offerings.','asserted',['Pigul teaching cited in 6a:15–19'],[],'בקדשים קלים אין מועלין בו'),
('6a:16','On the proposed interpretation, actual sprinkling would remove meilah.','hypothetical',['Most-holy pigul case; interrogative consequence'],[],'אבל זרק מאי הכי נמי דאין מועלין בו'),
('6b:10','In the proposed one-clause reading, Rabbi Eliezer would impose meilah on exited most-holy meat.','hypothetical',['Counterfactual had only most-holy case been stated'],['רבי אליעזר'],"בהא קא אמר ר' אליעזר מועלין בו"),
('7a:11','Rabbi Akiva’s reported doctrine is that sprinkling benefits exited material.','asserted',['Nested report by elder to Rabbi Shimon'],['רבי עקיבא'],"אומר היה ר' עקיבא זריקה מועלת ליוצא"),
('7b:4','The comparison offering is treated as invalid within the criticism.','asserted',['Premise of Rav Hoshaya/Reish Lakish criticism, not independent practical ruling'],[],'דכיון דפסול הוא'),
('7b:7','The two offerings might be treated as one body, an assumption questioned in the argument.','hypothetical',['Rabbi Yohanan’s argument; not a maintained identity claim'],[], 'ואי ס"ד חד גופא הוא'),
]
added_claims=[]
for loc,prop,mode,cond,holders,needle in ADDCLAIMS:
    cc=add('claims',loc,dict(proposition=prop,conditions=cond,scope='local source argument',assertion_mode=mode),links=[attrs[loc]],needle=needle)
    added_claims.append((loc,cc,holders,cond,mode))

# Bounded comparable question sets: independent doctrinal outcomes are not merged.
qold={r['evidence'][0]['segment_id'].split(' ')[1]:r['id'] for r in old if r['layer']=='questions'}
threshold_old=prev('questions','4b:14')[0]
threshold=add('questions','4b:14',dict(formulation='Which threshold does שעת היתר לכהנים denote: slaughter, fitness for sprinkling, or permission to eat?',question_origin='explicit',conditions=['Rabbi Yehoshua’s meilah rule'],answer_set_status='topic_inventory'),supersedes=threshold_old['id'],evidence=[ev('4b:14'),ev('5a:1')])
answer_sets=[dict(question_id=threshold,scope=['Meilah 4b:14','Meilah 5a:1'],answers=[dict(claim_id=cid('4b:14'),holder_candidates=[],status='candidate'),dict(claim_id=cid('5a:1',0),holder_candidates=[],status='candidate'),dict(claim_id=cid('5a:1',1),holder_candidates=[],status='candidate'),dict(claim_id=cid('5a:1',2),holder_candidates=['חזקיה'],status='named_position'),dict(claim_id=cid('5a:1',3),holder_candidates=['רבי יוחנן'],status='named_position')],local_outcome='Three alternatives inventoried; subsequent proofs and answers do not name a holder for the middle candidate. No final halakhic selection inferred.')]
position_question={};outcomes=['meilah','pigul liability','notar liability','impurity liability']
for category,locs,cond in [('most_holy',['6b:2','6b:3'],'Most-holy meat exited before sprinkling'),('lesser_holy',['6b:8'],'Lesser-holy sacrificial fats exited before sprinkling')]:
    for n,outcome in enumerate(outcomes):
        qq=add('questions',locs[0],dict(formulation=f'Does {outcome} apply after sprinkling?',question_origin='editorial_reconstruction',conditions=[cond],answer_set_status='topic_inventory'),origin='editorial_inference',evidence=[ev(x) for x in locs])
        pairs=[(cid('6b:2',n),['רבי אליעזר']),(cid('6b:3',n),['רבי עקיבא'])] if category=='most_holy' else [(cid('6b:8',n),['רבי אליעזר']),(cid('6b:8',n+4),['רבי עקיבא'])]
        for cc,_ in pairs:position_question[cc]=qq
        answer_sets.append(dict(question_id=qq,scope=[ref(x) for x in locs],answers=[dict(claim_id=cc,holder_candidates=hh,status='named_mishnah_position') for cc,hh in pairs],local_outcome='Opposed named positions. Akiva’s scope later qualified by partial exit (6b:14), flesh versus blood (7a:7), and benefit not permission to eat (7b:19–8a:1).'))
for cc in [cid('4b:14')]+[cid('5a:1',n) for n in range(4)]:position_question[cc]=threshold
newq=add('questions','5b:14',dict(formulation='What does לעולם add in the pigul teaching?',question_origin='explicit',conditions=['Pigul always has meilah'],answer_set_status='topic_inventory'),needle='ומאי לעולם')
answer_sets.append(dict(question_id=newq,scope=['Meilah 5b:14'],answers=[dict(claim_id=cid('5b:14',2),holder_candidates=[],status='anonymous_explanation')],local_outcome='Explained by Rav Giddel in Rav on ineffective pigul sprinkling.'))

# Effective holders distinguish commentators, quoted authorities, narrative statements and hypotheticals.
HOLD={loc:[who] for loc,(who,role,ch) in PRIMARY.items()}
for loc in ['3b:9','3b:11','5b:1','5a:1','6b:15','7a:11','7b:8']:HOLD[loc]=[]
HOLD.update({'3b:8':['רב'],'3b:13':['עולא'],'4a:3':['אילפא'],'4a:4':['אילפא'],'5b:14':['רב'],'6b:10':['רבי אליעזר'],'6b:11':['רבי אליעזר'],'6b:12':['רבי עקיבא'],'6b:13':['רבי עקיבא'],'7a:12':['רבי עקיבא'],'7b:3':['רב אושעיא']})
SPECIAL={('5a:1',2):['חזקיה'],('5a:1',3):['רבי יוחנן'],('5b:1',1):['רב אסי'],('5b:14',2):[],('6b:13',1):[],('7a:11',0):['זקן אחד'],('7a:11',1):['רבי שמעון'],('7a:11',2):['חבירי שבגליל'],('7b:7',0):['עולא'],('7b:7',1):['עולא'],('7b:8',1):['רבי יוחנן']}
for n in range(8):SPECIAL[('6b:8',n)]=['רבי אליעזר'] if n<4 else ['רבי עקיבא']
for r in [x for x in old if x['layer']=='positions']:
    loc=r['evidence'][0]['segment_id'].split(' ')[1];cl=r['content']['claim_id'];n=[x['id'] for x in prev('claims',loc)].index(cl)
    c=copy.deepcopy(r['content']);c['holder_candidates']=SPECIAL.get((loc,n),HOLD.get(loc,[]));c['claim_id']=remap.get(cl,cl)
    c['question_id']=position_question.get(cl,remap.get(c['question_id'],c['question_id']))
    if loc=='3b:11' and n==1:c['local_status']='Narrated silence by Abaye, not a challenged doctrine or explicit retraction.'
    if loc=='5a:2':c['local_status']='Named textual observation with compressed negative syntax; continuation inventoried without forcing final resolution.'
    if loc=='6b:13' and n==1:c['local_status']='Actual conclusion of necessity argument, not itself rejected.'
    if loc=='7a:11' and n==0:c['local_status']='Elder reports a doctrine; original wording does not require an interrogative.'
    if loc=='7b:7' and n==2:c['local_status']='Rabbi Yohanan’s objection within hypothetical, not a freestanding rule for lesser-holy fats.'
    if loc in ['7b:14','7b:17'] and n==1:c['local_status']='Asserted property premise used in objection; objection is answered without rejecting the premise.'
    replacement(r,c)
for loc,cc,holders,cond,mode in added_claims:
    add('positions',loc,dict(holder_candidates=holders,claim_id=cc,question_id=newq if loc=='5b:14' else None,conditions=cond,local_status=mode+' in bounded source argument; no practical ruling inferred'),links=[cc],origin='editorial_inference')

# Retire the accidental answer/objection edge that attached narrative transmission rather
# than the transmitted content; replace with exact claim-level relation as continuation.
edge_fixes={
('3b:11','3b:8','objection'):(cid('3b:11'),cid('3b:8',1),'objection'),
('3b:13','3b:12','objection'):(qold['3b:13'],cid('3b:12'),'objection'),
('4a:1','3b:15','objection'):(qold['4a:1'],cid('3b:15'),'objection'),
('4a:3','3b:15','objection'):(qold['4a:3'],cid('3b:15'),'objection'),
('4b:5','4b:4','qualification'):(cid('4b:5'),cid('4b:4',1),'qualification'),
('5a:10','5a:9','objection'):(qold['5a:10'],cid('5a:9'),'objection'),
('5b:1','5a:15','analogy'):(cid('5b:1'),cid('5a:15',1),'analogy'),
('5b:2','5b:1','answer'):(cid('5b:2'),cid('5b:1',1),'answer'),
('5b:5','5b:3','objection'):(qold['5b:5'],cid('5b:3'),'objection'),
('6b:15','6b:14','objection'):(cid('7a:2'),cid('6b:14',1),'objection'),
('7a:6','7a:1','correction'):(cid('7a:6'),cid('7a:1'),'correction'),
('7b:3','7b:2','objection'):(cid('7b:3'),cid('7b:2'),'objection'),
('7b:7','7b:6','support'):(cid('7b:7',2),cid('7b:6'),'continuation'),
('7b:8','7b:5','local_resolution'):(cid('7b:8'),qold['7b:5'],'local_resolution'),
}
allold={r['id']:r for r in old}
for r in [x for x in old if x['layer']=='edges']:
    c=copy.deepcopy(r['content']);a=allold[c['source_id']]['evidence'][0]['segment_id'].split(' ')[1];b=allold[c['target_id']]['evidence'][0]['segment_id'].split(' ')[1]
    if (a,b,c['relation']) in edge_fixes:
        aa,bb,rel=edge_fixes[(a,b,c['relation'])];c.update(source_id=aa,target_id=bb,relation=rel)
        evidence=r['evidence']+[ev('7a:2')] if a=='6b:15' else r['evidence']
        replacement(r,c,evidence=evidence)

def edge(loc,ss,tt,relation,needle=None):
    add('edges',loc,dict(source_id=ss,target_id=tt,relation=relation,explicitness='editorial_reconstruction'),links=[ss,tt],origin='editorial_inference',needle=needle)
edge('7a:6',cid('7a:6',1),cid('7a:1',1),'correction')
edge('5b:9',cid('5b:9',1),cid('5b:3'),'qualification')
edge('5b:10',cid('5b:10'),cid('5b:4'),'qualification')
edge('5a:1',cid('5a:1',2),threshold,'answer')
edge('5a:1',cid('5a:1',3),threshold,'answer')
edge('5b:14',cid('5b:14',2),newq,'answer')
for a in answer_sets[1:9]:
    for ans in a['answers']:
        cc=ans['claim_id'];loc=allold[cc]['evidence'][0]['segment_id'];edge(loc,cc,a['question_id'],'answer')

# Source boundaries independently rechecked; primary ownership remains original full segments.
for start,end,title in [('3b:8','4b:10','Pigul sprinkling, thanksgiving bread, and qualified proofs'),('4b:11','6a:19','Meaning of priestly permission and competing threshold readings'),('6b:1','7b:8','Exited flesh/fats, Akiva and Eliezer, restrictions and analogies'),('7b:9','8a:1','Blood-service effects and residual prohibition for exited material')]:
    refs=job['core_refs'][job['core_refs'].index(ref(start)):job['core_refs'].index(ref(end))+1]
    add('structure',start,dict(title=title,primary=False,boundary='closed',legacy_ids=[]),origin='editorial_inference',evidence=[ev(x) for x in refs])

# Reconciliation notes were made after rereading the original strings, not inferred from
# successful mechanical validation. Each window covers every original core in order.
WINDOWS=[
('3b:8','3b:15','Checked both holiness categories, Rav Giddel/Rav transmission, Abaye’s repetition, Rav Pappa’s bread objection, silence, Rabbi Abba’s sprinkling distinction, Rav Ashi/Rava/Ulla roles and pigul-precursor response. Added missing Abaye transmission; kept silence non-retraction.'),
('4a:1','4a:10','Checked repeated precursor answer, Ravina/Ilfa/Rav Ashi nesting, one/two services, delayed clarification, bread-for-burning resolution and each tentative proof/deflection. Added literal always-meilah premise; prospective proof not final agreement.'),
('4b:1','4b:10','Checked overnight blood versus olah, proposed support, printed (לאו), action versus thought distinction, lesser/most-holy proof asymmetry and proposed before/after alternative. Added literal most-holy premise and the two hypothetical alternative rulings; unresolved printed qualification retained.'),
('4b:11','5a:1','Checked both halves of Rabbi Yehoshua’s rule, each example, Bar Kappara/Bar Pedat exchange and three threshold candidates. Named Hezekiah and Rabbi Yohanan positions separated from unnamed middle candidate; comparable answer set explicitly bounded.'),
('5a:2','5a:15','Checked Rabbi Zeira wording, blood/flesh overnight alternative, invalid reception versus invalid sprinkling, Rav Yosef’s washing parallel, verse exclusion and nonprecision answer. Preserved compressed negative wording without unsupported resolution; repeated examples retained as occurrences.'),
('5b:1','5b:10','Checked Rav Assi’s redundancy challenge, precise meilah wording, invalid actor makes residual blood, later valid service ineffectiveness, Reish Lakish/Rabbi Yohanan exchange and final impurity/other-disqualified distinction. Included both qualifications of broad residual-blood claim; no Rav/Rav Assi conflation.'),
('5b:11','5b:14','Checked proposed threshold inference, unpunctuated לא זרקה and continuation explaining לעולם through Rav Giddel/Rav. Added explicit לעולם question and separated anonymous explanation from the two Rav rulings.'),
('6a:1','6a:8','Checked both Rabbi Shimon notar alternatives, opportunity-to-sprinkle inference, near-sunset answer and before/after suitability reinterpretation. Inference remains attempted, not adjudicated threshold victory.'),
('6a:9','6a:14','Checked distinct pigul occurrence, before/after alternatives, opportunity inference and sunset challenge/answer. Preserved this occurrence separately from notar and marked hypothetical consequence separately from actual answer.'),
('6a:15','6a:19','Checked most-holy proof, no-sprinkling answer, hypothetical after-sprinkling consequence, lesser-holy ending, and asymmetric introduction/removal resolution. Added omitted no-sprinkling answer and ending premise; retained tension with Rav report rather than harmonizing.'),
('6b:1','6b:8','Checked exited most-holy meat and lesser-holy fats independently; atomic meilah/pigul/notar/impurity outcomes for both sages; lost/replaced/found offering analogy and a-fortiori inference. Added eight bounded comparable question/answer inventories, including inherited after-sprinkling condition.'),
('6b:9','6b:15','Checked necessity counterfactuals in both directions, final קמ״ל, Rabbi Yohanan partial/whole restriction and Rav Assi’s diaspora transmission. Corrected actual conclusion assertion mode and separately inventoried counterfactual Eliezer meilah premise.'),
('7a:1','7a:8','Checked lost/burned claims, Rav Assi consistency question, Rabbi Zeira/אלל analogy, Rava’s standing-to-be-lost/burned correction, Rav Pappa flesh/blood restriction and baraita’s three rulings. Corrected edges to refer to both lost and burned claims.'),
('7a:9','7b:4','Checked quotation heading, Rabbi Eleazar simultaneity restriction, Rabbi Shimon/elder/Akiva/Galilean colleagues nested report, two offerings before and after blood, a-fortiori argument, Reish Lakish in Rav Hoshaya’s name and critique. Corrected elder statement from unmarked question to report; no name-order assignment or explicit retraction invented.'),
('7b:5','7b:8','Checked Rabbi Yohanan to Reish Lakish, hypothetical two guilt offerings, placement before sprinkling, concession of descent, one-body assumption, Ulla quotation, silence and claimed victory. Corrected hypothetical argument scope and holders; silence does not prove durable recantation.'),
('7b:9','7b:13','Checked before/after sprinkling in both holiness categories, fats/meat separation, each pigul/notar/impurity liability and leniency/stringency summary. Atomic parallel outcomes retained.'),
('7b:14','8a:1','Checked priest and owner property objections, stylistic answer, repeated lesser-holy mishnah occurrence, Rabbi Hanina’s exited-material/Akiva interpretation and burning/eating distinction across page boundary. Property premises are asserted within objections, not themselves rejected.'),
('8a:2','8a:2','Checked original chapter-closing markup; no doctrinal speaker, proposition, question, position or argumentative edge. Structural record owns every character.')]
reconciliation=[]
for start,end,note in WINDOWS:
    refs=job['core_refs'][job['core_refs'].index(ref(start)):job['core_refs'].index(ref(end))+1]
    for rr in refs:reconciliation.append(dict(segment_id=rr,start_char=0,end_char=len(texts[rr]),quote=texts[rr],passes=['utterances','claims','attributions','questions','positions','edges','reconciliation'],result='bounded_source_only_inventory_pass_completed',note=note))
assert [r['segment_id'] for r in reconciliation]==job['core_refs']

# Resolve supersession transitively, then make replacements for any remaining inherited
# record whose links/content point at superseded records. No frozen bytes are edited.
def mapped(x):
    while x in remap:x=remap[x]
    return x
for r in old:
    if r['id'] in remap:continue
    c=copy.deepcopy(r['content']);links=[mapped(x) for x in r['links']];changed=links!=r['links']
    for key in ['claim_id','question_id','source_id','target_id']:
        if key in c and c[key] in remap:c[key]=mapped(c[key]);changed=True
    if changed:
        rr=copy.deepcopy(r);rr['links']=links;replacement(rr,c)
for r in new:
    r['links']=[mapped(x) for x in r['links']]
    for key in ['claim_id','question_id','source_id','target_id']:
        if key in r['content']:r['content'][key]=mapped(r['content'][key])
for aa in answer_sets:
    aa['question_id']=mapped(aa['question_id'])
    for ans in aa['answers']:ans['claim_id']=mapped(ans['claim_id'])
effective=[r for r in old if r['id'] not in remap]+new
known={r['id'] for r in old+new};effknown={r['id'] for r in effective}
for r in effective:
    assert all(x in effknown for x in r['links'])
    for k in ['claim_id','question_id','source_id','target_id']:
        if k in r['content'] and r['content'][k] is not None:assert r['content'][k] in effknown
    for e in r['evidence']:assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
schema=json.loads((ROOT/'source_only_common/schema.json').read_text(encoding='utf-8-sig'))
for r in new:Draft202012Validator(schema['properties']['records']['items']).validate(r)
coverage=[]
for rr in job['core_refs']:
    for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
        ids=[r['id'] for r in effective if r['layer']==layer and any(e['segment_id']==rr for e in r['evidence'])]
        rationale=('Source-based omission/continuation pass completed; see exact-span reconciliation entry.' if layer=='reconciliation' else 'Bounded independent inventory pass completed against reread original text; no human certification or universal exhaustive-truth claim.')
        if not ids and layer!='reconciliation':rationale=('Chapter closing marker has no doctrinal semantic unit.' if rr=='Meilah 8a:2' else 'After source-only second pass, no separate '+layer+' record required in this source segment; inherited discourse handled by linked surrounding records. '+next(x['note'] for x in reconciliation if x['segment_id']==rr))
        coverage.append(dict(segment_id=rr,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else ('not_applicable' if rr=='Meilah 8a:2' and layer!='reconciliation' else 'none_found_after_pass'),record_ids=ids,rationale=rationale))
        Draft202012Validator(schema['properties']['coverage']['items']).validate(coverage[-1])
result=dict(artifact_kind='additive_source_only_bounded_inventory_completion',job_id=job['job_id'],base_artifact={'path':str(P),'sha256':H(P)},source=job['source'],job={'path':str(jobpath),'sha256':H(jobpath)},common_documents=job['common_documents'],provenance={'agent_id':'/root/reader_meilah_supplement002','producer_comparison_started':False,'other_reader_material_accessed':False,'inputs':'same original source and common instructions plus this reader’s own frozen base artifact','core_reread_count':128,'new_context_read_count':0,'offset_unit':'Python Unicode code points, half-open, no normalization'},status='bounded_independent_inventory_completed',clarification='Base artifact marked semantic layers in_progress because a separate source-based omission/reconciliation pass had not been completed. This additive artifact completes that pass over all 128 core source segments. Completed means actual bounded source-only passes performed, not certainty that no future scholarly correction or further atomization is possible.',records=new,supersession_map=remap,effective_record_ids=[r['id'] for r in effective],coverage=coverage,reconciliation=reconciliation,comparable_answer_sets=answer_sets,remaining_unprocessed_core_coordinates=[],remaining_unprocessed_core_layers=[],context_scope=base['context_refs_read'],context_limit='20 original context segments were read in base pass to delimit the cores; they are not promoted to full core annotation coverage.',unresolved_interpretations=[{'refs':['Meilah 4b:5'],'issue':'Parenthetic (לאו) retained; no edition correction or forced unconditional support.'},{'refs':['Meilah 5a:2'],'issue':'Compressed negative precision statement retained with uncertainty; no forced final threshold conclusion.'},{'refs':['Meilah 5b:13','Meilah 5b:14'],'issue':'לא זרקה interpreted as לא, זרקה from continuation; source punctuation is not altered.'},{'refs':['Meilah 3b:8','Meilah 6a:18','Meilah 6a:19'],'issue':'Different local formulations preserved without invented harmonization or attribution of final anonymous claim to Rav.'},{'refs':['Meilah 7a:10','Meilah 7b:3'],'issue':'Simultaneous/successive event chronology not expanded beyond source words.'},{'refs':['Meilah 7b:6','Meilah 7b:7'],'issue':'Guilt-offering one-body argument inventoried as source hypothetical; full external conceptual reconstruction not claimed.'}],human_scholarly_certification=False,ml_eligible=False)
result['counts']={'core_segments_second_pass_completed':128,'coverage_rows_completed':len(coverage),'additive_records':len(new),'superseded_base_records':len(remap),'effective_total_records':len(effective),'effective_by_layer':{l:sum(r['layer']==l for r in effective) for l in ['structure','utterances','claims','attributions','questions','positions','edges']},'remaining_unprocessed_core_segments':0,'comparable_answer_sets':len(answer_sets)}
out=ROOT/'readings/meilah_supplement002_completion001.json';assert not out.exists()
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
digest=H(out);out.with_suffix('.json.sha256').write_text(digest+'  '+out.name+'\n',encoding='ascii')
print(json.dumps({'path':str(out),'sha256':digest,'counts':result['counts']},ensure_ascii=True))
