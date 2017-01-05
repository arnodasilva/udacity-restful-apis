import flask_restful
from flask import Blueprint

from app.v1.dates.controllers import DatesAPI, DateAPI
from app.v1.proposals.controllers import ProposalsAPI, ProposalAPI
from app.v1.requests.controllers import RequestsAPI, RequestAPI
from app.v1.users.controllers import UserAPI, UsersAPI
from app.v1.utils.helper import Helper
from web_application_exception import WebApplicationException

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = flask_restful.Api(api_v1_bp)

api_v1.add_resource(UsersAPI, '/users')
api_v1.add_resource(UserAPI, '/users/<int:id>')
api_v1.add_resource(RequestsAPI, '/requests')
api_v1.add_resource(RequestAPI, '/requests/<int:id>')
api_v1.add_resource(ProposalsAPI, '/proposals')
api_v1.add_resource(ProposalAPI, '/proposals/<int:id>')
api_v1.add_resource(DatesAPI, '/dates')
api_v1.add_resource(DateAPI, '/dates/<int:id>')


@api_v1_bp.errorhandler(WebApplicationException)
def web_application_exception_mapper(error):
    return Helper.createErrorResponse(error.message, error.description, status_code=error.code)
