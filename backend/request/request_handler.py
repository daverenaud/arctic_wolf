import json
import sys
import traceback
from typing import Any, Type

from flask import Request, Response
from werkzeug.exceptions import HTTPException

from api.base_api import BaseApi
from dal.anagram_submissions_database import AnagramSubmissionsDatabase


class RequestHandler:

    @classmethod
    def handle_request(cls, api_class: Type[BaseApi], request: Request, **kwargs: Any) -> Response:
        try:
            print(request.data)
            response = api_class(AnagramSubmissionsDatabase.get_instance()).process_request(request, **kwargs)
            print(response.data)
            return response
        except HTTPException as e:
            print(e)
            return Response(status=e.code if e.code is not None else 500,
                            response=json.dumps({'error_message': e.description}),
                            content_type='application/json')
        except Exception as e:
            print(e)
            exc_type, exc_value, exc_tb = sys.exc_info()
            exception_details = traceback.format_exception(exc_type, exc_value, exc_tb)
            print(''.join(exception_details))
            return Response(status=500)
