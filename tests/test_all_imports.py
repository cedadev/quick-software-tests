import os
import sys
import re
import subprocess
import time

packs = []

libdir, = [d for d in sys.path if d.endswith('site-packages')]

print(libdir)

packages = sorted(re.sub('[.-].*$', '', name)
                  for name in os.listdir(libdir,)
                  if not (name.endswith("-info") or name.endswith(".egg") or name.endswith(".pth") or name.startswith("_") or name.endswith(".txt")))

failures = []

#strace_out = "/tmp/strace.out"

for pack in packages:
    print(pack)

    #if os.path.exists(strace_out):
    #    os.remove(strace_out)
        
    #strace = subprocess.Popen(f"strace -f -p {os.getpid()} -o {strace_out}", shell=True,
    #                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, 
    #                          )
    
    try:
        __import__(pack)
    #except ImportError:
    except Exception as exc:
        print(f"failed: {exc}")
        failures.append(pack)

    #time.sleep(0.5)
    #strace.kill()
    #
    #with open(strace_out) as f:
    #    for line in f:
    #        if re.match('^[0-9]+\s+open\(.*\.so(\.[0-9])*\".*= [0-9]+$', line):
    #            print(f"{pack} so-opened {line.strip()}")
    #
    #        if 'fortran' in line:
    #            print(f"{pack} all-fortran: {line.strip()}")
        

if failures:
    print("Failures:", failures)
    sys.exit(1)
else:
    print("no failures")
    
