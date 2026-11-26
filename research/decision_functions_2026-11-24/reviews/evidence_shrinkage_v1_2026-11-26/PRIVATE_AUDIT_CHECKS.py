"""Independent derivative, bound-identity, inventory, and receipt checks; no fits."""
import json, time
from pathlib import Path
import numpy as np
import PRIVATE_AUDIT as a

start=time.process_time(); checks={}
def require(name, condition):
    checks[name]=bool(condition)
    if not condition: raise AssertionError(name)

# Fixed arithmetic test points, not generated research people/worlds.
z=np.array([[1.,0.],[0.,1.],[-1.,.5]])
base=np.array([[.1,0.,-.1],[.2,-.1,.3],[0.,.2,-.2]])
y=np.array([[0,1,2],[2,0,1]])
v=np.arange(12,dtype=float).reshape(3,2,2)/13-.4
for name,basis in [('B3',None),('M1',v)]:
    cols=3 if basis is None else 5
    x=np.arange(2*cols,dtype=float)/17-.2
    obj,res,A=a.personal(x,z,base,y,basis,.06,.6)
    numeric=[]
    for j in range(len(x)):
        d=np.zeros_like(x);d[j]=1e-5
        numeric.append((a.personal(x+d,z,base,y,basis,.06,.6)[0]-a.personal(x-d,z,base,y,basis,.06,.6)[0])/2e-5)
    require(name+'/finite_difference_gradient',np.max(abs(np.array(numeric)-res.ravel()/2))<1e-9)
    own=a.personal(x.reshape(2,cols)[:1].ravel(),z,base,y[:1],basis,.06,.6)[1]
    require(name+'/person_residual_batch_independence',np.max(abs(own[0]-res[0]))<1e-14)
    # Logistic Hessian PSD plus positive diagonal penalties supplies mu.
    require(name+'/positive_penalty',min(.6,.06 if basis is not None else .6)>0)

directory=Path(__file__).parent/'private_audit_02'
data=a.read(directory/'analysis.json'); receipt=a.read(directory/'receipt.json'); inputs=a.read(directory/'inputs.json')
require('audit_pass',receipt['status']=='PASS' and len(receipt['checks'])==911)
require('64_personal_vectors',len(data['optimizer_diagnostics'])==64)
require('1664_personal_instances',sum(x['batch'] for x in data['optimizer_diagnostics'])==1664)
require('112_private_inputs',len(inputs['private_sha256'])==112)
require('153_active_caps',sum(x['cap_count'] for x in data['weights'] if x['stratum']=='active')==153)
require('zero_inactive_caps',sum(x['cap_count'] for x in data['weights'] if x['stratum']=='inactive')==0)
require('all_eight_ES_lower_bounds_fail',all(x['nrmse_lower']>.5 for x in data['per_history'] if x['stratum']=='active' and x['method']=='ES'))
for path,digest in receipt['outputs'].items(): require('output_hash/'+path,a.sha(directory/path)==digest)
require('script_binding',a.sha(Path(a.__file__))==inputs['script_sha256'])
for world in 'EFGH':
    scores=a.read(a.RUN/(world+'_scores.json'))
    for row in data['aggregates']:
        if row['world']!=world: continue
        saved=scores['gates'][row['method']]['values']
        for public,old in [('active_gain','gain'),('recovery','recovery'),('contrast_nrmse','contrast'),('inactive_degradation','inactive')]:
            require(world+'/'+row['method']+'/'+public,abs(row[public]-saved[old])<1e-12)
try:
    a.scipy.optimize.minimize(None,None)
except RuntimeError: require('optimizer_guard',True)
else: require('optimizer_guard',False)
try:
    a.fixture.generate()
except RuntimeError: require('generator_guard',True)
else: require('generator_guard',False)
try:
    a.main(Path('nonexistent'),directory)
except FileExistsError: require('receipt_collision_rejected',True)
else: require('receipt_collision_rejected',False)
print(json.dumps(dict(status='PASS',checks=checks,cpu_seconds=time.process_time()-start,optimization=0,world_generation=0,script_sha256=a.sha(Path(__file__))),indent=2))
