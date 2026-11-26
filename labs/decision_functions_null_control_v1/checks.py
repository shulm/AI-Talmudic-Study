"""Analytic/mocked tests only. Neither fixture() nor a scientific optimizer runs."""
import copy
import tempfile
import time
import unittest
from unittest.mock import patch
from design import *
from engine import schedule, score_arrays, validate_probs

class Checks(unittest.TestCase):
    def test_candidates(self):
        self.assertEqual(len(CANDIDATES),20)
        self.assertEqual(len({c['id'] for c in CANDIDATES}),20)
        self.assertEqual(len({c['lb'] for c in CANDIDATES if c['w']==0}),2)
    def test_counts(self):
        e=expected('dev',DEV_N)
        self.assertEqual((e['shared_fits'],e['adaptation_batches'],e['person_solves'],e['optimizer_records'],e['archives']),(216,2016,48384,2232,72))
        for c in CANDIDATES:
            for lb in [.1,.6]:
                e=expected('confirmation',MAX_N,c,lb)
                self.assertEqual(e['shared_fits'],1728)
                self.assertEqual(e['adaptation_batches'],4608 if c['lb']==lb else 5760)
    def test_seed_banks(self):
        seeds=[s[k] for phase in ['dev','confirmation'] for s in bank(phase) for k in ['generator_seed','label_seed']]
        self.assertEqual(len(seeds),len(set(seeds)))
        self.assertFalse(set(seeds)&{20261126,20261127,20261128,20261129,2719,2720,2721,2722})
    def test_schedule(self):
        angles=np.tile(np.arange(3)*2*np.pi/3,32); z=np.column_stack([np.cos(angles),np.sin(angles)])
        for h in SCHEDULES:
            ix=schedule('analytic',h,np.arange(96))
            self.assertEqual(len(set(ix)),16)
            np.testing.assert_allclose(np.linalg.eigvalsh(z[ix].T@z[ix]/16),[.46875,.53125],atol=1e-12)
    def test_blend_probability_not_logits(self):
        q=np.broadcast_to([.2,.3,.5],(24,36,3)).copy(); b=np.broadcast_to([.7,.2,.1],q.shape).copy()
        a=dict(oracle=q,query_y=np.zeros((24,36),dtype=int),B2=b)
        for h in SCHEDULES:
            a[f'h{h}_B1']=b
            for lb in [.1,.6]:a[f'h{h}_B3_{lb}']=b
            for p in PAIRS:
                for s in SEEDS:a[f'h{h}_{p["id"]}_{s}']=q
        r=score_arrays(a,CANDIDATES,[.1,.6]);c=CANDIDATES[2]
        self.assertAlmostEqual(r[c['id']]['loss'],float(-(q*np.log((q+b)/2)).sum(-1).mean()))
        self.assertEqual(r['p0_w0']['loss'],r['p2_w0']['loss'])
    def test_invalid_inputs(self):
        for x in [[],[1],[1,1],[1,float('nan')]]:
            with self.assertRaises(ValueError):bounds(x)
        for p in [np.zeros((24,36,3)),np.full((24,36,3),np.nan)]:
            with self.assertRaises(ValueError):validate_probs(p)
        with self.assertRaises(ValueError):select([])
        with self.assertRaises(ValueError):confirm([],dict(state='INVALID'))
    @staticmethod
    def scores(n, harmful=False):
        out=[]
        for i in range(n):
            world={}; jitter=(i-(n-1)/2)*.0001
            for r in REGIMES:
                row=dict(oracle_loss=.3,contrast_den=10.)
                for lb in [.1,.6]:row[f'B3_{lb}']=dict(loss=1.+(.002 if lb==.1 else 0))
                for c in CANDIDATES:
                    delta=(.02 if harmful else .001)+jitter if r in NULLS else -.4+jitter
                    row[c['id']]=dict(loss=1.+delta,contrast_mse=.1)
                world[r]=row
            out.append(world)
        return out
    def test_selection_and_confirmation(self):
        scores=self.scores(DEV_N);s=select(scores)
        self.assertEqual(s['state'],'SELECTED');self.assertEqual(s['selected']['w'],.25)
        self.assertEqual(s['common_lb'],.6);self.assertEqual(s['confirmation_n'],MIN_N)
        result=confirm(self.scores(MIN_N),s)
        self.assertTrue(result['qualification'])
        self.assertFalse(confirm(self.scores(MIN_N,True),s)['qualification'])
        with self.assertRaises(ValueError):confirm(self.scores(MIN_N-1),s)
        for row in scores:
            row['strong']['oracle_loss']=1
        self.assertEqual(select(scores)['state'],'DEV_NO_CANDIDATE')
    def test_precision_cap(self):
        self.assertIsNone(count_from_dev([np.arange(DEV_N)]))
        s=select(self.scores(DEV_N));x=self.scores(MIN_N)
        for i,row in enumerate(x):row['population'][s['selected']['id']]['loss']+=i*.02
        self.assertEqual(confirm(x,s)['state'],'COMPLETE_INSUFFICIENT_PRECISION')
    def test_empty_missing_records(self):
        import sys
        sys.path.insert(0,str(ROOT/'labs/decision_functions_short_history_v1'))
        from core import validate_records
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ValueError):validate_records(Path(td),{})
            with self.assertRaises(ValueError):validate_records(Path(td),{'a':dict(person_solves=24)})
    def test_no_authorization(self):
        from run import authorize
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/'auth.json';write(f,dict(owner_authorized_execution=False))
            with self.assertRaises(ValueError):authorize(f)
    def test_objective_gradient_without_fit(self):
        import sys
        sys.path.insert(0,str(ROOT/'labs/decision_functions_short_history_v1'))
        from head import personal_objective
        z=np.array([[1.,0.],[0.,1.],[-1.,0.]])
        y=np.array([[0,1,2],[2,1,0]]);base=np.zeros((3,3));v=np.arange(12).reshape(3,2,2)/30
        fun,shape=personal_objective(z,y,base,.06,.6,v);x=np.arange(10)/30
        val,g=fun(x);num=[]
        for j in range(len(x)):
            d=np.eye(len(x))[j]*1e-6;num.append((fun(x+d)[0]-fun(x-d)[0])/2e-6)
        np.testing.assert_allclose(g,num,atol=1e-8,rtol=0)

def main():
    import scipy.optimize
    start=time.process_time()
    with patch.object(scipy.optimize,'minimize',side_effect=AssertionError('Optimizer forbidden in planning')),patch('engine.fixture',side_effect=AssertionError('Fresh generator forbidden in planning')):
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    receipt=dict(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,failures=[str(x) for x in result.failures],errors=[str(x) for x in result.errors],scientific_fits=0,human_evaluations=0,fresh_generator_calls=0,python_cpu_seconds=time.process_time()-start,source_hashes={p.name:digest(p) for p in Path(__file__).parent.glob('*.py')},limitations='Analytic tests do not validate predictive performance or full future execution. End-to-end mocked stage tests are separate.')
    path=PACKAGE/'ZERO_FIT_CHECKS.json'
    if path.exists():path=PACKAGE/f'ZERO_FIT_CHECKS_{time.time_ns()}.json'
    write(path,receipt)
    if not result.wasSuccessful():raise SystemExit(1)

if __name__=='__main__':main()
