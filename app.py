from flask import Flask, jsonify
from flask import json
from flask import request

from database_service import DatabaseService
from json_helper import JSONHelper
from models import User

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


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
