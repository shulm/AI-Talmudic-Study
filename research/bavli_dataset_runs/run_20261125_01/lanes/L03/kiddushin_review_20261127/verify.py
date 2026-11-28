"""Independent, nonblind comparison against a separately frozen source-first reading."""
import json, hashlib, sys
from pathlib import Path
OUT=Path(__file__).parent
ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists(): ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin')
P=OUT.parent/'kiddushin/bounded_001_20261127'
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/readings/kiddushin_batch001.json')
HEAD='485622fdbe5533eba01863f478943dfd0b7ad5ffa38f9832c18776dbd4f74e2d'
PH='1ba6786415d87e15834b70f181ead177deb8988224f993a2a4bafd9e33dac1c2'
RH='36a55f796bb1e1e90d692370449f372186886a7f14e96b8bc937a9e3b962db16'
assert sha(R.read_bytes())==RH
reader=read(R)
for pin in [reader['source'],reader['original_source_schema'],reader['frozen_plan']]+reader['common_documents']:
 assert sha(Path(pin['path']).read_bytes())==pin['sha256']
assert sha((P/'INITIAL_PROPOSAL.json').read_bytes())==PH
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);rebuilt=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 previous=rebuilt['proposals'];rebuilt=runner.validate_apply(rebuilt,json.loads(b),segs,job);rebuilt['proposals']=previous+[h]
assert runner.encoded(rebuilt)==runner.encoded(head)
receipt=read(P/'RECEIPT.json');ep=Path(receipt['export_directory'])
assert sha((ep/'manifest.json').read_bytes())==receipt['export_manifest_sha256']
for name,h in receipt['export_files'].items():assert sha((ep/name).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:10 for k in runner.LAYERS}
rows={r['id']:r for r in head['records']};byref={s['ref']:s for s in segs.values()}
core=reader['core_refs'][:10]
selected=[c for c in reader['atomic_claims'] if any(e['ref'] in core for e in c['evidence'])]
assert len(selected)==21
for c in selected:
 for e in c['evidence']:assert byref[e['ref']]['text'][e['start_char']:e['end_char']]==e['quote']
targets=['money','document','intercourse','shammai','hillel','perutah_value','get','husband_death','yevamah_acquisition','yevamah_halitzah','yevamah_death','money_word','taking_analogy','purchase_name','jeremiah','two_registers','hekdesh','same_subject','death_not_transfer','consent','consent']
mapping=[{'reader_id':c['id'],'producer_id':'kid001.'+t,'disposition':'represented','note':'Complementary consent polarity is retained in one contrastive proposition.' if i>=19 else 'Source-supported local proposition.'} for i,(c,t) in enumerate(zip(selected,targets))]
assert all(m['producer_id'] in rows for m in mapping)
findings=[
 {'id':'K01','refs':['Kiddushin 2a:1'],'producer_ids':['kid001.shammai.p','kid001.hillel.p'],'reader_ids':['kiddushin_b001_c004','kiddushin_b001_c005'],'category':'editorial_question_not_adjudicated','severity':'task_limitation','disposition':'deferred; no comparable answer-set admission','evidence':'בכסף בית שמאי אומרים בדינר ובשווה דינר ובית הלל אומרים בפרוטה ובשווה פרוטה','judgment':'Both school-specific amounts and scope edges are correct. A shared editorial monetary-threshold question and linked comparable positions are absent; question_id remains null. This does not omit an explicit source question. Before scholar-choice use, add/review the common question and its conditions; no such eligibility is granted here.'},
 {'id':'K02','refs':['Kiddushin 2a:1'],'producer_ids':['kid001.a.mishnah','kid001.a.shammai','kid001.a.hillel'],'reader_ids':['kiddushin_b001_c001','kiddushin_b001_c002','kiddushin_b001_c003','kiddushin_b001_c006'],'category':'reader_attribution_overbreadth','severity':'reader_caveat','disposition':'preserve reader; accept producer narrower attribution','evidence':'נקנית בכסף בשטר ובביאה בכסף בית שמאי אומרים','judgment':'Frozen reader repeats Mishnah; Beit Shammai; Beit Hillel as holder list across these claims. Source explicitly attaches school names to monetary amount clauses. Do not import that list as named holdings for every method or valuation.'},
 {'id':'K03','refs':['Kiddushin 2b:5'],'producer_ids':['kid001.consent','kid001.coercion_hyp','kid001.coercion_corrected','kid001.consent_alternative'],'reader_ids':['kiddushin_b001_c020','kiddushin_b001_c021'],'category':'reasonable_granularity','severity':'none','disposition':'accepted locally','evidence':'ואי בעית אימא ... דמדעתה אין שלא מדעתה לא','judgment':'Positive consent and exclusion of coercion are one complementary contrast, not unrelated bundled rulings. Hypothetical coercive inference remains hypothetical and has an explicit correction edge. Alternative answer is anonymous; no named disagreement or retraction of first answer inferred.'},
 {'id':'K04','refs':['Kiddushin 2b:5','Kiddushin 2b:6'],'producer_ids':['kid001.gemara','kid001.subject'],'reader_ids':[],'category':'boundary_granularity','severity':'none','disposition':'accepted open parent / closed child','evidence':'2b:6 begins ומאי איריא דתני שלוש','judgment':'The source reader closes the local subject discussion at 2b:5. Producer closes that child but preserves broad wording discussion open_right; compatible granularity, not a false completion.'}
]
verdict={'verdict':'ACCEPT_PARTIAL_WITH_EXCEPTIONS','scope':'Kiddushin 2a:1–2b:5 only','snapshot_sha256':HEAD,'proposal_sha256':PH,'reader_sha256':RH,'producer_receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'pins':receipt['pins'],'reviewer':'/root/rosh_hashanah','method':'Nonblind comparison of separately frozen source-first reading; comparator read frozen reader before production. Not a new blind cohort. No Kiddushin production by comparator.','core_segments_compared':10,'endpoint_core_segments':10,'probability_core_segments_compared':0,'reader_core_segments_pending_production':20,'reader_claims_compared':21,'reader_claims_represented':21,'confirmed_producer_semantic_errors':0,'task_limitations':['K01'],'reader_caveats':['K02'],'context_read':'Kiddushin 2b:6–3a:7; context only, no coverage or review-core credit','layer_matrix':{k:{'production_completed':10,'bounded_source_checked':10,'tractate_total':2406} for k in runner.LAYERS},'claim_mapping':mapping,'findings':findings,'integrity':{'exact_version_replayed':True,'original_source_and_common_hashes':True,'source_quotes_links_coverage_validated':True,'export_manifest_and_all_files':True},'eligibility':{'ml_eligible':False,'all_demanding_task_eligibility':False,'eligible_records':0},'tractate_acceptance':False,'remaining_source_per_layer':2396,'next_production':'Kiddushin 2b:6','open_tails':['kid001.gemara'],'resume':'Any changed production version needs changed-record/dependency recheck. Remaining 20 frozen sampled cores await production; do not call them omissions. No additional source production or review scope authorized in this bounded comparison.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(verdict))
runner.immutable(OUT/'SOURCE_EVIDENCE.json',runner.encoded([{'ref':r,'source_index':byref[r]['source_index'],'text':byref[r]['text']} for r in core]))
runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}))
manifest={p.name:sha(p.read_bytes()) for p in OUT.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
runner.immutable(OUT/'MANIFEST.json',runner.encoded(manifest))
print(json.dumps({'verdict':verdict['verdict'],'verdict_sha256':manifest['VERDICT.json'],'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes())}))
