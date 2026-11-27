"""Required-command accounting and child cleanup; used by real and mocked launches."""
from common import *
import psutil

def supervise(command,out,cpu_limit=3600,rss_limit=4*1024**3,interrupt=False):
    out=Path(out);root=out/'commands';root.mkdir(parents=True,exist_ok=True)
    starts=list(root.glob('*.start.json'));ends=list(root.glob('*.complete.json'))
    require({p.stem.split('.')[0] for p in starts}=={p.stem.split('.')[0] for p in ends},'Unaccounted command; no automatic retry')
    prior=sum(read(p)['cpu_seconds_sampled'] for p in ends)
    require(prior<cpu_limit,'CPU ceiling')
    key=str(time.time_ns());atomic(root/(key+'.start.json'),dict(command=command,prior_cpu=prior,time=time.time()))
    child=None;peak=0;seen={};reason=None;code=None;beg=time.monotonic()
    try:
        child=subprocess.Popen(command,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'})
        process=psutil.Process(child.pid)
        while child.poll() is None:
            if interrupt and (interrupt is True or Path(interrupt).exists()):raise KeyboardInterrupt('mock supervisor interruption')
            try:tree=[process]+process.children(recursive=True)
            except psutil.Error:tree=[]
            rss=0
            for p in tree:
                try:
                    t=p.cpu_times();seen[(p.pid,p.create_time())]=max(seen.get((p.pid,p.create_time()),0),t.user+t.system);rss+=p.memory_info().rss
                except psutil.Error:pass
            peak=max(peak,rss)
            if prior+sum(seen.values())>=cpu_limit-1 or peak>rss_limit:raise RuntimeError('RESOURCE_STOP')
            time.sleep(.02)
        code=child.wait()
        if code:reason='CHILD_FAILURE'
    except BaseException as e:
        reason=repr(e)
        if child is not None:
            try:desc=psutil.Process(child.pid).children(recursive=True)
            except psutil.Error:desc=[]
            for p in reversed(desc):
                try:p.terminate()
                except psutil.Error:pass
            if child.poll() is None:child.terminate()
            try:child.wait(timeout=5)
            except subprocess.TimeoutExpired:child.kill();child.wait()
            _,alive=psutil.wait_procs(desc,timeout=5)
            for p in alive:
                try:p.kill()
                except psutil.Error:pass
            psutil.wait_procs(alive,timeout=5)
            code=child.returncode
    receipt=dict(command=command,exit_code=code,reason=reason,cpu_seconds_sampled=sum(seen.values()),wall_seconds=time.monotonic()-beg,peak_process_tree_rss_bytes_sampled=peak,sampling_seconds=.02,child_pid=None if child is None else child.pid,child_reaped=child is None or child.poll() is not None,scope='process tree; retained observed CPU per PID/create-time; startup/exit CPU and short-lived processes/transient RSS may be missed')
    atomic(root/(key+'.complete.json'),receipt)
    if reason:
        atomic(out/('SUPERVISOR_STOP_'+key+'.json'),terminal(completed=0,expected=82,integrity='INCOMPLETE',numerical='NOT_ESTABLISHED',scientific='NOT_ESTABLISHED',reason=reason))
    elif any(x in ('report','recover-report') for x in command):
        from reporting import finalize
        finalize(out)
    return receipt

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,required=True);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
    r=supervise(a.command,a.output_root);sys.exit(0 if not r['reason'] else 1)
