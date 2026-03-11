from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

sr_client = SchemaRegistryClient({'url': 'http://127.0.0.1:8081'})

# BREAKING CHANGE: Changing 'age' from int to string
schema_broken = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "string"}
  ]
}
"""

try:
    serializer = AvroSerializer(sr_client, schema_broken)
    producer = SerializingProducer({'bootstrap.servers': 'localhost:9092', 'value.serializer': serializer})
    producer.produce(topic='evolution_topic', value={"name": "Broken", "age": "Twenty-Five"})
    producer.flush()
except Exception as e:
    print(f"\n[SUCCESS] Schema Registry rejected the breaking change:")
    print(f"Error: {e}")