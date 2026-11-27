import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import runner as r

class ProductionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.job=Path(self.tmp.name)/'job'; self.job.mkdir()
        self.meta=dict(tractate='Test',source_sha256='source',**r.hashes())
        self.segments={'s':dict(id='s',ref='Test 2a:1',text='אב😀ג'),'t':dict(id='t',ref='Test 2a:2',text='הו')}
        self.p=dict(schema_version=r.VERSION,owner='one',epoch=1,**self.meta,execution=dict(route='interactive_agent',agent_id='test-fixture',model_id=None),records=[dict(id='struct',layer='structure',evidence=[dict(segment_id='s',start_char=0,end_char=4,quote='אב😀ג')],content=dict(title='test',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference',uncertainty=[],links=[])],coverage=[dict(segment_id='s',layer='structure',extraction_state='completed',extraction_result='records_found',record_ids=['struct'],rationale='Synthetic test, not actual annotation')],open_tails=['struct'])
        r.atomic(self.job/'OWNER.json',dict(owner='one',epoch=1))
        self.file=self.job/'input.json'; self.save()
        self.mock=patch.object(r,'load',return_value=(self.meta,self.segments)); self.mock.start(); self.addCleanup(self.mock.stop)
    def save(self): self.file.write_bytes(r.encoded(self.p))
    def test_restart_replay_and_idempotence(self):
        with self.assertRaises(RuntimeError): r.submit(self.job,self.file,'one',1,True)
        self.assertFalse((self.job/'CURRENT.json').exists())
        accepted=r.submit(self.job,self.file,'one',1)
        self.assertTrue(r.submit(self.job,self.file,'one',1)['idempotent'])
        self.assertEqual(accepted['snapshot_sha256'],r.replay(self.job)['snapshot_sha256'])
        self.assertEqual(r.replay(self.job)['completed_by_layer']['structure'],1)
        self.assertEqual(r.replay(self.job)['next_unprocessed_by_layer']['structure'],'Test 2a:2')
    def test_stale_owner_does_not_promote(self):
        with self.assertRaisesRegex(ValueError,'stale'): r.submit(self.job,self.file,'two',1)
        with self.assertRaisesRegex(ValueError,'stale'): r.submit(self.job,self.file,'one',2)
    def test_bad_quote_saved_but_not_promoted(self):
        self.p['records'][0]['evidence'][0]['quote']='wrong'; self.save()
        with self.assertRaisesRegex(ValueError,'quote'): r.submit(self.job,self.file,'one',1)
        self.assertEqual(len(list((self.job/'proposals').glob('*.json'))),1)
        self.assertFalse((self.job/'CURRENT.json').exists())
    def test_interval_gap(self):
        self.p['records'][0]['evidence'][0].update(end_char=3,quote='אב😀'); self.save()
        with self.assertRaisesRegex(ValueError,'partition'): r.submit(self.job,self.file,'one',1)
    def test_interval_overlap(self):
        b=copy.deepcopy(self.p['records'][0]); b['id']='second'; self.p['records'].append(b); self.p['open_tails'].append('second'); self.save()
        with self.assertRaisesRegex(ValueError,'overlap'): r.submit(self.job,self.file,'one',1)
    def test_schema_rejects_unknown_content(self):
        self.p['records'][0]['content']['invented']=1; self.save()
        with self.assertRaises(r.jsonschema.ValidationError): r.submit(self.job,self.file,'one',1)
    def test_state_result_consistency(self):
        self.p['coverage'][0]['extraction_result']=None; self.save()
        with self.assertRaisesRegex(ValueError,'state/result'): r.submit(self.job,self.file,'one',1)
    def test_endpoint_types(self):
        e=copy.deepcopy(self.p['records'][0]); e.update(id='edge',layer='edges',content=dict(source_id='struct',target_id='struct',relation='objection',explicitness='source_explicit')); self.p['records'].append(e); self.save()
        with self.assertRaisesRegex(ValueError,'endpoint type'): r.submit(self.job,self.file,'one',1)
    def test_corrupt_proposal_replay(self):
        r.submit(self.job,self.file,'one',1)
        next((self.job/'proposals').glob('*.json')).write_text('{}')
        with self.assertRaisesRegex(ValueError,'corruption'): r.replay(self.job)
    def test_wrong_manifest_pin(self):
        p=Path(self.tmp.name)/'manifest'; p.write_text('{}')
        with self.assertRaisesRegex(ValueError,'unapproved'): r.source(Path(self.tmp.name),p,'Test')
    def test_changed_protocol(self):
        self.p['protocol_sha256']='bad'; self.save()
        with self.assertRaisesRegex(ValueError,'contract mismatch'): r.submit(self.job,self.file,'one',1)
    def test_stale_coverage_after_revision(self):
        r.submit(self.job,self.file,'one',1)
        self.p['records'][0].update(id='newstruct',supersedes='struct'); self.p['coverage']=[]; self.p['open_tails']=['newstruct']; self.save()
        with self.assertRaisesRegex(ValueError,'dependent coverage'): r.submit(self.job,self.file,'one',1)
    def test_dropped_or_unknown_tail(self):
        for tails in [[],['unknown']]:
            self.p['open_tails']=tails; self.save()
            with self.assertRaisesRegex(ValueError,'open tails'): r.submit(self.job,self.file,'one',1)
    def test_competing_successors(self):
        r.submit(self.job,self.file,'one',1)
        a=copy.deepcopy(self.p['records'][0]); a.update(id='a',supersedes='struct')
        b=copy.deepcopy(a); b['id']='b'; self.p['records']=[a,b]; self.save()
        with self.assertRaisesRegex(ValueError,'successor'): r.submit(self.job,self.file,'one',1)
    def test_revision_invalidates_graph(self):
        a=copy.deepcopy(self.p['records'][0]); a.update(id='claim',layer='claims',content=dict(proposition='test',conditions=[],scope='test',assertion_mode='asserted'))
        b=copy.deepcopy(a); b.update(id='position',layer='positions',content=dict(holder_candidates=[],claim_id='claim',question_id=None,conditions=[],local_status='unresolved'))
        self.p['records'] += [a,b]; self.save(); r.submit(self.job,self.file,'one',1)
        a.update(id='newclaim',supersedes='claim'); self.p['records']=[a]; self.p['coverage']=[]; self.save()
        with self.assertRaisesRegex(ValueError,'active graph'): r.submit(self.job,self.file,'one',1)
    def test_export_binds_snapshot_and_is_deterministic(self):
        r.submit(self.job,self.file,'one',1)
        out=self.job/'export'; receipt=r.export(self.job,out)
        self.assertEqual(receipt,r.export(self.job,out))
        self.assertEqual(receipt['snapshot_sha256'],r.replay(self.job)['snapshot_sha256'])
        self.assertFalse(r.read(out/'qualification.json')['ml_eligible'])
    def test_migration_preserves_bytes_and_requires_owner(self):
        legacy=Path(self.tmp.name)/'legacy'; (legacy/'data').mkdir(parents=True)
        row=dict(id='oldclaim',tractate='Test',ml_eligible=False)
        raw=json.dumps(row,indent=None).encode()+b'\r\n'; (legacy/'data'/'statements.jsonl').write_bytes(raw)
        with self.assertRaisesRegex(ValueError,'stale'): r.migrate(self.job,legacy,'wrong',1)
        result=r.migrate(self.job,legacy,'one',1)
        self.assertEqual(result,r.migrate(self.job,legacy,'one',1))
        mapping=r.read(self.job/'migrations'/f'{result["migration_sha256"]}.json')
        self.assertEqual(mapping['mappings'][0]['relationship'],'unmapped')
        self.assertEqual((self.job/'legacy'/f'{r.sha(raw)}.jsonl').read_bytes(),raw)

if __name__=='__main__': unittest.main()
