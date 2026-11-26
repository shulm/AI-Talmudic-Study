import sys, json, math, itertools
from pathlib import Path
import numpy as np

if len(sys.argv) != 3:
    raise SystemExit('Usage: check_math.py REPOSITORY_ROOT FRESH_OUTPUT_DIRECTORY')
ROOT = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(ROOT / 'labs/decision_functions_evidence_shrinkage_v1'))
import evidence

checks=[]
def check(key,a,b,tol=1e-10):
    d=abs(float(a)-float(b)); checks.append(dict(id=key,absolute_difference=d,passed=d<=tol,tolerance=tol))
def lse(vals):
    m=max(vals);return m+math.log(math.fsum(math.exp(x-m) for x in vals))

v=np.array([[[.27,-.38],[.15,.49]],[[-.41,.19],[.34,-.29]],[[.14,.19],[-.49,-.20]]])
u=np.array([[.7,-.2],[-.3,.9]])
bias=np.array([-.41,.16,.9])
count_groups=0; ordered_assignments=0
for k in (0,1,3,6):
    z=np.array([[math.cos(i+.13),math.sin(i+.13)] for i in range(k)]).reshape(k,2)
    g=np.array([[.12*math.cos(i+c*.71) for c in range(3)] for i in range(k)]).reshape(k,3)
    ys=np.array(list(itertools.product(range(3),repeat=k)),dtype=int).reshape(3**k,k)
    ordered_assignments+=len(ys)
    out=evidence.seed_evidence(z,g,ys,v,u)
    atoms=np.vstack((u,-u,np.zeros((1,2))))
    logits=np.array([[[float(g[i,c]+atom@v[c]@z[i]) for c in range(3)] for i in range(k)] for atom in atoms]).reshape(5,k,3)
    groups={tuple(n):[j for j,y in enumerate(ys) if tuple(np.bincount(y,minlength=3))==tuple(n)] for n in out['count_order']}
    count_groups+=len(groups)
    scores=np.array([[math.fsum(float(logits[a,i,c]) for i,c in enumerate(y)) for y in ys] for a in range(5)])
    for col,n in enumerate(out['count_order']):
        members=groups[tuple(n)]; normalizers=[lse([float(scores[a,j]) for j in members]) for a in range(5)]
        for a in range(5):check(f'k{k}/count{tuple(n)}/dp/a{a}',out['normalizers'][a,col],normalizers[a])
        q0=[math.exp(float(scores[-1,j])-normalizers[-1]) for j in members]
        check(f'k{k}/count{tuple(n)}/null_normalization',math.fsum(q0),1)
        check(f'k{k}/count{tuple(n)}/e_mean',math.fsum(p*math.exp(float(out['log_e'][j])) for p,j in zip(q0,members)),1)
        for a in (0,4):
            denom=math.fsum(lse([float(logits[a,i,c]+bias[c]) for c in range(3)]) for i in range(k))
            unconditional=[math.exp(float(scores[a,j])+sum(int(n[c])*bias[c] for c in range(3))-denom) for j in members]
            mass=math.fsum(unconditional)
            for j,p in zip(members,unconditional):check(f'k{k}/count{tuple(n)}/offset/a{a}/y{j}',p/mass,math.exp(float(scores[a,j])-normalizers[a]))
out=dict(status='PASS' if all(c['passed'] for c in checks) else 'FAIL',checks=len(checks),maximum_absolute_difference=max(c['absolute_difference'] for c in checks),feasible_count_groups=count_groups,ordered_assignments=ordered_assignments,scope='Deterministic non-scientific k=0,1,3,6 toy enumeration using actual evidence.py. No RNG draws, optimizer calls, scientific-fixture materialization or private-cache replay.',failures=[c for c in checks if not c['passed']])
(OUT / 'math_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['status'] == 'PASS' else 1)
