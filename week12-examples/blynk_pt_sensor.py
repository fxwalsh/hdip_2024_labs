import BlynkLib
from time import sleep
from sense_hat import SenseHat
from sensor_listener import SensorListener

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Initialise the Blynk instance
blynk = BlynkLib.Blynk("RYIj9R2_QtUkPmZHBFjU8jKeAIoKmplF")

def motion_detected(data):
    print("motion detected")
    blynk.log_event("movement_event", "Motion Detected")
    blynk.virtual_write(0, 1)
    sleep(2)
    blynk.virtual_write(0, 0)
    
# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for button presses...")
    listener = SensorListener(port=5000)
    listener.callback = motion_detected
    listener.start()
    while True:
        blynk.run()  # Process Blynk events
           