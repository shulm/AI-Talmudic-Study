"""Read-only exact-version v2 comparison with explicit human-readable adjudications.
No other Bava Batra independent reading is an input.
"""
import sys
sys.dont_write_bytecode=True
import json,hashlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_bava_batra')
SNAP='f82c4e3f725e0eac9e92ce05eeb4070e085b2aa370f3e27d64445236f3c97077'
READ='0c0763b9a31ce8b183b3ce6f2e2832f5b57f8d0fc98882e89f1942af87de8593'
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
def publish(p,x):
    raw=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():assert p.read_bytes()==raw,'Existing artifact differs'
    else:
        with p.open('xb') as f:f.write(raw)
    return bind(p)
rp=BASE/'readings/bava_batra_batch001.json';assert sha(rp.read_bytes())==READ
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
        if {'source_ref','start','end','quote'}<=o.keys():
            s=byref[o['source_ref']];a,b=o['start'],o['end']
            assert s['source_index']==[o['page_index'],o['segment_index']]
            assert 0<=a<b<=len(s['text']) and s['text'][a:b]==o['quote'];qa['reading_evidence_slices']+=1
        for v in o.values():walk(v)
    elif isinstance(o,list):
        for v in o:walk(v)
walk(reading)
for r in records.values():
    for e in r['evidence']:
        t=segments[e['segment_id']]['text'];a,b=e['start_char'],e['end_char']
        assert 0<=a<b<=len(t) and t[a:b]==e['quote'];qa['producer_evidence_slices']+=1
completed={layer:{c['segment_id'] for c in state['coverage'] if c['layer']==layer and c['extraction_state']=='completed'} for layer in runner.LAYERS}
overlap=[ref for ref in reading['core_refs'] if all(byref[ref]['id'] in ss for ss in completed.values())]
assert len(overlap)==30
findings={f['id']:f for f in reading['findings']}
corefind=[f for f in reading['findings'] if any(e['source_ref'] in overlap for e in f['evidence'])]
assert len(corefind)==46
O='bb.opening001.';V='bb.visual002.';A='bb.alternative003.';M='bb.materials004.'
mapping={1:[O+'joint.c'],2:[O+'custom.c'],3:[O+'gvil.c'],4:[O+'gazit.c'],5:[O+'kefisin.c'],6:[O+'levenim.c'],7:[O+'jointfall.c'],
8:[O+'garden.c'],9:[O+'valley.c'],10:[O+'single.c.granularity015'],11:[O+'singlefall.c'],12:[O+'bothvalley.c.granularity015'],13:[O+'bothvalleyfall.c'],
14:[O+'wallreading.c'],15:[O+'vineyardnotice.c.granularity015'],16:[O+'vineyardliability.c.granularity015'],17:[O+'noharm.c'],
18:[O+'divisionreading.c',O+'forcedwall.c',O+'harm.c'],19:[O+'divisionword.q'],20:[O+'fullwall.c'],
30:[V+'windows.c',V+'above.c'],31:[V+'windows.c',V+'below.c'],32:[V+'windows.c',V+'opposite.c'],33:[V+'home.c'],34:[V+'roof.c'],
35:[V+'roofdistinct.c',V+'fixeduse.c',V+'unknownarrival.c',V+'hide.c'],36:[A+'division.c',A+'force.c',A+'harm.c'],
37:[A+'wallalternative.q',A+'consent.c',A+'noharm.c'],38:[A+'idiom.c'],39:[A+'small.c'],40:[A+'newwall.c'],41:[A+'scripture.c'],42:[A+'altkinyan.c'],
43:[A+'misread.c',A+'prevent.c'],44:[A+'altmarker.c'],45:[A+'altscripture.c'],46:[A+'acquisition.c'],47:[A+'words.q'],48:[A+'directions.c'],49:[A+'possession.c'],
50:[M+'gvil.c'],51:[M+'gazit.c'],52:[M+'kefisin.c'],53:[M+'bricks.c'],54:[M+'halfgazit.c'],55:[M+'brickanalogy.c']}
used=set();comparisons=[]
for f in corefind:
    n=int(f['id'][1:]);rids=mapping[n]
    related=list(rids)
    related += [r['id'] for r in active.values() if r['layer']=='positions' and r['content']['claim_id'] in rids]
    # Include only source-corresponding attribution rows; preserve their exact scopes.
    refs={e['source_ref'] for e in f['evidence']}
    related += [r['id'] for r in active.values() if r['layer']=='attributions' and any(segments[e['segment_id']]['ref'] in refs for e in r['evidence'])]
    related=sorted(set(related));assert all(rid in active for rid in related);used.update(related)
    status='SUPPORTED_CONTENT_REPRESENTED'
    note='Source content, conditions, attribution/transmission and local status checked; no incompatible maintained position inferred.'
    if n in [30,31,32]:
        status='CONTENT_IN_BUNDLED_RULE_ATOMIC_OBLIGATION_NOT_SEPARATE'
        note='Producer windows.c combines three distance obligations; reason nodes separate privacy above/below from light opposite. No distinct obligation node for each independent case; graph-scope issue BB-WINDOW applies.'
    elif n==47:
        status='ASSERTED_PREMISE_ONLY_IN_QUESTION'
        note='Question preserves the objection text, but no claim node explicitly records that acquisition of mere words does not bind. BB-KINYAN applies; do not count a question as an extracted atomic legal premise.'
    elif n==19:
        status='QUESTION_FORM_REPRESENTATION'
        note='The reader item is itself a wording objection, naturally represented as an explicit producer question. No separate substantive legal proposition is missing.'
    elif n==55:
        status='READER_ATTRIBUTION_CORRECTION'
        note='3a:17 continues Rabba son of Rava speaking to Rav Ashi at3a:16; response begins אמר ליה at3a:18. Producer correctly retains the challenger, whereas reader labels this anonymous.'
    elif n in [3,4,5,6,7,8,9,11,12,13,34,40,41,42,46,48,49]:
        note='Producer retains operative condition in proposition/condition fields. Reader often leaves structured conditions empty although its wording/evidence retains the case; do not interpret empty reader list as unconditional.'
    elif n in [18,35,36,37,43]:
        status='COMPOSITE_READER_FINDING_SPLIT_IN_PRODUCER'
        note='Reader finding combines premises/conclusion or case/reason. Producer separates these components; counted as one frozen reader finding, not one verified atomic production claim.'
    comparisons.append({'independent_id':f['id'],'independent_reading':f,'producer_record_ids':related,
      'producer_record_hashes':{rid:sha(runner.encoded(active[rid])) for rid in related},'status':status,'assessment':note})
qm={'q01':[O+'divisionq.q',O+'divisionword.q',O+'wallword.q',A+'wallalternative.q',A+'divisionword.q',A+'wallword.q'],
 'q03':[A+'consentwhy.q'],'q04':[A+'novelty.q',A+'omitprior.q',A+'bettercase.q',A+'knownconsent.q',A+'altwall.q',A+'altomit.q'],
 'q05':[A+'altwithdraw.q',A+'withdraw.q',A+'words.q'],'q06':[M+'gvilchallenge.q']}
questions=[]
for q in reading['questions']:
    if q['id'] not in qm:continue
    rids=qm[q['id']];used.update(rids)
    questions.append({'independent_question':q,'producer_record_ids':rids,
      'assessment':'Aggregate reader question mapped to local producer questions; variants and different cases are not opposing maintained named positions. q06 second version at3a:19 is context only, not extra core.'})
em=[[O+'division.challenge',O+'forced.harm'],[O+'divisionword.objection'],[V+'home.distinction'],[V+'home.distinction'],
 [V+'roof.distinction',V+'fixed.reason',V+'unknown.reason',V+'hide.reason'],[A+'small.answer'],[A+'words.objection'],[A+'words.answer']]
edges=[]
for i,(edge,rids) in enumerate(zip(reading['relations'][:8],em),1):
    assert any(e['source_ref'] in overlap for e in edge['evidence']);used.update(rids)
    note='Supported relation content represented; finer producer question/premise representation retained.'
    if i==1:note='Reader connects alternative damage conclusion to contrary inference; producer attacks its wall-reading premise then derives damage. More precise premise target, not missing opposition.'
    if i in [3,4]:note='Producer distinction targets bundled windows.c, which also includes unrelated light obstruction. Refine targets to above/below privacy obligations; BB-WINDOW.'
    if i in [7,8]:note='Question-based objection/answer exists, but no distinct nonbinding-words claim as reader legal premise; BB-KINYAN.'
    if i==6:note='Reader targets composite initial second-version c36. Producer answers explicit consent question with undersized-courtyard condition; condition preserved.'
    edges.append({'independent_relation_ordinal':i,'independent_relation':edge,'producer_record_ids':rids,'assessment':note})
issues=[{'id':'BB-WINDOW','category':'atomic_claim_and_argument_scope','severity':'moderate_local','resolution_state':'OPEN_TARGETED_REWORK',
 'independent_ids':['c30','c31','c32','c33'],'records':[V+'windows.c',V+'windows.p',V+'windows.challenge',V+'home.distinction'],
 'evidence':findings['c30']['evidence']+findings['c33']['evidence'],
 'finding':'Three distinct window-distance obligations are bundled in one node. The challenge to no visual damage and the house distinction target that aggregate, including opposite-window light obstruction even though the argumentative visual-intrusion force comes from the above/below privacy cases.',
 'required_change':'Add distinct source-anchored obligation claims/positions for above, below and opposite; keep their reasons separate. Scope the visual-intrusion objection and home distinction to the privacy cases or an explicitly scoped privacy aggregate, not the opposite/light component. Preserve all originals through new IDs and supersession where appropriate.',
 'regression_check':'Above/below privacy and opposite/light obligations are independently recoverable; the light-blocking rule is not a premise that visual intrusion is legally damage.'},
 {'id':'BB-KINYAN','category':'atomic_argument_premise_omission','severity':'moderate_local','resolution_state':'OPEN_TARGETED_REWORK',
 'independent_ids':['c47'],'records':[A+'words.q',A+'words.objection',A+'words.answer',A+'acquisition.c'],
 'evidence':findings['c47']['evidence'],
 'finding':'The claim that mere acquisition of words cannot bind the proposed division agreement survives only inside words.q. The source objection and its property-specific resolution have no independently extracted legal premise node.',
 'required_change':'Add a source-anchored claim/position for insufficiency of mere verbal-agreement acquisition in this proposed case, preserving its objection role and undersized consensual-division scope. Link it to the acquisition answer and preserve directions/possession as answers; do not invent a Rabbi Yohanan versus Rav Ashi dispute.',
 'regression_check':'The objection premise is recoverable as a claim with its proper scope, while alternatives remain compatible legal mechanisms and question/answer evidence remains exact.'}]
reader_corrections=[{'id':'BB-READER-C55','category':'speaker_scope','independent_ids':['c55'],
 'finding':'Reader c55 says anonymous, but3a:17 remains in Rabba son of Rava speech begun3a:16 until Rav Ashi answers3a:18. Producer named attribution is supported.',
 'evidence':findings['c54']['evidence']+findings['c55']['evidence']+[{'source_ref':'Bava Batra 3a:18','start':0,'end':len(byref['Bava Batra 3a:18']['text']),'quote':byref['Bava Batra 3a:18']['text']}],
 'required_change':'Preserve frozen original. Record a superseding reader adjudication for c55 holder; do not overwrite or count as producer false attribution.'},
 {'id':'BB-READER-GRANULARITY','category':'denominator_and_conditions','finding':'Several frozen atomic_claim fields are composite (notably c18,c35,c36,c37,c43), and numerous explicit case restrictions remain in prose while conditions is empty. Forty-six is a frozen finding-unit denominator, not a certified complete atomic-claim count.',
 'required_change':'Preserve initial units; any atomization/structured-condition refinement needs its own version and denominator. No extra cores or accuracy percentage are inferred.'}]
bindings={'run_contract':bind(contractp),'runner':bind(runnerp),'schema':bind(REPO/'research/bavli_production_v1/schema.json'),
 'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),'contract_production_commit':contract['production_git_commit'],
 'initial_reading':bind(rp),'snapshot':bind(sp),'source':bind(Path(reading['bindings']['source']['path'])),
 'plan':bind(Path(reading['bindings']['frozen_plan']['path'])),'plan_embedded_sha256':reading['bindings']['plan_sha256'],
 'proposals':proposals,'comparison_script':bind(Path(__file__))}
assert bindings['source']['sha256']==reading['bindings']['source']['sha256']==j['source_sha256']
assert bindings['plan']['sha256']==reading['bindings']['frozen_plan']['sha256']
for k in ['schema','protocol']:assert bindings[k]['sha256']==j[k+'_sha256']
denominators={'independent_core_finding_units':46,'atomic_claim_denominator_certified':False,
 'reader_declared_structured_condition_bearing_findings':sum(bool(f['conditions']) for f in corefind),
 'reader_attributable_findings_including_quoted_anonymous_sources':sum(f['holder_candidates']!=['anonymous'] for f in corefind),
 'corrected_attributable_findings':sum(f['holder_candidates']!=['anonymous'] for f in corefind)+1,
 'core_anchored_question_groups':5,'core_anchored_answer_sets':5,'core_anchored_relations':8,
 'raw_content_missing_findings':0,'findings_with_atomic_obligation_or_premise_rework':['c30','c31','c32','c47'],
 'omission_denominator_policy':'Only frozen independent core findings within completed producer scope; question-only representation is explicitly distinguished from claim nodes.'}
cohorts={'probability_core_segments_compared':30,'endpoint_core_segments_compared':10,'overlap_core_segments':10,
 'unique_core_segments_compared':30,'unprocessed_independent_core_refs':[],'risk_reviewed':0}
matrix={**cohorts,'independent_core_denominators':denominators,'producer_completed_per_layer':{k:len(v) for k,v in completed.items()},'source_segments_total':len(segments)}
used.update(rid for issue in issues for rid in issue['records']);assert all(rid in active for rid in used)
qa.update({'exact_snapshot_in_memory_replay':True,'replayed_snapshot_sha256':SNAP,'source_schema_protocol_hashes':True,
 'initial_reading_verified_before_producer_access':True,'initial_reading_unchanged':sha(rp.read_bytes())==READ,
 'all_preserved_producer_records':len(records),'active_producer_records':len(active),
 'execution_route':'runner.load + validate_apply only, no lock/current selection/promotion/write',
 'other_independent_bava_batra_reading_inspected':False})
artifact={'artifact_kind':'independent_ai_exact_version_comparison_v2','bindings':bindings,'denominators':denominators,'cohorts':cohorts,
 'core_refs':overlap,'context_refs_not_in_core_denominator':reading['context_refs'],
 'context_comparison':'Only continuations necessary for core interpretation; 3a:18–20 checked for named challenge/reply boundaries. q02 context umbrella not pooled as an extra core/question denominator; q07–q09 not semantically compared here.',
 'claim_comparisons':comparisons,'question_comparisons':questions,'edge_comparisons':edges,
 'answer_set_comparisons':[{'initial_answer_set':a,'scope':'Compare core members only; context members retained but not independently admitted.','comparability':'No automatic choice labels; variants and case-specific reasons remain separate.'} for a in reading['answer_sets'] if a['question_id'] in qm],
 'producer_issues':issues,'reader_corrections':reader_corrections,'qa':qa,
 'mapped_producer_records':{rid:active[rid] for rid in sorted(used)},
 'mapped_producer_record_hashes':{rid:sha(runner.encoded(active[rid])) for rid in sorted(used)},
 'record_hash_contract':'SHA256 sorted-key compact UTF8 JSON ensure_ascii=false followed by LF (runner.encoded).',
 'limits':['30 unique cores only; 10 opening cores overlap probability and endpoint sets and count once.',
 'Original snapshot contains later content; replay does not semantically admit it.',
 'No other overlapping independent reading was inspected or pooled.',
 'No full risk, export or whole-tractate review; no accuracy estimate or human certification.'],
 'human_certification':False,'ml_eligible':False}
cp=publish(BASE/'comparisons/bava_batra_batch001_exact_version.json',artifact)
verdict={'verdict':'REWORK_TARGETED','bindings':bindings,'comparison':cp,'scope':'Exact30 frozen core segments only; partial v2 comparison.',
 'required_changes':issues,'reader_corrections':reader_corrections,'task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},
 'layer_matrix':matrix,'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'admission_owner':'global coordinator',
 'remaining':'Authorized producer revisions for window graph scope and explicit kinyan premise, followed by new exact-version review. Preserve frozen reader c55 error and denominator qualifications in versioned adjudication. Continue remaining independent cores separately.'}
vp=publish(BASE/'verdicts/bava_batra_batch001_v2_verdict.json',verdict)
print(json.dumps({'comparison':cp,'verdict':vp,'matrix':matrix,'qa':qa},ensure_ascii=False))
