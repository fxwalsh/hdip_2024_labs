import BlynkLib
from time import sleep
from sense_hat import SenseHat


#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 'YOUR_AUTH_TOKEN'
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def button_pressed(event):
    print("Button Pressed")
    if event.action == "pressed":
        print("Button Pressed")
        blynk.log_event("button_event", "Someone prsseed the buitton")
        blynk.virtual_write(0, 1)
        sleep(2)
        blynk.virtual_write(0, 0)
    
# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for button presses...")
    sense.stick.direction_middle = button_pressed
    while True:
        blynk.run()  # Process Blynk events
           

