import json
from pathlib import Path
import tempfile
import unittest
import integrate_run as m

class ReviewGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.job={'job_id':'test','source_sha256':'source'};self.snap='snapshot'
        self.source={'s':{'ref':'T 2a:1','text':'abc'},'t':{'ref':'T 2a:2','text':'def'}}
        self.active=[{'id':'risk','layer':'claims','uncertainty':['ambiguous']}]
    def tearDown(self):self.tmp.cleanup()
    def write(self,path,obj):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(m.r.encoded(obj));return {'path':path,'sha256':m.r.sha(p.read_bytes())}
    def fixture(self,core=None,quote='abc',risks=None):
        plan=self.write('review_plans/test.json',{'review_blocks':[{'spans':[{'ref':'T 2a:1'},{'ref':'T 2a:2'}]}]})
        reading=self.write('review/initial.json',{'source_sha256':'source','frozen_before_comparison':True,'producer_labels_exposed':False,'execution':{'agent_id':'fresh-reader','route':'interactive_agent'},'core_refs':core or ['T 2a:1','T 2a:2'],'findings':[{'interpretation':'Source-first reading','evidence':[{'ref':'T 2a:1','start_char':0,'end_char':3,'quote':quote}]}]})
        comparison=self.write('review/comparison.json',{'snapshot_sha256':self.snap,'initial_reading_hashes':[reading['sha256']],'omission_pass_performed':True,'reviewed_risk_record_ids':['risk'] if risks is None else risks,'unresolved_integrity_critical_count':0})
        self.write('review/test/snapshot.json',{'snapshot_sha256':self.snap,'source_sha256':'source','plan_file_sha256':plan['sha256'],'review_kind':'independent_ai_source_first','initial_readings':[reading],'comparison':comparison,'verdict':'ACCEPT_PROVISIONAL_TRACTATE'})
    def assess(self):return m.assess_review(self.root,self.job,self.snap,self.active,self.source)
    def test_missing_receipt_fails(self):self.assertFalse(self.assess()[0])
    def test_missing_sample_core_fails(self):self.fixture(core=['T 2a:1']);self.assertFalse(self.assess()[0])
    def test_missing_risk_fails(self):self.fixture(risks=[]);self.assertFalse(self.assess()[0])
    def test_corrupt_quote_fails(self):
        self.fixture(quote='bad')
        with self.assertRaises(AssertionError):self.assess()
    def test_complete_bound_review_passes(self):self.fixture();self.assertTrue(self.assess()[0])
    def test_missing_ranges(self):
        rows=[{'id':str(i),'ref':str(i)} for i in range(5)]
        self.assertEqual(m.missing_ranges(rows,{'1','4'}),[{'start_ref':'0','end_ref':'0','source_segments':1},{'start_ref':'2','end_ref':'3','source_segments':2}])

if __name__=='__main__':unittest.main()
