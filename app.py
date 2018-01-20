import os
from flask import Flask
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from markov_chain3 import MarkovChain
app = Flask(__name__)
api = Api(app)


class FDR(Resource):

    def get(self):
        word_num = 25
        text_file = 'FDR.txt'
        markov_chain = MarkovChain(text_file)
        sentence = markov_chain.create_sentence(word_num)
        return sentence


class Lincoln(Resource):

    def get(self):
        word_num = 25
        text_file = 'lincoln.txt'
        markov_chain = MarkovChain(text_file)
        sentence = markov_chain.create_sentence(word_num)
        return sentence


class Washington(Resource):

    def get(self):
        word_num = 25
        text_file = 'washington.txt'
        markov_chain = MarkovChain(text_file)
        sentence = markov_chain.create_sentence(word_num)
        return sentence


api.add_resource(Washington, '/Washington')
api.add_resource(Lincoln, '/Lincoln')
api.add_resource(FDR, '/FDR')


if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
