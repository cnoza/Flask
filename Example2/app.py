from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Customer(Resource):
    def get(self,name):
        return {'customer-name':name}

api.add_resource(Customer, '/customer/<string:name>')

app.run()