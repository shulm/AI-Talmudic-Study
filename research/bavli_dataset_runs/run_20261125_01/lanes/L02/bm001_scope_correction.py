"""Targeted producer revision; no independent review or new coverage claimed."""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'research/bavli_production_v1'))
import runner

JOB = pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L02/bavli_bava_metzia')
LANE = pathlib.Path(__file__).parent
REVIEW = pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
EXPECTED = '25ffca05e9a6f9445ac1f1b285f70d8e113e962353c02e0e108ce4aa2d5e5990'
comparison = REVIEW / 'comparisons/bava_metzia_batch001.json'
verdict = REVIEW / 'verdicts/bava_metzia_batch001.json'
assert runner.sha(comparison.read_bytes()) == '5ac8b873f2c15e7f1c532916290ed1e35b3330e09773c57653467411c7448e12'
assert runner.sha(verdict.read_bytes()) == '0a830742f5c4a3b75344e9952436e0dcc6cdb79e23b13d1a61fbd78dc114ada7'
assert runner.read(JOB / 'OWNER.json') == dict(owner='/root/bava_metzia', epoch=2)
assert runner.read(JOB / 'CURRENT.json')['snapshot_sha256'] == EXPECTED
before_replay = runner.replay(JOB)
meta, segments = runner.load(JOB)
old = runner.current(JOB)
byref = {r['ref']: r for r in segments.values()}
active = {r['id']: r for r in old['records'] if r['release_state'] == 'valid'}
prefix = 'bm.gemara001.opening.'
seeds = {prefix + 'claims.' + n for n in ['17', '44', '54']}
affected = set(seeds)
while True:
    prior = set(affected)
    for rid, record in active.items():
        deps = record['links'] + [record['content'].get(k) for k in ['claim_id', 'question_id', 'source_id', 'target_id']]
        if affected.intersection(deps):
            affected.add(rid)
    if prior == affected:
        break
mapping = {rid: rid + '.bm001scope' for rid in affected}

def evidence(ref):
    s = byref['Bava Metzia ' + ref]
    return dict(segment_id=s['id'], start_char=0, end_char=len(s['text']), quote=s['text'])

context = [evidence(ref) for ref in ['2a:5', '2a:10', '2a:11']]
condition = 'Provisional combined-clause hypothesis (חדא קתני) of 2a:5: finding and whole-ownership wording form one combined claim.'
status = ('Provisional wording explanation under the combined-clause hypothesis; that explanation is displaced by the distinct finding/purchase cases at 2a:10–11. '
          'The rule that sight alone does not acquire is not rejected by this displacement.')
propositions = {
    prefix + 'claims.17': 'Under the provisional combined-clause hypothesis, adding כולה שלי to אני מצאתיה is explained as teaching that sight alone does not acquire; this wording explanation is displaced at 2a:10–11, not the nonacquisition rule.',
    prefix + 'claims.44': 'Under the provisional combined-clause hypothesis and the colloquial reading of מצאתיה, the added כולה שלי wording is explained as excluding acquisition by sight alone; this wording explanation is displaced at 2a:10–11, not the nonacquisition rule.',
    prefix + 'claims.54': 'Under the provisional combined-clause hypothesis, retaining both אני מצאתיה and כולה שלי is explained as redundant wording teaching that sight alone does not acquire; this redundancy explanation is displaced at 2a:10–11, not the nonacquisition rule.'
}

def remap(value):
    if isinstance(value, str):
        return mapping.get(value, value)
    if isinstance(value, list):
        return [remap(v) for v in value]
    if isinstance(value, dict):
        return {k: remap(v) for k, v in value.items()}
    return value

records = []
for rid in sorted(affected):
    record = {k: copy.deepcopy(v) for k, v in active[rid].items() if k not in ['release_state', 'review_state', 'ml_eligible']}
    record['id'] = mapping[rid]
    record['supersedes'] = rid
    record['links'] = remap(record['links'])
    record['content'] = remap(record['content'])
    if rid in seeds:
        record['content'].update(proposition=propositions[rid], assertion_mode='conditional', conditions=[condition],
                                 scope='Provisional explanation of Mishnah wording at ' + active[rid]['content']['scope'] + '; dependency displaced at Bava Metzia 2a:10–11; no rejection of sight-nonacquisition.')
        record['evidence'] += copy.deepcopy(context)
    elif record['layer'] == 'positions':
        record['content'].update(conditions=[condition], local_status=status)
        record['evidence'] += copy.deepcopy(context)
    records.append(record)

# Isolate the legal principle from the superseded explanation of repeated wording.
rule_id = 'bm.bm001scope.sight_nonacquisition.claim'
rule_evidence = [copy.deepcopy(active[rid]['evidence'][0]) for rid in sorted(seeds)]
records.append(dict(id=rule_id, layer='claims', evidence=rule_evidence,
    content=dict(proposition='Sight alone does not acquire the found object.', conditions=['Mere seeing without acquisition of possession.'],
                 scope='Legal principle expressly stated at Bava Metzia 2a:6, 2a:8 and 2a:9; kept distinct from the provisional combined-clause explanation of the Mishnah wording.', assertion_mode='asserted'),
    origin='source_paraphrase', uncertainty=[], links=[prefix+'utterances.'+n for n in ['16','43','53']]))
records.append(dict(id='bm.bm001scope.sight_nonacquisition.position', layer='positions', evidence=copy.deepcopy(rule_evidence),
    content=dict(holder_candidates=[], claim_id=rule_id, question_id=None, conditions=['Mere seeing without acquisition of possession.'],
                 local_status='Asserted anonymous source principle; not rejected by the later displacement of the combined-clause wording explanation. No downstream halakhic certification.'),
    origin='source_paraphrase', uncertainty=[], links=[rule_id]))
records.append(dict(id='bm.bm001scope.sight_nonacquisition.attribution', layer='attributions', evidence=copy.deepcopy(rule_evidence),
    content=dict(surface='anonymous Gemara', role='anonymous', candidates=[], scope=rule_id, transmission_chain=[]),
    origin='source_paraphrase', uncertainty=[], links=[rule_id]))

coverage = []
newids = {r['id'] for r in records if not r.get('supersedes')}
for row in old['coverage']:
    c = {k: copy.deepcopy(v) for k, v in row.items() if k != 'proposal_execution'}
    c['record_ids'] = remap(c['record_ids'])
    for record in records:
        if record['id'] in newids and record['layer'] == c['layer'] and any(e['segment_id'] == c['segment_id'] for e in record['evidence']):
            c['record_ids'].append(record['id'])
    if c['record_ids'] != row['record_ids']:
        c['rationale'] += ' BM001-SCOPE: source-based targeted correction distinguishes displaced combined-clause wording explanations from retained nonacquisition principle; dependent IDs repointed. No new source coverage or independent approval.'
        coverage.append(c)

proposal = {k: meta[k] for k in ['schema_version', 'tractate', 'source_sha256', 'schema_sha256', 'protocol_sha256']}
proposal.update(owner='/root/bava_metzia', epoch=2, execution=dict(route='interactive_agent', agent_id='/root/bava_metzia', model_id=None),
                records=records, coverage=coverage, open_tails=old['open_tails'])
candidate = runner.validate_apply(old, proposal, segments, meta)
assert runner.report(candidate, segments)['completed_by_layer'] == before_replay['completed_by_layer']
preserved = [prefix+'claims.3', prefix+'claims.66.reviewfix1', prefix+'claims.70.reviewfix1',
             prefix+'attributions.67.reviewfix1', prefix+'attributions.71.reviewfix1']
after_byid = {r['id']: r for r in candidate['records']}
for rid in preserved:
    assert runner.encoded(after_byid[rid]) == runner.encoded(active[rid])
for rid in seeds:
    revised = after_byid[mapping[rid]]
    assert revised['content']['assertion_mode'] == 'conditional'
    assert 'combined-clause' in revised['content']['conditions'][0]
assert after_byid[rule_id]['content']['assertion_mode'] == 'asserted'
assert all(r['review_state']=='unreviewed' and r['ml_eligible'] is False for r in candidate['records'] if r['id'] in {n['id'] for n in records})
proposal_path = LANE / 'bm001_scope_correction_proposal.json'
runner.immutable(proposal_path, runner.encoded(proposal))
submitted = runner.submit(JOB, proposal_path, '/root/bava_metzia', 2)
replay = runner.replay(JOB)
export_path = JOB / 'exports' / ('bm001_scope_' + submitted['snapshot_sha256'][:12])
export = runner.export(JOB, export_path)
receipt = dict(status='PRODUCER_CORRECTION_SUBMITTED_PENDING_INDEPENDENT_REREVIEW', discrepancy_id='BM001-SCOPE',
    comparison_verdict='REWORK_TARGETED', independent_re_review_completed=False,
    comparison_sha256=runner.sha(comparison.read_bytes()), verdict_sha256=runner.sha(verdict.read_bytes()),
    run_id='run_20261125_01', run_contract_sha256='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174',
    production_git_commit='15bba19d80273232b4554dfe507ceb37e97843a2', owner='/root/bava_metzia', epoch=2,
    source_sha256=meta['source_sha256'], schema_sha256=meta['schema_sha256'], protocol_sha256=meta['protocol_sha256'],
    previous_snapshot_sha256=EXPECTED, snapshot_sha256=submitted['snapshot_sha256'], proposal_sha256=submitted['proposal_sha256'],
    proposal_path=proposal_path.relative_to(ROOT).as_posix(), correction_script_sha256=runner.sha(pathlib.Path(__file__).read_bytes()),
    supersession_map=mapping, new_principle_records=sorted(newids), preserved_record_sha256s={rid:runner.sha(runner.encoded(active[rid])) for rid in preserved},
    rationale='Confirmed same dependency for claim17 as claims44/54 from original 2a:5–11. Revised claims, positions and full dependent closure; isolated the retained legal principle. No reader-side records edited.',
    regression_checks=dict(coverage_unchanged=True, originals_preserved=True, active_dependencies_valid=True, prior_combined_clause_rejection_and_alternative_attributions_unchanged=True, legal_rule_asserted_not_rejected=True),
    replay=replay, export_path=str(export_path), export_manifest_sha256=runner.sha((export_path/'manifest.json').read_bytes()),
    open_tails=old['open_tails'], next_ref='Bava Metzia 3a:14', interior_next_ref='Bava Metzia 23a:3',
    source_segments_remaining_per_pass=3613, full_tractate_review_completed=False, ml_eligible=False, tractate_delivered=False,
    reproduce=['python -X utf8 research/bavli_production_v1/runner.py replay --job-dir '+JOB.as_posix(),
               'python -X utf8 research/bavli_production_v1/runner.py export --job-dir '+JOB.as_posix()+' --output NEW_EMPTY_EXTERNAL_DIRECTORY'],
    correction_route='Independent reviewer compares the new exact snapshot/proposal to frozen initial reading and BM001-SCOPE; existing REWORK_TARGETED verdict remains unchanged until their superseding verdict.')
receipt_path = LANE/'bm001_scope_correction_receipt.json'
runner.immutable(receipt_path, runner.encoded(receipt))
print(json.dumps(dict(snapshot=submitted['snapshot_sha256'],proposal=submitted['proposal_sha256'],receipt=runner.sha(receipt_path.read_bytes()),
                     manifest=receipt['export_manifest_sha256'],revised=len(mapping),new=len(newids),coverage=replay['completed_by_layer'],replay_pass=replay['replay_pass']),indent=2))
