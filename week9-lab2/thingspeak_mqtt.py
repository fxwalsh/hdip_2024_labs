#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
from sense_hat import SenseHat
import logging
from dotenv import dotenv_values

# Load configuration
config = dotenv_values(".env")

# Initialize SenseHAT
sense = SenseHat()
sense.clear()

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Define event callbacks for MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected successfully to MQTT broker.")
    else:
        logging.error("Failed to connect, return code %d\n", rc)

def on_publish(client, userdata, mid):
    logging.info(f"Message Published with ID: {mid}")

# Initialize MQTT client with client ID
mqttc = mqtt.Client(client_id=config.get("clientId"))

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
print(config.get("password"))

url = urlparse("mqtt://mqtt3.thingspeak.com:1883")
base_topic = url.path[1:]

# Configure MQTT client with username and password
mqttc.username_pw_set(config.get("username"), config.get("password"))

# Connect to MQTT Broker with error handling
try:
    mqttc.connect(url.hostname, url.port or 1883)
    mqttc.loop_start()
except Exception as e:
    logging.error(f"Could not connect to MQTT broker: {e}")
    sys.exit(1)

# Set Thingspeak Channel topic to publish to
topic = f"channels/{config.get('channelId')}/publish"

# Publish temperature data to MQTT broker
def publish_temperature():
    temp = round(sense.get_temperature(), 2)
    payload = f"field1={temp}"
    mqttc.publish(topic, payload)
    logging.info(f"Published temperature: {temp}")

# Main loop to publish temperature every specified interval
def main():
    interval = int(config.get("transmissionInterval", 15))
    try:
        while True:
            publish_temperature()
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Interrupted by user")
    finally:
        mqttc.loop_stop()
        mqttc.disconnect()
        logging.info("MQTT client disconnected.")

if __name__ == "__main__":
    main()
