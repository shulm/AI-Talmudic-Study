"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shevuot')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='83746e4b7a9c884bb3cb3c79684f804cc5b85770bb15bd84aa85b753a8896489';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shevuot','epoch':2}
assert I[19]['ref']=='Shevuot 2b:12' and I[28]['ref']=='Shevuot 3a:9'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='she.s2706.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('sequence','structure',range(19,25),dict(title='Why Shevuot follows Makkot and why these four classifications are grouped and ordered',primary=True,boundary='closed',legacy_ids=[]))
s2=add('classes','structure',range(25,29),dict(title='Explication of two-that-are-four classifications; author and liability scope investigated in continuation',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('order',19,'Given that the tanna has just concluded Makkot, why does he teach Shevuot next?', ['Sequence of tractates','Opening of Gemara'])
C('head',19,'For the head he is liable for two: one on this side and one on that side.','Quoted closing Makkot material used for sequence explanation; the core does not name a new holder',cond=['Head-side liability in quoted Makkot classification'])
C('beard',[19,20],'For the beard there are two on this side, two on that side, and one below.','Full continuation of quoted Makkot material across folio; all five locations retained',cond=['Beard liability in quoted Makkot classification'])
C('sequenceanswer',[19,20,21],'Having taught one matter for which there are two liabilities, the tanna teaches oaths as two that are four.','Answer explaining sequence by repeated numerical form; head/beard quotation preserved, not interpreted as every case totaling two')
Q('allhere',22,'Why are all of these classifications taught here, whereas the passages on Shabbat transfers and leprous appearances do not teach all of them?', ['Opening list of oaths, impurity awareness, Shabbat transfers and appearances'])
C('togetherwritten',23,'Oaths and awareness of impurity are written adjacent to one another.','First reason for their joint teaching')
C('sameoffering',23,'Oaths and awareness of impurity resemble one another in the variable-value offering.','Second reason for joint teaching; קרבן עולה ויורד preserved without generalizing to every liability')
C('teachpair',23,'Oaths and awareness of impurity are therefore taught together.','Joint teaching based on textual proximity and shared offering')
C('allfour',23,'Once two classifications were taught, all were taught.','Answer why this opening includes the additional classifications')
Q('begin',24,'Why begin with oaths but then explain awareness of impurity?', ['Order of opening headings versus subsequent detailed treatment'])
C('shortfirst',24,'Because the matters of impurity awareness are few, the tanna completes them first.','Explanation for order of detailed treatment')
C('oathlater',24,'Afterward he teaches oaths, whose matters are numerous.','Second part of ordering explanation, not a source omission')
unc=['These are the anonymous opening classifications. Full continuation3a10–5a5 revises proposed named holders and liability interpretations; do not assign the entire list to Rabbi Yishmael or Rabbi Akiva, or assume every item has identical sacrificial/lashes liability.']
C('oathfutureeat',25,'The oath “I will eat” is one of the basic two.','Future affirmative member of שתים',cond=['Oath formula שאוכל'],unc=unc)
C('oathfuturenot',25,'The oath “I will not eat” is the other basic member.','Future negative member of שתים',cond=['Oath formula שלא אוכל'],unc=unc)
C('oathpasteat',25,'The oath “I ate” is included in the expanded four.','Past affirmative member added by שהן ארבע',cond=['Oath formula אכלתי'],unc=unc)
C('oathpastnot',25,'The oath “I did not eat” is included in the expanded four.','Past negative member added by שהן ארבע',cond=['Oath formula שלא אכלתי'],unc=unc)
C('impurityholy',26,'ידיעת טומאת קדש is one of the two basic awareness categories.','Literal category label: awareness of impurity concerning sacred food; do not collapse with awareness of sacred status',unc=unc)
C('impuritytemple',26,'ידיעת טומאת מקדש is the other basic awareness category.','Literal category label: awareness of impurity concerning the Temple; distinct from awareness of Temple status',unc=unc)
C('holystatus',26,'קדש is added in the expansion to four.','Awareness category concerning sacred status itself, as distinct from impurity; later העלם distinctions govern liability',unc=unc)
C('templestatus',26,'מקדש is added in the expansion to four.','Awareness category concerning Temple status itself, as distinct from impurity; later העלם distinctions govern liability',unc=unc)
C('poorout',27,'The poor person’s carrying out is one of the basic two Shabbat transfers.','הוצאה דעני',cond=['Shabbat','Outward transfer','Poor person'],unc=unc)
C('houseout',27,'The householder’s carrying out is the other basic Shabbat transfer.','הוצאה דבעל הבית',cond=['Shabbat','Outward transfer','Householder'],unc=unc)
C('poorin',27,'The poor person’s carrying in is added in the expansion to four.','הכנסה דעני',cond=['Shabbat','Inward transfer','Poor person'],unc=unc)
C('housein',27,'The householder’s carrying in is added in the expansion to four.','הכנסה דבעל הבית',cond=['Shabbat','Inward transfer','Householder'],unc=unc)
C('seet',28,'שאת is one of the two primary appearances.','Source appearance taxonomy; no named author forced',unc=unc)
C('baheret',28,'בהרת is the other primary appearance.','Source appearance taxonomy',unc=unc)
C('seetderived',28,'שאת together with its derivative forms one pair in the expanded four.','שאת ותולדתה; primary/derivative relationship retained',unc=unc)
C('baheretderived',28,'בהרת together with its derivative forms the other pair in the expanded four.','בהרת ותולדתה; primary/derivative relationship retained',unc=unc)
for n,(ii,a,b,r) in enumerate([(21,'sequenceanswer','order','answer'),(21,'head','sequenceanswer','support'),(23,'togetherwritten','teachpair','support'),(23,'sameoffering','teachpair','support'),(23,'teachpair','allhere','answer'),(23,'allfour','allhere','answer'),(24,'shortfirst','begin','answer'),(24,'oathlater','begin','answer')]):E(str(n),ii,a,b,r)
# The classification is explicitly anonymous here: retain supported positions without inventing a named holder.
for key in ['oathfutureeat','oathfuturenot','oathpasteat','oathpastnot','impurityholy','impuritytemple','holystatus','templestatus','poorout','houseout','poorin','housein','seet','baheret','seetderived','baheretderived']:
 claim=next(r for r in R if r['id']==c[key]);ii=next(i for i in range(25,29) if I[i]['id']==claim['evidence'][0]['segment_id']);add(key+'.p','positions',ii,dict(holder_candidates=[],claim_id=c[key],question_id=None,conditions=claim['content']['conditions'],local_status='Anonymous opening classification; named-holder and liability analysis continues beyond this bounded core'),[c[key]],unc=unc)
notes={19:'Sequence question and quoted head liabilities; continuation beard and sequence answer carried through3a2, including markup.',20:'Preserve all beard loci two+two+one and full split sentence; no isolated sentence invented.',21:'Answer links numerical form to oath opening; do not make beard total two.',22:'Explicit contrast question includes here versus Shabbat/appearance passages.',23:'Textual adjacency, shared variable offering, joint teaching and extension to all classifications separately retained.',24:'Implicitly interrogative opening-versus-explanation sequence recorded as source-explicit question; short versus numerous matters explains order.',25:'Future positive/negative basic two and past positive/negative expanded four distinct.3a10–5a5 context read: proposed all-Yishmael/Akiva identities and liability/exemption and lashes explanations are revised;5a5 ends with Rabbi transmitting oaths per Akiva without personally agreeing.',26:'Impurity-of-sacred/Temple awareness and sacred/Temple-status awareness kept separate; no unnoticed impurity versus unnoticed Temple conflation. Later Rabbi own impurity reasoning versus borrowed oath position not projected as one whole-list holder.',27:'Poor-person/householder roles and outward/inward direction all preserved; later lashes analysis not silently adopted.',28:'Both primary appearances and each derivative retained; no imported colors or specifications. Unit remains open for subsequent author/qualification argument through5a5, context not counted as extracted.'}
for i in range(19,29):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous Gemara and its quotation of preceding teaching',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara' if i>=22 else 'Anonymous Gemara quoting preceding Makkot teaching',role='anonymous',candidates=[],scope='No named position holder established in this segment; do not infer one from subsequent rejected proposals',transmission_chain=[]))
COV=[]
for i in range(19,29):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shevuot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s2])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shevuot_2b12_3a9_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=10,sha256=hashlib.sha256(b).hexdigest())))
