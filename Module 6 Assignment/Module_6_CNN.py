# importting libraries
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.datasets import fashion_mnist


# Load the datasets containing the images of fashion categories.

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Label descriptions for the Fashion MNIST dataset

label_descriptions = {
    0: 'T-shirt/top',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle boot'
}

# Process and prepere data

x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255

# Create a CNN Model

model = Sequential([
    Input(shape=(28, 28, 1)),  # Define the input shape here
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')  # 10 classes for Fashion MNIST
])

# Compile and Train the Model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the Model

model.fit(x_train, y_train, epochs=7, batch_size=64, validation_split=0.2)

# Evaluate the model

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc}")

# Make predictions

predictions = model.predict(x_test[:2])

# Visualize predictions with description

for i in range(2):
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    predicted_label = np.argmax(predictions[i])
    actual_label = y_test[i]
    plt.title(f"Predicted: {label_descriptions[predicted_label]} "
              f"(Index: {predicted_label})\nActual: {label_descriptions[actual_label]} "
              f"(Index: {actual_label})")
    plt.axis('off')
    plt.show()

