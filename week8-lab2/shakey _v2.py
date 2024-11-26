from sense_hat import SenseHat
import time

# Define colors
GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red
OFF = (0, 0, 0)      # RGB for off

# Initial state
active = True

# Initialize Sense HAT
sense = SenseHat()
sense.clear(GREEN)  # Start with green color

# Define threshold for shake detection
SHAKE_THRESHOLD = 1.5  # Adjust as needed for sensitivity

def is_shaken():
    # Get raw accelerometer data
    accel = sense.get_accelerometer_raw()
    x = abs(accel['x'])
    y = abs(accel['y'])
    z = abs(accel['z'])
    
    # Check if the acceleration exceeds the shake threshold on any axis
    return x > SHAKE_THRESHOLD or y > SHAKE_THRESHOLD or z > SHAKE_THRESHOLD


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action == "pressed":
            if active:
                sense.clear(OFF)
            else:
                sense.clear(GREEN)
            active = not active

    if is_shaken():
        if active:
            print("Shakey shakey")
            sense.clear(RED)  # Set LEDs to red
            time.sleep(1)  # Keep red for a second
            sense.clear(GREEN)  # Reset back to green

    # Short delay to prevent high CPU usage
    time.sleep(0.1)
