"""Source-authored MK054 targeted repairs; no new source-window coverage."""
import copy
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading, r

BASE = 'e5f88150985e9541e2f1a5def9b2975ab102767f3a5b5b2fe05770b5d3ae12e0'
a = ScopedReading('moed_katan', 'Moed Katan', 'mk.r047')
a.agent_id = '/root'
state = r.current(a.job)
assert r.sha(r.encoded(state)) == BASE
assert r.read(a.job/'OWNER.json') == {'owner': 'L04/moed_katan_resume_20261126', 'epoch': 3}
review = a.job.parent/'review_20261127_delegated047/comparisons/mk047_v2_verdict054.json'
assert r.sha(review.read_bytes()) == 'e55a09160f83a74e1b712186f2cd9b211c9a12217006c8e953820716553165b6'
by = {x['id']: x for x in state['records']}
changed = {}
def edit(ident):
    if ident not in changed:
        assert by[ident]['release_state'] == 'valid'
        changed[ident] = copy.deepcopy(by[ident])
    return changed[ident]

# Rav Ashi's reply continues his explicit named sentence. The repeated reply
# at14b:7 is corrected as continuation context, not an extra sampled core.
for key, ref in [('mixed', '14b:3'), ('mixed2', '14b:7')]:
    prefix = 'mk.r040.'+key
    edit(prefix+'.u')['content']['textual_voice'] = 'רב אשי'
    attr = edit(prefix+'.a')
    attr['content'].update(surface='רב אשי', role='speaker', candidates=['רב אשי'])
    attr['evidence'] = [a.evidence(ref)]
    edit(prefix+'.p')['content']['holder_candidates'] = ['רב אשי']

# Rav Huna is the holder of a narrated permission, not a quoted narrator.
edit('mk.r037.market.u')['content'].update(textual_voice='anonymous narrator', discourse_role='narrative report of a ruling')
edit('mk.r037.market.a')['content'].update(role='position_holder', scope='mk.r037.market.c')
edit('mk.r037.market.a')['links'] = ['mk.r037.market.c']
edit('mk.r037.market.a')['uncertainty'].append('Rav Huna is the reported ruling holder; the anonymous narrator reports שרא. No direct speech is reconstructed.')

# The child-mourning consequence depends on both premises, neither promoted
# here into a final ruling. Rav Ashi challenges the converse premise later.
conditions = ['first-version restriction inferred for birth before the festival', 'the challenged converse from festival prohibition to mourning prohibition']
edit('mk.r040.child.c')['content']['conditions'] = conditions
edit('mk.r040.child.p')['content']['conditions'] = conditions
edit('mk.r040.child.c')['content']['scope'] = 'Conditional consequence in the objection, using both the first-version restrictive inference and Pinhas\u2019s converse premise; Rav Ashi subsequently challenges that converse.'

# Follow dependent IDs, including IDs embedded in the legacy free-text scope.
def strings(value):
    if isinstance(value, str): return [value]
    if isinstance(value, list): return [s for v in value for s in strings(v)]
    if isinstance(value, dict): return [s for v in value.values() for s in strings(v)]
    return []
def mentions(row, ident):
    pat = re.compile(r'(?<![A-Za-z0-9_.])'+re.escape(ident)+r'(?![A-Za-z0-9_.])')
    return any(pat.search(v) for v in strings(row['content'])+row['links'])
while True:
    extra = {ident: copy.deepcopy(row) for ident, row in by.items()
             if row['release_state']=='valid' and ident not in changed
             and any(mentions(row, old) for old in changed)}
    if not extra: break
    changed.update(extra)
mapping = {old: old+'.review054' for old in changed}
def remap(value):
    if isinstance(value, str):
        for old in sorted(mapping, key=len, reverse=True):
            value = re.sub(r'(?<![A-Za-z0-9_.])'+re.escape(old)+r'(?![A-Za-z0-9_.])', mapping[old], value)
        return value
    if isinstance(value, list): return [remap(v) for v in value]
    if isinstance(value, dict): return {k: remap(v) for k,v in value.items()}
    return value
for old, row in changed.items():
    for key in ['release_state', 'review_state', 'ml_eligible']: row.pop(key, None)
    row.update(id=mapping[old], supersedes=old)
    row['content'] = remap(row['content'])
    row['links'] = remap(row['links'])
    a.rows.append(row)

# Explicitly omitted permission, retained as this repeated source occurrence.
teaching = a.claim('teaching', '15b:4', 'מנודה שונה ושונין לו',
    'Others may teach a person under niddui.', conditions=['person under niddui'],
    scope='Anonymous cited baraita at this repeated15b:4 occurrence; separate from studying and the hiring permissions.')

# Decompose the cited permitted-grains endpoint without replacing or erasing
# its preserved composite quotation. These are not new independent topics.
grain_claims = []
for key, name in [('hilka', 'חילקא'), ('targis', 'טרגיס'), ('tisni', 'טיסני')]:
    grain_claims.append(a.claim('vow_'+key, '13b:10', 'ומותר באורז בחילקא וטרגיס וטיסני',
        name+' is permitted under the cited vow against דגן.', conditions=['vow against דגן'],
        scope='Decomposition of mk.r037.vow.c at the same source occurrence; anonymous cited authority, not an additional topic.'))

# Do not assign the two מר positions by order. Rava is the describing speaker,
# while these scoped nodes identify the two analogical comparisons themselves.
travel = []
for key, quote, text in [
    ('profit_tour', 'מר מדמי ליה כלשוט', 'One side compares profit travel to touring.'),
    ('profit_food', 'ומר מדמי ליה כלמזונות', 'The other side compares profit travel to livelihood travel.')]:
    cid = a.claim(key, '14a:12', quote, text, candidates=['רבא'],
        conditions=['travel for profit'], scope='Rava describes an opposing comparison; this is not Rava\u2019s own tannaitic ruling. Decomposition of mk.r039.compare.c; individual tannaitic identity is not inferred from מר order.')
    a.rows[-1]['content']['holder_candidates'] = []
    a.rows[-1]['uncertainty'].append('Named citing/describing speaker is Rava; this comparison node does not assign an original tannaitic holder by order.')
    travel.append(cid)

# Six reviewed relation patterns: the grain-vow support expands into all
# three explicit permitted grain endpoints, yielding eight concrete edges.
edges = []
edges.append(a.e('wet_support', 'mk.r037.wet.c', 'mk.r037.impure.c', 'support', '13b:8'))
for cid in grain_claims:
    edges.append(a.e('changed_support_'+cid.split('.')[-2], 'mk.r037.changed.c', cid, 'support', '13b:10'))
edges.append(a.e('profit_tour_analogy', travel[0], 'mk.r039.tour.c', 'analogy', '14a:12'))
edges.append(a.e('profit_food_analogy', travel[1], 'mk.r039.food.c', 'analogy', '14a:12'))
edges.append(a.e('child_objection', mapping['mk.r040.child.c'], 'mk.r040.infer.c', 'objection', '14b:1'))
edges.append(a.e('converse_support', 'mk.r040.negative.c', mapping['mk.r040.child.c'], 'support', '14b:1'))
for row in a.rows:
    if row['id'] in edges[-2:]:
        row['evidence'] = [a.evidence('14a:16'), a.evidence('14a:17'), a.evidence('14b:1')]
        row['uncertainty'].append('Local hypothetical objection depends on both premises; this does not validate the converse after Rav Ashi\u2019s response or assert child mourning obligations.')

active = {ident: row for ident,row in by.items() if row['release_state']=='valid' and ident not in mapping}
active.update({row['id']: row for row in a.rows})
affected = {(ev['segment_id'], row['layer']) for row in a.rows for ev in row['evidence']}
affected.update((cell['segment_id'],cell['layer']) for cell in state['coverage'] if set(cell['record_ids']) & set(mapping))
coverage = []
for cell in state['coverage']:
    if (cell['segment_id'],cell['layer']) not in affected: continue
    row = copy.deepcopy(cell); row.pop('proposal_execution', None)
    row['record_ids'] = sorted(x['id'] for x in active.values() if x['layer']==row['layer'] and any(ev['segment_id']==row['segment_id'] for ev in x['evidence']))
    row['extraction_result'] = 'records_found' if row['record_ids'] else 'none_found_after_pass'
    row['rationale'] = 'Targeted MK054 source reread: preserve named Rav Ashi replies, anonymous narration/reported Rav Huna holder, repeated teaching permission, atomic relation endpoints and conditional argument stages. Existing source window only; unresolved reader/granularity/attribution restrictions remain. '+row['layer']+' surviving inventory reconciled.'
    coverage.append(row)
assert len(coverage)==len(affected), 'No new coverage cells allowed'
p = dict(schema_version=r.VERSION, tractate=a.title, owner='L04/moed_katan_resume_20261126', epoch=3,
    source_sha256=a.meta['source_sha256'], **r.hashes(), execution=dict(route='interactive_agent', agent_id='/root', model_id=None),
    records=a.rows, coverage=coverage, open_tails=remap(state['open_tails']))
preview = r.validate_apply(state, p, a.source, a.meta)
sup = {x['id'] for x in preview['records'] if x['release_state']=='superseded'}
for row in preview['records']:
    if row['release_state']=='valid': assert not any(mentions(row, ident) for ident in sup), row['id']
assert r.report(preview,a.source)['completed_by_layer']==r.report(state,a.source)['completed_by_layer']
out = a.job/'staging'/'resume_moed_katan_review054_047.json'
r.immutable(out, r.encoded(p))
receipt = dict(status='PREVALIDATED_PENDING_SUBMISSION_AND_INDEPENDENT_RECHECK', base_snapshot=BASE,
    proposal_path=str(out), proposal_sha256=r.sha(out.read_bytes()), supersession_mapping=mapping,
    new_records=len(a.rows)-len(mapping), coverage_cells_updated=len(coverage), completed_by_layer=r.report(preview,a.source)['completed_by_layer'],
    issue_mapping={'MK054-001':[mapping['mk.r040.mixed.'+s] for s in ['u','a','p']],
        'MK054-002':[teaching], 'MK054-003':edges,
        'MK054-004':[mapping['mk.r037.market.u'],mapping['mk.r037.market.a']]},
    context_only_parallel_repair=[mapping['mk.r040.mixed2.'+s] for s in ['u','a','p']],
    restrictions='All original reader errors, composite-unit/holder/stage and uncertainty findings retained; no new core credit or full acceptance.',
    actual_author='/root', no_new_source_window=True)
r.immutable(Path(__file__).with_name('REPAIR_MK054_047_PREVALIDATION.json'), r.encoded(receipt))
print(json.dumps(receipt, ensure_ascii=False, indent=2))
