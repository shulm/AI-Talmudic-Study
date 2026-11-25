"""Scalar scoring after immutable predictions; loss-level history aggregation."""
from contracts import *
from fixture import contrast

def cell_loss(p,oracle):return -(oracle*np.log(np.maximum(p,1e-12))).sum(-1)
def measures(p,y,oracle):
 return dict(expected_nll=float(cell_loss(p,oracle).mean()),nll=float(-np.log(np.maximum(np.take_along_axis(p,y[...,None],-1)[...,0],1e-12)).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))
def row_score(c,arrays,evaluator):
 r,pol,k,h,info=c;key=ident(c);oracle=evaluator[r+'_oracle'];y=evaluator[r+'_y'];truth=contrast(oracle);pred=contrast(arrays[key+'_M1']);den=float(np.mean(truth**2));mse=float(np.mean((pred-truth)**2));rms=float(np.mean(pred**2))
 metrics={m:measures(arrays[key+'_'+m],y,oracle) for m in MODELS};eo=float(cell_loss(oracle,oracle).mean());gain=metrics['B3']['expected_nll']-metrics['M1']['expected_nll'];gap=metrics['B3']['expected_nll']-eo
 result=dict(id=key,regime=r,policy=pol,k=k,schedule=h,condition=info,metrics=metrics,oracle_expected_nll=eo,expected_gain=gain,oracle_gap=gap,oracle_gap_recovery=gain/gap if gap>0 else None,contrast_mse=mse,contrast_denominator=den,contrast_nrmse=float(np.sqrt(mse/den)) if den>1e-20 else None,null_contrast_rms=float(np.sqrt(rms)),contrast_square_mean=rms)
 if info=='informative':
  result['donor']={m:{metric:float(value-metrics[m][metric]) for metric,value in measures(arrays[key+'_'+m+'_donor'],y,oracle).items()} for m in MODELS}
  if k>0:result['seeds']={str(s):measures(arrays[key+f'_M1_{s}'],y,oracle) for s in SEEDS}
 return result
def aggregate(rows,regime,policy,k,info='informative'):
 rr=[r for r in rows if r['regime']==regime and r['policy']==policy and r['k']==k and r['condition']==info]
 if len(rr)!=(1 if k in [0,96] else 2):raise ValueError('Missing history rows')
 mean=lambda field:float(np.mean([r[field] for r in rr]));den=mean('contrast_denominator');gap=mean('oracle_gap');gain=mean('expected_gain')
 return dict(regime=regime,policy=policy,k=k,condition=info,history_rows=[r['id'] for r in rr],history_aggregation='mean losses/squared contrasts; not probability pooling',expected_gain=gain,oracle_gap_recovery=gain/gap if gap>0 else None,contrast_nrmse=float(np.sqrt(mean('contrast_mse')/den)) if den>1e-20 else None,null_contrast_rms=float(np.sqrt(mean('contrast_square_mean'))),metrics={m:{key:float(np.mean([r['metrics'][m][key] for r in rr])) for key in rr[0]['metrics'][m]} for m in MODELS},donor={m:{key:float(np.mean([r['donor'][m][key] for r in rr])) for key in rr[0]['donor'][m]} for m in MODELS} if info=='informative' else None)
def gates(positive,null):
 values=dict(gain=positive['expected_gain'],recovery=positive['oracle_gap_recovery'],contrast=positive['contrast_nrmse'],null=-null['expected_gain'])
 margins=dict(gain=values['gain']-.05,recovery=None if values['recovery'] is None else values['recovery']-.5,contrast=None if values['contrast'] is None else .5-values['contrast'],null=.01-values['null'])
 passed={k:bool(v is not None and np.isfinite(v) and v>=0) for k,v in margins.items()}
 return dict(values=values,margins=margins,passed=passed)
def score(arrays,evaluator):
 rows=[row_score(c,arrays,evaluator) for c in conditions()];aggregates=[]
 for r in REG:
  for pol,config in POLICIES.items():
   for k in config['budgets']:aggregates.append(aggregate(rows,r,pol,k))
  aggregates.extend([aggregate(rows,r,'primary',0),aggregate(rows,r,'primary',16,'uninformative')])
 tables={}
 for pol in POLICIES:
  pair=[next(x for x in aggregates if x['regime']==r and x['policy']==pol and x['k']==16 and x['condition']=='informative') for r in REG]
  table=gates(*pair);per={}
  for h in SCHEDULES:per[str(h)]=gates(*[next(x for x in rows if x['regime']==r and x['policy']==pol and x['k']==16 and x['schedule']==str(h) and x['condition']=='informative') for r in REG])
  table['schedules']=per;table['worst_schedule_margins']={k:min(v['margins'][k] for v in per.values()) for k in table['margins']};tables[pol]=table
 return dict(rows=rows,aggregates=aggregates,gates=tables)
def boot_inputs(arrays,evaluator):
 out={}
 for metric,r in [('positive_gain','positive'),('null_degradation','null'),('positive_donor','positive')]:
  vals=[]
  for h in SCHEDULES:
   key=ident((r,'primary',16,str(h),'informative'));o=evaluator[r+'_oracle'];pm=arrays[key+'_M1'];pb=arrays[key+'_B3'];pd=arrays[key+'_M1_donor']
   vals.append(cell_loss(pb,o)-cell_loss(pm,o) if metric=='positive_gain' else (cell_loss(pm,o)-cell_loss(pb,o) if metric=='null_degradation' else cell_loss(pd,o)-cell_loss(pm,o)))
  out[metric]=np.mean(vals,axis=0)
 return out
def bootstrap(arrays,evaluator):
 rng=np.random.Generator(np.random.PCG64(1701));pp=rng.integers(0,12,(2000,12));qq=rng.integers(0,12,(2000,12));out=dict(person_pairs=pp,query_groups=qq);summaries={}
 for key,cells in boot_inputs(arrays,evaluator).items():
  block=cells.reshape(12,2,12,3);values=np.array([block[pairs,:,groups[:,None],:].mean() for pairs,groups in zip(pp,qq)])
  # Advanced indexing above gives independent cross-product of sampled pair/group IDs.
  out[key]=values;summaries[key]=dict(point=float(cells.mean()),interval95=np.quantile(values,[.025,.975],method='linear').tolist(),replicates=2000)
 return out,summaries
