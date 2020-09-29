import json
from typing import Any, List, Tuple

from flask import Request, Response
from werkzeug.exceptions import BadRequest

from api.base_api import BaseApi
from dal.anagram_submissions_database import AnagramSubmissionsDatabase


class TopAnagramsApi(BaseApi):

    def __init__(self, anagram_submissions_database: AnagramSubmissionsDatabase):
        super().__init__(anagram_submissions_database)

    def process_request(self, request: Request, **kwargs: Any) -> Response:
        self._validate_request(request)
        top_anagrams = self._anagram_submissions_database.get_top_anagram_submissions(request.args.get('max_results', default=10, type=int))

        return Response(status=200, content_type='application/json', response=self._format_output(top_anagrams))

    @classmethod
    def _validate_request(cls, request: Request) -> None:
        """
        Checks that all required parameters have been passed to the API

        :param request: The request which was received
        :raises BadRequest: When there is a problem with the parameters which have been passed.
        """
        if 'max_results' in request.args:
            max_results = request.args.get('max_results', default=None, type=int)
            if max_results is None or max_results < 1:
                raise BadRequest('"max_results" must be an integer greater than 0')

    @classmethod
    def _format_output(cls, top_anagrams: List[Tuple[Tuple[str, ...], int]]) -> str:
        return json.dumps({
            'top_anagrams': [{
                'anagram': list(anagram),
                'count': count
            } for anagram, count in top_anagrams]
        })
