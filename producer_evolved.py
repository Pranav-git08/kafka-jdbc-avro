from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

sr_client = SchemaRegistryClient({'url': 'http://127.0.0.1:8081'})

# EVOLVED SCHEMA (v2): Added 'phone' with a default
schema_v2 = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "int"},
    {"name": "phone", "type": "string", "default": "000-0000"}
  ]
}
"""

serializer = AvroSerializer(sr_client, schema_v2)
producer = SerializingProducer({
    'bootstrap.servers': 'localhost:9092',
    'value.serializer': serializer
})

data = {"name": "Pranav", "age": 25, "phone": "555-1234"}
producer.produce(topic='evolution_topic', value=data)
producer.flush()
print("Sent evolved message (V2) with phone number!")
