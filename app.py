from flask import Flask
from flask import json
from flask import request

from database_service import DatabaseService
from date_inputs_validator import DateInputsValidator
from helper import Helper
from models import User, Request, Proposal, Date
from proposal_inputs_validator import ProposalInputsValidator
from request_inputs_validator import RequestInputsValidator
from user_inputs_validator import UserInputsValidator
from web_application_exception import WebApplicationException

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


@app.errorhandler(WebApplicationException)
def web_application_exception_mapper(error):
    return Helper.createErrorResponse(error.message, error.description, status_code=error.code)


@app.route('/api/v1/users')
def getUsers():
    users = DatabaseService.getUsers()
    return Helper.createSuccessResponse([u.serialize for u in users], status_code=200)


@app.route('/api/v1/users', methods=['POST'])
def addUser():
    Helper.validateConstraints(UserInputsValidator, request)

    user = Helper.parseJSONToObject(User, request.data)
    user.hash_password(user.password_hash)
    user_inserted = DatabaseService.addUser(user)

    return Helper.createSuccessResponse(user_inserted.serialize, status_code=201)


@app.route('/api/v1/users/<int:id>', methods=['PUT'])
def updateUser(id):
    Helper.validateConstraints(UserInputsValidator, request)

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


@app.route('/api/v1/requests')
def getRequests():
    requests = DatabaseService.getRequests()
    return Helper.createSuccessResponse([r.serialize for r in requests], status_code=200)


@app.route('/api/v1/requests', methods=['POST'])
def addRequest():
    Helper.validateConstraints(RequestInputsValidator, request)

    user_request = Helper.parseJSONToObject(Request, request.data)
    request_inserted = DatabaseService.addRequest(user_request)

    return Helper.createSuccessResponse(request_inserted.serialize, status_code=201)


@app.route('/api/v1/requests/<int:id>', methods=['PUT'])
def updateRequest(id):
    Helper.validateConstraints(RequestInputsValidator, request)

    if DatabaseService.getRequest(id):
        user_request = Helper.parseJSONToObject(Request, request.data)
        request_updated = DatabaseService.updateRequest(id, user_request)

        return Helper.createSuccessResponse(request_updated.serialize, status_code=202)


@app.route('/api/v1/requests/<int:id>')
def getRequest(id):
    user_request = DatabaseService.getRequest(id)
    return Helper.createSuccessResponse(user_request.serialize, status_code=200)


@app.route('/api/v1/requests/<int:id>', methods=['DELETE'])
def deleteRequest(id):
    if DatabaseService.getRequest(id):
        DatabaseService.deleteRequest(id)
        return Helper.createSuccessResponse("Request successfully deleted")


@app.route('/api/v1/proposals')
def getProposals():
    proposals = DatabaseService.getProposals()
    return Helper.createSuccessResponse([p.serialize for p in proposals], status_code=200)


@app.route('/api/v1/proposals', methods=['POST'])
def addProposal():
    Helper.validateConstraints(ProposalInputsValidator, request)

    proposal = Helper.parseJSONToObject(Proposal, request.data)
    proposal_inserted = DatabaseService.addProposal(proposal)

    return Helper.createSuccessResponse(proposal_inserted.serialize, status_code=201)


@app.route('/api/v1/proposals/<int:id>', methods=['PUT'])
def updateProposal(id):
    Helper.validateConstraints(ProposalInputsValidator, request)

    if DatabaseService.getProposal(id):
        proposal = Helper.parseJSONToObject(Proposal, request.data)
        proposal_updated = DatabaseService.updateRequest(id, proposal)

        return Helper.createSuccessResponse(proposal_updated.serialize, status_code=202)


@app.route('/api/v1/proposals/<int:id>')
def getProposal(id):
    proposal = DatabaseService.getProposal(id)
    return Helper.createSuccessResponse(proposal.serialize, status_code=200)


@app.route('/api/v1/dates')
def getDates():
    dates = DatabaseService.getDates()
    return Helper.createSuccessResponse([d.serialize for d in dates], status_code=200)


@app.route('/api/v1/dates', methods=['POST'])
def addDate():
    Helper.validateConstraints(DateInputsValidator, request)

    date = Helper.parseJSONToObject(Date, request.data)
    date_inserted = DatabaseService.addDate(date)

    return Helper.createSuccessResponse(date_inserted.serialize, status_code=201)


@app.route('/api/v1/dates/<int:id>', methods=['PUT'])
def updateDate(id):
    Helper.validateConstraints(DateInputsValidator, request)

    if DatabaseService.getDate(id):
        date = Helper.parseJSONToObject(Date, request.data)
        date_updated = DatabaseService.updateDate(id, date)

        return Helper.createSuccessResponse(date_updated.serialize, status_code=202)


@app.route('/api/v1/dates/<int:id>')
def getDate(id):
    date = DatabaseService.getDate(id)
    return Helper.createSuccessResponse(date.serialize, status_code=200)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
