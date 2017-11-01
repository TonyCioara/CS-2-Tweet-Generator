import re
import sys
import time


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


def histogram_dict(data_list):
    """Takes in list of words.
    Returns dictionary of words and frequency"""
    final_data_dict = {}
    get = final_data_dict.get
    for word in data_list:
        final_data_dict[word] = get(word, 0) + 1
    return final_data_dict


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


def main(current_input):
    """Run all funtions"""
    if len(current_input) < 3:
        print("Invalid input")
    else:
        func_type = current_input[1]
        input_word = current_input[2]

        initial_time = time.time()

        if func_type == "dict":
            data_list = create_data()
            hist_dict = histogram_dict(data_list)
            print(hist_dict)
            print("Unique words:", unique_words(hist_dict))
            print(input_word, ":", dict_frequency(input_word, hist_dict))

        elif func_type == "list":
            data_list = create_data()
            hist_list = histogram_list(data_list)
            print(hist_list)
            print("Unique words:", unique_words(hist_list))
            print(input_word, ":", list_frequency(input_word, hist_list))

        else:
            print("Input not valid")

        final_time = time.time()
        run_time = final_time - initial_time
        print("Run time =", run_time)


if __name__ == "__main__":
    """Pass in inputs. Run main function."""
    current_input = sys.argv
    main(current_input)

"""Count total number of words.
Create rand_num from 0 to total words.
For each member of the histogram, subtract number from rand_num.
If 0 Add word to sentence."""
