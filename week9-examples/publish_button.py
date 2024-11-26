import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat
from datetime import datetime

# Initialize the Sense HAT
sense = SenseHat()

# MQTT connection details
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/YourID/test"


# Set up MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the client loop in a background thread
client.loop_start()

def publish_message():
    # Get the current time
    current_time = datetime.now()
   #Function to publish the message to the MQTT topic
    message = f"Frank pressed the button at {current_time:%H:%M}"
    client.publish(MQTT_TOPIC, message)
    print("Message published:", message)

# Main loop to detect joystick button press
try:
    while True:
        # Check if the middle button is pressed
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction == "middle":
                publish_message()
        time.sleep(0.1)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
