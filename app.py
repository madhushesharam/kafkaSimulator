import logging, time,json,datetime
from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT, jwt_required, current_identity

from pythonKafkaexampApp import Producer,Consumer
from auth import authenticate, identity,secrettoken


app = Flask(__name__)
app.secret_key = secrettoken()
# Authentication , JWT will pass the params  username & Password to the function authenticate(username,password)
# This will create /auth
jwt = JWT(app, authenticate, identity)


api = Api(app)

class homepage(Resource):
    def get(self):
        return  'This is Message Simulator for KAFKA ..Welcome to home page ...'
 
class communicate_kafka(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        a=Producer(data)
        a.run()
        time.sleep(3)
        return data, 201
    
    @jwt_required()
    def get(self):
        b=Consumer()
        myvalue = b.run()
        print "Here in Get call reading myvalue : \t" + myvalue + "\n"
        print type (myvalue)
        print myvalue
        myvalue = json.loads(myvalue)
        return myvalue , 200
    
   

api.add_resource(homepage,'/')
api.add_resource(communicate_kafka,'/messages')


app.run(port =5000, debug=True)    
