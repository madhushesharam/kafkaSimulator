# Reference : https://pypi.org/project/kafka-python/

import logging, time,json
#from bson import json_util2
from kafka import KafkaConsumer, KafkaProducer


class Producer():
    def __init__(self,message):
        self.message =message
        
    
    def run(self):
        
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        message = json.dumps(self.message) 
        producer.send(b'my-topic', message)
        time.sleep(1)
        producer.close()

class Consumer():
    def __init__(self):
        pass
        
    def run(self):
        
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        consumer.subscribe(['my-topic'])
        
        for message in consumer:
            print "Message are READ AS SHOWN \n"
            print(message.value)
            val = message.value
        consumer.close()
        return val  # returns last read message...

        
