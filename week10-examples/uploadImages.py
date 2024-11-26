import requests
import os

GLITCH_API_URL = "https://hdip-up-demo.glitch.me/upload"
IMAGE_FOLDER = "./images"

def uploadImage():
    for image in os.listdir(IMAGE_FOLDER):
        print(image)
        if image.endswith(".jpg"):
            with open(os.path.join(IMAGE_FOLDER, image), 'rb') as img_file:
                response = requests.post(GLITCH_API_URL, files={'file': img_file})
                print(response.status_code, response.text)