import numpy as np
from netCDF4 import Dataset,num2date, date2num, date2index
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from mpl_toolkits.basemap import Basemap,shiftgrid,maskoceans,addcyclic
matplotlib.use('Agg')

path = 'testdata/xjoad.d18Opw.10yrs.annual.nc'
var_name='d18O'
label = r'$\delta^{18} O$'+u' ('+u'\u2030'+')'

f = Dataset(path)
var = f.variables[var_name][:,:]#[0,0,:,:]
lat = f.variables['latitude'][:]
lon = f.variables['longitude'][:]
f.close()

fig = plt.figure()
m=Basemap(projection='spstere',boundinglat=-60,lon_0=-180,resolution='h')
var_cyclic,lon_cyclic = addcyclic(var,lon)
var_cyclic,lon_cyclic = shiftgrid(180.,var_cyclic,lon_cyclic,start=False)
lon2d,lat2d=np.meshgrid(lon_cyclic,lat)
x,y=m(lon2d,lat2d)
mdata=maskoceans(lon2d,lat2d,var_cyclic,resolution='h',grid=1.25,inlands=True)
cs=m.contourf(x,y,mdata,cmap=plt.cm.rainbow,alpha=0.5)
levels = np.arange(var.min(),var.max(),5)
cs2 = m.contour(x,y,mdata,levels=levels,linewidth=1.)
plt.clabel(cs2,fmt='%4.0f',fontsize=8)
m.drawcoastlines(color='grey')
m.drawmapboundary()
cbar=m.colorbar(cs,location='bottom')
cbar.set_label(label)
cbar.ax.tick_params(labelsize=8)
plt.show()
