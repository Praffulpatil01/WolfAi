#import requests

#def get_placeholder_image(prompt):
# Replace with a known good fallback image URL
#img_url = "https://placekitten.com/800/400"  # 🐱 Works reliably on Replit
#img_data = requests.get(img_url).content
#with open("image.jpg", "wb") as f:
#f.write(img_data)
#return "image.jpg"

import os
import requests


def get_placeholder_image(prompt):
    print("🖼️ Generating image using DeepAI...")

    api_key = os.getenv("DEEPAI_API_KEY")  # Add this in Replit secrets
    if not api_key:
        raise ValueError("DEEPAI_API_KEY not set!")

    response = requests.post("https://api.deepai.org/api/text2img",
                             data={"text": prompt},
                             headers={"api-key": api_key})

    if response.status_code != 200:
        print("❌ DeepAI Error:", response.status_code, response.text)
        return None

    result = response.json()
    image_url = result.get("output_url")

    if not image_url:
        print("⚠️ No image returned.")
        return None

    # Download image
    image_data = requests.get(image_url).content
    image_path = "image.jpg"
    with open(image_path, "wb") as f:
        f.write(image_data)

    return image_path
