import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import numpy as np
import pickle
import tensorflow as tf
from flask import Flask, request, render_template
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

app = Flask(__name__)
print("Loading tokenizer...")
try:
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    print("Tokenizer loaded!")
except FileNotFoundError:
    print("ERROR: tokenizer.pkl not found. Please make sure it is in the same folder.")

print("Loading Keras model...")
try:
    model = load_model("Fake_job_detection.h5") 
    print("Keras model loaded!")
except OSError:
    print("ERROR: 'Fake_job_detection.h5' not found. Check the filename.")

MAX_SEQUENCE_LENGTH = 200

def preprocess_text(text):
    sequence = tokenizer.texts_to_sequences([text])
    return pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH, dtype="float32")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    combined_text = request.form.get("combined_text")

    if not combined_text:
        return render_template("index.html", prediction="Please enter the job description.")

    input_data = preprocess_text(combined_text)

    prediction = model.predict(input_data)[0][0]
    
    result = "Fraudulent" if prediction > 0.7 else "Legitimate"

    return render_template("index.html", prediction=f"The job post is {result}")

if __name__ == "__main__":
    app.run(debug=True)