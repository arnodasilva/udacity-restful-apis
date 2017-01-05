from flask import json, jsonify
from flask import make_response

from web_application_exception import WebApplicationException


class Helper():
    @staticmethod
    def createErrorResponse(error_message, description, status_code):
        error = WebApplicationException(error_message, description, status_code)
        response = make_response(jsonify(error=error.serialize), status_code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def createSuccessResponse(data, status_code):
        response = make_response(jsonify(data), status_code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def parseJSONToObject(className, data):
        try:
            return className(**json.loads(data))
        except TypeError as e:
            description = e.message[1:]
            raise WebApplicationException('Validation error', description, status_code=400)

    @staticmethod
    def validateConstraints(validatorName, request):
        inputs = validatorName(request)
        if not inputs.validate():
            raise WebApplicationException('Validation error', inputs.errors, status_code=400)
