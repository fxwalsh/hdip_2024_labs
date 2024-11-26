from picamera2 import Picamera2

def capture_image(output_file):
    # Create and configure Picamera2 instance
    picam2 = Picamera2()

    # Set up the camera with preview configuration (faster setup)
    picam2.configure(picam2.create_preview_configuration())

    # Start the camera
    picam2.start()

    # Capture an image
    picam2.capture_file(output_file)

    # Stop the camera
    picam2.stop()

# Capture an image and save it to output.jpg
capture_image("output.jpg")