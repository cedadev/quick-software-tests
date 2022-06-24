import os
import pyferret
pyferret.start(quiet=True)
import shutil

import iris_sample_data
fname = 'A1B_north_america.nc'
srcpath = os.path.join(iris_sample_data.path, fname)
ncpath = os.path.join('/tmp', fname)

shutil.copy(srcpath, ncpath)

ds = pyferret.FerDSet(ncpath)
assert(ds['height'].unit == 'm')
assert(ds['air_temperature'].data.shape == (49, 37, 1, 240, 1, 1))

os.remove(ncpath)
print('ran pyferret test')
