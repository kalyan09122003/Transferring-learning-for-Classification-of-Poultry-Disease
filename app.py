from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model("poultry_disease_model.h5")
class_names = ['Healthy', 'Coccidiosis', 'Newcastle', 'Salmonella']  # Adjust as per your model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_page')
def prediction_page():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded!'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file!'
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Image processing
    img = image.load_img(file_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img) / 255.0
    img_tensor = np.expand_dims(img_tensor, axis=0)

    # Model prediction
    prediction = model.predict(img_tensor)
    class_index = np.argmax(prediction)
    result = class_names[class_index]

    return render_template('result.html', prediction=result, image_name=filename)

if __name__ == '__main__':
    app.run(debug=True)
