from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

sr_client = SchemaRegistryClient({'url': 'http://127.0.0.1:8081'})

# SCHEMA V3: Removed 'age' field
schema_v3 = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "phone", "type": "string", "default": "000-0000"}
  ]
}
"""

serializer = AvroSerializer(sr_client, schema_v3)
producer = SerializingProducer({'bootstrap.servers': 'localhost:9092', 'value.serializer': serializer})

# Data without 'age'
producer.produce(topic='evolution_topic', value={"name": "Alice", "phone": "111-2222"})
producer.flush()
print("Sent V3 (Age removed)!")