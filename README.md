
SceneMood - NLP-Powered Mood Detection App

🧠💬 "Describe a scene... and let AI read the mood!"

Project Overview:
SceneMood is a smart and stylish desktop application that uses Natural Language Processing (NLP) and Machine Learning to detect emotions from text-based scene descriptions.
Type your experience — whether joyful, anxious, peaceful, or melancholic — and let the app reveal the underlying mood with emojis and elegant design.

Features:
- Simple & Beautiful PyQt5 GUI
- Custom-trained ML model using real datasets
- Flask API integration for smart backend prediction
- Light theme, emoji-rich output, smooth user experience

Example Input:
- "Finally I am done with my semester projects!" → 😊 relieved

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
- GoEmotions Dataset (https://huggingface.co/datasets/go_emotions)

The ML model is trained using TF-IDF + Logistic Regression.

Future Ideas:
- Add voice input
- Multilingual support
- Save mood journal
- Use LSTM or BERT for more accurate results


License:
This project is licensed under the MIT License — feel free to use, modify, and share!

![image](https://github.com/user-attachments/assets/85719bca-f196-4464-854c-61b7a9945bc9)
![image](https://github.com/user-attachments/assets/85719bca-f196-4464-854c-61b7a9945bc9)


![image](https://github.com/user-attachments/assets/5143e446-9235-40be-b370-9d1a9501ac1b)
![image](https://github.com/user-attachments/assets/5143e446-9235-40be-b370-9d1a9501ac1b)


![image](https://github.com/user-attachments/assets/86c095c1-66a2-4ca0-a90f-d30a695cbf23)
![image](https://github.com/user-attachments/assets/86c095c1-66a2-4ca0-a90f-d30a695cbf23)


![image](https://github.com/user-attachments/assets/e36a4dbd-1975-4b64-977a-4042a4c4e9f5)
![image](https://github.com/user-attachments/assets/e36a4dbd-1975-4b64-977a-4042a4c4e9f5)



