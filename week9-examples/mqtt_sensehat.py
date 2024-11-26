import time
import random
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# Initialize the Sense HAT
sense = SenseHat()

# MQTT connection details
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "/yourID/test"

# Define colors
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 255, 255)  # White
]

# The callback function for when a message is received
def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()}")
    
     # Flash the LED matrix with random colors for 2 seconds
    end_time = time.time() + 2
    while time.time() < end_time:
        color = random.choice(colors)
        sense.clear(color)
        time.sleep(0.1)
        sense.clear()
        time.sleep(0.1)
    sense.clear()  # Clear the LED matrix after flashing

# The callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start a background thread for the MQTT client loop
client.loop_start()

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    sense.clear()
    client.loop_stop()
    client.disconnect()