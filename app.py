from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = load_model('fmodel.h5')

# Load the classes
classes = np.load('classes.npy')

# Define the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the file from the POST request
        f = request.files['file']

        # Save the file to ./static/uploads
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(file_path)

        # Make prediction
        prediction, confidence = predict_weather(file_path)

        # Pass image URL and prediction with confidence to the result template
        image_url = '/static/uploads/' + f.filename  # Assuming 'uploads' directory is in 'static' folder
        return render_template('result.html', image_url=image_url, prediction=prediction, confidence=confidence)

def predict_weather(image_path):
    img = image.load_img(image_path, target_size=(32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale pixel values to [0, 1]

    # Predict
    result = model.predict(img_array)

    # Get the predicted class label
    predicted_class = classes[np.argmax(result)]

    # Get confidence levels for each class
    confidence = {classes[i]: result[0][i] for i in range(len(classes))}

    return predicted_class, confidence

if __name__ == '__main__':
    app.run(debug=True)
