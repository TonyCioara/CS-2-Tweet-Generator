from dictogram import Dictogram
import re
import sys
import time
import random


def main():
    word_num = int(sys.argv[1])
    text_file = 'dracula.txt'
    markov_chain = MarkovChain(text_file)
    # print(markov_chain.markov_chain)
    sentence = markov_chain.create_sentence(word_num)
    print(sentence)


class MarkovChain(object):

    def __init__(self, text_file):
        """Init stochastic object
        Takes in name of file"""
        self.text_file = text_file
        data_list = self.create_data()
        self.markov_chain = self.create_markov_chain(data_list)
        self.total_word_count = self.count_words()

    def count_words(self):
        """Count all the words in the histogram"""
        total_word_count = 0
        for key in self.markov_chain:
            total_word_count += self.markov_chain[key].tokens
        return total_word_count

    def create_data(self):
        """Takes no parameters.
        Returns a list of all words in the file"""
        with open(self.text_file) as words_file:
            raw_data = words_file.read()
            raw_data = raw_data.replace('\n', ' ')
            raw_data = raw_data.replace('. ', ' STOP START ')
            raw_data = raw_data.replace('? ', ' STOP START ')
            raw_data = raw_data.replace('! ', ' STOP START ')
            raw_data = re.sub('[^a-zA-Z]+', ' ', raw_data)
            data_list = raw_data.split(" ")
            return data_list

    def create_markov_chain(self, data_list):
        markov_chain = {}
        markov_chain['START'] = Dictogram()
        markov_chain['START'].add_count(data_list[0])
        for index in range(0, len(data_list) - 1):
            word = data_list[index]
            if word not in markov_chain:
                markov_chain[word] = Dictogram()
            markov_chain[word].add_count(data_list[index + 1])
        return markov_chain

    def create_sentence(self, word_num):
        """Takes in number of words in sentence, and histogram.
        Returns sentence."""

        sentence = []
        last_word = 'START'

        for index in range(0, word_num):
            word = self.stochastic(last_word)
            last_word = word
            if last_word == 'STOP':
                sentence.append(".")
                return " ".join(sentence)
            sentence.append(word)
        sentence.append(".")
        return " ".join(sentence)
        # return sentence

    def stochastic(self, last_word):
        """If last word is passed in get word based on the last word.
        If last word is none, get random word"""
        """if last_word is None:
            index = random.randint(1, self.total_word_count)
            for word in self.markov_chain:
                word_dict = self.markov_chain[word]
                frequency = word_dict.tokens
                if index > frequency:
                    index -= frequency
                else:
                    return word
        else:"""
        index = random.randint(1, self.markov_chain[last_word].tokens)
        for word in self.markov_chain[last_word]:
            frequency = self.markov_chain[last_word].frequency(word)
            if index > frequency:
                index -= frequency
            else:
                return word


if __name__ == "__main__":
    main()
