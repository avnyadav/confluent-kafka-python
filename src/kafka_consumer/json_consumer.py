

import argparse

from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from src.entity.car import Car
from src.kafka_config import sasl_conf





def main(topic):

    schema_str = """
    {
  "$id": "http://example.com/myURI.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "additionalProperties": false,
  "description": "Sample schema to help you get started.",
  "properties": {
    "brand": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "car_name": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "engine": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "fuel_type": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "km_driven": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "max_power": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "mileage": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "model": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "seats": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "seller_type": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "selling_price": {
      "description": "The type(v) type is used.",
      "type": "number"
    },
    "transmission_type": {
      "description": "The type(v) type is used.",
      "type": "string"
    },
    "vehicle_age": {
      "description": "The type(v) type is used.",
      "type": "number"
    }
  },
  "title": "SampleRecord",
  "type": "object"
}
    """
    json_deserializer = JSONDeserializer(schema_str,
                                         from_dict=Car.dict_to_car)

    consumer_conf = sasl_conf()
    consumer_conf.update({
                     'group.id': 'group1',
                     'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])




    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            car = json_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            if car is not None:
                print("User record {}: car: {}\n"
                      .format(msg.key(), car))
        except KeyboardInterrupt:
            break

    consumer.close()

