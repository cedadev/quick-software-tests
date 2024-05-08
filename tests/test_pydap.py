import numpy as np
from pydap.client import open_url

print("running pydap test")

# dataset = open_url('http://test.opendap.org/dap/data/nc/coads_climatology.nc')
# sst = dataset['SST']
# 
# assert sst.shape == (12, 90, 180)
# val, = sst[1, 40, 70].array
# assert 29 < val < 30
#


dataset = open_url('https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.mnmean.nc')
sst = dataset['sst']

assert sst.shape == (494, 180, 360)

val = np.array(sst[1, 40, 70]).flatten()[0]
assert val == 922

