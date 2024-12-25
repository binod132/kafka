from kafka import KafkaProducer
import json
import time
import os

# Environment variables for Kafka broker and topic
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
TOPIC_NAME = os.getenv('TOPIC_NAME', 'test-topic')

def produce_messages():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print(f"Producer connected to Kafka broker: {KAFKA_BROKER}")
    print(f"Sending messages to topic: {TOPIC_NAME}")

    counter = 1
    while True:
        message = {'id': counter, 'message': f'Hello Kafka {counter}'}
        producer.send(TOPIC_NAME, value=message)
        print(f"Sent: {message}")
        counter += 1
        time.sleep(5)  # Wait 5 seconds between messages

if __name__ == "__main__":
    produce_messages()
