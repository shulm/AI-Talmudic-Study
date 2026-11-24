"""Read-only integrity verification; no labels, inference or rescore."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--public-only',action='store_true');a=ap.parse_args()
    count=0
    for file,key in [('diagnostic_spec_manifest.json','files'),('diagnostic_review_signoff.json','reviewed_files'),('diagnostic_lock.json','files'),('delivery_manifest.json','files')]:
        for f,h in read(R/file)[key].items():assert sha(R/f)==h,(file,f);count+=1
    assert read(R/'exploratory_score_attempt.json')==dict(status='completed',attempt=1,new_confirmation=False)
    result=read(R/'exploratory_results.json');assert result['people']==102 and result['target_choices']==1020 and result['target_families']==1
    assert result['original_verdict_preserved']=='inconclusive' and result['exploratory_pass_count']==1
    assert result['contrasts']['mixture_8']['estimate']==-0.007573037030300332
    assert result['contrasts']['legacy_population_minus_own_8']['estimate']==0.11127584316082857
    assert result['selected_source_blind']=='item_frequency'
    assert result['contrasts']['value_8']['ci95'][1]<0
    assert result['contrasts']['identity_8']['ci95'][0]<0<result['contrasts']['identity_8']['ci95'][1]
    for b in [0,2,4,8]:
        c=result['contrasts'];assert abs(c[f'identity_{b}']['estimate']-c[f'mixture_{b}']['estimate']-c[f'jensen_gap_{b}']['estimate'])<1e-12
    if not a.public_only:
        import diagnostics as d
        old=d.verify_original();d.check_lock()
        for f,h in read(R/'probability_manifest.json')['files'].items():assert sha(R/'local_data'/f)==h
        assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=old,text=True).strip()==d.DELIVERY
    changed=subprocess.check_output(['git','diff','--name-only','6ca2dedc547144d7279696bd5322c1e39c7f03d3'],cwd=R,text=True).splitlines()
    assert all(p.startswith('research/individual_decision_followup_pr5/') for p in changed)
    print(json.dumps(dict(passed=True,hash_checks=count,original_local_hashes_checked=not a.public_only,outcomes_loaded=False,scoring_runs=0)))
if __name__=='__main__':main()
