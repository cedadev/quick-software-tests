import os
import cf
import matplotlib.pyplot as plt
import cfplot as cfp

import _confirm_images as CI

pngs = ['tas.png', 'ggap1.png', 'ggap2.png']
cfp.setvars(file=pngs[0])

f=cf.read('testdata/tas_A1.nc')[0]
cfp.con(f.subspace(time=15))


cfp.setvars(file=pngs[1])
f=cf.read('testdata/ggap.nc')[1]
cfp.mapset(proj='npstere')
cfp.con(f.subspace(pressure=500))

cfp.setvars(file=pngs[2])
f=cf.read('testdata/ggap.nc')[1]
cfp.gopen(rows=2, columns=2, bottom=0.2)
cfp.gpos(1)
cfp.con(f.subspace(pressure=500), lines=False, colorbar=None)
cfp.gpos(2)
cfp.mapset(proj='moll')
cfp.con(f.subspace(pressure=500), lines=False, colorbar=None)
cfp.gpos(3)
cfp.mapset(proj='npstere', boundinglat=30, lon_0=180)
cfp.con(f.subspace(pressure=500), lines=False, colorbar=None)
cfp.gpos(4)
cfp.mapset(proj='spstere', boundinglat=-30, lon_0=0)
#cfp.con(f.subspace(pressure=500), lines=False, 
#        colorbar_orientation='horizontal')
cfp.con(f.subspace(pressure=500), lines=False)
cfp.gclose()

for png in pngs:
    if not os.path.isfile(png):
        raise Exception(f'PNG not written: {png}')

    os.system(f'display {png} &')

CI.images_launched(pngs)
CI.image_confirm('cfplot')
