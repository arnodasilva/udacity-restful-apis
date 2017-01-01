from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

schema = {
    "type": "object",
    "properties": {
        "user_proposed_to": {"type": "integer"},
        "user_proposed_from": {"type": "integer"},
        "request_id": {"type": "integer"},
        "filled": {"type": "boolean"}
    },
    "required": [
        "user_proposed_to",
        "user_proposed_from",
        "request_id"
    ]
}


class ProposalInputsValidator(Inputs):
    json = [JsonSchema(schema=schema)]
