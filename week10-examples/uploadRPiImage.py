import requests
import os

GLITCH_API_URL = "https://hdip-up-demo.glitch.me/upload"

def upload_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            response = requests.post(GLITCH_API_URL, files={'file': img_file})
            print(response.status_code, response.text)
    else:
        print(f"Image not found: {image_path}")

# Call the function with the image path
upload_image("./images/sensehat_image.jpg")