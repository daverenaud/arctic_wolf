import json
from unittest import TestCase

from flask import Flask
from werkzeug.exceptions import BadRequest

from api.top_anagrams_api.top_anagrams_api import TopAnagramsApi
from tests.api_tests.top_anagrams_api_tests.anagram_submissions_database_mock import AnagramSubmissionsDatabaseMock


class TopAnagramsApiTests(TestCase):

    def test_returns_top_ten_submissions_when_max_results_not_present(self):
        with Flask(__name__).test_request_context() as request_context:
            response = TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertEqual(len(response_body['top_anagrams']), 10)

    def test_returns_submissions_in_order_of_count_with_higher_count_at_beginning(self):
        with Flask(__name__).test_request_context() as request_context:
            response = TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)
            response_body = json.loads(response.data)
            for i in range(len(response_body['top_anagrams']) - 1):
                self.assertGreaterEqual(response_body['top_anagrams'][i]['count'], response_body['top_anagrams'][i + 1]['count'])

    def test_returns_all_results_when_max_results_greater_than_total_submissions(self):
        with Flask(__name__).test_request_context('/?max_results=25') as request_context:
            response = TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertEqual(len(response_body['top_anagrams']), 15)

    def test_returns_no_more_than_max_results(self):
        with Flask(__name__).test_request_context('/?max_results=5') as request_context:
            response = TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertEqual(len(response_body['top_anagrams']), 5)

    def test_raises_bad_request_when_result_is_not_int(self):
        with Flask(__name__).test_request_context('/?max_results=c23') as request_context, self.assertRaises(BadRequest):
            TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)

    def test_raises_bad_request_when_result_is_zero(self):
        with Flask(__name__).test_request_context('/?max_results=0') as request_context, self.assertRaises(BadRequest):
            TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)

    def test_raises_bad_request_when_result_is_negative(self):
        with Flask(__name__).test_request_context('/?max_results=-1') as request_context, self.assertRaises(BadRequest):
            TopAnagramsApi(AnagramSubmissionsDatabaseMock()).process_request(request_context.request)
