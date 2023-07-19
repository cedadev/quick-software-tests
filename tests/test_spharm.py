from mpl_toolkits.basemap import Basemap, addcyclic
from spharm import Spharmt, getspecindx
import matplotlib.pyplot as plt
import numpy as np

import _confirm_images as CI

# set up orthographic map projection.
map = Basemap(projection='ortho',lat_0=30,lon_0=-60,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines()
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary()
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
#min = int(input('input degree (m) of legendre function to plot:'))
#nin = int(input('input order  (n) of legendre function to plot:'))
min = 3
nin = 3
nlons = 720; nlats = 361
x = Spharmt(nlons,nlats,legfunc='computed')
ntrunc = nlats-1
indxm, indxn = getspecindx(ntrunc)
nm = -1
i = 0
for m,n in zip(indxm,indxn):
    if m  == min and n == nin:
        nm = i
        exit
    else:
        i = i + 1
if nm < 0:
    raise ValueError('invalid m,n - must fit within triangular truncation at wavenumber '+repr(ntrunc))
coeffs = np.zeros((ntrunc+1)*(ntrunc+2)//2,complex)
coeffs[nm] = 1.
spharmonic = x.spectogrd(coeffs)
delta = 360./nlons
lats = 90.-delta*np.arange(nlats)
lons = delta*np.arange(nlons)
spharmonic, lons = addcyclic(spharmonic, lons)
print(spharmonic.min(), spharmonic.max())
lons, lats = np.meshgrid(lons, lats)
x, y = map(lons,lats)
CS = map.contourf(x,y,spharmonic,15,cmap=plt.cm.jet)
plt.title('Spherical Harmonic of degree %2i and order %2i'% (min,nin))

CI.images_follow(['spharm_example.png'])
plt.show()
CI.image_confirm('spharm')
