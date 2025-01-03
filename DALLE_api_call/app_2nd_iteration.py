"""
**Prompt to chatgpt - second iteration**
I have this code (api_1st_iteration.py) that calls the REST endpint for DALL-E to generate an image.
The code has the parameter for the calls hardcoded in the code.
Can you externalize the parameters to a JSON file and
update the code to read the parameters from the JSON file?

Please also provide an exhaustive list of the parameters
that can be passed to the DALL-E endpoint.
https://platform.openai.com/docs/api-reference/images/create

"""

import requests
import json
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv()) # read local .env file

openai_api_key  = os.getenv('OPENAI_API_KEY')

# Load configuration from JSON file
with open("DALLE_api_call/config.json", "r") as config_file:
    config = json.load(config_file)

# Update headers with API key
headers = config["headers"]
headers["Authorization"] = f"Bearer {openai_api_key}"

# Extract endpoint URL and payload
url = config["endpoint_url"]
payload = config["payload"]

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    response_data = response.json()
    print("Image created successfully!")
    print("Image URL:", response_data["data"][0]["url"])
else:
    print("Error:", response.status_code, response.text)
