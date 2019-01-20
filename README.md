Simple example with python Producer Consumer, with Docker Kafka and Zookeper

# Refer : https://pypi.org/project/kafka-python/


TODO:
   1) Parametrize the PORT,HOST etc 
   2) simplify installation requirements.txt / make File 
   
   
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
