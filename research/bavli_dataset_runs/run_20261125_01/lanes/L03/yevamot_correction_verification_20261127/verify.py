"""Read-only exact-version correction check; no producer promotion or review admission."""
import json,hashlib,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT.parents[5]
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
P=OUT.parent/'yevamot/review_correction_20261126';J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot')
BASE='d2e871c3e71086468534d07c26eda7351bc26789286d55d371a5b95016a22821';HEAD='f826b12fdf8ceb153343497762bb2851ab1fa5865e2d536cb4b5554e6c21276a'
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
bindings={}
for name in ['comparison_frozen.json','reader_frozen.json','verdict_frozen.json','proposal.json','RESPONSE.json','MANIFEST.json']:
 bindings[name]={'path':str(P/name),'sha256':sha((P/name).read_bytes())}
response=read(P/'RESPONSE.json')
for name,key in [('comparison_frozen.json','comparison_sha256'),('reader_frozen.json','reader_sha256'),('verdict_frozen.json','verdict_sha256'),('proposal.json','proposal_sha256')]:assert bindings[name]['sha256']==response[key]
for name,h in read(P/'MANIFEST.json').items():assert sha((P/name).read_bytes())==h
for h in [BASE,HEAD]:assert sha((J/'snapshots'/(h+'.json')).read_bytes())==h
base=read(J/'snapshots'/(BASE+'.json'));head=read(J/'snapshots'/(HEAD+'.json'));proposal=read(P/'proposal.json')
# load re-reads the exact pinned original edition and verifies source/schema/protocol pins.
job,segments=runner.load(J)
rebuilt=runner.validate_apply(base,proposal,segments,job);rebuilt['proposals']=base['proposals']+[bindings['proposal.json']['sha256']]
assert runner.encoded(rebuilt)==runner.encoded(head)
for h in head['proposals']:assert sha((J/'proposals'/(h+'.json')).read_bytes())==h
assert len(proposal['records'])==112 and sum(bool(r.get('supersedes')) for r in proposal['records'])==37
br=runner.report(base,segments);hr=runner.report(head,segments);assert br['completed_by_layer']==hr['completed_by_layer']=={k:178 for k in runner.LAYERS}
assert br['next_unprocessed_by_layer']==hr['next_unprocessed_by_layer']
active={r['id']:r for r in head['records'] if r['release_state']=='valid'};allrows={r['id']:r for r in head['records']}
stale_scope=[r['id'] for r in active.values() if r['content'].get('scope') in allrows and allrows[r['content']['scope']]['release_state']!='valid'];assert not stale_scope
ep=Path(response['export_manifest_path']);assert sha(ep.read_bytes())==response['export_manifest_sha256']
for n,h in read(ep)['files'].items():assert sha((ep.parent/n).read_bytes())==h
byref={s['ref']:s for s in segments.values()}
source_evidence=[]
refs=['2a:1','2a:2','2a:3','2a:4','2b:1','2b:2','2b:3','2b:4','2b:5','2b:6','2b:7','2b:8','4a:5','4a:6','4a:7','4a:8','4a:9','4a:10','4a:11','4a:12','4a:13','4b:1','4b:2']
for ref in refs:
 s=byref['Yevamot '+ref];source_evidence.append({k:s[k] for k in ['id','ref','source_index','text','text_sha256']})
runner.immutable(OUT/'source_evidence.json',runner.encoded({'source_sha256':job['source_sha256'],'purpose':'Bounded original-source correction verification; context not new sample credit','segments':source_evidence}))
def edges_target(suffix):return [r['content']['target_id'] for r in active.values() if r['layer']=='edges' and suffix in r['id']]
assert set(edges_target('edge.yev001.chronology.qual.'))=={'yev.review20261126.permission.death','yev.review20261126.permission.divorce'}
assert edges_target('edge.yev001.refusal.qual.')==['yev.review20261126.permission.miun']
assert active['yev.review20261126.edge.yev001.exclude.qual.0']['content']['target_id']=='yev.review20261126.permission.aylonit'
assert active['yev.review20261126.edge.yev001.exclude.qual.1']['content']['target_id']=='yev.review20261126.permission.miun'
assert active['yev.review20261126.derivation_objection']['content']['target_id']=='yev.review20261126.benazzai.derivation'
assert active['yev004.benazzai_stoning']['release_state']==active['yev004.judah_stoning']['release_state']=='valid'
checks={'exact_base_and_corrected_hashes':True,'frozen_input_hashes':True,'all_accepted_proposal_bytes_preserved':True,'source_schema_protocol_verified':True,'corrected_snapshot_reconstructed_without_promotion':True,'schema_and_all_evidence_offsets':True,'active_graph_no_superseded_dependencies':True,'exact_ID_scope_fields_no_stale_targets':True,'export_manifest_and_files':True,'new_records':112,'superseded_records':37,'coverage_unchanged':hr['completed_by_layer'],'next_unprocessed':hr['next_unprocessed_by_layer'],'chronology_edges_only_death_divorce':True,'refusal_edge_only_miun':True,'exception_edges_match_case':True,'both_stoning_outcomes_remain_active':True}
verdict={'artifact_kind':'nonblind_independent_correction_verification','verdict':'TARGETED_CORRECTIONS_VERIFIED_NO_TRACTATE_ACCEPTANCE','reviewer':'/root/rosh_hashanah','capacity':'Completed bounded three-issue check with available local agent capacity; no paid APIs or producer writes','independence':'Reviewer produced Rosh Hashanah, not Yevamot. Exposed to frozen reading, comparison and producer correction; this is NOT a new blind cohort.','base_snapshot_sha256':BASE,'corrected_snapshot_sha256':HEAD,'bindings':bindings,'source_sha256':job['source_sha256'],'schema_sha256':job['schema_sha256'],'protocol_sha256':job['protocol_sha256'],'checks':checks,'findings':[
 {'id':'YV-ATOMIC','disposition':'verified_for_targeted_correction','evidence_refs':['Yevamot 2a:1','Yevamot 2b:1-8','Yevamot 4a:6','Yevamot 4a:8','Yevamot 4a:12'],'assessment':'Distinct halitzah/yibum/recursion claims, four release cases, two exclusions, six father/son rape/seduction rulings, awaiting-yibum scope/two-prohibition consequence and rhetorical rejection are separately represented. Death/divorce before brother death attaches only to those cases. Actual miun is distinct from mere capacity to refuse. Aylonit timing remains explicitly unadjudicated. Positions retain each split condition. Category-to-exemption edges preserve the listed relation framework; they do not invent fifteen new rulings.','limits':'The two unnamed prohibitions remain an aggregate source assertion; naming them would exceed this brief source. One primary supersedes plus separate split-lineage ledger is the current schema representation, not loss of initial evidence.'},
 {'id':'YV-QUESTION','disposition':'verified_for_targeted_correction','evidence_refs':['Yevamot 4a:8-10'],'assessment':'Explicit מה טעמא דרבי יהודה question is now present with an answer from father_skirt. Rav Giddel transmits Rav’s explanation of Rabbi Yehudah; no independent Rav adoption or Rav–Shmuel opposition is added. The following anonymous adjacency explanation is not silently attributed to Rav.'},
 {'id':'YV-DERIVATION-SCOPE','disposition':'verified_for_targeted_correction','evidence_refs':['Yevamot 4a:5-7'],'assessment':'Rabbi Yehudah’s rhetorical rejection targets Ben Azzai’s adjacency basis. The distinct ov/yidoni derivation is compared with that basis; both original stoning claims remain active. No retraction or reversal of the common penalty is implied by the replacement edge.'}
 ],'reader_caveats_preserved':response['reader_corrections_preserved'],'residual_limits':['This check closes only the three targeted producer issues at the exact corrected hash. It does not certify every claim in the thirty-core reading or full tractate.','Miun/aylonit timing particulars, broader omission/risk review and task-specific qualification remain pending.','Qualification edges from the release cases to recursive exemption are read within the original co-wife framework, not as a general timing rule for every later generation.','No new sampled-source denominator, independent blind-reading credit, precision/recall rate or human certification.'],'new_source_coverage':0,'task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},'tractate_accepted':False,'human_certification':False,'admission_owner':'global coordinator'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(verdict));runner.immutable(OUT/'CHECKS.json',runner.encoded(checks))
manifest={p.name:sha(p.read_bytes()) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(manifest))
print(json.dumps({'verdict_sha256':sha((OUT/'VERDICT.json').read_bytes()),'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes()),'verdict':verdict['verdict']}))
