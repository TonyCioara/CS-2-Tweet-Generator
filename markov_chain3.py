from dictogram import Dictogram
import re
import sys
import time
import random


def main():
    word_num = int(sys.argv[1])
    text_file = 'washington.txt'
    markov_chain = MarkovChain(text_file)
    #print(markov_chain.markov_chain)
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
        word = None
        middle_word = None
        for index in range(0, len(data_list) - 1):
            touple_key = None
            last_word = middle_word
            middle_word = word
            word = data_list[index]
            if word == 'START' or word == 'STOP':
                touple_key = word
            else:
                if last_word is None:
                    touple_key = (middle_word, word)
                else:
                    touple_key = (last_word, middle_word, word)
                print(touple_key)
            if touple_key is None:
                pass
            else:
                if touple_key not in markov_chain:
                    markov_chain[touple_key] = Dictogram()
                markov_chain[touple_key].add_count(data_list[index + 1])
        return markov_chain

    def create_sentence(self, word_num):
        """Takes in number of words in sentence, and histogram.
        Returns sentence."""

        sentence = []
        word = 'START'
        last_word = None
        middle_word = None

        for index in range(0, word_num):
            if middle_word is None:
                stochastic_key = word
            elif last_word is None:
                stochastic_key = (middle_word, word)
            else:
                stochastic_key = (last_word, middle_word, word)
            new_word = self.stochastic(stochastic_key)
            last_word = middle_word
            middle_word = word
            word = new_word
            if word == 'STOP':
                sentence.append(".")
                return " ".join(sentence)
            sentence.append(word)
        if len(sentence) >= word_num - 3:
            return self.create_sentence(word_num)
        else:
            sentence.append(".")
            return " ".join(sentence)
        # return sentence

    def stochastic(self, last_key):
        """If last word is passed in get word based on the last word.
        If last word is none, get random word"""

        print(last_key, " ", self.markov_chain[last_key].tokens)
        index = random.randint(1, self.markov_chain[last_key].tokens)
        for word in self.markov_chain[last_key]:
            frequency = self.markov_chain[last_key].frequency(word)
            if index > frequency:
                index -= frequency
            else:
                return word


if __name__ == "__main__":
    main()
