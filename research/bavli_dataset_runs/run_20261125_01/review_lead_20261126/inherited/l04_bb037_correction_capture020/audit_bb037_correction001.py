from audit_bb037 import *
P=T/'proposals/ca45f4b1bac7f8cf9b753353b9cebd6ec542952a0b016c8a43c38da04577b774.json'
N=T/'snapshots/ee2e62cbfe215a12296b48c06f4aee841b358f41f2f652cf53fea1343706660f.json'
B=T/'snapshots/45510ebd6b2486c0695e120808be45afa55e373ebad4eacae6d6fd2171842a9d.json'
Q=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/bava_batra/next_release_20261127/BB037_REPAIR_036_RECEIPT.json')
assert sha(Q)=='4f968bcc8782923de8ee2cd8785ceff8eaf156b4017858d51c25b09eb02685bd'
for f in [P,N,B]:assert sha(f)==f.stem
p,n,b=read(P),read(N),read(B);q=read(Q)
old_comparison=O/'bb037_exact_version_comparison.json';old_verdict=O/'bb037_v2_verdict.json'
assert sha(old_comparison)=='bd07e5649e304f72f08cba5ce1356f79c5d6c578d9f11972c2135f19c7ea97da'
assert sha(old_verdict)=='6f8e2c1f1156fc36a56e3cebc76cb070d22bed07fad3f8d34081fe6072cec2d3'
assert n['proposals']==b['proposals']+[P.stem]
assert n['proposals'][:len(s['proposals'])]==s['proposals']
state=m.empty();proposal_bindings=[];parent_reproduced=False
for h in n['proposals']:
 f=T/'proposals'/f'{h}.json';assert sha(f)==h;prev=state['proposals'];state=m.validate_apply(state,read(f),segs,job);state['proposals']=prev+[h];proposal_bindings.append(bind(f))
 if state['proposals']==b['proposals']:assert m.encoded(state)==B.read_bytes();parent_reproduced=True
assert parent_reproduced and m.encoded(state)==N.read_bytes()
newlookup={x['id']:x for x in n['records']};oldlookup={x['id']:x for x in b['records']}
assert all(newlookup[k]==v for k,v in oldlookup.items())
assert all(newlookup[x['id']]==x for x in s['records'])
added=set(newlookup)-set(oldlookup);assert len(added)==8==len(p['records'])
assert added=={x['id'] for x in p['records']}==set(sum(q['issue_to_ids'].values(),[]))
assert all(not x.get('supersedes') for x in p['records'])
def completed(x):return {(c['segment_id'],c['layer']) for c in x['coverage'] if c['extraction_state']=='completed'}
assert completed(n)==completed(b)
completed_counts={l:sum(layer==l for sid,layer in completed(n)) for l in m.LAYERS};assert set(completed_counts.values())=={317}
allowed={br[x]['id'] for x in ['Bava Batra 11b:10','Bava Batra 11b:12','Bava Batra 12a:1']}
assert {c['segment_id'] for c in p['coverage']}==allowed
oldcov={(c['segment_id'],c['layer']):c for c in b['coverage']}
newcov={(c['segment_id'],c['layer']):c for c in n['coverage']}
assert set(oldcov)==set(newcov)
assert all(v==newcov[k] for k,v in oldcov.items() if k[0] not in allowed)
for c in p['coverage']:
 assert set(c['record_ids'])=={x['id'] for x in n['records'] if x['release_state']=='valid' and x['layer']==c['layer'] and any(e['segment_id']==c['segment_id'] for e in x['evidence'])}
for x in p['records']:
 assert newlookup[x['id']]['release_state']=='valid'
 assert set(x['links'])<=set(newlookup)
 for k in ['source_id','target_id','claim_id','question_id']:
  if x['content'].get(k):assert x['content'][k] in newlookup
prefix='bb.r036.'
u=newlookup[prefix+'reopen_lemma.u'];a=newlookup[prefix+'reopen_lemma.a'];auth=newlookup[prefix+'reopen_lemma.quoted_authority'];cl=newlookup[prefix+'reopen_lemma.c'];po=newlookup[prefix+'reopen_lemma.p']
assert u['content']['textual_voice']=='anonymous discussion' and a['content']['role']=='anonymous' and a['content']['candidates']==[]
assert auth['content']['role']=='quoted_authority' and auth['content']['candidates']==['רבי'] and auth['content']['scope']==cl['id']
assert po['content']['claim_id']==cl['id'] and po['content']['holder_candidates']==['רבי']
assert cl['evidence'][0]['quote']=='אמר מר היה סתום ובקש לפותחו אין בני מבוי מעכבין עליו'
edge_expected={'reopen_quotation':('quotation',cl['id'],'bb.r032.reopen.c'),'reopen_retained_qualification':('qualification','bb.r032.retained.c',cl['id']),'four_cubit_distinction':('distinction','bb.r032.nopost.c','bb.r032.closed.c')}
for k,values in edge_expected.items():
 x=newlookup[prefix+k];assert x['layer']=='edges';c=x['content'];assert (c['relation'],c['source_id'],c['target_id'])==values;assert all(newlookup[c[t]]['layer']=='claims' for t in ['source_id','target_id'])
corrected_ev=evidence(p);all_ev=evidence(n)
binds=dict(inherited_contract=bindings,original_comparison=bind(old_comparison),original_verdict=bind(old_verdict),producer_mapping_receipt=bind(Q),immediate_parent317=bind(B),corrected_snapshot317=bind(N),repair_proposal=bind(P),audit_helper=bind(Path(__file__)),exact_prefix_proposals=proposal_bindings)
checks=dict(result='PASS',exact_prefix_replay=True,accepted_proposals=len(n['proposals']),immediate_parent_reproduced=True,added_records=8,supersessions=0,immediate_parent_records_unchanged=len(b['records']),historical310_records_unchanged=len(s['records']),source_inventory_segments=len(segs),repair_exact_evidence_slices=corrected_ev,corrected_snapshot_exact_evidence_slices=all_ev,completed_by_layer_unchanged=completed_counts,coverage_coordinates_unchanged=True,unaffected_coverage_objects_unchanged=True,repair_coverage_ids_exact=True,typed_edge_endpoints_checked=3,original_readings_and_comparison_preserved=True,no_CURRENT_access=True,no_production_writes=True,mechanical_replay_does_not_semantically_admit_intervening_records=True)
audit=put('bb037_correction001_audit.json',dict(artifact_kind='bounded_correction_readonly_replay_audit',agent_id='/root/bb_compare037',role='NONBLIND',bindings=binds,checks=checks))
issues=[dict(id='BB037-P001',result='CORRECTION_VERIFIED_AT_EXACT_VERSION',record_ids=q['issue_to_ids']['BB037-P001'],assessment='Distinct 11b:12 lemma occurrence now has an anonymous citing utterance/attribution, claim and position. Rabbi is correctly identified as quoted authority from 11b:10, not the anonymous current speaker. Quotation points to earlier reopening claim. Rava retained-doorpost qualification points to the new repeated claim; existing removed-post contrast remains intact. Conditions/local status explicitly prevent treating permission as unconditional or as a new doctrine.',source_refs=['Bava Batra 11b:10','Bava Batra 11b:12']),dict(id='BB037-P002',result='CORRECTION_VERIFIED_AT_EXACT_VERSION',record_ids=q['issue_to_ids']['BB037-P002'],assessment='Exact 12a:1 evidence supports typed distinction from removed-post/no-four-cubit claim to closed-house/four-cubit claim. Both endpoints are existing valid claims with correct conditions. Existing separate baraita-to-Rava support relations remain unchanged.',source_refs=['Bava Batra 12a:1'])]
receipt=dict(artifact_kind='bounded_nonblind_correction001_receipt',agent_id='/root/bb_compare037',role='NONBLIND independent original comparator continuation',launch_provenance='Follow-up to original fresh fork:none comparator; not a new source-only reading',result='TWO_TARGETED_CORRECTIONS_VERIFIED',bindings=binds,audit=audit,issues=issues,scope=dict(original_probability_block='block_000028',original_core_refs=j['core_refs'],correction_source_refs=['Bava Batra 11b:10','Bava Batra 11b:12','Bava Batra 12a:1'],new_core_credit=0,new_source_reading_credit=0,new_comparison_core_credit=0,corrected_production_core_count=317,intervening_seven_cores_semantically_evaluated=False,excluded_new_window='Bava Batra 12b:9–13a:1'),preserved_disagreements=[dict(id='BB037-R001',status='Original reader error preserved; parent reports excluding bb037r2.repair from effective valid relation evidence. Frozen reader bytes unchanged; no new corrected reader artifact asserted here.'),dict(id='BB037-G001',status='Tomb composite and atomic outcome/edge restrictions remain unchanged.'),dict(id='BB037-U001',status='Named-report versus anonymous explanation boundary uncertainty remains unchanged.')],history='Original REWORK_TARGETED verdict and both initial/effective reader versions remain immutable. This additive event closes only producer P001/P002 for the exact corrected snapshot; no whole-snapshot acceptance inherited.',current_release015_unchanged=True,producer_modified=False,tractate_accepted=False,full_snapshot_accepted=False,later_versions_inherit_review=False,new_task_eligibility=False,human_certification=False,remaining_scope_owner='Root review lead intakes this bounded receipt; no automatic aggregate credit.')
out=put('bb037_correction001_receipt.json',receipt)
helper=Path(__file__);qsha=helper.with_suffix('.py.sha256');line=sha(helper)+'  '+helper.name+'\n'
if qsha.exists():assert qsha.read_text()==line
else:qsha.write_text(line,encoding='ascii')
assert sha(RP)==bindings['effective_reading']['sha256'] and sha(I)==bindings['initial_reading']['sha256'] and sha(S)==bindings['snapshot']['sha256']
print(json.dumps(dict(receipt=out,audit=audit,helper=bind(helper),checks=checks),ensure_ascii=False))
