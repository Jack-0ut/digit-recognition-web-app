import matplotlib.pyplot as plt
import numpy as np
from keras.api.datasets import mnist
from PIL import Image
import os

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Function to preprocess the uploaded image (resize, convert to grayscale, normalize)
def preprocess_image(image_path):
    img = Image.open(image_path).convert('L').resize((28, 28))
    img_array = np.array(img) / 255.0  # Normalize to [0, 1]
    return img_array

# Function to plot images of a specific digit
def plot_digit_images(digit, num_images=10):
    # Filter the images for the specified digit
    indices = np.where(y_train == digit)[0]
    selected_images = x_train[indices][:num_images]  # Get first 'num_images' of the specified digit
    
    # Plot the images
    fig, axes = plt.subplots(1, num_images, figsize=(15, 3))
    for i, ax in enumerate(axes):
        ax.imshow(selected_images[i], cmap='gray')
        ax.axis('off')  # Hide axis
    plt.show()

# Function to compare the uploaded image with a dataset image
def compare_with_dataset(uploaded_image_path, digit=6):
    # Preprocess the uploaded image
    uploaded_img = preprocess_image(uploaded_image_path)

    # Filter the dataset to get images of the specified digit
    indices = np.where(y_train == digit)[0]
    selected_images = x_train[indices]

    # Randomly select one image from the dataset
    random_image = selected_images[np.random.choice(len(selected_images))]

    # Plot the uploaded image and the random dataset image
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(uploaded_img, cmap='gray')
    axes[0].set_title(f"Uploaded Image ({digit})")
    axes[0].axis('off')

    axes[1].imshow(random_image, cmap='gray')
    axes[1].set_title(f"Random Dataset Image ({digit})")
    axes[1].axis('off')

    plt.show()

# Example: Compare the uploaded '6.png' with a random '6' image from the dataset
uploaded_image_path = os.path.join('uploads', '6.png')
compare_with_dataset(uploaded_image_path, digit=6)
