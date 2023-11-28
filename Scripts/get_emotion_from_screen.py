from fer import FER
import cv2
from pyautogui import screenshot
import csv
import numpy as np
import keyboard
from datetime import datetime

def get_emotions(img):
    #print('height: ', img.shape[0], 'width: ', img.shape[1])
    detector = FER(mtcnn=True)
    emotions = detector.detect_emotions(img)
    topEmotions = [(max(emotion['emotions'], key=emotion['emotions'].get), emotion['emotions'].get(max(emotion['emotions'], key=emotion['emotions'].get))) for emotion in emotions]
    return topEmotions

def save_results(results):
    with open("data.csv", mode="a", newline='') as archivo_csv:
        campos = ["datetime", "emotion", "score"]
        escritor_csv = csv.DictWriter(archivo_csv, campos)
        hora = datetime.now().strftime('%H:%M:%S') 
        rows = [{'datetime':hora,'emotion': re[0], 'score': re[1]} for re in results]
        escritor_csv.writerows(rows)
        print("Data loaded")

def main():
    count = 0
    while True:
        if keyboard.is_pressed('q'):
            break

        img = screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        emotions = get_emotions(frame)
        print(emotions)
        if len(emotions):
            count += 1
            print(f'{len(emotions)} faces detected, iteration number {count}')
            save_results(emotions)


if __name__ == "__main__":
    main()

        






