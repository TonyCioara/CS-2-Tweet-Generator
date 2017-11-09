import re
import sys
import time
import random


class Stochastic(object):

    def __init__(self, text_file):
        """Init stochastic object
        Takes in name of file"""
        self.text_file = text_file
        data_list = self.create_data()
        self.histogram = self.create_histogram(data_list)
        self.total_word_count = self.count_words()

    def count_words(self):
        """Count all the words in the histogram"""
        total_word_count = 0
        for key in self.histogram:
            total_word_count += self.histogram[key]
        return total_word_count

    def create_data(self):
        """Takes no parameters.
        Returns a list of all words in the file"""
        with open(self.text_file) as words_file:
            raw_data = words_file.read()
            raw_data = raw_data.lower()
            raw_data = raw_data.replace('\n', ' ')
            raw_data = re.sub('[^a-z]+', ' ', raw_data)
            data_list = raw_data.split(" ")
            return data_list

    def create_histogram(self, data_list):
        """Takes in list of words.
        Returns dictionary of words and frequency"""
        histogram = {}
        get = histogram.get
        for word in data_list:
            histogram[word] = get(word, 0) + 1
        return histogram

    def create_sentence(self, word_num):
        """Takes in number of words in sentence, and histogram.
        Returns sentence."""

        sentence = []
        for index in range(0, word_num):
            word = self.stochastic()
            sentence.append(word)
        return " ".join(sentence)
        # return sentence

    def stochastic(self):
        """Takes in histogram and total word count.
        Returns random word based on probability"""
        index = random.randint(1, self.total_word_count)

        for word in self.histogram:
            frequency = self.histogram[word]
            if index > frequency:
                index -= frequency
            else:
                return word


if __name__ == "__main__":
    start_time = time.time()
    word_num = int(sys.argv[1])
    text_file = 'dracula.txt'
    dracula_stochastic = Stochastic('dracula.txt')
    sentence = dracula_stochastic.create_sentence(word_num)

    end_time = time.time()
    run_time = end_time - start_time
    # print(sentence_histogram)
    print(sentence)
    print("Run time:", run_time)
