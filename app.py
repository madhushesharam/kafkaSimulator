import logging, time,json,datetime
from flask import Flask,jsonify,request
from pythonKafkaexampApp import Producer,Consumer
from ast import literal_eval

app = Flask(__name__)

@app.route('/posttoKafka',methods=["POST"])
def posttokafka():
    data = request.json
    a=Producer(data)
    a.run()
    time.sleep(3)
    return jsonify(data)


@app.route('/getLatestKafka')
def readfromkafka():
    b=Consumer()
    myvalue = b.run()
    print "Here in Get call reading myvalue : \t" + myvalue + "\n"
    print type (myvalue)
    print myvalue
    '''
    s = json.dumps(myvalue, indent=4, sort_keys=True)
    print(s)    
    print type (s)
    d = json.loads(s) 
    print " CHECK HERE.....=>>>> "
    print type (d)
    d = {
        "timeStamp" : datetime.datetime.now(),
        "readlatestMessage ": d
    }
    '''
    
    myvalue = json.loads(myvalue)
    return jsonify(myvalue)


@app.route('/')
def read():
    return "Welcome to message simulator App"
    

    

app.run()    
