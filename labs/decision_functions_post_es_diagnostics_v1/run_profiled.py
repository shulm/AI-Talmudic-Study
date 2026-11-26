"""Cumulative single-thread supervisor; immutable start/completion and terminal stop."""
from common import *
def main():
    cmd=sys.argv[1:];root=OUT/'commands';starts=list(root.glob('*.start.json'));ends=list(root.glob('*.complete.json'))
    if {p.name.split('.')[0] for p in starts}!={p.name.split('.')[0] for p in ends}:raise RuntimeError('Unaccounted prior command; stop')
    used=sum(read(p)['cpu_seconds_sampled'] for p in ends)
    if used>=590:raise RuntimeError('600 CPU-second ceiling guard')
    key=str(time.time_ns());atomic(root/(key+'.start.json'),dict(command=cmd,utc=time.time(),used_cpu=used))
    child=subprocess.Popen(cmd,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'});proc=psutil.Process(child.pid);cpu=0.;rss=0;start=time.monotonic();stop=None
    while child.poll() is None:
        try:times=proc.cpu_times();cpu=max(cpu,times.user+times.system);rss=max(rss,proc.memory_info().rss)
        except psutil.Error:pass
        if cpu+used>590 or rss>1024**3:
            stop='RESOURCE_STOP';child.terminate()
        time.sleep(.02)
    atomic(root/(key+'.complete.json'),dict(command=cmd,exit_code=child.returncode,cpu_seconds_sampled=cpu,wall_seconds=time.monotonic()-start,peak_rss_bytes_sampled=rss,stop=stop,sampling_seconds=.02))
    if stop:
        import terminal
        terminal.publish(OUT/'RESOURCE_STOP.json',completed=dict(attempts=len(list((OUT/'attempts').glob('*.complete.json')))),expected=dict(attempts=384),integrity='INCOMPLETE',numerical='INCOMPLETE',scientific='NOT_RUN',reason=stop)
    sys.exit(child.returncode)
if __name__=='__main__':main()
