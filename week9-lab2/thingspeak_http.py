from sense_hat import SenseHat
import requests
import time

# Initialize Sense HAT
sense = SenseHat()

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "YOUR WRITE KEY"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


while True:
    # Read temperature and humidity from Sense HAT
    temperature = round(sense.get_temperature(),2)
    
    print(f"Temperature: {temperature} C")

    # Send the data to ThingSpeak
    send_to_thingspeak(temperature)

    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(15)
