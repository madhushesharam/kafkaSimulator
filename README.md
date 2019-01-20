# Simulate Events 

Simple Secured Restful Service [Written in *FlaskRestful* ,*kafka-python*, *flask_jwt*]
Writes/Reads JSON messages to/from  Kafka Broker Hosted on local Docker Containers (kafka broker with ZooKeeper) 
This would be helpful , for Dev & Test projects.

## Prerequisites
   1) Docker /Docker Compose is available
   2) Python 2.7> 
   
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```
git clone git@github.com:madhushesharam/messageSimulator-kafka.git
cd messageSimulator-kafka 
pip install -r requirements.txt 
docker-compose -f docker-compose.yml up 
python app.py
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

### TODO:
   1) Parametrize the PORT,HOST etc 
   2) simplify installation requirements.txt / make File 
   1) Parametrize the PORT,HOST / create CONFIG utils 
   2) simplify installation requirements.txt / make File
   3) Refactor & Additional Error Handling 
   4) Add Tests & CICD

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
