# import utility library
library(utils)

# define path to the zip file
zip_file_path <- "ALSON_LEE.zip"

expdir_path <- dirname(zip_file_path)

# unzip the file to the same directory 
unzip(zip_file_path, exdir = expdir_path)

csv_file <- list.files(expdir_path, pattern = "*.csv", full.names = TRUE)

# Read the CSV file
exployee_data <- read.csv(csv_file[1])

# display the employee data
print(exployee_data)


