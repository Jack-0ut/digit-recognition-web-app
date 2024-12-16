# 📝 **Digit Recognition Web App**

## 🚀 Introduction

Welcome to the **Digit Recognition Web App**, an interactive web-based application that uses the famous MNIST dataset to recognize handwritten digits. This project combines machine learning with a modern user interface to offer a sleek, real-time experience where you can draw digits and instantly see the model's predictions.

Utilizing the power of **Deep Learning** and a minimalist design inspired by Steve Jobs' aesthetic principles, this web app provides a unique and enjoyable way to explore digit recognition.

## 🖼️ Features

- **Real-Time Digit Recognition:** Draw digits on a canvas and get immediate predictions from the model.
- **Customizable Brush Color:** Use a color picker to change the color of your drawn digits.
- **Sleek Interface:** Clean, minimalist design with smooth transitions and animations, making the experience both functional and visually appealing.
- **Clear & Submit Buttons:** Easily clear the canvas or submit the drawing for recognition with a click.

## 🌐 Demo

Try the demo of the **Digit Recognition Web App** directly by visiting the deployed version (if available).

## 🧑‍💻 Technologies Used

- **Frontend:**
  - **HTML5, CSS3, JavaScript**: For the structure, styling, and interactivity of the web app.
  - **Canvas API**: For drawing the digits.
  - **Fetch API**: For submitting the drawn images to the backend for prediction.

- **Backend:**
  - **Python, TensorFlow**: For building the machine learning model that recognizes the digits.
  - **Flask**: For creating the server to handle requests and serve the model.

- **Deployment:**
  - **GitHub Pages (Frontend)**: For hosting the frontend of the app.
  - **Heroku / Google Cloud / AWS**: For hosting the backend API, making predictions in real-time.

## 🎯 How It Works

1. **Drawing Digits:** You can use the canvas to draw digits. A color picker allows you to choose the brush color for your drawing.
2. **Submitting the Drawing:** Once you're satisfied with your drawing, hit the **Submit** button to send it to the server.
3. **Prediction:** The drawing is sent to the backend, where the pre-trained model (using the MNIST dataset) predicts the digit.
4. **Displaying the Result:** The predicted digit is displayed on the second canvas.

## 💻 Setup and Installation

### 1. Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Jack-0ut/digit-recognition-web-app.git
cd digit-recognition-web-app
```

### 2. Install Backend Dependencies

Navigate to the backend directory and install the necessary Python dependencies:

```bash
pip install -r requirements.txt
``` 

### Run the Backend Flask Server

```bash 
python app.py
```
### 🎉 Play and Have Fun!
Now you're all set! Open the web application, start drawing digits, and let the model recognize them. It's that simple! 😄

Feel free to experiment, improve, and share your results with others. We're excited to see how you use this project!