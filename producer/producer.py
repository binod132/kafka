import logging
import time
import random
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('producer')

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'])

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
