from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Start the camera preview
camera.start_preview()
sleep(5)  # Allow time for adjustments

# Capture the image
camera.capture('./images/image.jpg')
print("Image captured!")

# Stop the preview
camera.stop_preview()
