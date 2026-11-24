"""Bounded binary choice models. Inputs are alternative-1 minus alternative-0 features.

All shared fits use development people only. Prediction accepts revealed source
labels and target *features*, never target labels. Feature construction/scaling
must be frozen outside this module. No extra intercept is added: a canonical
alternative utility intercept, if wanted, must be an explicit difference feature.

Profile utility difference: x @ w + (x @ B) @ z, z ~ N(0,I).
Training minimizes target episode NLL after five differentiable damped Newton
source-MAP steps, averaged over fixed support budgets, plus reg*mean(B**2)/2.
w is a frozen ridge population fit. Prediction uses converged source MAP and
inverse posterior Hessian (Laplace), then deterministic 20-node Gauss-Hermite
integration of the univariate Gaussian logit. By frozen protocol, zero support
returns the population predictor for all comparators (a deliberate fallback,
not the integrated prior predictive). This is an approximate posterior,
not exact Bayesian inference. Shared B is nonconvex; seeds are explicit.
"""
from __future__ import annotations
import time
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, logsumexp


def _check(x, y=None):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim != 3 or not np.isfinite(x).all():
        raise ValueError('features must be finite [person, decision, feature]')
    if y is None:
        return x
    y = np.asarray(y, dtype=np.float64)
    if y.shape != x.shape[:2] or not np.isin(y, [0, 1]).all():
        raise ValueError('labels must be binary and align with features')
    return x, y


def _ridge(x, y, reg, offset=None):
    x = x.reshape(-1, x.shape[-1]); y = y.reshape(-1)
    offset = np.zeros(len(y)) if offset is None else np.asarray(offset).reshape(-1)
    def objective(w):
        a = x @ w + offset
        return (np.mean(np.logaddexp(0, a) - y*a) + reg*np.dot(w,w)/2,
                x.T @ (expit(a)-y)/len(y) + reg*w)
    fit = minimize(objective, np.zeros(x.shape[1]), jac=True, method='L-BFGS-B',
                   options={'maxiter': 300, 'ftol': 1e-11})
    if not fit.success:
        raise RuntimeError('population/summary optimization failed: '+fit.message)
    return fit.x


class PopulationModel:
    def __init__(self, reg=1.): self.reg = float(reg)
    def fit(self, source_x, source_y, target_x, target_y, **kwargs):
        start = time.process_time()
        sx, sy = _check(source_x, source_y); tx, ty = _check(target_x, target_y)
        self.w = _ridge(np.concatenate([sx,tx],1), np.concatenate([sy,ty],1), self.reg)
        self.cpu_seconds = time.process_time()-start
        return self
    def predict(self, source_x, source_y, target_x):
        _check(source_x, source_y)
        return expit(_check(target_x) @ self.w)


def _summary(x,y):
    # Signed utility-feature means preserve alternative-order invariance. A
    # canonical bias is represented by its task-specific difference feature.
    if x.shape[1] == 0: return np.zeros((len(x),x.shape[2]))
    signs = 2*y-1
    return (x*signs[:,:,None]).mean(1)


class SummaryModel:
    def __init__(self, reg=1., population_reg=0.01):
        self.reg = float(reg); self.population_reg=float(population_reg)
    @staticmethod
    def design(sx,sy,tx):
        h = _summary(sx,sy)
        return np.concatenate([tx, (tx[:,:,:,None]*h[:,None,None,:]).reshape(len(tx),tx.shape[1],-1)],2)
    def fit(self, source_x, source_y, target_x, target_y, budgets=(0,2,4,8)):
        start = time.process_time()
        sx,sy = _check(source_x,source_y); tx,ty = _check(target_x,target_y)
        self.population=PopulationModel(self.population_reg).fit(sx,sy,tx,ty)
        budgets = _budgets(budgets, sx.shape[1])
        xx = np.concatenate([self.design(sx[:,:b],sy[:,:b],tx) for b in budgets],1)
        self.w = _ridge(xx,np.tile(ty,(1,len(budgets))),self.reg)
        self.cpu_seconds = time.process_time()-start
        return self
    def predict(self, source_x, source_y, target_x):
        sx,sy = _check(source_x,source_y); tx = _check(target_x)
        if sx.shape[1]==0: return self.population.predict(sx,sy,tx)
        return expit(self.design(sx,sy,tx) @ self.w)


def _budgets(budgets, available):
    budgets = tuple(int(b) for b in budgets)
    if not budgets or any(b < 0 or b > available for b in budgets):
        raise ValueError('support budgets exceed available observed source decisions')
    return budgets


class ProfileModel:
    def __init__(self, dim=2, reg=1., seed=17, epochs=100, population_reg=0.01):
        self.dim=int(dim); self.reg=float(reg); self.seed=int(seed)
        self.epochs=int(epochs); self.population_reg=float(population_reg)
    def fit(self, source_x, source_y, target_x, target_y, budgets=(0,2,4,8)):
        import torch
        torch.set_num_threads(1)
        start = time.process_time()
        sx,sy = _check(source_x,source_y); tx,ty = _check(target_x,target_y)
        budgets = _budgets(budgets,sx.shape[1])
        pop = PopulationModel(self.population_reg).fit(sx,sy,tx,ty)
        self.w = pop.w.copy()
        dtype=torch.float64
        sx,sy,tx,ty,w = [torch.tensor(a,dtype=dtype) for a in (sx,sy,tx,ty,self.w)]
        generator=torch.Generator().manual_seed(self.seed)
        B=torch.nn.Parameter(torch.randn(sx.shape[2],self.dim,generator=generator,dtype=dtype)*0.15)
        optimizer=torch.optim.Adam([B],lr=0.04)
        identity=torch.eye(self.dim,dtype=dtype)[None]
        self.training_losses=[]
        for epoch in range(self.epochs):
            optimizer.zero_grad(); losses=[]
            for b in budgets:
                if b==0:
                    losses.append(torch.nn.functional.binary_cross_entropy_with_logits(tx@w,ty))
                    continue
                h=sx[:,:b] @ B
                z=torch.zeros(len(sx),self.dim,dtype=dtype)
                for _ in range(5):
                    p=torch.sigmoid(sx[:,:b]@w + torch.einsum('nsd,nd->ns',h,z))
                    grad=z+torch.einsum('nsd,ns->nd',h,p-sy[:,:b])
                    H=identity+torch.einsum('nsd,nse,ns->nde',h,h,p*(1-p))
                    step=torch.linalg.solve(H,grad[:,:,None]).squeeze(-1)
                    z=z-0.8*step
                # Training also marginalizes the same approximate Laplace uncertainty.
                p=torch.sigmoid(sx[:,:b]@w + torch.einsum('nsd,nd->ns',h,z))
                H=identity+torch.einsum('nsd,nse,ns->nde',h,h,p*(1-p))
                cov=torch.linalg.inv(H); ht=tx@B
                mu=tx@w+torch.einsum('ntd,nd->nt',ht,z)
                var=torch.einsum('ntd,nde,nte->nt',ht,cov,ht).clamp(min=1e-12)
                nodes,weights=np.polynomial.hermite.hermgauss(20)
                nodes=torch.tensor(nodes,dtype=dtype); weights=torch.tensor(weights/np.sqrt(np.pi),dtype=dtype)
                pred=(torch.sigmoid(mu[:,:,None]+torch.sqrt(2*var[:,:,None])*nodes)*weights).sum(-1)
                losses.append(torch.nn.functional.binary_cross_entropy(pred.clamp(1e-10,1-1e-10),ty))
            loss=torch.stack(losses).mean()+self.reg*B.square().mean()/2
            loss.backward(); torch.nn.utils.clip_grad_norm_([B],10.); optimizer.step()
            self.training_losses.append(float(loss.detach()))
        self.B=B.detach().numpy().copy()
        self.cpu_seconds=time.process_time()-start
        return self
    def infer(self, source_x, source_y):
        x,y=_check(np.asarray(source_x)[None],np.asarray(source_y)[None]); x=x[0];y=y[0]
        h=x@self.B; offset=x@self.w
        def objective(z):
            a=offset+h@z
            return np.sum(np.logaddexp(0,a)-y*a)+z@z/2, h.T@(expit(a)-y)+z
        fit=minimize(objective,np.zeros(self.dim),jac=True,method='BFGS',options={'gtol':1e-7})
        if not fit.success and np.linalg.norm(fit.jac)>1e-5:
            raise RuntimeError('profile MAP failed: '+fit.message)
        z=fit.x; p=expit(offset+h@z)
        covariance=np.linalg.inv(np.eye(self.dim)+h.T@(h*(p*(1-p))[:,None]))
        return z,covariance
    def predict_from_posterior(self,target_x,mean,cov):
        x=np.asarray(target_x,dtype=float); h=x@self.B
        mu=x@self.w+h@mean; var=np.maximum(np.einsum('...d,de,...e->...',h,cov,h),0)
        nodes,weights=np.polynomial.hermite.hermgauss(20)
        return np.sum(expit(mu[...,None]+np.sqrt(2*var[...,None])*nodes)*weights/np.sqrt(np.pi),axis=-1)
    def predict(self,source_x,source_y,target_x):
        sx,sy=_check(source_x,source_y);tx=_check(target_x)
        if sx.shape[1]==0: return expit(tx@self.w)
        return np.stack([self.predict_from_posterior(t,*self.infer(s,y)) for s,y,t in zip(sx,sy,tx)])


class CommonProbeRetrieval:
    """Scenario matching at 10 decimals; weights exp(-summed source log loss).

    Training people's matching source decisions define distance, their matching
    target decisions define prediction. Features must uniquely define scenarios.
    Uses Laplace-smoothed per-probe probabilities; unavailable probes fall back
    to population. No test target answers, person identifiers, or extra support.
    """
    def __init__(self, reg=0.01): self.reg=float(reg)
    def fit(self,source_x,source_y,target_x,target_y,**kwargs):
        start=time.process_time()
        self.sx,self.sy=_check(source_x,source_y);self.tx,self.ty=_check(target_x,target_y)
        self.population=PopulationModel(self.reg).fit(self.sx,self.sy,self.tx,self.ty)
        self.source_bank=self._bank(self.sx,self.sy)
        self.target_bank=self._bank(self.tx,self.ty)
        self.cpu_seconds=time.process_time()-start
        return self
    @staticmethod
    def _key(x): return tuple(np.round(x,10))
    def _lookup(self,bank,x):
        pair=bank.get(self._key(x))
        if pair is not None: return pair
        pair=bank.get(self._key(-x))
        return None if pair is None else (1-pair[0],pair[1])
    @classmethod
    def _bank(cls,x,y):
        bank={}
        for i in range(len(x)):
            for feature,answer in zip(x[i],y[i]):
                key=cls._key(feature)
                if key not in bank: bank[key]=[np.zeros(len(x)),np.zeros(len(x))]
                bank[key][0][i]+=answer;bank[key][1][i]+=1
        return {k:((a+1)/(c+2),c>0) for k,(a,c) in bank.items()}
    def predict(self,source_x,source_y,target_x):
        sx,sy=_check(source_x,source_y);tx=_check(target_x)
        output=self.population.predict(sx,sy,tx);used=0;total=output.size
        if sx.shape[1]==0:
            self.last_coverage={'retrieved':0,'total':total};return output
        for i,(source,answer,targets) in enumerate(zip(sx,sy,tx)):
            comparable=np.ones(len(self.sx),dtype=bool);log_weights=np.zeros(len(self.sx))
            for x,y in zip(source,answer):
                pair=self._lookup(self.source_bank,x)
                if pair is None: comparable[:]=False;break
                p,has_probe=pair;comparable &= has_probe
                log_weights+=y*np.log(p)+(1-y)*np.log1p(-p)
            if not comparable.any(): continue
            weights=np.exp(log_weights-log_weights[comparable].max())*comparable
            for k,x in enumerate(targets):
                pair=self._lookup(self.target_bank,x)
                if pair is None: continue
                probs,has_probe=pair;ww=weights*has_probe
                if ww.sum()>0:
                    output[i,k]=np.average(probs,weights=ww);used+=1
        self.last_coverage={'retrieved':used,'total':total}
        return output


def participant_scores(y,p):
    """One task family: trial means within each person. Caller averages families."""
    y=np.asarray(y);p=np.asarray(p)
    if y.shape!=p.shape or not np.isfinite(p).all() or np.any((p<0)|(p>1)):
        raise ValueError('invalid probabilities')
    p=np.clip(p,1e-12,1-1e-12)
    return {'nll':(-y*np.log(p)-(1-y)*np.log1p(-p)).mean(1),
            'brier':2*((p-y)**2).mean(1),'accuracy':((p>=.5)==y).mean(1)}


def paired_bootstrap(a,b,seed=20261124,draws=2000):
    """Participant-cluster percentile CI for loss(a)-loss(b)."""
    difference=np.asarray(a)-np.asarray(b)
    if difference.ndim!=1 or len(difference)<2: raise ValueError('need >=2 people')
    rng=np.random.default_rng(seed)
    means=difference[rng.integers(0,len(difference),(draws,len(difference)))].mean(1)
    return {'estimate':float(difference.mean()),'ci95':np.quantile(means,[.025,.975]).tolist(),
            'participants':len(difference),'draws':draws}
