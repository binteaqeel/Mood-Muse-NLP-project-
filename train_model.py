# train_model.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from datasets import load_dataset
from sklearn.model_selection import train_test_split

# Sample training data
ds = load_dataset("AdamCodd/emotion-balanced")  
texts = ds["train"]["text"]
labels = ds["train"]["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2)
scenes = [
    "We won the university cricket match and I scored the winning run!",
    "My best friend moved abroad today, and I already miss her so much.",
    "I'm lying on the rooftop after Fajr, watching the sky slowly turn blue.",
    "I have my final viva tomorrow, and I can’t focus or sleep properly.",
    "Just got a new puppy and I can't stop smiling!",
    "I failed my exam and feel terrible.",
    "I’m sitting at the beach listening to the waves.",
    "I feel restless about the upcoming job interview."
]

labels = ["happy", "sad", "calm", "anxious", "joyfully Rejoiced", "Delightful", "Pleased", "Guiltyy"]

# Vectorize and train
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(scenes)

model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
with open("mood_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")
