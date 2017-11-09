import sys
import random
import time


def dictionary_words():
    # Get words from file
    with open('/usr/share/dict/words') as words_file:
        raw_data = words_file.readlines()
        raw_data_list = list(raw_data)
        words_array = []
        for index in raw_data_list:
            words_array.append(index.replace('\n', ''))
    return words_array


# function purpose, params, return values
def create_sentence(words_array, word_number):
    # Create random sentence
    sentence = []
    for index in range(0, word_number):
        rand_num = random.randint(0, len(words_array) - 1)
        sentence.append(words_array[rand_num])
        # del words_array[rand_num]
    return " ".join(sentence)


if __name__ == "__main__":
    initial_time = time.time()
    current_input = sys.argv
    words_array = dictionary_words()
    sentence = create_sentence(words_array, int(current_input[1]))
    final_time = time.time()
    run_time = final_time - initial_time
    print(sentence)
    print(len(words_array))
    print("Ran in", run_time)
