from flask import request
from flask_restful import Resource

from app.v1.requests.models import Request
from app.v1.requests.validators import RequestInputsValidator
from app.v1.utils.database_service import DatabaseService
from app.v1.utils.helper import Helper


class RequestAPI(Resource):
    def get(self, id):
        user_request = DatabaseService.getRequest(id)
        return Helper.createSuccessResponse(user_request.serialize, status_code=200)

    def put(self, id):
        Helper.validateConstraints(RequestInputsValidator, request)

        if DatabaseService.getRequest(id):
            user_request = Helper.parseJSONToObject(Request, request.data)
            request_updated = DatabaseService.updateRequest(id, user_request)

            return Helper.createSuccessResponse(request_updated.serialize, status_code=202)

    def delete(self, id):
        if DatabaseService.getRequest(id):
            DatabaseService.deleteRequest(id)
            return Helper.createSuccessResponse("Request successfully deleted", status_code=202)


class RequestsAPI(Resource):
    def get(self):
        requests = DatabaseService.getRequests()
        return Helper.createSuccessResponse([r.serialize for r in requests], status_code=200)

    def post(self):
        Helper.validateConstraints(RequestInputsValidator, request)

        user_request = Helper.parseJSONToObject(Request, request.data)
        request_inserted = DatabaseService.addRequest(user_request)

        return Helper.createSuccessResponse(request_inserted.serialize, status_code=201)
