from typing import Any

from flask import Request, Response
from werkzeug.exceptions import NotFound

from api.base_api import BaseApi


class ApiThrowingHttpException(BaseApi):

    def process_request(self, request: Request, **kwargs: Any) -> Response:
        raise NotFound('NotFound')
