import logging
from kafka import KafkaConsumer
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('consumer')

# Kafka consumer setup
consumer = KafkaConsumer('my-topic', bootstrap_servers=['kafka-service:9092'])

def consume_message():
    for message in consumer:
        logger.info(f"Consumed message: {message.value.decode('utf-8')}")
        # Simulate message processing
        time.sleep(2)

if __name__ == "__main__":
    logger.info("Consumer started")
    consume_message()
