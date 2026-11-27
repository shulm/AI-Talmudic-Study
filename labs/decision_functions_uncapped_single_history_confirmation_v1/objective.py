"""Individual support-only objective, independent loop evaluator and analytic bounds."""
import numpy as np
from scipy.special import logsumexp,softmax
def design(z,v):
    eye=np.broadcast_to(np.eye(3),(len(z),3,3))
    return eye.copy() if v is None else np.concatenate([eye,np.einsum('crd,nd->ncr',v,z)],axis=2)
def penalty(dim):return np.array([.6]*3+[.06]*(dim-3))
def value_grad_hess(theta,a,g,y,d):
    logits=g+np.einsum('ncd,d->nc',a,theta);p=softmax(logits,axis=1);res=p-np.eye(3)[y]
    value=(logsumexp(logits,axis=1)-logits[np.arange(len(y)),y]).mean()+.5*np.dot(d*theta,theta)
    grad=np.einsum('nc,ncd->d',res,a)/len(y)+d*theta
    cov=np.eye(3)[None]*p[:,:,None]-p[:,:,None]*p[:,None,:]
    hess=np.einsum('nci,ncd,ndj->ij',a,cov,a)/len(y)+np.diag(d)
    return float(value),grad,hess
def independent(theta,a,g,y,d):
    value=0.;grad=np.zeros(len(theta))
    for ai,gi,yi in zip(a,g,y):
        logits=np.array([gi[c]+np.dot(ai[c],theta) for c in range(3)])
        top=max(logits);e=np.exp(logits-top);p=e/sum(e)
        value+=top+np.log(sum(e))-logits[yi]
        for c in range(3):grad+=(p[c]-int(c==yi))*ai[c]
    return float(value/len(y)+sum(d*theta**2)/2),grad/len(y)+d*theta
def probability(theta,a,g):
    l=g+np.stack([ai@theta for ai in a]);p=np.exp(l-l.max(1,keepdims=True));return p/p.sum(1,keepdims=True)
def error_bounds(theta,a,g,y,d,query_a):
    _,grad=independent(theta,a,g,y,d);_,other,_=value_grad_hess(theta,a,g,y,d)
    delta=float(abs(grad-other).max());allowance=1e-12*max(1.,float(abs(grad).max()),float(abs(other).max()))
    if delta>allowance:raise ValueError('Independent residual disagreement')
    # Fixed evaluation padding; analytic bound evaluated numerically, not interval-certified.
    r=float(np.linalg.norm(grad/np.sqrt(d)));padding=allowance*float(np.sqrt(np.sum(1/d)));upper=r+padding
    p=np.eye(3)-np.ones((3,3))/3;k=np.array([np.linalg.norm(p@aq/np.sqrt(d),2) for aq in query_a])
    return dict(gradient=grad,R=r,R_allowance=padding,R_used=upper,gradient_comparison=delta,theta_D_norm=float(np.linalg.norm(theta*np.sqrt(d))),K=k,probability_bound=.5*k*upper,log_probability_bound=np.sqrt(2)*k*upper)
