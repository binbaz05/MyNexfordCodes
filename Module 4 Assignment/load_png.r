if (!require("png")) {
  install.packages("png")
  library(png)
}

# Load additional required libraries
if (!require("grid")) {
  install.packages("grid")
  library(grid)
}

# Load necessary libraries

library(png)
library(grid)

# Be sure to replace this path with the directory where the PNG file is located.

setwd("/Users/binbaz/Developer/MyNexfordCodes/Module 4 Assignment")

# Load and display the image
img <- readPNG("most_watched_genres.png")
grid.raster(img)
