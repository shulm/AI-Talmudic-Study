"""Source-adjudicated targeted review corrections; no new source coverage."""
import copy,json,re
from pathlib import Path
from author_lib_cont2 import Author,r
a=Author('r022');state=r.current(a.job)
assert r.sha(r.encoded(state))=='83703222712ce4dda8a900326878ea0351e44318321431771ea10deb69e635a1'
assert r.read(a.job/'OWNER.json')==dict(owner='L04/makkot_resume_20261126',epoch=3)
contract=Path('research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
assert r.sha(contract.read_bytes())=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for f,h in r.read(contract)['production_files'].items():assert r.sha(Path(f).read_bytes())==h
reviews=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated020/comparisons')
pins={'makkot_delegated020_v2_verdict.json':'030c6647347d51b2cecada017587dd0baccaa57f3fcb876ecceed1f0825e3329','makkot_delegated020_context_addendum.json':'9c47fd47a16b9bd1ee3e57131e4b9b302c34eea1efb99ed6934be43456049e98'}
for f,h in pins.items():assert r.sha((reviews/f).read_bytes())==h
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
affected={'ma.r008.vision.u','ma.r008.vision.c','ma.r008.vision.p','ma.r008.camel.u','ma.r008.camel.c','ma.r008.camel.p'}
def ids(x):return set(re.findall(r'ma\.[A-Za-z0-9_.]+',json.dumps(x,ensure_ascii=False)))
while True:
 new={rid for rid,x in active.items() if ids({'content':x['content'],'links':x['links']}) & affected}-affected
 if not new:break
 affected |= new
mapping={old:old+'.review022' for old in affected}
def replace(x):
 if isinstance(x,str):
  return re.sub(r'ma\.[A-Za-z0-9_.]+',lambda m:mapping.get(m.group(),m.group()),x)
 if isinstance(x,list):return [replace(v) for v in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
for rid in sorted(affected):
 old=active[rid];row=replace({k:copy.deepcopy(v) for k,v in old.items() if k not in ['review_state','release_state','ml_eligible','supersedes']});row['supersedes']=rid
 if rid in ['ma.r008.vision.c','ma.r008.camel.c']:
  row['content']['assertion_mode']='asserted'
  row['content']['scope']='Accepted local teaching: do not allow the hypothetical extraordinary '+('vision' if '.vision.' in rid else 'travel')+' possibility to defeat hazama under the stated ordinary-capacity test. No denial of physical possibility or historical measurement.'
 if rid in ['ma.r008.vision.p','ma.r008.camel.p']:row['content']['local_status']='asserted rejection of the hypothetical exceptional-capacity allowance within the local hazama test'
 if rid in ['ma.r008.vision.u','ma.r008.camel.u']:
  row['content']['discourse_role']='explanation rejecting hypothetical allowance';row['content']['composition']='composite'
 a.rows.append(row)
issues=[]
def edge(issue,key,source,target,relation,evidence,note):
 rid=a.add(key,'edges',dict(source_id=source,target_id=target,relation=relation,explicitness='source_explicit'),[a.ev(ref,quote) for ref,quote in evidence],[source,target],uncertainty=[note])
 issues.append(dict(issue_id=issue,decision='corrected',new_ids=[rid],source_refs=[ref for ref,quote in evidence],adjudication=note));return rid
edge('MA020-EDGE-e18','version.qualification','ma.r007.version.c','ma.r007.ullameir.c','qualification',[('4b:3','איכא דמתני להא דעולא אהא דתניא')],'Alternative transmission placement qualifies attribution of the first report; neither occurrence is erased or declared false.')
edge('MA020-EDGE-e19','akiva.objection','ma.r007.akiva.c','ma.r007.yehuda.c','objection',[('4b:4',"ר' עקיבא אומר לא מן השם הוא זה")],'Explicit rejection of Rabbi Yehuda’s reason for this exemption, not merely editorial direction imposed on juxtaposed opinions.')
edge('MA020-EDGE-e21','yehuda.support','ma.r007.yehuda.c','ma.r007.yehinfer.c','support',[('4b:4',"מכלל דר' יהודה סבר לאו שאין בו מעשה לוקין עליו")],'Premise-to-inference direction: the anonymous discussion infers a general view from Rabbi Yehuda’s chosen reason; no new direct speech by Rabbi Yehuda.')
edge('MA020-EDGE-e24','rl.correction','ma.r007.rl.c','ma.r007.ulla2.c','correction',[('4b:6','אלא אמר ריש לקיש גמר מעדים זוממין')],'Replacement of the single-source derivation at this proof stage; later combined proof remains intact. This does not retract the legal conclusion or erase Ulla’s other transmission.')
edge('MA020-EDGE-e34','announce.distinction','ma.r007.announce.c','ma.r007.yirmeya.c','distinction',[('4b:12','ורבנן ההוא מיבעי ליה'),('5a:1','להכרזה')],'The Sages allocate this verse to proclamation rather than the prohibition assigned to Rabbi Meir by Rabbi Yirmeya. Both parts of the cross-page sentence are evidence.')
edge('MA020-EDGE-e41','contradiction.qualification','ma.r008.contradiction.c','ma.r008.self.c','qualification',[('5a:6','כיצד אמרו מעידין אנו באיש פלוני שהרג את הנפש אמרו להם היאך אתם מעידין שהרי נהרג זה או ההורג זה היה עמנו אותו היום במקום פלוני אין אלו זוממין')],'The negative illustration states what does not satisfy the general witness-directed hazama requirement; it is not itself hazama.')
edge('MA020-EDGE-e42','hazama.distinction','ma.r008.hazama.c','ma.r008.contradiction.c','distinction',[('5a:6','אבל אמרו להם היאך אתם מעידין שהרי אתם הייתם עמנו אותו היום במקום פלוני הרי אלו זוממין ונהרגין על פיהם')],'Explicit אבל distinguishes the witnesses’ location from contradiction about victim or killer.')
edge('MA020-CONTEXT-e50','options.distinction','ma.r006.option2.c','ma.r006.option1.c','distinction',[('4a:4',"או דלמא רב לא תני חסר קורטוב ברישא ור' יוחנן בן נורי כי פליג אסיפא הוא דפליג")],'Explicit alternative in Rav Pappa’s question, not a resolution of his uncertainty or a new direct speech by Rav.')
edge('MA020-CONTEXT-e52','setq.objection','ma.r008.setq.q','ma.r008.yehuda.c','objection',[('5b:1',"אי איסטטית היא זו אפי' כת ראשונה נמי לא")],'Question directly challenges the first-set execution limit; no forced resolution of the subsequent קשיא.')
edge('MA020-CONTEXT-e55','rava.correction','ma.r008.rava.c','ma.r008.avahu.c','correction',[('5b:2','אלא אמר רבא הכי קאמר אם אינה אלא כת אחת נהרגת אי איכא טפי אין נהרגין')],'Rava replaces Rabbi Abbahu’s already-executed explanation; Rava’s replacement remains challenged by בלבד and unresolved קשיא, not certified final resolution.')
for name,issue,ref in [('vision','MA020-STATUS01','5a:11'),('camel','MA020-CONTEXT-STATUS01','5a:13')]:
 issues.append(dict(issue_id=issue,decision='corrected',new_ids=[mapping[rid] for rid in sorted(affected) if '.'+name+'.' in rid],source_refs=[ref],adjudication='Existing negative proposition is asserted; position agrees. Utterance marked composite explanation of a rejected hypothetical. Existing answer edge remains directed to its פשיטא question and is revised to the successor claim.'))
new_edges=[x for x in a.rows if x['layer']=='edges' and not x.get('supersedes')]
cov=[]
for old in state['coverage']:
 additions=[x['id'] for x in new_edges if old['layer'] in ['edges','reconciliation'] and any(v['segment_id']==old['segment_id'] for v in x['evidence'])]
 if set(old['record_ids']) & affected or additions:
  row=replace({k:copy.deepcopy(v) for k,v in old.items() if k!='proposal_execution'});row['record_ids']=list(dict.fromkeys(row['record_ids']+additions));row['extraction_result']='records_found' if row['record_ids'] else 'none_found_after_pass';row['rationale']+=' Targeted source reread of4a3–7 and complete4b–5b continuation; status polarity and explicitly supported typed relations adjudicated with dependency closure. No new source coverage or review acceptance.';cov.append(row)
p=dict(schema_version=r.VERSION,tractate='Makkot',owner='L04/makkot_resume_20261126',epoch=3,source_sha256=a.j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/makkot_continuation_2',model_id=None),records=a.rows,coverage=cov,open_tails=state['open_tails'])
out=a.job/'staging'/'continuation_r022_review020.json';r.immutable(out,r.encoded(p));result=r.submit(a.job,out,p['owner'],3)
receipt=dict(status='TARGETED_CORRECTIONS_AWAIT_INDEPENDENT_RECHECK',base_snapshot_sha256=r.sha(r.encoded(state)),result=result,proposal_sha256=r.sha(out.read_bytes()),review_artifact_hashes=pins,issues=issues,revision_mapping=mapping,revision_count=len(affected),added_edges=len(new_edges),coverage_cells_revised=len(cov),source_read=['Makkot4a:1–12','Makkot4b:1–12','Makkot5a:1–20','Makkot5b:1–25'],reader_qualifications_preserved=['MA020-READER01: Rav/anonymous scope remains unresolved; no change to existing anonymous explanation.','MA020-READER02: transmission versus holder distinction retained; no new direct speech assigned.','MA020-READER03: do not copy reader directional objection edges for mere tannaitic juxtaposition.','MA020-READER04: e21 encoded as support premise-to-inference.','Context e49/e57/e59 do not require extra source-explicit edges; accepted comparator qualifications.'],chronology_qualification=r.read(reviews/'makkot_delegated020_context_addendum.json')['chronology_qualification'],independent_review_inherited=False,new_reading_credit=0,new_source_coverage=0,ml_eligible=False)
r.immutable(Path(__file__).with_name('CORRECTION_022_ISSUE_MAP.json'),r.encoded(receipt));print(json.dumps(result,ensure_ascii=False))
