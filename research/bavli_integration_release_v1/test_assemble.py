import json
from pathlib import Path
import tempfile
import unittest
import assemble as a

class AssemblyTests(unittest.TestCase):
    def record(self, ident, links=()):
        return dict(id=ident, links=list(links), content={}, release_state='valid')

    def test_exact_hash_and_transitive_exclusion(self):
        rows=[self.record('bad'),self.record('middle',['bad']),self.record('last',['middle']),self.record('safe')]
        entry=dict(job_id='j',record_id='bad',record_sha256=a.r.sha(a.r.encoded(rows[0])),reason='unsupported')
        self.assertEqual(set(a.exclusion_closure('j',rows,[entry])),{'bad','middle','last'})
        entry['record_sha256']='stale'
        self.assertEqual(a.exclusion_closure('j',rows,[entry]),{})

    def test_nonprefix_coverage(self):
        coords=[dict(id=str(i),ref=str(i),ordinal=i) for i in range(6)]
        self.assertEqual([(x['start_ref'],x['end_ref'],x['segments']) for x in a.gaps(coords,{'0','3'})],[('1','2',2),('4','5',2)])

    def test_keys_and_path_escape(self):
        self.assertNotEqual(a.key('a,b','c'),a.key('a','b,c'))
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):a.safe(Path(d),'../escape')

    def test_manifest_corruption_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);raw=b'{}\n';(p/'one.json').write_bytes(raw)
            manifest=dict(files=[dict(path='one.json',sha256=a.r.sha(raw),bytes=len(raw))])
            (p/'INPUT_MANIFEST.json').write_bytes(a.r.encoded(manifest))
            (p/'POLICY_MANIFEST.json').write_bytes(a.r.encoded(dict(input_manifest_sha256=a.r.sha((p/'INPUT_MANIFEST.json').read_bytes()),files=[])))
            a.verify_inputs(p)
            (p/'one.json').write_bytes(b'{"changed":true}\n')
            with self.assertRaises(ValueError):a.verify_inputs(p)

if __name__=='__main__':unittest.main()
