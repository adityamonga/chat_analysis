from dataframe import Data
from analysis import Analyse
from collections import defaultdict, OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import config

class Visuals:
    """Creates visual representation of analysed chats"""
    # COLORS = ['#0D2149', '#C1292E'] # DARKER
    COLORS = ['#235789', '#F03A47'] # LIGHTER
    man = config.config['MAN']
    woman = config.config['WOMAN']

    def __init__(self, analysed_data):
        self.analysed_data = analysed_data
        self.dictionary = self.analysed_data.collect()

        ## REMAINING IN DICTIONARY
        # 'Average Word Length': self.average_word_length(),
        # 'Average Character Length': self.average_character_length()

    def messages_by_day(self):
        dayofweek = self.dictionary['Day of Week']
        arr = np.arange(7)
        man_time, woman_time = [], []
        for each in dayofweek.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])
        
        p1 = plt.bar(arr, man_time, color=self.COLORS[0])
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLORS[1])
        plt.xticks(np.arange(7) ,dayofweek.keys(), fontsize=7)
        plt.xlabel('Days of the Week', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.legend((p1[0], p2[0]), ('Boyfriend', 'Girlfriend'))
        # plt.savefig('report/messages_by_day.png', bbox_inches='tight')
        plt.show()

    def messages_by_time(self):
        timeofday = self.dictionary['Time of Day']
        arr = np.arange(24)
        man_time, woman_time = [], []
        for each in timeofday.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])

        p1 = plt.bar(arr, man_time, color=self.COLORS[0])
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLORS[1])
        plt.xticks(np.arange(24) ,timeofday.keys(), fontsize=7)
        plt.xlabel('Hours of the Day', fontsize=7)
        plt.ylabel('Number of Messages', fontsize=7)
        plt.legend((p1[0], p2[0]), ('Boyfriend', 'Girlfriend'))
        # plt.savefig('report/messages_by_time.png', bbox_inches='tight')
        plt.show()

    def messages_by_month(self):
        month = self.dictionary['Messages per Month']
        print('Feature Data Acquired.\nStarting plot')
        arr = np.arange(12)

        man_time, woman_time = [], []
        for each in month.values():
            man_time.append(each[self.man])
            woman_time.append(each[self.woman])

        p1 = plt.bar(arr, man_time, color=self.COLORS[0])
        p2 = plt.bar(arr, woman_time, bottom=man_time, color=self.COLORS[1])
        plt.xticks(arr, month.keys(), fontsize=7)
        plt.xlabel('Messages by Month', fontsize=7)
        plt.legend((p1[0], p2[0]), ('Boyfriend', 'Girlfriend'))
        # plt.savefig('report/messages_by_month.png', bbox_inches='tight')        
        plt.show()

    def messages_from_each(self):
        from_each = self.dictionary['Messages from each']
        from_man, from_woman = from_each[self.man], from_each[self.woman]
        plt.figure(figsize=(6,6))
        plt.pie([from_man, from_woman], labels=['Boyfriend', 'Girlfriend'],
            colors=self.COLORS, autopct=lambda p: '{:.2f}% ({:.0f})'.format(p,
                p*sum(from_each.values())/100))

        centre_circle = plt.Circle((0,0),0.75,color='black', fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.title('Messages Sent By Each Person')
        plt.legend()
        # plt.savefig('report/messages_from_each.png', bbox_inches='tight')
        plt.show()

    def words_from_each(self):
        from_each = self.dictionary['Words from each']
        from_man, from_woman = from_each[self.man], from_each[self.woman]
        plt.figure(figsize=(6,6))
        plt.pie([from_man, from_woman], labels=['Boyfriend', 'Girlfriend'],
            colors=self.COLORS, autopct=lambda p: '{:.2f}% ({:.0f})'.format(p, 
                p*sum(from_each.values())/100))

        centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=0.25)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        
        plt.title('Words Written By Each Person')
        plt.legend()
        # plt.savefig('report/words_from_each.png', bbox_inches='tight')
        plt.show()

    def top_words(self):
        words = self.dictionary['Top Words']
        plt.bar(words.words, words.frequency, color=self.COLORS[0])
        plt.title('Most Used Words')
        # plt.savefig('report/top_words.png', bbox_inches='tight')
        plt.show()

if __name__ == '__main__':

    data = Data(config.config['FILE_NAME'])
    df = data.parse_file()

    analysed_data = Analyse(df)
    visualize = Visuals(analysed_data)

    ## CALL FUNCTIONS TO GENERATE IMAGE
    # visualize.messages_by_day()
    # visualize.messages_by_time()
    # visualize.messages_by_month()
    # visualize.messages_from_each()
    # visualize.words_from_each()
    # visualize.top_words()
    # print(visualize.dictionary)