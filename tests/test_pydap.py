from pydap.client import open_url

print("running pydap test")

dataset = open_url('http://test.opendap.org/dap/data/nc/coads_climatology.nc')
sst = dataset['SST']

assert sst.shape == (12, 90, 180)
val, = sst[1, 40, 70].array
assert 29 < val < 30
