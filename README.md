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
 ** POST CALL ** to post ANY JSON messages to KAFKA Producer
 curl -X POST http://localhost:5000/posttoKafka -d ' {
        "xx44Checkkey1": "val1",
        "xx2llCheckkey2": "val2",
        "xx3llCheckkey3": "val3"
 }'

** GET CALL ** To Read latest single event from Kafka 


curl -X GET http://127.0.0.1:5000/getLatestKafka 
