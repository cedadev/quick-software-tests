import numpy as np

dt = np.float64
n = 1234
a = np.arange(n, dtype=dt)

assert len(a) == n
assert a.dtype == dt
assert a.sum() == n * (n-1) / 2

print('did numpy test')
