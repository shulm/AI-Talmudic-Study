"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='342e4c22b5c117279b77266d9f38f8b41e0c83d741c1ab33f1e933338cf54a33';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/chullin','epoch':2}
assert I[148]['ref']=='Chullin 7a:4' and I[167]['ref']=='Chullin 7b:9'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='ch.ret18r01.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
import copy,importlib.util
D={r['id']:r for r in S['records']};ids={'ch.s2718.whitemules','ch.s2718.q.deathmeal','ch.s2718.hospitality'}
while True:
 n=ids|{r['id'] for r in S['records'] if r['release_state']=='valid' and any(v in ids for v in r['links'])}
 if n==ids:break
 ids=n
mapping={rid:rid+'.ret18r01' for rid in ids}
def remap(v):
 if isinstance(v,str):return mapping.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
for rid in sorted(ids):
 r=remap({k:copy.deepcopy(v) for k,v in D[rid].items() if k not in ['review_state','release_state','ml_eligible','supersedes']});r['supersedes']=rid
 if rid=='ch.s2718.whitemules':r['evidence']+=ev([171]);r['content']['scope']+='; narrative observation not a general medical assertion:7b13 revises fatality to recovery language and narrows to white extremities; this does not prove these observed animals exact limb coloration'
 if rid=='ch.s2718.q.deathmeal':r['evidence']+=ev([168,171]);r['content']['conditions']+=['Rhetorical danger objection in narrative, not universal clinical assertion; subsequent exposition7b13 corrected and narrowed to white limb extremities','Narrative concludes7b10 with separation, not an accepted remedy or completed meal']
 if rid=='ch.s2718.hospitality':r['content']['boundary']='closed';r['content']['title']+='; source outcome and practice note preserved as context7b10–16, no meal completion inferred'
 R.append(r)
c={'white':mapping['ch.s2718.whitemules'],'death':mapping['ch.s2718.q.deathmeal'],'return':'ch.s2718.returnpromise','yes':'ch.s2718.yesdine','ruling':'ch.s2717.permittedbeit','testimony':'ch.s2717.testimony'};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
C('continuedpressing',168,'Rabbi continued pressing him strongly.','Narrative continuation after all proposed mule remedies rejected; not a new agreed remedy')
C('hillseparated',168,'A hill rose between them.','Source narrative separation of Rabbi and Pinhas, no completed shared meal')
C('rabbiwept',168,'Rabbi wept.','Narrative response')
Q('afterdeath',168,'If so during their lives, how much more after their deaths?', ['Rabbi reaction to separation'])
C('greaterdead',168,'The righteous are greater in death than in life.','Rabbi Hama bar Hanina statement cited here',holder='רבי חמא בר חנינא')
C('elishabones',168,'The cited verse describes a body cast into Elisha’s grave, touching his bones, reviving and standing.','Scriptural proof for greater-in-death claim, not producer empirical assertion')
Q('doubleportion',169,'Perhaps this was to fulfill Elijah’s blessing of a double portion?', ['Rav Pappa challenges Abaye','Elisha revival proof'])
C('stoodnotreturned',169,'The baraita says he stood on his feet but did not return home.','Abaye answer challenges proposed double-portion fulfillment through this event')
Q('fulfilledhow',170,'Then how was the blessing fulfilled?', ['Rejected fulfillment by this brief revival'])
C('naaman',170,'Rabbi Yohanan says Elisha healed Naaman’s leprosy.','Alternate fulfillment of double portion',holder='רבי יוחנן')
C('leprosylikedeath',170,'Leprosy is treated as equivalent to death, as shown by אל נא תהי כמת.','Source comparison explaining Naaman healing as life-restoration, not medical equivalence claim')
add('pappaabaye','attributions',169,dict(surface='אמר ליה רב פפא לאביי',role='speaker',candidates=['רב פפא'],scope='Question to Abaye about Elijah blessing',transmission_chain=[]),[z['doubleportion']])
add('abayereply','attributions',169,dict(surface='אמר ליה אי הכי',role='speaker',candidates=['אביי'],scope='Reply using stood-but-not-home baraita',transmission_chain=[]),[c['stoodnotreturned']])
Q('mulesname',171,'Why are they called ימים?', ['Mule-name exposition'])
C('awe',171,'Because their dread rests upon people.','Rabbi Yehoshua ben Levi etymological explanation',holder='רבי יהושע בן לוי')
C('fatalinitial',171,'Rabbi Hanina initially says no one ever asked him about a white mule’s blow and lived.','Initial wording challenged immediately; narrative report not endorsed universal medical rule',holder='רבי חנינא',mode='challenged')
Q('lives',171,'But we see that they live?', ['Initial fatality wording'])
C('recoveryrevision',171,'Rather say: and the wound healed.','אימא וחיית corrects living wording to healing wording within Hanina report; not final unqualified claim',holder='רבי חנינא',mode='challenged')
Q('heals',171,'But we see that they recover?', ['Revised no-healing reading'])
C('whiteextremities',171,'The statement concerns those whose limb extremities are white.','Final narrowing דחיוורן ריש כרעייהו, retained with initial/revised stages; source teaching, not general clinical certification',cond=['White limb extremities'],mode='reconciled')
add('yehoshuaname','attributions',171,dict(surface='אמר ר׳ יהושע בן לוי למה נקרא שמן ימים',role='speaker',candidates=['רבי יהושע בן לוי'],scope='Name question and dread answer, distinct from Hanina blow report',transmission_chain=[]),[z['mulesname'],c['awe']])
C('haninawitchcraft',172,'Rabbi Hanina includes even sorcery under אין עוד מלבדו.','Separate argument from mule injury discourse',holder='רבי חנינא')
C('dustwoman',172,'A woman tried to take dust from under Rabbi Hanina’s feet.','Source narrative setup')
C('takeshallfail',172,'He told her to take it, for her matter would not succeed, invoking אין עוד מלבדו.','Hanina confidence in this narrative; qualified by exceptional merit later',holder='רבי חנינא')
Q('witchcontradiction',172,'But did Rabbi Yohanan not explain sorcery as weakening the heavenly retinue?', ['Challenge to Hanina dismissal of attempted sorcery'])
Q('witchname',172,'Why is it called כשפים?', ['Quoted Rabbi Yohanan explanation'])
C('witchretinue',172,'Because it weakens the heavenly retinue.','Rabbi Yohanan etymological teaching, not producer metaphysical verification',holder='רבי יוחנן')
C('haninaexception',172,'Rabbi Hanina is different because his merit is abundant.','Resolution restricts narrative assurance to exceptional merit',cond=['Rabbi Hanina exceptional merit'])
C('fingerdecree',173,'No one bruises a finger below unless it is proclaimed about him above.','Rabbi Hanina theological statement with quoted verses, not measured causal claim',holder='רבי חנינא')
C('bloodatonement',173,'Blood from a bruise effects atonement like burnt-offering blood.','Rabbi Elazar teaching, qualifications supplied by Rava',holder='רבי אלעזר')
C('ravaconditions',173,'Rava restricts this to the right thumb, a second bruising, while going for a mitzvah.','All three conjunctive qualifications of bruise-blood teaching',cond=['Right thumb','Second bruising','Going for a mitzvah'],holder='רבא')
C('ownbread',174,'They said Pinhas ben Yair never broke bread on a portion not his own.','Reported hospitality practice, not erasure of earlier initial yes or proof a meal occurred')
C('nofathermeal',174,'From the time he attained understanding he did not benefit from his father’s meal.','Separate time-qualified practice report',cond=['Since attaining understanding'])
rels=[([142,150],'ch.s2718.initialsanctity','ruling','qualification'),([142,150],'ch.s2718.notfuture','ruling','qualification'),([142,151],'ch.s2718.bundle','testimony','qualification'),([142,153],'ch.s2718.greatwitness','testimony','support'),(168,'continuedpressing','hillseparated','support'),([162,168],'hillseparated','yes','qualification'),([164,168],'hillseparated','return','qualification'),(168,'elishabones','greaterdead','support'),(169,'doubleportion','greaterdead','objection'),(169,'stoodnotreturned','doubleportion','answer'),(170,'naaman','fulfilledhow','answer'),(170,'leprosylikedeath','naaman','support'),(171,'awe','mulesname','answer'),(171,'lives','fatalinitial','objection'),(171,'recoveryrevision','fatalinitial','correction'),(171,'heals','recoveryrevision','objection'),(171,'whiteextremities','heals','answer'),(171,'whiteextremities','recoveryrevision','qualification'),([165,171],'whiteextremities','white','qualification'),([165,171],'whiteextremities','death','qualification'),(172,'witchretinue','witchname','answer'),(172,'witchretinue','witchcontradiction','support'),(172,'haninaexception','witchcontradiction','answer'),(172,'haninaexception','takeshallfail','qualification'),(173,'ravaconditions','bloodatonement','qualification'),([162,174],'ownbread','yes','qualification'),([164,174],'nofathermeal','return','qualification')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
COV=[]
for pc in S['coverage']:
 needed=any(v in ids for v in pc['record_ids']) or any((pc['layer']=='reconciliation' or r['layer']==pc['layer']) and any(x['segment_id']==pc['segment_id'] for x in r['evidence']) for r in R)
 if needed:
  cv=remap({k:copy.deepcopy(v) for k,v in pc.items() if k!='proposal_execution'})
  for r in R:
   if (cv['layer']=='reconciliation' or r['layer']==cv['layer']) and any(x['segment_id']==cv['segment_id'] for x in r['evidence']) and r['id'] not in cv['record_ids']:cv['record_ids'].append(r['id'])
  if cv['record_ids']:cv['extraction_result']='records_found'
  cv['rationale']+=' RET18-R01 context7b10–16 retained and linked, mule wording corrections/narrowing explicit; Beit Shean claim-level cross-wave links added. No context core coverage.';COV.append(cv)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/chullin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=[v for v in S['open_tails'] if v!='ch.s2718.hospitality'])
runner=Path('F:/Sefaria_QA/worktrees/bavli-l05-production-20261126/research/bavli_production_v1/runner.py');spec=importlib.util.spec_from_file_location('runner',runner);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.validate_apply(S,P,{v['id']:v for v in I},M)
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'chullin_RET18_R01_context_correction.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),coverage_updates=len(COV),superseded=len(ids),sha256=hashlib.sha256(b).hexdigest())))
