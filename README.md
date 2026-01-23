# 🛡️ Fake Internship & Scam Job Detection System

### An AI-powered tool to protect students from fraudulent job postings.

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Framework](https://img.shields.io/badge/Framework-Flask-green) ![ML](https://img.shields.io/badge/Library-TensorFlow%20%2F%20Keras-orange) ![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Project Overview
In the current job market, scam job postings and fake internships are a growing threat, particularly for students and fresh graduates. These fraudulent listings often aim to steal personal data or demand money for "training" or "security deposits."

This project is a **Deep Learning-based Web Application** that analyzes job descriptions and predicts whether they are **Legitimate** or **Fraudulent**. It uses Natural Language Processing (NLP) techniques and a trained LSTM (Long Short-Term Memory) neural network to detect patterns common in scam listings.

## 🚀 Live Demo
You can test the application live here:
https://fake-internship-and-scam-job-detection.onrender.com/

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning:** TensorFlow, Keras
* **Data Processing:** NumPy, Pickle
* **Deployment:** Render / Gunicorn

## 📂 Project Structure
```bash
Fake-Internship-Scam-Detection/
│
├── app.py                   # Main Flask application
├── EDA_job_data.ipynb       # complete analysis of the data
├── fake_job_detection.h5    # Trained Keras Model (LSTM)
├── tokenizer.pkl            # Tokenizer for text preprocessing
├── requirements.txt         # List of dependencies
├── fake_job_postings.csv    # Data used for training the model
├── Procfile                 # Deployment configuration for Render
│
├── static/
│   └── style.css            # Styling for the web interface
│
└── templates/
    └── index.html           # Frontend user interface
```

### Model Architecture & Workflow


* Input: The user pastes a job description (Title, Company, Description, Requirements) into the web interface.

### Preprocessing:

* The text is cleaned and converted into a sequence of integers using a pre-fitted Tokenizer.

* The sequence is padded to a length of 200 to match the model's input layer.

### Inference:

* The processed data is fed into the loaded Keras (.h5) model.

* The model is trained on the EMSCAD and outputs a probability score between 0 and 1.

### Output:

* Score > 0.7: Classified as Fraudulent.

* Score <= 0.7: Classified as Legitimate.

### 💻 Local Installation & Setup
If you want to run this project locally on your machine, follow these steps:

# 1. Clone the Repository
```Bash
git clone hiteshjha24/Fake-internship-and-Scam-job-detection
```

# 2. Create a Virtual Environment (Recommended)
```Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
# 3. Install Dependencies
```Bash
pip install -r requirements.txt
```
# 4. Run the Application
```Bash
python app.py
```
# 5. Access the App
Open your web browser and navigate to: http://127.0.0.1:5000/

### 📸 Screenshots
<img width="1879" height="899" alt="image" src="https://github.com/user-attachments/assets/d01ec1b8-b91e-447b-8b7f-33d51e06d232" />


# 🔮 Future Scope
Chrome Extension: Integrate the model directly into job portals like LinkedIn or Internshala.

Explainable AI: Highlights specific words (e.g., "fast cash," "no experience") that triggered the fraud detection.

Real-time Scraping: Automatically fetch and verify latest job posts.

# 👤 Author
### Hitesh Jha

Role: B.Tech Student (AI & Data Science)

Institution: Dr. Akhilesh Das Gupta Institute of Professional Studies

Focus: Machine Learning, Data Science, and AI Projects

Disclaimer: This tool provides a prediction based on patterns found in training data. Always exercise your own judgment and due diligence before applying for jobs or sharing personal information.
