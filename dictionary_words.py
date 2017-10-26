import sys
import random


def dictionary_words():
    # Get words from file
    with open('/usr/share/dict/words') as f:
        raw_data = f.readlines()
        raw_data_list = list(raw_data)
        words_array = []
        for index in raw_data_list:
            words_array.append(index.replace('\n', ''))
    return words_array


def create_sentence(words_array, word_number):
    # Create random sentence
    sentence = ""
    for index in range(0, word_number):
        rand_num = random.randint(0, len(words_array) - 1)
        sentence += words_array[rand_num] + " "
        words_array.pop(rand_num)
    return sentence


if __name__ == "__main__":
    current_input = sys.argv
    words_array = dictionary_words()
    sentence = create_sentence(words_array, int(current_input[1]))
    print(sentence)
