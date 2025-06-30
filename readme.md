# Transfer Learning–Based Classification of Poultry Diseases for Enhanced Health Management
## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Tech Stack](#tech-stack)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Screenshots](#screenshots)  
8. [How It Works](#how-it-works)  
9. [Contributing](#contributing)  



---

## Overview

**Poultry Detect** is a real-time deep learning–powered web app that helps detect poultry diseases using uploaded images. It classifies images into four categories:

- **Healthy**
- **Coccidiosis**
- **Newcastle Disease**
- **Salmonella**

This application is designed to assist farmers, students, and agricultural researchers in performing fast, on-farm diagnosis to reduce economic losses.

---

##  Features

- 🖼️ Upload an image of poultry or feces
- 🤖 Detects disease using a trained deep learning model
- 🧠 Built using a CNN and deployed via Flask
- ⚡ Lightweight and runs on local machines
- 📱 Clean and mobile-friendly UI (HTML + CSS)
- 📥 Displays result with uploaded image

---

##  Project Structure

```
poultry-detect/
├── app.py                    # Flask backend
├── poultry_disease_model.h5 # Trained CNN model
│
├── templates/               # Frontend (HTML)
│   ├── index.html
│   ├── prediction.html
│   └── result.html
│
├── static/
│   ├── style.css            # Custom CSS
│   └── uploads/             # Folder for uploaded images
│
├── README.md
└── requirements.txt         # Python dependencies
```

---

##  Tech Stack

| Layer       | Technology                |
|-------------|----------------------------|
| Backend     | Flask (Python)             |
| ML Framework| TensorFlow + Keras         |
| Frontend    | HTML, CSS (Playfair Font)  |
| Model Type  | CNN (Image Classification) |
| File Upload | Werkzeug                   |

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kalyan09122003/Transferring-learning-for-Classification-of-Poultry-Disease.git
cd poultry-detect
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

##  Usage

1. Run the Flask app:
```bash
python app.py
```

2. Open in browser:
```
http://127.0.0.1:5000
```

3. Upload your poultry image → Click Predict → View the result.

---

##  Screenshots

![WhatsApp Image 2025-06-30 at 21 20 57_e1881da0](https://github.com/user-attachments/assets/1e8ce607-6489-4725-a3ba-7457f4e3ebbb)

![WhatsApp Image 2025-06-30 at 21 20 57_4ff1820f](https://github.com/user-attachments/assets/3a5bb2a0-bf13-415b-8550-7b2beec9725f)


---


## How It Works

🏠 The Home Page introduces users to the Poultry Health Hub and provides a “Get Started” button.

📤 On the Prediction Page, users upload an image of the poultry or symptoms.

🧠 The model preprocesses the image (resizing, scaling) and predicts the disease using a trained CNN model (Transfer Learning).

✅ The result is displayed on a new page showing both the disease name and the uploaded image.


##  Contributing

Contributions are welcome!

1. Fork the project
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes
4. Push to your branch: `git push origin feature/your-feature`
5. Create a pull request

---



