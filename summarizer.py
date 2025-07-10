import os
import requests
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
HF_TOKEN = os.environ['HF_TOKEN']

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
    }

def summarize_text(message, history):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if isinstance(result, dict) and "error" in result:
        return "Error: " + result["error"]
    summary = result[0]["summary_text"]
    return summary
