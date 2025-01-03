"""
Prompt to chatgpt:
Can you create code that accesses the OpenAI endpoint at:
https://platform.openai.com/docs/api-reference/images/create
directly to create an image?
"""

import requests
import json
import os
import openai
from dotenv import load_dotenv, find_dotenv

# Define your OpenAI API key
_ = load_dotenv(find_dotenv()) # read local .env file

openai_api_key  = os.getenv('OPENAI_API_KEY')

# Define the endpoint
url = "https://api.openai.com/v1/images/generations"

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Define the payload
payload = {
    "model": "dall-e-3",
    "prompt": "A cute baby sea otter",
    "n": 1,
    "size": "1024x1024"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    response_data = response.json()
    print("Image created successfully!")
    print("Image URL:", response_data["data"][0]["url"])
else:
    print("Error:", response.status_code, response.text)