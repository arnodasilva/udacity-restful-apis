from flask import json, jsonify
from flask import make_response

from web_application_exception import WebApplicationException


class Helper():
    @staticmethod
    def parseJSONToObject(className, data):
        try:
            return className(**json.loads(data))
        except TypeError as e:
            description = e.message[1:]
            raise WebApplicationException('Validation error', description, status_code=400)
