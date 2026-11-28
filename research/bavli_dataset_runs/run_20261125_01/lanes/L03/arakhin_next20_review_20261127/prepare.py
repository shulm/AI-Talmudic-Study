import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent
S=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Kodashim/Arakhin/Hebrew/Wikisource Talmud Bavli.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(S.read_bytes())=='1a25d9524ec1d35eee64749794e158a24bfa10177bc9c6db56b4fca6adbc9ed4'
t=json.loads(S.read_text(encoding='utf-8'))['text']
core=[f'Arakhin 2a:{n}' for n in range(11,18)]+[f'Arakhin 2b:{n}' for n in range(1,14)]
evidence=[]
for i,js in [(2,range(10,17)),(3,range(16))]:
 for j in js:
  ref=f'Arakhin 2{"a" if i==2 else "b"}:{j+1}';evidence.append({'ref':ref,'source_index':[i,j],'text':t[i][j],'role':'core' if ref in core else 'context'})
# These findings were written from original source, before any production access.
findings=[
 ('2a:11','Anonymous','Everything-in-leaning includes an heir; explicitly unlike Rabbi Yehudah.','inclusion','Supported by repeated baraita2a13; do not collapse occurrences.'),
 ('2a:12','Anonymous','Everything-in-substitution includes an heir; explicitly unlike Rabbi Yehudah.','inclusion','Separate action from leaning.'),
 ('2a:13','Anonymous baraita','An heir leans.','asserted','Tannaitic occurrence separate from2a11.'),
 ('2a:13','Anonymous baraita','An heir substitutes.','asserted','Separate from leaning.'),
 ('2a:13','Rabbi Yehudah','An heir does not lean.','disputed position','Scope inheritance of offering.'),
 ('2a:13','Rabbi Yehudah','An heir does not substitute.','disputed position','Not a retraction of leaning.'),
 ('2a:14','Rabbi Yehudah rationale','קרבנו excludes his father’s offering from leaning.','derivation','Textual attribution follows explicit why-question.'),
 ('2a:14','Rabbi Yehudah rationale','Initial consecration/substitution is inferred from end-stage leaning: heir does not substitute.','inference','Preserve direction end→begin, not rabbis reverse direction.'),
 ('2a:15','Rabbis rationale','המר ימיר includes the heir for substitution.','derivation','Distinct opposing interpretive use.'),
 ('2a:15','Rabbis rationale','End-stage leaning is learned from initial-stage substitution: heir leans.','inference','Direction begin→end.'),
 ('2a:16','Rabbis rationale','קרבנו excludes a gentile’s offering from leaning.','derivation','One of separate textual uses.'),
 ('2a:16','Rabbis rationale','קרבנו excludes another person’s offering from leaning.','derivation','Do not merge with father exclusion.'),
 ('2a:16','Rabbis rationale','קרבנו includes all co-owners in leaning.','derivation','Co-owner has stake unlike another’s offering.'),
 ('2a:17','Anonymous analysis of Rabbi Yehudah','One possible account is that he does not admit the co-owner inclusion.','alternative','לית ליה followed by ואי נמי אית ליה; no definitive exclusion.'),
 ('2a:17','Anonymous analysis of Rabbi Yehudah','Alternatively he admits co-owner inclusion.','alternative continuation','Sentence continues2b1; keep uncertainty and competing accounts.'),
 ('2b:1','Anonymous alternative account of Rabbi Yehudah','Gentile and another person exclusions can come from one occurrence.','alternative derivation','Depends on latter2a17 branch.'),
 ('2b:1','Anonymous alternative account of Rabbi Yehudah','One remaining קרבנו excludes his father’s offering.','alternative derivation','Same branch.'),
 ('2b:1','Anonymous alternative account of Rabbi Yehudah','The other remaining occurrence includes all co-owners.','alternative derivation','Do not contradict initial alternative by treating both as simultaneously maintained.'),
 ('2b:2','Rabbi Yehudah rationale / cited baraita','המר ימיר includes a woman in substitution despite masculine wording.','derivation','Explicit question what he uses that phrase for.'),
 ('2b:3','Rabbis rationale','Women are included through ואם.','alternative textual use','Distinct from heir inclusion by doubled phrase.'),
 ('2b:3','Rabbi Yehudah rationale','He does not expound ואם for this inclusion.','negative derivational claim','No general rejection of scriptural exposition inferred.'),
 ('2b:4','Anonymous inclusion / cited Mishnah','A minor not needing his mother is included in sukkah obligation.','conditional inclusion','Keep developmental condition.'),
 ('2b:5','Anonymous inclusion / cited Mishnah','A minor knowing how to wave is included in lulav obligation.','conditional inclusion','Do not apply mother-independence condition here.'),
 ('2b:6','Anonymous inclusion / cited baraita','A minor knowing how to wrap is included in tzitzit obligation.','conditional inclusion','Distinct skill.'),
 ('2b:7','Anonymous inclusion','A minor knowing how to guard tefillin is included.','conditional inclusion','Cited baraita operationalizes father’s purchase.'),
 ('2b:7','Cited baraita','His father buys tefillin for a minor able to guard them.','parental action','Not blanket independent child purchase duty.'),
 ('2b:8','Anonymous initial answer','Pilgrimage-appearance universal includes one half slave and half free.','initial inclusion','Later Ravina objection and chronology must qualify.'),
 ('2b:9','Ravina as quoted','One half slave and half free is exempt from pilgrimage appearance.','quoted position','Distinct from anonymous proposed universal inclusion.'),
 ('2b:9','Anonymous answer under Ravina','The universal may instead include one lame on first day and recovered on second.','conditional alternative','Only fits view that festival days compensate for each other.'),
 ('2b:10','Anonymous objection','Recovered-lameness inclusion works for mutual compensation view, but needs replacement if all compensate only first day.','objection','Two timing positions unnamed, do not invent named holders.'),
 ('2b:11','Anonymous alternative answer','Include one blind in one eye, unlike the following tanna.','alternative inclusion','Do not attribute exemption to this anonymous answer.'),
 ('2b:12','Yohanan ben Dehavai reporting Rabbi Yehudah','One blind in one eye is exempt from appearance.','transmitted position','Reporter not holder alone; neither is Rav Yehudah.'),
 ('2b:12','Same transmitted teaching','See/be-seen analogy requires both eyes.','support','Preserve textual derivation, not clinical statement.'),
 ('2b:13','Anonymous alternative','Return to half-slave/half-free inclusion; distinguish first and final Mishnah to answer Ravina tension.','chronological reconciliation','Read2b14–16 before extracting final status.'),
 ('2b:14','Beit Hillel in initial Mishnah','Half-slave/half-free serves master one day and himself one day.','initial position context only','Later retracted at2b16.'),
 ('2b:15','Beit Shammai','Alternating service fixes master but not man’s marriage/procreation predicament.','objection context only','Cannot marry slave woman or free woman; preserve both prohibitions and creation rationale.'),
 ('2b:16','Beit Shammai / revised Mishnah','Compel master to free him for public order, with debt deed for half value.','solution context only','Two actions; no uncompensated taking claim.'),
 ('2b:16','Beit Hillel','Retract and rule like Beit Shammai.','explicit retraction context only','Do not preserve initial alternating-service as their final local position.')
]
out={'artifact_kind':'frozen_purposive_contiguous_source_reading','reviewer':'/root/rosh_hashanah','tractate':'Arakhin','source':{'path':str(S),'sha256':sha(S.read_bytes())},'scope':{'core_refs':core,'core_segments':20,'context_refs':['Arakhin 2b:14','Arakhin 2b:15','Arakhin 2b:16'],'sampling':'purposive contiguous next production batch; not existing central probability cohort'},'exposure':{'production_seen':False,'earlier_source_exposure':'Original2a11–2b18 read earlier in this session, without production. Central arakhin_batch001 source reading for disjoint selected blocks seen; opening10 and later sampled blocks do not supply this20-core reading.','new_random_or_fresh_blind_cohort_claim':False},'source_evidence':evidence,'findings':[{'id':f'AR2-{i:02d}','ref':'Arakhin '+r,'holder':h,'proposition':p,'local_status':st,'qualification':q} for i,(r,h,p,st,q) in enumerate(findings,1)],'questions_to_preserve':['Each universal-inclusion question is a separate occurrence, not one generic all inquiry.','2a14 Rabbi Yehudah reason;2a16 rabbis use of קרבנו;2b2 Rabbi Yehudah use of המר ימיר;2b9 Ravina-conditioned inclusion;2b10 first-day compensation objection.'],'relation_checks':['Two opposed inference directions at2a14–15.','Alternative Rabbi Yehudah co-owner accounts across page boundary.','Ravina-conditioned replacements vs separate chronology reconciliation; latter does not erase alternative arguments.','Final explicit Beit Hillel retraction is required context for half-slave inclusion; no shifting core scope to count context as coverage.'],'qualification':{'ml_eligible':False,'all_demanding_tasks':False},'status':'FROZEN_BEFORE_PRODUCER_ACCESS'}
b=json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();p=OUT/'SOURCE_READING.json'
if p.exists():assert p.read_bytes()==b
else:p.write_bytes(b)
print(json.dumps({'source_reading_sha256':sha(b),'core_segments':20,'context_segments':3,'findings':len(findings)}))
