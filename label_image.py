from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('final_model.h5')

# Load the classes
classes = np.load('classes.npy')

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
    image_path = 'example_image.jpg'  # Replace with the path to your test image
    prediction, confidence = predict_weather(image_path)
    print("Predicted class:", prediction)
    print("Confidence levels:", confidence)
