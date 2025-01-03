"""
**Prompt to the chatgpt - third iteration**
Can you modify this code (from second iteration) to fix this two issues:

First, regardless of howm many images we ask for, you only parse out 1 image
from the response data.

Second, can you download the images form the URL and save them locally.
Add the desired file name to the JSON file, and save them as <filename>1.png,,
<filename>2.png, etc.
"""

import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
openai_api_key = os.getenv('OPENAI_API_KEY')

# Load configuration from JSON file
with open("DALLE_api_call/config.json", "r") as config_file:
    config = json.load(config_file)

# Update headers with the API key
headers = config["headers"]
headers["Authorization"] = f"Bearer {openai_api_key}"

# Extract endpoint URL, payload, and filename
url = config["endpoint_url"]
payload = config["payload"]
base_filename = config.get("filename", "generated_image")  # Default filename if not provided

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    response_data = response.json()
    print("Images created successfully!")

    # Extract and download all image URLs
    image_urls = [data["url"] for data in response_data["data"]]

    # Create a directory to save images if it doesn't exist
    save_directory = "downloaded_images"
    os.makedirs(save_directory, exist_ok=True)

    # Download and save each image
    for idx, image_url in enumerate(image_urls, start=1):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_path = os.path.join(save_directory, f"{base_filename}{idx}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            print(f"Image {idx} saved as {image_path}")
        else:
            print(f"Failed to download image {idx}. URL: {image_url}")
else:
    print("Error:", response.status_code, response.text)
