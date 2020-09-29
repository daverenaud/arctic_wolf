import json
from unittest import TestCase

from flask import Flask
from werkzeug.exceptions import BadRequest

from api.anagram_check_api.anagram_submission_api import AnagramSubmissionApi
from dal.anagram_submissions_database import AnagramSubmissionsDatabase


class AnagramSubmissionApiTests(TestCase):

    def test_returns_false_when_words_are_not_anagrams(self):
        request_body = {
            'words': ['wolf', 'owl']
        }
        with Flask(__name__).test_request_context(json=request_body) as request_context:
            response = AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertFalse(response_body['words_are_anagrams'])

    def test_returns_false_when_not_all_words_are_anagrams(self):
        request_body = {
            'words': ['wolf', 'flow', 'owl']
        }
        with Flask(__name__).test_request_context(json=request_body) as request_context:
            response = AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertFalse(response_body['words_are_anagrams'])

    def test_returns_true_when_all_words_are_anagrams(self):
        request_body = {
            'words': ['wolf', 'flow']
        }
        with Flask(__name__).test_request_context(json=request_body) as request_context:
            response = AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertTrue(response_body['words_are_anagrams'])

    def test_returns_true_when_only_one_word_is_submitted(self):
        request_body = {
            'words': ['wolf']
        }
        with Flask(__name__).test_request_context(json=request_body) as request_context:
            response = AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertTrue(response_body['words_are_anagrams'])

    def test_returns_true_when_no_words_are_submitted(self):
        request_body = {
            'words': []
        }
        with Flask(__name__).test_request_context(json=request_body) as request_context:
            response = AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)
            response_body = json.loads(response.data)
            self.assertTrue(response_body['words_are_anagrams'])

    def test_raises_bad_request_when_request_body_is_not_json(self):
        request_body = 'This is not valid JSON'
        with Flask(__name__).test_request_context(data=request_body) as request_context, self.assertRaises(BadRequest):
            AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)

    def test_raises_bad_request_when_request_body_does_not_contain_words_key(self):
        request_body = {'not_words': ['wolf', 'owl']}
        with Flask(__name__).test_request_context(data=request_body) as request_context, self.assertRaises(BadRequest):
            AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)

    def test_raises_bad_request_when_words_is_not_a_json_array(self):
        request_body = {'words': {'wolf': None, 'owl': None}}
        with Flask(__name__).test_request_context(data=request_body) as request_context, self.assertRaises(BadRequest):
            AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)

    def test_raises_bad_request_when_words_contains_non_string_values(self):
        request_body = {'words': ['wolf', 'owl', None]}
        with Flask(__name__).test_request_context(data=request_body) as request_context, self.assertRaises(BadRequest):
            AnagramSubmissionApi(AnagramSubmissionsDatabase.get_instance()).process_request(request_context.request)


