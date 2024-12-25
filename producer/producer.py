import logging
import time
import os
import random
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('producer')

# Kafka producer setup
kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')
logger.info(f"Connecting to Kafka broker at {kafka_broker}")
producer = KafkaProducer(bootstrap_servers=['kafka_broker'])

def produce_message():
    while True:
        message = f"Message {random.randint(1, 100)}"
        logger.info(f"Producing message: {message}")
        producer.send('my-topic', value=message.encode('utf-8'))
        producer.flush()  # Ensure the message is sent
        logger.info(f"Message produced: {message}")
        time.sleep(5)  # Produce a message every 5 seconds

if __name__ == "__main__":
    logger.info("Producer started")
    produce_message()
