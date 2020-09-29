from typing import Any

from flask import Request, Response

from api.base_api import BaseApi


class ApiThrowingUnknownException(BaseApi):

    def process_request(self, request: Request, **kwargs: Any) -> Response:
        raise EnvironmentError()
