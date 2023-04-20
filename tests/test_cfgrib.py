import os
import glob
import xarray as xr

url = "https://github.com/pydata/xarray-data/raw/7d8290e0be9d2a8f4b4381641f20a97db6eaea3d/era5-2mt-2019-03-uk.grib"

fname = os.path.basename(url)

if not os.path.exists(fname):
    os.system(f"wget {url}")
for f in glob.glob(f"{fname}.*.idx"):
    os.remove(f)
    
ds = xr.open_dataset(fname, engine="cfgrib")
print(ds)
t2m = ds.variables['t2m']
assert t2m.shape == (744, 33, 49)
assert 282.3 < float(t2m[2,3,4]) < 282.4
assert t2m.attrs['long_name'] == '2 metre temperature'

for f in glob.glob(f"{fname}.*.idx"):
    os.remove(f)
	
