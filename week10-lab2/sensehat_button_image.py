from picamera2 import Picamera2
from sense_hat import SenseHat

picam2 = Picamera2()
sense = SenseHat()

def capture_image(event):
    if event.action == "pressed":
        picam2.start()
        picam2.capture_file("./images/sensehat_image.jpg")
        picam2.stop()
        print("Image captured using SenseHAT button!")

sense.stick.direction_middle = capture_image
print("Press the middle button on the SenseHAT to capture an image.")
while True:
    pass  # Keep the script running to detect button presses