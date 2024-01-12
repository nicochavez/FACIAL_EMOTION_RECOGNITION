import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from fer import FER
import cv2

class EmotionWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()

        self.image_path = image_path
        self.initUI()

    def initUI(self):
        # Obtener emociones y la emoción superior
        img = cv2.imread(self.image_path)
        emotions, topEmotion = get_emotions(img)

        # Crear la ventana
        self.setWindowTitle('Emotion Detection')
        self.setGeometry(100, 100, 800, 600)

        # Mostrar la imagen
        self.label_image = QLabel(self)
        pixmap = QPixmap(self.image_path).scaled(800, 600)
        self.label_image.setPixmap(pixmap)

        self.label_emotions = QLabel(self)
        self.label_emotions.setText(f"{emotions}")
        self.label_top_emotion = QLabel(self)
        self.label_top_emotion.setText(f"Top Emotion: {topEmotion}")

        # Diseño de la ventana
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_image)
        layout.addWidget(self.label_emotions)
        layout.addWidget(self.label_top_emotion)

        self.show()

def get_emotions(img):
    detector = FER(mtcnn=True)
    emotions = detector.detect_emotions(img)
    topEmotion = detector.top_emotion(img)
    return emotions, topEmotion



def main():
    app = QApplication(sys.argv)
    path = './images/happy_boy.jpg'
    window = EmotionWindow(path)
    window.resize(800, 600)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
