"""Engineering controls only; generated choices are not human evidence.

Run: python research/individual_decision_model_2026-11-24/test_models.py
The printed JSON reports measured fitting CPU and held-out controls. Synthetic
train/test participants are disjoint. No-transfer target profiles are independently
generated; a generous tolerance checks catastrophic false transfer, not a formal
proof that estimated effects are exactly zero.
"""
import json
import time
import numpy as np
from models import (ProfileModel,PopulationModel,SummaryModel,CommonProbeRetrieval,
                    participant_scores,paired_bootstrap)


def synthetic(n,seed,transfer=True):
    rng=np.random.default_rng(seed)
    z=rng.choice([-1.,1.],n)
    z_target=z if transfer else rng.choice([-1.,1.],n)
    sx=np.zeros((n,8,2));sx[:,:,0]=1
    tx=np.zeros((n,16,2));tx[:,:,1]=1
    sy=rng.binomial(1,1/(1+np.exp(-3*z[:,None])),(n,8)).astype(float)
    ty=rng.binomial(1,1/(1+np.exp(-3*z_target[:,None])),(n,16)).astype(float)
    return sx,sy,tx,ty


def control(transfer):
    train=synthetic(240,111 if transfer else 222,transfer)
    sx,sy,tx,ty=synthetic(200,333 if transfer else 444,transfer)
    models={'population':PopulationModel(.01),'summary':SummaryModel(.1),
            'profile':ProfileModel(dim=2,reg=.1,epochs=100),
            'retrieval':CommonProbeRetrieval()}
    predictions={};cpu={};loss={}
    for name,model in models.items():
        model.fit(*train)
        cpu[name]=model.cpu_seconds
        predictions[name]=model.predict(sx,sy,tx)
        assert predictions[name].shape==ty.shape
        assert np.isfinite(predictions[name]).all()
        assert np.all((predictions[name]>0)&(predictions[name]<1))
        loss[name]=participant_scores(ty,predictions[name])['nll']
    profile=models['profile']
    # A real donor history intervention changes source observations, not IDs.
    donor=profile.predict(sx,np.roll(sy,1,axis=0),tx)
    donor_loss=participant_scores(ty,donor)['nll']
    personal=paired_bootstrap(loss['population'],loss['profile'])
    specific=paired_bootstrap(donor_loss,loss['profile'])
    if transfer:
        assert personal['estimate']>.08, personal
        assert specific['estimate']>.08, specific
    else:
        assert personal['estimate']<.08, personal
        assert specific['estimate']<.08, specific
    # Flipping available alternative order negates differences and relabels
    # observed source actions. Predicted probability for the new action 1 is 1-p.
    for name,model in models.items():
        flipped=model.predict(-sx,1-sy,-tx)
        assert np.allclose(flipped,1-predictions[name],atol=1e-7), name
    # Retrieval references also express alternatives in the flipped convention.
    retrieval=CommonProbeRetrieval().fit(-train[0],1-train[1],-train[2],1-train[3])
    assert np.allclose(retrieval.predict(-sx,1-sy,-tx),1-predictions['retrieval'],atol=1e-7)
    zero=profile.predict(sx[:,:0],sy[:,:0],tx)
    assert np.allclose(zero,profile.predict(sx[:,:0],sy[:,:0],tx))
    for model in models.values():
        assert np.allclose(model.predict(sx[:,:0],sy[:,:0],tx),predictions['population'])
    mean,cov=profile.infer(sx[0,:0],sy[0,:0])
    assert np.allclose(mean,0) and np.allclose(cov,np.eye(2))
    # Prediction API has no argument permitting hidden target labels.
    import inspect
    assert 'target_y' not in inspect.signature(profile.predict).parameters
    return {'synthetic_only':True,'transfer':transfer,'train_people':len(train[0]),
            'test_people':len(sx),'source_budget':8,'fit_process_cpu_seconds':cpu,
            'mean_nll':{k:float(v.mean()) for k,v in loss.items()},
            'delta_personal':personal,'delta_specific':specific,
            'profile_vs_summary':paired_bootstrap(loss['summary'],loss['profile'])}


if __name__=='__main__':
    started=time.process_time()
    results=[control(True),control(False)]
    print(json.dumps({'controls':results,'total_process_cpu_seconds':time.process_time()-started,
                      'invariants':'finite normalized binary probabilities, option-order invariance, zero-support prior, hidden-label-free prediction API'},indent=2))
