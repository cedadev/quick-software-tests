import numpy as np
import xarray as xr

from flox.xarray import xarray_reduce

print("doing flox test...", end="")

labels = xr.DataArray(
    [1, 2, 3, 1, 2, 3, 0, 0, 0],
    dims="x",
    name="label",
)

da = xr.DataArray(
    np.ones((9,)), dims="x", name="array"
)

vals = xarray_reduce(da, labels, func="sum")

assert xarray_reduce(da, labels, func="sum").to_numpy().tolist() == [3,2,2,2]

print("done")
