# (test_xesmf.py)
import xarray as xr
import xesmf as xe
import numpy as np

ds = xr.tutorial.open_dataset('air_temperature') 
ds_out = xr.Dataset({'lat': (['lat'], np.arange(16, 75, 1.0)),
                     'lon': (['lon'], np.arange(200, 330, 1.5))})

regridder = xe.Regridder(ds, ds_out, 'bilinear')
output = regridder.regrid_dataset(ds)

