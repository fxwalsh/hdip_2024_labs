import blynklib
from time import sleep
from sense_hat import SenseHat
from capture_image import capture_image
from upload_image import upload_image

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 'YOUR_AUTH_TOKEN'
IMAGE_PATH="./images/sensehat_image.jpg"
# Initialise the Blynk instance
blynk = blynklib.Blynk(BLYNK_AUTH)


sense.clear()

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            print("Blynk application started.")
            blynk.run()  # Process Blynk events
            blynk.virtual_write(0, round(sense.temperature,2))
            sleep(2)  # Add a short delay to avoid high CPU usage
    except KeyboardInterrupt:
        print("Blynk application stopped.")