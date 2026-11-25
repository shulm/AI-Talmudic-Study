"""Actual verifier mutations over mock optimizer evidence; research seeds never used."""
from contracts import *
import execute,fixture,head,verify
import shutil

def main(receipt):
    results={};start=time.process_time();original_generate=fixture.generate;original_solve=head.solve
    def toy_generate(*args,**kwargs):return original_generate(8001,8002,8003)
    def fake_solve(fun,initial,ledger,key,feature,person_scale):
        ledger.start(key,ledger.expected[key]);x=initial.ravel();value,grad=fun(x)
        ledger.parameter_root.mkdir(parents=True,exist_ok=True)
        with (ledger.parameter_root/(key+'.npy')).open('xb') as f:np.save(f,x,allow_pickle=False)
        ledger.complete(key,dict(success=True,finite=True,message='MOCK_NO_OPTIMIZATION',iterations=0,objective=float(value),gradient_max=float(abs(grad).max()),person_scaled_gradient_max=float(abs(grad).max()*person_scale),parameter_count=len(x),parameter_norm=float(np.linalg.norm(x)),feature_shape=list(feature.shape),feature_norm=float(np.linalg.norm(feature)),cpu_seconds=0.,wall_seconds=0.))
        return x
    fixture.generate=toy_generate;head.solve=fake_solve
    try:
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);private=root/'private';out=root/'public';out.mkdir()
            atomic(out/'environment.json',environment());atomic(out/'historical_blobs.json',historical())
            atomic(out/'prefit_sources.json',dict(files={p:file_hash(ROOT/p) for p in source_paths()}))
            for r in REAL:execute.run(r,private,out)
            atomic(out/'scientific_summary.json',execute.scientific_summary(out))
            good=verify.verify(private,out)
            if good['state']!='VERIFIED_COMPLETE' or good['qualification']:raise AssertionError('Mock full-run state incorrect')
            results['complete_mock']=dict(state=good['state'],comparisons=good['comparisons'],qualification=good['qualification'])
            # Snapshot exact disposable evidence; each mutation is isolated and restored.
            original={p:p.read_bytes() for p in root.rglob('*') if p.is_file()}
            def restore():
                for p,b in original.items():p.write_bytes(b)
            def put(p,x):p.write_text(json.dumps(x,allow_nan=False)+'\n',encoding='utf-8')
            def reseal():
                r='E';rr=private/r;man=read(out/(r+'_manifest.json'));man['private_files']={p.relative_to(rr).as_posix():file_hash(p) for p in rr.rglob('*') if p.is_file()};put(out/(r+'_manifest.json'),man)
                for st in STAGES:
                    path=out/'records'/f'{r}_{st}';b=read(path/'binding.json');b['input_hashes']={p:file_hash(rr/p) for p in binding_paths(r,st)};put(path/'binding.json',b)
                    for key in expected(r,st):
                        s=read(path/(key+'.start.json'));s['binding_hash']=file_hash(path/'binding.json');put(path/(key+'.start.json'),s)
            def reject(name,mutate):
                restore();mutate()
                try:verify.verify(private,out)
                except Exception as e:results[name]=dict(rejected=True,error=str(e));return
                raise AssertionError(name+' passed')
            def archive(role,change):
                path=private/'E'/(role+'.npz');a=execute.load(path);change(a)
                with path.open('wb') as f:np.savez_compressed(f,**a)
                reseal()
            reject('corrupt_bytes',lambda:(private/'E'/'evidence.npz').write_bytes(b'corrupt'))
            reject('missing_evidence',lambda:archive('evidence',lambda a:a.pop('101_w')))
            reject('wrong_prediction',lambda:archive('predictions',lambda a:a['101_ES'].__setitem__((0,0,slice(None)),a['101_ES'][0,0,::-1])))
            reject('bad_normalization',lambda:archive('predictions',lambda a:a['101_ES'].__setitem__((0,0,0),.9)))
            reject('wrong_evidence',lambda:archive('evidence',lambda a:a['101_11_log_e'].__setitem__(0,1.)))
            reject('wrong_weight',lambda:archive('evidence',lambda a:a['101_w'].__setitem__(0,.4)))
            reject('wrong_parameter_slice',lambda:archive('models',lambda a:a['11_U'].__setitem__((0,0),9.)))
            reject('empty_input_binding',lambda:put(out/'records/E_shared/binding.json',dict(input_hashes={},code_hashes={},environment={})))
            reject('empty_source_manifest',lambda:put(out/'prefit_sources.json',dict(files={})))
            reject('empty_history_manifest',lambda:put(out/'historical_blobs.json',{}))
            target=out/'records/E_support/E_support_101_B3_48.complete.json'
            reject('incomplete_log',lambda:put(target,dict(id='E_support_101_B3_48',meta=expected('E','support')['E_support_101_B3_48'],success=True,finite=True)))
            def bad_success():x=read(target);x['success']=False;put(target,x)
            reject('nonconvergence',bad_success)
            def bad_summary():x=read(out/'scientific_summary.json');x['predictive_qualified']=True;put(out/'scientific_summary.json',x)
            reject('inconsistent_qualification',bad_summary)
            def wrong_score():x=read(out/'E_scores.json');x['gates']['ES']['values']['gain']+=.1;put(out/'E_scores.json',x)
            reject('wrong_aggregation',wrong_score)
            def duplicate():
                import zipfile,io,warnings
                path=private/'E/evidence.npz';b=io.BytesIO();np.save(b,np.zeros(48),allow_pickle=False)
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    with zipfile.ZipFile(path,'a') as z:z.writestr('101_w.npy',b.getvalue())
                reseal()
            reject('duplicate_evidence',duplicate)
            restore()
            # A deletion is confined to this TemporaryDirectory and restored immediately.
            target.unlink()
            try:verify.verify(private,out)
            except Exception as e:results['missing_configuration']=dict(rejected=True,error=str(e))
            else:raise AssertionError('Missing configuration passed')
            restore()
            try:execute.run('E',private,out)
            except FileExistsError:results['output_collision']=dict(rejected=True)
            else:raise AssertionError('Collision passed')
        atomic(receipt,dict(passed=True,checks=results,cpu_seconds=time.process_time()-start,scientific_fits=0,scientific_seed_materializations=0,fixture='full-shape mock integration only: generator8001/labels8002/mask8003; optimizer replaced by initial-vector passthrough; not research evidence'))
    except Exception as e:atomic(receipt,dict(passed=False,checks=results,error=repr(e),cpu_seconds=time.process_time()-start));raise
    finally:fixture.generate=original_generate;head.solve=original_solve

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);a=p.parse_args();main(a.receipt)
