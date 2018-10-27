from dataframe import Data
import pandas as pd
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
import config

class Analyse:
    """Analyse Chat"""
    def __init__(self, df):
        self.df = df
        
    ## CALL ALL FUNCTIONS FROM COLLECT
    def collect(self, lover=None):
        dictionary = {
        'Average Word Length': self.average_word_length(),
        'Average Character Length': self.average_character_length(),
        'Words from each': self.words_from_each(),
        'Messages from each': self.messages_from_each(),
        'Top Words': self.top_words(),
        'Time of Day': self.time_of_day(),
        'Day of Week': self.day_of_week(),
        'Messages per Month': self.messages_per_month()}
        return dictionary

    def average_word_length(self):
        self.df['words'] = self.df.message.apply(lambda x: len(x.split()))
        return {lover: self.df[self.df.sender == lover].words.mean().round(2) for lover in 
        (config.config['MAN'], config.config['WOMAN'])}

    def average_character_length(self, lover=None):
        self.df['characters'] = self.df.message.apply(len)
        # return self.df[self.df.sender == lover].characters.mean().round(2)
        return {lover: self.df[self.df.sender == lover].characters.mean().round(2) for lover in 
        (config.config['MAN'], config.config['WOMAN'])}

    def words_from_each(self):
        avg_length = self.average_word_length()
        from_each = self.messages_from_each()
        return {k: avg_length[k]*from_each[k] for k in (config.config['MAN'], config.config['WOMAN'])}

    def messages_from_each(self):
        return {lover: len(self.df[self.df.sender == lover]) for lover in (config.config['MAN'], config.config['WOMAN'])}

    def top_words(self):
        stop_words = set(stopwords.words('english'))
        custom_stop_words = ("i'm", "i’m", "i'll","i’ll", "<media", "omitted>", "it's","it’s", "that's")
        non_words = ['?', '*']

        words = ''
        words = [word.lower() for line in self.df.message.values for word in line.split() 
        if word.lower() not in stop_words and word.lower() not in custom_stop_words and word.lower() not in non_words]

        return pd.DataFrame(Counter(words).most_common(20), columns=['words', 'frequency'])

    def time_of_day(self):
        man, woman = config.config['MAN'], config.config['WOMAN']
        time = OrderedDict([(x,{man:0, woman:0}) for x in range(24)])
        for index, stamp in self.df.iterrows():
            time[stamp.timestamp.hour][stamp.sender] += 1
        return time

    def day_of_week(self):
        man, woman = config.config['MAN'], config.config['WOMAN']
        weekday = OrderedDict([('Monday',{man:0, woman:0}), ('Tuesday',{man:0, woman:0}), ('Wednesday',{man:0, woman:0}),
                ('Thursday',{man:0, woman:0}), ('Friday',{man:0, woman:0}), ('Saturday',{man:0, woman:0}), ('Sunday',{man:0, woman:0})])
        
        for index, stamp in self.df.iterrows():
            weekday[stamp.timestamp.day_name()][stamp.sender] += 1
        return weekday

    def messages_per_month(self):
        man, woman = config.config['MAN'], config.config['WOMAN']
        month = OrderedDict([("January",{man:0, woman:0}),("February",{man:0, woman:0}),("March",{man:0, woman:0}),
            ("April",{man:0, woman:0}),("May",{man:0, woman:0}),("June",{man:0, woman:0}),("July",{man:0, woman:0}),
            ("August",{man:0, woman:0}),("September",{man:0, woman:0}),("October",{man:0, woman:0}),
            ("November",{man:0, woman:0}), ("December",{man:0, woman:0})])

        for index, stamp in self.df.iterrows():
            month[stamp.timestamp.month_name()][stamp.sender] += 1
        return month

if __name__ == '__main__':
    data = Data(config.config['FILE_NAME'])
    df = data.parse_file()
    analysed_data = Analyse(df)

    print(analysed_data.words_from_each())
    # print(analysed_data.messages_from_each())
    # print(analysed_data.average_character_length())