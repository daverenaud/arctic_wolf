import json
from typing import Any

from flask import Request, Response
from werkzeug.exceptions import BadRequest

from api.base_api import BaseApi
from dal.anagram_submissions_database import AnagramSubmissionsDatabase
from lib.anagram import are_anagrams


class AnagramSubmissionApi(BaseApi):

    def __init__(self, anagram_submissions_database: AnagramSubmissionsDatabase):
        super().__init__(anagram_submissions_database)

    def process_request(self, request: Request, **kwargs: Any) -> Response:
        self._validate_request(request)
        words = request.get_json()['words']
        words_are_anagrams = are_anagrams(*words)

        if words_are_anagrams:
            self._anagram_submissions_database.record_anagram_submission(words)

        return Response(status=200,
                        content_type='application/json',
                        response=self._format_output(words_are_anagrams))

    @classmethod
    def _validate_request(cls, request: Request) -> None:
        """
        Checks that all required parameters have been passed to the API

        :param request: The request which was received
        :raises BadRequest: When there is a problem with the parameters which have been passed.
        """
        request_parameters = request.get_json(silent=True)

        if request_parameters is None:
            raise BadRequest('request body is not valid JSON')

        if not isinstance(request_parameters, dict):
            raise BadRequest('request body must be a JSON object')

        if 'words' not in request_parameters:
            raise BadRequest('"words" must be present in the request')

        if not isinstance(request_parameters['words'], list):
            raise BadRequest('"words" must be a JSON array')

        if any(not isinstance(word, str) for word in request_parameters['words']):
            raise BadRequest('"words" must only contain JSON strings')

    @classmethod
    def _format_output(cls, words_are_anagrams: bool) -> str:
        return json.dumps({
            'words_are_anagrams': words_are_anagrams
        })

