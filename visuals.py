from dataframe import Data
from analysis import Analyse
from collections import defaultdict, OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Visuals:
    COLOR = 'red'
    """Creates visual representation of analysed chats"""
    def __init__(self, analysed_data):
        self.analysed_data = analysed_data

    def messages_by_day(self):
        dayofweek = analysed_data.day_of_week()
        print(dayofweek)
        plt.bar(dayofweek.keys(), dayofweek.values())
        plt.xticks(np.arange(7) ,dayofweek.keys(), fontsize=7)
        plt.xlabel('Days of the Week', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.show()

    def messages_by_time(self):
        timeofday = analysed_data.time_of_day()
        print(timeofday)
        plt.bar(timeofday.keys(), timeofday.values())
        plt.xticks(np.arange(24) ,timeofday.keys(), fontsize=7)
        plt.xlabel('Hours of the Day', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.show()    

    def messages_from_each(self):
        boyfriend = analysed_data.messages_from_each('Aditya Vikram Monga')
        girlfriend = analysed_data.messages_from_each('Anubhavi')
        plt.pie([boyfriend, girlfriend], labels=['boyfriend', 'girlfriend'])
        plt.show()

    def words_from_each(self):
        boyfriend = analysed_data.words_from_each('Aditya Vikram Monga')
        girlfriend = analysed_data.words_from_each('Anubhavi')
        plt.pie([boyfriend, girlfriend], labels=['boyfriend', 'girlfriend'])
        plt.show()

    def top_words(self):
        words = analysed_data.top_words()
        plt.bar(words.words, words.frequency, color=self.COLOR)
        plt.show()

if __name__ == '__main__':

    data = Data('WhatsApp Chat with Anubhavi.txt')
    df = data.parse_file()

    analysed_data = Analyse(df)
    visualize = Visuals(analysed_data)
    # visualize.messages_by_day()
    # visualize.messages_by_time()
    # visualize.messages_from_each()
    # visualize.words_from_each()
    visualize.top_words()