"""R1/R2 regressions with mocked I/O/CPU; no scientific generator or optimizer."""
import tempfile
import time
import unittest
from unittest.mock import patch,Mock
import run
from design import *

OUT=PACKAGE/'engineering_repair_2026-11-26'

class RepairChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'study';self.root.mkdir();self.auth=Path(self.tmp.name)/'auth.json'
        write(self.auth,{'mock':True})
        for target,value in [('verify_freeze',None),('watchdog',None)]:
            p=patch.object(run,target,return_value=value);p.start();self.addCleanup(p.stop)
        p=patch.object(run,'config',return_value=(dict(n=2,stages=[]),[],[],[]));p.start();self.addCleanup(p.stop)
        self.generator=Mock(side_effect=RuntimeError('injected failure after attempt'))
        p=patch.object(run,'fixture',self.generator);p.start();self.addCleanup(p.stop)
        self.proc=Mock();self.proc.cpu_times.return_value=(300.,200.);self.proc.memory_info.return_value.rss=4096
        p=patch.object(run.psutil,'Process',return_value=self.proc);p.start();self.addCleanup(p.stop)

    def blocked_next(self):
        before={p.relative_to(self.root).as_posix():digest(p) for p in self.root.rglob('*') if p.is_file()}
        self.generator.reset_mock()
        with self.assertRaises(ValueError):run.execute(self.root,'dev',1,self.auth)
        self.generator.assert_not_called()
        self.assertFalse((self.root/'attempts/dev001.json').exists())
        self.assertEqual(before,{p.relative_to(self.root).as_posix():digest(p) for p in self.root.rglob('*') if p.is_file()})

    def test_failed_attempt_records_cpu_blocks_direct_and_all(self):
        with self.assertRaisesRegex(RuntimeError,'injected'):run.execute(self.root,'dev',0,self.auth)
        self.assertEqual(read(self.root/'resources/dev000.json')['cpu_seconds'],500.)
        failure=read(self.root/'EXECUTION_FAILURE.json');self.assertEqual(failure['cpu_seconds_measured'],500.)
        self.assertEqual(failure['expenditure_status'],'PARTIALLY_MEASURED')
        self.assertFalse((self.root/'execution.lock').exists());self.blocked_next()
        write(self.root/'freeze.json',{'mock':True})
        with patch.object(run.sys,'argv',['run.py','all','--root',str(self.root),'--authorization',str(self.auth)]),patch.object(run.subprocess,'run') as child:
            with self.assertRaises(ValueError):run.main()
            child.assert_not_called()

    def test_failed_component_also_blocks(self):
        self.generator.side_effect=None;self.generator.return_value={'population':{}}
        with patch.object(run,'config',return_value=(dict(n=2,stages=[dict(id='dev000/population')]),[],[],[])),patch.object(run,'components',side_effect=ValueError('mock component failure')):
            with self.assertRaisesRegex(ValueError,'mock component'):run.execute(self.root,'dev',0,self.auth)
        self.blocked_next()

    def test_unknown_cpu_is_null_and_terminal(self):
        self.proc.cpu_times.side_effect=OSError('measurement unavailable')
        with self.assertRaises(RuntimeError):run.execute(self.root,'dev',0,self.auth)
        failure=read(self.root/'EXECUTION_FAILURE.json')
        self.assertIsNone(failure['cpu_seconds_measured']);self.assertEqual(failure['expenditure_status'],'UNRESOLVED')
        self.assertFalse((self.root/'resources/dev000.json').exists());self.blocked_next()

    def test_hard_interruption_stale_lock_removal_cannot_bypass(self):
        write(self.root/'attempts/dev000.json',dict(spec=bank('dev')[0],state='STARTED'))
        (self.root/'execution.lock').write_text('terminated process')
        (self.root/'execution.lock').unlink()  # simulate external stale-lock cleanup
        self.blocked_next()

    def test_terminal_marker_removal_does_not_make_failed_cpu_free(self):
        with self.assertRaises(RuntimeError):run.execute(self.root,'dev',0,self.auth)
        (self.root/'EXECUTION_FAILURE.json').unlink()
        self.blocked_next()  # partial resource receipt is not completion evidence

    def test_missing_resources_blocks_even_with_completion(self):
        spec=bank('dev')[0];write(self.root/'attempts/dev000.json',dict(spec=spec,state='STARTED'))
        write(self.root/'complete/dev000.json',dict(spec=spec,state='COMPLETE'))
        self.blocked_next()

    def test_repeat_verification_preserves_all_bytes_and_rejects_tampering(self):
        # Isolate verifier publication with complete mocked early-stop inventory.
        stop=dict(state='VERIFIED_DECLARED_EARLY_STOP',reason='DEV_NO_CANDIDATE',qualification=False,development_worlds=12,development_hash='',selection_hash='')
        write(self.root/'development_scores.json',[]);write(self.root/'selection.json',dict(state='DEV_NO_CANDIDATE'))
        stop.update(development_hash=digest(self.root/'development_scores.json'),selection_hash=digest(self.root/'selection.json'))
        write(self.root/'stop.json',stop)
        for spec in bank('dev'):
            for d in ['attempts','complete','resources']:write(self.root/d/(spec['id']+'.json'),{'mock':True})
            for r in REGIMES:(self.root/'worlds'/spec['id']/r).mkdir(parents=True)
        with patch.object(run,'verify_selection',return_value=dict(state='DEV_NO_CANDIDATE')):
            first=run.verify(self.root,self.auth)
            self.assertNotIn('verification.json',first['evidence_hashes'])
            before={p.relative_to(self.root).as_posix():digest(p) for p in self.root.rglob('*') if p.is_file()}
            for _ in range(2):
                with patch.object(run.sys,'argv',['run.py','verify','--root',str(self.root),'--authorization',str(self.auth)]):run.main()
            self.assertEqual(before,{p.relative_to(self.root).as_posix():digest(p) for p in self.root.rglob('*') if p.is_file()})
            receipt=self.root/'verification.json';original=receipt.read_bytes()
            bad=read(receipt);bad['qualification']=True;receipt.write_text(json.dumps(bad))
            with self.assertRaisesRegex(ValueError,'differs'):run.verify(self.root,self.auth)
            receipt.write_bytes(original)
            (self.root/'development_scores.json').write_text('[1]')
            with self.assertRaises(ValueError):run.verify(self.root,self.auth)

def main():
    import scipy.optimize
    start=time.process_time()
    with patch.object(scipy.optimize,'minimize',side_effect=AssertionError('Optimizer forbidden')):
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RepairChecks))
    dest=OUT/'REPAIR_REGRESSION_CHECKS.json'
    if dest.exists():dest=OUT/f'REPAIR_REGRESSION_CHECKS_{time.time_ns()}.json'
    write(dest,dict(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,failures=[str(x) for x in result.failures],errors=[str(x) for x in result.errors],source_hashes=run.pins(),scientific_fits=0,fresh_research_generator_calls=0,human_evaluations=0,python_cpu_seconds=time.process_time()-start,scope='Mocked exception/CPU and publication regressions; not a scientific execution'))
    if not result.wasSuccessful():raise SystemExit(1)

if __name__=='__main__':main()
