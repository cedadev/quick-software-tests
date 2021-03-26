print("About to read netcdf data.")

library(ncdf4)
nc_data <- nc_open('cfplot_data/ggap.nc')
lon <- ncvar_get(nc_data, "longitude")
lat <- ncvar_get(nc_data, "latitude")
U <- ncvar_get(nc_data, "U")

print("About to plot netcdf data to screen.")

library(raster)

U.slice <- U[,,1]
r <- raster(t(U.slice), xmn=0, xmx=360, ymn=-90, ymx=90, crs=CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs+ towgs84=0,0,0"))

plot(r)

print("Finished plotting. Waiting 5")
Sys.sleep(5)
print("Goodbye.")
