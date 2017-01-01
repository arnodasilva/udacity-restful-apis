from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

schema = {
    "type": "object",
    "properties": {
        "password_hash": {"type": "string"},
        "email": {"type": "string"},
        "picture": {"type": "string"}
    },
    "required": [
        "email"
    ]
}


class UserInputsValidator(Inputs):
    json = [JsonSchema(schema=schema)]
