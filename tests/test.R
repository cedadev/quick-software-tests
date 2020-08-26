# Get DATA_DIR env variable
data_dir <- Sys.getenv('DATA_DIR')

# Test ggplot2
library(ggplot2)

# Test you can read a netcdf file
library(ncdf4)
#nc <- nc_open('/appx/contrib/jaspy/miniconda_envs/jaspy3.7/m3-4.6.14/envs/jaspy3.7-m3-4.6.14-r20200226/lib/python3.7/site-packages/iris_sample_data/sample_data/A1B_north_america.nc')
nc <- nc_open(paste(data_dir, "/", "A1B_north_america.nc", sep=""))
print(nc)


# Test simple features ("sf") works
library(sf)
(x <- st_point(c(1,2)))
st_zm(x, drop = TRUE, what = "ZM")


# Test "igraph"
library(igraph)
eye.col.v <- c("brown", "green", "brown", "blue", "blue", "blue")         #vector
eye.col.f <- factor(c("brown", "green", "brown", "blue", "blue", "blue")) #factor
eye.col.v


# Test "ggplot2"
# Load ggplot2
library(ggplot2)

# Very basic chart
basic <- ggplot(mtcars, aes(x=mpg, y=wt)) + geom_point()
basic
