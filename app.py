from flask import Flask
from flask import json
from flask import request

from database_service import DatabaseService
from helper import Helper
from models import User, Request
from request_inputs_validator import RequestInputsValidator
from web_application_exception import WebApplicationException

app = Flask(__name__)

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


@app.errorhandler(WebApplicationException)
def web_application_exception_mapper(error):
    return Helper.createErrorResponse(error.message, error.description, status_code=error.code)


@app.route('/api/v1/users')
def getUsers():
    users = DatabaseService.getUsers()
    return Helper.createSuccessResponse([u.serialize for u in users], status_code=200)


@app.route('/api/v1/users', methods=['POST'])
def addUser():
    user = Helper.parseJSONToObject(User, request.data)
    user.hash_password(user.password_hash)
    user_inserted = DatabaseService.addUser(user)
    return Helper.createSuccessResponse(user_inserted.serialize, status_code=201)


@app.route('/api/v1/users/<int:id>', methods=['PUT'])
def updateUser(id):
    if DatabaseService.getUser(id):
        user = Helper.parseJSONToObject(User, request.data)
        user_updated = DatabaseService.updateUser(id, user)
        return Helper.createSuccessResponse(user_updated.serialize, status_code=202)


@app.route('/api/v1/users/<int:id>')
def getUser(id):
    user = DatabaseService.getUser(id)
    return Helper.createSuccessResponse(user.serialize, status_code=200)


@app.route('/api/v1/users', methods=['DELETE'])
def deleteUser():
    return Helper.createSuccessResponse("User successfully deleted", status_code=202)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
