from sense_hat import SenseHat
import time

sense = SenseHat()

# Define colours
GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initial state
is_green = True
sense.clear(GREEN)  # Start with green

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action == "pressed":
            if is_green:
                sense.clear(RED)
            else:
                sense.clear(GREEN)
            is_green = not is_green
    time.sleep(0.1)  # Slight delay to avoid high CPU usage

