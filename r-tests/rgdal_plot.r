library(rgdal)

print("Reading data.")

trees <- readOGR(dsn="testdata", layer="Heritage_Trees_pdx")

print("About to plot to screen.")

plot(trees['HEIGHT'])
axis(1)
axis(2)
title(main="Tree locations")

print("Finished plotting. Waiting 5")
Sys.sleep(5)
print("Goodbye.")
