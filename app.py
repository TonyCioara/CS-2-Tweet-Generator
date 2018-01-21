import os
from flask import Flask
from markov_chain2 import MarkovChain
app = Flask(__name__)


def main(text_file):
    """Create sentence to display on website"""
    word_num = 25
    markov_chain = MarkovChain(text_file)
    sentence = markov_chain.create_sentence(word_num)
    return sentence


@app.route('/')
def add_sentence():
    sentence = main()
    return sentence

@app.route('/FDR')
def quote_FDR():
    sentence = main('FDR.txt')
    return sentence

@app.route('/Washington')
def quote_Washington():
    sentence = main('washington.txt')
    return sentence

@app.route('/Lincoln')
def quote_Lincoln():
    sentence = main('lincoln.txt')
    return sentence


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
