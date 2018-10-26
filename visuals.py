from dataframe import Data
from analysis import Analyse
from collections import defaultdict, OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import config

class Visuals:
    """Creates visual representation of analysed chats"""
    COLOR = 'red'
    man = config.config['MAN']
    woman = config.config['WOMAN']

    def __init__(self, analysed_data):
        self.analysed_data = analysed_data

    def messages_by_day(self):
        dayofweek = self.analysed_data.day_of_week()
        arr = np.arange(7)
        man_time, woman_time = [], []
        for each in dayofweek.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])
        
        p1 = plt.bar(arr, man_time)
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLOR)
        plt.xticks(np.arange(7) ,dayofweek.keys(), fontsize=7)
        plt.xlabel('Days of the Week', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.show()

    def messages_by_time(self):
        timeofday = self.analysed_data.time_of_day()
        arr = np.arange(24)
        man_time, woman_time = [], []
        for each in timeofday.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])

        p1 = plt.bar(arr, man_time)
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLOR)
        plt.xticks(np.arange(24) ,timeofday.keys(), fontsize=7)
        plt.xlabel('Hours of the Day', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.show()    

    def messages_by_month(self):
        month = self.analysed_data.messages_per_month()
        arr = np.arange(12)

        man_time, woman_time = [], []
        for each in month.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])

        p1 = plt.bar(arr, man_time)
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLOR)
        plt.xticks(arr, month.keys(), fontsize=7)
        plt.show()

    def messages_from_each(self):
        from_man = self.analysed_data.messages_from_each(self.man)
        from_woman = self.analysed_data.messages_from_each(self.woman)
        plt.pie([from_man, from_woman], labels=['boyfriend', 'girlfriend'], colors=['blue', 'red'])
        plt.show()

    def words_from_each(self):
        from_man = self.analysed_data.words_from_each(self.man)
        from_woman = self.analysed_data.words_from_each(self.woman)
        plt.pie([from_man, from_woman], labels=['boyfriend', 'girlfriend'], colors=['blue', 'red'])
        plt.show()


    def top_words(self):
        words = self.analysed_data.top_words()
        plt.bar(words.words, words.frequency, color=self.COLOR)
        plt.show()

if __name__ == '__main__':

    data = Data(config.config['FILE_NAME'])
    df = data.parse_file()

    analysed_data = Analyse(df)
    visualize = Visuals(analysed_data)
    # visualize.messages_by_day()
    # visualize.messages_by_time()
    # visualize.messages_from_each()
    # visualize.words_from_each()
    # visualize.top_words()
    visualize.messages_by_month()