from picamera import PiCamera
from sense_hat import SenseHat
from signal import pause
from uploadImages import uploadImage

# Initialize the Sense HAT and the Pi Camera
sense = SenseHat()
camera = PiCamera()

# Function to capture an image
def capture_image(event):
    if event.action == 'pressed':  # Check if the joystick is pressed
        print("Button pressed! Capturing image...")
        camera.capture('./images/sensehat_image.jpg')
        print("Image captured and saved as sensehat_image.jpg")
        uploadImage()


# Assign the function to the joystick's middle button
sense.stick.direction_middle = capture_image

# Keep the script running to listen for button presses
print("Press the joystick button to capture an image.")
pause()
