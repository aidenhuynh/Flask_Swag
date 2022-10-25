from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
app_api2 = Blueprint('api', __name__,
                   url_prefix='/api/tester')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api2)

class TestAPI:
    class _GetThing(Resource):
        def get(self):
            return jsonify([1, 2, 3])


    api.add_resource(_GetThing, '/')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000"
    server = 'https://swag.nighthawkcodingteams.cf'
    url = server + "/api/tester"