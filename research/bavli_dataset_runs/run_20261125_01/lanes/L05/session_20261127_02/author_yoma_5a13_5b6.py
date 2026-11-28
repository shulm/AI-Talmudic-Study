"""Bounded direct reading: reasons and scope of indispensable inauguration details."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
before='b19a963efc6173c4ac6f795c4f2fe896c9c83b6bc86d3ef48bd0d8c0c1019d73'
S=json.loads((J/'snapshots'/f'{before}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=()):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2702.next.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin='source_paraphrase',uncertainty=list(unc),links=list(links)));return rid
def claim(k,ii,p,scope,cond=(),holder=None):
 c=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode='asserted'))
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[c])
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=list(cond),local_status='Reported local interpretation; AI provisional'),[c])
 return c
def q(k,ii,p,conditions):return add(k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=conditions,answer_set_status='partial'))
def edge(k,ii,a,b,relation):return add(k,'edges',ii,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),[a,b])
s=add('scope','structure',range(80,87),dict(title='מקורות עיכוב במילואים והרחבת הכתוב למכנסיים, עשירית האיפה ומקרא פרשה',primary=True,boundary='open_both',legacy_ids=[]),unc=['Continuation of prior indispensability dispute; bounded stop before clothing-order discussion. Existing open structures retained.'])
edge('continuation',80,'yom.s2701.mil_required',s,'continuation')
roles={80:'Source question, Rabbi Yitzhak bar Bisna answer and opening objection',81:'Cross-folio completion of scope objection',82:'Three proposed sources extending indispensability',83:'Baraita: three command formulations and distinct meanings',84:'Rabbi Yose bar Hanina: unmentioned garments and meal-offering inclusion',85:'Question and verbal analogy for tenth-ephah inclusion',86:'Rabbi Yohanan reporting Rabbi Shimon ben Yohai: reading the passage indispensable'}
for i,r in roles.items():
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous discussion and named teaching as separately attributed',discourse_role=r,composition='composite'))
 if i in [80,81,83,85]:add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara / baraita',role='anonymous',candidates=[],scope=r,transmission_chain=[]))
qs={};cs={}
qs['all']=q('q.all',80,'What is the reason for the view that every written detail of the inauguration rites is indispensable?', ['All-written-details view identified earlier','Inauguration rites'])
cs['kakha']=claim('kakha',80,'Rabbi Yitzhak bar Bisna derives indispensability from ועשית לאהרן ולבניו ככה: ככה indicates an indispensable requirement.','Source for all-written-details view',holder='רבי יצחק בר ביסנא')
qs['outside']=q('q.outside',[80,81],'That accounts for matters written in this passage; from where is indispensability of matters not written in this passage derived?', ['ככה argument','Distinguish details within the cited passage from details elsewhere'])
cs['petah']=claim('petah',82,'Rav Nahman bar Yitzhak derives the extension by פתח–פתח.','First proposed source for details outside the cited passage',holder='רב נחמן בר יצחק')
cs['guard']=claim('guard',82,'Rav Mesharshiya treats ושמרתם את משמרת ה׳ as indicating indispensability.','Another source for the extension; preserve as separate answer',holder='רב משרשיא')
cs['command']=claim('command',82,'Rav Ashi treats כי כן צויתי as indicating indispensability.','Another source for the extension; not merged with prior proofs',holder='רב אשי')
cs['mourning']=claim('mourning',83,'The baraita interprets כי כן צויתי as instructing that they eat it during acute mourning (אנינות).','First of three distinct command-formula interpretations',cond=['Eating in אנינות'],holder='Anonymous quoted baraita')
cs['time']=claim('time',83,'The baraita interprets כאשר צויתי as saying that he told them at the time of the action.','Second command-formula interpretation; timing of the instruction',holder='Anonymous quoted baraita')
cs['authority']=claim('authority',83,'The baraita interprets כאשר צוה ה׳ as “I am not saying this on my own authority.”','Third command-formula interpretation; reported divine authority, not a new human attribution',holder='Anonymous quoted baraita')
cs['absent']=claim('absent',84,'Rabbi Yose bar Hanina states that the breeches are not written in this passage.','Local absence claim, not absence from all garment passages',holder='רבי יוסי בר חנינא')
cs['breeches']=claim('breeches',84,'וזה הדבר אשר תעשה להם לקדש אותם לכהן includes the breeches.','First inclusion in Rabbi Yose bar Hanina teaching',holder='רבי יוסי בר חנינא')
cs['tenth']=claim('tenth',84,'The same wording includes the tenth-ephah offering.','Second inclusion in Rabbi Yose bar Hanina teaching',holder='רבי יוסי בר חנינא')
cs['garment']=claim('garment',85,'Breeches are written in the garment context, making their inclusion intelligible.','Concession before question about the tenth-ephah offering')
qs['tenth']=q('q.tenth',85,'But from where is inclusion of the tenth-ephah offering derived?', ['Breeches already occur in garment context','Need source for tenth-ephah inclusion in inauguration requirements'])
cs['zeh']=claim('zeh',85,'The זה–זה analogy links this passage to וזה קרבן אהרן ובניו ... עשירית האיפה.','Specific source for tenth-ephah inclusion; both sides of verbal link retained')
qs['reading']=q('q.reading',86,'From where do we know that even reading the passage is indispensable?', ['Inauguration rites','Extension beyond physical actions'])
cs['reading']=claim('reading',86,'Rabbi Shimon ben Yohai teaches that even reading the passage is indispensable, from ויאמר משה אל העדה זה הדבר אשר צוה ה׳; even speech is indispensable.','Rabbi Yohanan reports in Rabbi Shimon ben Yohai’s name; not assigned as Yohanan’s independent view',holder='רבי שמעון בן יוחאי')
add('reading.reporter','attributions',86,dict(surface='רבי יוחנן',role='transmitter',candidates=['רבי יוחנן'],scope='Even reading the passage is indispensable',transmission_chain=['רבי יוחנן','רבי שמעון בן יוחאי']),[cs['reading']])
for k,i,c,t in [('kakha',80,'kakha','all'),('petah',82,'petah','outside'),('guard',82,'guard','outside'),('command',82,'command','outside'),('zeh',85,'zeh','tenth'),('reading',86,'reading','reading')]:edge('answer.'+k,i,cs[c],qs[t],'answer')
edge('outside.objection',[80,81],qs['outside'],cs['kakha'],'objection')
edge('tenth.proof',85,cs['zeh'],cs['tenth'],'support')
edge('all.proof',80,cs['kakha'],'yom.s2701.all','support')
notes={80:'Explicit question and ככה proof retained; objection read across folio to5b1.',81:'Full split objection includes matters written and not written in the cited passage; neither half omitted.',82:'Three named answers retained separately; Rav Nahman bar Yitzhak not collapsed into Rav Nahman.',83:'Three similar command formulas map to three distinct explanations: mourning, timing, divine authority.',84:'Local breeches absence plus two separate inclusions preserved; no absolute absence claim.',85:'Concession about garment context distinct from tenth-ephah question and זה–זה proof.',86:'Yohanan transmitter and Shimon ben Yohai authority separated; even speech and explicit verse retained. Subsequent clothing-order discussion read for boundary only, no new coverage.'}
C=[]
for i in range(80,87):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==I[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Actual source omission reread: ' if l=='reconciliation' else 'Direct source '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=C,open_tails=S['open_tails']+[s])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_5a13_5b6_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),sha256=hashlib.sha256(b).hexdigest())))
