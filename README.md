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


 Auth
 Retreive Token 
 curl -X POST http://127.0.0.1:5000/auth -d ' {"username" : "user1","password" : "abcxyz"}'


 curl -X POST  http://127.0.0.1:5000/messages -H 'authorization: JWT $TOKEN  -d '{"key1": "val1","Key2": "val2"}'

** GET CALL ** To Read latest single event from Kafka 

curl -X GET http://localhost:5000/messages -H 'authorization: JWT $TOKEN 
  

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

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Versioning

## Authors

* **Madhu Shesharam** - *Initial work* 


ils

## Reference

  https://kafka-python.readthedocs.io 
  https://flask-restful.readthedocs.io
  https://pythonhosted.org/Flask-JWT/
  https://github.com/simplesteph/kafka-stack-docker-compose



