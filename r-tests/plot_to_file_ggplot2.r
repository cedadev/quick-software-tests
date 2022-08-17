library(ggplot2)
png("plot.png")

# Very basic chart
basic <- ggplot( mtcars , aes(x=mpg, y=wt)) +
geom_point()
basic

dev.off()
