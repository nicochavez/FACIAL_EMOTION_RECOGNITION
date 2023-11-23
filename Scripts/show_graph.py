import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def main():

    data = pd.read_csv('data.csv')

    average_emotions = data.groupby('emotion')['score'].mean() * 100

    plt.barh(average_emotions.index, average_emotions, color=['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink'])


    #add labels and title
    plt.xlabel('Score (%)', fontweight='bold')
    plt.ylabel('Emotion', fontweight='bold')
    plt.title('Emotions detected', fontweight='bold')

    plt.gca().xaxis.set_major_locator(MultipleLocator(5))

    #Display the graph
    plt.show()

if __name__ == "__main__":
    main()

