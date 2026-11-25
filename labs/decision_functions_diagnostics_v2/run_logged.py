"""Supervise single-thread diagnostic stages; preserve failed command receipts."""
import subprocess
from core import *

def main():
    command=sys.argv[1:]; previous=list((OUT/'commands').glob('*.json'))
    used=sum(read(p)['cpu_seconds_sampled'] for p in previous)
    if used>=3500: raise RuntimeError('CPU budget guard')
    proc=subprocess.Popen(command,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
    process=psutil.Process(proc.pid); start=time.monotonic(); peak=0; cpu=0; killed=None
    while proc.poll() is None:
        try:
            t=process.cpu_times(); cpu=max(cpu,t.user+t.system); peak=max(peak,process.memory_info().rss)
        except psutil.Error: pass
        if cpu+used>3500 or peak>4*1024**3:
            killed='RESOURCE_LIMIT'; proc.terminate()
        time.sleep(.05)
    atomic(OUT/'commands'/f'{time.time_ns()}.json',dict(command=command,exit_status=proc.returncode,cpu_seconds_sampled=cpu,peak_rss_bytes_sampled=peak,wall_seconds=time.monotonic()-start,termination=killed,code_commit=head(),sampling_seconds=.05))
    sys.exit(proc.returncode)

if __name__=='__main__': main()
