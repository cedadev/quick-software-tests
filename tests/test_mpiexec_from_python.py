import sys
import subprocess
import netCDF4

p = subprocess.Popen('mpiexec -n 2 /usr/bin/echo hello'.split(), 
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

out, err = p.communicate()
out = out.decode()
err = err.decode()
rc = p.returncode

if out != 'hello\nhello\n' or rc != 0 or err:
    print(f"mpiexec from python test failed: RC={rc} OUT={out}, ERR={err}")
    sys.exit(1)



