import BlynkLib
import time
from sense_hat import SenseHat
from shakey import is_shaken

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initialise Sense HAT
sense = SenseHat()
sense.clear(GREEN)  # Start with green color

# Blynk authentication token
BLYNK_AUTH = 'YOUR_AUTH_TOKEN'
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Define threshold for shake detection
SHAKE_THRESHOLD = 1.5  # Adjust as needed for sensitivity


if __name__ == "__main__":
    while True:
        blynk.run()
        if is_shaken():
            print("Shakey shakey")
            blynk.log_event("movement_event") # Has to match name of event in Blynk, including case!!!
            sense.clear(RED)  # Set LEDs to red
            blynk.virtual_write(0, 1)
            time.sleep(2)  # Keep red for a second
            sense.clear(GREEN)  # Reset back to green
            blynk.virtual_write(0, 0)

        # Short delay to prevent high CPU usage
        time.sleep(0.1)