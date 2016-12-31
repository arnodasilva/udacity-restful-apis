from flask import json


class JSONHelper():
    @staticmethod
    def parseJSONToObject(className, data):
        return className(**json.loads(data))
