# main_gui.py
import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

MOOD_EMOJIS = {
    "happy": "😊 Joyfully Rejoicing",
    "sad": "😢 Sad",
    "calm": "🌅 Calm",
    "anxious": "😰 Anxious"
}

class MoodApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌈 SceneMood - NLP Edition")
        self.setGeometry(300, 100, 700, 450)
        self.setStyleSheet("background-color: #e0f7fa;")
        self.initUI()

    def initUI(self):
        self.title = QLabel("📝 Describe a Scene Below:", self)
        self.title.setGeometry(50, 30, 600, 40)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arial", 18, QFont.Bold))

        self.input = QTextEdit(self)
        self.input.setPlaceholderText("E.g. We won the university cricket match...")
        self.input.setGeometry(100, 90, 500, 100)
        self.input.setStyleSheet("""
            background-color: white;
            font-size: 16px;
            border: 2px solid #4dd0e1;
            border-radius: 10px;
            padding: 10px;
        """)

        self.button = QPushButton("💡 Predict Mood", self)
        self.button.setGeometry(270, 210, 160, 40)
        self.button.setStyleSheet("""
            background-color: #4dd0e1;
            color: black;
            font-weight: bold;
            border-radius: 8px;
        """)
        self.button.clicked.connect(self.predict)

        self.result = QLabel("", self)
        self.result.setGeometry(100, 270, 500, 80)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setFont(QFont("Arial", 20))
        self.result.setStyleSheet("color: #006064;")

    def predict(self):
        scene = self.input.toPlainText().strip()
        if not scene:
            QMessageBox.warning(self, "Input Required", "Please type a scene first.")
            return

        try:
            response = requests.post("http://127.0.0.1:5000/predict", json={"scene": scene})
            mood = response.json().get("mood", "unknown")
            mood_display = MOOD_EMOJIS.get(mood, "🤔 Mood Unknown")
            self.result.setText(mood_display)
        except Exception as e:
            self.result.setText("🚫 Error contacting server")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodApp()
    window.show()
    sys.exit(app.exec_())
