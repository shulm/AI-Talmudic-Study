"""Measure child CPU, sampled peak RSS, wall time, exit status; persist failures."""
import subprocess
import sys
import time
import psutil
from common import *

def main():
    command=sys.argv[1:]; start=time.time()
    proc=subprocess.Popen(command)
    p=psutil.Process(proc.pid); peak=0; cpu=0
    while proc.poll() is None:
        try:
            peak=max(peak,p.memory_info().rss)
            t=p.cpu_times(); cpu=max(cpu,t.user+t.system)
        except psutil.Error: pass
        if peak>8*1024**3 or cpu>6*3600:
            proc.terminate()
        time.sleep(.1)
    path=OUT/'command_log.json'
    records=read(path) if path.exists() else []
    records.append(dict(command=command,exit_status=proc.returncode,wall_seconds=time.time()-start,cpu_seconds_sampled=cpu,peak_rss_bytes_sampled=peak))
    write(path,records)
    sys.exit(proc.returncode)

if __name__=='__main__': main()
