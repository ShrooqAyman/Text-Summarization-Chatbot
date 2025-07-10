import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
HF_TOKEN = os.environ['HF_TOKEN']

# API URLs for models
AR_MODEL_API_URL = "https://api-inference.huggingface.co/models/csebuetnlp/mT5_multilingual_XLSum"
EN_MODEL_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
LANGUAGE_NOT_SUPPORTED_MESSAGE = "Sorry, this language is not supported. Please enter text in English or Arabic."

# Headers
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}
