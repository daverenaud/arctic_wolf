import json
from unittest import TestCase

from flask import Flask
from werkzeug.exceptions import NotFound

from request.request_handler import RequestHandler
from tests.request_handler_tests.api_throwing_http_exception import ApiThrowingHttpException
from tests.request_handler_tests.api_throwing_unknown_exception import ApiThrowingUnknownException


class RequestHandlerTests(TestCase):

    def test_returns_response_code_and_error_from_http_exception(self):
        with Flask(__name__).test_request_context() as request_context:
            response = RequestHandler.handle_request(ApiThrowingHttpException, request_context.request)
            response_body = json.loads(response.data)
            self.assertEqual(response.status_code, NotFound().code)
            self.assertEqual(response_body['error_message'], 'NotFound')

    def test_returns_500_with_no_body_for_unknown_exception(self):
        with Flask(__name__).test_request_context() as request_context:
            response = RequestHandler.handle_request(ApiThrowingUnknownException, request_context.request)
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.data, b'')

