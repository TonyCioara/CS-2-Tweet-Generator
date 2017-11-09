from stochastic import Stochastic


def stochastic_test():
    test_stochastic = Stochastic('words_sample.txt')
    sentence = test_stochastic.create_sentence(10000)
    words_list = sentence.split(" ")
    sentence_histogram = test_stochastic.create_histogram(words_list)
    print(sentence_histogram)


if __name__ == "__main__":
    stochastic_test()
