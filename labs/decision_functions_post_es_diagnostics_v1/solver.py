"""Sole fixed Newton algorithm. No historical-data imports or query inputs."""
import numpy as np
from objective import value_grad_hess,independent
def solve(a,g,y,d):
    scale=np.sqrt(d);eta=np.zeros(len(d));trace=[];guarded=[]
    for step in range(101):
        value,grad,hess=value_grad_hess(eta/scale,a,g,y,d);ge=grad/scale;he=hess/scale[:,None]/scale[None,:];r=float(np.linalg.norm(ge))
        if not np.isfinite(value) or not np.isfinite(ge).all() or not np.isfinite(he).all():raise FloatingPointError('Nonfinite Newton evaluation')
        trace.append(dict(iteration=step,objective=value,R=r,theta=(eta/scale).tolist()))
        if r<=1e-10:return eta/scale,dict(success=True,reason='RESIDUAL_TARGET',R=r,steps=step,trace=trace,guarded=guarded)
        if step==100:break
        try:chol=np.linalg.cholesky(he);direction=np.linalg.solve(chol.T,np.linalg.solve(chol,-ge))
        except np.linalg.LinAlgError:return eta/scale,dict(success=False,reason='CHOLESKY_FAILURE',R=r,steps=step,trace=trace,guarded=guarded)
        slope=float(ge@direction)
        if not np.isfinite(direction).all() or not np.isfinite(slope):raise FloatingPointError('Nonfinite direction')
        if slope>=0:return eta/scale,dict(success=False,reason='NON_DESCENT',R=r,steps=step,trace=trace,guarded=guarded)
        allowance=64*2.**-52*max(1.,abs(value));accepted=False
        for j in range(40):
            alpha=2.**-j;candidate=eta+alpha*direction;nv,ng,_=value_grad_hess(candidate/scale,a,g,y,d)
            if not np.isfinite(nv) or not np.isfinite(ng).all():raise FloatingPointError('Nonfinite trial')
            if nv<=value+1e-4*alpha*slope:accepted=True;rule='ARMIJO'
            elif j==0 and -slope<=allowance:
                _,ig=independent(candidate/scale,a,g,y,d);nr=float(np.linalg.norm(ig/scale))
                if nr<r and nv<=value+allowance:
                    accepted=True;rule='ROUNDOFF_FULL_STEP';guarded.append(dict(J_old=value,J_new=nv,R_old=r,R_new=nr,predicted_decrease=-slope,allowance=allowance,acceptance_rule=rule))
            if accepted:eta=candidate;trace[-1].update(alpha=alpha,acceptance_rule=rule);break
        if not accepted:return eta/scale,dict(success=False,reason='BACKTRACKING_EXHAUSTED',R=r,steps=step,trace=trace,guarded=guarded)
    return eta/scale,dict(success=False,reason='MAXIMUM_STEPS',R=r,steps=100,trace=trace,guarded=guarded)
