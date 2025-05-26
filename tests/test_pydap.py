import numpy as np
from pydap.client import open_url

print("running pydap test")

try:
    dataset = open_url('http://test.opendap.org/dap/data/nc/coads_climatology.nc',
                       timeout=10)

    print('Using COADS data for test')
    sst = dataset['SST']
    assert sst.shape == (12, 90, 180)
    val = sst[1, 40, 70].data.item()
    assert 29 < val < 30

except Exception as exc:

    if str(exc) != 'Timeout':
        raise

    dataset = open_url('https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2/sst.mnmean.nc',
                       timeout=20)
    print('Using NOAA OISST data for test')
    sst = dataset['sst']
    assert sst.shape == (494, 180, 360)
    val = sst[1, 40, 70].data.item()
    assert val == 922

