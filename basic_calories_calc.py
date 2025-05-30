import os
import json
import base64
from openai import OpenAI

# Load API key and assistant ID from config file
CONFIG_PATH = "config.json"

if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, 'r') as config_file:
        config = json.load(config_file)
        api_key = config.get("openai_api_key")
        assistant_id = config.get("assistant_id_diag")

        if not api_key or not assistant_id:
            raise ValueError("Missing required config values.")
        os.environ["OPENAI_API_KEY"] = api_key
        print("Config loaded successfully.")
else:
    raise FileNotFoundError(f"The config file {CONFIG_PATH} does not exist.")

client = OpenAI(api_key=api_key)

# Helper function to get output from assistant
def outputs(thread_id, assistant_id, user_query):
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=user_query
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id, assistant_id=assistant_id
    )
    messages_output = list(client.beta.threads.messages.list(
        thread_id=thread_id, run_id=run.id
    ))
    return messages_output[0].content[0].text.value

# Initialize thread and assistants
thread = client.beta.threads.create()
thread_id = thread.id
print(f"Thread ID: {thread_id}")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Path to your image
image_path = "/Users/stuti/Downloads/clipboard-image.png"

# Upload the image file to OpenAI
with open(image_path, "rb") as image_file:
    file_response = client.files.create(
        file=image_file,
        purpose="vision"
    )

user_query = [
    {
        "type": "text", 
        "text": "Give nutrition content?"
    },
    {
        "type": "image_file",
        "image_file": {
            "file_id": file_response.id
        }
    }
]

diagnosis = outputs(thread_id, assistant_id, user_query)
print(diagnosis)
