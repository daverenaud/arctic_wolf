from flask import Flask, request
from flask_cors import cross_origin

from api.anagram_check_api.anagram_submission_api import AnagramSubmissionApi
from api.top_anagrams_api.top_anagrams_api import TopAnagramsApi
from request.request_handler import RequestHandler


def set_routes(app: Flask) -> None:

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/anagram', methods=['POST'])
    @cross_origin(methods=['POST'])
    def check_anagram():
        return RequestHandler.handle_request(AnagramSubmissionApi, request)

    @app.route('/anagram/top', methods=['GET'])
    @cross_origin(methods=['GET'])
    def top_anagrams():
        return RequestHandler.handle_request(TopAnagramsApi, request)
