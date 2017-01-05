from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "meal_type": {"type": "string"},
        "location_string": {"type": "string"},
        "latitude": {"type": "string"},
        "longitude": {"type": "string"},
        "meal_time": {"type": "string"},
        "filled": {"type": "boolean"}
    },
    "required": [
        "user_id",
        "meal_type",
        "latitude",
        "longitude",
        "meal_time"
    ]
}


class RequestInputsValidator(Inputs):
    json = [JsonSchema(schema=schema)]
