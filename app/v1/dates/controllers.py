from flask import request
from flask_restful import Resource

from app.v1.dates.models import Date
from app.v1.dates.validators import DateInputsValidator
from app.v1.utils.database_service import DatabaseService
from app.v1.utils.helper import Helper


class DateAPI(Resource):
    def get(self, id):
        date = DatabaseService.getDate(id)
        return Helper.createSuccessResponse(date.serialize, status_code=200)

    def put(self, id):
        Helper.validateConstraints(DateInputsValidator, request)

        if DatabaseService.getDate(id):
            date = Helper.parseJSONToObject(Date, request.data)
            date_updated = DatabaseService.updateDate(id, date)

            return Helper.createSuccessResponse(date_updated.serialize, status_code=202)

    def delete(self, id):
        if DatabaseService.getDate(id):
            DatabaseService.deleteDate(id)
            return Helper.createSuccessResponse("Date successfully deleted", status_code=202)


class DatesAPI(Resource):
    def get(self):
        dates = DatabaseService.getDates()
        return Helper.createSuccessResponse([d.serialize for d in dates], status_code=200)

    def post(self):
        Helper.validateConstraints(DateInputsValidator, request)

        date = Helper.parseJSONToObject(Date, request.data)
        date_inserted = DatabaseService.addDate(date)

        return Helper.createSuccessResponse(date_inserted.serialize, status_code=201)
