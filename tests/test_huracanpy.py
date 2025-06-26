from shapely import MultiPolygon
import matplotlib.pyplot as plt
import huracanpy

import _confirm_images as CI

for n, (basin, geometry) in enumerate(huracanpy.basins["WMO-TC"].iterrows()):
    # South Atlantic (SA) crosses dateline so is defined as two regions
    if isinstance(geometry.geometry, MultiPolygon):
        for geom in geometry.geometry.geoms:
            x, y = geom.exterior.xy
            plt.plot(x, y, color=f"C{n}")
            x, y = geom.centroid.xy
            plt.text(x[0], y[0], basin, color=f"C{n}", ha="center", va="center")
    else:
        plt.plot(*geometry.geometry.exterior.xy, color=f"C{n}")
        x, y = geometry.geometry.centroid.xy
        plt.text(x[0], y[0], basin, color=f"C{n}", ha="center", va="center")

CI.images_follow(['huracanpy_example.png'])
plt.show()
CI.image_confirm('huracanpy')
