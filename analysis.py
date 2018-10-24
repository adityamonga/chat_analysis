from dataframe import Data
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords

class Analyse:
    """Analyse Chat"""
    def __init__(self, df):
        self.df = df
        
    def collect(self, lover=None):
        dictionary = {'Average Word Length': self.average_word_length(lover), 'Average Character Length': self.average_character_length(lover)}
        return dictionary

    def average_word_length(self, lover=None):
        self.df['words'] = self.df.message.apply(lambda x: len(x.split()))
        return self.df[self.df.sender == lover].words.mean().round(2)

    def average_character_length(self, lover=None):
        self.df['characters'] = self.df.message.apply(len)
        return self.df[self.df.sender == lover].characters.mean().round(2)

    def words_from_each(self, lover=None):
        return self.messages_from_each(lover) * self.average_word_length(lover)

    def messages_from_each(self, lover=None):
        return len(df[df.sender == lover])

    def top_words(self):
        stop_words = set(stopwords.words('english'))
        custom_stop_words = ("i'm", "i’m", "i'll","i’ll", "<media", "omitted>", "it's","it’s", "that's")
        non_words = ['?', '*']

        words = ''
        words = [word.lower() for line in self.df.message.values for word in line.split() 
        if word.lower() not in stop_words and word.lower() not in custom_stop_words and word.lower() not in non_words]

        return pd.DataFrame(Counter(words).most_common(25), columns=['words', 'frequency'])

    def test_prints(self):
        # average word length
        return self.average_word_length(), self.average_character_length()
        #average characters per message
        # return self.df.characters


if __name__ == '__main__':
    data = Data('WhatsApp Chat with Anubhavi.txt')
    df = data.parse_file()
    analysed_data = Analyse(df)
    print(analysed_data.collect('Aditya Vikram Monga'))
    print(analysed_data.collect('Anubhavi'))
    # print(analysed_data.top_words())
    print(analysed_data.words_from_each('Anubhavi'))
    print(analysed_data.words_from_each('Aditya Vikram Monga'))
    print(analysed_data.messages_from_each('Anubhavi'))