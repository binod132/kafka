import logging
from kafka import KafkaConsumer
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('consumer')

# Kafka consumer setup
kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')
consumer = KafkaConsumer('my-topic', bootstrap_servers=['kafka_broker'])

def consume_message():
    for message in consumer:
        logger.info(f"Consumed message: {message.value.decode('utf-8')}")
        # Simulate message processing
        time.sleep(2)

if __name__ == "__main__":
    logger.info("Consumer started")
    consume_message()
