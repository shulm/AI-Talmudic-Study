"""Post-run provenance/summary audit, separate from immutable scientific code."""
from contracts import *
def main():
 start=time.process_time();base='47b19560350aa8c5d877d99f381d5b27f5b3490a';prefixes=['labs/decision_functions/','labs/decision_functions_diagnostics/','labs/decision_functions_diagnostics_v2/','research/decision_functions_2026-11-24/runs/pilot_v1/','research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/','research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/']
 old=subprocess.check_output(['git','ls-tree','-r',base,'--',*prefixes],text=True);now=subprocess.check_output(['git','ls-tree','-r','HEAD','--',*prefixes],text=True);assert old==now;assert not subprocess.check_output(['git','diff',base,'--',*prefixes]).strip()
 source=read(OUT/'prefit_sources.json')
 for path,h in source['files'].items():assert file_hash(ROOT/path)==h
 v=read(OUT/'verification.json');summary=read(OUT/'results_summary.json');assert v['state']=='VERIFIED_COMPLETE' and v['comparison_count']==expected_comparison_count() and v['maximum_discrepancy']<=1e-12
 assert summary['qualification']==qualification(v['state'],v['numerical_pass'],v['primary_gates']) and summary['status']=='COMPLETED_PRIMARY_FAILURE'
 recs=[read(p) for p in (OUT/'records').glob('*/*.complete.json')];assert len(recs)==196
 detail={}
 for real in REAL:
  curves=read(OUT/(real+'_curvature.json'))['rows'];groups={}
  for reg in REG:
   for pol in POLICIES:
    rows=[r for r in curves if r['k']==16 and r['policy']==pol and r['id'].startswith(reg+'_')];groups[reg+'_'+pol]=dict(rows=len(rows),data_min_eigenvalue_range=[min(r['data_min'] for r in rows),max(r['data_min'] for r in rows)],data_condition_median=float(np.median([r['data_condition'] for r in rows if r['data_condition'] is not None])),singular_count=sum(r['data_singular'] for r in rows),penalized_min_eigenvalue_range=[min(r['penalized_min'] for r in rows),max(r['penalized_min'] for r in rows)],penalized_condition_median=float(np.median([r['penalized_condition'] for r in rows])))
  nb=read(OUT/(real+'_batch.json'));models=read(OUT/(real+'_manifest.json'))['archives'][real+'_models.npz']['sha256'];detail[real]=dict(curvature_k16=groups,max_probability_batch_difference=max(r['max_probability_difference'] for r in nb['rows']),max_first_person_nll_batch_difference=max(r['first_person_expected_nll_difference'] for r in nb['rows']),model_archive_sha256=models)
 receipt=dict(status='PASS',historical_files_preserved=len(old.splitlines()),historical_git_tree_sha256=digest(old.encode()),all_prefit_scientific_sources_unchanged=True,no_new_fits_or_predictions=True,summary_qualification_conjunction_verified=True,realizations=detail,max_optimizer_gradient=max(r['gradient_max'] for r in recs),max_person_scaled_gradient=max(r['person_scaled_gradient_max'] for r in recs),postrun_audit_source_hash=file_hash(Path(__file__)),process_cpu_seconds=time.process_time()-start,resource_scope='Python audit process only; Git subprocesses and metadata overhead unprofiled')
 atomic(OUT/'delivery_audit.json',receipt);print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
