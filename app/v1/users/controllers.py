from flask import request
from flask_restful import Resource

from app.v1.utils.database.database_service import DatabaseService
from app.v1.utils.helpers.helper import Helper
from models import User
from validators import UserInputsValidator


class UserAPI(Resource):
    def get(self, id):
        user = DatabaseService.getUser(id)
        return Helper.createSuccessResponse(user.serialize, status_code=200)

    def put(self, id):
        Helper.validateConstraints(UserInputsValidator, request)

        if DatabaseService.getUser(id):
            user = Helper.parseJSONToObject(User, request.data)
            user_updated = DatabaseService.updateUser(id, user)

            return Helper.createSuccessResponse(user_updated.serialize, status_code=202)

    def delete(self, id):
        return Helper.createSuccessResponse("User %d successfully deleted" % id, status_code=202)


class UsersAPI(Resource):
    def get(self):
        users = DatabaseService.getUsers()
        return Helper.createSuccessResponse([u.serialize for u in users], status_code=200)

    def post(self):
        Helper.validateConstraints(UserInputsValidator, request)

        user = Helper.parseJSONToObject(User, request.data)
        user.hash_password(user.password_hash)
        user_inserted = DatabaseService.addUser(user)

        return Helper.createSuccessResponse(user_inserted.serialize, status_code=201)
