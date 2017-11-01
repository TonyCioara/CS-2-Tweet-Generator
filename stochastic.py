import re
import sys
import time
import random


def create_data():
    """Takes no parameters.
    Returns a list of all words in the file"""
    with open('dracula.txt') as words_file:
        raw_data = words_file.read()
        raw_data = raw_data.lower()
        raw_data = raw_data.replace('\n', ' ')
        raw_data = re.sub('[^a-z]+', ' ', raw_data)
        data_list = raw_data.split(" ")
        return data_list


def create_histogram(data_list):
    """Takes in list of words.
    Returns dictionary of words and frequency"""
    histogram = {}
    get = histogram.get
    for word in data_list:
        histogram[word] = get(word, 0) + 1
    return histogram


def create_sentence(word_num, histogram):
    """Takes in number of words in sentence, and histogram.
    Returns sentence."""
    total_word_count = 0
    for key in histogram:
        total_word_count += histogram[key]

    sentence = []
    for index in range(0, word_num):
        word = stochastic(histogram, total_word_count)
        sentence.append(word)
    return " ".join(sentence)


def stochastic(histogram, total_word_count):
    """Takes in histogram and total word count.
    Returns random word based on probability"""
    rand_num = random.randint(0, total_word_count)

    for key in histogram:
        if rand_num - histogram[key] > 0:
            rand_num -= histogram[key]
        else:
            return key


if __name__ == "__main__":
    word_num = int(sys.argv[1])
    data_list = create_data()
    histogram = create_histogram(data_list)
    sentece = create_sentence(word_num, histogram)
    # sentece_histogram = create_histogram(list(sentece))
    # Comment out line above for testing purposes
    print(sentece)
