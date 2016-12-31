from collections import namedtuple

from flask import json


class JSONHelper():
    @staticmethod
    def parseFromJSONToObject(data, className):
        object = json.loads(data, object_hook=lambda d: namedtuple(className, d.keys())(*d.values()))
        return object
