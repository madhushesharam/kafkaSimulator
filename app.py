import logging, time,json,datetime
from flask import Flask,request
from flask_restful import Resource,Api
from pythonKafkaexampApp import Producer,Consumer




app = Flask(__name__)
api = Api(app)

class communicate_kafka(Resource):
    def post(self):
        data = request.json
        a=Producer(data)
        a.run()
        time.sleep(3)
        #logger.info("POSTING DATA is ")
        return data, 201
    
    def get(self):
        b=Consumer()
        myvalue = b.run()
        print "Here in Get call reading myvalue : \t" + myvalue + "\n"
        print type (myvalue)
        print myvalue
        myvalue = json.loads(myvalue)
        return myvalue , 200

api.add_resource(communicate_kafka,'/messages')

app.run()    
