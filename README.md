# Kafka-Avro Manual Schema Evolution Pipeline

This project is a hands-on implementation of a Kafka data pipeline focused on manual schema management and evolution. The goal was to move beyond automated tools and interact directly with the **Confluent Schema Registry API** to handle real-world schema changes.

## 🎯 Task Objectives
* **Manual API Mastery:** Built Producers and Consumers from scratch using the `confluent-kafka` Python API.
* **Schema Evolution:** Managed the lifecycle of a schema by manually adding and removing fields.
* **Concurrency:** Demonstrated real-time data flow with both Producer and Consumer running simultaneously.
* **Real-World Simulation:** Handled compatibility checks and database synchronization via JDBC.

## 🛠️ Evolution Workflow (The Scenario)
To mimic a real-world production environment, the schema was evolved through three distinct phases:

1.  **V1 (Baseline):** Initial schema containing `name` and `age`.
2.  **V2 (Field Addition):** Added a `phone` field with a default value to ensure **Backward Compatibility**.
3.  **V3 (Field Removal):** Removed the `age` field to demonstrate **Forward Compatibility**, ensuring the consumer continues to process data without interruption.

## 📁 Project Structure
* **`consumer.py`**: A robust, schema-agnostic consumer that dynamically fetches the required schema version from the Registry to deserialize incoming messages.
* **`producer_evolved.py`**: Implements the V2 schema change (Adding fields).
* **`producer_v3.py`**: Implements the V3 schema change (Removing fields).
* **`producer_broken.py`**: A validation script used to test the Schema Registry's guardrails by attempting an incompatible type change (triggers a 409 Conflict).
* **`docker-compose.yml`**: Full infrastructure stack including Kafka, Zookeeper, Schema Registry, Kafka Connect, and MySQL.

## 🚀 Key Learnings
* **Manual Schema Handling:** Gained deep familiarity with `AvroSerializer` and `AvroDeserializer` and how they interact with the Schema Registry.
* **JDBC Sink Mapping:** Configured the Kafka Connect JDBC Sink to handle schema evolution, allowing the MySQL table to adapt its structure automatically as the Avro schema changed.
* **Error Handling:** Successfully identified and resolved compatibility errors and database constraint issues (e.g., MySQL TEXT default value limitations).

## 💻 How to Use
1. **Infrastructure:** Run `docker-compose up -d`.
2. **Environment:** Install requirements: `pip install confluent-kafka fastavro authlib httpx cachetools`.
3. **Execution:** - Start `consumer.py` in one terminal.
   - Run the producers (`evolved`, `v3`) in another to see the live evolution.
