from flask import request
from flask_restful import Resource

from app.v1.proposals.models import Proposal
from app.v1.proposals.validators import ProposalInputsValidator
from app.v1.utils.database_service import DatabaseService
from app.v1.utils.helper import Helper


class ProposalAPI(Resource):
    def get(self, id):
        proposal = DatabaseService.getProposal(id)
        return Helper.createSuccessResponse(proposal.serialize, status_code=200)

    def put(self, id):
        Helper.validateConstraints(ProposalInputsValidator, request)

        if DatabaseService.getProposal(id):
            proposal = Helper.parseJSONToObject(Proposal, request.data)
            proposal_updated = DatabaseService.updateRequest(id, proposal)

            return Helper.createSuccessResponse(proposal_updated.serialize, status_code=202)

    def delete(self, id):
        if DatabaseService.getProposal(id):
            DatabaseService.deleteProposal(id)
            return Helper.createSuccessResponse("Proposal successfully deleted", status_code=202)


class ProposalsAPI(Resource):
    def get(self):
        proposals = DatabaseService.getProposals()
        return Helper.createSuccessResponse([p.serialize for p in proposals], status_code=200)

    def post(self):
        Helper.validateConstraints(ProposalInputsValidator, request)

        proposal = Helper.parseJSONToObject(Proposal, request.data)
        proposal_inserted = DatabaseService.addProposal(proposal)

        return Helper.createSuccessResponse(proposal_inserted.serialize, status_code=201)
