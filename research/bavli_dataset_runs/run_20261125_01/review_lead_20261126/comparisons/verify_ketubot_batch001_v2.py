"""Exact frozen Ketubot comparison; source-only reader precedes nonblind audit."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_ketubot')
SNAP='feaf61875f433691257d835a4681cfa805156825c0725a7d47dec13a4a84eea9'
READ='b71dcfa8a19601fea9e55b25210c566980a7a625da7c9b933511628cb4f8547e'
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
def publish(p,x):
    raw=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():assert p.read_bytes()==raw
    else:
        with p.open('xb') as f:f.write(raw)
    return bind(p)
rp=BASE/'readings/ketubot_batch001.json';assert sha(rp.read_bytes())==READ
reading=json.loads(rp.read_bytes())
sp=JOB/'snapshots'/f'{SNAP}.json';assert sha(sp.read_bytes())==SNAP
state=json.loads(sp.read_bytes())
contractp=REPO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
pointer=json.loads((REPO/'research/bavli_dataset_runs/ACTIVE_RUN.json').read_bytes())
assert sha(contractp.read_bytes())==pointer['contract_sha256']
contract=json.loads(contractp.read_bytes());runnerp=REPO/'research/bavli_production_v1/runner.py'
assert sha(runnerp.read_bytes())==contract['production_files']['research/bavli_production_v1/runner.py']
spec=importlib.util.spec_from_file_location('frozen_readonly_runner',runnerp)
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
j,segments=runner.load(JOB);byref={v['ref']:v for v in segments.values()}
replayed=runner.empty();proposals=[]
for h in state['proposals']:
    p=JOB/'proposals'/f'{h}.json';assert sha(p.read_bytes())==h
    replayed=runner.validate_apply(replayed,json.loads(p.read_bytes()),segments,j)
    replayed['proposals'].append(h);proposals.append(bind(p))
assert replayed==state and sha(runner.encoded(replayed))==SNAP
records={r['id']:r for r in state['records']};active={k:r for k,r in records.items() if r['release_state']=='valid'}
qa={'reading_evidence_slices':0,'producer_evidence_slices':0}
def walk(o):
    if isinstance(o,dict):
        if {'ref','start_char','end_char','quote'}<=o.keys():
            s=byref[o['ref']];a,b=o['start_char'],o['end_char']
            assert s['source_index']==[o['page_index'],o['segment_index']]
            assert 0<=a<b<=len(s['text']) and s['text'][a:b]==o['quote'];qa['reading_evidence_slices']+=1
        for v in o.values():walk(v)
    elif isinstance(o,list):
        for v in o:walk(v)
walk(reading)
for r in records.values():
    for e in r['evidence']:
        s=segments[e['segment_id']];a,b=e['start_char'],e['end_char']
        assert 0<=a<b<=len(s['text']) and s['text'][a:b]==e['quote'];qa['producer_evidence_slices']+=1
completed={layer:{c['segment_id'] for c in state['coverage'] if c['layer']==layer and c['extraction_state']=='completed'} for layer in runner.LAYERS}
overlap=[ref for ref in reading['core_refs'] if all(byref[ref]['id'] in ss for ss in completed.values())]
unprocessed=[ref for ref in reading['core_refs'] if ref not in overlap]
assert len(overlap)==20 and len(unprocessed)==10
findings={f['id']:f for f in reading['findings']}
corefind=[f for f in reading['findings'] if any(e['ref'] in overlap for e in f['evidence'])]
assert len(corefind)==36
O='kt.open1.';B='kt.resume26.b2.';C='kt.resume26.b3.'
mapping={1:[O+'c.virgin'],2:[O+'c.widow'],3:[O+'c.courts',O+'c.complaint'],4:[O+'c.initial_derivation',O+'c.sunday_initial'],
5:[O+'c.deadline'],6:[O+'c.deadline'],7:[O+'c.direction'],8:[O+'c.court_reform'],9:[O+'c.feast'],10:[O+'c.sunday_final'],
11:[O+'c.ill_him'],12:[O+'c.ill_her'],13:[O+'c.niddah'],14:[O+'c.him_excuse'],15:[O+'c.him_distinguish'],16:[O+'c.her_ready'],17:[O+'c.her_misfortune'],18:[O+'c.expected.condrev1'],
23:[B+'c.water'],24:[B+'c.water'],25:[B+'c.city'],26:[B+'c.village'],27:[B+'c.mehasya'],28:[B+'c.chamber_repeat'],29:[B+'c.intercourse_repeat'],30:[B+'c.order_repeat'],31:[B+'c.sleep_repeat'],32:[B+'c.niddah',C+'c.restate'],33:[B+'c.adorn_repeat'],34:[B+'c.evenings'],35:[B+'c.evenings'],36:[C+'c.private'],37:[C+'c.notconsummated',C+'c.menstrual_referent'],38:[C+'q.consummated'],39:[C+'c.restate'],40:[C+'q.lenient']}
used=set();cc=[]
for f in corefind:
    n=int(f['id'][1:]);rids=mapping[n];related=list(rids)
    related += [r['id'] for r in active.values() if r['layer']=='positions' and r['content']['claim_id'] in rids]
    refs={e['ref'] for e in f['evidence']}
    related += [r['id'] for r in active.values() if r['layer']=='attributions' and any(segments[e['segment_id']]['ref'] in refs for e in r['evidence'])]
    related=sorted(set(related));assert all(rid in active for rid in related);used.update(related)
    status='SUPPORTED_CONTENT_REPRESENTED';note='Checked source content, inherited conditions, holder/transmitter roles and local status.'
    if n in [5,6,34,35]:
        status='BUNDLED_ATOMIC_RESULTS';note='Distinct independent rules share one producer claim/position; no wholly absent content, but not separately retrievable atomic results. KT-ATOMIC applies.'
    elif n in [23,24,37]:
        status='MIXED_BRANCH_CONDITION_REWORK';note='A single condition set covers opposing branches inside one proposition. Preserve explicit branch-specific conditions and positions; KT-BRANCH applies.'
    elif n in [38,40]:
        status='QUESTION_FORM_REPRESENTATION';note='Reader labels a rhetorical objection/inference as atomic_claim. Producer preserves it as an explicit question with its local conditions; do not count the interrogative formulation as a missing maintained ruling.'
    elif n==7:
        status='READER_SPEECH_VOICE_REFINEMENT';note='Rav Yosef initiates the objection; the precise explicit-reason reformulation occurs in an anonymous clarification. Producer u4a/u4b separates voices and position says objection as clarified. Reader should preserve that distinction rather than quote the whole refined wording as direct Rav Yosef speech.'
        related += [O+'u4a',O+'u4b'];used.update([O+'u4a',O+'u4b'])
    elif n==9:
        note='Sages are enactment holders; Rav Yehuda transmits Shmuel reporting the enactment. Producer separates collective holder and report chain; reader Shmuel holder is a reporting-level label, not authorship by Shmuel.'
    elif n in [11,12,13,14,15,16,17,18]:
        note='First-version assertions and alternative inquiry branches remain distinct. k18 conclusion uses the explicitly recorded context continuation at2a:11–2b:1, without counting context as extra core.'
    related=sorted(set(related))
    cc.append({'independent_id':f['id'],'independent_reading':f,'producer_record_ids':related,
      'producer_record_hashes':{rid:sha(runner.encoded(active[rid])) for rid in related},'status':status,'assessment':note})
qm={'q1':[O+'q.why_initial',O+'q.why_final',O+'q.sunday_wedding'],'q2':[O+'q.him'],'q3':[O+'q.her'],
 'q4':[O+'q.niddah',O+'q.unexpected'],'q5':[B+'q.locality'],'q6':[C+'q.consummated',C+'q.likewise',C+'q.lenient']}
qc=[]
for q in reading['questions']:
    if q['id'] not in qm:continue
    used.update(qm[q['id']]);qc.append({'independent_question':q,'producer_record_ids':qm[q['id']],
      'assessment':'Conditional branches and different cases are preserved; no maintenance hypothesis or local mourning inference becomes an enduring named-scholar choice. q5 is reader editorial umbrella; producer locality question is the explicit local question.'})
rm={'r1':[O+'e.direction'],'r2':[O+'e.correction'],'r4':[B+'e.city'],'r5':[B+'e.village'],'r6':[B+'e.mehasya'],
 'r7':[B+'e.baraita_support'],'r8':[C+'e.support_private'],'r9':[C+'e.prior_objection'],'r10':[C+'e.qualify_niddah',C+'e.menstrual_scope']}
ec=[]
for edge in reading['relations']:
    if edge['id'] not in rm:continue
    used.update(rm[edge['id']]);note='Supported local relation preserved; source question versus claim representation documented.'
    if edge['id']=='r6':note='Producer answers explicit locality question with Mata Mehasya restriction; reader local_resolution-to-Rav-Hisda is a coarser summary of that answer. No contradiction inferred.'
    if edge['id']=='r7':note='Producer uses explicit baraita-support marker claim to support Rav Hisda. Reader uses the concrete baraita rule; both preserve support, but producer atomic split must retain it.'
    if edge['id']=='r9':note='Objection historically tests unqualified application to bereavement; it does not refute the final menstruation-qualified rule. Producer question conditions explicitly preserve that historical target; reader relation requires the same caution.'
    if edge['id']=='r10':note='Producer ties restated no-prior-intercourse limitation to the baraita menstruation rule and ties menstrual referent to Rava report. More precise targets than reader omnibus relation.'
    ec.append({'independent_relation':edge,'producer_record_ids':rm[edge['id']],'assessment':note})
issues=[{'id':'KT-BRANCH','category':'mixed_branch_condition_scope','severity':'moderate_local','resolution_state':'OPEN_TARGETED_REWORK',
 'independent_ids':['k23','k24','k37'],'records':[B+'c.water',B+'p.water',C+'c.notconsummated',C+'p.notconsummated'],
 'evidence':findings['k23']['evidence']+findings['k24']['evidence']+findings['k37']['evidence'],
 'finding':'Water-present concession and water-absent saleability occupy one claim conditioned on Water placed on meat. Likewise one Rava claim/position combines pre-consummation separation and post-consummation permission under a condition that intercourse already occurred for the permission. This cannot safely serve branch-specific extraction.',
 'required_change':'Split mutually exclusive branches into distinct claims and positions: watered/unsaleable prepared-feast concession versus unwatered saleability in intermediate locality; menstruation before intercourse requires separation versus after intercourse permits sleeping together. Preserve Rafram/Rav Hisda and Rav Yosef son of Rava/Rava chains, and repoint affected evidence/relations without overwriting originals.',
 'regression_check':'No water-absent saleability record requires water-present; no pre-consummation separation record requires prior intercourse. Place qualifications and menstruation-only scope survive in both claims and positions.'},
 {'id':'KT-ATOMIC','category':'atomic_result_bundling','severity':'moderate_local','resolution_state':'OPEN_TARGETED_REWORK',
 'independent_ids':['k05','k06','k34','k35'],'records':[O+'c.deadline',O+'p.deadline',B+'c.evenings',B+'p.evenings'],
 'evidence':findings['k05']['evidence']+findings['k34']['evidence'],
 'finding':'Maintenance and terumah are separate entitlements with distinct eligibility; Friday-night and Saturday-night prohibitions are distinct temporal claims with different later rationales. Each pair is bundled in one producer claim/position.',
 'required_change':'Create separate atomic claims/positions for the two entitlements, carrying the terumah eligibility restriction, and the two quoted temporal prohibitions, preserving quoted-baraita/local status and continuation restrictions. Apply the same policy to the repeated deadline occurrence rather than deleting repetition.',
 'regression_check':'Each outcome is independently recoverable with its own conditions and source occurrence; Friday prohibition is not silently certified as final in the later first-intercourse discussion, which remains outside compared producer-completed cores.'}]
reader_corrections=[{'id':'KT-READER-VOICE','category':'holder_reporter_and_clarification','independent_ids':['k07','k09'],
 'finding':'k07 should distinguish Rav Yosef initial objection from anonymous refined formulation at2a:4. k09 should distinguish Sages who enacted preparation from Shmuel reporting through Rav Yehuda. Producer records retain these distinctions.',
 'evidence':findings['k07']['evidence']+findings['k09']['evidence'],
 'required_change':'Preserve initial reading and add versioned role/voice refinement; no claim that the producer invented an erroneous named dispute.'},
 {'id':'KT-READER-QUESTION','category':'question_origin_and_unit_count','independent_ids':['q4','k38','k40'],
 'finding':'q4 is marked editorial_reconstruction even though פירסה נדה מהו explicitly asks it. k38/k40 are rhetorical objection/inference units, not independent maintained rulings. Thirty-six is the frozen finding-unit denominator, not a certified all-atomic count.',
 'required_change':'Preserve originals; record question-origin and unit-type refinements in later adjudication.'},
 {'id':'KT-READER-R9','category':'historical_objection_scope','independent_ids':['r9','k37'],
 'finding':'k37 already carries menstruation-only qualification. r9 must mean objection to its prior unqualified bereavement application, not refutation of the finally qualified rule. Producer q.consummated explicitly names the proposed bereavement application.',
 'required_change':'Add historical scope in superseding reader relation annotation; preserve the initial edge.'}]
for b in reading['bindings']:assert sha(Path(b['path']).read_bytes())==b['sha256']
sourcep=Path(next(b['path'] for b in reading['bindings'] if '/Hebrew/' in b['path']))
planp=BASE/'frozen_plans/bavli_ketubot.json'
bindings={'run_contract':bind(contractp),'runner':bind(runnerp),'schema':bind(REPO/'research/bavli_production_v1/schema.json'),
 'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),'contract_production_commit':contract['production_git_commit'],
 'initial_reading':bind(rp),'snapshot':bind(sp),'source':bind(sourcep),'plan':bind(planp),'plan_embedded_sha256':reading['plan_sha256'],
 'proposals':proposals,'comparison_script':bind(Path(__file__))}
assert bindings['source']['sha256']==j['source_sha256']
for k in ['schema','protocol']:assert bindings[k]['sha256']==j[k+'_sha256']
denominators={'independent_completed_core_finding_units':36,'atomic_claim_denominator_certified':False,
 'reader_declared_condition_bearing_findings':sum(bool(f['conditions']) for f in corefind),
 'core_anchored_question_groups':6,'core_anchored_answer_sets':6,'core_anchored_relations':9,
 'raw_content_missing_findings':0,'atomic_or_branch_rework_finding_ids':['k05','k06','k23','k24','k34','k35','k37'],
 'policy':'Only independent findings anchored in producer-completed cores; contextual continuations checked without adding core denominator. Question representations are not counted as maintained claim nodes.'}
cohorts={'probability_core_segments_compared':10,'endpoint_core_segments_compared':10,'overlap_core_segments':0,
 'unique_core_segments_compared':20,'independently_read_core_segments':30,'unprocessed_independent_core_refs':unprocessed,'risk_reviewed':0}
matrix={**cohorts,'independent_core_denominators':denominators,'producer_completed_per_layer':{k:len(v) for k,v in completed.items()},'source_segments_total':len(segments)}
used.update(rid for issue in issues for rid in issue['records']);assert all(rid in active for rid in used)
qa.update({'exact_prefix_in_memory_replay':True,'replayed_snapshot_sha256':SNAP,'source_schema_protocol_hashes':True,
 'initial_reading_verified_before_producer_access':True,'initial_reading_unchanged':sha(rp.read_bytes())==READ,
 'all_preserved_producer_records':len(records),'active_producer_records':len(active),
 'execution_route':'runner.load and validate_apply only; no lock/current selection/promotion/external writes'})
artifact={'artifact_kind':'independent_ai_exact_version_comparison_v2','bindings':bindings,'denominators':denominators,'cohorts':cohorts,
 'core_refs':overlap,'context_refs_not_in_core_denominator':reading['context_refs'],
 'context_comparison':'Read2a:11–2b:4 to resolve conditional maintenance branch and rejected proof;3b:9–5a:5 to resolve prepared-feast, bereavement/menstruation and Saturday-night rationale. No6a–7a sampled findings admitted against unprocessed producer scope.',
 'claim_comparisons':cc,'question_comparisons':qc,'edge_comparisons':ec,
 'answer_set_comparisons':[{'initial_answer_set':a,'assessment':'Same local question only; branch hypotheses, distinct localities and successive qualifications are not enduring scholar-choice alternatives.'} for a in reading['answer_sets'] if a.get('question_id',a.get('question')) in qm],
 'producer_issues':issues,'reader_corrections':reader_corrections,'qa':qa,
 'mapped_producer_records':{rid:active[rid] for rid in sorted(used)},
 'mapped_producer_record_hashes':{rid:sha(runner.encoded(active[rid])) for rid in sorted(used)},
 'record_hash_contract':'SHA256 sorted-key compact UTF8 JSON ensure_ascii=false followed by LF (runner.encoded).',
 'limits':['Ten independently read6a:7–6b:8 sample cores are unprocessed and never counted as omissions.',
 'No whole-tractate, full risk, exported-view or downstream task eligibility certification.',
 'All source and initial reader judgments remain immutable; no human certification or accuracy estimate.'],
 'human_certification':False,'ml_eligible':False}
cp=publish(BASE/'comparisons/ketubot_batch001_exact_version.json',artifact)
verdict={'verdict':'REWORK_TARGETED','bindings':bindings,'comparison':cp,'scope':'Exact20 completed selected core segments only; partial v2 comparison.',
 'required_changes':issues,'reader_corrections':reader_corrections,'task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},
 'layer_matrix':matrix,'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'admission_owner':'global coordinator',
 'remaining':'Authorized branch/atomic revisions, then exact-version targeted verification. Preserve reader voice/question refinements separately. Continue remaining production and independent sampling before any full admission.'}
vp=publish(BASE/'verdicts/ketubot_batch001_v2_verdict.json',verdict)
print(json.dumps({'comparison':cp,'verdict':vp,'matrix':matrix,'qa':qa,'answer_sets_mapped':len(artifact['answer_set_comparisons'])},ensure_ascii=False))
