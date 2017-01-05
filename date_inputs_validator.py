from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

schema = {
    "type": "object",
    "properties": {
        "user_1": {"type": "integer"},
        "user_2": {"type": "integer"},
        "restaurant_name": {"type": "string"},
        "restaurant_adress": {"type": "string"},
        "restaurant_picture": {"type": "string"},
        "meal_time": {"type": "string"}
    },
    "required": [
        "user_1",
        "user_2",
        "restaurant_adress",
        "restaurant_picture",
        "meal_time"
    ]
}


class DateInputsValidator(Inputs):
    json = [JsonSchema(schema=schema)]
