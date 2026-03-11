from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

# Setup Registry
sr_client = SchemaRegistryClient({'url': 'http://127.0.0.1:8081'})
avro_deserializer = AvroDeserializer(sr_client)

# Setup Consumer
consumer = DeserializingConsumer({
    'bootstrap.servers': 'localhost:9092',
    'value.deserializer': avro_deserializer,
    'group.id': 'evolution_group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['evolution_topic'])

print("Consumer (v1) waiting for data... (Press Ctrl+C to stop)")
while True:
    try:
        msg = consumer.poll(1.0)
        if msg:
            print(f"Received Record: {msg.value()}")
    except Exception as e:
        print(f"Error: {e}")
        break
consumer.close()