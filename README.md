# CNN Weather Classifier

This is a web application built with Flask that allows users to upload images of weather conditions and predicts the weather class using a trained convolutional neural network model.

## Getting Started

To get started with the application, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/qmjae/CPE019_HOA10.git
2. Navigate to the project directory:
    cd weather-classifier
3. Install the required Python packages using  
    pip install -r requirements.txt
4. Run the Flask application:
    python app.py
5. Open your web browser and go to http://localhost:5000 to access the application.

Usage
Upload an image of a weather condition using the provided form.
Click on the "Predict" button to see the predicted weather class and confidence levels.
Optionally, you can upload another image and make another prediction.

Project Structure:

weather-classifier/
│
├── app.py               # Flask application code
├── static/              # Static files (e.g., images)
│   └── uploads/         # Directory for uploaded images
├── templates/           # HTML templates
│   ├── index.html       # Main page with upload form
│   └── result.html      # Result page with prediction
├── uploads/             # Images 
│   └── images(n)        
├── fmodel.h5            # Trained CNN model
├── classes.npy          # Encoded class labels
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation

