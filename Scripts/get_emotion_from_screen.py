from fer import FER
import cv2
from pyautogui import screenshot
import csv
import numpy as np
import keyboard
from datetime import datetime

'''
The accuracy of facial emotion recognition using Python varies depending on the specific model and dataset used. Here are some reported accuracies:

1. A facial emotion recognition model integrating philosophy and machine learning theory achieved an accuracy of 72.16% on the FER2013 dataset[1][2].
2. Another study reported an accuracy of 36.36% on seven emotions for automatic facial expression recognition for masked faces[4].
3. A GitHub library for facial attribute analysis mentioned that human beings have 97.53% accuracy on facial recognition tasks[5].

It's important to note that achieving high accuracy in facial emotion recognition can be challenging due to factors such as variations in facial expressions, occlusions, and dataset quality. Therefore, while some models may achieve high accuracy on specific datasets, generalizing high accuracy across all scenarios remains a complex task.

Citations:
[1] https://www.frontiersin.org/articles/10.3389/fpsyg.2021.759485
[2] https://www.projectpro.io/article/facial-emotion-recognition-project-using-cnn-with-source-code/570
[3] https://stackoverflow.com/questions/62643515/facial-expression-recognition-accuracy
[4] https://link.springer.com/article/10.1007/s00521-023-08498-w
[5] https://github.com/serengil/deepface
'''

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
        if len(emotions):
            count += 1
            print(f'{len(emotions)} faces detected, iteration number {count}')
            save_results(emotions)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

        






