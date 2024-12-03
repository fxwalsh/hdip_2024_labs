from picamera2 import Picamera2

def capture_image(path):
    picam2 = Picamera2()
    picam2.start()
    picam2.capture_file(path)
    picam2.stop()
    picam2.close()  # Ensures the camera is released

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    capture_image("./images/image.jpg")