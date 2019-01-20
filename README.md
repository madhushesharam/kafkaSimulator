# Simulate Events 

Simple Secured Restful Service [Written in FlaskRestful,kafka-python,flask_jwt]
Writes/Reads JSON messages to/from  Kafka Broker Hosted on local Docker Containers (kafka broker with ZooKeeper) 
This would be helpful , for Dev & Test projects.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

git clone git@github.com:madhushesharam/messageSimulator-kafka.git
cd messageSimulator-kafka      

 Execution
 1) docker-compose -f docker-compose.yml up 
 2) python app.py
 

### Prerequisites

  
   1) Docker /Docker Compose is available
   2) Python 2.7> with kafka-python dependency installed.
 
```
Give examples
```

### Usage

Auth Retreive Token
```
 curl -X POST http://127.0.0.1:5000/auth -d ' {"username" : "user1","password" : "abcxyz"}'
```
 
Post Messages 
```
 curl -X POST  http://127.0.0.1:5000/messages -H 'authorization: JWT $TOKEN  -d '{"key1": "val1","Key2": "val2"}'
```

Read latest single event from Kafka 
```
curl -X GET http://localhost:5000/messages -H 'authorization: JWT $TOKEN 
```



  

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system




## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [kafka-python](https://kafka-python.readthedocs.io ) - Python lib  
* [Flask-Restful](https://flask-restful.readthedocs.io/) - The web framework used
* [Docker](https://github.com/simplesteph/kafka-stack-docker-compose) 


## Versioning

## Authors

* **Madhu Shesharam** - *Initial work* 


## Reference

  https://kafka-python.readthedocs.io 
  https://flask-restful.readthedocs.io
  https://pythonhosted.org/Flask-JWT/
  https://github.com/simplesteph/kafka-stack-docker-compose



