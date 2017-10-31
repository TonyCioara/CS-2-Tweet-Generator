import re
import sys
import time


def create_data():
    """Takes no parameters.
    Returns a list of all words in the file"""
    with open('dracula.txt') as words_file:
        raw_data = words_file.read()
        raw_data = re.sub('[^0-9a-zA-Z]+', ' ', raw_data)
        raw_data = raw_data.replace('\n', '')
        raw_data = raw_data.lower()
        data_list = raw_data.split(" ")
        return data_list


def histogram_dict(data_list):
    """Takes in list of words.
    Returns dictionary of words and frequency"""
    final_data_dict = {}
    get = final_data_dict.get
    for word in data_list:
        final_data_dict[word] = get(word, 0) + 1
    return final_data_dict


def unique_words(histogram):
    """Takes in dict histogram.
    Returns number of unique words"""
    return len(histogram)


def dict_frequency(word, histogram):
    """Takes in a word and a histogram as dict.
    Returns the word count for that word"""
    if word in histogram:
        return histogram[word]
    else:
        return 0


def list_frequency(word, histogram):
    """Takes in a word and a histogram as list.
    Returns the word count for that word"""
    for index in histogram:
        if index[0] == word:
            return index[1]
    return 0


def histogram_list(data_list):
    """Takes in list of words.
    Returns list of lists, containing words and frequency"""
    final_data_list = []
    for word in data_list:
        to_create = True
        for sub_list in final_data_list:
            if sub_list[0] == word:
                to_create = False
                sub_list[1] += 1
                break
        if to_create is True:
            sub_list = [word, 1]
            final_data_list.append(sub_list)
    return(final_data_list)


if __name__ == "__main__":
    current_input = sys.argv[1]
    input_word = sys.argv[2]
    initial_time = time.time()
    if current_input == "dict":
        data_list = create_data()
        histogram_dict = histogram_dict(data_list)
        print(histogram_dict)
        print("Unique words:", unique_words(histogram_dict))
        print(input_word, ":", dict_frequency(input_word, histogram_dict))
    elif current_input == "list":
        data_list = create_data()
        histogram_list = histogram_list(data_list)
        print(histogram_list)
        print("Unique words:", unique_words(histogram_list))
        print(input_word, ":", list_frequency(input_word, histogram_list))
    final_time = time.time()
    run_time = final_time - initial_time
    print("Run time =", run_time)
