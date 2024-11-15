# load libraries

library(keras)
library(grid)

# Load the fashion dataset

fashion_mnist <- dataset_fashion_mnist()
c(x_train, y_train) %<-% fashion_mnist$train
c(x_test, y_test) %<-% fashion_mnist$test

# Process and prepare data

x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1)) / 255
x_test <- array_reshape(x_test, c(nrow(x_test), 28, 28, 1)) / 255

# Create the CNN model

model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = 'relu', input_shape = c(28, 28, 1)) %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_flatten() %>%
  layer_dense(units = 128, activation = 'relu') %>%
  layer_dense(units = 10, activation = 'softmax')

# Complie the model

model %>% compile(
  optimizer = 'adam',
  loss = 'sparse_categorical_crossentropy',
  metrics = c('accuracy')
)

# Train the model

model %>% fit(x_train, y_train, epochs = 5, batch_size = 64, validation_split = 0.2)

# Evaluate the model

score <- model %>% evaluate(x_test, y_test)
cat('Test accuracy:', score[[2]],  "\n")

# make predictions

predictions <- model %>% predict(x_test[1:2,,,])

# Visualize the predictions
par(mfrow = c(1, 2))  
for (i in 1:2) {
  plot.new()  
  grid.raster(x_test[i,,,1], interpolate = FALSE) 
  title(paste("Predicted:", which.max(predictions[i,]) - 1, "Actual:", y_test[i]))  
}
