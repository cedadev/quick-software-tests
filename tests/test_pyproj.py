from pyproj import CRS
from pyproj import Geod

print("doing pyproj test")

crs = CRS.from_epsg(4326)
assert crs.to_authority() == ('EPSG', '4326')
assert crs.prime_meridian.name == "Greenwich"


# and test based on geodesic line length example from
# https://pyproj4.github.io/pyproj/stable/examples.html

lats = [-72.9, -71.9, -74.9, -74.3, -77.5, -77.4, -71.7, -65.9, -65.7,
        -66.6, -66.9, -69.8, -70.0, -71.0, -77.3, -77.9, -74.7]

lons = [-74, -102, -102, -131, -163, 163, 172, 140, 113,
        88, 59, 25, -4, -14, -33, -46, -61]

geod = Geod(ellps="WGS84")
total_length = geod.line_length(lons, lats)

assert 14 < total_length / 1e6 < 15

