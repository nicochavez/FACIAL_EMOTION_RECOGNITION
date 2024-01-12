import cv2
from fer import FER

def main():

    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return

    while True:
       
        ret, frame = cap.read()

        if not ret:
            print("Error al leer el fotograma.")
            break

        
        emotions = detector.detect_emotions(frame)
        
        
        if emotions:
            top_emotion= detector.top_emotion(frame)
            frame = draw_emotions(frame, emotions, top_emotion)
            
        
        cv2.imshow('Emotion Detection', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def draw_emotions(frame, emotions, top_emotion):
    for face in emotions:
        x, y, w, h = face['box']
        emotions_text = ', '.join([f"{emotion}: {value:.2f}" for emotion, value in face['emotions'].items()])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotions_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Top Emotion: {top_emotion}", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    return frame

if __name__ == "__main__":
    main()
