from common import *
import terminal
def execute(private,derived,out):
    if out.resolve()!=OUT.resolve():raise ValueError('Output root must match frozen protocol location')
    frozen();pub=read(out/'PUBLICATION.json')
    if not pub['verified'] or pub['commit']!=head():raise ValueError('Unverified pre-analysis checkpoint')
    if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS')):raise ValueError('Single computational thread required')
    if derived.resolve()==private.resolve() or private.resolve() in derived.resolve().parents:raise ValueError('Derived path overlaps historical cache')
    if (out/'EXECUTION_START.json').exists() or derived.exists():raise FileExistsError('No retries; fresh output required')
    atomic(out/'EXECUTION_START.json',dict(commit=head(),utc=time.time(),expected=expected()['counts']));derived.mkdir(parents=True,exist_ok=False)
    status=dict(diagnostic='INCOMPLETE',engineering='INCOMPLETE',ablation='UNAVAILABLE');reason=None;before=None
    try:
        if read(out/'INPUT_BINDINGS.json')['availability']=='AVAILABLE':
            before=verify_inputs(private)
            from diagnosis import calculate,old_forward
            from analysis import calculate as ablate
            forward=old_forward(private);atomic(out/'HISTORICAL_FORWARD.json',forward)
            residual,data=calculate(private);atomic(out/'RESIDUALS.json',residual)
            arrays,co,table=ablate(data,residual);save(derived/'uncapped_predictions.npz',arrays);save(derived/'coefficients.npz',co);atomic(out/'ABLATION.json',table)
            atomic(out/'DIAGNOSTIC_MANIFEST.json',dict(files={p.name:digest(p) for p in derived.glob('*.npz')},prediction_shapes={k:list(v.shape) for k,v in arrays.items()},coefficient_shapes={k:list(v.shape) for k,v in co.items()},residual_rows=len(residual['rows']),table_rows=len(table['rows']),aggregate_rows=len(table['aggregates']),old_forward_comparisons=forward['count']))
            status.update(diagnostic='COMPLETE',ablation='DESCRIPTIVE_COMPLETE')
        else:status['diagnostic']='PRIVATE_ARTIFACTS_UNAVAILABLE'
        from suite import run_suite
        checks=run_suite(derived,out);status['engineering']='PASS' if checks['passed'] else 'FAIL'
        if not checks['passed']:reason='ENGINEERING_CRITERION_FAILED; retained individual/analytic checks identify failures'
    except BaseException as e:reason=repr(e);raise
    finally:
        if before is not None:
            after=hashes(private);unchanged=before==after
            atomic(out/'INPUT_HASH_RECEIPT.json',dict(before=before,after=after,unchanged=unchanged))
            if not unchanged:reason='Historical input changed';status['diagnostic']='INCOMPLETE'
        completed=dict(attempts=len(list((out/'attempts').glob('*.complete.json'))),wrappers=len(list((out/'wrappers').glob('*.complete.json'))))
        atomic(out/'EXECUTION_TERMINAL.json',dict(**terminal.result(completed,dict(attempts=384,wrappers=114),'NOT_RUN',status['engineering'] if status['engineering'] in ('PASS','FAIL') else 'INCOMPLETE','NOT_RUN',reason),axes=status,historical_status='INCOMPLETE / NUMERICALLY_UNRESOLVED',qualification=False))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--derived-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();execute(a.private_root,a.derived_root,a.output_root)
