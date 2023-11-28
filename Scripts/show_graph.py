import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from datetime import datetime
import csv


def main():
    #get_emotion_mean()
    data = pd.read_csv('data_average.csv')
    unic_line_graph(data)
    
   
def unic_line_graph(data):

    emotions = data['emotion'].unique()
    times = set(data['datetime'].unique())
    
    for emotion in emotions:
        
        emotion_data = data[data['emotion'] == emotion].to_dict()
        
        emotion_dic = {}
        print(emotion)
        for key in emotion_data['emotion'].keys():
            emotion_dic[emotion_data['datetime'][key]] = emotion_data['score'][key]
        for key in times:
            emotion_dic.setdefault(key, 0)
        
        emotion_dic_sorted = dict(sorted(emotion_dic.items(), key=lambda x: datetime.strptime(x[0], '%H:%M:%S')))
        emotion_times =  [datetime.strptime(cadena, "%H:%M:%S") for cadena in list(emotion_dic_sorted.keys())]
        emotion_scores = list(emotion_dic_sorted.values())

        plt.plot_date(emotion_times, emotion_scores, '-', label=emotion)

    plt.xlabel('Hora')
    plt.ylabel('Puntaje')
    plt.legend()
    plt.show()

def multilpes_line_graphs(data):
    emotions = data['emotion'].unique()
    times = set(data['datetime'].unique())
    emotion_times_all = []
    emotion_scores_all = []

    for emotion in emotions:
        
        emotion_data = data[data['emotion'] == emotion].to_dict()
        
        
        emotion_dic = {}

        for key in emotion_data['emotion'].keys():
            emotion_dic[emotion_data['datetime'][key].strftime("%H:%M:%S")] = emotion_data['score'][key]
        for key in times:
            emotion_dic.setdefault(key.strftime("%H:%M:%S"), 0)
        
        emotion_dic_sorted = dict(sorted(emotion_dic.items(), key=lambda x: datetime.strptime(x[0], '%H:%M:%S')))
        emotion_times =  [datetime.strptime(cadena, "%H:%M:%S") for cadena in list(emotion_dic_sorted.keys())]
        emotion_scores = list(emotion_dic_sorted.values())

        emotion_times_all.append(emotion_times)
        emotion_scores_all.append(emotion_scores)

    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(2, 3, sharex=True)
    fig.suptitle('Emociones')

    #happy



def get_emotion_mean():
    with open("data_average.csv", mode="w", newline='') as archivo_csv:
        data = pd.read_csv('data.csv')
        promedios = data.groupby(['emotion', 'datetime'])['score'].mean()

        campos = ["datetime", "emotion", "score"]

        escritor_csv = csv.DictWriter(archivo_csv, campos)
        escritor_csv.writeheader()
        rows = [{'datetime':key[1],'emotion': key[0], 'score': value} for key, value in promedios.to_dict().items()]
        escritor_csv.writerows(rows)

if __name__ == "__main__":
    main()

