# Reference : https://pypi.org/project/kafka-python/

import logging, time,json
from kafka import KafkaConsumer, KafkaProducer

logger = logging.getLogger(__name__)

class Producer():
    def __init__(self,message):
        self.message =message
        
    
    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        print producer.topics()
        message = json.dumps(self.message) 
        producer.send(b'my-topic', message).get(timeout=10)
        time.sleep(1)
        producer.close()
        
        

class Consumer():
    def __init__(self):
        pass
        
    def run(self):
            consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
            print consumer.topics()
            consumer.subscribe(['my-topic'])
        
            for message in consumer:
                logger.info( "Messages Consumed :\n")
                logger.info(message.value)
                val = message.value
            consumer.close()
            return message.value  # returns last read message...

        
'''
settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'earliest'}
}

c = Consumer(settings)
'''
