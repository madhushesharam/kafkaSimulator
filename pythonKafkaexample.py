#!/usr/bin/env python
# Reference : https://pypi.org/project/kafka-python/

import  logging, time
from kafka import KafkaConsumer, KafkaProducer


class Producer():
    def __init__(self):
        pass
        
    
    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('my-topic', b"test")
        producer.send('my-topic', b"\xc2Hello, World!")
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
            print(message)
        consumer.close()
        
        
if __name__ == "__main__":
    a= Producer()
    b=Consumer()
    a.run()
    time.sleep(10)
    b.run()
    

    

    
    
    
    