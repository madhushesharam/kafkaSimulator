Simple Secured Restful Service [Written in FlaskRestful,kafka-python,flask_jwt]
Writes/Reads JSON messages to/from  Kafka Broker Hosted on local Docker Containers (kafka broker with ZooKeeper) 

# Refer : https://pypi.org/project/kafka-python/


TODO:
   1) Parametrize the PORT,HOST / create CONFIG utils 
   2) simplify installation requirements.txt / make File
   3) Refactor & Additional Error Handling 
   4) Add Tests
   
   
 Prerequisites  
   1) Docker /Docker Compose is available
   2) Python 2.7> with kafka-python dependency installed.
   
 

 Execution
 1) docker-compose -f docker-compose.yml up 
 2) python app.py
 
 Example Usage:
 
 Auth
 Retreive Token 
 curl -X POST http://127.0.0.1:5000/auth -d ' {"username" : "user1","password" : "abcxyz"}'


 curl -X POST  http://127.0.0.1:5000/messages -H 'authorization: JWT $TOKEN  -d '{"key1": "val1","Key2": "val2"}'

** GET CALL ** To Read latest single event from Kafka 

curl -X GET http://localhost:5000/messages -H 'authorization: JWT $TOKEN 
  

References :
## https://kafka-python.readthedocs.io 
## https://flask-restful.readthedocs.io
## https://pythonhosted.org/Flask-JWT/
## https://github.com/simplesteph/kafka-stack-docker-compose
