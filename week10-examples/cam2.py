from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Start recording
camera.start_recording('./images/video.mjpeg', format='mjpeg')
print("Recording started...")

sleep(10)  # Record for 10 seconds

# Stop recording
camera.stop_recording()
print("Recording stopped!")