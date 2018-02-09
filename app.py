import json
from flask import Flask
from markov_chain3 import MarkovChain


app = Flask(__name__)
app.markov_chains = {}
app.markov_chains['FDR'] = MarkovChain('FDR.txt')
app.markov_chains['Lincoln'] = MarkovChain('lincoln.txt')
app.markov_chains['Washington'] = MarkovChain('washington.txt')


def main(text_file):
    """Create sentence to display on website"""
    word_num = 25
    markov_chain = MarkovChain(text_file)
    # --
    sentence = markov_chain.create_sentence(word_num)
    return sentence


@app.route('/')
def add_sentence():
    sentence = main()
    return sentence


@app.route('/FDR')
def quote_FDR():
    sentence = app.markov_chain['FDR'].create_sentence(25)
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


@app.route('/Washington')
def quote_Washington():
    sentence = app.markov_chain['Lincoln'].create_sentence(25)
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


@app.route('/Lincoln')
def quote_Lincoln():
    sentence = app.markov_chain['Washington'].create_sentence(25)
    data = {}
    data['sentence'] = sentence
    json_data = json.dumps(data)
    return json_data


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
