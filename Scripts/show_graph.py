import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from datetime import datetime
import csv


def main():
    #get_emotion_mean()
    data = pd.read_csv('data_average.csv')
    unic_line_graph(data)
    multilpes_line_graphs(data)
    
   
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

    plt.xlabel('time')
    plt.ylabel('score')
    plt.legend()
    plt.show()

def multilpes_line_graphs(data):
    emotions = data['emotion'].unique()
    times = set(data['datetime'].unique())
    emotion_times_all = {}
    emotion_scores_all = {}

    for emotion in emotions:
        
        emotion_data = data[data['emotion'] == emotion].to_dict()
        
        
        emotion_dic = {}

        for key in emotion_data['emotion'].keys():
            emotion_dic[emotion_data['datetime'][key]] = emotion_data['score'][key]
        for key in times:
            emotion_dic.setdefault(key, 0)
        
        emotion_dic_sorted = dict(sorted(emotion_dic.items(), key=lambda x: datetime.strptime(x[0], '%H:%M:%S')))
        emotion_times =  [datetime.strptime(cadena, "%H:%M:%S") for cadena in list(emotion_dic_sorted.keys())]
        emotion_scores = list(emotion_dic_sorted.values())

        emotion_times_all[emotion] = emotion_times
        emotion_scores_all[emotion] = emotion_scores
    

    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, _, _)) = plt.subplots(3, 3, sharex=True)
    fig.suptitle('Emociones')

    
    # angry
    emTimes = emotion_times_all.get('angry', None)
    if emTimes is not None:
        ax1.plot_date(emotion_times_all['angry'], emotion_scores_all['angry'], '-', color='red')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Score')
        ax1.legend(['Angry'])

    # fear
    emTimes = emotion_times_all.get('fear', None)
    if emTimes is not None:
        ax2.plot_date(emotion_times_all['fear'], emotion_scores_all['fear'], '-', color='purple')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Score')
        ax2.legend(['Fear'])

    # happy
    emTimes = emotion_times_all.get('happy', None)
    if emTimes is not None:
        ax3.plot_date(emotion_times_all['happy'], emotion_scores_all['happy'], '-', color='green')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Score')
        ax3.legend(['Happy'])


    # neutral
    emTimes = emotion_times_all.get('neutral', None)
    if emTimes is not None:
        ax4.plot_date(emotion_times_all['neutral'], emotion_scores_all['neutral'], '-', color='orange')
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Score')
        ax4.legend(['Neutral'])

    # sad
    emTimes = emotion_times_all.get('sad', None)
    if emTimes is not None:
        ax5.plot_date(emotion_times_all['sad'], emotion_scores_all['sad'], '-', color='blue')
        ax5.set_xlabel('Time')
        ax5.set_ylabel('Score')
        ax5.legend(['Sad'])

    # disgust
    emTimes = emotion_times_all.get('disgust', None)
    if emTimes is not None:
        ax6.plot_date(emotion_times_all['disgust'], emotion_scores_all['disgust'], '-', color='brown')
        ax6.set_xlabel('Time')
        ax6.set_ylabel('Score')
        ax6.legend(['Disgust'])


    # surprise
    emTimes = emotion_times_all.get('surprise', None)
    if emTimes is not None:
        ax7.plot_date(emotion_times_all['surprise'], emotion_scores_all['surprise'], '-', color='yellow')
        ax7.set_xlabel('Time')
        ax7.set_ylabel('Score')
        ax7.legend(['Surprise'])

    plt.show()

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

