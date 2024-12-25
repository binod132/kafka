from kafka import KafkaConsumer
import json
import os

# Environment variables for Kafka broker and topic
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
TOPIC_NAME = os.getenv('TOPIC_NAME', 'test-topic')

def consume_messages():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )
    print(f"Consumer connected to Kafka broker: {KAFKA_BROKER}")
    print(f"Listening for messages on topic: {TOPIC_NAME}")

    for message in consumer:
        print(f"Received: {message.value}")

if __name__ == "__main__":
    consume_messages()
