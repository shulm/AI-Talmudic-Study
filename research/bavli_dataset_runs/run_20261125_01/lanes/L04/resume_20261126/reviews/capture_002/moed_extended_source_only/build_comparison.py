import json,hashlib
from pathlib import Path
out=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/moed_extended_source_only')
sha=lambda b:hashlib.sha256(b).hexdigest()
f=out/'source_reading_frozen.json'; assert sha(f.read_bytes())=='70716a6ff353ec78e66b6dac340dd2184312bdb089ec8a367c39867bd3477b95'
src=json.loads(f.read_bytes()); p=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_moed_katan/snapshots/5fac8984798328adcb8844f711954a943836d40eaad6e6bf605f1589d98cbfaf.json'); assert sha(p.read_bytes())==p.stem
prod=json.loads(p.read_bytes()); byid={r['id']:r for r in prod['records']}
# Manual semantic alignment, after the source-only freeze. Composite independent units can map to several production units.
spec={
'R01':'005.lashes.c 005.no_lashes.c','R02':'005.rule.c 005.why.q 005.hyp_yes.c 005.hyp_no.c','R03':'005.reject.c 005.fine.c 005.limited.c','R04':'005.baraita.q 005.field.c','R05':'005.tree.c','R06':'005.care.c','R07':'005.excluded.q 005.analogy.c','R08':'005.rabbinic.c','R09':'005.dimi.c 005.dimi_q.q 005.unknown.c 005.addition_q.q','R10':'005.elazar.c 005.details.c','R11':'005.yohanan.c 005.yohanan_q.q','R12':'005.shammai.c 005.hillel.c 005.close.c','R13':'005.moist.c','R14':'005.shimon_objection.c 005.fixed.c 005.hillel_pesach.c','R15':'005.annul.c 005.annul.a','R16':'005.annul_q.q 005.greater.c','R17':'005.pause.c 005.allow.c 005.allow.a','R18':'005.own.q 005.sinai.c 005.sinai.a','R19':'005.yitzhak.c','R20':'005.scripture.q 005.akiva.c 005.akiva_end.c','R21':'005.ishmael.c','R22':'005.young.c','R23':'005.young_q.q','R24':'005.split.c','R25':'005.yohanan_annul.c 005.shabbat.c','R26':'005.ashi_q.q','R27':'005.ashi.c','R28':'007.rain.q 007.effort.c','R29':'007.yohanan.c 007.yohanan.a','R30':'007.ashi.c','R31':'007.dispute.c 007.split.c','R32':'007.shmuel.c 007.shmuel.a 007.shmuel_repeat.c 007.shmuel_repeat.a','R33':'007.yirmeya.q','R34':'007.perennial.c','R35':'007.pools.c 007.channel.c','R36':'007.pappa.c','R37':'007.ashi_pool.c 007.time.c','R38':'007.drip.c','R39':'007.stop.q','R40':'007.still.c','R41':'007.spring.c','R42':'007.two_beds.c','R43':'007.one_bed.c','R44':'007.eat.c 007.beauty.c','R45':'007.story.c','R46':'007.ban_man.c 007.ravina.q','R47':'007.thin.c 007.yehuda.c 007.meir.c','R48':'007.explicit_water.q 007.accept.c'}
rows=[]
for r in src['records']:
 ids=['mk.r'+s for s in spec[r['id']].split()]; assert all(x in byid for x in ids)
 rows.append({'independent_id':r['id'],'production_ids':ids,'cohorts':r['cohorts'],'result':'substantive_content_present','note':{'R09':'Speaker of ולא ידענא remains a cautious attribution issue: frozen reading groups first-person uncertainty with Rav Dimi report; production separately makes it anonymous. No explicit named speaker at this clause, so this is retained as unresolved allocation rather than a confirmed production error.','R31':'Frozen reading offered a contextual named allocation only as inference; production leaves named distribution unresolved. Both keep explicit source allocation unknown. Do not promote that inference to a certain attribution.','R37':'Both opposed conditions and rationale are present. See F01 concerning absence of their direct contrast relation.','R17':'Alternative questioner/respondent chains preserved in production uncertainty; narrative pause is anonymous and not assigned to Daniel.'}.get(r['id'],'Matched meaning, conditions and local qualification; production may split the independent composite unit.')})
# Verify all relevant production raw evidence, using original text and full-segment structure anchors to recover the local coordinates.
raw=json.loads(Path(src['source_path']).read_bytes())
lookup={}
for pi,page in enumerate(raw['text']):
 for si,t in enumerate(page):lookup.setdefault(t,[]).append((pi,si))
segmap={}; ambiguous=[]
for r in prod['records']:
 if r['layer']!='structure':continue
 for e in r['evidence']:
  matches=lookup.get(e['quote'],[]) if e['start_char']==0 else []
  if len(matches)==1:segmap[e['segment_id']]=matches[0]
  elif len(matches)>1:ambiguous.append((e['segment_id'],matches))
# Repeated rabbinic answer has two exact occurrences; target context fixes the second at 3a:22.
for r in prod['records']:
 if r['id']=='mk.r005.rabbinic.c':
  for e in r['evidence']:segmap[e['segment_id']]=(4,21)
segmap['seg_5b94125869f70a167683']=(4,20)
checked=0; evidence_fail=[]; missing=[]
relevant=[r for r in prod['records'] if r['id'].startswith(('mk.r005.','mk.r007.'))]
for r in relevant:
 for e in r['evidence']:
  if e['segment_id'] not in segmap:missing.append([r['id'],e['segment_id']]);continue
  pi,si=segmap[e['segment_id']]; ok=raw['text'][pi][si][e['start_char']:e['end_char']]==e['quote']
  checked+=1
  if not ok:evidence_fail.append(r['id'])
assert not evidence_fail and not missing,(evidence_fail,missing)
# Actual production edge check, not merely a missing expected ID.
opposed={'mk.r007.pappa.c','mk.r007.ashi_pool.c'}
direct=[r['id'] for r in relevant if r['layer']=='edges' and {r['content']['source_id'],r['content']['target_id']}==opposed]
assert not direct
findings=[{'id':'F01','classification':'relation_representation_gap','severity':'minor','cohort':'probability_core','ref':'Moed Katan 4a:17','independent_relation':{'from':'R37','to':'R36','type':'disagrees'},'production_ids':['mk.r007.pappa.c','mk.r007.ashi_pool.c','mk.r007.pappa_qualifies','mk.r007.ashi_qualifies'],'finding':'Production preserves Rav Pappa’s majority requirement and Rav Ashi’s explicit even-without-majority alternative but links each only as a qualification of the general channel permission. It lacks a direct typed contrast between those two claims.','recommendation':'Add a supported contrast/objection relation under the admitted schema, or explicitly document why the two qualification edges fully encode this opposition in the intended argument view. Preserve both claims and their conditions.','not_a_claim_omission':True,'does_not_require_whole_snapshot_quarantine':True}]
comparison={'artifact_type':'post_freeze_exact_version_comparison','source_reading_sha256':sha(f.read_bytes()),'production_snapshot_path':str(p),'production_snapshot_sha256':sha(p.read_bytes()),'source_sha256':src['source_sha256'],'selected_probability_blocks':['block_000005','block_000008'],'probability_core_segments':20,'source_risk_segments':len(src['source_risk_cohort']['source_refs']),'risk_probability_overlap_segments':len(src['source_risk_cohort']['overlap_core_refs']),'independent_semantic_units':48,'probability_core_semantic_units':sum('probability_core' in r['cohorts'] for r in src['records']),'semantic_alignment':rows,'findings':findings,'confirmed_substantive_claim_omissions':0,'confirmed_forced_name_allocations':0,'uncertain_or_different_granularity_cases':['R09: first-person uncertainty speaker','R31: optional contextual mapping withheld from certain claims'],'integrity':{'relevant_production_records':len(relevant),'production_evidence_checks':checked,'evidence_failures':evidence_fail,'unmapped_evidence':missing,'source_freeze_unchanged':True,'production_unchanged':True,'coordinate_method':'Original source arrays; full-segment structure anchors; duplicate analogy and rabbinic answer fixed by local 3a:21–22 context'},'boundaries':{'independent_opportunities':3,'result':'Source boundaries retained or nested by production; Dimi report separates at3b:1; water-source unit begins4a:10; lifting unit contains4a:21 with continuation through4b:2. Coarser enclosing unit at4a:20 is compatible with independent local baraita transition.'},'verdict':'PROVISIONAL_CONTENT_AGREEMENT_WITH_MINOR_RELATION_GAP_AND_RETAINED_UNCERTAINTY','scope_limits':['No whole-tractate completeness claim.','Source-risk cohort and probability cores reported separately; overlaps not added twice.','All 48 extracted units fall within this produced snapshot; no unproduced scope counted as an omission.','No task eligibility or demanding evaluation qualification granted.','48 units are reviewer composite semantic units, not an atomic claim-count denominator.','Integrity checks on all r005/r007 evidence include adjacent4b:3–4, but those adjacent claims are not independently semantically certified.'],'interruption_record':{'parent_reported_interruption':True,'resume_instruction':'User explicitly says continue; resume exact-version comparison','state_at_resume':'Source freeze already complete; production snapshot already opened/read; no renewed blindness claim.','limitations_or_retries':'No repeated usage-limit retry performed; continuation succeeded.'}}
fn=out/'comparison_5fac8984.json'; assert not fn.exists();fn.write_text(json.dumps(comparison,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(out/'comparison_5fac8984.sha256').write_text(sha(fn.read_bytes())+'  '+fn.name+'\n',encoding='ascii')
print(json.dumps({'comparison_sha256':sha(fn.read_bytes()),'probability_units':comparison['probability_core_semantic_units'],'risk_segments':comparison['source_risk_segments'],'overlap':comparison['risk_probability_overlap_segments'],'evidence_checks':checked,'production_records':len(relevant),'findings':len(findings)}))

