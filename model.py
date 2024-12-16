from keras import layers, models
from keras.api.datasets import mnist
from keras.src.utils import to_categorical
from keras.src.layers import RandomRotation, RandomZoom, RandomFlip
from sklearn.model_selection import train_test_split  # To split the data

# Load and preprocess the MNIST dataset
(x_train_full, y_train_full), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train_full, x_test = x_train_full / 255.0, x_test / 255.0

# Reshape the data for CNN
x_train_full = x_train_full.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# One-hot encode the labels
y_train_full = to_categorical(y_train_full, 10)
y_test = to_categorical(y_test, 10)

# Split the training data into training and validation sets (80-20 split)
x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full, test_size=0.2, random_state=42)

# Data augmentation layers to improve generalization
data_augmentation = models.Sequential([
    RandomRotation(0.2),  # Rotate by a random angle up to 20%
    RandomZoom(0.2),      # Zoom by a random factor (up to 20%)
    RandomFlip('horizontal')  # Random horizontal flip
])

# Build the model
model = models.Sequential([
    data_augmentation,
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with train and validation data
model.fit(x_train, y_train, epochs=5, validation_data=(x_val, y_val))

# Save the model
model.save("mnist_model.keras")

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc}, Test Loss: {test_loss}")