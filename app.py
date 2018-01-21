import json
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
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


@app.route('/Washington')
def quote_Washington():
    sentence = main('washington.txt')
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


@app.route('/Lincoln')
def quote_Lincoln():
    sentence = main('lincoln.txt')
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
