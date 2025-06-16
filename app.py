# app.py
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model & vectorizer
with open("mood_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict_mood():
    data = request.json
    text = data.get("scene", "")
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return jsonify({"mood": prediction})

if __name__ == "__main__":
    app.run(debug=True)
