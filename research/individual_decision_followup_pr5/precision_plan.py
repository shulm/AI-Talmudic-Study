"""Development-only conditional planning simulation; never confirmation evidence."""
import time
import numpy as np
import diagnostics as d

def main():
    t=time.process_time();old=d.verify_original()
    if (d.ROOT/'precision_results.json').exists():raise RuntimeError('Planning simulation already saved')
    va=d.load(old,'validation');y=d.labels(old,va,'validation')
    p=dict(np.load(d.LOCAL/'development_probabilities.npz'))
    own=d.nll(y,p['own_8'])
    pair=np.column_stack([d.nll(y,p['item_frequency_8'])-own,
        np.mean([d.nll(y,q) for q in p['donor_single_8']],0)-own])
    residual=pair-pair.mean(0)
    # Each outer sample resamples people; multinomial weights are exactly the
    # inner participant bootstrap of that outer sample, retaining paired axes.
    rng=np.random.default_rng(20261125);results=[]
    for n in [100,250,500,1000,2000]:
        lower=[];width=[]
        for rep in range(200):
            counts=rng.multinomial(n,np.full(102,1/102))
            boots=rng.multinomial(n,counts/n,size=2000)@residual/n
            bounds=np.quantile(boots,[.025,.975],axis=0)
            lower.append(bounds[0]);width.append((bounds[1]-bounds[0])/2)
        lower=np.array(lower)
        for effect in [0,.01,.02]:
            success=np.all(lower+effect>0,axis=1);power=float(success.mean())
            results.append(dict(n=n,equal_true_advantage=effect,joint_success_rate=power,
                monte_carlo_se=float(np.sqrt(power*(1-power)/200)),
                mean_half_width=np.mean(width,axis=0).tolist()))
    d.dump(d.ROOT/'precision_results.json',dict(status='planning only; synthetic resampling of development residuals',
        development_people=102,contrasts=['value_item_frequency','identity_single_donor'],
        development_means=pair.mean(0).tolist(),development_sd=pair.std(0,ddof=1).tolist(),
        correlation=np.corrcoef(pair.T).tolist(),outer_draws=200,inner_draws=2000,seed=20261125,
        rule='both two-sided95% percentile lower endpoints exceed0',results=results,
        limitations='conditional fixed-model/bank residual approximation; original fixed positions and selected model do not establish new-cohort variance; no human evidence generated'))
    d.event('development_precision_simulation',time.process_time()-t,shared_fits=0,new_human_observations=0)
    print('Development-only joint precision simulation complete.')
if __name__=='__main__':main()
