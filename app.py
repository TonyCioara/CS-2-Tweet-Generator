import os
from flask import Flask
from stochastic import Stochastic
app = Flask(__name__)


def main():
    word_num = 30
    data_list = Stochastic.create_data()
    histogram = Stochastic.create_histogram(data_list)
    sentence = Stochastic.create_sentence(word_num, histogram)
    return sentence


@app.route('/')
def add_sentence():
    sentence = main()
    return sentence


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(host='0.0.0.0', port=port, debug=True)
