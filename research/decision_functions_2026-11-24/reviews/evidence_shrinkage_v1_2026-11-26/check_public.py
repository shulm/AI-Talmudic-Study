import json, math, statistics, sys
from pathlib import Path
from collections import Counter

if len(sys.argv) != 3:
    raise SystemExit('Usage: check_public.py REPOSITORY_ROOT FRESH_OUTPUT_DIRECTORY')
ROOT = Path(sys.argv[1]).resolve() / 'research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1'
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=False)
checks = []; failures = []

def check(key, actual, expected, tol=1e-12, relative=0):
    delta = abs(float(actual)-float(expected))
    passed = delta <= tol + relative*abs(float(expected))
    row = dict(id=key, actual=actual, expected=expected, absolute_difference=delta, tolerance=tol, relative_tolerance=relative, passed=passed)
    checks.append(row)
    if not passed: failures.append(row)

def mean(x): return math.fsum(x)/len(x)

def quantile(x, p):
    y=sorted(x); loc=(len(y)-1)*p; lo=math.floor(loc); hi=math.ceil(loc)
    return y[lo]+(loc-lo)*(y[hi]-y[lo])

def stats(x):
    return dict(min=min(x), median=quantile(x,.5), mean=mean(x), max=max(x), q10=quantile(x,.1), q90=quantile(x,.9))

totals=Counter(); results={}
for real in 'EFGH':
    s=json.loads((ROOT/f'{real}_scores.json').read_text()); e=json.loads((ROOT/f'{real}_evidence.json').read_text())
    rows={x['id']:x for x in s['rows']}; totals['score_rows']+=len(rows); totals['score_aggregates']+=len(s['aggregates']); totals['evidence_rows']+=len(e['rows'])
    for key,row in rows.items():
        tag=f'{real}/row/{key}'; base=rows[f"{row['history']}_{row['stratum']}_B3"]
        check(tag+'/gain_from_nll',row['gain'],base['metrics']['expected_nll']-row['metrics']['expected_nll'])
        check(tag+'/gap_from_nll',row['gap'],base['metrics']['expected_nll']-row['oracle_loss'])
        check(tag+'/gain_from_people',row['gain'],-mean(row['per_person_excess']))
        check(tag+'/positive_part',row['positive_part_excess'],mean([max(x,0) for x in row['per_person_excess']]))
    for ag in s['aggregates']:
        rr=[rows[f'{h}_{ag["id"]}'] for h in (101,211)]; tag=f'{real}/aggregate/{ag["id"]}'
        for k,v in ag['metrics'].items(): check(tag+'/'+k,v,mean([r['metrics'][k] for r in rr]))
        check(tag+'/contrast_rms',ag['inactive_contrast_rms'],math.sqrt(mean([r['contrast_square'] for r in rr])))
        xs=[(a+b)/2 for a,b in zip(rr[0]['per_person_excess'],rr[1]['per_person_excess'])]
        for i,(v,w) in enumerate(zip(ag['per_person_excess'],xs)):check(tag+f'/person/{i}',v,w)
        check(tag+'/positive_part',ag['positive_part_excess'],mean([max(x,0) for x in xs]))
        for k,v in ag.get('donor',{}).items():check(tag+'/donor/'+k,v,mean([r['donor'][k] for r in rr]))
    for method,g in s['gates'].items():
        for h in ('aggregate','101','211'):
            rr=[r for r in s['rows'] if r['method']==method and (h=='aggregate' or str(r['history'])==h)]
            aa=[r for r in rr if r['stratum']=='active']; nn=[r for r in rr if r['stratum']=='inactive']; gg=g if h=='aggregate' else g['histories'][h]
            gain=mean([r['gain'] for r in aa]); gap=mean([r['gap'] for r in aa]); denom=mean([r['contrast_den'] for r in aa])
            values=dict(gain=gain,recovery=gain/gap,contrast=math.sqrt(mean([r['contrast_mse'] for r in aa])/denom),inactive=-mean([r['gain'] for r in nn]))
            margins=dict(gain=values['gain']-.05,recovery=values['recovery']-.5,contrast=.5-values['contrast'],inactive=.01-values['inactive'])
            for k,v in values.items():
                tag=f'{real}/gate/{method}/{h}/{k}'
                check(tag+'/value',gg['values'][k],v);check(tag+'/margin',gg['margins'][k],margins[k]);check(tag+'/passed',gg['passed'][k],margins[k]>=0,tol=0)
        for k,v in g['worst_history_margins'].items():check(f'{real}/gate/{method}/worst/{k}',v,min(g['histories'][str(h)]['margins'][k] for h in (101,211)))
    er={r['id']:r for r in e['rows']}
    for key,row in er.items():
        logs=list(row['seed_log_e'].values()); top=max(logs); le=top+math.log(math.fsum(math.exp(x-top) for x in logs)/len(logs))
        ev=math.exp(le); h=min(.009*max(ev-1,0),math.log(10)); w=-math.expm1(-h)
        for k,v in [('log_e',le),('evidence',ev),('h',h),('w',w)]:check(f'{real}/evidence/{key}/{k}',row[k],v,tol=1e-12,relative=1e-14 if k=='evidence' else 0)
        check(f'{real}/evidence/{key}/count',sum(row['counts']),16,tol=0)
    for key,ss in e['summaries'].items():
        hist,act=key.split('_'); rr=[r for r in e['rows'] if str(r['history'])==hist and r['active']==(act=='active')]
        check(f'{real}/evidence_summary/{key}/people',len(rr),24,tol=0)
        for name,col in [('evidence','evidence'),('weight','w')]:
            for k,v in stats([r[col] for r in rr]).items():check(f'{real}/evidence_summary/{key}/{name}/{k}',ss[name][k],v,tol=1e-12,relative=1e-14 if name=='evidence' else 0)
        check(f'{real}/evidence_summary/{key}/zero',ss['fraction_zero'],mean([int(r['w']==0) for r in rr]))
        check(f'{real}/evidence_summary/{key}/cap',ss['fraction_cap'],mean([int(r['h']==math.log(10)) for r in rr]))
    for act,dd in e['history_disagreement'].items():
        rr=sorted([r for r in e['rows'] if r['history']==101 and r['active']==(act=='active')],key=lambda r:r['person'])
        diffs=[r['w']-er[f'211_{r["person"]}']['w'] for r in rr]
        for i,(a,b) in enumerate(zip(dd['all_weight_differences'],diffs)):check(f'{real}/disagreement/{act}/{i}',a,b)
        for k,v in stats([abs(x) for x in diffs]).items():check(f'{real}/disagreement/{act}/{k}',dd['absolute_weight_difference'][k],v)
        zero=mean([int((r['w']==0)!=(er[f'211_{r["person"]}']['w']==0)) for r in rr])
        check(f'{real}/disagreement/{act}/zero',dd['zero_disagreement'],zero)
    boot=json.loads((ROOT/f'{real}_bootstrap.json').read_text())
    gates=s['gates']; agg={x['id']:x for x in s['aggregates']}
    expected=dict(active_gain=gates['ES']['values']['gain'],inactive_degradation=gates['ES']['values']['inactive'],active_donor=agg['active_ES']['donor']['expected_nll'],active_ES_fixed=agg['active_ES']['metrics']['expected_nll']-agg['active_FIXED_MIX']['metrics']['expected_nll'],inactive_ES_fixed=agg['inactive_ES']['metrics']['expected_nll']-agg['inactive_FIXED_MIX']['metrics']['expected_nll'])
    for k,v in expected.items():check(f'{real}/bootstrap/{k}/point',boot[k]['point'],v)
    results[real]={m:gates[m]['values'] for m in ('M1','FIXED_MIX','ES')}
out=dict(status='PASS' if not failures else 'FAIL',checks=len(checks),failed=len(failures),maximum_absolute_difference=max(x['absolute_difference'] for x in checks),maximum_non_evidence_absolute_difference=max(x['absolute_difference'] for x in checks if '/evidence' not in x['id']),totals=dict(totals),boundaries='Public scalar arithmetic and reported evidence summaries only; no private probability/parameter/DP cache replay and no scientific optimization.',failures=failures,results=results)
(OUT/'public_science_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
(OUT/'public_science_comparisons.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['status'] == 'PASS' else 1)
