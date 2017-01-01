from flask import Flask, jsonify
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
    return jsonify(users=[u.serialize for u in users])


@app.route('/api/v1/users', methods=['POST'])
def addUser():
    user = JSONHelper.parseJSONToObject(User, request.data)
    user.hash_password(user.password_hash)
    user_inserted = DatabaseService.addUser(user)
    return jsonify(user=user_inserted.serialize)


@app.route('/api/v1/users/<int:id>', methods=['PUT'])
def updateUser(id):
    user = JSONHelper.parseJSONToObject(User, request.data)
    DatabaseService.updateUser(id, user)
    return 'User %d updated' % id


@app.route('/api/v1/users/<int:id>')
def getUser(id):
    user = DatabaseService.getUser(id)
    return jsonify(user=user.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
