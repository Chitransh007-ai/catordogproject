from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'

# Load .keras model
model = load_model('model/model.keras')

def predict_image(image_path):
    img = load_img(image_path, target_size=(128, 128))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return 'Dog' if prediction[0][0] > 0.5 else 'Cat'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded'
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    result = predict_image(filepath)
    return render_template('result.html', prediction=result, image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
