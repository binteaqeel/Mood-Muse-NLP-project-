
SceneMood - NLP-Powered Mood Detection App

🧠💬 "Describe a scene... and let AI read the mood!"

Project Overview:
SceneMood is a smart and stylish desktop application that uses Natural Language Processing (NLP) and Machine Learning to detect emotions from text-based scene descriptions.
Type your experience — whether joyful, anxious, peaceful, or melancholic — and let the app reveal the underlying mood with emojis and elegant design.

Features:
- Simple & Beautiful PyQt5 GUI
- Custom-trained ML model using real datasets
- Flask API integration for smart backend prediction
- Cheatcode support (e.g. "I scored the winning run!" → 😊 Joyfully Rejoicing)
- Light theme, emoji-rich output, smooth user experience
- Offline support – no external emotion APIs

Example Inputs:
- "We won the university cricket match and I scored the winning run!" → 😊 Joyfully Rejoicing
- "My best friend moved abroad today, and I already miss her." → 😢 Sad
- "I'm lying on the rooftop after Fajr, watching the sky slowly turn blue." → 🌿 Calm
- "I have my final viva tomorrow, and I can’t sleep properly." → 😰 Anxious

Tech Stack:
Frontend: PyQt5 (Desktop GUI)
Backend: Flask REST API
ML/NLP: Scikit-learn + TF-IDF + Custom Model
Dataset: emotion-balanced or GoEmotions (from HuggingFace Datasets)

Installation:
1. Clone the repository: git clone https://github.com/your-username/SceneMood.git
2. Navigate to project folder: cd SceneMood
3. Install requirements: pip install -r requirements.txt

Run the Flask API:
cd backend
python app.py

Run the GUI:
cd gui
python app.py

Folder Structure:
- backend/: Flask API and ML model
- gui/: PyQt5 GUI files
- data/: Optional dataset & training scripts
- requirements.txt: List of dependencies

Dataset:
You can use either:
- emotion-balanced (https://huggingface.co/datasets/AdamCodd/emotion-balanced)
- GoEmotions Dataset (https://huggingface.co/datasets/go_emotions)

The ML model is trained using TF-IDF + Logistic Regression.

Future Ideas:
- Add voice input
- Multilingual support
- Save mood journal
- Use LSTM or BERT for more accurate results

Author:
Made with love by [Your Name]
LinkedIn: https://www.linkedin.com/in/your-profile

License:
This project is licensed under the MIT License — feel free to use, modify, and share!
