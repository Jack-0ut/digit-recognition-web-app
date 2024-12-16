from flask import Flask, render_template, request, jsonify
import numpy as np
import keras
from PIL import Image
import time
import tensorflow as tf
import os

# Set logging level to ERROR to suppress unnecessary messages
tf.get_logger().setLevel('ERROR')

app = Flask(__name__)

# Load the model
model = keras.models.load_model("mnist_model.keras")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the image is in the request
    if 'digit' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    img = request.files['digit']
    
    # Generate a unique filename using the current timestamp
    timestamp = int(time.time()) 

    # Create the uploads directory if it doesn't exist
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    img_filename = os.path.join(UPLOAD_FOLDER, f'digit_{timestamp}.png')
    try:
        img.save(img_filename)
    except Exception as e:
        print(f"Error saving the image: {e}")
        return jsonify({'error': 'Error saving the image'}), 500
    
    # Process the image
    try:
        img = Image.open(img).convert('L').resize((28, 28))
        img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0
    except Exception as e:
        print(f"Error processing the image: {e}")
        return jsonify({'error': 'Error processing the image'}), 500
    
    # Predict the digit
    try:
        prediction = model.predict(img_array)
        print(f"Prediction: {prediction}")
        predicted_digit = np.argmax(prediction)
        return jsonify({'digit': int(predicted_digit)})
    except Exception as e:
        print(f"Error predicting the digit: {e}")
        return jsonify({'error': 'Error predicting the digit'}), 500

if __name__ == '__main__':
    app.run(debug=True)
