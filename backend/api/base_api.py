from abc import ABC, abstractmethod
from typing import Any

from flask import Request, Response

from dal.anagram_submissions_database import AnagramSubmissionsDatabase


class BaseApi(ABC):

    def __init__(self, anagram_submissions_database: AnagramSubmissionsDatabase):
        self._anagram_submissions_database = anagram_submissions_database

    @abstractmethod
    def process_request(self, request: Request, **kwargs: Any) -> Response:
        """
        Processes the given request and generates a response

        :param request: The Flask request to process
        :param kwargs: Additional keyword arguments passed to the function
        :returns: The response generated for the given request
        :raises HTTPException: When there is a problem which prevents the request from completing successfully.
        """
        pass
