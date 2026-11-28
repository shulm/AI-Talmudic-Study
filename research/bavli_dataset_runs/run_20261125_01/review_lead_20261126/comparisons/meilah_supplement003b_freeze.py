import sys,json
sys.dont_write_bytecode=True
import meilah_supplement003b_inspect as z
import meilah_supplement003b_verify as v
qa=v.verify(); cores=z.a['core_refs']; core=set(cores)
def ev(ref):return {'ref':ref,'start_char':0,'end_char':len(z.texts[ref]),'quote':z.texts[ref]}
pr={x['id']:x for x in z.p['records']};rr={x['id']:x for x in z.r}
specs=[
 ('11b:3','blood.q.goat','blood.c.goat','0011',['11b:2','11b:3','11b:4'],'The permission branch challenges use of scapegoat limbs as the second exceptional case. Retain the prohibited-benefit branch and the garments replacement.'),
 ('11b:6','blood.q.dosa','blood.c.garments','0014',['11b:4','11b:5','11b:6','11b:7'],'Rabbi Dosa permits reuse by an ordinary priest, challenging garments as the second exceptional case. Retain the Sages versus Dosa distinction and the heifer replacement.'),
 ('11b:8','blood.q.general','blood.c.heifer','0016',['11b:7','11b:8','11b:9','11b:10'],'The view that two specified cases can teach generally challenges the two-case exclusion. Retain that conditional branch and the two explicit exclusions answering it.'),
 ('12a:8','bloodletting.q.birds','libations.c.birds','0033',['11b:18','12a:6','12a:7','12a:8','12a:9'],'The animal lacking time challenges the Sages\u2019 exemption for immature birds, not Rabbi Shimon\u2019s liability. Preserve the redemption distinction in the answer.'),
 ('13a:13','growth.q.detached','growth.c.thresher','0069',['13a:13'],'The detached-property requirement objects to the stated field-threshing liability. Preserve Ravina\u2019s dust-benefit answer; do not identify the uncertain plant term.')]
findings=[]
for n,(_,s,t,r,refs,reason) in enumerate(specs,1):
 s='l06.mei.'+s;t='l06.mei.'+t
 assert s in pr and t in pr
 assert not any(x['layer']=='edges' and x['content'].get('source_id')==s and x['content'].get('target_id')==t and x['content'].get('relation')=='objection' for x in pr.values())
 findings.append({'id':f'MS03B-P{n:02}','classification':'confirmed_typed_relation_omission','source_record':s,'target_record':t,'reader_record':'meilah_supp003b.edges.'+r,'reason':reason,'repair':'Add a source-explicit scoped objection relation between these existing semantic endpoints, retaining the answer and conditions. Equivalent precise utterance endpoints are acceptable.','evidence':[ev('Meilah '+f) for f in refs],'content_missing':False})
corrections=[]
for n,r,ref,reason in [
 ('01','claims.0025','11b:3','The proposition says the previous answer fits prohibition, but its condition states permission. The fitting branch must be prohibition; permission belongs to the challenge.'),
 ('02','claims.0033','11b:8','The proposition says the previous answer fits cases not teaching, but its condition says cases can teach. Separate the fitting and challenging branches.'),
 ('03','edges.0045','12b:6','The cited waste rule supports Rabbi Elazar\u2019s general proceeds-to-chamber rule. The reader edge points from the utterance containing Elazar\u2019s rule back to the waste utterance, reversing the support direction. Producer waste-to-Elazar support is preferable.')]:
  rid='meilah_supp003b.'+r;corrections.append({'id':'MS03B-R'+n,'reader_record':rid,'initial_record':rr[rid],'reason':reason,'evidence':[ev('Meilah '+ref)]})
exceptions=[
 'Six reader editorial comparison questions are topic inventories, not six omitted explicit source questions. Answer-set 0027 includes ash claims0054–0056 alongside birds and must not be used as a homogeneous bird-answer set. Other sets mix reports, questions, objections and answers; require proposition and condition filtering before QA use.',
 'Reader narrative claim/position0075 is labelled challenged because its surrounding exchange challenges the reported ruling; the narrative of Ulla sitting is not itself disputed. Similar compound local-status labels describe discourse context, not final acceptance of every atom.',
 'Producer compound claims preserve multiple reader atoms. Record-count differences do not establish whole-content omission. Source כיצד at13a1 introduces listed examples; no separate producer question node is required to preserve that content.',
 'Blood baraita11a13 does not explicitly specify its stage; do not force the Rabbi Shimon timing statement onto the Meir/Shimon-versus-Sages formulation. Derivations by Ulla, the school of Yishmael and Yohanan remain alternatives.',
 '11b15–17 retains both formulations, capture qualification and rabbinic/asmachta answer. Capture stage is not expanded beyond source. Garment/heifer branches and explicit exclusions are preserved; they do not yield a new practical legal conclusion.',
 '12a10 Ulla transmits Yohanan;12b2 Rav Huna transmits Rav, while Rav Hamnuna objects. Anonymous exchanges12a12–13 and12b3 remain anonymous. ר"א at12a2 remains unexpanded; no named-order attribution.',
 '13a7 volunteer nursing arrangement remains underspecified.13a13 קלעילין remains untranslated and dust benefit is the stated explanation. Reader remaining gaps are interpretive uncertainties, retained without invented resolution.',
 'An answer edge alone is not an erroneous enum. Five objections here are additional explicit source relations with identified targets; existing answers are retained, not relabelled.',
 'No later snapshot inheritance, full admission, practical halakhic certification, or task eligibility. Shared inherited L06 overlap is separately quarantined and creates no new independent credit here.'
]
prior_r=z.read(z.B/'readings/meilah_batch001.json')['core_refs']+z.read(z.B/'readings/meilah_supplement002.json')['core_refs_read']
prior_c=z.read(z.B/'comparisons/meilah_batch001_exact_version.json')['compared_core_refs']+z.read(z.B/'readings/meilah_supplement002.json')['core_refs_read']
assert not core.intersection(prior_r);assert not core.intersection(prior_c)
bindings={'reading':v.binding(z.B/'readings/meilah_supplement003b.json'),'snapshot':v.binding(z.J/'snapshots'/f'{z.H}.json'),'runner':v.binding(z.runner),'verifier':v.binding(z.B/'comparisons/meilah_supplement003b_verify.py'),'inspection_helper':v.binding(z.B/'comparisons/meilah_supplement003b_inspect.py'),'neutral_job':z.a['neutral_job_binding'],'source':z.a['source_binding'],'common_documents':z.a['common_document_bindings'],'prior_reading':v.binding(z.B/'readings/meilah_batch001.json'),'prior_supplement':v.binding(z.B/'readings/meilah_supplement002.json'),'prior_comparison':v.binding(z.B/'comparisons/meilah_batch001_exact_version.json')}
scope={'cohort':'supplemental_coordinate_review_not_probability_sample','core_refs':cores,'unique_read_cores':68,'unique_compared_completed_cores':68,'pending_cores':0,'prior_direct_reading_overlap':0,'prior_direct_comparison_overlap':0,'new_direct_reading_cores':68,'new_direct_comparison_cores':68,'new_probability_draw_cores':0,'endpoint_sample_credit':0,'inherited_overlap':'Separately quarantined; excluded from new independent aggregate credit. This receipt does not reconcile inherited union.','original_probability_plan_overlap':'Not reclassified or credited here; coordinator retains original frozen-plan accounting.'}
rows=[{'ref':ref,'source':ev(ref),'reader_record_ids':[x['id'] for x in z.r if ref in z.refs(x)],'producer_record_ids':[x['id'] for x in pr.values() if x.get('release_state')=='valid' and ref in z.refs(x)],'producer_completed_layers':list(qa['compared_by_layer']),'reconciliation':'Compound claims and explicit questions reviewed against source; no whole-content omission established. See scoped relation findings and retained reader qualifications.'} for ref in cores]
elig={k:False for k in ['ml','scholar_choice','attribution','retrieval','qa','argument_extraction','segmentation']}
c={'artifact_kind':'nonblind_exact_version_source_inventory_comparison','bindings':bindings,'comparator':{'provenance':'NONBLIND independent comparator of previously frozen fresh source-only reading; no other active fresh-reader context inspected','originals':'Immutable; corrections are adjudication only'},'scope':scope,'verification':qa,'proposal_prefix':z.p['proposals'],'source_context_reviewed':['Meilah10b1–11a7 preceding context','Meilah11a8–13a13 all68cores','Meilah13b1–10 following context'],'core_reconciliation':rows,'required_changes':findings,'reader_corrections':corrections,'reader_remaining_gaps_preserved':z.a['remaining_gaps'],'reader_comparable_answer_sets_preserved':z.a['comparable_answer_sets'],'exceptions':exceptions,'verdict':'REWORK_TARGETED','confirmed_whole_content_omissions':0,'confirmed_typed_relation_omissions':5,'task_eligibility':elig,'tractate_accepted':False,'full_review_receipt':False,'human_certification':False}
cp=z.B/'comparisons/meilah_supplement003b_exact_version.json'
vp=z.B/'verdicts/meilah_supplement003b_v2_verdict.json'
assert not cp.exists() and not vp.exists()
cp.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
verdict={'verdict':'REWORK_TARGETED','bindings':bindings,'comparison':v.binding(cp),'scope':scope,'layer_matrix':qa,'required_changes':findings,'reader_corrections':corrections,'exceptions':exceptions,'task_eligibility':elig,'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'admission_owner':'global coordinator','remaining':'Repair five explicit relation gaps and recheck a separately pinned correction snapshot; preserve this reading and verdict.'}
vp.write_text(json.dumps(verdict,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'comparison':v.binding(cp),'verdict':v.binding(vp),'verification':qa}))
