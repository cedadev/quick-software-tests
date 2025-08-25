library(terra)

point.location = data.frame(latitude = -72.5, longitude = 3.75)
point.spatial = vect(point.location, geom=c("longitude", "latitude"), crs = "epsg:4326")

# Load the NetCDF file
ras = rast("testdata/tasmax.nc")
x = extract(ras, point.spatial , method="simple")

val = x[[2]]
expected = 265.8456
tolerance = 1e-4

if (abs(val - expected) < tolerance) {
  print("R terra netcdf test succeeded")
  quit()
} else {
  print("R terra netcdf test failed")
  quit(status=1)
}
