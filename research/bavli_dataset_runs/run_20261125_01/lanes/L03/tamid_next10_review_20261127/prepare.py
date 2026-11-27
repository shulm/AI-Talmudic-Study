import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent;sha=lambda b:hashlib.sha256(b).hexdigest()
S=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Kodashim/Tamid/Hebrew/Wikisource Talmud Bavli.json');assert sha(S.read_bytes())=='d37fab6314d84a21da855c5b5d8b91f8bfc594b336817e13393e383ffdcd453d'
t=json.loads(S.read_text(encoding='utf-8'))['text'];core=[f'Tamid 26a:{n}' for n in range(8,11)]+[f'Tamid 26b:{n}' for n in range(1,8)]
ev=[]
for i,js in [(50,range(4,10)),(51,range(8))]:
 for j in js:
  ref=f'Tamid 26{"a" if i==50 else "b"}:{j+1}';ev.append({'ref':ref,'source_index':[i,j],'text':t[i][j],'role':'core' if ref in core else 'context'})
notes=[
 ('26a:8','Anonymous question','What establishes the separated reading?','question','Continues prior26a7 claim; do not reset argument at batch boundary.'),
 ('26a:8','Anonymous answer','והחונים and שומרים distinguish campers from guards.','derivation','Two lexical categories separated; evidence is both words and חונים לחוד ושומרים לחוד.'),
 ('26a:9','Anonymous objection','Perhaps all of them occupy one place.','hypothetical objection','אימא is not final maintained single-station position.'),
 ('26a:9','Anonymous reply','Rejects the single-place suggestion by comparison with Moses separately in one place.','reply','Keep exact אף אהרן ובניו בחד מקום לחודיה wording; any expansion to each one separately is interpretation, not literal quotation.'),
 ('26a:10','Rav Ashi','Derives from the verse ending שומרים משמרת למשמרת.','alternative derivation','Rav Ashi distinct from Rav; no transmitter chain named here.'),
 ('26b:1','Anonymous inquiry','Were Avtinas/Nitzotz actual upper rooms or merely elevated like upper rooms?','explicit two alternatives','Do not turn question alternatives into established architecture.'),
 ('26b:2','Cited Mishnah','Northern Nitzotz gate was like a portico.','description','Separate from room above.'),
 ('26b:2','Cited Mishnah','An upper room was built above it.','answer evidence','Explicit citation establishes actual upper room; source explicitly Nitzotz, no invented Avtinas description.'),
 ('26b:2','Cited Mishnah','Priests guard above.','spatial allocation','Different group from Levites.'),
 ('26b:2','Cited Mishnah','Levites guard below.','spatial allocation','Separate allocation.'),
 ('26b:2','Cited Mishnah','It had an opening to the unconsecrated area.','description','Keep spatial condition.'),
 ('26b:3','Anonymous source question','What is the source for the arrangement?','question','Citation begins and continues26b4.'),
 ('26b:3','Cited baraita','וילוו עליך וישרתוך speaks of service assisting your work.','derivation','Addressed to priest; not Levites own separate service reading.'),
 ('26b:4','Cited baraita','Alternative suggestion: verse may refer to Levites own work.','rejected alternative','Not maintained equivalent ruling.'),
 ('26b:4','Cited baraita','ונלוו עליך ושמרו לכל כליו ולכל עבודתו already speaks of their own work.','distinction','Supports eliminating alternative use of first verse.'),
 ('26b:4','Cited baraita','Therefore first verse describes assisting priests work.','conclusion','Repeat occurrence distinct from26b3 opening statement.'),
 ('26b:4','Cited baraita','Priests guard above, Levites below as practical arrangement.','paired conclusion','Producer should recover separate group allocations even if paired textual conclusion retained.'),
 ('26b:5','Mishnah reprise','Beit Hamoked was domed and large.','quoted lemma','Repeated occurrence, not new independent building.'),
 ('26b:6','Anonymous objection','How can one guard suffice when there are two gates?','objection','Do not treat existence of two gates as proof of two guards.'),
 ('26b:6','Cited Mishnah','One gate opens to the hel.','description','Distinct from courtyard gate.'),
 ('26b:6','Cited Mishnah','One gate opens to the courtyard.','description','Different destination.'),
 ('26b:6','Rabbi Yehudah in citation','Courtyard entrance had a small wicket used to inspect the courtyard.','named assertion','Do not attribute Abaye response to Rabbi Yehudah.'),
 ('26b:6','Abaye','One guard suffices because gates stand near one another and he observes each.','conditional reconciliation','Not universal one-guard rule independent of adjacency.'),
 ('26b:7','Anonymous question and gloss','Stone tiers are steps by which one ascends to a platform.','lexical explanation','Do not silently substitute later preparation resolution.'),
 ('26b:7','Anonymous challenge','Were stones split, despite whole-stone building verse?','objection','Keep challenged premise as such.'),
 ('26b:8','Abaye','Small and large stones were prepared and brought beforehand; cites ten-cubit and eight-cubit stones.','context resolution','Answers26b7 challenge; not core coverage.')]
out={'artifact_kind':'frozen_purposive_contiguous_source_reading','reviewer':'/root/rosh_hashanah','source':{'path':str(S),'sha256':sha(S.read_bytes())},'scope':{'core_refs':core,'core_segments':10,'context_refs':[e['ref'] for e in ev if e['role']=='context'],'sampling':'Purposive contiguous next batch, not a new random sample'},'exposure':{'new_production_seen':False,'prior_source_context_seen':'Entire core read previously as context through28a10; first10core production and its correction also reviewed. This is a source-first freeze relative to new labels, not a fresh blind-reader cohort.','central_reading_seen':'Central Tamid first30 sampled reading was previously accessed; no independence from that reading claimed.'},'evidence':ev,'findings':[{'id':f'TA2-{i:02d}','ref':'Tamid '+r,'holder':h,'proposition':p,'status':st,'qualification':q} for i,(r,h,p,st,q) in enumerate(notes,1)],'qualification':{'ml_eligible':False,'all_demanding_tasks':False},'status':'FROZEN_BEFORE_NEXT_BATCH_LABELS'}
b=json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();p=OUT/'SOURCE_READING.json'
if p.exists():assert p.read_bytes()==b
else:p.write_bytes(b)
print(json.dumps({'source_reading_sha256':sha(b),'core_segments':10,'findings':len(notes)}))
