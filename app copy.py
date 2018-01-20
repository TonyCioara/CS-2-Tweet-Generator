import os
from flask import Flask
from markov_chain2 import MarkovChain
app = Flask(__name__)


def main():
    """Create sentence to display on website"""
    word_num = 30
    text_file = 'dracula.txt'
    markov_chain = MarkovChain(text_file)
    sentence = markov_chain.create_sentence(word_num)
    return sentence


@app.route('/')
def add_sentence():
    sentence = main()
    return sentence


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
