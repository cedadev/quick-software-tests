# older versions of R will fail with this test
# thanks to Selma Guerreiro for the test code

library(terra)

gauge_locations = data.frame( latitude = 54.966667, longitude = -1.600000)

gauges_spatial = vect(gauge_locations, geom=c("longitude", "latitude"), crs = "epsg:4326") # Create a SpatialPoints object with WGS84 coordinates

gauges_rotated = rotate(gauges_spatial, long=0, split=TRUE, left=FALSE)

print("did terra test")
