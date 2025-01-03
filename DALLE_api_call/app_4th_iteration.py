"""
chatgpt prompt:
can you make 2 more modifications to the code from the third iteration?

First, add style and quality parameters to the payload configuration.
Second, pickle the images data alongside the config file.
"""

import requests
import json
import os
import pickle
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
openai_api_key = os.getenv('OPENAI_API_KEY')

# Load configuration from JSON file
config_filename = "DALLE_api_call/config.json"
with open(config_filename, "r") as config_file:
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

    # List to store image data for pickling
    images_data = []

    # Download and save each image
    for idx, image_url in enumerate(image_urls, start=1):
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_path = os.path.join(save_directory, f"{base_filename}{idx}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(image_response.content)
            print(f"Image {idx} saved as {image_path}")

            # Save image data for pickling (image content)
            images_data.append({
                "image_path": image_path,
                "image_content": image_response.content  # Store the image content
            })
        else:
            print(f"Failed to download image {idx}. URL: {image_url}")

    # Pickle the images data alongside the config file
    pickle_filename = "image_data_with_config.pkl"
    with open(pickle_filename, "wb") as pickle_file:
        # Include both the images data and the config content
        pickle.dump({
            "config": config,  # Include the config data
            "images": images_data  # Include the images data
        }, pickle_file)
    print(f"Images and config have been pickled into {pickle_filename}")
else:
    print("Error:", response.status_code, response.text)
