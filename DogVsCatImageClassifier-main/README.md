🐶🐱 Dog vs Cat Image Classifier
A deep learning web application built with Flask that classifies uploaded images as a Dog 🐕 or a Cat 🐈 using a trained Convolutional Neural Network (CNN) model.

📌 Project Structure
image-classification-using-cnn/
├── app.py                # Flask backend application
├── model/
│   └── model.keras        # Trained CNN model file
├── static/
│   ├── uploads/           # Uploaded images (temporary)
│   └── css/               # Styles (optional)
├── templates/
│   ├── index.html         # Upload page
│   └── result.html        # Prediction results page
├── .gitignore             # Files to ignore in Git
├── requirements.txt       # Python dependencies
└── README.md              # Project description

🚀 How to Run the Project Locally
1. Clone the Repository
git clone https://github.com/7206582513/DogVsCatImageClassifier.git
cd DogVsCatImageClassifier

3. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

5. Install Dependencies
pip install -r requirements.txt

7. Start the Flask Server
python app.py

9. Open in Browser
Navigate to:
👉 http://127.0.0.1:5000/

Upload any cat or dog image and view the prediction!

🎯 Features
📂 Upload an image of a cat or dog

🧠 Pre-trained CNN model for classification

⚡ Real-time predictions

🎨 Bootstrap-based simple UI

📈 Image augmentation for better accuracy during training

🛠️ Model Information
CNN Architecture:

3 Convolutional layers + MaxPooling

Flatten + Dense layers

Output: 1 Neuron (Sigmoid activation)

Training dataset:

Microsoft Cat & Dog dataset (25,000 images)

Achieved validation accuracy: ~78%

📦 Requirements
Python 3.10+

Flask

TensorFlow 2.x

NumPy

Pillow

All dependencies are listed in requirements.txt.

📷 Sample Screenshots
<img width="887" alt="image" src="https://github.com/user-attachments/assets/9df80bd8-ec1d-4402-a44c-eb9367d240a8" />

Upload Page	Prediction Result
<img width="427" alt="image" src="https://github.com/user-attachments/assets/63fd5f0c-65ee-47f4-acf0-c39c42839d7e" />


🧹 Notes
Uploaded images are saved temporarily in static/uploads/.

.gitignore ensures large files like the model, training dataset, or uploads are not pushed to GitHub.

For larger deployment (like on Render, Railway, or HuggingFace Spaces), model loading optimization may be needed.

🤝 Contribution
Feel free to fork this repo and submit pull requests for:

UI improvements 🎨

Model retraining 🧠

API-based classification ⚡

📄 License
This project is licensed under the MIT License.
